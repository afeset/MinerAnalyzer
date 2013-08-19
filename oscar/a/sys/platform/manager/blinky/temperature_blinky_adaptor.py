#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: shmulika
# 

__pychecker__ = 'maxrefs=20' 

from a.infra.basic.return_codes import ReturnCodes

# temperature
import a.sys.platform.tech_platform_temperature.tech.platform.temperature.blinky_temperature_gen # BlinkyTemperature
import a.sys.platform.tech_platform_temperature.tech.platform.temperature.status.blinky_status_oper_gen # BlinkyOperStatus
import a.sys.platform.tech_platform_temperature.tech.platform.temperature.alarm.blinky_alarm_oper_gen # BlinkyOperAlarm

# sensor
import a.sys.platform.tech_platform_temperature.tech.platform.temperature.sensor.blinky_sensor_gen # BlinkySensor
import a.sys.platform.tech_platform_temperature.tech.platform.temperature.sensor.blinky_sensor_list_gen # BlinkySensorList
import a.sys.platform.tech_platform_temperature.tech.platform.temperature.sensor.device.blinky_device_gen # BlinkyDevice
import a.sys.platform.tech_platform_temperature.tech.platform.temperature.sensor.device.status.blinky_status_oper_gen # BlinkyOperStatus
import a.sys.platform.tech_platform_temperature.tech.platform.temperature.sensor.status.blinky_status_oper_gen # BlinkyOperStatus
import a.sys.platform.tech_platform_temperature.tech.platform.temperature.sensor.alarm.blinky_alarm_oper_gen # BlinkyOperAlarm

import a.sys.blinky.domain_priority


# Bypass for PyChecker
if  __package__ is None:
    G_GROUP_NAME_PLATFORM_TEMPERATURE_BLINKY_ADAPTOR           = "unknown"
else:
    from . import G_GROUP_NAME_PLATFORM_TEMPERATURE_BLINKY_ADAPTOR     


class TemperatureBlinkyAdaptor:
    """ Manages Blinky Adapter """

    def __init__ (self, logger, platformInitializer, configDomain, operDomain, maapiDomain):
        self._log = logger.createLoggerSameModule(G_GROUP_NAME_PLATFORM_TEMPERATURE_BLINKY_ADAPTOR)
        self._configDomain = configDomain
        self._operDomain   = operDomain
        self._maapiDomain  = maapiDomain

        #TODO(shmulika): this name is going to change probably
        self._platformInitializer = platformInitializer

    def getMaapiDomain (self):
        return self._maapiDomain

