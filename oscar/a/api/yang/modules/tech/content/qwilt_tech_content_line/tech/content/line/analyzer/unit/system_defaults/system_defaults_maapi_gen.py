


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

from system_defaults_maapi_base_gen import SystemDefaultsMaapiBase

from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.analyzer.unit.system_defaults.logging.logging_maapi_gen import BlinkyLoggingMaapi
from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.analyzer.unit.system_defaults.vip.vip_maapi_gen import BlinkyVipMaapi

from a.api.yang.modules.tech.content.qwilt_tech_content_line.qwilt_tech_content_line_module_gen import AnalyzerUnitModeType


class BlinkySystemDefaultsMaapi(SystemDefaultsMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-systemDefaults")
        self.domain = None

        
        self.loggingObj = None
        
        self.vipObj = None
        

        
        self.threadAffinityRequested = False
        self.threadAffinity = None
        self.threadAffinitySet = False
        
        self.idleSleepMsecRequested = False
        self.idleSleepMsec = None
        self.idleSleepMsecSet = False
        
        self.enabledRequested = False
        self.enabled = None
        self.enabledSet = False
        
        self.modeRequested = False
        self.mode = None
        self.modeSet = False
        
        self.threadPriorityRequested = False
        self.threadPriority = None
        self.threadPrioritySet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestThreadAffinity(True)
        
        self.requestIdleSleepMsec(True)
        
        self.requestEnabled(True)
        
        self.requestMode(True)
        
        self.requestThreadPriority(True)
        
        
        
        if not self.loggingObj:
            self.loggingObj = self.newLogging()
            self.loggingObj.requestConfigAndOper()
        
        if not self.vipObj:
            self.vipObj = self.newVip()
            self.vipObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestThreadAffinity(True)
        
        self.requestIdleSleepMsec(True)
        
        self.requestEnabled(True)
        
        self.requestMode(True)
        
        self.requestThreadPriority(True)
        
        
        
        if not self.loggingObj:
            self.loggingObj = self.newLogging()
            self.loggingObj.requestConfig()
        
        if not self.vipObj:
            self.vipObj = self.newVip()
            self.vipObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestThreadAffinity(False)
        
        self.requestIdleSleepMsec(False)
        
        self.requestEnabled(False)
        
        self.requestMode(False)
        
        self.requestThreadPriority(False)
        
        
        
        if not self.loggingObj:
            self.loggingObj = self.newLogging()
            self.loggingObj.requestOper()
        
        if not self.vipObj:
            self.vipObj = self.newVip()
            self.vipObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestThreadAffinity(False)
        
        self.requestIdleSleepMsec(False)
        
        self.requestEnabled(False)
        
        self.requestMode(False)
        
        self.requestThreadPriority(False)
        
        
        
        if not self.loggingObj:
            self.loggingObj = self.newLogging()
            self.loggingObj.clearAllRequested()
        
        if not self.vipObj:
            self.vipObj = self.newVip()
            self.vipObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setThreadAffinity(None)
        self.threadAffinitySet = False
        
        self.setIdleSleepMsec(None)
        self.idleSleepMsecSet = False
        
        self.setEnabled(None)
        self.enabledSet = False
        
        self.setMode(None)
        self.modeSet = False
        
        self.setThreadPriority(None)
        self.threadPrioritySet = False
        
        
        if self.loggingObj:
            self.loggingObj.clearAllSet()
        
        if self.vipObj:
            self.vipObj.clearAllSet()
        

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


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.loggingObj:
            self.loggingObj._clearAllReadData()
        
        if self.vipObj:
            self.vipObj._clearAllReadData()
        

        
        self.threadAffinity = 0
        self.threadAffinitySet = False
        
        self.idleSleepMsec = 0
        self.idleSleepMsecSet = False
        
        self.enabled = 0
        self.enabledSet = False
        
        self.mode = 0
        self.modeSet = False
        
        self.threadPriority = 0
        self.threadPrioritySet = False
        

    def _getSelfKeyPath (self, line
                         , unit
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
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
        
        if self.hasMode():
            valMode = Value()
            if self.mode is not None:
                valMode.setEnum(self.mode.getValue())
            else:
                valMode.setEmpty()
            tagValueList.push(("mode", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valMode)
        
        if self.hasThreadPriority():
            valThreadPriority = Value()
            if self.threadPriority is not None:
                valThreadPriority.setString(self.threadPriority)
            else:
                valThreadPriority.setEmpty()
            tagValueList.push(("thread-priority", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valThreadPriority)
        

        
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
        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isThreadAffinityRequested():
            valThreadAffinity = Value()
            valThreadAffinity.setEmpty()
            tagValueList.push(("thread-affinity", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valThreadAffinity)
        
        if self.isIdleSleepMsecRequested():
            valIdleSleepMsec = Value()
            valIdleSleepMsec.setEmpty()
            tagValueList.push(("idle-sleep-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valIdleSleepMsec)
        
        if self.isEnabledRequested():
            valEnabled = Value()
            valEnabled.setEmpty()
            tagValueList.push(("enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valEnabled)
        
        if self.isModeRequested():
            valMode = Value()
            valMode.setEmpty()
            tagValueList.push(("mode", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valMode)
        
        if self.isThreadPriorityRequested():
            valThreadPriority = Value()
            valThreadPriority.setEmpty()
            tagValueList.push(("thread-priority", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valThreadPriority)
        

        
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
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "systemDefaults", 
        "namespace": "system_defaults", 
        "className": "SystemDefaultsMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.analyzer.unit.system_defaults.system_defaults_maapi_gen import SystemDefaultsMaapi", 
        "baseClassName": "SystemDefaultsMaapiBase", 
        "baseModule": "system_defaults_maapi_base_gen"
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
            "isCurrent": false, 
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
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "system-defaults"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "memberName": "logging", 
            "yangName": "logging", 
            "className": "BlinkyLoggingMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.analyzer.unit.system_defaults.logging.logging_maapi_gen import BlinkyLoggingMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "memberName": "vip", 
            "yangName": "vip", 
            "className": "BlinkyVipMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.analyzer.unit.system_defaults.vip.vip_maapi_gen import BlinkyVipMaapi", 
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
            "defaultVal": "", 
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
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "mode", 
            "yangName": "mode", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "process-packets", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "threadPriority", 
            "yangName": "thread-priority", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
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
            "defaultVal": "", 
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
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "mode", 
            "yangName": "mode", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "process-packets", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "threadPriority", 
            "yangName": "thread-priority", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


