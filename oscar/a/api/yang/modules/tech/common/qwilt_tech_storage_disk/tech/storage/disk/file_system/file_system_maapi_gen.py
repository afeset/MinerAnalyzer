


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

from file_system_maapi_base_gen import FileSystemMaapiBase

from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.file_system.status.status_maapi_gen import BlinkyStatusMaapi
from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.file_system.commands.commands_maapi_gen import BlinkyCommandsMaapi
from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.file_system.timeouts.timeouts_maapi_gen import BlinkyTimeoutsMaapi

from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import FileSystemTypeType


class BlinkyFileSystemMaapi(FileSystemMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-fileSystem")
        self.domain = None

        
        self.statusObj = None
        
        self.commandsObj = None
        
        self.timeoutsObj = None
        

        
        self.autoInitRequested = False
        self.autoInit = None
        self.autoInitSet = False
        
        self.checkUuidRequested = False
        self.checkUuid = None
        self.checkUuidSet = False
        
        self.readAheadRequested = False
        self.readAhead = None
        self.readAheadSet = False
        
        self.fileSystemTypeRequested = False
        self.fileSystemType = None
        self.fileSystemTypeSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestAutoInit(True)
        
        self.requestCheckUuid(True)
        
        self.requestReadAhead(True)
        
        self.requestFileSystemType(True)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.requestConfigAndOper()
        
        if not self.commandsObj:
            self.commandsObj = self.newCommands()
            self.commandsObj.requestConfigAndOper()
        
        if not self.timeoutsObj:
            self.timeoutsObj = self.newTimeouts()
            self.timeoutsObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestAutoInit(True)
        
        self.requestCheckUuid(True)
        
        self.requestReadAhead(True)
        
        self.requestFileSystemType(True)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.requestConfig()
        
        if not self.commandsObj:
            self.commandsObj = self.newCommands()
            self.commandsObj.requestConfig()
        
        if not self.timeoutsObj:
            self.timeoutsObj = self.newTimeouts()
            self.timeoutsObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestAutoInit(False)
        
        self.requestCheckUuid(False)
        
        self.requestReadAhead(False)
        
        self.requestFileSystemType(False)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.requestOper()
        
        if not self.commandsObj:
            self.commandsObj = self.newCommands()
            self.commandsObj.requestOper()
        
        if not self.timeoutsObj:
            self.timeoutsObj = self.newTimeouts()
            self.timeoutsObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestAutoInit(False)
        
        self.requestCheckUuid(False)
        
        self.requestReadAhead(False)
        
        self.requestFileSystemType(False)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.clearAllRequested()
        
        if not self.commandsObj:
            self.commandsObj = self.newCommands()
            self.commandsObj.clearAllRequested()
        
        if not self.timeoutsObj:
            self.timeoutsObj = self.newTimeouts()
            self.timeoutsObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setAutoInit(None)
        self.autoInitSet = False
        
        self.setCheckUuid(None)
        self.checkUuidSet = False
        
        self.setReadAhead(None)
        self.readAheadSet = False
        
        self.setFileSystemType(None)
        self.fileSystemTypeSet = False
        
        
        if self.statusObj:
            self.statusObj.clearAllSet()
        
        if self.commandsObj:
            self.commandsObj.clearAllSet()
        
        if self.timeoutsObj:
            self.timeoutsObj.clearAllSet()
        

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

    def newStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-status').debug3Func(): logFunc('called.')
        status = BlinkyStatusMaapi(self._log)
        status.init(self.domain)
        return status

    def setStatusObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-status').debug3Func(): logFunc('called. obj=%s', obj)
        self.statusObj = obj

    def getStatusObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-status').debug3Func(): logFunc('called. self.statusObj=%s', self.statusObj)
        return self.statusObj

    def hasStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-status').debug3Func(): logFunc('called. self.statusObj=%s', self.statusObj)
        if self.statusObj:
            return True
        return False

    def newCommands (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-commands').debug3Func(): logFunc('called.')
        commands = BlinkyCommandsMaapi(self._log)
        commands.init(self.domain)
        return commands

    def setCommandsObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-commands').debug3Func(): logFunc('called. obj=%s', obj)
        self.commandsObj = obj

    def getCommandsObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-commands').debug3Func(): logFunc('called. self.commandsObj=%s', self.commandsObj)
        return self.commandsObj

    def hasCommands (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-commands').debug3Func(): logFunc('called. self.commandsObj=%s', self.commandsObj)
        if self.commandsObj:
            return True
        return False

    def newTimeouts (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-timeouts').debug3Func(): logFunc('called.')
        timeouts = BlinkyTimeoutsMaapi(self._log)
        timeouts.init(self.domain)
        return timeouts

    def setTimeoutsObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-timeouts').debug3Func(): logFunc('called. obj=%s', obj)
        self.timeoutsObj = obj

    def getTimeoutsObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-timeouts').debug3Func(): logFunc('called. self.timeoutsObj=%s', self.timeoutsObj)
        return self.timeoutsObj

    def hasTimeouts (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-timeouts').debug3Func(): logFunc('called. self.timeoutsObj=%s', self.timeoutsObj)
        if self.timeoutsObj:
            return True
        return False



    def requestAutoInit (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-autoinit').debug3Func(): logFunc('called. requested=%s', requested)
        self.autoInitRequested = requested
        self.autoInitSet = False

    def isAutoInitRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-autoinit-requested').debug3Func(): logFunc('called. requested=%s', self.autoInitRequested)
        return self.autoInitRequested

    def getAutoInit (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-autoinit').debug3Func(): logFunc('called. self.autoInitSet=%s, self.autoInit=%s', self.autoInitSet, self.autoInit)
        if self.autoInitSet:
            return self.autoInit
        return None

    def hasAutoInit (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-autoinit').debug3Func(): logFunc('called. self.autoInitSet=%s, self.autoInit=%s', self.autoInitSet, self.autoInit)
        if self.autoInitSet:
            return True
        return False

    def setAutoInit (self, autoInit):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-autoinit').debug3Func(): logFunc('called. autoInit=%s, old=%s', autoInit, self.autoInit)
        self.autoInitSet = True
        self.autoInit = autoInit

    def requestCheckUuid (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-checkuuid').debug3Func(): logFunc('called. requested=%s', requested)
        self.checkUuidRequested = requested
        self.checkUuidSet = False

    def isCheckUuidRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-checkuuid-requested').debug3Func(): logFunc('called. requested=%s', self.checkUuidRequested)
        return self.checkUuidRequested

    def getCheckUuid (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-checkuuid').debug3Func(): logFunc('called. self.checkUuidSet=%s, self.checkUuid=%s', self.checkUuidSet, self.checkUuid)
        if self.checkUuidSet:
            return self.checkUuid
        return None

    def hasCheckUuid (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-checkuuid').debug3Func(): logFunc('called. self.checkUuidSet=%s, self.checkUuid=%s', self.checkUuidSet, self.checkUuid)
        if self.checkUuidSet:
            return True
        return False

    def setCheckUuid (self, checkUuid):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-checkuuid').debug3Func(): logFunc('called. checkUuid=%s, old=%s', checkUuid, self.checkUuid)
        self.checkUuidSet = True
        self.checkUuid = checkUuid

    def requestReadAhead (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-readahead').debug3Func(): logFunc('called. requested=%s', requested)
        self.readAheadRequested = requested
        self.readAheadSet = False

    def isReadAheadRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-readahead-requested').debug3Func(): logFunc('called. requested=%s', self.readAheadRequested)
        return self.readAheadRequested

    def getReadAhead (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-readahead').debug3Func(): logFunc('called. self.readAheadSet=%s, self.readAhead=%s', self.readAheadSet, self.readAhead)
        if self.readAheadSet:
            return self.readAhead
        return None

    def hasReadAhead (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-readahead').debug3Func(): logFunc('called. self.readAheadSet=%s, self.readAhead=%s', self.readAheadSet, self.readAhead)
        if self.readAheadSet:
            return True
        return False

    def setReadAhead (self, readAhead):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-readahead').debug3Func(): logFunc('called. readAhead=%s, old=%s', readAhead, self.readAhead)
        self.readAheadSet = True
        self.readAhead = readAhead

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


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.statusObj:
            self.statusObj._clearAllReadData()
        
        if self.commandsObj:
            self.commandsObj._clearAllReadData()
        
        if self.timeoutsObj:
            self.timeoutsObj._clearAllReadData()
        

        
        self.autoInit = 0
        self.autoInitSet = False
        
        self.checkUuid = 0
        self.checkUuidSet = False
        
        self.readAhead = 0
        self.readAheadSet = False
        
        self.fileSystemType = 0
        self.fileSystemTypeSet = False
        

    def _getSelfKeyPath (self, disk
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
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

        
        if self.statusObj:
            res = self.statusObj._collectItemsToDelete(disk, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-status-failed').errorFunc(): logFunc('statusObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.commandsObj:
            res = self.commandsObj._collectItemsToDelete(disk, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-commands-failed').errorFunc(): logFunc('commandsObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.timeoutsObj:
            res = self.timeoutsObj._collectItemsToDelete(disk, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-timeouts-failed').errorFunc(): logFunc('timeoutsObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasAutoInit():
            valAutoInit = Value()
            if self.autoInit is not None:
                valAutoInit.setBool(self.autoInit)
            else:
                valAutoInit.setEmpty()
            tagValueList.push(("auto-init", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valAutoInit)
        
        if self.hasCheckUuid():
            valCheckUuid = Value()
            if self.checkUuid is not None:
                valCheckUuid.setBool(self.checkUuid)
            else:
                valCheckUuid.setEmpty()
            tagValueList.push(("check-uuid", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valCheckUuid)
        
        if self.hasReadAhead():
            valReadAhead = Value()
            if self.readAhead is not None:
                valReadAhead.setInt64(self.readAhead)
            else:
                valReadAhead.setEmpty()
            tagValueList.push(("read-ahead", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valReadAhead)
        
        if self.hasFileSystemType():
            valFileSystemType = Value()
            if self.fileSystemType is not None:
                valFileSystemType.setEnum(self.fileSystemType.getValue())
            else:
                valFileSystemType.setEmpty()
            tagValueList.push(("file-system-type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valFileSystemType)
        

        
        if self.statusObj:
            valBegin = Value()
            (tag, ns, prefix) = ("status" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.statusObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-status-failed').errorFunc(): logFunc('statusObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.commandsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("commands" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.commandsObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-commands-failed').errorFunc(): logFunc('commandsObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.timeoutsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("timeouts" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.timeoutsObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-timeouts-failed').errorFunc(): logFunc('timeoutsObj._fillWriteTagValues() failed. PARAMS')
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

        
        if self.isAutoInitRequested():
            valAutoInit = Value()
            valAutoInit.setEmpty()
            tagValueList.push(("auto-init", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valAutoInit)
        
        if self.isCheckUuidRequested():
            valCheckUuid = Value()
            valCheckUuid.setEmpty()
            tagValueList.push(("check-uuid", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valCheckUuid)
        
        if self.isReadAheadRequested():
            valReadAhead = Value()
            valReadAhead.setEmpty()
            tagValueList.push(("read-ahead", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valReadAhead)
        
        if self.isFileSystemTypeRequested():
            valFileSystemType = Value()
            valFileSystemType.setEmpty()
            tagValueList.push(("file-system-type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valFileSystemType)
        

        
        if self.statusObj:
            valBegin = Value()
            (tag, ns, prefix) = ("status" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.statusObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-status-failed').errorFunc(): logFunc('statusObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.commandsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("commands" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.commandsObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-commands-failed').errorFunc(): logFunc('commandsObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.timeoutsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("timeouts" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.timeoutsObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-timeouts-failed').errorFunc(): logFunc('timeoutsObj._fillReadTagValues() failed. PARAMS')
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
        
        if self.isAutoInitRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "auto-init") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-autoinit').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "autoInit", "auto-init", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-auto-init-bad-value').infoFunc(): logFunc('autoInit not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setAutoInit(tempVar)
            for logFunc in self._log('read-tag-values-auto-init').debug3Func(): logFunc('read autoInit. autoInit=%s, tempValue=%s', self.autoInit, tempValue.getType())
        
        if self.isCheckUuidRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "check-uuid") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-checkuuid').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "checkUuid", "check-uuid", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-check-uuid-bad-value').infoFunc(): logFunc('checkUuid not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setCheckUuid(tempVar)
            for logFunc in self._log('read-tag-values-check-uuid').debug3Func(): logFunc('read checkUuid. checkUuid=%s, tempValue=%s', self.checkUuid, tempValue.getType())
        
        if self.isReadAheadRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "read-ahead") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-readahead').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "readAhead", "read-ahead", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-read-ahead-bad-value').infoFunc(): logFunc('readAhead not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setReadAhead(tempVar)
            for logFunc in self._log('read-tag-values-read-ahead').debug3Func(): logFunc('read readAhead. readAhead=%s, tempValue=%s', self.readAhead, tempValue.getType())
        
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
        

        
        if self.statusObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "status") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.statusObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-status-failed').errorFunc(): logFunc('statusObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "status") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.commandsObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "commands") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "commands", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.commandsObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-commands-failed').errorFunc(): logFunc('commandsObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "commands") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "commands", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.timeoutsObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "timeouts") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "timeouts", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.timeoutsObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-timeouts-failed').errorFunc(): logFunc('timeoutsObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "timeouts") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "timeouts", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "fileSystem", 
        "namespace": "file_system", 
        "className": "FileSystemMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.file_system.file_system_maapi_gen import FileSystemMaapi", 
        "baseClassName": "FileSystemMaapiBase", 
        "baseModule": "file_system_maapi_base_gen"
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
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "name": "file-system"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "memberName": "status", 
            "yangName": "status", 
            "className": "BlinkyStatusMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.file_system.status.status_maapi_gen import BlinkyStatusMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "memberName": "commands", 
            "yangName": "commands", 
            "className": "BlinkyCommandsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.file_system.commands.commands_maapi_gen import BlinkyCommandsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "memberName": "timeouts", 
            "yangName": "timeouts", 
            "className": "BlinkyTimeoutsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.file_system.timeouts.timeouts_maapi_gen import BlinkyTimeoutsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "autoInit", 
            "yangName": "auto-init", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "checkUuid", 
            "yangName": "check-uuid", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "readAhead", 
            "yangName": "read-ahead", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
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
            "common", 
            "qwilt_tech_storage_disk"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "autoInit", 
            "yangName": "auto-init", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "checkUuid", 
            "yangName": "check-uuid", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "readAhead", 
            "yangName": "read-ahead", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
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
            "hasDefaultRef": true
        }
    ], 
    "createTime": "2013"
}
"""


