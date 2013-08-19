


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket

import struct


class PrefixData(object):

    def __init__ (self):

        self.prefix = None
        self._myHasPrefix=False
        

    def copyFrom (self, other):

        self.prefix=other.prefix
        self._myHasPrefix=other._myHasPrefix
        
    # has...() methods

    def hasPrefix (self):
        return self._myHasPrefix


    # setHas...() methods

    def setHasPrefix (self):
        self._myHasPrefix=True


    def clearAllHas (self):

        self._myHasPrefix=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasPrefix:
            x = "+"
        (ip, prefix) = self.prefix
        leafStr = "%s/%d" % (socket.inet_ntop(socket.AF_INET6, ip), prefix)
        items.append(x + "Prefix="+leafStr)

        return "{PrefixData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "PrefixData", 
        "namespace": "prefix", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.zones.zone.ipv6.prefix.prefix_data_gen import PrefixData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "content", 
            "isCurrent": false
        }, 
        {
            "namespace": "zones", 
            "isCurrent": false
        }, 
        {
            "namespace": "zone", 
            "isCurrent": false
        }, 
        {
            "namespace": "ipv6", 
            "isCurrent": false
        }, 
        {
            "namespace": "prefix", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: Ipv6PrefixHandlerPy", 
            "memberName": "prefix", 
            "yangName": "prefix", 
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
            "content", 
            "qwilt_tech_content"
        ]
    }, 
    "createTime": "2013"
}
"""


