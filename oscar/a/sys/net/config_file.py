# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: yoave

import a.sys.net.lnx.common
import os
import shutil
import json
import copy

#-----------------------------------------------------------------------------------------------------------------------
class _BaseConfigJson(object):
    def __init__(self, filename):
        self.logger = None
        self.filename = filename
        self.tempfile = "%s.tmp" % filename

    def initLogger(self, logger):
        self.logger = logger

    def isExists(self):
        return os.path.exists(self.filename)

    def dumpData(self):
        """dump data into a json file"""

        data = self.__dict__.copy()
        data.pop("filename")
        data.pop("tempfile")
        data.pop("logger")

        self._modifyDataToDump(data)

        if self.logger: self.logger("dump-data-cfg").debug3("%s: dump data - %s", self.filename, data)

        fd =  open(self.tempfile, 'w')
        json.dump(data, fd, indent=4)
        fd.close()

    def commit(self):
        if self.logger: self.logger("commit-cfg").debug3("%s: from %s commit data", self.filename, self.tempfile)
        shutil.move(self.tempfile, self.filename)
        self.update()

    def abort(self):
        if self.logger: self.logger("abort-cfg").debug3("%s: abort data", self.tempfile)
        os.remove(self.tempfile)

    def update(self):
        pass
       
    def clear(self):
        pass

    def _modifyDataToDump(self, data):
        pass

    def __str__(self):
        return str(self.__dict__)

#-----------------------------------------------------------------------------------------------------------------------
class DeliveryIp(object):
    def __init__(self, aPrefixLen):
        self.deliveryIP = ""
        self.deliveryGateway = ""
        self.deliveryPrefixLen = aPrefixLen

    def clear(self, aPrefixLen):
        self.deliveryIP = ""
        self.deliveryGateway = ""
        self.deliveryPrefixLen = aPrefixLen

class DeliveryInterface(object):
    def __init__(self):
        self.interfaceName = ""
        self.osDevice = ""
        self.deliveryIPv4=DeliveryIp(32)
        self.deliveryIPv6=DeliveryIp(64)
        self.hostname = ""
        self.adminEnable = False

    def clear(self):
        self.interfaceName = ""
        self.osDevice = ""
        self.deliveryIPv4.clear(32)
        self.deliveryIPv6.clear(64) 
        self.hostname = ""
        self.adminEnable = False

class LineInterface(object):
    def __init__(self):
        self.interfaceName = ""
        self.pciIndex = -1
        self.preferredDeliveryInterface = ""
        self.adminEnable = False

    def clear(self):
        self.interfaceName = ""
        self.pciIndex = -1
        self.preferredDeliveryInterface = ""
        self.adminEnable = False

class LanIpv6Redirects(object):
    def __init__(self):
        self.enabled = True
        self.maxRequestsPerSec = 100
        self.requestsQueueSize = 100

class LineConfigFile(_BaseConfigJson):
    DELIVERY_INTERFACES_KEY = "deliveryInterfaces"
    LINE_INTERFACES_KEY     = "lineInterfaces"
    IPV6_LAN_REDIRECTS_KEY  = "lanIpv6Redirects"
    
    def __init__(self, file):
        self.configId=0
        self.deliveryInterfaceFailover=False

        # delivery interface list
        delivery1 = DeliveryInterface()
        delivery2 = DeliveryInterface()
        self.deliveryInterfaces = [delivery1,delivery2]

        # line interface list
        self.lineInterfaces = []

        # lan IPv6 redirects
        self.lanIpv6Redirects = LanIpv6Redirects()

        _BaseConfigJson.__init__(self, file)

    def dumpData(self):
        self.configId+=1
        _BaseConfigJson.dumpData(self)

    def clear(self):
        self.deliveryInterfaceFailover=False

        # clear delivery list
        for delivery in self.deliveryInterfaces:
            delivery.clear()

        # clear line list
        self.lineInterfaces[:] = []

    def addLineInterface(self, name, pciIndex, preferredDeliveryInterface, adminEnable):
        line = LineInterface()
        line.interfaceName = name
        line.pciIndex = pciIndex
        line.preferredDeliveryInterface = preferredDeliveryInterface
        line.adminEnable = adminEnable
        self.lineInterfaces.append(line)

    def _modifyDataToDump(self, data):
        # prepare delivery list
        deliveryIfList = []
        for delivery in self.deliveryInterfaces:
            deliveryData = delivery.__dict__.copy()
            deliveryData["deliveryIPv4"] = delivery.deliveryIPv4.__dict__
            deliveryData["deliveryIPv6"] = delivery.deliveryIPv6.__dict__

            deliveryIfList.append(deliveryData)

        # prepare line list
        lineIfList = []
        for line in self.lineInterfaces:
            lineData = line.__dict__.copy()

            lineIfList.append(lineData)

        # modify data
        data[LineConfigFile.DELIVERY_INTERFACES_KEY]= deliveryIfList
        data[LineConfigFile.LINE_INTERFACES_KEY]    = lineIfList
        data[LineConfigFile.IPV6_LAN_REDIRECTS_KEY] = self.lanIpv6Redirects.__dict__

#-----------------------------------------------------------------------------------------------------------------------
class DeliveryIpState(object):
    def __init__(self):
        self.serviceStatus = False
        self.deliveryGatewayMac = ""

