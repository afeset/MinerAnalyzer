#
# Copyright Qwilt, 2013
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: shmulika
# 

from a.api.yang.modules.tech.common.qwilt_tech_types.qwilt_tech_types_module_gen import SeverityType
from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.qwilt_tech_system_alarms_module_gen import AlarmNameType
from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.qwilt_tech_system_alarms_module_gen import AlarmDeclarationStateType
import a.api.alarms.alarm.alarm_base

EXPORT_ENTITY_PATTERN = "[export-name]"
CONTENT_REPORTING_EXPORT_ALARM_SOURCE_NAME = "content-reporting-export-source"

EXPORT_ALARM_NAME_REPORT_QUEUE_GETTING_FULL = AlarmNameType.kReportsQueueGettingFull
EXPORT_ALARM_NAME_REPORT_QUEUE_IS_FULL      = AlarmNameType.kReportsQueueFull

a.api.alarms.alarm.alarm_base.registerAlarm(EXPORT_ALARM_NAME_REPORT_QUEUE_GETTING_FULL, SeverityType.kWarning, AlarmDeclarationStateType.kActive, CONTENT_REPORTING_EXPORT_ALARM_SOURCE_NAME, "3.0.0", "",\
                                            "%s report queue is getting full"%a.api.alarms.alarm.alarm_base.ENTITY_FORMAT_STRING, EXPORT_ENTITY_PATTERN)

a.api.alarms.alarm.alarm_base.registerAlarm(EXPORT_ALARM_NAME_REPORT_QUEUE_IS_FULL, SeverityType.kError, AlarmDeclarationStateType.kActive, CONTENT_REPORTING_EXPORT_ALARM_SOURCE_NAME, "3.0.0", "",\
                                            "%s report queue is full"%a.api.alarms.alarm.alarm_base.ENTITY_FORMAT_STRING, EXPORT_ENTITY_PATTERN)

