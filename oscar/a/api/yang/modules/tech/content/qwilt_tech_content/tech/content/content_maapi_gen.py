


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

from content_maapi_base_gen import ContentMaapiBase

from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.delivery.delivery_maapi_gen import BlinkyDeliveryMaapi
from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.signatures.signatures_maapi_gen import BlinkySignaturesMaapi
from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.zones.zones_maapi_gen import BlinkyZonesMaapi
from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.system_defaults.system_defaults_maapi_gen import BlinkySystemDefaultsMaapi
from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.policy.policy_maapi_gen import BlinkyPolicyMaapi



class BlinkyContentMaapi(ContentMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-content")
        self.domain = None

        
        self.deliveryObj = None
        
        self.signaturesObj = None
        
        self.zonesObj = None
        
        self.systemDefaultsObj = None
        
        self.policyObj = None
        

        
        self.tempJunkDescriptionTypeRequested = False
        self.tempJunkDescriptionType = None
        self.tempJunkDescriptionTypeSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestTempJunkDescriptionType(True)
        
        
        
        if not self.deliveryObj:
            self.deliveryObj = self.newDelivery()
            self.deliveryObj.requestConfigAndOper()
        
        if not self.signaturesObj:
            self.signaturesObj = self.newSignatures()
            self.signaturesObj.requestConfigAndOper()
        
        if not self.zonesObj:
            self.zonesObj = self.newZones()
            self.zonesObj.requestConfigAndOper()
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.requestConfigAndOper()
        
        if not self.policyObj:
            self.policyObj = self.newPolicy()
            self.policyObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestTempJunkDescriptionType(True)
        
        
        
        if not self.deliveryObj:
            self.deliveryObj = self.newDelivery()
            self.deliveryObj.requestConfig()
        
        if not self.signaturesObj:
            self.signaturesObj = self.newSignatures()
            self.signaturesObj.requestConfig()
        
        if not self.zonesObj:
            self.zonesObj = self.newZones()
            self.zonesObj.requestConfig()
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.requestConfig()
        
        if not self.policyObj:
            self.policyObj = self.newPolicy()
            self.policyObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestTempJunkDescriptionType(False)
        
        
        
        if not self.deliveryObj:
            self.deliveryObj = self.newDelivery()
            self.deliveryObj.requestOper()
        
        if not self.signaturesObj:
            self.signaturesObj = self.newSignatures()
            self.signaturesObj.requestOper()
        
        if not self.zonesObj:
            self.zonesObj = self.newZones()
            self.zonesObj.requestOper()
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.requestOper()
        
        if not self.policyObj:
            self.policyObj = self.newPolicy()
            self.policyObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestTempJunkDescriptionType(False)
        
        
        
        if not self.deliveryObj:
            self.deliveryObj = self.newDelivery()
            self.deliveryObj.clearAllRequested()
        
        if not self.signaturesObj:
            self.signaturesObj = self.newSignatures()
            self.signaturesObj.clearAllRequested()
        
        if not self.zonesObj:
            self.zonesObj = self.newZones()
            self.zonesObj.clearAllRequested()
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.clearAllRequested()
        
        if not self.policyObj:
            self.policyObj = self.newPolicy()
            self.policyObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setTempJunkDescriptionType(None)
        self.tempJunkDescriptionTypeSet = False
        
        
        if self.deliveryObj:
            self.deliveryObj.clearAllSet()
        
        if self.signaturesObj:
            self.signaturesObj.clearAllSet()
        
        if self.zonesObj:
            self.zonesObj.clearAllSet()
        
        if self.systemDefaultsObj:
            self.systemDefaultsObj.clearAllSet()
        
        if self.policyObj:
            self.policyObj.clearAllSet()
        

    def write (self
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(trxContext)

    def read (self
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(
                                  True,
                                  trxContext)

    def newDelivery (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-delivery').debug3Func(): logFunc('called.')
        delivery = BlinkyDeliveryMaapi(self._log)
        delivery.init(self.domain)
        return delivery

    def setDeliveryObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-delivery').debug3Func(): logFunc('called. obj=%s', obj)
        self.deliveryObj = obj

    def getDeliveryObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-delivery').debug3Func(): logFunc('called. self.deliveryObj=%s', self.deliveryObj)
        return self.deliveryObj

    def hasDelivery (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-delivery').debug3Func(): logFunc('called. self.deliveryObj=%s', self.deliveryObj)
        if self.deliveryObj:
            return True
        return False

    def newSignatures (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-signatures').debug3Func(): logFunc('called.')
        signatures = BlinkySignaturesMaapi(self._log)
        signatures.init(self.domain)
        return signatures

    def setSignaturesObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-signatures').debug3Func(): logFunc('called. obj=%s', obj)
        self.signaturesObj = obj

    def getSignaturesObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-signatures').debug3Func(): logFunc('called. self.signaturesObj=%s', self.signaturesObj)
        return self.signaturesObj

    def hasSignatures (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-signatures').debug3Func(): logFunc('called. self.signaturesObj=%s', self.signaturesObj)
        if self.signaturesObj:
            return True
        return False

    def newZones (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-zones').debug3Func(): logFunc('called.')
        zones = BlinkyZonesMaapi(self._log)
        zones.init(self.domain)
        return zones

    def setZonesObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-zones').debug3Func(): logFunc('called. obj=%s', obj)
        self.zonesObj = obj

    def getZonesObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-zones').debug3Func(): logFunc('called. self.zonesObj=%s', self.zonesObj)
        return self.zonesObj

    def hasZones (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-zones').debug3Func(): logFunc('called. self.zonesObj=%s', self.zonesObj)
        if self.zonesObj:
            return True
        return False

    def newSystemDefaults (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-systemdefaults').debug3Func(): logFunc('called.')
        systemDefaults = BlinkySystemDefaultsMaapi(self._log)
        systemDefaults.init(self.domain)
        return systemDefaults

    def setSystemDefaultsObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-systemdefaults').debug3Func(): logFunc('called. obj=%s', obj)
        self.systemDefaultsObj = obj

    def getSystemDefaultsObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-systemdefaults').debug3Func(): logFunc('called. self.systemDefaultsObj=%s', self.systemDefaultsObj)
        return self.systemDefaultsObj

    def hasSystemDefaults (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-systemdefaults').debug3Func(): logFunc('called. self.systemDefaultsObj=%s', self.systemDefaultsObj)
        if self.systemDefaultsObj:
            return True
        return False

    def newPolicy (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-policy').debug3Func(): logFunc('called.')
        policy = BlinkyPolicyMaapi(self._log)
        policy.init(self.domain)
        return policy

    def setPolicyObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-policy').debug3Func(): logFunc('called. obj=%s', obj)
        self.policyObj = obj

    def getPolicyObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-policy').debug3Func(): logFunc('called. self.policyObj=%s', self.policyObj)
        return self.policyObj

    def hasPolicy (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-policy').debug3Func(): logFunc('called. self.policyObj=%s', self.policyObj)
        if self.policyObj:
            return True
        return False



    def requestTempJunkDescriptionType (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-tempjunkdescriptiontype').debug3Func(): logFunc('called. requested=%s', requested)
        self.tempJunkDescriptionTypeRequested = requested
        self.tempJunkDescriptionTypeSet = False

    def isTempJunkDescriptionTypeRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-tempjunkdescriptiontype-requested').debug3Func(): logFunc('called. requested=%s', self.tempJunkDescriptionTypeRequested)
        return self.tempJunkDescriptionTypeRequested

    def getTempJunkDescriptionType (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-tempjunkdescriptiontype').debug3Func(): logFunc('called. self.tempJunkDescriptionTypeSet=%s, self.tempJunkDescriptionType=%s', self.tempJunkDescriptionTypeSet, self.tempJunkDescriptionType)
        if self.tempJunkDescriptionTypeSet:
            return self.tempJunkDescriptionType
        return None

    def hasTempJunkDescriptionType (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-tempjunkdescriptiontype').debug3Func(): logFunc('called. self.tempJunkDescriptionTypeSet=%s, self.tempJunkDescriptionType=%s', self.tempJunkDescriptionTypeSet, self.tempJunkDescriptionType)
        if self.tempJunkDescriptionTypeSet:
            return True
        return False

    def setTempJunkDescriptionType (self, tempJunkDescriptionType):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-tempjunkdescriptiontype').debug3Func(): logFunc('called. tempJunkDescriptionType=%s, old=%s', tempJunkDescriptionType, self.tempJunkDescriptionType)
        self.tempJunkDescriptionTypeSet = True
        self.tempJunkDescriptionType = tempJunkDescriptionType


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.deliveryObj:
            self.deliveryObj._clearAllReadData()
        
        if self.signaturesObj:
            self.signaturesObj._clearAllReadData()
        
        if self.zonesObj:
            self.zonesObj._clearAllReadData()
        
        if self.systemDefaultsObj:
            self.systemDefaultsObj._clearAllReadData()
        
        if self.policyObj:
            self.policyObj._clearAllReadData()
        

        
        self.tempJunkDescriptionType = 0
        self.tempJunkDescriptionTypeSet = False
        

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("content", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       
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

        keyPath = self._getSelfKeyPath(
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
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        
        if self.deliveryObj:
            res = self.deliveryObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-delivery-failed').errorFunc(): logFunc('deliveryObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.signaturesObj:
            res = self.signaturesObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-signatures-failed').errorFunc(): logFunc('signaturesObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.zonesObj:
            res = self.zonesObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-zones-failed').errorFunc(): logFunc('zonesObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.systemDefaultsObj:
            res = self.systemDefaultsObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.policyObj:
            res = self.policyObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-policy-failed').errorFunc(): logFunc('policyObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasTempJunkDescriptionType():
            valTempJunkDescriptionType = Value()
            if self.tempJunkDescriptionType is not None:
                valTempJunkDescriptionType.setString(self.tempJunkDescriptionType)
            else:
                valTempJunkDescriptionType.setEmpty()
            tagValueList.push(("temp-junk-description-type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"), valTempJunkDescriptionType)
        

        
        if self.deliveryObj:
            valBegin = Value()
            (tag, ns, prefix) = ("delivery" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.deliveryObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-delivery-failed').errorFunc(): logFunc('deliveryObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.signaturesObj:
            valBegin = Value()
            (tag, ns, prefix) = ("signatures" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.signaturesObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-signatures-failed').errorFunc(): logFunc('signaturesObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.zonesObj:
            valBegin = Value()
            (tag, ns, prefix) = ("zones" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.zonesObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-zones-failed').errorFunc(): logFunc('zonesObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.systemDefaultsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("system-defaults" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.systemDefaultsObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.policyObj:
            valBegin = Value()
            (tag, ns, prefix) = ("policy" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.policyObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-policy-failed').errorFunc(): logFunc('policyObj._fillWriteTagValues() failed. PARAMS')
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

        
        if self.isTempJunkDescriptionTypeRequested():
            valTempJunkDescriptionType = Value()
            valTempJunkDescriptionType.setEmpty()
            tagValueList.push(("temp-junk-description-type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"), valTempJunkDescriptionType)
        

        
        if self.deliveryObj:
            valBegin = Value()
            (tag, ns, prefix) = ("delivery" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.deliveryObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-delivery-failed').errorFunc(): logFunc('deliveryObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.signaturesObj:
            valBegin = Value()
            (tag, ns, prefix) = ("signatures" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.signaturesObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-signatures-failed').errorFunc(): logFunc('signaturesObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.zonesObj:
            valBegin = Value()
            (tag, ns, prefix) = ("zones" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.zonesObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-zones-failed').errorFunc(): logFunc('zonesObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.systemDefaultsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("system-defaults" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.systemDefaultsObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.policyObj:
            valBegin = Value()
            (tag, ns, prefix) = ("policy" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.policyObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-policy-failed').errorFunc(): logFunc('policyObj._fillReadTagValues() failed. PARAMS')
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
        
        if self.isTempJunkDescriptionTypeRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "temp-junk-description-type") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-tempjunkdescriptiontype').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "tempJunkDescriptionType", "temp-junk-description-type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-temp-junk-description-type-bad-value').infoFunc(): logFunc('tempJunkDescriptionType not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTempJunkDescriptionType(tempVar)
            for logFunc in self._log('read-tag-values-temp-junk-description-type').debug3Func(): logFunc('read tempJunkDescriptionType. tempJunkDescriptionType=%s, tempValue=%s', self.tempJunkDescriptionType, tempValue.getType())
        

        
        if self.deliveryObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "delivery") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "delivery", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.deliveryObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-delivery-failed').errorFunc(): logFunc('deliveryObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "delivery") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "delivery", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.signaturesObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "signatures") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "signatures", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.signaturesObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-signatures-failed').errorFunc(): logFunc('signaturesObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "signatures") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "signatures", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.zonesObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "zones") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "zones", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.zonesObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-zones-failed').errorFunc(): logFunc('zonesObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "zones") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "zones", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.systemDefaultsObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "system-defaults") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.systemDefaultsObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "system-defaults") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.policyObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "policy") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "policy", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.policyObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-policy-failed').errorFunc(): logFunc('policyObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "policy") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "policy", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "content", 
        "namespace": "content", 
        "className": "ContentMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.content_maapi_gen import ContentMaapi", 
        "baseClassName": "ContentMaapiBase", 
        "baseModule": "content_maapi_base_gen"
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
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "name": "content"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qtc", 
            "memberName": "delivery", 
            "yangName": "delivery", 
            "className": "BlinkyDeliveryMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.delivery.delivery_maapi_gen import BlinkyDeliveryMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "memberName": "signatures", 
            "yangName": "signatures", 
            "className": "BlinkySignaturesMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.signatures.signatures_maapi_gen import BlinkySignaturesMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "memberName": "zones", 
            "yangName": "zones", 
            "className": "BlinkyZonesMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.zones.zones_maapi_gen import BlinkyZonesMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "memberName": "systemDefaults", 
            "yangName": "system-defaults", 
            "className": "BlinkySystemDefaultsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.system_defaults.system_defaults_maapi_gen import BlinkySystemDefaultsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "memberName": "policy", 
            "yangName": "policy", 
            "className": "BlinkyPolicyMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.policy.policy_maapi_gen import BlinkyPolicyMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "tempJunkDescriptionType", 
            "yangName": "temp-junk-description-type", 
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
            "qwilt_tech_content"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "tempJunkDescriptionType", 
            "yangName": "temp-junk-description-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


