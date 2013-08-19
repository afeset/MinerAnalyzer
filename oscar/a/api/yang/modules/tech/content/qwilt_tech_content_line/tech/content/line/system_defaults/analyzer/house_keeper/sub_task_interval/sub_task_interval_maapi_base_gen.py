


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class SubTaskIntervalMaapiBase(object):
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





    # config leaves

    # readRedirectNeighbourTableMsec
    def requestReadRedirectNeighbourTableMsec (self, requested):
        raise NotImplementedError()

    def isReadRedirectNeighbourTableMsecRequested (self):
        raise NotImplementedError()

    def getReadRedirectNeighbourTableMsec (self):
        raise NotImplementedError()

    def hasReadRedirectNeighbourTableMsec (self):
        raise NotImplementedError()

    def setReadRedirectNeighbourTableMsec (self, readRedirectNeighbourTableMsec):
        raise NotImplementedError()

    # triggerTitleTableSaveMsec
    def requestTriggerTitleTableSaveMsec (self, requested):
        raise NotImplementedError()

    def isTriggerTitleTableSaveMsecRequested (self):
        raise NotImplementedError()

    def getTriggerTitleTableSaveMsec (self):
        raise NotImplementedError()

    def hasTriggerTitleTableSaveMsec (self):
        raise NotImplementedError()

    def setTriggerTitleTableSaveMsec (self, triggerTitleTableSaveMsec):
        raise NotImplementedError()

    # readRedirectEnablerMsec
    def requestReadRedirectEnablerMsec (self, requested):
        raise NotImplementedError()

    def isReadRedirectEnablerMsecRequested (self):
        raise NotImplementedError()

    def getReadRedirectEnablerMsec (self):
        raise NotImplementedError()

    def hasReadRedirectEnablerMsec (self):
        raise NotImplementedError()

    def setReadRedirectEnablerMsec (self, readRedirectEnablerMsec):
        raise NotImplementedError()

    # readBrownieQuotaMsec
    def requestReadBrownieQuotaMsec (self, requested):
        raise NotImplementedError()

    def isReadBrownieQuotaMsecRequested (self):
        raise NotImplementedError()

    def getReadBrownieQuotaMsec (self):
        raise NotImplementedError()

    def hasReadBrownieQuotaMsec (self):
        raise NotImplementedError()

    def setReadBrownieQuotaMsec (self, readBrownieQuotaMsec):
        raise NotImplementedError()

    # logDebugStatsMsec
    def requestLogDebugStatsMsec (self, requested):
        raise NotImplementedError()

    def isLogDebugStatsMsecRequested (self):
        raise NotImplementedError()

    def getLogDebugStatsMsec (self):
        raise NotImplementedError()

    def hasLogDebugStatsMsec (self):
        raise NotImplementedError()

    def setLogDebugStatsMsec (self, logDebugStatsMsec):
        raise NotImplementedError()

    # readDeliveryBlockerUpdatesMsec
    def requestReadDeliveryBlockerUpdatesMsec (self, requested):
        raise NotImplementedError()

    def isReadDeliveryBlockerUpdatesMsecRequested (self):
        raise NotImplementedError()

    def getReadDeliveryBlockerUpdatesMsec (self):
        raise NotImplementedError()

    def hasReadDeliveryBlockerUpdatesMsec (self):
        raise NotImplementedError()

    def setReadDeliveryBlockerUpdatesMsec (self, readDeliveryBlockerUpdatesMsec):
        raise NotImplementedError()

    # readExternalStateMsec
    def requestReadExternalStateMsec (self, requested):
        raise NotImplementedError()

    def isReadExternalStateMsecRequested (self):
        raise NotImplementedError()

    def getReadExternalStateMsec (self):
        raise NotImplementedError()

    def hasReadExternalStateMsec (self):
        raise NotImplementedError()

    def setReadExternalStateMsec (self, readExternalStateMsec):
        raise NotImplementedError()

    # writeAcquiredTitlesMsec
    def requestWriteAcquiredTitlesMsec (self, requested):
        raise NotImplementedError()

    def isWriteAcquiredTitlesMsecRequested (self):
        raise NotImplementedError()

    def getWriteAcquiredTitlesMsec (self):
        raise NotImplementedError()

    def hasWriteAcquiredTitlesMsec (self):
        raise NotImplementedError()

    def setWriteAcquiredTitlesMsec (self, writeAcquiredTitlesMsec):
        raise NotImplementedError()

    # readExternalConfigMsec
    def requestReadExternalConfigMsec (self, requested):
        raise NotImplementedError()

    def isReadExternalConfigMsecRequested (self):
        raise NotImplementedError()

    def getReadExternalConfigMsec (self):
        raise NotImplementedError()

    def hasReadExternalConfigMsec (self):
        raise NotImplementedError()

    def setReadExternalConfigMsec (self, readExternalConfigMsec):
        raise NotImplementedError()

    # readDeliveredTitlesMsec
    def requestReadDeliveredTitlesMsec (self, requested):
        raise NotImplementedError()

    def isReadDeliveredTitlesMsecRequested (self):
        raise NotImplementedError()

    def getReadDeliveredTitlesMsec (self):
        raise NotImplementedError()

    def hasReadDeliveredTitlesMsec (self):
        raise NotImplementedError()

    def setReadDeliveredTitlesMsec (self, readDeliveredTitlesMsec):
        raise NotImplementedError()

    # requestNeighbourDiscoveryMsec
    def requestRequestNeighbourDiscoveryMsec (self, requested):
        raise NotImplementedError()

    def isRequestNeighbourDiscoveryMsecRequested (self):
        raise NotImplementedError()

    def getRequestNeighbourDiscoveryMsec (self):
        raise NotImplementedError()

    def hasRequestNeighbourDiscoveryMsec (self):
        raise NotImplementedError()

    def setRequestNeighbourDiscoveryMsec (self, requestNeighbourDiscoveryMsec):
        raise NotImplementedError()

    # updateRedirectQuotaMsec
    def requestUpdateRedirectQuotaMsec (self, requested):
        raise NotImplementedError()

    def isUpdateRedirectQuotaMsecRequested (self):
        raise NotImplementedError()

    def getUpdateRedirectQuotaMsec (self):
        raise NotImplementedError()

    def hasUpdateRedirectQuotaMsec (self):
        raise NotImplementedError()

    def setUpdateRedirectQuotaMsec (self, updateRedirectQuotaMsec):
        raise NotImplementedError()

    # checkContentDisksSizeMsec
    def requestCheckContentDisksSizeMsec (self, requested):
        raise NotImplementedError()

    def isCheckContentDisksSizeMsecRequested (self):
        raise NotImplementedError()

    def getCheckContentDisksSizeMsec (self):
        raise NotImplementedError()

    def hasCheckContentDisksSizeMsec (self):
        raise NotImplementedError()

    def setCheckContentDisksSizeMsec (self, checkContentDisksSizeMsec):
        raise NotImplementedError()

    # sampleCountersMsec
    def requestSampleCountersMsec (self, requested):
        raise NotImplementedError()

    def isSampleCountersMsecRequested (self):
        raise NotImplementedError()

    def getSampleCountersMsec (self):
        raise NotImplementedError()

    def hasSampleCountersMsec (self):
        raise NotImplementedError()

    def setSampleCountersMsec (self, sampleCountersMsec):
        raise NotImplementedError()

    # attenuatePastVolumeMsec
    def requestAttenuatePastVolumeMsec (self, requested):
        raise NotImplementedError()

    def isAttenuatePastVolumeMsecRequested (self):
        raise NotImplementedError()

    def getAttenuatePastVolumeMsec (self):
        raise NotImplementedError()

    def hasAttenuatePastVolumeMsec (self):
        raise NotImplementedError()

    def setAttenuatePastVolumeMsec (self, attenuatePastVolumeMsec):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "subTaskInterval", 
        "namespace": "sub_task_interval", 
        "className": "SubTaskIntervalMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.system_defaults.analyzer.house_keeper.sub_task_interval.sub_task_interval_maapi_gen import SubTaskIntervalMaapi", 
        "baseClassName": "SubTaskIntervalMaapiBase", 
        "baseModule": "sub_task_interval_maapi_base_gen"
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
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "system-defaults"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "yangName": "analyzer", 
            "namespace": "analyzer", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "analyzer"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "yangName": "house-keeper", 
            "namespace": "house_keeper", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "house-keeper"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "yangName": "sub-task-interval", 
            "namespace": "sub_task_interval", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "sub-task-interval"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "readRedirectNeighbourTableMsec", 
            "yangName": "read-redirect-neighbour-table-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "triggerTitleTableSaveMsec", 
            "yangName": "trigger-title-table-save-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "readRedirectEnablerMsec", 
            "yangName": "read-redirect-enabler-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "readBrownieQuotaMsec", 
            "yangName": "read-brownie-quota-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "logDebugStatsMsec", 
            "yangName": "log-debug-stats-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "readDeliveryBlockerUpdatesMsec", 
            "yangName": "read-delivery-blocker-updates-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "readExternalStateMsec", 
            "yangName": "read-external-state-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "writeAcquiredTitlesMsec", 
            "yangName": "write-acquired-titles-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "readExternalConfigMsec", 
            "yangName": "read-external-config-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "readDeliveredTitlesMsec", 
            "yangName": "read-delivered-titles-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "requestNeighbourDiscoveryMsec", 
            "yangName": "request-neighbour-discovery-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "updateRedirectQuotaMsec", 
            "yangName": "update-redirect-quota-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "checkContentDisksSizeMsec", 
            "yangName": "check-content-disks-size-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "sampleCountersMsec", 
            "yangName": "sample-counters-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "attenuatePastVolumeMsec", 
            "yangName": "attenuate-past-volume-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
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
            "typeHandler": "handler: IntHandler", 
            "memberName": "readRedirectNeighbourTableMsec", 
            "yangName": "read-redirect-neighbour-table-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "triggerTitleTableSaveMsec", 
            "yangName": "trigger-title-table-save-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "readRedirectEnablerMsec", 
            "yangName": "read-redirect-enabler-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "readBrownieQuotaMsec", 
            "yangName": "read-brownie-quota-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "logDebugStatsMsec", 
            "yangName": "log-debug-stats-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "readDeliveryBlockerUpdatesMsec", 
            "yangName": "read-delivery-blocker-updates-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "readExternalStateMsec", 
            "yangName": "read-external-state-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "writeAcquiredTitlesMsec", 
            "yangName": "write-acquired-titles-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "readExternalConfigMsec", 
            "yangName": "read-external-config-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "readDeliveredTitlesMsec", 
            "yangName": "read-delivered-titles-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "requestNeighbourDiscoveryMsec", 
            "yangName": "request-neighbour-discovery-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "updateRedirectQuotaMsec", 
            "yangName": "update-redirect-quota-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "checkContentDisksSizeMsec", 
            "yangName": "check-content-disks-size-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "sampleCountersMsec", 
            "yangName": "sample-counters-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "attenuatePastVolumeMsec", 
            "yangName": "attenuate-past-volume-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


