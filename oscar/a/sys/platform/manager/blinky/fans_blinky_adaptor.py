#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: shmulika
# 

__pychecker__ = 'maxrefs=20' 

from a.infra.basic.return_codes import ReturnCodes

# fans
import a.sys.platform.tech_platform_fans.tech.platform.fans.blinky_fans_gen # BlinkyFans
import a.sys.platform.tech_platform_fans.tech.platform.fans.status.blinky_status_oper_gen # BlinkyOperStatus
import a.sys.platform.tech_platform_fans.tech.platform.fans.alarm.blinky_alarm_oper_gen # BlinkyOperAlarm

# fan
import a.sys.platform.tech_platform_fans.tech.platform.fans.fan.blinky_fan_gen # BlinkyFan
import a.sys.platform.tech_platform_fans.tech.platform.fans.fan.blinky_fan_list_gen # BlinkyFanList
import a.sys.platform.tech_platform_fans.tech.platform.fans.fan.device.blinky_device_gen # BlinkyDevice
import a.sys.platform.tech_platform_fans.tech.platform.fans.fan.device.status.blinky_status_oper_gen # BlinkyOperStatus
import a.sys.platform.tech_platform_fans.tech.platform.fans.fan.status.blinky_status_oper_gen # BlinkyOperStatus
import a.sys.platform.tech_platform_fans.tech.platform.fans.fan.alarm.blinky_alarm_oper_gen # BlinkyOperAlarm

import a.sys.blinky.domain_priority


# Bypass for PyChecker
if  __package__ is None:
    G_GROUP_NAME_PLATFORM_FANS_BLINKY_ADAPTOR           = "unknown"
else:
    from . import G_GROUP_NAME_PLATFORM_FANS_BLINKY_ADAPTOR     


class FansBlinkyAdaptor:
    """ Manages Blinky Adapter """

    def __init__ (self, logger, platformInitializer, configDomain, operDomain, maapiDomain):
        self._log = logger.createLoggerSameModule(G_GROUP_NAME_PLATFORM_FANS_BLINKY_ADAPTOR)
        self._configDomain = configDomain
        self._operDomain   = operDomain
        self._maapiDomain  = maapiDomain

        #TODO(shmulika): this name is going to change probably
        self._platformInitializer = platformInitializer

    def getMaapiDomain (self):
        return self._maapiDomain

