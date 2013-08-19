#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: shmulika
# 

__pychecker__ = 'maxrefs=20' 

from a.infra.basic.return_codes import ReturnCodes

from a.sys.platform.tech_platform_manager.tech.platform.manager.counters.blinky_counters_oper_gen import BlinkyOperCounters
import a.sys.platform.tech_platform_manager.tech.platform.manager.blinky_manager_gen # BlinkyManager

import a.sys.blinky.domain_priority


# Bypass for PyChecker
if  __package__ is None:
    G_GROUP_NAME_PLATFORM_MANAGER_BLINKY_ADAPTOR           = "unknown"
else:
    from . import G_GROUP_NAME_PLATFORM_MANAGER_BLINKY_ADAPTOR     


class ManagerBlinkyAdaptor:
    """ Manages Blinky Adapter """

    def __init__ (self, logger, platformInitializer, configDomain, operDomain, maapiDomain):
        self._log = logger.createLoggerSameModule(G_GROUP_NAME_PLATFORM_MANAGER_BLINKY_ADAPTOR)
        self._configDomain = configDomain
        self._operDomain   = operDomain
        self._maapiDomain  = maapiDomain

        #TODO(shmulika): this name is going to change probably
        self._platformInitializer = platformInitializer

    def getMaapiDomain (self):
        return self._maapiDomain


    def createAndAttachBlinkyPlatform (self, platformManager):
        self.blinkyManager = a.sys.platform.tech_platform_manager.tech.platform.manager.blinky_manager_gen.BlinkyManager.s_create(self._log, self._configDomain)
        rc = self._attachToBlinkyPlatform(self.blinkyManager, platformManager)
        if rc != ReturnCodes.kOk:
            self._log("create-and-attach-blinky-platform").error("failed.")
            return ReturnCodes.kGeneralError 

        self._configDomain.registerNode(self.blinkyManager)
        return ReturnCodes.kOk 


    def _attachToBlinkyPlatform (self, blinkyManager, platformManager):
        """ attaches the platform manager to the given blinky platform
        """
        self._log("attach-to-blinky-platform").debug3("attaching")

        # regular container functors        
        blinkyManager.setValueSetFunctor          (self._createFunctorPlatformValueSet(platformManager))
        blinkyManager.setNotifyTrxProgressFunctor (self._createFunctorTrxProgress(platformManager), True)
        blinkyManager.setDestroySelfFunctor       (self._createFunctorPlatformDestroySelf(blinkyManager, platformManager))        

        # containers and lists
        blinkyManager.setCreateThresholdsFunctor  (self._createFunctorCreateThresholds(platformManager))

        #TODO(shmulika): enable when naama updates yang
        blinkyManager.setDoActionFunctor          (self._createFunctorDoAction(platformManager))

        # error message functor        
        platformManager.setConfigMsgFunctor(lambda msgStr: blinkyManager.setConfigErrorStr(msgStr))

        # active the blinky node
        rc = blinkyManager.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-platforms-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 


        # attach oper elements
        rc = self._attachToBlinkyCounters (self._operDomain, blinkyManager, platformManager)
        if rc != ReturnCodes.kOk:
            return ReturnCodes.kGeneralError 


        self._log("attach-to-blinky-platforms-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorPlatformValueSet (self, platformManager):
        self._log("create-functor-platforms-value-set").debug2("created blinky-adapter functor")

        def functorPlatformValueSet (phase, platformsData):
            self._log("functor-platform-value-set").debug2("functor called. phase=%s, platformsData=%s", phase, platformsData)
            if phase.isPreparePrivate():
                self._log("prepare-private-process").debug2("calling platform manager's preparePrivateData()")
                rc = platformManager.preparePrivateData(platformsData)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorPlatformValueSet

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorTrxProgress (self, platformManager):
        def functorTrxProgress (progress):
            """ Calls platformManager progress functors according to given progress """
            self._log("functor-trx-progress").debug1("functor called.  progress=%s", progress)

            if progress.isPreparePrivateBefore():
                rc = platformManager.configStartTransaction()
                if rc!=ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            if progress.isPreparePrivateAfter():
                rc = platformManager.configPreparePrivateAfter()
                if rc!=ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            if progress.isPreparePublicAfter():
                rc = platformManager.configPreparePublicAfter()
                if rc!=ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            if progress.isCommitPublicBefore():
                rc = platformManager.configCommitTransaction()
                if rc!=ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            if progress.isAbortPrivateAfter():
                rc = platformManager.configAbortTransaction()
                if rc!=ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorTrxProgress

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorPlatformDestroySelf (self, blinkyManager, platformManager):
        self._log("create-destroy-self-functor").debug3("creating destroy-self functor")

        def functorDestroySelf (phase):
            self._log("functor-destroy").debug2("functor called. phase=%s", phase)

            if phase.isCommitPrivate():
                self._log("destroy-platform-manager").debug1("commit destroying platform-manager")
                platformManager.destroy()
                blinkyManager.deactivate()

            return ReturnCodes.kOk

        return functorDestroySelf

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorDoAction (self, platformManager):
        self._log("create-functor-platform-manager-do-action").debug2("created blinky-adapter functor")

        def functorPlatformManagerDoAction (userInfo, actionPoint, actionName, params, nParams):
            self._log("functor-platform-manager-do-action").debug2("functor called. userInfo=%s, actionPoint=%s, actionName=%s, params=%s, nParams=%s", userInfo, actionPoint, actionName, params, nParams)

            rc, errMessage = platformManager.actionClearCounters()
            if rc != ReturnCodes.kOk:
                platformManager.setActionError(userInfo, errMessage)
                return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorPlatformManagerDoAction

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorCreateThresholds (self, platformManager):
        self._log("create-functor-create-thresholds").debug2("created blinky-adapter functor")

        def functorCreateThresholds (phase, blinkyThresholds):        
            self._log("functor-create-thresholds").debug2("functor called. phase=%s", phase)

            if phase.isPreparePrivate():
                self._log("prepare-private-create-thresholds").debug2("calling _attachToBlinkyThresholds()")

                rc = self._attachToBlinkyThresholds(blinkyThresholds, platformManager)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorCreateThresholds


#######################################################################################################################
# THRESHOLDS
#######################################################################################################################

    def _attachToBlinkyThresholds (self, blinkyThresholds, platformManager):
        """ attaches the platform manager to the given blinky thresholds
        Arguments:
            blinkyProcess - BlinkyProcess (a BlinkyNode created by Blinky)
            platformManager         - Nanny
        """
        self._log("attach-to-blinky-thresholds").debug3("attaching")

        # regular container functors        
        blinkyThresholds.setValueSetFunctor          (self._createFunctorThresholdsValueSet(platformManager))
        blinkyThresholds.setDestroySelfFunctor       (self._createFunctorThresholdsDestroySelf(blinkyThresholds, platformManager))        

        # active the blinky node
        rc = blinkyThresholds.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-thresholds-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-thresholds-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorThresholdsValueSet (self, platformManager):
        self._log("create-functor-thresholds-value-set").debug2("created blinky-adapter functor")

        def functorThresholdsValueSet (phase, thresholdsData):
            self._log("functor-thresholds-value-set").debug2("functor called. phase=%s, thresholdsData=%s", phase, thresholdsData)

            if phase.isPreparePrivate():
                self._log("prepare-private-process").debug2("calling platform manager's preparePrivateThresholdsData()")
                rc = platformManager.preparePrivateThresholdsData(thresholdsData)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorThresholdsValueSet

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorThresholdsDestroySelf(self, blinkyThresholds, platformManager):
        """ creates a destroy self functor that does nothing """
        __pychecker__ = 'unusednames=blinkyThresholds,platformManager'
        def functorThresholdsDestroySelf (phase):
            self._log("functor-thresholds-destroy-self").debug2("functor called. phase=%s", phase)
            return ReturnCodes.kOk

        return functorThresholdsDestroySelf


#######################################################################################################################
# COUNTERS
#######################################################################################################################

    def _attachToBlinkyCounters (self, operDomain, blinkyManager, platformManager):
        self._log("attach-to-blinky-platform-manager-counters").debug3("attaching")

        blinkyOpCounters = BlinkyOperCounters(self._log)
        blinkyOpCounters.setParent(blinkyManager)
        blinkyOpCounters.setConfigObj(blinkyManager)
        blinkyOpCounters.setDomain(operDomain)
        blinkyOpCounters.setBasicFunctors(self._createFunctorCountersGetObj(platformManager))                                       

        rc = blinkyOpCounters.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-platform-manager-counters-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-platform-manager-counters-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorCountersGetObj (self, platformManager):
        self._log("create-functor-counters-get-obj").debug2("created")

        def functorCountersGetObj (dpTrxContext, operData):
            self._log("functor-counters-get-obj").debug2("functor called. dpTrxContext=%s, operData=%s", dpTrxContext, operData)

            rc = platformManager.getObjCountersOperData(dpTrxContext, operData)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError 

            return ReturnCodes.kOk

        return functorCountersGetObj




