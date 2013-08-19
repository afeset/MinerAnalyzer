


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class ThresholdsData(object):

    def __init__ (self):

        self.fileArchiveDurationWarningSeconds = 0
        self._myHasFileArchiveDurationWarningSeconds=False
        
        self.pendingFileCountWarning = 0
        self._myHasPendingFileCountWarning=False
        
        self.overallArchiveDurationWarningSeconds = 0
        self._myHasOverallArchiveDurationWarningSeconds=False
        
        self.pendingFileCountError = 0
        self._myHasPendingFileCountError=False
        
        self.fileArchiveDurationErrorSeconds = 0
        self._myHasFileArchiveDurationErrorSeconds=False
        
        self.overallArchiveDurationErrorSeconds = 0
        self._myHasOverallArchiveDurationErrorSeconds=False
        

    def copyFrom (self, other):

        self.fileArchiveDurationWarningSeconds=other.fileArchiveDurationWarningSeconds
        self._myHasFileArchiveDurationWarningSeconds=other._myHasFileArchiveDurationWarningSeconds
        
        self.pendingFileCountWarning=other.pendingFileCountWarning
        self._myHasPendingFileCountWarning=other._myHasPendingFileCountWarning
        
        self.overallArchiveDurationWarningSeconds=other.overallArchiveDurationWarningSeconds
        self._myHasOverallArchiveDurationWarningSeconds=other._myHasOverallArchiveDurationWarningSeconds
        
        self.pendingFileCountError=other.pendingFileCountError
        self._myHasPendingFileCountError=other._myHasPendingFileCountError
        
        self.fileArchiveDurationErrorSeconds=other.fileArchiveDurationErrorSeconds
        self._myHasFileArchiveDurationErrorSeconds=other._myHasFileArchiveDurationErrorSeconds
        
        self.overallArchiveDurationErrorSeconds=other.overallArchiveDurationErrorSeconds
        self._myHasOverallArchiveDurationErrorSeconds=other._myHasOverallArchiveDurationErrorSeconds
        
    # has...() methods

    def hasFileArchiveDurationWarningSeconds (self):
        return self._myHasFileArchiveDurationWarningSeconds

    def hasPendingFileCountWarning (self):
        return self._myHasPendingFileCountWarning

    def hasOverallArchiveDurationWarningSeconds (self):
        return self._myHasOverallArchiveDurationWarningSeconds

    def hasPendingFileCountError (self):
        return self._myHasPendingFileCountError

    def hasFileArchiveDurationErrorSeconds (self):
        return self._myHasFileArchiveDurationErrorSeconds

    def hasOverallArchiveDurationErrorSeconds (self):
        return self._myHasOverallArchiveDurationErrorSeconds


    # setHas...() methods

    def setHasFileArchiveDurationWarningSeconds (self):
        self._myHasFileArchiveDurationWarningSeconds=True

    def setHasPendingFileCountWarning (self):
        self._myHasPendingFileCountWarning=True

    def setHasOverallArchiveDurationWarningSeconds (self):
        self._myHasOverallArchiveDurationWarningSeconds=True

    def setHasPendingFileCountError (self):
        self._myHasPendingFileCountError=True

    def setHasFileArchiveDurationErrorSeconds (self):
        self._myHasFileArchiveDurationErrorSeconds=True

    def setHasOverallArchiveDurationErrorSeconds (self):
        self._myHasOverallArchiveDurationErrorSeconds=True


    def clearAllHas (self):

        self._myHasFileArchiveDurationWarningSeconds=False

        self._myHasPendingFileCountWarning=False

        self._myHasOverallArchiveDurationWarningSeconds=False

        self._myHasPendingFileCountError=False

        self._myHasFileArchiveDurationErrorSeconds=False

        self._myHasOverallArchiveDurationErrorSeconds=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasFileArchiveDurationWarningSeconds:
            x = "+"
        leafStr = str(self.fileArchiveDurationWarningSeconds)
        items.append(x + "FileArchiveDurationWarningSeconds="+leafStr)

        x=""
        if self._myHasPendingFileCountWarning:
            x = "+"
        leafStr = str(self.pendingFileCountWarning)
        items.append(x + "PendingFileCountWarning="+leafStr)

        x=""
        if self._myHasOverallArchiveDurationWarningSeconds:
            x = "+"
        leafStr = str(self.overallArchiveDurationWarningSeconds)
        items.append(x + "OverallArchiveDurationWarningSeconds="+leafStr)

        x=""
        if self._myHasPendingFileCountError:
            x = "+"
        leafStr = str(self.pendingFileCountError)
        items.append(x + "PendingFileCountError="+leafStr)

        x=""
        if self._myHasFileArchiveDurationErrorSeconds:
            x = "+"
        leafStr = str(self.fileArchiveDurationErrorSeconds)
        items.append(x + "FileArchiveDurationErrorSeconds="+leafStr)

        x=""
        if self._myHasOverallArchiveDurationErrorSeconds:
            x = "+"
        leafStr = str(self.overallArchiveDurationErrorSeconds)
        items.append(x + "OverallArchiveDurationErrorSeconds="+leafStr)

        return "{ThresholdsData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "ThresholdsData", 
        "namespace": "thresholds", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_log.tech.log.system_defaults.housekeeper.log_archiving.thresholds.thresholds_data_gen import ThresholdsData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "log", 
            "isCurrent": false
        }, 
        {
            "namespace": "system_defaults", 
            "isCurrent": false
        }, 
        {
            "namespace": "housekeeper", 
            "isCurrent": false
        }, 
        {
            "namespace": "log_archiving", 
            "isCurrent": false
        }, 
        {
            "namespace": "thresholds", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "fileArchiveDurationWarningSeconds", 
            "yangName": "file-archive-duration-warning-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "pendingFileCountWarning", 
            "yangName": "pending-file-count-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallArchiveDurationWarningSeconds", 
            "yangName": "overall-archive-duration-warning-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "pendingFileCountError", 
            "yangName": "pending-file-count-error", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "fileArchiveDurationErrorSeconds", 
            "yangName": "file-archive-duration-error-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallArchiveDurationErrorSeconds", 
            "yangName": "overall-archive-duration-error-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
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
            "qwilt_tech_log"
        ]
    }, 
    "createTime": "2013"
}
"""


