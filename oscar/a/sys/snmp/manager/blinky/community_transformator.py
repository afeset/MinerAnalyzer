#
# Copyright Qwilt, 2013
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: naamas
# 

from a.infra.misc.timeout_guard import TimeoutGuard
from a.infra.basic.return_codes import ReturnCodes

from a.sys.confd.pyconfdlib.key_path import KeyPath
from a.sys.confd.pyconfdlib.value import Value
from a.sys.confd.pyconfdlib.tag_values import TagValues

from a.api.yang.modules.common.qwilt_types.qwilt_types_module_gen import Accessmodetype

from community_utils import CommunityUtils

import copy


# Bypass for PyChecker
if  __package__ is None:
    G_GROUP_NAME_SNMP_MANAGER_BLINKY_COMMUNITY_TRANSFORMATOR           = "unknown"
else:
    from . import G_GROUP_NAME_SNMP_MANAGER_BLINKY_COMMUNITY_TRANSFORMATOR


class CommunityTransformator:

    def __init__ (self, logger, dpDomain, maapiDomain, configNode):
        self._log = logger.createLoggerSameModule(G_GROUP_NAME_SNMP_MANAGER_BLINKY_COMMUNITY_TRANSFORMATOR)
        self._dpDomain = dpDomain
        self._maapiDomain = maapiDomain

        self._configNode = configNode

        self._relativeKeyPath = KeyPath()

        self._keyPath = copy.deepcopy(configNode.getKeyPath())

        xmlVal = Value()
        xmlVal.setXmlTag(("community", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", "qt-snmp"))
        self._keyPath.addKeyPathPostfix(xmlVal)

        self._callpointName = "tech-snmp-community-callpoint"

        self._readSecurityName = "all-read-only"

        self._keyPathForCursor = KeyPath()

        valCommunity = Value()
        (tag, ns, prefix) = ("SNMP-COMMUNITY-MIB", "http://tail-f.com/ns/mibs/SNMP-COMMUNITY-MIB/200308060000Z", "SNMP_COMMUNITY_MIB")
        valCommunity.setXmlTag((tag, ns, prefix))
        self._keyPathForCursor.addKeyPathPostfix(valCommunity)

        valCommunityTable = Value()
        (tag, ns, prefix) = ("snmpCommunityTable", "http://tail-f.com/ns/mibs/SNMP-COMMUNITY-MIB/200308060000Z", "SNMP_COMMUNITY_MIB")
        valCommunityTable.setXmlTag((tag, ns, prefix))
        self._keyPathForCursor.addKeyPathPostfix(valCommunityTable)

        valEntry = Value()
        (tag, ns, prefix) = ("snmpCommunityEntry", "http://tail-f.com/ns/mibs/SNMP-COMMUNITY-MIB/200308060000Z", "SNMP_COMMUNITY_MIB")
        valEntry.setXmlTag((tag, ns, prefix))
        self._keyPathForCursor.addKeyPathPostfix(valEntry)

        self._communityUtils = CommunityUtils(self._log, self._maapiDomain, self._keyPathForCursor)

    def getCommunityUtils (self):
        return self._communityUtils

    def getCallpointName (self):
        return self._callpointName

    def getRelativeKeyPath (self):
        return self._relativeKeyPath

    def getKeyPath (self):
        return self._keyPath

    def getElement (self, trxContext, keyPath):
        self._log("get-element").debug2("called - shouldn't have happened for a transaction-hook. trxContext=%s, keyPath=%s", trxContext, keyPath)

        return ReturnCodes.kGeneralError

    def getNext (self, trxContext, keyPath, nextKey):
        self._log("get-next").error("called - shouldn't have happened for a transaction-hook. keyPath=%s, nextKey=%s, trxContext=%s", 
                                    keyPath, nextKey, trxContext)

        return ReturnCodes.kGeneralError

    def setElement (self, trxContext, keyPath, newValue):
        self._log("set-element").debug2("called. trxContext=%s, keyPath=%s, newValue=%s", trxContext, keyPath, newValue)

        # community --> SNMP-COMMUNITY-MIB snmpCommunityTable snmpCommunityEntry entry-name snmpCommunityName

        entryName = keyPath.getAt(keyPath.getLen()-2).asString()
        valLeafTag = keyPath.getAt(keyPath.getLen()-1).asXmlTag()
        self._log("set-element-details").debug2("read details: entry-name=%s, valLeafTag=%s. trxContext=%s, keyPath=%s, newValue=%s", entryName, valLeafTag, trxContext, keyPath, newValue)

        if valLeafTag[0] == "community":
            res = self._communityUtils.setCommunityName(trxContext, entryName, newValue.asString())
            if res != ReturnCodes.kOk:
                self._log('set-element-set-community-name-failed').error('self._communityUtils.setCommunityName() failed. PARAMS, newValue=%s', newValue)
                return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def create (self, trxContext, keyPath):
        self._log("create").debug2("called. trxContext=%s, keyPath=%s", trxContext, keyPath)

        # create an entry with the same name in SNMP-COMMUNITY-MIB snmpCommunityTable snmpCommunityEntry 
        # set snmpCommunitySecurityName to all-read-only
        # set snmpCommunityContextEngineID to 80:00:61:81:05:01

        entryName = keyPath.getAt(keyPath.getLen()-1).asString()
        self._log("create-entry-name").debug2("read entry-name: %s. trxContext=%s, keyPath=%s", entryName, trxContext, keyPath)

        # check entryName validity
        if entryName[0] == '_':
            self._log("create-illegal-entry-name").notice("entry-name: %s is illegal - cannot begin with a '_'. trxContext=%s, keyPath=%s", entryName, trxContext, keyPath)
            self._dpDomain.setDpErrorStr(trxContext, 'entry-name %s is illegal. Must not begin with a \'_\'' % (entryName))
            return ReturnCodes.kGeneralError

        res = self._communityUtils.createEntry(trxContext, entryName, "", self._readSecurityName)
        if res != ReturnCodes.kOk:
            self._log("create-create-entry-failed").notice("_communityUtils.createEntry() failed. entryName=%s, securityName=%s, trxContext=%s, keyPath=%s", entryName, self._readSecurityName, trxContext, keyPath)
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def remove (self, trxContext, keyPath):
        self._log("remove").debug2("called. trxContext=%s, keyPath=%s", trxContext, keyPath)

        entryName = keyPath.getAt(keyPath.getLen()-1).asString()
        self._log("remove-details").debug2("read details: entry-name=%s, trxContext=%s, keyPath=%s", entryName, trxContext, keyPath)

        res = self._communityUtils.removeEntry(trxContext, entryName)
        if res != ReturnCodes.kOk:
            self._log("remove-remove-entry-failed").notice("_communityUtils.removeEntry() failed. entryName=%s, securityName=%s, trxContext=%s, keyPath=%s", entryName, self._readSecurityName, trxContext, keyPath)
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def initTransformationTrx (self, trxContext):
        self._log("init-transformation-trx").debug2("called. trxContext=%s", trxContext)
    
        return ReturnCodes.kOk

    def finishTransformationTrx (self, trxContext):
        self._log("finish-transformation-trx").debug2("called. trxContext=%s", trxContext)

        res = self._maapiDomain.detachMaapi(trxContext)
        if res != ReturnCodes.kOk:
            self._log("finish-transformation-trx-attach-maapi-failed").error("self._maapiDomain.detachMaapi() failed. trxContext=%s", trxContext)
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

