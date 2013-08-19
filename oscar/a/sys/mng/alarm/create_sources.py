#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: shmulika
# 

#### README ######################################################
# All supported AlarmSources should be added to this function.
# Folow the example of ExampleAlarmSource
##################################################################

import a.sys.mng.alarm.sources.content_reporting_export
import a.sys.mng.alarm.sources.disk
import a.sys.mng.alarm.sources.example
import a.sys.mng.alarm.sources.interface
import a.sys.mng.alarm.sources.platform
import a.sys.mng.alarm.sources.system_alarms

def createSources (alarmManager, logger):
    alarmManager.addAlarmSource(a.sys.mng.alarm.sources.content_reporting_export.ContentReportingExportSource(logger))
    alarmManager.addAlarmSource(a.sys.mng.alarm.sources.disk.DiskSource(logger))
    alarmManager.addAlarmSource(a.sys.mng.alarm.sources.example.ExampleAlarmSource(logger))
    alarmManager.addAlarmSource(a.sys.mng.alarm.sources.interface.InterfaceSource(logger))
    alarmManager.addAlarmSource(a.sys.mng.alarm.sources.platform.PlatformSource(logger))
    alarmManager.addAlarmSource(a.sys.mng.alarm.sources.system_alarms.SystemAlarmsSource(logger))


