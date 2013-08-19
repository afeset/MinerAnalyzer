


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


from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import FileSystemTypeType
from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import FileSystemOperationalStatusType
from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import FileSystemOperationalStatusReasonType


class BlinkyStatusMaapi(StatusMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-status")
        self.domain = None

        

        
        self.uuidRequested = False
        self.uuid = None
        self.uuidSet = False
        
        self.operationalStatusRequested = False
        self.operationalStatus = None
        self.operationalStatusSet = False
        
        self.fileSystemTypeRawRequested = False
        self.fileSystemTypeRaw = None
        self.fileSystemTypeRawSet = False
        
        self.fileSystemTypeRequested = False
        self.fileSystemType = None
        self.fileSystemTypeSet = False
        
        self.expectedUuidRequested = False
        self.expectedUuid = None
        self.expectedUuidSet = False
        
        self.operationalStatusReasonRequested = False
        self.operationalStatusReason = None
        self.operationalStatusReasonSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestUuid(True)
        
        self.requestOperationalStatus(True)
        
        self.requestFileSystemTypeRaw(True)
        
        self.requestFileSystemType(True)
        
        self.requestExpectedUuid(True)
        
        self.requestOperationalStatusReason(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestUuid(False)
        
        self.requestOperationalStatus(False)
        
        self.requestFileSystemTypeRaw(False)
        
        self.requestFileSystemType(False)
        
        self.requestExpectedUuid(False)
        
        self.requestOperationalStatusReason(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestUuid(True)
        
        self.requestOperationalStatus(True)
        
        self.requestFileSystemTypeRaw(True)
        
        self.requestFileSystemType(True)
        
        self.requestExpectedUuid(True)
        
        self.requestOperationalStatusReason(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestUuid(False)
        
        self.requestOperationalStatus(False)
        
        self.requestFileSystemTypeRaw(False)
        
        self.requestFileSystemType(False)
        
        self.requestExpectedUuid(False)
        
        self.requestOperationalStatusReason(False)
        
        

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



    def requestUuid (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-uuid').debug3Func(): logFunc('called. requested=%s', requested)
        self.uuidRequested = requested
        self.uuidSet = False

    def isUuidRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-uuid-requested').debug3Func(): logFunc('called. requested=%s', self.uuidRequested)
        return self.uuidRequested

    def getUuid (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-uuid').debug3Func(): logFunc('called. self.uuidSet=%s, self.uuid=%s', self.uuidSet, self.uuid)
        if self.uuidSet:
            return self.uuid
        return None

    def hasUuid (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-uuid').debug3Func(): logFunc('called. self.uuidSet=%s, self.uuid=%s', self.uuidSet, self.uuid)
        if self.uuidSet:
            return True
        return False

    def setUuid (self, uuid):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-uuid').debug3Func(): logFunc('called. uuid=%s, old=%s', uuid, self.uuid)
        self.uuidSet = True
        self.uuid = uuid

    def requestOperationalStatus (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-operationalstatus').debug3Func(): logFunc('called. requested=%s', requested)
        self.operationalStatusRequested = requested
        self.operationalStatusSet = False

    def isOperationalStatusRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-operationalstatus-requested').debug3Func(): logFunc('called. requested=%s', self.operationalStatusRequested)
        return self.operationalStatusRequested

    def getOperationalStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-operationalstatus').debug3Func(): logFunc('called. self.operationalStatusSet=%s, self.operationalStatus=%s', self.operationalStatusSet, self.operationalStatus)
        if self.operationalStatusSet:
            return self.operationalStatus
        return None

    def hasOperationalStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-operationalstatus').debug3Func(): logFunc('called. self.operationalStatusSet=%s, self.operationalStatus=%s', self.operationalStatusSet, self.operationalStatus)
        if self.operationalStatusSet:
            return True
        return False

    def setOperationalStatus (self, operationalStatus):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-operationalstatus').debug3Func(): logFunc('called. operationalStatus=%s, old=%s', operationalStatus, self.operationalStatus)
        self.operationalStatusSet = True
        self.operationalStatus = operationalStatus

    def requestFileSystemTypeRaw (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-filesystemtyperaw').debug3Func(): logFunc('called. requested=%s', requested)
        self.fileSystemTypeRawRequested = requested
        self.fileSystemTypeRawSet = False

    def isFileSystemTypeRawRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-filesystemtyperaw-requested').debug3Func(): logFunc('called. requested=%s', self.fileSystemTypeRawRequested)
        return self.fileSystemTypeRawRequested

    def getFileSystemTypeRaw (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-filesystemtyperaw').debug3Func(): logFunc('called. self.fileSystemTypeRawSet=%s, self.fileSystemTypeRaw=%s', self.fileSystemTypeRawSet, self.fileSystemTypeRaw)
        if self.fileSystemTypeRawSet:
            return self.fileSystemTypeRaw
        return None

    def hasFileSystemTypeRaw (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-filesystemtyperaw').debug3Func(): logFunc('called. self.fileSystemTypeRawSet=%s, self.fileSystemTypeRaw=%s', self.fileSystemTypeRawSet, self.fileSystemTypeRaw)
        if self.fileSystemTypeRawSet:
            return True
        return False

    def setFileSystemTypeRaw (self, fileSystemTypeRaw):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-filesystemtyperaw').debug3Func(): logFunc('called. fileSystemTypeRaw=%s, old=%s', fileSystemTypeRaw, self.fileSystemTypeRaw)
        self.fileSystemTypeRawSet = True
        self.fileSystemTypeRaw = fileSystemTypeRaw

    def requestFileSystemType (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-filesystemtype').debug3Func(): logFunc('called. requested=%s', requested)
        self.fileSystemTypeRequested = requested
        self.fileSystemTypeSet = False

    def isFileSystemTypeRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-filesystemtype-requested').debug3Func(): logFunc('called. requested=%s', self.fileSystemTypeRequested)
        return self.fileSystemTypeRequested

    def getFileSystemType (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-filesystemtype').debug3Func(): logFunc('called. self.fileSystemTypeSet=%s, self.fileSystemType=%s', self.fileSystemTypeSet, self.fileSystemType)
        if self.fileSystemTypeSet:
            return self.fileSystemType
        return None

    def hasFileSystemType (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-filesystemtype').debug3Func(): logFunc('called. self.fileSystemTypeSet=%s, self.fileSystemType=%s', self.fileSystemTypeSet, self.fileSystemType)
        if self.fileSystemTypeSet:
            return True
        return False

    def setFileSystemType (self, fileSystemType):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-filesystemtype').debug3Func(): logFunc('called. fileSystemType=%s, old=%s', fileSystemType, self.fileSystemType)
        self.fileSystemTypeSet = True
        self.fileSystemType = fileSystemType

    def requestExpectedUuid (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-expecteduuid').debug3Func(): logFunc('called. requested=%s', requested)
        self.expectedUuidRequested = requested
        self.expectedUuidSet = False

    def isExpectedUuidRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-expecteduuid-requested').debug3Func(): logFunc('called. requested=%s', self.expectedUuidRequested)
        return self.expectedUuidRequested

    def getExpectedUuid (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-expecteduuid').debug3Func(): logFunc('called. self.expectedUuidSet=%s, self.expectedUuid=%s', self.expectedUuidSet, self.expectedUuid)
        if self.expectedUuidSet:
            return self.expectedUuid
        return None

    def hasExpectedUuid (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-expecteduuid').debug3Func(): logFunc('called. self.expectedUuidSet=%s, self.expectedUuid=%s', self.expectedUuidSet, self.expectedUuid)
        if self.expectedUuidSet:
            return True
        return False

    def setExpectedUuid (self, expectedUuid):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-expecteduuid').debug3Func(): logFunc('called. expectedUuid=%s, old=%s', expectedUuid, self.expectedUuid)
        self.expectedUuidSet = True
        self.expectedUuid = expectedUuid

    def requestOperationalStatusReason (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-operationalstatusreason').debug3Func(): logFunc('called. requested=%s', requested)
        self.operationalStatusReasonRequested = requested
        self.operationalStatusReasonSet = False

    def isOperationalStatusReasonRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-operationalstatusreason-requested').debug3Func(): logFunc('called. requested=%s', self.operationalStatusReasonRequested)
        return self.operationalStatusReasonRequested

    def getOperationalStatusReason (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-operationalstatusreason').debug3Func(): logFunc('called. self.operationalStatusReasonSet=%s, self.operationalStatusReason=%s', self.operationalStatusReasonSet, self.operationalStatusReason)
        if self.operationalStatusReasonSet:
            return self.operationalStatusReason
        return None

    def hasOperationalStatusReason (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-operationalstatusreason').debug3Func(): logFunc('called. self.operationalStatusReasonSet=%s, self.operationalStatusReason=%s', self.operationalStatusReasonSet, self.operationalStatusReason)
        if self.operationalStatusReasonSet:
            return True
        return False

    def setOperationalStatusReason (self, operationalStatusReason):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-operationalstatusreason').debug3Func(): logFunc('called. operationalStatusReason=%s, old=%s', operationalStatusReason, self.operationalStatusReason)
        self.operationalStatusReasonSet = True
        self.operationalStatusReason = operationalStatusReason


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.uuid = 0
        self.uuidSet = False
        
        self.operationalStatus = 0
        self.operationalStatusSet = False
        
        self.fileSystemTypeRaw = 0
        self.fileSystemTypeRawSet = False
        
        self.fileSystemType = 0
        self.fileSystemTypeSet = False
        
        self.expectedUuid = 0
        self.expectedUuidSet = False
        
        self.operationalStatusReason = 0
        self.operationalStatusReasonSet = False
        

    def _getSelfKeyPath (self, disk
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("file-system", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk"))
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

        
        if self.isUuidRequested():
            valUuid = Value()
            valUuid.setEmpty()
            tagValueList.push(("uuid", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valUuid)
        
        if self.isOperationalStatusRequested():
            valOperationalStatus = Value()
            valOperationalStatus.setEmpty()
            tagValueList.push(("operational-status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valOperationalStatus)
        
        if self.isFileSystemTypeRawRequested():
            valFileSystemTypeRaw = Value()
            valFileSystemTypeRaw.setEmpty()
            tagValueList.push(("file-system-type-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valFileSystemTypeRaw)
        
        if self.isFileSystemTypeRequested():
            valFileSystemType = Value()
            valFileSystemType.setEmpty()
            tagValueList.push(("file-system-type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valFileSystemType)
        
        if self.isExpectedUuidRequested():
            valExpectedUuid = Value()
            valExpectedUuid.setEmpty()
            tagValueList.push(("expected-uuid", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valExpectedUuid)
        
        if self.isOperationalStatusReasonRequested():
            valOperationalStatusReason = Value()
            valOperationalStatusReason.setEmpty()
            tagValueList.push(("operational-status-reason", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valOperationalStatusReason)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isUuidRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "uuid") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-uuid').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "uuid", "uuid", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-uuid-bad-value').infoFunc(): logFunc('uuid not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setUuid(tempVar)
            for logFunc in self._log('read-tag-values-uuid').debug3Func(): logFunc('read uuid. uuid=%s, tempValue=%s', self.uuid, tempValue.getType())
        
        if self.isOperationalStatusRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "operational-status") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-operationalstatus').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "operationalStatus", "operational-status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-operational-status-bad-value').infoFunc(): logFunc('operationalStatus not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOperationalStatus(tempVar)
            for logFunc in self._log('read-tag-values-operational-status').debug3Func(): logFunc('read operationalStatus. operationalStatus=%s, tempValue=%s', self.operationalStatus, tempValue.getType())
        
        if self.isFileSystemTypeRawRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "file-system-type-raw") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-filesystemtyperaw').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "fileSystemTypeRaw", "file-system-type-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-file-system-type-raw-bad-value').infoFunc(): logFunc('fileSystemTypeRaw not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setFileSystemTypeRaw(tempVar)
            for logFunc in self._log('read-tag-values-file-system-type-raw').debug3Func(): logFunc('read fileSystemTypeRaw. fileSystemTypeRaw=%s, tempValue=%s', self.fileSystemTypeRaw, tempValue.getType())
        
        if self.isFileSystemTypeRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "file-system-type") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-filesystemtype').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "fileSystemType", "file-system-type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-file-system-type-bad-value').infoFunc(): logFunc('fileSystemType not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setFileSystemType(tempVar)
            for logFunc in self._log('read-tag-values-file-system-type').debug3Func(): logFunc('read fileSystemType. fileSystemType=%s, tempValue=%s', self.fileSystemType, tempValue.getType())
        
        if self.isExpectedUuidRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "expected-uuid") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-expecteduuid').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "expectedUuid", "expected-uuid", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-expected-uuid-bad-value').infoFunc(): logFunc('expectedUuid not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setExpectedUuid(tempVar)
            for logFunc in self._log('read-tag-values-expected-uuid').debug3Func(): logFunc('read expectedUuid. expectedUuid=%s, tempValue=%s', self.expectedUuid, tempValue.getType())
        
        if self.isOperationalStatusReasonRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "operational-status-reason") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-operationalstatusreason').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "operationalStatusReason", "operational-status-reason", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-operational-status-reason-bad-value').infoFunc(): logFunc('operationalStatusReason not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOperationalStatusReason(tempVar)
            for logFunc in self._log('read-tag-values-operational-status-reason').debug3Func(): logFunc('read operationalStatusReason. operationalStatusReason=%s, tempValue=%s', self.operationalStatusReason, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "status", 
        "namespace": "status", 
        "className": "StatusMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.file_system.status.status_maapi_gen import StatusMaapi", 
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
            "yangName": "file-system", 
            "namespace": "file_system", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "name": "file-system"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "yangName": "status", 
            "namespace": "status", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "name": "status"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "uuid", 
            "yangName": "uuid", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "operationalStatus", 
            "yangName": "operational-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "fileSystemTypeRaw", 
            "yangName": "file-system-type-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "fileSystemType", 
            "yangName": "file-system-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "expectedUuid", 
            "yangName": "expected-uuid", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "operationalStatusReason", 
            "yangName": "operational-status-reason", 
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
            "typeHandler": "handler: StringHandler", 
            "memberName": "uuid", 
            "yangName": "uuid", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "operationalStatus", 
            "yangName": "operational-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "fileSystemTypeRaw", 
            "yangName": "file-system-type-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "fileSystemType", 
            "yangName": "file-system-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "expectedUuid", 
            "yangName": "expected-uuid", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "operationalStatusReason", 
            "yangName": "operational-status-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


