


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

from delivery_maapi_base_gen import DeliveryMaapiBase

from a.api.yang.modules.tech.content.qwilt_tech_content_interfaces.tech.content.interfaces.interface.delivery.ipv4.ipv4_maapi_gen import BlinkyIpv4Maapi
from a.api.yang.modules.tech.content.qwilt_tech_content_interfaces.tech.content.interfaces.interface.delivery.ipv6.ipv6_maapi_gen import BlinkyIpv6Maapi



class BlinkyDeliveryMaapi(DeliveryMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-delivery")
        self.domain = None

        
        self.ipv4Obj = None
        
        self.ipv6Obj = None
        

        
        self.preferredDeliveryInterfaceRequested = False
        self.preferredDeliveryInterface = None
        self.preferredDeliveryInterfaceSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestPreferredDeliveryInterface(True)
        
        
        
        if not self.ipv4Obj:
            self.ipv4Obj = self.newIpv4()
            self.ipv4Obj.requestConfigAndOper()
        
        if not self.ipv6Obj:
            self.ipv6Obj = self.newIpv6()
            self.ipv6Obj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestPreferredDeliveryInterface(True)
        
        
        
        if not self.ipv4Obj:
            self.ipv4Obj = self.newIpv4()
            self.ipv4Obj.requestConfig()
        
        if not self.ipv6Obj:
            self.ipv6Obj = self.newIpv6()
            self.ipv6Obj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestPreferredDeliveryInterface(False)
        
        
        
        if not self.ipv4Obj:
            self.ipv4Obj = self.newIpv4()
            self.ipv4Obj.requestOper()
        
        if not self.ipv6Obj:
            self.ipv6Obj = self.newIpv6()
            self.ipv6Obj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestPreferredDeliveryInterface(False)
        
        
        
        if not self.ipv4Obj:
            self.ipv4Obj = self.newIpv4()
            self.ipv4Obj.clearAllRequested()
        
        if not self.ipv6Obj:
            self.ipv6Obj = self.newIpv6()
            self.ipv6Obj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setPreferredDeliveryInterface(None)
        self.preferredDeliveryInterfaceSet = False
        
        
        if self.ipv4Obj:
            self.ipv4Obj.clearAllSet()
        
        if self.ipv6Obj:
            self.ipv6Obj.clearAllSet()
        

    def write (self
              , interface
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(interface, trxContext)

    def read (self
              , interface
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(interface, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , interface
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(interface, 
                                  True,
                                  trxContext)

    def newIpv4 (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-ipv4').debug3Func(): logFunc('called.')
        ipv4 = BlinkyIpv4Maapi(self._log)
        ipv4.init(self.domain)
        return ipv4

    def setIpv4Obj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-ipv4').debug3Func(): logFunc('called. obj=%s', obj)
        self.ipv4Obj = obj

    def getIpv4Obj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-ipv4').debug3Func(): logFunc('called. self.ipv4Obj=%s', self.ipv4Obj)
        return self.ipv4Obj

    def hasIpv4 (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-ipv4').debug3Func(): logFunc('called. self.ipv4Obj=%s', self.ipv4Obj)
        if self.ipv4Obj:
            return True
        return False

    def newIpv6 (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-ipv6').debug3Func(): logFunc('called.')
        ipv6 = BlinkyIpv6Maapi(self._log)
        ipv6.init(self.domain)
        return ipv6

    def setIpv6Obj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-ipv6').debug3Func(): logFunc('called. obj=%s', obj)
        self.ipv6Obj = obj

    def getIpv6Obj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-ipv6').debug3Func(): logFunc('called. self.ipv6Obj=%s', self.ipv6Obj)
        return self.ipv6Obj

    def hasIpv6 (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-ipv6').debug3Func(): logFunc('called. self.ipv6Obj=%s', self.ipv6Obj)
        if self.ipv6Obj:
            return True
        return False



    def requestPreferredDeliveryInterface (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-preferreddeliveryinterface').debug3Func(): logFunc('called. requested=%s', requested)
        self.preferredDeliveryInterfaceRequested = requested
        self.preferredDeliveryInterfaceSet = False

    def isPreferredDeliveryInterfaceRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-preferreddeliveryinterface-requested').debug3Func(): logFunc('called. requested=%s', self.preferredDeliveryInterfaceRequested)
        return self.preferredDeliveryInterfaceRequested

    def getPreferredDeliveryInterface (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-preferreddeliveryinterface').debug3Func(): logFunc('called. self.preferredDeliveryInterfaceSet=%s, self.preferredDeliveryInterface=%s', self.preferredDeliveryInterfaceSet, self.preferredDeliveryInterface)
        if self.preferredDeliveryInterfaceSet:
            return self.preferredDeliveryInterface
        return None

    def hasPreferredDeliveryInterface (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-preferreddeliveryinterface').debug3Func(): logFunc('called. self.preferredDeliveryInterfaceSet=%s, self.preferredDeliveryInterface=%s', self.preferredDeliveryInterfaceSet, self.preferredDeliveryInterface)
        if self.preferredDeliveryInterfaceSet:
            return True
        return False

    def setPreferredDeliveryInterface (self, preferredDeliveryInterface):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-preferreddeliveryinterface').debug3Func(): logFunc('called. preferredDeliveryInterface=%s, old=%s', preferredDeliveryInterface, self.preferredDeliveryInterface)
        self.preferredDeliveryInterfaceSet = True
        self.preferredDeliveryInterface = preferredDeliveryInterface


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.ipv4Obj:
            self.ipv4Obj._clearAllReadData()
        
        if self.ipv6Obj:
            self.ipv6Obj._clearAllReadData()
        

        
        self.preferredDeliveryInterface = 0
        self.preferredDeliveryInterfaceSet = False
        

    def _getSelfKeyPath (self, interface
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("delivery", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-interfaces", "qtc-if"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(interface);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("interface", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-interfaces", "qtc-if"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("interfaces", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-interfaces", "qtc-if"))
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
                        interface, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(interface, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(interface, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       interface, 
                       
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

        keyPath = self._getSelfKeyPath(interface, 
                                       
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
                               interface, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        
        if self.ipv4Obj:
            res = self.ipv4Obj._collectItemsToDelete(interface, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-ipv4-failed').errorFunc(): logFunc('ipv4Obj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.ipv6Obj:
            res = self.ipv6Obj._collectItemsToDelete(interface, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-ipv6-failed').errorFunc(): logFunc('ipv6Obj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasPreferredDeliveryInterface():
            valPreferredDeliveryInterface = Value()
            if self.preferredDeliveryInterface is not None:
                valPreferredDeliveryInterface.setString(self.preferredDeliveryInterface)
            else:
                valPreferredDeliveryInterface.setEmpty()
            tagValueList.push(("preferred-delivery-interface", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-interfaces"), valPreferredDeliveryInterface)
        

        
        if self.ipv4Obj:
            valBegin = Value()
            (tag, ns, prefix) = ("ipv4" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-interfaces", "qtc-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.ipv4Obj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-ipv4-failed').errorFunc(): logFunc('ipv4Obj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.ipv6Obj:
            valBegin = Value()
            (tag, ns, prefix) = ("ipv6" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-interfaces", "qtc-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.ipv6Obj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-ipv6-failed').errorFunc(): logFunc('ipv6Obj._fillWriteTagValues() failed. PARAMS')
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

        
        if self.isPreferredDeliveryInterfaceRequested():
            valPreferredDeliveryInterface = Value()
            valPreferredDeliveryInterface.setEmpty()
            tagValueList.push(("preferred-delivery-interface", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-interfaces"), valPreferredDeliveryInterface)
        

        
        if self.ipv4Obj:
            valBegin = Value()
            (tag, ns, prefix) = ("ipv4" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-interfaces", "qtc-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.ipv4Obj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-ipv4-failed').errorFunc(): logFunc('ipv4Obj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.ipv6Obj:
            valBegin = Value()
            (tag, ns, prefix) = ("ipv6" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-interfaces", "qtc-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.ipv6Obj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-ipv6-failed').errorFunc(): logFunc('ipv6Obj._fillReadTagValues() failed. PARAMS')
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
        
        if self.isPreferredDeliveryInterfaceRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "preferred-delivery-interface") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-preferreddeliveryinterface').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "preferredDeliveryInterface", "preferred-delivery-interface", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-preferred-delivery-interface-bad-value').infoFunc(): logFunc('preferredDeliveryInterface not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPreferredDeliveryInterface(tempVar)
            for logFunc in self._log('read-tag-values-preferred-delivery-interface').debug3Func(): logFunc('read preferredDeliveryInterface. preferredDeliveryInterface=%s, tempValue=%s', self.preferredDeliveryInterface, tempValue.getType())
        

        
        if self.ipv4Obj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "ipv4") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-interfaces") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "ipv4", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-interfaces", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.ipv4Obj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-ipv4-failed').errorFunc(): logFunc('ipv4Obj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "ipv4") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-interfaces") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "ipv4", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-interfaces", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.ipv6Obj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "ipv6") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-interfaces") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "ipv6", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-interfaces", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.ipv6Obj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-ipv6-failed').errorFunc(): logFunc('ipv6Obj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "ipv6") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-interfaces") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "ipv6", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-interfaces", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "delivery", 
        "namespace": "delivery", 
        "className": "DeliveryMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_interfaces.tech.content.interfaces.interface.delivery.delivery_maapi_gen import DeliveryMaapi", 
        "baseClassName": "DeliveryMaapiBase", 
        "baseModule": "delivery_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qtc-if", 
            "yangName": "interfaces", 
            "namespace": "interfaces", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-interfaces", 
            "name": "interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-if", 
            "isCurrent": false, 
            "yangName": "interface", 
            "namespace": "interface", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-interfaces", 
            "keyLeaf": {
                "varName": "interface", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "interface"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-if", 
            "yangName": "delivery", 
            "namespace": "delivery", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-interfaces", 
            "name": "delivery"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qtc-if", 
            "memberName": "ipv4", 
            "yangName": "ipv4", 
            "className": "BlinkyIpv4Maapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_interfaces.tech.content.interfaces.interface.delivery.ipv4.ipv4_maapi_gen import BlinkyIpv4Maapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-if", 
            "memberName": "ipv6", 
            "yangName": "ipv6", 
            "className": "BlinkyIpv6Maapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_interfaces.tech.content.interfaces.interface.delivery.ipv6.ipv6_maapi_gen import BlinkyIpv6Maapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-interfaces"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-interfaces", 
            "moduleYangNamespacePrefix": "qtc-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "preferredDeliveryInterface", 
            "yangName": "preferred-delivery-interface", 
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
            "content", 
            "qwilt_tech_content_interfaces"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-interfaces", 
            "moduleYangNamespacePrefix": "qtc-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "preferredDeliveryInterface", 
            "yangName": "preferred-delivery-interface", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }
    ], 
    "createTime": "2013"
}
"""


