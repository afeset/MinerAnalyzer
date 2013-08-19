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
from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.registered.registered_oper_data_gen import RegisteredOperData

ENTITY_KEY_STRING = "entity"
ENTITY_FORMAT_STRING = "%(" + ENTITY_KEY_STRING + ")s"

class RegisteredAlarms(object):
    registeredAlarms = []
    registeredHash = {}
    registeredAlarmDescriptionPatterns = {}

#    def __init__ (self, name, severity, description, state, softwareVersion, devComment):
#        self.name            = name            
#        self.severity        = severity        
#        self.description     = description     
#        self.state           = state           
#        self.softwareVersion = softwareVersion 
#        self.devComment      = devComment      

    def __init__ (self):
        pass

    @classmethod
    def s_getRegisteredAlarmsList (cls):
        return cls.registeredAlarms


    @classmethod
    def s_getRegisteredAlarmDescriptionPattern (cls, name):
        return cls.registeredAlarmDescriptionPatterns[name]


    @classmethod
    def s_addRegisteredAlarmToList (cls, name, severity, state, source, softwareVersion, devComment, descriptionPattern, entityPattern):
        if name in cls.registeredHash:
            # alarm already registered - add source to the registration
            registeredAlarm = cls.registeredHash[name]
            registeredAlarm.setSource(", ".join([registeredAlarm.source, source]))
            return

        # new registered alarm

        # format the description field (notice: in case of bug this will throw expcetion, which I'm good with because this is API and should be perfect)
        formattedDescription  = descriptionPattern % ({ENTITY_KEY_STRING : entityPattern})

        registeredAlarm = RegisteredOperData()
        registeredAlarm.setDescription(formattedDescription)
        registeredAlarm.setSeverity(severity)
        registeredAlarm.setDevComment(devComment)
        registeredAlarm.setSoftwareVersion(softwareVersion)
        registeredAlarm.setState(state)
        registeredAlarm.setName(name)
        registeredAlarm.setSource(source)
        
        registeredAlarm.setDescriptionRequested()
        registeredAlarm.setSeverityRequested()
        registeredAlarm.setDevCommentRequested()
        registeredAlarm.setSoftwareVersionRequested()
        registeredAlarm.setStateRequested()
        registeredAlarm.setNameRequested()
        registeredAlarm.setSourceRequested()

        cls.registeredHash[registeredAlarm.name] = registeredAlarm
        # TODO(shmulika): keeping the description pattern in separate hash is ugly, consider creating a wrapper to the registeredAlarm object containing both RegisteredData and descriptionPattern 
        cls.registeredAlarmDescriptionPatterns[registeredAlarm.name] = descriptionPattern
        cls.registeredAlarms.append(registeredAlarm)
        return


def registerAlarm (name, severity, state, source, softwareVersion, devComment, descriptionPattern, entityPattern):
    RegisteredAlarms.s_addRegisteredAlarmToList(name, severity, state, source, softwareVersion, devComment, descriptionPattern, entityPattern)


