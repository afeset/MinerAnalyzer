#!/usr/local/bin/python2.6
# 
# Copyright Qwilt, 2013
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: lenak

from datetime import datetime
import json
import os
import re
import shutil
import subprocess
import time

from a.api.yang.modules.tech.common.qwilt_tech_system_clock.tech.system.clock.clock_data_gen import ClockData
from a.api.yang.modules.tech.common.qwilt_tech_system_clock.tech.system.clock.status.status_oper_data_gen import StatusOperData
from a.infra.basic.return_codes import ReturnCodes
from a.infra.process import processFatal
from a.sys.clock.manager.time_zone_info import TimeZoneInfo
from a.sys.clock.utils.clock_utils import ClockUtils 


# Bypass for PyChecker
if  __package__ is None:
    G_NAME_MODULE_CLOCK_MANAGER = "unknown"
    G_NAME_GROUP_CLOCK_MANAGER = "unknown"
else:
    from . import G_NAME_MODULE_CLOCK_MANAGER 
    from . import G_NAME_GROUP_CLOCK_MANAGER


class ClockManagerBase(object):
    """Virtual base class of clock manager

    The correct way to use this class:
    1. Initiate an object
    2. call initTimezoneSupportedList(kSupportedTimezoneList) with the supported time zones list.
    3. call limitConfigToRunning() if the platform is mini (otherwise full operation)
    4. call createClockManager() to complete the objects initialization and readiness

    Executes processFatal() exception if object methods are called, before calling a successful createClockManager() on it

    Attributes:
        _createdObject: boolean flag which indicates whether the object was successfully created 
        _limitConfigToRunningFlag: boolean flag which indicates whether the configuration is limited only to running
        _clockDataRunningConfig: running config blinky data
        _clockDataCandidateConfig: candidate config blinky data
        _tzSupportedList: time-zones supported list
    """

    def __init__(self, logger):
        self._log = logger.createLogger(G_NAME_MODULE_CLOCK_MANAGER, G_NAME_GROUP_CLOCK_MANAGER)
        self._clockDataRunningConfig  = None
        self._clockDataCandidateConfig  = None
        self._tzSupportedList = []
        self._createdObject = False
        self._limitConfigToRunningFlag = False

    def initTimezoneSupportedList(self, inputList): 
        """Inits time-zones supported list

        Args:
            inputList: input tz list
        """
        self._tzSupportedList = inputList
        self._log("init-list").debug3("initList() called: tz supported list = %s", self._tzSupportedList)

    def limitConfigToRunning (self):
        """sets the limitConfigToRunningFlag to True
        """
        self._limitConfigToRunningFlag = True
        self._log("init-limit-config-to-runnning-called").debug3("initLimitConfigToRunningFlag() called: limitConfigToRunningFlag =%s", self._limitConfigToRunningFlag)
    

    def createClockManager (self):
        """Initialize the clock manager object

        Checks the initial configuration and sets clockDataRunningConfig

        Returns:
            ReturnCodes.kOk on success, ReturnCodes.kGeneralError otherwise (configuration file open/read wasn't successful)
        """
        self._log("create-clock-manager-called").debug3("createClockManager() called")
        (rc, currentTimeZone) = ClockUtils.s_getCurrentTimeZone(self._log, self._getConfigFile())#self.__getCurrentTimeZone()
        if rc == ReturnCodes.kOk:
            initialData = ClockData()
            initialData.timezone = currentTimeZone
            if self._isTimeZoneValid(initialData.timezone) is False:
                rc = ReturnCodes.kGeneralError
                self._log("create-clock-manager-valid-err").error("createClockManager(): current timezone=%s is not valid", currentTimeZone)
            else:
                self._createdObject = True
                self._clockDataRunningConfig  = initialData
        else:
            rc = ReturnCodes.kGeneralError
            self._log("create-clock-manager-read-current-err").error("createClockManager(): current timezone read error")
        self._log("create-clock-manager-ended").debug3("createClockManager() ended: clockDataRunningConfig=%s, return code=%s", self._clockDataRunningConfig, rc)
        return rc

    def getRunningConfig(self):
        self._log("get-running-manager-called").debug4("getRunningConfig() called: running=%s", self._clockDataRunningConfig)
        self.__crashIfNotCreated()
        return self._clockDataRunningConfig

    def getCandidateConfig(self):
        self._log("get-candidate-config-called").debug4("getCandidateConfig() called: running=%s, candidate=%s", self._clockDataRunningConfig, self._clockDataCandidateConfig)
        self.__crashIfNotCreated()
        if self._clockDataCandidateConfig is None:
            return self._clockDataRunningConfig
        else: 
            return self._clockDataCandidateConfig

    def configBeginTrx(self):
        self._log("config-begin-trx-called").debug4("configBeginTrx() called") 
        self.__crashIfNotCreated()
        self._clockDataCandidateConfig = None
        return ReturnCodes.kOk

    def setCandidate(self, inputData):
        """Sets clock data candidate

        Args: 
            inputData: candidate blinky node
        Returns:
                None if the candidate is valid, error string otherwise
        """
        self._log("set-candidate-called").debug4("setCandidate() called: input=%s", inputData) 
        self.__crashIfNotCreated()
        returnStr = None
        # check the limitConfigToRunningFlag
        if self._limitConfigToRunningFlag:
            if inputData.timezone != self._clockDataRunningConfig.timezone:
                self._log("set-time-zone-limit-config-to-running-").info("setCandidate(): limitConfigToRunningFlag is True! candidate=%s", inputData.timezone)
                returnStr = "On this platform, timezone configuration is limited to '%s'" % self._clockDataRunningConfig.timezone
        else:
            if inputData.timezone not in self._tzSupportedList:
                self._log("set-time-zone-candidate-wrong-candidate").info("setCandidate(): wrong time zone candidate, is not found in supported tz list. candidate=%s", inputData.timezone)
                returnStr = "Timezone '%s' is not supported" % (inputData.timezone)
            else:
                if not self._isTimeZoneValid(inputData.timezone):
                    self._log("set-time-zone-candidate-not-valid").warning("setCandidate(): time zone candidate is not valid. candidate=%s", inputData.timezone)
                    returnStr = "Internal error: Timezone '%s' candidate is not valid" % (inputData.timezone)
                else:
                    self._clockDataCandidateConfig = inputData
                    self._log("set-time-zone-candidate-success").debug3("setCandidate(): time zone candidate was set. candidate=%s", inputData.timezone)
        self._log("set-candidate-ended").debug4("setCandidate() ended: return value=%s", returnStr) 
        return returnStr

    def commitTrx(self):
        """Commit Transaction function

        Returns:
            ReturnCodes.kOk on success, ReturnCodes.kGeneralError otherwise
        """
        self._log("commit-trx-called").debug4("commitTrx() called: time zone candidate=%s, time zone running=%s", self._clockDataCandidateConfig, self._clockDataRunningConfig)
        self.__crashIfNotCreated()
        rc = ReturnCodes.kOk
        if self._clockDataCandidateConfig:
            if self._clockDataRunningConfig.timezone != self._clockDataCandidateConfig.timezone: 
                if ClockUtils.s_setTimezone(self._log, self._clockDataCandidateConfig.timezone, self._getConfigFile(), self._getConfigUtility()) != ReturnCodes.kOk:
                    self._log("commit-trx-failed").error("commitTrx() failed: candidate timezone=%s trx failed", self._clockDataCandidateConfig.timezone)
                    rc = ReturnCodes.kGeneralError
                else:
                    self._clockDataRunningConfig  = self._clockDataCandidateConfig
            self._clockDataCandidateConfig = None
        self._log("commit-trx-ended").debug4("commitTrx() ended: time zone candidate=%s, time zone running=%s", self._clockDataCandidateConfig, self._clockDataRunningConfig)
        return rc

    def abortTrx(self):
        self._log("abort-trx-called").debug4("abortTrx() called: time zone candidate=%s, time zone running=%s", self._clockDataCandidateConfig, self._clockDataRunningConfig)
        self.__crashIfNotCreated()
        self._clockDataCandidateConfig  = None
        return ReturnCodes.kOk
        
    def getTimeZoneInfo (self, mode, name, tzInfoList):
        """Fills the given tzInfoList with information of the requested time-zones  

        Args:
            mode: one of the following strings: 
                'current': request for the current configured time-zone information  
                'name': request for a specific time-zone information, which is specified in the name argument  
                'all': request for all supported time-zone information  
            name: in case the mode is 'name' a string which represents a time-zone, ignored otherwise
            tzInfoList: the list to be filled with requested information
        Returns:
            None on success, error string otherwise
        """

        self._log("get-time-zone-info-called").debug4("getTimeZoneInfo() called: mode=%s, name=%s, tzInfoList=%s", mode, name, tzInfoList)
        self.__crashIfNotCreated()
        requestedList = []
        computeList = []
        errString = None

        if mode == 'current':
            requestedList = [self._clockDataRunningConfig.timezone]
        elif mode == 'name':
            if name not in self._tzSupportedList:
                errString = "Timezone '%s' not supported" % name
                self._log("get-time-zone-info-wrong-name").info("getTimeZoneInfo() returned error string: %s", errString)
                return errString
            else:
                requestedList = [name]
        elif mode == 'all':
            requestedList = self._tzSupportedList
        else: # wrong mode
            errString = "Internal error: getTimeZoneInfo() called with invalid mode '%s'" % mode
            self._log("get-time-zone-info-syntax-error-mode").error("getTimeZoneInfo() returned error string: no such mode, mode=%s", mode)
            return errString

        for requested in requestedList:
            if self._isTimeZoneValid(requested): #check time zone validity
                computeList.append(requested)
            else:
                tzInfoList.append(TimeZoneInfo(requested)) #time zone is not valid - TimeZoneInfo.valid flag is False
        
        rc = self.__fillTimeZoneInfoList (computeList, tzInfoList)

        if rc != ReturnCodes.kOk:
            errString = "Internal error: Error in retrieving timezone info"

        self._log("get-time-zone-info-ended").debug4("getTimeZoneInfo() ended: return string=%s", errString)
        return errString
     

    def getObjectStatus(self, dpTrxContext, operData):  
        """Fills the given blinky operational data   
    
        The function has a retry mechanism. The reason is to support the case that while this fuction in being evaluated, some other process changes the timezone configuration. 
        Three retries are made in case of a data mismatch that cased by this senario. 

        Args:
            dpTrxContext: ?
            operData: the given operational data to be filled
        Returns:
            ReturnCodes.kOk on success, ReturnCodes.kGeneralError otherwise
        """
        self._log("get-object-status-called").debug4("getObjectStatus() called: dpTrxContext=%s, operData=%s", dpTrxContext, operData)
        self.__crashIfNotCreated()

        rc = ReturnCodes.kGeneralError
        retryNumber = 4
        while retryNumber > 0 and rc != ReturnCodes.kOk:
            time.tzset() # to refresh the rules used by the module!!! 
            epoch = self._getEpoch()
            try:
                dtLocal = datetime.fromtimestamp(epoch)
                dtUtc = datetime.utcfromtimestamp(epoch)
                tzName = time.strftime('%Z')
            except ValueError as e:
                self._log("get-object-status-error").error("getObjectStatus(): raised an exception=%e, dpTrxContext=%s, operData=%s, epoch=%s", e, dpTrxContext, operData, epoch)
                return ReturnCodes.kGeneralError 
            
            rc1, localOutString = self.__getTimeString(dtLocal, tzName)
            if rc1 != ReturnCodes.kOk: #exception was raised
                self._log("get-object-status-error").error("getObjectStatus(): __getTimeString() call returned an error. dtLocal=%s tzName=%s epoch=%s", dtLocal, tzName, epoch)
                return ReturnCodes.kGeneralError 
    
            rc2, utcOutString = self.__getTimeString(dtUtc, 'UTC')
            if rc2 != ReturnCodes.kOk: #exception was raised
                self._log("get-object-status-error").error("getObjectStatus(): __getTimeString() call returned an error. dtUtc=%s tzName=%s epoch=%s", dtUtc, tzName, epoch)
                return ReturnCodes.kGeneralError 
    
            rc = self.__setDayLightSavingTimeAndOffset(tzName, operData)
            retryNumber -= 1

        if rc != ReturnCodes.kOk:
            self._log("get-object-status-name-error").error("getObjectStatus(): not suitable timezone name=%s, time.tzname=%s ", tzName, time.tzname)
            return ReturnCodes.kGeneralError

        operData.setEpoch(int(round(epoch)))
        operData.setLocalTimeString(localOutString)
        operData.setUtcTimeString(utcOutString)

        self._log("getObjectStatus-ended").debug4("getObjectStatus() ended: operData=%s", operData)
        return rc
    
    def __crashIfNotCreated (self):
        """Checks that the object was created successfully. If not calls processFatal
        """
        if not self._createdObject:
            processFatal("performing operation on uninitialize clockManager object")

    def __setDayLightSavingTimeAndOffset (self, tzName, operData):
        """Sets the dayLightSavingTime and offset fields in blinky oper data

        Args:
            tzName: current timezone abbreviation
            operData: blinky oper data to be updated
        Returns:
            ReturnCodes.kOk on success, ReturnCodes.kGeneralError otherwise
        """
        rc = ReturnCodes.kOk
        if (time.daylight != 0) and (time.localtime().tm_isdst == 1): #dst
            offset = self.__getOffset(time.altzone, 'dst', tzName)
            operData.setDaylightSavingTime(True)
            operData.setUtcOffsetMinutes(offset)
            self._log("set-daylight-saving-time-and-offset").debug4("__setDayLightSavingTimeAndOffset(): dst time: timezone name=%s, time.tzname[1]=%s, offset=%s ", tzName, time.tzname[1], offset)
        else: #standard-time
            offset = self.__getOffset(time.timezone, 'standard', tzName)
            operData.setDaylightSavingTime(False)
            operData.setUtcOffsetMinutes(offset)
            self._log("set-daylight-saving-time-and-offset").debug4("__setDayLightSavingTimeAndOffset(): standard time: timezone name=%s, time.tzname[0]=%s, offset=%s ", tzName, time.tzname[0], offset)
        return rc


    def __getTimeString (self, dt, tzStr):
        """Prepares the appropriate time string  

        Args:
            dt: datetime object
            tzStr: a string with the relevant timezone abbreviation
        Returns:
            the prepared time string
        """
        milli = int(round(dt.microsecond/1000.0))

        try:
            timeStr = dt.strftime('%H:%M:%S') + '.' + str(milli)
            dateStr = dt.strftime('%a %b %d %Y') 
        except ValueError as e:
            self._log("get-time-string-error").error("__getTimeString(): raised an exception=%e, datetime=%s, timezoneName=%s", e, dt, tzStr)
            return (ReturnCodes.kGeneralError, None)
        
        return (ReturnCodes.kOk, timeStr + ' ' + tzStr + ' ' + dateStr)


    def __fillTimeZoneInfoList (self, computeList, tzInfoList):
        """Private function that fills the tzInfoList with information of the computeList time-zones  
        
        Create a child process which is responsible for the core computation. The parent and child process communicate via pipe.
        Main child computation is done in  __childComputeTimeZoneInfo() function

        Args:
            computeList: the needed to compute time-zone list
            tzInfoList: the output TimeZoneInfo output list
        Returns:
            ReturnCodes.kOk on success, ReturnCodes.kGeneralError otherwise
        """

        self._log("fill-timezone-info-list-called").debug4("fillTimeZoneInfoList() called: computeList=%s, tzInfoList=%s", computeList, tzInfoList)
        rc = ReturnCodes.kOk
        if len(computeList) > 0: #check if any computation is needed
            rPipe, wPipe = os.pipe() #first, create a pipe
            rPipe, wPipe = os.fdopen(rPipe, 'r', 0) , os.fdopen(wPipe, 'w', 0)
            try:
                pid = os.fork() #secondly, execute fork()
            except OSError as e:
                self._log("fill-timezone-info-list-fork-error").error("__fillTimeZoneInfoList() - fork() raised OSError exception=%s", e)
                rc = ReturnCodes.kGeneralError
            else:
                if pid: # parent process
                    self._log("fill-timezone-info-list-parent-process").debug4("__fillTimeZoneInfoList() parent process continued after fork")
                    wPipe.close()
                    out = rPipe.read()
                    rPipe.close()
                    try:
                        childReturnCode = os.waitpid(pid, 0)[1]
                    except OSError as e:
                        self._log("fill-timezone-info-list-waitpid-error").error("__fillTimeZoneInfoList() - waitpid() raised OSError exception = %s", e)
                        rc = ReturnCodes.kGeneralError
                    else:
                        if childReturnCode:
                            self._log("fill-timezone-info-list-child-proc-err").error("__fillTimeZoneInfoList() - child process retured an err: %s", childReturnCode)
                            rc = ReturnCodes.kGeneralError
                        else:
                            outList = json.loads(out)
                            for dic in outList:
                                tzInfo = TimeZoneInfo()
                                tzInfo.loadFromDict(dic)
                                tzInfoList.append(tzInfo)
                else: # child proc
                    self._log("fill-time-zoneinfo-list-child-process").debug4("__fillTimeZoneInfoList() child process started")
                    rPipe.close()
                    wPipe.write(json.dumps(self.__childComputeTimeZoneInfo(computeList)))
                    wPipe.close()
                    os._exit(0)                    
        self._log("fill-time-zone-info-list-ended").debug4("fillTimeZoneInfoList() ended: rc=%s", rc)
        return rc

    def __getOffset(self, offsetInSeconds, offsetType, timezone):
        """Calcs the offset in minutes
        
        Args:
            offsetInseconds: the offset in seconds
            offsetType: 'standard' / 'dst' string
            timezone: the time zone name 
        Returns:
            The offset in minutes
        """
        if offsetInSeconds % 60 != 0: 
           self._log("get-offset-not-round-hour").warning("__getOffset() - timezone=%s %s offset isn't in round minutes, offset in seconds=%s", timezone, offsetType, offsetInSeconds)
        return  -offsetInSeconds / 60


    def __childComputeTimeZoneInfo (self, computeList):
        """Private function which gather the information for all time-zone within computeList   
        
        This function is run by a child process of the main application process and this is due to the fact that it chenges the TZ enviroment variable, thus it can not be done in the parent process.
        
        Args:
            computeList: the needed to compute time-zone list
        Returns:
            A list of the dictionaries, each dictionary represent a TimeZoneInfo object. 
        """
        
        self._log("child-compute-time-zone-info-called").debug4("__childComputeTimeZoneInfo() called: computeList=%s", computeList)
        outList = []
        for name in computeList:
            tzInfo = TimeZoneInfo(name)
            os.environ['TZ'] = tzInfo.name
            time.tzset()
            tzInfo.standardAbbr = time.tzname[0]
            tzInfo.standardOffset = self.__getOffset(time.timezone, 'standard', tzInfo.name)
               
            if time.daylight != 0:
                tzInfo.dstAbbr = time.tzname[1] 
                tzInfo.dstOffset = self.__getOffset(time.altzone, 'dst', tzInfo.name)

            tzInfo.validData = True
            outList.append(tzInfo.dumpToDict())
        self._log("child-compute-time-zone-info-ended").debug4("__childComputeTimeZoneInfo() ended: outList=%s", outList)
        return outList

    def _getConfigFile (self):
        """virtual function which returns the timezone configuration file path
    
        Should be implemented in the derived classes. Raises a NotImplementedError exception if called on a base object
        """

        raise NotImplementedError()

    def _getConfigUtility (self):
        """virtual function which returns the timezone configuration utility
    
        Should be implemented in the derived classes. Raises a NotImplementedError exception if called on a base object
        """

        raise NotImplementedError()
     
    def _isTimeZoneValid(self, timeZoneName):
        """virtual function which checks whether the requested timezone is valid
    
        Args:
            timeZoneName: requested timezone name
        Returns:
            Boolean value: True if valid, False otherwise
        """

        __pychecker__ = 'no-argsused'
        raise NotImplementedError()

    def _getEpoch(self):
        """virtual function which returns the epoch
    
        Returns:
            epoch
        """

        raise NotImplementedError()

    def __str__ (self):
        return "created=" + str(self._createdObject) + "limitConfigToRunningFlag=" + str(self._limitConfigToRunningFlag) + "supported list=" + str(self._tzSupportedList) + "\nrunning=" + str(self._clockDataRunningConfig) + "\ncandidate=" +str(self._clockDataCandidateConfig)
        

    


