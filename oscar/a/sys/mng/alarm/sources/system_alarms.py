
#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: shmulika
# 

import a.api.alarms.alarm.system_alarms

import a.sys.blinky.maapi_domain # this is a patch because of bug in MAAPI import, when naamas fixes - remove it
from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.qwilt_tech_system_alarms_module_gen import AlarmNameType
from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.alarms.alarms_maapi_gen import BlinkyAlarmsMaapi

from a.sys.mng.alarm.sources.source_base import AlarmSourceBase
from a.sys.mng.alarm.sources.source_base import AlarmSourceError
from a.sys.mng.alarm.sources.source_base import MaapiObject

class SystemAlarmsSource(AlarmSourceBase):

    ALARM_SOURCE_INSTACE_NAME = a.api.alarms.alarm.system_alarms.SYSTEM_ALARM_SOURCE_NAME    
    SUPPORTED_ALARM_NAME = a.api.alarms.alarm.system_alarms.SYSTEM_ALARM_NAME_TEST_ALARM_RAISED
    ALARM_ENTITY = "system-alarms"

    def __init__ (self, logger):
        AlarmSourceBase.__init__(self, logger, SystemAlarmsSource.ALARM_SOURCE_INSTACE_NAME)
        self.systemAlarmsObject = SystemAlarmsMaapiObject(logger, self)

    def initSupportedAlarmNames (self):
        self._addSupportedAlarmName(SystemAlarmsSource.SUPPORTED_ALARM_NAME)
    

    def _pollUnsimulatedActiveAlarms (self):
        # read and get the maapi object
        alarmMaapi = self.systemAlarmsObject.get()

        if alarmMaapi is None:
            # the get failed
            self._log("get-real-active-alarms").warning("alarm is None, should have been an object")
            raise AlarmSourceError("could not get system alarm information")

        if alarmMaapi.hasTestAlarm() and alarmMaapi.testAlarm:
            return [self._newAlarmInfo(SystemAlarmsSource.SUPPORTED_ALARM_NAME, SystemAlarmsSource.ALARM_ENTITY)]        

        # no alarms
        return []


class SystemAlarmsMaapiObject(MaapiObject):
    def __init__ (self, logger, alarmSource):
        MaapiObject.__init__(self, logger, alarmSource)

    def _getMaapiObject (self, logger):
        """ See base class
        """
        return BlinkyAlarmsMaapi(logger)

    def _requestObject (self, alarmsObject):
        """ Calls the extensions-specific request maapi fields """
        alarmsObject.requestTestAlarm(True)











