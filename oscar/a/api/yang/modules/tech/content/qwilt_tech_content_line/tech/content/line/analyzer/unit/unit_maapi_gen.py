


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

from unit_maapi_base_gen import UnitMaapiBase

from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.analyzer.unit.logging.logging_maapi_gen import BlinkyLoggingMaapi
from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.analyzer.unit.vip.vip_maapi_gen import BlinkyVipMaapi
from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.analyzer.unit.system_defaults.system_defaults_maapi_gen import BlinkySystemDefaultsMaapi

from a.api.yang.modules.tech.content.qwilt_tech_content_line.qwilt_tech_content_line_module_gen import AnalyzerUnitModeType


class BlinkyUnitMaapi(UnitMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-unit")
        self.domain = None

        
        self.loggingObj = None
        
        self.vipObj = None
        
        self.systemDefaultsObj = None
        

        
        self.threadAffinityRequested = False
        self.threadAffinity = None
        self.threadAffinitySet = False
        
        self.nameRequested = False
        self.name = None
        self.nameSet = False
        
        self.idleSleepMsecRequested = False
        self.idleSleepMsec = None
        self.idleSleepMsecSet = False
        
        self.enabledRequested = False
        self.enabled = None
        self.enabledSet = False
        
        self.threadPriorityRequested = False
        self.threadPriority = None
        self.threadPrioritySet = False
        
        self.modeRequested = False
        self.mode = None
        self.modeSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestThreadAffinity(True)
        
        self.requestName(True)
        
        self.requestIdleSleepMsec(True)
        
        self.requestEnabled(True)
        
        self.requestThreadPriority(True)
        
        self.requestMode(True)
        
        
        
        if not self.loggingObj:
            self.loggingObj = self.newLogging()
            self.loggingObj.requestConfigAndOper()
        
        if not self.vipObj:
            self.vipObj = self.newVip()
            self.vipObj.requestConfigAndOper()
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestThreadAffinity(True)
        
        self.requestName(True)
        
        self.requestIdleSleepMsec(True)
        
        self.requestEnabled(True)
        
        self.requestThreadPriority(True)
        
        self.requestMode(True)
        
        
        
        if not self.loggingObj:
            self.loggingObj = self.newLogging()
            self.loggingObj.requestConfig()
        
        if not self.vipObj:
            self.vipObj = self.newVip()
            self.vipObj.requestConfig()
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestThreadAffinity(False)
        
        self.requestName(False)
        
        self.requestIdleSleepMsec(False)
        
        self.requestEnabled(False)
        
        self.requestThreadPriority(False)
        
        self.requestMode(False)
        
        
        
        if not self.loggingObj:
            self.loggingObj = self.newLogging()
            self.loggingObj.requestOper()
        
        if not self.vipObj:
            self.vipObj = self.newVip()
            self.vipObj.requestOper()
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestThreadAffinity(False)
        
        self.requestName(False)
        
        self.requestIdleSleepMsec(False)
        
        self.requestEnabled(False)
        
        self.requestThreadPriority(False)
        
        self.requestMode(False)
        
        
        
        if not self.loggingObj:
            self.loggingObj = self.newLogging()
            self.loggingObj.clearAllRequested()
        
        if not self.vipObj:
            self.vipObj = self.newVip()
            self.vipObj.clearAllRequested()
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setThreadAffinity(None)
        self.threadAffinitySet = False
        
        self.setName(None)
        self.nameSet = False
        
        self.setIdleSleepMsec(None)
        self.idleSleepMsecSet = False
        
        self.setEnabled(None)
        self.enabledSet = False
        
        self.setThreadPriority(None)
        self.threadPrioritySet = False
        
        self.setMode(None)
        self.modeSet = False
        
        
        if self.loggingObj:
            self.loggingObj.clearAllSet()
        
        if self.vipObj:
            self.vipObj.clearAllSet()
        
        if self.systemDefaultsObj:
            self.systemDefaultsObj.clearAllSet()
        

    def write (self
              , line
              , unit
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(line, unit, trxContext)

    def read (self
              , line
              , unit
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(line, unit, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , line
                       , unit
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(line, unit, 
                                  True,
                                  trxContext)

    def newLogging (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-logging').debug3Func(): logFunc('called.')
        logging = BlinkyLoggingMaapi(self._log)
        logging.init(self.domain)
        return logging

    def setLoggingObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-logging').debug3Func(): logFunc('called. obj=%s', obj)
        self.loggingObj = obj

    def getLoggingObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-logging').debug3Func(): logFunc('called. self.loggingObj=%s', self.loggingObj)
        return self.loggingObj

    def hasLogging (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-logging').debug3Func(): logFunc('called. self.loggingObj=%s', self.loggingObj)
        if self.loggingObj:
            return True
        return False

    def newVip (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-vip').debug3Func(): logFunc('called.')
        vip = BlinkyVipMaapi(self._log)
        vip.init(self.domain)
        return vip

    def setVipObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-vip').debug3Func(): logFunc('called. obj=%s', obj)
        self.vipObj = obj

    def getVipObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-vip').debug3Func(): logFunc('called. self.vipObj=%s', self.vipObj)
        return self.vipObj

    def hasVip (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-vip').debug3Func(): logFunc('called. self.vipObj=%s', self.vipObj)
        if self.vipObj:
            return True
        return False

    def newSystemDefaults (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-systemdefaults').debug3Func(): logFunc('called.')
        systemDefaults = BlinkySystemDefaultsMaapi(self._log)
        systemDefaults.init(self.domain)
        return systemDefaults

    def setSystemDefaultsObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-systemdefaults').debug3Func(): logFunc('called. obj=%s', obj)
        self.systemDefaultsObj = obj

    def getSystemDefaultsObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-systemdefaults').debug3Func(): logFunc('called. self.systemDefaultsObj=%s', self.systemDefaultsObj)
        return self.systemDefaultsObj

    def hasSystemDefaults (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-systemdefaults').debug3Func(): logFunc('called. self.systemDefaultsObj=%s', self.systemDefaultsObj)
        if self.systemDefaultsObj:
            return True
        return False



    def requestThreadAffinity (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-threadaffinity').debug3Func(): logFunc('called. requested=%s', requested)
        self.threadAffinityRequested = requested
        self.threadAffinitySet = False

    def isThreadAffinityRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-threadaffinity-requested').debug3Func(): logFunc('called. requested=%s', self.threadAffinityRequested)
        return self.threadAffinityRequested

    def getThreadAffinity (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-threadaffinity').debug3Func(): logFunc('called. self.threadAffinitySet=%s, self.threadAffinity=%s', self.threadAffinitySet, self.threadAffinity)
        if self.threadAffinitySet:
            return self.threadAffinity
        return None

    def hasThreadAffinity (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-threadaffinity').debug3Func(): logFunc('called. self.threadAffinitySet=%s, self.threadAffinity=%s', self.threadAffinitySet, self.threadAffinity)
        if self.threadAffinitySet:
            return True
        return False

    def setThreadAffinity (self, threadAffinity):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-threadaffinity').debug3Func(): logFunc('called. threadAffinity=%s, old=%s', threadAffinity, self.threadAffinity)
        self.threadAffinitySet = True
        self.threadAffinity = threadAffinity

    def requestName (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-name').debug3Func(): logFunc('called. requested=%s', requested)
        self.nameRequested = requested
        self.nameSet = False

    def isNameRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-name-requested').debug3Func(): logFunc('called. requested=%s', self.nameRequested)
        return self.nameRequested

    def getName (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-name').debug3Func(): logFunc('called. self.nameSet=%s, self.name=%s', self.nameSet, self.name)
        if self.nameSet:
            return self.name
        return None

    def hasName (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-name').debug3Func(): logFunc('called. self.nameSet=%s, self.name=%s', self.nameSet, self.name)
        if self.nameSet:
            return True
        return False

    def setName (self, name):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-name').debug3Func(): logFunc('called. name=%s, old=%s', name, self.name)
        self.nameSet = True
        self.name = name

    def requestIdleSleepMsec (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-idlesleepmsec').debug3Func(): logFunc('called. requested=%s', requested)
        self.idleSleepMsecRequested = requested
        self.idleSleepMsecSet = False

    def isIdleSleepMsecRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-idlesleepmsec-requested').debug3Func(): logFunc('called. requested=%s', self.idleSleepMsecRequested)
        return self.idleSleepMsecRequested

    def getIdleSleepMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-idlesleepmsec').debug3Func(): logFunc('called. self.idleSleepMsecSet=%s, self.idleSleepMsec=%s', self.idleSleepMsecSet, self.idleSleepMsec)
        if self.idleSleepMsecSet:
            return self.idleSleepMsec
        return None

    def hasIdleSleepMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-idlesleepmsec').debug3Func(): logFunc('called. self.idleSleepMsecSet=%s, self.idleSleepMsec=%s', self.idleSleepMsecSet, self.idleSleepMsec)
        if self.idleSleepMsecSet:
            return True
        return False

    def setIdleSleepMsec (self, idleSleepMsec):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-idlesleepmsec').debug3Func(): logFunc('called. idleSleepMsec=%s, old=%s', idleSleepMsec, self.idleSleepMsec)
        self.idleSleepMsecSet = True
        self.idleSleepMsec = idleSleepMsec

    def requestEnabled (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-enabled').debug3Func(): logFunc('called. requested=%s', requested)
        self.enabledRequested = requested
        self.enabledSet = False

    def isEnabledRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-enabled-requested').debug3Func(): logFunc('called. requested=%s', self.enabledRequested)
        return self.enabledRequested

    def getEnabled (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-enabled').debug3Func(): logFunc('called. self.enabledSet=%s, self.enabled=%s', self.enabledSet, self.enabled)
        if self.enabledSet:
            return self.enabled
        return None

    def hasEnabled (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-enabled').debug3Func(): logFunc('called. self.enabledSet=%s, self.enabled=%s', self.enabledSet, self.enabled)
        if self.enabledSet:
            return True
        return False

    def setEnabled (self, enabled):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-enabled').debug3Func(): logFunc('called. enabled=%s, old=%s', enabled, self.enabled)
        self.enabledSet = True
        self.enabled = enabled

    def requestThreadPriority (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-threadpriority').debug3Func(): logFunc('called. requested=%s', requested)
        self.threadPriorityRequested = requested
        self.threadPrioritySet = False

    def isThreadPriorityRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-threadpriority-requested').debug3Func(): logFunc('called. requested=%s', self.threadPriorityRequested)
        return self.threadPriorityRequested

    def getThreadPriority (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-threadpriority').debug3Func(): logFunc('called. self.threadPrioritySet=%s, self.threadPriority=%s', self.threadPrioritySet, self.threadPriority)
        if self.threadPrioritySet:
            return self.threadPriority
        return None

    def hasThreadPriority (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-threadpriority').debug3Func(): logFunc('called. self.threadPrioritySet=%s, self.threadPriority=%s', self.threadPrioritySet, self.threadPriority)
        if self.threadPrioritySet:
            return True
        return False

    def setThreadPriority (self, threadPriority):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-threadpriority').debug3Func(): logFunc('called. threadPriority=%s, old=%s', threadPriority, self.threadPriority)
        self.threadPrioritySet = True
        self.threadPriority = threadPriority

    def requestMode (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-mode').debug3Func(): logFunc('called. requested=%s', requested)
        self.modeRequested = requested
        self.modeSet = False

    def isModeRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-mode-requested').debug3Func(): logFunc('called. requested=%s', self.modeRequested)
        return self.modeRequested

    def getMode (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-mode').debug3Func(): logFunc('called. self.modeSet=%s, self.mode=%s', self.modeSet, self.mode)
        if self.modeSet:
            return self.mode
        return None

    def hasMode (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-mode').debug3Func(): logFunc('called. self.modeSet=%s, self.mode=%s', self.modeSet, self.mode)
        if self.modeSet:
            return True
        return False

    def setMode (self, mode):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-mode').debug3Func(): logFunc('called. mode=%s, old=%s', mode, self.mode)
        self.modeSet = True
        self.mode = mode


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.loggingObj:
            self.loggingObj._clearAllReadData()
        
        if self.vipObj:
            self.vipObj._clearAllReadData()
        
        if self.systemDefaultsObj:
            self.systemDefaultsObj._clearAllReadData()
        

        
        self.threadAffinity = 0
        self.threadAffinitySet = False
        
        self.name = 0
        self.nameSet = False
        
        self.idleSleepMsec = 0
        self.idleSleepMsecSet = False
        
        self.enabled = 0
        self.enabledSet = False
        
        self.threadPriority = 0
        self.threadPrioritySet = False
        
        self.mode = 0
        self.modeSet = False
        

    def _getSelfKeyPath (self, line
                         , unit
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        ancestorVal = Value()
        ancestorVal.setString(unit);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("unit", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("analyzer", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(line);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("line", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("content", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        line, 
                        unit, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(line, 
                                         unit, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(line, 
                                       unit, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       line, 
                       unit, 
                       
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

        keyPath = self._getSelfKeyPath(line, 
                                       unit, 
                                       
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
                               line, 
                               unit, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        
        if self.loggingObj:
            res = self.loggingObj._collectItemsToDelete(line, 
                                                                          unit, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-logging-failed').errorFunc(): logFunc('loggingObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.vipObj:
            res = self.vipObj._collectItemsToDelete(line, 
                                                                          unit, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-vip-failed').errorFunc(): logFunc('vipObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.systemDefaultsObj:
            res = self.systemDefaultsObj._collectItemsToDelete(line, 
                                                                          unit, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasThreadAffinity():
            valThreadAffinity = Value()
            if self.threadAffinity is not None:
                valThreadAffinity.setString(self.threadAffinity)
            else:
                valThreadAffinity.setEmpty()
            tagValueList.push(("thread-affinity", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valThreadAffinity)
        
        if self.hasName():
            valName = Value()
            if self.name is not None:
                valName.setString(self.name)
            else:
                valName.setEmpty()
            tagValueList.push(("name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valName)
        
        if self.hasIdleSleepMsec():
            valIdleSleepMsec = Value()
            if self.idleSleepMsec is not None:
                valIdleSleepMsec.setInt64(self.idleSleepMsec)
            else:
                valIdleSleepMsec.setEmpty()
            tagValueList.push(("idle-sleep-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valIdleSleepMsec)
        
        if self.hasEnabled():
            valEnabled = Value()
            if self.enabled is not None:
                valEnabled.setBool(self.enabled)
            else:
                valEnabled.setEmpty()
            tagValueList.push(("enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valEnabled)
        
        if self.hasThreadPriority():
            valThreadPriority = Value()
            if self.threadPriority is not None:
                valThreadPriority.setString(self.threadPriority)
            else:
                valThreadPriority.setEmpty()
            tagValueList.push(("thread-priority", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valThreadPriority)
        
        if self.hasMode():
            valMode = Value()
            if self.mode is not None:
                valMode.setEnum(self.mode.getValue())
            else:
                valMode.setEmpty()
            tagValueList.push(("mode", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valMode)
        

        
        if self.loggingObj:
            valBegin = Value()
            (tag, ns, prefix) = ("logging" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.loggingObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-logging-failed').errorFunc(): logFunc('loggingObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.vipObj:
            valBegin = Value()
            (tag, ns, prefix) = ("vip" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.vipObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-vip-failed').errorFunc(): logFunc('vipObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.systemDefaultsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("system-defaults" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.systemDefaultsObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isThreadAffinityRequested():
            valThreadAffinity = Value()
            valThreadAffinity.setEmpty()
            tagValueList.push(("thread-affinity", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valThreadAffinity)
        
        if self.isNameRequested():
            valName = Value()
            valName.setEmpty()
            tagValueList.push(("name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valName)
        
        if self.isIdleSleepMsecRequested():
            valIdleSleepMsec = Value()
            valIdleSleepMsec.setEmpty()
            tagValueList.push(("idle-sleep-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valIdleSleepMsec)
        
        if self.isEnabledRequested():
            valEnabled = Value()
            valEnabled.setEmpty()
            tagValueList.push(("enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valEnabled)
        
        if self.isThreadPriorityRequested():
            valThreadPriority = Value()
            valThreadPriority.setEmpty()
            tagValueList.push(("thread-priority", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valThreadPriority)
        
        if self.isModeRequested():
            valMode = Value()
            valMode.setEmpty()
            tagValueList.push(("mode", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valMode)
        

        
        if self.loggingObj:
            valBegin = Value()
            (tag, ns, prefix) = ("logging" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.loggingObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-logging-failed').errorFunc(): logFunc('loggingObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.vipObj:
            valBegin = Value()
            (tag, ns, prefix) = ("vip" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.vipObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-vip-failed').errorFunc(): logFunc('vipObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.systemDefaultsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("system-defaults" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.systemDefaultsObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isThreadAffinityRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "thread-affinity") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-threadaffinity').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "threadAffinity", "thread-affinity", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-thread-affinity-bad-value').infoFunc(): logFunc('threadAffinity not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setThreadAffinity(tempVar)
            for logFunc in self._log('read-tag-values-thread-affinity').debug3Func(): logFunc('read threadAffinity. threadAffinity=%s, tempValue=%s', self.threadAffinity, tempValue.getType())
        
        if self.isNameRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "name") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-name').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "name", "name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-name-bad-value').infoFunc(): logFunc('name not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setName(tempVar)
            for logFunc in self._log('read-tag-values-name').debug3Func(): logFunc('read name. name=%s, tempValue=%s', self.name, tempValue.getType())
        
        if self.isIdleSleepMsecRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "idle-sleep-msec") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-idlesleepmsec').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "idleSleepMsec", "idle-sleep-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-idle-sleep-msec-bad-value').infoFunc(): logFunc('idleSleepMsec not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setIdleSleepMsec(tempVar)
            for logFunc in self._log('read-tag-values-idle-sleep-msec').debug3Func(): logFunc('read idleSleepMsec. idleSleepMsec=%s, tempValue=%s', self.idleSleepMsec, tempValue.getType())
        
        if self.isEnabledRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "enabled") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-enabled').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "enabled", "enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-enabled-bad-value').infoFunc(): logFunc('enabled not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setEnabled(tempVar)
            for logFunc in self._log('read-tag-values-enabled').debug3Func(): logFunc('read enabled. enabled=%s, tempValue=%s', self.enabled, tempValue.getType())
        
        if self.isThreadPriorityRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "thread-priority") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-threadpriority').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "threadPriority", "thread-priority", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-thread-priority-bad-value').infoFunc(): logFunc('threadPriority not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setThreadPriority(tempVar)
            for logFunc in self._log('read-tag-values-thread-priority').debug3Func(): logFunc('read threadPriority. threadPriority=%s, tempValue=%s', self.threadPriority, tempValue.getType())
        
        if self.isModeRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "mode") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-mode').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "mode", "mode", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-mode-bad-value').infoFunc(): logFunc('mode not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMode(tempVar)
            for logFunc in self._log('read-tag-values-mode').debug3Func(): logFunc('read mode. mode=%s, tempValue=%s', self.mode, tempValue.getType())
        

        
        if self.loggingObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "logging") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "logging", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.loggingObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-logging-failed').errorFunc(): logFunc('loggingObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "logging") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "logging", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.vipObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "vip") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "vip", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.vipObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-vip-failed').errorFunc(): logFunc('vipObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "vip") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "vip", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.systemDefaultsObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "system-defaults") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.systemDefaultsObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "system-defaults") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "unit", 
        "namespace": "unit", 
        "className": "UnitMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.analyzer.unit.unit_maapi_gen import UnitMaapi", 
        "baseClassName": "UnitMaapiBase", 
        "baseModule": "unit_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qtc", 
            "yangName": "content", 
            "namespace": "content", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "name": "content"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "isCurrent": false, 
            "yangName": "line", 
            "namespace": "line", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "keyLeaf": {
                "varName": "line", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "line"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "yangName": "analyzer", 
            "namespace": "analyzer", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "analyzer"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "isCurrent": true, 
            "yangName": "unit", 
            "namespace": "unit", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "keyLeaf": {
                "varName": "unit", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "unit"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "memberName": "logging", 
            "yangName": "logging", 
            "className": "BlinkyLoggingMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.analyzer.unit.logging.logging_maapi_gen import BlinkyLoggingMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "memberName": "vip", 
            "yangName": "vip", 
            "className": "BlinkyVipMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.analyzer.unit.vip.vip_maapi_gen import BlinkyVipMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "memberName": "systemDefaults", 
            "yangName": "system-defaults", 
            "className": "BlinkySystemDefaultsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.analyzer.unit.system_defaults.system_defaults_maapi_gen import BlinkySystemDefaultsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "threadAffinity", 
            "yangName": "thread-affinity", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "idleSleepMsec", 
            "yangName": "idle-sleep-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "threadPriority", 
            "yangName": "thread-priority", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "mode", 
            "yangName": "mode", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }
    ], 
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "content", 
            "qwilt_tech_content_line"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "threadAffinity", 
            "yangName": "thread-affinity", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "idleSleepMsec", 
            "yangName": "idle-sleep-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "threadPriority", 
            "yangName": "thread-priority", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "mode", 
            "yangName": "mode", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }
    ], 
    "createTime": "2013"
}
"""


