


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class ActionsMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , rule
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , rule
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , rule
                       
                       , trxContext=None):
        raise NotImplementedError()



    # descendants

    # action
    def newAction (self):
        raise NotImplementedError()

    def setActionObj (self, obj):
        raise NotImplementedError()

    def getActionObj (self):
        raise NotImplementedError()

    def hasAction (self):
        raise NotImplementedError()




    # config leaves

    # ignore
    def requestIgnore (self, requested):
        raise NotImplementedError()

    def isIgnoreRequested (self):
        raise NotImplementedError()

    def getIgnore (self):
        raise NotImplementedError()

    def hasIgnore (self):
        raise NotImplementedError()

    def setIgnore (self, ignore):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "actions", 
        "namespace": "actions", 
        "className": "ActionsMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.policy.rules.rule.actions.actions_maapi_gen import ActionsMaapi", 
        "baseClassName": "ActionsMaapiBase", 
        "baseModule": "actions_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qtc", 
            "yangName": "policy", 
            "namespace": "policy", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "name": "policy"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "yangName": "rules", 
            "namespace": "rules", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "name": "rules"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "isCurrent": false, 
            "yangName": "rule", 
            "namespace": "rule", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "keyLeaf": {
                "varName": "rule", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "rule"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "yangName": "actions", 
            "namespace": "actions", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "name": "actions"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qtc", 
            "memberName": "action", 
            "yangName": "action", 
            "className": "BlinkyActionMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.policy.rules.rule.actions.action.action_maapi_gen import BlinkyActionMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "ignore", 
            "yangName": "ignore", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }
    ], 
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "content", 
            "qwilt_tech_content"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "ignore", 
            "yangName": "ignore", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


