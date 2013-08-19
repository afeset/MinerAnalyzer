


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class FishMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , lake
              , fish_
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , lake
              , fish_
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , lake
                       , fish_
                       
                       , trxContext=None):
        raise NotImplementedError()



    # descendants

    # mood
    def newMood (self):
        raise NotImplementedError()

    def setMoodObj (self, obj):
        raise NotImplementedError()

    def getMoodObj (self):
        raise NotImplementedError()

    def hasMood (self):
        raise NotImplementedError()

    # antenna
    def newAntenna (self):
        raise NotImplementedError()

    def setAntennaObj (self, obj):
        raise NotImplementedError()

    def getAntennaObj (self):
        raise NotImplementedError()

    def hasAntenna (self):
        raise NotImplementedError()

    # testGenerationUnderscoreList
    def newTestGenerationUnderscoreList (self):
        raise NotImplementedError()

    def setTestGenerationUnderscoreListObj (self, obj):
        raise NotImplementedError()

    def getTestGenerationUnderscoreListObj (self):
        raise NotImplementedError()

    def hasTestGenerationUnderscoreList (self):
        raise NotImplementedError()

    # design
    def newDesign (self):
        raise NotImplementedError()

    def setDesignObj (self, obj):
        raise NotImplementedError()

    def getDesignObj (self):
        raise NotImplementedError()

    def hasDesign (self):
        raise NotImplementedError()

    # transparentContainer
    def newTransparentContainer (self):
        raise NotImplementedError()

    def setTransparentContainerObj (self, obj):
        raise NotImplementedError()

    def getTransparentContainerObj (self):
        raise NotImplementedError()

    def hasTransparentContainer (self):
        raise NotImplementedError()




    # config leaves

    # transparentField
    def requestTransparentField (self, requested):
        raise NotImplementedError()

    def isTransparentFieldRequested (self):
        raise NotImplementedError()

    def getTransparentField (self):
        raise NotImplementedError()

    def hasTransparentField (self):
        raise NotImplementedError()

    def setTransparentField (self, transparentField):
        raise NotImplementedError()

    # color
    def requestColor (self, requested):
        raise NotImplementedError()

    def isColorRequested (self):
        raise NotImplementedError()

    def getColor (self):
        raise NotImplementedError()

    def hasColor (self):
        raise NotImplementedError()

    def setColor (self, color):
        raise NotImplementedError()

    # eyeNumber
    def requestEyeNumber (self, requested):
        raise NotImplementedError()

    def isEyeNumberRequested (self):
        raise NotImplementedError()

    def getEyeNumber (self):
        raise NotImplementedError()

    def hasEyeNumber (self):
        raise NotImplementedError()

    def setEyeNumber (self, eyeNumber):
        raise NotImplementedError()

    # hasTail
    def requestHasTail (self, requested):
        raise NotImplementedError()

    def isHasTailRequested (self):
        raise NotImplementedError()

    def getHasTail (self):
        raise NotImplementedError()

    def hasHasTail (self):
        raise NotImplementedError()

    def setHasTail (self, hasTail):
        raise NotImplementedError()

    # finNumber
    def requestFinNumber (self, requested):
        raise NotImplementedError()

    def isFinNumberRequested (self):
        raise NotImplementedError()

    def getFinNumber (self):
        raise NotImplementedError()

    def hasFinNumber (self):
        raise NotImplementedError()

    def setFinNumber (self, finNumber):
        raise NotImplementedError()

    # length
    def requestLength (self, requested):
        raise NotImplementedError()

    def isLengthRequested (self):
        raise NotImplementedError()

    def getLength (self):
        raise NotImplementedError()

    def hasLength (self):
        raise NotImplementedError()

    def setLength (self, length):
        raise NotImplementedError()

    # ip6
    def requestIp6 (self, requested):
        raise NotImplementedError()

    def isIp6Requested (self):
        raise NotImplementedError()

    def getIp6 (self):
        raise NotImplementedError()

    def hasIp6 (self):
        raise NotImplementedError()

    def setIp6 (self, ip6):
        raise NotImplementedError()

    # id
    def requestId (self, requested):
        raise NotImplementedError()

    def isIdRequested (self):
        raise NotImplementedError()

    def getId (self):
        raise NotImplementedError()

    def hasId (self):
        raise NotImplementedError()

    def setId (self, id):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "fish_", 
        "namespace": "fish_", 
        "className": "FishMaapi", 
        "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.fish__maapi_gen import FishMaapi", 
        "baseClassName": "FishMaapiBase", 
        "baseModule": "fish__maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "isCurrent": false, 
            "yangName": "lake", 
            "namespace": "lake", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "keyLeaf": {
                "varName": "lake", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "lake"
        }, 
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "isCurrent": true, 
            "yangName": "fish", 
            "namespace": "fish_", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "keyLeaf": {
                "varName": "fish_", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "fish_"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "memberName": "mood", 
            "yangName": "mood", 
            "className": "BlinkyMoodMaapi", 
            "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.mood.mood_maapi_gen import BlinkyMoodMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example"
        }, 
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "memberName": "antenna", 
            "yangName": "antenna", 
            "className": "BlinkyAntennaMaapi", 
            "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.antenna.antenna_maapi_gen import BlinkyAntennaMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example"
        }, 
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "memberName": "testGenerationUnderscoreList", 
            "yangName": "test-generation_underscore", 
            "className": "BlinkyTestGenerationUnderscoreMaapiList", 
            "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.test_generation_underscore.test_generation_underscore_maapi_list_gen import BlinkyTestGenerationUnderscoreMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example"
        }, 
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "memberName": "design", 
            "yangName": "design", 
            "className": "BlinkyDesignMaapi", 
            "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.design.design_maapi_gen import BlinkyDesignMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example"
        }, 
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "memberName": "transparentContainer", 
            "yangName": "transparent-container", 
            "className": "BlinkyTransparentContainerMaapi", 
            "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.transparent_container.transparent_container_maapi_gen import BlinkyTransparentContainerMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "transparentField", 
            "yangName": "transparent-field", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "color", 
            "yangName": "color", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "eyeNumber", 
            "yangName": "eye-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "hasTail", 
            "yangName": "has-tail", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "finNumber", 
            "yangName": "fin-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "length", 
            "yangName": "length", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: Ipv6AddressHandlerPy", 
            "memberName": "ip6", 
            "yangName": "ip6", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "id", 
            "yangName": "id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "env": {
        "namespaces": [
            "a", 
            "sys", 
            "blinky", 
            "example", 
            "lake_example"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "transparentField", 
            "yangName": "transparent-field", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "color", 
            "yangName": "color", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "eyeNumber", 
            "yangName": "eye-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "hasTail", 
            "yangName": "has-tail", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "finNumber", 
            "yangName": "fin-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "length", 
            "yangName": "length", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: Ipv6AddressHandlerPy", 
            "memberName": "ip6", 
            "yangName": "ip6", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "id", 
            "yangName": "id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


