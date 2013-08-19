


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

from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.device.status.status_maapi_gen import BlinkyStatusMaapi
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.device.counters.counters_maapi_gen import BlinkyCountersMaapi

from a.api.yang.modules.tech.common.qwilt_tech_interfaces_types.qwilt_tech_interfaces_types_module_gen import DeviceCountersClearEventType


class BlinkyDeviceMaapi(DeviceMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-device")
        self.domain = None

        
        self.statusObj = None
        
        self.countersObj = None
        

        
        self.osNameRequested = False
        self.osName = None
        self.osNameSet = False
        
        self.pciDeviceIdRequested = False
        self.pciDeviceId = None
        self.pciDeviceIdSet = False
        
        self.pciVendorIdRequested = False
        self.pciVendorId = None
        self.pciVendorIdSet = False
        
        self.postUpCommandRequested = False
        self.postUpCommand = None
        self.postUpCommandSet = False
        
        self.countersClearEventRequested = False
        self.countersClearEvent = None
        self.countersClearEventSet = False
        
        self.pciIndexRequested = False
        self.pciIndex = None
        self.pciIndexSet = False
        
        self.postInitCommandRequested = False
        self.postInitCommand = None
        self.postInitCommandSet = False
        
        self.postDownCommandRequested = False
        self.postDownCommand = None
        self.postDownCommandSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestOsName(True)
        
        self.requestPciDeviceId(True)
        
        self.requestPciVendorId(True)
        
        self.requestPostUpCommand(True)
        
        self.requestCountersClearEvent(True)
        
        self.requestPciIndex(True)
        
        self.requestPostInitCommand(True)
        
        self.requestPostDownCommand(True)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.requestConfigAndOper()
        
        if not self.countersObj:
            self.countersObj = self.newCounters()
            self.countersObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestOsName(True)
        
        self.requestPciDeviceId(True)
        
        self.requestPciVendorId(True)
        
        self.requestPostUpCommand(True)
        
        self.requestCountersClearEvent(True)
        
        self.requestPciIndex(True)
        
        self.requestPostInitCommand(True)
        
        self.requestPostDownCommand(True)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.requestConfig()
        
        if not self.countersObj:
            self.countersObj = self.newCounters()
            self.countersObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestOsName(False)
        
        self.requestPciDeviceId(False)
        
        self.requestPciVendorId(False)
        
        self.requestPostUpCommand(False)
        
        self.requestCountersClearEvent(False)
        
        self.requestPciIndex(False)
        
        self.requestPostInitCommand(False)
        
        self.requestPostDownCommand(False)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.requestOper()
        
        if not self.countersObj:
            self.countersObj = self.newCounters()
            self.countersObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestOsName(False)
        
        self.requestPciDeviceId(False)
        
        self.requestPciVendorId(False)
        
        self.requestPostUpCommand(False)
        
        self.requestCountersClearEvent(False)
        
        self.requestPciIndex(False)
        
        self.requestPostInitCommand(False)
        
        self.requestPostDownCommand(False)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.clearAllRequested()
        
        if not self.countersObj:
            self.countersObj = self.newCounters()
            self.countersObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setOsName(None)
        self.osNameSet = False
        
        self.setPciDeviceId(None)
        self.pciDeviceIdSet = False
        
        self.setPciVendorId(None)
        self.pciVendorIdSet = False
        
        self.setPostUpCommand(None)
        self.postUpCommandSet = False
        
        self.setCountersClearEvent(None)
        self.countersClearEventSet = False
        
        self.setPciIndex(None)
        self.pciIndexSet = False
        
        self.setPostInitCommand(None)
        self.postInitCommandSet = False
        
        self.setPostDownCommand(None)
        self.postDownCommandSet = False
        
        
        if self.statusObj:
            self.statusObj.clearAllSet()
        
        if self.countersObj:
            self.countersObj.clearAllSet()
        

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

    def newStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-status').debug3Func(): logFunc('called.')
        status = BlinkyStatusMaapi(self._log)
        status.init(self.domain)
        return status

    def setStatusObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-status').debug3Func(): logFunc('called. obj=%s', obj)
        self.statusObj = obj

    def getStatusObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-status').debug3Func(): logFunc('called. self.statusObj=%s', self.statusObj)
        return self.statusObj

    def hasStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-status').debug3Func(): logFunc('called. self.statusObj=%s', self.statusObj)
        if self.statusObj:
            return True
        return False

    def newCounters (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-counters').debug3Func(): logFunc('called.')
        counters = BlinkyCountersMaapi(self._log)
        counters.init(self.domain)
        return counters

    def setCountersObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-counters').debug3Func(): logFunc('called. obj=%s', obj)
        self.countersObj = obj

    def getCountersObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-counters').debug3Func(): logFunc('called. self.countersObj=%s', self.countersObj)
        return self.countersObj

    def hasCounters (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-counters').debug3Func(): logFunc('called. self.countersObj=%s', self.countersObj)
        if self.countersObj:
            return True
        return False



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

    def requestPostUpCommand (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-postupcommand').debug3Func(): logFunc('called. requested=%s', requested)
        self.postUpCommandRequested = requested
        self.postUpCommandSet = False

    def isPostUpCommandRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-postupcommand-requested').debug3Func(): logFunc('called. requested=%s', self.postUpCommandRequested)
        return self.postUpCommandRequested

    def getPostUpCommand (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-postupcommand').debug3Func(): logFunc('called. self.postUpCommandSet=%s, self.postUpCommand=%s', self.postUpCommandSet, self.postUpCommand)
        if self.postUpCommandSet:
            return self.postUpCommand
        return None

    def hasPostUpCommand (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-postupcommand').debug3Func(): logFunc('called. self.postUpCommandSet=%s, self.postUpCommand=%s', self.postUpCommandSet, self.postUpCommand)
        if self.postUpCommandSet:
            return True
        return False

    def setPostUpCommand (self, postUpCommand):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-postupcommand').debug3Func(): logFunc('called. postUpCommand=%s, old=%s', postUpCommand, self.postUpCommand)
        self.postUpCommandSet = True
        self.postUpCommand = postUpCommand

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

    def requestPostInitCommand (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-postinitcommand').debug3Func(): logFunc('called. requested=%s', requested)
        self.postInitCommandRequested = requested
        self.postInitCommandSet = False

    def isPostInitCommandRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-postinitcommand-requested').debug3Func(): logFunc('called. requested=%s', self.postInitCommandRequested)
        return self.postInitCommandRequested

    def getPostInitCommand (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-postinitcommand').debug3Func(): logFunc('called. self.postInitCommandSet=%s, self.postInitCommand=%s', self.postInitCommandSet, self.postInitCommand)
        if self.postInitCommandSet:
            return self.postInitCommand
        return None

    def hasPostInitCommand (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-postinitcommand').debug3Func(): logFunc('called. self.postInitCommandSet=%s, self.postInitCommand=%s', self.postInitCommandSet, self.postInitCommand)
        if self.postInitCommandSet:
            return True
        return False

    def setPostInitCommand (self, postInitCommand):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-postinitcommand').debug3Func(): logFunc('called. postInitCommand=%s, old=%s', postInitCommand, self.postInitCommand)
        self.postInitCommandSet = True
        self.postInitCommand = postInitCommand

    def requestPostDownCommand (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-postdowncommand').debug3Func(): logFunc('called. requested=%s', requested)
        self.postDownCommandRequested = requested
        self.postDownCommandSet = False

    def isPostDownCommandRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-postdowncommand-requested').debug3Func(): logFunc('called. requested=%s', self.postDownCommandRequested)
        return self.postDownCommandRequested

    def getPostDownCommand (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-postdowncommand').debug3Func(): logFunc('called. self.postDownCommandSet=%s, self.postDownCommand=%s', self.postDownCommandSet, self.postDownCommand)
        if self.postDownCommandSet:
            return self.postDownCommand
        return None

    def hasPostDownCommand (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-postdowncommand').debug3Func(): logFunc('called. self.postDownCommandSet=%s, self.postDownCommand=%s', self.postDownCommandSet, self.postDownCommand)
        if self.postDownCommandSet:
            return True
        return False

    def setPostDownCommand (self, postDownCommand):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-postdowncommand').debug3Func(): logFunc('called. postDownCommand=%s, old=%s', postDownCommand, self.postDownCommand)
        self.postDownCommandSet = True
        self.postDownCommand = postDownCommand


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.statusObj:
            self.statusObj._clearAllReadData()
        
        if self.countersObj:
            self.countersObj._clearAllReadData()
        

        
        self.osName = 0
        self.osNameSet = False
        
        self.pciDeviceId = 0
        self.pciDeviceIdSet = False
        
        self.pciVendorId = 0
        self.pciVendorIdSet = False
        
        self.postUpCommand = 0
        self.postUpCommandSet = False
        
        self.countersClearEvent = 0
        self.countersClearEventSet = False
        
        self.pciIndex = 0
        self.pciIndexSet = False
        
        self.postInitCommand = 0
        self.postInitCommandSet = False
        
        self.postDownCommand = 0
        self.postDownCommandSet = False
        

    def _getSelfKeyPath (self, interface
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("device", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
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

        
        if self.statusObj:
            res = self.statusObj._collectItemsToDelete(interface, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-status-failed').errorFunc(): logFunc('statusObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.countersObj:
            res = self.countersObj._collectItemsToDelete(interface, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-counters-failed').errorFunc(): logFunc('countersObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasOsName():
            valOsName = Value()
            if self.osName is not None:
                valOsName.setString(self.osName)
            else:
                valOsName.setEmpty()
            tagValueList.push(("os-name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valOsName)
        
        if self.hasPciDeviceId():
            valPciDeviceId = Value()
            if self.pciDeviceId is not None:
                valPciDeviceId.setString(self.pciDeviceId)
            else:
                valPciDeviceId.setEmpty()
            tagValueList.push(("pci-device-id", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valPciDeviceId)
        
        if self.hasPciVendorId():
            valPciVendorId = Value()
            if self.pciVendorId is not None:
                valPciVendorId.setString(self.pciVendorId)
            else:
                valPciVendorId.setEmpty()
            tagValueList.push(("pci-vendor-id", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valPciVendorId)
        
        if self.hasPostUpCommand():
            valPostUpCommand = Value()
            if self.postUpCommand is not None:
                valPostUpCommand.setString(self.postUpCommand)
            else:
                valPostUpCommand.setEmpty()
            tagValueList.push(("post-up-command", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valPostUpCommand)
        
        if self.hasCountersClearEvent():
            valCountersClearEvent = Value()
            if self.countersClearEvent is not None:
                valCountersClearEvent.setEnum(self.countersClearEvent.getValue())
            else:
                valCountersClearEvent.setEmpty()
            tagValueList.push(("counters-clear-event", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valCountersClearEvent)
        
        if self.hasPciIndex():
            valPciIndex = Value()
            if self.pciIndex is not None:
                valPciIndex.setUint64(self.pciIndex)
            else:
                valPciIndex.setEmpty()
            tagValueList.push(("pci-index", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valPciIndex)
        
        if self.hasPostInitCommand():
            valPostInitCommand = Value()
            if self.postInitCommand is not None:
                valPostInitCommand.setString(self.postInitCommand)
            else:
                valPostInitCommand.setEmpty()
            tagValueList.push(("post-init-command", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valPostInitCommand)
        
        if self.hasPostDownCommand():
            valPostDownCommand = Value()
            if self.postDownCommand is not None:
                valPostDownCommand.setString(self.postDownCommand)
            else:
                valPostDownCommand.setEmpty()
            tagValueList.push(("post-down-command", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valPostDownCommand)
        

        
        if self.statusObj:
            valBegin = Value()
            (tag, ns, prefix) = ("status" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.statusObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-status-failed').errorFunc(): logFunc('statusObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.countersObj:
            valBegin = Value()
            (tag, ns, prefix) = ("counters" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.countersObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-counters-failed').errorFunc(): logFunc('countersObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isOsNameRequested():
            valOsName = Value()
            valOsName.setEmpty()
            tagValueList.push(("os-name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valOsName)
        
        if self.isPciDeviceIdRequested():
            valPciDeviceId = Value()
            valPciDeviceId.setEmpty()
            tagValueList.push(("pci-device-id", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valPciDeviceId)
        
        if self.isPciVendorIdRequested():
            valPciVendorId = Value()
            valPciVendorId.setEmpty()
            tagValueList.push(("pci-vendor-id", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valPciVendorId)
        
        if self.isPostUpCommandRequested():
            valPostUpCommand = Value()
            valPostUpCommand.setEmpty()
            tagValueList.push(("post-up-command", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valPostUpCommand)
        
        if self.isCountersClearEventRequested():
            valCountersClearEvent = Value()
            valCountersClearEvent.setEmpty()
            tagValueList.push(("counters-clear-event", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valCountersClearEvent)
        
        if self.isPciIndexRequested():
            valPciIndex = Value()
            valPciIndex.setEmpty()
            tagValueList.push(("pci-index", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valPciIndex)
        
        if self.isPostInitCommandRequested():
            valPostInitCommand = Value()
            valPostInitCommand.setEmpty()
            tagValueList.push(("post-init-command", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valPostInitCommand)
        
        if self.isPostDownCommandRequested():
            valPostDownCommand = Value()
            valPostDownCommand.setEmpty()
            tagValueList.push(("post-down-command", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valPostDownCommand)
        

        
        if self.statusObj:
            valBegin = Value()
            (tag, ns, prefix) = ("status" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.statusObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-status-failed').errorFunc(): logFunc('statusObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.countersObj:
            valBegin = Value()
            (tag, ns, prefix) = ("counters" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.countersObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-counters-failed').errorFunc(): logFunc('countersObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
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
        
        if self.isPostUpCommandRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "post-up-command") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-postupcommand').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "postUpCommand", "post-up-command", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-post-up-command-bad-value').infoFunc(): logFunc('postUpCommand not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPostUpCommand(tempVar)
            for logFunc in self._log('read-tag-values-post-up-command').debug3Func(): logFunc('read postUpCommand. postUpCommand=%s, tempValue=%s', self.postUpCommand, tempValue.getType())
        
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
        
        if self.isPostInitCommandRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "post-init-command") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-postinitcommand').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "postInitCommand", "post-init-command", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-post-init-command-bad-value').infoFunc(): logFunc('postInitCommand not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPostInitCommand(tempVar)
            for logFunc in self._log('read-tag-values-post-init-command').debug3Func(): logFunc('read postInitCommand. postInitCommand=%s, tempValue=%s', self.postInitCommand, tempValue.getType())
        
        if self.isPostDownCommandRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "post-down-command") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-postdowncommand').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "postDownCommand", "post-down-command", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-post-down-command-bad-value').infoFunc(): logFunc('postDownCommand not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPostDownCommand(tempVar)
            for logFunc in self._log('read-tag-values-post-down-command').debug3Func(): logFunc('read postDownCommand. postDownCommand=%s, tempValue=%s', self.postDownCommand, tempValue.getType())
        

        
        if self.statusObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "status") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.statusObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-status-failed').errorFunc(): logFunc('statusObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "status") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.countersObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "counters") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "counters", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.countersObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-counters-failed').errorFunc(): logFunc('countersObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "counters") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "counters", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "device", 
        "namespace": "device", 
        "className": "DeviceMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.device.device_maapi_gen import DeviceMaapi", 
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
            "yangName": "device", 
            "namespace": "device", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "device"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "memberName": "status", 
            "yangName": "status", 
            "className": "BlinkyStatusMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.device.status.status_maapi_gen import BlinkyStatusMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "memberName": "counters", 
            "yangName": "counters", 
            "className": "BlinkyCountersMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.device.counters.counters_maapi_gen import BlinkyCountersMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "osName", 
            "yangName": "os-name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "pciDeviceId", 
            "yangName": "pci-device-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "pciVendorId", 
            "yangName": "pci-vendor-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "postUpCommand", 
            "yangName": "post-up-command", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
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
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pciIndex", 
            "yangName": "pci-index", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "postInitCommand", 
            "yangName": "post-init-command", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "postDownCommand", 
            "yangName": "post-down-command", 
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
            "common", 
            "qwilt_tech_interfaces"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "osName", 
            "yangName": "os-name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "pciDeviceId", 
            "yangName": "pci-device-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "pciVendorId", 
            "yangName": "pci-vendor-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "postUpCommand", 
            "yangName": "post-up-command", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
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
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pciIndex", 
            "yangName": "pci-index", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "postInitCommand", 
            "yangName": "post-init-command", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "postDownCommand", 
            "yangName": "post-down-command", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


