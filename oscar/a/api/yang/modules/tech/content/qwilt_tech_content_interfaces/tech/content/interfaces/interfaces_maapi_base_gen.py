


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class InterfacesMaapiBase(object):
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

    # interfaceList
    def newInterfaceList (self):
        raise NotImplementedError()

    def setInterfaceListObj (self, obj):
        raise NotImplementedError()

    def getInterfaceListObj (self):
        raise NotImplementedError()

    def hasInterfaceList (self):
        raise NotImplementedError()








"""
Extracted from the below data: 
{
    "node": {
        "name": "interfaces", 
        "namespace": "interfaces", 
        "className": "InterfacesMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_interfaces.tech.content.interfaces.interfaces_maapi_gen import InterfacesMaapi", 
        "baseClassName": "InterfacesMaapiBase", 
        "baseModule": "interfaces_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qtc-if", 
            "yangName": "interfaces", 
            "namespace": "interfaces", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-interfaces", 
            "name": "interfaces"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qtc-if", 
            "memberName": "interfaceList", 
            "yangName": "interface", 
            "className": "BlinkyInterfaceMaapiList", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_interfaces.tech.content.interfaces.interface.interface_maapi_list_gen import BlinkyInterfaceMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-interfaces"
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
            "qwilt_tech_content_interfaces"
        ]
    }, 
    "leaves": [], 
    "createTime": "2013"
}
"""


