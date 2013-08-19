
#
# Copyright Qwilt, 2013
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: shmulika
# 

import a.api.alarms.alarm.content_reporting_export

import a.sys.blinky.maapi_domain # this is a patch because of bug in MAAPI import, when naamas fixes - remove it
from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.qwilt_tech_system_alarms_module_gen import AlarmNameType
from a.api.yang.modules.tech.content.qwilt_tech_content_reporting.tech.content.reporting.export_.export__maapi_list_gen import BlinkyExportMaapiList
from a.api.yang.modules.tech.content.qwilt_tech_content_reporting.tech.content.reporting.export_.export__maapi_gen import BlinkyExportMaapi

from a.sys.mng.alarm.sources.source_base import AlarmSourceBase
from a.sys.mng.alarm.sources.source_base import AlarmSourceError
from a.sys.mng.alarm.sources.source_base import DynamicMaapiList

class ContentReportingExportSource(AlarmSourceBase):

    ALARM_SOURCE_INSTACE_NAME = a.api.alarms.alarm.content_reporting_export.CONTENT_REPORTING_EXPORT_ALARM_SOURCE_NAME
    
    def __init__ (self, logger):
        AlarmSourceBase.__init__(self, logger, ContentReportingExportSource.ALARM_SOURCE_INSTACE_NAME)
        self.exportStaticList = ExportStaticMaapiList(logger, self)

    def initSupportedAlarmNames (self):
        self._addSupportedAlarmName(a.api.alarms.alarm.content_reporting_export.EXPORT_ALARM_NAME_REPORT_QUEUE_GETTING_FULL)
        self._addSupportedAlarmName(a.api.alarms.alarm.content_reporting_export.EXPORT_ALARM_NAME_REPORT_QUEUE_IS_FULL)
    

    def _pollUnsimulatedActiveAlarms (self):
        tuplesKeyExports = self.exportStaticList.get()
        if tuplesKeyExports is None:
            self._log("get-real-active-alarms").warning("list of tuples-key-exports is None, should have been a list")
            raise AlarmSourceError("could not get exports information")

        alarms = []        
        for (exportName, exportObject) in tuplesKeyExports:
            alarmsObj = exportObject.getAlarmObj()
            self._log("get-real-active-alarms").debug3("export %s, hasAlarm = %s, alarm-getting-full=%s", exportName, alarmsObj.hasReportsQueueGettingFull(), alarmsObj.reportsQueueGettingFull)
            if alarmsObj.hasReportsQueueGettingFull() and alarmsObj.reportsQueueGettingFull:
                alarms.append(self._newAlarmInfo(a.api.alarms.alarm.content_reporting_export.EXPORT_ALARM_NAME_REPORT_QUEUE_GETTING_FULL, self._exportNameToEntity(exportName)))

            self._log("get-real-active-alarms").debug3("export %s, hasAlarm = %s, alarm-is-full=%s", exportName, alarmsObj.hasReportsQueueFull(), alarmsObj.reportsQueueFull)
            if alarmsObj.hasReportsQueueFull() and alarmsObj.reportsQueueFull:
                alarms.append(self._newAlarmInfo(a.api.alarms.alarm.content_reporting_export.EXPORT_ALARM_NAME_REPORT_QUEUE_IS_FULL, self._exportNameToEntity(exportName)))

        self._log("get-real-active-alarms").debug3("alarms=%s", alarms)
        return alarms


    def _exportNameToEntity (self, name):
        return name


class ExportStaticMaapiList(DynamicMaapiList):
    def __init__ (self, logger, alarmSource):
        DynamicMaapiList.__init__(self, logger, alarmSource)
        
    def _getMaapiList (self, logger):
        """ Creates and returns a MaapiList object (Blinky generated) specific for the extension class.
        Used by the Static list handler methods of the base.
        In failure cases - returns None.
        Failure does not cause immediate harm (further static maapi operation will simply not occur).

        Extensions of this class should implement this function (if static maapi list functionality desired)

        Returns: MaapiList
        Raises: None
        """
        return BlinkyExportMaapiList(logger)

    def _getNewObject (self, list):
        """ Calls the extension-specific MaapiList NewObject method. """
        return list.newExport_()

    def _requestObject (self, exportObject):
        """ Calls the extensions-specific request maapi fields """
        alarmsObj = exportObject.newAlarm()
        alarmsObj.requestReportsQueueFull(True)
        alarmsObj.requestReportsQueueGettingFull(True)
        exportObject.setAlarmObj(alarmsObj)

    def _setObject (self, list, key, object):
        """ Calls the extension-specific MaapiList setObject method. """
        return list.setExport_Obj(key, object)


