
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

DISK_ENTITY_PATTERN = "Disk<X>/<Y>"
DISK_ALARM_SOURCE_NAME = "disk-source"
DISK_ALARM_NAME_CONTENT_DISK_FAILURE = AlarmNameType.kContentDiskFailure

# TODO(shmulika): fix description, severity and such of alarms
a.api.alarms.alarm.alarm_base.registerAlarm(DISK_ALARM_NAME_CONTENT_DISK_FAILURE, SeverityType.kError, AlarmDeclarationStateType.kActive, DISK_ALARM_SOURCE_NAME, "2.7.0", "",\
                                            "Content disk %s failure"%a.api.alarms.alarm.alarm_base.ENTITY_FORMAT_STRING, DISK_ENTITY_PATTERN)

