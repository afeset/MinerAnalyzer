#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

from a.infra.basic.return_codes import ReturnCodes

import a.sys.log.blinky.manager.tech.logger_class.blinky_logger_class_list_gen
#import a.sys.log.blinky.manager.tech.logger_class.blinky_logger_class_gen
#import a.sys.log.blinky.manager.tech.logger_class.instance.blinky_instance_list_gen
#import a.sys.log.blinky.manager.tech.logger_class.instance.blinky_instance_gen
#import a.sys.log.blinky.manager.tech.logger_class.instance.destination.blinky_destination_list_gen
#import a.sys.log.blinky.manager.tech.logger_class.instance.destination.blinky_destination_gen
#import a.sys.log.blinky.manager.tech.logger_class.instance.destination.output.blinky_output_gen
#import a.sys.log.housekeeper.blinky.tech.log.blinky_log_gen                                               
import a.sys.log.housekeeper.blinky.tech.log.housekeeper.blinky_housekeeper_gen                           
import a.sys.log.housekeeper.blinky.tech.log.housekeeper.counters.blinky_counters_oper_gen                
#import a.sys.log.housekeeper.blinky.tech.log.housekeeper.thresholds.blinky_thresholds_gen                 
#import a.sys.log.housekeeper.blinky.tech.log.housekeeper.log_archiving.blinky_log_archiving_gen           
#import a.sys.log.housekeeper.blinky.tech.log.housekeeper.log_archiving.thresholds.blinky_thresholds_gen   
import a.sys.log.housekeeper.blinky.tech.log.housekeeper.log_archiving.counters.blinky_counters_oper_gen  


import a.sys.blinky.domain_priority


# Bypass for PyChecker
if  __package__ is None:
    G_NAME_MODULE_SYS_LOG_HOUSEKEEPER_BLINKY = "unknown"
    G_NAME_GROUP_SYS_LOG_HOUSEKEEPER_BLINKY_DESTINATION = "unknown"
    G_NAME_GROUP_SYS_LOG_HOUSEKEEPER_BLINKY_COLLECTION = "unknown"
    G_NAME_GROUP_SYS_LOG_HOUSEKEEPER_BLINKY_MASTER = "unknown"
else:
    from . import G_NAME_MODULE_SYS_LOG_HOUSEKEEPER_BLINKY
    from . import G_NAME_GROUP_SYS_LOG_HOUSEKEEPER_BLINKY_DESTINATION
    from . import G_NAME_GROUP_SYS_LOG_HOUSEKEEPER_BLINKY_COLLECTION
    from . import G_NAME_GROUP_SYS_LOG_HOUSEKEEPER_BLINKY_MASTER 


class LoggerLoggerHousekeeperBlinkyAdapter:
    
    def __init__ (self, logger):
        self._log = logger.createLogger(G_NAME_MODULE_SYS_LOG_HOUSEKEEPER_BLINKY,
                                        G_NAME_GROUP_SYS_LOG_HOUSEKEEPER_BLINKY_MASTER)
        self._configDomain = None
        self._operDomain = None

#----------------------------------------------------------------------------------------------------------------------

    def createDomainAndBlinkyLoggerHousekeeperAndAttach (self, agent, infraLoggerHousekeeper):
        """ Creates a domain, and a BlinkyLoggerHousekeeper node, and attaches it to the given infraLoggerHousekeeper """
        priority=a.sys.blinky.domain_priority.DomainPriority.kDefault
        self._configDomain = agent.createConfigDomain("config-logger-housekeeper", priority)
        self._operDomain = agent.createConfigDomain("oper-logger-housekeeper", priority)

        self._infraLoggerHousekeeper = infraLoggerHousekeeper

        def trxProgressFunctor(progress):
            return self._trxProgressDomain(progress)        
        self._configDomain.registerNotifyTrxProgressFunctor(trxProgressFunctor)

        self._blinkyLoggerHousekeeper = a.sys.log.housekeeper.blinky.tech.log.housekeeper.blinky_housekeeper_gen.BlinkyHousekeeper.s_create(self._log, self._configDomain)
        # error message functor        
        self._infraLoggerHousekeeper.initConfigMsgFunctor(lambda msgStr: self._blinkyLoggerHousekeeper.setConfigErrorStr(msgStr))

        self._attachToBlinkyLoggerHousekeeper(self._blinkyLoggerHousekeeper)

        self._blinkyLoggerClassList = a.sys.log.blinky.manager.tech.logger_class.blinky_logger_class_list_gen.BlinkyLoggerClassList.s_create(self._log, self._configDomain)
        self._attachToBlinkyLoggerClassList(self._blinkyLoggerClassList)

        self._operDomain.registrationDone() 
        self._configDomain.registerNode(self._blinkyLoggerHousekeeper)        
        self._configDomain.registerNode(self._blinkyLoggerClassList)        
        self._configDomain.registrationDone()
        self._configDomain.triggerSubscriptions()

