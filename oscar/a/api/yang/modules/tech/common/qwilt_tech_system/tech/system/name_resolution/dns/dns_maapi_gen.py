


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

from dns_maapi_base_gen import DnsMaapiBase

from a.api.yang.modules.tech.common.qwilt_tech_system.tech.system.name_resolution.dns.name_servers.name_servers_maapi_gen import BlinkyNameServersMaapi
from a.api.yang.modules.tech.common.qwilt_tech_system.tech.system.name_resolution.dns.search.search_maapi_list_gen import BlinkySearchMaapiList



class BlinkyDnsMaapi(DnsMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-dns")
        self.domain = None

        
        self.nameServersObj = None
        
        self.searchListObj = None
        

        
        self.enabledRequested = False
        self.enabled = None
        self.enabledSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestEnabled(True)
        
        
        
        if not self.nameServersObj:
            self.nameServersObj = self.newNameServers()
            self.nameServersObj.requestConfigAndOper()
        
        if not self.searchListObj:
            self.searchListObj = self.newSearchList()
            self.searchListObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestEnabled(True)
        
        
        
        if not self.nameServersObj:
            self.nameServersObj = self.newNameServers()
            self.nameServersObj.requestConfig()
        
        if not self.searchListObj:
            self.searchListObj = self.newSearchList()
            self.searchListObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestEnabled(False)
        
        
        
        if not self.nameServersObj:
            self.nameServersObj = self.newNameServers()
            self.nameServersObj.requestOper()
        
        if not self.searchListObj:
            self.searchListObj = self.newSearchList()
            self.searchListObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestEnabled(False)
        
        
        
        if not self.nameServersObj:
            self.nameServersObj = self.newNameServers()
            self.nameServersObj.clearAllRequested()
        
        if not self.searchListObj:
            self.searchListObj = self.newSearchList()
            self.searchListObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setEnabled(None)
        self.enabledSet = False
        
        
        if self.nameServersObj:
            self.nameServersObj.clearAllSet()
        
        if self.searchListObj:
            self.searchListObj.clearAllSet()
        

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

    def newNameServers (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-nameservers').debug3Func(): logFunc('called.')
        nameServers = BlinkyNameServersMaapi(self._log)
        nameServers.init(self.domain)
        return nameServers

    def setNameServersObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-nameservers').debug3Func(): logFunc('called. obj=%s', obj)
        self.nameServersObj = obj

    def getNameServersObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-nameservers').debug3Func(): logFunc('called. self.nameServersObj=%s', self.nameServersObj)
        return self.nameServersObj

    def hasNameServers (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-nameservers').debug3Func(): logFunc('called. self.nameServersObj=%s', self.nameServersObj)
        if self.nameServersObj:
            return True
        return False

    def newSearchList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-searchlist').debug3Func(): logFunc('called.')
        searchList = BlinkySearchMaapiList(self._log)
        searchList.init(self.domain)
        return searchList

    def setSearchListObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-searchlist').debug3Func(): logFunc('called. obj=%s', obj)
        self.searchListObj = obj

    def getSearchListObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-searchlist').debug3Func(): logFunc('called. self.searchListObj=%s', self.searchListObj)
        return self.searchListObj

    def hasSearchList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-searchlist').debug3Func(): logFunc('called. self.searchListObj=%s', self.searchListObj)
        if self.searchListObj:
            return True
        return False



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


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.nameServersObj:
            self.nameServersObj._clearAllReadData()
        
        if self.searchListObj:
            self.searchListObj._clearAllReadData()
        

        
        self.enabled = 0
        self.enabledSet = False
        

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("dns", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", "qt-sys"))
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

        
        if self.nameServersObj:
            res = self.nameServersObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-name-servers-failed').errorFunc(): logFunc('nameServersObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.searchListObj:
            res = self.searchListObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-search-failed').errorFunc(): logFunc('searchListObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasEnabled():
            valEnabled = Value()
            if self.enabled is not None:
                valEnabled.setBool(self.enabled)
            else:
                valEnabled.setEmpty()
            tagValueList.push(("enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system"), valEnabled)
        

        
        if self.nameServersObj:
            valBegin = Value()
            (tag, ns, prefix) = ("name-servers" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", "qt-sys")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.nameServersObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-name-servers-failed').errorFunc(): logFunc('nameServersObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.searchListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("search" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", "qt-sys")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.searchListObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-search-failed').errorFunc(): logFunc('searchListObj._fillWriteTagValues() failed. PARAMS')
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

        
        if self.isEnabledRequested():
            valEnabled = Value()
            valEnabled.setEmpty()
            tagValueList.push(("enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system"), valEnabled)
        

        
        if self.nameServersObj:
            valBegin = Value()
            (tag, ns, prefix) = ("name-servers" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", "qt-sys")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.nameServersObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-name-servers-failed').errorFunc(): logFunc('nameServersObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.searchListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("search" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", "qt-sys")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.searchListObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-search-failed').errorFunc(): logFunc('searchListObj._fillReadTagValues() failed. PARAMS')
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
        
        if self.isEnabledRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "enabled") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-enabled').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "enabled", "enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", tag, ns)
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
        

        
        if self.nameServersObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "name-servers") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "name-servers", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.nameServersObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-name-servers-failed').errorFunc(): logFunc('nameServersObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "name-servers") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "name-servers", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.searchListObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "search") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "search", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.searchListObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-search-failed').errorFunc(): logFunc('searchListObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "search") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "search", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "dns", 
        "namespace": "dns", 
        "className": "DnsMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system.tech.system.name_resolution.dns.dns_maapi_gen import DnsMaapi", 
        "baseClassName": "DnsMaapiBase", 
        "baseModule": "dns_maapi_base_gen"
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
            "yangName": "dns", 
            "namespace": "dns", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", 
            "name": "dns"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-sys", 
            "memberName": "nameServers", 
            "yangName": "name-servers", 
            "className": "BlinkyNameServersMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system.tech.system.name_resolution.dns.name_servers.name_servers_maapi_gen import BlinkyNameServersMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys", 
            "memberName": "searchList", 
            "yangName": "search", 
            "className": "BlinkySearchMaapiList", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system.tech.system.name_resolution.dns.search.search_maapi_list_gen import BlinkySearchMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", 
            "moduleYangNamespacePrefix": "qt-sys", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
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
            "common", 
            "qwilt_tech_system"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", 
            "moduleYangNamespacePrefix": "qt-sys", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }
    ], 
    "createTime": "2013"
}
"""


