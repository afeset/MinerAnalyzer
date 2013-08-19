#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: amiry
# 

from a.content.reporting.export.export_list_manager import ExportListManager
from a.content.reporting.tech_content_reporting.tech.content.reporting.export_.blinky_export__list_gen import BlinkyExportList
from a.content.reporting.tech_content_reporting.tech.content.reporting.export_.blinky_export__gen import BlinkyExport
from a.content.reporting.tech_content_reporting.tech.content.reporting.export_.alarm.blinky_alarm_oper_gen import BlinkyOperAlarm
from a.content.reporting.tech_content_reporting.tech.content.reporting.export_.status.blinky_status_oper_gen import BlinkyOperStatus
from a.infra.basic.return_codes import ReturnCodes


if  __package__ is None:
    G_GROUP_NAME_EXPORT_BLINKY_ADAPTER = "unknown"
else:
    from . import G_GROUP_NAME_EXPORT_BLINKY_ADAPTER


class ExportBlinkyAdapter:
    """ Blinky adapter for BlinkyExport and BlinktExportList """

#-----------------------------------------------------------------------------------------------------------------------
    def __init__ (self, logger, operDomain):
        self._log = logger.createLoggerSameModule(G_GROUP_NAME_EXPORT_BLINKY_ADAPTER)
        self._operDomain = operDomain

#-----------------------------------------------------------------------------------------------------------------------
    def attachToBlinkyExportList(self, blinkyExportList, exportListManager):

        self._log("attach-to-blinky-export-list").debug1("Attach to blinky export list")

        blinkyExportList.setCreateFunctor                (self._createFunctorExportCreate(exportListManager))
        blinkyExportList.setDeleteFunctor                (self._createFunctorExportDelete(exportListManager))
        blinkyExportList.setDestroySelfFunctor           (self._createFunctorExportListDestroySelf(blinkyExportList, exportListManager))
        
        # Error message functor
        exportListManager.setConfigMsgFunctor(lambda msgStr: blinkyExportList.setConfigErrorStr(msgStr))

        # Active the blinky node
        rc = blinkyExportList.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-export-list-failed-activating").error("Failed to activate")
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def _createFunctorExportCreate (self, exportListManager):

        def functorExportCreate (phase, key, blinkyExport):
            self._log("functor-create-export").debug2("functor called. phase=%s, key=%s, blinkyExport=%s", phase, key, blinkyExport)

            if phase.isPreparePrivate():
                self._log("create-export").debug1("Create export. Key %s" % key)
                exportManager = exportListManager.createCandidateExport(key)
                if exportManager is None:
                    self._log("create-export-failed").error("Create export failed, key %s" % key)
                    return ReturnCodes.kGeneralError
                self._attachToBlinkyExport(blinkyExport, exportManager)

            elif phase.isCommitPublic():
                self._log("attach-to-blinky-export-oper").debug1("Attach to Blinky export oper. Key %s" % key)
                exportManager = exportListManager.getCandidateExport(key)
                self._activateBlinkyExportOper(exportManager)

            return ReturnCodes.kOk

        return functorExportCreate

#-----------------------------------------------------------------------------------------------------------------------
    def _createFunctorExportDelete (self, exportListManager):

        def functorExportListDelete (phase, key):
            self._log("functor-delete-export").debug2("functor called. phase=%s", phase)
            if phase.isPreparePublic():
                self._log("delete-export").debug1("Delete export. Key %s" % key)
                return exportListManager.deleteCandidateExport(key)
            return ReturnCodes.kOk
        return functorExportListDelete

#----------------------------------------------------------------------------------------------------------------------
    def _createFunctorExportListDestroySelf(self, blinkyExportList, exportListManager):

        def functorExportListDestroySelf (phase):
            self._log("functor-export-list-destroy-self").debug2("functor called. phase=%s", phase)
            if phase.isCommitPublic():
                self._log("destroy-export-list-manager").debug1("Destroy export list manager")
                exportListManager.destroy()
                blinkyExportList.deactivate()
            return ReturnCodes.kOk

        return functorExportListDestroySelf

