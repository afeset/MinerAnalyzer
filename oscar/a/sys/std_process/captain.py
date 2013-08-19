#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

if  __package__ is None:
    G_NAME_MODULE_SYS_STD_PROCESS = "unknown"
    G_NAME_GROUP_SYS_STD_PROCESS_CAPTAIN = "unknown"
else:
    from . import G_NAME_MODULE_SYS_STD_PROCESS 
    from . import G_NAME_GROUP_SYS_STD_PROCESS_CAPTAIN

import os
import time
import a.infra.process.captain
import a.sys.mng.user_log.service
import a.sys.platform_basic.platform_basic
import a.sys.boot.utils
import a.sys.ipc.simple

class Captain(a.infra.process.captain.Captain):
    
    INIT_PARAM_DATA_IPC_SERVER_PATH = "ipc-server-path"
    INIT_PARAM_DATA_IPC_SERVER_JOIN_TIMEOUT = "ipc-server-join-timeout"

    #init param dicts    
    INIT_PARAM_DICT_KEY_PLATFORM_BASIC_DATA = "platform-basic-data"
    INIT_PARAM_DICT_KEY_BOOT_UTILS = "boot-utils"

    #simple IPC strings
    SIMPLE_IPC_COMMAND_NAME_BACKTRACE_ALL_THREADS = "backtrace-all-threads"
    SIMPLE_IPC_IN_DICT_KEY_BACKTRACE_ALL_THREADS_TO_LOG = "to-log"
    SIMPLE_IPC_IN_DICT_KEY_BACKTRACE_ALL_THREADS_TO_STDERR = "to-stderr"


    def __init__ (self, processName = None, earlyLogLevel = None, initParamFilesDirEnvVar = None, kickNumber=None): 
        """ctor - see parent for discription
        """
        a.infra.process.captain.Captain.__init__(self, processName, earlyLogLevel, initParamFilesDirEnvVar, kickNumber)     
        self._userLogService = None
        self._platformBasicData = None
        self._ipcServer = None
        self._ipcServerJoinTimout = 0

    def _createClients (self):
        a.infra.process.captain.Captain._createClients(self)
        self._platformBasicData = a.sys.platform_basic.platform_basic.PlatformBasic(self._log)
        self._platformBasicData.initCaptain(self)
        self._addClient("platform-basic-data", self._platformBasicData)
        bootUtils = a.sys.boot.utils.BootUtils(self._log)
        bootUtils.initCaptain(self)
        self._addClient("boot-utils", bootUtils)

    def captainClient_getFromOsef (self):
        a.infra.process.captain.Captain.captainClient_getFromOsef(self)
        self._userLogService = a.sys.mng.user_log.service.Service.s_getFromOsefUnsafe(self.getOsef())  
        
    def _captainClient_initFromParamFile (self, initParamData):
        a.infra.process.captain.Captain._captainClient_initFromParamFile(self, initParamData)
        self._ipcServer = a.sys.ipc.simple.Server(self._log, "captain-%s"%self._processName, 
                                                  initParamData[self.INIT_PARAM_DATA_IPC_SERVER_PATH])
        self._ipcServerJoinTimout = initParamData[self.INIT_PARAM_DATA_IPC_SERVER_JOIN_TIMEOUT]
        def backtraceAllThreads (inputData):
            self.__backtraceAllThreads(inputData[self.SIMPLE_IPC_IN_DICT_KEY_BACKTRACE_ALL_THREADS_TO_STDERR], 
                                       inputData[self.SIMPLE_IPC_IN_DICT_KEY_BACKTRACE_ALL_THREADS_TO_LOG])

        self._ipcServer.initAddCommand(self.SIMPLE_IPC_COMMAND_NAME_BACKTRACE_ALL_THREADS, backtraceAllThreads)
        self._ipcServer.init()

    def captainClient_dormant2Passive (self):
        a.infra.process.captain.Captain.captainClient_dormant2Passive(self)
        self._ipcServer.start()

    def captainClient_passive2Dormant (self):
        a.infra.process.captain.Captain.captainClient_passive2Dormant(self)
        self._ipcServer.stop()
        self._ipcServer.join(self._ipcServerJoinTimout)

    def logUserMessage (self, userLogMessage):
        """create a user message log message
        """
        (isValid, msgText) = self._verifyUserMessage(userLogMessage)
        if not isValid:
            return

        severity = None
        if userLogMessage.severity == a.api.user_log.msg.message_base.MessageBase.EMERGENCY:
            severity = a.sys.mng.user_log.service.Service.SEVERITY_EMERGENCY
        elif userLogMessage.severity == a.api.user_log.msg.message_base.MessageBase.ALERT:
            severity = a.sys.mng.user_log.service.Service.SEVERITY_ALERT
        elif userLogMessage.severity == a.api.user_log.msg.message_base.MessageBase.CRITICAL:
            severity = a.sys.mng.user_log.service.Service.SEVERITY_CRITICAL
        elif userLogMessage.severity == a.api.user_log.msg.message_base.MessageBase.ERROR:
            severity = a.sys.mng.user_log.service.Service.SEVERITY_ERROR
        elif userLogMessage.severity == a.api.user_log.msg.message_base.MessageBase.WARNING:
            severity = a.sys.mng.user_log.service.Service.SEVERITY_WARNING
        elif userLogMessage.severity == a.api.user_log.msg.message_base.MessageBase.NOTIFICATION:
            severity = a.sys.mng.user_log.service.Service.SEVERITY_NOTIFICATION
        elif userLogMessage.severity == a.api.user_log.msg.message_base.MessageBase.INFORMATIONAL:
            severity = a.sys.mng.user_log.service.Service.SEVERITY_INFORMATIONAL
        elif userLogMessage.severity == a.api.user_log.msg.message_base.MessageBase.DEBUGGING:
            severity = a.sys.mng.user_log.service.Service.SEVERITY_DEBUGGING

        if severity is None:
            self._log("invalid-user-log-severity").error("invalid user log message severity: %s. Failed to log %s-%s-%s: %s", 
                                                         userLogMessage.severity, userLogMessage.category, userLogMessage.group, userLogMessage.code, msgText)

        if not userLogMessage.getIsActive():
            self._log("user-log-message-not-impl").error("sending a user log message marked as not implemented: %s-%s-%s-%s", 
                                                         userLogMessage.category, userLogMessage.group, 
                                                         userLogMessage.severity, userLogMessage.code)

        processName = self._processName
        if processName is None:
            self._log("user-log-missing-process-name").warning("creating a user log message with no process name availble")
            processName = "N/A"

        timeOfDayGmt = time.time()
        timeOfDayGmtNanoseconds = long(timeOfDayGmt * 1000 * 1000 * 1000)

        if time.localtime(timeOfDayGmt).tm_isdst and time.daylight:
            gmtOffset = -time.altzone
        else:
            gmtOffset = -time.timezone

        timeOfDayGmtOffsetMinutes = gmtOffset/60
        

        if self._userLogService is None:
            self._log("no-user-log-service").error("trying to log user message with no existing user log service:  %s-%s-%d-%s: %s",
                                                   userLogMessage.category, userLogMessage.group, severity, userLogMessage.code, msgText)
            return

        self._userLogService.log(severity, 
                                 userLogMessage.category, userLogMessage.group, userLogMessage.code,                          
                                 msgText,
                                 timeOfDayGmtNanoseconds, timeOfDayGmtOffsetMinutes,
                                 processName, os.getpid())
        


        


    def getPlatformBasicData (self):   
        return self._platformBasicData

    @classmethod
    def s_createInitParamFiles(cls, dbglog, initParamFilesDir, dictionary):
        a.infra.process.captain.Captain.s_infraCaptainCreateInitParamFiles(dbglog, initParamFilesDir, dictionary)
        a.sys.platform_basic.platform_basic.PlatformBasic.s_createInitParamFile(dbglog, initParamFilesDir, dictionary[cls.INIT_PARAM_DICT_KEY_PLATFORM_BASIC_DATA])
        a.sys.boot.utils.BootUtils.s_createInitParamFile(dbglog, initParamFilesDir, dictionary[cls.INIT_PARAM_DICT_KEY_BOOT_UTILS])

