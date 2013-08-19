


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class StatusMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , disk
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , disk
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , disk
                       
                       , trxContext=None):
        raise NotImplementedError()







    # oper leaves

    # productId
    def requestProductId (self, requested):
        raise NotImplementedError()

    def isProductIdRequested (self):
        raise NotImplementedError()

    def getProductId (self):
        raise NotImplementedError()

    def hasProductId (self):
        raise NotImplementedError()

    def setProductId (self, productId):
        raise NotImplementedError()

    # sasAddress
    def requestSasAddress (self, requested):
        raise NotImplementedError()

    def isSasAddressRequested (self):
        raise NotImplementedError()

    def getSasAddress (self):
        raise NotImplementedError()

    def hasSasAddress (self):
        raise NotImplementedError()

    def setSasAddress (self, sasAddress):
        raise NotImplementedError()

    # modelNumber
    def requestModelNumber (self, requested):
        raise NotImplementedError()

    def isModelNumberRequested (self):
        raise NotImplementedError()

    def getModelNumber (self):
        raise NotImplementedError()

    def hasModelNumber (self):
        raise NotImplementedError()

    def setModelNumber (self, modelNumber):
        raise NotImplementedError()

    # serialNumber
    def requestSerialNumber (self, requested):
        raise NotImplementedError()

    def isSerialNumberRequested (self):
        raise NotImplementedError()

    def getSerialNumber (self):
        raise NotImplementedError()

    def hasSerialNumber (self):
        raise NotImplementedError()

    def setSerialNumber (self, serialNumber):
        raise NotImplementedError()

    # usedRaidSpace
    def requestUsedRaidSpace (self, requested):
        raise NotImplementedError()

    def isUsedRaidSpaceRequested (self):
        raise NotImplementedError()

    def getUsedRaidSpace (self):
        raise NotImplementedError()

    def hasUsedRaidSpace (self):
        raise NotImplementedError()

    def setUsedRaidSpace (self, usedRaidSpace):
        raise NotImplementedError()

    # statusRaw
    def requestStatusRaw (self, requested):
        raise NotImplementedError()

    def isStatusRawRequested (self):
        raise NotImplementedError()

    def getStatusRaw (self):
        raise NotImplementedError()

    def hasStatusRaw (self):
        raise NotImplementedError()

    def setStatusRaw (self, statusRaw):
        raise NotImplementedError()

    # firmwareRevision
    def requestFirmwareRevision (self, requested):
        raise NotImplementedError()

    def isFirmwareRevisionRequested (self):
        raise NotImplementedError()

    def getFirmwareRevision (self):
        raise NotImplementedError()

    def hasFirmwareRevision (self):
        raise NotImplementedError()

    def setFirmwareRevision (self, firmwareRevision):
        raise NotImplementedError()

    # size
    def requestSize (self, requested):
        raise NotImplementedError()

    def isSizeRequested (self):
        raise NotImplementedError()

    def getSize (self):
        raise NotImplementedError()

    def hasSize (self):
        raise NotImplementedError()

    def setSize (self, size):
        raise NotImplementedError()

    # failurePredicted
    def requestFailurePredicted (self, requested):
        raise NotImplementedError()

    def isFailurePredictedRequested (self):
        raise NotImplementedError()

    def getFailurePredicted (self):
        raise NotImplementedError()

    def hasFailurePredicted (self):
        raise NotImplementedError()

    def setFailurePredicted (self, failurePredicted):
        raise NotImplementedError()

    # sizeRaw
    def requestSizeRaw (self, requested):
        raise NotImplementedError()

    def isSizeRawRequested (self):
        raise NotImplementedError()

    def getSizeRaw (self):
        raise NotImplementedError()

    def hasSizeRaw (self):
        raise NotImplementedError()

    def setSizeRaw (self, sizeRaw):
        raise NotImplementedError()

    # deviceLifeStatus
    def requestDeviceLifeStatus (self, requested):
        raise NotImplementedError()

    def isDeviceLifeStatusRequested (self):
        raise NotImplementedError()

    def getDeviceLifeStatus (self):
        raise NotImplementedError()

    def hasDeviceLifeStatus (self):
        raise NotImplementedError()

    def setDeviceLifeStatus (self, deviceLifeStatus):
        raise NotImplementedError()

    # deviceLifeRemaining
    def requestDeviceLifeRemaining (self, requested):
        raise NotImplementedError()

    def isDeviceLifeRemainingRequested (self):
        raise NotImplementedError()

    def getDeviceLifeRemaining (self):
        raise NotImplementedError()

    def hasDeviceLifeRemaining (self):
        raise NotImplementedError()

    def setDeviceLifeRemaining (self, deviceLifeRemaining):
        raise NotImplementedError()

    # powerStatus
    def requestPowerStatus (self, requested):
        raise NotImplementedError()

    def isPowerStatusRequested (self):
        raise NotImplementedError()

    def getPowerStatus (self):
        raise NotImplementedError()

    def hasPowerStatus (self):
        raise NotImplementedError()

    def setPowerStatus (self, powerStatus):
        raise NotImplementedError()

    # state
    def requestState (self, requested):
        raise NotImplementedError()

    def isStateRequested (self):
        raise NotImplementedError()

    def getState (self):
        raise NotImplementedError()

    def hasState (self):
        raise NotImplementedError()

    def setState (self, state):
        raise NotImplementedError()

    # progress
    def requestProgress (self, requested):
        raise NotImplementedError()

    def isProgressRequested (self):
        raise NotImplementedError()

    def getProgress (self):
        raise NotImplementedError()

    def hasProgress (self):
        raise NotImplementedError()

    def setProgress (self, progress):
        raise NotImplementedError()

    # status
    def requestStatus (self, requested):
        raise NotImplementedError()

    def isStatusRequested (self):
        raise NotImplementedError()

    def getStatus (self):
        raise NotImplementedError()

    def hasStatus (self):
        raise NotImplementedError()

    def setStatus (self, status):
        raise NotImplementedError()

    # manufactureYear
    def requestManufactureYear (self, requested):
        raise NotImplementedError()

    def isManufactureYearRequested (self):
        raise NotImplementedError()

    def getManufactureYear (self):
        raise NotImplementedError()

    def hasManufactureYear (self):
        raise NotImplementedError()

    def setManufactureYear (self, manufactureYear):
        raise NotImplementedError()

    # failurePredictedRaw
    def requestFailurePredictedRaw (self, requested):
        raise NotImplementedError()

    def isFailurePredictedRawRequested (self):
        raise NotImplementedError()

    def getFailurePredictedRaw (self):
        raise NotImplementedError()

    def hasFailurePredictedRaw (self):
        raise NotImplementedError()

    def setFailurePredictedRaw (self, failurePredictedRaw):
        raise NotImplementedError()

    # mediaType
    def requestMediaType (self, requested):
        raise NotImplementedError()

    def isMediaTypeRequested (self):
        raise NotImplementedError()

    def getMediaType (self):
        raise NotImplementedError()

    def hasMediaType (self):
        raise NotImplementedError()

    def setMediaType (self, mediaType):
        raise NotImplementedError()

    # manufactureDay
    def requestManufactureDay (self, requested):
        raise NotImplementedError()

    def isManufactureDayRequested (self):
        raise NotImplementedError()

    def getManufactureDay (self):
        raise NotImplementedError()

    def hasManufactureDay (self):
        raise NotImplementedError()

    def setManufactureDay (self, manufactureDay):
        raise NotImplementedError()

    # availableRaidSpace
    def requestAvailableRaidSpace (self, requested):
        raise NotImplementedError()

    def isAvailableRaidSpaceRequested (self):
        raise NotImplementedError()

    def getAvailableRaidSpace (self):
        raise NotImplementedError()

    def hasAvailableRaidSpace (self):
        raise NotImplementedError()

    def setAvailableRaidSpace (self, availableRaidSpace):
        raise NotImplementedError()

    # partNumber
    def requestPartNumber (self, requested):
        raise NotImplementedError()

    def isPartNumberRequested (self):
        raise NotImplementedError()

    def getPartNumber (self):
        raise NotImplementedError()

    def hasPartNumber (self):
        raise NotImplementedError()

    def setPartNumber (self, partNumber):
        raise NotImplementedError()

    # hotSpare
    def requestHotSpare (self, requested):
        raise NotImplementedError()

    def isHotSpareRequested (self):
        raise NotImplementedError()

    def getHotSpare (self):
        raise NotImplementedError()

    def hasHotSpare (self):
        raise NotImplementedError()

    def setHotSpare (self, hotSpare):
        raise NotImplementedError()

    # capableSpeed
    def requestCapableSpeed (self, requested):
        raise NotImplementedError()

    def isCapableSpeedRequested (self):
        raise NotImplementedError()

    def getCapableSpeed (self):
        raise NotImplementedError()

    def hasCapableSpeed (self):
        raise NotImplementedError()

    def setCapableSpeed (self, capableSpeed):
        raise NotImplementedError()

    # certified
    def requestCertified (self, requested):
        raise NotImplementedError()

    def isCertifiedRequested (self):
        raise NotImplementedError()

    def getCertified (self):
        raise NotImplementedError()

    def hasCertified (self):
        raise NotImplementedError()

    def setCertified (self, certified):
        raise NotImplementedError()

    # deviceWriteCache
    def requestDeviceWriteCache (self, requested):
        raise NotImplementedError()

    def isDeviceWriteCacheRequested (self):
        raise NotImplementedError()

    def getDeviceWriteCache (self):
        raise NotImplementedError()

    def hasDeviceWriteCache (self):
        raise NotImplementedError()

    def setDeviceWriteCache (self, deviceWriteCache):
        raise NotImplementedError()

    # stateRaw
    def requestStateRaw (self, requested):
        raise NotImplementedError()

    def isStateRawRequested (self):
        raise NotImplementedError()

    def getStateRaw (self):
        raise NotImplementedError()

    def hasStateRaw (self):
        raise NotImplementedError()

    def setStateRaw (self, stateRaw):
        raise NotImplementedError()

    # manufactureWeek
    def requestManufactureWeek (self, requested):
        raise NotImplementedError()

    def isManufactureWeekRequested (self):
        raise NotImplementedError()

    def getManufactureWeek (self):
        raise NotImplementedError()

    def hasManufactureWeek (self):
        raise NotImplementedError()

    def setManufactureWeek (self, manufactureWeek):
        raise NotImplementedError()

    # negotiatedSpeed
    def requestNegotiatedSpeed (self, requested):
        raise NotImplementedError()

    def isNegotiatedSpeedRequested (self):
        raise NotImplementedError()

    def getNegotiatedSpeed (self):
        raise NotImplementedError()

    def hasNegotiatedSpeed (self):
        raise NotImplementedError()

    def setNegotiatedSpeed (self, negotiatedSpeed):
        raise NotImplementedError()

    # vendorId
    def requestVendorId (self, requested):
        raise NotImplementedError()

    def isVendorIdRequested (self):
        raise NotImplementedError()

    def getVendorId (self):
        raise NotImplementedError()

    def hasVendorId (self):
        raise NotImplementedError()

    def setVendorId (self, vendorId):
        raise NotImplementedError()




