


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class SitesMaapiBase(object):
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

    # siteList
    def newSiteList (self):
        raise NotImplementedError()

    def setSiteListObj (self, obj):
        raise NotImplementedError()

    def getSiteListObj (self):
        raise NotImplementedError()

    def hasSiteList (self):
        raise NotImplementedError()








"""
Extracted from the below data: 
{
    "node": {
        "name": "sites", 
        "namespace": "sites", 
        "className": "SitesMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.signatures.sites.sites_maapi_gen import SitesMaapi", 
        "baseClassName": "SitesMaapiBase", 
        "baseModule": "sites_maapi_base_gen"
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
            "yangName": "signatures", 
            "namespace": "signatures", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "name": "signatures"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "yangName": "sites", 
            "namespace": "sites", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "name": "sites"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qtc", 
            "memberName": "siteList", 
            "yangName": "site", 
            "className": "BlinkySiteMaapiList", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.signatures.sites.site.site_maapi_list_gen import BlinkySiteMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"
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
            "qwilt_tech_content"
        ]
    }, 
    "leaves": [], 
    "createTime": "2013"
}
"""


