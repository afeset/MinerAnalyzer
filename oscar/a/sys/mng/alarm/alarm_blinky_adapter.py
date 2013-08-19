#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: shmulika
# 

from a.infra.basic.return_codes import ReturnCodes

from a.sys.mng.alarm.tech_system_alarms.tech.system.alarms.blinky_alarms_gen import BlinkyAlarms
from a.sys.mng.alarm.tech_system_alarms.tech.system.alarms.list.blinky_list_oper_list_gen import BlinkyOperListList
from a.sys.mng.alarm.tech_system_alarms.tech.system.alarms.summary.blinky_summary_oper_gen import BlinkyOperSummary
from a.sys.mng.alarm.tech_system_alarms.tech.system.alarms.counters.blinky_counters_oper_gen import BlinkyOperCounters
from a.sys.mng.alarm.tech_system_alarms.tech.system.alarms.alarms.blinky_alarms_oper_gen import BlinkyOperAlarms
from a.sys.mng.alarm.tech_system_alarms.tech.system.alarms.registered.blinky_registered_oper_list_gen import BlinkyOperRegisteredList
from a.sys.mng.alarm.tech_system_alarms.tech.system.alarms.simulate.blinky_simulate_list_gen import BlinkySimulateList
from a.sys.mng.alarm.tech_system_alarms.tech.system.alarms.simulate.blinky_simulate_gen import BlinkySimulate

import a.sys.blinky.domain_priority


# Bypass for PyChecker
if  __package__ is None:
    G_NAME_GROUP_ALARM_BLINKY_ADAPTER           = "unknown"
else:
    from . import G_NAME_GROUP_ALARM_BLINKY_ADAPTER     


class AlarmBlinkyAdapter:
    """ Manages Blinky Adapter """


    def __init__ (self, logger):
        self._log = logger.createLoggerSameModule(G_NAME_GROUP_ALARM_BLINKY_ADAPTER)
        self._configDomain = None
        self._maapiDomain = None


    def createDomainAndBlinkyAlarmAndAttach (self, agent, alarmManager):
        """ Creates a domain, and a BlinkyAlarms node, and attaches it to the given AlarmManager """
        priority=a.sys.blinky.domain_priority.DomainPriority.kDefault
        self._configDomain = agent.createConfigDomain("config-alarms", priority)
        self._operDomain = agent.createConfigDomain("oper-alarms", priority)
        self._maapiDomain = agent.createMaapiDomain("maapi-alarms")

        self.blinkyAlarms = BlinkyAlarms.s_create(self._log, self._configDomain)
        self._attachToBlinkyAlarms(self.blinkyAlarms, alarmManager)
        
        # Do registertion
        self._operDomain.registrationDone() # TODO(shmulika): naamas might change this interface later for the oper-domain.
        self._configDomain.registerNode(self.blinkyAlarms)        
        self._configDomain.registrationDone()
        self._configDomain.triggerSubscriptions()


    def getMaapiDomain (self):
        return self._maapiDomain