#----------------------------------------------------------------------------------------------------------------------

    def _trxProgressDomain (self, progress):
        """ Calls infraLoggerHousekeeper progress functors according to given progress """
        self._log("trx-progress").debug3("functor called.  progress=%s", progress)

        if progress.isPreparePrivateBefore():
            self._log("prepare-private-before").debug2("prepare private before")
            rc = self._infraLoggerHousekeeper.configStartTransaction()
            if rc!=ReturnCodes.kOk:
                return ReturnCodes.kGeneralError

        if progress.isPreparePrivateAfter():
            self._log("prepare-private-after").debug2("prepare private after")
            rc = self._infraLoggerHousekeeper.configPreparePrivateAfter()
            if rc!=ReturnCodes.kOk:
                return ReturnCodes.kGeneralError

        if progress.isPreparePublicAfter():
            self._log("prepare-public-after").debug2("prepare publc after")
            rc = self._infraLoggerHousekeeper.configPreparePublicAfter()
            if rc!=ReturnCodes.kOk:
                return ReturnCodes.kGeneralError

        if progress.isCommitPublicBefore():
            self._log("commit-public-before").debug2("commit public before")
            rc = self._infraLoggerHousekeeper.configCommitTransaction()
            if rc!=ReturnCodes.kOk:
                return ReturnCodes.kGeneralError

        if progress.isAbortPublicBefore():
            self._log("abort-public-before").debug2("abort public before")
            rc = self._infraLoggerHousekeeper.configAbortTransaction()
            if rc!=ReturnCodes.kOk:
                return ReturnCodes.kGeneralError

        return ReturnCodes.kOk


