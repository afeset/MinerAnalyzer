


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket

import struct


class Ipv4Data(object):

    def __init__ (self):

        self.address = None
        self._myHasAddress=False
        

    def copyFrom (self, other):

        self.address=other.address
        self._myHasAddress=other._myHasAddress
        
    # has...() methods

    def hasAddress (self):
        return self._myHasAddress


    # setHas...() methods

    def setHasAddress (self):
        self._myHasAddress=True


    def clearAllHas (self):

        self._myHasAddress=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasAddress:
            x = "+"
        leafStr = socket.inet_ntop(socket.AF_INET, struct.pack('!L', self.address))
        items.append(x + "Address="+leafStr)

        return "{Ipv4Data: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "Ipv4Data", 
        "namespace": "ipv4", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system.tech.system.name_resolution.static_resolution.hosts.ipv4.ipv4_data_gen import Ipv4Data"
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
            "namespace": "name_resolution", 
            "isCurrent": false
        }, 
        {
            "namespace": "static_resolution", 
            "isCurrent": false
        }, 
        {
            "namespace": "hosts", 
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
            "typeHandler": "handler: Ipv4AddressHandlerPy", 
            "memberName": "address", 
            "yangName": "address", 
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
            "qwilt_tech_system"
        ]
    }, 
    "createTime": "2013"
}
"""


