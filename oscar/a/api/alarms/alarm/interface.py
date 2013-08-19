

#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: shmulika
# 

from a.api.yang.modules.tech.common.qwilt_tech_types.qwilt_tech_types_module_gen import SeverityType
from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.qwilt_tech_system_alarms_module_gen import AlarmNameType
from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.qwilt_tech_system_alarms_module_gen import AlarmDeclarationStateType
import a.api.alarms.alarm.alarm_base

INTERFACE_ENTITY_PATTERN = "<interface>"
INTERFACE_ALARM_SOURCE_NAME = "interface-source"
INTERFACE_ALARM_NAME_FAILURE = AlarmNameType.kInterfaceFailure
INTERFACE_ALARM_NAME_IPV4_CONNECTIVITY_FAILURE = AlarmNameType.kInterfaceIpv4ConnectivityFailure
INTERFACE_ALARM_NAME_IPV6_CONNECTIVITY_FAILURE = AlarmNameType.kInterfaceIpv6ConnectivityFailure

# TODO(shmulika): fix description, severity and such of alarms
a.api.alarms.alarm.alarm_base.registerAlarm(INTERFACE_ALARM_NAME_FAILURE,                   SeverityType.kError,    AlarmDeclarationStateType.kActive, INTERFACE_ALARM_SOURCE_NAME, "2.7.0", "",\
                                            "Network interface %s failure"%a.api.alarms.alarm.alarm_base.ENTITY_FORMAT_STRING, INTERFACE_ENTITY_PATTERN)

a.api.alarms.alarm.alarm_base.registerAlarm(INTERFACE_ALARM_NAME_IPV4_CONNECTIVITY_FAILURE, SeverityType.kError,    AlarmDeclarationStateType.kActive, INTERFACE_ALARM_SOURCE_NAME, "2.7.0", "",\
                                            "Network interface %s IPv4 connectivity check failure"%a.api.alarms.alarm.alarm_base.ENTITY_FORMAT_STRING, INTERFACE_ENTITY_PATTERN)

a.api.alarms.alarm.alarm_base.registerAlarm(INTERFACE_ALARM_NAME_IPV6_CONNECTIVITY_FAILURE, SeverityType.kError,    AlarmDeclarationStateType.kActive, INTERFACE_ALARM_SOURCE_NAME, "2.7.0", "",\
                                            "Network interface %s IPv6 connectivity check failure"%a.api.alarms.alarm.alarm_base.ENTITY_FORMAT_STRING, INTERFACE_ENTITY_PATTERN)
