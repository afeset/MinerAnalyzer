# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: yoave


from common import Command
from common import IpConstant
from common import IpOption
from common import IpAction
import os

##############################################
# ip link - network device configuration
# link is a network device and the corresponding commands display and change the state of devices
##############################################
class IpLink(object):

    STATISTICS_OPTION = "-statistics"

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def showDevices(logger):
        """This function list all devices

        Args:
            logger
            
        Return:
            tuple (rc, stdout, stderr) 

        Raise:
            None
        """

        rc =  Command.executeIp(logger, IpOption.LINK, IpAction.SHOW)   
        return rc 

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def showDevice(logger, device):
        """This function shows a device

        Args:
            logger
            device - the name specifies network device to show
            
        Return:
            tuple (rc, stdout, stderr) 

        Raise:
            None
        """

        rc =  Command.executeIp(logger, IpOption.LINK, IpAction.SHOW,
                                    IpConstant.DEV, device)   
        return rc 

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def showDeviceStatistics(logger, device):
        """This function shows a device statistics

        Args:
            logger
            device - the name specifies network device to show
            
        Return:
            tuple (rc, stdout, stderr) 

        Raise:
            None
        """

        rc =  Command.executeIp(logger, IpOption.LINK, IpLink.STATISTICS_OPTION, IpAction.SHOW,
                                    IpConstant.DEV, device)   
        return rc 

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def activateDevice(logger, device):
        """This function change the state of the device to UP

        Args:
            logger
            device - the name specifies network device to operate on
            
        Return:
            tuple (rc, stdout, stderr) 

        Raise:
            None
        """

        rc =  Command.executeIp(logger, IpOption.LINK, IpAction.SET, 
                                    device, IpConstant.UP)   
        return rc 

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def deactivateDevice(logger, device):
        """This function change the state of the device to DOWN

        Args:
            logger
            device - the name specifies network device to operate on
            
        Return:
            tuple (rc, stdout, stderr) 

        Raise:
            None
        """

        rc =  Command.executeIp(logger, IpOption.LINK, IpAction.SET, 
                                    device, IpConstant.DOWN)   
        return rc 

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def renameDevice(logger, device, name):
        """This function change the name of the device
        Note: This operation is not recommended if the device is running or has some addresses already configured

        Args:
            logger
            device - the name specifies network device to rename
            name   - change the name of the device
            
        Return:
            tuple (rc, stdout, stderr) 

        Raise:
            None
        """

        rc =  Command.executeIp(logger, IpOption.LINK, IpAction.SET, 
                                    IpConstant.DEV, device, IpConstant.NAME, name)   
        return rc 

##############################################
# ip address - protocol address management 
# The address is a protocol (IP or IPv6) address attached to a network device
##############################################
class IpAddress(object):

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def showAddresses(logger):
        """This function list all protocol addresseses

        Args:
            logger
            
        Return:
            tuple (rc, stdout, stderr) 

        Raise:
            None
        """
        rc =  Command.executeIp(logger, IpOption.ADDRESS, IpAction.SHOW)   
        return rc 

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def showAddress(logger, device):
        """This function list an device protocol addresseses

        Args:
            logger
            device - the name of the device to show
            
        Return:
            tuple (rc, stdout, stderr) 

        Raise:
            None
        """
        rc =  Command.executeIp(logger, IpOption.ADDRESS, IpAction.SHOW,
                                    IpConstant.DEV, device)   
        return rc 

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def addAddress(logger, address, device, version=None):
        """This function adds a new IP address

        Args:
            logger
            address - IP address to attach
            device - the name of the device to add the address to
            version - IPv4 or IPv6 as an integer, 4 or 6
            
        Return:
            tuple (rc, stdout, stderr) 

        Raise:
            None
        """

        if version:
            if version == 4:
                return Command.executeIp(logger, IpConstant.IPV4, IpOption.ADDRESS, IpAction.ADD, 
                            address, IpConstant.DEV, device)   
            elif version == 6:
                return Command.executeIp(logger, IpConstant.IPV6, IpOption.ADDRESS, IpAction.ADD, 
                            address, IpConstant.DEV, device)   

        rc =  Command.executeIp(logger, IpOption.ADDRESS, IpAction.ADD, 
                            address, IpConstant.DEV, device)   
        return rc 

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def deleteAddress(logger, address, device, version=None):
        """This function deletes an IP address

        Args:
            logger
            address - IP address to dettach
            device - the name of the device to delete the address from
            version - IPv4 or IPv6 as an integer, 4 or 6
            
        Return:
            tuple (rc, stdout, stderr) 

        Raise:
            None
        """

        if version:
            if version == 4:
                return Command.executeIp(logger, IpConstant.IPV4, IpOption.ADDRESS, IpAction.DELETE, 
                    address, IpConstant.DEV, device) 
            elif version == 6:
                return Command.executeIp(logger, IpConstant.IPV6, IpOption.ADDRESS, IpAction.DELETE, 
                    address, IpConstant.DEV, device) 

        rc =  Command.executeIp(logger, IpOption.ADDRESS, IpAction.DELETE, 
                    address, IpConstant.DEV, device)   
        return rc 

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def flushAddresses(logger, device, scope=None, version=None):
        """This function flushes all IP addresses assigned to a device

        Args:
            logger
            device - the name of the device to flush all addresses
            version - IPv4 or IPv6 as an integer, 4 or 6
            scope  -  the scope of the area where this address flush is valid: global, site, link, host
            
        Return:
            tuple (rc, stdout, stderr) 

        Raise:
            None
        """

        args = []

        if version:
            if version == 4:
                args.append(IpConstant.IPV4)
            elif version == 6:
                args.append(IpConstant.IPV6)

        args += [IpOption.ADDRESS, IpAction.FLUSH, IpConstant.DEV, device]

        if scope: args += [IpConstant.SCOPE, scope]

        option = args[0]
        cmd = args[1:]

        rc =  Command.executeIp(logger, option, *cmd)   
        return rc 


