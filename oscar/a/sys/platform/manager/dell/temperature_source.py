# Copyright Qwilt, 2013
# 
# The code contained in this file may not be used by any other entities 
# without explicit written permission from Qwilt.
# 
# Author: shmulika
#
__pychecker__ = 'maxrefs=20' 

# Tempearture Blinky Data
import a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.tech.platform.temperature.status.status_oper_data_gen # StatusOperData
import a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.tech.platform.temperature.sensor.device.status.status_oper_data_gen #StatusOperData

import a.sys.platform.manager.dell.source
import a.sys.platform.dell.open_manage.omreport_parser


#-----------------------------------------------------------------------------#
class ReportedTemperatureInformtion:
    """
    This POD simply contains several BlinkyDatas (because one temperature report produces many datas)
    """
    def __init__ (self):
        self.temperatureStatus = a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.tech.platform.temperature.status.status_oper_data_gen.StatusOperData()
        self.temperatureStatus.setAllRequested()
        self.sensorDeviceStatusList = [] # of type: a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.tech.platform.temperature.sensor.device.status.status_oper_data_gen.StatusOperData()

    def newDeviceStatus (self):
        deviceStatus = a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.tech.platform.temperature.sensor.device.status.status_oper_data_gen.StatusOperData()
        deviceStatus.setAllRequested()
        self.sensorDeviceStatusList.append(deviceStatus)
        return deviceStatus

#-----------------------------------------------------------------------------#

class TemperatureSource(a.sys.platform.manager.dell.source.Source):
    OMREPORT_ARGS = ["chassis", "temps"]

    def __init__ (self, logger):
        a.sys.platform.manager.dell.source.Source.__init__(self, "temperature", logger, TemperatureSource.OMREPORT_ARGS)
        self._initComparisonFilter("(^Reading\s*:\s*)(\d*)(\.\d*)?(\s*C\s*$)", r'\1REPLACED\4')


    def _createHeaderUnit (self):
        """ See Base
        """
        headerUnit = a.sys.platform.dell.open_manage.omreport_parser.OmreportUnit(self._log, "header", titleString = "Temperature Probes Information")
        headerUnit.addField("Main System Chassis Temperatures",          mandatory = False, allowMany = False)
        return headerUnit

    def _createListUnit (self):
        """ See Base
        """
        elementUnit = a.sys.platform.dell.open_manage.omreport_parser.OmreportUnit(self._log, "element", titleField = "Index")
        elementUnit.addField("Index                     ", mandatory = True,  allowMany = False)
        elementUnit.addField("Status                    ", mandatory = True,  allowMany = False)
        elementUnit.addField("Probe Name                ", mandatory = True,  allowMany = False)
        elementUnit.addField("Reading                   ", mandatory = False, allowMany = True)
        elementUnit.addField("Minimum Warning Threshold ", mandatory = False, allowMany = True)
        elementUnit.addField("Maximum Warning Threshold ", mandatory = False, allowMany = True)
        elementUnit.addField("Minimum Failure Threshold ", mandatory = False, allowMany = True)
        elementUnit.addField("Maximum Failure Threshold ", mandatory = False, allowMany = True)        
        elementUnitList = a.sys.platform.dell.open_manage.omreport_parser.OmreportUnitList(self._log, "element-list", elementUnit, titleField = "Index", isTitlePartOfUnit = True)
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

        temperatureInformation = ReportedTemperatureInformtion()        

        temperatureInformation.temperatureStatus.setAllRequested()
        if headerUnit.hasParsedField("Main System Chassis Temperatures"):
            temperatureInformation.temperatureStatus.setTemperatureStatusRaw(headerUnit.getParsedField("Main System Chassis Temperatures"))
        
        for parsedElement in elementUnitList.getParsedUnits():
            deviceStatus = temperatureInformation.newDeviceStatus()
            deviceStatus.setAllRequested()
            if parsedElement.hasParsedField("Probe Name"):
                deviceStatus.setProbeName(parsedElement.getParsedField("Probe Name"))
            if parsedElement.hasParsedField("Status"):
                deviceStatus.setStatusRaw(parsedElement.getParsedFieldCommaSeperated("Status"))
            if parsedElement.hasParsedField("Index"):
                deviceStatus.setIndex(parsedElement.getParsedFieldCommaSeperated("Index"))
            if parsedElement.hasParsedField("Reading"):                         
                deviceStatus.setTemperatureRaw(parsedElement.getParsedFieldCommaSeperated("Reading"))
            if parsedElement.hasParsedField("Minimum Warning Threshold"):
                deviceStatus.setMinimumWarningRaw(parsedElement.getParsedFieldCommaSeperated("Minimum Warning Threshold"))
            if parsedElement.hasParsedField("Maximum Warning Threshold"):
                deviceStatus.setMaximumWarningRaw(parsedElement.getParsedFieldCommaSeperated("Maximum Warning Threshold")) 
            if parsedElement.hasParsedField("Minimum Failure Threshold"):
                deviceStatus.setMinimumCriticalRaw(parsedElement.getParsedFieldCommaSeperated("Minimum Failure Threshold")) 
            if parsedElement.hasParsedField("Maximum Failure Threshold"):
                deviceStatus.setMaximumCriticalRaw(parsedElement.getParsedFieldCommaSeperated("Maximum Failure Threshold")) 
            self._log("parse-text-element").debug2("constructed %s from the parsed element %s", deviceStatus, parsedElement)

        return temperatureInformation

