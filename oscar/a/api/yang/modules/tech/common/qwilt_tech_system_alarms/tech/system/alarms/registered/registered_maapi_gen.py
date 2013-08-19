


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

from registered_maapi_base_gen import RegisteredMaapiBase


from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.qwilt_tech_system_alarms_module_gen import AlarmDeclarationStateType
from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.qwilt_tech_system_alarms_module_gen import AlarmNameType
from a.api.yang.modules.tech.common.qwilt_tech_types.qwilt_tech_types_module_gen import SeverityType


class BlinkyRegisteredMaapi(RegisteredMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-registered")
        self.domain = None

        

        
        self.descriptionRequested = False
        self.description = None
        self.descriptionSet = False
        
        self.devCommentRequested = False
        self.devComment = None
        self.devCommentSet = False
        
        self.softwareVersionRequested = False
        self.softwareVersion = None
        self.softwareVersionSet = False
        
        self.nameRequested = False
        self.name = None
        self.nameSet = False
        
        self.sourceRequested = False
        self.source = None
        self.sourceSet = False
        
        self.stateRequested = False
        self.state = None
        self.stateSet = False
        
        self.severityRequested = False
        self.severity = None
        self.severitySet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestDescription(True)
        
        self.requestDevComment(True)
        
        self.requestSoftwareVersion(True)
        
        self.requestName(True)
        
        self.requestSource(True)
        
        self.requestState(True)
        
        self.requestSeverity(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestDescription(False)
        
        self.requestDevComment(False)
        
        self.requestSoftwareVersion(False)
        
        self.requestName(False)
        
        self.requestSource(False)
        
        self.requestState(False)
        
        self.requestSeverity(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestDescription(True)
        
        self.requestDevComment(True)
        
        self.requestSoftwareVersion(True)
        
        self.requestName(True)
        
        self.requestSource(True)
        
        self.requestState(True)
        
        self.requestSeverity(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestDescription(False)
        
        self.requestDevComment(False)
        
        self.requestSoftwareVersion(False)
        
        self.requestName(False)
        
        self.requestSource(False)
        
        self.requestState(False)
        
        self.requestSeverity(False)
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        

    def write (self
              , registered
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(registered, trxContext)

    def read (self
              , registered
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(registered, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , registered
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(registered, 
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

    def requestDevComment (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-devcomment').debug3Func(): logFunc('called. requested=%s', requested)
        self.devCommentRequested = requested
        self.devCommentSet = False

    def isDevCommentRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-devcomment-requested').debug3Func(): logFunc('called. requested=%s', self.devCommentRequested)
        return self.devCommentRequested

    def getDevComment (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-devcomment').debug3Func(): logFunc('called. self.devCommentSet=%s, self.devComment=%s', self.devCommentSet, self.devComment)
        if self.devCommentSet:
            return self.devComment
        return None

    def hasDevComment (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-devcomment').debug3Func(): logFunc('called. self.devCommentSet=%s, self.devComment=%s', self.devCommentSet, self.devComment)
        if self.devCommentSet:
            return True
        return False

    def setDevComment (self, devComment):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-devcomment').debug3Func(): logFunc('called. devComment=%s, old=%s', devComment, self.devComment)
        self.devCommentSet = True
        self.devComment = devComment

    def requestSoftwareVersion (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-softwareversion').debug3Func(): logFunc('called. requested=%s', requested)
        self.softwareVersionRequested = requested
        self.softwareVersionSet = False

    def isSoftwareVersionRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-softwareversion-requested').debug3Func(): logFunc('called. requested=%s', self.softwareVersionRequested)
        return self.softwareVersionRequested

    def getSoftwareVersion (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-softwareversion').debug3Func(): logFunc('called. self.softwareVersionSet=%s, self.softwareVersion=%s', self.softwareVersionSet, self.softwareVersion)
        if self.softwareVersionSet:
            return self.softwareVersion
        return None

    def hasSoftwareVersion (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-softwareversion').debug3Func(): logFunc('called. self.softwareVersionSet=%s, self.softwareVersion=%s', self.softwareVersionSet, self.softwareVersion)
        if self.softwareVersionSet:
            return True
        return False

    def setSoftwareVersion (self, softwareVersion):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-softwareversion').debug3Func(): logFunc('called. softwareVersion=%s, old=%s', softwareVersion, self.softwareVersion)
        self.softwareVersionSet = True
        self.softwareVersion = softwareVersion

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

    def requestState (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-state').debug3Func(): logFunc('called. requested=%s', requested)
        self.stateRequested = requested
        self.stateSet = False

    def isStateRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-state-requested').debug3Func(): logFunc('called. requested=%s', self.stateRequested)
        return self.stateRequested

    def getState (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-state').debug3Func(): logFunc('called. self.stateSet=%s, self.state=%s', self.stateSet, self.state)
        if self.stateSet:
            return self.state
        return None

    def hasState (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-state').debug3Func(): logFunc('called. self.stateSet=%s, self.state=%s', self.stateSet, self.state)
        if self.stateSet:
            return True
        return False

    def setState (self, state):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-state').debug3Func(): logFunc('called. state=%s, old=%s', state, self.state)
        self.stateSet = True
        self.state = state

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


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.description = 0
        self.descriptionSet = False
        
        self.devComment = 0
        self.devCommentSet = False
        
        self.softwareVersion = 0
        self.softwareVersionSet = False
        
        self.name = 0
        self.nameSet = False
        
        self.source = 0
        self.sourceSet = False
        
        self.state = 0
        self.stateSet = False
        
        self.severity = 0
        self.severitySet = False
        

    def _getSelfKeyPath (self, registered
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        ancestorVal = Value()
        ancestorVal.setEnum(registered.getValue());
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("registered", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "qt-sys-alarms"))
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
                        registered, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(registered, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(registered, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       registered, 
                       
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

        keyPath = self._getSelfKeyPath(registered, 
                                       
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
                               registered, 
                               
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
        
        if self.isDevCommentRequested():
            valDevComment = Value()
            valDevComment.setEmpty()
            tagValueList.push(("dev-comment", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valDevComment)
        
        if self.isSoftwareVersionRequested():
            valSoftwareVersion = Value()
            valSoftwareVersion.setEmpty()
            tagValueList.push(("software-version", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valSoftwareVersion)
        
        if self.isNameRequested():
            valName = Value()
            valName.setEmpty()
            tagValueList.push(("name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valName)
        
        if self.isSourceRequested():
            valSource = Value()
            valSource.setEmpty()
            tagValueList.push(("source", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valSource)
        
        if self.isStateRequested():
            valState = Value()
            valState.setEmpty()
            tagValueList.push(("state", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valState)
        
        if self.isSeverityRequested():
            valSeverity = Value()
            valSeverity.setEmpty()
            tagValueList.push(("severity", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valSeverity)
        

        

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
        
        if self.isDevCommentRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "dev-comment") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-devcomment').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "devComment", "dev-comment", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-dev-comment-bad-value').infoFunc(): logFunc('devComment not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setDevComment(tempVar)
            for logFunc in self._log('read-tag-values-dev-comment').debug3Func(): logFunc('read devComment. devComment=%s, tempValue=%s', self.devComment, tempValue.getType())
        
        if self.isSoftwareVersionRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "software-version") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-softwareversion').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "softwareVersion", "software-version", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-software-version-bad-value').infoFunc(): logFunc('softwareVersion not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setSoftwareVersion(tempVar)
            for logFunc in self._log('read-tag-values-software-version').debug3Func(): logFunc('read softwareVersion. softwareVersion=%s, tempValue=%s', self.softwareVersion, tempValue.getType())
        
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
        
        if self.isStateRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "state") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-state').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "state", "state", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-state-bad-value').infoFunc(): logFunc('state not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setState(tempVar)
            for logFunc in self._log('read-tag-values-state').debug3Func(): logFunc('read state. state=%s, tempValue=%s', self.state, tempValue.getType())
        
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
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "registered", 
        "namespace": "registered", 
        "className": "RegisteredMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.registered.registered_maapi_gen import RegisteredMaapi", 
        "baseClassName": "RegisteredMaapiBase", 
        "baseModule": "registered_maapi_base_gen"
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
            "yangName": "registered", 
            "namespace": "registered", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "keyLeaf": {
                "varName": "registered", 
                "defaultVal": null, 
                "typeHandler": "handler: EnumHandlerPy"
            }, 
            "name": "registered"
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
            "typeHandler": "handler: StringHandler", 
            "memberName": "devComment", 
            "yangName": "dev-comment", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "softwareVersion", 
            "yangName": "software-version", 
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
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "state", 
            "yangName": "state", 
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
            "typeHandler": "handler: StringHandler", 
            "memberName": "devComment", 
            "yangName": "dev-comment", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "softwareVersion", 
            "yangName": "software-version", 
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
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "state", 
            "yangName": "state", 
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
        }
    ], 
    "createTime": "2013"
}
"""


