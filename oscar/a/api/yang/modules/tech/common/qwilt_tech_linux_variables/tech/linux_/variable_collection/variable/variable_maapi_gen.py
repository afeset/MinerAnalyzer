


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

from variable_maapi_base_gen import VariableMaapiBase

from a.api.yang.modules.tech.common.qwilt_tech_linux_variables.tech.linux_.variable_collection.variable.status.status_maapi_gen import BlinkyStatusMaapi
from a.api.yang.modules.tech.common.qwilt_tech_linux_variables.tech.linux_.variable_collection.variable.system_defaults.system_defaults_maapi_gen import BlinkySystemDefaultsMaapi

from a.api.yang.modules.tech.common.qwilt_tech_linux_variables.qwilt_tech_linux_variables_module_gen import InitPhase


class BlinkyVariableMaapi(VariableMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-variable")
        self.domain = None

        
        self.statusObj = None
        
        self.systemDefaultsObj = None
        

        
        self.nameRequested = False
        self.name = None
        self.nameSet = False
        
        self.descriptionRequested = False
        self.description = None
        self.descriptionSet = False
        
        self.systemProtectedRequested = False
        self.systemProtected = None
        self.systemProtectedSet = False
        
        self.valueRequested = False
        self.value = None
        self.valueSet = False
        
        self.initPhaseRequested = False
        self.initPhase = None
        self.initPhaseSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestName(True)
        
        self.requestDescription(True)
        
        self.requestSystemProtected(True)
        
        self.requestValue(True)
        
        self.requestInitPhase(True)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.requestConfigAndOper()
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestName(True)
        
        self.requestDescription(True)
        
        self.requestSystemProtected(True)
        
        self.requestValue(True)
        
        self.requestInitPhase(True)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.requestConfig()
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestName(False)
        
        self.requestDescription(False)
        
        self.requestSystemProtected(False)
        
        self.requestValue(False)
        
        self.requestInitPhase(False)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.requestOper()
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestName(False)
        
        self.requestDescription(False)
        
        self.requestSystemProtected(False)
        
        self.requestValue(False)
        
        self.requestInitPhase(False)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.clearAllRequested()
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setName(None)
        self.nameSet = False
        
        self.setDescription(None)
        self.descriptionSet = False
        
        self.setSystemProtected(None)
        self.systemProtectedSet = False
        
        self.setValue(None)
        self.valueSet = False
        
        self.setInitPhase(None)
        self.initPhaseSet = False
        
        
        if self.statusObj:
            self.statusObj.clearAllSet()
        
        if self.systemDefaultsObj:
            self.systemDefaultsObj.clearAllSet()
        

    def write (self
              , linux_
              , variableCollection
              , variable
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(linux_, variableCollection, variable, trxContext)

    def read (self
              , linux_
              , variableCollection
              , variable
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(linux_, variableCollection, variable, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , linux_
                       , variableCollection
                       , variable
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(linux_, variableCollection, variable, 
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

    def newSystemDefaults (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-systemdefaults').debug3Func(): logFunc('called.')
        systemDefaults = BlinkySystemDefaultsMaapi(self._log)
        systemDefaults.init(self.domain)
        return systemDefaults

    def setSystemDefaultsObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-systemdefaults').debug3Func(): logFunc('called. obj=%s', obj)
        self.systemDefaultsObj = obj

    def getSystemDefaultsObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-systemdefaults').debug3Func(): logFunc('called. self.systemDefaultsObj=%s', self.systemDefaultsObj)
        return self.systemDefaultsObj

    def hasSystemDefaults (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-systemdefaults').debug3Func(): logFunc('called. self.systemDefaultsObj=%s', self.systemDefaultsObj)
        if self.systemDefaultsObj:
            return True
        return False



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

    def requestSystemProtected (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-systemprotected').debug3Func(): logFunc('called. requested=%s', requested)
        self.systemProtectedRequested = requested
        self.systemProtectedSet = False

    def isSystemProtectedRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-systemprotected-requested').debug3Func(): logFunc('called. requested=%s', self.systemProtectedRequested)
        return self.systemProtectedRequested

    def getSystemProtected (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-systemprotected').debug3Func(): logFunc('called. self.systemProtectedSet=%s, self.systemProtected=%s', self.systemProtectedSet, self.systemProtected)
        if self.systemProtectedSet:
            return self.systemProtected
        return None

    def hasSystemProtected (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-systemprotected').debug3Func(): logFunc('called. self.systemProtectedSet=%s, self.systemProtected=%s', self.systemProtectedSet, self.systemProtected)
        if self.systemProtectedSet:
            return True
        return False

    def setSystemProtected (self, systemProtected):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-systemprotected').debug3Func(): logFunc('called. systemProtected=%s, old=%s', systemProtected, self.systemProtected)
        self.systemProtectedSet = True
        self.systemProtected = systemProtected

    def requestValue (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-value').debug3Func(): logFunc('called. requested=%s', requested)
        self.valueRequested = requested
        self.valueSet = False

    def isValueRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-value-requested').debug3Func(): logFunc('called. requested=%s', self.valueRequested)
        return self.valueRequested

    def getValue (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-value').debug3Func(): logFunc('called. self.valueSet=%s, self.value=%s', self.valueSet, self.value)
        if self.valueSet:
            return self.value
        return None

    def hasValue (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-value').debug3Func(): logFunc('called. self.valueSet=%s, self.value=%s', self.valueSet, self.value)
        if self.valueSet:
            return True
        return False

    def setValue (self, value):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-value').debug3Func(): logFunc('called. value=%s, old=%s', value, self.value)
        self.valueSet = True
        self.value = value

    def requestInitPhase (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-initphase').debug3Func(): logFunc('called. requested=%s', requested)
        self.initPhaseRequested = requested
        self.initPhaseSet = False

    def isInitPhaseRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-initphase-requested').debug3Func(): logFunc('called. requested=%s', self.initPhaseRequested)
        return self.initPhaseRequested

    def getInitPhase (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-initphase').debug3Func(): logFunc('called. self.initPhaseSet=%s, self.initPhase=%s', self.initPhaseSet, self.initPhase)
        if self.initPhaseSet:
            return self.initPhase
        return None

    def hasInitPhase (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-initphase').debug3Func(): logFunc('called. self.initPhaseSet=%s, self.initPhase=%s', self.initPhaseSet, self.initPhase)
        if self.initPhaseSet:
            return True
        return False

    def setInitPhase (self, initPhase):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-initphase').debug3Func(): logFunc('called. initPhase=%s, old=%s', initPhase, self.initPhase)
        self.initPhaseSet = True
        self.initPhase = initPhase


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.statusObj:
            self.statusObj._clearAllReadData()
        
        if self.systemDefaultsObj:
            self.systemDefaultsObj._clearAllReadData()
        

        
        self.name = 0
        self.nameSet = False
        
        self.description = 0
        self.descriptionSet = False
        
        self.systemProtected = 0
        self.systemProtectedSet = False
        
        self.value = 0
        self.valueSet = False
        
        self.initPhase = 0
        self.initPhaseSet = False
        

    def _getSelfKeyPath (self, linux_
                         , variableCollection
                         , variable
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        ancestorVal = Value()
        ancestorVal.setString(variable);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("variable", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", "qt-lnx-variables"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(variableCollection);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("variable-collection", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", "qt-lnx-variables"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(linux_);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("linux", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux", "qt-lnx"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        linux_, 
                        variableCollection, 
                        variable, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(linux_, 
                                         variableCollection, 
                                         variable, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(linux_, 
                                       variableCollection, 
                                       variable, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       linux_, 
                       variableCollection, 
                       variable, 
                       
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

        keyPath = self._getSelfKeyPath(linux_, 
                                       variableCollection, 
                                       variable, 
                                       
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
                               linux_, 
                               variableCollection, 
                               variable, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        
        if self.statusObj:
            res = self.statusObj._collectItemsToDelete(linux_, 
                                                                          variableCollection, 
                                                                          variable, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-status-failed').errorFunc(): logFunc('statusObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.systemDefaultsObj:
            res = self.systemDefaultsObj._collectItemsToDelete(linux_, 
                                                                          variableCollection, 
                                                                          variable, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasName():
            valName = Value()
            if self.name is not None:
                valName.setString(self.name)
            else:
                valName.setEmpty()
            tagValueList.push(("name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"), valName)
        
        if self.hasDescription():
            valDescription = Value()
            if self.description is not None:
                valDescription.setString(self.description)
            else:
                valDescription.setEmpty()
            tagValueList.push(("description", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"), valDescription)
        
        if self.hasSystemProtected():
            valSystemProtected = Value()
            if self.systemProtected is not None:
                valSystemProtected.setBool(self.systemProtected)
            else:
                valSystemProtected.setEmpty()
            tagValueList.push(("system-protected", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"), valSystemProtected)
        
        if self.hasValue():
            valValue = Value()
            if self.value is not None:
                valValue.setString(self.value)
            else:
                valValue.setEmpty()
            tagValueList.push(("value", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"), valValue)
        
        if self.hasInitPhase():
            valInitPhase = Value()
            if self.initPhase is not None:
                valInitPhase.setEnum(self.initPhase.getValue())
            else:
                valInitPhase.setEmpty()
            tagValueList.push(("init-phase", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"), valInitPhase)
        

        
        if self.statusObj:
            valBegin = Value()
            (tag, ns, prefix) = ("status" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", "qt-lnx-variables")
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
        
        if self.systemDefaultsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("system-defaults" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", "qt-lnx-variables")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.systemDefaultsObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._fillWriteTagValues() failed. PARAMS')
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

        
        if self.isNameRequested():
            valName = Value()
            valName.setEmpty()
            tagValueList.push(("name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"), valName)
        
        if self.isDescriptionRequested():
            valDescription = Value()
            valDescription.setEmpty()
            tagValueList.push(("description", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"), valDescription)
        
        if self.isSystemProtectedRequested():
            valSystemProtected = Value()
            valSystemProtected.setEmpty()
            tagValueList.push(("system-protected", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"), valSystemProtected)
        
        if self.isValueRequested():
            valValue = Value()
            valValue.setEmpty()
            tagValueList.push(("value", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"), valValue)
        
        if self.isInitPhaseRequested():
            valInitPhase = Value()
            valInitPhase.setEmpty()
            tagValueList.push(("init-phase", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"), valInitPhase)
        

        
        if self.statusObj:
            valBegin = Value()
            (tag, ns, prefix) = ("status" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", "qt-lnx-variables")
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
        
        if self.systemDefaultsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("system-defaults" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", "qt-lnx-variables")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.systemDefaultsObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._fillReadTagValues() failed. PARAMS')
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
        
        if self.isNameRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "name") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-name').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "name", "name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", tag, ns)
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
        
        if self.isDescriptionRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "description") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-description').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "description", "description", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", tag, ns)
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
        
        if self.isSystemProtectedRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "system-protected") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-systemprotected').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "systemProtected", "system-protected", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-system-protected-bad-value').infoFunc(): logFunc('systemProtected not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setSystemProtected(tempVar)
            for logFunc in self._log('read-tag-values-system-protected').debug3Func(): logFunc('read systemProtected. systemProtected=%s, tempValue=%s', self.systemProtected, tempValue.getType())
        
        if self.isValueRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "value") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-value').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "value", "value", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-value-bad-value').infoFunc(): logFunc('value not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setValue(tempVar)
            for logFunc in self._log('read-tag-values-value').debug3Func(): logFunc('read value. value=%s, tempValue=%s', self.value, tempValue.getType())
        
        if self.isInitPhaseRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "init-phase") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-initphase').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "initPhase", "init-phase", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-init-phase-bad-value').infoFunc(): logFunc('initPhase not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setInitPhase(tempVar)
            for logFunc in self._log('read-tag-values-init-phase').debug3Func(): logFunc('read initPhase. initPhase=%s, tempValue=%s', self.initPhase, tempValue.getType())
        

        
        if self.statusObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "status") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", Value.kXmlBegin,
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
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.systemDefaultsObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "system-defaults") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.systemDefaultsObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "system-defaults") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "variable", 
        "namespace": "variable", 
        "className": "VariableMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_linux_variables.tech.linux_.variable_collection.variable.variable_maapi_gen import VariableMaapi", 
        "baseClassName": "VariableMaapiBase", 
        "baseModule": "variable_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-lnx", 
            "isCurrent": false, 
            "yangName": "linux", 
            "namespace": "linux_", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux", 
            "keyLeaf": {
                "varName": "linux_", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "linux_"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "isCurrent": false, 
            "yangName": "variable-collection", 
            "namespace": "variable_collection", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "keyLeaf": {
                "varName": "variableCollection", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "variable-collection"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "isCurrent": true, 
            "yangName": "variable", 
            "namespace": "variable", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "keyLeaf": {
                "varName": "variable", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "variable"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "memberName": "status", 
            "yangName": "status", 
            "className": "BlinkyStatusMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_linux_variables.tech.linux_.variable_collection.variable.status.status_maapi_gen import BlinkyStatusMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "memberName": "systemDefaults", 
            "yangName": "system-defaults", 
            "className": "BlinkySystemDefaultsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_linux_variables.tech.linux_.variable_collection.variable.system_defaults.system_defaults_maapi_gen import BlinkySystemDefaultsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "systemProtected", 
            "yangName": "system-protected", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "value", 
            "yangName": "value", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "initPhase", 
            "yangName": "init-phase", 
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
            "qwilt_tech_linux_variables"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "systemProtected", 
            "yangName": "system-protected", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "value", 
            "yangName": "value", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "initPhase", 
            "yangName": "init-phase", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }
    ], 
    "createTime": "2013"
}
"""


