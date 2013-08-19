#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: amiry
# 

import threading
from export_manager import ExportManager
from a.infra.basic.return_codes import ReturnCodes


if  __package__ is None:
    G_GROUP_NAME_EXPORT_LIST_MANAGER  = "unknown"
else:
    from . import G_GROUP_NAME_EXPORT_LIST_MANAGER


class ExportListManager:
    """ Represent a list of content reporting export entities. """

#-----------------------------------------------------------------------------------------------------------------------
    def __init__ (self, logger, reportingManager, cfg):
        self._log = logger.createLoggerSameModule(G_GROUP_NAME_EXPORT_LIST_MANAGER)
        self._reportingManager = reportingManager
        self._cfg = cfg
        self._configErrorMsgFunctor = None
        self._runningExportList = {}
        self._candidateExportList = None
        self._isDeletedExportList = {}
        # self._configurationLock = threading.RLock()
        self._configurationLock = threading.Lock()

#-----------------------------------------------------------------------------------------------------------------------
    def setConfigMsgFunctor (self, functor):
        """ Sets the config error message functor - which will be used to report configuration error messages """
        def logAndCallFunctor (message):
            self._log("config-error-msg").debug2("error-msg-functor called with message: %s", message)
            functor(message)    
        self._configErrorMsgFunctor = logAndCallFunctor

#-----------------------------------------------------------------------------------------------------------------------
    def beginTransaction (self):
        self._log("begin-transaction").debug1("Begin transaction")
        for export in self._runningExportList.values():
            export.beginTransaction()
        self._candidateExportList = self._runningExportList.copy()
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def commitTransaction (self):
        self._log("commit-transaction").debug1("Commit transaction")

        for export in self._candidateExportList.values():
            export.commitTransaction()
            export.activateRunningConfigIfChanged()

        with self._configurationLock:
            # Add deleted exports to the deleted list so that would be stopped in the next watchdog
            for key, runningExport in self._runningExportList.items():
                candidateExport = self._candidateExportList.get(key)
                if candidateExport is None:
                    self._isDeletedExportList[key] = runningExport
    
            self._runningExportList = self._candidateExportList.copy()
            self._candidateExportList = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def abortTransaction (self):
        self._log("abort-transaction").debug1("Abort transaction")
        for export in self._candidateExportList.values():
            export.abortTransaction()
        self._candidateExportList = None
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def destroy (self):
        self._log("export-list-destroy").debug2("Export list destroy")
        # Do nothing. Blinky will call destroy on all childs.
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def getCandidateExportList (self):
        # Inportant to distinguish between an empty list (all candidated deleted in transaction) and None (not in transaction)
        if not self._candidateExportList is None:
            return self._candidateExportList
        return self._runningExportList

#-----------------------------------------------------------------------------------------------------------------------
    def getRunningExportList (self):
        return self._runningExportList

#-----------------------------------------------------------------------------------------------------------------------
    def createCandidateExport (self, key):
        self._log("create-candidate-export").debug1("Create candicate export. key %s", key)

        if len(self._candidateExportList) > 0:
            self._configErrorMsgFunctor("only one export is allowed. delete existing export before creating %s" % key)
            return None

        if key in self._candidateExportList:
            self._configErrorMsgFunctor("export list already contains element with key %s" % key)
            return None

        exportManager = ExportManager(self._log, self._reportingManager, self._cfg)
        self._candidateExportList[key] = exportManager
        return exportManager

#-----------------------------------------------------------------------------------------------------------------------
    def deleteCandidateExport (self, key):
        self._log("delete-candidate-export").debug1("Delete export. key %s", key)
        if not key in self._candidateExportList:
            self._configErrorMsgFunctor("key %s is not in export list" % key)
            return ReturnCodes.kGeneralError
        del self._candidateExportList[key]
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def getCandidateExport (self, key):
        self._log("get-candidate-export").debug2("Get export. key %s", key)
        exportList = self.getCandidateExportList()
        if not key in exportList:
            self._configErrorMsgFunctor("key %s is not in export list" % key)
            return None
        return exportList[key]

#-----------------------------------------------------------------------------------------------------------------------
    def watchdog (self):

        with self._configurationLock:

            self._log("watchdog-after-log").debug1("Watchdog. Running export list %s" % self._runningExportList.keys())

            for runningExport in self._runningExportList.values():
                self._log("watchdog").debug1("Watchdog export %s" % runningExport.getName())
                runningExport.watchdog()
    
            for isDeletedExport in self._isDeletedExportList.values():
                self._log("stop-deleted").debug1("Export %s is deleted. Stopping" % isDeletedExport.getName())
                isDeletedExport.stop()
    
            self._isDeletedExportList = {}

#-----------------------------------------------------------------------------------------------------------------------
    def stop (self):

        with self._configurationLock:

            for export in self._runningExportList.values():
                self._log("stop-running").notice("Stopping export %s" % export.getName())
                export.stop()

            for export in self._isDeletedExportList.values():
                self._log("stop-isdeleted").notice("Stopping export %s" % export.getName())
                export.stop()


