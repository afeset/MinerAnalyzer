#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: shmulika
# 

# TODO(programmer): copy these imports (uncomment alarm_base)
from a.api.yang.modules.tech.common.qwilt_tech_types.qwilt_tech_types_module_gen import SeverityType
from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.qwilt_tech_system_alarms_module_gen import AlarmNameType
from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.qwilt_tech_system_alarms_module_gen import AlarmDeclarationStateType
#import a.api.alarms.alarm.alarm_base

# TODO(programmer): give the alarm source a name
EXAMPLE_ALARM_SOURCE_NAME = "example-source"
EXAMPLE_ENTITY_PATTERN = "example<X>/<Y>"

# TODO(programmer): this is how you declare an alarm
# method prototype: registerAlarm (name, severity, description, state, softwareVersion, devComment)
# Notice: name, state, severity are enums defined in the yang
# The entity name will be placed where you put the special entity string a.api.alarms.alarm.alarm_base.ENTITY_KEY_STRING
#a.api.alarms.alarm.alarm_base.registerAlarm(AlarmNameType.kAaaDown, SeverityType.kError,    AlarmDeclarationStateType.kRegistered, EXAMPLE_ALARM_SOURCE_NAME, "2.7.0", "This alarm should not actually be used",\
#                                            "An example alarm from %s"%a.api.alarms.alarm.alarm_base.ENTITY_FORMAT_STRING,   EXAMPLE_ENTITY_PATTERN)
#a.api.alarms.alarm.alarm_base.registerAlarm(AlarmNameType.kXxxDown, SeverityType.kCritical, AlarmDeclarationStateType.kRegistered, EXAMPLE_ALARM_SOURCE_NAME, "2.7.0", "This alarm should not actually be used",\
#                                            "Another example alarm from %s"%a.api.alarms.alarm.alarm_base.ENTITY_FORMAT_STRING, EXAMPLE_ENTITY_PATTERN)

# Notice this is a repition of the first registered alarm. Two sources can register on the same alarm, and both will show in the CLI as registered sources.
# But there is no reason to repeat the same alarm for the same source (this is just a demonstration, and a test of this "multiple-registration" feature)
#a.api.alarms.alarm.alarm_base.registerAlarm(AlarmNameType.kAaaDown, SeverityType.kError,    AlarmDeclarationStateType.kRegistered, EXAMPLE_ALARM_SOURCE_NAME, "2.7.0", "This alarm should not actually be used",\
#                                            "An example alarm from %s"%a.api.alarms.alarm.alarm_base.ENTITY_FORMAT_STRING,   EXAMPLE_ENTITY_PATTERN)

# TODO(programmer): if you added an entirely new py file to this directory, you MUST add it to the imports in all_declared.py
