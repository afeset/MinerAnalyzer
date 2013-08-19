


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket

from a.api.yang.modules.tech.debug.qwilt_tech_debug.qwilt_tech_debug_module_gen import LogArchiveModeType
from a.api.yang.modules.tech.debug.qwilt_tech_debug.qwilt_tech_debug_module_gen import LogWriteModeType


class OutputData(object):

    def __init__ (self):

        self.fileBaseName = ""
        self._myHasFileBaseName=False
        
        self.maxFileSizePercent = 0
        self._myHasMaxFileSizePercent=False
        
        self.fileDirectory = ""
        self._myHasFileDirectory=False
        
        self.archiveMode = LogArchiveModeType.kNoCompression
        self._myHasArchiveMode=False
        
        self.maxSizeMb = 0
        self._myHasMaxSizeMb=False
        
        self.writeMode = LogWriteModeType.kSafe
        self._myHasWriteMode=False
        
        self.fileRotationIntervalMinutes = 0
        self._myHasFileRotationIntervalMinutes=False
        

    def copyFrom (self, other):

        self.fileBaseName=other.fileBaseName
        self._myHasFileBaseName=other._myHasFileBaseName
        
        self.maxFileSizePercent=other.maxFileSizePercent
        self._myHasMaxFileSizePercent=other._myHasMaxFileSizePercent
        
        self.fileDirectory=other.fileDirectory
        self._myHasFileDirectory=other._myHasFileDirectory
        
        self.archiveMode=other.archiveMode
        self._myHasArchiveMode=other._myHasArchiveMode
        
        self.maxSizeMb=other.maxSizeMb
        self._myHasMaxSizeMb=other._myHasMaxSizeMb
        
        self.writeMode=other.writeMode
        self._myHasWriteMode=other._myHasWriteMode
        
        self.fileRotationIntervalMinutes=other.fileRotationIntervalMinutes
        self._myHasFileRotationIntervalMinutes=other._myHasFileRotationIntervalMinutes
        
    # has...() methods

    def hasFileBaseName (self):
        return self._myHasFileBaseName

    def hasMaxFileSizePercent (self):
        return self._myHasMaxFileSizePercent

    def hasFileDirectory (self):
        return self._myHasFileDirectory

    def hasArchiveMode (self):
        return self._myHasArchiveMode

    def hasMaxSizeMb (self):
        return self._myHasMaxSizeMb

    def hasWriteMode (self):
        return self._myHasWriteMode

    def hasFileRotationIntervalMinutes (self):
        return self._myHasFileRotationIntervalMinutes


    # setHas...() methods

    def setHasFileBaseName (self):
        self._myHasFileBaseName=True

    def setHasMaxFileSizePercent (self):
        self._myHasMaxFileSizePercent=True

    def setHasFileDirectory (self):
        self._myHasFileDirectory=True

    def setHasArchiveMode (self):
        self._myHasArchiveMode=True

    def setHasMaxSizeMb (self):
        self._myHasMaxSizeMb=True

    def setHasWriteMode (self):
        self._myHasWriteMode=True

    def setHasFileRotationIntervalMinutes (self):
        self._myHasFileRotationIntervalMinutes=True


    def clearAllHas (self):

        self._myHasFileBaseName=False

        self._myHasMaxFileSizePercent=False

        self._myHasFileDirectory=False

        self._myHasArchiveMode=False

        self._myHasMaxSizeMb=False

        self._myHasWriteMode=False

        self._myHasFileRotationIntervalMinutes=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasFileBaseName:
            x = "+"
        leafStr = str(self.fileBaseName)
        items.append(x + "FileBaseName="+leafStr)

        x=""
        if self._myHasMaxFileSizePercent:
            x = "+"
        leafStr = str(self.maxFileSizePercent)
        items.append(x + "MaxFileSizePercent="+leafStr)

        x=""
        if self._myHasFileDirectory:
            x = "+"
        leafStr = str(self.fileDirectory)
        items.append(x + "FileDirectory="+leafStr)

        x=""
        if self._myHasArchiveMode:
            x = "+"
        leafStr = str(self.archiveMode)
        items.append(x + "ArchiveMode="+leafStr)

        x=""
        if self._myHasMaxSizeMb:
            x = "+"
        leafStr = str(self.maxSizeMb)
        items.append(x + "MaxSizeMb="+leafStr)

        x=""
        if self._myHasWriteMode:
            x = "+"
        leafStr = str(self.writeMode)
        items.append(x + "WriteMode="+leafStr)

        x=""
        if self._myHasFileRotationIntervalMinutes:
            x = "+"
        leafStr = str(self.fileRotationIntervalMinutes)
        items.append(x + "FileRotationIntervalMinutes="+leafStr)

        return "{OutputData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "OutputData", 
        "namespace": "output", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.destination.output.output_data_gen import OutputData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "logger_class", 
            "isCurrent": false
        }, 
        {
            "namespace": "instance", 
            "isCurrent": false
        }, 
        {
            "namespace": "destination", 
            "isCurrent": false
        }, 
        {
            "namespace": "output", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "fileBaseName", 
            "yangName": "file-base-name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxFileSizePercent", 
            "yangName": "max-file-size-percent", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "fileDirectory", 
            "yangName": "file-directory", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "archiveMode", 
            "yangName": "archive-mode", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxSizeMb", 
            "yangName": "max-size-mb", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "writeMode", 
            "yangName": "write-mode", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "fileRotationIntervalMinutes", 
            "yangName": "file-rotation-interval-minutes", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }
    ], 
    "module": {}, 
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
    "createTime": "2013"
}
"""


