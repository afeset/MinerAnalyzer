#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: hagaia
# 

import a.infra.process

import subprocess
import os, errno
import shlex
import time
from threading import Thread

#-----------------------------------------------------------------------------------------------
def parseErrnoToString (e):

    try:
        errStr =  "Type = " + type(e) + " Args = " + e.args + "Err Message = " + os.strerror(e.errno)
    except Exception:
        errStr = str(e)

    return errStr

  #return  "Errno = " + str(e.errno) + " Err Code = " + str(errno.errorcode[e.errno]) + " Err Message = " + os.strerror(e.errno)

#-----------------------------------------------------------------------------------------------
def isEINTR (e):

    try:
        if e.errno == errno.EINTR:
            return True
        else:
            return False
    except Exception, e:
        return False

#-----------------------------------------------------------------------------------------------
def runPopen (command, close_fds = False, stdout = None, shell = False, maxTimeMsec = 0):
    """
        Run Sub process command and handle EINTR signal

        Args:    commannd to split and run + Popen arguments
            
        Returns: 1. True/False, 
                 2. if False the exception errno, 
                 3. subprocess.Popen("") return value Subprocess class)
    """

    #self.__log("run-linux-cmd").info("Run Popen - %s, CloseFds = %s, MaxtimeMsec = %d",command,str(close_fds),maxTimeMsec)
    
    if shell is True:
        args = command
    else:
        args = shlex.split(command)

    e  = Exception
    sp = None

    while 1:
        
        try:
            sp = subprocess.Popen(args,close_fds=close_fds,stdout = stdout,shell = shell)

            retVal = True
            
            #self.__log("run-popen-finishtime").debug1("Child process finished after %s/%s msec",counter,maxTimeMsec)
            
        except Exception, e:
            if isEINTR(e):
                continue
            else:        
                retVal =  False

        break

    # Wait for child process to end but not more than maxTimeMsec
    if maxTimeMsec and retVal:
                                
        counter = 0

        while(counter < maxTimeMsec):
            # None means the child not finished yet
            if (sp.poll() != None):
                break
        
            time.sleep(0.01)
                    
            counter = counter + 10

        
    return (retVal,e,sp)


#-----------------------------------------------------------------------------------------------
class TimesSerivce(object):

    def __init__ (self):
        self.reset()

    #-------------------------------------------------------------------------------------------------
    def reset (self):
        self.__lastTimeMsec = 0

    #-------------------------------------------------------------------------------------------------
    def init (self):    
        self.__lastTimeMsec = self.getCurTimeMsec()
        
    #-------------------------------------------------------------------------------------------------
    def getLastTimeMsec(self):
        return self.__lastTimeMsec

    #-------------------------------------------------------------------------------------------------
    def getCurTimeMsec (self):
       return long(time.time() * 1000)

    #-------------------------------------------------------------------------------------------------
    def getCurTimeSec (self):
       return long(time.time())

    #-------------------------------------------------------------------------------------------------
    def tickFromInitMsec (self):

        curTimeMsec = self.getCurTimeMsec()

        timeFromLastTickMsec = (curTimeMsec - self.__lastTimeMsec)            
        
        return timeFromLastTickMsec

    #-------------------------------------------------------------------------------------------------
    def tickFromInitSec (self):
               
        return (float(self.tickFromInitMsec())/1000.0)

    #-------------------------------------------------------------------------------------------------
    def tickFromLastMsec (self):

        curTimeMsec = self.getCurTimeMsec()

        if not self.__lastTimeMsec:
            self.__lastTimeMsec = curTimeMsec
            return 0

        timeFromLastTickMsec = (curTimeMsec - self.__lastTimeMsec)
        self.__lastTimeMsec = curTimeMsec        
        return timeFromLastTickMsec

    #-------------------------------------------------------------------------------------------------
    def tickFromLastSec (self):

        return (float(self.tickFromLastMsec())/1000.0)

    #-------------------------------------------------------------------------------------------------
    def sleepTimeFromInitSec (self, logger, maxSleepSec):

        timeFromLastTickSec = self.tickFromInitSec()
        sleepTimeoutSec = max(0,maxSleepSec - timeFromLastTickSec)

        logger("sleep-time-tick").debug5("Tick Duration (%d ms) - Sleep Timeout Interval %.4f sec", 
                                         timeFromLastTickSec*1000,sleepTimeoutSec)

        return sleepTimeoutSec

#-----------------------------------------------------------------------------------------------
class PeriodicThread(Thread):

    def __init__ (self, logger, name):
        Thread.__init__(self, name=("%s-thread" % name))
        self.daemon = True # a daemon thread - does not affect app exit

        self.__log              = logger
        self.__functor          = None
        self.__wasStopped       = False
        self.__loopSleepTimeSec = 0
        self.__numExceedThresh  = 0
        self.__maxTimeDelta     = 0
        self.__timeService      = TimesSerivce()

    def init(self, functor, loopSleepTimeSec):  
        self.__functor             = functor
        self.__loopSleepTimeSec    = loopSleepTimeSec
              
    def run(self):
        self.__log("start-periodic-thread").notice("%s: Thread has been Launched.", self.name)

        if self.__functor is None:
            a.infra.process.processFatal("%s: no task was set", self.name)
        
        while not self.__wasStopped:

            self.__timeService.init()

            try:
                self.__log("execute-run").debug4("%s: functor '%s' has been executed.", self.name, self.__functor)
                self.__functor()

            except Exception as ex:  
                a.infra.process.processFatal("%s: unexpected error for task '%s' - %s", self.name, self.__functor, ex)

            self._checkAndLog()
            
            # Calculate time to sleep
            sleepTimeoutSec = self.__timeService.sleepTimeFromInitSec(self.__log, self.__loopSleepTimeSec)
            time.sleep(sleepTimeoutSec)
        
        self.__log("terminate-periodic-thread").notice("%s: Thread has been Terminated.", self.name)

    def stop(self):
        self.__log("stop-periodic-thread").notice("%s: Thread has been Stopped.", self.name)
        self.__wasStopped = True

    def _checkAndLog (self):
        timeoutMili         = self.__loopSleepTimeSec * 1000
        timeDelta           = self.__timeService.tickFromInitMsec()
        warningTimeoutMili  = timeoutMili*2
        shouldWarn = False
        
        if timeDelta < timeoutMili:
            self.__log("check-and-log-low").debug5("%s: time delta is low. timeDelta=%s, timeoutMili=%s", 
                                                   self.name, timeDelta, timeoutMili)
        else:
            if timeDelta >= warningTimeoutMili:
                self.__numExceedThresh += 1

                if timeDelta > self.__maxTimeDelta:
                    self.__maxTimeDelta = timeDelta
                    shouldWarn = True

            if shouldWarn is True:
                self.__log("check-and-log-warning").warning("%s: time delta is above threshold. timeDelta=%s, warningTimeoutMili=%s, timeoutMili=%s, numExceedThresh=%s", 
                                                            self.name, timeDelta, warningTimeoutMili, timeoutMili, self.__numExceedThresh)
            else:
                self.__log("check-and-log-valid").debug4("%s: time delta is valid. timeDelta=%s, timeoutMili=%s", 
                                                         self.name, timeDelta, timeoutMili)