#######################################################################################################################
# HOUSEKEEPER 
#######################################################################################################################
        
    def _attachToBlinkyLoggerHousekeeper (self, blinkyLoggerHousekeeper):
        """ attaches the logger housekeeper to the given blinky housekeeper
        """
        self._log("attach-logger-housekeeper").debug3("attach")

        # regular container functors
        def valueSetFunctor(phase, housekeeperData):
            return self._valueSetLoggerHousekeeper(phase, housekeeperData)
        blinkyLoggerHousekeeper.setValueSetFunctor(valueSetFunctor)

        def doActionFunctor(userInfo, actionPoint, actionName, params, nParams):
            return self._doActionLoggerHousekeeper(userInfo, actionPoint, actionName, params, nParams)        
        blinkyLoggerHousekeeper.setDoActionFunctor(doActionFunctor)

        def destroySelfFunctor(phase):
            return self._destroySelfLoggerHousekeeper(blinkyLoggerHousekeeper, phase)
        blinkyLoggerHousekeeper.setDestroySelfFunctor(destroySelfFunctor)        

        # contained elements functors
        def createThresholdsFunctor(phase, blinkyLoggerHousekeeperThresholds):
            return self._createLoggerHousekeeperThresholds(phase, blinkyLoggerHousekeeperThresholds)        
        blinkyLoggerHousekeeper.setCreateThresholdsFunctor(createThresholdsFunctor)

        def createLogArchivingFunctor(phase, blinkyLogArchiving):
            return self._createLogArchiving(phase, blinkyLogArchiving)        
        blinkyLoggerHousekeeper.setCreateLogArchivingFunctor(createLogArchivingFunctor)

        # activate the blinky node
        rc = blinkyLoggerHousekeeper.activate()
        if rc != ReturnCodes.kOk:
            self._log("logger-housekeeper-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        # attach oper elements
        rc = self._attachToBlinkyLoggerHousekeeperCounters (blinkyLoggerHousekeeper)
        if rc != ReturnCodes.kOk:
            return ReturnCodes.kGeneralError 

        self._log("attach-logger-housekeeper-done").debug2("attached done")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _valueSetLoggerHousekeeper (self, phase, housekeeperData):
        self._log("value-set-logger-housekeeper").debug3("functor called. phase=%s, housekeeperData=%s", phase, housekeeperData)
        if phase.isPreparePrivate():
            self._log("prepare-private-process").debug2("calling logger housekeeper's value set prepare private. housekeeperData=%s", 
                                                        housekeeperData)
            rc = self._infraLoggerHousekeeper.preparePrivateHousekeeperData(housekeeperData)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _doActionLoggerHousekeeper (self, userInfo, actionPoint, actionName, params, nParams):
        self._log("do-action-log-housekeeper").debug2("functor called. userInfo=%s, actionPoint=%s, actionName=%s, params=%s, nParams=%s", 
                                                      userInfo, actionPoint, actionName, params, nParams)
        self._infraLoggerHousekeeper.clearHousekeeperCounters()
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _destroySelfLoggerHousekeeper (self, blinkyLoggerHousekeeper, phase):
        self._log("destroy").debug3("functor called. phase=%s", phase)
        
        if phase.isCommitPrivate():
            self._log("destroy-logger-housekeeper-manager").debug1("destroy self - logger housekeeper")
            blinkyLoggerHousekeeper.deactivate()

        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createLoggerHousekeeperThresholds (self, phase, blinkyLoggerHousekeeperThresholds):        
        self._log("create-thresholds").debug3("functor called. phase=%s", phase)

        if phase.isPreparePrivate():
            self._log("prepare-private-create-thresholds").debug2("calling housekeeper's create threshold prepare private")
            rc = self._attachToBlinkyLoggerHousekeeperThresholds(blinkyLoggerHousekeeperThresholds)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createLogArchiving (self, phase, blinkyLogArchiving):        
        self._log("create-log-archiving").debug3("functor called. phase=%s", phase)

        if phase.isPreparePrivate():
            self._log("prepare-private-create-log-archiving").debug2("calling housekeeper's create log archiving prepare private")
            rc = self._attachToBlinkyLogArchiving(blinkyLogArchiving)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError

        if phase.isCommitPublic():
            # attach oper elements
            self._log("commit-public-create-log-archiving").debug2("calling housekeeper's create log archiving counters")
            rc = self._attachToBlinkyLogArchivingCounters(blinkyLogArchiving)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError

        return ReturnCodes.kOk


#######################################################################################################################
# HOUSEKEEPER THRESHOLD
#######################################################################################################################

    def _attachToBlinkyLoggerHousekeeperThresholds (self, blinkyLoggerHousekeeperThresholds):
        """ attaches the logger housekeeper thresholds to the given blinky housekeeper
        """
        self._log("attach-logger-housekeeper-thresholds").debug3("attach")

        # regular container functors
        def valueSetFunctor(phase, thresholdsData):
            return self._valueSetLoggerHousekeeperThresholds(phase, thresholdsData)
        blinkyLoggerHousekeeperThresholds.setValueSetFunctor(valueSetFunctor)

        def destroySelfFunctor(phase):
            return self._destroySelfLoggerHousekeeperThresholds(blinkyLoggerHousekeeperThresholds, phase)
        blinkyLoggerHousekeeperThresholds.setDestroySelfFunctor(destroySelfFunctor)        

        # activate the blinky node
        rc = blinkyLoggerHousekeeperThresholds.activate()
        if rc != ReturnCodes.kOk:
            self._log("logger-housekeeper-thresholds-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-logger-housekeeper-thresholds-done").debug2("attached done")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _valueSetLoggerHousekeeperThresholds (self, phase, thresholdsData):
        self._log("value-set-logger-housekeeper-thresholds").debug3("functor called. phase=%s, thresholdsData=%s", phase, thresholdsData)
        if phase.isPreparePrivate():
            self._log("prepare-private-process").debug2("calling logger housekeeper thresholds's value set prepare private, thresholdsData=%s", 
                                                        thresholdsData)
            rc = self._infraLoggerHousekeeper.preparePrivateHousekeeperThresholdData(thresholdsData)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _destroySelfLoggerHousekeeperThresholds (self, blinkyLoggerHousekeeperThresholds, phase):
        self._log("destroy").debug3("functor called. phase=%s", phase)

        if phase.isCommitPrivate():
            self._log("destroy-logger-housekeeper-thresholds-manager").debug2("destroy self - logger housekeeper thresholds")
            blinkyLoggerHousekeeperThresholds.deactivate()

        return ReturnCodes.kOk

#######################################################################################################################
# HOUSEKEEPER COUNTERS
#######################################################################################################################

    def _attachToBlinkyLoggerHousekeeperCounters (self, blinkyLoggerHousekeeper):
        self._log("attach-logger-housekeeper-counters").debug3("attaching")

        blinkyOpCounters = a.sys.log.housekeeper.blinky.tech.log.housekeeper.counters.blinky_counters_oper_gen.BlinkyOperCounters(self._log)
        blinkyOpCounters.setParent(blinkyLoggerHousekeeper)
        blinkyOpCounters.setConfigObj(blinkyLoggerHousekeeper)
        blinkyOpCounters.setDomain(self._operDomain)        
        def getDataObjectCounters(dpTrxContext, operData):
            return self._getDataObjectLoggerHousekeeperCounters(dpTrxContext, operData)        
        blinkyOpCounters.setBasicFunctors(getDataObjectCounters)                                       

        rc = blinkyOpCounters.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-logger-housekeeper-counters-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-logger-housekeeper-counters-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _getDataObjectLoggerHousekeeperCounters (self, dpTrxContext, operData):    
        self._log("counters-get-data").debug2("functor called. dpTrxContext=%s, operData=%s", dpTrxContext, operData)

        rc = self._infraLoggerHousekeeper.getHousekeeperCountersOperData(dpTrxContext, operData)
        if rc != ReturnCodes.kOk:
            return ReturnCodes.kGeneralError 

        return ReturnCodes.kOk


#######################################################################################################################
# HOUSEKEEPER LOG ARCHIVING
#######################################################################################################################

    def _attachToBlinkyLogArchiving (self, blinkyLogArchiving):
        """ attaches the log archiving to the given blinky housekeeper
        """
        self._log("attach-log-archiving").debug3("attach")

        # regular container functors
        def valueSetFunctor(phase, housekeeperData):
            return self._valueSetLogArchiving(phase, housekeeperData)
        blinkyLogArchiving.setValueSetFunctor(valueSetFunctor)


        def doActionFunctor(userInfo, actionPoint, actionName, params, nParams):
            return self._doActionLogArchiving(userInfo, actionPoint, actionName, params, nParams)        
        blinkyLogArchiving.setDoActionFunctor(doActionFunctor)

        def destroySelfFunctor(phase):
            return self._destroySelfLogArchiving(blinkyLogArchiving, phase)
        blinkyLogArchiving.setDestroySelfFunctor(destroySelfFunctor)        

        # contained elements functors
        def createThresholdsFunctor(phase, blinkyLogArchivingThresholds):
            return self._createLogArchivingThresholds(phase, blinkyLogArchivingThresholds)        
        blinkyLogArchiving.setCreateThresholdsFunctor(createThresholdsFunctor)

        # activate the blinky node
        rc = blinkyLogArchiving.activate()
        if rc != ReturnCodes.kOk:
            self._log("log-archiving-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-log-archiving-done").debug2("attached done")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _valueSetLogArchiving (self, phase, logArchivingData):
        self._log("value-set-log-archiving").debug3("functor called. phase=%s, logArchivingData=%s", phase, logArchivingData)
        if phase.isPreparePrivate():
            self._log("prepare-private-process").debug2("calling log archiving's value set prepare private, logArchivingData=%s", 
                                                        logArchivingData)
            rc = self._infraLoggerHousekeeper.preparePrivateArchivingData(logArchivingData)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _doActionLogArchiving (self, userInfo, actionPoint, actionName, params, nParams):
        self._log("do-action-log-archiving").debug2("functor called. userInfo=%s, actionPoint=%s, actionName=%s, params=%s, nParams=%s", 
                                                      userInfo, actionPoint, actionName, params, nParams)
        self._infraLoggerHousekeeper.clearArchivingCounters()
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _destroySelfLogArchiving (self, blinkyLogArchiving, phase):
        self._log("destroy").debug3("functor called. phase=%s", phase)

        if phase.isCommitPrivate():
            self._log("destroy-log-archiving-manager").debug2("destroy self - log archiving")
            blinkyLogArchiving.deactivate()

        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createLogArchivingThresholds (self, phase, blinkyLogArchivingThresholds):        
        self._log("create-thresholds").debug3("functor called. phase=%s", phase)

        if phase.isPreparePrivate():
            self._log("prepare-private-create-thresholds").debug2("calling housekeeper's create threshold prepare private")
            rc = self._attachToBlinkyLogArchivingThresholds(blinkyLogArchivingThresholds)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError

        return ReturnCodes.kOk


#######################################################################################################################
# HOUSEKEEPER LOG ARCHIVING THRESHOLD
#######################################################################################################################

    def _attachToBlinkyLogArchivingThresholds (self, blinkyLogArchivingThresholds):
        """ attaches the log archiving thresholds to the given blinky housekeeper
        """
        self._log("attach-log-archiving-thresholds").debug3("attach")

        # regular container functors
        def valueSetFunctor(phase, thresholdsData):
            return self._valueSetLogArchivingThresholds(phase, thresholdsData)
        blinkyLogArchivingThresholds.setValueSetFunctor(valueSetFunctor)

        def destroySelfFunctor(phase):
            return self._destroySelfLogArchivingThresholds(blinkyLogArchivingThresholds, phase)
        blinkyLogArchivingThresholds.setDestroySelfFunctor(destroySelfFunctor)        

        # activate the blinky node
        rc = blinkyLogArchivingThresholds.activate()
        if rc != ReturnCodes.kOk:
            self._log("log-archiving-thresholds-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-log-archiving-thresholds-done").debug2("attached done")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _valueSetLogArchivingThresholds (self, phase, thresholdsData):
        self._log("value-set-log-archiving-thresholds").debug2("functor called. phase=%s, thresholdsData=%s", phase, thresholdsData)
        if phase.isPreparePrivate():
            self._log("prepare-private-process").debug3("calling log archiving thresholds's value set prepare private, thresholdsData=%s", 
                                                        thresholdsData)
            rc = self._infraLoggerHousekeeper.preparePrivateArchivingThresholdData(thresholdsData)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _destroySelfLogArchivingThresholds (self, blinkyLogArchivingThresholds, phase):
        self._log("destroy").debug3("functor called. phase=%s", phase)

        if phase.isCommitPrivate():
            self._log("destroy-log-archiving-thresholds-manager").debug2("destroy self - log archiving thresholds")
            blinkyLogArchivingThresholds.deactivate()

        return ReturnCodes.kOk

#######################################################################################################################
# HOUSEKEEPER LOG ARCHIVING COUNTERS
#######################################################################################################################

    def _attachToBlinkyLogArchivingCounters (self, blinkyLogArchiving):
        self._log("attach-log-archiving-counters").debug3("attaching")

        blinkyOpCounters = a.sys.log.housekeeper.blinky.tech.log.housekeeper.log_archiving.counters.blinky_counters_oper_gen.BlinkyOperCounters(self._log)
        blinkyOpCounters.setParent(blinkyLogArchiving)
        blinkyOpCounters.setConfigObj(blinkyLogArchiving)
        blinkyOpCounters.setDomain(self._operDomain)        
        def getDataObjectCounters(dpTrxContext, operData):
            return self._getDataObjectLogArchivingCounters(dpTrxContext, operData)        
        blinkyOpCounters.setBasicFunctors(getDataObjectCounters)                                       

        rc = blinkyOpCounters.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-log-archiving-counters-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-log-archiving-counters-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _getDataObjectLogArchivingCounters (self, dpTrxContext, operData):    
        self._log("counters-get-data").debug2("functor called. dpTrxContext=%s, operData=%s", dpTrxContext, operData)

        rc = self._infraLoggerHousekeeper.getArchivingCountersOperData(dpTrxContext, operData)
        if rc != ReturnCodes.kOk:
            return ReturnCodes.kGeneralError 

        return ReturnCodes.kOk






#######################################################################################################################
# LOGGER CLASS LIST
#######################################################################################################################

    def _attachToBlinkyLoggerClassList (self, blinkyLoggerClassList):
        """ attaches the housekeeper to the given blinky LoggerClassList
        Arguments:
            blinkyLoggerClassList
        """
        self._log("attach-to-blinky-logger-class-list").debug3("attaching")

        def prepareCandidateLoggerClassListAddClassFunctor(phase, loggerClassKey, blinkyLoggerClass):
            return self._prepareCandidateLoggerClassListAddClass(phase, loggerClassKey, blinkyLoggerClass)
        blinkyLoggerClassList.setCreateFunctor(prepareCandidateLoggerClassListAddClassFunctor)           
        def prepareCandidateLoggerClassListDeleteClassFunctor(phase, loggerClassKey):
            return self._prepareCandidateLoggerClassListDeleteClass(blinkyLoggerClassList, phase, loggerClassKey)                      
        blinkyLoggerClassList.setDeleteFunctor(prepareCandidateLoggerClassListDeleteClassFunctor)   
        def destroySelfLoggerClassListFunctor(phase):
            return self._destroySelfLoggerClassList(phase)
        blinkyLoggerClassList.setDestroySelfFunctor(destroySelfLoggerClassListFunctor)        

        # active the blinky node
        rc = blinkyLoggerClassList.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-logger-class-list-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-logger-class-list-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------
    def _prepareCandidateLoggerClassListAddClass (self, phase, loggerClassKey, blinkyLoggerClass):
        self._log("functor-logger-class-list-add").debug3("add logger class called. phase=%s, loggerClassKey=%s", 
                                                          phase, loggerClassKey)

        if phase.isPreparePrivate():
            self._log("prepare-private-logger-class-list").debug2("called. loggerClassKey=%s", loggerClassKey)
            self._attachToBlinkyLoggerClass(blinkyLoggerClass, loggerClassKey)
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------
    def _prepareCandidateLoggerClassListDeleteClass (self, blinkyLoggerClassList, phase, loggerClassKey):
        self._log("functor-logger-class-list-del").debug3("delete logger class called. phase=%s, loggerClassKey=%s,", 
                                                          phase, loggerClassKey)
        __pychecker__ = 'unusednames=blinkyLoggerClassList' 
        #nothing to do
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------
    def _destroySelfLoggerClassList(self, phase):
        self._log("functor-logger-class-list-destroy-self").debug2("called. phase=%s", phase)
        return ReturnCodes.kOk


#######################################################################################################################
# LOGGER CLASS
#######################################################################################################################
    def _attachToBlinkyLoggerClass (self, blinkyLoggerClass, loggerClassKey):
        self._log("attach-to-blinky-logger-class").debug3("attaching. loggerClassKey=%s", 
                                                          loggerClassKey)

        def createLoggerInstanceListFunctor(phase, blinkyLoggerInstanceList):
            return self._createLoggerInstanceList(loggerClassKey, phase, blinkyLoggerInstanceList)
        blinkyLoggerClass.setCreateInstanceListFunctor(createLoggerInstanceListFunctor)           
        def deleteLoggerInstanceListFunctor(phase):
            return self._deleteLoggerInstanceList(loggerClassKey, phase)
        blinkyLoggerClass.setDeleteInstanceListFunctor(deleteLoggerInstanceListFunctor)           
        def destroySelfLoggerClassFunctor(phase):
            return self._destroySelfLoggerClass(loggerClassKey, phase)
        blinkyLoggerClass.setDestroySelfFunctor(destroySelfLoggerClassFunctor)        

                
        # active the blinky node
        rc = blinkyLoggerClass.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-logger-class-failed-activating").error("failed to activate. loggerClassKey=%s", 
                                                                     loggerClassKey)
            return ReturnCodes.kGeneralError 

        self._log("attach-logger-class-activated").debug2("attached and activated. loggerClassKey=%s", 
                                                          loggerClassKey)
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------
    def _createLoggerInstanceList (self, loggerClassKey, phase, blinkyLoggerInstanceList):
        self._log("create-functor-create-logger-instance-list").debug3("called, loggerClassKey=%s, phase=%s",
                                                                       loggerClassKey, phase)
        if phase.isPreparePrivate():
            self._log("prepare-private-create-logger-instance-list").debug2("called, loggerClassKey=%s", loggerClassKey)
            rc = self._attachToBlinkyLoggerInstanceList(loggerClassKey, blinkyLoggerInstanceList)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError

        return ReturnCodes.kOk