#######################################################################################################################
# ALARMS
#######################################################################################################################
        
    def _attachToBlinkyAlarms (self, blinkyAlarms, alarmManager):
        """ attaches the alarm manager to the given blinky alarms
        """
        self._log("attach-to-blinky-alarms").debug3("attaching")

        # regular container functors        
        blinkyAlarms.setValueSetFunctor          (self._createFunctorAlarmsValueSet(alarmManager))
        blinkyAlarms.setNotifyTrxProgressFunctor (self._createFunctorTrxProgress(alarmManager), True) # TODO (shmulika): check what the True is for...
        blinkyAlarms.setDestroySelfFunctor       (self._createFunctorAlarmsDestroySelf(blinkyAlarms, alarmManager))        

        # contained elements functors
        blinkyAlarms.setCreateThresholdsFunctor  (self._createFunctorCreateThresholds(alarmManager))
        #blinkyAlarms.setDeleteThresholdsFunctor  (self.createFunctorDeleteThresholds) # TODO(shmulika): is necessary?

        blinkyAlarms.setCreateSimulateListFunctor(self._createFunctorCreateSimulateList(alarmManager))
        #blinkyAlarms.setDeleteSimulateListFunctor(self.create) # TODO(shmulika): is necessary?
        
        blinkyAlarms.setDoActionFunctor          (self._createFunctorDoAction(alarmManager))

        # error message functor        
        alarmManager.setConfigMsgFunctor(lambda msgStr: blinkyAlarms.setConfigErrorStr(msgStr))

        # active the blinky node
        rc = blinkyAlarms.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-alarms-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        # attach oper elements
        rc = self._attachToBlinkyList (self._operDomain, blinkyAlarms, alarmManager)
        if rc != ReturnCodes.kOk:
            return ReturnCodes.kGeneralError 

        rc = self._attachToBlinkySummary (self._operDomain, blinkyAlarms, alarmManager)
        if rc != ReturnCodes.kOk:
            return ReturnCodes.kGeneralError 

        rc = self._attachToBlinkyCounters (self._operDomain, blinkyAlarms, alarmManager)
        if rc != ReturnCodes.kOk:
            return ReturnCodes.kGeneralError 

        rc = self._attachToBlinkyDecalred (self._operDomain, blinkyAlarms, alarmManager)
        if rc != ReturnCodes.kOk:
            return ReturnCodes.kGeneralError 

        rc = self._attachToBlinkyAlarm (self._operDomain, blinkyAlarms, alarmManager)
        if rc != ReturnCodes.kOk:
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-alarms-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorAlarmsValueSet (self, alarmManager):
        self._log("create-functor-alarms-value-set").debug2("created blinky-adapter functor")

        def functorAlarmsValueSet (phase, alarmsData):
            self._log("functor-alarm-value-set").debug2("functor called. phase=%s, alarmsData=%s", phase, alarmsData)
            if phase.isPreparePrivate():
                self._log("prepare-private-process").debug2("calling alarm manager's preparePrivateAlarmData()")
                rc = alarmManager.preparePrivateAlarmData(alarmsData)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError
    
            return ReturnCodes.kOk

        return functorAlarmsValueSet

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorTrxProgress (self, alarmManager):
        def functorTrxProgress (progress):
            """ Calls alarmManager progress functors according to given progress """
            self._log("functor-trx-progress").debug1("functor called.  progress=%s", progress)
    
            if progress.isPreparePrivateBefore():
                rc = alarmManager.configStartTransaction()
                if rc!=ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError
    
            if progress.isPreparePrivateAfter():
                rc = alarmManager.configPreparePrivateAfter()
                if rc!=ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            if progress.isPreparePublicAfter():
                rc = alarmManager.configPreparePublicAfter()
                if rc!=ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            if progress.isCommitPublicBefore():
                rc = alarmManager.configCommitTransaction()
                if rc!=ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            if progress.isAbortPrivateAfter():
                rc = alarmManager.configAbortTransaction()
                if rc!=ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError
            
            return ReturnCodes.kOk

        return functorTrxProgress

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorAlarmsDestroySelf (self, blinkyAlarms, alarmManager):
        self._log("create-destroy-self-functor").debug3("creating destroy-self functor")

        def functorDestroySelf (phase):
            self._log("functor-destroy").debug2("functor called. phase=%s", phase)
            
            if phase.isCommitPrivate():
                self._log("destroy-alarm-manager").debug1("commit destroying alarm-manager")
                alarmManager.destroy()
                blinkyAlarms.deactivate()

            return ReturnCodes.kOk

        return functorDestroySelf

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorCreateThresholds (self, alarmManager):
        self._log("create-functor-create-thresholds").debug2("created blinky-adapter functor")

        def functorCreateThresholds (phase, blinkyThresholds):        
            self._log("functor-create-thresholds").debug2("functor called. phase=%s", phase)
    
            if phase.isPreparePrivate():
                self._log("prepare-private-create-thresholds").debug2("calling _attachToBlinkyThresholds()")
    
                rc = self._attachToBlinkyThresholds(blinkyThresholds, alarmManager)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError
    
            return ReturnCodes.kOk

        return functorCreateThresholds

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorCreateSimulateList (self, alarmManager):
        self._log("create-functor-create-simulate-list").debug2("created blinky-adapter functor")
        __pychecker__ = "unusednames=alarmManager"

        def functorCreateSimulateList (phase, blinkySimulateList):        
            self._log("functor-create-simulate-list").debug2("functor called. phase=%s, simulate-list=%s", phase, blinkySimulateList)

            if phase.isPreparePrivate():
                self._log("prepare-private-create-simulate-list").debug2("calling _attachToBlinkySimulateList()")
                rc = self._attachToBlinkySimulateList(blinkySimulateList, alarmManager)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorCreateSimulateList

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorCreateAlarm (self, alarmManager):
        self._log("create-functor-create-alarm").debug2("created blinky-adapter functor")

        def functorCreateAlarm (phase, blinkyAlarm):        
            self._log("functor-create-alarm").debug2("functor called. phase=%s", phase)

            if phase.isPreparePrivate():
                self._log("prepare-private-create-alarm").debug2("calling _attachToBlinkyAlarm()")

                rc = self._attachToBlinkyAlarm(blinkyAlarm, alarmManager)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorCreateAlarm

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorDoAction (self, alarmManager):
        self._log("create-functor-alarms-do-action").debug2("created blinky-adapter functor")

        def functorAlarmsDoAction (userInfo, actionPoint, actionName, params, nParams):
            self._log("functor-alarm-do-action").debug2("functor called. userInfo=%s, actionPoint=%s, actionName=%s, params=%s, nParams=%s", userInfo, actionPoint, actionName, params, nParams)

            rc, errMessage = alarmManager.actionClearCounters()
            if rc != ReturnCodes.kOk:
                alarmManager.setActionError(userInfo, errMessage)
                return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorAlarmsDoAction

