


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class LineMaapiBase(object):
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

    # analyzer
    def newAnalyzer (self):
        raise NotImplementedError()

    def setAnalyzerObj (self, obj):
        raise NotImplementedError()

    def getAnalyzerObj (self):
        raise NotImplementedError()

    def hasAnalyzer (self):
        raise NotImplementedError()

    # qShell
    def newQShell (self):
        raise NotImplementedError()

    def setQShellObj (self, obj):
        raise NotImplementedError()

    def getQShellObj (self):
        raise NotImplementedError()

    def hasQShell (self):
        raise NotImplementedError()

    # systemDefaults
    def newSystemDefaults (self):
        raise NotImplementedError()

    def setSystemDefaultsObj (self, obj):
        raise NotImplementedError()

    def getSystemDefaultsObj (self):
        raise NotImplementedError()

    def hasSystemDefaults (self):
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




    # config leaves

    # description
    def requestDescription (self, requested):
        raise NotImplementedError()

    def isDescriptionRequested (self):
        raise NotImplementedError()

    def getDescription (self):
        raise NotImplementedError()

    def hasDescription (self):
        raise NotImplementedError()

    def setDescription (self, description):
        raise NotImplementedError()

    # tempJunkThreadPriority2
    def requestTempJunkThreadPriority2 (self, requested):
        raise NotImplementedError()

    def isTempJunkThreadPriority2Requested (self):
        raise NotImplementedError()

    def getTempJunkThreadPriority2 (self):
        raise NotImplementedError()

    def hasTempJunkThreadPriority2 (self):
        raise NotImplementedError()

    def setTempJunkThreadPriority2 (self, tempJunkThreadPriority2):
        raise NotImplementedError()

    # tempJunkAcquisitionAlgorithm
    def requestTempJunkAcquisitionAlgorithm (self, requested):
        raise NotImplementedError()

    def isTempJunkAcquisitionAlgorithmRequested (self):
        raise NotImplementedError()

    def getTempJunkAcquisitionAlgorithm (self):
        raise NotImplementedError()

    def hasTempJunkAcquisitionAlgorithm (self):
        raise NotImplementedError()

    def setTempJunkAcquisitionAlgorithm (self, tempJunkAcquisitionAlgorithm):
        raise NotImplementedError()

    # tempJunkDecision2
    def requestTempJunkDecision2 (self, requested):
        raise NotImplementedError()

    def isTempJunkDecision2Requested (self):
        raise NotImplementedError()

    def getTempJunkDecision2 (self):
        raise NotImplementedError()

    def hasTempJunkDecision2 (self):
        raise NotImplementedError()

    def setTempJunkDecision2 (self, tempJunkDecision2):
        raise NotImplementedError()

    # tempJunkDecision
    def requestTempJunkDecision (self, requested):
        raise NotImplementedError()

    def isTempJunkDecisionRequested (self):
        raise NotImplementedError()

    def getTempJunkDecision (self):
        raise NotImplementedError()

    def hasTempJunkDecision (self):
        raise NotImplementedError()

    def setTempJunkDecision (self, tempJunkDecision):
        raise NotImplementedError()

    # number
    def requestNumber (self, requested):
        raise NotImplementedError()

    def isNumberRequested (self):
        raise NotImplementedError()

    def getNumber (self):
        raise NotImplementedError()

    def hasNumber (self):
        raise NotImplementedError()

    def setNumber (self, number):
        raise NotImplementedError()

    # tempJunkThreadPriority
    def requestTempJunkThreadPriority (self, requested):
        raise NotImplementedError()

    def isTempJunkThreadPriorityRequested (self):
        raise NotImplementedError()

    def getTempJunkThreadPriority (self):
        raise NotImplementedError()

    def hasTempJunkThreadPriority (self):
        raise NotImplementedError()

    def setTempJunkThreadPriority (self, tempJunkThreadPriority):
        raise NotImplementedError()

    # tempJunkAcquisitionAlgorithm2
    def requestTempJunkAcquisitionAlgorithm2 (self, requested):
        raise NotImplementedError()

    def isTempJunkAcquisitionAlgorithm2Requested (self):
        raise NotImplementedError()

    def getTempJunkAcquisitionAlgorithm2 (self):
        raise NotImplementedError()

    def hasTempJunkAcquisitionAlgorithm2 (self):
        raise NotImplementedError()

    def setTempJunkAcquisitionAlgorithm2 (self, tempJunkAcquisitionAlgorithm2):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "line", 
        "namespace": "line", 
        "className": "LineMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.line_maapi_gen import LineMaapi", 
        "baseClassName": "LineMaapiBase", 
        "baseModule": "line_maapi_base_gen"
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
            "isCurrent": true, 
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
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "memberName": "analyzer", 
            "yangName": "analyzer", 
            "className": "BlinkyAnalyzerMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.analyzer.analyzer_maapi_gen import BlinkyAnalyzerMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "memberName": "qShell", 
            "yangName": "q-shell", 
            "className": "BlinkyQShellMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.q_shell.q_shell_maapi_gen import BlinkyQShellMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "memberName": "systemDefaults", 
            "yangName": "system-defaults", 
            "className": "BlinkySystemDefaultsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.system_defaults.system_defaults_maapi_gen import BlinkySystemDefaultsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "memberName": "dispatcher", 
            "yangName": "dispatcher", 
            "className": "BlinkyDispatcherMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.dispatcher.dispatcher_maapi_gen import BlinkyDispatcherMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "tempJunkThreadPriority2", 
            "yangName": "temp-junk-thread-priority-2", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "tempJunkAcquisitionAlgorithm", 
            "yangName": "temp-junk-acquisition-algorithm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "tempJunkDecision2", 
            "yangName": "temp-junk-decision-2", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "tempJunkDecision", 
            "yangName": "temp-junk-decision", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "number", 
            "yangName": "number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "tempJunkThreadPriority", 
            "yangName": "temp-junk-thread-priority", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "tempJunkAcquisitionAlgorithm2", 
            "yangName": "temp-junk-acquisition-algorithm-2", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
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
            "qwilt_tech_content_line"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "tempJunkThreadPriority2", 
            "yangName": "temp-junk-thread-priority-2", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "tempJunkAcquisitionAlgorithm", 
            "yangName": "temp-junk-acquisition-algorithm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "tempJunkDecision2", 
            "yangName": "temp-junk-decision-2", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "tempJunkDecision", 
            "yangName": "temp-junk-decision", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "number", 
            "yangName": "number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "tempJunkThreadPriority", 
            "yangName": "temp-junk-thread-priority", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "tempJunkAcquisitionAlgorithm2", 
            "yangName": "temp-junk-acquisition-algorithm-2", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


