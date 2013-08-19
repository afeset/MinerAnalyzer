


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



from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import DiskOperationalStatusReasonType
from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import DiskOperationalStatusType


class StatusOperData (object):

    def __init__ (self):

        self.osDevice = ""
        self._myHasOsDevice=False
        self._myOsDeviceRequested=False
        
        self.oprtationalStatus = DiskOperationalStatusType.kDown
        self._myHasOprtationalStatus=False
        self._myOprtationalStatusRequested=False
        
        self.operationalStatusReason = DiskOperationalStatusReasonType.kNone
        self._myHasOperationalStatusReason=False
        self._myOperationalStatusReasonRequested=False
        
        self.size = 0
        self._myHasSize=False
        self._mySizeRequested=False
        


    def copyFrom (self, other):

        self.osDevice=other.osDevice
        self._myHasOsDevice=other._myHasOsDevice
        self._myOsDeviceRequested=other._myOsDeviceRequested
        
        self.oprtationalStatus=other.oprtationalStatus
        self._myHasOprtationalStatus=other._myHasOprtationalStatus
        self._myOprtationalStatusRequested=other._myOprtationalStatusRequested
        
        self.operationalStatusReason=other.operationalStatusReason
        self._myHasOperationalStatusReason=other._myHasOperationalStatusReason
        self._myOperationalStatusReasonRequested=other._myOperationalStatusReasonRequested
        
        self.size=other.size
        self._myHasSize=other._myHasSize
        self._mySizeRequested=other._mySizeRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isOsDeviceRequested():
            self.osDevice=other.osDevice
            self._myHasOsDevice=other._myHasOsDevice
            self._myOsDeviceRequested=other._myOsDeviceRequested
        
        if self.isOprtationalStatusRequested():
            self.oprtationalStatus=other.oprtationalStatus
            self._myHasOprtationalStatus=other._myHasOprtationalStatus
            self._myOprtationalStatusRequested=other._myOprtationalStatusRequested
        
        if self.isOperationalStatusReasonRequested():
            self.operationalStatusReason=other.operationalStatusReason
            self._myHasOperationalStatusReason=other._myHasOperationalStatusReason
            self._myOperationalStatusReasonRequested=other._myOperationalStatusReasonRequested
        
        if self.isSizeRequested():
            self.size=other.size
            self._myHasSize=other._myHasSize
            self._mySizeRequested=other._mySizeRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasOsDevice():
            self.osDevice=other.osDevice
            self._myHasOsDevice=other._myHasOsDevice
            self._myOsDeviceRequested=other._myOsDeviceRequested
        
        if other.hasOprtationalStatus():
            self.oprtationalStatus=other.oprtationalStatus
            self._myHasOprtationalStatus=other._myHasOprtationalStatus
            self._myOprtationalStatusRequested=other._myOprtationalStatusRequested
        
        if other.hasOperationalStatusReason():
            self.operationalStatusReason=other.operationalStatusReason
            self._myHasOperationalStatusReason=other._myHasOperationalStatusReason
            self._myOperationalStatusReasonRequested=other._myOperationalStatusReasonRequested
        
        if other.hasSize():
            self.size=other.size
            self._myHasSize=other._myHasSize
            self._mySizeRequested=other._mySizeRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.osDevice=other.osDevice
        self._myHasOsDevice=other._myHasOsDevice
        
        self.oprtationalStatus=other.oprtationalStatus
        self._myHasOprtationalStatus=other._myHasOprtationalStatus
        
        self.operationalStatusReason=other.operationalStatusReason
        self._myHasOperationalStatusReason=other._myHasOperationalStatusReason
        
        self.size=other.size
        self._myHasSize=other._myHasSize
        


    def setAllNumericToZero (self):
        
        self.size=0
        self.setHasSize()
        
        pass

    def subtractAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasSize():
            if other.hasSize():
                self.size -= other.size
        
        
        pass


    def addAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasSize():
            if other.hasSize():
                self.size += other.size
        
        
        pass


    # has...() methods

    def hasOsDevice (self):
        return self._myHasOsDevice

    def hasOprtationalStatus (self):
        return self._myHasOprtationalStatus

    def hasOperationalStatusReason (self):
        return self._myHasOperationalStatusReason

    def hasSize (self):
        return self._myHasSize




    # setHas...() methods

    def setHasOsDevice (self):
        self._myHasOsDevice=True

    def setHasOprtationalStatus (self):
        self._myHasOprtationalStatus=True

    def setHasOperationalStatusReason (self):
        self._myHasOperationalStatusReason=True

    def setHasSize (self):
        self._myHasSize=True




    # isRequested...() methods

    def isOsDeviceRequested (self):
        return self._myOsDeviceRequested

    def isOprtationalStatusRequested (self):
        return self._myOprtationalStatusRequested

    def isOperationalStatusReasonRequested (self):
        return self._myOperationalStatusReasonRequested

    def isSizeRequested (self):
        return self._mySizeRequested




    # setRequested...() methods

    def setOsDeviceRequested (self):
        self._myOsDeviceRequested=True

    def setOprtationalStatusRequested (self):
        self._myOprtationalStatusRequested=True

    def setOperationalStatusReasonRequested (self):
        self._myOperationalStatusReasonRequested=True

    def setSizeRequested (self):
        self._mySizeRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myOsDeviceRequested:
            x = "+OsDevice="
            if self._myHasOsDevice:
                leafStr = str(self.osDevice)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myOprtationalStatusRequested:
            x = "+OprtationalStatus="
            if self._myHasOprtationalStatus:
                leafStr = str(self.oprtationalStatus)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myOperationalStatusReasonRequested:
            x = "+OperationalStatusReason="
            if self._myHasOperationalStatusReason:
                leafStr = str(self.operationalStatusReason)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._mySizeRequested:
            x = "+Size="
            if self._myHasSize:
                leafStr = str(self.size)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{StatusOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+OsDevice="
        if self._myHasOsDevice:
            leafStr = str(self.osDevice)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myOsDeviceRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+OprtationalStatus="
        if self._myHasOprtationalStatus:
            leafStr = str(self.oprtationalStatus)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myOprtationalStatusRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+OperationalStatusReason="
        if self._myHasOperationalStatusReason:
            leafStr = str(self.operationalStatusReason)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myOperationalStatusReasonRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+Size="
        if self._myHasSize:
            leafStr = str(self.size)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._mySizeRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{StatusOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setOsDeviceRequested()
        self.setOprtationalStatusRequested()
        self.setOperationalStatusReasonRequested()
        self.setSizeRequested()
        
        


    def setOsDevice (self, osDevice):
        self.osDevice = osDevice
        self.setHasOsDevice()

    def setOprtationalStatus (self, oprtationalStatus):
        self.oprtationalStatus = oprtationalStatus
        self.setHasOprtationalStatus()

    def setOperationalStatusReason (self, operationalStatusReason):
        self.operationalStatusReason = operationalStatusReason
        self.setHasOperationalStatusReason()

    def setSize (self, size):
        self.size = size
        self.setHasSize()


"""
Extracted from the below data: 
{
    "node": {
        "className": "StatusOperData", 
        "namespace": "status", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.status.status_oper_data_gen import StatusOperData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "storage", 
            "isCurrent": false
        }, 
        {
            "namespace": "disk", 
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
            "typeHandler": "handler: StringHandler", 
            "memberName": "osDevice", 
            "yangName": "os-device", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "oprtationalStatus", 
            "yangName": "oprtational-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "operationalStatusReason", 
            "yangName": "operational-status-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "size", 
            "yangName": "size", 
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
            "qwilt_tech_storage_disk"
        ]
    }, 
    "createTime": "2013"
}
"""


