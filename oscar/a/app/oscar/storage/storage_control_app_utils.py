#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: effiz
# 

import os
import a.infra.format.json

class StorageControlAppUtils(object):

    _STATUS_FILE_NAME                                    = "start_status.json"
    _STATUS_FILE_KEY_STATUS_SUMMARY_STRING               = "status-summary-string"
    _STATUS_FILE_KEY_DETAILED_STATUS_STRING              = "detailed-status-string"
    _STATUS_FILE_KEY_SHELL_STATUS_STRING                 = "shell-status-string" 
    _STATUS_FILE_KEY_ACTIVE_DISKS_LIST                   = "active-disks-list"
    _STATUS_FILE_KEY_IS_QSM_ENABLED                      = "is-qsm-enabled"
    _STATUS_FILE_KEY_STORAGE_ERROR_STATUS                = "storage-error-status"    


    @classmethod
    def _s_getFromStatusFile (cls, statusDir, key):
        statusFileName = os.path.join(statusDir, cls._STATUS_FILE_NAME)
        dataDict = {}
        try:
            dataDict = a.infra.format.json.readFromFile(None, statusFileName)
        except:
            return None
    
        if not key in dataDict:
            return None
    
        return dataDict[key]
    
    @classmethod
    def s_getStatusSummaryString (cls, statusDir):
        shortStatus = cls._s_getFromStatusFile (statusDir, cls._STATUS_FILE_KEY_STATUS_SUMMARY_STRING)
        if (shortStatus == None):
            return "No data available."
        return shortStatus
    
    @classmethod
    def s_getDetailedStatusString (cls, statusDir):
        longStatus = cls._s_getFromStatusFile (statusDir, cls._STATUS_FILE_KEY_DETAILED_STATUS_STRING)
        if (longStatus == None):
            return "No data available."
        return longStatus
    
    @classmethod
    def s_getShellStatusString (cls, statusDir):
        status = cls._s_getFromStatusFile (statusDir, cls._STATUS_FILE_KEY_SHELL_STATUS_STRING)
        if (status == None):
            return "No data available."
        return status
    
    @classmethod
    def s_getActiveDisksList (cls, statusDir):
        activeDiskList = cls._s_getFromStatusFile (statusDir, cls._STATUS_FILE_KEY_ACTIVE_DISKS_LIST)
        if (activeDiskList == None):
            return []
        return activeDiskList
    
    @classmethod
    def s_isQsmEnabled (cls, statusDir):
        storageError = cls._s_getFromStatusFile (statusDir, cls._STATUS_FILE_KEY_IS_QSM_ENABLED)
        if (storageError == None):
            return True
        return storageError

    @classmethod
    def s_getStorageErrorStatus (cls, statusDir):
        storageError = cls._s_getFromStatusFile (statusDir, cls._STATUS_FILE_KEY_STORAGE_ERROR_STATUS)
        if (storageError == None):
            return True
        return storageError



