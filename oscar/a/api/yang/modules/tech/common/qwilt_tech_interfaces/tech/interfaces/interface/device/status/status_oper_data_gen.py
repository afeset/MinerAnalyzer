


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



from a.api.yang.modules.tech.common.qwilt_tech_interfaces.qwilt_tech_interfaces_module_gen import DriverTypeType


class StatusOperData (object):

    def __init__ (self):

        self.driverType = DriverTypeType.kNone
        self._myHasDriverType=False
        self._myDriverTypeRequested=False
        
        self.pciAddress = ""
        self._myHasPciAddress=False
        self._myPciAddressRequested=False
        
        self.routeTableId = ""
        self._myHasRouteTableId=False
        self._myRouteTableIdRequested=False
        


    def copyFrom (self, other):

        self.driverType=other.driverType
        self._myHasDriverType=other._myHasDriverType
        self._myDriverTypeRequested=other._myDriverTypeRequested
        
        self.pciAddress=other.pciAddress
        self._myHasPciAddress=other._myHasPciAddress
        self._myPciAddressRequested=other._myPciAddressRequested
        
        self.routeTableId=other.routeTableId
        self._myHasRouteTableId=other._myHasRouteTableId
        self._myRouteTableIdRequested=other._myRouteTableIdRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isDriverTypeRequested():
            self.driverType=other.driverType
            self._myHasDriverType=other._myHasDriverType
            self._myDriverTypeRequested=other._myDriverTypeRequested
        
        if self.isPciAddressRequested():
            self.pciAddress=other.pciAddress
            self._myHasPciAddress=other._myHasPciAddress
            self._myPciAddressRequested=other._myPciAddressRequested
        
        if self.isRouteTableIdRequested():
            self.routeTableId=other.routeTableId
            self._myHasRouteTableId=other._myHasRouteTableId
            self._myRouteTableIdRequested=other._myRouteTableIdRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasDriverType():
            self.driverType=other.driverType
            self._myHasDriverType=other._myHasDriverType
            self._myDriverTypeRequested=other._myDriverTypeRequested
        
        if other.hasPciAddress():
            self.pciAddress=other.pciAddress
            self._myHasPciAddress=other._myHasPciAddress
            self._myPciAddressRequested=other._myPciAddressRequested
        
        if other.hasRouteTableId():
            self.routeTableId=other.routeTableId
            self._myHasRouteTableId=other._myHasRouteTableId
            self._myRouteTableIdRequested=other._myRouteTableIdRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.driverType=other.driverType
        self._myHasDriverType=other._myHasDriverType
        
        self.pciAddress=other.pciAddress
        self._myHasPciAddress=other._myHasPciAddress
        
        self.routeTableId=other.routeTableId
        self._myHasRouteTableId=other._myHasRouteTableId
        


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

    def hasDriverType (self):
        return self._myHasDriverType

    def hasPciAddress (self):
        return self._myHasPciAddress

    def hasRouteTableId (self):
        return self._myHasRouteTableId




    # setHas...() methods

    def setHasDriverType (self):
        self._myHasDriverType=True

    def setHasPciAddress (self):
        self._myHasPciAddress=True

    def setHasRouteTableId (self):
        self._myHasRouteTableId=True




    # isRequested...() methods

    def isDriverTypeRequested (self):
        return self._myDriverTypeRequested

    def isPciAddressRequested (self):
        return self._myPciAddressRequested

    def isRouteTableIdRequested (self):
        return self._myRouteTableIdRequested




    # setRequested...() methods

    def setDriverTypeRequested (self):
        self._myDriverTypeRequested=True

    def setPciAddressRequested (self):
        self._myPciAddressRequested=True

    def setRouteTableIdRequested (self):
        self._myRouteTableIdRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myDriverTypeRequested:
            x = "+DriverType="
            if self._myHasDriverType:
                leafStr = str(self.driverType)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myPciAddressRequested:
            x = "+PciAddress="
            if self._myHasPciAddress:
                leafStr = str(self.pciAddress)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myRouteTableIdRequested:
            x = "+RouteTableId="
            if self._myHasRouteTableId:
                leafStr = str(self.routeTableId)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{StatusOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+DriverType="
        if self._myHasDriverType:
            leafStr = str(self.driverType)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myDriverTypeRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+PciAddress="
        if self._myHasPciAddress:
            leafStr = str(self.pciAddress)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myPciAddressRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+RouteTableId="
        if self._myHasRouteTableId:
            leafStr = str(self.routeTableId)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myRouteTableIdRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{StatusOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setDriverTypeRequested()
        self.setPciAddressRequested()
        self.setRouteTableIdRequested()
        
        


    def setDriverType (self, driverType):
        self.driverType = driverType
        self.setHasDriverType()

    def setPciAddress (self, pciAddress):
        self.pciAddress = pciAddress
        self.setHasPciAddress()

    def setRouteTableId (self, routeTableId):
        self.routeTableId = routeTableId
        self.setHasRouteTableId()


"""
Extracted from the below data: 
{
    "node": {
        "className": "StatusOperData", 
        "namespace": "status", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.device.status.status_oper_data_gen import StatusOperData"
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
            "namespace": "device", 
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
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "driverType", 
            "yangName": "driver-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "pciAddress", 
            "yangName": "pci-address", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "routeTableId", 
            "yangName": "route-table-id", 
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