##############################################
# ethtool - Display or change ethernet card settings 
##############################################
class EthTool(object):

    ETH_TOOL_COMMAND_NAME = "/sbin/ethtool"

    STATISTICS_OPTION = "--statistics"
    CHANGE_OPTION = "--change"

    SPEED_SETTING = "speed"
    DUPLEX_SETTING = "duplx"
    AUTO_NEG_SETTING = "autoneg"

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def showEth(logger, device):
        """This function shows current settings of the specified device

        Args:
            logger
            device - device name
            
        Return:
            tuple (rc, stdout, stderr) 

        Raise:
            None
        """

        rc =  Command.execute(logger, EthTool.ETH_TOOL_COMMAND_NAME, 
                              [EthTool.ETH_TOOL_COMMAND_NAME, device])   
        return rc 

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def showEthStatistics(logger, device):
        """This function shows the specified ethernet device for NIC- and driver-specific statistics

        Args:
            logger
            device - device name
            
        Return:
            tuple (rc, stdout, stderr) 

        Raise:
            None
        """

        rc =  Command.execute(logger, EthTool.ETH_TOOL_COMMAND_NAME, 
                              [EthTool.ETH_TOOL_COMMAND_NAME, EthTool.STATISTICS_OPTION, device])   
        return rc 

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def setEth(logger, device, speed=None, fullduplex=True, autoneg=True):
        """This function changes some or all settings of the specified ethernet device 

        Args:
            logger
            device  - device name
            speed   - Set speed in Mb/s
            fullduplex  - Sets full or half duplex mode
            autoneg - Specifies whether autonegotiation should be enabled
            
        Return:
            tuple (rc, stdout, stderr) 

        Raise:
            None
        """

        args = [EthTool.ETH_TOOL_COMMAND_NAME, EthTool.CHANGE_OPTION, device]

        if speed:
            args += [EthTool.SPEED_SETTING, speed]

        args.append(EthTool.DUPLEX_SETTING)
        if fullduplex:
            args.append('full')
        else:
            args.append('half')

        args.append(EthTool.AUTO_NEG_SETTING)
        if autoneg:
            args.append('on')
        else:
            args.append('off')

        rc =  Command.execute(logger, EthTool.ETH_TOOL_COMMAND_NAME, 
                              args)   
        return rc 

