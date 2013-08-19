


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

from ipv4_maapi_base_gen import Ipv4MaapiBase

from a.api.yang.modules.tech.common.qwilt_tech_system.tech.system.name_resolution.static_resolution.hosts.ipv4.host.host_maapi_list_gen import BlinkyHostMaapiList

import struct


class BlinkyIpv4Maapi(Ipv4MaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-ipv4")
        self.domain = None

        
        self.hostListObj = None
        

        
        self.addressRequested = False
        self.address = None
        self.addressSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestAddress(True)
        
        
        
        if not self.hostListObj:
            self.hostListObj = self.newHostList()
            self.hostListObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestAddress(True)
        
        
        
        if not self.hostListObj:
            self.hostListObj = self.newHostList()
            self.hostListObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestAddress(False)
        
        
        
        if not self.hostListObj:
            self.hostListObj = self.newHostList()
            self.hostListObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestAddress(False)
        
        
        
        if not self.hostListObj:
            self.hostListObj = self.newHostList()
            self.hostListObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setAddress(None)
        self.addressSet = False
        
        
        if self.hostListObj:
            self.hostListObj.clearAllSet()
        

    def write (self
              , ipv4
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(ipv4, trxContext)

    def read (self
              , ipv4
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(ipv4, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , ipv4
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(ipv4, 
                                  True,
                                  trxContext)

    def newHostList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-hostlist').debug3Func(): logFunc('called.')
        hostList = BlinkyHostMaapiList(self._log)
        hostList.init(self.domain)
        return hostList

    def setHostListObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-hostlist').debug3Func(): logFunc('called. obj=%s', obj)
        self.hostListObj = obj

    def getHostListObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-hostlist').debug3Func(): logFunc('called. self.hostListObj=%s', self.hostListObj)
        return self.hostListObj

    def hasHostList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-hostlist').debug3Func(): logFunc('called. self.hostListObj=%s', self.hostListObj)
        if self.hostListObj:
            return True
        return False



    def requestAddress (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-address').debug3Func(): logFunc('called. requested=%s', requested)
        self.addressRequested = requested
        self.addressSet = False

    def isAddressRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-address-requested').debug3Func(): logFunc('called. requested=%s', self.addressRequested)
        return self.addressRequested

    def getAddress (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-address').debug3Func(): logFunc('called. self.addressSet=%s, self.address=%s', self.addressSet, self.address)
        if self.addressSet:
            return self.address
        return None

    def hasAddress (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-address').debug3Func(): logFunc('called. self.addressSet=%s, self.address=%s', self.addressSet, self.address)
        if self.addressSet:
            return True
        return False

    def setAddress (self, address):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-address').debug3Func(): logFunc('called. address=%s, old=%s', address, self.address)
        self.addressSet = True
        self.address = address


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.hostListObj:
            self.hostListObj._clearAllReadData()
        

        
        self.address = 0
        self.addressSet = False
        

    def _getSelfKeyPath (self, ipv4
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        ancestorVal = Value()
        ancestorVal.setString(ipv4);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("ipv4", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", "qt-sys"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("hosts", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", "qt-sys"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("static", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", "qt-sys"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("name-resolution", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", "qt-sys"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", "qt-sys"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        ipv4, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(ipv4, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(ipv4, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       ipv4, 
                       
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

        keyPath = self._getSelfKeyPath(ipv4, 
                                       
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
                               ipv4, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        
        if self.hostListObj:
            res = self.hostListObj._collectItemsToDelete(ipv4, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-host-failed').errorFunc(): logFunc('hostListObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasAddress():
            valAddress = Value()
            if self.address is not None:
                valAddress.setIPv4(self.address)
            else:
                valAddress.setEmpty()
            tagValueList.push(("address", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system"), valAddress)
        

        
        if self.hostListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("host" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", "qt-sys")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.hostListObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-host-failed').errorFunc(): logFunc('hostListObj._fillWriteTagValues() failed. PARAMS')
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

        
        if self.isAddressRequested():
            valAddress = Value()
            valAddress.setEmpty()
            tagValueList.push(("address", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system"), valAddress)
        

        
        if self.hostListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("host" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", "qt-sys")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.hostListObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-host-failed').errorFunc(): logFunc('hostListObj._fillReadTagValues() failed. PARAMS')
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
        
        if self.isAddressRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "address") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-address').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "address", "address", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = (tempValue.asIPv4())
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-address-bad-value').infoFunc(): logFunc('address not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setAddress(tempVar)
            for logFunc in self._log('read-tag-values-address').debug3Func(): logFunc('read address. address=%s, tempValue=%s', self.address, tempValue.getType())
        

        
        if self.hostListObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "host") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "host", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.hostListObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-host-failed').errorFunc(): logFunc('hostListObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "host") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "host", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "ipv4", 
        "namespace": "ipv4", 
        "className": "Ipv4Maapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system.tech.system.name_resolution.static_resolution.hosts.ipv4.ipv4_maapi_gen import Ipv4Maapi", 
        "baseClassName": "Ipv4MaapiBase", 
        "baseModule": "ipv4_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-sys", 
            "yangName": "system", 
            "namespace": "system", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", 
            "name": "system"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys", 
            "yangName": "name-resolution", 
            "namespace": "name_resolution", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", 
            "name": "name-resolution"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys", 
            "yangName": "static", 
            "namespace": "static_resolution", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", 
            "name": "static-resolution"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys", 
            "yangName": "hosts", 
            "namespace": "hosts", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", 
            "name": "hosts"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys", 
            "isCurrent": true, 
            "yangName": "ipv4", 
            "namespace": "ipv4", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", 
            "keyLeaf": {
                "varName": "ipv4", 
                "defaultVal": null, 
                "typeHandler": "handler: Ipv4AddressHandlerPy"
            }, 
            "name": "ipv4"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-sys", 
            "memberName": "hostList", 
            "yangName": "host", 
            "className": "BlinkyHostMaapiList", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system.tech.system.name_resolution.static_resolution.hosts.ipv4.host.host_maapi_list_gen import BlinkyHostMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", 
            "moduleYangNamespacePrefix": "qt-sys", 
            "typeHandler": "handler: Ipv4AddressHandlerPy", 
            "memberName": "address", 
            "yangName": "address", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
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
            "qwilt_tech_system"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", 
            "moduleYangNamespacePrefix": "qt-sys", 
            "typeHandler": "handler: Ipv4AddressHandlerPy", 
            "memberName": "address", 
            "yangName": "address", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


