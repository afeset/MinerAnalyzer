


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class AddressData(object):

    def __init__ (self):

        self.ip = ""
        self._myHasIp=False
        

    def copyFrom (self, other):

        self.ip=other.ip
        self._myHasIp=other._myHasIp
        
    # has...() methods

    def hasIp (self):
        return self._myHasIp


    # setHas...() methods

    def setHasIp (self):
        self._myHasIp=True


    def clearAllHas (self):

        self._myHasIp=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasIp:
            x = "+"
        leafStr = str(self.ip)
        items.append(x + "Ip="+leafStr)

        return "{AddressData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "AddressData", 
        "namespace": "address", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.ipv6.address.address_data_gen import AddressData"
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
            "namespace": "ipv6", 
            "isCurrent": false
        }, 
        {
            "namespace": "address", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: BuiltinStringHandler", 
            "memberName": "ip", 
            "yangName": "ip", 
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


