


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

from host_maapi_list_base_gen import HostMaapiListBase
from host_maapi_gen import BlinkyHostMaapi

class BlinkyHostMaapiList(HostMaapiListBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-host")
        self.domain = None

        self.hosts = {}
        self.hostKeys = []

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def newHost (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-host').debug3Func(): logFunc('called.')
        host = BlinkyHostMaapi(self._log)
        host.init(self.domain)
        return host

    def setHostObj (self, key, hostObj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-host-obj').debug3Func(): logFunc('called. key=%s, hostObj=%s', key, hostObj)
        if key not in self.hosts:
            self.hostKeys.append(key)
        self.hosts[str(key)] = hostObj

    def getHostObj (self, key):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-host-obj').debug3Func(): logFunc('called. key=%s', key)
        if str(key) in self.hosts.keys():
            for logFunc in self._log('get-host-obj-done').debug3Func(): logFunc('Done. found key=%s, obj=%s', key, self.hosts[str(key)])
            return self.hosts[str(key)]
        for logFunc in self._log('get-host-obj-missing').errorFunc(): logFunc('host %s not in hosts. existing items: %s', key, self.hosts.keys())
        return None

    def deleteHost (self, key):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('delete-host').debug3Func(): logFunc('called. key=%s', key)
        if str(key) not in self.hostKeys:
            for logFunc in self._log('delete-host-not-found').warningFunc(): logFunc('key=%s is missing from the hostKeys list', key)
            if str(key) in self.hosts.keys():
                # internal problem - list & dictionary are not synced
                for logFunc in self._log('delete-host-not-found-but-in-dict').errorFunc(): logFunc('hosts dictionary & hostKeys list are out-of-sync. key %s exists in dict but not in list', key)
            return ReturnCodes.kGeneralError
        if str(key) not in self.hosts.keys():
            # internal problem - list & dictionary are not synced
            for logFunc in self._log('delete-host-not-found-but-in-list').errorFunc(): logFunc('hosts dictionary & hostKeys list are out-of-sync. key %s exists in list but not in dict', key)
            return ReturnCodes.kGeneralError

        self.hostKeys.remove(str(key))
        del self.hosts[str(key)]

    def hasHostObj (self, key):
        self.myInitGuard.isInitOrCrash()
        has = False
        if str(key) in self.hosts.keys():
            if self.hosts[str(key)]:
                has = True
        for logFunc in self._log('has-host-done').debug3Func(): logFunc('done. key=%s exists=%s', key, has)
        return has

    def getListKeys (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-list-keys').debug3Func(): logFunc('called. keys=%s', [str(x) for x in self.hostKeys])
        return self.hostKeys

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called.')
        for host in self.hosts.values():
            host.requestConfigAndOper()

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called.')
        for host in self.hosts.values():
            host.requestConfig()

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called.')
        for host in self.hosts.values():
            host.requestOper()

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called.')
        for host in self.hosts.values():
            host.clearAllRequested()

    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')
        for host in self.hosts.values():
            if host:
                host._clearAllReadData()

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        for key in self.hosts.keys():
            if self.hosts[key]:
                self.hosts[key].clearAllSet()
            else:
                self.hostKeys.remove(str(key))
                del self.hosts[str(key)]

    def _getSelfKeyPath (self, ipv4
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS. junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()

        
        
        
        
        ancestorVal = Value()
        ancestorVal.setString(ipv4);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("ipv4", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", "qt-sys"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("hosts", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", "qt-sys"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("static", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", "qt-sys"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("name-resolution", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", "qt-sys"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", "qt-sys"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def readListKeys (self
                      , ipv4
                      
                      , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-list-keys').debug3Func(): logFunc('called')

        # clear the old map
        self.hosts = {}
        self.hostKeys = []

        keyPath = self._getSelfKeyPath(ipv4, 
                                       
                                       None)

        xmlVal = Value()
        xmlVal.setXmlTag(("host", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", "qt-sys"))
        keyPath.addKeyPathPostfix(xmlVal)

        keys = []

        res = self.domain.readMaapiKeys(keyPath, keys, trxContext)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-list-keys-domain-failed').errorFunc(): logFunc('domain.readMaapiKeys() failed')
            return ReturnCodes.kGeneralError

        for key in keys:
            self.hostKeys.append(key.getCannonicalStr())
            self.hosts[key.getCannonicalStr()] = None

        return ReturnCodes.kOk

    def write (self
               , ipv4
               , trxContext=None
               ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(ipv4, 
                                   trxContext)

    def read (self
              , ipv4
              
              , trxContext=None):
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(ipv4, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , ipv4
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(ipv4, 
                                  True,
                                  trxContext)

    def _internalWrite (self, 
                        ipv4, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called.')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('internal-write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(ipv4, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(ipv4, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       ipv4, 
                       
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

        keyPath = self._getSelfKeyPath(ipv4, 
                                       
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
                               ipv4, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        for key in self.hosts.keys():
            if self.hosts[key]:
                res = self.hosts[key]._collectItemsToDelete(ipv4, 
                                                                     
                                                                     key,
                                                                     itemsToDelete)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('collect-items-to-delete-host-failed').errorFunc(): logFunc('hostObj._collectItemsToDelete() failed. key=%s. PARAMS', key)
                    return ReturnCodes.kGeneralError

            else:
                keyPath = self._getSelfKeyPath(ipv4, 
                                               
                                               None)
                xmlVal = Value()
                xmlVal.setXmlTag(("host", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", "qt-sys"))
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

        for key in self.hosts.keys():
            if self.hosts[key]:
                valBegin = Value()
                (tag, ns, prefix) = ("host", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", "qt-sys")
                valBegin.setXmlBegin((tag, ns, prefix))
                tagValueList.push((tag, ns), valBegin)

                valKey = Value()
                valKey.setString(key)
                tagValueList.push(("hostname", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system"), valKey)

                tagValueListLen = tagValueList.getLen()

                res = self.hosts[key]._fillWriteTagValues(tagValueList)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('fill-write-tag-values-host-failed').errorFunc(): logFunc('host._fillWriteTagValues() failed. key=%s', key)
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

        for key in self.hosts.keys():
            if self.hosts[key]:
                valBegin = Value()
                (tag, ns, prefix) = ("host", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", "qt-sys")
                valBegin.setXmlBegin((tag, ns, prefix))
                tagValueList.push((tag, ns), valBegin)

                valKey = Value()
                valKey.setString(key)
                tagValueList.push(("hostname", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system"), valKey)

                tagValueListLen = tagValueList.getLen()

                res = self.hosts[key]._fillReadTagValues(tagValueList)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('fill-read-tag-values-host-failed').errorFunc(): logFunc('host._fillReadTagValues() failed. key=%s', key)
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

        for key in self.hosts.keys():
            if self.hosts[key]:
                ((tag, ns), valBegin) = tagValueList.popFront()
                if (tag != "host") or \
                    (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system") or \
                    (valBegin.getType() != Value.kXmlBegin):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                            "host", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", Value.kXmlBegin,
                                                                            tag, ns, valBegin.getType())
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                ((tag, ns), valKey) = tagValueList.popFront()
                if (tag != "hostname") or \
                    (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system"):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-key').errorFunc(): logFunc('got unexpected tag-value for key. expected: (%s, %s), got: (%s, %s)',
                                                                          "hostname", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", tag, ns)
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                key = valKey.asString()
                if res != ReturnCodes.kOk:
                    if readAllOrFail:
                        self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                res = self.hosts[key]._readTagValues(tagValueList, readAllOrFail)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('read-tag-values-host-failed').errorFunc(): logFunc('host._readTagValues() failed. key=%s', key)
                    if readAllOrFail:
                        self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                ((tag, ns), valEnd) = tagValueList.popFront()
                if (tag != "host") or \
                    (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system") or \
                    (valEnd.getType() != Value.kXmlEnd):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                          "host", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", Value.kXmlEnd,
                                                                            tag, ns, valEnd.getType())
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. tagValueList=%s, readAllOrFail=%s', tagValueList, readAllOrFail)
        return ReturnCodes.kOk

"""
Extracted from the below data: 
{
    "node": {
        "containerClassName": "BlinkyHostMaapi", 
        "name": "host", 
        "keyLeaf": {
            "varName": "host", 
            "yangName": "hostname", 
            "typeHandler": "handler: BuiltinStringHandler"
        }, 
        "yangName": "host", 
        "namespace": "host", 
        "moduleYangNamespacePrefix": "qt-sys", 
        "className": "HostMaapiList", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system.tech.system.name_resolution.static_resolution.hosts.ipv4.host.host_maapi_list_gen import HostMaapiList", 
        "baseClassName": "HostMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", 
        "containerModule": "host_maapi_gen", 
        "baseModule": "host_maapi_list_base_gen"
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
            "moduleYangNamespacePrefix": "qt-sys", 
            "yangName": "name-resolution", 
            "namespace": "name_resolution", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", 
            "name": "name-resolution"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys", 
            "yangName": "static", 
            "namespace": "static_resolution", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", 
            "name": "static-resolution"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys", 
            "yangName": "hosts", 
            "namespace": "hosts", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", 
            "name": "hosts"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys", 
            "isCurrent": false, 
            "yangName": "ipv4", 
            "namespace": "ipv4", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", 
            "keyLeaf": {
                "varName": "ipv4", 
                "yangName": "address", 
                "typeHandler": "handler: Ipv4AddressHandlerPy"
            }, 
            "name": "ipv4"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys", 
            "isCurrent": true, 
            "yangName": "host", 
            "namespace": "host", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", 
            "keyLeaf": {
                "varName": "host", 
                "yangName": "hostname", 
                "typeHandler": "handler: BuiltinStringHandler"
            }, 
            "name": "host"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", 
            "moduleYangNamespacePrefix": "qt-sys", 
            "typeHandler": "handler: BuiltinStringHandler", 
            "memberName": "hostname", 
            "yangName": "hostname", 
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
            "common", 
            "qwilt_tech_system"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", 
            "moduleYangNamespacePrefix": "qt-sys", 
            "typeHandler": "handler: BuiltinStringHandler", 
            "memberName": "hostname", 
            "yangName": "hostname", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


