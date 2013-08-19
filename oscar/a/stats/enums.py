#!/usr/local/bin/python2.6
# 
# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# ver 1.0 
#
# Author: galm
#
########################################################################################################################
# 
# Aid of Stats script - enums
#                                                                                                                      #
########################################################################################################################
#
# === Globals - ENUMS =====================================================================================

class AggregationQueueJobType (object):
    VALUES = 0
    DESCRIPTORS = 1

class AggregationCounterType (object):
    """
    COUNTER = Only increments, integers only, stores the delta, not the value
    GAUGE = Same as counter, but can also decrease. ( integers only, stores the delta, not the value )    
    """
    COUNTER = "COUNTER"
    GAUGE = "GAUGE"
    ABSOLUTE = "ABSOLUTE"
    DERIVE = "DERIVE"
    #COMPUTE = 5 

    #This dictionary is used to get enum value's string names
    #VALNAMES = { 1:"COUNTER", 2:"GAUGE", 3:"DERIVE", 4:"ABSOLUTE" }
    #NAMESVAL = { "COUNTER":1, "GAUGE":2, "DERIVE":3, "ABSOLUTE":4 }

class OscarProcess (object):
    TOPPER = "topper"
    LINE = "line"
    CONFD = "confd"
    DELIVERY = "delivery"
    BLADE_MANAGER = "blade_manager"
    SYS_WEB = "sys_web"
    #ALL = "all" - to me it seemed that it might cause troubles and that duplicating for five processes is not that difficult/ugly

class AggregationConsolidationFunctionType (object):
    """
    Consolidation functions. Stores smaller data resolutions
    AVERAGE, MIN, MAX, LAST
    """
    AVERAGE = "AVERAGE"
    MIN = "MIN"
    MAX = "MAX"
    LAST = "LAST"

class VariableTypes (object):
    STRING = 'str'
    INTEGER = 'int'
    DOUBLE = 'doub'

    FORMAT_BY_NAMES = {
        "str":'%s',
        "int":'%d',
        "long":'%d',
        "float":'%f',
        "doub":'%f'
    }

class CommMethodTypes:
    QSHELL = 'qshell'
    FILE = 'file'
