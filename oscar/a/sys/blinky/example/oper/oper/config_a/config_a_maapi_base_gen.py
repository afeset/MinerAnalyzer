


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class ConfigAMaapiBase(object):
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

    # opN
    def newOpN (self):
        raise NotImplementedError()

    def setOpNObj (self, obj):
        raise NotImplementedError()

    def getOpNObj (self):
        raise NotImplementedError()

    def hasOpN (self):
        raise NotImplementedError()

    # opL
    def newOpL (self):
        raise NotImplementedError()

    def setOpLObj (self, obj):
        raise NotImplementedError()

    def getOpLObj (self):
        raise NotImplementedError()

    def hasOpL (self):
        raise NotImplementedError()

    # opM
    def newOpM (self):
        raise NotImplementedError()

    def setOpMObj (self, obj):
        raise NotImplementedError()

    def getOpMObj (self):
        raise NotImplementedError()

    def hasOpM (self):
        raise NotImplementedError()

    # opB
    def newOpB (self):
        raise NotImplementedError()

    def setOpBObj (self, obj):
        raise NotImplementedError()

    def getOpBObj (self):
        raise NotImplementedError()

    def hasOpB (self):
        raise NotImplementedError()

    # configQ
    def newConfigQ (self):
        raise NotImplementedError()

    def setConfigQObj (self, obj):
        raise NotImplementedError()

    def getConfigQObj (self):
        raise NotImplementedError()

    def hasConfigQ (self):
        raise NotImplementedError()

    # configPList
    def newConfigPList (self):
        raise NotImplementedError()

    def setConfigPListObj (self, obj):
        raise NotImplementedError()

    def getConfigPListObj (self):
        raise NotImplementedError()

    def hasConfigPList (self):
        raise NotImplementedError()

    # configUList
    def newConfigUList (self):
        raise NotImplementedError()

    def setConfigUListObj (self, obj):
        raise NotImplementedError()

    def getConfigUListObj (self):
        raise NotImplementedError()

    def hasConfigUList (self):
        raise NotImplementedError()

    # opVList
    def newOpVList (self):
        raise NotImplementedError()

    def setOpVListObj (self, obj):
        raise NotImplementedError()

    def getOpVListObj (self):
        raise NotImplementedError()

    def hasOpVList (self):
        raise NotImplementedError()






    # oper leaves

    # opZ
    def requestOpZ (self, requested):
        raise NotImplementedError()

    def isOpZRequested (self):
        raise NotImplementedError()

    def getOpZ (self):
        raise NotImplementedError()

    def hasOpZ (self):
        raise NotImplementedError()

    def setOpZ (self, opZ):
        raise NotImplementedError()

    # opY
    def requestOpY (self, requested):
        raise NotImplementedError()

    def isOpYRequested (self):
        raise NotImplementedError()

    def getOpY (self):
        raise NotImplementedError()

    def hasOpY (self):
        raise NotImplementedError()

    def setOpY (self, opY):
        raise NotImplementedError()




"""
Extracted from the below data: 
{
    "node": {
        "name": "configA", 
        "namespace": "config_a", 
        "className": "ConfigAMaapi", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.config_a_maapi_gen import ConfigAMaapi", 
        "baseClassName": "ConfigAMaapiBase", 
        "baseModule": "config_a_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "oper", 
            "yangName": "config-a", 
            "namespace": "config_a", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "name": "config-a"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "oper", 
            "memberName": "opN", 
            "yangName": "op-n", 
            "className": "BlinkyOpNMaapi", 
            "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_n.op_n_maapi_gen import BlinkyOpNMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/oper"
        }, 
        {
            "moduleYangNamespacePrefix": "oper", 
            "memberName": "opL", 
            "yangName": "op-l", 
            "className": "BlinkyOpLMaapi", 
            "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_l.op_l_maapi_gen import BlinkyOpLMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/oper"
        }, 
        {
            "moduleYangNamespacePrefix": "oper", 
            "memberName": "opM", 
            "yangName": "op-m", 
            "className": "BlinkyOpMMaapi", 
            "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_m.op_m_maapi_gen import BlinkyOpMMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/oper"
        }, 
        {
            "moduleYangNamespacePrefix": "oper", 
            "memberName": "opB", 
            "yangName": "op-b", 
            "className": "BlinkyOpBMaapi", 
            "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_b.op_b_maapi_gen import BlinkyOpBMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/oper"
        }, 
        {
            "moduleYangNamespacePrefix": "oper", 
            "memberName": "configQ", 
            "yangName": "config-q", 
            "className": "BlinkyConfigQMaapi", 
            "importStatement": "from a.sys.blinky.example.oper.oper.config_a.config_q.config_q_maapi_gen import BlinkyConfigQMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/oper"
        }, 
        {
            "moduleYangNamespacePrefix": "oper", 
            "memberName": "configPList", 
            "yangName": "config-p", 
            "className": "BlinkyConfigPMaapiList", 
            "importStatement": "from a.sys.blinky.example.oper.oper.config_a.config_p.config_p_maapi_list_gen import BlinkyConfigPMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/oper"
        }, 
        {
            "moduleYangNamespacePrefix": "oper", 
            "memberName": "configUList", 
            "yangName": "config-u", 
            "className": "BlinkyConfigUMaapiList", 
            "importStatement": "from a.sys.blinky.example.oper.oper.config_a.config_u.config_u_maapi_list_gen import BlinkyConfigUMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/oper"
        }, 
        {
            "moduleYangNamespacePrefix": "oper", 
            "memberName": "opVList", 
            "yangName": "op-v", 
            "className": "BlinkyOpVMaapiList", 
            "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_v.op_v_maapi_list_gen import BlinkyOpVMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/oper"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "opZ", 
            "yangName": "op-z", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "opY", 
            "yangName": "op-y", 
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
            "memberName": "opZ", 
            "yangName": "op-z", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "opY", 
            "yangName": "op-y", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


