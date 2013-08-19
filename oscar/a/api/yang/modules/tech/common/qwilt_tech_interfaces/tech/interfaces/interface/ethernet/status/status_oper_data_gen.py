


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



from a.infra.net.mac_address import MacAddress


class StatusOperData (object):

    def __init__ (self):

        self.macAddress = MacAddress('\0'*6)
        self._myHasMacAddress=False
        self._myMacAddressRequested=False
        


    def copyFrom (self, other):

        self.macAddress=other.macAddress
        self._myHasMacAddress=other._myHasMacAddress
        self._myMacAddressRequested=other._myMacAddressRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isMacAddressRequested():
            self.macAddress=other.macAddress
            self._myHasMacAddress=other._myHasMacAddress
            self._myMacAddressRequested=other._myMacAddressRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasMacAddress():
            self.macAddress=other.macAddress
            self._myHasMacAddress=other._myHasMacAddress
            self._myMacAddressRequested=other._myMacAddressRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.macAddress=other.macAddress
        self._myHasMacAddress=other._myHasMacAddress
        


    def setAllNumericToZero (self):
        
        
        pass

    def subtractAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        
        pass


    def addAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        
        pass


    # has...() methods

    def hasMacAddress (self):
        return self._myHasMacAddress




    # setHas...() methods

    def setHasMacAddress (self):
        self._myHasMacAddress=True




    # isRequested...() methods

    def isMacAddressRequested (self):
        return self._myMacAddressRequested




    # setRequested...() methods

    def setMacAddressRequested (self):
        self._myMacAddressRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myMacAddressRequested:
            x = "+MacAddress="
            if self._myHasMacAddress:
                leafStr = str(self.macAddress)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{StatusOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+MacAddress="
        if self._myHasMacAddress:
            leafStr = str(self.macAddress)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myMacAddressRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{StatusOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setMacAddressRequested()
        
        


    def setMacAddress (self, macAddress):
        self.macAddress = macAddress
        self.setHasMacAddress()


"""
Extracted from the below data: 
{
    "node": {
        "className": "StatusOperData", 
        "namespace": "status", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.ethernet.status.status_oper_data_gen import StatusOperData"
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
            "isCurrent": false
        }, 
        {
            "namespace": "status", 
            "isCurrent": true
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: MacAddressHandlerPy", 
            "memberName": "macAddress", 
            "yangName": "mac-address", 
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