#----------------------------------------------------------------------------------------------------------------------
    def _deleteLoggerInstanceList (self, loggerClassKey, phase):
        self._log("delete-functor-delete-logger-instance-list").debug2("called, loggerClassKey=%s, phase=%s",
                                                                       loggerClassKey, phase)
        return ReturnCodes.kOk

    def _destroySelfLoggerClass(self, loggerClassKey, phase):
        self._log("functor-logger-class-destroy-self").debug3("called. loggerClassKey=%s, phase=%s", 
                                                              loggerClassKey, phase)
        return ReturnCodes.kOk

#######################################################################################################################
# LOGGER INSTANCE LIST
#######################################################################################################################

    def _attachToBlinkyLoggerInstanceList (self, loggerClassKey, blinkyLoggerInstanceList):
        """ attaches the housekeeper to the given blinky LoggerInstanceList
        Arguments:
            blinkyLoggerInstanceList
        """
        self._log("attach-to-blinky-logger-instance-list").debug3("attaching. loggerClassKey=%s", loggerClassKey)

        def prepareCandidateLoggerInstanceListAddInstanceFunctor(phase, loggerInstanceKey, blinkyLoggerInstance):
            return self._prepareCandidateLoggerInstanceListAddInstance(loggerClassKey, phase, loggerInstanceKey, blinkyLoggerInstance)
        blinkyLoggerInstanceList.setCreateFunctor(prepareCandidateLoggerInstanceListAddInstanceFunctor)           
        def prepareCandidateLoggerInstanceListDeleteInstanceFunctor(phase, loggerInstanceKey):
            return self._prepareCandidateLoggerInstanceListDeleteInstance(loggerClassKey, blinkyLoggerInstanceList, phase, loggerInstanceKey)                      
        blinkyLoggerInstanceList.setDeleteFunctor(prepareCandidateLoggerInstanceListDeleteInstanceFunctor)   
        def destroySelfLoggerInstanceListFunctor(phase):
            return self._destroySelfLoggerInstanceList(loggerClassKey, phase)
        blinkyLoggerInstanceList.setDestroySelfFunctor(destroySelfLoggerInstanceListFunctor)        

        # active the blinky node
        rc = blinkyLoggerInstanceList.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-logger-instance-list-failed-activating").error("failed to activate. loggerClassKey=%s", 
                                                                             loggerClassKey)
            return ReturnCodes.kGeneralError 

        self._log("attach-logger-instance-list-activated").debug2("attached and activated. loggerClassKey=%s", 
                                                                  loggerClassKey)
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------
    def _prepareCandidateLoggerInstanceListAddInstance (self, loggerClassKey, phase, loggerInstanceKey, blinkyLoggerInstance):
        self._log("functor-logger-instance-list-add").debug3("add logger instance called. loggerClassKey=%s, phase=%s, loggerInstanceKey=%s, blinkyLoggerInstance=%s", 
                                                             loggerClassKey, phase, loggerInstanceKey, blinkyLoggerInstance)

        if phase.isPreparePrivate():
            self._log("prepare-private-logger-instance-list").debug2("called. loggerClassKey=%s, loggerInstanceKey=%s", 
                                                                     loggerClassKey, loggerInstanceKey)
            self._attachToBlinkyLoggerInstance(loggerClassKey, blinkyLoggerInstance, loggerInstanceKey)
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------
    def _prepareCandidateLoggerInstanceListDeleteInstance (self, loggerClassKey, blinkyLoggerInstanceList, phase, loggerInstanceKey):
        self._log("functor-logger-instance-list-del").debug3("delete logger instance called. loggerClassKey=%s, phase=%s, loggerInstanceKey=%s,", 
                                                             loggerClassKey, phase, loggerInstanceKey)
        __pychecker__ = 'unusednames=blinkyLoggerInstanceList' 
        #nothing to do
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------
    def _destroySelfLoggerInstanceList(self, loggerClassKey, phase):
        self._log("functor-logger-instance-list-destroy-self").debug3("called. loggerClassKey=%s, phase=%s", 
                                                                      loggerClassKey, phase)
        return ReturnCodes.kOk


