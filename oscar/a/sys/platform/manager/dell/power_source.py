# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities 
# without explicit written permission from Qwilt.
# 
# Author: shmulika
#
__pychecker__ = 'maxrefs=20' 

# Power Blinky Data
import a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.status.status_oper_data_gen #StatusOperData
import a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.power_supply.device.status.status_oper_data_gen #StatusOperData

import a.sys.platform.manager.dell.source
import a.sys.platform.dell.open_manage.omreport_parser


#-----------------------------------------------------------------------------#
class ReportedPowerSuppliesInformtion:
    """
    This POD simply contains several BlinkyDatas (because one PowerSupplies report produces many datas)
    """
    def __init__ (self):                           
        self.powerStatus = a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.status.status_oper_data_gen.StatusOperData()        
        self.powerStatus.setAllRequested()        
        self.subsystemStatusRaw = None # When this is not None, it means RedundancyStatusRaw is formatted differently (as a "sub-system status" string)
        self.powerSupplyDeviceStatusList = []

    def newDeviceStatus (self):
        deviceStatus = a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.power_supply.device.status.status_oper_data_gen.StatusOperData()
        deviceStatus.setAllRequested()
        self.powerSupplyDeviceStatusList.append(deviceStatus)
        return deviceStatus

#-----------------------------------------------------------------------------#
class PowerSource(a.sys.platform.manager.dell.source.Source):
    OMREPORT_ARGS = ["chassis", "pwrsupplies"]

    def __init__ (self, logger):
        a.sys.platform.manager.dell.source.Source.__init__(self, "power-supplies", logger, PowerSource.OMREPORT_ARGS)

    def _createHeaderUnit (self):
        """ See Base
        """
        headerUnit = a.sys.platform.dell.open_manage.omreport_parser.OmreportUnit(self._log, "header", titleString = "Power Supplies Information")
        headerUnit.addField("Redundancy Status",                    mandatory = False, allowMany = False)
        headerUnit.addField("Main System Chassis Power Supplies",   mandatory = False, allowMany = False)
        return headerUnit

    def _createListUnit (self):
        """ See Base
        """
        elementUnit = a.sys.platform.dell.open_manage.omreport_parser.OmreportUnit(self._log, "element", titleField = "Index")
        elementUnit.addField("Index                    ", mandatory = True,  allowMany = False)
        elementUnit.addField("Status                   ", mandatory = True,  allowMany = False)
        elementUnit.addField("Location                 ", mandatory = True,  allowMany = False)
        elementUnit.addField("Type                     ", mandatory = False, allowMany = True)
        elementUnit.addField("Rated Input Wattage      ", mandatory = False, allowMany = True)
        elementUnit.addField("Maximum Output Wattage   ", mandatory = False, allowMany = True)
        elementUnit.addField("Firmware Version         ", mandatory = False, allowMany = True)
        elementUnit.addField("Online Status            ", mandatory = False, allowMany = True)        
        elementUnit.addField("Power Monitoring Capable ", mandatory = False, allowMany = True)
        elementUnitList = a.sys.platform.dell.open_manage.omreport_parser.OmreportUnitList(self._log, "element-list", elementUnit, titleString = "Individual Power Supply Elements")
        return elementUnitList

    def _translateHeaderAndListUnit (self, headerUnit, elementUnitList):
        """"
        Takes the standard header and list units, after their fields parsed by the omreport parser.
        The method is to retrieve information from the parsed unit, create & store a data-structure containing that information.
        Note: this is done in a single method, instead of two methods, because a Lock should be placed around the update of the data.
        Return: The translated data, or None if parsing failed.
        """
        if headerUnit is None or elementUnitList is None:
            return None

        powerInformation = ReportedPowerSuppliesInformtion()        

        powerInformation.powerStatus.setAllRequested()
        if headerUnit.hasParsedField("Redundancy Status"):            
            powerInformation.powerStatus.setRedundancyStatusRaw(headerUnit.getParsedField("Redundancy Status"))
        elif headerUnit.hasParsedField("Main System Chassis Power Supplies"):                                                
            powerInformation.subsystemStatusRaw = headerUnit.getParsedField("Main System Chassis Power Supplies")
            powerInformation.powerStatus.setRedundancyStatusRaw(powerInformation.subsystemStatusRaw)
            
        for parsedElement in elementUnitList.getParsedUnits():
            deviceStatus = powerInformation.newDeviceStatus()
            deviceStatus.setAllRequested()            
            if parsedElement.hasParsedField("Location"):
                deviceStatus.setLocation(parsedElement.getParsedField("Location"))
            if parsedElement.hasParsedField("Index"):
                deviceStatus.setIndex(parsedElement.getParsedFieldCommaSeperated("Index"))
            if parsedElement.hasParsedField("Status"):
                deviceStatus.setStatusRaw(parsedElement.getParsedFieldCommaSeperated("Status"))
            if parsedElement.hasParsedField("Type"):
                deviceStatus.setInputType(parsedElement.getParsedFieldCommaSeperated("Type"))
            if parsedElement.hasParsedField("Rated Input Wattage"):
                deviceStatus.setRatedInputWattage(parsedElement.getParsedFieldCommaSeperated("Rated Input Wattage"))
            if parsedElement.hasParsedField("Maximum Output Wattage"):
                deviceStatus.setMaximumOutputWattage(parsedElement.getParsedFieldCommaSeperated("Maximum Output Wattage"))
            if parsedElement.hasParsedField("Firmware Version"):
                deviceStatus.setFirmwareVersion(parsedElement.getParsedFieldCommaSeperated("Firmware Version"))
            if parsedElement.hasParsedField("Online Status"):
                deviceStatus.setOnlineStatusRaw(parsedElement.getParsedFieldCommaSeperated("Online Status"))

        return powerInformation