#-----------------------------------------------------------------------------------------------------------------------
    def _attachToBlinkyExport(self, blinkyExport, exportManager):

        self._log("attach-to-blinky-export").debug1("Attach to blinky export")

        self._createBlinkyOperNodes(blinkyExport, exportManager)

        blinkyExport.setValueSetFunctor(self._createFunctorExportValueSet(exportManager))
        blinkyExport.setDestroySelfFunctor(self._createFunctorExportDestroySelf(blinkyExport, exportManager))

        # Error message functor
        exportManager.setConfigMsgFunctor(lambda msgStr: blinkyExport.setConfigErrorStr(msgStr))

        # Active the blinky node
        rc = blinkyExport.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-export-list-failed-activating").error("Failed to activate")
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def _createBlinkyOperNodes(self, blinkyExport, exportManager):

        blinkyOperAlarm = BlinkyOperAlarm(self._log)
        blinkyOperAlarm.setParent(blinkyExport)
        blinkyOperAlarm.setConfigObj(blinkyExport)
        blinkyOperAlarm.setDomain(self._operDomain)
        blinkyOperAlarm.setBasicFunctors(self._createFunctorExportAlarmGetObj(exportManager))
        exportManager.setBlinkyOperAlarm(blinkyOperAlarm)

        blinkyOperStatus = BlinkyOperStatus(self._log)
        blinkyOperStatus.setParent(blinkyExport)
        blinkyOperStatus.setConfigObj(blinkyExport)
        blinkyOperStatus.setDomain(self._operDomain)
        blinkyOperStatus.setBasicFunctors(self._createFunctorExportStatusGetObj(exportManager))
        exportManager.setBlinkyOperStatus(blinkyOperStatus)

#-----------------------------------------------------------------------------------------------------------------------
    def _activateBlinkyExportOper(self, exportManager):

        blinkyOperAlarm = exportManager.getBlinkyOperAlarm()
        if blinkyOperAlarm is None:
            self._log("activate-blinky-export-oper-alarm-none").error("Blinky oper alarm is none")
            return ReturnCodes.kGeneralError 

        rc = blinkyOperAlarm.activate()
        if rc != ReturnCodes.kOk:
            self._log("activate-blinky-export-oper-alarm-failed").error("Failed to activate")
            return ReturnCodes.kGeneralError 

        blinkyOperStatus = exportManager.getBlinkyOperStatus()
        if blinkyOperStatus is None:
            self._log("activate-blinky-export-oper-status-none").error("Blinky oper status is none")
            return ReturnCodes.kGeneralError 

        rc = blinkyOperStatus.activate()
        if rc != ReturnCodes.kOk:
            self._log("activate-blinky-export-oper-status-failed").error("Failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("activate-blinky-export-oper-ok").debug2("Blinky oper activated")
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def _createFunctorExportAlarmGetObj (self, exportManager):

        def functorAlarmGetObj (dpTrxContext, operData):
            self._log("functor-export-alarm-get-obj").debug2("functor called. dpTrxContext=%s, operData=%s", dpTrxContext, operData)

            rc = exportManager.getObjAlarmOperData(dpTrxContext, operData)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError 

            return ReturnCodes.kOk

        return functorAlarmGetObj

#-----------------------------------------------------------------------------------------------------------------------
    def _createFunctorExportStatusGetObj (self, exportManager):
    
        def functorStatusGetObj (dpTrxContext, operData):
            self._log("functor-export-status-get-obj").debug2("functor called. dpTrxContext=%s, operData=%s", dpTrxContext, operData)
    
            rc = exportManager.getObjStatusOperData(dpTrxContext, operData)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError 
    
            return ReturnCodes.kOk
    
        return functorStatusGetObj

#-----------------------------------------------------------------------------------------------------------------------
    def _createFunctorExportValueSet (self, exportManager):

        def functorExportValueSet (phase, exportData):
            self._log("functor-export-value-set").debug2("functor called. phase=%s, exportData=%s", phase, exportData)
            if phase.isPreparePrivate():
                self._log("prepare-private-export-value-set").debug1("Export value set")
                return exportManager.valueSet(exportData)
            return ReturnCodes.kOk

        return functorExportValueSet

#-----------------------------------------------------------------------------------------------------------------------
    def _createFunctorExportDestroySelf(self, blinkyExport, exportManager):

        def functorExportDestroySelf (phase):
            self._log("functor-export-destroy-self").debug2("functor called. phase=%s", phase)

            if phase.isCommitPrivate():
                self._log("destroy-export-manager").debug1("Destroy export manager")
                blinkyExport.deactivate()
                exportManager.destroy()

            if phase.isCommitPublic():
                self._log("deactivate-oper").debug1("Deactivate oper nodes")

                blinkyOperAlarm = exportManager.getBlinkyOperAlarm()
                if blinkyOperAlarm is not None:
                    blinkyOperAlarm.deactivate()
                else:
                    self._log("deactivate-oper-alarm-failed").error("Can't deactivate oper alarm. blinkyOperAlarm is none")

                blinkyOperStatus = exportManager.getBlinkyOperStatus()
                if blinkyOperStatus is not None:
                    blinkyOperStatus.deactivate()
                else:
                    self._log("deactivate-oper-status-failed").error("Can't deactivate oper status. blinkyOperStatus is none")


            return ReturnCodes.kOk

        return functorExportDestroySelf

#-----------------------------------------------------------------------------------------------------------------------

