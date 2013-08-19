


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

from ipv6_maapi_base_gen import Ipv6MaapiBase

from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.system_defaults.connectivity_check.ipv6.ping.ping_maapi_gen import BlinkyPingMaapi
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.system_defaults.connectivity_check.ipv6.neighbor_discovery.neighbor_discovery_maapi_gen import BlinkyNeighborDiscoveryMaapi

from a.api.yang.modules.tech.common.qwilt_tech_interfaces_types.qwilt_tech_interfaces_types_module_gen import ConnectivityCheckIpv6MethodType


class BlinkyIpv6Maapi(Ipv6MaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-ipv6")
        self.domain = None

        
        self.pingObj = None
        
        self.neighborDiscoveryObj = None
        

        
        self.methodRequested = False
        self.method = None
        self.methodSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestMethod(True)
        
        
        
        if not self.pingObj:
            self.pingObj = self.newPing()
            self.pingObj.requestConfigAndOper()
        
        if not self.neighborDiscoveryObj:
            self.neighborDiscoveryObj = self.newNeighborDiscovery()
            self.neighborDiscoveryObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestMethod(True)
        
        
        
        if not self.pingObj:
            self.pingObj = self.newPing()
            self.pingObj.requestConfig()
        
        if not self.neighborDiscoveryObj:
            self.neighborDiscoveryObj = self.newNeighborDiscovery()
            self.neighborDiscoveryObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestMethod(False)
        
        
        
        if not self.pingObj:
            self.pingObj = self.newPing()
            self.pingObj.requestOper()
        
        if not self.neighborDiscoveryObj:
            self.neighborDiscoveryObj = self.newNeighborDiscovery()
            self.neighborDiscoveryObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestMethod(False)
        
        
        
        if not self.pingObj:
            self.pingObj = self.newPing()
            self.pingObj.clearAllRequested()
        
        if not self.neighborDiscoveryObj:
            self.neighborDiscoveryObj = self.newNeighborDiscovery()
            self.neighborDiscoveryObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setMethod(None)
        self.methodSet = False
        
        
        if self.pingObj:
            self.pingObj.clearAllSet()
        
        if self.neighborDiscoveryObj:
            self.neighborDiscoveryObj.clearAllSet()
        

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

    def newPing (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-ping').debug3Func(): logFunc('called.')
        ping = BlinkyPingMaapi(self._log)
        ping.init(self.domain)
        return ping

    def setPingObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-ping').debug3Func(): logFunc('called. obj=%s', obj)
        self.pingObj = obj

    def getPingObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-ping').debug3Func(): logFunc('called. self.pingObj=%s', self.pingObj)
        return self.pingObj

    def hasPing (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-ping').debug3Func(): logFunc('called. self.pingObj=%s', self.pingObj)
        if self.pingObj:
            return True
        return False

    def newNeighborDiscovery (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-neighbordiscovery').debug3Func(): logFunc('called.')
        neighborDiscovery = BlinkyNeighborDiscoveryMaapi(self._log)
        neighborDiscovery.init(self.domain)
        return neighborDiscovery

    def setNeighborDiscoveryObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-neighbordiscovery').debug3Func(): logFunc('called. obj=%s', obj)
        self.neighborDiscoveryObj = obj

    def getNeighborDiscoveryObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-neighbordiscovery').debug3Func(): logFunc('called. self.neighborDiscoveryObj=%s', self.neighborDiscoveryObj)
        return self.neighborDiscoveryObj

    def hasNeighborDiscovery (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-neighbordiscovery').debug3Func(): logFunc('called. self.neighborDiscoveryObj=%s', self.neighborDiscoveryObj)
        if self.neighborDiscoveryObj:
            return True
        return False



    def requestMethod (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-method').debug3Func(): logFunc('called. requested=%s', requested)
        self.methodRequested = requested
        self.methodSet = False

    def isMethodRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-method-requested').debug3Func(): logFunc('called. requested=%s', self.methodRequested)
        return self.methodRequested

    def getMethod (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-method').debug3Func(): logFunc('called. self.methodSet=%s, self.method=%s', self.methodSet, self.method)
        if self.methodSet:
            return self.method
        return None

    def hasMethod (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-method').debug3Func(): logFunc('called. self.methodSet=%s, self.method=%s', self.methodSet, self.method)
        if self.methodSet:
            return True
        return False

    def setMethod (self, method):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-method').debug3Func(): logFunc('called. method=%s, old=%s', method, self.method)
        self.methodSet = True
        self.method = method


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.pingObj:
            self.pingObj._clearAllReadData()
        
        if self.neighborDiscoveryObj:
            self.neighborDiscoveryObj._clearAllReadData()
        

        
        self.method = 0
        self.methodSet = False
        

    def _getSelfKeyPath (self, interface
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("ipv6", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("connectivity-check", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
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

        
        if self.pingObj:
            res = self.pingObj._collectItemsToDelete(interface, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-ping-failed').errorFunc(): logFunc('pingObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.neighborDiscoveryObj:
            res = self.neighborDiscoveryObj._collectItemsToDelete(interface, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-neighbor-discovery-failed').errorFunc(): logFunc('neighborDiscoveryObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasMethod():
            valMethod = Value()
            if self.method is not None:
                valMethod.setEnum(self.method.getValue())
            else:
                valMethod.setEmpty()
            tagValueList.push(("method", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valMethod)
        

        
        if self.pingObj:
            valBegin = Value()
            (tag, ns, prefix) = ("ping" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.pingObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-ping-failed').errorFunc(): logFunc('pingObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.neighborDiscoveryObj:
            valBegin = Value()
            (tag, ns, prefix) = ("neighbor-discovery" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.neighborDiscoveryObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-neighbor-discovery-failed').errorFunc(): logFunc('neighborDiscoveryObj._fillWriteTagValues() failed. PARAMS')
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

        
        if self.isMethodRequested():
            valMethod = Value()
            valMethod.setEmpty()
            tagValueList.push(("method", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valMethod)
        

        
        if self.pingObj:
            valBegin = Value()
            (tag, ns, prefix) = ("ping" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.pingObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-ping-failed').errorFunc(): logFunc('pingObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.neighborDiscoveryObj:
            valBegin = Value()
            (tag, ns, prefix) = ("neighbor-discovery" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.neighborDiscoveryObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-neighbor-discovery-failed').errorFunc(): logFunc('neighborDiscoveryObj._fillReadTagValues() failed. PARAMS')
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
        
        if self.isMethodRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "method") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-method').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "method", "method", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-method-bad-value').infoFunc(): logFunc('method not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMethod(tempVar)
            for logFunc in self._log('read-tag-values-method').debug3Func(): logFunc('read method. method=%s, tempValue=%s', self.method, tempValue.getType())
        

        
        if self.pingObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "ping") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "ping", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.pingObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-ping-failed').errorFunc(): logFunc('pingObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "ping") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "ping", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.neighborDiscoveryObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "neighbor-discovery") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "neighbor-discovery", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.neighborDiscoveryObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-neighbor-discovery-failed').errorFunc(): logFunc('neighborDiscoveryObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "neighbor-discovery") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "neighbor-discovery", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "ipv6", 
        "namespace": "ipv6", 
        "className": "Ipv6Maapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.system_defaults.connectivity_check.ipv6.ipv6_maapi_gen import Ipv6Maapi", 
        "baseClassName": "Ipv6MaapiBase", 
        "baseModule": "ipv6_maapi_base_gen"
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
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "system-defaults"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "connectivity-check", 
            "namespace": "connectivity_check", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "connectivity-check"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "ipv6", 
            "namespace": "ipv6", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "ipv6"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "memberName": "ping", 
            "yangName": "ping", 
            "className": "BlinkyPingMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.system_defaults.connectivity_check.ipv6.ping.ping_maapi_gen import BlinkyPingMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "memberName": "neighborDiscovery", 
            "yangName": "neighbor-discovery", 
            "className": "BlinkyNeighborDiscoveryMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.system_defaults.connectivity_check.ipv6.neighbor_discovery.neighbor_discovery_maapi_gen import BlinkyNeighborDiscoveryMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "method", 
            "yangName": "method", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "neighbor-discovery", 
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
            "common", 
            "qwilt_tech_interfaces"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "method", 
            "yangName": "method", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "neighbor-discovery", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


