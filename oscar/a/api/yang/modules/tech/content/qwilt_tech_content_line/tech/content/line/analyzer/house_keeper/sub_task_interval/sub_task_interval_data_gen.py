


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class SubTaskIntervalData(object):

    def __init__ (self):

        self.readRedirectNeighbourTableMsec = 0
        self._myHasReadRedirectNeighbourTableMsec=False
        
        self.triggerTitleTableSaveMsec = 0
        self._myHasTriggerTitleTableSaveMsec=False
        
        self.readRedirectEnablerMsec = 0
        self._myHasReadRedirectEnablerMsec=False
        
        self.readBrownieQuotaMsec = 0
        self._myHasReadBrownieQuotaMsec=False
        
        self.logDebugStatsMsec = 0
        self._myHasLogDebugStatsMsec=False
        
        self.readDeliveryBlockerUpdatesMsec = 0
        self._myHasReadDeliveryBlockerUpdatesMsec=False
        
        self.readExternalStateMsec = 0
        self._myHasReadExternalStateMsec=False
        
        self.writeAcquiredTitlesMsec = 0
        self._myHasWriteAcquiredTitlesMsec=False
        
        self.readExternalConfigMsec = 0
        self._myHasReadExternalConfigMsec=False
        
        self.readDeliveredTitlesMsec = 0
        self._myHasReadDeliveredTitlesMsec=False
        
        self.requestNeighbourDiscoveryMsec = 0
        self._myHasRequestNeighbourDiscoveryMsec=False
        
        self.updateRedirectQuotaMsec = 0
        self._myHasUpdateRedirectQuotaMsec=False
        
        self.checkContentDisksSizeMsec = 0
        self._myHasCheckContentDisksSizeMsec=False
        
        self.sampleCountersMsec = 0
        self._myHasSampleCountersMsec=False
        
        self.attenuatePastVolumeMsec = 0
        self._myHasAttenuatePastVolumeMsec=False
        

    def copyFrom (self, other):

        self.readRedirectNeighbourTableMsec=other.readRedirectNeighbourTableMsec
        self._myHasReadRedirectNeighbourTableMsec=other._myHasReadRedirectNeighbourTableMsec
        
        self.triggerTitleTableSaveMsec=other.triggerTitleTableSaveMsec
        self._myHasTriggerTitleTableSaveMsec=other._myHasTriggerTitleTableSaveMsec
        
        self.readRedirectEnablerMsec=other.readRedirectEnablerMsec
        self._myHasReadRedirectEnablerMsec=other._myHasReadRedirectEnablerMsec
        
        self.readBrownieQuotaMsec=other.readBrownieQuotaMsec
        self._myHasReadBrownieQuotaMsec=other._myHasReadBrownieQuotaMsec
        
        self.logDebugStatsMsec=other.logDebugStatsMsec
        self._myHasLogDebugStatsMsec=other._myHasLogDebugStatsMsec
        
        self.readDeliveryBlockerUpdatesMsec=other.readDeliveryBlockerUpdatesMsec
        self._myHasReadDeliveryBlockerUpdatesMsec=other._myHasReadDeliveryBlockerUpdatesMsec
        
        self.readExternalStateMsec=other.readExternalStateMsec
        self._myHasReadExternalStateMsec=other._myHasReadExternalStateMsec
        
        self.writeAcquiredTitlesMsec=other.writeAcquiredTitlesMsec
        self._myHasWriteAcquiredTitlesMsec=other._myHasWriteAcquiredTitlesMsec
        
        self.readExternalConfigMsec=other.readExternalConfigMsec
        self._myHasReadExternalConfigMsec=other._myHasReadExternalConfigMsec
        
        self.readDeliveredTitlesMsec=other.readDeliveredTitlesMsec
        self._myHasReadDeliveredTitlesMsec=other._myHasReadDeliveredTitlesMsec
        
        self.requestNeighbourDiscoveryMsec=other.requestNeighbourDiscoveryMsec
        self._myHasRequestNeighbourDiscoveryMsec=other._myHasRequestNeighbourDiscoveryMsec
        
        self.updateRedirectQuotaMsec=other.updateRedirectQuotaMsec
        self._myHasUpdateRedirectQuotaMsec=other._myHasUpdateRedirectQuotaMsec
        
        self.checkContentDisksSizeMsec=other.checkContentDisksSizeMsec
        self._myHasCheckContentDisksSizeMsec=other._myHasCheckContentDisksSizeMsec
        
        self.sampleCountersMsec=other.sampleCountersMsec
        self._myHasSampleCountersMsec=other._myHasSampleCountersMsec
        
        self.attenuatePastVolumeMsec=other.attenuatePastVolumeMsec
        self._myHasAttenuatePastVolumeMsec=other._myHasAttenuatePastVolumeMsec
        
    # has...() methods

    def hasReadRedirectNeighbourTableMsec (self):
        return self._myHasReadRedirectNeighbourTableMsec

    def hasTriggerTitleTableSaveMsec (self):
        return self._myHasTriggerTitleTableSaveMsec

    def hasReadRedirectEnablerMsec (self):
        return self._myHasReadRedirectEnablerMsec

    def hasReadBrownieQuotaMsec (self):
        return self._myHasReadBrownieQuotaMsec

    def hasLogDebugStatsMsec (self):
        return self._myHasLogDebugStatsMsec

    def hasReadDeliveryBlockerUpdatesMsec (self):
        return self._myHasReadDeliveryBlockerUpdatesMsec

    def hasReadExternalStateMsec (self):
        return self._myHasReadExternalStateMsec

    def hasWriteAcquiredTitlesMsec (self):
        return self._myHasWriteAcquiredTitlesMsec

    def hasReadExternalConfigMsec (self):
        return self._myHasReadExternalConfigMsec

    def hasReadDeliveredTitlesMsec (self):
        return self._myHasReadDeliveredTitlesMsec

    def hasRequestNeighbourDiscoveryMsec (self):
        return self._myHasRequestNeighbourDiscoveryMsec

    def hasUpdateRedirectQuotaMsec (self):
        return self._myHasUpdateRedirectQuotaMsec

    def hasCheckContentDisksSizeMsec (self):
        return self._myHasCheckContentDisksSizeMsec

    def hasSampleCountersMsec (self):
        return self._myHasSampleCountersMsec

    def hasAttenuatePastVolumeMsec (self):
        return self._myHasAttenuatePastVolumeMsec


    # setHas...() methods

    def setHasReadRedirectNeighbourTableMsec (self):
        self._myHasReadRedirectNeighbourTableMsec=True

    def setHasTriggerTitleTableSaveMsec (self):
        self._myHasTriggerTitleTableSaveMsec=True

    def setHasReadRedirectEnablerMsec (self):
        self._myHasReadRedirectEnablerMsec=True

    def setHasReadBrownieQuotaMsec (self):
        self._myHasReadBrownieQuotaMsec=True

    def setHasLogDebugStatsMsec (self):
        self._myHasLogDebugStatsMsec=True

    def setHasReadDeliveryBlockerUpdatesMsec (self):
        self._myHasReadDeliveryBlockerUpdatesMsec=True

    def setHasReadExternalStateMsec (self):
        self._myHasReadExternalStateMsec=True

    def setHasWriteAcquiredTitlesMsec (self):
        self._myHasWriteAcquiredTitlesMsec=True

    def setHasReadExternalConfigMsec (self):
        self._myHasReadExternalConfigMsec=True

    def setHasReadDeliveredTitlesMsec (self):
        self._myHasReadDeliveredTitlesMsec=True

    def setHasRequestNeighbourDiscoveryMsec (self):
        self._myHasRequestNeighbourDiscoveryMsec=True

    def setHasUpdateRedirectQuotaMsec (self):
        self._myHasUpdateRedirectQuotaMsec=True

    def setHasCheckContentDisksSizeMsec (self):
        self._myHasCheckContentDisksSizeMsec=True

    def setHasSampleCountersMsec (self):
        self._myHasSampleCountersMsec=True

    def setHasAttenuatePastVolumeMsec (self):
        self._myHasAttenuatePastVolumeMsec=True


    def clearAllHas (self):

        self._myHasReadRedirectNeighbourTableMsec=False

        self._myHasTriggerTitleTableSaveMsec=False

        self._myHasReadRedirectEnablerMsec=False

        self._myHasReadBrownieQuotaMsec=False

        self._myHasLogDebugStatsMsec=False

        self._myHasReadDeliveryBlockerUpdatesMsec=False

        self._myHasReadExternalStateMsec=False

        self._myHasWriteAcquiredTitlesMsec=False

        self._myHasReadExternalConfigMsec=False

        self._myHasReadDeliveredTitlesMsec=False

        self._myHasRequestNeighbourDiscoveryMsec=False

        self._myHasUpdateRedirectQuotaMsec=False

        self._myHasCheckContentDisksSizeMsec=False

        self._myHasSampleCountersMsec=False

        self._myHasAttenuatePastVolumeMsec=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasReadRedirectNeighbourTableMsec:
            x = "+"
        leafStr = str(self.readRedirectNeighbourTableMsec)
        items.append(x + "ReadRedirectNeighbourTableMsec="+leafStr)

        x=""
        if self._myHasTriggerTitleTableSaveMsec:
            x = "+"
        leafStr = str(self.triggerTitleTableSaveMsec)
        items.append(x + "TriggerTitleTableSaveMsec="+leafStr)

        x=""
        if self._myHasReadRedirectEnablerMsec:
            x = "+"
        leafStr = str(self.readRedirectEnablerMsec)
        items.append(x + "ReadRedirectEnablerMsec="+leafStr)

        x=""
        if self._myHasReadBrownieQuotaMsec:
            x = "+"
        leafStr = str(self.readBrownieQuotaMsec)
        items.append(x + "ReadBrownieQuotaMsec="+leafStr)

        x=""
        if self._myHasLogDebugStatsMsec:
            x = "+"
        leafStr = str(self.logDebugStatsMsec)
        items.append(x + "LogDebugStatsMsec="+leafStr)

        x=""
        if self._myHasReadDeliveryBlockerUpdatesMsec:
            x = "+"
        leafStr = str(self.readDeliveryBlockerUpdatesMsec)
        items.append(x + "ReadDeliveryBlockerUpdatesMsec="+leafStr)

        x=""
        if self._myHasReadExternalStateMsec:
            x = "+"
        leafStr = str(self.readExternalStateMsec)
        items.append(x + "ReadExternalStateMsec="+leafStr)

        x=""
        if self._myHasWriteAcquiredTitlesMsec:
            x = "+"
        leafStr = str(self.writeAcquiredTitlesMsec)
        items.append(x + "WriteAcquiredTitlesMsec="+leafStr)

        x=""
        if self._myHasReadExternalConfigMsec:
            x = "+"
        leafStr = str(self.readExternalConfigMsec)
        items.append(x + "ReadExternalConfigMsec="+leafStr)

        x=""
        if self._myHasReadDeliveredTitlesMsec:
            x = "+"
        leafStr = str(self.readDeliveredTitlesMsec)
        items.append(x + "ReadDeliveredTitlesMsec="+leafStr)

        x=""
        if self._myHasRequestNeighbourDiscoveryMsec:
            x = "+"
        leafStr = str(self.requestNeighbourDiscoveryMsec)
        items.append(x + "RequestNeighbourDiscoveryMsec="+leafStr)

        x=""
        if self._myHasUpdateRedirectQuotaMsec:
            x = "+"
        leafStr = str(self.updateRedirectQuotaMsec)
        items.append(x + "UpdateRedirectQuotaMsec="+leafStr)

        x=""
        if self._myHasCheckContentDisksSizeMsec:
            x = "+"
        leafStr = str(self.checkContentDisksSizeMsec)
        items.append(x + "CheckContentDisksSizeMsec="+leafStr)

        x=""
        if self._myHasSampleCountersMsec:
            x = "+"
        leafStr = str(self.sampleCountersMsec)
        items.append(x + "SampleCountersMsec="+leafStr)

        x=""
        if self._myHasAttenuatePastVolumeMsec:
            x = "+"
        leafStr = str(self.attenuatePastVolumeMsec)
        items.append(x + "AttenuatePastVolumeMsec="+leafStr)

        return "{SubTaskIntervalData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "SubTaskIntervalData", 
        "namespace": "sub_task_interval", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.analyzer.house_keeper.sub_task_interval.sub_task_interval_data_gen import SubTaskIntervalData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "content", 
            "isCurrent": false
        }, 
        {
            "namespace": "line", 
            "isCurrent": false
        }, 
        {
            "namespace": "analyzer", 
            "isCurrent": false
        }, 
        {
            "namespace": "house_keeper", 
            "isCurrent": false
        }, 
        {
            "namespace": "sub_task_interval", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "readRedirectNeighbourTableMsec", 
            "yangName": "read-redirect-neighbour-table-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "triggerTitleTableSaveMsec", 
            "yangName": "trigger-title-table-save-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "readRedirectEnablerMsec", 
            "yangName": "read-redirect-enabler-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "readBrownieQuotaMsec", 
            "yangName": "read-brownie-quota-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "logDebugStatsMsec", 
            "yangName": "log-debug-stats-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "readDeliveryBlockerUpdatesMsec", 
            "yangName": "read-delivery-blocker-updates-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "readExternalStateMsec", 
            "yangName": "read-external-state-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "writeAcquiredTitlesMsec", 
            "yangName": "write-acquired-titles-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "readExternalConfigMsec", 
            "yangName": "read-external-config-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "readDeliveredTitlesMsec", 
            "yangName": "read-delivered-titles-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "requestNeighbourDiscoveryMsec", 
            "yangName": "request-neighbour-discovery-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "updateRedirectQuotaMsec", 
            "yangName": "update-redirect-quota-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "checkContentDisksSizeMsec", 
            "yangName": "check-content-disks-size-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "sampleCountersMsec", 
            "yangName": "sample-counters-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "attenuatePastVolumeMsec", 
            "yangName": "attenuate-past-volume-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }
    ], 
    "module": {}, 
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
    "createTime": "2013"
}
"""


