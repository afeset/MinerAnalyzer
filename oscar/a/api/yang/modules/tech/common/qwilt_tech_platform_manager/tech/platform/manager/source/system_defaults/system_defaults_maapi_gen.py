


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

from system_defaults_maapi_base_gen import SystemDefaultsMaapiBase




class BlinkySystemDefaultsMaapi(SystemDefaultsMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-systemDefaults")
        self.domain = None

        

        
        self.commandWarningTimeoutRequested = False
        self.commandWarningTimeout = None
        self.commandWarningTimeoutSet = False
        
        self.commandTimeoutRequested = False
        self.commandTimeout = None
        self.commandTimeoutSet = False
        
        self.enabledRequested = False
        self.enabled = None
        self.enabledSet = False
        
        self.simulationFileRequested = False
        self.simulationFile = None
        self.simulationFileSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestCommandWarningTimeout(True)
        
        self.requestCommandTimeout(True)
        
        self.requestEnabled(True)
        
        self.requestSimulationFile(True)
        
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestCommandWarningTimeout(True)
        
        self.requestCommandTimeout(True)
        
        self.requestEnabled(True)
        
        self.requestSimulationFile(True)
        
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestCommandWarningTimeout(False)
        
        self.requestCommandTimeout(False)
        
        self.requestEnabled(False)
        
        self.requestSimulationFile(False)
        
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestCommandWarningTimeout(False)
        
        self.requestCommandTimeout(False)
        
        self.requestEnabled(False)
        
        self.requestSimulationFile(False)
        
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setCommandWarningTimeout(None)
        self.commandWarningTimeoutSet = False
        
        self.setCommandTimeout(None)
        self.commandTimeoutSet = False
        
        self.setEnabled(None)
        self.enabledSet = False
        
        self.setSimulationFile(None)
        self.simulationFileSet = False
        
        

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



    def requestCommandWarningTimeout (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-commandwarningtimeout').debug3Func(): logFunc('called. requested=%s', requested)
        self.commandWarningTimeoutRequested = requested
        self.commandWarningTimeoutSet = False

    def isCommandWarningTimeoutRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-commandwarningtimeout-requested').debug3Func(): logFunc('called. requested=%s', self.commandWarningTimeoutRequested)
        return self.commandWarningTimeoutRequested

    def getCommandWarningTimeout (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-commandwarningtimeout').debug3Func(): logFunc('called. self.commandWarningTimeoutSet=%s, self.commandWarningTimeout=%s', self.commandWarningTimeoutSet, self.commandWarningTimeout)
        if self.commandWarningTimeoutSet:
            return self.commandWarningTimeout
        return None

    def hasCommandWarningTimeout (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-commandwarningtimeout').debug3Func(): logFunc('called. self.commandWarningTimeoutSet=%s, self.commandWarningTimeout=%s', self.commandWarningTimeoutSet, self.commandWarningTimeout)
        if self.commandWarningTimeoutSet:
            return True
        return False

    def setCommandWarningTimeout (self, commandWarningTimeout):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-commandwarningtimeout').debug3Func(): logFunc('called. commandWarningTimeout=%s, old=%s', commandWarningTimeout, self.commandWarningTimeout)
        self.commandWarningTimeoutSet = True
        self.commandWarningTimeout = commandWarningTimeout

    def requestCommandTimeout (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-commandtimeout').debug3Func(): logFunc('called. requested=%s', requested)
        self.commandTimeoutRequested = requested
        self.commandTimeoutSet = False

    def isCommandTimeoutRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-commandtimeout-requested').debug3Func(): logFunc('called. requested=%s', self.commandTimeoutRequested)
        return self.commandTimeoutRequested

    def getCommandTimeout (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-commandtimeout').debug3Func(): logFunc('called. self.commandTimeoutSet=%s, self.commandTimeout=%s', self.commandTimeoutSet, self.commandTimeout)
        if self.commandTimeoutSet:
            return self.commandTimeout
        return None

    def hasCommandTimeout (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-commandtimeout').debug3Func(): logFunc('called. self.commandTimeoutSet=%s, self.commandTimeout=%s', self.commandTimeoutSet, self.commandTimeout)
        if self.commandTimeoutSet:
            return True
        return False

    def setCommandTimeout (self, commandTimeout):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-commandtimeout').debug3Func(): logFunc('called. commandTimeout=%s, old=%s', commandTimeout, self.commandTimeout)
        self.commandTimeoutSet = True
        self.commandTimeout = commandTimeout

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

    def requestSimulationFile (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-simulationfile').debug3Func(): logFunc('called. requested=%s', requested)
        self.simulationFileRequested = requested
        self.simulationFileSet = False

    def isSimulationFileRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-simulationfile-requested').debug3Func(): logFunc('called. requested=%s', self.simulationFileRequested)
        return self.simulationFileRequested

    def getSimulationFile (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-simulationfile').debug3Func(): logFunc('called. self.simulationFileSet=%s, self.simulationFile=%s', self.simulationFileSet, self.simulationFile)
        if self.simulationFileSet:
            return self.simulationFile
        return None

    def hasSimulationFile (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-simulationfile').debug3Func(): logFunc('called. self.simulationFileSet=%s, self.simulationFile=%s', self.simulationFileSet, self.simulationFile)
        if self.simulationFileSet:
            return True
        return False

    def setSimulationFile (self, simulationFile):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-simulationfile').debug3Func(): logFunc('called. simulationFile=%s, old=%s', simulationFile, self.simulationFile)
        self.simulationFileSet = True
        self.simulationFile = simulationFile


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.commandWarningTimeout = 0
        self.commandWarningTimeoutSet = False
        
        self.commandTimeout = 0
        self.commandTimeoutSet = False
        
        self.enabled = 0
        self.enabledSet = False
        
        self.simulationFile = 0
        self.simulationFileSet = False
        

    def _getSelfKeyPath (self, source
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", "qt-pltf-mngr"))
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

        
        if self.hasCommandWarningTimeout():
            valCommandWarningTimeout = Value()
            if self.commandWarningTimeout is not None:
                valCommandWarningTimeout.setInt64(self.commandWarningTimeout)
            else:
                valCommandWarningTimeout.setEmpty()
            tagValueList.push(("command-warning-timeout", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"), valCommandWarningTimeout)
        
        if self.hasCommandTimeout():
            valCommandTimeout = Value()
            if self.commandTimeout is not None:
                valCommandTimeout.setInt64(self.commandTimeout)
            else:
                valCommandTimeout.setEmpty()
            tagValueList.push(("command-timeout", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"), valCommandTimeout)
        
        if self.hasEnabled():
            valEnabled = Value()
            if self.enabled is not None:
                valEnabled.setBool(self.enabled)
            else:
                valEnabled.setEmpty()
            tagValueList.push(("enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"), valEnabled)
        
        if self.hasSimulationFile():
            valSimulationFile = Value()
            if self.simulationFile is not None:
                valSimulationFile.setString(self.simulationFile)
            else:
                valSimulationFile.setEmpty()
            tagValueList.push(("simulation-file", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"), valSimulationFile)
        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isCommandWarningTimeoutRequested():
            valCommandWarningTimeout = Value()
            valCommandWarningTimeout.setEmpty()
            tagValueList.push(("command-warning-timeout", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"), valCommandWarningTimeout)
        
        if self.isCommandTimeoutRequested():
            valCommandTimeout = Value()
            valCommandTimeout.setEmpty()
            tagValueList.push(("command-timeout", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"), valCommandTimeout)
        
        if self.isEnabledRequested():
            valEnabled = Value()
            valEnabled.setEmpty()
            tagValueList.push(("enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"), valEnabled)
        
        if self.isSimulationFileRequested():
            valSimulationFile = Value()
            valSimulationFile.setEmpty()
            tagValueList.push(("simulation-file", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"), valSimulationFile)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isCommandWarningTimeoutRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "command-warning-timeout") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-commandwarningtimeout').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "commandWarningTimeout", "command-warning-timeout", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-command-warning-timeout-bad-value').infoFunc(): logFunc('commandWarningTimeout not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setCommandWarningTimeout(tempVar)
            for logFunc in self._log('read-tag-values-command-warning-timeout').debug3Func(): logFunc('read commandWarningTimeout. commandWarningTimeout=%s, tempValue=%s', self.commandWarningTimeout, tempValue.getType())
        
        if self.isCommandTimeoutRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "command-timeout") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-commandtimeout').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "commandTimeout", "command-timeout", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-command-timeout-bad-value').infoFunc(): logFunc('commandTimeout not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setCommandTimeout(tempVar)
            for logFunc in self._log('read-tag-values-command-timeout').debug3Func(): logFunc('read commandTimeout. commandTimeout=%s, tempValue=%s', self.commandTimeout, tempValue.getType())
        
        if self.isEnabledRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "enabled") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-enabled').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "enabled", "enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", tag, ns)
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
        
        if self.isSimulationFileRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "simulation-file") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-simulationfile').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "simulationFile", "simulation-file", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-simulation-file-bad-value').infoFunc(): logFunc('simulationFile not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setSimulationFile(tempVar)
            for logFunc in self._log('read-tag-values-simulation-file').debug3Func(): logFunc('read simulationFile. simulationFile=%s, tempValue=%s', self.simulationFile, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "systemDefaults", 
        "namespace": "system_defaults", 
        "className": "SystemDefaultsMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.source.system_defaults.system_defaults_maapi_gen import SystemDefaultsMaapi", 
        "baseClassName": "SystemDefaultsMaapiBase", 
        "baseModule": "system_defaults_maapi_base_gen"
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
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "name": "system-defaults"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "commandWarningTimeout", 
            "yangName": "command-warning-timeout", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "commandTimeout", 
            "yangName": "command-timeout", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "simulationFile", 
            "yangName": "simulation-file", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
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
            "qwilt_tech_platform_manager"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "commandWarningTimeout", 
            "yangName": "command-warning-timeout", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "commandTimeout", 
            "yangName": "command-timeout", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "simulationFile", 
            "yangName": "simulation-file", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


