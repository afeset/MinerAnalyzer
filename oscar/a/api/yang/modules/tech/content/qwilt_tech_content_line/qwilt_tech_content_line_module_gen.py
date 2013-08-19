
# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes


class DispatcherInterfaceType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kDpdk=_Type_(1, "kDpdk", "dpdk")
    
    kPcap=_Type_(3, "kPcap", "pcap")
    
    kJake=_Type_(2, "kJake", "jake")
    

    @staticmethod
    def isValidValue (value):
        return DispatcherInterfaceType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return DispatcherInterfaceType._Type_.getByValue(value)


class AnalyzerUnitModeType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kProcessPackets=_Type_(0, "kProcessPackets", "process-packets")
    
    kDiscardPackets=_Type_(1, "kDiscardPackets", "discard-packets")
    

    @staticmethod
    def isValidValue (value):
        return AnalyzerUnitModeType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return AnalyzerUnitModeType._Type_.getByValue(value)




"""
Extracted from the below data: 
{
    "conditionalDebugName": null, 
    "enumTypes": [
        {
            "className": "DispatcherInterfaceType", 
            "enums": [
                {
                    "yangName": "dispatcher_interface_type_dpdk", 
                    "displayName": "dpdk", 
                    "name": "kDpdk", 
                    "value": "1"
                }, 
                {
                    "yangName": "dispatcher_interface_type_pcap", 
                    "displayName": "pcap", 
                    "name": "kPcap", 
                    "value": "3"
                }, 
                {
                    "yangName": "dispatcher_interface_type_jake", 
                    "displayName": "jake", 
                    "name": "kJake", 
                    "value": "2"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.qwilt_tech_content_line_module_gen import DispatcherInterfaceType"
        }, 
        {
            "className": "AnalyzerUnitModeType", 
            "enums": [
                {
                    "yangName": "analyzer_unit_mode_process_packets", 
                    "displayName": "process-packets", 
                    "name": "kProcessPackets", 
                    "value": "0"
                }, 
                {
                    "yangName": "analyzer_unit_mode_discard_packets", 
                    "displayName": "discard-packets", 
                    "name": "kDiscardPackets", 
                    "value": "1"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.qwilt_tech_content_line_module_gen import AnalyzerUnitModeType"
        }
    ], 
    "createTime": "2013", 
    "module": {
        "prefix": "qtc_line"
    }, 
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "content", 
            "qwilt_tech_content_line"
        ]
    }
}
"""