#######################################################################################################################
# TEMPERAURE
#######################################################################################################################
    
    def createAndAttachBlinkyTemperature (self, temperature):
        self.blinkyTemperature = a.sys.platform.tech_platform_temperature.tech.platform.temperature.blinky_temperature_gen.BlinkyTemperature.s_create(self._log, self._configDomain)
        rc = self._attachToBlinkyTemperature(self.blinkyTemperature, temperature)
        if rc != ReturnCodes.kOk:
            self._log("create-and-attach-blinky-temperature").error("failed.")
            return ReturnCodes.kGeneralError 

        self._configDomain.registerNode(self.blinkyTemperature)
        return ReturnCodes.kOk 


    def _attachToBlinkyTemperature (self, blinkyTemperature, temperature):
        """ attaches the temperature sub-system (managed-element) to the given blinky-temperature object
        """
        self._log("attach-to-blinky-temperature").debug3("attaching")
        
        # regular container functors        
        blinkyTemperature.setValueSetFunctor          (self._createFunctorTemperatureValueSet(temperature))
        blinkyTemperature.setNotifyTrxProgressFunctor (self._createFunctorTemperatureTrxProgress(temperature), True)
        blinkyTemperature.setDestroySelfFunctor       (self._createFunctorTemperatureDestroySelf(blinkyTemperature, temperature))        

        # containers & lists
        blinkyTemperature.setCreateSimulationFunctor(self._createFunctorTemperatureCreateSimulation(temperature))
        blinkyTemperature.setCreateSensorListFunctor(self._createFunctorTemperatureCreateSensorList(temperature))

        # error message functor        
        temperature.setConfigMsgFunctor(lambda msgStr: blinkyTemperature.setConfigErrorStr(msgStr))

        # active the blinky node
        rc = blinkyTemperature.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-temperature-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        # attach oper elements
        rc = self._attachToBlinkyTemperatureStatus (self._operDomain, blinkyTemperature, temperature)
        if rc != ReturnCodes.kOk:
            return ReturnCodes.kGeneralError 
        rc = self._attachToBlinkyTemperatureAlarm (self._operDomain, blinkyTemperature, temperature)
        if rc != ReturnCodes.kOk:
            return ReturnCodes.kGeneralError 

        return ReturnCodes.kOk 

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorTemperatureValueSet (self, temperature):
        self._log("create-functor-temperature-supplies-value-set").debug2("created blinky-adapter functor")

        def functorTemperatureValueSet (phase, temperatureData):
            self._log("functor-temperature-value-set").debug2("functor called. phase=%s, temperatureData=%s", phase, temperatureData)
            if phase.isPreparePrivate():
                self._log("prepare-private-process").debug2("calling temperature-supplies' preparePrivateData()")
                rc = temperature.preparePrivateData(temperatureData)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError
    
            return ReturnCodes.kOk

        return functorTemperatureValueSet

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorTemperatureTrxProgress (self, temperature):
        def functorTemperatureTrxProgress (progress):
            """ Calls temperature progress functors according to given progress """
            self._log("functor-temperature-trx-progress").debug1("functor called.  progress=%s", progress)
    
            if progress.isPreparePrivateBefore():
                rc = temperature.configStartTransaction()
                if rc!=ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError
    
            if progress.isPreparePrivateAfter():
                rc = temperature.configPreparePrivateAfter()
                if rc!=ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            if progress.isPreparePublicAfter():
                rc = temperature.configPreparePublicAfter()
                if rc!=ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            if progress.isCommitPublicBefore():
                rc = temperature.configCommitTransaction()
                if rc!=ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            if progress.isAbortPrivateAfter():
                rc = temperature.configAbortTransaction()
                if rc!=ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError
            
            return ReturnCodes.kOk

        return functorTemperatureTrxProgress

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorTemperatureDestroySelf (self, blinkyTemperature, temperature):
        self._log("create-destroy-self-functor").debug3("creating destroy-self functor")

        def functorDestroySelf (phase):
            self._log("functor-destroy").debug2("functor called. phase=%s", phase)

            if phase.isCommitPrivate():
                self._log("destroy-temperature-supplies").debug1("commit destroying temperature-supplies")
                temperature.destroy()
                blinkyTemperature.deactivate()

            return ReturnCodes.kOk

        return functorDestroySelf

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorTemperatureCreateSimulation (self, temperature):
        self._log("create-functor-create-simulation").debug2("created blinky-adapter functor")

        def functorCreateSimulation (phase, blinkySimulation):        
            self._log("functor-create-simulation").debug2("functor called. phase=%s", phase)

            if phase.isPreparePrivate():
                self._log("prepare-private-create-simulation").debug2("calling _attachToBlinkyTemperatureSimulation()")    
                return self._attachToBlinkyTemperatureSimulation(blinkySimulation, temperature)

            if phase.isCommitPublic():
                # Simulation container has no oper - nothing special to do, kept as filler if oper inserted later
                pass

            return ReturnCodes.kOk

        return functorCreateSimulation