#######################################################################################################################
# LOGGER INSTANCE
#######################################################################################################################

    def _attachToBlinkyLoggerInstance (self, loggerClassKey, blinkyLoggerInstance, loggerInstanceKey):
        self._log("attach-to-blinky-logger-instance").debug3("attaching, loggerClassKey=%s, loggerInstanceKey=%s",
                                                             loggerClassKey, loggerInstanceKey)

        def createLoggerDestinationListFunctor(phase, blinkyLoggerDestinationList):
            return self._createLoggerDestinationList(loggerClassKey, loggerInstanceKey, phase, blinkyLoggerDestinationList)
        blinkyLoggerInstance.setCreateDestinationListFunctor(createLoggerDestinationListFunctor)           
        def deleteLoggerDestinationListFunctor(phase):
            return self._deleteLoggerDestinationList(loggerClassKey, loggerInstanceKey, phase)
        blinkyLoggerInstance.setDeleteDestinationListFunctor(deleteLoggerDestinationListFunctor)           
        def destroySelfLoggerInstanceFunctor(phase):
            return self._destroySelfLoggerInstance(loggerClassKey, loggerInstanceKey, phase)
        blinkyLoggerInstance.setDestroySelfFunctor(destroySelfLoggerInstanceFunctor)        

        # active the blinky node
        rc = blinkyLoggerInstance.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-logger-instance-failed-activating").error("failed to activate: loggerClassKey=%s, loggerInstanceKey=%s",
                                                                        loggerClassKey, loggerInstanceKey)
            return ReturnCodes.kGeneralError 

        self._log("attach-logger-instance-activated").debug2("attached and activated: loggerClassKey=%s, loggerInstanceKey=%s",
                                                             loggerClassKey, loggerInstanceKey)
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------
    def _createLoggerDestinationList (self, loggerClassKey, loggerInstanceKey, phase, blinkyLoggerDestinationList):
        self._log("create-functor-create-logger-instance-list").debug2("called, loggerClassKey=%s, loggerInstanceKey=%s, phase=%s",
                                                                       loggerClassKey, loggerInstanceKey, phase)
        if phase.isPreparePrivate():
            self._log("prepare-private-create-logger-instance-list").debug2("called, loggerClassKey=%s, loggerInstanceKey=%s", 
                                                                            loggerClassKey, loggerInstanceKey)
            rc = self._attachToBlinkyLoggerDestinationList(loggerClassKey, loggerInstanceKey, blinkyLoggerDestinationList)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError

        return ReturnCodes.kOk