#######################################################################################################################
# THRESHOLDS
#######################################################################################################################

    def _attachToBlinkyThresholds (self, blinkyThresholds, alarmManager):
        """ attaches the alarm manager to the given blinky thresholds
        Arguments:
            blinkyProcess - BlinkyProcess (a BlinkyNode created by Blinky)
            alarmManager         - Nanny
        """
        self._log("attach-to-blinky-thresholds").debug3("attaching")

        # regular container functors        
        blinkyThresholds.setValueSetFunctor          (self._createFunctorThresholdsValueSet(alarmManager))
        blinkyThresholds.setDestroySelfFunctor       (self._createFunctorThresholdsDestroySelf(blinkyThresholds, alarmManager))        
                
        # active the blinky node
        rc = blinkyThresholds.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-thresholds-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-thresholds-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorThresholdsValueSet (self, alarmManager):
        self._log("create-functor-thresholds-value-set").debug2("created blinky-adapter functor")

        def functorThresholdsValueSet (phase, thresholdsData):
            self._log("functor-thresholds-value-set").debug2("functor called. phase=%s, thresholdsData=%s", phase, thresholdsData)

            if phase.isPreparePrivate():
                self._log("prepare-private-process").debug2("calling alarm manager's preparePrivateThresholdsData()")
                rc = alarmManager.preparePrivateThresholdsData(thresholdsData)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorThresholdsValueSet

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorThresholdsDestroySelf(self, blinkyThresholds, alarmManager):
        """ creates a destroy self functor that does nothing """
        __pychecker__ = 'unusednames=blinkyThresholds,alarmManager'
        def functorThresholdsDestroySelf (phase):
            self._log("functor-thresholds-destroy-self").debug2("functor called. phase=%s", phase)
            return ReturnCodes.kOk

        return functorThresholdsDestroySelf