#----------------------------------------------------------------------------------------------------------------------

    def _attachToBlinkyTemperatureSimulation (self, blinkySimulation, temperature):
        """ attaches the temperature to the given blinky simulation container
        """
        self._log("attach-to-blinky-simulation").debug3("attaching")

        # regular container functors        
        blinkySimulation.setValueSetFunctor          (self._createFunctorTemperatureSimulationValueSet(temperature))
        blinkySimulation.setDestroySelfFunctor       (self._createFunctorTemperatureSimulationDestroySelf(blinkySimulation, temperature))        

        # active the blinky node
        rc = blinkySimulation.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-simulation-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-simulation-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorTemperatureSimulationValueSet (self, temperature):
        self._log("create-functor-simulation-value-set").debug2("created blinky-adapter functor")

        def functorSimulationValueSet (phase, simulationData):
            self._log("functor-simulation-value-set").debug2("functor called. phase=%s, simulationData=%s", phase, simulationData)

            if phase.isPreparePrivate():
                self._log("prepare-private-process").debug2("calling temperature's preparePrivateSimulationData()")
                rc = temperature.preparePrivateSimulationData(simulationData)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorSimulationValueSet

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorTemperatureSimulationDestroySelf(self, blinkySimulation, temperature):
        """ creates a destroy self functor that does nothing """
        __pychecker__ = 'unusednames=blinkySimulation,temperature'
        def functorSimulationDestroySelf (phase):
            self._log("functor-simulation-destroy-self").debug2("functor called. phase=%s", phase)
            return ReturnCodes.kOk

        return functorSimulationDestroySelf
    
#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorTemperatureCreateSensorList (self, temperature):
        self._log("create-functor-create-sensor-list").debug2("created blinky-adapter functor")
        __pychecker__ = "unusednames=temperature"

        def functorCreateSensorList (phase, blinkySensorList):        
            self._log("functor-create-sensor-list").debug2("functor called. phase=%s, blinkySensorList=%s", phase, blinkySensorList)

            if phase.isPreparePrivate():
                self._log("prepare-private-create-sensor-list").debug2("calling _attachToBlinkySensorList()")
                rc = self._attachToBlinkySensorList(blinkySensorList, temperature)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorCreateSensorList

#----------------------------------------------------------------------------------------------------------------------
    def _attachToBlinkyTemperatureStatus (self, operDomain, blinkyTemperature, temperature):
        self._log("attach-to-blinky-temperature-status").debug3("attaching temperature status")

        blinkyOpStatus = a.sys.platform.tech_platform_temperature.tech.platform.temperature.status.blinky_status_oper_gen.BlinkyOperStatus(self._log)
        blinkyOpStatus.setParent(blinkyTemperature)
        blinkyOpStatus.setConfigObj(blinkyTemperature)
        blinkyOpStatus.setDomain(operDomain)
        blinkyOpStatus.setBasicFunctors(self._createFunctorTemperatureStatusGetObj(temperature))                                       

        rc = blinkyOpStatus.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-temperature-status-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-temperature-status-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorTemperatureStatusGetObj (self, temperature):
        self._log("create-functor-temperature-status-get-obj").debug2("created")

        def functorStatusGetObj (dpTrxContext, operData):
            self._log("functor-temperature-status-get-obj").debug2("functor called. dpTrxContext=%s, operData=%s", dpTrxContext, operData)

            rc = temperature.getObjStatusOperData(dpTrxContext, operData)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError 

            return ReturnCodes.kOk

        return functorStatusGetObj

#----------------------------------------------------------------------------------------------------------------------
    def _attachToBlinkyTemperatureAlarm (self, operDomain, blinkyTemperature, temperature):
        self._log("attach-to-blinky-temperature-alarm").debug3("attaching")
        
        blinkyOpAlarm = a.sys.platform.tech_platform_temperature.tech.platform.temperature.alarm.blinky_alarm_oper_gen.BlinkyOperAlarm(self._log)
        blinkyOpAlarm.setParent(blinkyTemperature)
        blinkyOpAlarm.setConfigObj(blinkyTemperature)
        blinkyOpAlarm.setDomain(operDomain)
        blinkyOpAlarm.setBasicFunctors(self._createFunctorTemperatureAlarmGetObj(temperature))                                       

        rc = blinkyOpAlarm.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-temperature-alarm-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-temperature-alarm-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorTemperatureAlarmGetObj (self, temperature):
        self._log("create-functor-temperature-alarm-get-obj").debug2("created")

        def functorAlarmGetObj (dpTrxContext, operData):
            self._log("functor-temperature-alarm-get-obj").debug2("functor called. dpTrxContext=%s, operData=%s", dpTrxContext, operData)

            rc = temperature.getObjAlarmOperData(dpTrxContext, operData)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError 

            return ReturnCodes.kOk

        return functorAlarmGetObj

