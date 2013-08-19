


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

from list_maapi_base_gen import ListMaapiBase


from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.qwilt_tech_system_alarms_module_gen import AlarmNameType
from a.api.yang.modules.tech.common.qwilt_tech_types.qwilt_tech_types_module_gen import SeverityType


class BlinkyListMaapi(ListMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-list")
        self.domain = None

        

        
        self.descriptionRequested = False
        self.description = None
        self.descriptionSet = False
        
        self.severityRequested = False
        self.severity = None
        self.severitySet = False
        
        self.numberRequested = False
        self.number = None
        self.numberSet = False
        
        self.entityRequested = False
        self.entity = None
        self.entitySet = False
        
        self.sourceRequested = False
        self.source = None
        self.sourceSet = False
        
        self.simulatedRequested = False
        self.simulated = None
        self.simulatedSet = False
        
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
        
        self.requestSeverity(True)
        
        self.requestNumber(True)
        
        self.requestEntity(True)
        
        self.requestSource(True)
        
        self.requestSimulated(True)
        
        self.requestName(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestDescription(False)
        
        self.requestSeverity(False)
        
        self.requestNumber(False)
        
        self.requestEntity(False)
        
        self.requestSource(False)
        
        self.requestSimulated(False)
        
        self.requestName(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestDescription(True)
        
        self.requestSeverity(True)
        
        self.requestNumber(True)
        
        self.requestEntity(True)
        
        self.requestSource(True)
        
        self.requestSimulated(True)
        
        self.requestName(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestDescription(False)
        
        self.requestSeverity(False)
        
        self.requestNumber(False)
        
        self.requestEntity(False)
        
        self.requestSource(False)
        
        self.requestSimulated(False)
        
        self.requestName(False)
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        

    def write (self
              , list
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(list, trxContext)

    def read (self
              , list
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(list, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , list
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(list, 
                                  True,
                                  trxContext)



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

    def requestSeverity (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-severity').debug3Func(): logFunc('called. requested=%s', requested)
        self.severityRequested = requested
        self.severitySet = False

    def isSeverityRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-severity-requested').debug3Func(): logFunc('called. requested=%s', self.severityRequested)
        return self.severityRequested

    def getSeverity (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-severity').debug3Func(): logFunc('called. self.severitySet=%s, self.severity=%s', self.severitySet, self.severity)
        if self.severitySet:
            return self.severity
        return None

    def hasSeverity (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-severity').debug3Func(): logFunc('called. self.severitySet=%s, self.severity=%s', self.severitySet, self.severity)
        if self.severitySet:
            return True
        return False

    def setSeverity (self, severity):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-severity').debug3Func(): logFunc('called. severity=%s, old=%s', severity, self.severity)
        self.severitySet = True
        self.severity = severity

    def requestNumber (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-number').debug3Func(): logFunc('called. requested=%s', requested)
        self.numberRequested = requested
        self.numberSet = False

    def isNumberRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-number-requested').debug3Func(): logFunc('called. requested=%s', self.numberRequested)
        return self.numberRequested

    def getNumber (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-number').debug3Func(): logFunc('called. self.numberSet=%s, self.number=%s', self.numberSet, self.number)
        if self.numberSet:
            return self.number
        return None

    def hasNumber (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-number').debug3Func(): logFunc('called. self.numberSet=%s, self.number=%s', self.numberSet, self.number)
        if self.numberSet:
            return True
        return False

    def setNumber (self, number):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-number').debug3Func(): logFunc('called. number=%s, old=%s', number, self.number)
        self.numberSet = True
        self.number = number

    def requestEntity (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-entity').debug3Func(): logFunc('called. requested=%s', requested)
        self.entityRequested = requested
        self.entitySet = False

    def isEntityRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-entity-requested').debug3Func(): logFunc('called. requested=%s', self.entityRequested)
        return self.entityRequested

    def getEntity (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-entity').debug3Func(): logFunc('called. self.entitySet=%s, self.entity=%s', self.entitySet, self.entity)
        if self.entitySet:
            return self.entity
        return None

    def hasEntity (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-entity').debug3Func(): logFunc('called. self.entitySet=%s, self.entity=%s', self.entitySet, self.entity)
        if self.entitySet:
            return True
        return False

    def setEntity (self, entity):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-entity').debug3Func(): logFunc('called. entity=%s, old=%s', entity, self.entity)
        self.entitySet = True
        self.entity = entity

    def requestSource (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-source').debug3Func(): logFunc('called. requested=%s', requested)
        self.sourceRequested = requested
        self.sourceSet = False

    def isSourceRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-source-requested').debug3Func(): logFunc('called. requested=%s', self.sourceRequested)
        return self.sourceRequested

    def getSource (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-source').debug3Func(): logFunc('called. self.sourceSet=%s, self.source=%s', self.sourceSet, self.source)
        if self.sourceSet:
            return self.source
        return None

    def hasSource (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-source').debug3Func(): logFunc('called. self.sourceSet=%s, self.source=%s', self.sourceSet, self.source)
        if self.sourceSet:
            return True
        return False

    def setSource (self, source):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-source').debug3Func(): logFunc('called. source=%s, old=%s', source, self.source)
        self.sourceSet = True
        self.source = source

    def requestSimulated (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-simulated').debug3Func(): logFunc('called. requested=%s', requested)
        self.simulatedRequested = requested
        self.simulatedSet = False

    def isSimulatedRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-simulated-requested').debug3Func(): logFunc('called. requested=%s', self.simulatedRequested)
        return self.simulatedRequested

    def getSimulated (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-simulated').debug3Func(): logFunc('called. self.simulatedSet=%s, self.simulated=%s', self.simulatedSet, self.simulated)
        if self.simulatedSet:
            return self.simulated
        return None

    def hasSimulated (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-simulated').debug3Func(): logFunc('called. self.simulatedSet=%s, self.simulated=%s', self.simulatedSet, self.simulated)
        if self.simulatedSet:
            return True
        return False

    def setSimulated (self, simulated):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-simulated').debug3Func(): logFunc('called. simulated=%s, old=%s', simulated, self.simulated)
        self.simulatedSet = True
        self.simulated = simulated

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

        

        
        self.description = 0
        self.descriptionSet = False
        
        self.severity = 0
        self.severitySet = False
        
        self.number = 0
        self.numberSet = False
        
        self.entity = 0
        self.entitySet = False
        
        self.source = 0
        self.sourceSet = False
        
        self.simulated = 0
        self.simulatedSet = False
        
        self.name = 0
        self.nameSet = False
        

    def _getSelfKeyPath (self, list
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        ancestorVal = Value()
        ancestorVal.setInt64(list);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("list", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "qt-sys-alarms"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("alarms", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "qt-sys-alarms"))
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
                        list, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(list, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(list, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       list, 
                       
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

        keyPath = self._getSelfKeyPath(list, 
                                       
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
                               list, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isDescriptionRequested():
            valDescription = Value()
            valDescription.setEmpty()
            tagValueList.push(("description", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valDescription)
        
        if self.isSeverityRequested():
            valSeverity = Value()
            valSeverity.setEmpty()
            tagValueList.push(("severity", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valSeverity)
        
        if self.isNumberRequested():
            valNumber = Value()
            valNumber.setEmpty()
            tagValueList.push(("number", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valNumber)
        
        if self.isEntityRequested():
            valEntity = Value()
            valEntity.setEmpty()
            tagValueList.push(("entity", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valEntity)
        
        if self.isSourceRequested():
            valSource = Value()
            valSource.setEmpty()
            tagValueList.push(("source", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valSource)
        
        if self.isSimulatedRequested():
            valSimulated = Value()
            valSimulated.setEmpty()
            tagValueList.push(("simulated", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valSimulated)
        
        if self.isNameRequested():
            valName = Value()
            valName.setEmpty()
            tagValueList.push(("name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valName)
        

        

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
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-description').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "description", "description", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", tag, ns)
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
        
        if self.isSeverityRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "severity") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-severity').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "severity", "severity", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-severity-bad-value').infoFunc(): logFunc('severity not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setSeverity(tempVar)
            for logFunc in self._log('read-tag-values-severity').debug3Func(): logFunc('read severity. severity=%s, tempValue=%s', self.severity, tempValue.getType())
        
        if self.isNumberRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "number") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-number').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "number", "number", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-number-bad-value').infoFunc(): logFunc('number not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setNumber(tempVar)
            for logFunc in self._log('read-tag-values-number').debug3Func(): logFunc('read number. number=%s, tempValue=%s', self.number, tempValue.getType())
        
        if self.isEntityRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "entity") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-entity').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "entity", "entity", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-entity-bad-value').infoFunc(): logFunc('entity not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setEntity(tempVar)
            for logFunc in self._log('read-tag-values-entity').debug3Func(): logFunc('read entity. entity=%s, tempValue=%s', self.entity, tempValue.getType())
        
        if self.isSourceRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "source") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-source').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "source", "source", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-source-bad-value').infoFunc(): logFunc('source not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setSource(tempVar)
            for logFunc in self._log('read-tag-values-source').debug3Func(): logFunc('read source. source=%s, tempValue=%s', self.source, tempValue.getType())
        
        if self.isSimulatedRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "simulated") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-simulated').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "simulated", "simulated", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-simulated-bad-value').infoFunc(): logFunc('simulated not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setSimulated(tempVar)
            for logFunc in self._log('read-tag-values-simulated').debug3Func(): logFunc('read simulated. simulated=%s, tempValue=%s', self.simulated, tempValue.getType())
        
        if self.isNameRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "name") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-name').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "name", "name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-name-bad-value').infoFunc(): logFunc('name not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setName(tempVar)
            for logFunc in self._log('read-tag-values-name').debug3Func(): logFunc('read name. name=%s, tempValue=%s', self.name, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "list", 
        "namespace": "list", 
        "className": "ListMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.list.list_maapi_gen import ListMaapi", 
        "baseClassName": "ListMaapiBase", 
        "baseModule": "list_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "yangName": "alarms", 
            "namespace": "alarms", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "name": "alarms"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "isCurrent": true, 
            "yangName": "list", 
            "namespace": "list", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "keyLeaf": {
                "varName": "list", 
                "defaultVal": null, 
                "typeHandler": "handler: IntHandler"
            }, 
            "name": "list"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "severity", 
            "yangName": "severity", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "number", 
            "yangName": "number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "entity", 
            "yangName": "entity", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "source", 
            "yangName": "source", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "simulated", 
            "yangName": "simulated", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "module": {}, 
    "configLeaves": [], 
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "common", 
            "qwilt_tech_system_alarms"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "severity", 
            "yangName": "severity", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "number", 
            "yangName": "number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "entity", 
            "yangName": "entity", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "source", 
            "yangName": "source", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "simulated", 
            "yangName": "simulated", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: EnumHandlerPy", 
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


