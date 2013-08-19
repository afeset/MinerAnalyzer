


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

from logger_class_maapi_list_base_gen import LoggerClassMaapiListBase
from logger_class_maapi_gen import BlinkyLoggerClassMaapi

class BlinkyLoggerClassMaapiList(LoggerClassMaapiListBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-loggerClass")
        self.domain = None

        self.loggerClasss = {}
        self.loggerClassKeys = []

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def newLoggerClass (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-loggerclass').debug3Func(): logFunc('called.')
        loggerClass = BlinkyLoggerClassMaapi(self._log)
        loggerClass.init(self.domain)
        return loggerClass

    def setLoggerClassObj (self, key, loggerClassObj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-loggerclass-obj').debug3Func(): logFunc('called. key=%s, loggerClassObj=%s', key, loggerClassObj)
        if key not in self.loggerClasss:
            self.loggerClassKeys.append(key)
        self.loggerClasss[str(key)] = loggerClassObj

    def getLoggerClassObj (self, key):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-loggerclass-obj').debug3Func(): logFunc('called. key=%s', key)
        if str(key) in self.loggerClasss.keys():
            for logFunc in self._log('get-loggerclass-obj-done').debug3Func(): logFunc('Done. found key=%s, obj=%s', key, self.loggerClasss[str(key)])
            return self.loggerClasss[str(key)]
        for logFunc in self._log('get-loggerclass-obj-missing').errorFunc(): logFunc('loggerClass %s not in loggerClasss. existing items: %s', key, self.loggerClasss.keys())
        return None

    def deleteLoggerClass (self, key):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('delete-loggerclass').debug3Func(): logFunc('called. key=%s', key)
        if str(key) not in self.loggerClassKeys:
            for logFunc in self._log('delete-loggerClass-not-found').warningFunc(): logFunc('key=%s is missing from the loggerClassKeys list', key)
            if str(key) in self.loggerClasss.keys():
                # internal problem - list & dictionary are not synced
                for logFunc in self._log('delete-loggerclass-not-found-but-in-dict').errorFunc(): logFunc('loggerClasss dictionary & loggerClassKeys list are out-of-sync. key %s exists in dict but not in list', key)
            return ReturnCodes.kGeneralError
        if str(key) not in self.loggerClasss.keys():
            # internal problem - list & dictionary are not synced
            for logFunc in self._log('delete-loggerClass-not-found-but-in-list').errorFunc(): logFunc('loggerClasss dictionary & loggerClassKeys list are out-of-sync. key %s exists in list but not in dict', key)
            return ReturnCodes.kGeneralError

        self.loggerClassKeys.remove(str(key))
        del self.loggerClasss[str(key)]

    def hasLoggerClassObj (self, key):
        self.myInitGuard.isInitOrCrash()
        has = False
        if str(key) in self.loggerClasss.keys():
            if self.loggerClasss[str(key)]:
                has = True
        for logFunc in self._log('has-loggerclass-done').debug3Func(): logFunc('done. key=%s exists=%s', key, has)
        return has

    def getListKeys (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-list-keys').debug3Func(): logFunc('called. keys=%s', [str(x) for x in self.loggerClassKeys])
        return self.loggerClassKeys

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called.')
        for loggerClass in self.loggerClasss.values():
            loggerClass.requestConfigAndOper()

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called.')
        for loggerClass in self.loggerClasss.values():
            loggerClass.requestConfig()

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called.')
        for loggerClass in self.loggerClasss.values():
            loggerClass.requestOper()

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called.')
        for loggerClass in self.loggerClasss.values():
            loggerClass.clearAllRequested()

    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')
        for loggerClass in self.loggerClasss.values():
            if loggerClass:
                loggerClass._clearAllReadData()

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        for key in self.loggerClasss.keys():
            if self.loggerClasss[key]:
                self.loggerClasss[key].clearAllSet()
            else:
                self.loggerClassKeys.remove(str(key))
                del self.loggerClasss[str(key)]

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS. junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()

        
        
        
        
        
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
        self.loggerClasss = {}
        self.loggerClassKeys = []

        keyPath = self._getSelfKeyPath(
                                       None)

        xmlVal = Value()
        xmlVal.setXmlTag(("logger-class", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug"))
        keyPath.addKeyPathPostfix(xmlVal)

        keys = []

        res = self.domain.readMaapiKeys(keyPath, keys, trxContext)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-list-keys-domain-failed').errorFunc(): logFunc('domain.readMaapiKeys() failed')
            return ReturnCodes.kGeneralError

        for key in keys:
            self.loggerClassKeys.append(key.getCannonicalStr())
            self.loggerClasss[key.getCannonicalStr()] = None

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

        for key in self.loggerClasss.keys():
            if self.loggerClasss[key]:
                res = self.loggerClasss[key]._collectItemsToDelete(
                                                                     key,
                                                                     itemsToDelete)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('collect-items-to-delete-loggerClass-failed').errorFunc(): logFunc('loggerClassObj._collectItemsToDelete() failed. key=%s. PARAMS', key)
                    return ReturnCodes.kGeneralError

            else:
                keyPath = self._getSelfKeyPath(
                                               None)
                xmlVal = Value()
                xmlVal.setXmlTag(("logger-class", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug"))
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

        for key in self.loggerClasss.keys():
            if self.loggerClasss[key]:
                valBegin = Value()
                (tag, ns, prefix) = ("logger-class", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug")
                valBegin.setXmlBegin((tag, ns, prefix))
                tagValueList.push((tag, ns), valBegin)

                valKey = Value()
                valKey.setString(key)
                tagValueList.push(("name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valKey)

                tagValueListLen = tagValueList.getLen()

                res = self.loggerClasss[key]._fillWriteTagValues(tagValueList)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('fill-write-tag-values-loggerClass-failed').errorFunc(): logFunc('loggerClass._fillWriteTagValues() failed. key=%s', key)
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

        for key in self.loggerClasss.keys():
            if self.loggerClasss[key]:
                valBegin = Value()
                (tag, ns, prefix) = ("logger-class", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug")
                valBegin.setXmlBegin((tag, ns, prefix))
                tagValueList.push((tag, ns), valBegin)

                valKey = Value()
                valKey.setString(key)
                tagValueList.push(("name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valKey)

                tagValueListLen = tagValueList.getLen()

                res = self.loggerClasss[key]._fillReadTagValues(tagValueList)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('fill-read-tag-values-loggerClass-failed').errorFunc(): logFunc('loggerClass._fillReadTagValues() failed. key=%s', key)
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

        for key in self.loggerClasss.keys():
            if self.loggerClasss[key]:
                ((tag, ns), valBegin) = tagValueList.popFront()
                if (tag != "logger-class") or \
                    (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug") or \
                    (valBegin.getType() != Value.kXmlBegin):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                            "logger-class", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", Value.kXmlBegin,
                                                                            tag, ns, valBegin.getType())
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                ((tag, ns), valKey) = tagValueList.popFront()
                if (tag != "name") or \
                    (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-key').errorFunc(): logFunc('got unexpected tag-value for key. expected: (%s, %s), got: (%s, %s)',
                                                                          "name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                key = valKey.asString()
                if res != ReturnCodes.kOk:
                    if readAllOrFail:
                        self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                res = self.loggerClasss[key]._readTagValues(tagValueList, readAllOrFail)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('read-tag-values-loggerClass-failed').errorFunc(): logFunc('loggerClass._readTagValues() failed. key=%s', key)
                    if readAllOrFail:
                        self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                ((tag, ns), valEnd) = tagValueList.popFront()
                if (tag != "logger-class") or \
                    (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug") or \
                    (valEnd.getType() != Value.kXmlEnd):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                          "logger-class", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", Value.kXmlEnd,
                                                                            tag, ns, valEnd.getType())
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. tagValueList=%s, readAllOrFail=%s', tagValueList, readAllOrFail)
        return ReturnCodes.kOk

"""
Extracted from the below data: 
{
    "node": {
        "containerClassName": "BlinkyLoggerClassMaapi", 
        "name": "loggerClass", 
        "keyLeaf": {
            "varName": "loggerClass", 
            "yangName": "name", 
            "typeHandler": "handler: StringHandler"
        }, 
        "yangName": "logger-class", 
        "namespace": "logger_class", 
        "moduleYangNamespacePrefix": "qt-debug", 
        "className": "LoggerClassMaapiList", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.logger_class_maapi_list_gen import LoggerClassMaapiList", 
        "baseClassName": "LoggerClassMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
        "containerModule": "logger_class_maapi_gen", 
        "baseModule": "logger_class_maapi_list_base_gen"
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
            "moduleYangNamespacePrefix": "qt-debug", 
            "isCurrent": true, 
            "yangName": "logger-class", 
            "namespace": "logger_class", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "keyLeaf": {
                "varName": "loggerClass", 
                "yangName": "name", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "logger-class"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-debug", 
            "memberName": "instanceList", 
            "yangName": "instance", 
            "className": "BlinkyInstanceMaapiList", 
            "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.instance_maapi_list_list_gen import BlinkyInstanceMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
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
            "debug", 
            "qwilt_tech_debug"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
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