#######################################################################################################################
# SIMULATE
#######################################################################################################################

    def _attachToBlinkySimulateList (self, blinkySimulateList, alarmManager):
        """ attaches the alarm manager to the given blinky SimulateList
        Arguments:
            blinkyProcess - BlinkyProcess (a BlinkyNode created by Blinky)
            alarmManager  - AlarmManager
        """
        self._log("attach-to-blinky-simulate-list").debug3("attaching")

        blinkySimulateList.setCreateFunctor     (self._createFunctorSimulateListCreate(alarmManager))                                 
        blinkySimulateList.setDeleteFunctor     (self._createFunctorSimulateListDelete(alarmManager))   
        blinkySimulateList.setDestroySelfFunctor(self._createFunctorSimulateListDestroySelf(alarmManager))        

        # active the blinky node
        rc = blinkySimulateList.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-simulate-list-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-simulate-list-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorSimulateListCreate (self, alarmManager):
        self._log("create-functor-simulate-list-create").debug2("created")

        def functorSimulateListCreate (phase, listKey, blinkyContainer):
            self._log("functor-simulate-list").debug2("functor called. phase=%s, listKey=%s, blinkyContainer=%s", phase, listKey, blinkyContainer)

            if phase.isPreparePrivate():
                self._log("prepare-private-simulate-list-create").debug2("calling alarm manager's preparePrivateSimulateListCreate()")
                rc = alarmManager.preparePrivateSimulateListCreate(listKey)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError 

                # value sets will be received by the added container itself
                self._attachToBlinkySimulate(blinkyContainer, listKey, alarmManager)

            return ReturnCodes.kOk

        return functorSimulateListCreate

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorSimulateListDelete (self, alarmManager):
        self._log("create-functor-simulate-list-create").debug2("created")

        def functorSimulateListDelete (phase, listKey):
            self._log("functor-simulate-list").debug2("functor called. phase=%s, listKey=%s", phase, listKey)

            if phase.isPreparePrivate():
                self._log("prepare-private-simulate-list-create").debug2("calling alarm manager's preparePrivateSimulateListCreate()")
                rc = alarmManager.preparePrivateSimulateListDelete(listKey)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError 

            return ReturnCodes.kOk

        return functorSimulateListDelete

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorSimulateListDestroySelf(self, alarmManager):
        """ creates a destroy self functor that does nothing """
        __pychecker__ = 'unusednames=alarmManager'
        def functorSimulateListDestroySelf (phase):
            self._log("functor-simulate-list-destroy-self").debug2("functor called. phase=%s", phase)
            return ReturnCodes.kOk

        return functorSimulateListDestroySelf


#----------------------------------------------------------------------------------------------------------------------

    def _attachToBlinkySimulate (self, blinkySimulate, listKey, alarmManager):
        """ attaches the alarm manager to the given blinky SimulateList
        Arguments:
            blinkySimulate - BlinkySimulate (a BlinkyNode created by Blinky)
            alarmManager  - AlarmManager
        """
        self._log("attach-to-blinky-simulate").debug3("attaching")

        # regular container functors        
        blinkySimulate.setValueSetFunctor          (self._createFunctorSimulateValueSet(listKey, alarmManager))
        blinkySimulate.setDestroySelfFunctor       (self._createFunctorSimulateDestroySelf(listKey, alarmManager))        

        # active the blinky node
        rc = blinkySimulate.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-simulate-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-simulate-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorSimulateValueSet (self, listKey, alarmManager):
        self._log("create-functor-simulate-value-set").debug2("created blinky-adapter functor")

        def functorSimulateValueSet (phase, simulateData):
            self._log("functor-simulate-value-set").debug2("functor called. phase=%s, simulateData=%s", phase, simulateData)
            if phase.isPreparePrivate():
                self._log("prepare-private-simulate-value-set").debug2("calling alarm manager's preparePrivateSimulateData(listKey=%s,...)", listKey)
                rc = alarmManager.preparePrivateSimulateData(listKey, simulateData)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorSimulateValueSet

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorSimulateDestroySelf(self, listKey, alarmManager):
        """ creates a destroy self functor that does nothing """
        __pychecker__ = 'unusednames=listKey,alarmManager'
        def functorSimulateDestroySelf (phase):
            self._log("functor-simulate-destroy-self").debug2("functor called. phase=%s", phase)
            return ReturnCodes.kOk

        return functorSimulateDestroySelf

