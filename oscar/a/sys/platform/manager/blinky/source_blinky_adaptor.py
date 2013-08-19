#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: shmulika
# 

__pychecker__ = 'maxrefs=20' 

from a.infra.basic.return_codes import ReturnCodes

from a.sys.platform.tech_platform_manager.tech.platform.manager.source.counters.blinky_counters_oper_gen import BlinkyOperCounters
import a.sys.platform.tech_platform_manager.tech.platform.manager.source.blinky_source_gen # BlinkySource

import a.sys.blinky.domain_priority


# Bypass for PyChecker
if  __package__ is None:
    G_GROUP_NAME_PLATFORM_SOURCE_BLINKY_ADAPTOR           = "unknown"
else:
    from . import G_GROUP_NAME_PLATFORM_SOURCE_BLINKY_ADAPTOR     


class SourceBlinkyAdaptor:
    """ Manages Blinky Adapter """

    def __init__ (self, logger, sourceInitializer, configDomain, operDomain, maapiDomain):
        self._log = logger.createLoggerSameModule(G_GROUP_NAME_PLATFORM_SOURCE_BLINKY_ADAPTOR)
        self._configDomain = configDomain
        self._operDomain   = operDomain
        self._maapiDomain  = maapiDomain

        self._sourceNameToObject = {}


        #TODO(shmulika): this name is going to change probably
        self._sourceInitializer = sourceInitializer


    def getMaapiDomain (self):
        return self._maapiDomain


    def createAndAttachBlinkySourceList (self):
        blinkySourceList = a.sys.platform.tech_platform_manager.tech.platform.manager.source.blinky_source_list_gen.BlinkySourceList.s_create(self._log, self._configDomain)
        rc = self._attachToBlinkySourceList(blinkySourceList)
        if rc != ReturnCodes.kOk:
            self._log("create-and-attach-blinky-sources").error("failed.")
            return ReturnCodes.kGeneralError 

        self._configDomain.registerNode(blinkySourceList)
        return ReturnCodes.kOk 



    def _attachToBlinkySourceList (self, blinkySourceList):
        self._log("attach-to-blinky-source-list").debug3("attaching")

        blinkySourceList.setCreateFunctor     (self._createFunctorSourceListCreate(blinkySourceList))                                 
        blinkySourceList.setDeleteFunctor     (self._createFunctorSourceListDelete(blinkySourceList))   
        blinkySourceList.setDestroySelfFunctor(self._createFunctorSourceListDestroySelf())        

        # active the blinky node
        rc = blinkySourceList.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-source-list-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-source-list-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorSourceListCreate (self, blinkySourceList):
        self._log("create-functor-source-list-create").debug2("created")

        def functorSimulateListCreate (phase, listKey, blinkyContainer):
            self._log("functor-source-list").debug2("functor called. phase=%s, listKey=%s, blinkyContainer=%s", phase, listKey, blinkyContainer)            

            if phase.isPreparePrivate():
                if not blinkySourceList.isInTrigger():
                    self._log("create-source-not-in-trigger").debug1("cannot create source %s out-of-trigger, source list is static", listKey)
                    blinkySourceList.setConfigErrorStr("cannot create source, source list is static")
                    return ReturnCodes.kGeneralError 

                self._log("prepare-private-source-list-create").debug2("getting the preconfigured source and attaching it to blinky")                               
                source = self.getSource(listKey)                
                if source is None:
                    self._log("prepare-private-source-list-create-fail").error("source %s was not preconfigured", listKey)                
                    blinkySourceList.setConfigErrorStr("source %s was not preconfigured", listKey)
                    return ReturnCodes.kGeneralError 

                return self._attachToBlinkySource(blinkyContainer, source)

            if phase.isCommitPublic():
                self._log("commit-public-source-list-create").debug2("attaching the source to oper domain")                
                source = self.getSource(listKey)                
                if source is None:
                    self._log("commit-public-source-list-create-fail").error("failed getting source %s, but not failing transaction - inconsistencies will probably occur", listKey)      
                    return ReturnCodes.kOk

                return self._attachToOperDomainSource(blinkyContainer, source)

            return ReturnCodes.kOk

        return functorSimulateListCreate

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorSourceListDelete (self, blinkySourceList):
        self._log("create-functor-source-list-create").debug2("created")

        def functorSourceListDelete (phase, listKey):
            self._log("functor-source-list").debug2("functor called. phase=%s, listKey=%s", phase, listKey)

            if phase.isAbortPublic() or phase.isAbortPrivate():
                # abort is not a problem                
                return ReturnCodes.kOk
            else:
                # anything else should be failed, because we never allow the deletion of an entry in a static list
                self._log("functor-source-list").debug2("list is static - cannot delete", phase, listKey)
                blinkySourceList.setConfigErrorStr("source list is static, cannot delete")
                return ReturnCodes.kGeneralError

        return functorSourceListDelete

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorSourceListDestroySelf(self):
        """ creates a destroy self functor that does nothing """
        def functorSourceListDestroySelf (phase):
            self._log("functor-source-list-destroy-self").debug2("functor called. phase=%s", phase)
            return ReturnCodes.kOk

        return functorSourceListDestroySelf