"""
Extracted from the below data: 
{
    "node": {
        "name": "status", 
        "namespace": "status", 
        "className": "StatusMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.physical.status.status_maapi_gen import StatusMaapi", 
        "baseClassName": "StatusMaapiBase", 
        "baseModule": "status_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-strg", 
            "yangName": "storage", 
            "namespace": "storage", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage", 
            "name": "storage"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "isCurrent": false, 
            "yangName": "disk", 
            "namespace": "disk", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "keyLeaf": {
                "varName": "disk", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "disk"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "yangName": "physical", 
            "namespace": "physical", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "name": "physical"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "yangName": "status", 
            "namespace": "status", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "name": "status"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "productId", 
            "yangName": "product-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "sasAddress", 
            "yangName": "sas-address", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "modelNumber", 
            "yangName": "model-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "serialNumber", 
            "yangName": "serial-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "usedRaidSpace", 
            "yangName": "used-raid-space", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "statusRaw", 
            "yangName": "status-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "firmwareRevision", 
            "yangName": "firmware-revision", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "size", 
            "yangName": "size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "failurePredicted", 
            "yangName": "failure-predicted", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "sizeRaw", 
            "yangName": "size-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "deviceLifeStatus", 
            "yangName": "device-life-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "deviceLifeRemaining", 
            "yangName": "device-life-remaining", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "powerStatus", 
            "yangName": "power-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "state", 
            "yangName": "state", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "progress", 
            "yangName": "progress", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "status", 
            "yangName": "status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "manufactureYear", 
            "yangName": "manufacture-year", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "failurePredictedRaw", 
            "yangName": "failure-predicted-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "mediaType", 
            "yangName": "media-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "manufactureDay", 
            "yangName": "manufacture-day", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "availableRaidSpace", 
            "yangName": "available-raid-space", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "partNumber", 
            "yangName": "part-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "hotSpare", 
            "yangName": "hot-spare", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "capableSpeed", 
            "yangName": "capable-speed", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "certified", 
            "yangName": "certified", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "deviceWriteCache", 
            "yangName": "device-write-cache", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "stateRaw", 
            "yangName": "state-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "manufactureWeek", 
            "yangName": "manufacture-week", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "negotiatedSpeed", 
            "yangName": "negotiated-speed", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "vendorId", 
            "yangName": "vendor-id", 
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
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "common", 
            "qwilt_tech_storage_disk"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "productId", 
            "yangName": "product-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "sasAddress", 
            "yangName": "sas-address", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "modelNumber", 
            "yangName": "model-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "serialNumber", 
            "yangName": "serial-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "usedRaidSpace", 
            "yangName": "used-raid-space", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "statusRaw", 
            "yangName": "status-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "firmwareRevision", 
            "yangName": "firmware-revision", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "size", 
            "yangName": "size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "failurePredicted", 
            "yangName": "failure-predicted", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "sizeRaw", 
            "yangName": "size-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "deviceLifeStatus", 
            "yangName": "device-life-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "deviceLifeRemaining", 
            "yangName": "device-life-remaining", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "powerStatus", 
            "yangName": "power-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "state", 
            "yangName": "state", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "progress", 
            "yangName": "progress", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "status", 
            "yangName": "status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "manufactureYear", 
            "yangName": "manufacture-year", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "failurePredictedRaw", 
            "yangName": "failure-predicted-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "mediaType", 
            "yangName": "media-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "manufactureDay", 
            "yangName": "manufacture-day", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "availableRaidSpace", 
            "yangName": "available-raid-space", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "partNumber", 
            "yangName": "part-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "hotSpare", 
            "yangName": "hot-spare", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "capableSpeed", 
            "yangName": "capable-speed", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "certified", 
            "yangName": "certified", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "deviceWriteCache", 
            "yangName": "device-write-cache", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "stateRaw", 
            "yangName": "state-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "manufactureWeek", 
            "yangName": "manufacture-week", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "negotiatedSpeed", 
            "yangName": "negotiated-speed", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "vendorId", 
            "yangName": "vendor-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


