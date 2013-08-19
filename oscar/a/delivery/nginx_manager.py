#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: hagaia
# 

import os
import time 
import errno
import subprocess
import getpass

import utils
import nginx_conf

from nginx_status import CurrentOperationTypes
from a.infra.misc.enum_with_value import EnumWithValue

if  __package__ is None:
    G_NAME_MODULE_DELIVERY = "unknown"
    G_NAME_GROUP_DELIVERY_NGINX_MNG = "unknown"
else:
    from . import G_NAME_MODULE_DELIVERY 
    from . import G_NAME_GROUP_DELIVERY_NGINX_MNG

#-----------------------------------------------------------------
class NginxWorkersGroup(object):

    def __init__ (self, masterPid, pidSet):
        self.timestamp = time.time() # creation timestamp
        self.masterPid = masterPid   # master pid
        self.pidSet    = pidSet      # list of workers' PIDs 
      
#-----------------------------------------------------------------
class StateCmd(EnumWithValue):

    """contains a single data member"""

    def __init__ (self, value, name):

        EnumWithValue.__init__(self, value, name) 

#-----------------------------------------------------------------
class StateCmdTypes(object):

    """ optional data members """

    kRunNginxNow  = StateCmd(0, "kRunNginxNow")

    kDelayRestart = StateCmd(1, "kDelayRestart")

    kExitDelivery = StateCmd(2, "kExitDelivery")

    kNginxIsUp    = StateCmd(3, "kNginxIsUp")
        
