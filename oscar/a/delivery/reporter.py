#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: hagaia
# 

import os
import json
import shutil
import subprocess
import re

from a.stats.stats_comm_over_file_client import StatsCommOverFileClient

import utils
import nginx_ipc
import nginx_log
import web_backend
import topper_reporter
import delivery_volume

if  __package__ is None:
    G_NAME_MODULE_DELIVERY = "unknown"
    G_NAME_GROUP_DELIVERY_REPORTER = "unknown"
else:
    from . import G_NAME_MODULE_DELIVERY 
    from . import G_NAME_GROUP_DELIVERY_REPORTER

#-------------------------------------------------------------------------------------------------
class Reporter(object):
   
    def __init__ (self, name, logger):
        self.__name = name        
        self.__log = logger.createLogger(G_NAME_MODULE_DELIVERY, G_NAME_GROUP_DELIVERY_REPORTER)

        self.__timeFromLastCounterFetchMsec = 0
        self.__timeFromLastReadLinuxStatsMsec  = 0
        self.__timeFromLastVolumeReportMsec = 0
        self.__timeFromLastWebReportMsec    = 0
        self.__timeFromLastRotateReportMsec = 0
        self.__timeFromLastStatReportMsec   = 0
        self.__timeFromLastNginxRotateMsec  = 0
        
        self.__ngxIpc = nginx_ipc.NginxIpc("nginx-ipc", logger)    
        self.__webApp = web_backend.WebBackend(self.__log)
        self.__ngxLog = nginx_log.NginxLog(logger)
        self.__volumeManager = delivery_volume.VolumeManager(self.__log)

        self.__conf = None

        self.__topperReporter = topper_reporter.TopperReporter("delivery-topper", logger)        
        self.__topperFileNum = 0
        self.__topperTempFile = ""        
        self.__topperRotataionDiffTime = utils.TimesSerivce()

        self.__timeService = utils.TimesSerivce()
        self.__localTimeService = utils.TimesSerivce()

        # Dictionary of current Nginx Counters
        self.__nginxCounterDic = {}
        self.__vmStatDic = {}
        self.__diskStatDic = {}

        self.__vmRelevantFields = ["nr_free_pages","nr_dirty","nr_writeback","nr_shmem","nr_dirtied",
                                   "nr_written","nr_dirty_threshold","nr_dirty_background_threshold",
                                   "pgpgin","pgpgout","pswpin","pswpout","pgfree","pgfault"]


        self.__diskFieldsNames = ["read-completed","read-merged","sectors-read","read-time-ms",
                                  "write-completed","write-merged","sectors-write","write-time-ms",
                                  "current-io","io-time-ms","weighted-io-ms"]    

        self.__diskDeviceRegex = re.compile('sd[a-z]*')

        self.__stats = StatsCommOverFileClient("delivery",logger)

        self.__nginxFetchCounterError = 0
        
    
    #-------------------------------------------------------------------------------------------------
    def init (self, conf, ngxCmd, ngxStatus):

        self.__conf      = conf        
        self.__ngxCmd    = ngxCmd    

        self.__ngxStatus = ngxStatus

        if len(conf.statsDir):
            self.__stats.init(conf.statsDir)
        
        self.__webApp.init(conf)

        self.__volumeManager.init(conf)

        if not self.__topperReporter.init(conf) :
            return False

        if not self.__ngxLog.init(self.__conf):
            return False

        self._handleLinuxStats()
        self._handleStats()

        return True

        
    #-------------------------------------------------------------------------------------------------
    def start (self):

        self.__log("start-reporter").info("Start Reporter")
        self.__webApp.writeTitelsDeliverd(0)
        rc = self.__topperReporter.start()          
        return rc
    
    #-------------------------------------------------------------------------------------------------
    def end (self):
        
        # Before exist check if there is records to handle
        self._handleTopperRotation()
        self.__webApp.writeTitelsDeliverd(0)
        self.__topperReporter.end();
        self.__ngxLog.end()
        self.__log("end-reporter").info("End Reporter")

    
    #-------------------------------------------------------------------------------------------------
    def oneTick (self):

        retVal = True
        isReopenNginxLogs = False

        timeFromLastTickMsec = self.__timeService.tickFromLastMsec()
           
        #  Fetch Nginx Counters - Only in case Nginx is Up
        ##---------------------------------------------------------------------------------------------------                              
        self.__timeFromLastCounterFetchMsec = self.__timeFromLastCounterFetchMsec + timeFromLastTickMsec
 
        if self.__timeFromLastCounterFetchMsec >= self.__conf.kConf.kFetchCountersFromNginxIntervalMsec :
               
            self.__timeFromLastCounterFetchMsec = 0

            self.__localTimeService.init()
                                        
            self._handleNginxCounters()

            self.__log("handle-nginx-counters").debug4("Handle Nginx Counters (%d ms) - Interval %d",
                                                       self.__localTimeService.tickFromInitMsec(),self.__conf.kConf.kFetchCountersFromNginxIntervalMsec)


        #  Handle Linux Stats
        ##---------------------------------------------------------------------------------------------------                              
        self.__timeFromLastReadLinuxStatsMsec = self.__timeFromLastReadLinuxStatsMsec + timeFromLastTickMsec
 
        if self.__timeFromLastReadLinuxStatsMsec >= self.__conf.kConf.kReadLinuxStatsIntervalMsec :
               
            self.__timeFromLastReadLinuxStatsMsec = 0

            self.__localTimeService.init()
                        
            self._handleLinuxStats()          
            
            self.__log("handle-nginx-counters").debug4("Handle Linux Stats (%d ms) - Interval %d",
                                                       self.__localTimeService.tickFromInitMsec(),self.__conf.kConf.kReadLinuxStatsIntervalMsec)
                        

        # Update Web Application
        #--------------------------------------------------------------------------------------------------- 
        self.__timeFromLastWebReportMsec = self.__timeFromLastWebReportMsec + timeFromLastTickMsec
 
        if self.__timeFromLastWebReportMsec >= self.__conf.kConf.kWebAppFileUpdateIntervalMsec :

            self.__timeFromLastWebReportMsec = 0

            self.__localTimeService.init()            
              
            self._handleWebApp()

            self.__log("handle-web-app").debug4("Handle Web App (%d ms) - Interval %d",
                                                       self.__localTimeService.tickFromInitMsec(),self.__conf.kConf.kWebAppFileUpdateIntervalMsec)
            
                         
        # Update Volume Report
        #---------------------------------------------------------------------------------------------------         
        self.__timeFromLastVolumeReportMsec = self.__timeFromLastVolumeReportMsec + timeFromLastTickMsec
     
        if self.__timeFromLastVolumeReportMsec >= self.__conf.kConf.kVolumeReportIntervalMsec :
     
            self.__timeFromLastVolumeReportMsec = 0

            self.__localTimeService.init()            
     
            self._handleVRecords()

            self.__log("handle-volume").debug4("Handle Volume (%d ms) - Interval %d",
                                               self.__localTimeService.tickFromInitMsec(),self.__conf.kConf.kVolumeReportIntervalMsec)


        # Handle Topper File Rotation
        #--------------------------------------------------------------------------------------------------- 
        self.__timeFromLastRotateReportMsec = self.__timeFromLastRotateReportMsec + timeFromLastTickMsec
 
        if self.__timeFromLastRotateReportMsec >= self.__conf.kConf.kTopperFileRotateIntervalMsec :
 
            self.__timeFromLastRotateReportMsec = 0

            self.__localTimeService.init()            

            if self._handleTopperRotation():
                isReopenNginxLogs = True

            self.__log("handle-rotation").debug4("Handle Topper Rotation (%d ms) - Interval %d",
                                                 self.__localTimeService.tickFromInitMsec(),self.__conf.kConf.kTopperFileRotateIntervalMsec)
         


        # Handle Stat Report
        #--------------------------------------------------------------------------------------------------- 
        self.__timeFromLastStatReportMsec = self.__timeFromLastStatReportMsec + timeFromLastTickMsec

        if self.__timeFromLastStatReportMsec >= self.__conf.kConf.kReportToStatIntervalMsec :

            self.__timeFromLastStatReportMsec = 0

            self.__localTimeService.init()            

            retVal = self._handleStats()

            self.__log("handle-stats").debug4("Handle Stats (%d ms) - Interval %d",
                                              self.__localTimeService.tickFromInitMsec(),self.__conf.kConf.kReportToStatIntervalMsec)



        # Handle Nginx Log Rotation
        #--------------------------------------------------------------------------------------------------- 
        self.__timeFromLastNginxRotateMsec = self.__timeFromLastNginxRotateMsec + timeFromLastTickMsec

        if self.__timeFromLastNginxRotateMsec >= self.__conf.kConf.kNginxLogRotateIntervalMsec :

            self.__timeFromLastNginxRotateMsec = 0

            self.__localTimeService.init()            

            if self._handleErrLogRotation():
                isReopenNginxLogs = True

            self.__log("handle-errlog-rotation").debug4("Handle Nginx Log Rotation (%d ms) - Interval %d",
                                                        self.__localTimeService.tickFromInitMsec(),self.__conf.kConf.kNginxLogRotateIntervalMsec)


        # Signal Nginx to Repoen Log Files 
        #--------------------------------------------------------------------------------------------------- 
        if isReopenNginxLogs:            

            # Files: record.log, error.log
            self.__reOpenTopperFile()

            # In case Nginx is down do not send signal of reopen
            if self.__ngxStatus.operStatus:
                self.__ngxCmd.reOpenLogs()
                self.__log("reopen-logs").debug2("Send to Nginx Signal to Reopen log Files")

        return retVal


    # protected
    #-------------------------------------------------------------------------------------------------
    def _handleNginxCounters (self):

        if not self.__ngxStatus.operStatus:
            self.__nginxFetchCounterError = 0
            return

        # Failed to collect Counters
        if not self.__collectNginxCounters():

            self.__nginxFetchCounterError = self.__nginxFetchCounterError + 1

            if self.__nginxFetchCounterError > self.__conf.maxFetchCounterError:                
                self.__log("handle-counters-fail").error("Fail to Fetch Counters from Nginx - %d - Set Nginx Down", self.__nginxFetchCounterError)
                self.__nginxFetchCounterError  = 0
                self.__ngxStatus.startNginxRestart()
            else:
                self.__log("handle-counters-fail").info("Fail to Fetch Counters from Nginx - %d < %d", self.__nginxFetchCounterError,self.__conf.maxFetchCounterError)

        else:
            self.__nginxFetchCounterError = 0
            self.__CheckIfWorkerCrashed()
                   

    #-------------------------------------------------------------------------------------------------
    def _handleWebApp (self):

        if self.__ngxStatus.operStatus:
            key = "ActiveRequests"
            if key in self.__nginxCounterDic:
                currentDeliverd   = long(self.__nginxCounterDic["ActiveRequests"])
                self.__webApp.writeTitelsDeliverd(currentDeliverd)
                return
        
        self.__webApp.writeTitelsDeliverd(0)
                    

    #-------------------------------------------------------------------------------------------------
    def _handleVRecords (self):

        volume = delivery_volume.VolumeCounters()

        if self.__volumeManager.collectVolume(volume):
            self.__reportVolume(volume)
                    
    #-------------------------------------------------------------------------------------------------
    def _handleTopperRotation (self):
        """
        Return True in case rotation succeed and 
        reopen log files is needed
        """
        
        # Is topper Temp file valid - during rotation process
        if len(self.__topperTempFile):

             # Too much time when file is still opened
             # by Any Stale?? process, so the temp file is deleted
            if (self.__topperRotataionDiffTime.tickFromInitSec() >= self.__conf.maxTimeReopenWaitSec):

                self.__log("ignore-report").error("Topper File Open by Nginx Process for %d sec, Max Waiting Time is = %d sec --- Delete(Ignore) File Report - %s",
                                                  self.__topperRotataionDiffTime.tickFromInitSec(),self.__conf.maxTimeReopenWaitSec,self.__topperTempFile)
               
                # print all opened workers
                self.__isTopperFileOpen(True)
                self.__deleteTopperTempFile() 
                self.__topperTempFile = ""           
                # Signal Now to Reopen and Reset State
                return True
            else:            
                # If all processes closed the file it is posible to 
                # rename it to Topper Regullar report
                if not self.__isTopperFileOpen(False):            
                    self.__renameTopperFileStage2()                
                    self.__topperTempFile = ""
                else:                
                    self.__log("topper-file-open").notice("Topper File is still Open by Nginx Process for %d sec, Max Waiting Time = %d sec",
                                                          self.__topperRotataionDiffTime.tickFromInitSec(),self.__conf.maxTimeReopenWaitSec)
                return False

        # Do not start Topper rotation in case of Status Down
        if not self.__ngxStatus.operStatus:
            return False
            
        curSize = self.__getFileSize(self.__conf.actualNgxRecordsLogFile)

        # Fail to get filename size
        if curSize == (-1):
            self.__log("get-filesize-failed").error("Failed to get Records Log File %s Size",self.__conf.actualNgxRecordsLogFile)
            return False
        
        # Nothing to in the file - no rotation
        if curSize == 0:
            self.__log("no-data").debug3("No Records in Records Log File %s",self.__conf.actualNgxRecordsLogFile)
            return False

        # Report To Topper
        #------------------------------------
        if self.__conf.reportToTopper:

            # mv Base file to Topper Tmp File
            if not self.__renameTopperFileStage1():
                return False
            else:
                # Set rotation start time
                self.__topperRotataionDiffTime.init()
            

        # Ignore Topper, Delete Old File
        #------------------------------------
        else:
            # delete Base file 
            if not self.__deleteTopperFile():            
                return False            
                         
        return True

    #-------------------------------------------------------------------------------------------------
    def _handleErrLogRotation (self):

        # Do not start Topper rotation in case of Status Down
        if not self.__ngxStatus.operStatus:
            return False

        return self.__ngxLog.tick()


    #-------------------------------------------------------------------------------------------------  
    def _handleStats (self):
        """
        Report Counters to Stats Module
        """

        mergedDic = dict(self.__nginxCounterDic.items() + self.__vmStatDic.items() + self.__diskStatDic.items())

        # If stat module configured with path 
        if len(self.__conf.statsDir):

            self.__stats.send(mergedDic)
            self.__log("write-stats").debug5("Write Delivery Counters to Stats Module\n - %s", str(mergedDic))


    #-------------------------------------------------------------------------------------------------  
    def _handleLinuxStats(self):
        
        self.__readVmStats()
        self.__readDiskStats()


    # private    
    #-------------------------------------------------------------------------------------------------  
    def __getFileSize (self,fileName):
    
        try:
            curSize = os.path.getsize(fileName)
            self.__log("file-size-ok").debug3("Get %s size, Size = %s", fileName,str(curSize))
        except OSError, e:
            self.__log("file-size-err").error("Get %s size Failed - %s",fileName,utils.parseErrnoToString(e))
            return (-1)
                            
        return curSize

    #-------------------------------------------------------------------------------------------------  
    def __deleteTopperFile (self):

        try:
            os.remove(self.__conf.actualNgxRecordsLogFile)
            retVal = True
            self.__log("del-topper-base-file").debug1("Delete Topper File (Instead of rotation - Cfg ReportToTopper = False) = %s",self.__conf.actualNgxRecordsLogFile)
        except OSError:
            self.__log("del-topper-base-file-fail").error("Delete Topper File Failed = %s",self.__conf.actualNgxRecordsLogFile)
            retVal = False

        return retVal


    #-------------------------------------------------------------------------------------------------  
    def __deleteTopperTempFile (self):

        if len(self.__topperTempFile) == 0:
            return

        try:
            os.remove(self.__topperTempFile)
            self.__log("del-topper-temp-file").debug1("Delete Topper Temp File (Instead of rotation - Cfg ReportToTopper = False) = %s",self.__topperTempFile)
        except OSError:
            self.__log("del-topper-temp-file-fail").error("Delete Topper Temp File Failed = %s",self.__topperTempFile)            
        
        return
           
    #-------------------------------------------------------------------------------------------------  
    def __isTopperFileOpen (self, isLogResult):

        """
        Return True if topper file is opened by other process
        """
    
        cmd = "lsof " + self.__topperTempFile

        self.__log("is-file-opend").debug3("Check if temp topper file is still open by any other process - %s",cmd)

        (rc,exception,sp) = utils.runPopen(cmd, stdout=subprocess.PIPE)

        if not rc:
            self.__log("is-open-failed").error("Fail to run Cmd  %s - %s",cmd,utils.parseErrnoToString(exception))
            return False

        while 1:
            try: 
                if isLogResult:
                    for line in sp.stdout:
                        self.__log("sp.stdout-log").error("Open Worker on Record Log File After Reopen Signal - %s",line)
                    return True
                else:
                    if len(sp.stdout.readline()) == 0:
                        self.__log("sp.stdout").debug3("File %s, is not Opened by any Other processes",self.__topperTempFile)
                        return False 
                    else:
                        self.__log("sp.stdout-notempty").debug1("File %s is still opened By Nginx processes",self.__topperTempFile)

            except Exception, e:
                if utils.isEINTR(e):
                    continue
                else:
                    self.__log("run-isopen-failed").error("Failed to read from sp.stdout for is Open File = %s -%s",self.__topperTempFile,utils.parseErrnoToString(e))
                    return False

            break

        return True

    #-------------------------------------------------------------------------------------------------
    def __renameTopperFileStage1 (self):
        """
        Rotate (move) Tooper Records File To Temp File
        When All Nginx Processes close the file move it to final File in stage2            
        """
                                            
        dataFileName = "data" + str('%08d' % self.__topperFileNum) + ".data.tmp"
        
        newFileName = os.path.join(self.__conf.topperDir, self.__conf.kConf.kTopperDataDir, dataFileName)

        try:
            shutil.move(self.__conf.actualNgxRecordsLogFile,newFileName)            
            retVal = True
            self.__log("rename-topper-base-file").debug3("Rename Topper File (Rotation) = %s to Temp File = %s",self.__conf.actualNgxRecordsLogFile,dataFileName)
        except:
            self.__log("rename-topper-base-file-fail").error("Rename Topper File (Rotation) = %s  to Temp File = %s Failed",self.__conf.actualNgxRecordsLogFile, dataFileName)
            retVal = False


        if retVal:
            self.__topperTempFile = newFileName

            self.__topperFileNum =  self.__topperFileNum + 1
    
            # This is because '%08'
            self.__topperFileName = self.__topperFileNum % 100000000
        else:
            self.__topperTempFile = ""

        
        return retVal
        
        
    #-------------------------------------------------------------------------------------------------
    def __renameTopperFileStage2 (self):

        """
        Even in case of failure in rename It finish the process of rotating
        So It can handle new Files and not stuck on a Loop
        """
                                        
        # remove .tmp
        newFileName = self.__topperTempFile[:-4]

        try:
            os.rename(self.__topperTempFile,newFileName)
            self.__log("rename-topper-tmp-file").debug3("Rename Topper Temp File (Rotation) To Data File = %s",newFileName)
            
        except:
            self.__log("rename-topper-tmp-file-fail").error("Rename Topper Temp File (Rotation) Failed = %s",newFileName)            
        
    
    
    #-------------------------------------------------------------------------------------------------
    def __reOpenTopperFile (self):
        
        retVal = self.__topperReporter.repoen()
        
        if not retVal:
            self.__log("reopen-fail").error("Failed to reopen topper base file")
        else:
            self.__log("reopen-topper-file").debug2("Reopen Tooper File")

        return retVal

    #-------------------------------------------------------------------------------------------------
    def __reportVolume (self, volume):

        i = 0        
        for iConf in self.__conf.InterfaceMap.values():
            self.__log("report-v-record").debug2("Report V Record Interface - %s Device = %s -- RX = %s TX = %s", 
                                                 iConf.name, iConf.egressInterface, str(volume.volumeCounters[i].bytesIn), str(volume.volumeCounters[i].bytesOut))
            i = i + 1

        self.__topperReporter.reportVolume(volume)
        
    #-------------------------------------------------------------------------------------------------
    def __collectNginxCounters (self):
                        
        request  = nginx_ipc.Request()        
        response = nginx_ipc.Response()

        request.host    = self.__conf.kConf.kNginxStatusIp
        request.port    = self.__conf.nginxStatusPort
        request.url     = self.__conf.kConf.kNginxStatusUrl
        request.timeout = self.__conf.countersFetchTimeoutSec

        retVal = self.__ngxIpc.sendRequest(request, response)

        if not retVal:
            self.__log("nginx-status-error").info("Failed to receive counters from Nginx")
            return False

        if response.status != 200 or response.reason != "OK":
            self.__log("nginx-status-failed").notice("Failed to read Nginx Status over HTTP - Status = '%d' : Reason = %s", response.status, response.reason)
            return True

        try:
            decoder = json.JSONDecoder()            
            self.__nginxCounterDic = decoder.decode(response.data)
            self.__log("nginx-counters").debug5(str(self.__nginxCounterDic))
        except Exception, e:
            self.__log("decode-counters-fail").error("Fail to decode Nginx Counters - %s",utils.parseErrnoToString(e))

        return True  

    #-------------------------------------------------------------------------------------------------  
    def __readVmStats (self):

        cmd = "cat /proc/vmstat"        

        self.__log("read-vmstat").debug5("Perfoem - %s",cmd)

        (rc,exception,sp) = utils.runPopen(cmd, stdout=subprocess.PIPE)

        if not rc:
            self.__log("popen-vm-failed").error("Fail to run Cmd  %s - %s",cmd,utils.parseErrnoToString(exception))
            return False
            
        try:                   
            for line in sp.stdout:
                value = line.split(" ")                
                if (value[0] in self.__vmRelevantFields):
                    key = "vm_stat_" + value[0]
                    self.__vmStatDic[key] = value[1].rstrip('\r\n')
        
        except Exception, e:
            if not utils.isEINTR(e):
                self.__log("run-vmstat-err").error("Failed to read from sp.stdout vmstat info %s",utils.parseErrnoToString(e))
                return False

        self.__log("read-vmstat").debug5("Vmstat Dictionary - %s",str(self.__vmStatDic))
                
        return True


    #-------------------------------------------------------------------------------------------------  
    def __readDiskStats (self):

        cmd = "cat /proc/diskstats"        

        self.__log("read-diskstat").debug5("Perfoem - %s",cmd)

        (rc,exception,sp) = utils.runPopen(cmd, stdout=subprocess.PIPE)

        if not rc:
            self.__log("popen-disk-failed").error("Fail to run Cmd  %s - %s",cmd,utils.parseErrnoToString(exception))
            return False
    
        try:                   
            for line in sp.stdout:
                value = line.split()                               
                if (len(value) >= 3 and self.__diskDeviceRegex.match(value[2])):                    
                    for i in range(len(self.__diskFieldsNames)):
                        if len(value) >= (i+3):
                            key = "disk_hdd_" + value[2] + "-" + self.__diskFieldsNames[i]
                            self.__diskStatDic[key] = value[i+3].rstrip('\r\n')
                            self.__log("disk-stat-value").debug4("i = %d key - %s, value - %s",i,key,self.__diskStatDic[key])
        
        except Exception, e:
            if not utils.isEINTR(e):
                self.__log("run-diskstat-err").error("Failed to read from sp.stdout diskstat info %s",utils.parseErrnoToString(e))
                return False

        self.__log("read-diskstat").debug5("Diskstat Dictionary - %s",str(self.__diskStatDic))
                
        return True

    
    #-------------------------------------------------------------------------------------------------
    def __CheckIfWorkerCrashed (self):

        key = "General-NginxWorkerProcessCrashed"
        numberOfCrashedWorkers = 0

        if key in self.__nginxCounterDic:
            numberOfCrashedWorkers = long(self.__nginxCounterDic[key])

        if numberOfCrashedWorkers != 0:
            self.__log("worker-crashed").error("Using Nginx q-status response - Nginx Worker Crashed = %d", numberOfCrashedWorkers)
        else:
            return

        if self.__conf.deliveryRestartOnWorkerCrash is False:
            return

        self.__log("restart-after-crash").notice("Nginx Worker Crashed, Restart Nginx")
        self.__ngxStatus.startNginxRestart()