#----------------------------------------------------------------------------------------------------------------------

    def _attachToBlinkySensorList (self, blinkySensorList, temperature):
        """ attaches the alarm manager to the given blinky SensorList
        Arguments:
            blinkyProcess - BlinkyProcess (a BlinkyNode created by Blinky)
            temperature  - AlarmManager
        """
        self._log("attach-to-blinky-sensor-list").debug3("attaching")

        blinkySensorList.setCreateFunctor     (self._createFunctorSensorListCreate(temperature, blinkySensorList))                                 
        blinkySensorList.setDeleteFunctor     (self._createFunctorSensorListDelete(temperature))   
        blinkySensorList.setDestroySelfFunctor(self._createFunctorSensorListDestroySelf(temperature))        

        # active the blinky node
        rc = blinkySensorList.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-sensor-list-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-sensor-list-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorSensorListCreate (self, temperature, blinkySensorList):
        self._log("create-functor-sensor-list-create").debug2("created")

        def functorSensorListCreate (phase, listKey, blinkyContainer):
            self._log("functor-sensor-list").debug2("functor called. phase=%s, listKey=%s, blinkyContainer=%s", phase, listKey, blinkyContainer)

            if not blinkySensorList.isInTrigger():
                self._log("create-sensor-not-in-trigger").debug1("cannot create sensor %s out-of-trigger, sensor list is static", listKey)
                temperature.setConfigErrorStr("cannot create sensor, sensor list is static")
                return ReturnCodes.kGeneralError 

            if phase.isPreparePrivate():
                self._log("prepare-private-sensor-list-create").debug2("creating a sensor unit and attaching it to blinky")                
                sensor = temperature.createManagedUnit(listKey)
                if sensor is None:
                    self._log("prepare-private-sensor-list-create-fail").error("failed creating a sensor unit")                
                    temperature.setConfigErrorStr("failed creating sensor unit")
                    return ReturnCodes.kGeneralError 

                return self._attachToBlinkySensor(blinkyContainer, sensor)

            if phase.isCommitPublic():
                self._log("commit-public-sensor-list-create").debug2("attaching the sensor to oper domain")                
                # note: at commit phase this should never fail
                sensor = temperature.getManagedUnit(listKey)
                if sensor is None:
                    self._log("commit-public-sensor-list-create-fail").error("failed creating a sensor unit, but not failing transaction - inconsistencies will probably occur")      
                    return ReturnCodes.kOk

                return self._attachToOperDomainSensor(blinkyContainer, sensor)


            return ReturnCodes.kOk

        return functorSensorListCreate

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorSensorListDelete (self, temperature):
        self._log("create-functor-sensor-list-create").debug2("created")

        def functorSensorListDelete (phase, listKey):
            self._log("functor-sensor-list").debug2("functor called. phase=%s, listKey=%s", phase, listKey)
            self._log("delete-sensor-not-supported").debug1("cannot delete sensor %s, sensor list is static", listKey)
            temperature.setConfigErrorStr("cannot delete sensor, sensor list is static")
            return ReturnCodes.kGeneralError 

        return functorSensorListDelete

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorSensorListDestroySelf(self, temperature):
        """ creates a destroy self functor that does nothing """
        __pychecker__ = 'unusednames=temperature'
        def functorSensorListDestroySelf (phase):
            self._log("functor-sensor-list-destroy-self").debug2("functor called. phase=%s", phase)
            return ReturnCodes.kOk

        return functorSensorListDestroySelf

