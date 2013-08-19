


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class PreTopperMaapiBase(object):
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

    # instancesList
    def newInstancesList (self):
        raise NotImplementedError()

    def setInstancesListObj (self, obj):
        raise NotImplementedError()

    def getInstancesListObj (self):
        raise NotImplementedError()

    def hasInstancesList (self):
        raise NotImplementedError()








"""
Extracted from the below data: 
{
    "node": {
        "name": "preTopper", 
        "namespace": "pre_topper", 
        "className": "PreTopperMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_pre_topper.tech.content.pre_topper.pre_topper_maapi_gen import PreTopperMaapi", 
        "baseClassName": "PreTopperMaapiBase", 
        "baseModule": "pre_topper_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "qt", 
            "yangName": "tech", 
            "namespace": "tech", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech", 
            "name": "tech"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "yangName": "content", 
            "namespace": "content", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "name": "content"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-pt", 
            "yangName": "pre-topper", 
            "namespace": "pre_topper", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "name": "pre-topper"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qtc-pt", 
            "memberName": "instancesList", 
            "yangName": "instances", 
            "className": "BlinkyInstancesMaapiList", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_pre_topper.tech.content.pre_topper.instances.instances_maapi_list_gen import BlinkyInstancesMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [], 
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "content", 
            "qwilt_tech_content_pre_topper"
        ]
    }, 
    "leaves": [], 
    "createTime": "2013"
}
"""


