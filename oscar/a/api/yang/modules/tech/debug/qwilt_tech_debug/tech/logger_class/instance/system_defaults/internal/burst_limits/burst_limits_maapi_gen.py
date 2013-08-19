


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes
from a.infra.misc.init_guard import InitGuard

from a.sys.confd.pyconfdlib.tag_values import TagValues
from a.sys.confd.pyconfdlib.value import Value
from a.sys.confd.pyconfdlib.key_path import KeyPath

from burst_limits_maapi_base_gen import BurstLimitsMaapiBase




class BlinkyBurstLimitsMaapi(BurstLimitsMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-burstLimits")
        self.domain = None

        

        
        self.infoDropLevelRequested = False
        self.infoDropLevel = None
        self.infoDropLevelSet = False
        
        self.debug2DropLevelRequested = False
        self.debug2DropLevel = None
        self.debug2DropLevelSet = False
        
        self.noticeDropLevelRequested = False
        self.noticeDropLevel = None
        self.noticeDropLevelSet = False
        
        self.debug5DropLevelRequested = False
        self.debug5DropLevel = None
        self.debug5DropLevelSet = False
        
        self.warningDropLevelRequested = False
        self.warningDropLevel = None
        self.warningDropLevelSet = False
        
        self.alertDropLevelRequested = False
        self.alertDropLevel = None
        self.alertDropLevelSet = False
        
        self.debug3DropLevelRequested = False
        self.debug3DropLevel = None
        self.debug3DropLevelSet = False
        
        self.emergencyDropLevelRequested = False
        self.emergencyDropLevel = None
        self.emergencyDropLevelSet = False
        
        self.debug4DropLevelRequested = False
        self.debug4DropLevel = None
        self.debug4DropLevelSet = False
        
        self.debug1DropLevelRequested = False
        self.debug1DropLevel = None
        self.debug1DropLevelSet = False
        
        self.criticalDropLevelRequested = False
        self.criticalDropLevel = None
        self.criticalDropLevelSet = False
        
        self.burstMaxRequested = False
        self.burstMax = None
        self.burstMaxSet = False
        
        self.errorDropLevelRequested = False
        self.errorDropLevel = None
        self.errorDropLevelSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestInfoDropLevel(True)
        
        self.requestDebug2DropLevel(True)
        
        self.requestNoticeDropLevel(True)
        
        self.requestDebug5DropLevel(True)
        
        self.requestWarningDropLevel(True)
        
        self.requestAlertDropLevel(True)
        
        self.requestDebug3DropLevel(True)
        
        self.requestEmergencyDropLevel(True)
        
        self.requestDebug4DropLevel(True)
        
        self.requestDebug1DropLevel(True)
        
        self.requestCriticalDropLevel(True)
        
        self.requestBurstMax(True)
        
        self.requestErrorDropLevel(True)
        
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestInfoDropLevel(True)
        
        self.requestDebug2DropLevel(True)
        
        self.requestNoticeDropLevel(True)
        
        self.requestDebug5DropLevel(True)
        
        self.requestWarningDropLevel(True)
        
        self.requestAlertDropLevel(True)
        
        self.requestDebug3DropLevel(True)
        
        self.requestEmergencyDropLevel(True)
        
        self.requestDebug4DropLevel(True)
        
        self.requestDebug1DropLevel(True)
        
        self.requestCriticalDropLevel(True)
        
        self.requestBurstMax(True)
        
        self.requestErrorDropLevel(True)
        
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestInfoDropLevel(False)
        
        self.requestDebug2DropLevel(False)
        
        self.requestNoticeDropLevel(False)
        
        self.requestDebug5DropLevel(False)
        
        self.requestWarningDropLevel(False)
        
        self.requestAlertDropLevel(False)
        
        self.requestDebug3DropLevel(False)
        
        self.requestEmergencyDropLevel(False)
        
        self.requestDebug4DropLevel(False)
        
        self.requestDebug1DropLevel(False)
        
        self.requestCriticalDropLevel(False)
        
        self.requestBurstMax(False)
        
        self.requestErrorDropLevel(False)
        
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestInfoDropLevel(False)
        
        self.requestDebug2DropLevel(False)
        
        self.requestNoticeDropLevel(False)
        
        self.requestDebug5DropLevel(False)
        
        self.requestWarningDropLevel(False)
        
        self.requestAlertDropLevel(False)
        
        self.requestDebug3DropLevel(False)
        
        self.requestEmergencyDropLevel(False)
        
        self.requestDebug4DropLevel(False)
        
        self.requestDebug1DropLevel(False)
        
        self.requestCriticalDropLevel(False)
        
        self.requestBurstMax(False)
        
        self.requestErrorDropLevel(False)
        
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setInfoDropLevel(None)
        self.infoDropLevelSet = False
        
        self.setDebug2DropLevel(None)
        self.debug2DropLevelSet = False
        
        self.setNoticeDropLevel(None)
        self.noticeDropLevelSet = False
        
        self.setDebug5DropLevel(None)
        self.debug5DropLevelSet = False
        
        self.setWarningDropLevel(None)
        self.warningDropLevelSet = False
        
        self.setAlertDropLevel(None)
        self.alertDropLevelSet = False
        
        self.setDebug3DropLevel(None)
        self.debug3DropLevelSet = False
        
        self.setEmergencyDropLevel(None)
        self.emergencyDropLevelSet = False
        
        self.setDebug4DropLevel(None)
        self.debug4DropLevelSet = False
        
        self.setDebug1DropLevel(None)
        self.debug1DropLevelSet = False
        
        self.setCriticalDropLevel(None)
        self.criticalDropLevelSet = False
        
        self.setBurstMax(None)
        self.burstMaxSet = False
        
        self.setErrorDropLevel(None)
        self.errorDropLevelSet = False
        
        

    def write (self
              , loggerClass
              , instance
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(loggerClass, instance, trxContext)

    def read (self
              , loggerClass
              , instance
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(loggerClass, instance, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , loggerClass
                       , instance
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(loggerClass, instance, 
                                  True,
                                  trxContext)



    def requestInfoDropLevel (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-infodroplevel').debug3Func(): logFunc('called. requested=%s', requested)
        self.infoDropLevelRequested = requested
        self.infoDropLevelSet = False

    def isInfoDropLevelRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-infodroplevel-requested').debug3Func(): logFunc('called. requested=%s', self.infoDropLevelRequested)
        return self.infoDropLevelRequested

    def getInfoDropLevel (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-infodroplevel').debug3Func(): logFunc('called. self.infoDropLevelSet=%s, self.infoDropLevel=%s', self.infoDropLevelSet, self.infoDropLevel)
        if self.infoDropLevelSet:
            return self.infoDropLevel
        return None

    def hasInfoDropLevel (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-infodroplevel').debug3Func(): logFunc('called. self.infoDropLevelSet=%s, self.infoDropLevel=%s', self.infoDropLevelSet, self.infoDropLevel)
        if self.infoDropLevelSet:
            return True
        return False

    def setInfoDropLevel (self, infoDropLevel):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-infodroplevel').debug3Func(): logFunc('called. infoDropLevel=%s, old=%s', infoDropLevel, self.infoDropLevel)
        self.infoDropLevelSet = True
        self.infoDropLevel = infoDropLevel

    def requestDebug2DropLevel (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-debug2droplevel').debug3Func(): logFunc('called. requested=%s', requested)
        self.debug2DropLevelRequested = requested
        self.debug2DropLevelSet = False

    def isDebug2DropLevelRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-debug2droplevel-requested').debug3Func(): logFunc('called. requested=%s', self.debug2DropLevelRequested)
        return self.debug2DropLevelRequested

    def getDebug2DropLevel (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-debug2droplevel').debug3Func(): logFunc('called. self.debug2DropLevelSet=%s, self.debug2DropLevel=%s', self.debug2DropLevelSet, self.debug2DropLevel)
        if self.debug2DropLevelSet:
            return self.debug2DropLevel
        return None

    def hasDebug2DropLevel (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-debug2droplevel').debug3Func(): logFunc('called. self.debug2DropLevelSet=%s, self.debug2DropLevel=%s', self.debug2DropLevelSet, self.debug2DropLevel)
        if self.debug2DropLevelSet:
            return True
        return False

    def setDebug2DropLevel (self, debug2DropLevel):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-debug2droplevel').debug3Func(): logFunc('called. debug2DropLevel=%s, old=%s', debug2DropLevel, self.debug2DropLevel)
        self.debug2DropLevelSet = True
        self.debug2DropLevel = debug2DropLevel

    def requestNoticeDropLevel (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-noticedroplevel').debug3Func(): logFunc('called. requested=%s', requested)
        self.noticeDropLevelRequested = requested
        self.noticeDropLevelSet = False

    def isNoticeDropLevelRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-noticedroplevel-requested').debug3Func(): logFunc('called. requested=%s', self.noticeDropLevelRequested)
        return self.noticeDropLevelRequested

    def getNoticeDropLevel (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-noticedroplevel').debug3Func(): logFunc('called. self.noticeDropLevelSet=%s, self.noticeDropLevel=%s', self.noticeDropLevelSet, self.noticeDropLevel)
        if self.noticeDropLevelSet:
            return self.noticeDropLevel
        return None

    def hasNoticeDropLevel (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-noticedroplevel').debug3Func(): logFunc('called. self.noticeDropLevelSet=%s, self.noticeDropLevel=%s', self.noticeDropLevelSet, self.noticeDropLevel)
        if self.noticeDropLevelSet:
            return True
        return False

    def setNoticeDropLevel (self, noticeDropLevel):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-noticedroplevel').debug3Func(): logFunc('called. noticeDropLevel=%s, old=%s', noticeDropLevel, self.noticeDropLevel)
        self.noticeDropLevelSet = True
        self.noticeDropLevel = noticeDropLevel

    def requestDebug5DropLevel (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-debug5droplevel').debug3Func(): logFunc('called. requested=%s', requested)
        self.debug5DropLevelRequested = requested
        self.debug5DropLevelSet = False

    def isDebug5DropLevelRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-debug5droplevel-requested').debug3Func(): logFunc('called. requested=%s', self.debug5DropLevelRequested)
        return self.debug5DropLevelRequested

    def getDebug5DropLevel (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-debug5droplevel').debug3Func(): logFunc('called. self.debug5DropLevelSet=%s, self.debug5DropLevel=%s', self.debug5DropLevelSet, self.debug5DropLevel)
        if self.debug5DropLevelSet:
            return self.debug5DropLevel
        return None

    def hasDebug5DropLevel (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-debug5droplevel').debug3Func(): logFunc('called. self.debug5DropLevelSet=%s, self.debug5DropLevel=%s', self.debug5DropLevelSet, self.debug5DropLevel)
        if self.debug5DropLevelSet:
            return True
        return False

    def setDebug5DropLevel (self, debug5DropLevel):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-debug5droplevel').debug3Func(): logFunc('called. debug5DropLevel=%s, old=%s', debug5DropLevel, self.debug5DropLevel)
        self.debug5DropLevelSet = True
        self.debug5DropLevel = debug5DropLevel

    def requestWarningDropLevel (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-warningdroplevel').debug3Func(): logFunc('called. requested=%s', requested)
        self.warningDropLevelRequested = requested
        self.warningDropLevelSet = False

    def isWarningDropLevelRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-warningdroplevel-requested').debug3Func(): logFunc('called. requested=%s', self.warningDropLevelRequested)
        return self.warningDropLevelRequested

    def getWarningDropLevel (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-warningdroplevel').debug3Func(): logFunc('called. self.warningDropLevelSet=%s, self.warningDropLevel=%s', self.warningDropLevelSet, self.warningDropLevel)
        if self.warningDropLevelSet:
            return self.warningDropLevel
        return None

    def hasWarningDropLevel (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-warningdroplevel').debug3Func(): logFunc('called. self.warningDropLevelSet=%s, self.warningDropLevel=%s', self.warningDropLevelSet, self.warningDropLevel)
        if self.warningDropLevelSet:
            return True
        return False

    def setWarningDropLevel (self, warningDropLevel):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-warningdroplevel').debug3Func(): logFunc('called. warningDropLevel=%s, old=%s', warningDropLevel, self.warningDropLevel)
        self.warningDropLevelSet = True
        self.warningDropLevel = warningDropLevel

    def requestAlertDropLevel (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-alertdroplevel').debug3Func(): logFunc('called. requested=%s', requested)
        self.alertDropLevelRequested = requested
        self.alertDropLevelSet = False

    def isAlertDropLevelRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-alertdroplevel-requested').debug3Func(): logFunc('called. requested=%s', self.alertDropLevelRequested)
        return self.alertDropLevelRequested

    def getAlertDropLevel (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-alertdroplevel').debug3Func(): logFunc('called. self.alertDropLevelSet=%s, self.alertDropLevel=%s', self.alertDropLevelSet, self.alertDropLevel)
        if self.alertDropLevelSet:
            return self.alertDropLevel
        return None

    def hasAlertDropLevel (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-alertdroplevel').debug3Func(): logFunc('called. self.alertDropLevelSet=%s, self.alertDropLevel=%s', self.alertDropLevelSet, self.alertDropLevel)
        if self.alertDropLevelSet:
            return True
        return False

    def setAlertDropLevel (self, alertDropLevel):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-alertdroplevel').debug3Func(): logFunc('called. alertDropLevel=%s, old=%s', alertDropLevel, self.alertDropLevel)
        self.alertDropLevelSet = True
        self.alertDropLevel = alertDropLevel

    def requestDebug3DropLevel (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-debug3droplevel').debug3Func(): logFunc('called. requested=%s', requested)
        self.debug3DropLevelRequested = requested
        self.debug3DropLevelSet = False

    def isDebug3DropLevelRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-debug3droplevel-requested').debug3Func(): logFunc('called. requested=%s', self.debug3DropLevelRequested)
        return self.debug3DropLevelRequested

    def getDebug3DropLevel (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-debug3droplevel').debug3Func(): logFunc('called. self.debug3DropLevelSet=%s, self.debug3DropLevel=%s', self.debug3DropLevelSet, self.debug3DropLevel)
        if self.debug3DropLevelSet:
            return self.debug3DropLevel
        return None

    def hasDebug3DropLevel (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-debug3droplevel').debug3Func(): logFunc('called. self.debug3DropLevelSet=%s, self.debug3DropLevel=%s', self.debug3DropLevelSet, self.debug3DropLevel)
        if self.debug3DropLevelSet:
            return True
        return False

    def setDebug3DropLevel (self, debug3DropLevel):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-debug3droplevel').debug3Func(): logFunc('called. debug3DropLevel=%s, old=%s', debug3DropLevel, self.debug3DropLevel)
        self.debug3DropLevelSet = True
        self.debug3DropLevel = debug3DropLevel

    def requestEmergencyDropLevel (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-emergencydroplevel').debug3Func(): logFunc('called. requested=%s', requested)
        self.emergencyDropLevelRequested = requested
        self.emergencyDropLevelSet = False

    def isEmergencyDropLevelRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-emergencydroplevel-requested').debug3Func(): logFunc('called. requested=%s', self.emergencyDropLevelRequested)
        return self.emergencyDropLevelRequested

    def getEmergencyDropLevel (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-emergencydroplevel').debug3Func(): logFunc('called. self.emergencyDropLevelSet=%s, self.emergencyDropLevel=%s', self.emergencyDropLevelSet, self.emergencyDropLevel)
        if self.emergencyDropLevelSet:
            return self.emergencyDropLevel
        return None

    def hasEmergencyDropLevel (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-emergencydroplevel').debug3Func(): logFunc('called. self.emergencyDropLevelSet=%s, self.emergencyDropLevel=%s', self.emergencyDropLevelSet, self.emergencyDropLevel)
        if self.emergencyDropLevelSet:
            return True
        return False

    def setEmergencyDropLevel (self, emergencyDropLevel):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-emergencydroplevel').debug3Func(): logFunc('called. emergencyDropLevel=%s, old=%s', emergencyDropLevel, self.emergencyDropLevel)
        self.emergencyDropLevelSet = True
        self.emergencyDropLevel = emergencyDropLevel

    def requestDebug4DropLevel (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-debug4droplevel').debug3Func(): logFunc('called. requested=%s', requested)
        self.debug4DropLevelRequested = requested
        self.debug4DropLevelSet = False

    def isDebug4DropLevelRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-debug4droplevel-requested').debug3Func(): logFunc('called. requested=%s', self.debug4DropLevelRequested)
        return self.debug4DropLevelRequested

    def getDebug4DropLevel (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-debug4droplevel').debug3Func(): logFunc('called. self.debug4DropLevelSet=%s, self.debug4DropLevel=%s', self.debug4DropLevelSet, self.debug4DropLevel)
        if self.debug4DropLevelSet:
            return self.debug4DropLevel
        return None

    def hasDebug4DropLevel (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-debug4droplevel').debug3Func(): logFunc('called. self.debug4DropLevelSet=%s, self.debug4DropLevel=%s', self.debug4DropLevelSet, self.debug4DropLevel)
        if self.debug4DropLevelSet:
            return True
        return False

    def setDebug4DropLevel (self, debug4DropLevel):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-debug4droplevel').debug3Func(): logFunc('called. debug4DropLevel=%s, old=%s', debug4DropLevel, self.debug4DropLevel)
        self.debug4DropLevelSet = True
        self.debug4DropLevel = debug4DropLevel

    def requestDebug1DropLevel (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-debug1droplevel').debug3Func(): logFunc('called. requested=%s', requested)
        self.debug1DropLevelRequested = requested
        self.debug1DropLevelSet = False

    def isDebug1DropLevelRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-debug1droplevel-requested').debug3Func(): logFunc('called. requested=%s', self.debug1DropLevelRequested)
        return self.debug1DropLevelRequested

    def getDebug1DropLevel (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-debug1droplevel').debug3Func(): logFunc('called. self.debug1DropLevelSet=%s, self.debug1DropLevel=%s', self.debug1DropLevelSet, self.debug1DropLevel)
        if self.debug1DropLevelSet:
            return self.debug1DropLevel
        return None

    def hasDebug1DropLevel (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-debug1droplevel').debug3Func(): logFunc('called. self.debug1DropLevelSet=%s, self.debug1DropLevel=%s', self.debug1DropLevelSet, self.debug1DropLevel)
        if self.debug1DropLevelSet:
            return True
        return False

    def setDebug1DropLevel (self, debug1DropLevel):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-debug1droplevel').debug3Func(): logFunc('called. debug1DropLevel=%s, old=%s', debug1DropLevel, self.debug1DropLevel)
        self.debug1DropLevelSet = True
        self.debug1DropLevel = debug1DropLevel

    def requestCriticalDropLevel (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-criticaldroplevel').debug3Func(): logFunc('called. requested=%s', requested)
        self.criticalDropLevelRequested = requested
        self.criticalDropLevelSet = False

    def isCriticalDropLevelRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-criticaldroplevel-requested').debug3Func(): logFunc('called. requested=%s', self.criticalDropLevelRequested)
        return self.criticalDropLevelRequested

    def getCriticalDropLevel (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-criticaldroplevel').debug3Func(): logFunc('called. self.criticalDropLevelSet=%s, self.criticalDropLevel=%s', self.criticalDropLevelSet, self.criticalDropLevel)
        if self.criticalDropLevelSet:
            return self.criticalDropLevel
        return None

    def hasCriticalDropLevel (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-criticaldroplevel').debug3Func(): logFunc('called. self.criticalDropLevelSet=%s, self.criticalDropLevel=%s', self.criticalDropLevelSet, self.criticalDropLevel)
        if self.criticalDropLevelSet:
            return True
        return False

    def setCriticalDropLevel (self, criticalDropLevel):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-criticaldroplevel').debug3Func(): logFunc('called. criticalDropLevel=%s, old=%s', criticalDropLevel, self.criticalDropLevel)
        self.criticalDropLevelSet = True
        self.criticalDropLevel = criticalDropLevel

    def requestBurstMax (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-burstmax').debug3Func(): logFunc('called. requested=%s', requested)
        self.burstMaxRequested = requested
        self.burstMaxSet = False

    def isBurstMaxRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-burstmax-requested').debug3Func(): logFunc('called. requested=%s', self.burstMaxRequested)
        return self.burstMaxRequested

    def getBurstMax (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-burstmax').debug3Func(): logFunc('called. self.burstMaxSet=%s, self.burstMax=%s', self.burstMaxSet, self.burstMax)
        if self.burstMaxSet:
            return self.burstMax
        return None

    def hasBurstMax (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-burstmax').debug3Func(): logFunc('called. self.burstMaxSet=%s, self.burstMax=%s', self.burstMaxSet, self.burstMax)
        if self.burstMaxSet:
            return True
        return False

    def setBurstMax (self, burstMax):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-burstmax').debug3Func(): logFunc('called. burstMax=%s, old=%s', burstMax, self.burstMax)
        self.burstMaxSet = True
        self.burstMax = burstMax

    def requestErrorDropLevel (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-errordroplevel').debug3Func(): logFunc('called. requested=%s', requested)
        self.errorDropLevelRequested = requested
        self.errorDropLevelSet = False

    def isErrorDropLevelRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-errordroplevel-requested').debug3Func(): logFunc('called. requested=%s', self.errorDropLevelRequested)
        return self.errorDropLevelRequested

    def getErrorDropLevel (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-errordroplevel').debug3Func(): logFunc('called. self.errorDropLevelSet=%s, self.errorDropLevel=%s', self.errorDropLevelSet, self.errorDropLevel)
        if self.errorDropLevelSet:
            return self.errorDropLevel
        return None

    def hasErrorDropLevel (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-errordroplevel').debug3Func(): logFunc('called. self.errorDropLevelSet=%s, self.errorDropLevel=%s', self.errorDropLevelSet, self.errorDropLevel)
        if self.errorDropLevelSet:
            return True
        return False

    def setErrorDropLevel (self, errorDropLevel):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-errordroplevel').debug3Func(): logFunc('called. errorDropLevel=%s, old=%s', errorDropLevel, self.errorDropLevel)
        self.errorDropLevelSet = True
        self.errorDropLevel = errorDropLevel


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.infoDropLevel = 0
        self.infoDropLevelSet = False
        
        self.debug2DropLevel = 0
        self.debug2DropLevelSet = False
        
        self.noticeDropLevel = 0
        self.noticeDropLevelSet = False
        
        self.debug5DropLevel = 0
        self.debug5DropLevelSet = False
        
        self.warningDropLevel = 0
        self.warningDropLevelSet = False
        
        self.alertDropLevel = 0
        self.alertDropLevelSet = False
        
        self.debug3DropLevel = 0
        self.debug3DropLevelSet = False
        
        self.emergencyDropLevel = 0
        self.emergencyDropLevelSet = False
        
        self.debug4DropLevel = 0
        self.debug4DropLevelSet = False
        
        self.debug1DropLevel = 0
        self.debug1DropLevelSet = False
        
        self.criticalDropLevel = 0
        self.criticalDropLevelSet = False
        
        self.burstMax = 0
        self.burstMaxSet = False
        
        self.errorDropLevel = 0
        self.errorDropLevelSet = False
        

    def _getSelfKeyPath (self, loggerClass
                         , instance
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("burst-limits", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("internal", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(instance);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("instance", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(loggerClass);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("logger-class", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        loggerClass, 
                        instance, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(loggerClass, 
                                         instance, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(loggerClass, 
                                       instance, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       loggerClass, 
                       instance, 
                       
                       readAllOrFail,
                       trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-read').debug3Func(): logFunc('called. PARAMS, readAllOrFail=%s', readAllOrFail)

        if readAllOrFail:
            self._clearAllReadData()

        tagValueList = TagValues()

        res = self._fillReadTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-fill-read-tag-value-failed').errorFunc(): logFunc('_fillReadTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(loggerClass, 
                                       instance, 
                                       
                                       None)

        res = self.domain.readMaapi(tagValueList, keyPath, trxContext)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-domain-failed').errorFunc(): logFunc('domain.readMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        res = self._readTagValues(tagValueList, readAllOrFail)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-read-tag-values-failed').errorFunc(): logFunc('_readTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-read-done').debug3Func(): logFunc('done. PARAMS, readAllOrFail=%s', readAllOrFail)
        return ReturnCodes.kOk

    def _collectItemsToDelete (self,
                               loggerClass, 
                               instance, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasInfoDropLevel():
            valInfoDropLevel = Value()
            if self.infoDropLevel is not None:
                valInfoDropLevel.setInt64(self.infoDropLevel)
            else:
                valInfoDropLevel.setEmpty()
            tagValueList.push(("info-drop-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valInfoDropLevel)
        
        if self.hasDebug2DropLevel():
            valDebug2DropLevel = Value()
            if self.debug2DropLevel is not None:
                valDebug2DropLevel.setInt64(self.debug2DropLevel)
            else:
                valDebug2DropLevel.setEmpty()
            tagValueList.push(("debug2-drop-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valDebug2DropLevel)
        
        if self.hasNoticeDropLevel():
            valNoticeDropLevel = Value()
            if self.noticeDropLevel is not None:
                valNoticeDropLevel.setInt64(self.noticeDropLevel)
            else:
                valNoticeDropLevel.setEmpty()
            tagValueList.push(("notice-drop-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valNoticeDropLevel)
        
        if self.hasDebug5DropLevel():
            valDebug5DropLevel = Value()
            if self.debug5DropLevel is not None:
                valDebug5DropLevel.setInt64(self.debug5DropLevel)
            else:
                valDebug5DropLevel.setEmpty()
            tagValueList.push(("debug5-drop-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valDebug5DropLevel)
        
        if self.hasWarningDropLevel():
            valWarningDropLevel = Value()
            if self.warningDropLevel is not None:
                valWarningDropLevel.setInt64(self.warningDropLevel)
            else:
                valWarningDropLevel.setEmpty()
            tagValueList.push(("warning-drop-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valWarningDropLevel)
        
        if self.hasAlertDropLevel():
            valAlertDropLevel = Value()
            if self.alertDropLevel is not None:
                valAlertDropLevel.setInt64(self.alertDropLevel)
            else:
                valAlertDropLevel.setEmpty()
            tagValueList.push(("alert-drop-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valAlertDropLevel)
        
        if self.hasDebug3DropLevel():
            valDebug3DropLevel = Value()
            if self.debug3DropLevel is not None:
                valDebug3DropLevel.setInt64(self.debug3DropLevel)
            else:
                valDebug3DropLevel.setEmpty()
            tagValueList.push(("debug3-drop-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valDebug3DropLevel)
        
        if self.hasEmergencyDropLevel():
            valEmergencyDropLevel = Value()
            if self.emergencyDropLevel is not None:
                valEmergencyDropLevel.setInt64(self.emergencyDropLevel)
            else:
                valEmergencyDropLevel.setEmpty()
            tagValueList.push(("emergency-drop-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valEmergencyDropLevel)
        
        if self.hasDebug4DropLevel():
            valDebug4DropLevel = Value()
            if self.debug4DropLevel is not None:
                valDebug4DropLevel.setInt64(self.debug4DropLevel)
            else:
                valDebug4DropLevel.setEmpty()
            tagValueList.push(("debug4-drop-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valDebug4DropLevel)
        
        if self.hasDebug1DropLevel():
            valDebug1DropLevel = Value()
            if self.debug1DropLevel is not None:
                valDebug1DropLevel.setInt64(self.debug1DropLevel)
            else:
                valDebug1DropLevel.setEmpty()
            tagValueList.push(("debug1-drop-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valDebug1DropLevel)
        
        if self.hasCriticalDropLevel():
            valCriticalDropLevel = Value()
            if self.criticalDropLevel is not None:
                valCriticalDropLevel.setInt64(self.criticalDropLevel)
            else:
                valCriticalDropLevel.setEmpty()
            tagValueList.push(("critical-drop-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valCriticalDropLevel)
        
        if self.hasBurstMax():
            valBurstMax = Value()
            if self.burstMax is not None:
                valBurstMax.setInt64(self.burstMax)
            else:
                valBurstMax.setEmpty()
            tagValueList.push(("burst-max", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valBurstMax)
        
        if self.hasErrorDropLevel():
            valErrorDropLevel = Value()
            if self.errorDropLevel is not None:
                valErrorDropLevel.setInt64(self.errorDropLevel)
            else:
                valErrorDropLevel.setEmpty()
            tagValueList.push(("error-drop-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valErrorDropLevel)
        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isInfoDropLevelRequested():
            valInfoDropLevel = Value()
            valInfoDropLevel.setEmpty()
            tagValueList.push(("info-drop-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valInfoDropLevel)
        
        if self.isDebug2DropLevelRequested():
            valDebug2DropLevel = Value()
            valDebug2DropLevel.setEmpty()
            tagValueList.push(("debug2-drop-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valDebug2DropLevel)
        
        if self.isNoticeDropLevelRequested():
            valNoticeDropLevel = Value()
            valNoticeDropLevel.setEmpty()
            tagValueList.push(("notice-drop-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valNoticeDropLevel)
        
        if self.isDebug5DropLevelRequested():
            valDebug5DropLevel = Value()
            valDebug5DropLevel.setEmpty()
            tagValueList.push(("debug5-drop-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valDebug5DropLevel)
        
        if self.isWarningDropLevelRequested():
            valWarningDropLevel = Value()
            valWarningDropLevel.setEmpty()
            tagValueList.push(("warning-drop-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valWarningDropLevel)
        
        if self.isAlertDropLevelRequested():
            valAlertDropLevel = Value()
            valAlertDropLevel.setEmpty()
            tagValueList.push(("alert-drop-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valAlertDropLevel)
        
        if self.isDebug3DropLevelRequested():
            valDebug3DropLevel = Value()
            valDebug3DropLevel.setEmpty()
            tagValueList.push(("debug3-drop-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valDebug3DropLevel)
        
        if self.isEmergencyDropLevelRequested():
            valEmergencyDropLevel = Value()
            valEmergencyDropLevel.setEmpty()
            tagValueList.push(("emergency-drop-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valEmergencyDropLevel)
        
        if self.isDebug4DropLevelRequested():
            valDebug4DropLevel = Value()
            valDebug4DropLevel.setEmpty()
            tagValueList.push(("debug4-drop-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valDebug4DropLevel)
        
        if self.isDebug1DropLevelRequested():
            valDebug1DropLevel = Value()
            valDebug1DropLevel.setEmpty()
            tagValueList.push(("debug1-drop-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valDebug1DropLevel)
        
        if self.isCriticalDropLevelRequested():
            valCriticalDropLevel = Value()
            valCriticalDropLevel.setEmpty()
            tagValueList.push(("critical-drop-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valCriticalDropLevel)
        
        if self.isBurstMaxRequested():
            valBurstMax = Value()
            valBurstMax.setEmpty()
            tagValueList.push(("burst-max", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valBurstMax)
        
        if self.isErrorDropLevelRequested():
            valErrorDropLevel = Value()
            valErrorDropLevel.setEmpty()
            tagValueList.push(("error-drop-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valErrorDropLevel)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isInfoDropLevelRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "info-drop-level") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-infodroplevel').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "infoDropLevel", "info-drop-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-info-drop-level-bad-value').infoFunc(): logFunc('infoDropLevel not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setInfoDropLevel(tempVar)
            for logFunc in self._log('read-tag-values-info-drop-level').debug3Func(): logFunc('read infoDropLevel. infoDropLevel=%s, tempValue=%s', self.infoDropLevel, tempValue.getType())
        
        if self.isDebug2DropLevelRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "debug2-drop-level") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-debug2droplevel').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "debug2DropLevel", "debug2-drop-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-debug2-drop-level-bad-value').infoFunc(): logFunc('debug2DropLevel not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setDebug2DropLevel(tempVar)
            for logFunc in self._log('read-tag-values-debug2-drop-level').debug3Func(): logFunc('read debug2DropLevel. debug2DropLevel=%s, tempValue=%s', self.debug2DropLevel, tempValue.getType())
        
        if self.isNoticeDropLevelRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "notice-drop-level") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-noticedroplevel').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "noticeDropLevel", "notice-drop-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-notice-drop-level-bad-value').infoFunc(): logFunc('noticeDropLevel not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setNoticeDropLevel(tempVar)
            for logFunc in self._log('read-tag-values-notice-drop-level').debug3Func(): logFunc('read noticeDropLevel. noticeDropLevel=%s, tempValue=%s', self.noticeDropLevel, tempValue.getType())
        
        if self.isDebug5DropLevelRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "debug5-drop-level") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-debug5droplevel').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "debug5DropLevel", "debug5-drop-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-debug5-drop-level-bad-value').infoFunc(): logFunc('debug5DropLevel not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setDebug5DropLevel(tempVar)
            for logFunc in self._log('read-tag-values-debug5-drop-level').debug3Func(): logFunc('read debug5DropLevel. debug5DropLevel=%s, tempValue=%s', self.debug5DropLevel, tempValue.getType())
        
        if self.isWarningDropLevelRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "warning-drop-level") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-warningdroplevel').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "warningDropLevel", "warning-drop-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-warning-drop-level-bad-value').infoFunc(): logFunc('warningDropLevel not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setWarningDropLevel(tempVar)
            for logFunc in self._log('read-tag-values-warning-drop-level').debug3Func(): logFunc('read warningDropLevel. warningDropLevel=%s, tempValue=%s', self.warningDropLevel, tempValue.getType())
        
        if self.isAlertDropLevelRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "alert-drop-level") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-alertdroplevel').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "alertDropLevel", "alert-drop-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-alert-drop-level-bad-value').infoFunc(): logFunc('alertDropLevel not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setAlertDropLevel(tempVar)
            for logFunc in self._log('read-tag-values-alert-drop-level').debug3Func(): logFunc('read alertDropLevel. alertDropLevel=%s, tempValue=%s', self.alertDropLevel, tempValue.getType())
        
        if self.isDebug3DropLevelRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "debug3-drop-level") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-debug3droplevel').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "debug3DropLevel", "debug3-drop-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-debug3-drop-level-bad-value').infoFunc(): logFunc('debug3DropLevel not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setDebug3DropLevel(tempVar)
            for logFunc in self._log('read-tag-values-debug3-drop-level').debug3Func(): logFunc('read debug3DropLevel. debug3DropLevel=%s, tempValue=%s', self.debug3DropLevel, tempValue.getType())
        
        if self.isEmergencyDropLevelRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "emergency-drop-level") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-emergencydroplevel').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "emergencyDropLevel", "emergency-drop-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-emergency-drop-level-bad-value').infoFunc(): logFunc('emergencyDropLevel not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setEmergencyDropLevel(tempVar)
            for logFunc in self._log('read-tag-values-emergency-drop-level').debug3Func(): logFunc('read emergencyDropLevel. emergencyDropLevel=%s, tempValue=%s', self.emergencyDropLevel, tempValue.getType())
        
        if self.isDebug4DropLevelRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "debug4-drop-level") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-debug4droplevel').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "debug4DropLevel", "debug4-drop-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-debug4-drop-level-bad-value').infoFunc(): logFunc('debug4DropLevel not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setDebug4DropLevel(tempVar)
            for logFunc in self._log('read-tag-values-debug4-drop-level').debug3Func(): logFunc('read debug4DropLevel. debug4DropLevel=%s, tempValue=%s', self.debug4DropLevel, tempValue.getType())
        
        if self.isDebug1DropLevelRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "debug1-drop-level") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-debug1droplevel').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "debug1DropLevel", "debug1-drop-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-debug1-drop-level-bad-value').infoFunc(): logFunc('debug1DropLevel not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setDebug1DropLevel(tempVar)
            for logFunc in self._log('read-tag-values-debug1-drop-level').debug3Func(): logFunc('read debug1DropLevel. debug1DropLevel=%s, tempValue=%s', self.debug1DropLevel, tempValue.getType())
        
        if self.isCriticalDropLevelRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "critical-drop-level") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-criticaldroplevel').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "criticalDropLevel", "critical-drop-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-critical-drop-level-bad-value').infoFunc(): logFunc('criticalDropLevel not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setCriticalDropLevel(tempVar)
            for logFunc in self._log('read-tag-values-critical-drop-level').debug3Func(): logFunc('read criticalDropLevel. criticalDropLevel=%s, tempValue=%s', self.criticalDropLevel, tempValue.getType())
        
        if self.isBurstMaxRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "burst-max") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-burstmax').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "burstMax", "burst-max", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-burst-max-bad-value').infoFunc(): logFunc('burstMax not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setBurstMax(tempVar)
            for logFunc in self._log('read-tag-values-burst-max').debug3Func(): logFunc('read burstMax. burstMax=%s, tempValue=%s', self.burstMax, tempValue.getType())
        
        if self.isErrorDropLevelRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "error-drop-level") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-errordroplevel').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "errorDropLevel", "error-drop-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-error-drop-level-bad-value').infoFunc(): logFunc('errorDropLevel not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setErrorDropLevel(tempVar)
            for logFunc in self._log('read-tag-values-error-drop-level').debug3Func(): logFunc('read errorDropLevel. errorDropLevel=%s, tempValue=%s', self.errorDropLevel, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "burstLimits", 
        "namespace": "burst_limits", 
        "className": "BurstLimitsMaapi", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.system_defaults.internal.burst_limits.burst_limits_maapi_gen import BurstLimitsMaapi", 
        "baseClassName": "BurstLimitsMaapiBase", 
        "baseModule": "burst_limits_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "qt", 
            "yangName": "tech", 
            "namespace": "tech", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech", 
            "name": "tech"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-debug", 
            "isCurrent": false, 
            "yangName": "logger-class", 
            "namespace": "logger_class", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "keyLeaf": {
                "varName": "loggerClass", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "logger-class"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-debug", 
            "isCurrent": false, 
            "yangName": "instance", 
            "namespace": "instance", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "keyLeaf": {
                "varName": "instance", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "instance"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-debug", 
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "name": "system-defaults"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-debug", 
            "yangName": "internal", 
            "namespace": "internal", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "name": "internal"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-debug", 
            "yangName": "burst-limits", 
            "namespace": "burst_limits", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "name": "burst-limits"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "infoDropLevel", 
            "yangName": "info-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "debug2DropLevel", 
            "yangName": "debug2-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "noticeDropLevel", 
            "yangName": "notice-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "debug5DropLevel", 
            "yangName": "debug5-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "warningDropLevel", 
            "yangName": "warning-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "alertDropLevel", 
            "yangName": "alert-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "debug3DropLevel", 
            "yangName": "debug3-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "emergencyDropLevel", 
            "yangName": "emergency-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "debug4DropLevel", 
            "yangName": "debug4-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "debug1DropLevel", 
            "yangName": "debug1-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "criticalDropLevel", 
            "yangName": "critical-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "burstMax", 
            "yangName": "burst-max", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "errorDropLevel", 
            "yangName": "error-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }
    ], 
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "debug", 
            "qwilt_tech_debug"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "infoDropLevel", 
            "yangName": "info-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "debug2DropLevel", 
            "yangName": "debug2-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "noticeDropLevel", 
            "yangName": "notice-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "debug5DropLevel", 
            "yangName": "debug5-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "warningDropLevel", 
            "yangName": "warning-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "alertDropLevel", 
            "yangName": "alert-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "debug3DropLevel", 
            "yangName": "debug3-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "emergencyDropLevel", 
            "yangName": "emergency-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "debug4DropLevel", 
            "yangName": "debug4-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "debug1DropLevel", 
            "yangName": "debug1-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "criticalDropLevel", 
            "yangName": "critical-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "burstMax", 
            "yangName": "burst-max", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "errorDropLevel", 
            "yangName": "error-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