#######################################################################################################################
# FANS
#######################################################################################################################
    
    def createAndAttachBlinkyFans (self, fans):
        self.blinkyFans = a.sys.platform.tech_platform_fans.tech.platform.fans.blinky_fans_gen.BlinkyFans.s_create(self._log, self._configDomain)
        rc = self._attachToBlinkyFans(self.blinkyFans, fans)
        if rc != ReturnCodes.kOk:
            self._log("create-and-attach-blinky-fans").error("failed.")
            return ReturnCodes.kGeneralError 

        self._configDomain.registerNode(self.blinkyFans)
        return ReturnCodes.kOk 


    def _attachToBlinkyFans (self, blinkyFans, fans):
        """ attaches the fans-supplies (managed-element) to the given blinky-fans object
        """
        self._log("attach-to-blinky-fans").debug3("attaching")
        
        # regular container functors        
        blinkyFans.setValueSetFunctor          (self._createFunctorFansValueSet(fans))
        blinkyFans.setNotifyTrxProgressFunctor (self._createFunctorFansTrxProgress(fans), True)
        blinkyFans.setDestroySelfFunctor       (self._createFunctorFansDestroySelf(blinkyFans, fans))        

        # containers & lists
        blinkyFans.setCreateSimulationFunctor(self._createFunctorFansCreateSimulation(fans))
        blinkyFans.setCreateFanListFunctor(self._createFunctorFansCreateFanList(fans))

        # error message functor        
        fans.setConfigMsgFunctor(lambda msgStr: blinkyFans.setConfigErrorStr(msgStr))

        # active the blinky node
        rc = blinkyFans.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-fans-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        # attach oper elements
        rc = self._attachToBlinkyFansStatus (self._operDomain, blinkyFans, fans)
        if rc != ReturnCodes.kOk:
            return ReturnCodes.kGeneralError 
        rc = self._attachToBlinkyFansAlarm (self._operDomain, blinkyFans, fans)
        if rc != ReturnCodes.kOk:
            return ReturnCodes.kGeneralError 

        return ReturnCodes.kOk 

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorFansValueSet (self, fans):
        self._log("create-functor-fans-supplies-value-set").debug2("created blinky-adapter functor")

        def functorFansValueSet (phase, fansData):
            self._log("functor-fans-value-set").debug2("functor called. phase=%s, fansData=%s", phase, fansData)
            if phase.isPreparePrivate():
                self._log("prepare-private-process").debug2("calling fans-supplies' preparePrivateData()")
                rc = fans.preparePrivateData(fansData)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError
    
            return ReturnCodes.kOk

        return functorFansValueSet

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorFansTrxProgress (self, fans):
        def functorFansTrxProgress (progress):
            """ Calls fans progress functors according to given progress """
            self._log("functor-fans-trx-progress").debug1("functor called.  progress=%s", progress)
    
            if progress.isPreparePrivateBefore():
                rc = fans.configStartTransaction()
                if rc!=ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError
    
            if progress.isPreparePrivateAfter():
                rc = fans.configPreparePrivateAfter()
                if rc!=ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            if progress.isPreparePublicAfter():
                rc = fans.configPreparePublicAfter()
                if rc!=ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            if progress.isCommitPublicBefore():
                rc = fans.configCommitTransaction()
                if rc!=ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            if progress.isAbortPrivateAfter():
                rc = fans.configAbortTransaction()
                if rc!=ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError
            
            return ReturnCodes.kOk

        return functorFansTrxProgress

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorFansDestroySelf (self, blinkyFans, fans):
        self._log("create-destroy-self-functor").debug3("creating destroy-self functor")

        def functorDestroySelf (phase):
            self._log("functor-destroy").debug2("functor called. phase=%s", phase)

            if phase.isCommitPrivate():
                self._log("destroy-fans-supplies").debug1("commit destroying fans-supplies")
                fans.destroy()
                blinkyFans.deactivate()

            return ReturnCodes.kOk

        return functorDestroySelf

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorFansCreateSimulation (self, fans):
        self._log("create-functor-create-simulation").debug2("created blinky-adapter functor")

        def functorCreateSimulation (phase, blinkySimulation):        
            self._log("functor-create-simulation").debug2("functor called. phase=%s", phase)

            if phase.isPreparePrivate():
                self._log("prepare-private-create-simulation").debug2("calling _attachToBlinkyFansSimulation()")    
                return self._attachToBlinkyFansSimulation(blinkySimulation, fans)

            if phase.isCommitPublic():
                # Simulation container has no oper - nothing special to do, kept as filler if oper inserted later
                pass

            return ReturnCodes.kOk

        return functorCreateSimulation

#----------------------------------------------------------------------------------------------------------------------

    def _attachToBlinkyFansSimulation (self, blinkySimulation, fans):
        """ attaches the fans to the given blinky simulation container
        """
        self._log("attach-to-blinky-simulation").debug3("attaching")

        # regular container functors        
        blinkySimulation.setValueSetFunctor          (self._createFunctorFansSimulationValueSet(fans))
        blinkySimulation.setDestroySelfFunctor       (self._createFunctorFansSimulationDestroySelf(blinkySimulation, fans))        

        # active the blinky node
        rc = blinkySimulation.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-simulation-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-simulation-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorFansSimulationValueSet (self, fans):
        self._log("create-functor-simulation-value-set").debug2("created blinky-adapter functor")

        def functorSimulationValueSet (phase, simulationData):
            self._log("functor-simulation-value-set").debug2("functor called. phase=%s, simulationData=%s", phase, simulationData)

            if phase.isPreparePrivate():
                self._log("prepare-private-process").debug2("calling fans's preparePrivateSimulationData()")
                rc = fans.preparePrivateSimulationData(simulationData)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorSimulationValueSet

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorFansSimulationDestroySelf(self, blinkySimulation, fans):
        """ creates a destroy self functor that does nothing """
        __pychecker__ = 'unusednames=blinkySimulation,fans'
        def functorSimulationDestroySelf (phase):
            self._log("functor-simulation-destroy-self").debug2("functor called. phase=%s", phase)
            return ReturnCodes.kOk

        return functorSimulationDestroySelf


