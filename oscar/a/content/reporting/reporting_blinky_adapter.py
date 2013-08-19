#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: amiry
# 

from reporting_manager import ReportingManager
from export.export_blinky_adapter import ExportBlinkyAdapter
from a.content.reporting.tech_content_reporting.tech.content.reporting.blinky_reporting_gen import BlinkyReporting
from a.infra.basic.return_codes import ReturnCodes


if  __package__ is None:
    G_GROUP_NAME_CONTENT_REPORTING_BLINKY_ADAPTER = "unknown"
else:
    from . import G_GROUP_NAME_CONTENT_REPORTING_BLINKY_ADAPTER


class ReportingBlinkyAdapter:
    """ Adapter for BlinkyReporting """

    def __init__ (self, logger, operDomain):
        self._log = logger.createLoggerSameModule(G_GROUP_NAME_CONTENT_REPORTING_BLINKY_ADAPTER)
        self._exportBlinkyAdapter = ExportBlinkyAdapter(self._log, operDomain)

#-----------------------------------------------------------------------------------------------------------------------
    def attachToBlinky (self, blinkyReporting, reportingManager):

        self._log("attach-to-blinky-reporting").debug1("Attach to blinky reporting")

        blinkyReporting.setCreateExportListFunctor      (self._createFunctorExportListCreate(reportingManager))
        blinkyReporting.setDeleteExportListFunctor      (self._createFunctorExportListDelete(reportingManager))
        blinkyReporting.setDestroySelfFunctor           (self._createFunctorDestroySelf(blinkyReporting, reportingManager))
        blinkyReporting.setNotifyTrxProgressFunctor     (self._createFunctorTrxProgress(reportingManager), True)

        # Active the blinky node
        rc = blinkyReporting.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-export-list-failed-activating").error("Failed to activate")
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def _createFunctorExportListCreate (self, reportingManager):

        def functorExportListCreate (phase, blinkyExportList):
            self._log("functor-create-export-list").debug2("functor called. phase=%s, blinkyExportList=%s" % (phase, blinkyExportList))
            if phase.isPreparePrivate():
                exportListManager = reportingManager.getExportListManager()
                self._exportBlinkyAdapter.attachToBlinkyExportList(blinkyExportList, exportListManager)
            return ReturnCodes.kOk

        return functorExportListCreate

#-----------------------------------------------------------------------------------------------------------------------
    def _createFunctorExportListDelete (self, reportingManager):
        __pychecker__ = "unusednames=reportingManager"
        def functorExportListDelete (phase, blinkyExportList):
            self._log("functor-delete-export-list").debug2("functor called. phase=%s, blinkyExportList=%s" %(phase, blinkyExportList))
            return ReturnCodes.kOk

        return functorExportListDelete

#-----------------------------------------------------------------------------------------------------------------------
    def _createFunctorDestroySelf (self, blinkyReporting, reportingManager):

        def functorDestroySelf (phase):
            self._log("functor-destroy").debug2("functor called. phase=%s", phase)

            if phase.isCommitPrivate():
                self._log("destroy-reporting-manager").debug1("Destroy reporting manager")
                reportingManager.destroy()
                blinkyReporting.deactivate()
            return ReturnCodes.kOk

        return functorDestroySelf

#-----------------------------------------------------------------------------------------------------------------------
    def _createFunctorTrxProgress (self, reportingManager):

        def functorTrxProgress (progress):
            """ Calls reporting progress functors according to given progress """
            self._log("functor-trx-progress").debug2("functor called.  progress=%s", progress)

            if progress.isPreparePrivateBefore():
                return reportingManager.beginTransaction()

            if progress.isPreparePublicAfter():
                # After all elements in the transaction are prepared, we need to prepare
                # a configuration file that will be used by other components in the system (e.g.
                # pre-topper in the case of CDN integration)
                # File will be renamed on commit or deleted on abort
                return reportingManager.prepareExternalConfig()

            if progress.isCommitPublicAfter():
                return reportingManager.commitTransaction()

            if progress.isAbortPublicAfter():
                return reportingManager.abortTransaction()

            return ReturnCodes.kOk

        return functorTrxProgress

