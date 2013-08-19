
#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: shmulika
# 

import a.api.alarms.alarm.interface

import a.sys.blinky.maapi_domain # this is a patch because of bug in MAAPI import, when naamas fixes - remove it
from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.qwilt_tech_system_alarms_module_gen import AlarmNameType
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.interface_maapi_list_gen import BlinkyInterfaceMaapiList
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.interface_maapi_gen import BlinkyInterfaceMaapi

from a.sys.mng.alarm.sources.source_base import AlarmSourceBase
from a.sys.mng.alarm.sources.source_base import AlarmSourceError
from a.sys.mng.alarm.sources.source_base import StaticMaapiList

class InterfaceSource(AlarmSourceBase):

    ALARM_SOURCE_INSTACE_NAME = a.api.alarms.alarm.interface.INTERFACE_ALARM_SOURCE_NAME
    
    # TODO(shmulika): change this to proper alarms
    SUPPORTED_ALARM_NAME_INTERFACE_FAILURE         = a.api.alarms.alarm.interface.INTERFACE_ALARM_NAME_FAILURE
    SUPPORTED_ALARM_NAME_IPV4_CONNECTIVITY_FAILURE = a.api.alarms.alarm.interface.INTERFACE_ALARM_NAME_IPV4_CONNECTIVITY_FAILURE
    SUPPORTED_ALARM_NAME_IPV6_CONNECTIVITY_FAILURE = a.api.alarms.alarm.interface.INTERFACE_ALARM_NAME_IPV6_CONNECTIVITY_FAILURE

    def __init__ (self, logger):
        AlarmSourceBase.__init__(self, logger, InterfaceSource.ALARM_SOURCE_INSTACE_NAME)
        self.interfaceStaticList = InterfaceStaticMaapiList(logger, self)

    def initSupportedAlarmNames (self):
        self._addSupportedAlarmName(InterfaceSource.SUPPORTED_ALARM_NAME_INTERFACE_FAILURE)
        self._addSupportedAlarmName(InterfaceSource.SUPPORTED_ALARM_NAME_IPV4_CONNECTIVITY_FAILURE)
        self._addSupportedAlarmName(InterfaceSource.SUPPORTED_ALARM_NAME_IPV6_CONNECTIVITY_FAILURE)
    

    def _pollUnsimulatedActiveAlarms (self):
        tuplesKeyInterfaces = self.interfaceStaticList.get()
        if tuplesKeyInterfaces is None:
            self._log("get-real-active-alarms").warning("list of tuples-key-interfaces is None, should have been a list")
            raise AlarmSourceError("could not get interfaces information")

        alarms = []
        for (interfaceName, interfaceObject) in tuplesKeyInterfaces:
            self._log("get-real-active-alarms").debug3("interface %s, interfaceObject=%s", interfaceName, interfaceObject)            

            alarmsObj = interfaceObject.getAlarmsObj()
            if alarmsObj.hasInterfaceFailureAlarm() and alarmsObj.interfaceFailureAlarm:
                newAlarm = self._newAlarmInfo(InterfaceSource.SUPPORTED_ALARM_NAME_INTERFACE_FAILURE, self._interfaceNameToEntity(interfaceName))
                self._log("get-real-active-alarms").debug4("interface %s, raised alarm=%s", interfaceName, newAlarm)
                alarms.append(newAlarm)
                
            if alarmsObj.hasInterfaceIpv4ConnectivityFailureAlarm() and alarmsObj.interfaceIpv4ConnectivityFailureAlarm:
                newAlarm = self._newAlarmInfo(InterfaceSource.SUPPORTED_ALARM_NAME_IPV4_CONNECTIVITY_FAILURE, self._interfaceNameToEntity(interfaceName))
                self._log("get-real-active-alarms").debug4("interface %s, raised alarm=%s", interfaceName, newAlarm)
                alarms.append(newAlarm)

            if alarmsObj.hasInterfaceIpv6ConnectivityFailureAlarm() and alarmsObj.interfaceIpv6ConnectivityFailureAlarm:
                newAlarm = self._newAlarmInfo(InterfaceSource.SUPPORTED_ALARM_NAME_IPV6_CONNECTIVITY_FAILURE, self._interfaceNameToEntity(interfaceName))
                self._log("get-real-active-alarms").debug4("interface %s, raised alarm=%s", interfaceName, newAlarm)
                alarms.append(newAlarm)


        self._log("get-real-active-alarms").debug3("alarms=%s", alarms)
        return alarms

    def _interfaceNameToEntity (self, name):
        return "interface %s" % name


class InterfaceStaticMaapiList(StaticMaapiList):
    def __init__ (self, logger, alarmSource):
        StaticMaapiList.__init__(self, logger, alarmSource)
        
    def _getMaapiList (self, logger):
        """ Creates and returns a MaapiList object (Blinky generated) specific for the extension class.
        Used by the Static list handler methods of the base.
        In failure cases - returns None.
        Failure does not cause immediate harm (further static maapi operation will simply not occur).

        Extensions of this class should implement this function (if static maapi list functionality desired)

        Returns: MaapiList
        Raises: None
        """
        return BlinkyInterfaceMaapiList(logger)

    def _getNewObject (self, list):
        """ Calls the extension-specific MaapiList NewObject method. """
        return list.newInterface()

    def _requestObject (self, interfaceObject):
        """ Calls the extensions-specific request maapi fields """
        alarmsObj = interfaceObject.newAlarms()
        alarmsObj.requestInterfaceFailureAlarm(True)
        alarmsObj.requestInterfaceIpv4ConnectivityFailureAlarm(True)
        alarmsObj.requestInterfaceIpv6ConnectivityFailureAlarm(True)
        interfaceObject.setAlarmsObj(alarmsObj)

    def _setObject (self, list, key, object):
        """ Calls the extension-specific MaapiList setObject method. """
        return list.setInterfaceObj(key, object)


