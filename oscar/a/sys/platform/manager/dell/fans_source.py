# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities 
# without explicit written permission from Qwilt.
# 
# Author: shmulika
#
__pychecker__ = 'maxrefs=20' 

# Fans Blinky Data
import a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.status.status_oper_data_gen # StatusOperData
import a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.fan.device.status.status_oper_data_gen #StatusOperData

import a.sys.platform.manager.dell.source
import a.sys.platform.dell.open_manage.omreport_parser


#-----------------------------------------------------------------------------#
class ReportedFansInformtion:
    """
    This POD simply contains several BlinkyDatas (because one Fans report produces many datas)
    """
    def __init__ (self):
        self.fansStatus = a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.status.status_oper_data_gen.StatusOperData()
        self.fansStatus.setAllRequested()
        self.fanDeviceStatusList = [] # of type: a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.fan.device.status.status_oper_data_gen.StatusOperData()

    def newDeviceStatus (self):
        deviceStatus = a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.fan.device.status.status_oper_data_gen.StatusOperData()
        deviceStatus.setAllRequested()
        self.fanDeviceStatusList.append(deviceStatus)
        return deviceStatus

#-----------------------------------------------------------------------------#

class FansSource(a.sys.platform.manager.dell.source.Source):
    OMREPORT_ARGS = ["chassis", "fans"]

    def __init__ (self, logger):
        a.sys.platform.manager.dell.source.Source.__init__(self, "fans", logger, FansSource.OMREPORT_ARGS)
        self._initComparisonFilter("(^Reading\s*:\s*)(\d*)(\s*RPM\s*$)", r'\1REPLACED\3')


    def _createHeaderUnit (self):
        """ See Base
        """
        headerUnit = a.sys.platform.dell.open_manage.omreport_parser.OmreportUnit(self._log, "header", titleString = "Fan Probes Information")
        headerUnit.addField("Redundancy Status",          mandatory = False, allowMany = False)
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
        elementUnitList = a.sys.platform.dell.open_manage.omreport_parser.OmreportUnitList(self._log, "element-list", elementUnit, titleString = "Probe List")
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

        fansInformation = ReportedFansInformtion()        

        fansInformation.fansStatus.setAllRequested()
        if headerUnit.hasParsedField("Redundancy Status"):
            fansInformation.fansStatus.setRedundancyStatusRaw(headerUnit.getParsedField("Redundancy Status"))
        
        for parsedElement in elementUnitList.getParsedUnits():
            deviceStatus = fansInformation.newDeviceStatus()
            deviceStatus.setAllRequested()
            if parsedElement.hasParsedField("Probe Name"):
                deviceStatus.setProbeName(parsedElement.getParsedField("Probe Name"))
            if parsedElement.hasParsedField("Status"):
                deviceStatus.setStatusRaw(parsedElement.getParsedFieldCommaSeperated("Status"))
            if parsedElement.hasParsedField("Index"):
                deviceStatus.setIndex(parsedElement.getParsedFieldCommaSeperated("Index"))
            if parsedElement.hasParsedField("Reading"):                         
                deviceStatus.setCurrentRpm(parsedElement.getParsedFieldCommaSeperated("Reading"))
            if parsedElement.hasParsedField("Minimum Warning Threshold"):
                deviceStatus.setMinimumWarningRpm(parsedElement.getParsedFieldCommaSeperated("Minimum Warning Threshold"))
            if parsedElement.hasParsedField("Maximum Warning Threshold"):
                deviceStatus.setMaximumWarningRpm(parsedElement.getParsedFieldCommaSeperated("Maximum Warning Threshold")) 
            if parsedElement.hasParsedField("Minimum Failure Threshold"):
                deviceStatus.setMinimumErrorRpm(parsedElement.getParsedFieldCommaSeperated("Minimum Failure Threshold")) 
            if parsedElement.hasParsedField("Maximum Failure Threshold"):
                deviceStatus.setMaximumErrorRpm(parsedElement.getParsedFieldCommaSeperated("Maximum Failure Threshold")) 
            self._log("parse-text-element").debug2("constructed %s from the parsed element %s", deviceStatus, parsedElement)

        return fansInformation

