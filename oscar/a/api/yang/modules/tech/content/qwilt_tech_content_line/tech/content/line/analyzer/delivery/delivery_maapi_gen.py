


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

from delivery_maapi_base_gen import DeliveryMaapiBase

from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.analyzer.delivery.blocker.blocker_maapi_gen import BlinkyBlockerMaapi



class BlinkyDeliveryMaapi(DeliveryMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-delivery")
        self.domain = None

        
        self.blockerObj = None
        

        
        self.maxActiveConnectionsRequested = False
        self.maxActiveConnections = None
        self.maxActiveConnectionsSet = False
        
        self.enabledRequested = False
        self.enabled = None
        self.enabledSet = False
        
        self.maxRedirectRateRequested = False
        self.maxRedirectRate = None
        self.maxRedirectRateSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestMaxActiveConnections(True)
        
        self.requestEnabled(True)
        
        self.requestMaxRedirectRate(True)
        
        
        
        if not self.blockerObj:
            self.blockerObj = self.newBlocker()
            self.blockerObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestMaxActiveConnections(True)
        
        self.requestEnabled(True)
        
        self.requestMaxRedirectRate(True)
        
        
        
        if not self.blockerObj:
            self.blockerObj = self.newBlocker()
            self.blockerObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestMaxActiveConnections(False)
        
        self.requestEnabled(False)
        
        self.requestMaxRedirectRate(False)
        
        
        
        if not self.blockerObj:
            self.blockerObj = self.newBlocker()
            self.blockerObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestMaxActiveConnections(False)
        
        self.requestEnabled(False)
        
        self.requestMaxRedirectRate(False)
        
        
        
        if not self.blockerObj:
            self.blockerObj = self.newBlocker()
            self.blockerObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setMaxActiveConnections(None)
        self.maxActiveConnectionsSet = False
        
        self.setEnabled(None)
        self.enabledSet = False
        
        self.setMaxRedirectRate(None)
        self.maxRedirectRateSet = False
        
        
        if self.blockerObj:
            self.blockerObj.clearAllSet()
        

    def write (self
              , line
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(line, trxContext)

    def read (self
              , line
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(line, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , line
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(line, 
                                  True,
                                  trxContext)

    def newBlocker (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-blocker').debug3Func(): logFunc('called.')
        blocker = BlinkyBlockerMaapi(self._log)
        blocker.init(self.domain)
        return blocker

    def setBlockerObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-blocker').debug3Func(): logFunc('called. obj=%s', obj)
        self.blockerObj = obj

    def getBlockerObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-blocker').debug3Func(): logFunc('called. self.blockerObj=%s', self.blockerObj)
        return self.blockerObj

    def hasBlocker (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-blocker').debug3Func(): logFunc('called. self.blockerObj=%s', self.blockerObj)
        if self.blockerObj:
            return True
        return False



    def requestMaxActiveConnections (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-maxactiveconnections').debug3Func(): logFunc('called. requested=%s', requested)
        self.maxActiveConnectionsRequested = requested
        self.maxActiveConnectionsSet = False

    def isMaxActiveConnectionsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-maxactiveconnections-requested').debug3Func(): logFunc('called. requested=%s', self.maxActiveConnectionsRequested)
        return self.maxActiveConnectionsRequested

    def getMaxActiveConnections (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-maxactiveconnections').debug3Func(): logFunc('called. self.maxActiveConnectionsSet=%s, self.maxActiveConnections=%s', self.maxActiveConnectionsSet, self.maxActiveConnections)
        if self.maxActiveConnectionsSet:
            return self.maxActiveConnections
        return None

    def hasMaxActiveConnections (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-maxactiveconnections').debug3Func(): logFunc('called. self.maxActiveConnectionsSet=%s, self.maxActiveConnections=%s', self.maxActiveConnectionsSet, self.maxActiveConnections)
        if self.maxActiveConnectionsSet:
            return True
        return False

    def setMaxActiveConnections (self, maxActiveConnections):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-maxactiveconnections').debug3Func(): logFunc('called. maxActiveConnections=%s, old=%s', maxActiveConnections, self.maxActiveConnections)
        self.maxActiveConnectionsSet = True
        self.maxActiveConnections = maxActiveConnections

    def requestEnabled (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-enabled').debug3Func(): logFunc('called. requested=%s', requested)
        self.enabledRequested = requested
        self.enabledSet = False

    def isEnabledRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-enabled-requested').debug3Func(): logFunc('called. requested=%s', self.enabledRequested)
        return self.enabledRequested

    def getEnabled (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-enabled').debug3Func(): logFunc('called. self.enabledSet=%s, self.enabled=%s', self.enabledSet, self.enabled)
        if self.enabledSet:
            return self.enabled
        return None

    def hasEnabled (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-enabled').debug3Func(): logFunc('called. self.enabledSet=%s, self.enabled=%s', self.enabledSet, self.enabled)
        if self.enabledSet:
            return True
        return False

    def setEnabled (self, enabled):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-enabled').debug3Func(): logFunc('called. enabled=%s, old=%s', enabled, self.enabled)
        self.enabledSet = True
        self.enabled = enabled

    def requestMaxRedirectRate (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-maxredirectrate').debug3Func(): logFunc('called. requested=%s', requested)
        self.maxRedirectRateRequested = requested
        self.maxRedirectRateSet = False

    def isMaxRedirectRateRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-maxredirectrate-requested').debug3Func(): logFunc('called. requested=%s', self.maxRedirectRateRequested)
        return self.maxRedirectRateRequested

    def getMaxRedirectRate (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-maxredirectrate').debug3Func(): logFunc('called. self.maxRedirectRateSet=%s, self.maxRedirectRate=%s', self.maxRedirectRateSet, self.maxRedirectRate)
        if self.maxRedirectRateSet:
            return self.maxRedirectRate
        return None

    def hasMaxRedirectRate (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-maxredirectrate').debug3Func(): logFunc('called. self.maxRedirectRateSet=%s, self.maxRedirectRate=%s', self.maxRedirectRateSet, self.maxRedirectRate)
        if self.maxRedirectRateSet:
            return True
        return False

    def setMaxRedirectRate (self, maxRedirectRate):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-maxredirectrate').debug3Func(): logFunc('called. maxRedirectRate=%s, old=%s', maxRedirectRate, self.maxRedirectRate)
        self.maxRedirectRateSet = True
        self.maxRedirectRate = maxRedirectRate


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.blockerObj:
            self.blockerObj._clearAllReadData()
        

        
        self.maxActiveConnections = 0
        self.maxActiveConnectionsSet = False
        
        self.enabled = 0
        self.enabledSet = False
        
        self.maxRedirectRate = 0
        self.maxRedirectRateSet = False
        

    def _getSelfKeyPath (self, line
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("delivery", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("analyzer", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(line);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("line", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line"))
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
                        line, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(line, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(line, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       line, 
                       
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

        keyPath = self._getSelfKeyPath(line, 
                                       
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
                               line, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        
        if self.blockerObj:
            res = self.blockerObj._collectItemsToDelete(line, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-blocker-failed').errorFunc(): logFunc('blockerObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasMaxActiveConnections():
            valMaxActiveConnections = Value()
            if self.maxActiveConnections is not None:
                valMaxActiveConnections.setInt64(self.maxActiveConnections)
            else:
                valMaxActiveConnections.setEmpty()
            tagValueList.push(("max-active-connections", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valMaxActiveConnections)
        
        if self.hasEnabled():
            valEnabled = Value()
            if self.enabled is not None:
                valEnabled.setBool(self.enabled)
            else:
                valEnabled.setEmpty()
            tagValueList.push(("enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valEnabled)
        
        if self.hasMaxRedirectRate():
            valMaxRedirectRate = Value()
            if self.maxRedirectRate is not None:
                valMaxRedirectRate.setInt64(self.maxRedirectRate)
            else:
                valMaxRedirectRate.setEmpty()
            tagValueList.push(("max-redirect-rate", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valMaxRedirectRate)
        

        
        if self.blockerObj:
            valBegin = Value()
            (tag, ns, prefix) = ("blocker" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.blockerObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-blocker-failed').errorFunc(): logFunc('blockerObj._fillWriteTagValues() failed. PARAMS')
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

        
        if self.isMaxActiveConnectionsRequested():
            valMaxActiveConnections = Value()
            valMaxActiveConnections.setEmpty()
            tagValueList.push(("max-active-connections", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valMaxActiveConnections)
        
        if self.isEnabledRequested():
            valEnabled = Value()
            valEnabled.setEmpty()
            tagValueList.push(("enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valEnabled)
        
        if self.isMaxRedirectRateRequested():
            valMaxRedirectRate = Value()
            valMaxRedirectRate.setEmpty()
            tagValueList.push(("max-redirect-rate", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valMaxRedirectRate)
        

        
        if self.blockerObj:
            valBegin = Value()
            (tag, ns, prefix) = ("blocker" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.blockerObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-blocker-failed').errorFunc(): logFunc('blockerObj._fillReadTagValues() failed. PARAMS')
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
        
        if self.isMaxActiveConnectionsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "max-active-connections") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-maxactiveconnections').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "maxActiveConnections", "max-active-connections", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-max-active-connections-bad-value').infoFunc(): logFunc('maxActiveConnections not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMaxActiveConnections(tempVar)
            for logFunc in self._log('read-tag-values-max-active-connections').debug3Func(): logFunc('read maxActiveConnections. maxActiveConnections=%s, tempValue=%s', self.maxActiveConnections, tempValue.getType())
        
        if self.isEnabledRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "enabled") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-enabled').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "enabled", "enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-enabled-bad-value').infoFunc(): logFunc('enabled not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setEnabled(tempVar)
            for logFunc in self._log('read-tag-values-enabled').debug3Func(): logFunc('read enabled. enabled=%s, tempValue=%s', self.enabled, tempValue.getType())
        
        if self.isMaxRedirectRateRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "max-redirect-rate") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-maxredirectrate').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "maxRedirectRate", "max-redirect-rate", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-max-redirect-rate-bad-value').infoFunc(): logFunc('maxRedirectRate not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMaxRedirectRate(tempVar)
            for logFunc in self._log('read-tag-values-max-redirect-rate').debug3Func(): logFunc('read maxRedirectRate. maxRedirectRate=%s, tempValue=%s', self.maxRedirectRate, tempValue.getType())
        

        
        if self.blockerObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "blocker") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "blocker", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.blockerObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-blocker-failed').errorFunc(): logFunc('blockerObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "blocker") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "blocker", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "delivery", 
        "namespace": "delivery", 
        "className": "DeliveryMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.analyzer.delivery.delivery_maapi_gen import DeliveryMaapi", 
        "baseClassName": "DeliveryMaapiBase", 
        "baseModule": "delivery_maapi_base_gen"
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
            "yangName": "analyzer", 
            "namespace": "analyzer", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "analyzer"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "yangName": "delivery", 
            "namespace": "delivery", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "delivery"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "memberName": "blocker", 
            "yangName": "blocker", 
            "className": "BlinkyBlockerMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.analyzer.delivery.blocker.blocker_maapi_gen import BlinkyBlockerMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxActiveConnections", 
            "yangName": "max-active-connections", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxRedirectRate", 
            "yangName": "max-redirect-rate", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
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
            "memberName": "maxActiveConnections", 
            "yangName": "max-active-connections", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxRedirectRate", 
            "yangName": "max-redirect-rate", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }
    ], 
    "createTime": "2013"
}
"""