#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorFansCreateFanList (self, fans):
        self._log("create-functor-create-fan-list").debug2("created blinky-adapter functor")
        __pychecker__ = "unusednames=fans"

        def functorCreateFanList (phase, blinkyFanList):        
            self._log("functor-create-fan-list").debug2("functor called. phase=%s, blinkyFanList=%s", phase, blinkyFanList)

            if phase.isPreparePrivate():
                self._log("prepare-private-create-fan-list").debug2("calling _attachToBlinkyFanList()")
                rc = self._attachToBlinkyFanList(blinkyFanList, fans)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorCreateFanList

#----------------------------------------------------------------------------------------------------------------------
    def _attachToBlinkyFansStatus (self, operDomain, blinkyFans, fans):
        self._log("attach-to-blinky-fans-status").debug3("attaching fans status")

        blinkyOpStatus = a.sys.platform.tech_platform_fans.tech.platform.fans.status.blinky_status_oper_gen.BlinkyOperStatus(self._log)
        blinkyOpStatus.setParent(blinkyFans)
        blinkyOpStatus.setConfigObj(blinkyFans)
        blinkyOpStatus.setDomain(operDomain)
        blinkyOpStatus.setBasicFunctors(self._createFunctorFansStatusGetObj(fans))                                       

        rc = blinkyOpStatus.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-fans-status-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-fans-status-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorFansStatusGetObj (self, fans):
        self._log("create-functor-fans-status-get-obj").debug2("created")

        def functorStatusGetObj (dpTrxContext, operData):
            self._log("functor-fans-status-get-obj").debug2("functor called. dpTrxContext=%s, operData=%s", dpTrxContext, operData)

            rc = fans.getObjStatusOperData(dpTrxContext, operData)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError 

            return ReturnCodes.kOk

        return functorStatusGetObj

#----------------------------------------------------------------------------------------------------------------------
    def _attachToBlinkyFansAlarm (self, operDomain, blinkyFans, fans):
        self._log("attach-to-blinky-fans-alarm").debug3("attaching")
        
        blinkyOpAlarm = a.sys.platform.tech_platform_fans.tech.platform.fans.alarm.blinky_alarm_oper_gen.BlinkyOperAlarm(self._log)
        blinkyOpAlarm.setParent(blinkyFans)
        blinkyOpAlarm.setConfigObj(blinkyFans)
        blinkyOpAlarm.setDomain(operDomain)
        blinkyOpAlarm.setBasicFunctors(self._createFunctorFansAlarmGetObj(fans))                                       

        rc = blinkyOpAlarm.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-fans-alarm-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-fans-alarm-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorFansAlarmGetObj (self, fans):
        self._log("create-functor-fans-alarm-get-obj").debug2("created")

        def functorAlarmGetObj (dpTrxContext, operData):
            self._log("functor-fans-alarm-get-obj").debug2("functor called. dpTrxContext=%s, operData=%s", dpTrxContext, operData)

            rc = fans.getObjAlarmOperData(dpTrxContext, operData)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError 

            return ReturnCodes.kOk

        return functorAlarmGetObj

