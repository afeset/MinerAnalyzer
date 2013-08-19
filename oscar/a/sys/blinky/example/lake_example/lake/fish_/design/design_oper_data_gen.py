


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
from a.sys.blinky.example.lake_example.lake_example_module_gen import DesignColorT


class DesignOperData (object):

    def __init__ (self):

        self.color = DesignColorT.kWhite
        self._myHasColor=False
        self._myColorRequested=False
        
        self.pattern = ""
        self._myHasPattern=False
        self._myPatternRequested=False
        
        self.macAddress = MacAddress('\0'*6)
        self._myHasMacAddress=False
        self._myMacAddressRequested=False
        
        self.lineWidth = 0
        self._myHasLineWidth=False
        self._myLineWidthRequested=False
        


    def copyFrom (self, other):

        self.color=other.color
        self._myHasColor=other._myHasColor
        self._myColorRequested=other._myColorRequested
        
        self.pattern=other.pattern
        self._myHasPattern=other._myHasPattern
        self._myPatternRequested=other._myPatternRequested
        
        self.macAddress=other.macAddress
        self._myHasMacAddress=other._myHasMacAddress
        self._myMacAddressRequested=other._myMacAddressRequested
        
        self.lineWidth=other.lineWidth
        self._myHasLineWidth=other._myHasLineWidth
        self._myLineWidthRequested=other._myLineWidthRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isColorRequested():
            self.color=other.color
            self._myHasColor=other._myHasColor
            self._myColorRequested=other._myColorRequested
        
        if self.isPatternRequested():
            self.pattern=other.pattern
            self._myHasPattern=other._myHasPattern
            self._myPatternRequested=other._myPatternRequested
        
        if self.isMacAddressRequested():
            self.macAddress=other.macAddress
            self._myHasMacAddress=other._myHasMacAddress
            self._myMacAddressRequested=other._myMacAddressRequested
        
        if self.isLineWidthRequested():
            self.lineWidth=other.lineWidth
            self._myHasLineWidth=other._myHasLineWidth
            self._myLineWidthRequested=other._myLineWidthRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasColor():
            self.color=other.color
            self._myHasColor=other._myHasColor
            self._myColorRequested=other._myColorRequested
        
        if other.hasPattern():
            self.pattern=other.pattern
            self._myHasPattern=other._myHasPattern
            self._myPatternRequested=other._myPatternRequested
        
        if other.hasMacAddress():
            self.macAddress=other.macAddress
            self._myHasMacAddress=other._myHasMacAddress
            self._myMacAddressRequested=other._myMacAddressRequested
        
        if other.hasLineWidth():
            self.lineWidth=other.lineWidth
            self._myHasLineWidth=other._myHasLineWidth
            self._myLineWidthRequested=other._myLineWidthRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.color=other.color
        self._myHasColor=other._myHasColor
        
        self.pattern=other.pattern
        self._myHasPattern=other._myHasPattern
        
        self.macAddress=other.macAddress
        self._myHasMacAddress=other._myHasMacAddress
        
        self.lineWidth=other.lineWidth
        self._myHasLineWidth=other._myHasLineWidth
        


    def setAllNumericToZero (self):
        
        self.lineWidth=0
        self.setHasLineWidth()
        
        pass

    def subtractAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasLineWidth():
            if other.hasLineWidth():
                self.lineWidth -= other.lineWidth
        
        
        pass


    def addAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasLineWidth():
            if other.hasLineWidth():
                self.lineWidth += other.lineWidth
        
        
        pass


    # has...() methods

    def hasColor (self):
        return self._myHasColor

    def hasPattern (self):
        return self._myHasPattern

    def hasMacAddress (self):
        return self._myHasMacAddress

    def hasLineWidth (self):
        return self._myHasLineWidth




    # setHas...() methods

    def setHasColor (self):
        self._myHasColor=True

    def setHasPattern (self):
        self._myHasPattern=True

    def setHasMacAddress (self):
        self._myHasMacAddress=True

    def setHasLineWidth (self):
        self._myHasLineWidth=True




    # isRequested...() methods

    def isColorRequested (self):
        return self._myColorRequested

    def isPatternRequested (self):
        return self._myPatternRequested

    def isMacAddressRequested (self):
        return self._myMacAddressRequested

    def isLineWidthRequested (self):
        return self._myLineWidthRequested




    # setRequested...() methods

    def setColorRequested (self):
        self._myColorRequested=True

    def setPatternRequested (self):
        self._myPatternRequested=True

    def setMacAddressRequested (self):
        self._myMacAddressRequested=True

    def setLineWidthRequested (self):
        self._myLineWidthRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myColorRequested:
            x = "+Color="
            if self._myHasColor:
                leafStr = str(self.color)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myPatternRequested:
            x = "+Pattern="
            if self._myHasPattern:
                leafStr = str(self.pattern)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myMacAddressRequested:
            x = "+MacAddress="
            if self._myHasMacAddress:
                leafStr = str(self.macAddress)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myLineWidthRequested:
            x = "+LineWidth="
            if self._myHasLineWidth:
                leafStr = str(self.lineWidth)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{DesignOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+Color="
        if self._myHasColor:
            leafStr = str(self.color)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myColorRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+Pattern="
        if self._myHasPattern:
            leafStr = str(self.pattern)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myPatternRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

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

        x=""
        x = "+LineWidth="
        if self._myHasLineWidth:
            leafStr = str(self.lineWidth)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myLineWidthRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{DesignOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setColorRequested()
        self.setPatternRequested()
        self.setMacAddressRequested()
        self.setLineWidthRequested()
        
        


    def setColor (self, color):
        self.color = color
        self.setHasColor()

    def setPattern (self, pattern):
        self.pattern = pattern
        self.setHasPattern()

    def setMacAddress (self, macAddress):
        self.macAddress = macAddress
        self.setHasMacAddress()

    def setLineWidth (self, lineWidth):
        self.lineWidth = lineWidth
        self.setHasLineWidth()


"""
Extracted from the below data: 
{
    "node": {
        "className": "DesignOperData", 
        "namespace": "design", 
        "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.design.design_oper_data_gen import DesignOperData"
    }, 
    "ancestors": [
        {
            "namespace": "lake", 
            "isCurrent": false
        }, 
        {
            "namespace": "fish_", 
            "isCurrent": false
        }, 
        {
            "namespace": "design", 
            "isCurrent": true
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "color", 
            "yangName": "color", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "pattern", 
            "yangName": "pattern", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: MacAddressHandlerPy", 
            "memberName": "macAddress", 
            "yangName": "mac-address", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "lineWidth", 
            "yangName": "line-width", 
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


