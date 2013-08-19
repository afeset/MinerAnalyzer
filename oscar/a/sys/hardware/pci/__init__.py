# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: effiz

G_NAME_MODULE_SYS_HARDWARE_PCI = "sys-hardware-pci"
G_NAME_GROUP_SYS_HARDWARE_PCI_HAL = "hal"


import os
from a.infra.basic.return_codes import ReturnCodes


if  __package__ is None:
    G_NAME_MODULE_SYS_HARDWARE_PCI = "unknown"
    G_NAME_GROUP_SYS_HARDWARE_PCI_HAL = "unknown"
else:
    from . import G_NAME_MODULE_SYS_HARDWARE_PCI
    from . import G_NAME_GROUP_SYS_HARDWARE_PCI_HAL


# Constants
DEFAULT_SYS_PCI_DEVICE_DIR = "/sys/bus/pci/devices/"
DEFAULT_VENDOR_FILE_NAME = "vendor"
DEFAULT_DEVICE_FILE_NAME = "device"


class PciHal(object):

    def __init__ (self, logger):
        self._log = logger.createLogger(G_NAME_MODULE_SYS_HARDWARE_PCI, G_NAME_GROUP_SYS_HARDWARE_PCI_HAL)


    def init(self,deviceDir=DEFAULT_SYS_PCI_DEVICE_DIR, vendorFileName=DEFAULT_VENDOR_FILE_NAME, deviceFileName=DEFAULT_DEVICE_FILE_NAME):
        if not os.path.isdir(deviceDir):
            self._log("bad-device-dir").error("Bad device directory '%s' - non existent or not a dir",deviceDir)
            return False # TODO - change to return codes or exception

        self._deviceDir      = deviceDir
        self._vendorFileName = vendorFileName
        self._deviceFileName = deviceFileName
        return True # TODO - change to return codes or exception

    def getDevicePciAddressByDeviceId(self,vendorId,deviceId,index):
        """
        Get a pci device id by vendorId, deviceId and index.
        
        Args:
            vendorId (number)
            deviceId (number)
            index

        Returns:
            A string representing the pci address (in the form of xxxx:xx:xx.x , e.g. 0000:03:00.0)
            or None if no much was found.
        """

        return self.getDevicePciAddressByDeviceIdList(vendorId,[deviceId],index)

          
    def getDevicePciAddressByDeviceIdList(self,vendorId,deviceIds,index):
        """
        Get a pci device id by vendorId, multiple deviceIds and index.
        
        Args:
            vendorId (number)
            deviceId list (number,...)
            index

        Returns:
            A string representing the pci address (in the form of xxxx:xx:xx.x , e.g. 0000:03:00.0)
            or None if no much was found.
        """

        deviceIdStrList = ['0x%04x' % deviceId for deviceId in deviceIds]

        try:
            matchCount = 0
            # Scan the device directory for a match on vendor id and device id
            for pciAddress in sorted(os.listdir(self._deviceDir)):
                curVendorPath = os.path.join(self._deviceDir,pciAddress,self._vendorFileName)
                curDevicePath = os.path.join(self._deviceDir,pciAddress,self._deviceFileName)
    
                # Read the files' content of vendor and device
                curVendorFd = open(curVendorPath,"r")
                curVendorId = int(curVendorFd.readline(),16)
                curVendorFd.close()
                curDeviceFd = open(curDevicePath,"r")
                curDeviceId = int(curDeviceFd.readline(),16)
                curDeviceFd.close()
                self._log("a-device-found").debug4("a device with vendorId=0x%04x and deviceId=0x%04x was found in pci address %s.",vendorId,deviceId,pciAddress)
    
                # handle found match - append to list of potential matches
                if ((curVendorId==vendorId) and (curDeviceId in deviceIds)):
                    if (index == matchCount):
                        self._log("matching-device-found-on-index").debug1("matching device with vendorId=0x%04x ,deviceId=0x%04x and index=%d was found in pci address %s.",curVendorId,curDeviceId,index,pciAddress)
                        return pciAddress
                    else:
                        self._log("matching-device-found-not-on-index").debug2("matching device with vendorId=0x%04x ,deviceIds=%s and index=%d (requestedIndex was %d) was found in pci address %s.",vendorId,deviceIdStrList,matchCount,index,pciAddress)
                        matchCount+=1
        except:
            self._log("scan-failed-on-device-dir").exception("Failed to scan %s for pci id.",self._deviceDir)
            return None

        # if you got here, you didn't find the device
        self._log("no-matching-device-found").warning("Matching device with vendorId=0x%04x, deviceId=%s and index=%d was not found.",vendorId,deviceIdStrList,index)
        return None
