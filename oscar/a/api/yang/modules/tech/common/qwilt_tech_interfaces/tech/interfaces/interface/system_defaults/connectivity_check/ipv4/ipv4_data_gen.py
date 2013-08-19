


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket

from a.api.yang.modules.tech.common.qwilt_tech_interfaces_types.qwilt_tech_interfaces_types_module_gen import ConnectivityCheckIpv4MethodType


class Ipv4Data(object):

    def __init__ (self):

        self.method = ConnectivityCheckIpv4MethodType.kArp
        self._myHasMethod=False
        

    def copyFrom (self, other):

        self.method=other.method
        self._myHasMethod=other._myHasMethod
        
    # has...() methods

    def hasMethod (self):
        return self._myHasMethod


    # setHas...() methods

    def setHasMethod (self):
        self._myHasMethod=True


    def clearAllHas (self):

        self._myHasMethod=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasMethod:
            x = "+"
        leafStr = str(self.method)
        items.append(x + "Method="+leafStr)

        return "{Ipv4Data: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "Ipv4Data", 
        "namespace": "ipv4", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.system_defaults.connectivity_check.ipv4.ipv4_data_gen import Ipv4Data"
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
            "namespace": "system_defaults", 
            "isCurrent": false
        }, 
        {
            "namespace": "connectivity_check", 
            "isCurrent": false
        }, 
        {
            "namespace": "ipv4", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "method", 
            "yangName": "method", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "arp", 
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


