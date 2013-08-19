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

from a.api.yang.modules.tech.common.qwilt_tech_snmp.tech.snmp.counters.counters_oper_data_gen import CountersOperData

import copy


# Bypass for PyChecker
if  __package__ is None:
    G_GROUP_NAME_SNMP_MANAGER_BLINKY_COUNTERS_TRANSFORMATOR           = "unknown"
else:
    from . import G_GROUP_NAME_SNMP_MANAGER_BLINKY_COUNTERS_TRANSFORMATOR


class CountersTransformator(object):

    def __init__ (self, logger, maapiDomain):
        self._log = logger.createLoggerSameModule(G_GROUP_NAME_SNMP_MANAGER_BLINKY_COUNTERS_TRANSFORMATOR)
        self._maapiDomain = maapiDomain

        self.targetKeyPath = KeyPath()

        valCommunity = Value()
        (tag, ns, prefix) = ("SNMPv2-MIB", "http://tail-f.com/ns/mibs/SNMPv2-MIB/200210160000Z", "SNMPv2_MIB")
        valCommunity.setXmlTag((tag, ns, prefix))
        self.targetKeyPath.addKeyPathPostfix(valCommunity)

        valCommunityTable = Value()
        (tag, ns, prefix) = ("snmp", "http://tail-f.com/ns/mibs/SNMPv2-MIB/200210160000Z", "SNMPv2_MIB")
        valCommunityTable.setXmlTag((tag, ns, prefix))
        self.targetKeyPath.addKeyPathPostfix(valCommunityTable)



    def readSnmpCounters (self, operData):
        self._log("read-snmp-counters").debug3("called. operData=%s", operData)

        tagValueList = TagValues()

        if operData.isInPacketsRequested():
            posValInPkts = tagValueList.getLen()
            valInPkts = Value()
            tagValueList.push(("snmpInPkts", "http://tail-f.com/ns/mibs/SNMPv2-MIB/200210160000Z"), valInPkts)

        if operData.isInBadVersionPacketsRequested():
            posValInBadVersions = tagValueList.getLen()
            valInBadVersions = Value()
            tagValueList.push(("snmpInBadVersions", "http://tail-f.com/ns/mibs/SNMPv2-MIB/200210160000Z"), valInBadVersions)

        if operData.isInBadCommunityPacketsRequested():
            posValInBadCommunityNames = tagValueList.getLen()
            valInBadCommunityNames = Value()
            tagValueList.push(("snmpInBadCommunityNames", "http://tail-f.com/ns/mibs/SNMPv2-MIB/200210160000Z"), valInBadCommunityNames)

        if operData.isInBadCommunityUsePacketsRequested():
            posValInBadCommunityUses = tagValueList.getLen()
            valInBadCommunityUses = Value()
            tagValueList.push(("snmpInBadCommunityUses", "http://tail-f.com/ns/mibs/SNMPv2-MIB/200210160000Z"), valInBadCommunityUses)

        if operData.isInAsnParseErrorsRequested():
            posValInASNParseErrs = tagValueList.getLen()
            valInASNParseErrs = Value()
            tagValueList.push(("snmpInASNParseErrs", "http://tail-f.com/ns/mibs/SNMPv2-MIB/200210160000Z"), valInASNParseErrs)

        if operData.isSilentDroppedPacketsRequested():
            posValSilentDrops = tagValueList.getLen()
            valSilentDrops = Value()
            tagValueList.push(("snmpSilentDrops", "http://tail-f.com/ns/mibs/SNMPv2-MIB/200210160000Z"), valSilentDrops)

        res = self._maapiDomain.readMaapi(tagValueList, self.targetKeyPath, None)
        if res != ReturnCodes.kOk:
            self._log('read-snmp-counters-domain-failed').error('self._maapiDomain.readMaapi() failed. operData=%s', operData)
            return None

        if operData.isInPacketsRequested():
            operData.setInPackets(tagValueList.getAt(posValInPkts)[1].asUint32())

        if operData.isInBadVersionPacketsRequested():
            self._log("read-snmp-counters-got-in-bad-version").debug3("got snmpInBadVersions=%s", tagValueList.getAt(posValInBadVersions)[1])
            operData.setInBadVersionPackets(tagValueList.getAt(posValInBadVersions)[1].asUint32())

        if operData.isInBadCommunityPacketsRequested():
            operData.setInBadCommunityPackets(tagValueList.getAt(posValInBadCommunityNames)[1].asUint32())

        if operData.isInBadCommunityUsePacketsRequested():
            operData.setInBadCommunityUsePackets(tagValueList.getAt(posValInBadCommunityUses)[1].asUint32())

        if operData.isInAsnParseErrorsRequested():
            operData.setInAsnParseErrors(tagValueList.getAt(posValInASNParseErrs)[1].asUint32())

        if operData.isSilentDroppedPacketsRequested():
            operData.setSilentDroppedPackets(tagValueList.getAt(posValSilentDrops)[1].asUint32())

        self._log("read-snmp-counters-done").debug3("returning: operData=%s", operData)
        return ReturnCodes.kOk


