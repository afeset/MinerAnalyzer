


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

from prediction_maapi_base_gen import PredictionMaapiBase




class BlinkyPredictionMaapi(PredictionMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-prediction")
        self.domain = None

        

        
        self.estimatedDeliveryTrxPerConnectionRequested = False
        self.estimatedDeliveryTrxPerConnection = None
        self.estimatedDeliveryTrxPerConnectionSet = False
        
        self.simulatedDiskSizeGbRequested = False
        self.simulatedDiskSizeGb = None
        self.simulatedDiskSizeGbSet = False
        
        self.deliveryMaxActiveConnectionsRequested = False
        self.deliveryMaxActiveConnections = None
        self.deliveryMaxActiveConnectionsSet = False
        
        self.enabledRequested = False
        self.enabled = None
        self.enabledSet = False
        
        self.deliveryMaxBwMbpsRequested = False
        self.deliveryMaxBwMbps = None
        self.deliveryMaxBwMbpsSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestEstimatedDeliveryTrxPerConnection(True)
        
        self.requestSimulatedDiskSizeGb(True)
        
        self.requestDeliveryMaxActiveConnections(True)
        
        self.requestEnabled(True)
        
        self.requestDeliveryMaxBwMbps(True)
        
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestEstimatedDeliveryTrxPerConnection(True)
        
        self.requestSimulatedDiskSizeGb(True)
        
        self.requestDeliveryMaxActiveConnections(True)
        
        self.requestEnabled(True)
        
        self.requestDeliveryMaxBwMbps(True)
        
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestEstimatedDeliveryTrxPerConnection(False)
        
        self.requestSimulatedDiskSizeGb(False)
        
        self.requestDeliveryMaxActiveConnections(False)
        
        self.requestEnabled(False)
        
        self.requestDeliveryMaxBwMbps(False)
        
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestEstimatedDeliveryTrxPerConnection(False)
        
        self.requestSimulatedDiskSizeGb(False)
        
        self.requestDeliveryMaxActiveConnections(False)
        
        self.requestEnabled(False)
        
        self.requestDeliveryMaxBwMbps(False)
        
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setEstimatedDeliveryTrxPerConnection(None)
        self.estimatedDeliveryTrxPerConnectionSet = False
        
        self.setSimulatedDiskSizeGb(None)
        self.simulatedDiskSizeGbSet = False
        
        self.setDeliveryMaxActiveConnections(None)
        self.deliveryMaxActiveConnectionsSet = False
        
        self.setEnabled(None)
        self.enabledSet = False
        
        self.setDeliveryMaxBwMbps(None)
        self.deliveryMaxBwMbpsSet = False
        
        

    def write (self
              , line
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(line, trxContext)

    def read (self
              , line
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(line, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , line
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(line, 
                                  True,
                                  trxContext)



    def requestEstimatedDeliveryTrxPerConnection (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-estimateddeliverytrxperconnection').debug3Func(): logFunc('called. requested=%s', requested)
        self.estimatedDeliveryTrxPerConnectionRequested = requested
        self.estimatedDeliveryTrxPerConnectionSet = False

    def isEstimatedDeliveryTrxPerConnectionRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-estimateddeliverytrxperconnection-requested').debug3Func(): logFunc('called. requested=%s', self.estimatedDeliveryTrxPerConnectionRequested)
        return self.estimatedDeliveryTrxPerConnectionRequested

    def getEstimatedDeliveryTrxPerConnection (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-estimateddeliverytrxperconnection').debug3Func(): logFunc('called. self.estimatedDeliveryTrxPerConnectionSet=%s, self.estimatedDeliveryTrxPerConnection=%s', self.estimatedDeliveryTrxPerConnectionSet, self.estimatedDeliveryTrxPerConnection)
        if self.estimatedDeliveryTrxPerConnectionSet:
            return self.estimatedDeliveryTrxPerConnection
        return None

    def hasEstimatedDeliveryTrxPerConnection (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-estimateddeliverytrxperconnection').debug3Func(): logFunc('called. self.estimatedDeliveryTrxPerConnectionSet=%s, self.estimatedDeliveryTrxPerConnection=%s', self.estimatedDeliveryTrxPerConnectionSet, self.estimatedDeliveryTrxPerConnection)
        if self.estimatedDeliveryTrxPerConnectionSet:
            return True
        return False

    def setEstimatedDeliveryTrxPerConnection (self, estimatedDeliveryTrxPerConnection):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-estimateddeliverytrxperconnection').debug3Func(): logFunc('called. estimatedDeliveryTrxPerConnection=%s, old=%s', estimatedDeliveryTrxPerConnection, self.estimatedDeliveryTrxPerConnection)
        self.estimatedDeliveryTrxPerConnectionSet = True
        self.estimatedDeliveryTrxPerConnection = estimatedDeliveryTrxPerConnection

    def requestSimulatedDiskSizeGb (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-simulateddisksizegb').debug3Func(): logFunc('called. requested=%s', requested)
        self.simulatedDiskSizeGbRequested = requested
        self.simulatedDiskSizeGbSet = False

    def isSimulatedDiskSizeGbRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-simulateddisksizegb-requested').debug3Func(): logFunc('called. requested=%s', self.simulatedDiskSizeGbRequested)
        return self.simulatedDiskSizeGbRequested

    def getSimulatedDiskSizeGb (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-simulateddisksizegb').debug3Func(): logFunc('called. self.simulatedDiskSizeGbSet=%s, self.simulatedDiskSizeGb=%s', self.simulatedDiskSizeGbSet, self.simulatedDiskSizeGb)
        if self.simulatedDiskSizeGbSet:
            return self.simulatedDiskSizeGb
        return None

    def hasSimulatedDiskSizeGb (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-simulateddisksizegb').debug3Func(): logFunc('called. self.simulatedDiskSizeGbSet=%s, self.simulatedDiskSizeGb=%s', self.simulatedDiskSizeGbSet, self.simulatedDiskSizeGb)
        if self.simulatedDiskSizeGbSet:
            return True
        return False

    def setSimulatedDiskSizeGb (self, simulatedDiskSizeGb):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-simulateddisksizegb').debug3Func(): logFunc('called. simulatedDiskSizeGb=%s, old=%s', simulatedDiskSizeGb, self.simulatedDiskSizeGb)
        self.simulatedDiskSizeGbSet = True
        self.simulatedDiskSizeGb = simulatedDiskSizeGb

    def requestDeliveryMaxActiveConnections (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-deliverymaxactiveconnections').debug3Func(): logFunc('called. requested=%s', requested)
        self.deliveryMaxActiveConnectionsRequested = requested
        self.deliveryMaxActiveConnectionsSet = False

    def isDeliveryMaxActiveConnectionsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-deliverymaxactiveconnections-requested').debug3Func(): logFunc('called. requested=%s', self.deliveryMaxActiveConnectionsRequested)
        return self.deliveryMaxActiveConnectionsRequested

    def getDeliveryMaxActiveConnections (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-deliverymaxactiveconnections').debug3Func(): logFunc('called. self.deliveryMaxActiveConnectionsSet=%s, self.deliveryMaxActiveConnections=%s', self.deliveryMaxActiveConnectionsSet, self.deliveryMaxActiveConnections)
        if self.deliveryMaxActiveConnectionsSet:
            return self.deliveryMaxActiveConnections
        return None

    def hasDeliveryMaxActiveConnections (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-deliverymaxactiveconnections').debug3Func(): logFunc('called. self.deliveryMaxActiveConnectionsSet=%s, self.deliveryMaxActiveConnections=%s', self.deliveryMaxActiveConnectionsSet, self.deliveryMaxActiveConnections)
        if self.deliveryMaxActiveConnectionsSet:
            return True
        return False

    def setDeliveryMaxActiveConnections (self, deliveryMaxActiveConnections):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-deliverymaxactiveconnections').debug3Func(): logFunc('called. deliveryMaxActiveConnections=%s, old=%s', deliveryMaxActiveConnections, self.deliveryMaxActiveConnections)
        self.deliveryMaxActiveConnectionsSet = True
        self.deliveryMaxActiveConnections = deliveryMaxActiveConnections

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

    def requestDeliveryMaxBwMbps (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-deliverymaxbwmbps').debug3Func(): logFunc('called. requested=%s', requested)
        self.deliveryMaxBwMbpsRequested = requested
        self.deliveryMaxBwMbpsSet = False

    def isDeliveryMaxBwMbpsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-deliverymaxbwmbps-requested').debug3Func(): logFunc('called. requested=%s', self.deliveryMaxBwMbpsRequested)
        return self.deliveryMaxBwMbpsRequested

    def getDeliveryMaxBwMbps (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-deliverymaxbwmbps').debug3Func(): logFunc('called. self.deliveryMaxBwMbpsSet=%s, self.deliveryMaxBwMbps=%s', self.deliveryMaxBwMbpsSet, self.deliveryMaxBwMbps)
        if self.deliveryMaxBwMbpsSet:
            return self.deliveryMaxBwMbps
        return None

    def hasDeliveryMaxBwMbps (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-deliverymaxbwmbps').debug3Func(): logFunc('called. self.deliveryMaxBwMbpsSet=%s, self.deliveryMaxBwMbps=%s', self.deliveryMaxBwMbpsSet, self.deliveryMaxBwMbps)
        if self.deliveryMaxBwMbpsSet:
            return True
        return False

    def setDeliveryMaxBwMbps (self, deliveryMaxBwMbps):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-deliverymaxbwmbps').debug3Func(): logFunc('called. deliveryMaxBwMbps=%s, old=%s', deliveryMaxBwMbps, self.deliveryMaxBwMbps)
        self.deliveryMaxBwMbpsSet = True
        self.deliveryMaxBwMbps = deliveryMaxBwMbps


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.estimatedDeliveryTrxPerConnection = 0
        self.estimatedDeliveryTrxPerConnectionSet = False
        
        self.simulatedDiskSizeGb = 0
        self.simulatedDiskSizeGbSet = False
        
        self.deliveryMaxActiveConnections = 0
        self.deliveryMaxActiveConnectionsSet = False
        
        self.enabled = 0
        self.enabledSet = False
        
        self.deliveryMaxBwMbps = 0
        self.deliveryMaxBwMbpsSet = False
        

    def _getSelfKeyPath (self, line
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("prediction", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("analyzer", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(line);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("line", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line"))
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
                        line, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(line, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(line, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       line, 
                       
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

        keyPath = self._getSelfKeyPath(line, 
                                       
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
                               line, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasEstimatedDeliveryTrxPerConnection():
            valEstimatedDeliveryTrxPerConnection = Value()
            if self.estimatedDeliveryTrxPerConnection is not None:
                valEstimatedDeliveryTrxPerConnection.setInt64(self.estimatedDeliveryTrxPerConnection)
            else:
                valEstimatedDeliveryTrxPerConnection.setEmpty()
            tagValueList.push(("estimated-delivery-trx-per-connection", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valEstimatedDeliveryTrxPerConnection)
        
        if self.hasSimulatedDiskSizeGb():
            valSimulatedDiskSizeGb = Value()
            if self.simulatedDiskSizeGb is not None:
                valSimulatedDiskSizeGb.setInt64(self.simulatedDiskSizeGb)
            else:
                valSimulatedDiskSizeGb.setEmpty()
            tagValueList.push(("simulated-disk-size-gb", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valSimulatedDiskSizeGb)
        
        if self.hasDeliveryMaxActiveConnections():
            valDeliveryMaxActiveConnections = Value()
            if self.deliveryMaxActiveConnections is not None:
                valDeliveryMaxActiveConnections.setInt64(self.deliveryMaxActiveConnections)
            else:
                valDeliveryMaxActiveConnections.setEmpty()
            tagValueList.push(("delivery-max-active-connections", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valDeliveryMaxActiveConnections)
        
        if self.hasEnabled():
            valEnabled = Value()
            if self.enabled is not None:
                valEnabled.setBool(self.enabled)
            else:
                valEnabled.setEmpty()
            tagValueList.push(("enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valEnabled)
        
        if self.hasDeliveryMaxBwMbps():
            valDeliveryMaxBwMbps = Value()
            if self.deliveryMaxBwMbps is not None:
                valDeliveryMaxBwMbps.setInt64(self.deliveryMaxBwMbps)
            else:
                valDeliveryMaxBwMbps.setEmpty()
            tagValueList.push(("delivery-max-bw-mbps", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valDeliveryMaxBwMbps)
        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isEstimatedDeliveryTrxPerConnectionRequested():
            valEstimatedDeliveryTrxPerConnection = Value()
            valEstimatedDeliveryTrxPerConnection.setEmpty()
            tagValueList.push(("estimated-delivery-trx-per-connection", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valEstimatedDeliveryTrxPerConnection)
        
        if self.isSimulatedDiskSizeGbRequested():
            valSimulatedDiskSizeGb = Value()
            valSimulatedDiskSizeGb.setEmpty()
            tagValueList.push(("simulated-disk-size-gb", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valSimulatedDiskSizeGb)
        
        if self.isDeliveryMaxActiveConnectionsRequested():
            valDeliveryMaxActiveConnections = Value()
            valDeliveryMaxActiveConnections.setEmpty()
            tagValueList.push(("delivery-max-active-connections", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valDeliveryMaxActiveConnections)
        
        if self.isEnabledRequested():
            valEnabled = Value()
            valEnabled.setEmpty()
            tagValueList.push(("enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valEnabled)
        
        if self.isDeliveryMaxBwMbpsRequested():
            valDeliveryMaxBwMbps = Value()
            valDeliveryMaxBwMbps.setEmpty()
            tagValueList.push(("delivery-max-bw-mbps", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valDeliveryMaxBwMbps)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isEstimatedDeliveryTrxPerConnectionRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "estimated-delivery-trx-per-connection") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-estimateddeliverytrxperconnection').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "estimatedDeliveryTrxPerConnection", "estimated-delivery-trx-per-connection", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-estimated-delivery-trx-per-connection-bad-value').infoFunc(): logFunc('estimatedDeliveryTrxPerConnection not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setEstimatedDeliveryTrxPerConnection(tempVar)
            for logFunc in self._log('read-tag-values-estimated-delivery-trx-per-connection').debug3Func(): logFunc('read estimatedDeliveryTrxPerConnection. estimatedDeliveryTrxPerConnection=%s, tempValue=%s', self.estimatedDeliveryTrxPerConnection, tempValue.getType())
        
        if self.isSimulatedDiskSizeGbRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "simulated-disk-size-gb") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-simulateddisksizegb').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "simulatedDiskSizeGb", "simulated-disk-size-gb", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-simulated-disk-size-gb-bad-value').infoFunc(): logFunc('simulatedDiskSizeGb not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setSimulatedDiskSizeGb(tempVar)
            for logFunc in self._log('read-tag-values-simulated-disk-size-gb').debug3Func(): logFunc('read simulatedDiskSizeGb. simulatedDiskSizeGb=%s, tempValue=%s', self.simulatedDiskSizeGb, tempValue.getType())
        
        if self.isDeliveryMaxActiveConnectionsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "delivery-max-active-connections") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-deliverymaxactiveconnections').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "deliveryMaxActiveConnections", "delivery-max-active-connections", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-delivery-max-active-connections-bad-value').infoFunc(): logFunc('deliveryMaxActiveConnections not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setDeliveryMaxActiveConnections(tempVar)
            for logFunc in self._log('read-tag-values-delivery-max-active-connections').debug3Func(): logFunc('read deliveryMaxActiveConnections. deliveryMaxActiveConnections=%s, tempValue=%s', self.deliveryMaxActiveConnections, tempValue.getType())
        
        if self.isEnabledRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "enabled") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-enabled').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "enabled", "enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
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
        
        if self.isDeliveryMaxBwMbpsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "delivery-max-bw-mbps") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-deliverymaxbwmbps').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "deliveryMaxBwMbps", "delivery-max-bw-mbps", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-delivery-max-bw-mbps-bad-value').infoFunc(): logFunc('deliveryMaxBwMbps not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setDeliveryMaxBwMbps(tempVar)
            for logFunc in self._log('read-tag-values-delivery-max-bw-mbps').debug3Func(): logFunc('read deliveryMaxBwMbps. deliveryMaxBwMbps=%s, tempValue=%s', self.deliveryMaxBwMbps, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "prediction", 
        "namespace": "prediction", 
        "className": "PredictionMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.system_defaults.analyzer.prediction.prediction_maapi_gen import PredictionMaapi", 
        "baseClassName": "PredictionMaapiBase", 
        "baseModule": "prediction_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qtc-line", 
            "isCurrent": false, 
            "yangName": "line", 
            "namespace": "line", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "keyLeaf": {
                "varName": "line", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "line"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "system-defaults"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "yangName": "analyzer", 
            "namespace": "analyzer", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "analyzer"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "yangName": "prediction", 
            "namespace": "prediction", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "prediction"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "estimatedDeliveryTrxPerConnection", 
            "yangName": "estimated-delivery-trx-per-connection", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "simulatedDiskSizeGb", 
            "yangName": "simulated-disk-size-gb", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "deliveryMaxActiveConnections", 
            "yangName": "delivery-max-active-connections", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "deliveryMaxBwMbps", 
            "yangName": "delivery-max-bw-mbps", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
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
            "content", 
            "qwilt_tech_content_line"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "estimatedDeliveryTrxPerConnection", 
            "yangName": "estimated-delivery-trx-per-connection", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "simulatedDiskSizeGb", 
            "yangName": "simulated-disk-size-gb", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "deliveryMaxActiveConnections", 
            "yangName": "delivery-max-active-connections", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "deliveryMaxBwMbps", 
            "yangName": "delivery-max-bw-mbps", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


