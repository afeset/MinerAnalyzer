#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: amiry
# 

import os, os.path
from export.export_list_manager import ExportListManager
from profile.profile_list_manager import ProfileListManager
from a.infra.basic.return_codes import ReturnCodes
import a.infra.format.json

if  __package__ is None:
    G_MODULE_NAME_CONTENT_REPORTING_MANAGER         = "unknown"
    G_GROUP_NAME_CONTENT_REPORTING_MANAGER_GENERAL  = "unknown"
else:
    from . import G_MODULE_NAME_CONTENT_REPORTING_MANAGER
    from . import G_GROUP_NAME_CONTENT_REPORTING_MANAGER_GENERAL
        
class ReportingManager:
    """ 
    Manages content reporting in the system.
    """

#-----------------------------------------------------------------------------------------------------------------------
    def __init__ (self, logger, cdnIntegrationManager, cfg):
        self._log = logger.createLogger(G_MODULE_NAME_CONTENT_REPORTING_MANAGER, G_GROUP_NAME_CONTENT_REPORTING_MANAGER_GENERAL)
        self._cdnIntegrationManager = cdnIntegrationManager
        self._cfg = cfg
        self._profileListManager = ProfileListManager(self._log)
        self._exportListManager = ExportListManager(self._log, self, self._cfg)
        self._tempConfigFile = self._cfg.configFile + ".tmp"

#-----------------------------------------------------------------------------------------------------------------------
    def getExportListManager (self):
        return self._exportListManager

#-----------------------------------------------------------------------------------------------------------------------
    def destroy (self):
        self._exportListManager = None

#-----------------------------------------------------------------------------------------------------------------------
    def beginTransaction (self):                                 
        self._profileListManager.beginTransaction()
        self._exportListManager.beginTransaction()
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def commitTransaction (self):
        self._profileListManager.commitTransaction()
        self._exportListManager.commitTransaction()
        if os.path.exists(self._tempConfigFile):
            os.rename(self._tempConfigFile, self._cfg.configFile)
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def abortTransaction (self):
        self._profileListManager.abortTransaction()
        self._exportListManager.abortTransaction()
        if os.path.exists(self._tempConfigFile):
            os.unlink(self._tempConfigFile)
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def watchdog (self):
        self._exportListManager.watchdog()
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def stop (self):
        self._exportListManager.stop()
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def netConfigChanged (self, newIfaceList):
        exportList = self._exportListManager.getRunningExportList()
        for name, export in exportList.items():
            self._log("net-config-change").debug1("Notify net config changed to running export %s" % export.getName()) 
            export.netConfigChanged(newIfaceList)

#-----------------------------------------------------------------------------------------------------------------------
    def netStatusChanged (self, newIfaceList):
        exportList = self._exportListManager.getRunningExportList()
        for name, export in exportList.items():
            self._log("net-status-change").debug1("Notify net status changed to running export %s" % export.getName()) 
            export.netStatusChanged(newIfaceList)

#-----------------------------------------------------------------------------------------------------------------------
    def prepareExternalConfig (self):
        if not self._writeCDNIntegrationConfigFile():
            return ReturnCodes.kGeneralError
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def getIfaceList (self):
        return self._cdnIntegrationManager.getIfaceList()

#-----------------------------------------------------------------------------------------------------------------------
    def _writeCDNIntegrationConfigFile (self):
        cfg = {}
        exportList = self._exportListManager.getCandidateExportList()
        self._log("prepare-external-config").debug1("Prepare external config. Candidate list %s" % exportList) 

        # TODO(amiry) - Add llnwd specific params (profile) only for type=limelight

        for name, export in exportList.items():
            cfg[name] = {
                    "enabled":                export.getEnabled(),
                    "analytics":              export.getAnalytics(),
                    "type":                   str(export.getType()),
                    "urlTranslation":         export.getUrlTranslation(),
                    "logdir":                 export.getLogDir(),
                    "rotationTimeSec":        self._cfg.llnwdRotationTimeSec,
                    "rotationSizeKB":         self._cfg.llnwdRotationSizeKB,
                    "unsentQueueMaxSizeMB":   self._cfg.llnwdUnsentQueueMaxSizeMB,
                    "metaFlushIntervalSec":   self._cfg.llnwdMetaFlushIntervalSec,
                    "unsentArchiveDir":       export.getUnsentArchiveDir(),
                    "metaArchiveDir":         export.getMetaArchiveDir(),
                    "unsentArchiveMaxSizeGB": self._cfg.llnwdUnsentArchiveMaxSizeGB,
                    "metaArchiveMaxSizeGB":   self._cfg.llnwdMetaArchiveMaxSizeGB,
            }

        if not cfg:
            self._log("no-active-config").debug1("No active configurations") 
            # Need to write the file so that we can terminate a running export if needed

        try:
            self._log("write-config-file").info("Prepare exports external config file. %s" % cfg) 
            a.infra.format.json.writeToFile(self._log, cfg, self._tempConfigFile)
            return True
        except Exception as ex:
            self._log("write-config-error").error("Error writing exports external config file. %s. %s" % (self._tempConfigFile, ex)) 
            return False


