


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket

import struct


class LakeData(object):

    def __init__ (self):

        self.ip = None
        self._myHasIp=False
        
        self.name = ""
        self._myHasName=False
        

    def copyFrom (self, other):

        self.ip=other.ip
        self._myHasIp=other._myHasIp
        
        self.name=other.name
        self._myHasName=other._myHasName
        
    # has...() methods

    def hasIp (self):
        return self._myHasIp

    def hasName (self):
        return self._myHasName


    # setHas...() methods

    def setHasIp (self):
        self._myHasIp=True

    def setHasName (self):
        self._myHasName=True


    def clearAllHas (self):

        self._myHasIp=False

        self._myHasName=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasIp:
            x = "+"
        leafStr = socket.inet_ntop(socket.AF_INET, struct.pack('!L', self.ip))
        items.append(x + "Ip="+leafStr)

        x=""
        if self._myHasName:
            x = "+"
        leafStr = str(self.name)
        items.append(x + "Name="+leafStr)

        return "{LakeData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "LakeData", 
        "namespace": "lake", 
        "importStatement": "from a.sys.blinky.example.lake_example.lake.lake_data_gen import LakeData"
    }, 
    "ancestors": [
        {
            "namespace": "lake", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: Ipv4AddressHandlerPy", 
            "memberName": "ip", 
            "yangName": "ip", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
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
            "sys", 
            "blinky", 
            "example", 
            "lake_example"
        ]
    }, 
    "createTime": "2013"
}
"""


