# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities 
# without explicit written permission from Qwilt.
# 
# Author: shmulika
#
import a.sys.platform.dell.open_manage.omreport_parser
import a.sys.platform.manager.dell.source


#-----------------------------------------------------------------------------#
class ReportedFruInformtion:
    """
    This POD class is used by the FruSource as output, because it is general for all the different devices
    """
    def __init__ (self):
        self.fruDevice = None
        self.serialNumber = None
        self.partNumber = None
        self.manufacturer = None
        self.manufacturerDate = None
        self.revision = None

#-----------------------------------------------------------------------------#

class FruSource(a.sys.platform.manager.dell.source.Source):
    """
    getData() returns a list of TempOperPowerSupplyDeviceStatus
    """
    OMREPORT_ARGS = ["chassis", "fru"]

    def __init__ (self, logger):
        a.sys.platform.manager.dell.source.Source.__init__(self, "fru", logger, FruSource.OMREPORT_ARGS)

    def _createHeaderUnit (self):
        """ See Base
        None - FRU report has no header unit
        """
        return None

    def _createListUnit (self):
        """ See Base        
        """
        elementUnit = a.sys.platform.dell.open_manage.omreport_parser.OmreportUnit(self._log, "element", titleField = "Device")
        elementUnit.addField("Device           ", mandatory = True,  allowMany = False)
        elementUnit.addField("Serial No.       ", mandatory = False, allowMany = True)
        elementUnit.addField("Part No.         ", mandatory = False, allowMany = True)
        elementUnit.addField("Revision         ", mandatory = False, allowMany = True)
        elementUnit.addField("Manufacturer     ", mandatory = False, allowMany = True)
        elementUnit.addField("Manufacture Date ", mandatory = False, allowMany = True)
        return a.sys.platform.dell.open_manage.omreport_parser.OmreportUnitList(self._log, "element-list", elementUnit, titleString = "System Components (FRU) Information")
    
    def _translateHeaderAndListUnit (self, headerUnit, elementUnitList):
        """"
        Takes the standard header and list units, after their fields parsed by the omreport parser.
        The method is to retrieve information from the parsed unit, create & store a data-structure containing that information.
        Note: this is done in a single method, instead of two methods, because a Lock should be placed around the update of the data.
        Return: The translated data, or None if parsing failed.
        """
        __pychecker__ = "unusednames=headerUnit"
        if elementUnitList is None:
            return None

        devicesInfos = []
        for parsedElement in elementUnitList.getParsedUnits():
            deviceInfo = ReportedFruInformtion()
            deviceInfo.fruDevice       = parsedElement.getParsedFieldCommaSeperated("Device")
            deviceInfo.serialNumber    = parsedElement.getParsedFieldCommaSeperated("Serial No.")
            deviceInfo.partNumber      = parsedElement.getParsedFieldCommaSeperated("Part No.         ")
            deviceInfo.revision        = parsedElement.getParsedFieldCommaSeperated("Revision         ")
            deviceInfo.manufacturer    = parsedElement.getParsedFieldCommaSeperated("Manufacturer     ") 
            deviceInfo.manufactureDate = parsedElement.getParsedFieldCommaSeperated("Manufacture Date ") 
            devicesInfos.append(deviceInfo)        

        return devicesInfos