class DeliveryInterfacStateGpb(object):
    def __init__(self):
        self.interfaceName = ""
        self.deliveryIPv4State=DeliveryIpState()
        self.deliveryIPv6State=DeliveryIpState()

class LineStateFile(_BaseConfigJson):
    DELIVERY_INTERFACES_KEY = "deliveryInterfaces"
    
    def __init__(self, file):
        
        # interface map
        delivery1 = DeliveryInterfacStateGpb()
        delivery2 = DeliveryInterfacStateGpb()
        self.deliveryInterfaces = [delivery1,delivery2]

        _BaseConfigJson.__init__(self, file)

    def _modifyDataToDump(self, data):
        deliveryIfList = []
        for delivery in self.deliveryInterfaces:
            deliveryData = delivery.__dict__.copy()
            deliveryData["deliveryIPv4State"] = delivery.deliveryIPv4State.__dict__
            deliveryData["deliveryIPv6State"] = delivery.deliveryIPv6State.__dict__
            deliveryIfList.append(deliveryData)

        data[LineStateFile.DELIVERY_INTERFACES_KEY] = deliveryIfList

#-----------------------------------------------------------------------------------------------------------------------
class NeighborTableLineEntry(object):
    def __init__(self):
        self.ip = ""
        self.mac = ""

class NeighborTableInterfaceEntryGpb(object):
    def __init__(self):
        self.deviceName = ""
        self.tableLine = []
       
class NeighborTable(object):
    def __init__(self):
        neighborTable1 = NeighborTableInterfaceEntryGpb()
        neighborTable2 = NeighborTableInterfaceEntryGpb()
        self.interfaceNeighborTableList = [neighborTable1, neighborTable2]
    def __eq__(self, other):
        if not isinstance(other,NeighborTable):
            return False
        if len(self.interfaceNeighborTableList) != len(other.interfaceNeighborTableList):
            return False
        for selfInterface,otherInterface in zip(self.interfaceNeighborTableList, other.interfaceNeighborTableList):
            if selfInterface.deviceName != otherInterface.deviceName:
                return False
            if len(selfInterface.tableLine) != len(otherInterface.tableLine):
                return False
            for selfTableLine,otherTableLine in zip(selfInterface.tableLine, otherInterface.tableLine):
                if selfTableLine.ip != otherTableLine.ip:
                    return False
                if selfTableLine.mac != otherTableLine.mac:
                    return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__ (self):
        printList = []
        for neighborTable in self.interfaceNeighborTableList:
            tableLines = []
            for tableLine in neighborTable.tableLine:
                tableLines.append((tableLine.ip, tableLine.mac))
            printList.append((neighborTable.deviceName,tableLines))
        return str(printList)

    def copy (self,other):
        if not isinstance(other,NeighborTable):
            return
        self.interfaceNeighborTableList = copy.deepcopy(other.interfaceNeighborTableList)

class LineNeighborTableFile(_BaseConfigJson):
    INTERFACE_NEIGHBOR_TABLE_KEY = "neighborTables"


    def __init__(self, file):
        self.updateId = 0
        self.neighborTables = NeighborTable()
        _BaseConfigJson.__init__(self, file)

    def clearInterfaceNeighborTables(self):
        for interfaceNeighborTable in self.neighborTables.interfaceNeighborTableList:
            interfaceNeighborTable.tableLine = []

    def dumpData(self):
        self.updateId+=1
        _BaseConfigJson.dumpData(self)

    def _modifyDataToDump(self, data):
        interfaceNeighborTableList = []
        for neighborTable in self.neighborTables.interfaceNeighborTableList:
            interfaceNeighborTableData = neighborTable.__dict__.copy()

            neighborTableData = []
            for neighborTableLine in interfaceNeighborTableData["tableLine"]:
                neighborTableData.append(neighborTableLine.__dict__)
            interfaceNeighborTableData["tableLine"] = neighborTableData
            interfaceNeighborTableList.append(interfaceNeighborTableData)

        data[LineNeighborTableFile.INTERFACE_NEIGHBOR_TABLE_KEY] = interfaceNeighborTableList
            
#-----------------------------------------------------------------------------------------------------------------------
class SysWebConfigFile(_BaseConfigJson):

    UPDATE_OSCAR_COMMAND = ""

    def __init__(self, file):

        self.mngIp = ""
        _BaseConfigJson.__init__(self, file)

    def update(self):
        # run oscar core --update
        a.sys.net.lnx.common.Command.execute(self.logger, os.path.basename(self.filename),
                                             SysWebConfigFile.UPDATE_OSCAR_COMMAND, blocking=False)

    def clear(self):
        self.mngIp = ""

    @staticmethod
    def setUpdateCommand(cmd):
        SysWebConfigFile.UPDATE_OSCAR_COMMAND = cmd


#-----------------------------------------------------------------------------------------------------------------------
##############################################
# This class enables basic connectivity to the machine in maintenance mode:
# configures static IPs, default gateway and hostname
##############################################
class EarlyConfigFile(_BaseConfigJson):
    def __init__(self, file):

        self.ip = {}
        self.gw = ""
        self.host = ""
        _BaseConfigJson.__init__(self, file)

    def clear(self):
        self.ip = {}
        self.gw = ""
        self.host = ""



