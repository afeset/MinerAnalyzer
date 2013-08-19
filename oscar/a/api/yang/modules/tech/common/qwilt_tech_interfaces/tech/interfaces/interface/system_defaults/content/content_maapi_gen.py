


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

from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.system_defaults.content.delivery.delivery_maapi_gen import BlinkyDeliveryMaapi
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.system_defaults.content.analytics.analytics_maapi_gen import BlinkyAnalyticsMaapi
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.system_defaults.content.acquisition.acquisition_maapi_gen import BlinkyAcquisitionMaapi



class BlinkyContentMaapi(ContentMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-content")
        self.domain = None

        
        self.deliveryObj = None
        
        self.analyticsObj = None
        
        self.acquisitionObj = None
        

        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        
        if not self.deliveryObj:
            self.deliveryObj = self.newDelivery()
            self.deliveryObj.requestConfigAndOper()
        
        if not self.analyticsObj:
            self.analyticsObj = self.newAnalytics()
            self.analyticsObj.requestConfigAndOper()
        
        if not self.acquisitionObj:
            self.acquisitionObj = self.newAcquisition()
            self.acquisitionObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        
        if not self.deliveryObj:
            self.deliveryObj = self.newDelivery()
            self.deliveryObj.requestConfig()
        
        if not self.analyticsObj:
            self.analyticsObj = self.newAnalytics()
            self.analyticsObj.requestConfig()
        
        if not self.acquisitionObj:
            self.acquisitionObj = self.newAcquisition()
            self.acquisitionObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        
        if not self.deliveryObj:
            self.deliveryObj = self.newDelivery()
            self.deliveryObj.requestOper()
        
        if not self.analyticsObj:
            self.analyticsObj = self.newAnalytics()
            self.analyticsObj.requestOper()
        
        if not self.acquisitionObj:
            self.acquisitionObj = self.newAcquisition()
            self.acquisitionObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        
        if not self.deliveryObj:
            self.deliveryObj = self.newDelivery()
            self.deliveryObj.clearAllRequested()
        
        if not self.analyticsObj:
            self.analyticsObj = self.newAnalytics()
            self.analyticsObj.clearAllRequested()
        
        if not self.acquisitionObj:
            self.acquisitionObj = self.newAcquisition()
            self.acquisitionObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        
        if self.deliveryObj:
            self.deliveryObj.clearAllSet()
        
        if self.analyticsObj:
            self.analyticsObj.clearAllSet()
        
        if self.acquisitionObj:
            self.acquisitionObj.clearAllSet()
        

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

    def newAnalytics (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-analytics').debug3Func(): logFunc('called.')
        analytics = BlinkyAnalyticsMaapi(self._log)
        analytics.init(self.domain)
        return analytics

    def setAnalyticsObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-analytics').debug3Func(): logFunc('called. obj=%s', obj)
        self.analyticsObj = obj

    def getAnalyticsObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-analytics').debug3Func(): logFunc('called. self.analyticsObj=%s', self.analyticsObj)
        return self.analyticsObj

    def hasAnalytics (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-analytics').debug3Func(): logFunc('called. self.analyticsObj=%s', self.analyticsObj)
        if self.analyticsObj:
            return True
        return False

    def newAcquisition (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-acquisition').debug3Func(): logFunc('called.')
        acquisition = BlinkyAcquisitionMaapi(self._log)
        acquisition.init(self.domain)
        return acquisition

    def setAcquisitionObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-acquisition').debug3Func(): logFunc('called. obj=%s', obj)
        self.acquisitionObj = obj

    def getAcquisitionObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-acquisition').debug3Func(): logFunc('called. self.acquisitionObj=%s', self.acquisitionObj)
        return self.acquisitionObj

    def hasAcquisition (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-acquisition').debug3Func(): logFunc('called. self.acquisitionObj=%s', self.acquisitionObj)
        if self.acquisitionObj:
            return True
        return False




    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.deliveryObj:
            self.deliveryObj._clearAllReadData()
        
        if self.analyticsObj:
            self.analyticsObj._clearAllReadData()
        
        if self.acquisitionObj:
            self.acquisitionObj._clearAllReadData()
        

        

    def _getSelfKeyPath (self, interface
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("content", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
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

        
        if self.deliveryObj:
            res = self.deliveryObj._collectItemsToDelete(interface, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-delivery-failed').errorFunc(): logFunc('deliveryObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.analyticsObj:
            res = self.analyticsObj._collectItemsToDelete(interface, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-analytics-failed').errorFunc(): logFunc('analyticsObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.acquisitionObj:
            res = self.acquisitionObj._collectItemsToDelete(interface, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-acquisition-failed').errorFunc(): logFunc('acquisitionObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        

        
        if self.deliveryObj:
            valBegin = Value()
            (tag, ns, prefix) = ("delivery" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
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
        
        if self.analyticsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("analytics" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.analyticsObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-analytics-failed').errorFunc(): logFunc('analyticsObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.acquisitionObj:
            valBegin = Value()
            (tag, ns, prefix) = ("acquisition" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.acquisitionObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-acquisition-failed').errorFunc(): logFunc('acquisitionObj._fillWriteTagValues() failed. PARAMS')
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

        

        
        if self.deliveryObj:
            valBegin = Value()
            (tag, ns, prefix) = ("delivery" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
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
        
        if self.analyticsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("analytics" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.analyticsObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-analytics-failed').errorFunc(): logFunc('analyticsObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.acquisitionObj:
            valBegin = Value()
            (tag, ns, prefix) = ("acquisition" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.acquisitionObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-acquisition-failed').errorFunc(): logFunc('acquisitionObj._fillReadTagValues() failed. PARAMS')
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
        

        
        if self.deliveryObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "delivery") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "delivery", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlBegin,
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
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "delivery", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.analyticsObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "analytics") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "analytics", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.analyticsObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-analytics-failed').errorFunc(): logFunc('analyticsObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "analytics") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "analytics", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.acquisitionObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "acquisition") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "acquisition", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.acquisitionObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-acquisition-failed').errorFunc(): logFunc('acquisitionObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "acquisition") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "acquisition", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlEnd,
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
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.system_defaults.content.content_maapi_gen import ContentMaapi", 
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
            "yangName": "content", 
            "namespace": "content", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "content"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "memberName": "delivery", 
            "yangName": "delivery", 
            "className": "BlinkyDeliveryMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.system_defaults.content.delivery.delivery_maapi_gen import BlinkyDeliveryMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "memberName": "analytics", 
            "yangName": "analytics", 
            "className": "BlinkyAnalyticsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.system_defaults.content.analytics.analytics_maapi_gen import BlinkyAnalyticsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "memberName": "acquisition", 
            "yangName": "acquisition", 
            "className": "BlinkyAcquisitionMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.system_defaults.content.acquisition.acquisition_maapi_gen import BlinkyAcquisitionMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"
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
            "common", 
            "qwilt_tech_interfaces"
        ]
    }, 
    "leaves": [], 
    "createTime": "2013"
}
"""


