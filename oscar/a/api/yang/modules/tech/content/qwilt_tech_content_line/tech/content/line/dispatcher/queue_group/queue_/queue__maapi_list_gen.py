


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

from queue__maapi_list_base_gen import QueueMaapiListBase
from queue__maapi_gen import BlinkyQueueMaapi

class BlinkyQueueMaapiList(QueueMaapiListBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-queue_")
        self.domain = None

        self.queue_s = {}
        self.queue_Keys = []

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def newQueue_ (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-queue_').debug3Func(): logFunc('called.')
        queue_ = BlinkyQueueMaapi(self._log)
        queue_.init(self.domain)
        return queue_

    def setQueue_Obj (self, key, queue_Obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-queue_-obj').debug3Func(): logFunc('called. key=%s, queue_Obj=%s', key, queue_Obj)
        if key not in self.queue_s:
            self.queue_Keys.append(key)
        self.queue_s[str(key)] = queue_Obj

    def getQueue_Obj (self, key):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-queue_-obj').debug3Func(): logFunc('called. key=%s', key)
        if str(key) in self.queue_s.keys():
            for logFunc in self._log('get-queue_-obj-done').debug3Func(): logFunc('Done. found key=%s, obj=%s', key, self.queue_s[str(key)])
            return self.queue_s[str(key)]
        for logFunc in self._log('get-queue_-obj-missing').errorFunc(): logFunc('queue_ %s not in queue_s. existing items: %s', key, self.queue_s.keys())
        return None

    def deleteQueue_ (self, key):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('delete-queue_').debug3Func(): logFunc('called. key=%s', key)
        if str(key) not in self.queue_Keys:
            for logFunc in self._log('delete-queue_-not-found').warningFunc(): logFunc('key=%s is missing from the queue_Keys list', key)
            if str(key) in self.queue_s.keys():
                # internal problem - list & dictionary are not synced
                for logFunc in self._log('delete-queue_-not-found-but-in-dict').errorFunc(): logFunc('queue_s dictionary & queue_Keys list are out-of-sync. key %s exists in dict but not in list', key)
            return ReturnCodes.kGeneralError
        if str(key) not in self.queue_s.keys():
            # internal problem - list & dictionary are not synced
            for logFunc in self._log('delete-queue_-not-found-but-in-list').errorFunc(): logFunc('queue_s dictionary & queue_Keys list are out-of-sync. key %s exists in list but not in dict', key)
            return ReturnCodes.kGeneralError

        self.queue_Keys.remove(str(key))
        del self.queue_s[str(key)]

    def hasQueue_Obj (self, key):
        self.myInitGuard.isInitOrCrash()
        has = False
        if str(key) in self.queue_s.keys():
            if self.queue_s[str(key)]:
                has = True
        for logFunc in self._log('has-queue_-done').debug3Func(): logFunc('done. key=%s exists=%s', key, has)
        return has

    def getListKeys (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-list-keys').debug3Func(): logFunc('called. keys=%s', [str(x) for x in self.queue_Keys])
        return self.queue_Keys

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called.')
        for queue_ in self.queue_s.values():
            queue_.requestConfigAndOper()

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called.')
        for queue_ in self.queue_s.values():
            queue_.requestConfig()

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called.')
        for queue_ in self.queue_s.values():
            queue_.requestOper()

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called.')
        for queue_ in self.queue_s.values():
            queue_.clearAllRequested()

    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')
        for queue_ in self.queue_s.values():
            if queue_:
                queue_._clearAllReadData()

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        for key in self.queue_s.keys():
            if self.queue_s[key]:
                self.queue_s[key].clearAllSet()
            else:
                self.queue_Keys.remove(str(key))
                del self.queue_s[str(key)]

    def _getSelfKeyPath (self, line
                         , queueGroup
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS. junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()

        
        
        
        
        ancestorVal = Value()
        ancestorVal.setString(queueGroup);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("queue-group", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("dispatcher", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line"))
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

    def readListKeys (self
                      , line
                      , queueGroup
                      
                      , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-list-keys').debug3Func(): logFunc('called')

        # clear the old map
        self.queue_s = {}
        self.queue_Keys = []

        keyPath = self._getSelfKeyPath(line, 
                                       queueGroup, 
                                       
                                       None)

        xmlVal = Value()
        xmlVal.setXmlTag(("queue", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line"))
        keyPath.addKeyPathPostfix(xmlVal)

        keys = []

        res = self.domain.readMaapiKeys(keyPath, keys, trxContext)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-list-keys-domain-failed').errorFunc(): logFunc('domain.readMaapiKeys() failed')
            return ReturnCodes.kGeneralError

        for key in keys:
            self.queue_Keys.append(key.getCannonicalStr())
            self.queue_s[key.getCannonicalStr()] = None

        return ReturnCodes.kOk

    def write (self
               , line
               , queueGroup
               , trxContext=None
               ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(line, queueGroup, 
                                   trxContext)

    def read (self
              , line
              , queueGroup
              
              , trxContext=None):
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(line, queueGroup, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , line
                       , queueGroup
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(line, queueGroup, 
                                  True,
                                  trxContext)

    def _internalWrite (self, 
                        line, 
                        queueGroup, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called.')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('internal-write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(line, 
                                         queueGroup, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(line, 
                                       queueGroup, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       line, 
                       queueGroup, 
                       
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

        keyPath = self._getSelfKeyPath(line, 
                                       queueGroup, 
                                       
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
                               line, 
                               queueGroup, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        for key in self.queue_s.keys():
            if self.queue_s[key]:
                res = self.queue_s[key]._collectItemsToDelete(line, 
                                                                     queueGroup, 
                                                                     
                                                                     key,
                                                                     itemsToDelete)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('collect-items-to-delete-queue_-failed').errorFunc(): logFunc('queue_Obj._collectItemsToDelete() failed. key=%s. PARAMS', key)
                    return ReturnCodes.kGeneralError

            else:
                keyPath = self._getSelfKeyPath(line, 
                                               queueGroup, 
                                               
                                               None)
                xmlVal = Value()
                xmlVal.setXmlTag(("queue", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line"))
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

        for key in self.queue_s.keys():
            if self.queue_s[key]:
                valBegin = Value()
                (tag, ns, prefix) = ("queue", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line")
                valBegin.setXmlBegin((tag, ns, prefix))
                tagValueList.push((tag, ns), valBegin)

                valKey = Value()
                valKey.setString(key)
                tagValueList.push(("name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valKey)

                tagValueListLen = tagValueList.getLen()

                res = self.queue_s[key]._fillWriteTagValues(tagValueList)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('fill-write-tag-values-queue_-failed').errorFunc(): logFunc('queue_._fillWriteTagValues() failed. key=%s', key)
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

        for key in self.queue_s.keys():
            if self.queue_s[key]:
                valBegin = Value()
                (tag, ns, prefix) = ("queue", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line")
                valBegin.setXmlBegin((tag, ns, prefix))
                tagValueList.push((tag, ns), valBegin)

                valKey = Value()
                valKey.setString(key)
                tagValueList.push(("name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valKey)

                tagValueListLen = tagValueList.getLen()

                res = self.queue_s[key]._fillReadTagValues(tagValueList)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('fill-read-tag-values-queue_-failed').errorFunc(): logFunc('queue_._fillReadTagValues() failed. key=%s', key)
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

        for key in self.queue_s.keys():
            if self.queue_s[key]:
                ((tag, ns), valBegin) = tagValueList.popFront()
                if (tag != "queue") or \
                    (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line") or \
                    (valBegin.getType() != Value.kXmlBegin):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                            "queue", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", Value.kXmlBegin,
                                                                            tag, ns, valBegin.getType())
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                ((tag, ns), valKey) = tagValueList.popFront()
                if (tag != "name") or \
                    (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-key').errorFunc(): logFunc('got unexpected tag-value for key. expected: (%s, %s), got: (%s, %s)',
                                                                          "name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                key = valKey.asString()
                if res != ReturnCodes.kOk:
                    if readAllOrFail:
                        self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                res = self.queue_s[key]._readTagValues(tagValueList, readAllOrFail)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('read-tag-values-queue_-failed').errorFunc(): logFunc('queue_._readTagValues() failed. key=%s', key)
                    if readAllOrFail:
                        self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                ((tag, ns), valEnd) = tagValueList.popFront()
                if (tag != "queue") or \
                    (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line") or \
                    (valEnd.getType() != Value.kXmlEnd):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                          "queue", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", Value.kXmlEnd,
                                                                            tag, ns, valEnd.getType())
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. tagValueList=%s, readAllOrFail=%s', tagValueList, readAllOrFail)
        return ReturnCodes.kOk

"""
Extracted from the below data: 
{
    "node": {
        "containerClassName": "BlinkyQueueMaapi", 
        "name": "queue_", 
        "keyLeaf": {
            "varName": "queue_", 
            "yangName": "name", 
            "typeHandler": "handler: StringHandler"
        }, 
        "yangName": "queue", 
        "namespace": "queue_", 
        "moduleYangNamespacePrefix": "qtc-line", 
        "className": "QueueMaapiList", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.dispatcher.queue_group.queue_.queue__maapi_list_gen import QueueMaapiList", 
        "baseClassName": "QueueMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
        "containerModule": "queue__maapi_gen", 
        "baseModule": "queue__maapi_list_base_gen"
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
                "yangName": "number", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "line"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "yangName": "dispatcher", 
            "namespace": "dispatcher", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "dispatcher"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "isCurrent": false, 
            "yangName": "queue-group", 
            "namespace": "queue_group", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "keyLeaf": {
                "varName": "queueGroup", 
                "yangName": "name", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "queue-group"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "isCurrent": true, 
            "yangName": "queue", 
            "namespace": "queue_", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "keyLeaf": {
                "varName": "queue_", 
                "yangName": "name", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "queue_"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "memberName": "systemDefaults", 
            "yangName": "system-defaults", 
            "className": "BlinkySystemDefaultsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.dispatcher.queue_group.queue_.system_defaults.system_defaults_maapi_list_gen import BlinkySystemDefaultsMaapi", 
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
            "memberName": "queueThresholdLow", 
            "yangName": "queue-threshold-low", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "queueSize", 
            "yangName": "queue-size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "queueThresholdHigh", 
            "yangName": "queue-threshold-high", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
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
            "qwilt_tech_content_line"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "queueThresholdLow", 
            "yangName": "queue-threshold-low", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "queueSize", 
            "yangName": "queue-size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "queueThresholdHigh", 
            "yangName": "queue-threshold-high", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


