


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class AnalyzerMaapiBase(object):
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

    # houseKeeper
    def newHouseKeeper (self):
        raise NotImplementedError()

    def setHouseKeeperObj (self, obj):
        raise NotImplementedError()

    def getHouseKeeperObj (self):
        raise NotImplementedError()

    def hasHouseKeeper (self):
        raise NotImplementedError()

    # prediction
    def newPrediction (self):
        raise NotImplementedError()

    def setPredictionObj (self, obj):
        raise NotImplementedError()

    def getPredictionObj (self):
        raise NotImplementedError()

    def hasPrediction (self):
        raise NotImplementedError()

    # delivery
    def newDelivery (self):
        raise NotImplementedError()

    def setDeliveryObj (self, obj):
        raise NotImplementedError()

    def getDeliveryObj (self):
        raise NotImplementedError()

    def hasDelivery (self):
        raise NotImplementedError()

    # potential
    def newPotential (self):
        raise NotImplementedError()

    def setPotentialObj (self, obj):
        raise NotImplementedError()

    def getPotentialObj (self):
        raise NotImplementedError()

    def hasPotential (self):
        raise NotImplementedError()

    # unitList
    def newUnitList (self):
        raise NotImplementedError()

    def setUnitListObj (self, obj):
        raise NotImplementedError()

    def getUnitListObj (self):
        raise NotImplementedError()

    def hasUnitList (self):
        raise NotImplementedError()

    # policy
    def newPolicy (self):
        raise NotImplementedError()

    def setPolicyObj (self, obj):
        raise NotImplementedError()

    def getPolicyObj (self):
        raise NotImplementedError()

    def hasPolicy (self):
        raise NotImplementedError()

    # acquisition
    def newAcquisition (self):
        raise NotImplementedError()

    def setAcquisitionObj (self, obj):
        raise NotImplementedError()

    def getAcquisitionObj (self):
        raise NotImplementedError()

    def hasAcquisition (self):
        raise NotImplementedError()








"""
Extracted from the below data: 
{
    "node": {
        "name": "analyzer", 
        "namespace": "analyzer", 
        "className": "AnalyzerMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.analyzer.analyzer_maapi_gen import AnalyzerMaapi", 
        "baseClassName": "AnalyzerMaapiBase", 
        "baseModule": "analyzer_maapi_base_gen"
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
            "yangName": "analyzer", 
            "namespace": "analyzer", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "analyzer"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "memberName": "houseKeeper", 
            "yangName": "house-keeper", 
            "className": "BlinkyHouseKeeperMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.analyzer.house_keeper.house_keeper_maapi_gen import BlinkyHouseKeeperMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "memberName": "prediction", 
            "yangName": "prediction", 
            "className": "BlinkyPredictionMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.analyzer.prediction.prediction_maapi_gen import BlinkyPredictionMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "memberName": "delivery", 
            "yangName": "delivery", 
            "className": "BlinkyDeliveryMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.analyzer.delivery.delivery_maapi_gen import BlinkyDeliveryMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "memberName": "potential", 
            "yangName": "potential", 
            "className": "BlinkyPotentialMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.analyzer.potential.potential_maapi_gen import BlinkyPotentialMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "memberName": "unitList", 
            "yangName": "unit", 
            "className": "BlinkyUnitMaapiList", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.analyzer.unit.unit_maapi_list_gen import BlinkyUnitMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "memberName": "policy", 
            "yangName": "policy", 
            "className": "BlinkyPolicyMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.analyzer.policy.policy_maapi_gen import BlinkyPolicyMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "memberName": "acquisition", 
            "yangName": "acquisition", 
            "className": "BlinkyAcquisitionMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.analyzer.acquisition.acquisition_maapi_gen import BlinkyAcquisitionMaapi", 
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