#----------------------------------------------------------------------------------------------------------------------
    def _deleteLoggerDestinationList (self, loggerClassKey, loggerInstanceKey, phase):
        self._log("delete-functor-delete-logger-instance-list").debug2("called, loggerClassKey=%s, loggerInstanceKey=%s, phase=%s",
                                                                       loggerClassKey, loggerInstanceKey, phase)
        return ReturnCodes.kOk

    def _destroySelfLoggerInstance(self, loggerClassKey, loggerInstanceKey, phase):
        self._log("functor-logger-instance-destroy-self").debug3("called. loggerClassKey=%s, loggerInstanceKey=%s, phase=%s", 
                                                              loggerClassKey, loggerInstanceKey, phase)
        return ReturnCodes.kOk


#######################################################################################################################
# LOGGER DESTINATION LIST
#######################################################################################################################

    def _attachToBlinkyLoggerDestinationList (self, loggerClassKey, loggerInstanceKey, blinkyLoggerDestinationList):
        """ attaches the housekeeper to the given blinky LoggerDestinationList
        Arguments:
            blinkyLoggerDestinationList
        """
        self._log("attach-to-blinky-logger-destination-list").debug3("attaching. loggerClassKey=%s, loggerInstanceKey=%s", 
                                                                     loggerClassKey, loggerInstanceKey)

        def prepareCandidateLoggerDestinationListAddDestinationFunctor(phase, loggerDestinationKey, blinkyLoggerDestination):
            return self._prepareCandidateLoggerDestinationListAddDestination(loggerClassKey, loggerInstanceKey, phase, loggerDestinationKey, blinkyLoggerDestination)
        blinkyLoggerDestinationList.setCreateFunctor(prepareCandidateLoggerDestinationListAddDestinationFunctor)           
        def prepareCandidateLoggerDestinationListDeleteDestinationFunctor(phase, loggerDestinationKey):
            return self._prepareCandidateLoggerDestinationListDeleteDestination(loggerClassKey, loggerInstanceKey, blinkyLoggerDestinationList, phase, loggerDestinationKey)                      
        blinkyLoggerDestinationList.setDeleteFunctor(prepareCandidateLoggerDestinationListDeleteDestinationFunctor)   
        def destroySelfLoggerDestinationListFunctor(phase):
            return self._destroySelfLoggerDestinationList(loggerClassKey, loggerInstanceKey, phase)
        blinkyLoggerDestinationList.setDestroySelfFunctor(destroySelfLoggerDestinationListFunctor)        

        # active the blinky node
        rc = blinkyLoggerDestinationList.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-logger-destination-list-failed-activating").error("failed to activate. loggerClassKey=%s, loggerInstanceKey=%s", 
                                                                             loggerClassKey, loggerInstanceKey)
            return ReturnCodes.kGeneralError 

        self._log("attach-logger-destination-list-activated").debug2("attached and activated. . loggerClassKey=%s, loggerInstanceKey=%s", 
                                                                     loggerClassKey, loggerInstanceKey)
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------
    def _prepareCandidateLoggerDestinationListAddDestination (self, loggerClassKey, loggerInstanceKey, phase, loggerDestinationKey, blinkyLoggerDestination):
        self._log("functor-logger-destination-list-add").debug3("add logger destination called. loggerClassKey=%s, loggerInstanceKey=%s, "\
                                                                "phase=%s, loggerDestinationKey=%s, blinkyLoggerDestination=%s", 
                                                                loggerClassKey, loggerInstanceKey, phase, loggerDestinationKey, blinkyLoggerDestination)

        if phase.isPreparePrivate():
            self._log("prepare-private-logger-destination-list").debug2("called. loggerClassKey=%s, loggerInstanceKey=%s, loggerDestinationKey=%s", 
                                                                     loggerClassKey, loggerInstanceKey, loggerDestinationKey)
            destArchiver = self._infraLoggerHousekeeper.preparePrivateDestinationArchiversListCreate(loggerClassKey, loggerInstanceKey, loggerDestinationKey)
            self._attachToBlinkyLoggerDestination(loggerClassKey, loggerInstanceKey, destArchiver, blinkyLoggerDestination, loggerDestinationKey)
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------
    def _prepareCandidateLoggerDestinationListDeleteDestination (self, loggerClassKey, loggerInstanceKey, blinkyLoggerDestinationList, phase, loggerDestinationKey):
        self._log("functor-logger-destination-list-del").debug3("delete logger destination called. loggerClassKey=%s, loggerInstanceKey=%s, "\
                                                                "phase=%s, loggerDestinationKey=%s,", 
                                                                 loggerClassKey, loggerInstanceKey, phase, loggerDestinationKey)
        __pychecker__ = 'unusednames=blinkyLoggerDestinationList' 
        #nothing to do
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------
    def _destroySelfLoggerDestinationList(self, loggerClassKey, loggerInstanceKey, phase):
        self._log("functor-logger-destination-list-destroy-self").debug3("called. loggerClassKey=%s, loggerInstanceKey=%s, phase=%s", 
                                                                         loggerClassKey, loggerInstanceKey, phase)
        return ReturnCodes.kOk


