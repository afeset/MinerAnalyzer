#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: shmulika
# 

__pychecker__ = 'maxrefs=20' 

from a.infra.basic.return_codes import ReturnCodes

# power
import a.sys.platform.tech_platform_power.tech.platform.power.blinky_power_gen # BlinkyFans
import a.sys.platform.tech_platform_power.tech.platform.power.status.blinky_status_oper_gen # BlinkyOperStatus
import a.sys.platform.tech_platform_power.tech.platform.power.alarm.blinky_alarm_oper_gen # BlinkyOperAlarm

# power_supply
import a.sys.platform.tech_platform_power.tech.platform.power.power_supply.blinky_power_supply_gen # BlinkyPowerSupply
import a.sys.platform.tech_platform_power.tech.platform.power.power_supply.blinky_power_supply_list_gen # BlinkyPowerSupplyList
import a.sys.platform.tech_platform_power.tech.platform.power.power_supply.device.blinky_device_gen # BlinkyDevice
import a.sys.platform.tech_platform_power.tech.platform.power.power_supply.device.status.blinky_status_oper_gen # BlinkyOperStatus
import a.sys.platform.tech_platform_power.tech.platform.power.power_supply.status.blinky_status_oper_gen # BlinkyOperStatus
import a.sys.platform.tech_platform_power.tech.platform.power.power_supply.alarm.blinky_alarm_oper_gen # BlinkyOperAlarm

import a.sys.blinky.domain_priority


# Bypass for PyChecker
if  __package__ is None:
    G_GROUP_NAME_PLATFORM_POWER_BLINKY_ADAPTOR           = "unknown"
else:
    from . import G_GROUP_NAME_PLATFORM_POWER_BLINKY_ADAPTOR     


class PowerBlinkyAdaptor:
    """ Manages Blinky Adapter """

    def __init__ (self, logger, platformInitializer, configDomain, operDomain, maapiDomain):
        self._log = logger.createLoggerSameModule(G_GROUP_NAME_PLATFORM_POWER_BLINKY_ADAPTOR)
        self._configDomain = configDomain
        self._operDomain   = operDomain
        self._maapiDomain  = maapiDomain

        #TODO(shmulika): this name is going to change probably
        self._platformInitializer = platformInitializer

    def getMaapiDomain (self):
        return self._maapiDomain