#----------------------------------------------------------------------------------------------------------------------

    def _attachToBlinkyFanList (self, blinkyFanList, fans):
        """ attaches the alarm manager to the given blinky FanList
        Arguments:
            blinkyProcess - BlinkyProcess (a BlinkyNode created by Blinky)
            fans  - AlarmManager
        """
        self._log("attach-to-blinky-fan-list").debug3("attaching")

        blinkyFanList.setCreateFunctor     (self._createFunctorFanListCreate(fans, blinkyFanList))                                 
        blinkyFanList.setDeleteFunctor     (self._createFunctorFanListDelete(fans))   
        blinkyFanList.setDestroySelfFunctor(self._createFunctorFanListDestroySelf(fans))        

        # active the blinky node
        rc = blinkyFanList.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-fan-list-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-fan-list-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorFanListCreate (self, fans, blinkyFanList):
        self._log("create-functor-fan-list-create").debug2("created")

        def functorFanListCreate (phase, listKey, blinkyContainer):
            self._log("functor-fan-list").debug2("functor called. phase=%s, listKey=%s, blinkyContainer=%s", phase, listKey, blinkyContainer)

            if not blinkyFanList.isInTrigger():
                self._log("create-fan-not-in-trigger").debug1("cannot create fan %s out-of-trigger, fan list is static", listKey)
                fans.setConfigErrorStr("cannot create fan, fan list is static")
                return ReturnCodes.kGeneralError 

            if phase.isPreparePrivate():
                self._log("prepare-private-fan-list-create").debug2("creating a fan unit and attaching it to blinky")                
                #fan = self._platformInitializer.getFanUnit(listKey)
                fan = fans.createManagedUnit(listKey)
                if fan is None:
                    self._log("prepare-private-fan-list-create-fail").error("failed creating a fan unit")                
                    fans.setConfigErrorStr("failed creating fan unit")
                    return ReturnCodes.kGeneralError 

                return self._attachToBlinkyFan(blinkyContainer, fan)

            if phase.isCommitPublic():
                self._log("commit-public-fan-list-create").debug2("attaching the fan to oper domain")                
                # note: at commit phase this should never fail
                #fan = self._platformInitializer.getFanUnit(listKey)
                fan = fans.getManagedUnit(listKey)
                if fan is None:
                    self._log("commit-public-fan-list-create-fail").error("failed creating a fan unit, but not failing transaction - inconsistencies will probably occur")      
                    return ReturnCodes.kOk

                return self._attachToOperDomainFan(blinkyContainer, fan)


            return ReturnCodes.kOk

        return functorFanListCreate

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorFanListDelete (self, fans):
        self._log("create-functor-fan-list-create").debug2("created")

        def functorFanListDelete (phase, listKey):
            self._log("functor-fan-list").debug2("functor called. phase=%s, listKey=%s", phase, listKey)
            self._log("delete-fan-not-supported").debug1("cannot delete fan %s, fan list is static", listKey)
            fans.setConfigErrorStr("cannot delete fan, fan list is static")
            return ReturnCodes.kGeneralError 

        return functorFanListDelete

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorFanListDestroySelf(self, fans):
        """ creates a destroy self functor that does nothing """
        __pychecker__ = 'unusednames=fans'
        def functorFanListDestroySelf (phase):
            self._log("functor-fan-list-destroy-self").debug2("functor called. phase=%s", phase)
            return ReturnCodes.kOk

        return functorFanListDestroySelf

