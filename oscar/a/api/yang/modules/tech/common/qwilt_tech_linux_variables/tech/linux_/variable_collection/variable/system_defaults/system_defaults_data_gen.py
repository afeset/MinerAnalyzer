


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket

from a.api.yang.modules.tech.common.qwilt_tech_linux_variables.qwilt_tech_linux_variables_module_gen import InitPhase


class SystemDefaultsData(object):

    def __init__ (self):

        self.systemProtected = False
        self._myHasSystemProtected=False
        
        self.initPhase = InitPhase.kInitial
        self._myHasInitPhase=False
        
        self.description = ""
        self._myHasDescription=False
        
        self.value = ""
        self._myHasValue=False
        

    def copyFrom (self, other):

        self.systemProtected=other.systemProtected
        self._myHasSystemProtected=other._myHasSystemProtected
        
        self.initPhase=other.initPhase
        self._myHasInitPhase=other._myHasInitPhase
        
        self.description=other.description
        self._myHasDescription=other._myHasDescription
        
        self.value=other.value
        self._myHasValue=other._myHasValue
        
    # has...() methods

    def hasSystemProtected (self):
        return self._myHasSystemProtected

    def hasInitPhase (self):
        return self._myHasInitPhase

    def hasDescription (self):
        return self._myHasDescription

    def hasValue (self):
        return self._myHasValue


    # setHas...() methods

    def setHasSystemProtected (self):
        self._myHasSystemProtected=True

    def setHasInitPhase (self):
        self._myHasInitPhase=True

    def setHasDescription (self):
        self._myHasDescription=True

    def setHasValue (self):
        self._myHasValue=True


    def clearAllHas (self):

        self._myHasSystemProtected=False

        self._myHasInitPhase=False

        self._myHasDescription=False

        self._myHasValue=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasSystemProtected:
            x = "+"
        leafStr = str(self.systemProtected)
        items.append(x + "SystemProtected="+leafStr)

        x=""
        if self._myHasInitPhase:
            x = "+"
        leafStr = str(self.initPhase)
        items.append(x + "InitPhase="+leafStr)

        x=""
        if self._myHasDescription:
            x = "+"
        leafStr = str(self.description)
        items.append(x + "Description="+leafStr)

        x=""
        if self._myHasValue:
            x = "+"
        leafStr = str(self.value)
        items.append(x + "Value="+leafStr)

        return "{SystemDefaultsData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "SystemDefaultsData", 
        "namespace": "system_defaults", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_linux_variables.tech.linux_.variable_collection.variable.system_defaults.system_defaults_data_gen import SystemDefaultsData"
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
            "isCurrent": false
        }, 
        {
            "namespace": "system_defaults", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "systemProtected", 
            "yangName": "system-protected", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "initPhase", 
            "yangName": "init-phase", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "initial", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "value", 
            "yangName": "value", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
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
            "qwilt_tech_linux_variables"
        ]
    }, 
    "createTime": "2013"
}
"""


