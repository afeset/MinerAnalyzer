


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class OpBMaapiBase(object):
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

    # opCList
    def newOpCList (self):
        raise NotImplementedError()

    def setOpCListObj (self, obj):
        raise NotImplementedError()

    def getOpCListObj (self):
        raise NotImplementedError()

    def hasOpCList (self):
        raise NotImplementedError()

    # opD
    def newOpD (self):
        raise NotImplementedError()

    def setOpDObj (self, obj):
        raise NotImplementedError()

    def getOpDObj (self):
        raise NotImplementedError()

    def hasOpD (self):
        raise NotImplementedError()






    # oper leaves

    # opValueB
    def requestOpValueB (self, requested):
        raise NotImplementedError()

    def isOpValueBRequested (self):
        raise NotImplementedError()

    def getOpValueB (self):
        raise NotImplementedError()

    def hasOpValueB (self):
        raise NotImplementedError()

    def setOpValueB (self, opValueB):
        raise NotImplementedError()




"""
Extracted from the below data: 
{
    "node": {
        "name": "opB", 
        "namespace": "op_b", 
        "className": "OpBMaapi", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_b.op_b_maapi_gen import OpBMaapi", 
        "baseClassName": "OpBMaapiBase", 
        "baseModule": "op_b_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "oper", 
            "yangName": "config-a", 
            "namespace": "config_a", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "name": "config-a"
        }, 
        {
            "moduleYangNamespacePrefix": "oper", 
            "yangName": "op-b", 
            "namespace": "op_b", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "name": "op-b"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "oper", 
            "memberName": "opCList", 
            "yangName": "op-c", 
            "className": "BlinkyOpCMaapiList", 
            "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_b.op_c.op_c_maapi_list_gen import BlinkyOpCMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/oper"
        }, 
        {
            "moduleYangNamespacePrefix": "oper", 
            "memberName": "opD", 
            "yangName": "op-d", 
            "className": "BlinkyOpDMaapi", 
            "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_b.op_d.op_d_maapi_gen import BlinkyOpDMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/oper"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "opValueB", 
            "yangName": "op-value-b", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "module": {}, 
    "configLeaves": [], 
    "env": {
        "namespaces": [
            "a", 
            "sys", 
            "blinky", 
            "example", 
            "oper", 
            "oper"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "opValueB", 
            "yangName": "op-value-b", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


