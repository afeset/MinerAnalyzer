


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

from link_maapi_base_gen import LinkMaapiBase




class BlinkyLinkMaapi(LinkMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-link")
        self.domain = None

        

        
        self.testTimeoutMsecRequested = False
        self.testTimeoutMsec = None
        self.testTimeoutMsecSet = False
        
        self.testIntervalMsecRequested = False
        self.testIntervalMsec = None
        self.testIntervalMsecSet = False
        
        self.upPeriodRequested = False
        self.upPeriod = None
        self.upPeriodSet = False
        
        self.downPeriodRequested = False
        self.downPeriod = None
        self.downPeriodSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestTestTimeoutMsec(True)
        
        self.requestTestIntervalMsec(True)
        
        self.requestUpPeriod(True)
        
        self.requestDownPeriod(True)
        
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestTestTimeoutMsec(True)
        
        self.requestTestIntervalMsec(True)
        
        self.requestUpPeriod(True)
        
        self.requestDownPeriod(True)
        
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestTestTimeoutMsec(False)
        
        self.requestTestIntervalMsec(False)
        
        self.requestUpPeriod(False)
        
        self.requestDownPeriod(False)
        
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestTestTimeoutMsec(False)
        
        self.requestTestIntervalMsec(False)
        
        self.requestUpPeriod(False)
        
        self.requestDownPeriod(False)
        
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setTestTimeoutMsec(None)
        self.testTimeoutMsecSet = False
        
        self.setTestIntervalMsec(None)
        self.testIntervalMsecSet = False
        
        self.setUpPeriod(None)
        self.upPeriodSet = False
        
        self.setDownPeriod(None)
        self.downPeriodSet = False
        
        

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



    def requestTestTimeoutMsec (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-testtimeoutmsec').debug3Func(): logFunc('called. requested=%s', requested)
        self.testTimeoutMsecRequested = requested
        self.testTimeoutMsecSet = False

    def isTestTimeoutMsecRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-testtimeoutmsec-requested').debug3Func(): logFunc('called. requested=%s', self.testTimeoutMsecRequested)
        return self.testTimeoutMsecRequested

    def getTestTimeoutMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-testtimeoutmsec').debug3Func(): logFunc('called. self.testTimeoutMsecSet=%s, self.testTimeoutMsec=%s', self.testTimeoutMsecSet, self.testTimeoutMsec)
        if self.testTimeoutMsecSet:
            return self.testTimeoutMsec
        return None

    def hasTestTimeoutMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-testtimeoutmsec').debug3Func(): logFunc('called. self.testTimeoutMsecSet=%s, self.testTimeoutMsec=%s', self.testTimeoutMsecSet, self.testTimeoutMsec)
        if self.testTimeoutMsecSet:
            return True
        return False

    def setTestTimeoutMsec (self, testTimeoutMsec):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-testtimeoutmsec').debug3Func(): logFunc('called. testTimeoutMsec=%s, old=%s', testTimeoutMsec, self.testTimeoutMsec)
        self.testTimeoutMsecSet = True
        self.testTimeoutMsec = testTimeoutMsec

    def requestTestIntervalMsec (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-testintervalmsec').debug3Func(): logFunc('called. requested=%s', requested)
        self.testIntervalMsecRequested = requested
        self.testIntervalMsecSet = False

    def isTestIntervalMsecRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-testintervalmsec-requested').debug3Func(): logFunc('called. requested=%s', self.testIntervalMsecRequested)
        return self.testIntervalMsecRequested

    def getTestIntervalMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-testintervalmsec').debug3Func(): logFunc('called. self.testIntervalMsecSet=%s, self.testIntervalMsec=%s', self.testIntervalMsecSet, self.testIntervalMsec)
        if self.testIntervalMsecSet:
            return self.testIntervalMsec
        return None

    def hasTestIntervalMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-testintervalmsec').debug3Func(): logFunc('called. self.testIntervalMsecSet=%s, self.testIntervalMsec=%s', self.testIntervalMsecSet, self.testIntervalMsec)
        if self.testIntervalMsecSet:
            return True
        return False

    def setTestIntervalMsec (self, testIntervalMsec):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-testintervalmsec').debug3Func(): logFunc('called. testIntervalMsec=%s, old=%s', testIntervalMsec, self.testIntervalMsec)
        self.testIntervalMsecSet = True
        self.testIntervalMsec = testIntervalMsec

    def requestUpPeriod (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-upperiod').debug3Func(): logFunc('called. requested=%s', requested)
        self.upPeriodRequested = requested
        self.upPeriodSet = False

    def isUpPeriodRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-upperiod-requested').debug3Func(): logFunc('called. requested=%s', self.upPeriodRequested)
        return self.upPeriodRequested

    def getUpPeriod (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-upperiod').debug3Func(): logFunc('called. self.upPeriodSet=%s, self.upPeriod=%s', self.upPeriodSet, self.upPeriod)
        if self.upPeriodSet:
            return self.upPeriod
        return None

    def hasUpPeriod (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-upperiod').debug3Func(): logFunc('called. self.upPeriodSet=%s, self.upPeriod=%s', self.upPeriodSet, self.upPeriod)
        if self.upPeriodSet:
            return True
        return False

    def setUpPeriod (self, upPeriod):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-upperiod').debug3Func(): logFunc('called. upPeriod=%s, old=%s', upPeriod, self.upPeriod)
        self.upPeriodSet = True
        self.upPeriod = upPeriod

    def requestDownPeriod (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-downperiod').debug3Func(): logFunc('called. requested=%s', requested)
        self.downPeriodRequested = requested
        self.downPeriodSet = False

    def isDownPeriodRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-downperiod-requested').debug3Func(): logFunc('called. requested=%s', self.downPeriodRequested)
        return self.downPeriodRequested

    def getDownPeriod (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-downperiod').debug3Func(): logFunc('called. self.downPeriodSet=%s, self.downPeriod=%s', self.downPeriodSet, self.downPeriod)
        if self.downPeriodSet:
            return self.downPeriod
        return None

    def hasDownPeriod (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-downperiod').debug3Func(): logFunc('called. self.downPeriodSet=%s, self.downPeriod=%s', self.downPeriodSet, self.downPeriod)
        if self.downPeriodSet:
            return True
        return False

    def setDownPeriod (self, downPeriod):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-downperiod').debug3Func(): logFunc('called. downPeriod=%s, old=%s', downPeriod, self.downPeriod)
        self.downPeriodSet = True
        self.downPeriod = downPeriod


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.testTimeoutMsec = 0
        self.testTimeoutMsecSet = False
        
        self.testIntervalMsec = 0
        self.testIntervalMsecSet = False
        
        self.upPeriod = 0
        self.upPeriodSet = False
        
        self.downPeriod = 0
        self.downPeriodSet = False
        

    def _getSelfKeyPath (self, interface
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("link", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
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

        
        if self.hasTestTimeoutMsec():
            valTestTimeoutMsec = Value()
            if self.testTimeoutMsec is not None:
                valTestTimeoutMsec.setInt64(self.testTimeoutMsec)
            else:
                valTestTimeoutMsec.setEmpty()
            tagValueList.push(("test-timeout-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valTestTimeoutMsec)
        
        if self.hasTestIntervalMsec():
            valTestIntervalMsec = Value()
            if self.testIntervalMsec is not None:
                valTestIntervalMsec.setInt64(self.testIntervalMsec)
            else:
                valTestIntervalMsec.setEmpty()
            tagValueList.push(("test-interval-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valTestIntervalMsec)
        
        if self.hasUpPeriod():
            valUpPeriod = Value()
            if self.upPeriod is not None:
                valUpPeriod.setInt64(self.upPeriod)
            else:
                valUpPeriod.setEmpty()
            tagValueList.push(("up-period", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valUpPeriod)
        
        if self.hasDownPeriod():
            valDownPeriod = Value()
            if self.downPeriod is not None:
                valDownPeriod.setInt64(self.downPeriod)
            else:
                valDownPeriod.setEmpty()
            tagValueList.push(("down-period", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valDownPeriod)
        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isTestTimeoutMsecRequested():
            valTestTimeoutMsec = Value()
            valTestTimeoutMsec.setEmpty()
            tagValueList.push(("test-timeout-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valTestTimeoutMsec)
        
        if self.isTestIntervalMsecRequested():
            valTestIntervalMsec = Value()
            valTestIntervalMsec.setEmpty()
            tagValueList.push(("test-interval-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valTestIntervalMsec)
        
        if self.isUpPeriodRequested():
            valUpPeriod = Value()
            valUpPeriod.setEmpty()
            tagValueList.push(("up-period", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valUpPeriod)
        
        if self.isDownPeriodRequested():
            valDownPeriod = Value()
            valDownPeriod.setEmpty()
            tagValueList.push(("down-period", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valDownPeriod)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isTestTimeoutMsecRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "test-timeout-msec") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-testtimeoutmsec').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "testTimeoutMsec", "test-timeout-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-test-timeout-msec-bad-value').infoFunc(): logFunc('testTimeoutMsec not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTestTimeoutMsec(tempVar)
            for logFunc in self._log('read-tag-values-test-timeout-msec').debug3Func(): logFunc('read testTimeoutMsec. testTimeoutMsec=%s, tempValue=%s', self.testTimeoutMsec, tempValue.getType())
        
        if self.isTestIntervalMsecRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "test-interval-msec") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-testintervalmsec').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "testIntervalMsec", "test-interval-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-test-interval-msec-bad-value').infoFunc(): logFunc('testIntervalMsec not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTestIntervalMsec(tempVar)
            for logFunc in self._log('read-tag-values-test-interval-msec').debug3Func(): logFunc('read testIntervalMsec. testIntervalMsec=%s, tempValue=%s', self.testIntervalMsec, tempValue.getType())
        
        if self.isUpPeriodRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "up-period") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-upperiod').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "upPeriod", "up-period", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-up-period-bad-value').infoFunc(): logFunc('upPeriod not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setUpPeriod(tempVar)
            for logFunc in self._log('read-tag-values-up-period').debug3Func(): logFunc('read upPeriod. upPeriod=%s, tempValue=%s', self.upPeriod, tempValue.getType())
        
        if self.isDownPeriodRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "down-period") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-downperiod').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "downPeriod", "down-period", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-down-period-bad-value').infoFunc(): logFunc('downPeriod not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setDownPeriod(tempVar)
            for logFunc in self._log('read-tag-values-down-period').debug3Func(): logFunc('read downPeriod. downPeriod=%s, tempValue=%s', self.downPeriod, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "link", 
        "namespace": "link", 
        "className": "LinkMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.system_defaults.link.link_maapi_gen import LinkMaapi", 
        "baseClassName": "LinkMaapiBase", 
        "baseModule": "link_maapi_base_gen"
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
            "yangName": "link", 
            "namespace": "link", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "link"
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
            "typeHandler": "handler: IntHandler", 
            "memberName": "testTimeoutMsec", 
            "yangName": "test-timeout-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "500", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "testIntervalMsec", 
            "yangName": "test-interval-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "1000", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "upPeriod", 
            "yangName": "up-period", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "10", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "downPeriod", 
            "yangName": "down-period", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "5", 
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
            "typeHandler": "handler: IntHandler", 
            "memberName": "testTimeoutMsec", 
            "yangName": "test-timeout-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "500", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "testIntervalMsec", 
            "yangName": "test-interval-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "1000", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "upPeriod", 
            "yangName": "up-period", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "10", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "downPeriod", 
            "yangName": "down-period", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "5", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


