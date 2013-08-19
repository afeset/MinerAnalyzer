


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

from dispatcher_maapi_base_gen import DispatcherMaapiBase

from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.system_defaults.dispatcher.house_keeper.house_keeper_maapi_gen import BlinkyHouseKeeperMaapi
from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.system_defaults.dispatcher.dpdk.dpdk_maapi_gen import BlinkyDpdkMaapi



class BlinkyDispatcherMaapi(DispatcherMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-dispatcher")
        self.domain = None

        
        self.houseKeeperObj = None
        
        self.dpdkObj = None
        

        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        
        if not self.houseKeeperObj:
            self.houseKeeperObj = self.newHouseKeeper()
            self.houseKeeperObj.requestConfigAndOper()
        
        if not self.dpdkObj:
            self.dpdkObj = self.newDpdk()
            self.dpdkObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        
        if not self.houseKeeperObj:
            self.houseKeeperObj = self.newHouseKeeper()
            self.houseKeeperObj.requestConfig()
        
        if not self.dpdkObj:
            self.dpdkObj = self.newDpdk()
            self.dpdkObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        
        if not self.houseKeeperObj:
            self.houseKeeperObj = self.newHouseKeeper()
            self.houseKeeperObj.requestOper()
        
        if not self.dpdkObj:
            self.dpdkObj = self.newDpdk()
            self.dpdkObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        
        if not self.houseKeeperObj:
            self.houseKeeperObj = self.newHouseKeeper()
            self.houseKeeperObj.clearAllRequested()
        
        if not self.dpdkObj:
            self.dpdkObj = self.newDpdk()
            self.dpdkObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        
        if self.houseKeeperObj:
            self.houseKeeperObj.clearAllSet()
        
        if self.dpdkObj:
            self.dpdkObj.clearAllSet()
        

    def write (self
              , line
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(line, trxContext)

    def read (self
              , line
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(line, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , line
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(line, 
                                  True,
                                  trxContext)

    def newHouseKeeper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-housekeeper').debug3Func(): logFunc('called.')
        houseKeeper = BlinkyHouseKeeperMaapi(self._log)
        houseKeeper.init(self.domain)
        return houseKeeper

    def setHouseKeeperObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-housekeeper').debug3Func(): logFunc('called. obj=%s', obj)
        self.houseKeeperObj = obj

    def getHouseKeeperObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-housekeeper').debug3Func(): logFunc('called. self.houseKeeperObj=%s', self.houseKeeperObj)
        return self.houseKeeperObj

    def hasHouseKeeper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-housekeeper').debug3Func(): logFunc('called. self.houseKeeperObj=%s', self.houseKeeperObj)
        if self.houseKeeperObj:
            return True
        return False

    def newDpdk (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-dpdk').debug3Func(): logFunc('called.')
        dpdk = BlinkyDpdkMaapi(self._log)
        dpdk.init(self.domain)
        return dpdk

    def setDpdkObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-dpdk').debug3Func(): logFunc('called. obj=%s', obj)
        self.dpdkObj = obj

    def getDpdkObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-dpdk').debug3Func(): logFunc('called. self.dpdkObj=%s', self.dpdkObj)
        return self.dpdkObj

    def hasDpdk (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-dpdk').debug3Func(): logFunc('called. self.dpdkObj=%s', self.dpdkObj)
        if self.dpdkObj:
            return True
        return False




    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.houseKeeperObj:
            self.houseKeeperObj._clearAllReadData()
        
        if self.dpdkObj:
            self.dpdkObj._clearAllReadData()
        

        

    def _getSelfKeyPath (self, line
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("dispatcher", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line"))
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

    def _internalWrite (self, 
                        line, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(line, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(line, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       line, 
                       
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

        keyPath = self._getSelfKeyPath(line, 
                                       
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
                               line, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        
        if self.houseKeeperObj:
            res = self.houseKeeperObj._collectItemsToDelete(line, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-house-keeper-failed').errorFunc(): logFunc('houseKeeperObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.dpdkObj:
            res = self.dpdkObj._collectItemsToDelete(line, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-dpdk-failed').errorFunc(): logFunc('dpdkObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        

        
        if self.houseKeeperObj:
            valBegin = Value()
            (tag, ns, prefix) = ("house-keeper" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.houseKeeperObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-house-keeper-failed').errorFunc(): logFunc('houseKeeperObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.dpdkObj:
            valBegin = Value()
            (tag, ns, prefix) = ("dpdk" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.dpdkObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-dpdk-failed').errorFunc(): logFunc('dpdkObj._fillWriteTagValues() failed. PARAMS')
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

        

        
        if self.houseKeeperObj:
            valBegin = Value()
            (tag, ns, prefix) = ("house-keeper" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.houseKeeperObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-house-keeper-failed').errorFunc(): logFunc('houseKeeperObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.dpdkObj:
            valBegin = Value()
            (tag, ns, prefix) = ("dpdk" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.dpdkObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-dpdk-failed').errorFunc(): logFunc('dpdkObj._fillReadTagValues() failed. PARAMS')
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
        

        
        if self.houseKeeperObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "house-keeper") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "house-keeper", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.houseKeeperObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-house-keeper-failed').errorFunc(): logFunc('houseKeeperObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "house-keeper") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "house-keeper", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.dpdkObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "dpdk") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "dpdk", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.dpdkObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-dpdk-failed').errorFunc(): logFunc('dpdkObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "dpdk") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "dpdk", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "dispatcher", 
        "namespace": "dispatcher", 
        "className": "DispatcherMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.system_defaults.dispatcher.dispatcher_maapi_gen import DispatcherMaapi", 
        "baseClassName": "DispatcherMaapiBase", 
        "baseModule": "dispatcher_maapi_base_gen"
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
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "line"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "system-defaults"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "yangName": "dispatcher", 
            "namespace": "dispatcher", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "dispatcher"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "memberName": "houseKeeper", 
            "yangName": "house-keeper", 
            "className": "BlinkyHouseKeeperMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.system_defaults.dispatcher.house_keeper.house_keeper_maapi_gen import BlinkyHouseKeeperMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "memberName": "dpdk", 
            "yangName": "dpdk", 
            "className": "BlinkyDpdkMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.system_defaults.dispatcher.dpdk.dpdk_maapi_gen import BlinkyDpdkMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [], 
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
    "leaves": [], 
    "createTime": "2013"
}
"""


