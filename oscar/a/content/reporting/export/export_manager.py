#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: amiry
# 

import os, time, threading

from a.api.yang.modules.tech.content.qwilt_tech_content_reporting.tech.content.reporting.export_.export__data_gen import ExportData
from a.api.yang.modules.tech.content.qwilt_tech_content_reporting.tech.content.reporting.export_.alarm.alarm_oper_data_gen import AlarmOperData
from a.api.yang.modules.tech.content.qwilt_tech_content_reporting.tech.content.reporting.export_.status.status_oper_data_gen import StatusOperData
from a.api.yang.modules.tech.content.qwilt_tech_content_reporting.qwilt_tech_content_reporting_module_gen import ReportingExportTypesType
from a.api.yang.modules.tech.content.qwilt_tech_content_reporting.qwilt_tech_content_reporting_module_gen import ReportingExportQueueFullReasonType

from logpusher_adapter import LogpusherAdapter
from a.infra.basic.return_codes import ReturnCodes
import a.infra.process
import a.api.user_log.msg.export

if  __package__ is None:
    G_GROUP_NAME_EXPORT_MANAGER  = "unknown"
else:
    from . import G_GROUP_NAME_EXPORT_MANAGER

UPDATE_COUNTERS_INTERVAL = 10

class ExportManager:
    """ Represent a single content reporting export entity. """

#-----------------------------------------------------------------------------------------------------------------------
    def __init__ (self, logger, reportingManager, cfg):
        self._log = logger.createLoggerSameModule(G_GROUP_NAME_EXPORT_MANAGER)
        self._cfg = cfg
        self._runningExport = ExportData()
        self._candidateExport = None
        self._actualExport = ExportData()
        self._logpusherAdapter = LogpusherAdapter(logger, 
                                                  self._cfg.llnwdLogpusherExecutable, 
                                                  self._cfg.llnwdMonitorListenPort,
                                                  self._cfg.llnwdForceIfaceToBind,
                                                  self._cfg.llnwdSentArchiveMaxSizeGB)

        ifaceList = reportingManager.getIfaceList()
        self._logpusherAdapter.updateNetworkConfig(ifaceList)
        self._logDir = None
        self._confDir = None
        self._sentArchiveDir = None
        self._unsentArchiveDir = None
        self._metaArchiveDir = None
        self._firstActivation = True
        self._stopLogpusher = False
        self._lastUpdateCountersTime = 0

        # Oper
        # self._operLock = threading.RLock()
        self._operLock = threading.Lock()
        self._alarm = self.defaultAlarm()
        self._status = self.defaultStatus()

        self._blinkyOperAlarm = None
        self._blinkyOperStatus = None

#-----------------------------------------------------------------------------------------------------------------------
    def setConfigMsgFunctor (self, functor):
        """ Sets the config error message functor - which will be used to report configuration error messages """
        def logAndCallFunctor (message):
            self._log("config-error-msg").error(message)
            functor(message)
        self._configErrorMsgFunctor = logAndCallFunctor

#-----------------------------------------------------------------------------------------------------------------------
    def beginTransaction (self):
        self._log("begin-transaction").debug1("Begin transaction")
        self._candidateExport = ExportData()
        self._candidateExport.copyFrom(self._runningExport)
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def commitTransaction (self):
        self._log("commit-transaction").debug1("Commit transaction")
        self._runningExport.copyFrom(self._candidateExport)
        self._candidateExport = None
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def abortTransaction (self):
        self._log("abort-transaction").debug1("Abort transaction")
        self._candidateExport = None
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def activateRunningConfigIfChanged (self):
        if self._firstActivation or self._configChanged():
            self._log("config-changed").debug1("Export %s. Logpusher config changed. running export: %s. actual export: %s" % (
                self._runningExport.name, self._runningExport, self._actualExport))
            self._logpusherAdapter.updateConfig(self._runningExport.id, self._logDir, self._confDir, self._sentArchiveDir, self._runningExport.name)
            self._firstActivation = False

        if self._shouldStartLogpusher():
            self._log("should-start").notice("Export %s is now enabled. Starting" % self._runningExport.name)
            # No need to do anything. Watchdog will start it.

        elif self._shouldStopLogpusher():
            self._log("should-stop").notice("Export %s is now disabled. Stopping" % self._runningExport.name)
            self._stopLogpusher = True

        self._actualExport.copyFrom(self._runningExport)

