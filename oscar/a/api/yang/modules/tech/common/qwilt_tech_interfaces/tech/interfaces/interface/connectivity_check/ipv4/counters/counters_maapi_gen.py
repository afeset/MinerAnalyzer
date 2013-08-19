


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

        

        
        self.arpFailuresRequested = False
        self.arpFailures = None
        self.arpFailuresSet = False
        
        self.arpRequestsSentRequested = False
        self.arpRequestsSent = None
        self.arpRequestsSentSet = False
        
        self.pingSuccessesRequested = False
        self.pingSuccesses = None
        self.pingSuccessesSet = False
        
        self.pingRequestsSentRequested = False
        self.pingRequestsSent = None
        self.pingRequestsSentSet = False
        
        self.arpSuccessesRequested = False
        self.arpSuccesses = None
        self.arpSuccessesSet = False
        
        self.pingFailuresRequested = False
        self.pingFailures = None
        self.pingFailuresSet = False
        
        self.arpTimeoutsRequested = False
        self.arpTimeouts = None
        self.arpTimeoutsSet = False
        
        self.pingTimeoutsRequested = False
        self.pingTimeouts = None
        self.pingTimeoutsSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestArpFailures(True)
        
        self.requestArpRequestsSent(True)
        
        self.requestPingSuccesses(True)
        
        self.requestPingRequestsSent(True)
        
        self.requestArpSuccesses(True)
        
        self.requestPingFailures(True)
        
        self.requestArpTimeouts(True)
        
        self.requestPingTimeouts(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestArpFailures(False)
        
        self.requestArpRequestsSent(False)
        
        self.requestPingSuccesses(False)
        
        self.requestPingRequestsSent(False)
        
        self.requestArpSuccesses(False)
        
        self.requestPingFailures(False)
        
        self.requestArpTimeouts(False)
        
        self.requestPingTimeouts(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestArpFailures(True)
        
        self.requestArpRequestsSent(True)
        
        self.requestPingSuccesses(True)
        
        self.requestPingRequestsSent(True)
        
        self.requestArpSuccesses(True)
        
        self.requestPingFailures(True)
        
        self.requestArpTimeouts(True)
        
        self.requestPingTimeouts(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestArpFailures(False)
        
        self.requestArpRequestsSent(False)
        
        self.requestPingSuccesses(False)
        
        self.requestPingRequestsSent(False)
        
        self.requestArpSuccesses(False)
        
        self.requestPingFailures(False)
        
        self.requestArpTimeouts(False)
        
        self.requestPingTimeouts(False)
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        

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



    def requestArpFailures (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-arpfailures').debug3Func(): logFunc('called. requested=%s', requested)
        self.arpFailuresRequested = requested
        self.arpFailuresSet = False

    def isArpFailuresRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-arpfailures-requested').debug3Func(): logFunc('called. requested=%s', self.arpFailuresRequested)
        return self.arpFailuresRequested

    def getArpFailures (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-arpfailures').debug3Func(): logFunc('called. self.arpFailuresSet=%s, self.arpFailures=%s', self.arpFailuresSet, self.arpFailures)
        if self.arpFailuresSet:
            return self.arpFailures
        return None

    def hasArpFailures (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-arpfailures').debug3Func(): logFunc('called. self.arpFailuresSet=%s, self.arpFailures=%s', self.arpFailuresSet, self.arpFailures)
        if self.arpFailuresSet:
            return True
        return False

    def setArpFailures (self, arpFailures):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-arpfailures').debug3Func(): logFunc('called. arpFailures=%s, old=%s', arpFailures, self.arpFailures)
        self.arpFailuresSet = True
        self.arpFailures = arpFailures

    def requestArpRequestsSent (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-arprequestssent').debug3Func(): logFunc('called. requested=%s', requested)
        self.arpRequestsSentRequested = requested
        self.arpRequestsSentSet = False

    def isArpRequestsSentRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-arprequestssent-requested').debug3Func(): logFunc('called. requested=%s', self.arpRequestsSentRequested)
        return self.arpRequestsSentRequested

    def getArpRequestsSent (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-arprequestssent').debug3Func(): logFunc('called. self.arpRequestsSentSet=%s, self.arpRequestsSent=%s', self.arpRequestsSentSet, self.arpRequestsSent)
        if self.arpRequestsSentSet:
            return self.arpRequestsSent
        return None

    def hasArpRequestsSent (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-arprequestssent').debug3Func(): logFunc('called. self.arpRequestsSentSet=%s, self.arpRequestsSent=%s', self.arpRequestsSentSet, self.arpRequestsSent)
        if self.arpRequestsSentSet:
            return True
        return False

    def setArpRequestsSent (self, arpRequestsSent):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-arprequestssent').debug3Func(): logFunc('called. arpRequestsSent=%s, old=%s', arpRequestsSent, self.arpRequestsSent)
        self.arpRequestsSentSet = True
        self.arpRequestsSent = arpRequestsSent

    def requestPingSuccesses (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-pingsuccesses').debug3Func(): logFunc('called. requested=%s', requested)
        self.pingSuccessesRequested = requested
        self.pingSuccessesSet = False

    def isPingSuccessesRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-pingsuccesses-requested').debug3Func(): logFunc('called. requested=%s', self.pingSuccessesRequested)
        return self.pingSuccessesRequested

    def getPingSuccesses (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-pingsuccesses').debug3Func(): logFunc('called. self.pingSuccessesSet=%s, self.pingSuccesses=%s', self.pingSuccessesSet, self.pingSuccesses)
        if self.pingSuccessesSet:
            return self.pingSuccesses
        return None

    def hasPingSuccesses (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-pingsuccesses').debug3Func(): logFunc('called. self.pingSuccessesSet=%s, self.pingSuccesses=%s', self.pingSuccessesSet, self.pingSuccesses)
        if self.pingSuccessesSet:
            return True
        return False

    def setPingSuccesses (self, pingSuccesses):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-pingsuccesses').debug3Func(): logFunc('called. pingSuccesses=%s, old=%s', pingSuccesses, self.pingSuccesses)
        self.pingSuccessesSet = True
        self.pingSuccesses = pingSuccesses

    def requestPingRequestsSent (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-pingrequestssent').debug3Func(): logFunc('called. requested=%s', requested)
        self.pingRequestsSentRequested = requested
        self.pingRequestsSentSet = False

    def isPingRequestsSentRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-pingrequestssent-requested').debug3Func(): logFunc('called. requested=%s', self.pingRequestsSentRequested)
        return self.pingRequestsSentRequested

    def getPingRequestsSent (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-pingrequestssent').debug3Func(): logFunc('called. self.pingRequestsSentSet=%s, self.pingRequestsSent=%s', self.pingRequestsSentSet, self.pingRequestsSent)
        if self.pingRequestsSentSet:
            return self.pingRequestsSent
        return None

    def hasPingRequestsSent (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-pingrequestssent').debug3Func(): logFunc('called. self.pingRequestsSentSet=%s, self.pingRequestsSent=%s', self.pingRequestsSentSet, self.pingRequestsSent)
        if self.pingRequestsSentSet:
            return True
        return False

    def setPingRequestsSent (self, pingRequestsSent):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-pingrequestssent').debug3Func(): logFunc('called. pingRequestsSent=%s, old=%s', pingRequestsSent, self.pingRequestsSent)
        self.pingRequestsSentSet = True
        self.pingRequestsSent = pingRequestsSent

    def requestArpSuccesses (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-arpsuccesses').debug3Func(): logFunc('called. requested=%s', requested)
        self.arpSuccessesRequested = requested
        self.arpSuccessesSet = False

    def isArpSuccessesRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-arpsuccesses-requested').debug3Func(): logFunc('called. requested=%s', self.arpSuccessesRequested)
        return self.arpSuccessesRequested

    def getArpSuccesses (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-arpsuccesses').debug3Func(): logFunc('called. self.arpSuccessesSet=%s, self.arpSuccesses=%s', self.arpSuccessesSet, self.arpSuccesses)
        if self.arpSuccessesSet:
            return self.arpSuccesses
        return None

    def hasArpSuccesses (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-arpsuccesses').debug3Func(): logFunc('called. self.arpSuccessesSet=%s, self.arpSuccesses=%s', self.arpSuccessesSet, self.arpSuccesses)
        if self.arpSuccessesSet:
            return True
        return False

    def setArpSuccesses (self, arpSuccesses):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-arpsuccesses').debug3Func(): logFunc('called. arpSuccesses=%s, old=%s', arpSuccesses, self.arpSuccesses)
        self.arpSuccessesSet = True
        self.arpSuccesses = arpSuccesses

    def requestPingFailures (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-pingfailures').debug3Func(): logFunc('called. requested=%s', requested)
        self.pingFailuresRequested = requested
        self.pingFailuresSet = False

    def isPingFailuresRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-pingfailures-requested').debug3Func(): logFunc('called. requested=%s', self.pingFailuresRequested)
        return self.pingFailuresRequested

    def getPingFailures (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-pingfailures').debug3Func(): logFunc('called. self.pingFailuresSet=%s, self.pingFailures=%s', self.pingFailuresSet, self.pingFailures)
        if self.pingFailuresSet:
            return self.pingFailures
        return None

    def hasPingFailures (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-pingfailures').debug3Func(): logFunc('called. self.pingFailuresSet=%s, self.pingFailures=%s', self.pingFailuresSet, self.pingFailures)
        if self.pingFailuresSet:
            return True
        return False

    def setPingFailures (self, pingFailures):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-pingfailures').debug3Func(): logFunc('called. pingFailures=%s, old=%s', pingFailures, self.pingFailures)
        self.pingFailuresSet = True
        self.pingFailures = pingFailures

    def requestArpTimeouts (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-arptimeouts').debug3Func(): logFunc('called. requested=%s', requested)
        self.arpTimeoutsRequested = requested
        self.arpTimeoutsSet = False

    def isArpTimeoutsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-arptimeouts-requested').debug3Func(): logFunc('called. requested=%s', self.arpTimeoutsRequested)
        return self.arpTimeoutsRequested

    def getArpTimeouts (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-arptimeouts').debug3Func(): logFunc('called. self.arpTimeoutsSet=%s, self.arpTimeouts=%s', self.arpTimeoutsSet, self.arpTimeouts)
        if self.arpTimeoutsSet:
            return self.arpTimeouts
        return None

    def hasArpTimeouts (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-arptimeouts').debug3Func(): logFunc('called. self.arpTimeoutsSet=%s, self.arpTimeouts=%s', self.arpTimeoutsSet, self.arpTimeouts)
        if self.arpTimeoutsSet:
            return True
        return False

    def setArpTimeouts (self, arpTimeouts):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-arptimeouts').debug3Func(): logFunc('called. arpTimeouts=%s, old=%s', arpTimeouts, self.arpTimeouts)
        self.arpTimeoutsSet = True
        self.arpTimeouts = arpTimeouts

    def requestPingTimeouts (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-pingtimeouts').debug3Func(): logFunc('called. requested=%s', requested)
        self.pingTimeoutsRequested = requested
        self.pingTimeoutsSet = False

    def isPingTimeoutsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-pingtimeouts-requested').debug3Func(): logFunc('called. requested=%s', self.pingTimeoutsRequested)
        return self.pingTimeoutsRequested

    def getPingTimeouts (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-pingtimeouts').debug3Func(): logFunc('called. self.pingTimeoutsSet=%s, self.pingTimeouts=%s', self.pingTimeoutsSet, self.pingTimeouts)
        if self.pingTimeoutsSet:
            return self.pingTimeouts
        return None

    def hasPingTimeouts (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-pingtimeouts').debug3Func(): logFunc('called. self.pingTimeoutsSet=%s, self.pingTimeouts=%s', self.pingTimeoutsSet, self.pingTimeouts)
        if self.pingTimeoutsSet:
            return True
        return False

    def setPingTimeouts (self, pingTimeouts):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-pingtimeouts').debug3Func(): logFunc('called. pingTimeouts=%s, old=%s', pingTimeouts, self.pingTimeouts)
        self.pingTimeoutsSet = True
        self.pingTimeouts = pingTimeouts


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.arpFailures = 0
        self.arpFailuresSet = False
        
        self.arpRequestsSent = 0
        self.arpRequestsSentSet = False
        
        self.pingSuccesses = 0
        self.pingSuccessesSet = False
        
        self.pingRequestsSent = 0
        self.pingRequestsSentSet = False
        
        self.arpSuccesses = 0
        self.arpSuccessesSet = False
        
        self.pingFailures = 0
        self.pingFailuresSet = False
        
        self.arpTimeouts = 0
        self.arpTimeoutsSet = False
        
        self.pingTimeouts = 0
        self.pingTimeoutsSet = False
        

    def _getSelfKeyPath (self, interface
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("counters", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("ipv4", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("connectivity-check", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
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

        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isArpFailuresRequested():
            valArpFailures = Value()
            valArpFailures.setEmpty()
            tagValueList.push(("arp-failures", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valArpFailures)
        
        if self.isArpRequestsSentRequested():
            valArpRequestsSent = Value()
            valArpRequestsSent.setEmpty()
            tagValueList.push(("arp-requests-sent", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valArpRequestsSent)
        
        if self.isPingSuccessesRequested():
            valPingSuccesses = Value()
            valPingSuccesses.setEmpty()
            tagValueList.push(("ping-successes", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valPingSuccesses)
        
        if self.isPingRequestsSentRequested():
            valPingRequestsSent = Value()
            valPingRequestsSent.setEmpty()
            tagValueList.push(("ping-requests-sent", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valPingRequestsSent)
        
        if self.isArpSuccessesRequested():
            valArpSuccesses = Value()
            valArpSuccesses.setEmpty()
            tagValueList.push(("arp-successes", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valArpSuccesses)
        
        if self.isPingFailuresRequested():
            valPingFailures = Value()
            valPingFailures.setEmpty()
            tagValueList.push(("ping-failures", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valPingFailures)
        
        if self.isArpTimeoutsRequested():
            valArpTimeouts = Value()
            valArpTimeouts.setEmpty()
            tagValueList.push(("arp-timeouts", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valArpTimeouts)
        
        if self.isPingTimeoutsRequested():
            valPingTimeouts = Value()
            valPingTimeouts.setEmpty()
            tagValueList.push(("ping-timeouts", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valPingTimeouts)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isArpFailuresRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "arp-failures") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-arpfailures').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "arpFailures", "arp-failures", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-arp-failures-bad-value').infoFunc(): logFunc('arpFailures not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setArpFailures(tempVar)
            for logFunc in self._log('read-tag-values-arp-failures').debug3Func(): logFunc('read arpFailures. arpFailures=%s, tempValue=%s', self.arpFailures, tempValue.getType())
        
        if self.isArpRequestsSentRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "arp-requests-sent") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-arprequestssent').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "arpRequestsSent", "arp-requests-sent", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-arp-requests-sent-bad-value').infoFunc(): logFunc('arpRequestsSent not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setArpRequestsSent(tempVar)
            for logFunc in self._log('read-tag-values-arp-requests-sent').debug3Func(): logFunc('read arpRequestsSent. arpRequestsSent=%s, tempValue=%s', self.arpRequestsSent, tempValue.getType())
        
        if self.isPingSuccessesRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "ping-successes") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-pingsuccesses').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "pingSuccesses", "ping-successes", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-ping-successes-bad-value').infoFunc(): logFunc('pingSuccesses not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPingSuccesses(tempVar)
            for logFunc in self._log('read-tag-values-ping-successes').debug3Func(): logFunc('read pingSuccesses. pingSuccesses=%s, tempValue=%s', self.pingSuccesses, tempValue.getType())
        
        if self.isPingRequestsSentRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "ping-requests-sent") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-pingrequestssent').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "pingRequestsSent", "ping-requests-sent", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-ping-requests-sent-bad-value').infoFunc(): logFunc('pingRequestsSent not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPingRequestsSent(tempVar)
            for logFunc in self._log('read-tag-values-ping-requests-sent').debug3Func(): logFunc('read pingRequestsSent. pingRequestsSent=%s, tempValue=%s', self.pingRequestsSent, tempValue.getType())
        
        if self.isArpSuccessesRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "arp-successes") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-arpsuccesses').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "arpSuccesses", "arp-successes", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-arp-successes-bad-value').infoFunc(): logFunc('arpSuccesses not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setArpSuccesses(tempVar)
            for logFunc in self._log('read-tag-values-arp-successes').debug3Func(): logFunc('read arpSuccesses. arpSuccesses=%s, tempValue=%s', self.arpSuccesses, tempValue.getType())
        
        if self.isPingFailuresRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "ping-failures") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-pingfailures').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "pingFailures", "ping-failures", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-ping-failures-bad-value').infoFunc(): logFunc('pingFailures not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPingFailures(tempVar)
            for logFunc in self._log('read-tag-values-ping-failures').debug3Func(): logFunc('read pingFailures. pingFailures=%s, tempValue=%s', self.pingFailures, tempValue.getType())
        
        if self.isArpTimeoutsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "arp-timeouts") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-arptimeouts').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "arpTimeouts", "arp-timeouts", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-arp-timeouts-bad-value').infoFunc(): logFunc('arpTimeouts not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setArpTimeouts(tempVar)
            for logFunc in self._log('read-tag-values-arp-timeouts').debug3Func(): logFunc('read arpTimeouts. arpTimeouts=%s, tempValue=%s', self.arpTimeouts, tempValue.getType())
        
        if self.isPingTimeoutsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "ping-timeouts") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-pingtimeouts').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "pingTimeouts", "ping-timeouts", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-ping-timeouts-bad-value').infoFunc(): logFunc('pingTimeouts not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPingTimeouts(tempVar)
            for logFunc in self._log('read-tag-values-ping-timeouts').debug3Func(): logFunc('read pingTimeouts. pingTimeouts=%s, tempValue=%s', self.pingTimeouts, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "counters", 
        "namespace": "counters", 
        "className": "CountersMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.connectivity_check.ipv4.counters.counters_maapi_gen import CountersMaapi", 
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
            "yangName": "connectivity-check", 
            "namespace": "connectivity_check", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "connectivity-check"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "ipv4", 
            "namespace": "ipv4", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "ipv4"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "counters", 
            "namespace": "counters", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "counters"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "arpFailures", 
            "yangName": "arp-failures", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "arpRequestsSent", 
            "yangName": "arp-requests-sent", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pingSuccesses", 
            "yangName": "ping-successes", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pingRequestsSent", 
            "yangName": "ping-requests-sent", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "arpSuccesses", 
            "yangName": "arp-successes", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pingFailures", 
            "yangName": "ping-failures", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "arpTimeouts", 
            "yangName": "arp-timeouts", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pingTimeouts", 
            "yangName": "ping-timeouts", 
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
            "qwilt_tech_interfaces"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "arpFailures", 
            "yangName": "arp-failures", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "arpRequestsSent", 
            "yangName": "arp-requests-sent", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pingSuccesses", 
            "yangName": "ping-successes", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pingRequestsSent", 
            "yangName": "ping-requests-sent", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "arpSuccesses", 
            "yangName": "arp-successes", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pingFailures", 
            "yangName": "ping-failures", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "arpTimeouts", 
            "yangName": "arp-timeouts", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pingTimeouts", 
            "yangName": "ping-timeouts", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


