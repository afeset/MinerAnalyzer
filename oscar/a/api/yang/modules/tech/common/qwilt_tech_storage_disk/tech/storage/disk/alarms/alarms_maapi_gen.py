


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


from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import ContentDiskFailureReasonType


class BlinkyAlarmsMaapi(AlarmsMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-alarms")
        self.domain = None

        

        
        self.contentDiskFailureReasonRequested = False
        self.contentDiskFailureReason = None
        self.contentDiskFailureReasonSet = False
        
        self.contentDiskFailureAlarmRequested = False
        self.contentDiskFailureAlarm = None
        self.contentDiskFailureAlarmSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestContentDiskFailureReason(True)
        
        self.requestContentDiskFailureAlarm(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestContentDiskFailureReason(False)
        
        self.requestContentDiskFailureAlarm(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestContentDiskFailureReason(True)
        
        self.requestContentDiskFailureAlarm(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestContentDiskFailureReason(False)
        
        self.requestContentDiskFailureAlarm(False)
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        

    def write (self
              , disk
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(disk, trxContext)

    def read (self
              , disk
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(disk, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , disk
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(disk, 
                                  True,
                                  trxContext)



    def requestContentDiskFailureReason (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-contentdiskfailurereason').debug3Func(): logFunc('called. requested=%s', requested)
        self.contentDiskFailureReasonRequested = requested
        self.contentDiskFailureReasonSet = False

    def isContentDiskFailureReasonRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-contentdiskfailurereason-requested').debug3Func(): logFunc('called. requested=%s', self.contentDiskFailureReasonRequested)
        return self.contentDiskFailureReasonRequested

    def getContentDiskFailureReason (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-contentdiskfailurereason').debug3Func(): logFunc('called. self.contentDiskFailureReasonSet=%s, self.contentDiskFailureReason=%s', self.contentDiskFailureReasonSet, self.contentDiskFailureReason)
        if self.contentDiskFailureReasonSet:
            return self.contentDiskFailureReason
        return None

    def hasContentDiskFailureReason (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-contentdiskfailurereason').debug3Func(): logFunc('called. self.contentDiskFailureReasonSet=%s, self.contentDiskFailureReason=%s', self.contentDiskFailureReasonSet, self.contentDiskFailureReason)
        if self.contentDiskFailureReasonSet:
            return True
        return False

    def setContentDiskFailureReason (self, contentDiskFailureReason):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-contentdiskfailurereason').debug3Func(): logFunc('called. contentDiskFailureReason=%s, old=%s', contentDiskFailureReason, self.contentDiskFailureReason)
        self.contentDiskFailureReasonSet = True
        self.contentDiskFailureReason = contentDiskFailureReason

    def requestContentDiskFailureAlarm (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-contentdiskfailurealarm').debug3Func(): logFunc('called. requested=%s', requested)
        self.contentDiskFailureAlarmRequested = requested
        self.contentDiskFailureAlarmSet = False

    def isContentDiskFailureAlarmRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-contentdiskfailurealarm-requested').debug3Func(): logFunc('called. requested=%s', self.contentDiskFailureAlarmRequested)
        return self.contentDiskFailureAlarmRequested

    def getContentDiskFailureAlarm (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-contentdiskfailurealarm').debug3Func(): logFunc('called. self.contentDiskFailureAlarmSet=%s, self.contentDiskFailureAlarm=%s', self.contentDiskFailureAlarmSet, self.contentDiskFailureAlarm)
        if self.contentDiskFailureAlarmSet:
            return self.contentDiskFailureAlarm
        return None

    def hasContentDiskFailureAlarm (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-contentdiskfailurealarm').debug3Func(): logFunc('called. self.contentDiskFailureAlarmSet=%s, self.contentDiskFailureAlarm=%s', self.contentDiskFailureAlarmSet, self.contentDiskFailureAlarm)
        if self.contentDiskFailureAlarmSet:
            return True
        return False

    def setContentDiskFailureAlarm (self, contentDiskFailureAlarm):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-contentdiskfailurealarm').debug3Func(): logFunc('called. contentDiskFailureAlarm=%s, old=%s', contentDiskFailureAlarm, self.contentDiskFailureAlarm)
        self.contentDiskFailureAlarmSet = True
        self.contentDiskFailureAlarm = contentDiskFailureAlarm


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.contentDiskFailureReason = 0
        self.contentDiskFailureReasonSet = False
        
        self.contentDiskFailureAlarm = 0
        self.contentDiskFailureAlarmSet = False
        

    def _getSelfKeyPath (self, disk
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("alarms", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(disk);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("disk", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk"))
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
                        disk, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(disk, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(disk, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       disk, 
                       
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

        keyPath = self._getSelfKeyPath(disk, 
                                       
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
                               disk, 
                               
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

        
        if self.isContentDiskFailureReasonRequested():
            valContentDiskFailureReason = Value()
            valContentDiskFailureReason.setEmpty()
            tagValueList.push(("content-disk-failure-reason", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valContentDiskFailureReason)
        
        if self.isContentDiskFailureAlarmRequested():
            valContentDiskFailureAlarm = Value()
            valContentDiskFailureAlarm.setEmpty()
            tagValueList.push(("content-disk-failure-alarm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valContentDiskFailureAlarm)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isContentDiskFailureReasonRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "content-disk-failure-reason") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-contentdiskfailurereason').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "contentDiskFailureReason", "content-disk-failure-reason", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-content-disk-failure-reason-bad-value').infoFunc(): logFunc('contentDiskFailureReason not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setContentDiskFailureReason(tempVar)
            for logFunc in self._log('read-tag-values-content-disk-failure-reason').debug3Func(): logFunc('read contentDiskFailureReason. contentDiskFailureReason=%s, tempValue=%s', self.contentDiskFailureReason, tempValue.getType())
        
        if self.isContentDiskFailureAlarmRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "content-disk-failure-alarm") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-contentdiskfailurealarm').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "contentDiskFailureAlarm", "content-disk-failure-alarm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-content-disk-failure-alarm-bad-value').infoFunc(): logFunc('contentDiskFailureAlarm not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setContentDiskFailureAlarm(tempVar)
            for logFunc in self._log('read-tag-values-content-disk-failure-alarm').debug3Func(): logFunc('read contentDiskFailureAlarm. contentDiskFailureAlarm=%s, tempValue=%s', self.contentDiskFailureAlarm, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "alarms", 
        "namespace": "alarms", 
        "className": "AlarmsMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.alarms.alarms_maapi_gen import AlarmsMaapi", 
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
            "moduleYangNamespacePrefix": "qt-strg", 
            "yangName": "storage", 
            "namespace": "storage", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage", 
            "name": "storage"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "isCurrent": false, 
            "yangName": "disk", 
            "namespace": "disk", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "keyLeaf": {
                "varName": "disk", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "disk"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "yangName": "alarms", 
            "namespace": "alarms", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "name": "alarms"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "contentDiskFailureReason", 
            "yangName": "content-disk-failure-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "contentDiskFailureAlarm", 
            "yangName": "content-disk-failure-alarm", 
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
            "qwilt_tech_storage_disk"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "contentDiskFailureReason", 
            "yangName": "content-disk-failure-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "contentDiskFailureAlarm", 
            "yangName": "content-disk-failure-alarm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


