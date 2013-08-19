


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

from timeouts_maapi_base_gen import TimeoutsMaapiBase




class BlinkyTimeoutsMaapi(TimeoutsMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-timeouts")
        self.domain = None

        

        
        self.getLogicalDiskStatusRequested = False
        self.getLogicalDiskStatus = None
        self.getLogicalDiskStatusSet = False
        
        self.getPhysicalStatusRequested = False
        self.getPhysicalStatus = None
        self.getPhysicalStatusSet = False
        
        self.activateLogicalDiskRequested = False
        self.activateLogicalDisk = None
        self.activateLogicalDiskSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestGetLogicalDiskStatus(True)
        
        self.requestGetPhysicalStatus(True)
        
        self.requestActivateLogicalDisk(True)
        
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestGetLogicalDiskStatus(True)
        
        self.requestGetPhysicalStatus(True)
        
        self.requestActivateLogicalDisk(True)
        
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestGetLogicalDiskStatus(False)
        
        self.requestGetPhysicalStatus(False)
        
        self.requestActivateLogicalDisk(False)
        
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestGetLogicalDiskStatus(False)
        
        self.requestGetPhysicalStatus(False)
        
        self.requestActivateLogicalDisk(False)
        
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setGetLogicalDiskStatus(None)
        self.getLogicalDiskStatusSet = False
        
        self.setGetPhysicalStatus(None)
        self.getPhysicalStatusSet = False
        
        self.setActivateLogicalDisk(None)
        self.activateLogicalDiskSet = False
        
        

    def write (self
              , controller
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(controller, trxContext)

    def read (self
              , controller
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(controller, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , controller
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(controller, 
                                  True,
                                  trxContext)



    def requestGetLogicalDiskStatus (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-getlogicaldiskstatus').debug3Func(): logFunc('called. requested=%s', requested)
        self.getLogicalDiskStatusRequested = requested
        self.getLogicalDiskStatusSet = False

    def isGetLogicalDiskStatusRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-getlogicaldiskstatus-requested').debug3Func(): logFunc('called. requested=%s', self.getLogicalDiskStatusRequested)
        return self.getLogicalDiskStatusRequested

    def getGetLogicalDiskStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-getlogicaldiskstatus').debug3Func(): logFunc('called. self.getLogicalDiskStatusSet=%s, self.getLogicalDiskStatus=%s', self.getLogicalDiskStatusSet, self.getLogicalDiskStatus)
        if self.getLogicalDiskStatusSet:
            return self.getLogicalDiskStatus
        return None

    def hasGetLogicalDiskStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-getlogicaldiskstatus').debug3Func(): logFunc('called. self.getLogicalDiskStatusSet=%s, self.getLogicalDiskStatus=%s', self.getLogicalDiskStatusSet, self.getLogicalDiskStatus)
        if self.getLogicalDiskStatusSet:
            return True
        return False

    def setGetLogicalDiskStatus (self, getLogicalDiskStatus):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-getlogicaldiskstatus').debug3Func(): logFunc('called. getLogicalDiskStatus=%s, old=%s', getLogicalDiskStatus, self.getLogicalDiskStatus)
        self.getLogicalDiskStatusSet = True
        self.getLogicalDiskStatus = getLogicalDiskStatus

    def requestGetPhysicalStatus (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-getphysicalstatus').debug3Func(): logFunc('called. requested=%s', requested)
        self.getPhysicalStatusRequested = requested
        self.getPhysicalStatusSet = False

    def isGetPhysicalStatusRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-getphysicalstatus-requested').debug3Func(): logFunc('called. requested=%s', self.getPhysicalStatusRequested)
        return self.getPhysicalStatusRequested

    def getGetPhysicalStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-getphysicalstatus').debug3Func(): logFunc('called. self.getPhysicalStatusSet=%s, self.getPhysicalStatus=%s', self.getPhysicalStatusSet, self.getPhysicalStatus)
        if self.getPhysicalStatusSet:
            return self.getPhysicalStatus
        return None

    def hasGetPhysicalStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-getphysicalstatus').debug3Func(): logFunc('called. self.getPhysicalStatusSet=%s, self.getPhysicalStatus=%s', self.getPhysicalStatusSet, self.getPhysicalStatus)
        if self.getPhysicalStatusSet:
            return True
        return False

    def setGetPhysicalStatus (self, getPhysicalStatus):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-getphysicalstatus').debug3Func(): logFunc('called. getPhysicalStatus=%s, old=%s', getPhysicalStatus, self.getPhysicalStatus)
        self.getPhysicalStatusSet = True
        self.getPhysicalStatus = getPhysicalStatus

    def requestActivateLogicalDisk (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-activatelogicaldisk').debug3Func(): logFunc('called. requested=%s', requested)
        self.activateLogicalDiskRequested = requested
        self.activateLogicalDiskSet = False

    def isActivateLogicalDiskRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-activatelogicaldisk-requested').debug3Func(): logFunc('called. requested=%s', self.activateLogicalDiskRequested)
        return self.activateLogicalDiskRequested

    def getActivateLogicalDisk (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-activatelogicaldisk').debug3Func(): logFunc('called. self.activateLogicalDiskSet=%s, self.activateLogicalDisk=%s', self.activateLogicalDiskSet, self.activateLogicalDisk)
        if self.activateLogicalDiskSet:
            return self.activateLogicalDisk
        return None

    def hasActivateLogicalDisk (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-activatelogicaldisk').debug3Func(): logFunc('called. self.activateLogicalDiskSet=%s, self.activateLogicalDisk=%s', self.activateLogicalDiskSet, self.activateLogicalDisk)
        if self.activateLogicalDiskSet:
            return True
        return False

    def setActivateLogicalDisk (self, activateLogicalDisk):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-activatelogicaldisk').debug3Func(): logFunc('called. activateLogicalDisk=%s, old=%s', activateLogicalDisk, self.activateLogicalDisk)
        self.activateLogicalDiskSet = True
        self.activateLogicalDisk = activateLogicalDisk


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.getLogicalDiskStatus = 0
        self.getLogicalDiskStatusSet = False
        
        self.getPhysicalStatus = 0
        self.getPhysicalStatusSet = False
        
        self.activateLogicalDisk = 0
        self.activateLogicalDiskSet = False
        

    def _getSelfKeyPath (self, controller
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("timeouts", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", "qt-strg-ctrl"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", "qt-strg-ctrl"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(controller);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("controller", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", "qt-strg-ctrl"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("storage", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage", "qt-strg"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        controller, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(controller, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(controller, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       controller, 
                       
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

        keyPath = self._getSelfKeyPath(controller, 
                                       
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
                               controller, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasGetLogicalDiskStatus():
            valGetLogicalDiskStatus = Value()
            if self.getLogicalDiskStatus is not None:
                valGetLogicalDiskStatus.setInt64(self.getLogicalDiskStatus)
            else:
                valGetLogicalDiskStatus.setEmpty()
            tagValueList.push(("get-logical-disk-status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller"), valGetLogicalDiskStatus)
        
        if self.hasGetPhysicalStatus():
            valGetPhysicalStatus = Value()
            if self.getPhysicalStatus is not None:
                valGetPhysicalStatus.setInt64(self.getPhysicalStatus)
            else:
                valGetPhysicalStatus.setEmpty()
            tagValueList.push(("get-physical-status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller"), valGetPhysicalStatus)
        
        if self.hasActivateLogicalDisk():
            valActivateLogicalDisk = Value()
            if self.activateLogicalDisk is not None:
                valActivateLogicalDisk.setInt64(self.activateLogicalDisk)
            else:
                valActivateLogicalDisk.setEmpty()
            tagValueList.push(("activate-logical-disk", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller"), valActivateLogicalDisk)
        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isGetLogicalDiskStatusRequested():
            valGetLogicalDiskStatus = Value()
            valGetLogicalDiskStatus.setEmpty()
            tagValueList.push(("get-logical-disk-status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller"), valGetLogicalDiskStatus)
        
        if self.isGetPhysicalStatusRequested():
            valGetPhysicalStatus = Value()
            valGetPhysicalStatus.setEmpty()
            tagValueList.push(("get-physical-status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller"), valGetPhysicalStatus)
        
        if self.isActivateLogicalDiskRequested():
            valActivateLogicalDisk = Value()
            valActivateLogicalDisk.setEmpty()
            tagValueList.push(("activate-logical-disk", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller"), valActivateLogicalDisk)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isGetLogicalDiskStatusRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "get-logical-disk-status") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-getlogicaldiskstatus').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "getLogicalDiskStatus", "get-logical-disk-status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-get-logical-disk-status-bad-value').infoFunc(): logFunc('getLogicalDiskStatus not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setGetLogicalDiskStatus(tempVar)
            for logFunc in self._log('read-tag-values-get-logical-disk-status').debug3Func(): logFunc('read getLogicalDiskStatus. getLogicalDiskStatus=%s, tempValue=%s', self.getLogicalDiskStatus, tempValue.getType())
        
        if self.isGetPhysicalStatusRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "get-physical-status") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-getphysicalstatus').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "getPhysicalStatus", "get-physical-status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-get-physical-status-bad-value').infoFunc(): logFunc('getPhysicalStatus not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setGetPhysicalStatus(tempVar)
            for logFunc in self._log('read-tag-values-get-physical-status').debug3Func(): logFunc('read getPhysicalStatus. getPhysicalStatus=%s, tempValue=%s', self.getPhysicalStatus, tempValue.getType())
        
        if self.isActivateLogicalDiskRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "activate-logical-disk") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-activatelogicaldisk').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "activateLogicalDisk", "activate-logical-disk", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-activate-logical-disk-bad-value').infoFunc(): logFunc('activateLogicalDisk not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setActivateLogicalDisk(tempVar)
            for logFunc in self._log('read-tag-values-activate-logical-disk').debug3Func(): logFunc('read activateLogicalDisk. activateLogicalDisk=%s, tempValue=%s', self.activateLogicalDisk, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "timeouts", 
        "namespace": "timeouts", 
        "className": "TimeoutsMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_controller.tech.storage.controller.system_defaults.timeouts.timeouts_maapi_gen import TimeoutsMaapi", 
        "baseClassName": "TimeoutsMaapiBase", 
        "baseModule": "timeouts_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-strg", 
            "yangName": "storage", 
            "namespace": "storage", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage", 
            "name": "storage"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "isCurrent": false, 
            "yangName": "controller", 
            "namespace": "controller", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "keyLeaf": {
                "varName": "controller", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "controller"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "name": "system-defaults"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "yangName": "timeouts", 
            "namespace": "timeouts", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "name": "timeouts"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "getLogicalDiskStatus", 
            "yangName": "get-logical-disk-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "getPhysicalStatus", 
            "yangName": "get-physical-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "activateLogicalDisk", 
            "yangName": "activate-logical-disk", 
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
            "common", 
            "qwilt_tech_storage_controller"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "getLogicalDiskStatus", 
            "yangName": "get-logical-disk-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "getPhysicalStatus", 
            "yangName": "get-physical-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "activateLogicalDisk", 
            "yangName": "activate-logical-disk", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


