


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class ReportingMaapiBase(object):
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

    # export_List
    def newExport_List (self):
        raise NotImplementedError()

    def setExport_ListObj (self, obj):
        raise NotImplementedError()

    def getExport_ListObj (self):
        raise NotImplementedError()

    def hasExport_List (self):
        raise NotImplementedError()








"""
Extracted from the below data: 
{
    "node": {
        "name": "reporting", 
        "namespace": "reporting", 
        "className": "ReportingMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_reporting.tech.content.reporting.reporting_maapi_gen import ReportingMaapi", 
        "baseClassName": "ReportingMaapiBase", 
        "baseModule": "reporting_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qtc-report", 
            "yangName": "reporting", 
            "namespace": "reporting", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "name": "reporting"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qtc-report", 
            "memberName": "export_List", 
            "yangName": "export", 
            "className": "BlinkyExportMaapiList", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_reporting.tech.content.reporting.export_.export__maapi_list_gen import BlinkyExportMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting"
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
            "qwilt_tech_content_reporting"
        ]
    }, 
    "leaves": [], 
    "createTime": "2013"
}
"""


