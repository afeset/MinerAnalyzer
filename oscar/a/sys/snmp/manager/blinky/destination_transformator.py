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
from a.api.yang.modules.tech.common.qwilt_tech_snmp.qwilt_tech_snmp_module_gen import SnmpNotificationVersionType
from a.api.yang.modules.tech.common.qwilt_tech_snmp.qwilt_tech_snmp_module_gen import SnmpNotificationTypeType

import copy
import socket


# Bypass for PyChecker
if  __package__ is None:
    G_GROUP_NAME_SNMP_MANAGER_BLINKY_DESTINATION_TRANSFORMATOR           = "unknown"
else:
    from . import G_GROUP_NAME_SNMP_MANAGER_BLINKY_DESTINATION_TRANSFORMATOR


class DestinationTransformator:

    ALL_TRAPS_TAG_NAME = 'all-traps'
    T_DOMAIN_UDP_ADDR = [1,3,6,1,6,1,1]
    MAX_MESSAGE_SIZE = 2048
    SECURITY_LEVEL_NO_AUTH_NO_PRIV = 1
    AC_NOTIF_ONLY = 'notif-only'

    MP_MODEL_V1 = 0
    MP_MODEL_V2C = 1
    SECURITY_MODEL_V1 = 1
    SECURITY_MODEL_V2C = 2

    NOTIF_TYPE_TRAP = 0

    def __init__ (self, logger, dpDomain, maapiDomain, configNode, communityUtils):
        self._log = logger.createLoggerSameModule(G_GROUP_NAME_SNMP_MANAGER_BLINKY_DESTINATION_TRANSFORMATOR)
        self._dpDomain = dpDomain
        self._maapiDomain = maapiDomain

        self._configNode = configNode

        self._communityUtils = communityUtils

        self._snmpManager = None

        self._relativeKeyPath = KeyPath()

        self._keyPath = copy.deepcopy(configNode.getKeyPath())

        xmlValNotifications = Value()
        xmlValNotifications.setXmlTag(("notifications", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", "qt-snmp"))
        self._keyPath.addKeyPathPostfix(xmlValNotifications)

        xmlValDestination = Value()
        xmlValDestination.setXmlTag(("destination", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", "qt-snmp"))
        self._keyPath.addKeyPathPostfix(xmlValDestination)

        self._callpointName = "tech-snmp-destination-callpoint"

        self._keyPathForCursor = KeyPath()

        valTarget = Value()
        (tag, ns, prefix) = ("SNMP-TARGET-MIB", "http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z", "SNMP_TARGET_MIB")
        valTarget.setXmlTag((tag, ns, prefix))
        self._keyPathForCursor.addKeyPathPostfix(valTarget)

        valTargetAddrTable = Value()
        (tag, ns, prefix) = ("snmpTargetAddrTable", "http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z", "SNMP_TARGET_MIB")
        valTargetAddrTable.setXmlTag((tag, ns, prefix))
        self._keyPathForCursor.addKeyPathPostfix(valTargetAddrTable)

        valEntry = Value()
        (tag, ns, prefix) = ("snmpTargetAddrEntry", "http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z", "SNMP_TARGET_MIB")
        valEntry.setXmlTag((tag, ns, prefix))
        self._keyPathForCursor.addKeyPathPostfix(valEntry)

    def setSnmpManager (self, snmpManager):
        self._snmpManager = snmpManager

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
        self._log("set-element").debug2("called. trxContext=%s, keyPath=%s, newValue=%s", 
                                        trxContext, keyPath, newValue)

        # community-name --> SNMP-COMMUNITY-MIB snmpCommunityTable snmpCommunityEntry entry-name snmpCommunityName

        entryName = keyPath.getAt(keyPath.getLen()-2).asString()
        valLeafTag = keyPath.getAt(keyPath.getLen()-1).asXmlTag()
        self._log("set-element-details").debug2("read details: entry-name=%s, valLeafTag=%s. trxContext=%s, keyPath=%s, newValue=%s", entryName, valLeafTag, trxContext, keyPath, newValue)

        if valLeafTag[0] == 'version':
            destinationData = self._snmpManager.getRunningDestination(entryName)
            if destinationData:
                oldSnmpVersion = destinationData.version
            else:
                oldSnmpVersion = SnmpNotificationVersionType.kV1
            
        if valLeafTag[0] == 'destination':
            # set snmpTargetAddrTAddress (only bytes 0-3)
            try:
                ipAddress = socket.inet_aton(newValue.asString())
                self._log("set-element-destination-ip-address").debug2("ipAddress=%s. entry-name=%s, valLeafTag=%s. trxContext=%s, keyPath=%s, newValue=%s", 
                                                                       ipAddress, entryName, valLeafTag, trxContext, keyPath, newValue)
                oldIpAddress = self.getDestinationInTargetTableEntry(trxContext, entryName)
                if oldIpAddress:
                    self._log("set-element-destination-a").debug2("a) oldIpAddress=%s, entry-name=%s, valLeafTag=%s. trxContext=%s, keyPath=%s, newValue=%s", 
                                                                  oldIpAddress, entryName, valLeafTag, trxContext, keyPath, newValue)
                    newIpAddress = str(ipAddress)[:]+oldIpAddress[4:6]
                else:
                    self._log("set-element-destination-b").debug2("b) entry-name=%s, valLeafTag=%s. trxContext=%s, keyPath=%s, newValue=%s", 
                                                                  entryName, valLeafTag, trxContext, keyPath, newValue)
                    """self._log("set-element-destination-c").debug2("c) ipAddress[0:4]=%s, entry-name=%s, valLeafTag=%s. trxContext=%s, keyPath=%s, newValue=%s", 
                                                                  ipAddress[0:4], entryName, valLeafTag, trxContext, keyPath, newValue)
                    self._log("set-element-destination-c0").debug2("c0) chr(80)=%s", str(chr(80)))
                    self._log("set-element-destination-c1").debug2("c1) chr(160)=%s", str(chr(160)))
                    #self._log("set-element-destination-c2").debug2("c2) chr(162)=%s, entry-name=%s, valLeafTag=%s. trxContext=%s, keyPath=%s, newValue=%s", 
                    #                                               str(chr(162)), entryName, valLeafTag, trxContext, keyPath, newValue)
                    #self._log("set-element-destination-d").debug2("d) ipAddress[0:4]+chr(0)+chr(162)=%s, entry-name=%s, valLeafTag=%s. trxContext=%s, keyPath=%s, newValue=%s", 
                    #                                              str(ipAddress[0:4]+chr(0)+chr(162)), entryName, valLeafTag, trxContext, keyPath, newValue)"""
                    newIpAddress = ipAddress[:]+chr(0)+chr(162)
                #self._log("set-element-destination").debug2("newIpAddress=%s: entry-name=%s, valLeafTag=%s. trxContext=%s, keyPath=%s, newValue=%s", 
                #                                            newIpAddress, entryName, valLeafTag, trxContext, keyPath, newValue)
                res = self.setDestinationInTargetTableEntry(trxContext, entryName, newIpAddress)
                if res != ReturnCodes.kOk:
                    self._log("set-element-set-destination-in-table-failed").error("self.setDestinationInTargetTableEntry() failed. entry-name=%s, valLeafTag=%s. trxContext=%s, keyPath=%s, newValue=%s", 
                                                                                   entryName, valLeafTag, trxContext, keyPath, newValue)
                    return ReturnCodes.kGeneralError
            except socket.error:
                self._log("set-element-illegal-destination").notice("illegal destination: trxContext=%s, keyPath=%s, newValue=%s", trxContext, keyPath, newValue)
                self._dpDomain.setDpErrorStr(trxContext, '%s is not a valid destination string. Should be an IP address' % (newValue.asString()))
                return ReturnCodes.kGeneralError
        elif valLeafTag[0] == 'port':
            oldIpAddress = self.getDestinationInTargetTableEntry(trxContext, entryName)
            newPort = newValue.asUint16()
            if oldIpAddress:
                self._log("set-element-port-get-destination-a").debug2("a) oldIpAddress=%s, entry-name=%s, valLeafTag=%s. trxContext=%s, keyPath=%s, newValue=%s", 
                                                                       oldIpAddress, entryName, valLeafTag, trxContext, keyPath, newValue)
                newIpAddress = oldIpAddress[0:4]+chr(newPort>>8)+chr(newPort&0xFF)
            else:
                self._log("set-element-port-get-destination-b").debug2("b) entry-name=%s, valLeafTag=%s. trxContext=%s, keyPath=%s, newValue=%s", 
                                                                       entryName, valLeafTag, trxContext, keyPath, newValue)
                newIpAddress = chr(0)+chr(0)+chr(0)+chr(0)+chr(newPort>>8)+chr(newPort&0xFF)
            self._log("set-element-port-get-destination-in-table-succeeded").debug2("oldIpAddress=%s, newIpAddress=%s. entry-name=%s, valLeafTag=%s. trxContext=%s, keyPath=%s, newValue=%s", 
                                                                                    oldIpAddress, newIpAddress, entryName, valLeafTag, trxContext, keyPath, newValue)
            res = self.setDestinationInTargetTableEntry(trxContext, entryName, newIpAddress)
            if res != ReturnCodes.kOk:
                self._log("set-element-port-set-destination-in-table-failed").error("self.setDestinationInTargetTableEntry() failed. entry-name=%s, valLeafTag=%s. trxContext=%s, keyPath=%s, newValue=%s", 
                                                                                    entryName, valLeafTag, trxContext, keyPath, newValue)
                return ReturnCodes.kGeneralError
        elif valLeafTag[0] == 'version':
            # set snmpTargetAddrParams and use it to find the relevant entry in /SNMP-TARGET-MIB/snmpTargetParamsTable/snmpTargetParamsEntry - read field snmpTargetParamsSecurityModel
            # 1 --> v1, 2 --> v2c
            # remove the entry from the vacmSecurityToGroupTable and create a new one

            oldSecModel = None
            if oldSnmpVersion == SnmpNotificationVersionType.kV1:
                oldSecModel = self.SECURITY_MODEL_V1
            elif oldSnmpVersion == SnmpNotificationVersionType.kV2c:
                oldSecModel = self.SECURITY_MODEL_V2C
            else:
                self._log('set-element-read-snmp-version-unsupported-version').error('self.readDestinationSnmpVersion() returned unsupported version: %s. entryName=%s, trxContext=%s, keyPath=%s', 
                                                                                     oldSnmpVersion, entryName, trxContext, keyPath)
                return ReturnCodes.kGeneralError

            newSnmpVersion = SnmpNotificationVersionType.getByValue(newValue.asEnum())
            newSecModel = None
            if newSnmpVersion == SnmpNotificationVersionType.kV1:
                newSecModel = self.SECURITY_MODEL_V1
            elif newSnmpVersion == SnmpNotificationVersionType.kV2c:
                newSecModel = self.SECURITY_MODEL_V2C
            else:
                self._log('set-element-unsupported-new-version').error('unsupported version: %s. entryName=%s, trxContext=%s, keyPath=%s', 
                                                                       newSnmpVersion, entryName, trxContext, keyPath)
                return ReturnCodes.kGeneralError

            res = self.removeSecToGroupTableEntry(trxContext, oldSecModel, self.makeSecurityName(entryName))
            if res != ReturnCodes.kOk:
                self._log('set-element-remove-entry-sec-to-group-failed').error('self.removeSecToGroupTableEntry() failed. entryName=%s, trxContext=%s, keyPath=%s', entryName, trxContext, keyPath)
                return ReturnCodes.kGeneralError

            res = self.createSecToGroupTableEntry(trxContext, newSecModel, self.makeSecurityName(entryName))
            if res != ReturnCodes.kOk:
                self._log('set-element-create-entry-sec-to-group-failed').error('self.createSecToGroupTableEntry() failed. entryName=%s, trxContext=%s, keyPath=%s', entryName, trxContext, keyPath)
                return ReturnCodes.kGeneralError

            res = self.setVersionInTargetParamTableEntry(trxContext, entryName, newSnmpVersion)
            if res != ReturnCodes.kOk:
                self._log('set-element-set-entry-param-failed').error('self.setVersionInTargetParamTableEntry() failed. entryName=%s, trxContext=%s, keyPath=%s', entryName, trxContext, keyPath)
                return ReturnCodes.kGeneralError

        elif valLeafTag[0] == 'type':
            newNotifType = SnmpNotificationTypeType.getByValue(newValue.asEnum())

            newNotifTypeVal = None
            if newNotifType == SnmpNotificationTypeType.kTrap:
                newNotifTypeVal = self.NOTIF_TYPE_TRAP
            else:
                self._log('set-element-unsupported-new-notif-type').error('unsupported notification-type: %s. entryName=%s, trxContext=%s, keyPath=%s', 
                                                                          newNotifType, entryName, trxContext, keyPath)
                return ReturnCodes.kGeneralError
            # nothing to do - we only support traps
            self._log('set-element-notify-type').debug2('ignoring set-elem to notification type: newNotifType=%s, newNotifTypeVal=%s. only traps are supported. entryName=%s, trxContext=%s, keyPath=%s', 
                                                        newNotifType, newNotifTypeVal, entryName, trxContext, keyPath)
        elif valLeafTag[0] == 'community':
            # write the community-name in the snmpCommunityTable
            res = self._communityUtils.setCommunityName(trxContext, self.makeSecurityName(entryName), newValue.asString())
            if res != ReturnCodes.kOk:
                self._log('set-element-set-community-name-failed').error('self._communityUtils.setCommunityName() failed. PARAMS, newValue=%s', newValue)
                return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def makeSecurityName (self, entryName):
        return '_%s_notif' % entryName

    def setDestinationInTargetTableEntry (self, trxContext, entryName, ipAddress):
        self._log("set-destination-in-target-table-entry").debug2("called. trxContext=%s, entryName=%s", trxContext, entryName)

        targetKeyPath = KeyPath()

        valTarget = Value()
        (tag, ns, prefix) = ("SNMP-TARGET-MIB", "http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z", "SNMP_TARGET_MIB")
        valTarget.setXmlTag((tag, ns, prefix))
        targetKeyPath.addKeyPathPostfix(valTarget)

        tagValueList = TagValues()

        valTargetAddrTable = Value()
        (tag, ns, prefix) = ("snmpTargetAddrTable","http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z", "SNMP_TARGET_MIB")
        valTargetAddrTable.setXmlBegin((tag, ns, prefix))
        tagValueList.push((tag, ns), valTargetAddrTable)

        valBegin = Value()
        (tag, ns, prefix) = ("snmpTargetAddrEntry", "http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z", "SNMP_TARGET_MIB")
        valBegin.setXmlBegin((tag, ns, prefix))
        tagValueList.push((tag, ns), valBegin)

        valKey = Value()
        valKey.setString(entryName)
        tagValueList.push(("snmpTargetAddrName", "http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z"), valKey)

        # snmpTargetAddrTAddress to 0.0.0.0.0.162
        valTAddr = Value()
        addrStr = ipAddress
        valTAddr.setBinary(addrStr)
        tagValueList.push(("snmpTargetAddrTAddress", "http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z"), valTAddr)

        valEnd = Value()
        valEnd.setXmlEnd((tag, ns, prefix))
        tagValueList.push((tag, ns), valEnd)

        valTargetAddrTable = Value()
        (tag, ns, prefix) = ("snmpTargetAddrTable","http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z", "SNMP_TARGET_MIB")
        valTargetAddrTable.setXmlEnd((tag, ns, prefix))
        tagValueList.push((tag, ns), valTargetAddrTable)

        res = self._maapiDomain.writeMaapi(tagValueList, targetKeyPath, trxContext)
        if res != ReturnCodes.kOk:
            self._log('get-destination-in-target-table-entry-write-domain-failed').error('self._maapiDomain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        self._log("set-destination-in-target-table-entry-done").debug2("done. trxContext=%s, entryName=%s", trxContext, entryName)
        return ReturnCodes.kOk

    def getDestinationInTargetTableEntry (self, trxContext, entryName):
        self._log("get-destination-in-target-table-entry").debug2("called. trxContext=%s, entryName=%s", trxContext, entryName)

        targetKeyPath = KeyPath()

        valTarget = Value()
        (tag, ns, prefix) = ("SNMP-TARGET-MIB", "http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z", "SNMP_TARGET_MIB")
        valTarget.setXmlTag((tag, ns, prefix))
        targetKeyPath.addKeyPathPostfix(valTarget)

        tagValueList = TagValues()

        valTargetAddrTable = Value()
        (tag, ns, prefix) = ("snmpTargetAddrTable","http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z", "SNMP_TARGET_MIB")
        valTargetAddrTable.setXmlBegin((tag, ns, prefix))
        tagValueList.push((tag, ns), valTargetAddrTable)

        valBegin = Value()
        (tag, ns, prefix) = ("snmpTargetAddrEntry", "http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z", "SNMP_TARGET_MIB")
        valBegin.setXmlBegin((tag, ns, prefix))
        tagValueList.push((tag, ns), valBegin)

        valKey = Value()
        valKey.setString(entryName)
        tagValueList.push(("snmpTargetAddrName", "http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z"), valKey)

        valTAddr = Value()
        tagValueList.push(("snmpTargetAddrTAddress", "http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z"), valTAddr)

        valEnd = Value()
        valEnd.setXmlEnd((tag, ns, prefix))
        tagValueList.push((tag, ns), valEnd)

        valTargetAddrTable = Value()
        (tag, ns, prefix) = ("snmpTargetAddrTable","http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z", "SNMP_TARGET_MIB")
        valTargetAddrTable.setXmlEnd((tag, ns, prefix))
        tagValueList.push((tag, ns), valTargetAddrTable)

        res = self._maapiDomain.readMaapi(tagValueList, targetKeyPath, trxContext)
        if res != ReturnCodes.kOk:
            self._log('get-destination-in-target-table-entry-read-domain-failed').error('self._maapiDomain.writeMaapi() failed. PARAMS')
            return None

        ipAddress = tagValueList.getAt(tagValueList.getLen()-3)[1].asBinary()[0:6]

        self._log("get-destination-in-target-table-entry-done").debug2("done. trxContext=%s, entryName=%s, ipAddress=%s", trxContext, entryName, ipAddress)
        return ipAddress

    def createTargetAddrTableEntry (self, trxContext, entryName):
        """
        create an entry with the same name in SNMP-TARGET-MIB snmpTargetAddrTable snmpTargetAddrEntry 
            set snmpTargetAddrTDomain to 1.3.6.1.6.1.1
            set snmpTargetAddrTAddress to 0.0.0.0.0.162
            set snmpTargetAddrTagList to the same name
            set snmpTargetAddrParams to the same name
            set snmpTargetAddrMMS to 2048
        """

        self._log("create-target-addr-table-entry").debug2("called. trxContext=%s, entryName=%s", trxContext, entryName)

        targetKeyPath = KeyPath()

        valTarget = Value()
        (tag, ns, prefix) = ("SNMP-TARGET-MIB", "http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z", "SNMP_TARGET_MIB")
        valTarget.setXmlTag((tag, ns, prefix))
        targetKeyPath.addKeyPathPostfix(valTarget)

        tagValueList = TagValues()

        valTargetAddrTable = Value()
        (tag, ns, prefix) = ("snmpTargetAddrTable","http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z", "SNMP_TARGET_MIB")
        valTargetAddrTable.setXmlBegin((tag, ns, prefix))
        tagValueList.push((tag, ns), valTargetAddrTable)

        valBegin = Value()
        (tag, ns, prefix) = ("snmpTargetAddrEntry", "http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z", "SNMP_TARGET_MIB")
        valBegin.setXmlBegin((tag, ns, prefix))
        tagValueList.push((tag, ns), valBegin)

        valKey = Value()
        valKey.setString(entryName)
        tagValueList.push(("snmpTargetAddrName", "http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z"), valKey)

        # snmpTargetAddrTDomain to 1.3.6.1.6.1.1
        valTDomain = Value()
        valTDomain.setOid(self.T_DOMAIN_UDP_ADDR)
        tagValueList.push(("snmpTargetAddrTDomain", "http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z"), valTDomain)

        # snmpTargetAddrTAddress to 0.0.0.0.0.162
        valTAddr = Value()
        #addrStr = chr(0)+chr(0)+chr(0)+chr(0)+chr(0)+chr(162)
        addrStr = chr(0)+chr(0)+chr(0)+chr(0)+chr(0)+chr(162)
        valTAddr.setBinary(addrStr)
        tagValueList.push(("snmpTargetAddrTAddress", "http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z"), valTAddr)

        # snmpTargetAddrTagList to the same name
        valTagName = Value()
        valTagName.setString(self.ALL_TRAPS_TAG_NAME)
        tagValueList.push(("snmpTargetAddrTagList", "http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z"), valTagName)

        # snmpTargetAddrParams to the same name
        valParamName = Value()
        valParamName.setString(entryName)
        tagValueList.push(("snmpTargetAddrParams", "http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z"), valParamName)

        # snmpTargetAddrMMS to 2048
        valMMS = Value()
        valMMS.setInt32(self.MAX_MESSAGE_SIZE)
        tagValueList.push(("snmpTargetAddrMMS", "http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z"), valMMS)

        valEnd = Value()
        valEnd.setXmlEnd((tag, ns, prefix))
        tagValueList.push((tag, ns), valEnd)

        valTargetAddrTable = Value()
        (tag, ns, prefix) = ("snmpTargetAddrTable","http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z", "SNMP_TARGET_MIB")
        valTargetAddrTable.setXmlEnd((tag, ns, prefix))
        tagValueList.push((tag, ns), valTargetAddrTable)

        res = self._maapiDomain.writeMaapi(tagValueList, targetKeyPath, trxContext)
        if res != ReturnCodes.kOk:
            self._log('create-target-addr-table-entry-write-domain-failed').error('self._maapiDomain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        self._log("create-target-addr-table-entry-done").debug2("done. trxContext=%s, entryName=%s", trxContext, entryName)
        return ReturnCodes.kOk

    def removeTargetAddrTableEntry (self, trxContext, entryName):

        self._log("remove-target-addr-table-entry").debug2("called. trxContext=%s, entryName=%s", trxContext, entryName)


        pathToDelete = KeyPath()

        valTarget = Value()
        (tag, ns, prefix) = ("SNMP-TARGET-MIB", "http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z", "SNMP_TARGET_MIB")
        valTarget.setXmlTag((tag, ns, prefix))
        pathToDelete.addKeyPathPostfix(valTarget)

        valTargetAddrTable = Value()
        (tag, ns, prefix) = ("snmpTargetAddrTable","http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z", "SNMP_TARGET_MIB")
        valTargetAddrTable.setXmlTag((tag, ns, prefix))
        pathToDelete.addKeyPathPostfix(valTargetAddrTable)

        valEntry = Value()
        (tag, ns, prefix) = ("snmpTargetAddrEntry", "http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z", "SNMP_TARGET_MIB")
        valEntry.setXmlTag((tag, ns, prefix))
        pathToDelete.addKeyPathPostfix(valEntry)

        valKey = Value()
        valKey.setString(entryName)
        pathToDelete.addKeyPathPostfix(valKey)

        res = self._maapiDomain.writeMaapi(None, None, trxContext, itemsToDelete=[pathToDelete])
        if res != ReturnCodes.kOk:
            self._log('remove-domain-failed').error('self._maapiDomain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        self._log("remove-target-addr-table-entry-done").debug2("done. trxContext=%s, entryName=%s", trxContext, entryName)
        return ReturnCodes.kOk

    def createTargetParamTableEntry (self, trxContext, entryName):
        """
        create an entry with the entryName in SNMP-TARGET-MIB snmpTargetParamsTable snmpTargetParamsEntry 
            set snmpTargetParamsMPModel to 0 (v1)
            set snmpTargetParamsSecurityModel to 1 (v1)
            set snmpTargetParamsSecurityName to _<entryName>_notif
            set snmpTargetParamsSecurityLevel to noAuthNoPriv
        """

        self._log("create-target-param-table-entry").debug2("called. trxContext=%s, entryName=%s", trxContext, entryName)

        targetKeyPath = KeyPath()

        valTarget = Value()
        (tag, ns, prefix) = ("SNMP-TARGET-MIB", "http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z", "SNMP_TARGET_MIB")
        valTarget.setXmlTag((tag, ns, prefix))
        targetKeyPath.addKeyPathPostfix(valTarget)

        tagValueList = TagValues()

        valTargetParamTable = Value()
        (tag, ns, prefix) = ("snmpTargetParamsTable","http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z", "SNMP_TARGET_MIB")
        valTargetParamTable.setXmlBegin((tag, ns, prefix))
        tagValueList.push((tag, ns), valTargetParamTable)

        valBegin = Value()
        (tag, ns, prefix) = ("snmpTargetParamsEntry", "http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z", "SNMP_TARGET_MIB")
        valBegin.setXmlBegin((tag, ns, prefix))
        tagValueList.push((tag, ns), valBegin)

        valKey = Value()
        valKey.setString(entryName)
        tagValueList.push(("snmpTargetParamsName", "http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z"), valKey)

        # snmpTargetParamsMPModel to 0 (v1)
        valMPModel = Value()
        valMPModel.setInt32(self.MP_MODEL_V1)
        tagValueList.push(("snmpTargetParamsMPModel", "http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z"), valMPModel)

        # snmpTargetParamsSecurityModel to 1 (v1)
        valSecurityModel = Value()
        valSecurityModel.setInt32(self.SECURITY_MODEL_V1)
        tagValueList.push(("snmpTargetParamsSecurityModel", "http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z"), valSecurityModel)

        # snmpTargetParamsSecurityName to all-traps
        valSecurityName = Value()
        valSecurityName.setString(self.makeSecurityName(entryName))
        tagValueList.push(("snmpTargetParamsSecurityName", "http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z"), valSecurityName)

        # snmpTargetParamsSecurityLevel to noAuthNoPriv
        valSecurityLevel = Value()
        valSecurityLevel.setEnum(self.SECURITY_LEVEL_NO_AUTH_NO_PRIV)
        tagValueList.push(("snmpTargetParamsSecurityLevel", "http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z"), valSecurityLevel)

        valEnd = Value()
        valEnd.setXmlEnd((tag, ns, prefix))
        tagValueList.push((tag, ns), valEnd)

        valTargetParamTable = Value()
        (tag, ns, prefix) = ("snmpTargetParamsTable","http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z", "SNMP_TARGET_MIB")
        valTargetParamTable.setXmlEnd((tag, ns, prefix))
        tagValueList.push((tag, ns), valTargetParamTable)

        res = self._maapiDomain.writeMaapi(tagValueList, targetKeyPath, trxContext)
        if res != ReturnCodes.kOk:
            self._log('create-target-param-table-entry-write-domain-failed').error('self._maapiDomain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        self._log("create-target-param-table-entry-done").debug2("done. trxContext=%s, entryName=%s", trxContext, entryName)
        return ReturnCodes.kOk

    def setVersionInTargetParamTableEntry (self, trxContext, entryName, snmpVersion):
        """
        sets the entry with the entryName in SNMP-TARGET-MIB snmpTargetParamsTable snmpTargetParamsEntry 
            set snmpTargetParamsMPModel to 0 (v1) or 1 (v2c)
            set snmpTargetParamsSecurityModel to 1 (v1) or 2 (v2c)
        """
        self._log("set-version-in-target-param-table-entry").debug2("called. trxContext=%s, entryName=%s, snmpVersion=%s", 
                                                                    trxContext, entryName, snmpVersion)

        targetKeyPath = KeyPath()

        valTarget = Value()
        (tag, ns, prefix) = ("SNMP-TARGET-MIB", "http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z", "SNMP_TARGET_MIB")
        valTarget.setXmlTag((tag, ns, prefix))
        targetKeyPath.addKeyPathPostfix(valTarget)

        valTargetParamTable = Value()
        (tag, ns, prefix) = ("snmpTargetParamsTable","http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z", "SNMP_TARGET_MIB")
        valTargetParamTable.setXmlTag((tag, ns, prefix))
        targetKeyPath.addKeyPathPostfix(valTargetParamTable)

        valEntry = Value()
        (tag, ns, prefix) = ("snmpTargetParamsEntry", "http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z", "SNMP_TARGET_MIB")
        valEntry.setXmlTag((tag, ns, prefix))
        targetKeyPath.addKeyPathPostfix(valEntry)

        valKey = Value()
        valKey.setString(entryName)
        targetKeyPath.addKeyPathPostfix(valKey)

        tagValueList = TagValues()

        valMPModel = Value()
        # snmpTargetParamsMPModel to 0 (v1) or 1 (v2c)
        if snmpVersion == SnmpNotificationVersionType.kV1:
            valMPModel.setInt32(self.MP_MODEL_V1)
        elif snmpVersion == SnmpNotificationVersionType.kV2c:
            valMPModel.setInt32(self.MP_MODEL_V2C)

        tagValueList.push(("snmpTargetParamsMPModel", "http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z"), valMPModel)

        # snmpTargetParamsSecurityModel to 1 (v1)
        valSecurityModel = Value()
        if snmpVersion == SnmpNotificationVersionType.kV1:
            valSecurityModel.setInt32(self.SECURITY_MODEL_V1)
        elif snmpVersion == SnmpNotificationVersionType.kV2c:
            valSecurityModel.setInt32(self.SECURITY_MODEL_V2C)

        tagValueList.push(("snmpTargetParamsSecurityModel", "http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z"), valSecurityModel)

        res = self._maapiDomain.writeMaapi(tagValueList, targetKeyPath, trxContext)
        if res != ReturnCodes.kOk:
            self._log('create-target-param-table-entry-write-domain-failed').error('self._maapiDomain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        self._log("set-version-in-target-param-table-entry-done").debug2("done. trxContext=%s, entryName=%s, snmpVersion=%s", 
                                                                         trxContext, entryName, snmpVersion)
        return ReturnCodes.kOk

    def removeTargetParamTableEntry (self, trxContext, entryName):
        self._log("remove-target-param-table-entry").debug2("called. trxContext=%s, entryName=%s", trxContext, entryName)

        pathToDelete = KeyPath()

        valTarget = Value()
        (tag, ns, prefix) = ("SNMP-TARGET-MIB", "http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z", "SNMP_TARGET_MIB")
        valTarget.setXmlTag((tag, ns, prefix))
        pathToDelete.addKeyPathPostfix(valTarget)

        valTargetAddrTable = Value()
        (tag, ns, prefix) = ("snmpTargetParamsTable","http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z", "SNMP_TARGET_MIB")
        valTargetAddrTable.setXmlTag((tag, ns, prefix))
        pathToDelete.addKeyPathPostfix(valTargetAddrTable)

        valEntry = Value()
        (tag, ns, prefix) = ("snmpTargetParamsEntry", "http://tail-f.com/ns/mibs/SNMP-TARGET-MIB/200210140000Z", "SNMP_TARGET_MIB")
        valEntry.setXmlTag((tag, ns, prefix))
        pathToDelete.addKeyPathPostfix(valEntry)

        valKey = Value()
        valKey.setString(entryName)
        pathToDelete.addKeyPathPostfix(valKey)

        res = self._maapiDomain.writeMaapi(None, None, trxContext, itemsToDelete=[pathToDelete])
        if res != ReturnCodes.kOk:
            self._log('remove-domain-failed').error('self._maapiDomain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        self._log("remove-target-addr-table-entry-done").debug2("done. trxContext=%s, entryName=%s", trxContext, entryName)
        return ReturnCodes.kOk

    def createSecToGroupTableEntry (self, trxContext, securityModel, securityName):
        self._log("create-sec-to-group-table-entry").debug2("called. trxContext=%s, securityModel=%s, securityName=%s", trxContext, securityModel, securityName)

        """
        create an entry with the securityName in SNMP-VIEW-BASED-ACM-MIB vacmSecurityToGroupTable vacmSecurityToGroupEntry 
            set vacmSecurityModel to securityModel
            set vacmSecurityName to securityName
            set vacmGroupName to notif-only
        """

        self._log("create-sec-to-group-table-entry").debug2("called. trxContext=%s, securityModel=%s, securityName=%s", trxContext, securityModel, securityName)

        targetKeyPath = KeyPath()

        valVacm = Value()
        (tag, ns, prefix) = ("SNMP-VIEW-BASED-ACM-MIB", "http://tail-f.com/ns/mibs/SNMP-VIEW-BASED-ACM-MIB/200210160000Z", "SNMP_VIEW_BASED_ACM_MIB")
        valVacm.setXmlTag((tag, ns, prefix))
        targetKeyPath.addKeyPathPostfix(valVacm)

        tagValueList = TagValues()

        valVacmSecToGroupTable = Value()
        (tag, ns, prefix) = ("vacmSecurityToGroupTable", "http://tail-f.com/ns/mibs/SNMP-VIEW-BASED-ACM-MIB/200210160000Z", "SNMP_VIEW_BASED_ACM_MIB")
        valVacmSecToGroupTable.setXmlBegin((tag, ns, prefix))
        tagValueList.push((tag, ns), valVacmSecToGroupTable)

        valBegin = Value()
        (tag, ns, prefix) = ("vacmSecurityToGroupEntry", "http://tail-f.com/ns/mibs/SNMP-VIEW-BASED-ACM-MIB/200210160000Z", "SNMP_VIEW_BASED_ACM_MIB")
        valBegin.setXmlBegin((tag, ns, prefix))
        tagValueList.push((tag, ns), valBegin)

        valKeyModel = Value()
        valKeyModel.setInt32(securityModel)
        tagValueList.push(("vacmSecurityModel", "http://tail-f.com/ns/mibs/SNMP-VIEW-BASED-ACM-MIB/200210160000Z"), valKeyModel)

        valKeySecName = Value()
        valKeySecName.setString(securityName)
        tagValueList.push(("vacmSecurityName", "http://tail-f.com/ns/mibs/SNMP-VIEW-BASED-ACM-MIB/200210160000Z"), valKeySecName)

        # vacmGroupName to notif-only
        valGroupName = Value()
        valGroupName.setString(self.AC_NOTIF_ONLY)
        tagValueList.push(("vacmGroupName", "http://tail-f.com/ns/mibs/SNMP-VIEW-BASED-ACM-MIB/200210160000Z"), valGroupName)

        valEnd = Value()
        valEnd.setXmlEnd((tag, ns, prefix))
        tagValueList.push((tag, ns), valEnd)

        valTargetParamTable = Value()
        (tag, ns, prefix) = ("vacmSecurityToGroupTable","http://tail-f.com/ns/mibs/SNMP-VIEW-BASED-ACM-MIB/200210160000Z", "SNMP_VIEW_BASED_ACM_MIB")
        valTargetParamTable.setXmlEnd((tag, ns, prefix))
        tagValueList.push((tag, ns), valTargetParamTable)

        res = self._maapiDomain.writeMaapi(tagValueList, targetKeyPath, trxContext)
        if res != ReturnCodes.kOk:
            self._log('create-sec-to-group-table-entry-write-domain-failed').error('self._maapiDomain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        self._log("create-sec-to-group-table-entry-done").debug2("done. trxContext=%s, securityModel=%s, securityName=%s", trxContext, securityModel, securityName)
        return ReturnCodes.kOk

    def removeSecToGroupTableEntry (self, trxContext, secModel, secName):
        self._log("remove-sec-to-group-table-entry").debug2("called. trxContext=%s, secModel=%s, secName=%s", trxContext, secModel, secName)

        pathToDelete = KeyPath()

        valVacm = Value()
        (tag, ns, prefix) = ("SNMP-VIEW-BASED-ACM-MIB", "http://tail-f.com/ns/mibs/SNMP-VIEW-BASED-ACM-MIB/200210160000Z", "SNMP_VIEW_BASED_ACM_MIB")
        valVacm.setXmlTag((tag, ns, prefix))
        pathToDelete.addKeyPathPostfix(valVacm)

        valVacmSecToGroupTable = Value()
        (tag, ns, prefix) = ("vacmSecurityToGroupTable", "http://tail-f.com/ns/mibs/SNMP-VIEW-BASED-ACM-MIB/200210160000Z", "SNMP_VIEW_BASED_ACM_MIB")
        valVacmSecToGroupTable.setXmlTag((tag, ns, prefix))
        pathToDelete.addKeyPathPostfix(valVacmSecToGroupTable)

        valEntry = Value()
        (tag, ns, prefix) = ("vacmSecurityToGroupEntry", "http://tail-f.com/ns/mibs/SNMP-VIEW-BASED-ACM-MIB/200210160000Z", "SNMP_VIEW_BASED_ACM_MIB")
        valEntry.setXmlTag((tag, ns, prefix))
        pathToDelete.addKeyPathPostfix(valEntry)

        """valKeyModel = Value()
        valKeyModel.setInt32(secModel)
        pathToDelete.addKeyPathPostfix(valKeyModel)

        valKeySecName = Value()
        valKeySecName.setString(secName)
        pathToDelete.addKeyPathPostfix(valKeySecName)

        res = self._maapiDomain.writeMaapi(None, None, trxContext, itemsToDelete=[pathToDelete])
        if res != ReturnCodes.kOk:
            self._log('remove-sec-to-group-table-entry-domain-failed').error('self._maapiDomain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError"""

        # due to a limitation of pyconfdlib.key_path.KeyPath (which onlys support single-key lists), we have to manually build the key path string here
        pathToDeleteStr = "%s{%s %s}" % (pathToDelete.getCannonicalStr(), secModel, secName)

        res = self._maapiDomain.deleteMaapiByStringKeyPath([pathToDeleteStr], trxContext)
        if res != ReturnCodes.kOk:
            self._log('remove-sec-to-group-table-entry-domain-failed').error('self._maapiDomain.deleteMaapiByStringKeyPath() failed. PARAMS')
            return ReturnCodes.kGeneralError

        self._log("remove-sec-to-group-table-entry-done").debug2("done. trxContext=%s, secModel=%s, secName=%s", trxContext, secModel, secName)
        return ReturnCodes.kOk

    def create (self, trxContext, keyPath):
        self._log("create").debug2("called. trxContext=%s, keyPath=%s", trxContext, keyPath)

        entryName = keyPath.getAt(keyPath.getLen()-1).asString()[:]
        self._log("create-entry-name").debug2("read entry-name: %s. trxContext=%s, keyPath=%s", entryName, trxContext, keyPath)

        res = self.createTargetAddrTableEntry(trxContext, entryName)
        if res != ReturnCodes.kOk:
            self._log('create-entry-target-addr-failed').error('createTargetAddrTableEntry() failed. entryName=%s, trxContext=%s, keyPath=%s', entryName, trxContext, keyPath)
            return ReturnCodes.kGeneralError

        res = self.createTargetParamTableEntry(trxContext, entryName)
        if res != ReturnCodes.kOk:
            self._log('create-entry-target-param-failed').error('createTargetParamTableEntry() failed. entryName=%s, trxContext=%s, keyPath=%s', entryName, trxContext, keyPath)
            return ReturnCodes.kGeneralError

        res = self._communityUtils.createEntry(trxContext, self.makeSecurityName(entryName), '', self.makeSecurityName (entryName))
        if res != ReturnCodes.kOk:
            self._log('create-community-create-entry-failed').error('self._communityUtils.createEntry() failed. entryName=%s, trxContext=%s, keyPath=%s', entryName, trxContext, keyPath)
            return ReturnCodes.kGeneralError

        res = self.createSecToGroupTableEntry(trxContext, self.SECURITY_MODEL_V1, self.makeSecurityName(entryName))
        if res != ReturnCodes.kOk:
            self._log('create-entry-sec-to-group-failed').error('self.createSecToGroupTableEntry() failed. entryName=%s, trxContext=%s, keyPath=%s', entryName, trxContext, keyPath)
            return ReturnCodes.kGeneralError

        self._log("create-done").debug2("done. %entryName=%s, trxContext=%s, keyPath=%s", entryName, trxContext, keyPath)
        return ReturnCodes.kOk

    def remove (self, trxContext, keyPath):
        self._log("remove").debug2("called. trxContext=%s, keyPath=%s", trxContext, keyPath)

        entryName = keyPath.getAt(keyPath.getLen()-1).asString()
        self._log("remove-details").debug2("read details: entry-name=%s, trxContext=%s, keyPath=%s", entryName, trxContext, keyPath)

        snmpVersionKeyPath = copy.deepcopy(keyPath)
        versionTag = Value()
        versionTag.setXmlTag(("version", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", "qt-snmp"))
        snmpVersionKeyPath.addKeyPathPostfix(versionTag)

        destinationData = self._snmpManager.getRunningDestination(entryName)
        if not destinationData:
            self._log('remove-read-snmp-version-failed').error('self.readDestinationSnmpVersion() failed. entryName=%s, trxContext=%s, keyPath=%s', entryName, trxContext, keyPath)
            return ReturnCodes.kGeneralError
        snmpVersion = destinationData.version

        secModel = None
        if snmpVersion == SnmpNotificationVersionType.kV1:
            secModel = self.SECURITY_MODEL_V1
        elif snmpVersion == SnmpNotificationVersionType.kV2c:
            secModel = self.SECURITY_MODEL_V2C
        else:
            self._log('remove-read-snmp-version-unsupported-version').error('self.readDestinationSnmpVersion() returned unsupported version: %s. entryName=%s, trxContext=%s, keyPath=%s', 
                                                                            snmpVersion, entryName, trxContext, keyPath)
            return ReturnCodes.kGeneralError

        res = self.removeTargetAddrTableEntry(trxContext, entryName)
        if res != ReturnCodes.kOk:
            self._log('remove-entry-target-address-failed').error('self.removeTargetAddrTableEntry() failed. entryName=%s, trxContext=%s, keyPath=%s', entryName, trxContext, keyPath)
            return ReturnCodes.kGeneralError

        res = self.removeTargetParamTableEntry(trxContext, entryName)
        if res != ReturnCodes.kOk:
            self._log('remove-entry-target-param-failed').error('self.removeTargetParamTableEntry() failed. entryName=%s, trxContext=%s, keyPath=%s', entryName, trxContext, keyPath)
            return ReturnCodes.kGeneralError

        res = self._communityUtils.removeEntry(trxContext, self.makeSecurityName(entryName))
        if res != ReturnCodes.kOk:
            self._log('remove-community-remove-entry-failed').error('self._communityUtils.removeEntry() failed. entryName=%s, trxContext=%s, keyPath=%s', entryName, trxContext, keyPath)
            return ReturnCodes.kGeneralError
        res = self.removeSecToGroupTableEntry(trxContext, secModel, self.makeSecurityName(entryName))
        if res != ReturnCodes.kOk:
            self._log('remove-entry-sec-to-group-failed').error('self.removeSecToGroupTableEntry() failed. entryName=%s, trxContext=%s, keyPath=%s', entryName, trxContext, keyPath)
            return ReturnCodes.kGeneralError

        self._log("remove-done").debug2("done. trxContext=%s, keyPath=%s", trxContext, keyPath)

        return ReturnCodes.kOk

    def initTransformationTrx (self, trxContext):
        self._log("init-transformation-trx").debug2("called. trxContext=%s", trxContext)
    
        return ReturnCodes.kOk

    def finishTransformationTrx (self, trxContext):
        self._log("finish-transformation-trx").debug2("called. trxContext=%s", trxContext)

        self._maapiDomain.detachMaapi(trxContext)
        return ReturnCodes.kOk

