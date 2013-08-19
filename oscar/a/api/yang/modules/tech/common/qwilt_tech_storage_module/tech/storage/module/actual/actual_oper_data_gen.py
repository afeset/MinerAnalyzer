


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





class ActualOperData (object):

    def __init__ (self):

        self.enabled = False
        self._myHasEnabled=False
        self._myEnabledRequested=False
        


    def copyFrom (self, other):

        self.enabled=other.enabled
        self._myHasEnabled=other._myHasEnabled
        self._myEnabledRequested=other._myEnabledRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isEnabledRequested():
            self.enabled=other.enabled
            self._myHasEnabled=other._myHasEnabled
            self._myEnabledRequested=other._myEnabledRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasEnabled():
            self.enabled=other.enabled
            self._myHasEnabled=other._myHasEnabled
            self._myEnabledRequested=other._myEnabledRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.enabled=other.enabled
        self._myHasEnabled=other._myHasEnabled
        


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

    def hasEnabled (self):
        return self._myHasEnabled




    # setHas...() methods

    def setHasEnabled (self):
        self._myHasEnabled=True




    # isRequested...() methods

    def isEnabledRequested (self):
        return self._myEnabledRequested




    # setRequested...() methods

    def setEnabledRequested (self):
        self._myEnabledRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myEnabledRequested:
            x = "+Enabled="
            if self._myHasEnabled:
                leafStr = str(self.enabled)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{ActualOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+Enabled="
        if self._myHasEnabled:
            leafStr = str(self.enabled)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myEnabledRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{ActualOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setEnabledRequested()
        
        


    def setEnabled (self, enabled):
        self.enabled = enabled
        self.setHasEnabled()


"""
Extracted from the below data: 
{
    "node": {
        "className": "ActualOperData", 
        "namespace": "actual", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_module.tech.storage.module.actual.actual_oper_data_gen import ActualOperData"
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
            "namespace": "module", 
            "isCurrent": false
        }, 
        {
            "namespace": "actual", 
            "isCurrent": true
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
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
            "qwilt_tech_storage_module"
        ]
    }, 
    "createTime": "2013"
}
"""


