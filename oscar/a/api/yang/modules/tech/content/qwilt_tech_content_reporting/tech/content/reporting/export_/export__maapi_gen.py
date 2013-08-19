


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

from export__maapi_base_gen import ExportMaapiBase

from a.api.yang.modules.tech.content.qwilt_tech_content_reporting.tech.content.reporting.export_.status.status_maapi_gen import BlinkyStatusMaapi
from a.api.yang.modules.tech.content.qwilt_tech_content_reporting.tech.content.reporting.export_.alarm.alarm_maapi_gen import BlinkyAlarmMaapi

from a.api.yang.modules.tech.content.qwilt_tech_content_reporting.qwilt_tech_content_reporting_module_gen import ReportingExportTypesType


class BlinkyExportMaapi(ExportMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-export_")
        self.domain = None

        
        self.statusObj = None
        
        self.alarmObj = None
        

        
        self.descriptionRequested = False
        self.description = None
        self.descriptionSet = False
        
        self.enabledRequested = False
        self.enabled = None
        self.enabledSet = False
        
        self.analyticsRequested = False
        self.analytics = None
        self.analyticsSet = False
        
        self.urlTranslationRequested = False
        self.urlTranslation = None
        self.urlTranslationSet = False
        
        self.type_Requested = False
        self.type_ = None
        self.type_Set = False
        
        self.idRequested = False
        self.id = None
        self.idSet = False
        
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
        
        self.requestAnalytics(True)
        
        self.requestUrlTranslation(True)
        
        self.requestType_(True)
        
        self.requestId(True)
        
        self.requestName(True)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.requestConfigAndOper()
        
        if not self.alarmObj:
            self.alarmObj = self.newAlarm()
            self.alarmObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestDescription(True)
        
        self.requestEnabled(True)
        
        self.requestAnalytics(True)
        
        self.requestUrlTranslation(True)
        
        self.requestType_(True)
        
        self.requestId(True)
        
        self.requestName(True)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.requestConfig()
        
        if not self.alarmObj:
            self.alarmObj = self.newAlarm()
            self.alarmObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestDescription(False)
        
        self.requestEnabled(False)
        
        self.requestAnalytics(False)
        
        self.requestUrlTranslation(False)
        
        self.requestType_(False)
        
        self.requestId(False)
        
        self.requestName(False)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.requestOper()
        
        if not self.alarmObj:
            self.alarmObj = self.newAlarm()
            self.alarmObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestDescription(False)
        
        self.requestEnabled(False)
        
        self.requestAnalytics(False)
        
        self.requestUrlTranslation(False)
        
        self.requestType_(False)
        
        self.requestId(False)
        
        self.requestName(False)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.clearAllRequested()
        
        if not self.alarmObj:
            self.alarmObj = self.newAlarm()
            self.alarmObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setDescription(None)
        self.descriptionSet = False
        
        self.setEnabled(None)
        self.enabledSet = False
        
        self.setAnalytics(None)
        self.analyticsSet = False
        
        self.setUrlTranslation(None)
        self.urlTranslationSet = False
        
        self.setType_(None)
        self.type_Set = False
        
        self.setId(None)
        self.idSet = False
        
        self.setName(None)
        self.nameSet = False
        
        
        if self.statusObj:
            self.statusObj.clearAllSet()
        
        if self.alarmObj:
            self.alarmObj.clearAllSet()
        

    def write (self
              , export_
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(export_, trxContext)

    def read (self
              , export_
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(export_, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , export_
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(export_, 
                                  True,
                                  trxContext)

    def newStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-status').debug3Func(): logFunc('called.')
        status = BlinkyStatusMaapi(self._log)
        status.init(self.domain)
        return status

    def setStatusObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-status').debug3Func(): logFunc('called. obj=%s', obj)
        self.statusObj = obj

    def getStatusObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-status').debug3Func(): logFunc('called. self.statusObj=%s', self.statusObj)
        return self.statusObj

    def hasStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-status').debug3Func(): logFunc('called. self.statusObj=%s', self.statusObj)
        if self.statusObj:
            return True
        return False

    def newAlarm (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-alarm').debug3Func(): logFunc('called.')
        alarm = BlinkyAlarmMaapi(self._log)
        alarm.init(self.domain)
        return alarm

    def setAlarmObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-alarm').debug3Func(): logFunc('called. obj=%s', obj)
        self.alarmObj = obj

    def getAlarmObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-alarm').debug3Func(): logFunc('called. self.alarmObj=%s', self.alarmObj)
        return self.alarmObj

    def hasAlarm (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-alarm').debug3Func(): logFunc('called. self.alarmObj=%s', self.alarmObj)
        if self.alarmObj:
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

    def requestAnalytics (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-analytics').debug3Func(): logFunc('called. requested=%s', requested)
        self.analyticsRequested = requested
        self.analyticsSet = False

    def isAnalyticsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-analytics-requested').debug3Func(): logFunc('called. requested=%s', self.analyticsRequested)
        return self.analyticsRequested

    def getAnalytics (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-analytics').debug3Func(): logFunc('called. self.analyticsSet=%s, self.analytics=%s', self.analyticsSet, self.analytics)
        if self.analyticsSet:
            return self.analytics
        return None

    def hasAnalytics (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-analytics').debug3Func(): logFunc('called. self.analyticsSet=%s, self.analytics=%s', self.analyticsSet, self.analytics)
        if self.analyticsSet:
            return True
        return False

    def setAnalytics (self, analytics):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-analytics').debug3Func(): logFunc('called. analytics=%s, old=%s', analytics, self.analytics)
        self.analyticsSet = True
        self.analytics = analytics

    def requestUrlTranslation (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-urltranslation').debug3Func(): logFunc('called. requested=%s', requested)
        self.urlTranslationRequested = requested
        self.urlTranslationSet = False

    def isUrlTranslationRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-urltranslation-requested').debug3Func(): logFunc('called. requested=%s', self.urlTranslationRequested)
        return self.urlTranslationRequested

    def getUrlTranslation (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-urltranslation').debug3Func(): logFunc('called. self.urlTranslationSet=%s, self.urlTranslation=%s', self.urlTranslationSet, self.urlTranslation)
        if self.urlTranslationSet:
            return self.urlTranslation
        return None

    def hasUrlTranslation (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-urltranslation').debug3Func(): logFunc('called. self.urlTranslationSet=%s, self.urlTranslation=%s', self.urlTranslationSet, self.urlTranslation)
        if self.urlTranslationSet:
            return True
        return False

    def setUrlTranslation (self, urlTranslation):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-urltranslation').debug3Func(): logFunc('called. urlTranslation=%s, old=%s', urlTranslation, self.urlTranslation)
        self.urlTranslationSet = True
        self.urlTranslation = urlTranslation

    def requestType_ (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-type_').debug3Func(): logFunc('called. requested=%s', requested)
        self.type_Requested = requested
        self.type_Set = False

    def isType_Requested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-type_-requested').debug3Func(): logFunc('called. requested=%s', self.type_Requested)
        return self.type_Requested

    def getType_ (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-type_').debug3Func(): logFunc('called. self.type_Set=%s, self.type_=%s', self.type_Set, self.type_)
        if self.type_Set:
            return self.type_
        return None

    def hasType_ (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-type_').debug3Func(): logFunc('called. self.type_Set=%s, self.type_=%s', self.type_Set, self.type_)
        if self.type_Set:
            return True
        return False

    def setType_ (self, type_):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-type_').debug3Func(): logFunc('called. type_=%s, old=%s', type_, self.type_)
        self.type_Set = True
        self.type_ = type_

    def requestId (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-id').debug3Func(): logFunc('called. requested=%s', requested)
        self.idRequested = requested
        self.idSet = False

    def isIdRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-id-requested').debug3Func(): logFunc('called. requested=%s', self.idRequested)
        return self.idRequested

    def getId (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-id').debug3Func(): logFunc('called. self.idSet=%s, self.id=%s', self.idSet, self.id)
        if self.idSet:
            return self.id
        return None

    def hasId (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-id').debug3Func(): logFunc('called. self.idSet=%s, self.id=%s', self.idSet, self.id)
        if self.idSet:
            return True
        return False

    def setId (self, id):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-id').debug3Func(): logFunc('called. id=%s, old=%s', id, self.id)
        self.idSet = True
        self.id = id

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

        
        if self.statusObj:
            self.statusObj._clearAllReadData()
        
        if self.alarmObj:
            self.alarmObj._clearAllReadData()
        

        
        self.description = 0
        self.descriptionSet = False
        
        self.enabled = 0
        self.enabledSet = False
        
        self.analytics = 0
        self.analyticsSet = False
        
        self.urlTranslation = 0
        self.urlTranslationSet = False
        
        self.type_ = 0
        self.type_Set = False
        
        self.id = 0
        self.idSet = False
        
        self.name = 0
        self.nameSet = False
        

    def _getSelfKeyPath (self, export_
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        ancestorVal = Value()
        ancestorVal.setString(export_);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("export", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", "qtc-report"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("reporting", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", "qtc-report"))
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
                        export_, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(export_, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(export_, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       export_, 
                       
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

        keyPath = self._getSelfKeyPath(export_, 
                                       
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
                               export_, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        
        if self.statusObj:
            res = self.statusObj._collectItemsToDelete(export_, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-status-failed').errorFunc(): logFunc('statusObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.alarmObj:
            res = self.alarmObj._collectItemsToDelete(export_, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-alarm-failed').errorFunc(): logFunc('alarmObj._collectItemsToDelete() failed. PARAMS')
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
            tagValueList.push(("description", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting"), valDescription)
        
        if self.hasEnabled():
            valEnabled = Value()
            if self.enabled is not None:
                valEnabled.setBool(self.enabled)
            else:
                valEnabled.setEmpty()
            tagValueList.push(("enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting"), valEnabled)
        
        if self.hasAnalytics():
            valAnalytics = Value()
            if self.analytics is not None:
                valAnalytics.setBool(self.analytics)
            else:
                valAnalytics.setEmpty()
            tagValueList.push(("analytics", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting"), valAnalytics)
        
        if self.hasUrlTranslation():
            valUrlTranslation = Value()
            if self.urlTranslation is not None:
                valUrlTranslation.setBool(self.urlTranslation)
            else:
                valUrlTranslation.setEmpty()
            tagValueList.push(("url-translation", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting"), valUrlTranslation)
        
        if self.hasType_():
            valType_ = Value()
            if self.type_ is not None:
                valType_.setEnum(self.type_.getValue())
            else:
                valType_.setEmpty()
            tagValueList.push(("type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting"), valType_)
        
        if self.hasId():
            valId = Value()
            if self.id is not None:
                valId.setString(self.id)
            else:
                valId.setEmpty()
            tagValueList.push(("id", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting"), valId)
        
        if self.hasName():
            valName = Value()
            if self.name is not None:
                valName.setString(self.name)
            else:
                valName.setEmpty()
            tagValueList.push(("name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting"), valName)
        

        
        if self.statusObj:
            valBegin = Value()
            (tag, ns, prefix) = ("status" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", "qtc-report")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.statusObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-status-failed').errorFunc(): logFunc('statusObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.alarmObj:
            valBegin = Value()
            (tag, ns, prefix) = ("alarm" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", "qtc-report")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.alarmObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-alarm-failed').errorFunc(): logFunc('alarmObj._fillWriteTagValues() failed. PARAMS')
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
            tagValueList.push(("description", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting"), valDescription)
        
        if self.isEnabledRequested():
            valEnabled = Value()
            valEnabled.setEmpty()
            tagValueList.push(("enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting"), valEnabled)
        
        if self.isAnalyticsRequested():
            valAnalytics = Value()
            valAnalytics.setEmpty()
            tagValueList.push(("analytics", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting"), valAnalytics)
        
        if self.isUrlTranslationRequested():
            valUrlTranslation = Value()
            valUrlTranslation.setEmpty()
            tagValueList.push(("url-translation", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting"), valUrlTranslation)
        
        if self.isType_Requested():
            valType_ = Value()
            valType_.setEmpty()
            tagValueList.push(("type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting"), valType_)
        
        if self.isIdRequested():
            valId = Value()
            valId.setEmpty()
            tagValueList.push(("id", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting"), valId)
        
        if self.isNameRequested():
            valName = Value()
            valName.setEmpty()
            tagValueList.push(("name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting"), valName)
        

        
        if self.statusObj:
            valBegin = Value()
            (tag, ns, prefix) = ("status" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", "qtc-report")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.statusObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-status-failed').errorFunc(): logFunc('statusObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.alarmObj:
            valBegin = Value()
            (tag, ns, prefix) = ("alarm" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", "qtc-report")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.alarmObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-alarm-failed').errorFunc(): logFunc('alarmObj._fillReadTagValues() failed. PARAMS')
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
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-description').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "description", "description", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", tag, ns)
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
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-enabled').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "enabled", "enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", tag, ns)
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
        
        if self.isAnalyticsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "analytics") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-analytics').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "analytics", "analytics", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-analytics-bad-value').infoFunc(): logFunc('analytics not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setAnalytics(tempVar)
            for logFunc in self._log('read-tag-values-analytics').debug3Func(): logFunc('read analytics. analytics=%s, tempValue=%s', self.analytics, tempValue.getType())
        
        if self.isUrlTranslationRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "url-translation") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-urltranslation').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "urlTranslation", "url-translation", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-url-translation-bad-value').infoFunc(): logFunc('urlTranslation not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setUrlTranslation(tempVar)
            for logFunc in self._log('read-tag-values-url-translation').debug3Func(): logFunc('read urlTranslation. urlTranslation=%s, tempValue=%s', self.urlTranslation, tempValue.getType())
        
        if self.isType_Requested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "type") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-type_').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "type_", "type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-type-bad-value').infoFunc(): logFunc('type_ not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setType_(tempVar)
            for logFunc in self._log('read-tag-values-type').debug3Func(): logFunc('read type_. type_=%s, tempValue=%s', self.type_, tempValue.getType())
        
        if self.isIdRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "id") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-id').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "id", "id", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-id-bad-value').infoFunc(): logFunc('id not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setId(tempVar)
            for logFunc in self._log('read-tag-values-id').debug3Func(): logFunc('read id. id=%s, tempValue=%s', self.id, tempValue.getType())
        
        if self.isNameRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "name") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-name').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "name", "name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", tag, ns)
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
        

        
        if self.statusObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "status") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.statusObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-status-failed').errorFunc(): logFunc('statusObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "status") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.alarmObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "alarm") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "alarm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.alarmObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-alarm-failed').errorFunc(): logFunc('alarmObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "alarm") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "alarm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "export_", 
        "namespace": "export_", 
        "className": "ExportMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_reporting.tech.content.reporting.export_.export__maapi_gen import ExportMaapi", 
        "baseClassName": "ExportMaapiBase", 
        "baseModule": "export__maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qtc-report", 
            "yangName": "reporting", 
            "namespace": "reporting", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "name": "reporting"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-report", 
            "isCurrent": true, 
            "yangName": "export", 
            "namespace": "export_", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "keyLeaf": {
                "varName": "export_", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "export_"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qtc-report", 
            "memberName": "status", 
            "yangName": "status", 
            "className": "BlinkyStatusMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_reporting.tech.content.reporting.export_.status.status_maapi_gen import BlinkyStatusMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-report", 
            "memberName": "alarm", 
            "yangName": "alarm", 
            "className": "BlinkyAlarmMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_reporting.tech.content.reporting.export_.alarm.alarm_maapi_gen import BlinkyAlarmMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "moduleYangNamespacePrefix": "qtc-report", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "moduleYangNamespacePrefix": "qtc-report", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "moduleYangNamespacePrefix": "qtc-report", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "analytics", 
            "yangName": "analytics", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "moduleYangNamespacePrefix": "qtc-report", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "urlTranslation", 
            "yangName": "url-translation", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "moduleYangNamespacePrefix": "qtc-report", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "type_", 
            "yangName": "type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "none", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "moduleYangNamespacePrefix": "qtc-report", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "id", 
            "yangName": "id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "qwilt", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "moduleYangNamespacePrefix": "qtc-report", 
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
            "qwilt_tech_content_reporting"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "moduleYangNamespacePrefix": "qtc-report", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "moduleYangNamespacePrefix": "qtc-report", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "moduleYangNamespacePrefix": "qtc-report", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "analytics", 
            "yangName": "analytics", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "moduleYangNamespacePrefix": "qtc-report", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "urlTranslation", 
            "yangName": "url-translation", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "moduleYangNamespacePrefix": "qtc-report", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "type_", 
            "yangName": "type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "none", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "moduleYangNamespacePrefix": "qtc-report", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "id", 
            "yangName": "id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "qwilt", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "moduleYangNamespacePrefix": "qtc-report", 
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


