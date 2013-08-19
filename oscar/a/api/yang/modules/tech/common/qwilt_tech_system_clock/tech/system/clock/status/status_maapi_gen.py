


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

from status_maapi_base_gen import StatusMaapiBase




class BlinkyStatusMaapi(StatusMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-status")
        self.domain = None

        

        
        self.localTimeStringRequested = False
        self.localTimeString = None
        self.localTimeStringSet = False
        
        self.utcTimeStringRequested = False
        self.utcTimeString = None
        self.utcTimeStringSet = False
        
        self.daylightSavingTimeRequested = False
        self.daylightSavingTime = None
        self.daylightSavingTimeSet = False
        
        self.epochRequested = False
        self.epoch = None
        self.epochSet = False
        
        self.utcOffsetMinutesRequested = False
        self.utcOffsetMinutes = None
        self.utcOffsetMinutesSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestLocalTimeString(True)
        
        self.requestUtcTimeString(True)
        
        self.requestDaylightSavingTime(True)
        
        self.requestEpoch(True)
        
        self.requestUtcOffsetMinutes(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestLocalTimeString(False)
        
        self.requestUtcTimeString(False)
        
        self.requestDaylightSavingTime(False)
        
        self.requestEpoch(False)
        
        self.requestUtcOffsetMinutes(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestLocalTimeString(True)
        
        self.requestUtcTimeString(True)
        
        self.requestDaylightSavingTime(True)
        
        self.requestEpoch(True)
        
        self.requestUtcOffsetMinutes(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestLocalTimeString(False)
        
        self.requestUtcTimeString(False)
        
        self.requestDaylightSavingTime(False)
        
        self.requestEpoch(False)
        
        self.requestUtcOffsetMinutes(False)
        
        

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



    def requestLocalTimeString (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-localtimestring').debug3Func(): logFunc('called. requested=%s', requested)
        self.localTimeStringRequested = requested
        self.localTimeStringSet = False

    def isLocalTimeStringRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-localtimestring-requested').debug3Func(): logFunc('called. requested=%s', self.localTimeStringRequested)
        return self.localTimeStringRequested

    def getLocalTimeString (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-localtimestring').debug3Func(): logFunc('called. self.localTimeStringSet=%s, self.localTimeString=%s', self.localTimeStringSet, self.localTimeString)
        if self.localTimeStringSet:
            return self.localTimeString
        return None

    def hasLocalTimeString (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-localtimestring').debug3Func(): logFunc('called. self.localTimeStringSet=%s, self.localTimeString=%s', self.localTimeStringSet, self.localTimeString)
        if self.localTimeStringSet:
            return True
        return False

    def setLocalTimeString (self, localTimeString):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-localtimestring').debug3Func(): logFunc('called. localTimeString=%s, old=%s', localTimeString, self.localTimeString)
        self.localTimeStringSet = True
        self.localTimeString = localTimeString

    def requestUtcTimeString (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-utctimestring').debug3Func(): logFunc('called. requested=%s', requested)
        self.utcTimeStringRequested = requested
        self.utcTimeStringSet = False

    def isUtcTimeStringRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-utctimestring-requested').debug3Func(): logFunc('called. requested=%s', self.utcTimeStringRequested)
        return self.utcTimeStringRequested

    def getUtcTimeString (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-utctimestring').debug3Func(): logFunc('called. self.utcTimeStringSet=%s, self.utcTimeString=%s', self.utcTimeStringSet, self.utcTimeString)
        if self.utcTimeStringSet:
            return self.utcTimeString
        return None

    def hasUtcTimeString (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-utctimestring').debug3Func(): logFunc('called. self.utcTimeStringSet=%s, self.utcTimeString=%s', self.utcTimeStringSet, self.utcTimeString)
        if self.utcTimeStringSet:
            return True
        return False

    def setUtcTimeString (self, utcTimeString):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-utctimestring').debug3Func(): logFunc('called. utcTimeString=%s, old=%s', utcTimeString, self.utcTimeString)
        self.utcTimeStringSet = True
        self.utcTimeString = utcTimeString

    def requestDaylightSavingTime (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-daylightsavingtime').debug3Func(): logFunc('called. requested=%s', requested)
        self.daylightSavingTimeRequested = requested
        self.daylightSavingTimeSet = False

    def isDaylightSavingTimeRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-daylightsavingtime-requested').debug3Func(): logFunc('called. requested=%s', self.daylightSavingTimeRequested)
        return self.daylightSavingTimeRequested

    def getDaylightSavingTime (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-daylightsavingtime').debug3Func(): logFunc('called. self.daylightSavingTimeSet=%s, self.daylightSavingTime=%s', self.daylightSavingTimeSet, self.daylightSavingTime)
        if self.daylightSavingTimeSet:
            return self.daylightSavingTime
        return None

    def hasDaylightSavingTime (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-daylightsavingtime').debug3Func(): logFunc('called. self.daylightSavingTimeSet=%s, self.daylightSavingTime=%s', self.daylightSavingTimeSet, self.daylightSavingTime)
        if self.daylightSavingTimeSet:
            return True
        return False

    def setDaylightSavingTime (self, daylightSavingTime):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-daylightsavingtime').debug3Func(): logFunc('called. daylightSavingTime=%s, old=%s', daylightSavingTime, self.daylightSavingTime)
        self.daylightSavingTimeSet = True
        self.daylightSavingTime = daylightSavingTime

    def requestEpoch (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-epoch').debug3Func(): logFunc('called. requested=%s', requested)
        self.epochRequested = requested
        self.epochSet = False

    def isEpochRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-epoch-requested').debug3Func(): logFunc('called. requested=%s', self.epochRequested)
        return self.epochRequested

    def getEpoch (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-epoch').debug3Func(): logFunc('called. self.epochSet=%s, self.epoch=%s', self.epochSet, self.epoch)
        if self.epochSet:
            return self.epoch
        return None

    def hasEpoch (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-epoch').debug3Func(): logFunc('called. self.epochSet=%s, self.epoch=%s', self.epochSet, self.epoch)
        if self.epochSet:
            return True
        return False

    def setEpoch (self, epoch):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-epoch').debug3Func(): logFunc('called. epoch=%s, old=%s', epoch, self.epoch)
        self.epochSet = True
        self.epoch = epoch

    def requestUtcOffsetMinutes (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-utcoffsetminutes').debug3Func(): logFunc('called. requested=%s', requested)
        self.utcOffsetMinutesRequested = requested
        self.utcOffsetMinutesSet = False

    def isUtcOffsetMinutesRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-utcoffsetminutes-requested').debug3Func(): logFunc('called. requested=%s', self.utcOffsetMinutesRequested)
        return self.utcOffsetMinutesRequested

    def getUtcOffsetMinutes (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-utcoffsetminutes').debug3Func(): logFunc('called. self.utcOffsetMinutesSet=%s, self.utcOffsetMinutes=%s', self.utcOffsetMinutesSet, self.utcOffsetMinutes)
        if self.utcOffsetMinutesSet:
            return self.utcOffsetMinutes
        return None

    def hasUtcOffsetMinutes (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-utcoffsetminutes').debug3Func(): logFunc('called. self.utcOffsetMinutesSet=%s, self.utcOffsetMinutes=%s', self.utcOffsetMinutesSet, self.utcOffsetMinutes)
        if self.utcOffsetMinutesSet:
            return True
        return False

    def setUtcOffsetMinutes (self, utcOffsetMinutes):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-utcoffsetminutes').debug3Func(): logFunc('called. utcOffsetMinutes=%s, old=%s', utcOffsetMinutes, self.utcOffsetMinutes)
        self.utcOffsetMinutesSet = True
        self.utcOffsetMinutes = utcOffsetMinutes


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.localTimeString = 0
        self.localTimeStringSet = False
        
        self.utcTimeString = 0
        self.utcTimeStringSet = False
        
        self.daylightSavingTime = 0
        self.daylightSavingTimeSet = False
        
        self.epoch = 0
        self.epochSet = False
        
        self.utcOffsetMinutes = 0
        self.utcOffsetMinutesSet = False
        

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock", "qt-sys-clock"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("clock", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock", "qt-sys-clock"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", "qt-sys"))
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

        
        if self.isLocalTimeStringRequested():
            valLocalTimeString = Value()
            valLocalTimeString.setEmpty()
            tagValueList.push(("local-time-string", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock"), valLocalTimeString)
        
        if self.isUtcTimeStringRequested():
            valUtcTimeString = Value()
            valUtcTimeString.setEmpty()
            tagValueList.push(("utc-time-string", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock"), valUtcTimeString)
        
        if self.isDaylightSavingTimeRequested():
            valDaylightSavingTime = Value()
            valDaylightSavingTime.setEmpty()
            tagValueList.push(("daylight-saving-time", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock"), valDaylightSavingTime)
        
        if self.isEpochRequested():
            valEpoch = Value()
            valEpoch.setEmpty()
            tagValueList.push(("epoch", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock"), valEpoch)
        
        if self.isUtcOffsetMinutesRequested():
            valUtcOffsetMinutes = Value()
            valUtcOffsetMinutes.setEmpty()
            tagValueList.push(("utc-offset-minutes", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock"), valUtcOffsetMinutes)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isLocalTimeStringRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "local-time-string") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-localtimestring').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "localTimeString", "local-time-string", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-local-time-string-bad-value').infoFunc(): logFunc('localTimeString not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setLocalTimeString(tempVar)
            for logFunc in self._log('read-tag-values-local-time-string').debug3Func(): logFunc('read localTimeString. localTimeString=%s, tempValue=%s', self.localTimeString, tempValue.getType())
        
        if self.isUtcTimeStringRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "utc-time-string") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-utctimestring').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "utcTimeString", "utc-time-string", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-utc-time-string-bad-value').infoFunc(): logFunc('utcTimeString not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setUtcTimeString(tempVar)
            for logFunc in self._log('read-tag-values-utc-time-string').debug3Func(): logFunc('read utcTimeString. utcTimeString=%s, tempValue=%s', self.utcTimeString, tempValue.getType())
        
        if self.isDaylightSavingTimeRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "daylight-saving-time") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-daylightsavingtime').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "daylightSavingTime", "daylight-saving-time", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-daylight-saving-time-bad-value').infoFunc(): logFunc('daylightSavingTime not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setDaylightSavingTime(tempVar)
            for logFunc in self._log('read-tag-values-daylight-saving-time').debug3Func(): logFunc('read daylightSavingTime. daylightSavingTime=%s, tempValue=%s', self.daylightSavingTime, tempValue.getType())
        
        if self.isEpochRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "epoch") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-epoch').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "epoch", "epoch", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-epoch-bad-value').infoFunc(): logFunc('epoch not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setEpoch(tempVar)
            for logFunc in self._log('read-tag-values-epoch').debug3Func(): logFunc('read epoch. epoch=%s, tempValue=%s', self.epoch, tempValue.getType())
        
        if self.isUtcOffsetMinutesRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "utc-offset-minutes") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-utcoffsetminutes').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "utcOffsetMinutes", "utc-offset-minutes", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-utc-offset-minutes-bad-value').infoFunc(): logFunc('utcOffsetMinutes not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setUtcOffsetMinutes(tempVar)
            for logFunc in self._log('read-tag-values-utc-offset-minutes').debug3Func(): logFunc('read utcOffsetMinutes. utcOffsetMinutes=%s, tempValue=%s', self.utcOffsetMinutes, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "status", 
        "namespace": "status", 
        "className": "StatusMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system_clock.tech.system.clock.status.status_maapi_gen import StatusMaapi", 
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
            "moduleYangNamespacePrefix": "qt-sys", 
            "yangName": "system", 
            "namespace": "system", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", 
            "name": "system"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys-clock", 
            "yangName": "clock", 
            "namespace": "clock", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock", 
            "name": "clock"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys-clock", 
            "yangName": "status", 
            "namespace": "status", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock", 
            "name": "status"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock", 
            "moduleYangNamespacePrefix": "qt-sys-clock", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "localTimeString", 
            "yangName": "local-time-string", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock", 
            "moduleYangNamespacePrefix": "qt-sys-clock", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "utcTimeString", 
            "yangName": "utc-time-string", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock", 
            "moduleYangNamespacePrefix": "qt-sys-clock", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "daylightSavingTime", 
            "yangName": "daylight-saving-time", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock", 
            "moduleYangNamespacePrefix": "qt-sys-clock", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "epoch", 
            "yangName": "epoch", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock", 
            "moduleYangNamespacePrefix": "qt-sys-clock", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "utcOffsetMinutes", 
            "yangName": "utc-offset-minutes", 
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
            "qwilt_tech_system_clock"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock", 
            "moduleYangNamespacePrefix": "qt-sys-clock", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "localTimeString", 
            "yangName": "local-time-string", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock", 
            "moduleYangNamespacePrefix": "qt-sys-clock", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "utcTimeString", 
            "yangName": "utc-time-string", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock", 
            "moduleYangNamespacePrefix": "qt-sys-clock", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "daylightSavingTime", 
            "yangName": "daylight-saving-time", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock", 
            "moduleYangNamespacePrefix": "qt-sys-clock", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "epoch", 
            "yangName": "epoch", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock", 
            "moduleYangNamespacePrefix": "qt-sys-clock", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "utcOffsetMinutes", 
            "yangName": "utc-offset-minutes", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


