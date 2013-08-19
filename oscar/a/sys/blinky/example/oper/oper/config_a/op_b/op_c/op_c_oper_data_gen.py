


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



import struct


class OpCOperData (object):

    def __init__ (self):

        self.ipVal = None
        self._myHasIpVal=False
        self._myIpValRequested=False
        
        self.id = 0
        self._myHasId=False
        self._myIdRequested=False
        
        self.val = 0
        self._myHasVal=False
        self._myValRequested=False
        
        self.ipPrefixVal = None
        self._myHasIpPrefixVal=False
        self._myIpPrefixValRequested=False
        


    def copyFrom (self, other):

        self.ipVal=other.ipVal
        self._myHasIpVal=other._myHasIpVal
        self._myIpValRequested=other._myIpValRequested
        
        self.id=other.id
        self._myHasId=other._myHasId
        self._myIdRequested=other._myIdRequested
        
        self.val=other.val
        self._myHasVal=other._myHasVal
        self._myValRequested=other._myValRequested
        
        self.ipPrefixVal=other.ipPrefixVal
        self._myHasIpPrefixVal=other._myHasIpPrefixVal
        self._myIpPrefixValRequested=other._myIpPrefixValRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isIpValRequested():
            self.ipVal=other.ipVal
            self._myHasIpVal=other._myHasIpVal
            self._myIpValRequested=other._myIpValRequested
        
        if self.isIdRequested():
            self.id=other.id
            self._myHasId=other._myHasId
            self._myIdRequested=other._myIdRequested
        
        if self.isValRequested():
            self.val=other.val
            self._myHasVal=other._myHasVal
            self._myValRequested=other._myValRequested
        
        if self.isIpPrefixValRequested():
            self.ipPrefixVal=other.ipPrefixVal
            self._myHasIpPrefixVal=other._myHasIpPrefixVal
            self._myIpPrefixValRequested=other._myIpPrefixValRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasIpVal():
            self.ipVal=other.ipVal
            self._myHasIpVal=other._myHasIpVal
            self._myIpValRequested=other._myIpValRequested
        
        if other.hasId():
            self.id=other.id
            self._myHasId=other._myHasId
            self._myIdRequested=other._myIdRequested
        
        if other.hasVal():
            self.val=other.val
            self._myHasVal=other._myHasVal
            self._myValRequested=other._myValRequested
        
        if other.hasIpPrefixVal():
            self.ipPrefixVal=other.ipPrefixVal
            self._myHasIpPrefixVal=other._myHasIpPrefixVal
            self._myIpPrefixValRequested=other._myIpPrefixValRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.ipVal=other.ipVal
        self._myHasIpVal=other._myHasIpVal
        
        self.id=other.id
        self._myHasId=other._myHasId
        
        self.val=other.val
        self._myHasVal=other._myHasVal
        
        self.ipPrefixVal=other.ipPrefixVal
        self._myHasIpPrefixVal=other._myHasIpPrefixVal
        


    def setAllNumericToZero (self):
        
        self.id=0
        self.setHasId()
        self.val=0
        self.setHasVal()
        
        pass

    def subtractAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasId():
            if other.hasId():
                self.id -= other.id
        
        if self.hasVal():
            if other.hasVal():
                self.val -= other.val
        
        
        pass


    def addAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasId():
            if other.hasId():
                self.id += other.id
        
        if self.hasVal():
            if other.hasVal():
                self.val += other.val
        
        
        pass


    # has...() methods

    def hasIpVal (self):
        return self._myHasIpVal

    def hasId (self):
        return self._myHasId

    def hasVal (self):
        return self._myHasVal

    def hasIpPrefixVal (self):
        return self._myHasIpPrefixVal




    # setHas...() methods

    def setHasIpVal (self):
        self._myHasIpVal=True

    def setHasId (self):
        self._myHasId=True

    def setHasVal (self):
        self._myHasVal=True

    def setHasIpPrefixVal (self):
        self._myHasIpPrefixVal=True




    # isRequested...() methods

    def isIpValRequested (self):
        return self._myIpValRequested

    def isIdRequested (self):
        return self._myIdRequested

    def isValRequested (self):
        return self._myValRequested

    def isIpPrefixValRequested (self):
        return self._myIpPrefixValRequested




    # setRequested...() methods

    def setIpValRequested (self):
        self._myIpValRequested=True

    def setIdRequested (self):
        self._myIdRequested=True

    def setValRequested (self):
        self._myValRequested=True

    def setIpPrefixValRequested (self):
        self._myIpPrefixValRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myIpValRequested:
            x = "+IpVal="
            if self._myHasIpVal:
                leafStr = socket.inet_ntop(socket.AF_INET, struct.pack('!L', self.ipVal))
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myIdRequested:
            x = "+Id="
            if self._myHasId:
                leafStr = str(self.id)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myValRequested:
            x = "+Val="
            if self._myHasVal:
                leafStr = str(self.val)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myIpPrefixValRequested:
            x = "+IpPrefixVal="
            if self._myHasIpPrefixVal:
                (ip, prefix) = self.ipPrefixVal
                leafStr = "%s/%d" % (socket.inet_ntop(socket.AF_INET, struct.pack('!L', ip)), prefix)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{OpCOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+IpVal="
        if self._myHasIpVal:
            leafStr = socket.inet_ntop(socket.AF_INET, struct.pack('!L', self.ipVal))
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myIpValRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+Id="
        if self._myHasId:
            leafStr = str(self.id)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myIdRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+Val="
        if self._myHasVal:
            leafStr = str(self.val)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myValRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+IpPrefixVal="
        if self._myHasIpPrefixVal:
            (ip, prefix) = self.ipPrefixVal
            leafStr = "%s/%d" % (socket.inet_ntop(socket.AF_INET, struct.pack('!L', ip)), prefix)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myIpPrefixValRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{OpCOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setIpValRequested()
        self.setIdRequested()
        self.setValRequested()
        self.setIpPrefixValRequested()
        
        


    def setIpVal (self, ipVal):
        self.ipVal = ipVal
        self.setHasIpVal()

    def setId (self, id):
        self.id = id
        self.setHasId()

    def setVal (self, val):
        self.val = val
        self.setHasVal()

    def setIpPrefixVal (self, ipPrefixVal):
        self.ipPrefixVal = ipPrefixVal
        self.setHasIpPrefixVal()


"""
Extracted from the below data: 
{
    "node": {
        "className": "OpCOperData", 
        "namespace": "op_c", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_b.op_c.op_c_oper_data_gen import OpCOperData"
    }, 
    "ancestors": [
        {
            "namespace": "config_a", 
            "isCurrent": false
        }, 
        {
            "namespace": "op_b", 
            "isCurrent": false
        }, 
        {
            "namespace": "op_c", 
            "isCurrent": true
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: Ipv4AddressHandlerPy", 
            "memberName": "ipVal", 
            "yangName": "ip-val", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "id", 
            "yangName": "id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "val", 
            "yangName": "val", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: Ipv4PrefixHandlerPy", 
            "memberName": "ipPrefixVal", 
            "yangName": "ip-prefix-val", 
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
            "oper", 
            "oper"
        ]
    }, 
    "createTime": "2013"
}
"""


