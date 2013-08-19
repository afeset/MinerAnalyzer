


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

# Must be set here to avoid stupid warnings about stuff in BlinkyOperData
__pychecker__="no-classattr"

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.qwilt_tech_system_alarms_module_gen import AlarmNameType
from a.api.yang.modules.tech.common.qwilt_tech_types.qwilt_tech_types_module_gen import SeverityType


class ListOperData (object):

    def __init__ (self):

        self.description = ""
        self._myHasDescription=False
        self._myDescriptionRequested=False
        
        self.severity = SeverityType.kNone
        self._myHasSeverity=False
        self._mySeverityRequested=False
        
        self.number = 0
        self._myHasNumber=False
        self._myNumberRequested=False
        
        self.entity = ""
        self._myHasEntity=False
        self._myEntityRequested=False
        
        self.source = ""
        self._myHasSource=False
        self._mySourceRequested=False
        
        self.simulated = False
        self._myHasSimulated=False
        self._mySimulatedRequested=False
        
        self.name = AlarmNameType.kTemperatureSensorWarning
        self._myHasName=False
        self._myNameRequested=False
        


    def copyFrom (self, other):

        self.description=other.description
        self._myHasDescription=other._myHasDescription
        self._myDescriptionRequested=other._myDescriptionRequested
        
        self.severity=other.severity
        self._myHasSeverity=other._myHasSeverity
        self._mySeverityRequested=other._mySeverityRequested
        
        self.number=other.number
        self._myHasNumber=other._myHasNumber
        self._myNumberRequested=other._myNumberRequested
        
        self.entity=other.entity
        self._myHasEntity=other._myHasEntity
        self._myEntityRequested=other._myEntityRequested
        
        self.source=other.source
        self._myHasSource=other._myHasSource
        self._mySourceRequested=other._mySourceRequested
        
        self.simulated=other.simulated
        self._myHasSimulated=other._myHasSimulated
        self._mySimulatedRequested=other._mySimulatedRequested
        
        self.name=other.name
        self._myHasName=other._myHasName
        self._myNameRequested=other._myNameRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isDescriptionRequested():
            self.description=other.description
            self._myHasDescription=other._myHasDescription
            self._myDescriptionRequested=other._myDescriptionRequested
        
        if self.isSeverityRequested():
            self.severity=other.severity
            self._myHasSeverity=other._myHasSeverity
            self._mySeverityRequested=other._mySeverityRequested
        
        if self.isNumberRequested():
            self.number=other.number
            self._myHasNumber=other._myHasNumber
            self._myNumberRequested=other._myNumberRequested
        
        if self.isEntityRequested():
            self.entity=other.entity
            self._myHasEntity=other._myHasEntity
            self._myEntityRequested=other._myEntityRequested
        
        if self.isSourceRequested():
            self.source=other.source
            self._myHasSource=other._myHasSource
            self._mySourceRequested=other._mySourceRequested
        
        if self.isSimulatedRequested():
            self.simulated=other.simulated
            self._myHasSimulated=other._myHasSimulated
            self._mySimulatedRequested=other._mySimulatedRequested
        
        if self.isNameRequested():
            self.name=other.name
            self._myHasName=other._myHasName
            self._myNameRequested=other._myNameRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasDescription():
            self.description=other.description
            self._myHasDescription=other._myHasDescription
            self._myDescriptionRequested=other._myDescriptionRequested
        
        if other.hasSeverity():
            self.severity=other.severity
            self._myHasSeverity=other._myHasSeverity
            self._mySeverityRequested=other._mySeverityRequested
        
        if other.hasNumber():
            self.number=other.number
            self._myHasNumber=other._myHasNumber
            self._myNumberRequested=other._myNumberRequested
        
        if other.hasEntity():
            self.entity=other.entity
            self._myHasEntity=other._myHasEntity
            self._myEntityRequested=other._myEntityRequested
        
        if other.hasSource():
            self.source=other.source
            self._myHasSource=other._myHasSource
            self._mySourceRequested=other._mySourceRequested
        
        if other.hasSimulated():
            self.simulated=other.simulated
            self._myHasSimulated=other._myHasSimulated
            self._mySimulatedRequested=other._mySimulatedRequested
        
        if other.hasName():
            self.name=other.name
            self._myHasName=other._myHasName
            self._myNameRequested=other._myNameRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.description=other.description
        self._myHasDescription=other._myHasDescription
        
        self.severity=other.severity
        self._myHasSeverity=other._myHasSeverity
        
        self.number=other.number
        self._myHasNumber=other._myHasNumber
        
        self.entity=other.entity
        self._myHasEntity=other._myHasEntity
        
        self.source=other.source
        self._myHasSource=other._myHasSource
        
        self.simulated=other.simulated
        self._myHasSimulated=other._myHasSimulated
        
        self.name=other.name
        self._myHasName=other._myHasName
        


    def setAllNumericToZero (self):
        
        self.number=0
        self.setHasNumber()
        
        pass

    def subtractAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasNumber():
            if other.hasNumber():
                self.number -= other.number
        
        
        pass


    def addAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasNumber():
            if other.hasNumber():
                self.number += other.number
        
        
        pass


    # has...() methods

    def hasDescription (self):
        return self._myHasDescription

    def hasSeverity (self):
        return self._myHasSeverity

    def hasNumber (self):
        return self._myHasNumber

    def hasEntity (self):
        return self._myHasEntity

    def hasSource (self):
        return self._myHasSource

    def hasSimulated (self):
        return self._myHasSimulated

    def hasName (self):
        return self._myHasName




    # setHas...() methods

    def setHasDescription (self):
        self._myHasDescription=True

    def setHasSeverity (self):
        self._myHasSeverity=True

    def setHasNumber (self):
        self._myHasNumber=True

    def setHasEntity (self):
        self._myHasEntity=True

    def setHasSource (self):
        self._myHasSource=True

    def setHasSimulated (self):
        self._myHasSimulated=True

    def setHasName (self):
        self._myHasName=True




    # isRequested...() methods

    def isDescriptionRequested (self):
        return self._myDescriptionRequested

    def isSeverityRequested (self):
        return self._mySeverityRequested

    def isNumberRequested (self):
        return self._myNumberRequested

    def isEntityRequested (self):
        return self._myEntityRequested

    def isSourceRequested (self):
        return self._mySourceRequested

    def isSimulatedRequested (self):
        return self._mySimulatedRequested

    def isNameRequested (self):
        return self._myNameRequested




    # setRequested...() methods

    def setDescriptionRequested (self):
        self._myDescriptionRequested=True

    def setSeverityRequested (self):
        self._mySeverityRequested=True

    def setNumberRequested (self):
        self._myNumberRequested=True

    def setEntityRequested (self):
        self._myEntityRequested=True

    def setSourceRequested (self):
        self._mySourceRequested=True

    def setSimulatedRequested (self):
        self._mySimulatedRequested=True

    def setNameRequested (self):
        self._myNameRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myDescriptionRequested:
            x = "+Description="
            if self._myHasDescription:
                leafStr = str(self.description)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._mySeverityRequested:
            x = "+Severity="
            if self._myHasSeverity:
                leafStr = str(self.severity)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myNumberRequested:
            x = "+Number="
            if self._myHasNumber:
                leafStr = str(self.number)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myEntityRequested:
            x = "+Entity="
            if self._myHasEntity:
                leafStr = str(self.entity)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._mySourceRequested:
            x = "+Source="
            if self._myHasSource:
                leafStr = str(self.source)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._mySimulatedRequested:
            x = "+Simulated="
            if self._myHasSimulated:
                leafStr = str(self.simulated)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myNameRequested:
            x = "+Name="
            if self._myHasName:
                leafStr = str(self.name)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{ListOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+Description="
        if self._myHasDescription:
            leafStr = str(self.description)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myDescriptionRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+Severity="
        if self._myHasSeverity:
            leafStr = str(self.severity)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._mySeverityRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+Number="
        if self._myHasNumber:
            leafStr = str(self.number)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myNumberRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+Entity="
        if self._myHasEntity:
            leafStr = str(self.entity)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myEntityRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+Source="
        if self._myHasSource:
            leafStr = str(self.source)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._mySourceRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+Simulated="
        if self._myHasSimulated:
            leafStr = str(self.simulated)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._mySimulatedRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+Name="
        if self._myHasName:
            leafStr = str(self.name)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myNameRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{ListOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setDescriptionRequested()
        self.setSeverityRequested()
        self.setNumberRequested()
        self.setEntityRequested()
        self.setSourceRequested()
        self.setSimulatedRequested()
        self.setNameRequested()
        
        


    def setDescription (self, description):
        self.description = description
        self.setHasDescription()

    def setSeverity (self, severity):
        self.severity = severity
        self.setHasSeverity()

    def setNumber (self, number):
        self.number = number
        self.setHasNumber()

    def setEntity (self, entity):
        self.entity = entity
        self.setHasEntity()

    def setSource (self, source):
        self.source = source
        self.setHasSource()

    def setSimulated (self, simulated):
        self.simulated = simulated
        self.setHasSimulated()

    def setName (self, name):
        self.name = name
        self.setHasName()


"""
Extracted from the below data: 
{
    "node": {
        "className": "ListOperData", 
        "namespace": "list", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.list.list_oper_data_gen import ListOperData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "system", 
            "isCurrent": false
        }, 
        {
            "namespace": "alarms", 
            "isCurrent": false
        }, 
        {
            "namespace": "list", 
            "isCurrent": true
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "severity", 
            "yangName": "severity", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "number", 
            "yangName": "number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "entity", 
            "yangName": "entity", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "source", 
            "yangName": "source", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "simulated", 
            "yangName": "simulated", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "module": {}, 
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "common", 
            "qwilt_tech_system_alarms"
        ]
    }, 
    "createTime": "2013"
}
"""


