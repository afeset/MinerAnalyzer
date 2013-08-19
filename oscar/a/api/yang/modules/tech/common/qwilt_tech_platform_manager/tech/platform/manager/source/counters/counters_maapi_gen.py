


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

from counters_maapi_base_gen import CountersMaapiBase




class BlinkyCountersMaapi(CountersMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-counters")
        self.domain = None

        

        
        self.commandWarningTimeoutsRequested = False
        self.commandWarningTimeouts = None
        self.commandWarningTimeoutsSet = False
        
        self.commandErrorsRequested = False
        self.commandErrors = None
        self.commandErrorsSet = False
        
        self.fileErrorsRequested = False
        self.fileErrors = None
        self.fileErrorsSet = False
        
        self.readsRequested = False
        self.reads = None
        self.readsSet = False
        
        self.parsingErrorsRequested = False
        self.parsingErrors = None
        self.parsingErrorsSet = False
        
        self.commandTimeoutsRequested = False
        self.commandTimeouts = None
        self.commandTimeoutsSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestCommandWarningTimeouts(True)
        
        self.requestCommandErrors(True)
        
        self.requestFileErrors(True)
        
        self.requestReads(True)
        
        self.requestParsingErrors(True)
        
        self.requestCommandTimeouts(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestCommandWarningTimeouts(False)
        
        self.requestCommandErrors(False)
        
        self.requestFileErrors(False)
        
        self.requestReads(False)
        
        self.requestParsingErrors(False)
        
        self.requestCommandTimeouts(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestCommandWarningTimeouts(True)
        
        self.requestCommandErrors(True)
        
        self.requestFileErrors(True)
        
        self.requestReads(True)
        
        self.requestParsingErrors(True)
        
        self.requestCommandTimeouts(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestCommandWarningTimeouts(False)
        
        self.requestCommandErrors(False)
        
        self.requestFileErrors(False)
        
        self.requestReads(False)
        
        self.requestParsingErrors(False)
        
        self.requestCommandTimeouts(False)
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        

    def write (self
              , source
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(source, trxContext)

    def read (self
              , source
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(source, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , source
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(source, 
                                  True,
                                  trxContext)



    def requestCommandWarningTimeouts (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-commandwarningtimeouts').debug3Func(): logFunc('called. requested=%s', requested)
        self.commandWarningTimeoutsRequested = requested
        self.commandWarningTimeoutsSet = False

    def isCommandWarningTimeoutsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-commandwarningtimeouts-requested').debug3Func(): logFunc('called. requested=%s', self.commandWarningTimeoutsRequested)
        return self.commandWarningTimeoutsRequested

    def getCommandWarningTimeouts (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-commandwarningtimeouts').debug3Func(): logFunc('called. self.commandWarningTimeoutsSet=%s, self.commandWarningTimeouts=%s', self.commandWarningTimeoutsSet, self.commandWarningTimeouts)
        if self.commandWarningTimeoutsSet:
            return self.commandWarningTimeouts
        return None

    def hasCommandWarningTimeouts (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-commandwarningtimeouts').debug3Func(): logFunc('called. self.commandWarningTimeoutsSet=%s, self.commandWarningTimeouts=%s', self.commandWarningTimeoutsSet, self.commandWarningTimeouts)
        if self.commandWarningTimeoutsSet:
            return True
        return False

    def setCommandWarningTimeouts (self, commandWarningTimeouts):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-commandwarningtimeouts').debug3Func(): logFunc('called. commandWarningTimeouts=%s, old=%s', commandWarningTimeouts, self.commandWarningTimeouts)
        self.commandWarningTimeoutsSet = True
        self.commandWarningTimeouts = commandWarningTimeouts

    def requestCommandErrors (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-commanderrors').debug3Func(): logFunc('called. requested=%s', requested)
        self.commandErrorsRequested = requested
        self.commandErrorsSet = False

    def isCommandErrorsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-commanderrors-requested').debug3Func(): logFunc('called. requested=%s', self.commandErrorsRequested)
        return self.commandErrorsRequested

    def getCommandErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-commanderrors').debug3Func(): logFunc('called. self.commandErrorsSet=%s, self.commandErrors=%s', self.commandErrorsSet, self.commandErrors)
        if self.commandErrorsSet:
            return self.commandErrors
        return None

    def hasCommandErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-commanderrors').debug3Func(): logFunc('called. self.commandErrorsSet=%s, self.commandErrors=%s', self.commandErrorsSet, self.commandErrors)
        if self.commandErrorsSet:
            return True
        return False

    def setCommandErrors (self, commandErrors):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-commanderrors').debug3Func(): logFunc('called. commandErrors=%s, old=%s', commandErrors, self.commandErrors)
        self.commandErrorsSet = True
        self.commandErrors = commandErrors

    def requestFileErrors (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-fileerrors').debug3Func(): logFunc('called. requested=%s', requested)
        self.fileErrorsRequested = requested
        self.fileErrorsSet = False

    def isFileErrorsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-fileerrors-requested').debug3Func(): logFunc('called. requested=%s', self.fileErrorsRequested)
        return self.fileErrorsRequested

    def getFileErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-fileerrors').debug3Func(): logFunc('called. self.fileErrorsSet=%s, self.fileErrors=%s', self.fileErrorsSet, self.fileErrors)
        if self.fileErrorsSet:
            return self.fileErrors
        return None

    def hasFileErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-fileerrors').debug3Func(): logFunc('called. self.fileErrorsSet=%s, self.fileErrors=%s', self.fileErrorsSet, self.fileErrors)
        if self.fileErrorsSet:
            return True
        return False

    def setFileErrors (self, fileErrors):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-fileerrors').debug3Func(): logFunc('called. fileErrors=%s, old=%s', fileErrors, self.fileErrors)
        self.fileErrorsSet = True
        self.fileErrors = fileErrors

    def requestReads (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-reads').debug3Func(): logFunc('called. requested=%s', requested)
        self.readsRequested = requested
        self.readsSet = False

    def isReadsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-reads-requested').debug3Func(): logFunc('called. requested=%s', self.readsRequested)
        return self.readsRequested

    def getReads (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-reads').debug3Func(): logFunc('called. self.readsSet=%s, self.reads=%s', self.readsSet, self.reads)
        if self.readsSet:
            return self.reads
        return None

    def hasReads (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-reads').debug3Func(): logFunc('called. self.readsSet=%s, self.reads=%s', self.readsSet, self.reads)
        if self.readsSet:
            return True
        return False

    def setReads (self, reads):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-reads').debug3Func(): logFunc('called. reads=%s, old=%s', reads, self.reads)
        self.readsSet = True
        self.reads = reads

    def requestParsingErrors (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-parsingerrors').debug3Func(): logFunc('called. requested=%s', requested)
        self.parsingErrorsRequested = requested
        self.parsingErrorsSet = False

    def isParsingErrorsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-parsingerrors-requested').debug3Func(): logFunc('called. requested=%s', self.parsingErrorsRequested)
        return self.parsingErrorsRequested

    def getParsingErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-parsingerrors').debug3Func(): logFunc('called. self.parsingErrorsSet=%s, self.parsingErrors=%s', self.parsingErrorsSet, self.parsingErrors)
        if self.parsingErrorsSet:
            return self.parsingErrors
        return None

    def hasParsingErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-parsingerrors').debug3Func(): logFunc('called. self.parsingErrorsSet=%s, self.parsingErrors=%s', self.parsingErrorsSet, self.parsingErrors)
        if self.parsingErrorsSet:
            return True
        return False

    def setParsingErrors (self, parsingErrors):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-parsingerrors').debug3Func(): logFunc('called. parsingErrors=%s, old=%s', parsingErrors, self.parsingErrors)
        self.parsingErrorsSet = True
        self.parsingErrors = parsingErrors

    def requestCommandTimeouts (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-commandtimeouts').debug3Func(): logFunc('called. requested=%s', requested)
        self.commandTimeoutsRequested = requested
        self.commandTimeoutsSet = False

    def isCommandTimeoutsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-commandtimeouts-requested').debug3Func(): logFunc('called. requested=%s', self.commandTimeoutsRequested)
        return self.commandTimeoutsRequested

    def getCommandTimeouts (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-commandtimeouts').debug3Func(): logFunc('called. self.commandTimeoutsSet=%s, self.commandTimeouts=%s', self.commandTimeoutsSet, self.commandTimeouts)
        if self.commandTimeoutsSet:
            return self.commandTimeouts
        return None

    def hasCommandTimeouts (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-commandtimeouts').debug3Func(): logFunc('called. self.commandTimeoutsSet=%s, self.commandTimeouts=%s', self.commandTimeoutsSet, self.commandTimeouts)
        if self.commandTimeoutsSet:
            return True
        return False

    def setCommandTimeouts (self, commandTimeouts):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-commandtimeouts').debug3Func(): logFunc('called. commandTimeouts=%s, old=%s', commandTimeouts, self.commandTimeouts)
        self.commandTimeoutsSet = True
        self.commandTimeouts = commandTimeouts


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.commandWarningTimeouts = 0
        self.commandWarningTimeoutsSet = False
        
        self.commandErrors = 0
        self.commandErrorsSet = False
        
        self.fileErrors = 0
        self.fileErrorsSet = False
        
        self.reads = 0
        self.readsSet = False
        
        self.parsingErrors = 0
        self.parsingErrorsSet = False
        
        self.commandTimeouts = 0
        self.commandTimeoutsSet = False
        

    def _getSelfKeyPath (self, source
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("counters", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", "qt-pltf-mngr"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(source);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("source", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", "qt-pltf-mngr"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("manager", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", "qt-pltf-mngr"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("platform", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform", "qt-pltf"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        source, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(source, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(source, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       source, 
                       
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

        keyPath = self._getSelfKeyPath(source, 
                                       
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
                               source, 
                               
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

        
        if self.isCommandWarningTimeoutsRequested():
            valCommandWarningTimeouts = Value()
            valCommandWarningTimeouts.setEmpty()
            tagValueList.push(("command-warning-timeouts", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"), valCommandWarningTimeouts)
        
        if self.isCommandErrorsRequested():
            valCommandErrors = Value()
            valCommandErrors.setEmpty()
            tagValueList.push(("command-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"), valCommandErrors)
        
        if self.isFileErrorsRequested():
            valFileErrors = Value()
            valFileErrors.setEmpty()
            tagValueList.push(("file-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"), valFileErrors)
        
        if self.isReadsRequested():
            valReads = Value()
            valReads.setEmpty()
            tagValueList.push(("reads", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"), valReads)
        
        if self.isParsingErrorsRequested():
            valParsingErrors = Value()
            valParsingErrors.setEmpty()
            tagValueList.push(("parsing-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"), valParsingErrors)
        
        if self.isCommandTimeoutsRequested():
            valCommandTimeouts = Value()
            valCommandTimeouts.setEmpty()
            tagValueList.push(("command-timeouts", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"), valCommandTimeouts)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isCommandWarningTimeoutsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "command-warning-timeouts") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-commandwarningtimeouts').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "commandWarningTimeouts", "command-warning-timeouts", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-command-warning-timeouts-bad-value').infoFunc(): logFunc('commandWarningTimeouts not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setCommandWarningTimeouts(tempVar)
            for logFunc in self._log('read-tag-values-command-warning-timeouts').debug3Func(): logFunc('read commandWarningTimeouts. commandWarningTimeouts=%s, tempValue=%s', self.commandWarningTimeouts, tempValue.getType())
        
        if self.isCommandErrorsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "command-errors") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-commanderrors').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "commandErrors", "command-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-command-errors-bad-value').infoFunc(): logFunc('commandErrors not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setCommandErrors(tempVar)
            for logFunc in self._log('read-tag-values-command-errors').debug3Func(): logFunc('read commandErrors. commandErrors=%s, tempValue=%s', self.commandErrors, tempValue.getType())
        
        if self.isFileErrorsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "file-errors") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-fileerrors').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "fileErrors", "file-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-file-errors-bad-value').infoFunc(): logFunc('fileErrors not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setFileErrors(tempVar)
            for logFunc in self._log('read-tag-values-file-errors').debug3Func(): logFunc('read fileErrors. fileErrors=%s, tempValue=%s', self.fileErrors, tempValue.getType())
        
        if self.isReadsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "reads") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-reads').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "reads", "reads", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-reads-bad-value').infoFunc(): logFunc('reads not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setReads(tempVar)
            for logFunc in self._log('read-tag-values-reads').debug3Func(): logFunc('read reads. reads=%s, tempValue=%s', self.reads, tempValue.getType())
        
        if self.isParsingErrorsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "parsing-errors") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-parsingerrors').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "parsingErrors", "parsing-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-parsing-errors-bad-value').infoFunc(): logFunc('parsingErrors not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setParsingErrors(tempVar)
            for logFunc in self._log('read-tag-values-parsing-errors').debug3Func(): logFunc('read parsingErrors. parsingErrors=%s, tempValue=%s', self.parsingErrors, tempValue.getType())
        
        if self.isCommandTimeoutsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "command-timeouts") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-commandtimeouts').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "commandTimeouts", "command-timeouts", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-command-timeouts-bad-value').infoFunc(): logFunc('commandTimeouts not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setCommandTimeouts(tempVar)
            for logFunc in self._log('read-tag-values-command-timeouts').debug3Func(): logFunc('read commandTimeouts. commandTimeouts=%s, tempValue=%s', self.commandTimeouts, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "counters", 
        "namespace": "counters", 
        "className": "CountersMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.source.counters.counters_maapi_gen import CountersMaapi", 
        "baseClassName": "CountersMaapiBase", 
        "baseModule": "counters_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-pltf", 
            "yangName": "platform", 
            "namespace": "platform", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform", 
            "name": "platform"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "yangName": "manager", 
            "namespace": "manager", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "name": "manager"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "isCurrent": false, 
            "yangName": "source", 
            "namespace": "source", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "keyLeaf": {
                "varName": "source", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "source"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "yangName": "counters", 
            "namespace": "counters", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "name": "counters"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "commandWarningTimeouts", 
            "yangName": "command-warning-timeouts", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "commandErrors", 
            "yangName": "command-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "fileErrors", 
            "yangName": "file-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "reads", 
            "yangName": "reads", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "parsingErrors", 
            "yangName": "parsing-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "commandTimeouts", 
            "yangName": "command-timeouts", 
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
            "qwilt_tech_platform_manager"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "commandWarningTimeouts", 
            "yangName": "command-warning-timeouts", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "commandErrors", 
            "yangName": "command-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "fileErrors", 
            "yangName": "file-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "reads", 
            "yangName": "reads", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "parsingErrors", 
            "yangName": "parsing-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "commandTimeouts", 
            "yangName": "command-timeouts", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