#######################################################################################################################
# POWER
#######################################################################################################################
    
    def createAndAttachBlinkyPower (self, powerSupplies):
        self.blinkyPower = a.sys.platform.tech_platform_power.tech.platform.power.blinky_power_gen.BlinkyPower.s_create(self._log, self._configDomain)
        rc = self._attachToBlinkyPower(self.blinkyPower, powerSupplies)
        if rc != ReturnCodes.kOk:
            self._log("create-and-attach-blinky-power").error("failed.")
            return ReturnCodes.kGeneralError 

        self._configDomain.registerNode(self.blinkyPower)
        return ReturnCodes.kOk 


    def _attachToBlinkyPower (self, blinkyPower, powerSupplies):
        """ attaches the power-supplies (managed-element) to the given blinky-power object
        """
        self._log("attach-to-blinky-power").debug3("attaching")
        
        # regular container functors        
        blinkyPower.setValueSetFunctor          (self._createFunctorPowerValueSet(powerSupplies))
        blinkyPower.setNotifyTrxProgressFunctor (self._createFunctorPowerTrxProgress(powerSupplies), True)
        blinkyPower.setDestroySelfFunctor       (self._createFunctorPowerDestroySelf(blinkyPower, powerSupplies))        

        # containers & lists
        blinkyPower.setCreateSimulationFunctor(self._createFunctorPowerCreateSimulation(powerSupplies))
        blinkyPower.setCreatePowerSupplyListFunctor(self._createFunctorPowerCreatePowerSupplyList(powerSupplies))

        # error message functor        
        powerSupplies.setConfigMsgFunctor(lambda msgStr: blinkyPower.setConfigErrorStr(msgStr))

        # active the blinky node
        rc = blinkyPower.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-power-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        # attach oper elements
        rc = self._attachToBlinkyPowerStatus (self._operDomain, blinkyPower, powerSupplies)
        if rc != ReturnCodes.kOk:
            return ReturnCodes.kGeneralError 
        rc = self._attachToBlinkyPowerAlarm (self._operDomain, blinkyPower, powerSupplies)
        if rc != ReturnCodes.kOk:
            return ReturnCodes.kGeneralError
            
        return ReturnCodes.kOk 

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorPowerValueSet (self, powerSupplies):
        self._log("create-functor-power-supplies-value-set").debug2("created blinky-adapter functor")

        def functorPowerValueSet (phase, powerSuppliesData):
            self._log("functor-power-value-set").debug2("functor called. phase=%s, powerSuppliesData=%s", phase, powerSuppliesData)
            if phase.isPreparePrivate():
                self._log("prepare-private-process").debug2("calling power-supplies' preparePrivateData()")
                rc = powerSupplies.preparePrivateData(powerSuppliesData)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError
    
            return ReturnCodes.kOk

        return functorPowerValueSet

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorPowerTrxProgress (self, powerSupplies):
        def functorPowerTrxProgress (progress):
            """ Calls powerSupplies progress functors according to given progress """
            self._log("functor-power-trx-progress").debug1("functor called.  progress=%s", progress)
    
            if progress.isPreparePrivateBefore():
                rc = powerSupplies.configStartTransaction()
                if rc!=ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError
    
            if progress.isPreparePrivateAfter():
                rc = powerSupplies.configPreparePrivateAfter()
                if rc!=ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            if progress.isPreparePublicAfter():
                rc = powerSupplies.configPreparePublicAfter()
                if rc!=ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            if progress.isCommitPublicBefore():
                rc = powerSupplies.configCommitTransaction()
                if rc!=ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            if progress.isAbortPrivateAfter():
                rc = powerSupplies.configAbortTransaction()
                if rc!=ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError
            
            return ReturnCodes.kOk

        return functorPowerTrxProgress

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorPowerDestroySelf (self, blinkyPower, powerSupplies):
        self._log("create-destroy-self-functor").debug3("creating destroy-self functor")

        def functorDestroySelf (phase):
            self._log("functor-destroy").debug2("functor called. phase=%s", phase)

            if phase.isCommitPrivate():
                self._log("destroy-power-supplies").debug1("commit destroying power-supplies")
                powerSupplies.destroy()
                blinkyPower.deactivate()

            return ReturnCodes.kOk

        return functorDestroySelf

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorPowerCreateSimulation (self, powerSupplies):
        self._log("create-functor-create-simulation").debug2("created blinky-adapter functor")

        def functorCreateSimulation (phase, blinkySimulation):        
            self._log("functor-create-simulation").debug2("functor called. phase=%s", phase)

            if phase.isPreparePrivate():
                self._log("prepare-private-create-simulation").debug2("calling _attachToBlinkyPowerSimulation()")    
                return self._attachToBlinkyPowerSimulation(blinkySimulation, powerSupplies)

            if phase.isCommitPublic():
                # Simulation container has no oper - nothing special to do, kept as filler if oper inserted later
                pass

            return ReturnCodes.kOk

        return functorCreateSimulation

#----------------------------------------------------------------------------------------------------------------------

    def _attachToBlinkyPowerSimulation (self, blinkySimulation, powerSupplies):
        """ attaches the power to the given blinky simulation container
        """
        self._log("attach-to-blinky-simulation").debug3("attaching")

        # regular container functors        
        blinkySimulation.setValueSetFunctor          (self._createFunctorPowerSimulationValueSet(powerSupplies))
        blinkySimulation.setDestroySelfFunctor       (self._createFunctorPowerSimulationDestroySelf(blinkySimulation, powerSupplies))        

        # active the blinky node
        rc = blinkySimulation.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-simulation-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-simulation-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorPowerSimulationValueSet (self, powerSupplies):
        self._log("create-functor-simulation-value-set").debug2("created blinky-adapter functor")

        def functorSimulationValueSet (phase, simulationData):
            self._log("functor-simulation-value-set").debug2("functor called. phase=%s, simulationData=%s", phase, simulationData)

            if phase.isPreparePrivate():
                self._log("prepare-private-process").debug2("calling power's preparePrivateSimulationData()")
                rc = powerSupplies.preparePrivateSimulationData(simulationData)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorSimulationValueSet

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorPowerSimulationDestroySelf(self, blinkySimulation, power):
        """ creates a destroy self functor that does nothing """
        __pychecker__ = 'unusednames=blinkySimulation,power'
        def functorSimulationDestroySelf (phase):
            self._log("functor-simulation-destroy-self").debug2("functor called. phase=%s", phase)
            return ReturnCodes.kOk

        return functorSimulationDestroySelf

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorPowerCreatePowerSupplyList (self, powerSupplies):
        self._log("create-functor-create-power-supply-list").debug2("created blinky-adapter functor")
        __pychecker__ = "unusednames=powerSupplies"

        def functorCreatePowerSupplyList (phase, blinkyPowerSupplyList):        
            self._log("functor-create-power-supply-list").debug2("functor called. phase=%s, blinkyPowerSupplyList=%s", phase, blinkyPowerSupplyList)

            if phase.isPreparePrivate():
                self._log("prepare-private-create-power-supply-list").debug2("calling _attachToBlinkyPowerSupplyList()")
                rc = self._attachToBlinkyPowerSupplyList(blinkyPowerSupplyList, powerSupplies)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorCreatePowerSupplyList

