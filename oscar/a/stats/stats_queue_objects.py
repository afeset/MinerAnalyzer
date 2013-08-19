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
# Aid of Stats script
# This file defines the data structures used to pass messages in the prodecer Queue of the Stats script
#                                                                                                                      #
########################################################################################################################

from my_hash import myHash
import sys, traceback
import os
from UserString import MutableString


# === Globals - ENUMS =====================================================================================

class AggregationQueueJobType (object):
    VALUES = 0
    DESCRIPTORS = 1


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

# === Queue Objects =====================================================================================

class AbstractAggregationQueueJob (object): 
    def __init__(self, jobType):
        self.myJobType = jobType

    def quack(self):
        return self.myJobType

class AggregationQueueValues(AbstractAggregationQueueJob):
    def __init__(self, countersArray):
        super(AggregationQueueValues, self).__init__(AggregationQueueJobType.VALUES)
        self.myCountersArray = countersArray

class AggregationQueueDescriptions(AbstractAggregationQueueJob):
    def __init__(self, descriptionsArray):
        super(AggregationQueueDescriptions, self).__init__(AggregationQueueJobType.DESCRIPTORS)
        self.myDescriptionsArray = descriptionsArray 

class ValueObj(object):
    def __init__(self, counterId, timeStamp, value, description):
        self.myTimeStamp = timeStamp
        self.myDescription = description
        self.myValue = value
        self.myCounterId = counterId


# == Functions ====================================================================================================

def formatExceptionInfo(level = 6):
    error_type, error_value, trbk = sys.exc_info()
    tb_list = traceback.format_tb(trbk, level)    
    s = "Traceback:%s\nDescription: %s \nError: %s \n" % (error_type.__name__, tb_list, error_value)
    return s

def createDirIfNeeded (dirPath):
    if os.path.exists(dirPath):
        if os.path.isdir(dirPath):
            return True
        else:
            return False
    else:
        try:
            oldUmask = os.umask(0)
            os.makedirs(dirPath)
            os.umask(oldUmask)
            return True
        except:
            return False

def deleteFileIfNeeded (filePath):
    try:
        if os.path.exists(filePath):
            if os.path.isfile(filePath):
                os.remove(filePath)
                return True
            else:
                return False
        else:
            return True
    except:
        return False


