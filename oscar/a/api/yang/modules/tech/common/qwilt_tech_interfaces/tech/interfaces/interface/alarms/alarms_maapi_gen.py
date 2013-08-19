


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

from alarms_maapi_base_gen import AlarmsMaapiBase


from a.api.yang.modules.tech.common.qwilt_tech_interfaces.qwilt_tech_interfaces_module_gen import InterfaceIpv6ConnectivityFailureReasonType
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.qwilt_tech_interfaces_module_gen import InterfaceFailureReasonType
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.qwilt_tech_interfaces_module_gen import InterfaceIpv4ConnectivityFailureReasonType


class BlinkyAlarmsMaapi(AlarmsMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-alarms")
        self.domain = None

        

        
        self.interfaceFailureReasonRequested = False
        self.interfaceFailureReason = None
        self.interfaceFailureReasonSet = False
        
        self.interfaceIpv6ConnectivityFailureAlarmRequested = False
        self.interfaceIpv6ConnectivityFailureAlarm = None
        self.interfaceIpv6ConnectivityFailureAlarmSet = False
        
        self.interfaceFailureAlarmRequested = False
        self.interfaceFailureAlarm = None
        self.interfaceFailureAlarmSet = False
        
        self.interfaceIpv4ConnectivityFailureAlarmRequested = False
        self.interfaceIpv4ConnectivityFailureAlarm = None
        self.interfaceIpv4ConnectivityFailureAlarmSet = False
        
        self.interfaceIpv4ConnectivityFailureReasonRequested = False
        self.interfaceIpv4ConnectivityFailureReason = None
        self.interfaceIpv4ConnectivityFailureReasonSet = False
        
        self.interfaceIpv6ConnectivityFailureReasonRequested = False
        self.interfaceIpv6ConnectivityFailureReason = None
        self.interfaceIpv6ConnectivityFailureReasonSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestInterfaceFailureReason(True)
        
        self.requestInterfaceIpv6ConnectivityFailureAlarm(True)
        
        self.requestInterfaceFailureAlarm(True)
        
        self.requestInterfaceIpv4ConnectivityFailureAlarm(True)
        
        self.requestInterfaceIpv4ConnectivityFailureReason(True)
        
        self.requestInterfaceIpv6ConnectivityFailureReason(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestInterfaceFailureReason(False)
        
        self.requestInterfaceIpv6ConnectivityFailureAlarm(False)
        
        self.requestInterfaceFailureAlarm(False)
        
        self.requestInterfaceIpv4ConnectivityFailureAlarm(False)
        
        self.requestInterfaceIpv4ConnectivityFailureReason(False)
        
        self.requestInterfaceIpv6ConnectivityFailureReason(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestInterfaceFailureReason(True)
        
        self.requestInterfaceIpv6ConnectivityFailureAlarm(True)
        
        self.requestInterfaceFailureAlarm(True)
        
        self.requestInterfaceIpv4ConnectivityFailureAlarm(True)
        
        self.requestInterfaceIpv4ConnectivityFailureReason(True)
        
        self.requestInterfaceIpv6ConnectivityFailureReason(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestInterfaceFailureReason(False)
        
        self.requestInterfaceIpv6ConnectivityFailureAlarm(False)
        
        self.requestInterfaceFailureAlarm(False)
        
        self.requestInterfaceIpv4ConnectivityFailureAlarm(False)
        
        self.requestInterfaceIpv4ConnectivityFailureReason(False)
        
        self.requestInterfaceIpv6ConnectivityFailureReason(False)
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        

    def write (self
              , interface
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(interface, trxContext)

    def read (self
              , interface
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(interface, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , interface
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(interface, 
                                  True,
                                  trxContext)



    def requestInterfaceFailureReason (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-interfacefailurereason').debug3Func(): logFunc('called. requested=%s', requested)
        self.interfaceFailureReasonRequested = requested
        self.interfaceFailureReasonSet = False

    def isInterfaceFailureReasonRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-interfacefailurereason-requested').debug3Func(): logFunc('called. requested=%s', self.interfaceFailureReasonRequested)
        return self.interfaceFailureReasonRequested

    def getInterfaceFailureReason (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-interfacefailurereason').debug3Func(): logFunc('called. self.interfaceFailureReasonSet=%s, self.interfaceFailureReason=%s', self.interfaceFailureReasonSet, self.interfaceFailureReason)
        if self.interfaceFailureReasonSet:
            return self.interfaceFailureReason
        return None

    def hasInterfaceFailureReason (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-interfacefailurereason').debug3Func(): logFunc('called. self.interfaceFailureReasonSet=%s, self.interfaceFailureReason=%s', self.interfaceFailureReasonSet, self.interfaceFailureReason)
        if self.interfaceFailureReasonSet:
            return True
        return False

    def setInterfaceFailureReason (self, interfaceFailureReason):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-interfacefailurereason').debug3Func(): logFunc('called. interfaceFailureReason=%s, old=%s', interfaceFailureReason, self.interfaceFailureReason)
        self.interfaceFailureReasonSet = True
        self.interfaceFailureReason = interfaceFailureReason

    def requestInterfaceIpv6ConnectivityFailureAlarm (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-interfaceipv6connectivityfailurealarm').debug3Func(): logFunc('called. requested=%s', requested)
        self.interfaceIpv6ConnectivityFailureAlarmRequested = requested
        self.interfaceIpv6ConnectivityFailureAlarmSet = False

    def isInterfaceIpv6ConnectivityFailureAlarmRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-interfaceipv6connectivityfailurealarm-requested').debug3Func(): logFunc('called. requested=%s', self.interfaceIpv6ConnectivityFailureAlarmRequested)
        return self.interfaceIpv6ConnectivityFailureAlarmRequested

    def getInterfaceIpv6ConnectivityFailureAlarm (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-interfaceipv6connectivityfailurealarm').debug3Func(): logFunc('called. self.interfaceIpv6ConnectivityFailureAlarmSet=%s, self.interfaceIpv6ConnectivityFailureAlarm=%s', self.interfaceIpv6ConnectivityFailureAlarmSet, self.interfaceIpv6ConnectivityFailureAlarm)
        if self.interfaceIpv6ConnectivityFailureAlarmSet:
            return self.interfaceIpv6ConnectivityFailureAlarm
        return None

    def hasInterfaceIpv6ConnectivityFailureAlarm (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-interfaceipv6connectivityfailurealarm').debug3Func(): logFunc('called. self.interfaceIpv6ConnectivityFailureAlarmSet=%s, self.interfaceIpv6ConnectivityFailureAlarm=%s', self.interfaceIpv6ConnectivityFailureAlarmSet, self.interfaceIpv6ConnectivityFailureAlarm)
        if self.interfaceIpv6ConnectivityFailureAlarmSet:
            return True
        return False

    def setInterfaceIpv6ConnectivityFailureAlarm (self, interfaceIpv6ConnectivityFailureAlarm):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-interfaceipv6connectivityfailurealarm').debug3Func(): logFunc('called. interfaceIpv6ConnectivityFailureAlarm=%s, old=%s', interfaceIpv6ConnectivityFailureAlarm, self.interfaceIpv6ConnectivityFailureAlarm)
        self.interfaceIpv6ConnectivityFailureAlarmSet = True
        self.interfaceIpv6ConnectivityFailureAlarm = interfaceIpv6ConnectivityFailureAlarm

    def requestInterfaceFailureAlarm (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-interfacefailurealarm').debug3Func(): logFunc('called. requested=%s', requested)
        self.interfaceFailureAlarmRequested = requested
        self.interfaceFailureAlarmSet = False

    def isInterfaceFailureAlarmRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-interfacefailurealarm-requested').debug3Func(): logFunc('called. requested=%s', self.interfaceFailureAlarmRequested)
        return self.interfaceFailureAlarmRequested

    def getInterfaceFailureAlarm (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-interfacefailurealarm').debug3Func(): logFunc('called. self.interfaceFailureAlarmSet=%s, self.interfaceFailureAlarm=%s', self.interfaceFailureAlarmSet, self.interfaceFailureAlarm)
        if self.interfaceFailureAlarmSet:
            return self.interfaceFailureAlarm
        return None

    def hasInterfaceFailureAlarm (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-interfacefailurealarm').debug3Func(): logFunc('called. self.interfaceFailureAlarmSet=%s, self.interfaceFailureAlarm=%s', self.interfaceFailureAlarmSet, self.interfaceFailureAlarm)
        if self.interfaceFailureAlarmSet:
            return True
        return False

    def setInterfaceFailureAlarm (self, interfaceFailureAlarm):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-interfacefailurealarm').debug3Func(): logFunc('called. interfaceFailureAlarm=%s, old=%s', interfaceFailureAlarm, self.interfaceFailureAlarm)
        self.interfaceFailureAlarmSet = True
        self.interfaceFailureAlarm = interfaceFailureAlarm

    def requestInterfaceIpv4ConnectivityFailureAlarm (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-interfaceipv4connectivityfailurealarm').debug3Func(): logFunc('called. requested=%s', requested)
        self.interfaceIpv4ConnectivityFailureAlarmRequested = requested
        self.interfaceIpv4ConnectivityFailureAlarmSet = False

    def isInterfaceIpv4ConnectivityFailureAlarmRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-interfaceipv4connectivityfailurealarm-requested').debug3Func(): logFunc('called. requested=%s', self.interfaceIpv4ConnectivityFailureAlarmRequested)
        return self.interfaceIpv4ConnectivityFailureAlarmRequested

    def getInterfaceIpv4ConnectivityFailureAlarm (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-interfaceipv4connectivityfailurealarm').debug3Func(): logFunc('called. self.interfaceIpv4ConnectivityFailureAlarmSet=%s, self.interfaceIpv4ConnectivityFailureAlarm=%s', self.interfaceIpv4ConnectivityFailureAlarmSet, self.interfaceIpv4ConnectivityFailureAlarm)
        if self.interfaceIpv4ConnectivityFailureAlarmSet:
            return self.interfaceIpv4ConnectivityFailureAlarm
        return None

    def hasInterfaceIpv4ConnectivityFailureAlarm (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-interfaceipv4connectivityfailurealarm').debug3Func(): logFunc('called. self.interfaceIpv4ConnectivityFailureAlarmSet=%s, self.interfaceIpv4ConnectivityFailureAlarm=%s', self.interfaceIpv4ConnectivityFailureAlarmSet, self.interfaceIpv4ConnectivityFailureAlarm)
        if self.interfaceIpv4ConnectivityFailureAlarmSet:
            return True
        return False

    def setInterfaceIpv4ConnectivityFailureAlarm (self, interfaceIpv4ConnectivityFailureAlarm):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-interfaceipv4connectivityfailurealarm').debug3Func(): logFunc('called. interfaceIpv4ConnectivityFailureAlarm=%s, old=%s', interfaceIpv4ConnectivityFailureAlarm, self.interfaceIpv4ConnectivityFailureAlarm)
        self.interfaceIpv4ConnectivityFailureAlarmSet = True
        self.interfaceIpv4ConnectivityFailureAlarm = interfaceIpv4ConnectivityFailureAlarm

    def requestInterfaceIpv4ConnectivityFailureReason (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-interfaceipv4connectivityfailurereason').debug3Func(): logFunc('called. requested=%s', requested)
        self.interfaceIpv4ConnectivityFailureReasonRequested = requested
        self.interfaceIpv4ConnectivityFailureReasonSet = False

    def isInterfaceIpv4ConnectivityFailureReasonRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-interfaceipv4connectivityfailurereason-requested').debug3Func(): logFunc('called. requested=%s', self.interfaceIpv4ConnectivityFailureReasonRequested)
        return self.interfaceIpv4ConnectivityFailureReasonRequested

    def getInterfaceIpv4ConnectivityFailureReason (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-interfaceipv4connectivityfailurereason').debug3Func(): logFunc('called. self.interfaceIpv4ConnectivityFailureReasonSet=%s, self.interfaceIpv4ConnectivityFailureReason=%s', self.interfaceIpv4ConnectivityFailureReasonSet, self.interfaceIpv4ConnectivityFailureReason)
        if self.interfaceIpv4ConnectivityFailureReasonSet:
            return self.interfaceIpv4ConnectivityFailureReason
        return None

    def hasInterfaceIpv4ConnectivityFailureReason (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-interfaceipv4connectivityfailurereason').debug3Func(): logFunc('called. self.interfaceIpv4ConnectivityFailureReasonSet=%s, self.interfaceIpv4ConnectivityFailureReason=%s', self.interfaceIpv4ConnectivityFailureReasonSet, self.interfaceIpv4ConnectivityFailureReason)
        if self.interfaceIpv4ConnectivityFailureReasonSet:
            return True
        return False

    def setInterfaceIpv4ConnectivityFailureReason (self, interfaceIpv4ConnectivityFailureReason):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-interfaceipv4connectivityfailurereason').debug3Func(): logFunc('called. interfaceIpv4ConnectivityFailureReason=%s, old=%s', interfaceIpv4ConnectivityFailureReason, self.interfaceIpv4ConnectivityFailureReason)
        self.interfaceIpv4ConnectivityFailureReasonSet = True
        self.interfaceIpv4ConnectivityFailureReason = interfaceIpv4ConnectivityFailureReason

    def requestInterfaceIpv6ConnectivityFailureReason (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-interfaceipv6connectivityfailurereason').debug3Func(): logFunc('called. requested=%s', requested)
        self.interfaceIpv6ConnectivityFailureReasonRequested = requested
        self.interfaceIpv6ConnectivityFailureReasonSet = False

    def isInterfaceIpv6ConnectivityFailureReasonRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-interfaceipv6connectivityfailurereason-requested').debug3Func(): logFunc('called. requested=%s', self.interfaceIpv6ConnectivityFailureReasonRequested)
        return self.interfaceIpv6ConnectivityFailureReasonRequested

    def getInterfaceIpv6ConnectivityFailureReason (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-interfaceipv6connectivityfailurereason').debug3Func(): logFunc('called. self.interfaceIpv6ConnectivityFailureReasonSet=%s, self.interfaceIpv6ConnectivityFailureReason=%s', self.interfaceIpv6ConnectivityFailureReasonSet, self.interfaceIpv6ConnectivityFailureReason)
        if self.interfaceIpv6ConnectivityFailureReasonSet:
            return self.interfaceIpv6ConnectivityFailureReason
        return None

    def hasInterfaceIpv6ConnectivityFailureReason (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-interfaceipv6connectivityfailurereason').debug3Func(): logFunc('called. self.interfaceIpv6ConnectivityFailureReasonSet=%s, self.interfaceIpv6ConnectivityFailureReason=%s', self.interfaceIpv6ConnectivityFailureReasonSet, self.interfaceIpv6ConnectivityFailureReason)
        if self.interfaceIpv6ConnectivityFailureReasonSet:
            return True
        return False

    def setInterfaceIpv6ConnectivityFailureReason (self, interfaceIpv6ConnectivityFailureReason):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-interfaceipv6connectivityfailurereason').debug3Func(): logFunc('called. interfaceIpv6ConnectivityFailureReason=%s, old=%s', interfaceIpv6ConnectivityFailureReason, self.interfaceIpv6ConnectivityFailureReason)
        self.interfaceIpv6ConnectivityFailureReasonSet = True
        self.interfaceIpv6ConnectivityFailureReason = interfaceIpv6ConnectivityFailureReason


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.interfaceFailureReason = 0
        self.interfaceFailureReasonSet = False
        
        self.interfaceIpv6ConnectivityFailureAlarm = 0
        self.interfaceIpv6ConnectivityFailureAlarmSet = False
        
        self.interfaceFailureAlarm = 0
        self.interfaceFailureAlarmSet = False
        
        self.interfaceIpv4ConnectivityFailureAlarm = 0
        self.interfaceIpv4ConnectivityFailureAlarmSet = False
        
        self.interfaceIpv4ConnectivityFailureReason = 0
        self.interfaceIpv4ConnectivityFailureReasonSet = False
        
        self.interfaceIpv6ConnectivityFailureReason = 0
        self.interfaceIpv6ConnectivityFailureReasonSet = False
        

    def _getSelfKeyPath (self, interface
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("alarms", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(interface);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("interface", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("interfaces", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        interface, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(interface, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(interface, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       interface, 
                       
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

        keyPath = self._getSelfKeyPath(interface, 
                                       
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
                               interface, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isInterfaceFailureReasonRequested():
            valInterfaceFailureReason = Value()
            valInterfaceFailureReason.setEmpty()
            tagValueList.push(("interface-failure-reason", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valInterfaceFailureReason)
        
        if self.isInterfaceIpv6ConnectivityFailureAlarmRequested():
            valInterfaceIpv6ConnectivityFailureAlarm = Value()
            valInterfaceIpv6ConnectivityFailureAlarm.setEmpty()
            tagValueList.push(("interface-ipv6-connectivity-failure-alarm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valInterfaceIpv6ConnectivityFailureAlarm)
        
        if self.isInterfaceFailureAlarmRequested():
            valInterfaceFailureAlarm = Value()
            valInterfaceFailureAlarm.setEmpty()
            tagValueList.push(("interface-failure-alarm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valInterfaceFailureAlarm)
        
        if self.isInterfaceIpv4ConnectivityFailureAlarmRequested():
            valInterfaceIpv4ConnectivityFailureAlarm = Value()
            valInterfaceIpv4ConnectivityFailureAlarm.setEmpty()
            tagValueList.push(("interface-ipv4-connectivity-failure-alarm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valInterfaceIpv4ConnectivityFailureAlarm)
        
        if self.isInterfaceIpv4ConnectivityFailureReasonRequested():
            valInterfaceIpv4ConnectivityFailureReason = Value()
            valInterfaceIpv4ConnectivityFailureReason.setEmpty()
            tagValueList.push(("interface-ipv4-connectivity-failure-reason", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valInterfaceIpv4ConnectivityFailureReason)
        
        if self.isInterfaceIpv6ConnectivityFailureReasonRequested():
            valInterfaceIpv6ConnectivityFailureReason = Value()
            valInterfaceIpv6ConnectivityFailureReason.setEmpty()
            tagValueList.push(("interface-ipv6-connectivity-failure-reason", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valInterfaceIpv6ConnectivityFailureReason)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isInterfaceFailureReasonRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "interface-failure-reason") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-interfacefailurereason').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "interfaceFailureReason", "interface-failure-reason", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-interface-failure-reason-bad-value').infoFunc(): logFunc('interfaceFailureReason not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setInterfaceFailureReason(tempVar)
            for logFunc in self._log('read-tag-values-interface-failure-reason').debug3Func(): logFunc('read interfaceFailureReason. interfaceFailureReason=%s, tempValue=%s', self.interfaceFailureReason, tempValue.getType())
        
        if self.isInterfaceIpv6ConnectivityFailureAlarmRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "interface-ipv6-connectivity-failure-alarm") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-interfaceipv6connectivityfailurealarm').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "interfaceIpv6ConnectivityFailureAlarm", "interface-ipv6-connectivity-failure-alarm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-interface-ipv6-connectivity-failure-alarm-bad-value').infoFunc(): logFunc('interfaceIpv6ConnectivityFailureAlarm not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setInterfaceIpv6ConnectivityFailureAlarm(tempVar)
            for logFunc in self._log('read-tag-values-interface-ipv6-connectivity-failure-alarm').debug3Func(): logFunc('read interfaceIpv6ConnectivityFailureAlarm. interfaceIpv6ConnectivityFailureAlarm=%s, tempValue=%s', self.interfaceIpv6ConnectivityFailureAlarm, tempValue.getType())
        
        if self.isInterfaceFailureAlarmRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "interface-failure-alarm") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-interfacefailurealarm').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "interfaceFailureAlarm", "interface-failure-alarm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-interface-failure-alarm-bad-value').infoFunc(): logFunc('interfaceFailureAlarm not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setInterfaceFailureAlarm(tempVar)
            for logFunc in self._log('read-tag-values-interface-failure-alarm').debug3Func(): logFunc('read interfaceFailureAlarm. interfaceFailureAlarm=%s, tempValue=%s', self.interfaceFailureAlarm, tempValue.getType())
        
        if self.isInterfaceIpv4ConnectivityFailureAlarmRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "interface-ipv4-connectivity-failure-alarm") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-interfaceipv4connectivityfailurealarm').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "interfaceIpv4ConnectivityFailureAlarm", "interface-ipv4-connectivity-failure-alarm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-interface-ipv4-connectivity-failure-alarm-bad-value').infoFunc(): logFunc('interfaceIpv4ConnectivityFailureAlarm not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setInterfaceIpv4ConnectivityFailureAlarm(tempVar)
            for logFunc in self._log('read-tag-values-interface-ipv4-connectivity-failure-alarm').debug3Func(): logFunc('read interfaceIpv4ConnectivityFailureAlarm. interfaceIpv4ConnectivityFailureAlarm=%s, tempValue=%s', self.interfaceIpv4ConnectivityFailureAlarm, tempValue.getType())
        
        if self.isInterfaceIpv4ConnectivityFailureReasonRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "interface-ipv4-connectivity-failure-reason") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-interfaceipv4connectivityfailurereason').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "interfaceIpv4ConnectivityFailureReason", "interface-ipv4-connectivity-failure-reason", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-interface-ipv4-connectivity-failure-reason-bad-value').infoFunc(): logFunc('interfaceIpv4ConnectivityFailureReason not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setInterfaceIpv4ConnectivityFailureReason(tempVar)
            for logFunc in self._log('read-tag-values-interface-ipv4-connectivity-failure-reason').debug3Func(): logFunc('read interfaceIpv4ConnectivityFailureReason. interfaceIpv4ConnectivityFailureReason=%s, tempValue=%s', self.interfaceIpv4ConnectivityFailureReason, tempValue.getType())
        
        if self.isInterfaceIpv6ConnectivityFailureReasonRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "interface-ipv6-connectivity-failure-reason") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-interfaceipv6connectivityfailurereason').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "interfaceIpv6ConnectivityFailureReason", "interface-ipv6-connectivity-failure-reason", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-interface-ipv6-connectivity-failure-reason-bad-value').infoFunc(): logFunc('interfaceIpv6ConnectivityFailureReason not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setInterfaceIpv6ConnectivityFailureReason(tempVar)
            for logFunc in self._log('read-tag-values-interface-ipv6-connectivity-failure-reason').debug3Func(): logFunc('read interfaceIpv6ConnectivityFailureReason. interfaceIpv6ConnectivityFailureReason=%s, tempValue=%s', self.interfaceIpv6ConnectivityFailureReason, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "alarms", 
        "namespace": "alarms", 
        "className": "AlarmsMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.alarms.alarms_maapi_gen import AlarmsMaapi", 
        "baseClassName": "AlarmsMaapiBase", 
        "baseModule": "alarms_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "interfaces", 
            "namespace": "interfaces", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "isCurrent": false, 
            "yangName": "interface", 
            "namespace": "interface", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "keyLeaf": {
                "varName": "interface", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "interface"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "alarms", 
            "namespace": "alarms", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "alarms"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "interfaceFailureReason", 
            "yangName": "interface-failure-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "interfaceIpv6ConnectivityFailureAlarm", 
            "yangName": "interface-ipv6-connectivity-failure-alarm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "interfaceFailureAlarm", 
            "yangName": "interface-failure-alarm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "interfaceIpv4ConnectivityFailureAlarm", 
            "yangName": "interface-ipv4-connectivity-failure-alarm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "interfaceIpv4ConnectivityFailureReason", 
            "yangName": "interface-ipv4-connectivity-failure-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "interfaceIpv6ConnectivityFailureReason", 
            "yangName": "interface-ipv6-connectivity-failure-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "module": {}, 
    "configLeaves": [], 
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "common", 
            "qwilt_tech_interfaces"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "interfaceFailureReason", 
            "yangName": "interface-failure-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "interfaceIpv6ConnectivityFailureAlarm", 
            "yangName": "interface-ipv6-connectivity-failure-alarm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "interfaceFailureAlarm", 
            "yangName": "interface-failure-alarm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "interfaceIpv4ConnectivityFailureAlarm", 
            "yangName": "interface-ipv4-connectivity-failure-alarm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "interfaceIpv4ConnectivityFailureReason", 
            "yangName": "interface-ipv4-connectivity-failure-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "interfaceIpv6ConnectivityFailureReason", 
            "yangName": "interface-ipv6-connectivity-failure-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