#----------------------------------------------------------------------------------------------------------------------
    def _attachToBlinkyPowerStatus (self, operDomain, blinkyPower, powerSupplies):
        self._log("attach-to-blinky-power-status").debug3("attaching power status")

        blinkyOpStatus = a.sys.platform.tech_platform_power.tech.platform.power.status.blinky_status_oper_gen.BlinkyOperStatus(self._log)
        blinkyOpStatus.setParent(blinkyPower)
        blinkyOpStatus.setConfigObj(blinkyPower)
        blinkyOpStatus.setDomain(operDomain)
        blinkyOpStatus.setBasicFunctors(self._createFunctorPowerStatusGetObj(powerSupplies))                                       

        rc = blinkyOpStatus.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-power-status-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-power-status-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorPowerStatusGetObj (self, powerSupplies):
        self._log("create-functor-power-status-get-obj").debug2("created")

        def functorStatusGetObj (dpTrxContext, operData):
            self._log("functor-power-status-get-obj").debug2("functor called. dpTrxContext=%s, operData=%s", dpTrxContext, operData)

            rc = powerSupplies.getObjStatusOperData(dpTrxContext, operData)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError 

            return ReturnCodes.kOk

        return functorStatusGetObj

#----------------------------------------------------------------------------------------------------------------------
    def _attachToBlinkyPowerAlarm (self, operDomain, blinkyPower, powerSupplies):
        self._log("attach-to-blinky-power-alarm").debug3("attaching")
        
        blinkyOpAlarm = a.sys.platform.tech_platform_power.tech.platform.power.alarm.blinky_alarm_oper_gen.BlinkyOperAlarm(self._log)
        blinkyOpAlarm.setParent(blinkyPower)
        blinkyOpAlarm.setConfigObj(blinkyPower)
        blinkyOpAlarm.setDomain(operDomain)
        blinkyOpAlarm.setBasicFunctors(self._createFunctorPowerAlarmGetObj(powerSupplies))                                       

        rc = blinkyOpAlarm.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-power-alarm-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-power-alarm-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorPowerAlarmGetObj (self, powerSupplies):
        self._log("create-functor-power-alarm-get-obj").debug2("created")

        def functorAlarmGetObj (dpTrxContext, operData):
            self._log("functor-power-alarm-get-obj").debug2("functor called. dpTrxContext=%s, operData=%s", dpTrxContext, operData)

            rc = powerSupplies.getObjAlarmOperData(dpTrxContext, operData)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError 

            return ReturnCodes.kOk

        return functorAlarmGetObj