#-----------------------------------------------------------------------------------------------------------------------
    def valueSet (self, exportData):

        if self._validateCandidate(exportData) != ReturnCodes.kOk:
            return ReturnCodes.kGeneralError

        self._candidateExport = ExportData()
        self._candidateExport.copyFrom(exportData)
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def destroy (self):
        self._log("Destroy").debug1("Export %s destroy" % self.getName())
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def watchdog (self):

        now = time.time()
        if now - self._lastUpdateCountersTime > UPDATE_COUNTERS_INTERVAL:
            self._updateCounters()
            self._lastUpdateCountersTime = now

        if self._stopLogpusher:
            self._log("watchdog").debug1("Export %s watchdog stopping" % self.getName())
            self._logpusherAdapter.stop()
            self._stopLogpusher = False
            return

        if self._runningExport.enabled:
            self._log("watchdog").debug1("Export %s watchdog" % self.getName())
            self._logpusherAdapter.watchdog()
        else:
            self._log("disabled").debug1("Export %s is disabled" % self.getName())
                    
#-----------------------------------------------------------------------------------------------------------------------
    def stop (self):
        self._log("stop").debug1("Export %s stop logpusher" % self.getName())
        self._logpusherAdapter.stop()

#-----------------------------------------------------------------------------------------------------------------------
    def getName (self):
        if self._candidateExport:
            return self._candidateExport.name
        return self._runningExport.name

#-----------------------------------------------------------------------------------------------------------------------
    def getEnabled (self):
        if self._candidateExport:
            return self._candidateExport.enabled
        return self._runningExport.enabled

#-----------------------------------------------------------------------------------------------------------------------
    def getAnalytics (self):
        if self._candidateExport:
            return self._candidateExport.analytics
        return self._runningExport.analytics

#-----------------------------------------------------------------------------------------------------------------------
    def getType (self):
        if self._candidateExport:
            return self._candidateExport.type_
        return self._runningExport.type_

#-----------------------------------------------------------------------------------------------------------------------
    def getUrlTranslation (self):
        if self._candidateExport:
            return self._candidateExport.urlTranslation
        return self._runningExport.urlTranslation

#-----------------------------------------------------------------------------------------------------------------------
    def getLogDir (self):
        return self._logDir

#-----------------------------------------------------------------------------------------------------------------------
    def getUnsentArchiveDir (self):
        return self._unsentArchiveDir

#-----------------------------------------------------------------------------------------------------------------------
    def getMetaArchiveDir (self):
        return self._metaArchiveDir

#-----------------------------------------------------------------------------------------------------------------------
    def netConfigChanged (self, newIfaceList):
        return self._logpusherAdapter.updateNetworkConfig(newIfaceList)

#-----------------------------------------------------------------------------------------------------------------------
    def netStatusChanged (self, newIfaceList):
        return self._logpusherAdapter.updateNetworkStatus(newIfaceList)

#-----------------------------------------------------------------------------------------------------------------------
    def _validateCandidate (self, exportData):

        """
        if not exportData.id:
            self._configErrorMsgFunctor("missing export id")
            return ReturnCodes.kGeneralError
        """

        self._log("validate-candidate").debug1("Validate candidate %s" % exportData)

        if exportData.type_ != ReportingExportTypesType.kLimelight:
            self._configErrorMsgFunctor("unsupported type %s. only %s is supported" % (exportData.type_, ReportingExportTypesType.kLimelight))
            return ReturnCodes.kGeneralError

        if exportData.enabled and exportData.analytics:
            self._configErrorMsgFunctor("Can't set analytics mode when export is enabled")
            return ReturnCodes.kGeneralError

        self._logDir = self._ensureDir(self._cfg.logDir, exportData.name)
        self._confDir = self._ensureDir(self._cfg.confDir, exportData.name)
        self._sentArchiveDir = self._ensureDir(self._cfg.historyDir,   os.path.join(exportData.name, "sent"))
        self._unsentArchiveDir = self._ensureDir(self._cfg.historyDir, os.path.join(exportData.name, "unsent"))
        self._metaArchiveDir = self._ensureDir(self._cfg.historyDir,   os.path.join(exportData.name, "meta"))

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def _shouldStopLogpusher (self):
        return self._actualExport.enabled and not self._runningExport.enabled

