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

import copy


# Bypass for PyChecker
if  __package__ is None:
    G_GROUP_NAME_SNMP_MANAGER_BLINKY_COMMUNITY_UTILS           = "unknown"
else:
    from . import G_GROUP_NAME_SNMP_MANAGER_BLINKY_COMMUNITY_UTILS


class CommunityUtils:

    def __init__ (self, logger, maapiDomain, keyPathForCursor):
        self._log = logger.createLoggerSameModule(G_GROUP_NAME_SNMP_MANAGER_BLINKY_COMMUNITY_UTILS)
        self._maapiDomain = maapiDomain

        self._relativeKeyPath = KeyPath()

        self._keyPathForCursor = copy.deepcopy(keyPathForCursor)

    def createEntry (self, trxContext, entryName, communityName, securityName):
        self._log("create-entry").debug2("called. trxContext=%s, entryName=%s, communityName=%s, securityName=%s", trxContext, entryName, communityName, securityName)

        # create an entry in SNMP-COMMUNITY-MIB snmpCommunityTable snmpCommunityEntry 
        # set snmpCommunityCommunityName to communityName
        # set snmpCommunitySecurityName to securityName

        targetKeyPath = KeyPath()

        valCommunity = Value()
        (tag, ns, prefix) = ("SNMP-COMMUNITY-MIB", "http://tail-f.com/ns/mibs/SNMP-COMMUNITY-MIB/200308060000Z", "SNMP_COMMUNITY_MIB")
        valCommunity.setXmlTag((tag, ns, prefix))
        targetKeyPath.addKeyPathPostfix(valCommunity)

        valCommunityTable = Value()
        (tag, ns, prefix) = ("snmpCommunityTable", "http://tail-f.com/ns/mibs/SNMP-COMMUNITY-MIB/200308060000Z", "SNMP_COMMUNITY_MIB")
        valCommunityTable.setXmlTag((tag, ns, prefix))
        targetKeyPath.addKeyPathPostfix(valCommunityTable)

        tagValueList = TagValues()

        valBegin = Value()
        (tag, ns, prefix) = ("snmpCommunityEntry", "http://tail-f.com/ns/mibs/SNMP-COMMUNITY-MIB/200308060000Z", "SNMP_COMMUNITY_MIB")
        valBegin.setXmlBegin((tag, ns, prefix))
        tagValueList.push((tag, ns), valBegin)

        valKey = Value()
        valKey.setBuf((entryName, len(entryName)))
        tagValueList.push(("snmpCommunityIndex", "http://tail-f.com/ns/mibs/SNMP-COMMUNITY-MIB/200308060000Z"), valKey)

        valCommunityName = Value()
        valCommunityName.setString(communityName)
        tagValueList.push(("snmpCommunityName", "http://tail-f.com/ns/mibs/SNMP-COMMUNITY-MIB/200308060000Z"), valCommunityName)

        valSecurityName = Value()
        valSecurityName.setString(securityName)
        tagValueList.push(("snmpCommunitySecurityName", "http://tail-f.com/ns/mibs/SNMP-COMMUNITY-MIB/200308060000Z"), valSecurityName)

        valEnd = Value()
        valEnd.setXmlEnd((tag, ns, prefix))
        tagValueList.push((tag, ns), valEnd)

        res = self._maapiDomain.writeMaapi(tagValueList, targetKeyPath, trxContext)
        if res != ReturnCodes.kOk:
            self._log('create-entry-write-domain-failed').error('self._maapiDomain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def removeEntry (self, trxContext, entryName):
        self._log("remove-entry").debug2("called. trxContext=%s, entryName=%s", trxContext, entryName)

        pathToDelete = KeyPath()

        valCommunity = Value()
        (tag, ns, prefix) = ("SNMP-COMMUNITY-MIB", "http://tail-f.com/ns/mibs/SNMP-COMMUNITY-MIB/200308060000Z", "SNMP_COMMUNITY_MIB")
        valCommunity.setXmlTag((tag, ns, prefix))
        pathToDelete.addKeyPathPostfix(valCommunity)

        valCommunityTable = Value()
        (tag, ns, prefix) = ("snmpCommunityTable", "http://tail-f.com/ns/mibs/SNMP-COMMUNITY-MIB/200308060000Z", "SNMP_COMMUNITY_MIB")
        valCommunityTable.setXmlTag((tag, ns, prefix))
        pathToDelete.addKeyPathPostfix(valCommunityTable)

        valEntry = Value()
        (tag, ns, prefix) = ("snmpCommunityEntry", "http://tail-f.com/ns/mibs/SNMP-COMMUNITY-MIB/200308060000Z", "SNMP_COMMUNITY_MIB")
        valEntry.setXmlTag((tag, ns, prefix))
        pathToDelete.addKeyPathPostfix(valEntry)

        valKey = Value()
        valKey.setBuf((entryName, len(entryName)))
        pathToDelete.addKeyPathPostfix(valKey)

        res = self._maapiDomain.writeMaapi(None, None, trxContext, itemsToDelete=[pathToDelete])
        if res != ReturnCodes.kOk:
            self._log('remove-entry-domain-failed').error('self._maapiDomain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def setCommunityName (self, trxContext, entryName, communityName):
        self._log("set-community-name").debug2("called. trxContext=%s, entryName=%s, communityName=%s", trxContext, entryName, communityName)

        tagValueList = TagValues()

        valCommName = Value()
        valCommName.setString(communityName)
        tagValueList.push(("snmpCommunityName", "http://tail-f.com/ns/mibs/SNMP-COMMUNITY-MIB/200308060000Z"), valCommName)


        targetKeyPath = KeyPath()

        valCommunity = Value()
        (tag, ns, prefix) = ("SNMP-COMMUNITY-MIB", "http://tail-f.com/ns/mibs/SNMP-COMMUNITY-MIB/200308060000Z", "SNMP_COMMUNITY_MIB")
        valCommunity.setXmlTag((tag, ns, prefix))
        targetKeyPath.addKeyPathPostfix(valCommunity)

        valCommunityTable = Value()
        (tag, ns, prefix) = ("snmpCommunityTable", "http://tail-f.com/ns/mibs/SNMP-COMMUNITY-MIB/200308060000Z", "SNMP_COMMUNITY_MIB")
        valCommunityTable.setXmlTag((tag, ns, prefix))
        targetKeyPath.addKeyPathPostfix(valCommunityTable)

        valEntry = Value()
        (tag, ns, prefix) = ("snmpCommunityEntry", "http://tail-f.com/ns/mibs/SNMP-COMMUNITY-MIB/200308060000Z", "SNMP_COMMUNITY_MIB")
        valEntry.setXmlTag((tag, ns, prefix))
        targetKeyPath.addKeyPathPostfix(valEntry)

        valKey = Value()
        valKey.setBuf((entryName, len(entryName)))
        targetKeyPath.addKeyPathPostfix(valKey)

        res = self._maapiDomain.writeMaapi(tagValueList, targetKeyPath, trxContext)
        if res != ReturnCodes.kOk:
            self._log('set-community-name-domain-failed').error('self._maapiDomain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        self._log("set-community-name-done").debug2("done. trxContext=%s, entryName=%s, communityName=%s", trxContext, entryName, communityName)
        return ReturnCodes.kOk

    def getCommunityName (self, trxContext, entryName):
        self._log("get-community-name").debug2("called. trxContext=%s, entryName=%s", trxContext, entryName)

        tagValueList = TagValues()

        valCommName = Value()
        tagValueList.push(("snmpCommunityName", "http://tail-f.com/ns/mibs/SNMP-COMMUNITY-MIB/200308060000Z"), valCommName)


        targetKeyPath = KeyPath()

        valCommunity = Value()
        (tag, ns, prefix) = ("SNMP-COMMUNITY-MIB", "http://tail-f.com/ns/mibs/SNMP-COMMUNITY-MIB/200308060000Z", "SNMP_COMMUNITY_MIB")
        valCommunity.setXmlTag((tag, ns, prefix))
        targetKeyPath.addKeyPathPostfix(valCommunity)

        valCommunityTable = Value()
        (tag, ns, prefix) = ("snmpCommunityTable", "http://tail-f.com/ns/mibs/SNMP-COMMUNITY-MIB/200308060000Z", "SNMP_COMMUNITY_MIB")
        valCommunityTable.setXmlTag((tag, ns, prefix))
        targetKeyPath.addKeyPathPostfix(valCommunityTable)

        valEntry = Value()
        (tag, ns, prefix) = ("snmpCommunityEntry", "http://tail-f.com/ns/mibs/SNMP-COMMUNITY-MIB/200308060000Z", "SNMP_COMMUNITY_MIB")
        valEntry.setXmlTag((tag, ns, prefix))
        targetKeyPath.addKeyPathPostfix(valEntry)

        valKey = Value()
        valKey.setBuf((entryName, len(entryName)))
        targetKeyPath.addKeyPathPostfix(valKey)

        res = self._maapiDomain.readMaapi(tagValueList, targetKeyPath, trxContext)
        if res != ReturnCodes.kOk:
            self._log('get-community-name-domain-failed').error('self._maapiDomain.readMaapi() failed. PARAMS')
            return None

        communityName = tagValueList.getAt(tagValueList.getLen()-1)[1].asBuf()

        self._log("get-community-name-done").debug2("done. trxContext=%s, entryName=%s, communityName=%s", trxContext, entryName, communityName)
        return communityName

