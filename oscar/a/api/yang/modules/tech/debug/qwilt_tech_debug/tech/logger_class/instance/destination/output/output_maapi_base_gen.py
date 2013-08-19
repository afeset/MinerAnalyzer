


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class OutputMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , loggerClass
              , instance
              , destination
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , loggerClass
              , instance
              , destination
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , loggerClass
                       , instance
                       , destination
                       
                       , trxContext=None):
        raise NotImplementedError()





    # config leaves

    # fileBaseName
    def requestFileBaseName (self, requested):
        raise NotImplementedError()

    def isFileBaseNameRequested (self):
        raise NotImplementedError()

    def getFileBaseName (self):
        raise NotImplementedError()

    def hasFileBaseName (self):
        raise NotImplementedError()

    def setFileBaseName (self, fileBaseName):
        raise NotImplementedError()

    # maxFileSizePercent
    def requestMaxFileSizePercent (self, requested):
        raise NotImplementedError()

    def isMaxFileSizePercentRequested (self):
        raise NotImplementedError()

    def getMaxFileSizePercent (self):
        raise NotImplementedError()

    def hasMaxFileSizePercent (self):
        raise NotImplementedError()

    def setMaxFileSizePercent (self, maxFileSizePercent):
        raise NotImplementedError()

    # fileDirectory
    def requestFileDirectory (self, requested):
        raise NotImplementedError()

    def isFileDirectoryRequested (self):
        raise NotImplementedError()

    def getFileDirectory (self):
        raise NotImplementedError()

    def hasFileDirectory (self):
        raise NotImplementedError()

    def setFileDirectory (self, fileDirectory):
        raise NotImplementedError()

    # archiveMode
    def requestArchiveMode (self, requested):
        raise NotImplementedError()

    def isArchiveModeRequested (self):
        raise NotImplementedError()

    def getArchiveMode (self):
        raise NotImplementedError()

    def hasArchiveMode (self):
        raise NotImplementedError()

    def setArchiveMode (self, archiveMode):
        raise NotImplementedError()

    # maxSizeMb
    def requestMaxSizeMb (self, requested):
        raise NotImplementedError()

    def isMaxSizeMbRequested (self):
        raise NotImplementedError()

    def getMaxSizeMb (self):
        raise NotImplementedError()

    def hasMaxSizeMb (self):
        raise NotImplementedError()

    def setMaxSizeMb (self, maxSizeMb):
        raise NotImplementedError()

    # writeMode
    def requestWriteMode (self, requested):
        raise NotImplementedError()

    def isWriteModeRequested (self):
        raise NotImplementedError()

    def getWriteMode (self):
        raise NotImplementedError()

    def hasWriteMode (self):
        raise NotImplementedError()

    def setWriteMode (self, writeMode):
        raise NotImplementedError()

    # fileRotationIntervalMinutes
    def requestFileRotationIntervalMinutes (self, requested):
        raise NotImplementedError()

    def isFileRotationIntervalMinutesRequested (self):
        raise NotImplementedError()

    def getFileRotationIntervalMinutes (self):
        raise NotImplementedError()

    def hasFileRotationIntervalMinutes (self):
        raise NotImplementedError()

    def setFileRotationIntervalMinutes (self, fileRotationIntervalMinutes):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "output", 
        "namespace": "output", 
        "className": "OutputMaapi", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.destination.output.output_maapi_gen import OutputMaapi", 
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
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxFileSizePercent", 
            "yangName": "max-file-size-percent", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "fileDirectory", 
            "yangName": "file-directory", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "archiveMode", 
            "yangName": "archive-mode", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxSizeMb", 
            "yangName": "max-size-mb", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "writeMode", 
            "yangName": "write-mode", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "fileRotationIntervalMinutes", 
            "yangName": "file-rotation-interval-minutes", 
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
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxFileSizePercent", 
            "yangName": "max-file-size-percent", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "fileDirectory", 
            "yangName": "file-directory", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "archiveMode", 
            "yangName": "archive-mode", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxSizeMb", 
            "yangName": "max-size-mb", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "writeMode", 
            "yangName": "write-mode", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "fileRotationIntervalMinutes", 
            "yangName": "file-rotation-interval-minutes", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }
    ], 
    "createTime": "2013"
}
"""