#----------------------------------------------------------------------------------------------------------------------

    def _attachToBlinkyPowerSupplyList (self, blinkyPowerSupplyList, powerSupplies):
        """ attaches the alarm manager to the given blinky PowerSupplyList
        Arguments:
            blinkyProcess - BlinkyProcess (a BlinkyNode created by Blinky)
            powerSupplies  - AlarmManager
        """
        self._log("attach-to-blinky-power-supply-list").debug3("attaching")

        blinkyPowerSupplyList.setCreateFunctor     (self._createFunctorPowerSupplyListCreate(powerSupplies, blinkyPowerSupplyList))                                 
        blinkyPowerSupplyList.setDeleteFunctor     (self._createFunctorPowerSupplyListDelete(powerSupplies))   
        blinkyPowerSupplyList.setDestroySelfFunctor(self._createFunctorPowerSupplyListDestroySelf(powerSupplies))        

        # active the blinky node
        rc = blinkyPowerSupplyList.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-power-supply-list-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-power-supply-list-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorPowerSupplyListCreate (self, powerSupplies, blinkyPowerSupplyList):
        self._log("create-functor-power-supply-list-create").debug2("created")

        def functorPowerSupplyListCreate (phase, listKey, blinkyContainer):
            self._log("functor-power-supply-list").debug2("functor called. phase=%s, listKey=%s, blinkyContainer=%s", phase, listKey, blinkyContainer)

            if not blinkyPowerSupplyList.isInTrigger():
                self._log("create-power-supply-not-in-trigger").debug1("cannot create power-supply %s out-of-trigger, power-supply list is static", listKey)
                powerSupplies.setConfigErrorStr("cannot create power-supply, power-supply list is static")
                return ReturnCodes.kGeneralError 

            if phase.isPreparePrivate():
                self._log("prepare-private-power-supply-list-create").debug2("creating a power-supply unit and attaching it to blinky")                
                #powerSupply = self._platformInitializer.getPowerSupplyUnit(listKey)
                powerSupply = powerSupplies.createManagedUnit(listKey)                
                if powerSupply is None:
                    self._log("prepare-private-power-supply-list-create-fail").error("failed creating a power-supply unit")                
                    powerSupplies.setConfigErrorStr("failed creating power-supply element")
                    return ReturnCodes.kGeneralError 

                return self._attachToBlinkyPowerSupply(blinkyContainer, powerSupply)

            if phase.isCommitPublic():
                self._log("commit-public-power-supply-list-create").debug2("attaching the power-supply to oper domain")                
                # note: at commit phase this should never fail
                #powerSupply = self._platformInitializer.getPowerSupplyUnit(listKey)
                powerSupply = powerSupplies.getManagedUnit(listKey)
                if powerSupply is None:
                    self._log("commit-public-power-supply-list-create-fail").error("failed creating a power-supply unit, but not failing transaction - inconsistencies will probably occur")      
                    return ReturnCodes.kOk

                return self._attachToOperDomainPowerSupply(blinkyContainer, powerSupply)


            return ReturnCodes.kOk

        return functorPowerSupplyListCreate

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorPowerSupplyListDelete (self, powerSupplies):
        self._log("create-functor-power-supply-list-create").debug2("created")

        def functorPowerSupplyListDelete (phase, listKey):
            self._log("functor-power-supply-list").debug2("functor called. phase=%s, listKey=%s", phase, listKey)
            self._log("delete-power-supply-not-supported").debug1("cannot delete power-supply %s, power-supply list is static", listKey)
            powerSupplies.setConfigErrorStr("cannot delete power-supply, power-supply list is static")
            return ReturnCodes.kGeneralError 

        return functorPowerSupplyListDelete

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorPowerSupplyListDestroySelf(self, powerSupplies):
        """ creates a destroy self functor that does nothing """
        __pychecker__ = 'unusednames=powerSupplies'
        def functorPowerSupplyListDestroySelf (phase):
            self._log("functor-power-supply-list-destroy-self").debug2("functor called. phase=%s", phase)
            return ReturnCodes.kOk

        return functorPowerSupplyListDestroySelf