#######################################################################################################################
# LOGGER DESTINATION
#######################################################################################################################

    def _attachToBlinkyLoggerDestination (self, loggerClassKey, loggerInstanceKey, destinationArchiver, 
                                          blinkyLoggerDestination, loggerDestinationKey):
        self._log("attach-to-blinky-logger-destination").debug3("attaching, loggerClassKey=%s, loggerDestinationKey=%s",
                                                             loggerClassKey, loggerInstanceKey, loggerDestinationKey)

        # regular container functors
        def valueSetFunctor(phase, destinationData):
            return self._valueSetLoggerDestination(loggerClassKey, loggerInstanceKey, loggerDestinationKey,
                                                   destinationArchiver, phase, destinationData)
        blinkyLoggerDestination.setValueSetFunctor(valueSetFunctor)

        def destroySelfFunctor(phase):
            return self._destroySelfLoggerDestination(loggerClassKey, loggerInstanceKey, loggerDestinationKey,
                                                      destinationArchiver, blinkyLoggerDestination, phase)
        blinkyLoggerDestination.setDestroySelfFunctor(destroySelfFunctor)        

        # contained elements functors
        def createOutputFunctor(phase, blinkyLoggerDestinationOutput):
            return self._createLoggerDestinationOutput(loggerClassKey, loggerInstanceKey, loggerDestinationKey,
                                                       destinationArchiver, phase, blinkyLoggerDestinationOutput)        
        blinkyLoggerDestination.setCreateOutputFunctor(createOutputFunctor)

        # active the blinky node
        rc = blinkyLoggerDestination.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-logger-destination-failed-activating").error("failed to activate: loggerClassKey=%s, loggerDestinationKey=%s",
                                                                        loggerClassKey, loggerInstanceKey, loggerDestinationKey)
            return ReturnCodes.kGeneralError 

        self._log("attach-logger-destination-activated").debug2("attached and activated: loggerClassKey=%s, loggerDestinationKey=%s",
                                                             loggerClassKey, loggerInstanceKey, loggerDestinationKey)
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _valueSetLoggerDestination (self, loggerClassKey, loggerInstanceKey, loggerDestinationKey,
                                    destinationArchiver, phase, destinationData):
        self._log("value-set-logger-destination").debug3("functor called (%s.%s.%s) phase=%s, destinationData=%s", 
                                                         loggerClassKey, loggerInstanceKey, loggerDestinationKey,
                                                         phase, destinationData)
        if phase.isPreparePrivate():
            self._log("prepare-private-process").debug2("calling logger destination's (%s.%s.%s) value set prepare private", 
                                                        loggerClassKey, loggerInstanceKey, loggerDestinationKey)
            rc = destinationArchiver.preparePrivateLoggerDestinationValueSet(destinationData)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _destroySelfLoggerDestination (self, loggerClassKey, loggerInstanceKey, loggerDestinationKey,
                                       destinationArchiver, blinkyLoggerDestination, phase):
        __pychecker__ = 'unusednames=destinationArchiver' 
        self._log("destroy").debug3("functor called (%s.%s.%s). phase=%s", 
                                    loggerClassKey, loggerInstanceKey, loggerDestinationKey, phase)

        if phase.isCommitPrivate():
            self._log("destroy-logger-destination-manager").debug2("destroy self - logger destination (%s.%s.%s)", 
                                                                   loggerClassKey, loggerInstanceKey, loggerDestinationKey)
            blinkyLoggerDestination.deactivate()

        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createLoggerDestinationOutput (self, loggerClassKey, loggerInstanceKey, loggerDestinationKey,
                                        destinationArchiver, phase, blinkyLoggerDestinationOutput):        
        self._log("create-output").debug3("functor called (%s.%s.%s). phase=%s", 
                                          loggerClassKey, loggerInstanceKey, loggerDestinationKey, phase)

        if phase.isPreparePrivate():
            self._log("prepare-private-create-output").debug2("calling destination's (%s.%s.%s) create output prepare private",
                                                              loggerClassKey, loggerInstanceKey, loggerDestinationKey)
            rc = self._attachToBlinkyLoggerDestinationOutput(loggerClassKey, loggerInstanceKey, loggerDestinationKey,
                                                             destinationArchiver, blinkyLoggerDestinationOutput)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError

        return ReturnCodes.kOk


