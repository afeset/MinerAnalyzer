


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

from output_maapi_base_gen import OutputMaapiBase


from a.api.yang.modules.tech.debug.qwilt_tech_debug.qwilt_tech_debug_module_gen import LogArchiveModeType
from a.api.yang.modules.tech.debug.qwilt_tech_debug.qwilt_tech_debug_module_gen import LogWriteModeType


class BlinkyOutputMaapi(OutputMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-output")
        self.domain = None

        

        
        self.fileBaseNameRequested = False
        self.fileBaseName = None
        self.fileBaseNameSet = False
        
        self.maxFileSizePercentRequested = False
        self.maxFileSizePercent = None
        self.maxFileSizePercentSet = False
        
        self.fileDirectoryRequested = False
        self.fileDirectory = None
        self.fileDirectorySet = False
        
        self.archiveModeRequested = False
        self.archiveMode = None
        self.archiveModeSet = False
        
        self.maxSizeMbRequested = False
        self.maxSizeMb = None
        self.maxSizeMbSet = False
        
        self.writeModeRequested = False
        self.writeMode = None
        self.writeModeSet = False
        
        self.fileRotationIntervalMinutesRequested = False
        self.fileRotationIntervalMinutes = None
        self.fileRotationIntervalMinutesSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestFileBaseName(True)
        
        self.requestMaxFileSizePercent(True)
        
        self.requestFileDirectory(True)
        
        self.requestArchiveMode(True)
        
        self.requestMaxSizeMb(True)
        
        self.requestWriteMode(True)
        
        self.requestFileRotationIntervalMinutes(True)
        
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestFileBaseName(True)
        
        self.requestMaxFileSizePercent(True)
        
        self.requestFileDirectory(True)
        
        self.requestArchiveMode(True)
        
        self.requestMaxSizeMb(True)
        
        self.requestWriteMode(True)
        
        self.requestFileRotationIntervalMinutes(True)
        
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestFileBaseName(False)
        
        self.requestMaxFileSizePercent(False)
        
        self.requestFileDirectory(False)
        
        self.requestArchiveMode(False)
        
        self.requestMaxSizeMb(False)
        
        self.requestWriteMode(False)
        
        self.requestFileRotationIntervalMinutes(False)
        
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestFileBaseName(False)
        
        self.requestMaxFileSizePercent(False)
        
        self.requestFileDirectory(False)
        
        self.requestArchiveMode(False)
        
        self.requestMaxSizeMb(False)
        
        self.requestWriteMode(False)
        
        self.requestFileRotationIntervalMinutes(False)
        
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setFileBaseName(None)
        self.fileBaseNameSet = False
        
        self.setMaxFileSizePercent(None)
        self.maxFileSizePercentSet = False
        
        self.setFileDirectory(None)
        self.fileDirectorySet = False
        
        self.setArchiveMode(None)
        self.archiveModeSet = False
        
        self.setMaxSizeMb(None)
        self.maxSizeMbSet = False
        
        self.setWriteMode(None)
        self.writeModeSet = False
        
        self.setFileRotationIntervalMinutes(None)
        self.fileRotationIntervalMinutesSet = False
        
        

    def write (self
              , loggerClass
              , instance
              , destination
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(loggerClass, instance, destination, trxContext)

    def read (self
              , loggerClass
              , instance
              , destination
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(loggerClass, instance, destination, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , loggerClass
                       , instance
                       , destination
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(loggerClass, instance, destination, 
                                  True,
                                  trxContext)



    def requestFileBaseName (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-filebasename').debug3Func(): logFunc('called. requested=%s', requested)
        self.fileBaseNameRequested = requested
        self.fileBaseNameSet = False

    def isFileBaseNameRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-filebasename-requested').debug3Func(): logFunc('called. requested=%s', self.fileBaseNameRequested)
        return self.fileBaseNameRequested

    def getFileBaseName (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-filebasename').debug3Func(): logFunc('called. self.fileBaseNameSet=%s, self.fileBaseName=%s', self.fileBaseNameSet, self.fileBaseName)
        if self.fileBaseNameSet:
            return self.fileBaseName
        return None

    def hasFileBaseName (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-filebasename').debug3Func(): logFunc('called. self.fileBaseNameSet=%s, self.fileBaseName=%s', self.fileBaseNameSet, self.fileBaseName)
        if self.fileBaseNameSet:
            return True
        return False

    def setFileBaseName (self, fileBaseName):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-filebasename').debug3Func(): logFunc('called. fileBaseName=%s, old=%s', fileBaseName, self.fileBaseName)
        self.fileBaseNameSet = True
        self.fileBaseName = fileBaseName

    def requestMaxFileSizePercent (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-maxfilesizepercent').debug3Func(): logFunc('called. requested=%s', requested)
        self.maxFileSizePercentRequested = requested
        self.maxFileSizePercentSet = False

    def isMaxFileSizePercentRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-maxfilesizepercent-requested').debug3Func(): logFunc('called. requested=%s', self.maxFileSizePercentRequested)
        return self.maxFileSizePercentRequested

    def getMaxFileSizePercent (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-maxfilesizepercent').debug3Func(): logFunc('called. self.maxFileSizePercentSet=%s, self.maxFileSizePercent=%s', self.maxFileSizePercentSet, self.maxFileSizePercent)
        if self.maxFileSizePercentSet:
            return self.maxFileSizePercent
        return None

    def hasMaxFileSizePercent (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-maxfilesizepercent').debug3Func(): logFunc('called. self.maxFileSizePercentSet=%s, self.maxFileSizePercent=%s', self.maxFileSizePercentSet, self.maxFileSizePercent)
        if self.maxFileSizePercentSet:
            return True
        return False

    def setMaxFileSizePercent (self, maxFileSizePercent):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-maxfilesizepercent').debug3Func(): logFunc('called. maxFileSizePercent=%s, old=%s', maxFileSizePercent, self.maxFileSizePercent)
        self.maxFileSizePercentSet = True
        self.maxFileSizePercent = maxFileSizePercent

    def requestFileDirectory (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-filedirectory').debug3Func(): logFunc('called. requested=%s', requested)
        self.fileDirectoryRequested = requested
        self.fileDirectorySet = False

    def isFileDirectoryRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-filedirectory-requested').debug3Func(): logFunc('called. requested=%s', self.fileDirectoryRequested)
        return self.fileDirectoryRequested

    def getFileDirectory (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-filedirectory').debug3Func(): logFunc('called. self.fileDirectorySet=%s, self.fileDirectory=%s', self.fileDirectorySet, self.fileDirectory)
        if self.fileDirectorySet:
            return self.fileDirectory
        return None

    def hasFileDirectory (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-filedirectory').debug3Func(): logFunc('called. self.fileDirectorySet=%s, self.fileDirectory=%s', self.fileDirectorySet, self.fileDirectory)
        if self.fileDirectorySet:
            return True
        return False

    def setFileDirectory (self, fileDirectory):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-filedirectory').debug3Func(): logFunc('called. fileDirectory=%s, old=%s', fileDirectory, self.fileDirectory)
        self.fileDirectorySet = True
        self.fileDirectory = fileDirectory

    def requestArchiveMode (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-archivemode').debug3Func(): logFunc('called. requested=%s', requested)
        self.archiveModeRequested = requested
        self.archiveModeSet = False

    def isArchiveModeRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-archivemode-requested').debug3Func(): logFunc('called. requested=%s', self.archiveModeRequested)
        return self.archiveModeRequested

    def getArchiveMode (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-archivemode').debug3Func(): logFunc('called. self.archiveModeSet=%s, self.archiveMode=%s', self.archiveModeSet, self.archiveMode)
        if self.archiveModeSet:
            return self.archiveMode
        return None

    def hasArchiveMode (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-archivemode').debug3Func(): logFunc('called. self.archiveModeSet=%s, self.archiveMode=%s', self.archiveModeSet, self.archiveMode)
        if self.archiveModeSet:
            return True
        return False

    def setArchiveMode (self, archiveMode):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-archivemode').debug3Func(): logFunc('called. archiveMode=%s, old=%s', archiveMode, self.archiveMode)
        self.archiveModeSet = True
        self.archiveMode = archiveMode

    def requestMaxSizeMb (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-maxsizemb').debug3Func(): logFunc('called. requested=%s', requested)
        self.maxSizeMbRequested = requested
        self.maxSizeMbSet = False

    def isMaxSizeMbRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-maxsizemb-requested').debug3Func(): logFunc('called. requested=%s', self.maxSizeMbRequested)
        return self.maxSizeMbRequested

    def getMaxSizeMb (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-maxsizemb').debug3Func(): logFunc('called. self.maxSizeMbSet=%s, self.maxSizeMb=%s', self.maxSizeMbSet, self.maxSizeMb)
        if self.maxSizeMbSet:
            return self.maxSizeMb
        return None

    def hasMaxSizeMb (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-maxsizemb').debug3Func(): logFunc('called. self.maxSizeMbSet=%s, self.maxSizeMb=%s', self.maxSizeMbSet, self.maxSizeMb)
        if self.maxSizeMbSet:
            return True
        return False

    def setMaxSizeMb (self, maxSizeMb):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-maxsizemb').debug3Func(): logFunc('called. maxSizeMb=%s, old=%s', maxSizeMb, self.maxSizeMb)
        self.maxSizeMbSet = True
        self.maxSizeMb = maxSizeMb

    def requestWriteMode (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-writemode').debug3Func(): logFunc('called. requested=%s', requested)
        self.writeModeRequested = requested
        self.writeModeSet = False

    def isWriteModeRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-writemode-requested').debug3Func(): logFunc('called. requested=%s', self.writeModeRequested)
        return self.writeModeRequested

    def getWriteMode (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-writemode').debug3Func(): logFunc('called. self.writeModeSet=%s, self.writeMode=%s', self.writeModeSet, self.writeMode)
        if self.writeModeSet:
            return self.writeMode
        return None

    def hasWriteMode (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-writemode').debug3Func(): logFunc('called. self.writeModeSet=%s, self.writeMode=%s', self.writeModeSet, self.writeMode)
        if self.writeModeSet:
            return True
        return False

    def setWriteMode (self, writeMode):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-writemode').debug3Func(): logFunc('called. writeMode=%s, old=%s', writeMode, self.writeMode)
        self.writeModeSet = True
        self.writeMode = writeMode

    def requestFileRotationIntervalMinutes (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-filerotationintervalminutes').debug3Func(): logFunc('called. requested=%s', requested)
        self.fileRotationIntervalMinutesRequested = requested
        self.fileRotationIntervalMinutesSet = False

    def isFileRotationIntervalMinutesRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-filerotationintervalminutes-requested').debug3Func(): logFunc('called. requested=%s', self.fileRotationIntervalMinutesRequested)
        return self.fileRotationIntervalMinutesRequested

    def getFileRotationIntervalMinutes (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-filerotationintervalminutes').debug3Func(): logFunc('called. self.fileRotationIntervalMinutesSet=%s, self.fileRotationIntervalMinutes=%s', self.fileRotationIntervalMinutesSet, self.fileRotationIntervalMinutes)
        if self.fileRotationIntervalMinutesSet:
            return self.fileRotationIntervalMinutes
        return None

    def hasFileRotationIntervalMinutes (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-filerotationintervalminutes').debug3Func(): logFunc('called. self.fileRotationIntervalMinutesSet=%s, self.fileRotationIntervalMinutes=%s', self.fileRotationIntervalMinutesSet, self.fileRotationIntervalMinutes)
        if self.fileRotationIntervalMinutesSet:
            return True
        return False

    def setFileRotationIntervalMinutes (self, fileRotationIntervalMinutes):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-filerotationintervalminutes').debug3Func(): logFunc('called. fileRotationIntervalMinutes=%s, old=%s', fileRotationIntervalMinutes, self.fileRotationIntervalMinutes)
        self.fileRotationIntervalMinutesSet = True
        self.fileRotationIntervalMinutes = fileRotationIntervalMinutes


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.fileBaseName = 0
        self.fileBaseNameSet = False
        
        self.maxFileSizePercent = 0
        self.maxFileSizePercentSet = False
        
        self.fileDirectory = 0
        self.fileDirectorySet = False
        
        self.archiveMode = 0
        self.archiveModeSet = False
        
        self.maxSizeMb = 0
        self.maxSizeMbSet = False
        
        self.writeMode = 0
        self.writeModeSet = False
        
        self.fileRotationIntervalMinutes = 0
        self.fileRotationIntervalMinutesSet = False
        

    def _getSelfKeyPath (self, loggerClass
                         , instance
                         , destination
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("output", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(destination);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("destination", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(instance);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("instance", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(loggerClass);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("logger-class", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        loggerClass, 
                        instance, 
                        destination, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(loggerClass, 
                                         instance, 
                                         destination, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(loggerClass, 
                                       instance, 
                                       destination, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       loggerClass, 
                       instance, 
                       destination, 
                       
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

        keyPath = self._getSelfKeyPath(loggerClass, 
                                       instance, 
                                       destination, 
                                       
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
                               loggerClass, 
                               instance, 
                               destination, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasFileBaseName():
            valFileBaseName = Value()
            if self.fileBaseName is not None:
                valFileBaseName.setString(self.fileBaseName)
            else:
                valFileBaseName.setEmpty()
            tagValueList.push(("file-base-name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valFileBaseName)
        
        if self.hasMaxFileSizePercent():
            valMaxFileSizePercent = Value()
            if self.maxFileSizePercent is not None:
                valMaxFileSizePercent.setInt64(self.maxFileSizePercent)
            else:
                valMaxFileSizePercent.setEmpty()
            tagValueList.push(("max-file-size-percent", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valMaxFileSizePercent)
        
        if self.hasFileDirectory():
            valFileDirectory = Value()
            if self.fileDirectory is not None:
                valFileDirectory.setString(self.fileDirectory)
            else:
                valFileDirectory.setEmpty()
            tagValueList.push(("file-directory", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valFileDirectory)
        
        if self.hasArchiveMode():
            valArchiveMode = Value()
            if self.archiveMode is not None:
                valArchiveMode.setEnum(self.archiveMode.getValue())
            else:
                valArchiveMode.setEmpty()
            tagValueList.push(("archive-mode", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valArchiveMode)
        
        if self.hasMaxSizeMb():
            valMaxSizeMb = Value()
            if self.maxSizeMb is not None:
                valMaxSizeMb.setInt64(self.maxSizeMb)
            else:
                valMaxSizeMb.setEmpty()
            tagValueList.push(("max-size-mb", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valMaxSizeMb)
        
        if self.hasWriteMode():
            valWriteMode = Value()
            if self.writeMode is not None:
                valWriteMode.setEnum(self.writeMode.getValue())
            else:
                valWriteMode.setEmpty()
            tagValueList.push(("write-mode", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valWriteMode)
        
        if self.hasFileRotationIntervalMinutes():
            valFileRotationIntervalMinutes = Value()
            if self.fileRotationIntervalMinutes is not None:
                valFileRotationIntervalMinutes.setInt64(self.fileRotationIntervalMinutes)
            else:
                valFileRotationIntervalMinutes.setEmpty()
            tagValueList.push(("file-rotation-interval-minutes", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valFileRotationIntervalMinutes)
        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isFileBaseNameRequested():
            valFileBaseName = Value()
            valFileBaseName.setEmpty()
            tagValueList.push(("file-base-name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valFileBaseName)
        
        if self.isMaxFileSizePercentRequested():
            valMaxFileSizePercent = Value()
            valMaxFileSizePercent.setEmpty()
            tagValueList.push(("max-file-size-percent", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valMaxFileSizePercent)
        
        if self.isFileDirectoryRequested():
            valFileDirectory = Value()
            valFileDirectory.setEmpty()
            tagValueList.push(("file-directory", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valFileDirectory)
        
        if self.isArchiveModeRequested():
            valArchiveMode = Value()
            valArchiveMode.setEmpty()
            tagValueList.push(("archive-mode", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valArchiveMode)
        
        if self.isMaxSizeMbRequested():
            valMaxSizeMb = Value()
            valMaxSizeMb.setEmpty()
            tagValueList.push(("max-size-mb", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valMaxSizeMb)
        
        if self.isWriteModeRequested():
            valWriteMode = Value()
            valWriteMode.setEmpty()
            tagValueList.push(("write-mode", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valWriteMode)
        
        if self.isFileRotationIntervalMinutesRequested():
            valFileRotationIntervalMinutes = Value()
            valFileRotationIntervalMinutes.setEmpty()
            tagValueList.push(("file-rotation-interval-minutes", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valFileRotationIntervalMinutes)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isFileBaseNameRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "file-base-name") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-filebasename').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "fileBaseName", "file-base-name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-file-base-name-bad-value').infoFunc(): logFunc('fileBaseName not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setFileBaseName(tempVar)
            for logFunc in self._log('read-tag-values-file-base-name').debug3Func(): logFunc('read fileBaseName. fileBaseName=%s, tempValue=%s', self.fileBaseName, tempValue.getType())
        
        if self.isMaxFileSizePercentRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "max-file-size-percent") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-maxfilesizepercent').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "maxFileSizePercent", "max-file-size-percent", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-max-file-size-percent-bad-value').infoFunc(): logFunc('maxFileSizePercent not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMaxFileSizePercent(tempVar)
            for logFunc in self._log('read-tag-values-max-file-size-percent').debug3Func(): logFunc('read maxFileSizePercent. maxFileSizePercent=%s, tempValue=%s', self.maxFileSizePercent, tempValue.getType())
        
        if self.isFileDirectoryRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "file-directory") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-filedirectory').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "fileDirectory", "file-directory", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-file-directory-bad-value').infoFunc(): logFunc('fileDirectory not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setFileDirectory(tempVar)
            for logFunc in self._log('read-tag-values-file-directory').debug3Func(): logFunc('read fileDirectory. fileDirectory=%s, tempValue=%s', self.fileDirectory, tempValue.getType())
        
        if self.isArchiveModeRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "archive-mode") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-archivemode').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "archiveMode", "archive-mode", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-archive-mode-bad-value').infoFunc(): logFunc('archiveMode not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setArchiveMode(tempVar)
            for logFunc in self._log('read-tag-values-archive-mode').debug3Func(): logFunc('read archiveMode. archiveMode=%s, tempValue=%s', self.archiveMode, tempValue.getType())
        
        if self.isMaxSizeMbRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "max-size-mb") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-maxsizemb').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "maxSizeMb", "max-size-mb", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-max-size-mb-bad-value').infoFunc(): logFunc('maxSizeMb not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMaxSizeMb(tempVar)
            for logFunc in self._log('read-tag-values-max-size-mb').debug3Func(): logFunc('read maxSizeMb. maxSizeMb=%s, tempValue=%s', self.maxSizeMb, tempValue.getType())
        
        if self.isWriteModeRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "write-mode") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-writemode').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "writeMode", "write-mode", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-write-mode-bad-value').infoFunc(): logFunc('writeMode not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setWriteMode(tempVar)
            for logFunc in self._log('read-tag-values-write-mode').debug3Func(): logFunc('read writeMode. writeMode=%s, tempValue=%s', self.writeMode, tempValue.getType())
        
        if self.isFileRotationIntervalMinutesRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "file-rotation-interval-minutes") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-filerotationintervalminutes').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "fileRotationIntervalMinutes", "file-rotation-interval-minutes", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-file-rotation-interval-minutes-bad-value').infoFunc(): logFunc('fileRotationIntervalMinutes not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setFileRotationIntervalMinutes(tempVar)
            for logFunc in self._log('read-tag-values-file-rotation-interval-minutes').debug3Func(): logFunc('read fileRotationIntervalMinutes. fileRotationIntervalMinutes=%s, tempValue=%s', self.fileRotationIntervalMinutes, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "output", 
        "namespace": "output", 
        "className": "OutputMaapi", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.destination.system_defaults.output.output_maapi_gen import OutputMaapi", 
        "baseClassName": "OutputMaapiBase", 
        "baseModule": "output_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-debug", 
            "isCurrent": false, 
            "yangName": "logger-class", 
            "namespace": "logger_class", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "keyLeaf": {
                "varName": "loggerClass", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "logger-class"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-debug", 
            "isCurrent": false, 
            "yangName": "instance", 
            "namespace": "instance", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "keyLeaf": {
                "varName": "instance", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "instance"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-debug", 
            "isCurrent": false, 
            "yangName": "destination", 
            "namespace": "destination", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "keyLeaf": {
                "varName": "destination", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "destination"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-debug", 
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "name": "system-defaults"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-debug", 
            "yangName": "output", 
            "namespace": "output", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "name": "output"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "fileBaseName", 
            "yangName": "file-base-name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxFileSizePercent", 
            "yangName": "max-file-size-percent", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "fileDirectory", 
            "yangName": "file-directory", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "archiveMode", 
            "yangName": "archive-mode", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "none", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxSizeMb", 
            "yangName": "max-size-mb", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "writeMode", 
            "yangName": "write-mode", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "safe", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "fileRotationIntervalMinutes", 
            "yangName": "file-rotation-interval-minutes", 
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
            "debug", 
            "qwilt_tech_debug"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "fileBaseName", 
            "yangName": "file-base-name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxFileSizePercent", 
            "yangName": "max-file-size-percent", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "fileDirectory", 
            "yangName": "file-directory", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "archiveMode", 
            "yangName": "archive-mode", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "none", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxSizeMb", 
            "yangName": "max-size-mb", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "writeMode", 
            "yangName": "write-mode", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "safe", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "fileRotationIntervalMinutes", 
            "yangName": "file-rotation-interval-minutes", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


