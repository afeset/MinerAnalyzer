


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket

from a.api.yang.modules.tech.common.qwilt_tech_types.qwilt_tech_types_module_gen import DecisionType
from a.api.yang.modules.tech.content.qwilt_tech_content_line_types.qwilt_tech_content_line_types_module_gen import AcquisitionAlgorithmType


class LineData(object):

    def __init__ (self):

        self.description = ""
        self._myHasDescription=False
        
        self.tempJunkThreadPriority2 = ""
        self._myHasTempJunkThreadPriority2=False
        
        self.tempJunkAcquisitionAlgorithm = AcquisitionAlgorithmType.kFirstHit
        self._myHasTempJunkAcquisitionAlgorithm=False
        
        self.tempJunkDecision2 = DecisionType.kTrue
        self._myHasTempJunkDecision2=False
        
        self.tempJunkDecision = DecisionType.kTrue
        self._myHasTempJunkDecision=False
        
        self.number = ""
        self._myHasNumber=False
        
        self.tempJunkThreadPriority = ""
        self._myHasTempJunkThreadPriority=False
        
        self.tempJunkAcquisitionAlgorithm2 = AcquisitionAlgorithmType.kFirstHit
        self._myHasTempJunkAcquisitionAlgorithm2=False
        

    def copyFrom (self, other):

        self.description=other.description
        self._myHasDescription=other._myHasDescription
        
        self.tempJunkThreadPriority2=other.tempJunkThreadPriority2
        self._myHasTempJunkThreadPriority2=other._myHasTempJunkThreadPriority2
        
        self.tempJunkAcquisitionAlgorithm=other.tempJunkAcquisitionAlgorithm
        self._myHasTempJunkAcquisitionAlgorithm=other._myHasTempJunkAcquisitionAlgorithm
        
        self.tempJunkDecision2=other.tempJunkDecision2
        self._myHasTempJunkDecision2=other._myHasTempJunkDecision2
        
        self.tempJunkDecision=other.tempJunkDecision
        self._myHasTempJunkDecision=other._myHasTempJunkDecision
        
        self.number=other.number
        self._myHasNumber=other._myHasNumber
        
        self.tempJunkThreadPriority=other.tempJunkThreadPriority
        self._myHasTempJunkThreadPriority=other._myHasTempJunkThreadPriority
        
        self.tempJunkAcquisitionAlgorithm2=other.tempJunkAcquisitionAlgorithm2
        self._myHasTempJunkAcquisitionAlgorithm2=other._myHasTempJunkAcquisitionAlgorithm2
        
    # has...() methods

    def hasDescription (self):
        return self._myHasDescription

    def hasTempJunkThreadPriority2 (self):
        return self._myHasTempJunkThreadPriority2

    def hasTempJunkAcquisitionAlgorithm (self):
        return self._myHasTempJunkAcquisitionAlgorithm

    def hasTempJunkDecision2 (self):
        return self._myHasTempJunkDecision2

    def hasTempJunkDecision (self):
        return self._myHasTempJunkDecision

    def hasNumber (self):
        return self._myHasNumber

    def hasTempJunkThreadPriority (self):
        return self._myHasTempJunkThreadPriority

    def hasTempJunkAcquisitionAlgorithm2 (self):
        return self._myHasTempJunkAcquisitionAlgorithm2


    # setHas...() methods

    def setHasDescription (self):
        self._myHasDescription=True

    def setHasTempJunkThreadPriority2 (self):
        self._myHasTempJunkThreadPriority2=True

    def setHasTempJunkAcquisitionAlgorithm (self):
        self._myHasTempJunkAcquisitionAlgorithm=True

    def setHasTempJunkDecision2 (self):
        self._myHasTempJunkDecision2=True

    def setHasTempJunkDecision (self):
        self._myHasTempJunkDecision=True

    def setHasNumber (self):
        self._myHasNumber=True

    def setHasTempJunkThreadPriority (self):
        self._myHasTempJunkThreadPriority=True

    def setHasTempJunkAcquisitionAlgorithm2 (self):
        self._myHasTempJunkAcquisitionAlgorithm2=True


    def clearAllHas (self):

        self._myHasDescription=False

        self._myHasTempJunkThreadPriority2=False

        self._myHasTempJunkAcquisitionAlgorithm=False

        self._myHasTempJunkDecision2=False

        self._myHasTempJunkDecision=False

        self._myHasNumber=False

        self._myHasTempJunkThreadPriority=False

        self._myHasTempJunkAcquisitionAlgorithm2=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasDescription:
            x = "+"
        leafStr = str(self.description)
        items.append(x + "Description="+leafStr)

        x=""
        if self._myHasTempJunkThreadPriority2:
            x = "+"
        leafStr = str(self.tempJunkThreadPriority2)
        items.append(x + "TempJunkThreadPriority2="+leafStr)

        x=""
        if self._myHasTempJunkAcquisitionAlgorithm:
            x = "+"
        leafStr = str(self.tempJunkAcquisitionAlgorithm)
        items.append(x + "TempJunkAcquisitionAlgorithm="+leafStr)

        x=""
        if self._myHasTempJunkDecision2:
            x = "+"
        leafStr = str(self.tempJunkDecision2)
        items.append(x + "TempJunkDecision2="+leafStr)

        x=""
        if self._myHasTempJunkDecision:
            x = "+"
        leafStr = str(self.tempJunkDecision)
        items.append(x + "TempJunkDecision="+leafStr)

        x=""
        if self._myHasNumber:
            x = "+"
        leafStr = str(self.number)
        items.append(x + "Number="+leafStr)

        x=""
        if self._myHasTempJunkThreadPriority:
            x = "+"
        leafStr = str(self.tempJunkThreadPriority)
        items.append(x + "TempJunkThreadPriority="+leafStr)

        x=""
        if self._myHasTempJunkAcquisitionAlgorithm2:
            x = "+"
        leafStr = str(self.tempJunkAcquisitionAlgorithm2)
        items.append(x + "TempJunkAcquisitionAlgorithm2="+leafStr)

        return "{LineData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "LineData", 
        "namespace": "line", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.line_data_gen import LineData"
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
            "namespace": "line", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "tempJunkThreadPriority2", 
            "yangName": "temp-junk-thread-priority-2", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "tempJunkAcquisitionAlgorithm", 
            "yangName": "temp-junk-acquisition-algorithm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "tempJunkDecision2", 
            "yangName": "temp-junk-decision-2", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "tempJunkDecision", 
            "yangName": "temp-junk-decision", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "number", 
            "yangName": "number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "tempJunkThreadPriority", 
            "yangName": "temp-junk-thread-priority", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "tempJunkAcquisitionAlgorithm2", 
            "yangName": "temp-junk-acquisition-algorithm-2", 
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
            "qwilt_tech_content_line"
        ]
    }, 
    "createTime": "2013"
}
"""


