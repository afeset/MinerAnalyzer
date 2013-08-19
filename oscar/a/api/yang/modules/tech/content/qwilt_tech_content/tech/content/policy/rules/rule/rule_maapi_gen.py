


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

from rule_maapi_base_gen import RuleMaapiBase

from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.policy.rules.rule.destination_zone.destination_zone_maapi_list_gen import BlinkyDestinationZoneMaapiList
from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.policy.rules.rule.site.site_maapi_list_gen import BlinkySiteMaapiList
from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.policy.rules.rule.actions.actions_maapi_gen import BlinkyActionsMaapi
from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.policy.rules.rule.source_zone.source_zone_maapi_list_gen import BlinkySourceZoneMaapiList

from a.api.yang.modules.tech.content.qwilt_tech_content.qwilt_tech_content_module_gen import SiteListType


class BlinkyRuleMaapi(RuleMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-rule")
        self.domain = None

        
        self.destinationZoneListObj = None
        
        self.siteListObj = None
        
        self.actionsObj = None
        
        self.sourceZoneListObj = None
        

        
        self.descriptionRequested = False
        self.description = None
        self.descriptionSet = False
        
        self.enabledRequested = False
        self.enabled = None
        self.enabledSet = False
        
        self.siteListRequested = False
        self.siteList = None
        self.siteListSet = False
        
        self.nameRequested = False
        self.name = None
        self.nameSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestDescription(True)
        
        self.requestEnabled(True)
        
        self.requestSiteList(True)
        
        self.requestName(True)
        
        
        
        if not self.destinationZoneListObj:
            self.destinationZoneListObj = self.newDestinationZoneList()
            self.destinationZoneListObj.requestConfigAndOper()
        
        if not self.siteListObj:
            self.siteListObj = self.newSiteList()
            self.siteListObj.requestConfigAndOper()
        
        if not self.actionsObj:
            self.actionsObj = self.newActions()
            self.actionsObj.requestConfigAndOper()
        
        if not self.sourceZoneListObj:
            self.sourceZoneListObj = self.newSourceZoneList()
            self.sourceZoneListObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestDescription(True)
        
        self.requestEnabled(True)
        
        self.requestSiteList(True)
        
        self.requestName(True)
        
        
        
        if not self.destinationZoneListObj:
            self.destinationZoneListObj = self.newDestinationZoneList()
            self.destinationZoneListObj.requestConfig()
        
        if not self.siteListObj:
            self.siteListObj = self.newSiteList()
            self.siteListObj.requestConfig()
        
        if not self.actionsObj:
            self.actionsObj = self.newActions()
            self.actionsObj.requestConfig()
        
        if not self.sourceZoneListObj:
            self.sourceZoneListObj = self.newSourceZoneList()
            self.sourceZoneListObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestDescription(False)
        
        self.requestEnabled(False)
        
        self.requestSiteList(False)
        
        self.requestName(False)
        
        
        
        if not self.destinationZoneListObj:
            self.destinationZoneListObj = self.newDestinationZoneList()
            self.destinationZoneListObj.requestOper()
        
        if not self.siteListObj:
            self.siteListObj = self.newSiteList()
            self.siteListObj.requestOper()
        
        if not self.actionsObj:
            self.actionsObj = self.newActions()
            self.actionsObj.requestOper()
        
        if not self.sourceZoneListObj:
            self.sourceZoneListObj = self.newSourceZoneList()
            self.sourceZoneListObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestDescription(False)
        
        self.requestEnabled(False)
        
        self.requestSiteList(False)
        
        self.requestName(False)
        
        
        
        if not self.destinationZoneListObj:
            self.destinationZoneListObj = self.newDestinationZoneList()
            self.destinationZoneListObj.clearAllRequested()
        
        if not self.siteListObj:
            self.siteListObj = self.newSiteList()
            self.siteListObj.clearAllRequested()
        
        if not self.actionsObj:
            self.actionsObj = self.newActions()
            self.actionsObj.clearAllRequested()
        
        if not self.sourceZoneListObj:
            self.sourceZoneListObj = self.newSourceZoneList()
            self.sourceZoneListObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setDescription(None)
        self.descriptionSet = False
        
        self.setEnabled(None)
        self.enabledSet = False
        
        self.setSiteList(None)
        self.siteListSet = False
        
        self.setName(None)
        self.nameSet = False
        
        
        if self.destinationZoneListObj:
            self.destinationZoneListObj.clearAllSet()
        
        if self.siteListObj:
            self.siteListObj.clearAllSet()
        
        if self.actionsObj:
            self.actionsObj.clearAllSet()
        
        if self.sourceZoneListObj:
            self.sourceZoneListObj.clearAllSet()
        

    def write (self
              , rule
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(rule, trxContext)

    def read (self
              , rule
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
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

    def newDestinationZoneList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-destinationzonelist').debug3Func(): logFunc('called.')
        destinationZoneList = BlinkyDestinationZoneMaapiList(self._log)
        destinationZoneList.init(self.domain)
        return destinationZoneList

    def setDestinationZoneListObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-destinationzonelist').debug3Func(): logFunc('called. obj=%s', obj)
        self.destinationZoneListObj = obj

    def getDestinationZoneListObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-destinationzonelist').debug3Func(): logFunc('called. self.destinationZoneListObj=%s', self.destinationZoneListObj)
        return self.destinationZoneListObj

    def hasDestinationZoneList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-destinationzonelist').debug3Func(): logFunc('called. self.destinationZoneListObj=%s', self.destinationZoneListObj)
        if self.destinationZoneListObj:
            return True
        return False

    def newSiteList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-sitelist').debug3Func(): logFunc('called.')
        siteList = BlinkySiteMaapiList(self._log)
        siteList.init(self.domain)
        return siteList

    def setSiteListObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-sitelist').debug3Func(): logFunc('called. obj=%s', obj)
        self.siteListObj = obj

    def getSiteListObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-sitelist').debug3Func(): logFunc('called. self.siteListObj=%s', self.siteListObj)
        return self.siteListObj

    def hasSiteList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-sitelist').debug3Func(): logFunc('called. self.siteListObj=%s', self.siteListObj)
        if self.siteListObj:
            return True
        return False

    def newActions (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-actions').debug3Func(): logFunc('called.')
        actions = BlinkyActionsMaapi(self._log)
        actions.init(self.domain)
        return actions

    def setActionsObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-actions').debug3Func(): logFunc('called. obj=%s', obj)
        self.actionsObj = obj

    def getActionsObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-actions').debug3Func(): logFunc('called. self.actionsObj=%s', self.actionsObj)
        return self.actionsObj

    def hasActions (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-actions').debug3Func(): logFunc('called. self.actionsObj=%s', self.actionsObj)
        if self.actionsObj:
            return True
        return False

    def newSourceZoneList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-sourcezonelist').debug3Func(): logFunc('called.')
        sourceZoneList = BlinkySourceZoneMaapiList(self._log)
        sourceZoneList.init(self.domain)
        return sourceZoneList

    def setSourceZoneListObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-sourcezonelist').debug3Func(): logFunc('called. obj=%s', obj)
        self.sourceZoneListObj = obj

    def getSourceZoneListObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-sourcezonelist').debug3Func(): logFunc('called. self.sourceZoneListObj=%s', self.sourceZoneListObj)
        return self.sourceZoneListObj

    def hasSourceZoneList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-sourcezonelist').debug3Func(): logFunc('called. self.sourceZoneListObj=%s', self.sourceZoneListObj)
        if self.sourceZoneListObj:
            return True
        return False



    def requestDescription (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-description').debug3Func(): logFunc('called. requested=%s', requested)
        self.descriptionRequested = requested
        self.descriptionSet = False

    def isDescriptionRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-description-requested').debug3Func(): logFunc('called. requested=%s', self.descriptionRequested)
        return self.descriptionRequested

    def getDescription (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-description').debug3Func(): logFunc('called. self.descriptionSet=%s, self.description=%s', self.descriptionSet, self.description)
        if self.descriptionSet:
            return self.description
        return None

    def hasDescription (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-description').debug3Func(): logFunc('called. self.descriptionSet=%s, self.description=%s', self.descriptionSet, self.description)
        if self.descriptionSet:
            return True
        return False

    def setDescription (self, description):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-description').debug3Func(): logFunc('called. description=%s, old=%s', description, self.description)
        self.descriptionSet = True
        self.description = description

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

    def requestSiteList (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-sitelist').debug3Func(): logFunc('called. requested=%s', requested)
        self.siteListRequested = requested
        self.siteListSet = False

    def isSiteListRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-sitelist-requested').debug3Func(): logFunc('called. requested=%s', self.siteListRequested)
        return self.siteListRequested

    def getSiteList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-sitelist').debug3Func(): logFunc('called. self.siteListSet=%s, self.siteList=%s', self.siteListSet, self.siteList)
        if self.siteListSet:
            return self.siteList
        return None

    def hasSiteList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-sitelist').debug3Func(): logFunc('called. self.siteListSet=%s, self.siteList=%s', self.siteListSet, self.siteList)
        if self.siteListSet:
            return True
        return False

    def setSiteList (self, siteList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-sitelist').debug3Func(): logFunc('called. siteList=%s, old=%s', siteList, self.siteList)
        self.siteListSet = True
        self.siteList = siteList

    def requestName (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-name').debug3Func(): logFunc('called. requested=%s', requested)
        self.nameRequested = requested
        self.nameSet = False

    def isNameRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-name-requested').debug3Func(): logFunc('called. requested=%s', self.nameRequested)
        return self.nameRequested

    def getName (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-name').debug3Func(): logFunc('called. self.nameSet=%s, self.name=%s', self.nameSet, self.name)
        if self.nameSet:
            return self.name
        return None

    def hasName (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-name').debug3Func(): logFunc('called. self.nameSet=%s, self.name=%s', self.nameSet, self.name)
        if self.nameSet:
            return True
        return False

    def setName (self, name):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-name').debug3Func(): logFunc('called. name=%s, old=%s', name, self.name)
        self.nameSet = True
        self.name = name


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.destinationZoneListObj:
            self.destinationZoneListObj._clearAllReadData()
        
        if self.siteListObj:
            self.siteListObj._clearAllReadData()
        
        if self.actionsObj:
            self.actionsObj._clearAllReadData()
        
        if self.sourceZoneListObj:
            self.sourceZoneListObj._clearAllReadData()
        

        
        self.description = 0
        self.descriptionSet = False
        
        self.enabled = 0
        self.enabledSet = False
        
        self.siteList = 0
        self.siteListSet = False
        
        self.name = 0
        self.nameSet = False
        

    def _getSelfKeyPath (self, rule
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
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

    def _internalWrite (self, 
                        rule, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
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
        for logFunc in self._log('internal-read').debug3Func(): logFunc('called. PARAMS, readAllOrFail=%s', readAllOrFail)

        if readAllOrFail:
            self._clearAllReadData()

        tagValueList = TagValues()

        res = self._fillReadTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-fill-read-tag-value-failed').errorFunc(): logFunc('_fillReadTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(rule, 
                                       
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
                               rule, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        
        if self.destinationZoneListObj:
            res = self.destinationZoneListObj._collectItemsToDelete(rule, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-destination-zone-failed').errorFunc(): logFunc('destinationZoneListObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.siteListObj:
            res = self.siteListObj._collectItemsToDelete(rule, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-site-failed').errorFunc(): logFunc('siteListObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.actionsObj:
            res = self.actionsObj._collectItemsToDelete(rule, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-actions-failed').errorFunc(): logFunc('actionsObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.sourceZoneListObj:
            res = self.sourceZoneListObj._collectItemsToDelete(rule, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-source-zone-failed').errorFunc(): logFunc('sourceZoneListObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasDescription():
            valDescription = Value()
            if self.description is not None:
                valDescription.setString(self.description)
            else:
                valDescription.setEmpty()
            tagValueList.push(("description", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"), valDescription)
        
        if self.hasEnabled():
            valEnabled = Value()
            if self.enabled is not None:
                valEnabled.setBool(self.enabled)
            else:
                valEnabled.setEmpty()
            tagValueList.push(("enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"), valEnabled)
        
        if self.hasSiteList():
            valSiteList = Value()
            if self.siteList is not None:
                valSiteList.setEnum(self.siteList.getValue())
            else:
                valSiteList.setEmpty()
            tagValueList.push(("site-list", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"), valSiteList)
        
        if self.hasName():
            valName = Value()
            if self.name is not None:
                valName.setString(self.name)
            else:
                valName.setEmpty()
            tagValueList.push(("name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"), valName)
        

        
        if self.destinationZoneListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("destination-zone" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.destinationZoneListObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-destination-zone-failed').errorFunc(): logFunc('destinationZoneListObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.siteListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("site" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.siteListObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-site-failed').errorFunc(): logFunc('siteListObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.actionsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("actions" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.actionsObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-actions-failed').errorFunc(): logFunc('actionsObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.sourceZoneListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("source-zone" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.sourceZoneListObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-source-zone-failed').errorFunc(): logFunc('sourceZoneListObj._fillWriteTagValues() failed. PARAMS')
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

        
        if self.isDescriptionRequested():
            valDescription = Value()
            valDescription.setEmpty()
            tagValueList.push(("description", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"), valDescription)
        
        if self.isEnabledRequested():
            valEnabled = Value()
            valEnabled.setEmpty()
            tagValueList.push(("enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"), valEnabled)
        
        if self.isSiteListRequested():
            valSiteList = Value()
            valSiteList.setEmpty()
            tagValueList.push(("site-list", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"), valSiteList)
        
        if self.isNameRequested():
            valName = Value()
            valName.setEmpty()
            tagValueList.push(("name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"), valName)
        

        
        if self.destinationZoneListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("destination-zone" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.destinationZoneListObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-destination-zone-failed').errorFunc(): logFunc('destinationZoneListObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.siteListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("site" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.siteListObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-site-failed').errorFunc(): logFunc('siteListObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.actionsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("actions" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.actionsObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-actions-failed').errorFunc(): logFunc('actionsObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.sourceZoneListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("source-zone" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.sourceZoneListObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-source-zone-failed').errorFunc(): logFunc('sourceZoneListObj._fillReadTagValues() failed. PARAMS')
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
        
        if self.isDescriptionRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "description") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-description').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "description", "description", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-description-bad-value').infoFunc(): logFunc('description not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setDescription(tempVar)
            for logFunc in self._log('read-tag-values-description').debug3Func(): logFunc('read description. description=%s, tempValue=%s', self.description, tempValue.getType())
        
        if self.isEnabledRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "enabled") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-enabled').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "enabled", "enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", tag, ns)
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
        
        if self.isSiteListRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "site-list") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-sitelist').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "siteList", "site-list", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-site-list-bad-value').infoFunc(): logFunc('siteList not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setSiteList(tempVar)
            for logFunc in self._log('read-tag-values-site-list').debug3Func(): logFunc('read siteList. siteList=%s, tempValue=%s', self.siteList, tempValue.getType())
        
        if self.isNameRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "name") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-name').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "name", "name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-name-bad-value').infoFunc(): logFunc('name not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setName(tempVar)
            for logFunc in self._log('read-tag-values-name').debug3Func(): logFunc('read name. name=%s, tempValue=%s', self.name, tempValue.getType())
        

        
        if self.destinationZoneListObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "destination-zone") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "destination-zone", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.destinationZoneListObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-destination-zone-failed').errorFunc(): logFunc('destinationZoneListObj._readTagValues() failed. tagValueList=%s', tagValueList)
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
        
        if self.siteListObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "site") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "site", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.siteListObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-site-failed').errorFunc(): logFunc('siteListObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "site") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "site", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.actionsObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "actions") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "actions", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.actionsObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-actions-failed').errorFunc(): logFunc('actionsObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "actions") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "actions", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.sourceZoneListObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "source-zone") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "source-zone", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.sourceZoneListObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-source-zone-failed').errorFunc(): logFunc('sourceZoneListObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "source-zone") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "source-zone", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "rule", 
        "namespace": "rule", 
        "className": "RuleMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.policy.rules.rule.rule_maapi_gen import RuleMaapi", 
        "baseClassName": "RuleMaapiBase", 
        "baseModule": "rule_maapi_base_gen"
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
            "isCurrent": true, 
            "yangName": "rule", 
            "namespace": "rule", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "keyLeaf": {
                "varName": "rule", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "rule"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qtc", 
            "memberName": "destinationZoneList", 
            "yangName": "destination-zone", 
            "className": "BlinkyDestinationZoneMaapiList", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.policy.rules.rule.destination_zone.destination_zone_maapi_list_gen import BlinkyDestinationZoneMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "memberName": "siteList", 
            "yangName": "site", 
            "className": "BlinkySiteMaapiList", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.policy.rules.rule.site.site_maapi_list_gen import BlinkySiteMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "memberName": "actions", 
            "yangName": "actions", 
            "className": "BlinkyActionsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.policy.rules.rule.actions.actions_maapi_gen import BlinkyActionsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "memberName": "sourceZoneList", 
            "yangName": "source-zone", 
            "className": "BlinkySourceZoneMaapiList", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.policy.rules.rule.source_zone.source_zone_maapi_list_gen import BlinkySourceZoneMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "siteList", 
            "yangName": "site-list", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "include", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
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
            "qwilt_tech_content"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "siteList", 
            "yangName": "site-list", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "include", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
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