#-----------------------------------------------------------------------------------------------------------------------
    def _shouldStartLogpusher (self):
        return self._runningExport.enabled and not self._actualExport.enabled

#-----------------------------------------------------------------------------------------------------------------------
    def _configChanged (self):
        return  self._actualExport.id != self._runningExport.id or \
                self._actualExport.name != self._runningExport.name or \
                self._actualExport.enabled != self._runningExport.enabled

#-----------------------------------------------------------------------------------------------------------------------
    def _ensureDir(self, parent, subdir):
        fullPath = os.path.join(parent, subdir)
        if not os.path.exists(fullPath):
            os.makedirs(fullPath)
        return fullPath

#-----------------------------------------------------------------------------------------------------------------------
    def _updateCounters (self):

        totalSizeMB = self._getTotalDirSizeMB()
        percentage = (totalSizeMB / (self._cfg.llnwdUnsentQueueMaxSizeMB*1.0)) * 100

        with self._operLock:
            self._status.setQueueUtilizationPercent(int(percentage))

        self._log("update-counters").debug2("Log dir size %d/%d MB (%d%%) [curr %d, %d] [th %d, %d, %d, %d]" % \
                                            (totalSizeMB, self._cfg.llnwdUnsentQueueMaxSizeMB, percentage, \
                                             self._alarm.reportsQueueGettingFull, self._alarm.reportsQueueFull, \
                                             self._cfg.llnwdClearLogQueueGettingFullThreshold, self._cfg.llnwdLogQueueGettingFullThreshold, \
                                             self._cfg.llnwdClearLogQueueFullThreshold, self._cfg.llnwdLogQueueFullThreshold))

        if percentage >= self._cfg.llnwdLogQueueGettingFullThreshold:
            with self._operLock:
                if not self._alarm.reportsQueueGettingFull:
                    self._log("set-alarm-getting-full").notice("Log dir size %d/%d MB (%d%% >= %d%%). Set queue getting full alarm" % \
                                                               (totalSizeMB, self._cfg.llnwdUnsentQueueMaxSizeMB, percentage, \
                                                                   self._cfg.llnwdLogQueueGettingFullThreshold))
                    self._alarm.setReportsQueueGettingFull(True)
                    a.infra.process.logUserMessage(a.api.user_log.msg.export.QueueGettingFull(self._runningExport.name, "getting-full"))

        if percentage < self._cfg.llnwdClearLogQueueGettingFullThreshold:
            with self._operLock:
                if self._alarm.reportsQueueGettingFull:
                    self._log("clear-alarm-getting-full").notice("Log dir size %d/%d MB (%d%% < %d%%). Clear queue getting full alarm" % \
                                                                 (totalSizeMB, self._cfg.llnwdUnsentQueueMaxSizeMB, percentage, \
                                                                     self._cfg.llnwdClearLogQueueGettingFullThreshold))
                    self._alarm.setReportsQueueGettingFull(False)
                    a.infra.process.logUserMessage(a.api.user_log.msg.export.QueueGettingFull(self._runningExport.name, "normal"))

        if percentage >= self._cfg.llnwdLogQueueFullThreshold:
            with self._operLock:
                if not self._alarm.reportsQueueFull:
                    self._log("set-alarm-full").notice("Log dir size %d/%d MB (%d%% >= %d%%). Set queue full alarm" % \
                                                       (totalSizeMB, self._cfg.llnwdUnsentQueueMaxSizeMB, percentage, \
                                                           self._cfg.llnwdLogQueueFullThreshold))
                    self._alarm.setReportsQueueFull(True)
                    # Note: User log message is issued in the cdn_reported every tile a file is discarded

        if percentage < self._cfg.llnwdClearLogQueueFullThreshold:
            with self._operLock:
                if self._alarm.reportsQueueFull:
                    self._log("clear-alarm-full").notice("Log dir size %d/%d MB (%d%% < %d%%). Clear queue full alarm" % \
                                                       (totalSizeMB, self._cfg.llnwdUnsentQueueMaxSizeMB, percentage, \
                                                           self._cfg.llnwdClearLogQueueFullThreshold))
                    self._alarm.setReportsQueueFull(False)

