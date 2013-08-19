


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

from community_maapi_base_gen import CommunityMaapiBase


from a.api.yang.modules.common.qwilt_types.qwilt_types_module_gen import Accessmodetype


class BlinkyCommunityMaapi(CommunityMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-community")
        self.domain = None

        

        
        self.entryNameRequested = False
        self.entryName = None
        self.entryNameSet = False
        
        self.accessModeRequested = False
        self.accessMode = None
        self.accessModeSet = False
        
        self.communityRequested = False
        self.community = None
        self.communitySet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestEntryName(True)
        
        self.requestAccessMode(True)
        
        self.requestCommunity(True)
        
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestEntryName(True)
        
        self.requestAccessMode(True)
        
        self.requestCommunity(True)
        
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestEntryName(False)
        
        self.requestAccessMode(False)
        
        self.requestCommunity(False)
        
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestEntryName(False)
        
        self.requestAccessMode(False)
        
        self.requestCommunity(False)
        
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setEntryName(None)
        self.entryNameSet = False
        
        self.setAccessMode(None)
        self.accessModeSet = False
        
        self.setCommunity(None)
        self.communitySet = False
        
        

    def write (self
              , community
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(community, trxContext)

    def read (self
              , community
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(community, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , community
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(community, 
                                  True,
                                  trxContext)



    def requestEntryName (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-entryname').debug3Func(): logFunc('called. requested=%s', requested)
        self.entryNameRequested = requested
        self.entryNameSet = False

    def isEntryNameRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-entryname-requested').debug3Func(): logFunc('called. requested=%s', self.entryNameRequested)
        return self.entryNameRequested

    def getEntryName (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-entryname').debug3Func(): logFunc('called. self.entryNameSet=%s, self.entryName=%s', self.entryNameSet, self.entryName)
        if self.entryNameSet:
            return self.entryName
        return None

    def hasEntryName (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-entryname').debug3Func(): logFunc('called. self.entryNameSet=%s, self.entryName=%s', self.entryNameSet, self.entryName)
        if self.entryNameSet:
            return True
        return False

    def setEntryName (self, entryName):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-entryname').debug3Func(): logFunc('called. entryName=%s, old=%s', entryName, self.entryName)
        self.entryNameSet = True
        self.entryName = entryName

    def requestAccessMode (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-accessmode').debug3Func(): logFunc('called. requested=%s', requested)
        self.accessModeRequested = requested
        self.accessModeSet = False

    def isAccessModeRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-accessmode-requested').debug3Func(): logFunc('called. requested=%s', self.accessModeRequested)
        return self.accessModeRequested

    def getAccessMode (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-accessmode').debug3Func(): logFunc('called. self.accessModeSet=%s, self.accessMode=%s', self.accessModeSet, self.accessMode)
        if self.accessModeSet:
            return self.accessMode
        return None

    def hasAccessMode (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-accessmode').debug3Func(): logFunc('called. self.accessModeSet=%s, self.accessMode=%s', self.accessModeSet, self.accessMode)
        if self.accessModeSet:
            return True
        return False

    def setAccessMode (self, accessMode):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-accessmode').debug3Func(): logFunc('called. accessMode=%s, old=%s', accessMode, self.accessMode)
        self.accessModeSet = True
        self.accessMode = accessMode

    def requestCommunity (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-community').debug3Func(): logFunc('called. requested=%s', requested)
        self.communityRequested = requested
        self.communitySet = False

    def isCommunityRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-community-requested').debug3Func(): logFunc('called. requested=%s', self.communityRequested)
        return self.communityRequested

    def getCommunity (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-community').debug3Func(): logFunc('called. self.communitySet=%s, self.community=%s', self.communitySet, self.community)
        if self.communitySet:
            return self.community
        return None

    def hasCommunity (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-community').debug3Func(): logFunc('called. self.communitySet=%s, self.community=%s', self.communitySet, self.community)
        if self.communitySet:
            return True
        return False

    def setCommunity (self, community):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-community').debug3Func(): logFunc('called. community=%s, old=%s', community, self.community)
        self.communitySet = True
        self.community = community


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.entryName = 0
        self.entryNameSet = False
        
        self.accessMode = 0
        self.accessModeSet = False
        
        self.community = 0
        self.communitySet = False
        

    def _getSelfKeyPath (self, community
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        ancestorVal = Value()
        ancestorVal.setString(community);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("community", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", "qt-snmp"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("snmp", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", "qt-snmp"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        community, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(community, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(community, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       community, 
                       
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

        keyPath = self._getSelfKeyPath(community, 
                                       
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
                               community, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasEntryName():
            valEntryName = Value()
            if self.entryName is not None:
                valEntryName.setString(self.entryName)
            else:
                valEntryName.setEmpty()
            tagValueList.push(("entry-name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"), valEntryName)
        
        if self.hasAccessMode():
            valAccessMode = Value()
            if self.accessMode is not None:
                valAccessMode.setEnum(self.accessMode.getValue())
            else:
                valAccessMode.setEmpty()
            tagValueList.push(("access-mode", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"), valAccessMode)
        
        if self.hasCommunity():
            valCommunity = Value()
            if self.community is not None:
                valCommunity.setString(self.community)
            else:
                valCommunity.setEmpty()
            tagValueList.push(("community", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"), valCommunity)
        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isEntryNameRequested():
            valEntryName = Value()
            valEntryName.setEmpty()
            tagValueList.push(("entry-name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"), valEntryName)
        
        if self.isAccessModeRequested():
            valAccessMode = Value()
            valAccessMode.setEmpty()
            tagValueList.push(("access-mode", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"), valAccessMode)
        
        if self.isCommunityRequested():
            valCommunity = Value()
            valCommunity.setEmpty()
            tagValueList.push(("community", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"), valCommunity)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isEntryNameRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "entry-name") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-entryname').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "entryName", "entry-name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-entry-name-bad-value').infoFunc(): logFunc('entryName not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setEntryName(tempVar)
            for logFunc in self._log('read-tag-values-entry-name').debug3Func(): logFunc('read entryName. entryName=%s, tempValue=%s', self.entryName, tempValue.getType())
        
        if self.isAccessModeRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "access-mode") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-accessmode').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "accessMode", "access-mode", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-access-mode-bad-value').infoFunc(): logFunc('accessMode not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setAccessMode(tempVar)
            for logFunc in self._log('read-tag-values-access-mode').debug3Func(): logFunc('read accessMode. accessMode=%s, tempValue=%s', self.accessMode, tempValue.getType())
        
        if self.isCommunityRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "community") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-community').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "community", "community", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-community-bad-value').infoFunc(): logFunc('community not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setCommunity(tempVar)
            for logFunc in self._log('read-tag-values-community').debug3Func(): logFunc('read community. community=%s, tempValue=%s', self.community, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "community", 
        "namespace": "community", 
        "className": "CommunityMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_snmp.tech.snmp.community.community_maapi_gen import CommunityMaapi", 
        "baseClassName": "CommunityMaapiBase", 
        "baseModule": "community_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-snmp", 
            "yangName": "snmp", 
            "namespace": "snmp", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "name": "snmp"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-snmp", 
            "isCurrent": true, 
            "yangName": "community", 
            "namespace": "community", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "keyLeaf": {
                "varName": "community", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "community"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "entryName", 
            "yangName": "entry-name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "accessMode", 
            "yangName": "access-mode", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "community", 
            "yangName": "community", 
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
            "qwilt_tech_snmp"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "entryName", 
            "yangName": "entry-name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "accessMode", 
            "yangName": "access-mode", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "community", 
            "yangName": "community", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


