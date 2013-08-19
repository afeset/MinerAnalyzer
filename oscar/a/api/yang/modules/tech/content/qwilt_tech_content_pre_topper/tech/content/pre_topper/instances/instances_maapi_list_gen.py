


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

from instances_maapi_list_base_gen import InstancesMaapiListBase
from instances_maapi_gen import BlinkyInstancesMaapi

class BlinkyInstancesMaapiList(InstancesMaapiListBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-instances")
        self.domain = None

        self.instancess = {}
        self.instancesKeys = []

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def newInstances (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-instances').debug3Func(): logFunc('called.')
        instances = BlinkyInstancesMaapi(self._log)
        instances.init(self.domain)
        return instances

    def setInstancesObj (self, key, instancesObj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-instances-obj').debug3Func(): logFunc('called. key=%s, instancesObj=%s', key, instancesObj)
        if key not in self.instancess:
            self.instancesKeys.append(key)
        self.instancess[str(key)] = instancesObj

    def getInstancesObj (self, key):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-instances-obj').debug3Func(): logFunc('called. key=%s', key)
        if str(key) in self.instancess.keys():
            for logFunc in self._log('get-instances-obj-done').debug3Func(): logFunc('Done. found key=%s, obj=%s', key, self.instancess[str(key)])
            return self.instancess[str(key)]
        for logFunc in self._log('get-instances-obj-missing').errorFunc(): logFunc('instances %s not in instancess. existing items: %s', key, self.instancess.keys())
        return None

    def deleteInstances (self, key):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('delete-instances').debug3Func(): logFunc('called. key=%s', key)
        if str(key) not in self.instancesKeys:
            for logFunc in self._log('delete-instances-not-found').warningFunc(): logFunc('key=%s is missing from the instancesKeys list', key)
            if str(key) in self.instancess.keys():
                # internal problem - list & dictionary are not synced
                for logFunc in self._log('delete-instances-not-found-but-in-dict').errorFunc(): logFunc('instancess dictionary & instancesKeys list are out-of-sync. key %s exists in dict but not in list', key)
            return ReturnCodes.kGeneralError
        if str(key) not in self.instancess.keys():
            # internal problem - list & dictionary are not synced
            for logFunc in self._log('delete-instances-not-found-but-in-list').errorFunc(): logFunc('instancess dictionary & instancesKeys list are out-of-sync. key %s exists in list but not in dict', key)
            return ReturnCodes.kGeneralError

        self.instancesKeys.remove(str(key))
        del self.instancess[str(key)]

    def hasInstancesObj (self, key):
        self.myInitGuard.isInitOrCrash()
        has = False
        if str(key) in self.instancess.keys():
            if self.instancess[str(key)]:
                has = True
        for logFunc in self._log('has-instances-done').debug3Func(): logFunc('done. key=%s exists=%s', key, has)
        return has

    def getListKeys (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-list-keys').debug3Func(): logFunc('called. keys=%s', [str(x) for x in self.instancesKeys])
        return self.instancesKeys

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called.')
        for instances in self.instancess.values():
            instances.requestConfigAndOper()

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called.')
        for instances in self.instancess.values():
            instances.requestConfig()

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called.')
        for instances in self.instancess.values():
            instances.requestOper()

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called.')
        for instances in self.instancess.values():
            instances.clearAllRequested()

    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')
        for instances in self.instancess.values():
            if instances:
                instances._clearAllReadData()

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        for key in self.instancess.keys():
            if self.instancess[key]:
                self.instancess[key].clearAllSet()
            else:
                self.instancesKeys.remove(str(key))
                del self.instancess[str(key)]

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS. junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()

        
        
        
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("pre-topper", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", "qtc-pt"))
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
                      
                      , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-list-keys').debug3Func(): logFunc('called')

        # clear the old map
        self.instancess = {}
        self.instancesKeys = []

        keyPath = self._getSelfKeyPath(
                                       None)

        xmlVal = Value()
        xmlVal.setXmlTag(("instances", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", "qtc-pt"))
        keyPath.addKeyPathPostfix(xmlVal)

        keys = []

        res = self.domain.readMaapiKeys(keyPath, keys, trxContext)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-list-keys-domain-failed').errorFunc(): logFunc('domain.readMaapiKeys() failed')
            return ReturnCodes.kGeneralError

        for key in keys:
            self.instancesKeys.append(key.getCannonicalStr())
            self.instancess[key.getCannonicalStr()] = None

        return ReturnCodes.kOk

    def write (self
               , trxContext=None
               ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(
                                   trxContext)

    def read (self
              
              , trxContext=None):
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

    def _internalWrite (self, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called.')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('internal-write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed')
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
        for logFunc in self._log('internal-read').debug3Func(): logFunc('called. readAllOrFail=%s', readAllOrFail)

        if readAllOrFail:
            self._clearAllReadData()

        tagValueList = TagValues()

        res = self._fillReadTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('internal-read-fill-read-tag-values-failed').errorFunc(): logFunc('_fillReadTagValues() failed')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(
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
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        for key in self.instancess.keys():
            if self.instancess[key]:
                res = self.instancess[key]._collectItemsToDelete(
                                                                     key,
                                                                     itemsToDelete)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('collect-items-to-delete-instances-failed').errorFunc(): logFunc('instancesObj._collectItemsToDelete() failed. key=%s. PARAMS', key)
                    return ReturnCodes.kGeneralError

            else:
                keyPath = self._getSelfKeyPath(
                                               None)
                xmlVal = Value()
                xmlVal.setXmlTag(("instances", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", "qtc-pt"))
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

        for key in self.instancess.keys():
            if self.instancess[key]:
                valBegin = Value()
                (tag, ns, prefix) = ("instances", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", "qtc-pt")
                valBegin.setXmlBegin((tag, ns, prefix))
                tagValueList.push((tag, ns), valBegin)

                valKey = Value()
                valKey.setString(key)
                tagValueList.push(("instance", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper"), valKey)

                tagValueListLen = tagValueList.getLen()

                res = self.instancess[key]._fillWriteTagValues(tagValueList)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('fill-write-tag-values-instances-failed').errorFunc(): logFunc('instances._fillWriteTagValues() failed. key=%s', key)
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

        for key in self.instancess.keys():
            if self.instancess[key]:
                valBegin = Value()
                (tag, ns, prefix) = ("instances", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", "qtc-pt")
                valBegin.setXmlBegin((tag, ns, prefix))
                tagValueList.push((tag, ns), valBegin)

                valKey = Value()
                valKey.setString(key)
                tagValueList.push(("instance", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper"), valKey)

                tagValueListLen = tagValueList.getLen()

                res = self.instancess[key]._fillReadTagValues(tagValueList)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('fill-read-tag-values-instances-failed').errorFunc(): logFunc('instances._fillReadTagValues() failed. key=%s', key)
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

        for key in self.instancess.keys():
            if self.instancess[key]:
                ((tag, ns), valBegin) = tagValueList.popFront()
                if (tag != "instances") or \
                    (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper") or \
                    (valBegin.getType() != Value.kXmlBegin):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                            "instances", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", Value.kXmlBegin,
                                                                            tag, ns, valBegin.getType())
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                ((tag, ns), valKey) = tagValueList.popFront()
                if (tag != "instance") or \
                    (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper"):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-key').errorFunc(): logFunc('got unexpected tag-value for key. expected: (%s, %s), got: (%s, %s)',
                                                                          "instance", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", tag, ns)
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                key = valKey.asString()
                if res != ReturnCodes.kOk:
                    if readAllOrFail:
                        self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                res = self.instancess[key]._readTagValues(tagValueList, readAllOrFail)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('read-tag-values-instances-failed').errorFunc(): logFunc('instances._readTagValues() failed. key=%s', key)
                    if readAllOrFail:
                        self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                ((tag, ns), valEnd) = tagValueList.popFront()
                if (tag != "instances") or \
                    (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper") or \
                    (valEnd.getType() != Value.kXmlEnd):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                          "instances", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", Value.kXmlEnd,
                                                                            tag, ns, valEnd.getType())
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. tagValueList=%s, readAllOrFail=%s', tagValueList, readAllOrFail)
        return ReturnCodes.kOk

"""
Extracted from the below data: 
{
    "node": {
        "containerClassName": "BlinkyInstancesMaapi", 
        "name": "instances", 
        "keyLeaf": {
            "varName": "instances", 
            "yangName": "instance", 
            "typeHandler": "handler: StringHandler"
        }, 
        "yangName": "instances", 
        "namespace": "instances", 
        "moduleYangNamespacePrefix": "qtc-pt", 
        "className": "InstancesMaapiList", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_pre_topper.tech.content.pre_topper.instances.instances_maapi_list_gen import InstancesMaapiList", 
        "baseClassName": "InstancesMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
        "containerModule": "instances_maapi_gen", 
        "baseModule": "instances_maapi_list_base_gen"
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
            "moduleYangNamespacePrefix": "qtc-pt", 
            "yangName": "pre-topper", 
            "namespace": "pre_topper", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "name": "pre-topper"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-pt", 
            "isCurrent": true, 
            "yangName": "instances", 
            "namespace": "instances", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "keyLeaf": {
                "varName": "instances", 
                "yangName": "instance", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "instances"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "warnTotalRecordCount", 
            "yangName": "warn-total-record-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "periodicWorkRecordCount", 
            "yangName": "periodic-work-record-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "aggregationPeriod", 
            "yangName": "aggregation-period", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxTotalRecordCount", 
            "yangName": "max-total-record-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "periodicWorkInterval", 
            "yangName": "periodic-work-interval", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "warnSessionIdCount", 
            "yangName": "warn-session-id-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "instance", 
            "yangName": "instance", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxSessionIdCount", 
            "yangName": "max-session-id-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rotateFileInterval", 
            "yangName": "rotate-file-interval", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "recordWriteInterval", 
            "yangName": "record-write-interval", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "archive", 
            "yangName": "archive", 
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
            "qwilt_tech_content_pre_topper"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "warnTotalRecordCount", 
            "yangName": "warn-total-record-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "periodicWorkRecordCount", 
            "yangName": "periodic-work-record-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "aggregationPeriod", 
            "yangName": "aggregation-period", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxTotalRecordCount", 
            "yangName": "max-total-record-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "periodicWorkInterval", 
            "yangName": "periodic-work-interval", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "warnSessionIdCount", 
            "yangName": "warn-session-id-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "instance", 
            "yangName": "instance", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxSessionIdCount", 
            "yangName": "max-session-id-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rotateFileInterval", 
            "yangName": "rotate-file-interval", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "recordWriteInterval", 
            "yangName": "record-write-interval", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "archive", 
            "yangName": "archive", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