#-----------------------------------------------------------------------------------------------------------------------
    def _getTotalDirSizeMB (self):

        totalSize = 0
        if not self._logDir or not os.path.exists(self._logDir):
            return 0
    
        for dirpath, dirnames, filenames in os.walk(self._logDir):
            for f in filenames:
                # We only want to count ".bz" files
                if len(f) > 4 and f[-4:] == '.bz2':
                    fp = os.path.join(dirpath, f)
                    totalSize += os.path.getsize(fp)
        totalSizeMB = totalSize / (1024.0*1024.0)
        return totalSizeMB

#-----------------------------------------------------------------------------------------------------------------------
# OPER Alarm
#-----------------------------------------------------------------------------------------------------------------------

    def getObjAlarmOperData (self, dpTrxContext, operData):        
        operData.copyRequestedFrom(self.getAlarmCopy())
        self._log("get-obj-alarm-oper-data").debug3("returning: dpTrxContext=%s, operData=%s", dpTrxContext, operData)
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def getAlarmCopy (self):
        with self._operLock:
            alarmCopy  = self.defaultAlarm()
            alarmCopy.copySetFrom(self._alarm)
        return alarmCopy

#-----------------------------------------------------------------------------------------------------------------------
    @classmethod
    def defaultAlarm (cls):
        alarm = cls.newAlarm()
        alarm.setReportsQueueGettingFull(False)
        alarm.setReportsQueueGettingFullReason(ReportingExportQueueFullReasonType.kNone)
        alarm.setReportsQueueFull(False)
        alarm.setReportsQueueFullReason(ReportingExportQueueFullReasonType.kNone)
        return alarm

#-----------------------------------------------------------------------------------------------------------------------
    @classmethod
    def newAlarm (cls):
        __pychecker__ = "unusednames=cls"
        alarm = AlarmOperData()
        alarm.setAllRequested()
        return alarm
#-----------------------------------------------------------------------------------------------------------------------
    def setBlinkyOperAlarm (self, blinkyOperAlarm):
        self._blinkyOperAlarm = blinkyOperAlarm

#-----------------------------------------------------------------------------------------------------------------------
    def getBlinkyOperAlarm (self):
        return self._blinkyOperAlarm

#-----------------------------------------------------------------------------------------------------------------------
# OPER Status
#-----------------------------------------------------------------------------------------------------------------------

    def getObjStatusOperData (self, dpTrxContext, operData):        
        operData.copyRequestedFrom(self.getStatusCopy())
        self._log("get-obj-Status-oper-data").debug3("returning: dpTrxContext=%s, operData=%s", dpTrxContext, operData)
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def getStatusCopy (self):
        with self._operLock:
            statusCopy  = self.defaultStatus()
            statusCopy.copySetFrom(self._status)
        return statusCopy

#-----------------------------------------------------------------------------------------------------------------------
    @classmethod
    def defaultStatus (cls):
        status = cls.newStatus()
        status.setQueueUtilizationPercent(0)
        return status

#-----------------------------------------------------------------------------------------------------------------------
    @classmethod
    def newStatus (cls):
        __pychecker__ = "unusednames=cls"
        status = StatusOperData()
        status.setAllRequested()
        return status

#-----------------------------------------------------------------------------------------------------------------------
    def setBlinkyOperStatus (self, blinkyOperStatus):
        self._blinkyOperStatus = blinkyOperStatus

#-----------------------------------------------------------------------------------------------------------------------
    def getBlinkyOperStatus (self):
        return self._blinkyOperStatus

