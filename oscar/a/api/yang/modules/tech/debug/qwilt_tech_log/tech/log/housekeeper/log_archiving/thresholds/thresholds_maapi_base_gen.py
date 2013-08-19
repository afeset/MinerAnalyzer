


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class ThresholdsMaapiBase(object):
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





    # config leaves

    # fileArchiveDurationWarningSeconds
    def requestFileArchiveDurationWarningSeconds (self, requested):
        raise NotImplementedError()

    def isFileArchiveDurationWarningSecondsRequested (self):
        raise NotImplementedError()

    def getFileArchiveDurationWarningSeconds (self):
        raise NotImplementedError()

    def hasFileArchiveDurationWarningSeconds (self):
        raise NotImplementedError()

    def setFileArchiveDurationWarningSeconds (self, fileArchiveDurationWarningSeconds):
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

    # overallArchiveDurationWarningSeconds
    def requestOverallArchiveDurationWarningSeconds (self, requested):
        raise NotImplementedError()

    def isOverallArchiveDurationWarningSecondsRequested (self):
        raise NotImplementedError()

    def getOverallArchiveDurationWarningSeconds (self):
        raise NotImplementedError()

    def hasOverallArchiveDurationWarningSeconds (self):
        raise NotImplementedError()

    def setOverallArchiveDurationWarningSeconds (self, overallArchiveDurationWarningSeconds):
        raise NotImplementedError()

    # pendingFileCountError
    def requestPendingFileCountError (self, requested):
        raise NotImplementedError()

    def isPendingFileCountErrorRequested (self):
        raise NotImplementedError()

    def getPendingFileCountError (self):
        raise NotImplementedError()

    def hasPendingFileCountError (self):
        raise NotImplementedError()

    def setPendingFileCountError (self, pendingFileCountError):
        raise NotImplementedError()

    # fileArchiveDurationErrorSeconds
    def requestFileArchiveDurationErrorSeconds (self, requested):
        raise NotImplementedError()

    def isFileArchiveDurationErrorSecondsRequested (self):
        raise NotImplementedError()

    def getFileArchiveDurationErrorSeconds (self):
        raise NotImplementedError()

    def hasFileArchiveDurationErrorSeconds (self):
        raise NotImplementedError()

    def setFileArchiveDurationErrorSeconds (self, fileArchiveDurationErrorSeconds):
        raise NotImplementedError()

    # overallArchiveDurationErrorSeconds
    def requestOverallArchiveDurationErrorSeconds (self, requested):
        raise NotImplementedError()

    def isOverallArchiveDurationErrorSecondsRequested (self):
        raise NotImplementedError()

    def getOverallArchiveDurationErrorSeconds (self):
        raise NotImplementedError()

    def hasOverallArchiveDurationErrorSeconds (self):
        raise NotImplementedError()

    def setOverallArchiveDurationErrorSeconds (self, overallArchiveDurationErrorSeconds):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "thresholds", 
        "namespace": "thresholds", 
        "className": "ThresholdsMaapi", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_log.tech.log.housekeeper.log_archiving.thresholds.thresholds_maapi_gen import ThresholdsMaapi", 
        "baseClassName": "ThresholdsMaapiBase", 
        "baseModule": "thresholds_maapi_base_gen"
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
            "yangName": "thresholds", 
            "namespace": "thresholds", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "name": "thresholds"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "fileArchiveDurationWarningSeconds", 
            "yangName": "file-archive-duration-warning-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
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
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallArchiveDurationWarningSeconds", 
            "yangName": "overall-archive-duration-warning-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pendingFileCountError", 
            "yangName": "pending-file-count-error", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "fileArchiveDurationErrorSeconds", 
            "yangName": "file-archive-duration-error-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallArchiveDurationErrorSeconds", 
            "yangName": "overall-archive-duration-error-seconds", 
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
            "qwilt_tech_log"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "fileArchiveDurationWarningSeconds", 
            "yangName": "file-archive-duration-warning-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
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
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallArchiveDurationWarningSeconds", 
            "yangName": "overall-archive-duration-warning-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pendingFileCountError", 
            "yangName": "pending-file-count-error", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "fileArchiveDurationErrorSeconds", 
            "yangName": "file-archive-duration-error-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallArchiveDurationErrorSeconds", 
            "yangName": "overall-archive-duration-error-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }
    ], 
    "createTime": "2013"
}
"""


