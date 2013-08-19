


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

from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.destination.system_defaults.output.output_maapi_gen import BlinkyOutputMaapi
from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.destination.system_defaults.format.format_maapi_gen import BlinkyFormatMaapi

from a.api.yang.modules.tech.debug.qwilt_tech_debug.qwilt_tech_debug_module_gen import LogSeverity
from a.api.yang.modules.tech.debug.qwilt_tech_debug.qwilt_tech_debug_module_gen import DestinationType


class BlinkySystemDefaultsMaapi(SystemDefaultsMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-systemDefaults")
        self.domain = None

        
        self.outputObj = None
        
        self.formatObj = None
        

        
        self.minLevelRequested = False
        self.minLevel = None
        self.minLevelSet = False
        
        self.destinationTypeRequested = False
        self.destinationType = None
        self.destinationTypeSet = False
        
        self.enabledRequested = False
        self.enabled = None
        self.enabledSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestMinLevel(True)
        
        self.requestDestinationType(True)
        
        self.requestEnabled(True)
        
        
        
        if not self.outputObj:
            self.outputObj = self.newOutput()
            self.outputObj.requestConfigAndOper()
        
        if not self.formatObj:
            self.formatObj = self.newFormat()
            self.formatObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestMinLevel(True)
        
        self.requestDestinationType(True)
        
        self.requestEnabled(True)
        
        
        
        if not self.outputObj:
            self.outputObj = self.newOutput()
            self.outputObj.requestConfig()
        
        if not self.formatObj:
            self.formatObj = self.newFormat()
            self.formatObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestMinLevel(False)
        
        self.requestDestinationType(False)
        
        self.requestEnabled(False)
        
        
        
        if not self.outputObj:
            self.outputObj = self.newOutput()
            self.outputObj.requestOper()
        
        if not self.formatObj:
            self.formatObj = self.newFormat()
            self.formatObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestMinLevel(False)
        
        self.requestDestinationType(False)
        
        self.requestEnabled(False)
        
        
        
        if not self.outputObj:
            self.outputObj = self.newOutput()
            self.outputObj.clearAllRequested()
        
        if not self.formatObj:
            self.formatObj = self.newFormat()
            self.formatObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setMinLevel(None)
        self.minLevelSet = False
        
        self.setDestinationType(None)
        self.destinationTypeSet = False
        
        self.setEnabled(None)
        self.enabledSet = False
        
        
        if self.outputObj:
            self.outputObj.clearAllSet()
        
        if self.formatObj:
            self.formatObj.clearAllSet()
        

    def write (self
              , loggerClass
              , instance
              , destination
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(loggerClass, instance, destination, trxContext)

    def read (self
              , loggerClass
              , instance
              , destination
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(loggerClass, instance, destination, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , loggerClass
                       , instance
                       , destination
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(loggerClass, instance, destination, 
                                  True,
                                  trxContext)

    def newOutput (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-output').debug3Func(): logFunc('called.')
        output = BlinkyOutputMaapi(self._log)
        output.init(self.domain)
        return output

    def setOutputObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-output').debug3Func(): logFunc('called. obj=%s', obj)
        self.outputObj = obj

    def getOutputObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-output').debug3Func(): logFunc('called. self.outputObj=%s', self.outputObj)
        return self.outputObj

    def hasOutput (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-output').debug3Func(): logFunc('called. self.outputObj=%s', self.outputObj)
        if self.outputObj:
            return True
        return False

    def newFormat (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-format').debug3Func(): logFunc('called.')
        format = BlinkyFormatMaapi(self._log)
        format.init(self.domain)
        return format

    def setFormatObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-format').debug3Func(): logFunc('called. obj=%s', obj)
        self.formatObj = obj

    def getFormatObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-format').debug3Func(): logFunc('called. self.formatObj=%s', self.formatObj)
        return self.formatObj

    def hasFormat (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-format').debug3Func(): logFunc('called. self.formatObj=%s', self.formatObj)
        if self.formatObj:
            return True
        return False



    def requestMinLevel (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-minlevel').debug3Func(): logFunc('called. requested=%s', requested)
        self.minLevelRequested = requested
        self.minLevelSet = False

    def isMinLevelRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-minlevel-requested').debug3Func(): logFunc('called. requested=%s', self.minLevelRequested)
        return self.minLevelRequested

    def getMinLevel (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-minlevel').debug3Func(): logFunc('called. self.minLevelSet=%s, self.minLevel=%s', self.minLevelSet, self.minLevel)
        if self.minLevelSet:
            return self.minLevel
        return None

    def hasMinLevel (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-minlevel').debug3Func(): logFunc('called. self.minLevelSet=%s, self.minLevel=%s', self.minLevelSet, self.minLevel)
        if self.minLevelSet:
            return True
        return False

    def setMinLevel (self, minLevel):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-minlevel').debug3Func(): logFunc('called. minLevel=%s, old=%s', minLevel, self.minLevel)
        self.minLevelSet = True
        self.minLevel = minLevel

    def requestDestinationType (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-destinationtype').debug3Func(): logFunc('called. requested=%s', requested)
        self.destinationTypeRequested = requested
        self.destinationTypeSet = False

    def isDestinationTypeRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-destinationtype-requested').debug3Func(): logFunc('called. requested=%s', self.destinationTypeRequested)
        return self.destinationTypeRequested

    def getDestinationType (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-destinationtype').debug3Func(): logFunc('called. self.destinationTypeSet=%s, self.destinationType=%s', self.destinationTypeSet, self.destinationType)
        if self.destinationTypeSet:
            return self.destinationType
        return None

    def hasDestinationType (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-destinationtype').debug3Func(): logFunc('called. self.destinationTypeSet=%s, self.destinationType=%s', self.destinationTypeSet, self.destinationType)
        if self.destinationTypeSet:
            return True
        return False

    def setDestinationType (self, destinationType):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-destinationtype').debug3Func(): logFunc('called. destinationType=%s, old=%s', destinationType, self.destinationType)
        self.destinationTypeSet = True
        self.destinationType = destinationType

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


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.outputObj:
            self.outputObj._clearAllReadData()
        
        if self.formatObj:
            self.formatObj._clearAllReadData()
        

        
        self.minLevel = 0
        self.minLevelSet = False
        
        self.destinationType = 0
        self.destinationTypeSet = False
        
        self.enabled = 0
        self.enabledSet = False
        

    def _getSelfKeyPath (self, loggerClass
                         , instance
                         , destination
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(destination);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("destination", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug"))
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
                        destination, 
                        
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
                                         destination, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(loggerClass, 
                                       instance, 
                                       destination, 
                                       
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
                       destination, 
                       
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
                                       destination, 
                                       
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
                               destination, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        
        if self.outputObj:
            res = self.outputObj._collectItemsToDelete(loggerClass, 
                                                                          instance, 
                                                                          destination, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-output-failed').errorFunc(): logFunc('outputObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.formatObj:
            res = self.formatObj._collectItemsToDelete(loggerClass, 
                                                                          instance, 
                                                                          destination, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-format-failed').errorFunc(): logFunc('formatObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasMinLevel():
            valMinLevel = Value()
            if self.minLevel is not None:
                valMinLevel.setEnum(self.minLevel.getValue())
            else:
                valMinLevel.setEmpty()
            tagValueList.push(("min-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valMinLevel)
        
        if self.hasDestinationType():
            valDestinationType = Value()
            if self.destinationType is not None:
                valDestinationType.setEnum(self.destinationType.getValue())
            else:
                valDestinationType.setEmpty()
            tagValueList.push(("type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valDestinationType)
        
        if self.hasEnabled():
            valEnabled = Value()
            if self.enabled is not None:
                valEnabled.setBool(self.enabled)
            else:
                valEnabled.setEmpty()
            tagValueList.push(("enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valEnabled)
        

        
        if self.outputObj:
            valBegin = Value()
            (tag, ns, prefix) = ("output" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.outputObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-output-failed').errorFunc(): logFunc('outputObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.formatObj:
            valBegin = Value()
            (tag, ns, prefix) = ("format" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.formatObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-format-failed').errorFunc(): logFunc('formatObj._fillWriteTagValues() failed. PARAMS')
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

        
        if self.isMinLevelRequested():
            valMinLevel = Value()
            valMinLevel.setEmpty()
            tagValueList.push(("min-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valMinLevel)
        
        if self.isDestinationTypeRequested():
            valDestinationType = Value()
            valDestinationType.setEmpty()
            tagValueList.push(("type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valDestinationType)
        
        if self.isEnabledRequested():
            valEnabled = Value()
            valEnabled.setEmpty()
            tagValueList.push(("enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valEnabled)
        

        
        if self.outputObj:
            valBegin = Value()
            (tag, ns, prefix) = ("output" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.outputObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-output-failed').errorFunc(): logFunc('outputObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.formatObj:
            valBegin = Value()
            (tag, ns, prefix) = ("format" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.formatObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-format-failed').errorFunc(): logFunc('formatObj._fillReadTagValues() failed. PARAMS')
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
        
        if self.isMinLevelRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "min-level") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-minlevel').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "minLevel", "min-level", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-min-level-bad-value').infoFunc(): logFunc('minLevel not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMinLevel(tempVar)
            for logFunc in self._log('read-tag-values-min-level').debug3Func(): logFunc('read minLevel. minLevel=%s, tempValue=%s', self.minLevel, tempValue.getType())
        
        if self.isDestinationTypeRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "type") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-destinationtype').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "destinationType", "type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-type-bad-value').infoFunc(): logFunc('destinationType not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setDestinationType(tempVar)
            for logFunc in self._log('read-tag-values-type').debug3Func(): logFunc('read destinationType. destinationType=%s, tempValue=%s', self.destinationType, tempValue.getType())
        
        if self.isEnabledRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "enabled") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-enabled').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "enabled", "enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
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
        

        
        if self.outputObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "output") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "output", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.outputObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-output-failed').errorFunc(): logFunc('outputObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "output") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "output", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.formatObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "format") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "format", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.formatObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-format-failed').errorFunc(): logFunc('formatObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "format") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "format", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "systemDefaults", 
        "namespace": "system_defaults", 
        "className": "SystemDefaultsMaapi", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.destination.system_defaults.system_defaults_maapi_gen import SystemDefaultsMaapi", 
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
            "yangName": "destination", 
            "namespace": "destination", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "keyLeaf": {
                "varName": "destination", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "destination"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-debug", 
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "name": "system-defaults"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-debug", 
            "memberName": "output", 
            "yangName": "output", 
            "className": "BlinkyOutputMaapi", 
            "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.destination.system_defaults.output.output_maapi_gen import BlinkyOutputMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-debug", 
            "memberName": "format", 
            "yangName": "format", 
            "className": "BlinkyFormatMaapi", 
            "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.destination.system_defaults.format.format_maapi_gen import BlinkyFormatMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "minLevel", 
            "yangName": "min-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "any", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "destinationType", 
            "yangName": "type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "text", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
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
            "memberName": "minLevel", 
            "yangName": "min-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "any", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "destinationType", 
            "yangName": "type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "text", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