#-----------------------------------------------------------------
class NginxManager(object):

    def __init__ (self, name, logger):

        self.__name = name
        self.__log = logger.createLogger(G_NAME_MODULE_DELIVERY, G_NAME_GROUP_DELIVERY_NGINX_MNG)        
        self.__ngxConf   = nginx_conf.NginxConf("nginx-conf",logger)
        self.__timeService = utils.TimesSerivce()
        self.__errRunCounter = 0

        # workers monitoring data
        self.__oldWorkersGenerationList = [] # holds a list per workers' generation
        
    #-----------------------------------------------------------------
    def init (self,conf,ngxCmd,ngxStatus):

        self.__log("nginx-manager").info("Init Nginx Manager")

        self.__conf      = conf
        self.__ngxCmd    = ngxCmd
        self.__ngxStatus = ngxStatus
        self.__ngxStatus.reset()

         # cretae nginx Log directories
        if not self.__ngxConf.createDirs(self.__conf):
            return False

        return True

    #-----------------------------------------------------------------
    def start (self):

        self.__ngxStatus.reset()

        # Kill all Valid Nginx Processes        
        self.__killAllNginxProcesses()
       
        return True    
       
    #-----------------------------------------------------------------
    def oneTick (self):
        
        # In case Nginx is during operation (Stop,Configuration)
        # need to wait a stable time before can continue        
        if self.__waitAfterOperation():
            return True

        # If Web Server is in Admin Down, 
        # Nothing to Do
        if not self.__conf.isWebServerAdminUp:
            return True


        # Nginx Oper Status is Up and Restart Nginx Event 
        if self.__ngxStatus.operStatus:
            if self.__ngxStatus.shouldRestartNginx is True:
                self.__handleRestart()
                return True
        else:
            self.__ngxStatus.shouldRestartNginx = False
        
        # Nginx Oper Status is Up and Reconfigure Event
        # There is new configuration waiting
        if self.__ngxStatus.operStatus:
            if self.__ngxStatus.shouldReloadConfig is True:
                if self.__handleReconfigure():
                    return True  
        else:
            self.__ngxStatus.shouldReloadConfig = False
                      
        # Kill old workers in case:
        # 1. Too many generations
        # 2. Old workers time limit
        self.__handleOldWorkers()
                       
        # According to Nginx current Status this function 
        # returns action command
        # kRunNginxNow, kDelayRestart kExitDelivery kNginxIsUp
        cmd = self.__handleNginxStatus()         
            
        if cmd == StateCmdTypes.kExitDelivery:
            self.__log("fail-to-run-nginx").warning("Fail to run Nginx - Exit")
            return False

        # If Nginx is already Up or it is during delay restart procedure do nothing! (Do not start Nginx)
        if (cmd == StateCmdTypes.kDelayRestart) or (cmd == StateCmdTypes.kNginxIsUp):
            return True

        # Nginx is Down Run it              
        self.__runNginx()
        
        return  True

    #-----------------------------------------------------------------
    def stop (self):
        
        self.__errRunCounter = 0

        if self.__ngxStatus.operStatus:

            self.__log("in-config-reload").notice("Nginx is starting STOP process") 

            self.__ngxStatus.reset()

            self.__log("nginx-is-down").notice("Nginx Change state to Down")
            
            self.__ngxStatus.startOperation(CurrentOperationTypes.kStopOperation)
                                
            self.__ngxCmd.stop()

        else:
            self.__ngxStatus.reset()
                
    #-----------------------------------------------------------------
    def end (self):

        self.__log("nginx-end").info("End Nginx")

        self.__errRunCounter = 0

        if self.__ngxStatus.operStatus:
                
            self.__ngxCmd.stop()

            # Wait for all Nginx process to exit
            time.sleep(2)
        
            # kill all nginx processes in case of valid after stop        
            self.__killAllNginxProcesses()

            self.__ngxStatus.reset()
                                    
            self.__log("nginx-is-down").notice("Nginx Change state to Down")

    #-----------------------------------------------------------------
    def isAlive (self):
        return self.__ngxStatus.operStatus

    #private    
    #-----------------------------------------------------------------
    def __waitAfterOperation (self):

        # Not during any operation no need to wait
        if self.__ngxStatus.isOperInProgress() is False:
            return False

        # Wait kOperStabilizationTimeMsec for operation to become stable
        if (self.__ngxStatus.operStartTime.tickFromInitMsec() < self.__ngxStatus.kOperStabilizationTimeMsec):
            return True

        self.__log("nginx-oper-stable").notice("Nginx Finish stabilization time for Oper = %s",self.__ngxStatus.operInProcess)

        curOper = self.__ngxStatus.operInProcess
            
        self.__ngxStatus.endOperation()

        #========================================================
        if curOper == CurrentOperationTypes.kStopOperation:
                    
            # kill all nginx processes in case of valid after stop        
            self.__killAllNginxProcesses()

        #========================================================
        if curOper == CurrentOperationTypes.kConfigOperation:

            # Is configuration Reload
            if self.__ngxStatus.shouldReloadConfig is True:

                self.__ngxStatus.shouldReloadConfig = False

                self.__log("nginx-is-reloaded").notice("Nginx is Reloaded - %s", self.__conf.getActiveConfigString())
                
                # add old workers new generation
                self.__addOldWorkersPids()

            else:
                            
                if self.__checkIsAlive():
                    self.__errRunCounter = 0                                       
                    self.__ngxStatus.operStatus = True  
                    self.__ngxStatus.nginxStartCounter = self.__ngxStatus.nginxStartCounter + 1
                    self.__log("nginx-is-up").notice("Nginx is Up - %s", self.__conf.getActiveConfigString())
                else:
                    self.__runNginxFailed()
 
        return False

    #-----------------------------------------------------------------
    def __isOkToStart (self):
        """
        Not during retries         - ok to start (kRunNginxNow)
        During reries and wait     - not ok to start (kDelayRestart)
        max retries reached        - exit delivery (kExitDelivery)
        """

        # Nginx is down and not in errored delayed reastart
        # Run Nginx Again
        if self.__errRunCounter == 0:
            return StateCmdTypes.kRunNginxNow            

        # Nginx is Down
        # During Error scenario
        # If max retries reached exit Delivery Manager
        if self.__errRunCounter >= self.__conf.kConf.kMaxRunNginxRetries:
            self.__log("max-retries").notice("Failed to run Nginx for %d times Exit Delivery",self.__conf.kConf.kMaxRunNginxRetries)
            return StateCmdTypes.kExitDelivery 
            

        # Check Delay time passed before trying again
        passedTime = self.__timeService.tickFromInitMsec()                       
        if  passedTime < self.__conf.kConf.kDaleyInNginxRunMSec:
            self.__log("wait-to-start").debug4("Error Count - %d, Passed Time After Failure - %d, Need to Wait - %d",\
                                                   self.__errRunCounter,passedTime,self.__conf.kConf.kDaleyInNginxRunMSec)
            return StateCmdTypes.kDelayRestart


        self.__log("can-start").notice("Error Count - %d, After Delay - Can Start Nginx Now", self.__errRunCounter)

        return StateCmdTypes.kRunNginxNow

    #-----------------------------------------------------------------
    def __handleReconfigure (self):

        retVal = self.__reconfigureNginx()

        if retVal:                
            self.__log("nginx-is-reload").notice("Start Nginx RELOAD (Reconfigure) - %s", self.__conf.getActiveConfigString())
            self.__ngxStatus.startOperation(CurrentOperationTypes.kConfigOperation)                     

        # In case reconfigure failed kill remaining processes if exists
        else:
            self.__log("nginx-reload-failed").notice("Nginx Reconfigure Failed - %s - Restrat Nginx", self.__conf.getActiveConfigString())   
            self.stop()

        return retVal


    #-----------------------------------------------------------------
    def __handleRestart (self):

        self.__ngxStatus.shouldRestartNginx = False
        self.__log("restart-nginx").notice("Restart Nginx Now")
        self.stop()
            

    #-----------------------------------------------------------------
    def __handleNginxStatus (self):

        # If Nginx Oper Status is Up and 
        # Real Nginx Status is Down -- Run Nginx Again
        if self.__ngxStatus.operStatus:
    
            # Check if Nginx Master Process is Alive
            alive = self.__checkIsAlive()

            # All Good - Nginx is UP
            if alive is True:
                return StateCmdTypes.kNginxIsUp

            # Nginx State Changed from Up to Down
            # Kill all Nginx Processes that still UP            
            self.__log("nginx-change-state").notice("Nginx changed state from %s To %s",str(self.__ngxStatus.operStatus),str(alive))

            # Nginx Master is down
            # Change nginx Status to Down and Kill 
            # all Nginx workers if exist
            self.__ngxStatus.reset()            
            self.__killAllNginxProcesses()

            # Run nginx again
            return StateCmdTypes.kRunNginxNow


        # Nginx is Down state, is it ok to start it now
        cmd = self.__isOkToStart()

        return cmd
           
                                    
    #-----------------------------------------------------------------
    def __runNginx (self):
        
        self.__log("run-nginx").notice("Run Nginx Now - Retry - %d  ",self.__errRunCounter) 

        # Start Nginx
        if not self.__executeNginx():
            self.__runNginxFailed()
            return False

        self.__log("in-config").notice("Nginx is starting RUN process (Config)")
        self.__ngxStatus.startOperation(CurrentOperationTypes.kConfigOperation)
   
        return True
        
    #-----------------------------------------------------------------
    def __runNginxFailed (self):

        self.__log("run-after-tick").debug1("Fail to Run Nginx, Error Counter = %d from %d retries",self.__errRunCounter,self.__conf.kConf.kMaxRunNginxRetries)
        self.__logIfConfig()
        self.__timeService.init()
        self.__errRunCounter = self.__errRunCounter + 1
        self.__killAllNginxProcesses()

    #-----------------------------------------------------------------
    def __executeNginx (self):

        """
        Prepare Nginx Configuration file from Template Configuration File
        And Execute Nginx
        Return True in case of Success
        """
        self.__log("nginx-not-alive").info("Nginx is down - Prepare Configuration File and Execute Nginx")
           
        # create configuration file
        retVal = self.__ngxConf.prepareConfFile(self.__conf)
        if not retVal:            
            return False
                    
        # run Nginx
        retVal = self.__ngxCmd.execute()
                  
        return retVal

    #-----------------------------------------------------------------
    def __reconfigureNginx (self):

        """
        Prepare Nginx Configuration file from Template Configuration File
        And Reload Configuration Nginx
        Return True in case of Success
        """
        
        self.__log("nginx-prepare").info("Nginx is up - Prepare Configuration File and Reload Nginx")
           
        # create configuration file
        retVal = self.__ngxConf.prepareConfFile(self.__conf)
        if not retVal:            
            return False
                    
        # Nginx must be up for Configuration Reload
        if not self.__ngxStatus.operStatus:
            self.__log("error-state-on-reload").error("Oper State is Down and Cannot Reload Configuration")
            return False

        # reload Nginx
        self.__log("nginx-reconfig").notice("Nginx - Start Reload Configuration")
        retVal = self.__ngxCmd.reConfigure()
                 
        return retVal

    #-----------------------------------------------------------------
    def __checkIsAlive (self):

        """
        Check if Nginx Master Process is UP
        
        Returns: True in case its up
        """

        masterPid = self.__getNginxMasterPid()

        self.__log("master-pid").debug5("Master PID = %s",str(masterPid))
        
        # Fail to read Nginx Master Process ID File
        if masterPid == (-1):
            self.__log("no-nginx-pid-file").notice("No Nginx Master Process PID File")                
            return False

        # Pid File is valid
        # Check that this process ID is up
        if not self.__isMasterProcessUp(masterPid):
            # Master process is not part of processes (workers) that is up
            # Need to kill all worker processes
            # Kill all Sub processes in case they up and master process is down
            self.__log("master-pid-notin-processes").notice("Master PID (%s) is not in Process PID List",str(masterPid))                
            return False

        return True

    #-----------------------------------------------------------------
    def __getNginxMasterPid (self):

        """
        Read Master process pid from Nginx PID File
        
        Returns: -1 - Error in reading PID File
                  N - Nginx Master Process PID Value
        """
        
        pidFileName = self.__conf.actualNgxPidFile
                
        try:
            pidFile = open(pidFileName,"r")
        except IOError, e:

            # File not found
            if e.errno != errno.ENOENT :                            
                self.__log("pid-file-err").error("Failed to Read Nginx Pid File %s - %s",pidFileName,utils.parseErrnoToString(e))
            else :
                self.__log("pid-file-failed").debug2("Nginx Pid File - %s Not exist",pidFileName)

            return (-1)

        # read pid from nginx pid file
        nginxPid = pidFile.readline()

        pidFile.close()

        # Empty File
        if nginxPid == '\n':
            return (-1)

        return int(nginxPid)

    #-----------------------------------------------------------------
    def __isMasterProcessUp (self, masterPid):
        """
        Search Nginx Master PID, Use Linux Command 'ps'
        If valid it means Nginx is up
        TBD - Check if number of processes is the same as configured workers

        Args:    masterPid - Nginx Master Process pid value
                
        Returns: True in case Nginx Master Process is up
        """    

        cmd = "ps --no-heading " + str(masterPid)

        self.__log("is-master-up").debug5("Collect All Nginx Processes using Popen - %s",cmd)

        (rc,exception,sp) = utils.runPopen(cmd, stdout=subprocess.PIPE)

        if not rc:
            self.__log("popen-failed").error("Fail to run Cmd  %s - %s",cmd,utils.parseErrnoToString(exception))
            return False

        while 1:
            try:                
                if len(sp.stdout.readline()) == 0:
                    self.__log("sp.stdout").debug1("Master Process is not in Process List")
                    return False 
            except Exception, e:
                if utils.isEINTR(e):
                    continue
                else:
                    self.__log("run-pgrep-failed").error("Failed to read from sp.stdout pid list, Master Pid = %d -%s",masterPid,utils.parseErrnoToString(e))
                    return False
            
            break
        
        return True

    #-----------------------------------------------------------------
    def __handleOldWorkers (self):
        """
        Hanlde Old Nginx Workers Limitations      
        """

        if len(self.__oldWorkersGenerationList) == 0:
            return

        shouldKillOldWorkers = False
        currentTime = time.time()
        durationSec = currentTime - self.__oldWorkersGenerationList[0].timestamp # oldest generation duration sec

        # kill old workers (if reached generation limit)
        # ----------------------------------------
        if len(self.__oldWorkersGenerationList) >= self.__conf.nginxOldWorkersGenerationLimit:
            self.__log("nginx-old-workers-generation-limit").notice("Detected Nginx Old Workers %s generations exisitng (generation limit=%s)", 
                                                                    len(self.__oldWorkersGenerationList), 
                                                                    self.__conf.nginxOldWorkersGenerationLimit)
            shouldKillOldWorkers = True

        # kill old workers (if reached time limit)
        # ----------------------------------------
        elif durationSec > self.__conf.nginxOldWorkersTimeLimitSec:
            self.__log("nginx-old-workers-timeout-limit").notice("Detected Nginx Old Workers #%s generation exists %s sec (time limit=%s)", 
                                                                 len(self.__oldWorkersGenerationList), 
                                                                 durationSec,
                                                                 self.__conf.nginxOldWorkersTimeLimitSec)
            shouldKillOldWorkers = True

        if shouldKillOldWorkers is True:
            self.__killOldestNginxWorkers()

    #-----------------------------------------------------------------
    def __killOldestNginxWorkers (self):
        """
        Kill Oldest generation Nginx Workers      
        """

        # no old generation
        if len(self.__oldWorkersGenerationList) == 0:
            return True

        # extract oldest generation
        oldWorkersGroup = self.__oldWorkersGenerationList.pop(0)

        # no old workers in the oldest generation
        if len(oldWorkersGroup.pidSet) == 0:
            return True

        (rc,pidList) = self.__getAllNginxOldWorkersPids(oldWorkersGroup.masterPid)

        if not rc:
            self.__log("get-old-workers-pids").error("Failed to get Nginx Old Workers PIDs")
            return False

        # keeps only PIDs of active workers of this generation
        # note: set 'currentPidSet' keeping only elements also found in set 'oldWorkersGroup'
        currentPidSet = set(pidList)
        currentPidSet.intersection_update(oldWorkersGroup.pidSet)
        self.__log("kill-nginx-old-worker-pid").notice("Kill Nginx Old Worker PIDs: %s (out of %s)", 
                                                       currentPidSet, oldWorkersGroup.pidSet)
         
        retVal = True

        # kill any exisitng old worker
        for pid in currentPidSet:
            self.__log("kill-nginx-old-worker-pid").debug1("Kill Nginx Old Worker PID %s" % pid)  
            if not self.__KillNginxProcess(pid):                
                retVal = False

        return retVal
        
    #-----------------------------------------------------------------
    def __addOldWorkersPids (self):

        masterPid = self.__getNginxMasterPid()
        self.__log("master-pid").debug5("Master PID = %s",str(masterPid))

        # Fail to read Nginx Master Process ID File
        if masterPid == (-1):
            self.__log("no-nginx-pid-file").notice("No Nginx Master Process PID File")  
            return

        (rc,pidList) = self.__getAllNginxOldWorkersPids(masterPid)

        if not rc:
            self.__log("add-old-workers-ids-failed").error("Failed to add all Nginx Old Workers PIDs")
            return False

        currentPidSet = set(pidList)
        if len(self.__oldWorkersGenerationList) > 0 and len(currentPidSet) > 0:
            
            # remove PIDs from previous generations
            # note: return set 'currentPidSet' after removing elements found in 'workersGroup'
            for workersGroup in self.__oldWorkersGenerationList:
                currentPidSet.difference_update(workersGroup.pidSet)

        oldWorkersGroup = NginxWorkersGroup(masterPid, currentPidSet)
        self.__oldWorkersGenerationList.append(oldWorkersGroup)
        self.__log("next-nginx-old-workers").notice("Nginx Old Workers generation #%s: %s", 
                                                    len(self.__oldWorkersGenerationList), oldWorkersGroup.pidSet)
        
        return True

    #-----------------------------------------------------------------
    def __getAllNginxOldWorkersPids (self, ppid):
        """
        return (rc,pid list)
        rc = False in operation Failure
        pid list = All Process PID's with the same User Name and Current Working Directory
        """                    
            
        # display all current old worker processes whos parent is 'master pid' 
        cmd = "ps f --ppid %s -o pid,cmd | grep \"%s\" | awk '{print $1}' " % (ppid, self.__conf.kConf.kOldWorkerShutdownCmd)

        self.__log("get-old-workers").info("Collect All Nginx Old Workers using Popen - %s",cmd)

        (rc,exception,sp) = utils.runPopen(cmd, stdout=subprocess.PIPE, shell=True)
   
        pidList = []
  
        # ps Failed - Kill All Nginx Old Workers
        if not rc:
            self.__log("ps-failed").error("Failed to perfrom %s- %s",cmd,utils.parseErrnoToString(exception))
            return (False,pidList)
  
        # Try to Print all Up Old Workers and Kill them
        try:   

            for line in sp.stdout:
                self.__log("old-worker-next-pid").debug1("Next Nginx Old Worker Process - %s",line) 
                pid = line.strip()
                pidList.append(pid)

            self.__log("num-nginx-old-workers").notice("Found Total of %d Nginx Old Workers: %s", len(pidList), pidList)
            retVal = True            
  
        except Exception, e: 
            self.__log("read-stdout-failed").error("Failed to read ps result from stdout - %s",utils.parseErrnoToString(e))            
            retVal = False
  
  
        return (retVal,pidList)

    #-----------------------------------------------------------------
    def __getAllNginxRunningWorkersPids (self, ppid):
        """
        return (rc,pid list)
        rc = False in operation Failure
        pid list = All Process PID's with the same User Name and Current Working Directory
        """                    
            
        # display all current running worker processes whos parent is 'master pid' 
        cmd = "ps f --ppid %s -o pid,cmd | grep -v \"%s\" | awk '{print $1}' " % (ppid, self.__conf.kConf.kOldWorkerShutdownCmd)

        self.__log("get-running-workers").info("Collect All Nginx Running Workers using Popen - %s",cmd)

        (rc,exception,sp) = utils.runPopen(cmd, stdout=subprocess.PIPE, shell=True)
   
        pidList = []
  
        # ps Failed - Kill All Nginx running Workers
        if not rc:
            self.__log("ps-failed").error("Failed to perfrom %s- %s",cmd,utils.parseErrnoToString(exception))
            return (False,pidList)
  
        # Try to Print all Up running Workers and Kill them
        try:   

            for line in sp.stdout:
                self.__log("running-worker-next-pid").debug1("Next Nginx Running Worker Process - %s",line) 
                pid = line.strip()
                pidList.append(pid)

            self.__log("num-nginx-running-workers").notice("Found Total of %d Nginx Running Workers: %s", len(pidList), pidList)
            retVal = True            
  
        except Exception, e: 
            self.__log("read-stdout-failed").error("Failed to read ps result from stdout - %s",utils.parseErrnoToString(e))            
            retVal = False
  
  
        return (retVal,pidList)
                  
    #-----------------------------------------------------------------
    def __killAllNginxProcesses (self):

        """
        Kill All Nginx processes
        In Mini System kill only the Nginx processes with the same user ID and current working directory 
        else Kill all nginx processes (VM,STD)      
        """

        # reset monitoring
        self.__oldWorkersGenerationList[:] = []

        if self.__conf.isUT:
            self.__killNginxProcessesAllByUser()
            return
        elif self.__conf.isMini:
            if self.__killAllNginxProcessesMini():
                return
    
        self.__killNginxProcessesAll()            

    #-----------------------------------------------------------------
    def __killAllNginxProcessesMini (self):
        """
        Kill All Nginx processes in MINI system       
        """

        self.__log("kill-mini").info("Kill All Nginx Processes with (User,CWD) - Mini System")

        (rc,pidList) = self.__getAllNginxProcessIdMini()

        if not rc:
            self.__log("get-ids-failed").error("Failed to get all Mini Nginx Process ID's - Kill All")
            return False

        retVal = True

        if not len(pidList):
            self.__log("no-process").info("Not Found Nginx Process with My User and Current Working Directory")

        for pid in pidList:
            if not self.__KillNginxProcess(pid):                
                retVal = False
         
        return retVal
                   

    #-----------------------------------------------------------------
    def __getAllNginxProcessIdMini (self):
        """
        return (rc,pid list)
        rc = False in operation Failure
        pid list = All Process PID's with the same User Name and Current Worling Directory
        """                        
        userName = getpass.getuser()
        cmd = "pgrep -u "+ str(userName) + " " + self.__conf.kConf.kNginxExeName

        self.__log("get-mini").info("Collect All Nginx Processes using Popen - %s",cmd)

        (rc,exception,sp) = utils.runPopen(cmd, stdout=subprocess.PIPE)
   
        pidList = []
  
        # Pgrep Failed - Kill All Nginx Processes
        if not rc:
            self.__log("pgrep-failed").error("Failed to perfrom %s- %s",cmd,utils.parseErrnoToString(exception))
            return (False,pidList)
  
  
        # Try to Print all Up Processes and Kill them
        try:       
            num = 0     
            self.__log("cwd").info("Current Working Directory - %s",os.getcwd()) 
            for pid in sp.stdout:
                num = num+1 
                spid = pid.rstrip()
                if self.__compareCWD(spid):
                    pidList.append(spid)
  
            self.__log("num-nginx-compare-cwd").info("Found Total of %d Nginx Processes, %d Running in my CWD",num,len(pidList))
            retVal = True            
  
        except Exception, e: 
            self.__log("read-stdout-failed").error("Failed to read Pgrep result from stdout - %s",utils.parseErrnoToString(e))            
            retVal = False
  
  
        return (retVal,pidList)


    #-----------------------------------------------------------------
    def __compareCWD (self,pid):
        """
        Return True in case process with id = pid is running on current working directory
        """

        # Get Current Working Directory
        try:
            currentDirectory = os.getcwd()
        except Exception:
            return False
        
        try:                  
            pPath = "/proc/" + pid +  "/cwd"            
            result = os.readlink(pPath)
            self.__log("read-link").debug1("Read Link = %s, Result = %s",pPath,result)
            
            if result == currentDirectory:
                return True
            else:
                return False
        except Exception, e:
            self.__log("read-link-failed").error("Failed to read link %s - %s",pPath,utils.parseErrnoToString(e)) 
            return False


    #-----------------------------------------------------------------
    def __KillNginxProcess (self,pid):

        """
        Kill processes with id = pId
        Return True on successes
        """
 
        cmd = "kill " + "-s TERM " + pid 

        self.__log("kill-nginx-process").info("Kill Nginx Process - %s using Popen - %s",pid,cmd)
 
        (rc,exception,sp) = utils.runPopen(cmd)
 
        if not rc:
            self.__log("kill-nginx-process-error").error("Kill Nginx Processes with PID = %s Failed - %s",pid,utils.parseErrnoToString(exception))
 
        return rc
    
    #-----------------------------------------------------------------
    def __killNginxProcessesAll (self):
        """
        Kill all processes with name 'self.__conf.kConf.kNginxExeName'
        Return True on successes
        """

        cmd = "killall " + self.__conf.kConf.kNginxExeName + " -s TERM"

        self.__log("kill-nginx-processes").info("Kill All Nginx Processes using Popen - %s",cmd)

        (rc,exception,sp) = utils.runPopen(cmd)

        if not rc:
            self.__log("kill-nginx-process-all").error("Killall All Nginx Processes Failed - %s",utils.parseErrnoToString(exception))

        return rc

    #-----------------------------------------------------------------
    def __killNginxProcessesAllByUser (self):
        """
        Kill all processes with name 'self.__conf.kConf.kNginxExeName'
        Return True on successes
        """

        userName = getpass.getuser()
        cmd = "killall "+ self.__conf.kConf.kNginxExeName + " -u " + str(userName) + " -s TERM"
        
        self.__log("kill-nginx-processes-user").info("Kill All Nginx Processes of User - %s using Popen - %s",userName,cmd)

        (rc,exception,sp) = utils.runPopen(cmd)

        if not rc:
            self.__log("kill-nginx-process-user").error("Killall All User - %s, Nginx Processes Failed - %s",userName,utils.parseErrnoToString(exception))

        return rc

    #-----------------------------------------------------------------
    def __logIfConfig (self):

        
        cmd = "ifconfig" 
                   
        (rc,exception,sp) = utils.runPopen(cmd, stdout=subprocess.PIPE)

        if not rc:
            self.__log("log-if-config").error("Fail to run ifconfig as part exec Nginx failure - %s",utils.parseErrnoToString(exception))
            return

        try:
            for line in sp.stdout:
                self.__log("log-ifconfig").debug3("%s",line)
            
        except Exception:
            pass             

        return            
        
    # UT Functions    
    #-----------------------------------------------------------------
    def getNginxMasterPidUT (self):    
        return self.__getNginxMasterPid()

    #-----------------------------------------------------------------
    def getAllNginxRunningWorkersPidsUT (self, ppid):
        return self.__getAllNginxRunningWorkersPids(ppid)
