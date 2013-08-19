


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class SchoolMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       
                       , trxContext=None):
        raise NotImplementedError()



    # descendants

    # personList
    def newPersonList (self):
        raise NotImplementedError()

    def setPersonListObj (self, obj):
        raise NotImplementedError()

    def getPersonListObj (self):
        raise NotImplementedError()

    def hasPersonList (self):
        raise NotImplementedError()




    # config leaves

    # bestStudent
    def requestBestStudent (self, requested):
        raise NotImplementedError()

    def isBestStudentRequested (self):
        raise NotImplementedError()

    def getBestStudent (self):
        raise NotImplementedError()

    def hasBestStudent (self):
        raise NotImplementedError()

    def setBestStudent (self, bestStudent):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "school", 
        "namespace": "school", 
        "className": "SchoolMaapi", 
        "importStatement": "from a.sys.blinky.example.ut.school_example.school.school_maapi_gen import SchoolMaapi", 
        "baseClassName": "SchoolMaapiBase", 
        "baseModule": "school_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "sche", 
            "yangName": "school", 
            "namespace": "school", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/school-example", 
            "name": "school"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "sche", 
            "memberName": "personList", 
            "yangName": "people", 
            "className": "BlinkyPersonMaapiList", 
            "importStatement": "from a.sys.blinky.example.ut.school_example.school.person.person_maapi_list_gen import BlinkyPersonMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/school-example"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/school-example", 
            "moduleYangNamespacePrefix": "sche", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "bestStudent", 
            "yangName": "best-student", 
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
            "ut", 
            "school_example"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/school-example", 
            "moduleYangNamespacePrefix": "sche", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "bestStudent", 
            "yangName": "best-student", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


