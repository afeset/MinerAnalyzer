


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes
from a.infra.misc.init_guard import InitGuard

from a.sys.confd.pyconfdlib.tag_values import TagValues
from a.sys.confd.pyconfdlib.value import Value
from a.sys.confd.pyconfdlib.key_path import KeyPath

from device_maapi_base_gen import DeviceMaapiBase


from a.api.yang.modules.tech.common.qwilt_tech_interfaces_types.qwilt_tech_interfaces_types_module_gen import DeviceCountersClearEventType


class BlinkyDeviceMaapi(DeviceMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-device")
        self.domain = None

        

        
        self.pciDeviceIdRequested = False
        self.pciDeviceId = None
        self.pciDeviceIdSet = False
        
        self.countersClearEventRequested = False
        self.countersClearEvent = None
        self.countersClearEventSet = False
        
        self.pciVendorIdRequested = False
        self.pciVendorId = None
        self.pciVendorIdSet = False
        
        self.pciIndexRequested = False
        self.pciIndex = None
        self.pciIndexSet = False
        
        self.osNameRequested = False
        self.osName = None
        self.osNameSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestPciDeviceId(True)
        
        self.requestCountersClearEvent(True)
        
        self.requestPciVendorId(True)
        
        self.requestPciIndex(True)
        
        self.requestOsName(True)
        
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestPciDeviceId(True)
        
        self.requestCountersClearEvent(True)
        
        self.requestPciVendorId(True)
        
        self.requestPciIndex(True)
        
        self.requestOsName(True)
        
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestPciDeviceId(False)
        
        self.requestCountersClearEvent(False)
        
        self.requestPciVendorId(False)
        
        self.requestPciIndex(False)
        
        self.requestOsName(False)
        
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestPciDeviceId(False)
        
        self.requestCountersClearEvent(False)
        
        self.requestPciVendorId(False)
        
        self.requestPciIndex(False)
        
        self.requestOsName(False)
        
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setPciDeviceId(None)
        self.pciDeviceIdSet = False
        
        self.setCountersClearEvent(None)
        self.countersClearEventSet = False
        
        self.setPciVendorId(None)
        self.pciVendorIdSet = False
        
        self.setPciIndex(None)
        self.pciIndexSet = False
        
        self.setOsName(None)
        self.osNameSet = False
        
        

    def write (self
              , interface
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(interface, trxContext)

    def read (self
              , interface
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(interface, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , interface
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(interface, 
                                  True,
                                  trxContext)



    def requestPciDeviceId (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-pcideviceid').debug3Func(): logFunc('called. requested=%s', requested)
        self.pciDeviceIdRequested = requested
        self.pciDeviceIdSet = False

    def isPciDeviceIdRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-pcideviceid-requested').debug3Func(): logFunc('called. requested=%s', self.pciDeviceIdRequested)
        return self.pciDeviceIdRequested

    def getPciDeviceId (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-pcideviceid').debug3Func(): logFunc('called. self.pciDeviceIdSet=%s, self.pciDeviceId=%s', self.pciDeviceIdSet, self.pciDeviceId)
        if self.pciDeviceIdSet:
            return self.pciDeviceId
        return None

    def hasPciDeviceId (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-pcideviceid').debug3Func(): logFunc('called. self.pciDeviceIdSet=%s, self.pciDeviceId=%s', self.pciDeviceIdSet, self.pciDeviceId)
        if self.pciDeviceIdSet:
            return True
        return False

    def setPciDeviceId (self, pciDeviceId):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-pcideviceid').debug3Func(): logFunc('called. pciDeviceId=%s, old=%s', pciDeviceId, self.pciDeviceId)
        self.pciDeviceIdSet = True
        self.pciDeviceId = pciDeviceId

    def requestCountersClearEvent (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-countersclearevent').debug3Func(): logFunc('called. requested=%s', requested)
        self.countersClearEventRequested = requested
        self.countersClearEventSet = False

    def isCountersClearEventRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-countersclearevent-requested').debug3Func(): logFunc('called. requested=%s', self.countersClearEventRequested)
        return self.countersClearEventRequested

    def getCountersClearEvent (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-countersclearevent').debug3Func(): logFunc('called. self.countersClearEventSet=%s, self.countersClearEvent=%s', self.countersClearEventSet, self.countersClearEvent)
        if self.countersClearEventSet:
            return self.countersClearEvent
        return None

    def hasCountersClearEvent (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-countersclearevent').debug3Func(): logFunc('called. self.countersClearEventSet=%s, self.countersClearEvent=%s', self.countersClearEventSet, self.countersClearEvent)
        if self.countersClearEventSet:
            return True
        return False

    def setCountersClearEvent (self, countersClearEvent):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-countersclearevent').debug3Func(): logFunc('called. countersClearEvent=%s, old=%s', countersClearEvent, self.countersClearEvent)
        self.countersClearEventSet = True
        self.countersClearEvent = countersClearEvent

    def requestPciVendorId (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-pcivendorid').debug3Func(): logFunc('called. requested=%s', requested)
        self.pciVendorIdRequested = requested
        self.pciVendorIdSet = False

    def isPciVendorIdRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-pcivendorid-requested').debug3Func(): logFunc('called. requested=%s', self.pciVendorIdRequested)
        return self.pciVendorIdRequested

    def getPciVendorId (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-pcivendorid').debug3Func(): logFunc('called. self.pciVendorIdSet=%s, self.pciVendorId=%s', self.pciVendorIdSet, self.pciVendorId)
        if self.pciVendorIdSet:
            return self.pciVendorId
        return None

    def hasPciVendorId (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-pcivendorid').debug3Func(): logFunc('called. self.pciVendorIdSet=%s, self.pciVendorId=%s', self.pciVendorIdSet, self.pciVendorId)
        if self.pciVendorIdSet:
            return True
        return False

    def setPciVendorId (self, pciVendorId):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-pcivendorid').debug3Func(): logFunc('called. pciVendorId=%s, old=%s', pciVendorId, self.pciVendorId)
        self.pciVendorIdSet = True
        self.pciVendorId = pciVendorId

    def requestPciIndex (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-pciindex').debug3Func(): logFunc('called. requested=%s', requested)
        self.pciIndexRequested = requested
        self.pciIndexSet = False

    def isPciIndexRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-pciindex-requested').debug3Func(): logFunc('called. requested=%s', self.pciIndexRequested)
        return self.pciIndexRequested

    def getPciIndex (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-pciindex').debug3Func(): logFunc('called. self.pciIndexSet=%s, self.pciIndex=%s', self.pciIndexSet, self.pciIndex)
        if self.pciIndexSet:
            return self.pciIndex
        return None

    def hasPciIndex (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-pciindex').debug3Func(): logFunc('called. self.pciIndexSet=%s, self.pciIndex=%s', self.pciIndexSet, self.pciIndex)
        if self.pciIndexSet:
            return True
        return False

    def setPciIndex (self, pciIndex):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-pciindex').debug3Func(): logFunc('called. pciIndex=%s, old=%s', pciIndex, self.pciIndex)
        self.pciIndexSet = True
        self.pciIndex = pciIndex

    def requestOsName (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-osname').debug3Func(): logFunc('called. requested=%s', requested)
        self.osNameRequested = requested
        self.osNameSet = False

    def isOsNameRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-osname-requested').debug3Func(): logFunc('called. requested=%s', self.osNameRequested)
        return self.osNameRequested

    def getOsName (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-osname').debug3Func(): logFunc('called. self.osNameSet=%s, self.osName=%s', self.osNameSet, self.osName)
        if self.osNameSet:
            return self.osName
        return None

    def hasOsName (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-osname').debug3Func(): logFunc('called. self.osNameSet=%s, self.osName=%s', self.osNameSet, self.osName)
        if self.osNameSet:
            return True
        return False

    def setOsName (self, osName):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-osname').debug3Func(): logFunc('called. osName=%s, old=%s', osName, self.osName)
        self.osNameSet = True
        self.osName = osName


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.pciDeviceId = 0
        self.pciDeviceIdSet = False
        
        self.countersClearEvent = 0
        self.countersClearEventSet = False
        
        self.pciVendorId = 0
        self.pciVendorIdSet = False
        
        self.pciIndex = 0
        self.pciIndexSet = False
        
        self.osName = 0
        self.osNameSet = False
        

    def _getSelfKeyPath (self, interface
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("device", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(interface);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("interface", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("interfaces", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        interface, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(interface, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(interface, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       interface, 
                       
                       readAllOrFail,
                       trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-read').debug3Func(): logFunc('called. PARAMS, readAllOrFail=%s', readAllOrFail)

        if readAllOrFail:
            self._clearAllReadData()

        tagValueList = TagValues()

        res = self._fillReadTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-fill-read-tag-value-failed').errorFunc(): logFunc('_fillReadTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(interface, 
                                       
                                       None)

        res = self.domain.readMaapi(tagValueList, keyPath, trxContext)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-domain-failed').errorFunc(): logFunc('domain.readMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        res = self._readTagValues(tagValueList, readAllOrFail)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-read-tag-values-failed').errorFunc(): logFunc('_readTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-read-done').debug3Func(): logFunc('done. PARAMS, readAllOrFail=%s', readAllOrFail)
        return ReturnCodes.kOk

    def _collectItemsToDelete (self,
                               interface, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasPciDeviceId():
            valPciDeviceId = Value()
            if self.pciDeviceId is not None:
                valPciDeviceId.setString(self.pciDeviceId)
            else:
                valPciDeviceId.setEmpty()
            tagValueList.push(("pci-device-id", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valPciDeviceId)
        
        if self.hasCountersClearEvent():
            valCountersClearEvent = Value()
            if self.countersClearEvent is not None:
                valCountersClearEvent.setEnum(self.countersClearEvent.getValue())
            else:
                valCountersClearEvent.setEmpty()
            tagValueList.push(("counters-clear-event", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valCountersClearEvent)
        
        if self.hasPciVendorId():
            valPciVendorId = Value()
            if self.pciVendorId is not None:
                valPciVendorId.setString(self.pciVendorId)
            else:
                valPciVendorId.setEmpty()
            tagValueList.push(("pci-vendor-id", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valPciVendorId)
        
        if self.hasPciIndex():
            valPciIndex = Value()
            if self.pciIndex is not None:
                valPciIndex.setUint64(self.pciIndex)
            else:
                valPciIndex.setEmpty()
            tagValueList.push(("pci-index", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valPciIndex)
        
        if self.hasOsName():
            valOsName = Value()
            if self.osName is not None:
                valOsName.setString(self.osName)
            else:
                valOsName.setEmpty()
            tagValueList.push(("os-name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valOsName)
        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isPciDeviceIdRequested():
            valPciDeviceId = Value()
            valPciDeviceId.setEmpty()
            tagValueList.push(("pci-device-id", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valPciDeviceId)
        
        if self.isCountersClearEventRequested():
            valCountersClearEvent = Value()
            valCountersClearEvent.setEmpty()
            tagValueList.push(("counters-clear-event", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valCountersClearEvent)
        
        if self.isPciVendorIdRequested():
            valPciVendorId = Value()
            valPciVendorId.setEmpty()
            tagValueList.push(("pci-vendor-id", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valPciVendorId)
        
        if self.isPciIndexRequested():
            valPciIndex = Value()
            valPciIndex.setEmpty()
            tagValueList.push(("pci-index", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valPciIndex)
        
        if self.isOsNameRequested():
            valOsName = Value()
            valOsName.setEmpty()
            tagValueList.push(("os-name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valOsName)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isPciDeviceIdRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "pci-device-id") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-pcideviceid').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "pciDeviceId", "pci-device-id", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-pci-device-id-bad-value').infoFunc(): logFunc('pciDeviceId not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPciDeviceId(tempVar)
            for logFunc in self._log('read-tag-values-pci-device-id').debug3Func(): logFunc('read pciDeviceId. pciDeviceId=%s, tempValue=%s', self.pciDeviceId, tempValue.getType())
        
        if self.isCountersClearEventRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "counters-clear-event") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-countersclearevent').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "countersClearEvent", "counters-clear-event", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-counters-clear-event-bad-value').infoFunc(): logFunc('countersClearEvent not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setCountersClearEvent(tempVar)
            for logFunc in self._log('read-tag-values-counters-clear-event').debug3Func(): logFunc('read countersClearEvent. countersClearEvent=%s, tempValue=%s', self.countersClearEvent, tempValue.getType())
        
        if self.isPciVendorIdRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "pci-vendor-id") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-pcivendorid').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "pciVendorId", "pci-vendor-id", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-pci-vendor-id-bad-value').infoFunc(): logFunc('pciVendorId not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPciVendorId(tempVar)
            for logFunc in self._log('read-tag-values-pci-vendor-id').debug3Func(): logFunc('read pciVendorId. pciVendorId=%s, tempValue=%s', self.pciVendorId, tempValue.getType())
        
        if self.isPciIndexRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "pci-index") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-pciindex').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "pciIndex", "pci-index", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-pci-index-bad-value').infoFunc(): logFunc('pciIndex not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPciIndex(tempVar)
            for logFunc in self._log('read-tag-values-pci-index').debug3Func(): logFunc('read pciIndex. pciIndex=%s, tempValue=%s', self.pciIndex, tempValue.getType())
        
        if self.isOsNameRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "os-name") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-osname').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "osName", "os-name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-os-name-bad-value').infoFunc(): logFunc('osName not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOsName(tempVar)
            for logFunc in self._log('read-tag-values-os-name').debug3Func(): logFunc('read osName. osName=%s, tempValue=%s', self.osName, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "device", 
        "namespace": "device", 
        "className": "DeviceMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.system_defaults.device.device_maapi_gen import DeviceMaapi", 
        "baseClassName": "DeviceMaapiBase", 
        "baseModule": "device_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "interfaces", 
            "namespace": "interfaces", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "isCurrent": false, 
            "yangName": "interface", 
            "namespace": "interface", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "keyLeaf": {
                "varName": "interface", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "interface"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "system-defaults"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "device", 
            "namespace": "device", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "device"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "pciDeviceId", 
            "yangName": "pci-device-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "countersClearEvent", 
            "yangName": "counters-clear-event", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "none", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "pciVendorId", 
            "yangName": "pci-vendor-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pciIndex", 
            "yangName": "pci-index", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "osName", 
            "yangName": "os-name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
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
            "common", 
            "qwilt_tech_interfaces"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "pciDeviceId", 
            "yangName": "pci-device-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "countersClearEvent", 
            "yangName": "counters-clear-event", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "none", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "pciVendorId", 
            "yangName": "pci-vendor-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pciIndex", 
            "yangName": "pci-index", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "osName", 
            "yangName": "os-name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


