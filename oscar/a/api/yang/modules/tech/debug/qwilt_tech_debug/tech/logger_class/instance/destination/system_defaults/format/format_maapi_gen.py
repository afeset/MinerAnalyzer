


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

from format_maapi_base_gen import FormatMaapiBase




class BlinkyFormatMaapi(FormatMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-format")
        self.domain = None

        

        
        self.messageExtraRequested = False
        self.messageExtra = None
        self.messageExtraSet = False
        
        self.messageBaseRequested = False
        self.messageBase = None
        self.messageBaseSet = False
        
        self.payloadRequested = False
        self.payload = None
        self.payloadSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestMessageExtra(True)
        
        self.requestMessageBase(True)
        
        self.requestPayload(True)
        
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestMessageExtra(True)
        
        self.requestMessageBase(True)
        
        self.requestPayload(True)
        
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestMessageExtra(False)
        
        self.requestMessageBase(False)
        
        self.requestPayload(False)
        
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestMessageExtra(False)
        
        self.requestMessageBase(False)
        
        self.requestPayload(False)
        
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setMessageExtra(None)
        self.messageExtraSet = False
        
        self.setMessageBase(None)
        self.messageBaseSet = False
        
        self.setPayload(None)
        self.payloadSet = False
        
        

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



    def requestMessageExtra (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-messageextra').debug3Func(): logFunc('called. requested=%s', requested)
        self.messageExtraRequested = requested
        self.messageExtraSet = False

    def isMessageExtraRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-messageextra-requested').debug3Func(): logFunc('called. requested=%s', self.messageExtraRequested)
        return self.messageExtraRequested

    def getMessageExtra (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-messageextra').debug3Func(): logFunc('called. self.messageExtraSet=%s, self.messageExtra=%s', self.messageExtraSet, self.messageExtra)
        if self.messageExtraSet:
            return self.messageExtra
        return None

    def hasMessageExtra (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-messageextra').debug3Func(): logFunc('called. self.messageExtraSet=%s, self.messageExtra=%s', self.messageExtraSet, self.messageExtra)
        if self.messageExtraSet:
            return True
        return False

    def setMessageExtra (self, messageExtra):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-messageextra').debug3Func(): logFunc('called. messageExtra=%s, old=%s', messageExtra, self.messageExtra)
        self.messageExtraSet = True
        self.messageExtra = messageExtra

    def requestMessageBase (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-messagebase').debug3Func(): logFunc('called. requested=%s', requested)
        self.messageBaseRequested = requested
        self.messageBaseSet = False

    def isMessageBaseRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-messagebase-requested').debug3Func(): logFunc('called. requested=%s', self.messageBaseRequested)
        return self.messageBaseRequested

    def getMessageBase (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-messagebase').debug3Func(): logFunc('called. self.messageBaseSet=%s, self.messageBase=%s', self.messageBaseSet, self.messageBase)
        if self.messageBaseSet:
            return self.messageBase
        return None

    def hasMessageBase (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-messagebase').debug3Func(): logFunc('called. self.messageBaseSet=%s, self.messageBase=%s', self.messageBaseSet, self.messageBase)
        if self.messageBaseSet:
            return True
        return False

    def setMessageBase (self, messageBase):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-messagebase').debug3Func(): logFunc('called. messageBase=%s, old=%s', messageBase, self.messageBase)
        self.messageBaseSet = True
        self.messageBase = messageBase

    def requestPayload (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-payload').debug3Func(): logFunc('called. requested=%s', requested)
        self.payloadRequested = requested
        self.payloadSet = False

    def isPayloadRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-payload-requested').debug3Func(): logFunc('called. requested=%s', self.payloadRequested)
        return self.payloadRequested

    def getPayload (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-payload').debug3Func(): logFunc('called. self.payloadSet=%s, self.payload=%s', self.payloadSet, self.payload)
        if self.payloadSet:
            return self.payload
        return None

    def hasPayload (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-payload').debug3Func(): logFunc('called. self.payloadSet=%s, self.payload=%s', self.payloadSet, self.payload)
        if self.payloadSet:
            return True
        return False

    def setPayload (self, payload):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-payload').debug3Func(): logFunc('called. payload=%s, old=%s', payload, self.payload)
        self.payloadSet = True
        self.payload = payload


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.messageExtra = 0
        self.messageExtraSet = False
        
        self.messageBase = 0
        self.messageBaseSet = False
        
        self.payload = 0
        self.payloadSet = False
        

    def _getSelfKeyPath (self, loggerClass
                         , instance
                         , destination
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("format", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
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

        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasMessageExtra():
            valMessageExtra = Value()
            if self.messageExtra is not None:
                valMessageExtra.setString(self.messageExtra)
            else:
                valMessageExtra.setEmpty()
            tagValueList.push(("message-extra", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valMessageExtra)
        
        if self.hasMessageBase():
            valMessageBase = Value()
            if self.messageBase is not None:
                valMessageBase.setString(self.messageBase)
            else:
                valMessageBase.setEmpty()
            tagValueList.push(("message-base", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valMessageBase)
        
        if self.hasPayload():
            valPayload = Value()
            if self.payload is not None:
                valPayload.setString(self.payload)
            else:
                valPayload.setEmpty()
            tagValueList.push(("payload", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valPayload)
        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isMessageExtraRequested():
            valMessageExtra = Value()
            valMessageExtra.setEmpty()
            tagValueList.push(("message-extra", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valMessageExtra)
        
        if self.isMessageBaseRequested():
            valMessageBase = Value()
            valMessageBase.setEmpty()
            tagValueList.push(("message-base", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valMessageBase)
        
        if self.isPayloadRequested():
            valPayload = Value()
            valPayload.setEmpty()
            tagValueList.push(("payload", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valPayload)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isMessageExtraRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "message-extra") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-messageextra').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "messageExtra", "message-extra", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-message-extra-bad-value').infoFunc(): logFunc('messageExtra not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMessageExtra(tempVar)
            for logFunc in self._log('read-tag-values-message-extra').debug3Func(): logFunc('read messageExtra. messageExtra=%s, tempValue=%s', self.messageExtra, tempValue.getType())
        
        if self.isMessageBaseRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "message-base") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-messagebase').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "messageBase", "message-base", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-message-base-bad-value').infoFunc(): logFunc('messageBase not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMessageBase(tempVar)
            for logFunc in self._log('read-tag-values-message-base').debug3Func(): logFunc('read messageBase. messageBase=%s, tempValue=%s', self.messageBase, tempValue.getType())
        
        if self.isPayloadRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "payload") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-payload').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "payload", "payload", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-payload-bad-value').infoFunc(): logFunc('payload not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPayload(tempVar)
            for logFunc in self._log('read-tag-values-payload').debug3Func(): logFunc('read payload. payload=%s, tempValue=%s', self.payload, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "format", 
        "namespace": "format", 
        "className": "FormatMaapi", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.destination.system_defaults.format.format_maapi_gen import FormatMaapi", 
        "baseClassName": "FormatMaapiBase", 
        "baseModule": "format_maapi_base_gen"
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
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "name": "system-defaults"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-debug", 
            "yangName": "format", 
            "namespace": "format", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "name": "format"
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
            "typeHandler": "handler: StringHandler", 
            "memberName": "messageExtra", 
            "yangName": "message-extra", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "messageBase", 
            "yangName": "message-base", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "payload", 
            "yangName": "payload", 
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
            "debug", 
            "qwilt_tech_debug"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "messageExtra", 
            "yangName": "message-extra", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "messageBase", 
            "yangName": "message-base", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "payload", 
            "yangName": "payload", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


