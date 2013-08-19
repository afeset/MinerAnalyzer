


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

from action_maapi_base_gen import ActionMaapiBase




class BlinkyActionMaapi(ActionMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-action")
        self.domain = None

        

        
        self.deliveryRequested = False
        self.delivery = None
        self.deliverySet = False
        
        self.analyticsRequested = False
        self.analytics = None
        self.analyticsSet = False
        
        self.cachingPotentialRequested = False
        self.cachingPotential = None
        self.cachingPotentialSet = False
        
        self.acquisitionRequested = False
        self.acquisition = None
        self.acquisitionSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestDelivery(True)
        
        self.requestAnalytics(True)
        
        self.requestCachingPotential(True)
        
        self.requestAcquisition(True)
        
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestDelivery(True)
        
        self.requestAnalytics(True)
        
        self.requestCachingPotential(True)
        
        self.requestAcquisition(True)
        
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestDelivery(False)
        
        self.requestAnalytics(False)
        
        self.requestCachingPotential(False)
        
        self.requestAcquisition(False)
        
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestDelivery(False)
        
        self.requestAnalytics(False)
        
        self.requestCachingPotential(False)
        
        self.requestAcquisition(False)
        
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setDelivery(None)
        self.deliverySet = False
        
        self.setAnalytics(None)
        self.analyticsSet = False
        
        self.setCachingPotential(None)
        self.cachingPotentialSet = False
        
        self.setAcquisition(None)
        self.acquisitionSet = False
        
        

    def write (self
              , rule
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(rule, trxContext)

    def read (self
              , rule
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(rule, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , rule
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(rule, 
                                  True,
                                  trxContext)



    def requestDelivery (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-delivery').debug3Func(): logFunc('called. requested=%s', requested)
        self.deliveryRequested = requested
        self.deliverySet = False

    def isDeliveryRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-delivery-requested').debug3Func(): logFunc('called. requested=%s', self.deliveryRequested)
        return self.deliveryRequested

    def getDelivery (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-delivery').debug3Func(): logFunc('called. self.deliverySet=%s, self.delivery=%s', self.deliverySet, self.delivery)
        if self.deliverySet:
            return self.delivery
        return None

    def hasDelivery (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-delivery').debug3Func(): logFunc('called. self.deliverySet=%s, self.delivery=%s', self.deliverySet, self.delivery)
        if self.deliverySet:
            return True
        return False

    def setDelivery (self, delivery):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-delivery').debug3Func(): logFunc('called. delivery=%s, old=%s', delivery, self.delivery)
        self.deliverySet = True
        self.delivery = delivery

    def requestAnalytics (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-analytics').debug3Func(): logFunc('called. requested=%s', requested)
        self.analyticsRequested = requested
        self.analyticsSet = False

    def isAnalyticsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-analytics-requested').debug3Func(): logFunc('called. requested=%s', self.analyticsRequested)
        return self.analyticsRequested

    def getAnalytics (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-analytics').debug3Func(): logFunc('called. self.analyticsSet=%s, self.analytics=%s', self.analyticsSet, self.analytics)
        if self.analyticsSet:
            return self.analytics
        return None

    def hasAnalytics (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-analytics').debug3Func(): logFunc('called. self.analyticsSet=%s, self.analytics=%s', self.analyticsSet, self.analytics)
        if self.analyticsSet:
            return True
        return False

    def setAnalytics (self, analytics):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-analytics').debug3Func(): logFunc('called. analytics=%s, old=%s', analytics, self.analytics)
        self.analyticsSet = True
        self.analytics = analytics

    def requestCachingPotential (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-cachingpotential').debug3Func(): logFunc('called. requested=%s', requested)
        self.cachingPotentialRequested = requested
        self.cachingPotentialSet = False

    def isCachingPotentialRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-cachingpotential-requested').debug3Func(): logFunc('called. requested=%s', self.cachingPotentialRequested)
        return self.cachingPotentialRequested

    def getCachingPotential (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-cachingpotential').debug3Func(): logFunc('called. self.cachingPotentialSet=%s, self.cachingPotential=%s', self.cachingPotentialSet, self.cachingPotential)
        if self.cachingPotentialSet:
            return self.cachingPotential
        return None

    def hasCachingPotential (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-cachingpotential').debug3Func(): logFunc('called. self.cachingPotentialSet=%s, self.cachingPotential=%s', self.cachingPotentialSet, self.cachingPotential)
        if self.cachingPotentialSet:
            return True
        return False

    def setCachingPotential (self, cachingPotential):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-cachingpotential').debug3Func(): logFunc('called. cachingPotential=%s, old=%s', cachingPotential, self.cachingPotential)
        self.cachingPotentialSet = True
        self.cachingPotential = cachingPotential

    def requestAcquisition (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-acquisition').debug3Func(): logFunc('called. requested=%s', requested)
        self.acquisitionRequested = requested
        self.acquisitionSet = False

    def isAcquisitionRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-acquisition-requested').debug3Func(): logFunc('called. requested=%s', self.acquisitionRequested)
        return self.acquisitionRequested

    def getAcquisition (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-acquisition').debug3Func(): logFunc('called. self.acquisitionSet=%s, self.acquisition=%s', self.acquisitionSet, self.acquisition)
        if self.acquisitionSet:
            return self.acquisition
        return None

    def hasAcquisition (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-acquisition').debug3Func(): logFunc('called. self.acquisitionSet=%s, self.acquisition=%s', self.acquisitionSet, self.acquisition)
        if self.acquisitionSet:
            return True
        return False

    def setAcquisition (self, acquisition):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-acquisition').debug3Func(): logFunc('called. acquisition=%s, old=%s', acquisition, self.acquisition)
        self.acquisitionSet = True
        self.acquisition = acquisition


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.delivery = 0
        self.deliverySet = False
        
        self.analytics = 0
        self.analyticsSet = False
        
        self.cachingPotential = 0
        self.cachingPotentialSet = False
        
        self.acquisition = 0
        self.acquisitionSet = False
        

    def _getSelfKeyPath (self, rule
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("action", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("actions", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(rule);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("rule", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("rules", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("policy", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("content", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        rule, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(rule, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(rule, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       rule, 
                       
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

        keyPath = self._getSelfKeyPath(rule, 
                                       
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
                               rule, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasDelivery():
            valDelivery = Value()
            if self.delivery is not None:
                valDelivery.setBool(self.delivery)
            else:
                valDelivery.setEmpty()
            tagValueList.push(("delivery", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"), valDelivery)
        
        if self.hasAnalytics():
            valAnalytics = Value()
            if self.analytics is not None:
                valAnalytics.setBool(self.analytics)
            else:
                valAnalytics.setEmpty()
            tagValueList.push(("analytics", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"), valAnalytics)
        
        if self.hasCachingPotential():
            valCachingPotential = Value()
            if self.cachingPotential is not None:
                valCachingPotential.setBool(self.cachingPotential)
            else:
                valCachingPotential.setEmpty()
            tagValueList.push(("caching-potential", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"), valCachingPotential)
        
        if self.hasAcquisition():
            valAcquisition = Value()
            if self.acquisition is not None:
                valAcquisition.setBool(self.acquisition)
            else:
                valAcquisition.setEmpty()
            tagValueList.push(("acquisition", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"), valAcquisition)
        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isDeliveryRequested():
            valDelivery = Value()
            valDelivery.setEmpty()
            tagValueList.push(("delivery", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"), valDelivery)
        
        if self.isAnalyticsRequested():
            valAnalytics = Value()
            valAnalytics.setEmpty()
            tagValueList.push(("analytics", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"), valAnalytics)
        
        if self.isCachingPotentialRequested():
            valCachingPotential = Value()
            valCachingPotential.setEmpty()
            tagValueList.push(("caching-potential", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"), valCachingPotential)
        
        if self.isAcquisitionRequested():
            valAcquisition = Value()
            valAcquisition.setEmpty()
            tagValueList.push(("acquisition", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"), valAcquisition)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isDeliveryRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "delivery") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-delivery').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "delivery", "delivery", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-delivery-bad-value').infoFunc(): logFunc('delivery not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setDelivery(tempVar)
            for logFunc in self._log('read-tag-values-delivery').debug3Func(): logFunc('read delivery. delivery=%s, tempValue=%s', self.delivery, tempValue.getType())
        
        if self.isAnalyticsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "analytics") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-analytics').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "analytics", "analytics", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-analytics-bad-value').infoFunc(): logFunc('analytics not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setAnalytics(tempVar)
            for logFunc in self._log('read-tag-values-analytics').debug3Func(): logFunc('read analytics. analytics=%s, tempValue=%s', self.analytics, tempValue.getType())
        
        if self.isCachingPotentialRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "caching-potential") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-cachingpotential').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "cachingPotential", "caching-potential", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-caching-potential-bad-value').infoFunc(): logFunc('cachingPotential not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setCachingPotential(tempVar)
            for logFunc in self._log('read-tag-values-caching-potential').debug3Func(): logFunc('read cachingPotential. cachingPotential=%s, tempValue=%s', self.cachingPotential, tempValue.getType())
        
        if self.isAcquisitionRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "acquisition") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-acquisition').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "acquisition", "acquisition", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-acquisition-bad-value').infoFunc(): logFunc('acquisition not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setAcquisition(tempVar)
            for logFunc in self._log('read-tag-values-acquisition').debug3Func(): logFunc('read acquisition. acquisition=%s, tempValue=%s', self.acquisition, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "action", 
        "namespace": "action", 
        "className": "ActionMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.policy.rules.rule.actions.action.action_maapi_gen import ActionMaapi", 
        "baseClassName": "ActionMaapiBase", 
        "baseModule": "action_maapi_base_gen"
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
            "yangName": "policy", 
            "namespace": "policy", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "name": "policy"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "yangName": "rules", 
            "namespace": "rules", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "name": "rules"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "isCurrent": false, 
            "yangName": "rule", 
            "namespace": "rule", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "keyLeaf": {
                "varName": "rule", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "rule"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "yangName": "actions", 
            "namespace": "actions", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "name": "actions"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "yangName": "action", 
            "namespace": "action", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "name": "action"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "delivery", 
            "yangName": "delivery", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "analytics", 
            "yangName": "analytics", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "cachingPotential", 
            "yangName": "caching-potential", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "acquisition", 
            "yangName": "acquisition", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
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
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "delivery", 
            "yangName": "delivery", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "analytics", 
            "yangName": "analytics", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "cachingPotential", 
            "yangName": "caching-potential", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "acquisition", 
            "yangName": "acquisition", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


