


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

from command_maapi_base_gen import CommandMaapiBase




class BlinkyCommandMaapi(CommandMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-command")
        self.domain = None

        

        
        self.executableRequested = False
        self.executable = None
        self.executableSet = False
        
        self.shellRequested = False
        self.shell = None
        self.shellSet = False
        
        self.extraArgsRequested = False
        self.extraArgs = None
        self.extraArgsSet = False
        
        self.argsRequested = False
        self.args = None
        self.argsSet = False
        
        self.valgrindRequested = False
        self.valgrind = None
        self.valgrindSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestExecutable(True)
        
        self.requestShell(True)
        
        self.requestExtraArgs(True)
        
        self.requestArgs(True)
        
        self.requestValgrind(True)
        
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestExecutable(True)
        
        self.requestShell(True)
        
        self.requestExtraArgs(True)
        
        self.requestArgs(True)
        
        self.requestValgrind(True)
        
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestExecutable(False)
        
        self.requestShell(False)
        
        self.requestExtraArgs(False)
        
        self.requestArgs(False)
        
        self.requestValgrind(False)
        
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestExecutable(False)
        
        self.requestShell(False)
        
        self.requestExtraArgs(False)
        
        self.requestArgs(False)
        
        self.requestValgrind(False)
        
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setExecutable(None)
        self.executableSet = False
        
        self.setShell(None)
        self.shellSet = False
        
        self.setExtraArgs(None)
        self.extraArgsSet = False
        
        self.setArgs(None)
        self.argsSet = False
        
        self.setValgrind(None)
        self.valgrindSet = False
        
        

    def write (self
              , process
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(process, trxContext)

    def read (self
              , process
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(process, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , process
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(process, 
                                  True,
                                  trxContext)



    def requestExecutable (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-executable').debug3Func(): logFunc('called. requested=%s', requested)
        self.executableRequested = requested
        self.executableSet = False

    def isExecutableRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-executable-requested').debug3Func(): logFunc('called. requested=%s', self.executableRequested)
        return self.executableRequested

    def getExecutable (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-executable').debug3Func(): logFunc('called. self.executableSet=%s, self.executable=%s', self.executableSet, self.executable)
        if self.executableSet:
            return self.executable
        return None

    def hasExecutable (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-executable').debug3Func(): logFunc('called. self.executableSet=%s, self.executable=%s', self.executableSet, self.executable)
        if self.executableSet:
            return True
        return False

    def setExecutable (self, executable):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-executable').debug3Func(): logFunc('called. executable=%s, old=%s', executable, self.executable)
        self.executableSet = True
        self.executable = executable

    def requestShell (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-shell').debug3Func(): logFunc('called. requested=%s', requested)
        self.shellRequested = requested
        self.shellSet = False

    def isShellRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-shell-requested').debug3Func(): logFunc('called. requested=%s', self.shellRequested)
        return self.shellRequested

    def getShell (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-shell').debug3Func(): logFunc('called. self.shellSet=%s, self.shell=%s', self.shellSet, self.shell)
        if self.shellSet:
            return self.shell
        return None

    def hasShell (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-shell').debug3Func(): logFunc('called. self.shellSet=%s, self.shell=%s', self.shellSet, self.shell)
        if self.shellSet:
            return True
        return False

    def setShell (self, shell):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-shell').debug3Func(): logFunc('called. shell=%s, old=%s', shell, self.shell)
        self.shellSet = True
        self.shell = shell

    def requestExtraArgs (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-extraargs').debug3Func(): logFunc('called. requested=%s', requested)
        self.extraArgsRequested = requested
        self.extraArgsSet = False

    def isExtraArgsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-extraargs-requested').debug3Func(): logFunc('called. requested=%s', self.extraArgsRequested)
        return self.extraArgsRequested

    def getExtraArgs (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-extraargs').debug3Func(): logFunc('called. self.extraArgsSet=%s, self.extraArgs=%s', self.extraArgsSet, self.extraArgs)
        if self.extraArgsSet:
            return self.extraArgs
        return None

    def hasExtraArgs (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-extraargs').debug3Func(): logFunc('called. self.extraArgsSet=%s, self.extraArgs=%s', self.extraArgsSet, self.extraArgs)
        if self.extraArgsSet:
            return True
        return False

    def setExtraArgs (self, extraArgs):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-extraargs').debug3Func(): logFunc('called. extraArgs=%s, old=%s', extraArgs, self.extraArgs)
        self.extraArgsSet = True
        self.extraArgs = extraArgs

    def requestArgs (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-args').debug3Func(): logFunc('called. requested=%s', requested)
        self.argsRequested = requested
        self.argsSet = False

    def isArgsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-args-requested').debug3Func(): logFunc('called. requested=%s', self.argsRequested)
        return self.argsRequested

    def getArgs (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-args').debug3Func(): logFunc('called. self.argsSet=%s, self.args=%s', self.argsSet, self.args)
        if self.argsSet:
            return self.args
        return None

    def hasArgs (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-args').debug3Func(): logFunc('called. self.argsSet=%s, self.args=%s', self.argsSet, self.args)
        if self.argsSet:
            return True
        return False

    def setArgs (self, args):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-args').debug3Func(): logFunc('called. args=%s, old=%s', args, self.args)
        self.argsSet = True
        self.args = args

    def requestValgrind (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-valgrind').debug3Func(): logFunc('called. requested=%s', requested)
        self.valgrindRequested = requested
        self.valgrindSet = False

    def isValgrindRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-valgrind-requested').debug3Func(): logFunc('called. requested=%s', self.valgrindRequested)
        return self.valgrindRequested

    def getValgrind (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-valgrind').debug3Func(): logFunc('called. self.valgrindSet=%s, self.valgrind=%s', self.valgrindSet, self.valgrind)
        if self.valgrindSet:
            return self.valgrind
        return None

    def hasValgrind (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-valgrind').debug3Func(): logFunc('called. self.valgrindSet=%s, self.valgrind=%s', self.valgrindSet, self.valgrind)
        if self.valgrindSet:
            return True
        return False

    def setValgrind (self, valgrind):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-valgrind').debug3Func(): logFunc('called. valgrind=%s, old=%s', valgrind, self.valgrind)
        self.valgrindSet = True
        self.valgrind = valgrind


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.executable = 0
        self.executableSet = False
        
        self.shell = 0
        self.shellSet = False
        
        self.extraArgs = 0
        self.extraArgsSet = False
        
        self.args = 0
        self.argsSet = False
        
        self.valgrind = 0
        self.valgrindSet = False
        

    def _getSelfKeyPath (self, process
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("command", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", "qt-proc"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("execution", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", "qt-proc"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(process);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("process", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", "qt-proc"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        process, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(process, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(process, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       process, 
                       
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

        keyPath = self._getSelfKeyPath(process, 
                                       
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
                               process, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasExecutable():
            valExecutable = Value()
            if self.executable is not None:
                valExecutable.setString(self.executable)
            else:
                valExecutable.setEmpty()
            tagValueList.push(("executable", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"), valExecutable)
        
        if self.hasShell():
            valShell = Value()
            if self.shell is not None:
                valShell.setBool(self.shell)
            else:
                valShell.setEmpty()
            tagValueList.push(("shell", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"), valShell)
        
        if self.hasExtraArgs():
            valExtraArgs = Value()
            if self.extraArgs is not None:
                valExtraArgs.setString(self.extraArgs)
            else:
                valExtraArgs.setEmpty()
            tagValueList.push(("extra-args", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"), valExtraArgs)
        
        if self.hasArgs():
            valArgs = Value()
            if self.args is not None:
                valArgs.setString(self.args)
            else:
                valArgs.setEmpty()
            tagValueList.push(("args", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"), valArgs)
        
        if self.hasValgrind():
            valValgrind = Value()
            if self.valgrind is not None:
                valValgrind.setBool(self.valgrind)
            else:
                valValgrind.setEmpty()
            tagValueList.push(("valgrind", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"), valValgrind)
        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isExecutableRequested():
            valExecutable = Value()
            valExecutable.setEmpty()
            tagValueList.push(("executable", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"), valExecutable)
        
        if self.isShellRequested():
            valShell = Value()
            valShell.setEmpty()
            tagValueList.push(("shell", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"), valShell)
        
        if self.isExtraArgsRequested():
            valExtraArgs = Value()
            valExtraArgs.setEmpty()
            tagValueList.push(("extra-args", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"), valExtraArgs)
        
        if self.isArgsRequested():
            valArgs = Value()
            valArgs.setEmpty()
            tagValueList.push(("args", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"), valArgs)
        
        if self.isValgrindRequested():
            valValgrind = Value()
            valValgrind.setEmpty()
            tagValueList.push(("valgrind", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"), valValgrind)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isExecutableRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "executable") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-executable').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "executable", "executable", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-executable-bad-value').infoFunc(): logFunc('executable not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setExecutable(tempVar)
            for logFunc in self._log('read-tag-values-executable').debug3Func(): logFunc('read executable. executable=%s, tempValue=%s', self.executable, tempValue.getType())
        
        if self.isShellRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "shell") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-shell').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "shell", "shell", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-shell-bad-value').infoFunc(): logFunc('shell not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setShell(tempVar)
            for logFunc in self._log('read-tag-values-shell').debug3Func(): logFunc('read shell. shell=%s, tempValue=%s', self.shell, tempValue.getType())
        
        if self.isExtraArgsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "extra-args") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-extraargs').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "extraArgs", "extra-args", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-extra-args-bad-value').infoFunc(): logFunc('extraArgs not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setExtraArgs(tempVar)
            for logFunc in self._log('read-tag-values-extra-args').debug3Func(): logFunc('read extraArgs. extraArgs=%s, tempValue=%s', self.extraArgs, tempValue.getType())
        
        if self.isArgsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "args") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-args').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "args", "args", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-args-bad-value').infoFunc(): logFunc('args not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setArgs(tempVar)
            for logFunc in self._log('read-tag-values-args').debug3Func(): logFunc('read args. args=%s, tempValue=%s', self.args, tempValue.getType())
        
        if self.isValgrindRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "valgrind") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-valgrind').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "valgrind", "valgrind", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-valgrind-bad-value').infoFunc(): logFunc('valgrind not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setValgrind(tempVar)
            for logFunc in self._log('read-tag-values-valgrind').debug3Func(): logFunc('read valgrind. valgrind=%s, tempValue=%s', self.valgrind, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "command", 
        "namespace": "command", 
        "className": "CommandMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_process.tech.process.execution.command.command_maapi_gen import CommandMaapi", 
        "baseClassName": "CommandMaapiBase", 
        "baseModule": "command_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-proc", 
            "isCurrent": false, 
            "yangName": "process", 
            "namespace": "process", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "keyLeaf": {
                "varName": "process", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "process"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-proc", 
            "yangName": "execution", 
            "namespace": "execution", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "name": "execution"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-proc", 
            "yangName": "command", 
            "namespace": "command", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "name": "command"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "executable", 
            "yangName": "executable", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "shell", 
            "yangName": "shell", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "extraArgs", 
            "yangName": "extra-args", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "args", 
            "yangName": "args", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "valgrind", 
            "yangName": "valgrind", 
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
            "qwilt_tech_process"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "executable", 
            "yangName": "executable", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "shell", 
            "yangName": "shell", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "extraArgs", 
            "yangName": "extra-args", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "args", 
            "yangName": "args", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "valgrind", 
            "yangName": "valgrind", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