#----------------------------------------------------------------------------------------------------------------------

    def _attachToBlinkyFan (self, blinkyFan, fan):
        """ attaches the fans-suppy (managed-element) to the given blinky-fan object
        """
        self._log("attach-to-blinky-fan").debug3("attaching")
        
        # regular container functors        
        blinkyFan.setValueSetFunctor          (self._createFunctorFanValueSet(fan))
        #blinkyFan.setNotifyTrxProgressFunctor (self._createFunctorFanTrxProgress(fan), True)
        blinkyFan.setDestroySelfFunctor       (self._createFunctorFanDestroySelf(blinkyFan, fan))        

        # containers & lists
        blinkyFan.setCreateSimulationFunctor(self._createFunctorFanCreateSimulation(fan))
        blinkyFan.setCreateDeviceFunctor(self._createFunctorFanCreateDevice(fan))

        # error message functor        
        fan.setConfigMsgFunctor(lambda msgStr: blinkyFan.setConfigErrorStr(msgStr))

        # active the blinky node
        rc = blinkyFan.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-fan-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-fan-done").debug2("attached and activated")
        return ReturnCodes.kOk


    def _attachToOperDomainFan (self, blinkyFan, fan):        
        # attach oper elements
        rc = self._attachToBlinkyFanStatus(self._operDomain, blinkyFan, fan)
        if rc != ReturnCodes.kOk:
            # not failing transaction at commit!
            self._log("attach-to-oper-domain-fan-failed").error("failed attaching fan-status oper to blinky")
            
        rc = self._attachToBlinkyFanAlarm(self._operDomain, blinkyFan, fan)
        if rc != ReturnCodes.kOk:
            # not failing transaction at commit!
            self._log("attach-to-oper-domain-fan-failed").error("failed attaching fan-alarm oper to blinky")

        self._log("attach-to-oper-domain-fan-done").debug2("oper attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorFanValueSet (self, fan):
        self._log("create-functor-fan-supplies-value-set").debug2("created blinky-adapter functor")

        def functorFansValueSet (phase, fanData):
            self._log("functor-fan-value-set").debug2("functor called. phase=%s, fanData=%s", phase, fanData)
            if phase.isPreparePrivate():
                self._log("prepare-private-process").debug2("calling fan-supplies' preparePrivateData()")
                rc = fan.preparePrivateData(fanData)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorFansValueSet

#----------------------------------------------------------------------------------------------------------------------

#    def _createFunctorFanTrxProgress (self, fan):
#        def functorFanTrxProgress (progress):
#            """ Calls fan progress functors according to given progress """
#            self._log("functor-fan-trx-progress").debug1("functor called.  progress=%s", progress)
#
#            if progress.isPreparePrivateBefore():
#                rc = fan.configStartTransaction()
#                if rc!=ReturnCodes.kOk:
#                    return ReturnCodes.kGeneralError
#
#            if progress.isPreparePrivateAfter():
#                rc = fan.configPreparePrivateAfter()
#                if rc!=ReturnCodes.kOk:
#                    return ReturnCodes.kGeneralError
#
#            if progress.isPreparePublicAfter():
#                rc = fan.configPreparePublicAfter()
#                if rc!=ReturnCodes.kOk:
#                    return ReturnCodes.kGeneralError
#
#            if progress.isCommitPublicBefore():
#                rc = fan.configCommitTransaction()
#                if rc!=ReturnCodes.kOk:
#                    return ReturnCodes.kGeneralError
#
#            if progress.isAbortPrivateAfter():
#                rc = fan.configAbortTransaction()
#                if rc!=ReturnCodes.kOk:
#                    return ReturnCodes.kGeneralError
#
#            return ReturnCodes.kOk
#
#        return functorFanTrxProgress

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorFanDestroySelf (self, blinkyFans, fan):
        self._log("create-destroy-self-functor").debug3("creating destroy-self functor")

        def functorDestroySelf (phase):
            self._log("functor-destroy").debug2("functor called. phase=%s", phase)

            if phase.isCommitPrivate():
                self._log("destroy-fan-supplies").debug1("commit destroying fan-supplies")
                fan.destroy()
                blinkyFans.deactivate()

            return ReturnCodes.kOk

        return functorDestroySelf


#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorFanCreateSimulation (self, fan):
        self._log("create-functor-create-simulation").debug2("created blinky-adapter functor")

        def functorCreateSimulation (phase, blinkySimulation):        
            self._log("functor-create-simulation").debug2("functor called. phase=%s", phase)

            if phase.isPreparePrivate():
                self._log("prepare-private-create-simulation").debug2("calling _attachToBlinkyFanSimulation()")    
                return self._attachToBlinkyFanSimulation(blinkySimulation, fan)

            if phase.isCommitPublic():
                # Simulation container has no oper - nothing special to do, kept as filler if oper inserted later
                pass

            return ReturnCodes.kOk

        return functorCreateSimulation

#----------------------------------------------------------------------------------------------------------------------
    
    def _createFunctorFanCreateDevice (self, fan):
        self._log("create-functor-create-device").debug2("created blinky-adapter functor")

        def functorCreateDevice (phase, blinkyDevice):        
            self._log("functor-create-device").debug2("functor called. phase=%s", phase)
    
            if phase.isPreparePrivate():
                self._log("prepare-private-create-device").debug2("calling _attachToBlinkyFanDevice()")    
                return self._attachToBlinkyFanDevice(blinkyDevice, fan)

            if phase.isCommitPublic():
                self._log("commit-public-create-device").debug2("calling _attachToOperDomainFanDevice()")
                return self._attachToOperDomainFanDevice(blinkyDevice, fan)
                
            return ReturnCodes.kOk

        return functorCreateDevice

#----------------------------------------------------------------------------------------------------------------------
    def _attachToBlinkyFanStatus (self, operDomain, blinkyFan, fan):
        self._log("attach-to-blinky-fan-status").debug3("attaching")

        blinkyOpStatus = a.sys.platform.tech_platform_fans.tech.platform.fans.fan.status.blinky_status_oper_gen.BlinkyOperStatus(self._log)
        blinkyOpStatus.setParent(blinkyFan)
        blinkyOpStatus.setConfigObj(blinkyFan)
        blinkyOpStatus.setDomain(operDomain)
        blinkyOpStatus.setBasicFunctors(self._createFunctorFansStatusGetObj(fan))                                       

        rc = blinkyOpStatus.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-fan-status-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-fan-status-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorFanStatusGetObj (self, fan):
        self._log("create-functor-fan-status-get-obj").debug2("created")

        def functorStatusGetObj (dpTrxContext, operData):
            self._log("functor-fan-status-get-obj").debug2("functor called. dpTrxContext=%s, operData=%s", dpTrxContext, operData)

            rc = fan.getObjStatusOperData(dpTrxContext, operData)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError 

            return ReturnCodes.kOk

        return functorStatusGetObj

#----------------------------------------------------------------------------------------------------------------------
    def _attachToBlinkyFanAlarm (self, operDomain, blinkyFans, fan):
        self._log("attach-to-blinky-fan-alarm").debug3("attaching")

        blinkyOpAlarm = a.sys.platform.tech_platform_fans.tech.platform.fans.fan.alarm.blinky_alarm_oper_gen.BlinkyOperAlarm(self._log)
        blinkyOpAlarm.setParent(blinkyFans)
        blinkyOpAlarm.setConfigObj(blinkyFans)
        blinkyOpAlarm.setDomain(operDomain)
        blinkyOpAlarm.setBasicFunctors(self._createFunctorFansAlarmGetObj(fan))                                       

        rc = blinkyOpAlarm.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-fan-alarm-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-fan-alarm-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorFanAlarmGetObj (self, fan):
        self._log("create-functor-fan-alarm-get-obj").debug2("created")

        def functorAlarmGetObj (dpTrxContext, operData):
            self._log("functor-fan-alarm-get-obj").debug2("functor called. dpTrxContext=%s, operData=%s", dpTrxContext, operData)

            rc = fan.getObjAlarmOperData(dpTrxContext, operData)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError 

            return ReturnCodes.kOk

        return functorAlarmGetObj

#----------------------------------------------------------------------------------------------------------------------

    def _attachToBlinkyFanSimulation (self, blinkySimulation, fan):
        """ attaches the fan to the given blinky simulation container
        """
        self._log("attach-to-blinky-simulation").debug3("attaching")

        # regular container functors        
        blinkySimulation.setValueSetFunctor          (self._createFunctorFanSimulationValueSet(fan))
        blinkySimulation.setDestroySelfFunctor       (self._createFunctorFanSimulationDestroySelf(blinkySimulation, fan))        
              
        # active the blinky node
        rc = blinkySimulation.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-simulation-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-simulation-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorFanSimulationValueSet (self, fan):
        self._log("create-functor-simulation-value-set").debug2("created blinky-adapter functor")

        def functorSimulationValueSet (phase, simulationData):
            self._log("functor-simulation-value-set").debug2("functor called. phase=%s, simulationData=%s", phase, simulationData)

            if phase.isPreparePrivate():
                self._log("prepare-private-process").debug2("calling fan supply's preparePrivateSimulationData()")
                rc = fan.preparePrivateSimulationData(simulationData)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorSimulationValueSet

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorFanSimulationDestroySelf(self, blinkySimulation, fan):
        """ creates a destroy self functor that does nothing """
        __pychecker__ = 'unusednames=blinkySimulation,fan'
        def functorSimulationDestroySelf (phase):
            self._log("functor-simulation-destroy-self").debug2("functor called. phase=%s", phase)
            return ReturnCodes.kOk

        return functorSimulationDestroySelf
#----------------------------------------------------------------------------------------------------------------------

    def _attachToBlinkyFanDevice (self, blinkyDevice, fan):
        """ attaches the fans supply to the given blinky device
        Arguments:
            blinkyProcess - BlinkyProcess (a BlinkyNode created by Blinky)
            fan         - Nanny
        """
        self._log("attach-to-blinky-device").debug3("attaching")

        # regular container functors        
        blinkyDevice.setValueSetFunctor          (self._createFunctorFanDeviceValueSet(fan))
        blinkyDevice.setDestroySelfFunctor       (self._createFunctorFanDeviceDestroySelf(blinkyDevice, fan))        
              
        # active the blinky node
        rc = blinkyDevice.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-device-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-device-activated").debug2("attached and activated")
        return ReturnCodes.kOk


    def _attachToOperDomainFanDevice (self, blinkyDevice, fan):
        # attach oper elements
        rc = self._attachToBlinkyFanDeviceStatus (self._operDomain, blinkyDevice, fan)
        if rc != ReturnCodes.kOk:
            # not failing transaction at commit!
            self._log("attach-to-oper-domain-fan-device-failed").error("failed attaching fan-device-status oper to blinky")

        self._log("attach-to-oper-domain-device-activated").debug2("oper attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorFanDeviceValueSet (self, fan):
        self._log("create-functor-device-value-set").debug2("created blinky-adapter functor")

        def functorDeviceValueSet (phase, deviceData):
            self._log("functor-device-value-set").debug2("functor called. phase=%s, deviceData=%s", phase, deviceData)

            if phase.isPreparePrivate():
                self._log("prepare-private-process").debug2("calling fans supply's preparePrivateDeviceData()")
                rc = fan.preparePrivateDeviceData(deviceData)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorDeviceValueSet

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorFanDeviceDestroySelf(self, blinkyDevice, fan):
        """ creates a destroy self functor that does nothing """
        __pychecker__ = 'unusednames=blinkyDevice,fan'
        def functorDeviceDestroySelf (phase):
            self._log("functor-device-destroy-self").debug2("functor called. phase=%s", phase)
            return ReturnCodes.kOk

        return functorDeviceDestroySelf

#----------------------------------------------------------------------------------------------------------------------
    def _attachToBlinkyFanDeviceStatus (self, operDomain, blinkyDevice, fan):
        self._log("attach-to-blinky-fan-device-status").debug3("attaching")

        blinkyOpStatus = a.sys.platform.tech_platform_fans.tech.platform.fans.fan.device.status.blinky_status_oper_gen.BlinkyOperStatus(self._log)
        blinkyOpStatus.setParent(blinkyDevice)
        blinkyOpStatus.setConfigObj(blinkyDevice)
        blinkyOpStatus.setDomain(operDomain)
        blinkyOpStatus.setBasicFunctors(self._createFunctorFanDeviceStatusGetObj(fan))                                       

        rc = blinkyOpStatus.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-fan-status-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-fan-status-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorFanDeviceStatusGetObj (self, fan):
        self._log("create-functor-fan-status-get-obj").debug2("created")

        def functorStatusGetObj (dpTrxContext, operData):
            self._log("functor-fan-status-get-obj").debug2("functor called. dpTrxContext=%s, operData=%s", dpTrxContext, operData)

            rc = fan.getObjDeviceStatusOperData(dpTrxContext, operData)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError 

            return ReturnCodes.kOk

        return functorStatusGetObj


