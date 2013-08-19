


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket

from a.api.yang.modules.tech.common.qwilt_tech_linux_variables.qwilt_tech_linux_variables_module_gen import InitPhase


class VariableData(object):

    def __init__ (self):

        self.name = ""
        self._myHasName=False
        
        self.description = ""
        self._myHasDescription=False
        
        self.systemProtected = False
        self._myHasSystemProtected=False
        
        self.value = ""
        self._myHasValue=False
        
        self.initPhase = InitPhase.kInitial
        self._myHasInitPhase=False
        

    def copyFrom (self, other):

        self.name=other.name
        self._myHasName=other._myHasName
        
        self.description=other.description
        self._myHasDescription=other._myHasDescription
        
        self.systemProtected=other.systemProtected
        self._myHasSystemProtected=other._myHasSystemProtected
        
        self.value=other.value
        self._myHasValue=other._myHasValue
        
        self.initPhase=other.initPhase
        self._myHasInitPhase=other._myHasInitPhase
        
    # has...() methods

    def hasName (self):
        return self._myHasName

    def hasDescription (self):
        return self._myHasDescription

    def hasSystemProtected (self):
        return self._myHasSystemProtected

    def hasValue (self):
        return self._myHasValue

    def hasInitPhase (self):
        return self._myHasInitPhase


    # setHas...() methods

    def setHasName (self):
        self._myHasName=True

    def setHasDescription (self):
        self._myHasDescription=True

    def setHasSystemProtected (self):
        self._myHasSystemProtected=True

    def setHasValue (self):
        self._myHasValue=True

    def setHasInitPhase (self):
        self._myHasInitPhase=True


    def clearAllHas (self):

        self._myHasName=False

        self._myHasDescription=False

        self._myHasSystemProtected=False

        self._myHasValue=False

        self._myHasInitPhase=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasName:
            x = "+"
        leafStr = str(self.name)
        items.append(x + "Name="+leafStr)

        x=""
        if self._myHasDescription:
            x = "+"
        leafStr = str(self.description)
        items.append(x + "Description="+leafStr)

        x=""
        if self._myHasSystemProtected:
            x = "+"
        leafStr = str(self.systemProtected)
        items.append(x + "SystemProtected="+leafStr)

        x=""
        if self._myHasValue:
            x = "+"
        leafStr = str(self.value)
        items.append(x + "Value="+leafStr)

        x=""
        if self._myHasInitPhase:
            x = "+"
        leafStr = str(self.initPhase)
        items.append(x + "InitPhase="+leafStr)

        return "{VariableData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "VariableData", 
        "namespace": "variable", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_linux_variables.tech.linux_.variable_collection.variable.variable_data_gen import VariableData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "linux_", 
            "isCurrent": false
        }, 
        {
            "namespace": "variable_collection", 
            "isCurrent": false
        }, 
        {
            "namespace": "variable", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "systemProtected", 
            "yangName": "system-protected", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "value", 
            "yangName": "value", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "initPhase", 
            "yangName": "init-phase", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
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
            "qwilt_tech_linux_variables"
        ]
    }, 
    "createTime": "2013"
}
"""


