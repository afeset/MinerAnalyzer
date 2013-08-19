


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

from destination_maapi_base_gen import DestinationMaapiBase


from a.api.yang.modules.tech.common.qwilt_tech_snmp.qwilt_tech_snmp_module_gen import SnmpNotificationTypeType
from a.api.yang.modules.tech.common.qwilt_tech_snmp.qwilt_tech_snmp_module_gen import SnmpNotificationVersionType


class BlinkyDestinationMaapi(DestinationMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-destination")
        self.domain = None

        

        
        self.nameRequested = False
        self.name = None
        self.nameSet = False
        
        self.destinationRequested = False
        self.destination = None
        self.destinationSet = False
        
        self.communityRequested = False
        self.community = None
        self.communitySet = False
        
        self.versionRequested = False
        self.version = None
        self.versionSet = False
        
        self.type_Requested = False
        self.type_ = None
        self.type_Set = False
        
        self.portRequested = False
        self.port = None
        self.portSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestName(True)
        
        self.requestDestination(True)
        
        self.requestCommunity(True)
        
        self.requestVersion(True)
        
        self.requestType_(True)
        
        self.requestPort(True)
        
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestName(True)
        
        self.requestDestination(True)
        
        self.requestCommunity(True)
        
        self.requestVersion(True)
        
        self.requestType_(True)
        
        self.requestPort(True)
        
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestName(False)
        
        self.requestDestination(False)
        
        self.requestCommunity(False)
        
        self.requestVersion(False)
        
        self.requestType_(False)
        
        self.requestPort(False)
        
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestName(False)
        
        self.requestDestination(False)
        
        self.requestCommunity(False)
        
        self.requestVersion(False)
        
        self.requestType_(False)
        
        self.requestPort(False)
        
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setName(None)
        self.nameSet = False
        
        self.setDestination(None)
        self.destinationSet = False
        
        self.setCommunity(None)
        self.communitySet = False
        
        self.setVersion(None)
        self.versionSet = False
        
        self.setType_(None)
        self.type_Set = False
        
        self.setPort(None)
        self.portSet = False
        
        

    def write (self
              , destination
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(destination, trxContext)

    def read (self
              , destination
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(destination, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , destination
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(destination, 
                                  True,
                                  trxContext)



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

    def requestDestination (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-destination').debug3Func(): logFunc('called. requested=%s', requested)
        self.destinationRequested = requested
        self.destinationSet = False

    def isDestinationRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-destination-requested').debug3Func(): logFunc('called. requested=%s', self.destinationRequested)
        return self.destinationRequested

    def getDestination (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-destination').debug3Func(): logFunc('called. self.destinationSet=%s, self.destination=%s', self.destinationSet, self.destination)
        if self.destinationSet:
            return self.destination
        return None

    def hasDestination (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-destination').debug3Func(): logFunc('called. self.destinationSet=%s, self.destination=%s', self.destinationSet, self.destination)
        if self.destinationSet:
            return True
        return False

    def setDestination (self, destination):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-destination').debug3Func(): logFunc('called. destination=%s, old=%s', destination, self.destination)
        self.destinationSet = True
        self.destination = destination

    def requestCommunity (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-community').debug3Func(): logFunc('called. requested=%s', requested)
        self.communityRequested = requested
        self.communitySet = False

    def isCommunityRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-community-requested').debug3Func(): logFunc('called. requested=%s', self.communityRequested)
        return self.communityRequested

    def getCommunity (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-community').debug3Func(): logFunc('called. self.communitySet=%s, self.community=%s', self.communitySet, self.community)
        if self.communitySet:
            return self.community
        return None

    def hasCommunity (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-community').debug3Func(): logFunc('called. self.communitySet=%s, self.community=%s', self.communitySet, self.community)
        if self.communitySet:
            return True
        return False

    def setCommunity (self, community):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-community').debug3Func(): logFunc('called. community=%s, old=%s', community, self.community)
        self.communitySet = True
        self.community = community

    def requestVersion (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-version').debug3Func(): logFunc('called. requested=%s', requested)
        self.versionRequested = requested
        self.versionSet = False

    def isVersionRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-version-requested').debug3Func(): logFunc('called. requested=%s', self.versionRequested)
        return self.versionRequested

    def getVersion (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-version').debug3Func(): logFunc('called. self.versionSet=%s, self.version=%s', self.versionSet, self.version)
        if self.versionSet:
            return self.version
        return None

    def hasVersion (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-version').debug3Func(): logFunc('called. self.versionSet=%s, self.version=%s', self.versionSet, self.version)
        if self.versionSet:
            return True
        return False

    def setVersion (self, version):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-version').debug3Func(): logFunc('called. version=%s, old=%s', version, self.version)
        self.versionSet = True
        self.version = version

    def requestType_ (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-type_').debug3Func(): logFunc('called. requested=%s', requested)
        self.type_Requested = requested
        self.type_Set = False

    def isType_Requested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-type_-requested').debug3Func(): logFunc('called. requested=%s', self.type_Requested)
        return self.type_Requested

    def getType_ (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-type_').debug3Func(): logFunc('called. self.type_Set=%s, self.type_=%s', self.type_Set, self.type_)
        if self.type_Set:
            return self.type_
        return None

    def hasType_ (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-type_').debug3Func(): logFunc('called. self.type_Set=%s, self.type_=%s', self.type_Set, self.type_)
        if self.type_Set:
            return True
        return False

    def setType_ (self, type_):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-type_').debug3Func(): logFunc('called. type_=%s, old=%s', type_, self.type_)
        self.type_Set = True
        self.type_ = type_

    def requestPort (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-port').debug3Func(): logFunc('called. requested=%s', requested)
        self.portRequested = requested
        self.portSet = False

    def isPortRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-port-requested').debug3Func(): logFunc('called. requested=%s', self.portRequested)
        return self.portRequested

    def getPort (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-port').debug3Func(): logFunc('called. self.portSet=%s, self.port=%s', self.portSet, self.port)
        if self.portSet:
            return self.port
        return None

    def hasPort (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-port').debug3Func(): logFunc('called. self.portSet=%s, self.port=%s', self.portSet, self.port)
        if self.portSet:
            return True
        return False

    def setPort (self, port):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-port').debug3Func(): logFunc('called. port=%s, old=%s', port, self.port)
        self.portSet = True
        self.port = port


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.name = 0
        self.nameSet = False
        
        self.destination = 0
        self.destinationSet = False
        
        self.community = 0
        self.communitySet = False
        
        self.version = 0
        self.versionSet = False
        
        self.type_ = 0
        self.type_Set = False
        
        self.port = 0
        self.portSet = False
        

    def _getSelfKeyPath (self, destination
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        ancestorVal = Value()
        ancestorVal.setString(destination);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("destination", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", "qt-snmp"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("notifications", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", "qt-snmp"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("snmp", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", "qt-snmp"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
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
        res = self._collectItemsToDelete(destination, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(destination, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
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

        keyPath = self._getSelfKeyPath(destination, 
                                       
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
                               destination, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasName():
            valName = Value()
            if self.name is not None:
                valName.setString(self.name)
            else:
                valName.setEmpty()
            tagValueList.push(("name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"), valName)
        
        if self.hasDestination():
            valDestination = Value()
            if self.destination is not None:
                valDestination.setString(self.destination)
            else:
                valDestination.setEmpty()
            tagValueList.push(("destination", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"), valDestination)
        
        if self.hasCommunity():
            valCommunity = Value()
            if self.community is not None:
                valCommunity.setString(self.community)
            else:
                valCommunity.setEmpty()
            tagValueList.push(("community", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"), valCommunity)
        
        if self.hasVersion():
            valVersion = Value()
            if self.version is not None:
                valVersion.setEnum(self.version.getValue())
            else:
                valVersion.setEmpty()
            tagValueList.push(("version", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"), valVersion)
        
        if self.hasType_():
            valType_ = Value()
            if self.type_ is not None:
                valType_.setEnum(self.type_.getValue())
            else:
                valType_.setEmpty()
            tagValueList.push(("type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"), valType_)
        
        if self.hasPort():
            valPort = Value()
            if self.port is not None:
                valPort.setUint16(self.port)
            else:
                valPort.setEmpty()
            tagValueList.push(("port", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"), valPort)
        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isNameRequested():
            valName = Value()
            valName.setEmpty()
            tagValueList.push(("name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"), valName)
        
        if self.isDestinationRequested():
            valDestination = Value()
            valDestination.setEmpty()
            tagValueList.push(("destination", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"), valDestination)
        
        if self.isCommunityRequested():
            valCommunity = Value()
            valCommunity.setEmpty()
            tagValueList.push(("community", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"), valCommunity)
        
        if self.isVersionRequested():
            valVersion = Value()
            valVersion.setEmpty()
            tagValueList.push(("version", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"), valVersion)
        
        if self.isType_Requested():
            valType_ = Value()
            valType_.setEmpty()
            tagValueList.push(("type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"), valType_)
        
        if self.isPortRequested():
            valPort = Value()
            valPort.setEmpty()
            tagValueList.push(("port", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"), valPort)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isNameRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "name") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-name').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "name", "name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-name-bad-value').infoFunc(): logFunc('name not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setName(tempVar)
            for logFunc in self._log('read-tag-values-name').debug3Func(): logFunc('read name. name=%s, tempValue=%s', self.name, tempValue.getType())
        
        if self.isDestinationRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "destination") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-destination').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "destination", "destination", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-destination-bad-value').infoFunc(): logFunc('destination not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setDestination(tempVar)
            for logFunc in self._log('read-tag-values-destination').debug3Func(): logFunc('read destination. destination=%s, tempValue=%s', self.destination, tempValue.getType())
        
        if self.isCommunityRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "community") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-community').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "community", "community", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-community-bad-value').infoFunc(): logFunc('community not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setCommunity(tempVar)
            for logFunc in self._log('read-tag-values-community').debug3Func(): logFunc('read community. community=%s, tempValue=%s', self.community, tempValue.getType())
        
        if self.isVersionRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "version") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-version').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "version", "version", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-version-bad-value').infoFunc(): logFunc('version not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setVersion(tempVar)
            for logFunc in self._log('read-tag-values-version').debug3Func(): logFunc('read version. version=%s, tempValue=%s', self.version, tempValue.getType())
        
        if self.isType_Requested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "type") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-type_').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "type_", "type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-type-bad-value').infoFunc(): logFunc('type_ not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setType_(tempVar)
            for logFunc in self._log('read-tag-values-type').debug3Func(): logFunc('read type_. type_=%s, tempValue=%s', self.type_, tempValue.getType())
        
        if self.isPortRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "port") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-port').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "port", "port", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint16()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-port-bad-value').infoFunc(): logFunc('port not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPort(tempVar)
            for logFunc in self._log('read-tag-values-port').debug3Func(): logFunc('read port. port=%s, tempValue=%s', self.port, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "destination", 
        "namespace": "destination", 
        "className": "DestinationMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_snmp.tech.snmp.notifications.destination.destination_maapi_gen import DestinationMaapi", 
        "baseClassName": "DestinationMaapiBase", 
        "baseModule": "destination_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-snmp", 
            "yangName": "snmp", 
            "namespace": "snmp", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "name": "snmp"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-snmp", 
            "yangName": "notifications", 
            "namespace": "notifications", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "name": "notifications"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-snmp", 
            "isCurrent": true, 
            "yangName": "destination", 
            "namespace": "destination", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "keyLeaf": {
                "varName": "destination", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "destination"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "destination", 
            "yangName": "destination", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "community", 
            "yangName": "community", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "version", 
            "yangName": "version", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "v1", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "type_", 
            "yangName": "type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "trap", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "port", 
            "yangName": "port", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "162", 
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
            "qwilt_tech_snmp"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "destination", 
            "yangName": "destination", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "community", 
            "yangName": "community", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "version", 
            "yangName": "version", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "v1", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "type_", 
            "yangName": "type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "trap", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "port", 
            "yangName": "port", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "162", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