#######################################################################################################################
# SUMMARY
#######################################################################################################################

    def _attachToBlinkySummary (self, operDomain, blinkyAlarms, alarmManager):
        self._log("attach-to-blinky-alarms-summary").debug3("attaching")

        blinkyOpSummary = BlinkyOperSummary(self._log)
        blinkyOpSummary.setParent(blinkyAlarms)
        blinkyOpSummary.setConfigObj(blinkyAlarms)
        blinkyOpSummary.setDomain(operDomain)
        blinkyOpSummary.setBasicFunctors(self._createFunctorSummaryGetObj(alarmManager))                                       

        rc = blinkyOpSummary.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-alarms-summary-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-alarms-summary-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorSummaryGetObj (self, alarmManager):
        self._log("create-functor-summary-get-obj").debug2("created")

        def functorSummaryGetObj (dpTrxContext, operData):
            self._log("functor-summary-get-obj").debug2("functor called. dpTrxContext=%s, operData=%s", dpTrxContext, operData)

            rc = alarmManager.getObjSummaryOperData(dpTrxContext, operData)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError 

            return ReturnCodes.kOk

        return functorSummaryGetObj


#######################################################################################################################
# COUNTERS
#######################################################################################################################

    def _attachToBlinkyCounters (self, operDomain, blinkyAlarms, alarmManager):
        self._log("attach-to-blinky-alarms-counters").debug3("attaching")

        blinkyOpCounters = BlinkyOperCounters(self._log)
        blinkyOpCounters.setParent(blinkyAlarms)
        blinkyOpCounters.setConfigObj(blinkyAlarms)
        blinkyOpCounters.setDomain(operDomain)
        blinkyOpCounters.setBasicFunctors(self._createFunctorCountersGetObj(alarmManager))                                       

        rc = blinkyOpCounters.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-alarms-counters-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-alarms-counters-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorCountersGetObj (self, alarmManager):
        self._log("create-functor-counters-get-obj").debug2("created")

        def functorCountersGetObj (dpTrxContext, operData):
            self._log("functor-counters-get-obj").debug2("functor called. dpTrxContext=%s, operData=%s", dpTrxContext, operData)

            rc = alarmManager.getObjCountersOperData(dpTrxContext, operData)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError 

            return ReturnCodes.kOk

        return functorCountersGetObj

#######################################################################################################################
# ALARM
#######################################################################################################################

    def _attachToBlinkyAlarm (self, operDomain, blinkyAlarms, alarmManager):
        self._log("attach-to-blinky-alarms-alarm").debug3("attaching")

        blinkyOpAlarm = BlinkyOperAlarms(self._log)
        blinkyOpAlarm.setParent(blinkyAlarms)
        blinkyOpAlarm.setConfigObj(blinkyAlarms)
        blinkyOpAlarm.setDomain(operDomain)
        blinkyOpAlarm.setBasicFunctors(self._createFunctorAlarmGetObj(alarmManager))                                       

        rc = blinkyOpAlarm.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-alarms-alarm-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-alarms-alarm-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorAlarmGetObj (self, alarmManager):
        self._log("create-functor-alarm-get-obj").debug2("created")

        def functorAlarmGetObj (dpTrxContext, operData):
            self._log("functor-alarm-get-obj").debug2("functor called. dpTrxContext=%s, operData=%s", dpTrxContext, operData)

            rc = alarmManager.getObjAlarmOperData(dpTrxContext, operData)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError 

            return ReturnCodes.kOk

        return functorAlarmGetObj