##############################################
# This class holds device utilities
##############################################
class DeviceUtils(object):
    """This class holds device utilities"""

    # network info at /sys/class/net/
    INTERFACE_DIR_NAME = "/sys/class/net/"

    # interface info at /sys/class/net/eth0
    STATS_DIR_NAME = "statistics"
    OPER_STATE_FILE_NAME = "operstate"
    MAC_FILE_NAME = "address"
    MTU_FILE_NAME = "mtu"

    # device info at /sys/class/net/eth0/device
    DEVICE_DIR_NAME = "device"
    DEVICE_ID_FILE = "device"
    VENDOR_NAME_FILE = "vendor"

    # hardware data info at /usr/share/hwdata/
    HWADDR_DATA_FILE_NAME = "/usr/share/hwdata/pci.ids"

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def __getInfo(name, logger, device, dirname, filename):
        """This function returns the data in the given file"""

        target = os.path.join(dirname, filename)
        if not os.path.exists(target):
            if logger:
                logger("device-info-not-exsit").error("%s: %s info does not exist - %s", (name, device, target))
            return None

        info = ""
        try:
            fd = open(target, "r")
            info = fd.read().strip()
            fd.close()
        except IOError as (errno, strerror):  
            if logger:
                logger("device-info-faild").exception("%s: Failed to read from %s file - %s: I/O error(%d): {%s}", 
                                                      name, device, target, errno, strerror)
            return None

        return info

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def __getInterfaceInfo(name, logger, device, filename):
        """This function returns the requested interface information"""

        ethDir = os.path.join(DeviceUtils.INTERFACE_DIR_NAME,
                                device)

        info = DeviceUtils.__getInfo(name, logger, device, ethDir, filename)
        return info

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def __getDeviceInfo(name, logger, device, filename):
        """This function returns the requested device information"""

        deviceDir = os.path.join(DeviceUtils.INTERFACE_DIR_NAME,
                                device,
                                DeviceUtils.DEVICE_DIR_NAME)
        info = DeviceUtils.__getInfo(name, logger, device, deviceDir, filename)
        return info

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def __getEthDevicesByAttr(name, logger, key, value):
        """This function lists all ethernet devices that matches the given attribute"""

        deviceDir = os.path.join("*", DeviceUtils.DEVICE_DIR_NAME)

        (rc, stdout, stderr) = Command.execute(logger, name, 
                                               "grep \"\" %s" % os.path.join(deviceDir,key), 
                                               cwd=DeviceUtils.INTERFACE_DIR_NAME)

        if rc != 0:
            logger("device-attr-faild").error("Failed getting eths attribute: %s", key)
            return None

        output = stdout.splitlines()
        ethList = []

        for line in output:
            attr = line.split(':')[-1]

            if attr == value:
                deviceName = line.split('/')[0]
                ethList.append(deviceName)
            
        return ethList

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def getEthDevices():
        """This function lists all ethernet devices"""

        iList = os.listdir(DeviceUtils.INTERFACE_DIR_NAME)

        # filter interfaces for eth physical devices only
        # no lo, sit0, virbr0, etc.
        ethList = [iface for iface in iList if os.path.exists(os.path.join(DeviceUtils.INTERFACE_DIR_NAME,iface,DeviceUtils.DEVICE_DIR_NAME))]

        # sort by index
        ethList.sort()

        return ethList

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def getEthDevicesByDeviceId(name, logger, deviceid):
        """This function lists all ethernet devices that matches the given device id"""

        return DeviceUtils.__getEthDevicesByAttr(name, logger, 
                                                 DeviceUtils.DEVICE_ID_FILE, deviceid)

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def getEthDevicesByVendorId(name, logger, vendorid):
        """This function lists all ethernet devices that matches the given vendor id"""

        return DeviceUtils.__getEthDevicesByAttr(name, logger, 
                                                 DeviceUtils.VENDOR_NAME_FILE, vendorid)

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def getEthDeviceByPciAddress(pciAddress):

        iList = os.listdir(DeviceUtils.INTERFACE_DIR_NAME)

        for iface in iList:
            deviceSymLink = os.path.join(DeviceUtils.INTERFACE_DIR_NAME,iface,DeviceUtils.DEVICE_DIR_NAME)
            if os.path.exists(deviceSymLink):
                devicePath = os.path.realpath(deviceSymLink)
                if devicePath.endswith(pciAddress):
                    return iface

        return None

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def isDeviceExists(device):
        """This function returns whether the given device exists"""

        if device is None:
            return False

        ethDir = os.path.join(DeviceUtils.INTERFACE_DIR_NAME, device)
        return os.path.exists(ethDir)

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def getDeviceId(name, logger, device):
        """This function returns the device id"""

        deviceid = DeviceUtils.__getDeviceInfo(name, logger, device, DeviceUtils.DEVICE_ID_FILE)
        return deviceid

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def getVendorId(name, logger, device):
        """This function returns the device vendor id"""

        vendor = DeviceUtils.__getDeviceInfo(name, logger, device, DeviceUtils.VENDOR_NAME_FILE)
        return vendor

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def getOperState(name, logger, device):
        """This function returns the device operational state"""

        state = DeviceUtils.__getInterfaceInfo(name, logger, device, DeviceUtils.OPER_STATE_FILE_NAME)
        return state

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def getMacAddress(name, logger, device):
        """This function returns the device mac address"""

        mac = DeviceUtils.__getInterfaceInfo(name, logger, device, DeviceUtils.MAC_FILE_NAME)
        return mac

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def getMtu(name, logger, device):
        """This function returns the device maximum transmission unit (in bytes)"""

        mtu = DeviceUtils.__getInterfaceInfo(name, logger, device, DeviceUtils.MTU_FILE_NAME)
        if mtu and mtu.isdigit():
            return int(mtu)

        return None

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def getIpAddress(logger, device, version=4):
        """This function returns the device ip address"""

        (rc, stdout, stderr) = IpAddress.showAddress(logger, device)

        if rc != 0:
            return None

        # example:
        # 2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP qlen 1000
        #  link/ether 14:fe:b5:d4:11:cb brd ff:ff:ff:ff:ff:ff
        #  inet 10.9.8.11/24 brd 10.9.8.255 scope global eth0
        #  inet6 fe80::16fe:b5ff:fed4:11cb/64 scope link
        #  valid_lft forever preferred_lft forever
        output = stdout.splitlines()
        inetMap = {4:"inet ", 6:"inet6 "}

        for line in output:
            if (inetMap[version] in line) and ("global" in line):
                # e.g. 'inet 10.9.8.11/24 brd 10.9.8.255 scope global eth0'
                ip = line.split()[1]
                return ip

        return None

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def getPci(device):
        """This function returns the device pci ([doamin:]bus:device.function)"""

        # /sys/class/net/eth0/device (link)--> /sys/devices/pci0000:00/0000:00:16.0/0000:0b:00.0
        deviceDir = os.path.join(DeviceUtils.INTERFACE_DIR_NAME,
                                device,
                                DeviceUtils.DEVICE_DIR_NAME)
        deviceDir = os.path.realpath(deviceDir) 

        pci = os.path.basename(deviceDir) 
        return pci

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def getPciByIndex(logger, name, vendorid, deviceid, pciIndex):
        """This function returns the device pci (bus:device.function)"""

        (rc, stdout, stderr) = Command.execute(logger, name, 
                                               "/sbin/lspci -n | grep %s:%s" % (vendorid[2:], deviceid[2:]))

        if rc != 0:
            logger("device-lspci-faild").error("Failed getting '%s:%s-%s' lspci",vendorid, deviceid, pciIndex)
            return None

        # example:
        # 04:00.0 0200: 8086:10fb (rev 01)
        # 04:00.1 0200: 8086:10fb (rev 01)
        # 06:00.0 0200: 8086:10fb (rev 01)
        output = stdout.splitlines()

        pci = None
        if pciIndex < len(output):
            pci = output[pciIndex].split()[0]
        else:
            logger("device-lspci-bad-index").debug1("PCI list contains only %s devices of type '%s:%s' ", 
                                                    len(output), vendorid, deviceid)

        return pci

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def getStatistics(name, logger, device):
        """This function returns the device statistics"""

        statsDir = os.path.join(DeviceUtils.INTERFACE_DIR_NAME,
                                device,
                                DeviceUtils.STATS_DIR_NAME)

        (rc, stdout, stderr) = Command.execute(logger, name, 
                                               "grep \"\" *", 
                                               cwd=statsDir)

        if rc != 0:
            logger("device-stats-faild").error("Failed getting '%s' statistics", device)
            return None

        statsContainer = {}

        for pair in stdout.split():
            key,value = pair.split(":")
            statsContainer[key] = value

        return statsContainer

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def getVendorName(name, logger, vendorid):
        """This function returns the vendor name"""

        if vendorid.startswith("0x"):
            vendorid = vendorid[2:]

        (rc, stdout, stderr) = Command.execute(logger, name,
                                               "grep -E '^%s' %s" % (vendorid,DeviceUtils.HWADDR_DATA_FILE_NAME))

        if rc != 0:
            logger("vendor-name-faild").error("Failed getting '%s' vendor name", vendorid)
            return None

        vendorName = stdout[len(vendorid):].strip()
        return vendorName

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def getChipName(name, logger, deviceid):
        """This function returns the chip description"""

        if deviceid.startswith("0x"):
            deviceid = deviceid[2:]

        (rc, stdout, stderr) = Command.execute(logger, name,
                                               "grep '\< *%s\>' %s" % (deviceid,DeviceUtils.HWADDR_DATA_FILE_NAME))

        if rc != 0:
            logger("chip-name-faild").error("Failed getting '%s' chip name", deviceid)
            return None

        chipName = stdout.split(None,1)[1].strip()
        return chipName

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def getSpeed(logger, device):
        """This function returns the device speed in Mb/s"""

        rc = EthTool.showEth(logger, device)

        if Command.isReturnOk(rc):

            output = rc[1].splitlines()

            for line in output:
                if line.strip().startswith("Speed"):
                    # e.g. Speed: 1000Mb/s
                    speed = line[8:-4]

                    if speed.isdigit():
                        return int(speed)

        return None
