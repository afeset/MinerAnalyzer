


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

        self.defaultGateway = None
        self._myHasDefaultGateway=False
        

    def copyFrom (self, other):

        self.defaultGateway=other.defaultGateway
        self._myHasDefaultGateway=other._myHasDefaultGateway
        
    # has...() methods

    def hasDefaultGateway (self):
        return self._myHasDefaultGateway


    # setHas...() methods

    def setHasDefaultGateway (self):
        self._myHasDefaultGateway=True


    def clearAllHas (self):

        self._myHasDefaultGateway=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasDefaultGateway:
            x = "+"
        leafStr = socket.inet_ntop(socket.AF_INET, struct.pack('!L', self.defaultGateway))
        items.append(x + "DefaultGateway="+leafStr)

        return "{Ipv4Data: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "Ipv4Data", 
        "namespace": "ipv4", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.ipv4.ipv4_data_gen import Ipv4Data"
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
            "namespace": "ipv4", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: Ipv4AddressHandlerPy", 
            "memberName": "defaultGateway", 
            "yangName": "default-gateway", 
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


