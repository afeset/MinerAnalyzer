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

import copy


# Bypass for PyChecker
if  __package__ is None:
    G_GROUP_NAME_SNMP_MANAGER_BLINKY_SNMP_TRANSFORMATOR           = "unknown"
else:
    from . import G_GROUP_NAME_SNMP_MANAGER_BLINKY_SNMP_TRANSFORMATOR


class SnmpTransformator:

    def __init__ (self, logger, dpDomain, maapiDomain, configNode):
        self._log = logger.createLoggerSameModule(G_GROUP_NAME_SNMP_MANAGER_BLINKY_SNMP_TRANSFORMATOR)
        self._dpDomain = dpDomain
        self._maapiDomain = maapiDomain

        self._relativeKeyPath = KeyPath()

        self._keyPath = copy.deepcopy(configNode.getKeyPath())

        xmlVal = Value()
        xmlVal.setXmlTag(("snmp", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", "qt-snmp"))
        self._keyPath.addKeyPathPostfix(xmlVal)

        self._callpointName = "tech-snmp-callpoint"

        self._readSecurityName = "all-read-only"

        self._keyPathSnmpV2 = KeyPath()

        valMib = Value()
        (tag, ns, prefix) = ("SNMPv2-MIB", "http://tail-f.com/ns/mibs/SNMPv2-MIB/200210160000Z", "SNMPv2_MIB")
        valMib.setXmlTag((tag, ns, prefix))
        self._keyPathSnmpV2.addKeyPathPostfix(valMib)

        valSystem = Value()
        (tag, ns, prefix) = ("system", "http://tail-f.com/ns/mibs/SNMPv2-MIB/200210160000Z", "SNMPv2_MIB")
        valSystem.setXmlTag((tag, ns, prefix))
        self._keyPathSnmpV2.addKeyPathPostfix(valSystem)

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

        entryName = keyPath.getAt(keyPath.getLen()-2).asString()
        valLeafTag = keyPath.getAt(keyPath.getLen()-1).asXmlTag()
        self._log("set-element-details").debug2("read details: entry-name=%s, valLeafTag=%s. trxContext=%s, keyPath=%s, newValue=%s", entryName, valLeafTag, trxContext, keyPath, newValue)

        doWrite = False

        tagValueList = TagValues()

        if valLeafTag[0] == "contact":
            valContact = Value()
            valContact.setString(newValue.asString())
            tagValueList.push(("sysContact", "http://tail-f.com/ns/mibs/SNMPv2-MIB/200210160000Z"), valContact)
            doWrite = True
        elif valLeafTag[0] == "location":
            valLocation = Value()
            valLocation.setString(newValue.asString())
            tagValueList.push(("sysLocation", "http://tail-f.com/ns/mibs/SNMPv2-MIB/200210160000Z"), valLocation)
            doWrite = True

        if doWrite:
            res = self._maapiDomain.writeMaapi(tagValueList, self._keyPathSnmpV2, trxContext)
            if res != ReturnCodes.kOk:
                self._log('set-element-domain-failed').error('self._maapiDomain.writeMaapi() failed. PARAMS')
                return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def create (self, trxContext, keyPath):
        self._log("create").error("called - shouldn't have happened for this transaction-hook. trxContext=%s, keyPath=%s", 
                                  trxContext, keyPath)

        return ReturnCodes.kOk

    def remove (self, trxContext, keyPath):
        self._log("remove").debug2("called. trxContext=%s, keyPath=%s", trxContext, keyPath)

        valLeafTag = keyPath.getAt(keyPath.getLen()-1).asXmlTag()
        self._log("remove-details").debug2("read details: valLeafTag=%s. trxContext=%s, keyPath=%s", valLeafTag, trxContext, keyPath)

        pathToDelete = copy.deepcopy(self._keyPathSnmpV2)

        doDelete = False

        if valLeafTag[0] == "contact":
            valContact = Value()
            (tag, ns, prefix) = ("sysContact", "http://tail-f.com/ns/mibs/SNMPv2-MIB/200210160000Z", "SNMPv2_MIB")
            valContact.setXmlTag((tag, ns, prefix))
            pathToDelete.addKeyPathPostfix(valContact)
            doDelete = True

        if valLeafTag[0] == "location":
            valLocation = Value()
            (tag, ns, prefix) = ("sysLocation", "http://tail-f.com/ns/mibs/SNMPv2-MIB/200210160000Z", "SNMPv2_MIB")
            valLocation.setXmlTag((tag, ns, prefix))
            pathToDelete.addKeyPathPostfix(valLocation)
            doDelete = True

        if doDelete:
            res = self._maapiDomain.writeMaapi(None, None, trxContext, itemsToDelete=[pathToDelete])
            if res != ReturnCodes.kOk:
                self._log("remove-write-maapi-failed").notice("self._maapiDomain.writeMaapi() failed. pathToDelete=%s, trxContext=%s, keyPath=%s", pathToDelete, trxContext, keyPath)
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

