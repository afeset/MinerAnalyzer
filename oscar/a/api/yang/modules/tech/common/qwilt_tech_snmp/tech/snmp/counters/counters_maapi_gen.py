


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

from counters_maapi_base_gen import CountersMaapiBase




class BlinkyCountersMaapi(CountersMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-counters")
        self.domain = None

        

        
        self.silentDroppedPacketsRequested = False
        self.silentDroppedPackets = None
        self.silentDroppedPacketsSet = False
        
        self.inPacketsRequested = False
        self.inPackets = None
        self.inPacketsSet = False
        
        self.inBadVersionPacketsRequested = False
        self.inBadVersionPackets = None
        self.inBadVersionPacketsSet = False
        
        self.inBadCommunityUsePacketsRequested = False
        self.inBadCommunityUsePackets = None
        self.inBadCommunityUsePacketsSet = False
        
        self.inAsnParseErrorsRequested = False
        self.inAsnParseErrors = None
        self.inAsnParseErrorsSet = False
        
        self.inBadCommunityPacketsRequested = False
        self.inBadCommunityPackets = None
        self.inBadCommunityPacketsSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestSilentDroppedPackets(True)
        
        self.requestInPackets(True)
        
        self.requestInBadVersionPackets(True)
        
        self.requestInBadCommunityUsePackets(True)
        
        self.requestInAsnParseErrors(True)
        
        self.requestInBadCommunityPackets(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestSilentDroppedPackets(False)
        
        self.requestInPackets(False)
        
        self.requestInBadVersionPackets(False)
        
        self.requestInBadCommunityUsePackets(False)
        
        self.requestInAsnParseErrors(False)
        
        self.requestInBadCommunityPackets(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestSilentDroppedPackets(True)
        
        self.requestInPackets(True)
        
        self.requestInBadVersionPackets(True)
        
        self.requestInBadCommunityUsePackets(True)
        
        self.requestInAsnParseErrors(True)
        
        self.requestInBadCommunityPackets(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestSilentDroppedPackets(False)
        
        self.requestInPackets(False)
        
        self.requestInBadVersionPackets(False)
        
        self.requestInBadCommunityUsePackets(False)
        
        self.requestInAsnParseErrors(False)
        
        self.requestInBadCommunityPackets(False)
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        

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



    def requestSilentDroppedPackets (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-silentdroppedpackets').debug3Func(): logFunc('called. requested=%s', requested)
        self.silentDroppedPacketsRequested = requested
        self.silentDroppedPacketsSet = False

    def isSilentDroppedPacketsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-silentdroppedpackets-requested').debug3Func(): logFunc('called. requested=%s', self.silentDroppedPacketsRequested)
        return self.silentDroppedPacketsRequested

    def getSilentDroppedPackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-silentdroppedpackets').debug3Func(): logFunc('called. self.silentDroppedPacketsSet=%s, self.silentDroppedPackets=%s', self.silentDroppedPacketsSet, self.silentDroppedPackets)
        if self.silentDroppedPacketsSet:
            return self.silentDroppedPackets
        return None

    def hasSilentDroppedPackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-silentdroppedpackets').debug3Func(): logFunc('called. self.silentDroppedPacketsSet=%s, self.silentDroppedPackets=%s', self.silentDroppedPacketsSet, self.silentDroppedPackets)
        if self.silentDroppedPacketsSet:
            return True
        return False

    def setSilentDroppedPackets (self, silentDroppedPackets):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-silentdroppedpackets').debug3Func(): logFunc('called. silentDroppedPackets=%s, old=%s', silentDroppedPackets, self.silentDroppedPackets)
        self.silentDroppedPacketsSet = True
        self.silentDroppedPackets = silentDroppedPackets

    def requestInPackets (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-inpackets').debug3Func(): logFunc('called. requested=%s', requested)
        self.inPacketsRequested = requested
        self.inPacketsSet = False

    def isInPacketsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-inpackets-requested').debug3Func(): logFunc('called. requested=%s', self.inPacketsRequested)
        return self.inPacketsRequested

    def getInPackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-inpackets').debug3Func(): logFunc('called. self.inPacketsSet=%s, self.inPackets=%s', self.inPacketsSet, self.inPackets)
        if self.inPacketsSet:
            return self.inPackets
        return None

    def hasInPackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-inpackets').debug3Func(): logFunc('called. self.inPacketsSet=%s, self.inPackets=%s', self.inPacketsSet, self.inPackets)
        if self.inPacketsSet:
            return True
        return False

    def setInPackets (self, inPackets):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-inpackets').debug3Func(): logFunc('called. inPackets=%s, old=%s', inPackets, self.inPackets)
        self.inPacketsSet = True
        self.inPackets = inPackets

    def requestInBadVersionPackets (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-inbadversionpackets').debug3Func(): logFunc('called. requested=%s', requested)
        self.inBadVersionPacketsRequested = requested
        self.inBadVersionPacketsSet = False

    def isInBadVersionPacketsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-inbadversionpackets-requested').debug3Func(): logFunc('called. requested=%s', self.inBadVersionPacketsRequested)
        return self.inBadVersionPacketsRequested

    def getInBadVersionPackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-inbadversionpackets').debug3Func(): logFunc('called. self.inBadVersionPacketsSet=%s, self.inBadVersionPackets=%s', self.inBadVersionPacketsSet, self.inBadVersionPackets)
        if self.inBadVersionPacketsSet:
            return self.inBadVersionPackets
        return None

    def hasInBadVersionPackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-inbadversionpackets').debug3Func(): logFunc('called. self.inBadVersionPacketsSet=%s, self.inBadVersionPackets=%s', self.inBadVersionPacketsSet, self.inBadVersionPackets)
        if self.inBadVersionPacketsSet:
            return True
        return False

    def setInBadVersionPackets (self, inBadVersionPackets):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-inbadversionpackets').debug3Func(): logFunc('called. inBadVersionPackets=%s, old=%s', inBadVersionPackets, self.inBadVersionPackets)
        self.inBadVersionPacketsSet = True
        self.inBadVersionPackets = inBadVersionPackets

    def requestInBadCommunityUsePackets (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-inbadcommunityusepackets').debug3Func(): logFunc('called. requested=%s', requested)
        self.inBadCommunityUsePacketsRequested = requested
        self.inBadCommunityUsePacketsSet = False

    def isInBadCommunityUsePacketsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-inbadcommunityusepackets-requested').debug3Func(): logFunc('called. requested=%s', self.inBadCommunityUsePacketsRequested)
        return self.inBadCommunityUsePacketsRequested

    def getInBadCommunityUsePackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-inbadcommunityusepackets').debug3Func(): logFunc('called. self.inBadCommunityUsePacketsSet=%s, self.inBadCommunityUsePackets=%s', self.inBadCommunityUsePacketsSet, self.inBadCommunityUsePackets)
        if self.inBadCommunityUsePacketsSet:
            return self.inBadCommunityUsePackets
        return None

    def hasInBadCommunityUsePackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-inbadcommunityusepackets').debug3Func(): logFunc('called. self.inBadCommunityUsePacketsSet=%s, self.inBadCommunityUsePackets=%s', self.inBadCommunityUsePacketsSet, self.inBadCommunityUsePackets)
        if self.inBadCommunityUsePacketsSet:
            return True
        return False

    def setInBadCommunityUsePackets (self, inBadCommunityUsePackets):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-inbadcommunityusepackets').debug3Func(): logFunc('called. inBadCommunityUsePackets=%s, old=%s', inBadCommunityUsePackets, self.inBadCommunityUsePackets)
        self.inBadCommunityUsePacketsSet = True
        self.inBadCommunityUsePackets = inBadCommunityUsePackets

    def requestInAsnParseErrors (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-inasnparseerrors').debug3Func(): logFunc('called. requested=%s', requested)
        self.inAsnParseErrorsRequested = requested
        self.inAsnParseErrorsSet = False

    def isInAsnParseErrorsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-inasnparseerrors-requested').debug3Func(): logFunc('called. requested=%s', self.inAsnParseErrorsRequested)
        return self.inAsnParseErrorsRequested

    def getInAsnParseErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-inasnparseerrors').debug3Func(): logFunc('called. self.inAsnParseErrorsSet=%s, self.inAsnParseErrors=%s', self.inAsnParseErrorsSet, self.inAsnParseErrors)
        if self.inAsnParseErrorsSet:
            return self.inAsnParseErrors
        return None

    def hasInAsnParseErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-inasnparseerrors').debug3Func(): logFunc('called. self.inAsnParseErrorsSet=%s, self.inAsnParseErrors=%s', self.inAsnParseErrorsSet, self.inAsnParseErrors)
        if self.inAsnParseErrorsSet:
            return True
        return False

    def setInAsnParseErrors (self, inAsnParseErrors):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-inasnparseerrors').debug3Func(): logFunc('called. inAsnParseErrors=%s, old=%s', inAsnParseErrors, self.inAsnParseErrors)
        self.inAsnParseErrorsSet = True
        self.inAsnParseErrors = inAsnParseErrors

    def requestInBadCommunityPackets (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-inbadcommunitypackets').debug3Func(): logFunc('called. requested=%s', requested)
        self.inBadCommunityPacketsRequested = requested
        self.inBadCommunityPacketsSet = False

    def isInBadCommunityPacketsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-inbadcommunitypackets-requested').debug3Func(): logFunc('called. requested=%s', self.inBadCommunityPacketsRequested)
        return self.inBadCommunityPacketsRequested

    def getInBadCommunityPackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-inbadcommunitypackets').debug3Func(): logFunc('called. self.inBadCommunityPacketsSet=%s, self.inBadCommunityPackets=%s', self.inBadCommunityPacketsSet, self.inBadCommunityPackets)
        if self.inBadCommunityPacketsSet:
            return self.inBadCommunityPackets
        return None

    def hasInBadCommunityPackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-inbadcommunitypackets').debug3Func(): logFunc('called. self.inBadCommunityPacketsSet=%s, self.inBadCommunityPackets=%s', self.inBadCommunityPacketsSet, self.inBadCommunityPackets)
        if self.inBadCommunityPacketsSet:
            return True
        return False

    def setInBadCommunityPackets (self, inBadCommunityPackets):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-inbadcommunitypackets').debug3Func(): logFunc('called. inBadCommunityPackets=%s, old=%s', inBadCommunityPackets, self.inBadCommunityPackets)
        self.inBadCommunityPacketsSet = True
        self.inBadCommunityPackets = inBadCommunityPackets


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.silentDroppedPackets = 0
        self.silentDroppedPacketsSet = False
        
        self.inPackets = 0
        self.inPacketsSet = False
        
        self.inBadVersionPackets = 0
        self.inBadVersionPacketsSet = False
        
        self.inBadCommunityUsePackets = 0
        self.inBadCommunityUsePacketsSet = False
        
        self.inAsnParseErrors = 0
        self.inAsnParseErrorsSet = False
        
        self.inBadCommunityPackets = 0
        self.inBadCommunityPacketsSet = False
        

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("counters", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", "qt-snmp"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("snmp", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", "qt-snmp"))
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

        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isSilentDroppedPacketsRequested():
            valSilentDroppedPackets = Value()
            valSilentDroppedPackets.setEmpty()
            tagValueList.push(("silent-dropped-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"), valSilentDroppedPackets)
        
        if self.isInPacketsRequested():
            valInPackets = Value()
            valInPackets.setEmpty()
            tagValueList.push(("in-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"), valInPackets)
        
        if self.isInBadVersionPacketsRequested():
            valInBadVersionPackets = Value()
            valInBadVersionPackets.setEmpty()
            tagValueList.push(("in-bad-version-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"), valInBadVersionPackets)
        
        if self.isInBadCommunityUsePacketsRequested():
            valInBadCommunityUsePackets = Value()
            valInBadCommunityUsePackets.setEmpty()
            tagValueList.push(("in-bad-community-use-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"), valInBadCommunityUsePackets)
        
        if self.isInAsnParseErrorsRequested():
            valInAsnParseErrors = Value()
            valInAsnParseErrors.setEmpty()
            tagValueList.push(("in-asn-parse-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"), valInAsnParseErrors)
        
        if self.isInBadCommunityPacketsRequested():
            valInBadCommunityPackets = Value()
            valInBadCommunityPackets.setEmpty()
            tagValueList.push(("in-bad-community-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"), valInBadCommunityPackets)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isSilentDroppedPacketsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "silent-dropped-packets") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-silentdroppedpackets').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "silentDroppedPackets", "silent-dropped-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-silent-dropped-packets-bad-value').infoFunc(): logFunc('silentDroppedPackets not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setSilentDroppedPackets(tempVar)
            for logFunc in self._log('read-tag-values-silent-dropped-packets').debug3Func(): logFunc('read silentDroppedPackets. silentDroppedPackets=%s, tempValue=%s', self.silentDroppedPackets, tempValue.getType())
        
        if self.isInPacketsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "in-packets") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-inpackets').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "inPackets", "in-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-in-packets-bad-value').infoFunc(): logFunc('inPackets not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setInPackets(tempVar)
            for logFunc in self._log('read-tag-values-in-packets').debug3Func(): logFunc('read inPackets. inPackets=%s, tempValue=%s', self.inPackets, tempValue.getType())
        
        if self.isInBadVersionPacketsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "in-bad-version-packets") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-inbadversionpackets').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "inBadVersionPackets", "in-bad-version-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-in-bad-version-packets-bad-value').infoFunc(): logFunc('inBadVersionPackets not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setInBadVersionPackets(tempVar)
            for logFunc in self._log('read-tag-values-in-bad-version-packets').debug3Func(): logFunc('read inBadVersionPackets. inBadVersionPackets=%s, tempValue=%s', self.inBadVersionPackets, tempValue.getType())
        
        if self.isInBadCommunityUsePacketsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "in-bad-community-use-packets") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-inbadcommunityusepackets').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "inBadCommunityUsePackets", "in-bad-community-use-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-in-bad-community-use-packets-bad-value').infoFunc(): logFunc('inBadCommunityUsePackets not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setInBadCommunityUsePackets(tempVar)
            for logFunc in self._log('read-tag-values-in-bad-community-use-packets').debug3Func(): logFunc('read inBadCommunityUsePackets. inBadCommunityUsePackets=%s, tempValue=%s', self.inBadCommunityUsePackets, tempValue.getType())
        
        if self.isInAsnParseErrorsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "in-asn-parse-errors") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-inasnparseerrors').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "inAsnParseErrors", "in-asn-parse-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-in-asn-parse-errors-bad-value').infoFunc(): logFunc('inAsnParseErrors not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setInAsnParseErrors(tempVar)
            for logFunc in self._log('read-tag-values-in-asn-parse-errors').debug3Func(): logFunc('read inAsnParseErrors. inAsnParseErrors=%s, tempValue=%s', self.inAsnParseErrors, tempValue.getType())
        
        if self.isInBadCommunityPacketsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "in-bad-community-packets") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-inbadcommunitypackets').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "inBadCommunityPackets", "in-bad-community-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-in-bad-community-packets-bad-value').infoFunc(): logFunc('inBadCommunityPackets not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setInBadCommunityPackets(tempVar)
            for logFunc in self._log('read-tag-values-in-bad-community-packets').debug3Func(): logFunc('read inBadCommunityPackets. inBadCommunityPackets=%s, tempValue=%s', self.inBadCommunityPackets, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "counters", 
        "namespace": "counters", 
        "className": "CountersMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_snmp.tech.snmp.counters.counters_maapi_gen import CountersMaapi", 
        "baseClassName": "CountersMaapiBase", 
        "baseModule": "counters_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-snmp", 
            "yangName": "snmp", 
            "namespace": "snmp", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "name": "snmp"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-snmp", 
            "yangName": "counters", 
            "namespace": "counters", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "name": "counters"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "silentDroppedPackets", 
            "yangName": "silent-dropped-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inPackets", 
            "yangName": "in-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inBadVersionPackets", 
            "yangName": "in-bad-version-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inBadCommunityUsePackets", 
            "yangName": "in-bad-community-use-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inAsnParseErrors", 
            "yangName": "in-asn-parse-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inBadCommunityPackets", 
            "yangName": "in-bad-community-packets", 
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
            "qwilt_tech_snmp"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "silentDroppedPackets", 
            "yangName": "silent-dropped-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inPackets", 
            "yangName": "in-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inBadVersionPackets", 
            "yangName": "in-bad-version-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inBadCommunityUsePackets", 
            "yangName": "in-bad-community-use-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inAsnParseErrors", 
            "yangName": "in-asn-parse-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inBadCommunityPackets", 
            "yangName": "in-bad-community-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