#######################################################################################################################
# LIST
#######################################################################################################################
  
    def _attachToBlinkyList (self, operDomain, blinkyAlarms, alarmManager):
        self._log("attach-to-blinky-alarms-list").debug3("attaching")

        blinkyOpList = BlinkyOperListList(self._log)
        blinkyOpList.setParent(blinkyAlarms)
        blinkyOpList.setConfigObj(blinkyAlarms)
        blinkyOpList.setDomain(operDomain)
        blinkyOpList.setBasicFunctors(self._createFunctorListGetObj(alarmManager),\
                                       self._createFunctorListGetNext(alarmManager))

        rc = blinkyOpList.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-alarms-list-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-alarms-list-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------
    
    def _createFunctorListGetObj (self, alarmManager):
        self._log("create-functor-list-get-obj").debug2("created")

        def functorListGetObj (dpTrxContext, key, operData):
            self._log("functor-list-get-obj").debug2("functor called. dpTrxContext=%s, key=%s, operData=%s", dpTrxContext, key, operData)

            rc = alarmManager.getObjAlarmsList(dpTrxContext, key, operData)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError 

            return ReturnCodes.kOk

        return functorListGetObj

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorListGetNext (self, alarmManager):
        self._log("create-functor-list-get-next").debug2("created")

        def functorListGetNext (dpTrxContext, key, nextKey, isCompleted):
            self._log("functor-list-get-next").debug2("functor called. dpTrxContext=%s, key=%s, nextKey=%s, isCompleted=%s", dpTrxContext, key, nextKey, isCompleted)

            rc = alarmManager.getNextAlarmsList(dpTrxContext, key, nextKey, isCompleted)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError 

            return ReturnCodes.kOk

        return functorListGetNext

#######################################################################################################################
# DECLARED
#######################################################################################################################

    def _attachToBlinkyDecalred (self, operDomain, blinkyAlarms, alarmManager):
        self._log("attach-to-blinky-alarms-registered").debug3("attaching")

        blinkyOpRegistered = BlinkyOperRegisteredList(self._log)
        blinkyOpRegistered.setParent(blinkyAlarms)
        blinkyOpRegistered.setConfigObj(blinkyAlarms)
        blinkyOpRegistered.setDomain(operDomain)
        blinkyOpRegistered.setBasicFunctors(self._createFunctorRegisteredGetObj(alarmManager),\
                                       self._createFunctorRegisteredGetNext(alarmManager))

        rc = blinkyOpRegistered.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-alarms-registered-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-alarms-registered-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorRegisteredGetObj (self, alarmManager):
        self._log("create-functor-registered-get-obj").debug2("created")

        def functorRegisteredGetObj (dpTrxContext, key, operData):
            self._log("functor-registered-get-obj").debug2("functor called. dpTrxContext=%s, key=%s, operData=%s", dpTrxContext, key, operData)

            rc = alarmManager.getObjRegisteredList(dpTrxContext, key, operData)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError 

            return ReturnCodes.kOk

        return functorRegisteredGetObj

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorRegisteredGetNext (self, alarmManager):
        self._log("create-functor-registered-get-next").debug2("created")

        def functorRegisteredGetNext (dpTrxContext, key, nextKey, isCompleted):
            self._log("functor-registered-get-next").debug2("functor called. dpTrxContext=%s, key=%s, nextKey=%s, isCompleted=%s", dpTrxContext, key, nextKey, isCompleted)

            rc = alarmManager.getNextRegisteredList(dpTrxContext, key, nextKey, isCompleted)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError 

            return ReturnCodes.kOk

        return functorRegisteredGetNext

