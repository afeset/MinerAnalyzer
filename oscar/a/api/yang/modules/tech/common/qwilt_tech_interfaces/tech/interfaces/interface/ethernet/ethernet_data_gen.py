


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class EthernetData(object):

    def __init__ (self):

        self.dummy = False
        self._myHasDummy=False
        

    def copyFrom (self, other):

        self.dummy=other.dummy
        self._myHasDummy=other._myHasDummy
        
    # has...() methods

    def hasDummy (self):
        return self._myHasDummy


    # setHas...() methods

    def setHasDummy (self):
        self._myHasDummy=True


    def clearAllHas (self):

        self._myHasDummy=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasDummy:
            x = "+"
        leafStr = str(self.dummy)
        items.append(x + "Dummy="+leafStr)

        return "{EthernetData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "EthernetData", 
        "namespace": "ethernet", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.ethernet.ethernet_data_gen import EthernetData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "interfaces", 
            "isCurrent": false
        }, 
        {
            "namespace": "interface", 
            "isCurrent": false
        }, 
        {
            "namespace": "ethernet", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "dummy", 
            "yangName": "dummy", 
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
            "qwilt_tech_interfaces"
        ]
    }, 
    "createTime": "2013"
}
"""