#----------------------------------------------------------------------------------------------------------------------

    def setSource (self, source, listKey):
        self._sourceNameToObject[listKey] = source

    def getSource (self, listKey):
        if listKey not in self._sourceNameToObject:
            return None
        else:
            return self._sourceNameToObject[listKey]


    def createAndAttachBlinkySource (self, source, listKey):
        self.setSource(source, listKey)       
        # TODO(shmulika): attaching the source directly doesn't work for my model due to a (probably) confd bug
        #        blinkySource = a.sys.platform.tech_platform_manager.tech.platform.manager.source.blinky_source_gen.BlinkySource.s_create(self._log, listKey, self._configDomain)
        #        self._attachToBlinkySource(blinkySource, source)
        #        self._configDomain.registerNode(blinkySource)
        return ReturnCodes.kOk 



    def _attachToBlinkySource (self, blinkySource, source):
        """ attaches the suorce to the given blinky source
        """
        self._log("attach-to-blinky-source").debug3("attaching")

        # regular container functors        
        blinkySource.setValueSetFunctor          (self._createFunctorSourceValueSet(source))
        blinkySource.setNotifyTrxProgressFunctor (self._createFunctorTrxProgress(source), True)
        blinkySource.setDestroySelfFunctor       (self._createFunctorSourceDestroySelf(blinkySource, source))        

        #TODO(shmulika): enable when naama updates yang
        blinkySource.setDoActionFunctor          (self._createFunctorDoAction(source))

        # error message functor        
        source.setConfigMsgFunctor(lambda msgStr: blinkySource.setConfigErrorStr(msgStr))

        # active the blinky node
        rc = blinkySource.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-source-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-source-activated").debug2("attached and activated")
        return ReturnCodes.kOk

    def _attachToOperDomainSource (self, blinkySource, source):
        self._log("attach-to-oper-source").debug3("attaching")
        # attach oper elements
        rc = self._attachToBlinkyCounters (self._operDomain, blinkySource, source)
        if rc != ReturnCodes.kOk:
            return ReturnCodes.kGeneralError 


        self._log("attach-to-oper-source-activated").debug2("attached and activated")
        return ReturnCodes.kOk


#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorSourceValueSet (self, source):
        self._log("create-functor-source-value-set").debug1("created blinky-adapter functor")

        def functorSourceValueSet (phase, sourceData):
            self._log("functor-source-value-set").debug3("functor called. phase=%s, sourceData=%s", phase, sourceData)
            if phase.isPreparePrivate():
                self._log("prepare-private-process").debug2("calling source manager's preparePrivateData()")
                rc = source.preparePrivateData(sourceData)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorSourceValueSet

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorTrxProgress (self, source):
        def functorTrxProgress (progress):
            """ Calls source progress functors according to given progress """
            self._log("functor-trx-progress").debug1("functor called.  progress=%s", progress)

            if progress.isPreparePrivateBefore():
                rc = source.configStartTransaction()
                if rc!=ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            if progress.isPreparePrivateAfter():
                rc = source.configPreparePrivateAfter()
                if rc!=ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            if progress.isPreparePublicAfter():
                rc = source.configPreparePublicAfter()
                if rc!=ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            if progress.isCommitPublicBefore():
                rc = source.configCommitTransaction()
                if rc!=ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            if progress.isAbortPrivateAfter():
                rc = source.configAbortTransaction()
                if rc!=ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorTrxProgress

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorSourceDestroySelf (self, blinkySource, source):
        self._log("create-destroy-self-functor").debug3("creating destroy-self functor")

        def functorDestroySelf (phase):
            self._log("functor-destroy").debug2("functor called. phase=%s", phase)

            if phase.isCommitPrivate():
                self._log("destroy-source").debug1("commit destroying source")
                source.destroy()
                blinkySource.deactivate()

            return ReturnCodes.kOk

        return functorDestroySelf

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorDoAction (self, source):
        self._log("create-functor-source-do-action").debug2("created blinky-adapter functor")

        def functorSourceManagerDoAction (userInfo, actionPoint, actionName, params, nParams):
            self._log("functor-source-do-action").debug2("functor called. userInfo=%s, actionPoint=%s, actionName=%s, params=%s, nParams=%s", userInfo, actionPoint, actionName, params, nParams)

            rc, errMessage = source.actionClearCounters()
            if rc != ReturnCodes.kOk:
                source.setActionError(userInfo, errMessage)
                return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorSourceManagerDoAction
        
#######################################################################################################################
# COUNTERS
#######################################################################################################################

    def _attachToBlinkyCounters (self, operDomain, blinkySource, source):
        self._log("attach-to-blinky-source-counters").debug3("attaching")

        blinkyOpCounters = BlinkyOperCounters(self._log)
        blinkyOpCounters.setParent(blinkySource)
        blinkyOpCounters.setConfigObj(blinkySource)
        blinkyOpCounters.setDomain(operDomain)
        blinkyOpCounters.setBasicFunctors(self._createFunctorCountersGetObj(source))                                       

        rc = blinkyOpCounters.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-source-counters-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-source-counters-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorCountersGetObj (self, source):
        self._log("create-functor-counters-get-obj").debug2("created")

        def functorCountersGetObj (dpTrxContext, operData):
            self._log("functor-counters-get-obj").debug2("functor called. dpTrxContext=%s, operData=%s", dpTrxContext, operData)

            rc = source.getObjCountersOperData(dpTrxContext, operData)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError 

            return ReturnCodes.kOk

        return functorCountersGetObj



        
