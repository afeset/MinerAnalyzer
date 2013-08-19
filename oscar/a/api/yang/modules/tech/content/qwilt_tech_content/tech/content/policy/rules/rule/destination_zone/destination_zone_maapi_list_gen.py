


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

from destination_zone_maapi_list_base_gen import DestinationZoneMaapiListBase
from destination_zone_maapi_gen import BlinkyDestinationZoneMaapi

class BlinkyDestinationZoneMaapiList(DestinationZoneMaapiListBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-destinationZone")
        self.domain = None

        self.destinationZones = {}
        self.destinationZoneKeys = []

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def newDestinationZone (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-destinationzone').debug3Func(): logFunc('called.')
        destinationZone = BlinkyDestinationZoneMaapi(self._log)
        destinationZone.init(self.domain)
        return destinationZone

    def setDestinationZoneObj (self, key, destinationZoneObj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-destinationzone-obj').debug3Func(): logFunc('called. key=%s, destinationZoneObj=%s', key, destinationZoneObj)
        if key not in self.destinationZones:
            self.destinationZoneKeys.append(key)
        self.destinationZones[str(key)] = destinationZoneObj

    def getDestinationZoneObj (self, key):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-destinationzone-obj').debug3Func(): logFunc('called. key=%s', key)
        if str(key) in self.destinationZones.keys():
            for logFunc in self._log('get-destinationzone-obj-done').debug3Func(): logFunc('Done. found key=%s, obj=%s', key, self.destinationZones[str(key)])
            return self.destinationZones[str(key)]
        for logFunc in self._log('get-destinationzone-obj-missing').errorFunc(): logFunc('destinationZone %s not in destinationZones. existing items: %s', key, self.destinationZones.keys())
        return None

    def deleteDestinationZone (self, key):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('delete-destinationzone').debug3Func(): logFunc('called. key=%s', key)
        if str(key) not in self.destinationZoneKeys:
            for logFunc in self._log('delete-destinationZone-not-found').warningFunc(): logFunc('key=%s is missing from the destinationZoneKeys list', key)
            if str(key) in self.destinationZones.keys():
                # internal problem - list & dictionary are not synced
                for logFunc in self._log('delete-destinationzone-not-found-but-in-dict').errorFunc(): logFunc('destinationZones dictionary & destinationZoneKeys list are out-of-sync. key %s exists in dict but not in list', key)
            return ReturnCodes.kGeneralError
        if str(key) not in self.destinationZones.keys():
            # internal problem - list & dictionary are not synced
            for logFunc in self._log('delete-destinationZone-not-found-but-in-list').errorFunc(): logFunc('destinationZones dictionary & destinationZoneKeys list are out-of-sync. key %s exists in list but not in dict', key)
            return ReturnCodes.kGeneralError

        self.destinationZoneKeys.remove(str(key))
        del self.destinationZones[str(key)]

    def hasDestinationZoneObj (self, key):
        self.myInitGuard.isInitOrCrash()
        has = False
        if str(key) in self.destinationZones.keys():
            if self.destinationZones[str(key)]:
                has = True
        for logFunc in self._log('has-destinationzone-done').debug3Func(): logFunc('done. key=%s exists=%s', key, has)
        return has

    def getListKeys (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-list-keys').debug3Func(): logFunc('called. keys=%s', [str(x) for x in self.destinationZoneKeys])
        return self.destinationZoneKeys

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called.')
        for destinationZone in self.destinationZones.values():
            destinationZone.requestConfigAndOper()

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called.')
        for destinationZone in self.destinationZones.values():
            destinationZone.requestConfig()

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called.')
        for destinationZone in self.destinationZones.values():
            destinationZone.requestOper()

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called.')
        for destinationZone in self.destinationZones.values():
            destinationZone.clearAllRequested()

    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')
        for destinationZone in self.destinationZones.values():
            if destinationZone:
                destinationZone._clearAllReadData()

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        for key in self.destinationZones.keys():
            if self.destinationZones[key]:
                self.destinationZones[key].clearAllSet()
            else:
                self.destinationZoneKeys.remove(str(key))
                del self.destinationZones[str(key)]

    def _getSelfKeyPath (self, rule
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS. junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()

        
        
        
        
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

    def readListKeys (self
                      , rule
                      
                      , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-list-keys').debug3Func(): logFunc('called')

        # clear the old map
        self.destinationZones = {}
        self.destinationZoneKeys = []

        keyPath = self._getSelfKeyPath(rule, 
                                       
                                       None)

        xmlVal = Value()
        xmlVal.setXmlTag(("destination-zone", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc"))
        keyPath.addKeyPathPostfix(xmlVal)

        keys = []

        res = self.domain.readMaapiKeys(keyPath, keys, trxContext)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-list-keys-domain-failed').errorFunc(): logFunc('domain.readMaapiKeys() failed')
            return ReturnCodes.kGeneralError

        for key in keys:
            self.destinationZoneKeys.append(key.getCannonicalStr())
            self.destinationZones[key.getCannonicalStr()] = None

        return ReturnCodes.kOk

    def write (self
               , rule
               , trxContext=None
               ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(rule, 
                                   trxContext)

    def read (self
              , rule
              
              , trxContext=None):
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

    def _internalWrite (self, 
                        rule, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called.')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('internal-write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed')
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
        for logFunc in self._log('internal-read').debug3Func(): logFunc('called. readAllOrFail=%s', readAllOrFail)

        if readAllOrFail:
            self._clearAllReadData()

        tagValueList = TagValues()

        res = self._fillReadTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('internal-read-fill-read-tag-values-failed').errorFunc(): logFunc('_fillReadTagValues() failed')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(rule, 
                                       
                                       None)

        res = self.domain.readMaapi(tagValueList, keyPath, trxContext)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('internal-read-domain-failed').errorFunc(): logFunc('domain.readMaapi() failed.')
            return ReturnCodes.kGeneralError

        res = self._readTagValues(tagValueList, readAllOrFail)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('internal-read-read-tag-values-failed').errorFunc(): logFunc('_readTagValues() failed.')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-read-done').debug3Func(): logFunc('done. readAllOrFail=%s', readAllOrFail)
        return ReturnCodes.kOk

    def _collectItemsToDelete (self,
                               rule, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        for key in self.destinationZones.keys():
            if self.destinationZones[key]:
                res = self.destinationZones[key]._collectItemsToDelete(rule, 
                                                                     
                                                                     key,
                                                                     itemsToDelete)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('collect-items-to-delete-destinationZone-failed').errorFunc(): logFunc('destinationZoneObj._collectItemsToDelete() failed. key=%s. PARAMS', key)
                    return ReturnCodes.kGeneralError

            else:
                keyPath = self._getSelfKeyPath(rule, 
                                               
                                               None)
                xmlVal = Value()
                xmlVal.setXmlTag(("destination-zone", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc"))
                keyPath.addKeyPathPostfix(xmlVal)
                valKey = Value()
                valKey.setString(key)
                keyPath.addKeyPathPostfix(valKey)

                itemsToDelete.append(keyPath)

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        for key in self.destinationZones.keys():
            if self.destinationZones[key]:
                valBegin = Value()
                (tag, ns, prefix) = ("destination-zone", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc")
                valBegin.setXmlBegin((tag, ns, prefix))
                tagValueList.push((tag, ns), valBegin)

                valKey = Value()
                valKey.setString(key)
                tagValueList.push(("zone", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"), valKey)

                tagValueListLen = tagValueList.getLen()

                res = self.destinationZones[key]._fillWriteTagValues(tagValueList)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('fill-write-tag-values-destinationZone-failed').errorFunc(): logFunc('destinationZone._fillWriteTagValues() failed. key=%s', key)
                    return ReturnCodes.kGeneralError

                if tagValueList.getLen() == tagValueListLen:
                    # descendant didn't add anything, no need to read it.
                    tagValueList.pop()
                    tagValueList.pop()
                else:
                    valEnd = Value()
                    valEnd.setXmlEnd((tag, ns, prefix))
                    tagValueList.push((tag, ns), valEnd)

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        for key in self.destinationZones.keys():
            if self.destinationZones[key]:
                valBegin = Value()
                (tag, ns, prefix) = ("destination-zone", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc")
                valBegin.setXmlBegin((tag, ns, prefix))
                tagValueList.push((tag, ns), valBegin)

                valKey = Value()
                valKey.setString(key)
                tagValueList.push(("zone", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"), valKey)

                tagValueListLen = tagValueList.getLen()

                res = self.destinationZones[key]._fillReadTagValues(tagValueList)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('fill-read-tag-values-destinationZone-failed').errorFunc(): logFunc('destinationZone._fillReadTagValues() failed. key=%s', key)
                    return ReturnCodes.kGeneralError

                if tagValueList.getLen() == tagValueListLen:
                    # descendant didn't add anything, no need to read it.
                    tagValueList.pop()
                    tagValueList.pop()
                else:
                    valEnd = Value()
                    valEnd.setXmlEnd((tag, ns, prefix))
                    tagValueList.push((tag, ns), valEnd)

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. tagValueList=%s, readAllOrFail=%s', tagValueList, readAllOrFail)

        res = ReturnCodes.kOk

        for key in self.destinationZones.keys():
            if self.destinationZones[key]:
                ((tag, ns), valBegin) = tagValueList.popFront()
                if (tag != "destination-zone") or \
                    (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content") or \
                    (valBegin.getType() != Value.kXmlBegin):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                            "destination-zone", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", Value.kXmlBegin,
                                                                            tag, ns, valBegin.getType())
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                ((tag, ns), valKey) = tagValueList.popFront()
                if (tag != "zone") or \
                    (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-key').errorFunc(): logFunc('got unexpected tag-value for key. expected: (%s, %s), got: (%s, %s)',
                                                                          "zone", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", tag, ns)
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                key = valKey.asString()
                if res != ReturnCodes.kOk:
                    if readAllOrFail:
                        self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                res = self.destinationZones[key]._readTagValues(tagValueList, readAllOrFail)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('read-tag-values-destinationZone-failed').errorFunc(): logFunc('destinationZone._readTagValues() failed. key=%s', key)
                    if readAllOrFail:
                        self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                ((tag, ns), valEnd) = tagValueList.popFront()
                if (tag != "destination-zone") or \
                    (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content") or \
                    (valEnd.getType() != Value.kXmlEnd):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                          "destination-zone", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", Value.kXmlEnd,
                                                                            tag, ns, valEnd.getType())
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. tagValueList=%s, readAllOrFail=%s', tagValueList, readAllOrFail)
        return ReturnCodes.kOk

"""
Extracted from the below data: 
{
    "node": {
        "containerClassName": "BlinkyDestinationZoneMaapi", 
        "name": "destinationZone", 
        "keyLeaf": {
            "varName": "destinationZone", 
            "yangName": "zone", 
            "typeHandler": "handler: StringHandler"
        }, 
        "yangName": "destination-zone", 
        "namespace": "destination_zone", 
        "moduleYangNamespacePrefix": "qtc", 
        "className": "DestinationZoneMaapiList", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.policy.rules.rule.destination_zone.destination_zone_maapi_list_gen import DestinationZoneMaapiList", 
        "baseClassName": "DestinationZoneMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
        "containerModule": "destination_zone_maapi_gen", 
        "baseModule": "destination_zone_maapi_list_base_gen"
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
                "yangName": "name", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "rule"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "isCurrent": true, 
            "yangName": "destination-zone", 
            "namespace": "destination_zone", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "keyLeaf": {
                "varName": "destinationZone", 
                "yangName": "zone", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "destination-zone"
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
            "typeHandler": "handler: StringHandler", 
            "memberName": "zone", 
            "yangName": "zone", 
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
            "memberName": "zone", 
            "yangName": "zone", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