#######################################################################################################################
# LOGGER DESTINATION OUTPUT
#######################################################################################################################

    def _attachToBlinkyLoggerDestinationOutput (self, loggerClassKey, loggerInstanceKey, loggerDestinationKey,
                                                destinationArchiver, blinkyLoggerDestinationOutput):
        """ attaches the logger destination output to the given blinky
        """
        self._log("attach-logger-destination-output").debug3("attach output (%s.%s.%s)",
                                                             loggerClassKey, loggerInstanceKey, loggerDestinationKey)

        # regular container functors
        def valueSetFunctor(phase, outputData):
            return self._valueSetLoggerDestinationOutput(loggerClassKey, loggerInstanceKey, loggerDestinationKey,
                                                         destinationArchiver, phase, outputData)
        blinkyLoggerDestinationOutput.setValueSetFunctor(valueSetFunctor)

        def destroySelfFunctor(phase):
            return self._destroySelfLoggerDestinationOutput(loggerClassKey, loggerInstanceKey, loggerDestinationKey,
                                                            destinationArchiver, blinkyLoggerDestinationOutput, phase)
        blinkyLoggerDestinationOutput.setDestroySelfFunctor(destroySelfFunctor)        

        # activate the blinky node
        rc = blinkyLoggerDestinationOutput.activate()
        if rc != ReturnCodes.kOk:
            self._log("logger-destination-output-failed-activating").error("failed to activate logger output (%s.%s.%s)",
                                                                           loggerClassKey, loggerInstanceKey, loggerDestinationKey)
            return ReturnCodes.kGeneralError 

        self._log("attach-logger-destination-output-done").debug2("attached donelogger output (%s.%s.%s)",
                                                                  loggerClassKey, loggerInstanceKey, loggerDestinationKey)
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _valueSetLoggerDestinationOutput (self, loggerClassKey, loggerInstanceKey, loggerDestinationKey,
                                          destinationArchiver, phase, outputData):
        self._log("value-set-logger-destination-output").debug2("functor called (%s.%s.%s). phase=%s, outputData=%s", 
                                                                loggerClassKey, loggerInstanceKey, loggerDestinationKey,
                                                                phase, outputData)
        if phase.isPreparePrivate():
            self._log("prepare-private-process").debug2("calling logger destination output's (%s.%s.%s) value set prepare private",
                                                        loggerClassKey, loggerInstanceKey, loggerDestinationKey)
            rc = destinationArchiver.preparePrivateLoggerDestinationOutputValueSet(outputData)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _destroySelfLoggerDestinationOutput (self, loggerClassKey, loggerInstanceKey, loggerDestinationKey,
                                             destinationArchiver, blinkyLoggerDestinationOutput, phase):
        __pychecker__ = 'unusednames=destinationArchiver' 
        self._log("destroy").debug3("functor called (%s.%s.%s). phase=%s", 
                                    loggerClassKey, loggerInstanceKey, loggerDestinationKey, phase)

        if phase.isCommitPrivate():
            self._log("destroy-logger-destination-output-manager").debug2("destroy self - logger destination output (%s.%s.%s)",
                                                                          loggerClassKey, loggerInstanceKey, loggerDestinationKey)
            blinkyLoggerDestinationOutput.deactivate()

        return ReturnCodes.kOk

