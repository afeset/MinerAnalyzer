


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



from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import FileSystemTypeType
from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import FileSystemOperationalStatusType
from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import FileSystemOperationalStatusReasonType


class StatusOperData (object):

    def __init__ (self):

        self.uuid = ""
        self._myHasUuid=False
        self._myUuidRequested=False
        
        self.operationalStatus = FileSystemOperationalStatusType.kDown
        self._myHasOperationalStatus=False
        self._myOperationalStatusRequested=False
        
        self.fileSystemTypeRaw = ""
        self._myHasFileSystemTypeRaw=False
        self._myFileSystemTypeRawRequested=False
        
        self.fileSystemType = FileSystemTypeType.kExt3
        self._myHasFileSystemType=False
        self._myFileSystemTypeRequested=False
        
        self.expectedUuid = ""
        self._myHasExpectedUuid=False
        self._myExpectedUuidRequested=False
        
        self.operationalStatusReason = FileSystemOperationalStatusReasonType.kNoDevice
        self._myHasOperationalStatusReason=False
        self._myOperationalStatusReasonRequested=False
        


    def copyFrom (self, other):

        self.uuid=other.uuid
        self._myHasUuid=other._myHasUuid
        self._myUuidRequested=other._myUuidRequested
        
        self.operationalStatus=other.operationalStatus
        self._myHasOperationalStatus=other._myHasOperationalStatus
        self._myOperationalStatusRequested=other._myOperationalStatusRequested
        
        self.fileSystemTypeRaw=other.fileSystemTypeRaw
        self._myHasFileSystemTypeRaw=other._myHasFileSystemTypeRaw
        self._myFileSystemTypeRawRequested=other._myFileSystemTypeRawRequested
        
        self.fileSystemType=other.fileSystemType
        self._myHasFileSystemType=other._myHasFileSystemType
        self._myFileSystemTypeRequested=other._myFileSystemTypeRequested
        
        self.expectedUuid=other.expectedUuid
        self._myHasExpectedUuid=other._myHasExpectedUuid
        self._myExpectedUuidRequested=other._myExpectedUuidRequested
        
        self.operationalStatusReason=other.operationalStatusReason
        self._myHasOperationalStatusReason=other._myHasOperationalStatusReason
        self._myOperationalStatusReasonRequested=other._myOperationalStatusReasonRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isUuidRequested():
            self.uuid=other.uuid
            self._myHasUuid=other._myHasUuid
            self._myUuidRequested=other._myUuidRequested
        
        if self.isOperationalStatusRequested():
            self.operationalStatus=other.operationalStatus
            self._myHasOperationalStatus=other._myHasOperationalStatus
            self._myOperationalStatusRequested=other._myOperationalStatusRequested
        
        if self.isFileSystemTypeRawRequested():
            self.fileSystemTypeRaw=other.fileSystemTypeRaw
            self._myHasFileSystemTypeRaw=other._myHasFileSystemTypeRaw
            self._myFileSystemTypeRawRequested=other._myFileSystemTypeRawRequested
        
        if self.isFileSystemTypeRequested():
            self.fileSystemType=other.fileSystemType
            self._myHasFileSystemType=other._myHasFileSystemType
            self._myFileSystemTypeRequested=other._myFileSystemTypeRequested
        
        if self.isExpectedUuidRequested():
            self.expectedUuid=other.expectedUuid
            self._myHasExpectedUuid=other._myHasExpectedUuid
            self._myExpectedUuidRequested=other._myExpectedUuidRequested
        
        if self.isOperationalStatusReasonRequested():
            self.operationalStatusReason=other.operationalStatusReason
            self._myHasOperationalStatusReason=other._myHasOperationalStatusReason
            self._myOperationalStatusReasonRequested=other._myOperationalStatusReasonRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasUuid():
            self.uuid=other.uuid
            self._myHasUuid=other._myHasUuid
            self._myUuidRequested=other._myUuidRequested
        
        if other.hasOperationalStatus():
            self.operationalStatus=other.operationalStatus
            self._myHasOperationalStatus=other._myHasOperationalStatus
            self._myOperationalStatusRequested=other._myOperationalStatusRequested
        
        if other.hasFileSystemTypeRaw():
            self.fileSystemTypeRaw=other.fileSystemTypeRaw
            self._myHasFileSystemTypeRaw=other._myHasFileSystemTypeRaw
            self._myFileSystemTypeRawRequested=other._myFileSystemTypeRawRequested
        
        if other.hasFileSystemType():
            self.fileSystemType=other.fileSystemType
            self._myHasFileSystemType=other._myHasFileSystemType
            self._myFileSystemTypeRequested=other._myFileSystemTypeRequested
        
        if other.hasExpectedUuid():
            self.expectedUuid=other.expectedUuid
            self._myHasExpectedUuid=other._myHasExpectedUuid
            self._myExpectedUuidRequested=other._myExpectedUuidRequested
        
        if other.hasOperationalStatusReason():
            self.operationalStatusReason=other.operationalStatusReason
            self._myHasOperationalStatusReason=other._myHasOperationalStatusReason
            self._myOperationalStatusReasonRequested=other._myOperationalStatusReasonRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.uuid=other.uuid
        self._myHasUuid=other._myHasUuid
        
        self.operationalStatus=other.operationalStatus
        self._myHasOperationalStatus=other._myHasOperationalStatus
        
        self.fileSystemTypeRaw=other.fileSystemTypeRaw
        self._myHasFileSystemTypeRaw=other._myHasFileSystemTypeRaw
        
        self.fileSystemType=other.fileSystemType
        self._myHasFileSystemType=other._myHasFileSystemType
        
        self.expectedUuid=other.expectedUuid
        self._myHasExpectedUuid=other._myHasExpectedUuid
        
        self.operationalStatusReason=other.operationalStatusReason
        self._myHasOperationalStatusReason=other._myHasOperationalStatusReason
        


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

    def hasUuid (self):
        return self._myHasUuid

    def hasOperationalStatus (self):
        return self._myHasOperationalStatus

    def hasFileSystemTypeRaw (self):
        return self._myHasFileSystemTypeRaw

    def hasFileSystemType (self):
        return self._myHasFileSystemType

    def hasExpectedUuid (self):
        return self._myHasExpectedUuid

    def hasOperationalStatusReason (self):
        return self._myHasOperationalStatusReason




    # setHas...() methods

    def setHasUuid (self):
        self._myHasUuid=True

    def setHasOperationalStatus (self):
        self._myHasOperationalStatus=True

    def setHasFileSystemTypeRaw (self):
        self._myHasFileSystemTypeRaw=True

    def setHasFileSystemType (self):
        self._myHasFileSystemType=True

    def setHasExpectedUuid (self):
        self._myHasExpectedUuid=True

    def setHasOperationalStatusReason (self):
        self._myHasOperationalStatusReason=True




    # isRequested...() methods

    def isUuidRequested (self):
        return self._myUuidRequested

    def isOperationalStatusRequested (self):
        return self._myOperationalStatusRequested

    def isFileSystemTypeRawRequested (self):
        return self._myFileSystemTypeRawRequested

    def isFileSystemTypeRequested (self):
        return self._myFileSystemTypeRequested

    def isExpectedUuidRequested (self):
        return self._myExpectedUuidRequested

    def isOperationalStatusReasonRequested (self):
        return self._myOperationalStatusReasonRequested




    # setRequested...() methods

    def setUuidRequested (self):
        self._myUuidRequested=True

    def setOperationalStatusRequested (self):
        self._myOperationalStatusRequested=True

    def setFileSystemTypeRawRequested (self):
        self._myFileSystemTypeRawRequested=True

    def setFileSystemTypeRequested (self):
        self._myFileSystemTypeRequested=True

    def setExpectedUuidRequested (self):
        self._myExpectedUuidRequested=True

    def setOperationalStatusReasonRequested (self):
        self._myOperationalStatusReasonRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myUuidRequested:
            x = "+Uuid="
            if self._myHasUuid:
                leafStr = str(self.uuid)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myOperationalStatusRequested:
            x = "+OperationalStatus="
            if self._myHasOperationalStatus:
                leafStr = str(self.operationalStatus)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myFileSystemTypeRawRequested:
            x = "+FileSystemTypeRaw="
            if self._myHasFileSystemTypeRaw:
                leafStr = str(self.fileSystemTypeRaw)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myFileSystemTypeRequested:
            x = "+FileSystemType="
            if self._myHasFileSystemType:
                leafStr = str(self.fileSystemType)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myExpectedUuidRequested:
            x = "+ExpectedUuid="
            if self._myHasExpectedUuid:
                leafStr = str(self.expectedUuid)
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


        return "{StatusOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+Uuid="
        if self._myHasUuid:
            leafStr = str(self.uuid)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myUuidRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+OperationalStatus="
        if self._myHasOperationalStatus:
            leafStr = str(self.operationalStatus)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myOperationalStatusRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+FileSystemTypeRaw="
        if self._myHasFileSystemTypeRaw:
            leafStr = str(self.fileSystemTypeRaw)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myFileSystemTypeRawRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+FileSystemType="
        if self._myHasFileSystemType:
            leafStr = str(self.fileSystemType)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myFileSystemTypeRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+ExpectedUuid="
        if self._myHasExpectedUuid:
            leafStr = str(self.expectedUuid)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myExpectedUuidRequested:
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


        return "{StatusOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setUuidRequested()
        self.setOperationalStatusRequested()
        self.setFileSystemTypeRawRequested()
        self.setFileSystemTypeRequested()
        self.setExpectedUuidRequested()
        self.setOperationalStatusReasonRequested()
        
        


    def setUuid (self, uuid):
        self.uuid = uuid
        self.setHasUuid()

    def setOperationalStatus (self, operationalStatus):
        self.operationalStatus = operationalStatus
        self.setHasOperationalStatus()

    def setFileSystemTypeRaw (self, fileSystemTypeRaw):
        self.fileSystemTypeRaw = fileSystemTypeRaw
        self.setHasFileSystemTypeRaw()

    def setFileSystemType (self, fileSystemType):
        self.fileSystemType = fileSystemType
        self.setHasFileSystemType()

    def setExpectedUuid (self, expectedUuid):
        self.expectedUuid = expectedUuid
        self.setHasExpectedUuid()

    def setOperationalStatusReason (self, operationalStatusReason):
        self.operationalStatusReason = operationalStatusReason
        self.setHasOperationalStatusReason()


"""
Extracted from the below data: 
{
    "node": {
        "className": "StatusOperData", 
        "namespace": "status", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.file_system.status.status_oper_data_gen import StatusOperData"
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
            "namespace": "file_system", 
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
            "memberName": "uuid", 
            "yangName": "uuid", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "operationalStatus", 
            "yangName": "operational-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "fileSystemTypeRaw", 
            "yangName": "file-system-type-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "fileSystemType", 
            "yangName": "file-system-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "expectedUuid", 
            "yangName": "expected-uuid", 
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


