


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

from status_maapi_base_gen import StatusMaapiBase


from a.api.yang.modules.tech.common.qwilt_tech_interfaces.qwilt_tech_interfaces_module_gen import DriverTypeType


class BlinkyStatusMaapi(StatusMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-status")
        self.domain = None

        

        
        self.driverTypeRequested = False
        self.driverType = None
        self.driverTypeSet = False
        
        self.pciAddressRequested = False
        self.pciAddress = None
        self.pciAddressSet = False
        
        self.routeTableIdRequested = False
        self.routeTableId = None
        self.routeTableIdSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestDriverType(True)
        
        self.requestPciAddress(True)
        
        self.requestRouteTableId(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestDriverType(False)
        
        self.requestPciAddress(False)
        
        self.requestRouteTableId(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestDriverType(True)
        
        self.requestPciAddress(True)
        
        self.requestRouteTableId(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestDriverType(False)
        
        self.requestPciAddress(False)
        
        self.requestRouteTableId(False)
        
        

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



    def requestDriverType (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-drivertype').debug3Func(): logFunc('called. requested=%s', requested)
        self.driverTypeRequested = requested
        self.driverTypeSet = False

    def isDriverTypeRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-drivertype-requested').debug3Func(): logFunc('called. requested=%s', self.driverTypeRequested)
        return self.driverTypeRequested

    def getDriverType (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-drivertype').debug3Func(): logFunc('called. self.driverTypeSet=%s, self.driverType=%s', self.driverTypeSet, self.driverType)
        if self.driverTypeSet:
            return self.driverType
        return None

    def hasDriverType (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-drivertype').debug3Func(): logFunc('called. self.driverTypeSet=%s, self.driverType=%s', self.driverTypeSet, self.driverType)
        if self.driverTypeSet:
            return True
        return False

    def setDriverType (self, driverType):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-drivertype').debug3Func(): logFunc('called. driverType=%s, old=%s', driverType, self.driverType)
        self.driverTypeSet = True
        self.driverType = driverType

    def requestPciAddress (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-pciaddress').debug3Func(): logFunc('called. requested=%s', requested)
        self.pciAddressRequested = requested
        self.pciAddressSet = False

    def isPciAddressRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-pciaddress-requested').debug3Func(): logFunc('called. requested=%s', self.pciAddressRequested)
        return self.pciAddressRequested

    def getPciAddress (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-pciaddress').debug3Func(): logFunc('called. self.pciAddressSet=%s, self.pciAddress=%s', self.pciAddressSet, self.pciAddress)
        if self.pciAddressSet:
            return self.pciAddress
        return None

    def hasPciAddress (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-pciaddress').debug3Func(): logFunc('called. self.pciAddressSet=%s, self.pciAddress=%s', self.pciAddressSet, self.pciAddress)
        if self.pciAddressSet:
            return True
        return False

    def setPciAddress (self, pciAddress):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-pciaddress').debug3Func(): logFunc('called. pciAddress=%s, old=%s', pciAddress, self.pciAddress)
        self.pciAddressSet = True
        self.pciAddress = pciAddress

    def requestRouteTableId (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-routetableid').debug3Func(): logFunc('called. requested=%s', requested)
        self.routeTableIdRequested = requested
        self.routeTableIdSet = False

    def isRouteTableIdRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-routetableid-requested').debug3Func(): logFunc('called. requested=%s', self.routeTableIdRequested)
        return self.routeTableIdRequested

    def getRouteTableId (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-routetableid').debug3Func(): logFunc('called. self.routeTableIdSet=%s, self.routeTableId=%s', self.routeTableIdSet, self.routeTableId)
        if self.routeTableIdSet:
            return self.routeTableId
        return None

    def hasRouteTableId (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-routetableid').debug3Func(): logFunc('called. self.routeTableIdSet=%s, self.routeTableId=%s', self.routeTableIdSet, self.routeTableId)
        if self.routeTableIdSet:
            return True
        return False

    def setRouteTableId (self, routeTableId):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-routetableid').debug3Func(): logFunc('called. routeTableId=%s, old=%s', routeTableId, self.routeTableId)
        self.routeTableIdSet = True
        self.routeTableId = routeTableId


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.driverType = 0
        self.driverTypeSet = False
        
        self.pciAddress = 0
        self.pciAddressSet = False
        
        self.routeTableId = 0
        self.routeTableIdSet = False
        

    def _getSelfKeyPath (self, interface
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("device", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
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

        
        if self.isDriverTypeRequested():
            valDriverType = Value()
            valDriverType.setEmpty()
            tagValueList.push(("driver-type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valDriverType)
        
        if self.isPciAddressRequested():
            valPciAddress = Value()
            valPciAddress.setEmpty()
            tagValueList.push(("pci-address", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valPciAddress)
        
        if self.isRouteTableIdRequested():
            valRouteTableId = Value()
            valRouteTableId.setEmpty()
            tagValueList.push(("route-table-id", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valRouteTableId)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isDriverTypeRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "driver-type") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-drivertype').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "driverType", "driver-type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-driver-type-bad-value').infoFunc(): logFunc('driverType not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setDriverType(tempVar)
            for logFunc in self._log('read-tag-values-driver-type').debug3Func(): logFunc('read driverType. driverType=%s, tempValue=%s', self.driverType, tempValue.getType())
        
        if self.isPciAddressRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "pci-address") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-pciaddress').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "pciAddress", "pci-address", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-pci-address-bad-value').infoFunc(): logFunc('pciAddress not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPciAddress(tempVar)
            for logFunc in self._log('read-tag-values-pci-address').debug3Func(): logFunc('read pciAddress. pciAddress=%s, tempValue=%s', self.pciAddress, tempValue.getType())
        
        if self.isRouteTableIdRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "route-table-id") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-routetableid').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "routeTableId", "route-table-id", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-route-table-id-bad-value').infoFunc(): logFunc('routeTableId not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setRouteTableId(tempVar)
            for logFunc in self._log('read-tag-values-route-table-id').debug3Func(): logFunc('read routeTableId. routeTableId=%s, tempValue=%s', self.routeTableId, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "status", 
        "namespace": "status", 
        "className": "StatusMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.device.status.status_maapi_gen import StatusMaapi", 
        "baseClassName": "StatusMaapiBase", 
        "baseModule": "status_maapi_base_gen"
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
            "yangName": "device", 
            "namespace": "device", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "device"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "status", 
            "namespace": "status", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "status"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "driverType", 
            "yangName": "driver-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "pciAddress", 
            "yangName": "pci-address", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "routeTableId", 
            "yangName": "route-table-id", 
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
            "memberName": "driverType", 
            "yangName": "driver-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "pciAddress", 
            "yangName": "pci-address", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "routeTableId", 
            "yangName": "route-table-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


