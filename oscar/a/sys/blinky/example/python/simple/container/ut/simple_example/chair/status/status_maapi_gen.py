


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

        

        
        self.versionRequested = False
        self.version = None
        self.versionSet = False
        
        self.healthRequested = False
        self.health = None
        self.healthSet = False
        
        self.numOfCracksRequested = False
        self.numOfCracks = None
        self.numOfCracksSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestVersion(True)
        
        self.requestHealth(True)
        
        self.requestNumOfCracks(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestVersion(False)
        
        self.requestHealth(False)
        
        self.requestNumOfCracks(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestVersion(True)
        
        self.requestHealth(True)
        
        self.requestNumOfCracks(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestVersion(False)
        
        self.requestHealth(False)
        
        self.requestNumOfCracks(False)
        
        

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



    def requestVersion (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-version').debug3Func(): logFunc('called. requested=%s', requested)
        self.versionRequested = requested
        self.versionSet = False

    def isVersionRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-version-requested').debug3Func(): logFunc('called. requested=%s', self.versionRequested)
        return self.versionRequested

    def getVersion (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-version').debug3Func(): logFunc('called. self.versionSet=%s, self.version=%s', self.versionSet, self.version)
        if self.versionSet:
            return self.version
        return None

    def hasVersion (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-version').debug3Func(): logFunc('called. self.versionSet=%s, self.version=%s', self.versionSet, self.version)
        if self.versionSet:
            return True
        return False

    def setVersion (self, version):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-version').debug3Func(): logFunc('called. version=%s, old=%s', version, self.version)
        self.versionSet = True
        self.version = version

    def requestHealth (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-health').debug3Func(): logFunc('called. requested=%s', requested)
        self.healthRequested = requested
        self.healthSet = False

    def isHealthRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-health-requested').debug3Func(): logFunc('called. requested=%s', self.healthRequested)
        return self.healthRequested

    def getHealth (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-health').debug3Func(): logFunc('called. self.healthSet=%s, self.health=%s', self.healthSet, self.health)
        if self.healthSet:
            return self.health
        return None

    def hasHealth (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-health').debug3Func(): logFunc('called. self.healthSet=%s, self.health=%s', self.healthSet, self.health)
        if self.healthSet:
            return True
        return False

    def setHealth (self, health):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-health').debug3Func(): logFunc('called. health=%s, old=%s', health, self.health)
        self.healthSet = True
        self.health = health

    def requestNumOfCracks (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-numofcracks').debug3Func(): logFunc('called. requested=%s', requested)
        self.numOfCracksRequested = requested
        self.numOfCracksSet = False

    def isNumOfCracksRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-numofcracks-requested').debug3Func(): logFunc('called. requested=%s', self.numOfCracksRequested)
        return self.numOfCracksRequested

    def getNumOfCracks (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-numofcracks').debug3Func(): logFunc('called. self.numOfCracksSet=%s, self.numOfCracks=%s', self.numOfCracksSet, self.numOfCracks)
        if self.numOfCracksSet:
            return self.numOfCracks
        return None

    def hasNumOfCracks (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-numofcracks').debug3Func(): logFunc('called. self.numOfCracksSet=%s, self.numOfCracks=%s', self.numOfCracksSet, self.numOfCracks)
        if self.numOfCracksSet:
            return True
        return False

    def setNumOfCracks (self, numOfCracks):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-numofcracks').debug3Func(): logFunc('called. numOfCracks=%s, old=%s', numOfCracks, self.numOfCracks)
        self.numOfCracksSet = True
        self.numOfCracks = numOfCracks


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.version = 0
        self.versionSet = False
        
        self.health = 0
        self.healthSet = False
        
        self.numOfCracks = 0
        self.numOfCracksSet = False
        

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("status", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example", "se"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("chair", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example", "se"))
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

        
        if self.isVersionRequested():
            valVersion = Value()
            valVersion.setEmpty()
            tagValueList.push(("version", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example"), valVersion)
        
        if self.isHealthRequested():
            valHealth = Value()
            valHealth.setEmpty()
            tagValueList.push(("health", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example"), valHealth)
        
        if self.isNumOfCracksRequested():
            valNumOfCracks = Value()
            valNumOfCracks.setEmpty()
            tagValueList.push(("num-of-cracks", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example"), valNumOfCracks)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isVersionRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "version") or \
                (ns != "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-version').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "version", "version", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-version-bad-value').infoFunc(): logFunc('version not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setVersion(tempVar)
            for logFunc in self._log('read-tag-values-version').debug3Func(): logFunc('read version. version=%s, tempValue=%s', self.version, tempValue.getType())
        
        if self.isHealthRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "health") or \
                (ns != "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-health').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "health", "health", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-health-bad-value').infoFunc(): logFunc('health not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setHealth(tempVar)
            for logFunc in self._log('read-tag-values-health').debug3Func(): logFunc('read health. health=%s, tempValue=%s', self.health, tempValue.getType())
        
        if self.isNumOfCracksRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "num-of-cracks") or \
                (ns != "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-numofcracks').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "numOfCracks", "num-of-cracks", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-num-of-cracks-bad-value').infoFunc(): logFunc('numOfCracks not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setNumOfCracks(tempVar)
            for logFunc in self._log('read-tag-values-num-of-cracks').debug3Func(): logFunc('read numOfCracks. numOfCracks=%s, tempValue=%s', self.numOfCracks, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "status", 
        "namespace": "status", 
        "className": "StatusMaapi", 
        "importStatement": "from a.sys.blinky.example.python.simple.container.ut.simple_example.chair.status.status_maapi_gen import StatusMaapi", 
        "baseClassName": "StatusMaapiBase", 
        "baseModule": "status_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "se", 
            "yangName": "chair", 
            "namespace": "chair", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example", 
            "name": "chair"
        }, 
        {
            "moduleYangNamespacePrefix": "se", 
            "yangName": "status", 
            "namespace": "status", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example", 
            "name": "status"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example", 
            "moduleYangNamespacePrefix": "se", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "version", 
            "yangName": "version", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example", 
            "moduleYangNamespacePrefix": "se", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "health", 
            "yangName": "health", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example", 
            "moduleYangNamespacePrefix": "se", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "numOfCracks", 
            "yangName": "num-of-cracks", 
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
            "sys", 
            "blinky", 
            "example", 
            "python", 
            "simple", 
            "container", 
            "ut", 
            "simple_example"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example", 
            "moduleYangNamespacePrefix": "se", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "version", 
            "yangName": "version", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example", 
            "moduleYangNamespacePrefix": "se", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "health", 
            "yangName": "health", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example", 
            "moduleYangNamespacePrefix": "se", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "numOfCracks", 
            "yangName": "num-of-cracks", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


