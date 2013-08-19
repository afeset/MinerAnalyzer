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

SYSTEM_ALARM_SOURCE_NAME = "system-alarms-source"
SYSTEM_ALARM_NAME_TEST_ALARM_RAISED = AlarmNameType.kSystemAlarmTestAlarmRaised
SYSTEM_ALARM_ENTITY_PATTERN = "system-alarms"

a.api.alarms.alarm.alarm_base.registerAlarm(SYSTEM_ALARM_NAME_TEST_ALARM_RAISED, SeverityType.kDebug, AlarmDeclarationStateType.kActive, SYSTEM_ALARM_SOURCE_NAME, "2.7.0", "This alarm is used by dev to test reading alarm status via MAAPI",\
                                            "Test alarm from %s"%a.api.alarms.alarm.alarm_base.ENTITY_FORMAT_STRING, SYSTEM_ALARM_ENTITY_PATTERN)

