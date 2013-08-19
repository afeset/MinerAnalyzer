


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class CountersMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       
                       , trxContext=None):
        raise NotImplementedError()







    # oper leaves

    # activeSeconds
    def requestActiveSeconds (self, requested):
        raise NotImplementedError()

    def isActiveSecondsRequested (self):
        raise NotImplementedError()

    def getActiveSeconds (self):
        raise NotImplementedError()

    def hasActiveSeconds (self):
        raise NotImplementedError()

    def setActiveSeconds (self, activeSeconds):
        raise NotImplementedError()

    # archivedFiles
    def requestArchivedFiles (self, requested):
        raise NotImplementedError()

    def isArchivedFilesRequested (self):
        raise NotImplementedError()

    def getArchivedFiles (self):
        raise NotImplementedError()

    def hasArchivedFiles (self):
        raise NotImplementedError()

    def setArchivedFiles (self, archivedFiles):
        raise NotImplementedError()

    # overallArchiveDurationWarning
    def requestOverallArchiveDurationWarning (self, requested):
        raise NotImplementedError()

    def isOverallArchiveDurationWarningRequested (self):
        raise NotImplementedError()

    def getOverallArchiveDurationWarning (self):
        raise NotImplementedError()

    def hasOverallArchiveDurationWarning (self):
        raise NotImplementedError()

    def setOverallArchiveDurationWarning (self, overallArchiveDurationWarning):
        raise NotImplementedError()

    # onePendingFile
    def requestOnePendingFile (self, requested):
        raise NotImplementedError()

    def isOnePendingFileRequested (self):
        raise NotImplementedError()

    def getOnePendingFile (self):
        raise NotImplementedError()

    def hasOnePendingFile (self):
        raise NotImplementedError()

    def setOnePendingFile (self, onePendingFile):
        raise NotImplementedError()

    # fileArchiveDurationErrors
    def requestFileArchiveDurationErrors (self, requested):
        raise NotImplementedError()

    def isFileArchiveDurationErrorsRequested (self):
        raise NotImplementedError()

    def getFileArchiveDurationErrors (self):
        raise NotImplementedError()

    def hasFileArchiveDurationErrors (self):
        raise NotImplementedError()

    def setFileArchiveDurationErrors (self, fileArchiveDurationErrors):
        raise NotImplementedError()

    # overallArchiveDurationErrors
    def requestOverallArchiveDurationErrors (self, requested):
        raise NotImplementedError()

    def isOverallArchiveDurationErrorsRequested (self):
        raise NotImplementedError()

    def getOverallArchiveDurationErrors (self):
        raise NotImplementedError()

    def hasOverallArchiveDurationErrors (self):
        raise NotImplementedError()

    def setOverallArchiveDurationErrors (self, overallArchiveDurationErrors):
        raise NotImplementedError()

    # pendingFileCountErrors
    def requestPendingFileCountErrors (self, requested):
        raise NotImplementedError()

    def isPendingFileCountErrorsRequested (self):
        raise NotImplementedError()

    def getPendingFileCountErrors (self):
        raise NotImplementedError()

    def hasPendingFileCountErrors (self):
        raise NotImplementedError()

    def setPendingFileCountErrors (self, pendingFileCountErrors):
        raise NotImplementedError()

    # pendingFileCountWarning
    def requestPendingFileCountWarning (self, requested):
        raise NotImplementedError()

    def isPendingFileCountWarningRequested (self):
        raise NotImplementedError()

    def getPendingFileCountWarning (self):
        raise NotImplementedError()

    def hasPendingFileCountWarning (self):
        raise NotImplementedError()

    def setPendingFileCountWarning (self, pendingFileCountWarning):
        raise NotImplementedError()

    # dirScans
    def requestDirScans (self, requested):
        raise NotImplementedError()

    def isDirScansRequested (self):
        raise NotImplementedError()

    def getDirScans (self):
        raise NotImplementedError()

    def hasDirScans (self):
        raise NotImplementedError()

    def setDirScans (self, dirScans):
        raise NotImplementedError()

    # fileArchiveDurationWarning
    def requestFileArchiveDurationWarning (self, requested):
        raise NotImplementedError()

    def isFileArchiveDurationWarningRequested (self):
        raise NotImplementedError()

    def getFileArchiveDurationWarning (self):
        raise NotImplementedError()

    def hasFileArchiveDurationWarning (self):
        raise NotImplementedError()

    def setFileArchiveDurationWarning (self, fileArchiveDurationWarning):
        raise NotImplementedError()

    # archivedErrors
    def requestArchivedErrors (self, requested):
        raise NotImplementedError()

    def isArchivedErrorsRequested (self):
        raise NotImplementedError()

    def getArchivedErrors (self):
        raise NotImplementedError()

    def hasArchivedErrors (self):
        raise NotImplementedError()

    def setArchivedErrors (self, archivedErrors):
        raise NotImplementedError()

    # dirScansErrors
    def requestDirScansErrors (self, requested):
        raise NotImplementedError()

    def isDirScansErrorsRequested (self):
        raise NotImplementedError()

    def getDirScansErrors (self):
        raise NotImplementedError()

    def hasDirScansErrors (self):
        raise NotImplementedError()

    def setDirScansErrors (self, dirScansErrors):
        raise NotImplementedError()




"""
Extracted from the below data: 
{
    "node": {
        "name": "counters", 
        "namespace": "counters", 
        "className": "CountersMaapi", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_log.tech.log.housekeeper.log_archiving.counters.counters_maapi_gen import CountersMaapi", 
        "baseClassName": "CountersMaapiBase", 
        "baseModule": "counters_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-log", 
            "yangName": "log", 
            "namespace": "log", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "name": "log"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-log", 
            "yangName": "housekeeper", 
            "namespace": "housekeeper", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "name": "housekeeper"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-log", 
            "yangName": "log-archiving", 
            "namespace": "log_archiving", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "name": "log-archiving"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-log", 
            "yangName": "counters", 
            "namespace": "counters", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "name": "counters"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "activeSeconds", 
            "yangName": "active-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "archivedFiles", 
            "yangName": "archived-files", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallArchiveDurationWarning", 
            "yangName": "overall-archive-duration-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "onePendingFile", 
            "yangName": "one-pending-file", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "fileArchiveDurationErrors", 
            "yangName": "file-archive-duration-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallArchiveDurationErrors", 
            "yangName": "overall-archive-duration-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pendingFileCountErrors", 
            "yangName": "pending-file-count-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pendingFileCountWarning", 
            "yangName": "pending-file-count-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "dirScans", 
            "yangName": "dir-scans", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "fileArchiveDurationWarning", 
            "yangName": "file-archive-duration-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "archivedErrors", 
            "yangName": "archived-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "dirScansErrors", 
            "yangName": "dir-scans-errors", 
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
            "debug", 
            "qwilt_tech_log"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "activeSeconds", 
            "yangName": "active-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "archivedFiles", 
            "yangName": "archived-files", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallArchiveDurationWarning", 
            "yangName": "overall-archive-duration-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "onePendingFile", 
            "yangName": "one-pending-file", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "fileArchiveDurationErrors", 
            "yangName": "file-archive-duration-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallArchiveDurationErrors", 
            "yangName": "overall-archive-duration-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pendingFileCountErrors", 
            "yangName": "pending-file-count-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pendingFileCountWarning", 
            "yangName": "pending-file-count-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "dirScans", 
            "yangName": "dir-scans", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "fileArchiveDurationWarning", 
            "yangName": "file-archive-duration-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "archivedErrors", 
            "yangName": "archived-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "dirScansErrors", 
            "yangName": "dir-scans-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