#----------------------------------------------------------------------------------------------------------------------

    def _attachToBlinkySensor (self, blinkySensor, sensor):
        """ attaches the sensors-suppy (managed-element) to the given blinky-sensor object
        """
        self._log("attach-to-blinky-sensor").debug3("attaching")
        
        # regular container functors        
        blinkySensor.setValueSetFunctor          (self._createFunctorSensorValueSet(sensor))
        blinkySensor.setDestroySelfFunctor       (self._createFunctorSensorDestroySelf(blinkySensor, sensor))        

        # containers & lists
        blinkySensor.setCreateSimulationFunctor(self._createFunctorSensorCreateSimulation(sensor))
        blinkySensor.setCreateDeviceFunctor(self._createFunctorSensorCreateDevice(sensor))

        # error message functor        
        sensor.setConfigMsgFunctor(lambda msgStr: blinkySensor.setConfigErrorStr(msgStr))

        # active the blinky node
        rc = blinkySensor.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-sensor-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-sensor-done").debug2("attached and activated")
        return ReturnCodes.kOk


    def _attachToOperDomainSensor (self, blinkySensor, sensor):        
        # attach oper elements
        rc = self._attachToBlinkySensorStatus(self._operDomain, blinkySensor, sensor)
        if rc != ReturnCodes.kOk:
            # not failing transaction at commit!
            self._log("attach-to-oper-domain-sensor-failed").error("failed attaching sensor-status oper to blinky")
            
        rc = self._attachToBlinkySensorAlarm(self._operDomain, blinkySensor, sensor)
        if rc != ReturnCodes.kOk:
            # not failing transaction at commit!
            self._log("attach-to-oper-domain-sensor-failed").error("failed attaching sensor-alarm oper to blinky")

        self._log("attach-to-oper-domain-sensor-done").debug2("oper attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorSensorValueSet (self, sensor):
        self._log("create-functor-sensor-supplies-value-set").debug2("created blinky-adapter functor")

        def functorTemperatureValueSet (phase, sensorData):
            self._log("functor-sensor-value-set").debug2("functor called. phase=%s, sensorData=%s", phase, sensorData)
            if phase.isPreparePrivate():
                self._log("prepare-private-process").debug2("calling sensor-supplies' preparePrivateData()")
                rc = sensor.preparePrivateData(sensorData)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorTemperatureValueSet

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorSensorDestroySelf (self, temperature, sensor):
        self._log("create-destroy-self-functor").debug3("creating destroy-self functor")

        def functorDestroySelf (phase):
            self._log("functor-destroy").debug2("functor called. phase=%s", phase)

            if phase.isCommitPrivate():
                self._log("destroy-sensor-supplies").debug1("commit destroying sensor-supplies")
                sensor.destroy()
                temperature.deactivate()

            return ReturnCodes.kOk

        return functorDestroySelf

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorSensorCreateSimulation (self, sensor):
        self._log("create-functor-create-simulation").debug2("created blinky-adapter functor")

        def functorCreateSimulation (phase, blinkySimulation):        
            self._log("functor-create-simulation").debug2("functor called. phase=%s", phase)

            if phase.isPreparePrivate():
                self._log("prepare-private-create-simulation").debug2("calling _attachToBlinkySensorSimulation()")    
                return self._attachToBlinkySensorSimulation(blinkySimulation, sensor)

            if phase.isCommitPublic():
                # Simulation container has no oper - nothing special to do, kept as filler if oper inserted later
                pass

            return ReturnCodes.kOk

        return functorCreateSimulation

#----------------------------------------------------------------------------------------------------------------------
    
    def _createFunctorSensorCreateDevice (self, sensor):
        self._log("create-functor-create-device").debug2("created blinky-adapter functor")

        def functorCreateDevice (phase, blinkyDevice):        
            self._log("functor-create-device").debug2("functor called. phase=%s", phase)
    
            if phase.isPreparePrivate():
                self._log("prepare-private-create-device").debug2("calling _attachToBlinkySensorDevice()")    
                return self._attachToBlinkySensorDevice(blinkyDevice, sensor)

            if phase.isCommitPublic():
                self._log("commit-public-create-device").debug2("calling _attachToOperDomainSensorDevice()")
                return self._attachToOperDomainSensorDevice(blinkyDevice, sensor)
                
            return ReturnCodes.kOk

        return functorCreateDevice

#----------------------------------------------------------------------------------------------------------------------
    def _attachToBlinkySensorStatus (self, operDomain, blinkySensor, sensor):
        self._log("attach-to-blinky-sensor-status").debug3("attaching")

        blinkyOpStatus = a.sys.platform.tech_platform_temperature.tech.platform.temperature.sensor.status.blinky_status_oper_gen.BlinkyOperStatus(self._log)
        blinkyOpStatus.setParent(blinkySensor)
        blinkyOpStatus.setConfigObj(blinkySensor)
        blinkyOpStatus.setDomain(operDomain)
        blinkyOpStatus.setBasicFunctors(self._createFunctorSensorStatusGetObj(sensor))                                       

        rc = blinkyOpStatus.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-sensor-status-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-sensor-status-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorSensorStatusGetObj (self, sensor):
        self._log("create-functor-sensor-status-get-obj").debug2("created")

        def functorStatusGetObj (dpTrxContext, operData):
            self._log("functor-sensor-status-get-obj").debug2("functor called. dpTrxContext=%s, operData=%s", dpTrxContext, operData)

            rc = sensor.getObjStatusOperData(dpTrxContext, operData)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError 

            return ReturnCodes.kOk

        return functorStatusGetObj

#----------------------------------------------------------------------------------------------------------------------
    def _attachToBlinkySensorAlarm (self, operDomain, temperature, sensor):
        self._log("attach-to-blinky-sensor-alarm").debug3("attaching")

        blinkyOpAlarm = a.sys.platform.tech_platform_temperature.tech.platform.temperature.sensor.alarm.blinky_alarm_oper_gen.BlinkyOperAlarm(self._log)
        blinkyOpAlarm.setParent(temperature)
        blinkyOpAlarm.setConfigObj(temperature)
        blinkyOpAlarm.setDomain(operDomain)
        blinkyOpAlarm.setBasicFunctors(self._createFunctorSensorAlarmGetObj(sensor))                                       

        rc = blinkyOpAlarm.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-sensor-alarm-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-sensor-alarm-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorSensorAlarmGetObj (self, sensor):
        self._log("create-functor-sensor-alarm-get-obj").debug2("created")

        def functorAlarmGetObj (dpTrxContext, operData):
            self._log("functor-sensor-alarm-get-obj").debug2("functor called. dpTrxContext=%s, operData=%s", dpTrxContext, operData)

            rc = sensor.getObjAlarmOperData(dpTrxContext, operData)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError 

            return ReturnCodes.kOk

        return functorAlarmGetObj

#----------------------------------------------------------------------------------------------------------------------

    def _attachToBlinkySensorSimulation (self, blinkySimulation, sensor):
        """ attaches the sensor to the given blinky simulation container
        """
        self._log("attach-to-blinky-simulation").debug3("attaching")

        # regular container functors        
        blinkySimulation.setValueSetFunctor          (self._createFunctorSensorSimulationValueSet(sensor))
        blinkySimulation.setDestroySelfFunctor       (self._createFunctorSensorSimulationDestroySelf(blinkySimulation, sensor))        

        # active the blinky node
        rc = blinkySimulation.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-simulation-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-simulation-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorSensorSimulationValueSet (self, sensor):
        self._log("create-functor-simulation-value-set").debug2("created blinky-adapter functor")

        def functorSimulationValueSet (phase, simulationData):
            self._log("functor-simulation-value-set").debug2("functor called. phase=%s, simulationData=%s", phase, simulationData)

            if phase.isPreparePrivate():
                self._log("prepare-private-process").debug2("calling sensor supply's preparePrivateSimulationData()")
                rc = sensor.preparePrivateSimulationData(simulationData)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorSimulationValueSet

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorSensorSimulationDestroySelf(self, blinkySimulation, sensor):
        """ creates a destroy self functor that does nothing """
        __pychecker__ = 'unusednames=blinkySimulation,sensor'
        def functorSimulationDestroySelf (phase):
            self._log("functor-simulation-destroy-self").debug2("functor called. phase=%s", phase)
            return ReturnCodes.kOk

        return functorSimulationDestroySelf

#----------------------------------------------------------------------------------------------------------------------

    def _attachToBlinkySensorDevice (self, blinkyDevice, sensor):
        """ attaches the sensors supply to the given blinky device
        Arguments:
            blinkyProcess - BlinkyProcess (a BlinkyNode created by Blinky)
            sensor         - Nanny
        """
        self._log("attach-to-blinky-device").debug3("attaching")

        # regular container functors        
        blinkyDevice.setValueSetFunctor          (self._createFunctorSensorDeviceValueSet(sensor))
        blinkyDevice.setDestroySelfFunctor       (self._createFunctorSensorDeviceDestroySelf(blinkyDevice, sensor))        
              
        # active the blinky node
        rc = blinkyDevice.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-device-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-device-activated").debug2("attached and activated")
        return ReturnCodes.kOk


    def _attachToOperDomainSensorDevice (self, blinkyDevice, sensor):
        # attach oper elements
        rc = self._attachToBlinkySensorDeviceStatus (self._operDomain, blinkyDevice, sensor)
        if rc != ReturnCodes.kOk:
            # not failing transaction at commit!
            self._log("attach-to-oper-domain-sensor-device-failed").error("failed attaching sensor-device-status oper to blinky")

        self._log("attach-to-oper-domain-device-activated").debug2("oper attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorSensorDeviceValueSet (self, sensor):
        self._log("create-functor-device-value-set").debug2("created blinky-adapter functor")

        def functorDeviceValueSet (phase, deviceData):
            self._log("functor-device-value-set").debug2("functor called. phase=%s, deviceData=%s", phase, deviceData)

            if phase.isPreparePrivate():
                self._log("prepare-private-process").debug2("calling sensors supply's preparePrivateDeviceData()")
                rc = sensor.preparePrivateDeviceData(deviceData)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorDeviceValueSet

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorSensorDeviceDestroySelf(self, blinkyDevice, sensor):
        """ creates a destroy self functor that does nothing """
        __pychecker__ = 'unusednames=blinkyDevice,sensor'
        def functorDeviceDestroySelf (phase):
            self._log("functor-device-destroy-self").debug2("functor called. phase=%s", phase)
            return ReturnCodes.kOk

        return functorDeviceDestroySelf

#----------------------------------------------------------------------------------------------------------------------
    def _attachToBlinkySensorDeviceStatus (self, operDomain, blinkyDevice, sensor):
        self._log("attach-to-blinky-sensor-device-status").debug3("attaching")

        blinkyOpStatus = a.sys.platform.tech_platform_temperature.tech.platform.temperature.sensor.device.status.blinky_status_oper_gen.BlinkyOperStatus(self._log)
        blinkyOpStatus.setParent(blinkyDevice)
        blinkyOpStatus.setConfigObj(blinkyDevice)
        blinkyOpStatus.setDomain(operDomain)
        blinkyOpStatus.setBasicFunctors(self._createFunctorSensorDeviceStatusGetObj(sensor))                                       

        rc = blinkyOpStatus.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-sensor-status-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-sensor-status-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorSensorDeviceStatusGetObj (self, sensor):
        self._log("create-functor-sensor-status-get-obj").debug2("created")

        def functorStatusGetObj (dpTrxContext, operData):
            self._log("functor-sensor-status-get-obj").debug2("functor called. dpTrxContext=%s, operData=%s", dpTrxContext, operData)

            rc = sensor.getObjDeviceStatusOperData(dpTrxContext, operData)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError 

            return ReturnCodes.kOk

        return functorStatusGetObj


