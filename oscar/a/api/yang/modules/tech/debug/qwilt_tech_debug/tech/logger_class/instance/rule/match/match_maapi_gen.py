


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

from match_maapi_base_gen import MatchMaapiBase


from a.api.yang.modules.tech.debug.qwilt_tech_debug.qwilt_tech_debug_module_gen import LogSeverity
from a.api.yang.modules.tech.debug.qwilt_tech_debug.qwilt_tech_debug_module_gen import MatchBoolean


class BlinkyMatchMaapi(MatchMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-match")
        self.domain = None

        

        
        self.minSeverityRequested = False
        self.minSeverity = None
        self.minSeveritySet = False
        
        self.functionRequested = False
        self.function = None
        self.functionSet = False
        
        self.messageNameRequested = False
        self.messageName = None
        self.messageNameSet = False
        
        self.groupRequested = False
        self.group = None
        self.groupSet = False
        
        self.maxLineRequested = False
        self.maxLine = None
        self.maxLineSet = False
        
        self.minLineRequested = False
        self.minLine = None
        self.minLineSet = False
        
        self.moduleRequested = False
        self.module = None
        self.moduleSet = False
        
        self.fileRequested = False
        self.file = None
        self.fileSet = False
        
        self.conditionalRequested = False
        self.conditional = None
        self.conditionalSet = False
        
        self.maxSeverityRequested = False
        self.maxSeverity = None
        self.maxSeveritySet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestMinSeverity(True)
        
        self.requestFunction(True)
        
        self.requestMessageName(True)
        
        self.requestGroup(True)
        
        self.requestMaxLine(True)
        
        self.requestMinLine(True)
        
        self.requestModule(True)
        
        self.requestFile(True)
        
        self.requestConditional(True)
        
        self.requestMaxSeverity(True)
        
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestMinSeverity(True)
        
        self.requestFunction(True)
        
        self.requestMessageName(True)
        
        self.requestGroup(True)
        
        self.requestMaxLine(True)
        
        self.requestMinLine(True)
        
        self.requestModule(True)
        
        self.requestFile(True)
        
        self.requestConditional(True)
        
        self.requestMaxSeverity(True)
        
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestMinSeverity(False)
        
        self.requestFunction(False)
        
        self.requestMessageName(False)
        
        self.requestGroup(False)
        
        self.requestMaxLine(False)
        
        self.requestMinLine(False)
        
        self.requestModule(False)
        
        self.requestFile(False)
        
        self.requestConditional(False)
        
        self.requestMaxSeverity(False)
        
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestMinSeverity(False)
        
        self.requestFunction(False)
        
        self.requestMessageName(False)
        
        self.requestGroup(False)
        
        self.requestMaxLine(False)
        
        self.requestMinLine(False)
        
        self.requestModule(False)
        
        self.requestFile(False)
        
        self.requestConditional(False)
        
        self.requestMaxSeverity(False)
        
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setMinSeverity(None)
        self.minSeveritySet = False
        
        self.setFunction(None)
        self.functionSet = False
        
        self.setMessageName(None)
        self.messageNameSet = False
        
        self.setGroup(None)
        self.groupSet = False
        
        self.setMaxLine(None)
        self.maxLineSet = False
        
        self.setMinLine(None)
        self.minLineSet = False
        
        self.setModule(None)
        self.moduleSet = False
        
        self.setFile(None)
        self.fileSet = False
        
        self.setConditional(None)
        self.conditionalSet = False
        
        self.setMaxSeverity(None)
        self.maxSeveritySet = False
        
        

    def write (self
              , loggerClass
              , instance
              , rule
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(loggerClass, instance, rule, trxContext)

    def read (self
              , loggerClass
              , instance
              , rule
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(loggerClass, instance, rule, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , loggerClass
                       , instance
                       , rule
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(loggerClass, instance, rule, 
                                  True,
                                  trxContext)



    def requestMinSeverity (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-minseverity').debug3Func(): logFunc('called. requested=%s', requested)
        self.minSeverityRequested = requested
        self.minSeveritySet = False

    def isMinSeverityRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-minseverity-requested').debug3Func(): logFunc('called. requested=%s', self.minSeverityRequested)
        return self.minSeverityRequested

    def getMinSeverity (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-minseverity').debug3Func(): logFunc('called. self.minSeveritySet=%s, self.minSeverity=%s', self.minSeveritySet, self.minSeverity)
        if self.minSeveritySet:
            return self.minSeverity
        return None

    def hasMinSeverity (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-minseverity').debug3Func(): logFunc('called. self.minSeveritySet=%s, self.minSeverity=%s', self.minSeveritySet, self.minSeverity)
        if self.minSeveritySet:
            return True
        return False

    def setMinSeverity (self, minSeverity):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-minseverity').debug3Func(): logFunc('called. minSeverity=%s, old=%s', minSeverity, self.minSeverity)
        self.minSeveritySet = True
        self.minSeverity = minSeverity

    def requestFunction (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-function').debug3Func(): logFunc('called. requested=%s', requested)
        self.functionRequested = requested
        self.functionSet = False

    def isFunctionRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-function-requested').debug3Func(): logFunc('called. requested=%s', self.functionRequested)
        return self.functionRequested

    def getFunction (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-function').debug3Func(): logFunc('called. self.functionSet=%s, self.function=%s', self.functionSet, self.function)
        if self.functionSet:
            return self.function
        return None

    def hasFunction (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-function').debug3Func(): logFunc('called. self.functionSet=%s, self.function=%s', self.functionSet, self.function)
        if self.functionSet:
            return True
        return False

    def setFunction (self, function):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-function').debug3Func(): logFunc('called. function=%s, old=%s', function, self.function)
        self.functionSet = True
        self.function = function

    def requestMessageName (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-messagename').debug3Func(): logFunc('called. requested=%s', requested)
        self.messageNameRequested = requested
        self.messageNameSet = False

    def isMessageNameRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-messagename-requested').debug3Func(): logFunc('called. requested=%s', self.messageNameRequested)
        return self.messageNameRequested

    def getMessageName (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-messagename').debug3Func(): logFunc('called. self.messageNameSet=%s, self.messageName=%s', self.messageNameSet, self.messageName)
        if self.messageNameSet:
            return self.messageName
        return None

    def hasMessageName (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-messagename').debug3Func(): logFunc('called. self.messageNameSet=%s, self.messageName=%s', self.messageNameSet, self.messageName)
        if self.messageNameSet:
            return True
        return False

    def setMessageName (self, messageName):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-messagename').debug3Func(): logFunc('called. messageName=%s, old=%s', messageName, self.messageName)
        self.messageNameSet = True
        self.messageName = messageName

    def requestGroup (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-group').debug3Func(): logFunc('called. requested=%s', requested)
        self.groupRequested = requested
        self.groupSet = False

    def isGroupRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-group-requested').debug3Func(): logFunc('called. requested=%s', self.groupRequested)
        return self.groupRequested

    def getGroup (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-group').debug3Func(): logFunc('called. self.groupSet=%s, self.group=%s', self.groupSet, self.group)
        if self.groupSet:
            return self.group
        return None

    def hasGroup (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-group').debug3Func(): logFunc('called. self.groupSet=%s, self.group=%s', self.groupSet, self.group)
        if self.groupSet:
            return True
        return False

    def setGroup (self, group):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-group').debug3Func(): logFunc('called. group=%s, old=%s', group, self.group)
        self.groupSet = True
        self.group = group

    def requestMaxLine (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-maxline').debug3Func(): logFunc('called. requested=%s', requested)
        self.maxLineRequested = requested
        self.maxLineSet = False

    def isMaxLineRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-maxline-requested').debug3Func(): logFunc('called. requested=%s', self.maxLineRequested)
        return self.maxLineRequested

    def getMaxLine (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-maxline').debug3Func(): logFunc('called. self.maxLineSet=%s, self.maxLine=%s', self.maxLineSet, self.maxLine)
        if self.maxLineSet:
            return self.maxLine
        return None

    def hasMaxLine (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-maxline').debug3Func(): logFunc('called. self.maxLineSet=%s, self.maxLine=%s', self.maxLineSet, self.maxLine)
        if self.maxLineSet:
            return True
        return False

    def setMaxLine (self, maxLine):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-maxline').debug3Func(): logFunc('called. maxLine=%s, old=%s', maxLine, self.maxLine)
        self.maxLineSet = True
        self.maxLine = maxLine

    def requestMinLine (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-minline').debug3Func(): logFunc('called. requested=%s', requested)
        self.minLineRequested = requested
        self.minLineSet = False

    def isMinLineRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-minline-requested').debug3Func(): logFunc('called. requested=%s', self.minLineRequested)
        return self.minLineRequested

    def getMinLine (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-minline').debug3Func(): logFunc('called. self.minLineSet=%s, self.minLine=%s', self.minLineSet, self.minLine)
        if self.minLineSet:
            return self.minLine
        return None

    def hasMinLine (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-minline').debug3Func(): logFunc('called. self.minLineSet=%s, self.minLine=%s', self.minLineSet, self.minLine)
        if self.minLineSet:
            return True
        return False

    def setMinLine (self, minLine):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-minline').debug3Func(): logFunc('called. minLine=%s, old=%s', minLine, self.minLine)
        self.minLineSet = True
        self.minLine = minLine

    def requestModule (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-module').debug3Func(): logFunc('called. requested=%s', requested)
        self.moduleRequested = requested
        self.moduleSet = False

    def isModuleRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-module-requested').debug3Func(): logFunc('called. requested=%s', self.moduleRequested)
        return self.moduleRequested

    def getModule (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-module').debug3Func(): logFunc('called. self.moduleSet=%s, self.module=%s', self.moduleSet, self.module)
        if self.moduleSet:
            return self.module
        return None

    def hasModule (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-module').debug3Func(): logFunc('called. self.moduleSet=%s, self.module=%s', self.moduleSet, self.module)
        if self.moduleSet:
            return True
        return False

    def setModule (self, module):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-module').debug3Func(): logFunc('called. module=%s, old=%s', module, self.module)
        self.moduleSet = True
        self.module = module

    def requestFile (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-file').debug3Func(): logFunc('called. requested=%s', requested)
        self.fileRequested = requested
        self.fileSet = False

    def isFileRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-file-requested').debug3Func(): logFunc('called. requested=%s', self.fileRequested)
        return self.fileRequested

    def getFile (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-file').debug3Func(): logFunc('called. self.fileSet=%s, self.file=%s', self.fileSet, self.file)
        if self.fileSet:
            return self.file
        return None

    def hasFile (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-file').debug3Func(): logFunc('called. self.fileSet=%s, self.file=%s', self.fileSet, self.file)
        if self.fileSet:
            return True
        return False

    def setFile (self, file):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-file').debug3Func(): logFunc('called. file=%s, old=%s', file, self.file)
        self.fileSet = True
        self.file = file

    def requestConditional (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-conditional').debug3Func(): logFunc('called. requested=%s', requested)
        self.conditionalRequested = requested
        self.conditionalSet = False

    def isConditionalRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-conditional-requested').debug3Func(): logFunc('called. requested=%s', self.conditionalRequested)
        return self.conditionalRequested

    def getConditional (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-conditional').debug3Func(): logFunc('called. self.conditionalSet=%s, self.conditional=%s', self.conditionalSet, self.conditional)
        if self.conditionalSet:
            return self.conditional
        return None

    def hasConditional (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-conditional').debug3Func(): logFunc('called. self.conditionalSet=%s, self.conditional=%s', self.conditionalSet, self.conditional)
        if self.conditionalSet:
            return True
        return False

    def setConditional (self, conditional):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-conditional').debug3Func(): logFunc('called. conditional=%s, old=%s', conditional, self.conditional)
        self.conditionalSet = True
        self.conditional = conditional

    def requestMaxSeverity (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-maxseverity').debug3Func(): logFunc('called. requested=%s', requested)
        self.maxSeverityRequested = requested
        self.maxSeveritySet = False

    def isMaxSeverityRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-maxseverity-requested').debug3Func(): logFunc('called. requested=%s', self.maxSeverityRequested)
        return self.maxSeverityRequested

    def getMaxSeverity (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-maxseverity').debug3Func(): logFunc('called. self.maxSeveritySet=%s, self.maxSeverity=%s', self.maxSeveritySet, self.maxSeverity)
        if self.maxSeveritySet:
            return self.maxSeverity
        return None

    def hasMaxSeverity (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-maxseverity').debug3Func(): logFunc('called. self.maxSeveritySet=%s, self.maxSeverity=%s', self.maxSeveritySet, self.maxSeverity)
        if self.maxSeveritySet:
            return True
        return False

    def setMaxSeverity (self, maxSeverity):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-maxseverity').debug3Func(): logFunc('called. maxSeverity=%s, old=%s', maxSeverity, self.maxSeverity)
        self.maxSeveritySet = True
        self.maxSeverity = maxSeverity


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.minSeverity = 0
        self.minSeveritySet = False
        
        self.function = 0
        self.functionSet = False
        
        self.messageName = 0
        self.messageNameSet = False
        
        self.group = 0
        self.groupSet = False
        
        self.maxLine = 0
        self.maxLineSet = False
        
        self.minLine = 0
        self.minLineSet = False
        
        self.module = 0
        self.moduleSet = False
        
        self.file = 0
        self.fileSet = False
        
        self.conditional = 0
        self.conditionalSet = False
        
        self.maxSeverity = 0
        self.maxSeveritySet = False
        

    def _getSelfKeyPath (self, loggerClass
                         , instance
                         , rule
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("match", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(rule);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("rule", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(instance);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("instance", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(loggerClass);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("logger-class", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        loggerClass, 
                        instance, 
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
        res = self._collectItemsToDelete(loggerClass, 
                                         instance, 
                                         rule, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(loggerClass, 
                                       instance, 
                                       rule, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       loggerClass, 
                       instance, 
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

        keyPath = self._getSelfKeyPath(loggerClass, 
                                       instance, 
                                       rule, 
                                       
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
                               loggerClass, 
                               instance, 
                               rule, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasMinSeverity():
            valMinSeverity = Value()
            if self.minSeverity is not None:
                valMinSeverity.setEnum(self.minSeverity.getValue())
            else:
                valMinSeverity.setEmpty()
            tagValueList.push(("min-severity", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valMinSeverity)
        
        if self.hasFunction():
            valFunction = Value()
            if self.function is not None:
                valFunction.setString(self.function)
            else:
                valFunction.setEmpty()
            tagValueList.push(("function", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valFunction)
        
        if self.hasMessageName():
            valMessageName = Value()
            if self.messageName is not None:
                valMessageName.setString(self.messageName)
            else:
                valMessageName.setEmpty()
            tagValueList.push(("message-name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valMessageName)
        
        if self.hasGroup():
            valGroup = Value()
            if self.group is not None:
                valGroup.setString(self.group)
            else:
                valGroup.setEmpty()
            tagValueList.push(("group", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valGroup)
        
        if self.hasMaxLine():
            valMaxLine = Value()
            if self.maxLine is not None:
                valMaxLine.setInt64(self.maxLine)
            else:
                valMaxLine.setEmpty()
            tagValueList.push(("max-line", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valMaxLine)
        
        if self.hasMinLine():
            valMinLine = Value()
            if self.minLine is not None:
                valMinLine.setInt64(self.minLine)
            else:
                valMinLine.setEmpty()
            tagValueList.push(("min-line", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valMinLine)
        
        if self.hasModule():
            valModule = Value()
            if self.module is not None:
                valModule.setString(self.module)
            else:
                valModule.setEmpty()
            tagValueList.push(("module", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valModule)
        
        if self.hasFile():
            valFile = Value()
            if self.file is not None:
                valFile.setString(self.file)
            else:
                valFile.setEmpty()
            tagValueList.push(("file", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valFile)
        
        if self.hasConditional():
            valConditional = Value()
            if self.conditional is not None:
                valConditional.setEnum(self.conditional.getValue())
            else:
                valConditional.setEmpty()
            tagValueList.push(("conditional", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valConditional)
        
        if self.hasMaxSeverity():
            valMaxSeverity = Value()
            if self.maxSeverity is not None:
                valMaxSeverity.setEnum(self.maxSeverity.getValue())
            else:
                valMaxSeverity.setEmpty()
            tagValueList.push(("max-severity", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valMaxSeverity)
        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isMinSeverityRequested():
            valMinSeverity = Value()
            valMinSeverity.setEmpty()
            tagValueList.push(("min-severity", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valMinSeverity)
        
        if self.isFunctionRequested():
            valFunction = Value()
            valFunction.setEmpty()
            tagValueList.push(("function", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valFunction)
        
        if self.isMessageNameRequested():
            valMessageName = Value()
            valMessageName.setEmpty()
            tagValueList.push(("message-name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valMessageName)
        
        if self.isGroupRequested():
            valGroup = Value()
            valGroup.setEmpty()
            tagValueList.push(("group", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valGroup)
        
        if self.isMaxLineRequested():
            valMaxLine = Value()
            valMaxLine.setEmpty()
            tagValueList.push(("max-line", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valMaxLine)
        
        if self.isMinLineRequested():
            valMinLine = Value()
            valMinLine.setEmpty()
            tagValueList.push(("min-line", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valMinLine)
        
        if self.isModuleRequested():
            valModule = Value()
            valModule.setEmpty()
            tagValueList.push(("module", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valModule)
        
        if self.isFileRequested():
            valFile = Value()
            valFile.setEmpty()
            tagValueList.push(("file", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valFile)
        
        if self.isConditionalRequested():
            valConditional = Value()
            valConditional.setEmpty()
            tagValueList.push(("conditional", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valConditional)
        
        if self.isMaxSeverityRequested():
            valMaxSeverity = Value()
            valMaxSeverity.setEmpty()
            tagValueList.push(("max-severity", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valMaxSeverity)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isMinSeverityRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "min-severity") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-minseverity').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "minSeverity", "min-severity", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-min-severity-bad-value').infoFunc(): logFunc('minSeverity not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMinSeverity(tempVar)
            for logFunc in self._log('read-tag-values-min-severity').debug3Func(): logFunc('read minSeverity. minSeverity=%s, tempValue=%s', self.minSeverity, tempValue.getType())
        
        if self.isFunctionRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "function") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-function').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "function", "function", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-function-bad-value').infoFunc(): logFunc('function not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setFunction(tempVar)
            for logFunc in self._log('read-tag-values-function').debug3Func(): logFunc('read function. function=%s, tempValue=%s', self.function, tempValue.getType())
        
        if self.isMessageNameRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "message-name") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-messagename').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "messageName", "message-name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-message-name-bad-value').infoFunc(): logFunc('messageName not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMessageName(tempVar)
            for logFunc in self._log('read-tag-values-message-name').debug3Func(): logFunc('read messageName. messageName=%s, tempValue=%s', self.messageName, tempValue.getType())
        
        if self.isGroupRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "group") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-group').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "group", "group", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-group-bad-value').infoFunc(): logFunc('group not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setGroup(tempVar)
            for logFunc in self._log('read-tag-values-group').debug3Func(): logFunc('read group. group=%s, tempValue=%s', self.group, tempValue.getType())
        
        if self.isMaxLineRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "max-line") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-maxline').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "maxLine", "max-line", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-max-line-bad-value').infoFunc(): logFunc('maxLine not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMaxLine(tempVar)
            for logFunc in self._log('read-tag-values-max-line').debug3Func(): logFunc('read maxLine. maxLine=%s, tempValue=%s', self.maxLine, tempValue.getType())
        
        if self.isMinLineRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "min-line") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-minline').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "minLine", "min-line", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-min-line-bad-value').infoFunc(): logFunc('minLine not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMinLine(tempVar)
            for logFunc in self._log('read-tag-values-min-line').debug3Func(): logFunc('read minLine. minLine=%s, tempValue=%s', self.minLine, tempValue.getType())
        
        if self.isModuleRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "module") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-module').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "module", "module", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-module-bad-value').infoFunc(): logFunc('module not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setModule(tempVar)
            for logFunc in self._log('read-tag-values-module').debug3Func(): logFunc('read module. module=%s, tempValue=%s', self.module, tempValue.getType())
        
        if self.isFileRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "file") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-file').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "file", "file", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-file-bad-value').infoFunc(): logFunc('file not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setFile(tempVar)
            for logFunc in self._log('read-tag-values-file').debug3Func(): logFunc('read file. file=%s, tempValue=%s', self.file, tempValue.getType())
        
        if self.isConditionalRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "conditional") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-conditional').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "conditional", "conditional", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-conditional-bad-value').infoFunc(): logFunc('conditional not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setConditional(tempVar)
            for logFunc in self._log('read-tag-values-conditional').debug3Func(): logFunc('read conditional. conditional=%s, tempValue=%s', self.conditional, tempValue.getType())
        
        if self.isMaxSeverityRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "max-severity") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-maxseverity').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "maxSeverity", "max-severity", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-max-severity-bad-value').infoFunc(): logFunc('maxSeverity not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMaxSeverity(tempVar)
            for logFunc in self._log('read-tag-values-max-severity').debug3Func(): logFunc('read maxSeverity. maxSeverity=%s, tempValue=%s', self.maxSeverity, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "match", 
        "namespace": "match", 
        "className": "MatchMaapi", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.rule.match.match_maapi_gen import MatchMaapi", 
        "baseClassName": "MatchMaapiBase", 
        "baseModule": "match_maapi_base_gen"
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
            "isCurrent": false, 
            "yangName": "logger-class", 
            "namespace": "logger_class", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "keyLeaf": {
                "varName": "loggerClass", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "logger-class"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-debug", 
            "isCurrent": false, 
            "yangName": "instance", 
            "namespace": "instance", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "keyLeaf": {
                "varName": "instance", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "instance"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-debug", 
            "isCurrent": false, 
            "yangName": "rule", 
            "namespace": "rule", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "keyLeaf": {
                "varName": "rule", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "rule"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-debug", 
            "yangName": "match", 
            "namespace": "match", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "name": "match"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "minSeverity", 
            "yangName": "min-severity", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "any", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "function", 
            "yangName": "function", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "messageName", 
            "yangName": "message-name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "group", 
            "yangName": "group", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxLine", 
            "yangName": "max-line", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "minLine", 
            "yangName": "min-line", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "module", 
            "yangName": "module", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "file", 
            "yangName": "file", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "conditional", 
            "yangName": "conditional", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "any", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "maxSeverity", 
            "yangName": "max-severity", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "any", 
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
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "minSeverity", 
            "yangName": "min-severity", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "any", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "function", 
            "yangName": "function", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "messageName", 
            "yangName": "message-name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "group", 
            "yangName": "group", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxLine", 
            "yangName": "max-line", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "minLine", 
            "yangName": "min-line", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "module", 
            "yangName": "module", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "file", 
            "yangName": "file", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "conditional", 
            "yangName": "conditional", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "any", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "maxSeverity", 
            "yangName": "max-severity", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "any", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


