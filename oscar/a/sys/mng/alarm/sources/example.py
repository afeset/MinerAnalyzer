#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: shmulika
# 


###### README #################################################################
# This is an example on how to write an AlarmSource
# Notice you also need to add your AlarmSource to .../alarm/create_sources.py
# The example has special instructions with TODO(programmer) so you can ctrl+f
#
###############################################################################

#TODO(programmer): import the api file where your alarms were declared
import a.api.alarms.alarm.example

from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.qwilt_tech_system_alarms_module_gen import AlarmNameType
from a.sys.mng.alarm.sources.source_base import AlarmSourceBase
from a.sys.mng.alarm.sources.source_base import AlarmSourceError


#TODO(programmer): name the class appropriately
class ExampleAlarmSource(AlarmSourceBase):
    #TODO(programmer): take the name of the source from your api file
    ALARM_SOURCE_INSTACE_NAME = a.api.alarms.alarm.example.EXAMPLE_ALARM_SOURCE_NAME


    def __init__ (self, logger):
        AlarmSourceBase.__init__(self, logger, ExampleAlarmSource.ALARM_SOURCE_INSTACE_NAME)


    #TODO(programmer): add all the declared alarms in this method
    def initSupportedAlarmNames (self):
        #self._addSupportedAlarmName(AlarmNameType.kAaaDown)
        #self._addSupportedAlarmName(AlarmNameType.kXxxDown)
        pass

    
    #TODO(programmer): this function should gather information via MAAPI, and return only alarms that should be reported as active
    def _pollUnsimulatedActiveAlarms (self):
        return []












