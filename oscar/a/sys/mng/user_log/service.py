# 
# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: nirs

if  __package__ is None:
    G_NAME_MODULE_SYS_USER_LOG = "unknown"
    G_NAME_GROUP_SYS_USER_LOG_SERVICE = "unknown"
else:
    from . import G_NAME_MODULE_SYS_USER_LOG 
    from . import G_NAME_GROUP_SYS_USER_LOG_SERVICE 

import log_infra
import include.a.sys.mng.user_log.msg_data_pb2

class Service:

    SEVERITY_EMERGENCY = 0
    SEVERITY_ALERT = 1
    SEVERITY_CRITICAL = 2
    SEVERITY_ERROR = 3
    SEVERITY_WARNING = 4
    SEVERITY_NOTIFICATION = 5
    SEVERITY_INFORMATIONAL = 6
    SEVERITY_DEBUGGING = 7
    
    _VALID_SEVERITY = [SEVERITY_EMERGENCY, 
                       SEVERITY_ALERT,
                       SEVERITY_CRITICAL,
                       SEVERITY_ERROR,
                       SEVERITY_WARNING,
                       SEVERITY_NOTIFICATION,
                       SEVERITY_INFORMATIONAL,
                       SEVERITY_DEBUGGING]


    OSEF_KEY = "user-log-service"
    CAPTAIN_CLIENT_NAME = "user-log-service"

    def __init__ (self, logger):
        self._targetInfraLog = None
        self._log = logger.createLogger(G_NAME_MODULE_SYS_USER_LOG, G_NAME_GROUP_SYS_USER_LOG_SERVICE)

    def initCaptain (self, captain):
        self._captain = captain

    def captainClient_addToOsef (self):
        self._log("add-to-osef").debug3("adding service to osef")
        self._captain.getOsef()[self.OSEF_KEY] = self

    def captainClient_getFromOsef (self):
        self._targetInfraLog = log_infra.LogInfra.s_getFromOsefUnsafe(self._captain.getOsef())
        if self._targetInfraLog is None:
            self._log("get-infra-log-none").debug2("got 'None' infra logger from osef")
        else:
            self._log("get-infra-log").debug2("got infra logger from osef")
            self._targetInfraLog = self._targetInfraLog.getLoggerManager().createLogger("user-log", "service")
        
    def log(self,
            severity, 
            category, group, code,                          
            msgText,
            timeOfDayGmtNanoseconds, timeOfDayGmtOffsetMinutes,
            processName, processId):

        if not severity in self._VALID_SEVERITY:
            self._log("invalid-severity").error("invalid user log message severity: %s. Failed to log %s-%s-%s: %s", 
                                                severity, category, group, code, msgText)
            return

        msgDataGpb = include.a.sys.mng.user_log.msg_data_pb2.MsgDataGpb()
        msgDataGpb.mySeverity                  = severity
        msgDataGpb.myCategory                  = category
        msgDataGpb.myGroup                     = group
        msgDataGpb.myCode                      = code
        msgDataGpb.myBody                      = msgText
        msgDataGpb.myTimeOfDayGmtNanoseconds   = timeOfDayGmtNanoseconds
        msgDataGpb.myTimeOfDayGmtOffsetMinutes = timeOfDayGmtOffsetMinutes
        msgDataGpb.myProcessName               = processName
        msgDataGpb.myProcessId                 = processId
       
        self._log("user-log-message").notice("got user log message for %s-%s-%d-%s: %s", 
                                             category, group, severity, code, msgText, gpbs = msgDataGpb)

        if self._targetInfraLog is None:
            self._log("no-logger").error("Failed to send log message to user log - no infra logger. %s-%s-%d-%s: %s", 
                                         category, group, severity, code, msgText)
            return

        self._targetInfraLog("msg").notice("",gpbs = msgDataGpb)


    @classmethod
    def s_getFromOsefUnsafe (cls, osef):
        if not cls.OSEF_KEY in osef:
            return None
        return osef[cls.OSEF_KEY]





