


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



from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.qwilt_tech_system_alarms_module_gen import AlarmDeclarationStateType
from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.qwilt_tech_system_alarms_module_gen import AlarmNameType
from a.api.yang.modules.tech.common.qwilt_tech_types.qwilt_tech_types_module_gen import SeverityType


class RegisteredOperData (object):

    def __init__ (self):

        self.description = ""
        self._myHasDescription=False
        self._myDescriptionRequested=False
        
        self.devComment = ""
        self._myHasDevComment=False
        self._myDevCommentRequested=False
        
        self.softwareVersion = ""
        self._myHasSoftwareVersion=False
        self._mySoftwareVersionRequested=False
        
        self.name = AlarmNameType.kTemperatureSensorWarning
        self._myHasName=False
        self._myNameRequested=False
        
        self.source = ""
        self._myHasSource=False
        self._mySourceRequested=False
        
        self.state = AlarmDeclarationStateType.kActive
        self._myHasState=False
        self._myStateRequested=False
        
        self.severity = SeverityType.kNone
        self._myHasSeverity=False
        self._mySeverityRequested=False
        


    def copyFrom (self, other):

        self.description=other.description
        self._myHasDescription=other._myHasDescription
        self._myDescriptionRequested=other._myDescriptionRequested
        
        self.devComment=other.devComment
        self._myHasDevComment=other._myHasDevComment
        self._myDevCommentRequested=other._myDevCommentRequested
        
        self.softwareVersion=other.softwareVersion
        self._myHasSoftwareVersion=other._myHasSoftwareVersion
        self._mySoftwareVersionRequested=other._mySoftwareVersionRequested
        
        self.name=other.name
        self._myHasName=other._myHasName
        self._myNameRequested=other._myNameRequested
        
        self.source=other.source
        self._myHasSource=other._myHasSource
        self._mySourceRequested=other._mySourceRequested
        
        self.state=other.state
        self._myHasState=other._myHasState
        self._myStateRequested=other._myStateRequested
        
        self.severity=other.severity
        self._myHasSeverity=other._myHasSeverity
        self._mySeverityRequested=other._mySeverityRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isDescriptionRequested():
            self.description=other.description
            self._myHasDescription=other._myHasDescription
            self._myDescriptionRequested=other._myDescriptionRequested
        
        if self.isDevCommentRequested():
            self.devComment=other.devComment
            self._myHasDevComment=other._myHasDevComment
            self._myDevCommentRequested=other._myDevCommentRequested
        
        if self.isSoftwareVersionRequested():
            self.softwareVersion=other.softwareVersion
            self._myHasSoftwareVersion=other._myHasSoftwareVersion
            self._mySoftwareVersionRequested=other._mySoftwareVersionRequested
        
        if self.isNameRequested():
            self.name=other.name
            self._myHasName=other._myHasName
            self._myNameRequested=other._myNameRequested
        
        if self.isSourceRequested():
            self.source=other.source
            self._myHasSource=other._myHasSource
            self._mySourceRequested=other._mySourceRequested
        
        if self.isStateRequested():
            self.state=other.state
            self._myHasState=other._myHasState
            self._myStateRequested=other._myStateRequested
        
        if self.isSeverityRequested():
            self.severity=other.severity
            self._myHasSeverity=other._myHasSeverity
            self._mySeverityRequested=other._mySeverityRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasDescription():
            self.description=other.description
            self._myHasDescription=other._myHasDescription
            self._myDescriptionRequested=other._myDescriptionRequested
        
        if other.hasDevComment():
            self.devComment=other.devComment
            self._myHasDevComment=other._myHasDevComment
            self._myDevCommentRequested=other._myDevCommentRequested
        
        if other.hasSoftwareVersion():
            self.softwareVersion=other.softwareVersion
            self._myHasSoftwareVersion=other._myHasSoftwareVersion
            self._mySoftwareVersionRequested=other._mySoftwareVersionRequested
        
        if other.hasName():
            self.name=other.name
            self._myHasName=other._myHasName
            self._myNameRequested=other._myNameRequested
        
        if other.hasSource():
            self.source=other.source
            self._myHasSource=other._myHasSource
            self._mySourceRequested=other._mySourceRequested
        
        if other.hasState():
            self.state=other.state
            self._myHasState=other._myHasState
            self._myStateRequested=other._myStateRequested
        
        if other.hasSeverity():
            self.severity=other.severity
            self._myHasSeverity=other._myHasSeverity
            self._mySeverityRequested=other._mySeverityRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.description=other.description
        self._myHasDescription=other._myHasDescription
        
        self.devComment=other.devComment
        self._myHasDevComment=other._myHasDevComment
        
        self.softwareVersion=other.softwareVersion
        self._myHasSoftwareVersion=other._myHasSoftwareVersion
        
        self.name=other.name
        self._myHasName=other._myHasName
        
        self.source=other.source
        self._myHasSource=other._myHasSource
        
        self.state=other.state
        self._myHasState=other._myHasState
        
        self.severity=other.severity
        self._myHasSeverity=other._myHasSeverity
        


    def setAllNumericToZero (self):
        
        
        pass

    def subtractAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        
        pass


    def addAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        
        pass


    # has...() methods

    def hasDescription (self):
        return self._myHasDescription

    def hasDevComment (self):
        return self._myHasDevComment

    def hasSoftwareVersion (self):
        return self._myHasSoftwareVersion

    def hasName (self):
        return self._myHasName

    def hasSource (self):
        return self._myHasSource

    def hasState (self):
        return self._myHasState

    def hasSeverity (self):
        return self._myHasSeverity




    # setHas...() methods

    def setHasDescription (self):
        self._myHasDescription=True

    def setHasDevComment (self):
        self._myHasDevComment=True

    def setHasSoftwareVersion (self):
        self._myHasSoftwareVersion=True

    def setHasName (self):
        self._myHasName=True

    def setHasSource (self):
        self._myHasSource=True

    def setHasState (self):
        self._myHasState=True

    def setHasSeverity (self):
        self._myHasSeverity=True




    # isRequested...() methods

    def isDescriptionRequested (self):
        return self._myDescriptionRequested

    def isDevCommentRequested (self):
        return self._myDevCommentRequested

    def isSoftwareVersionRequested (self):
        return self._mySoftwareVersionRequested

    def isNameRequested (self):
        return self._myNameRequested

    def isSourceRequested (self):
        return self._mySourceRequested

    def isStateRequested (self):
        return self._myStateRequested

    def isSeverityRequested (self):
        return self._mySeverityRequested




    # setRequested...() methods

    def setDescriptionRequested (self):
        self._myDescriptionRequested=True

    def setDevCommentRequested (self):
        self._myDevCommentRequested=True

    def setSoftwareVersionRequested (self):
        self._mySoftwareVersionRequested=True

    def setNameRequested (self):
        self._myNameRequested=True

    def setSourceRequested (self):
        self._mySourceRequested=True

    def setStateRequested (self):
        self._myStateRequested=True

    def setSeverityRequested (self):
        self._mySeverityRequested=True




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
        if self._myDevCommentRequested:
            x = "+DevComment="
            if self._myHasDevComment:
                leafStr = str(self.devComment)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._mySoftwareVersionRequested:
            x = "+SoftwareVersion="
            if self._myHasSoftwareVersion:
                leafStr = str(self.softwareVersion)
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

        x=""
        if self._mySourceRequested:
            x = "+Source="
            if self._myHasSource:
                leafStr = str(self.source)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myStateRequested:
            x = "+State="
            if self._myHasState:
                leafStr = str(self.state)
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


        return "{RegisteredOperData: "+",".join(items)+"}"

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
        x = "+DevComment="
        if self._myHasDevComment:
            leafStr = str(self.devComment)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myDevCommentRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+SoftwareVersion="
        if self._myHasSoftwareVersion:
            leafStr = str(self.softwareVersion)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._mySoftwareVersionRequested:
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
        x = "+State="
        if self._myHasState:
            leafStr = str(self.state)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myStateRequested:
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


        return "{RegisteredOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setDescriptionRequested()
        self.setDevCommentRequested()
        self.setSoftwareVersionRequested()
        self.setNameRequested()
        self.setSourceRequested()
        self.setStateRequested()
        self.setSeverityRequested()
        
        


    def setDescription (self, description):
        self.description = description
        self.setHasDescription()

    def setDevComment (self, devComment):
        self.devComment = devComment
        self.setHasDevComment()

    def setSoftwareVersion (self, softwareVersion):
        self.softwareVersion = softwareVersion
        self.setHasSoftwareVersion()

    def setName (self, name):
        self.name = name
        self.setHasName()

    def setSource (self, source):
        self.source = source
        self.setHasSource()

    def setState (self, state):
        self.state = state
        self.setHasState()

    def setSeverity (self, severity):
        self.severity = severity
        self.setHasSeverity()


"""
Extracted from the below data: 
{
    "node": {
        "className": "RegisteredOperData", 
        "namespace": "registered", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.registered.registered_oper_data_gen import RegisteredOperData"
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
            "namespace": "registered", 
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
            "typeHandler": "handler: StringHandler", 
            "memberName": "devComment", 
            "yangName": "dev-comment", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "softwareVersion", 
            "yangName": "software-version", 
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
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "state", 
            "yangName": "state", 
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


