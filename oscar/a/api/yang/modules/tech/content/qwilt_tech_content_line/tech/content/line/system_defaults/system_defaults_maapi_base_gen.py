


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class SystemDefaultsMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , line
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , line
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , line
                       
                       , trxContext=None):
        raise NotImplementedError()



    # descendants

    # qShell
    def newQShell (self):
        raise NotImplementedError()

    def setQShellObj (self, obj):
        raise NotImplementedError()

    def getQShellObj (self):
        raise NotImplementedError()

    def hasQShell (self):
        raise NotImplementedError()

    # dispatcher
    def newDispatcher (self):
        raise NotImplementedError()

    def setDispatcherObj (self, obj):
        raise NotImplementedError()

    def getDispatcherObj (self):
        raise NotImplementedError()

    def hasDispatcher (self):
        raise NotImplementedError()

    # analyzer
    def newAnalyzer (self):
        raise NotImplementedError()

    def setAnalyzerObj (self, obj):
        raise NotImplementedError()

    def getAnalyzerObj (self):
        raise NotImplementedError()

    def hasAnalyzer (self):
        raise NotImplementedError()








"""
Extracted from the below data: 
{
    "node": {
        "name": "systemDefaults", 
        "namespace": "system_defaults", 
        "className": "SystemDefaultsMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.system_defaults.system_defaults_maapi_gen import SystemDefaultsMaapi", 
        "baseClassName": "SystemDefaultsMaapiBase", 
        "baseModule": "system_defaults_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qtc-line", 
            "isCurrent": false, 
            "yangName": "line", 
            "namespace": "line", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "keyLeaf": {
                "varName": "line", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "line"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "system-defaults"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "memberName": "qShell", 
            "yangName": "q-shell", 
            "className": "BlinkyQShellMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.system_defaults.q_shell.q_shell_maapi_gen import BlinkyQShellMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "memberName": "dispatcher", 
            "yangName": "dispatcher", 
            "className": "BlinkyDispatcherMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.system_defaults.dispatcher.dispatcher_maapi_gen import BlinkyDispatcherMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "memberName": "analyzer", 
            "yangName": "analyzer", 
            "className": "BlinkyAnalyzerMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.system_defaults.analyzer.analyzer_maapi_gen import BlinkyAnalyzerMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"
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
            "qwilt_tech_content_line"
        ]
    }, 
    "leaves": [], 
    "createTime": "2013"
}
"""


