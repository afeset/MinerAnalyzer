


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class DispatcherMaapiBase(object):
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

    # queueGroupList
    def newQueueGroupList (self):
        raise NotImplementedError()

    def setQueueGroupListObj (self, obj):
        raise NotImplementedError()

    def getQueueGroupListObj (self):
        raise NotImplementedError()

    def hasQueueGroupList (self):
        raise NotImplementedError()

    # interfaceList
    def newInterfaceList (self):
        raise NotImplementedError()

    def setInterfaceListObj (self, obj):
        raise NotImplementedError()

    def getInterfaceListObj (self):
        raise NotImplementedError()

    def hasInterfaceList (self):
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

    # dpdk
    def newDpdk (self):
        raise NotImplementedError()

    def setDpdkObj (self, obj):
        raise NotImplementedError()

    def getDpdkObj (self):
        raise NotImplementedError()

    def hasDpdk (self):
        raise NotImplementedError()








"""
Extracted from the below data: 
{
    "node": {
        "name": "dispatcher", 
        "namespace": "dispatcher", 
        "className": "DispatcherMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.dispatcher.dispatcher_maapi_gen import DispatcherMaapi", 
        "baseClassName": "DispatcherMaapiBase", 
        "baseModule": "dispatcher_maapi_base_gen"
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
            "yangName": "dispatcher", 
            "namespace": "dispatcher", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "dispatcher"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "memberName": "houseKeeper", 
            "yangName": "house-keeper", 
            "className": "BlinkyHouseKeeperMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.dispatcher.house_keeper.house_keeper_maapi_gen import BlinkyHouseKeeperMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "memberName": "queueGroupList", 
            "yangName": "queue-group", 
            "className": "BlinkyQueueGroupMaapiList", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.dispatcher.queue_group.queue_group_maapi_list_gen import BlinkyQueueGroupMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "memberName": "interfaceList", 
            "yangName": "interface", 
            "className": "BlinkyInterfaceMaapiList", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.dispatcher.interface.interface_maapi_list_gen import BlinkyInterfaceMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "memberName": "unitList", 
            "yangName": "unit", 
            "className": "BlinkyUnitMaapiList", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.dispatcher.unit.unit_maapi_list_gen import BlinkyUnitMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "memberName": "dpdk", 
            "yangName": "dpdk", 
            "className": "BlinkyDpdkMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.dispatcher.dpdk.dpdk_maapi_gen import BlinkyDpdkMaapi", 
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


