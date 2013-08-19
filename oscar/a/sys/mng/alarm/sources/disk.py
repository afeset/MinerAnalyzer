#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: shmulika
# 

import a.api.alarms.alarm.disk

import a.sys.blinky.maapi_domain # this is a patch because of bug in MAAPI import, when naamas fixes - remove it
from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.qwilt_tech_system_alarms_module_gen import AlarmNameType
from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.disk_maapi_list_gen import BlinkyDiskMaapiList
from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.disk_maapi_gen import BlinkyDiskMaapi

from a.sys.mng.alarm.sources.source_base import AlarmSourceBase
from a.sys.mng.alarm.sources.source_base import AlarmSourceError
from a.sys.mng.alarm.sources.source_base import StaticMaapiList

class DiskSource(AlarmSourceBase):

    ALARM_SOURCE_INSTACE_NAME = a.api.alarms.alarm.disk.DISK_ALARM_SOURCE_NAME
    
    # TODO(shmulika): change this to proper alarms    
    SUPPORTED_ALARM_NAME = a.api.alarms.alarm.disk.DISK_ALARM_NAME_CONTENT_DISK_FAILURE

    def __init__ (self, logger):
        AlarmSourceBase.__init__(self, logger, DiskSource.ALARM_SOURCE_INSTACE_NAME)
        self.diskStaticList = DiskStaticMaapiList(logger, self)

    def initSupportedAlarmNames (self):
        self._addSupportedAlarmName(DiskSource.SUPPORTED_ALARM_NAME)
    

    def _pollUnsimulatedActiveAlarms (self):
        tuplesKeyDisks = self.diskStaticList.get()
        if tuplesKeyDisks is None:
            self._log("get-real-active-alarms").warning("list of tuples-key-disks is None, should have been a list")
            raise AlarmSourceError("could not get disks information")

        alarms = []        
        for (diskName, diskObject) in tuplesKeyDisks:
            alarmsObj = diskObject.getAlarmsObj()
            self._log("get-real-active-alarms").debug3("disk %s, hasAlarm = %s, alarm=%s", diskName, alarmsObj.hasContentDiskFailureAlarm(), alarmsObj.contentDiskFailureAlarm)
            if alarmsObj.hasContentDiskFailureAlarm() and alarmsObj.contentDiskFailureAlarm:
                alarms.append(self._newAlarmInfo(DiskSource.SUPPORTED_ALARM_NAME, self._diskNameToEntity(diskName)))

        self._log("get-real-active-alarms").debug3("alarms=%s", alarms)
        return alarms


    def _diskNameToEntity (self, name):
        return "storage %s" % name


class DiskStaticMaapiList(StaticMaapiList):
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
        return BlinkyDiskMaapiList(logger)

    def _getNewObject (self, list):
        """ Calls the extension-specific MaapiList NewObject method. """
        return list.newDisk()

    def _requestObject (self, diskObject):
        """ Calls the extensions-specific request maapi fields """
        alarmsObj = diskObject.newAlarms()
        alarmsObj.requestContentDiskFailureAlarm(True)
        diskObject.setAlarmsObj(alarmsObj)

    def _setObject (self, list, key, object):
        """ Calls the extension-specific MaapiList setObject method. """
        return list.setDiskObj(key, object)