#----------------------------------------------------------------------------------------------------------------------

    def _attachToBlinkyPowerSupply (self, blinkyPowerSupply, powerSupply):
        """ attaches the power-suppy (managed-element) to the given blinky-power-supply object
        """
        self._log("attach-to-blinky-power-supply").debug3("attaching")
        
        # regular container functors        
        blinkyPowerSupply.setValueSetFunctor          (self._createFunctorPowerSupplyValueSet(powerSupply))
        #blinkyPowerSupply.setNotifyTrxProgressFunctor (self._createFunctorPowerSupplyTrxProgress(powerSupply), True)
        blinkyPowerSupply.setDestroySelfFunctor       (self._createFunctorPowerSupplyDestroySelf(blinkyPowerSupply, powerSupply))        

        # containers & lists
        blinkyPowerSupply.setCreateSimulationFunctor(self._createFunctorPowerSupplyCreateSimulation(powerSupply))
        blinkyPowerSupply.setCreateDeviceFunctor(self._createFunctorPowerSupplyCreateDevice(powerSupply))
        

        # error message functor        
        powerSupply.setConfigMsgFunctor(lambda msgStr: blinkyPowerSupply.setConfigErrorStr(msgStr))

        # active the blinky node
        rc = blinkyPowerSupply.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-power-supply-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-power-supply-done").debug2("attached and activated")
        return ReturnCodes.kOk


    def _attachToOperDomainPowerSupply (self, blinkyPowerSupply, powerSupply):        
        # attach oper elements
        rc = self._attachToBlinkyPowerSupplyStatus(self._operDomain, blinkyPowerSupply, powerSupply)
        if rc != ReturnCodes.kOk:
            # not failing transaction at commit!
            self._log("attach-to-oper-domain-power-supply-failed").error("failed attaching power-supply-status oper to blinky")
            
        rc = self._attachToBlinkyPowerSupplyAlarm(self._operDomain, blinkyPowerSupply, powerSupply)
        if rc != ReturnCodes.kOk:
            # not failing transaction at commit!
            self._log("attach-to-oper-domain-power-supply-failed").error("failed attaching power-supply-alarm oper to blinky")

        self._log("attach-to-oper-domain-power-supply-done").debug2("oper attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorPowerSupplyValueSet (self, powerSupply):
        self._log("create-functor-power-supply-supplies-value-set").debug2("created blinky-adapter functor")

        def functorPowerValueSet (phase, powerSupplyData):
            self._log("functor-power-supply-value-set").debug2("functor called. phase=%s, powerSupplyData=%s", phase, powerSupplyData)
            if phase.isPreparePrivate():
                self._log("prepare-private-process").debug2("calling power-supply-supplies' preparePrivateData()")
                rc = powerSupply.preparePrivateData(powerSupplyData)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorPowerValueSet

##----------------------------------------------------------------------------------------------------------------------
#
#    def _createFunctorPowerSupplyTrxProgress (self, powerSupply):
#        def functorPowerSupplyTrxProgress (progress):
#            """ Calls powerSupply progress functors according to given progress """
#            self._log("functor-power-supply-trx-progress").debug1("functor called.  progress=%s", progress)
#
#            if progress.isPreparePrivateBefore():
#                rc = powerSupply.configStartTransaction()
#                if rc!=ReturnCodes.kOk:
#                    return ReturnCodes.kGeneralError
#
#            if progress.isPreparePrivateAfter():
#                rc = powerSupply.configPreparePrivateAfter()
#                if rc!=ReturnCodes.kOk:
#                    return ReturnCodes.kGeneralError
#
#            if progress.isPreparePublicAfter():
#                rc = powerSupply.configPreparePublicAfter()
#                if rc!=ReturnCodes.kOk:
#                    return ReturnCodes.kGeneralError
#
#            if progress.isCommitPublicBefore():
#                rc = powerSupply.configCommitTransaction()
#                if rc!=ReturnCodes.kOk:
#                    return ReturnCodes.kGeneralError
#
#            if progress.isAbortPrivateAfter():
#                rc = powerSupply.configAbortTransaction()
#                if rc!=ReturnCodes.kOk:
#                    return ReturnCodes.kGeneralError
#
#            return ReturnCodes.kOk
#
#        return functorPowerSupplyTrxProgress

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorPowerSupplyDestroySelf (self, blinkyPower, powerSupply):
        self._log("create-destroy-self-functor").debug3("creating destroy-self functor")

        def functorDestroySelf (phase):
            self._log("functor-destroy").debug2("functor called. phase=%s", phase)

            if phase.isCommitPrivate():
                self._log("destroy-power-supply-supplies").debug1("commit destroying power-supply-supplies")
                powerSupply.destroy()
                blinkyPower.deactivate()

            return ReturnCodes.kOk

        return functorDestroySelf

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorPowerSupplyCreateSimulation (self, powerSupply):
        self._log("create-functor-create-simulation").debug2("created blinky-adapter functor")

        def functorCreateSimulation (phase, blinkySimulation):        
            self._log("functor-create-simulation").debug2("functor called. phase=%s", phase)
    
            if phase.isPreparePrivate():
                self._log("prepare-private-create-simulation").debug2("calling _attachToBlinkyPowerSupplySimulation()")    
                return self._attachToBlinkyPowerSupplySimulation(blinkySimulation, powerSupply)

            if phase.isCommitPublic():
                # Simulation container has no oper - nothing special to do, kept as filler if oper inserted later
                pass
                
            return ReturnCodes.kOk

        return functorCreateSimulation


#----------------------------------------------------------------------------------------------------------------------
    
    def _createFunctorPowerSupplyCreateDevice (self, powerSupply):
        self._log("create-functor-create-device").debug2("created blinky-adapter functor")

        def functorCreateDevice (phase, blinkyDevice):        
            self._log("functor-create-device").debug2("functor called. phase=%s", phase)
    
            if phase.isPreparePrivate():
                self._log("prepare-private-create-device").debug2("calling _attachToBlinkyPowerSupplyDevice()")    
                return self._attachToBlinkyPowerSupplyDevice(blinkyDevice, powerSupply)

            if phase.isCommitPublic():
                self._log("commit-public-create-device").debug2("calling _attachToOperDomainPowerSupplyDevice()")
                return self._attachToOperDomainPowerSupplyDevice(blinkyDevice, powerSupply)
                
            return ReturnCodes.kOk

        return functorCreateDevice

#----------------------------------------------------------------------------------------------------------------------
    def _attachToBlinkyPowerSupplyStatus (self, operDomain, blinkyPowerSupply, powerSupply):
        self._log("attach-to-blinky-power-supply-status").debug3("attaching")

        blinkyOpStatus = a.sys.platform.tech_platform_power.tech.platform.power.power_supply.status.blinky_status_oper_gen.BlinkyOperStatus(self._log)
        blinkyOpStatus.setParent(blinkyPowerSupply)
        blinkyOpStatus.setConfigObj(blinkyPowerSupply)
        blinkyOpStatus.setDomain(operDomain)
        blinkyOpStatus.setBasicFunctors(self._createFunctorPowerStatusGetObj(powerSupply))                                       

        rc = blinkyOpStatus.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-power-supply-status-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-power-supply-status-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorPowerSupplyStatusGetObj (self, powerSupply):
        self._log("create-functor-power-supply-status-get-obj").debug2("created")

        def functorStatusGetObj (dpTrxContext, operData):
            self._log("functor-power-supply-status-get-obj").debug2("functor called. dpTrxContext=%s, operData=%s", dpTrxContext, operData)

            rc = powerSupply.getObjStatusOperData(dpTrxContext, operData)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError 

            return ReturnCodes.kOk

        return functorStatusGetObj

#----------------------------------------------------------------------------------------------------------------------
    def _attachToBlinkyPowerSupplyAlarm (self, operDomain, blinkyPower, powerSupply):
        self._log("attach-to-blinky-power-supply-alarm").debug3("attaching")

        blinkyOpAlarm = a.sys.platform.tech_platform_power.tech.platform.power.power_supply.alarm.blinky_alarm_oper_gen.BlinkyOperAlarm(self._log)
        blinkyOpAlarm.setParent(blinkyPower)
        blinkyOpAlarm.setConfigObj(blinkyPower)
        blinkyOpAlarm.setDomain(operDomain)
        blinkyOpAlarm.setBasicFunctors(self._createFunctorPowerAlarmGetObj(powerSupply))                                       

        rc = blinkyOpAlarm.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-power-supply-alarm-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-power-supply-alarm-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorPowerSupplyAlarmGetObj (self, powerSupply):
        self._log("create-functor-power-supply-alarm-get-obj").debug2("created")

        def functorAlarmGetObj (dpTrxContext, operData):
            self._log("functor-power-supply-alarm-get-obj").debug2("functor called. dpTrxContext=%s, operData=%s", dpTrxContext, operData)

            rc = powerSupply.getObjAlarmOperData(dpTrxContext, operData)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError 

            return ReturnCodes.kOk

        return functorAlarmGetObj

#----------------------------------------------------------------------------------------------------------------------

    def _attachToBlinkyPowerSupplySimulation (self, blinkySimulation, powerSupply):
        """ attaches the power supply to the given blinky simulation container
        """
        self._log("attach-to-blinky-simulation").debug3("attaching")

        # regular container functors        
        blinkySimulation.setValueSetFunctor          (self._createFunctorPowerSupplySimulationValueSet(powerSupply))
        blinkySimulation.setDestroySelfFunctor       (self._createFunctorPowerSupplySimulationDestroySelf(blinkySimulation, powerSupply))        
              
        # active the blinky node
        rc = blinkySimulation.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-simulation-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-simulation-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorPowerSupplySimulationValueSet (self, powerSupply):
        self._log("create-functor-simulation-value-set").debug2("created blinky-adapter functor")

        def functorSimulationValueSet (phase, simulationData):
            self._log("functor-simulation-value-set").debug2("functor called. phase=%s, simulationData=%s", phase, simulationData)

            if phase.isPreparePrivate():
                self._log("prepare-private-process").debug2("calling power supply's preparePrivateSimulationData()")
                rc = powerSupply.preparePrivateSimulationData(simulationData)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorSimulationValueSet

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorPowerSupplySimulationDestroySelf(self, blinkySimulation, powerSupply):
        """ creates a destroy self functor that does nothing """
        __pychecker__ = 'unusednames=blinkySimulation,powerSupply'
        def functorSimulationDestroySelf (phase):
            self._log("functor-simulation-destroy-self").debug2("functor called. phase=%s", phase)
            return ReturnCodes.kOk

        return functorSimulationDestroySelf

#----------------------------------------------------------------------------------------------------------------------

    def _attachToBlinkyPowerSupplyDevice (self, blinkyDevice, powerSupply):
        """ attaches the power supply to the given blinky device
        """
        self._log("attach-to-blinky-device").debug3("attaching")

        # regular container functors        
        blinkyDevice.setValueSetFunctor          (self._createFunctorPowerSupplyDeviceValueSet(powerSupply))
        blinkyDevice.setDestroySelfFunctor       (self._createFunctorPowerSupplyDeviceDestroySelf(blinkyDevice, powerSupply))        
              
        # active the blinky node
        rc = blinkyDevice.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-device-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-device-activated").debug2("attached and activated")
        return ReturnCodes.kOk


    def _attachToOperDomainPowerSupplyDevice (self, blinkyDevice, powerSupply):
        # attach oper elements
        rc = self._attachToBlinkyPowerSupplyDeviceStatus (self._operDomain, blinkyDevice, powerSupply)
        if rc != ReturnCodes.kOk:
            # not failing transaction at commit!
            self._log("attach-to-oper-domain-power-supply-device-failed").error("failed attaching power-supply-device-status oper to blinky")

        self._log("attach-to-oper-domain-device-activated").debug2("oper attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorPowerSupplyDeviceValueSet (self, powerSupply):
        self._log("create-functor-device-value-set").debug2("created blinky-adapter functor")

        def functorDeviceValueSet (phase, deviceData):
            self._log("functor-device-value-set").debug2("functor called. phase=%s, deviceData=%s", phase, deviceData)

            if phase.isPreparePrivate():
                self._log("prepare-private-process").debug2("calling power supply's preparePrivateDeviceData()")
                rc = powerSupply.preparePrivateDeviceData(deviceData)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorDeviceValueSet

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorPowerSupplyDeviceDestroySelf(self, blinkyDevice, powerSupply):
        """ creates a destroy self functor that does nothing """
        __pychecker__ = 'unusednames=blinkyDevice,powerSupply'
        def functorDeviceDestroySelf (phase):
            self._log("functor-device-destroy-self").debug2("functor called. phase=%s", phase)
            return ReturnCodes.kOk

        return functorDeviceDestroySelf

#----------------------------------------------------------------------------------------------------------------------
    def _attachToBlinkyPowerSupplyDeviceStatus (self, operDomain, blinkyDevice, powerSupply):
        self._log("attach-to-blinky-power-supply-device-status").debug3("attaching")

        blinkyOpStatus = a.sys.platform.tech_platform_power.tech.platform.power.power_supply.device.status.blinky_status_oper_gen.BlinkyOperStatus(self._log)
        blinkyOpStatus.setParent(blinkyDevice)
        blinkyOpStatus.setConfigObj(blinkyDevice)
        blinkyOpStatus.setDomain(operDomain)
        blinkyOpStatus.setBasicFunctors(self._createFunctorPowerSupplyDeviceStatusGetObj(powerSupply))                                       

        rc = blinkyOpStatus.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-power-supply-status-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-power-supply-status-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorPowerSupplyDeviceStatusGetObj (self, powerSupply):
        self._log("create-functor-power-supply-status-get-obj").debug2("created")

        def functorStatusGetObj (dpTrxContext, operData):
            self._log("functor-power-supply-status-get-obj").debug2("functor called. dpTrxContext=%s, operData=%s", dpTrxContext, operData)

            rc = powerSupply.getObjDeviceStatusOperData(dpTrxContext, operData)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError 

            return ReturnCodes.kOk

        return functorStatusGetObj

