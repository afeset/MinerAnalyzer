


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




class BlinkyStatusMaapi(StatusMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-status")
        self.domain = None

        

        
        self.tableLastChangeTicksRequested = False
        self.tableLastChangeTicks = None
        self.tableLastChangeTicksSet = False
        
        self.interfaceNumberRequested = False
        self.interfaceNumber = None
        self.interfaceNumberSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestTableLastChangeTicks(True)
        
        self.requestInterfaceNumber(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestTableLastChangeTicks(False)
        
        self.requestInterfaceNumber(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestTableLastChangeTicks(True)
        
        self.requestInterfaceNumber(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestTableLastChangeTicks(False)
        
        self.requestInterfaceNumber(False)
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        

    def write (self
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(trxContext)

    def read (self
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(
                                  True,
                                  trxContext)



    def requestTableLastChangeTicks (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-tablelastchangeticks').debug3Func(): logFunc('called. requested=%s', requested)
        self.tableLastChangeTicksRequested = requested
        self.tableLastChangeTicksSet = False

    def isTableLastChangeTicksRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-tablelastchangeticks-requested').debug3Func(): logFunc('called. requested=%s', self.tableLastChangeTicksRequested)
        return self.tableLastChangeTicksRequested

    def getTableLastChangeTicks (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-tablelastchangeticks').debug3Func(): logFunc('called. self.tableLastChangeTicksSet=%s, self.tableLastChangeTicks=%s', self.tableLastChangeTicksSet, self.tableLastChangeTicks)
        if self.tableLastChangeTicksSet:
            return self.tableLastChangeTicks
        return None

    def hasTableLastChangeTicks (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-tablelastchangeticks').debug3Func(): logFunc('called. self.tableLastChangeTicksSet=%s, self.tableLastChangeTicks=%s', self.tableLastChangeTicksSet, self.tableLastChangeTicks)
        if self.tableLastChangeTicksSet:
            return True
        return False

    def setTableLastChangeTicks (self, tableLastChangeTicks):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-tablelastchangeticks').debug3Func(): logFunc('called. tableLastChangeTicks=%s, old=%s', tableLastChangeTicks, self.tableLastChangeTicks)
        self.tableLastChangeTicksSet = True
        self.tableLastChangeTicks = tableLastChangeTicks

    def requestInterfaceNumber (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-interfacenumber').debug3Func(): logFunc('called. requested=%s', requested)
        self.interfaceNumberRequested = requested
        self.interfaceNumberSet = False

    def isInterfaceNumberRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-interfacenumber-requested').debug3Func(): logFunc('called. requested=%s', self.interfaceNumberRequested)
        return self.interfaceNumberRequested

    def getInterfaceNumber (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-interfacenumber').debug3Func(): logFunc('called. self.interfaceNumberSet=%s, self.interfaceNumber=%s', self.interfaceNumberSet, self.interfaceNumber)
        if self.interfaceNumberSet:
            return self.interfaceNumber
        return None

    def hasInterfaceNumber (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-interfacenumber').debug3Func(): logFunc('called. self.interfaceNumberSet=%s, self.interfaceNumber=%s', self.interfaceNumberSet, self.interfaceNumber)
        if self.interfaceNumberSet:
            return True
        return False

    def setInterfaceNumber (self, interfaceNumber):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-interfacenumber').debug3Func(): logFunc('called. interfaceNumber=%s, old=%s', interfaceNumber, self.interfaceNumber)
        self.interfaceNumberSet = True
        self.interfaceNumber = interfaceNumber


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.tableLastChangeTicks = 0
        self.tableLastChangeTicksSet = False
        
        self.interfaceNumber = 0
        self.interfaceNumberSet = False
        

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
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
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       
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

        keyPath = self._getSelfKeyPath(
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

        
        if self.isTableLastChangeTicksRequested():
            valTableLastChangeTicks = Value()
            valTableLastChangeTicks.setEmpty()
            tagValueList.push(("table-last-change-ticks", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valTableLastChangeTicks)
        
        if self.isInterfaceNumberRequested():
            valInterfaceNumber = Value()
            valInterfaceNumber.setEmpty()
            tagValueList.push(("interface-number", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valInterfaceNumber)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isTableLastChangeTicksRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "table-last-change-ticks") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-tablelastchangeticks').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "tableLastChangeTicks", "table-last-change-ticks", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint32()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-table-last-change-ticks-bad-value').infoFunc(): logFunc('tableLastChangeTicks not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTableLastChangeTicks(tempVar)
            for logFunc in self._log('read-tag-values-table-last-change-ticks').debug3Func(): logFunc('read tableLastChangeTicks. tableLastChangeTicks=%s, tempValue=%s', self.tableLastChangeTicks, tempValue.getType())
        
        if self.isInterfaceNumberRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "interface-number") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-interfacenumber').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "interfaceNumber", "interface-number", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt32()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-interface-number-bad-value').infoFunc(): logFunc('interfaceNumber not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setInterfaceNumber(tempVar)
            for logFunc in self._log('read-tag-values-interface-number').debug3Func(): logFunc('read interfaceNumber. interfaceNumber=%s, tempValue=%s', self.interfaceNumber, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "status", 
        "namespace": "status", 
        "className": "StatusMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.status.status_maapi_gen import StatusMaapi", 
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
            "typeHandler": "handler: IntHandler", 
            "memberName": "tableLastChangeTicks", 
            "yangName": "table-last-change-ticks", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "interfaceNumber", 
            "yangName": "interface-number", 
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
            "typeHandler": "handler: IntHandler", 
            "memberName": "tableLastChangeTicks", 
            "yangName": "table-last-change-ticks", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "interfaceNumber", 
            "yangName": "interface-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


