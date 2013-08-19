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
#                                                                                                                      #
# One place for the configuration functions instead of duplicating this code over and over
# Suppose to be removed when confd will finally work
#                                                                                                                      #
########################################################################################################################

import sys

CFG_SECTION = "stats"
CFG_DB_FILES_BASE_NAME = "db-files-base-name"
CFG_COUNTERS = "counters-to-sample"
CFG_JOBS_QUEUE_MAX_SIZE = "jobs-queue-max-size"

# Counter parameters identations
CFG_PARSE_COUNTER_PARAMS_LENGTH = 7

CFG_PARSE_COUNTER_PATH_IDENTATION = 0
CFG_PARSE_COUNTER_NAME_IDENTATION = 1
CFG_PARSE_COUNTER_TYPE_ENUM_IDENTATION = 2
CFG_PARSE_COUNTER_VALUE_VARIABLE_TYPE_ENUM_IDENTATION = 3
CFG_PARSE_COUNTER_SHORT_DESCRIPTION_IDENTATION = 4
CFG_PARSE_COUNTER_HELP_STRING_IDENTATION = 5
CFG_PARSE_COUNTER_PROCESS_ENUM_IDENTATION = 6 

# Properies identations
CFG_PARSE_PROPERTY_PARAMS_LENGTH = 3

CFG_PARSE_PROPERTY_TOTAL_NUMBER_OF_PROPERTIES_IDENTATION = 0
CFG_PARSE_PROPERTY_NAME_IDENTATION = 0
CFG_PARSE_PROPERTY_VARIABLE_TYPE_IDENTATION = 1
CFG_PARSE_PROPERTY_VALUE_IDENTATION = 2

# Sampling rate factor identation from counter start
CFG_PARSE_COUNTER_SAMPLING_RATE_FACTOR_IDENTATION = 0
CFG_PARSE_COUNTER_CONSILIDATION_FUNCTION_IDENTATION = 1
CFG_PARSE_COUNTER_DEFAULT_ARCHAIVE_TOTAL_IDENTATION = 2

# Archaives identations
CFG_PARSE_ARCHAIVE_PARAMS_LENGTH = 4

CFG_PARSE_ARCHAIVE_TOTAL_NUMBER_OF_ARCHAIVES_IDENTATION = 0
CFG_PARSE_ARCHAIVE_TYPE_IDENTATION = 0
CFG_PARSE_ARCHAIVE_ERROR_RATE_IDENTATION = 1
CFG_PARSE_ARCHAIVE_CONSILIDATION_SPAN_IDENTATION = 2
CFG_PARSE_ARCHAIVE_ROWS_TO_KEEP_IDENTATION = 3


# === Configuration Functions =====================================================================================

class samplingRateClassEnum(object):
    HIGH='high'
    SUPER='super'

def getSysParamOrExit (systemParamsCfg, aSection, aVar, logger):
    result = getSysParamOrDefault(systemParamsCfg, aSection, aVar, {aVar:None})
    if not result:
        logger.notice("Critical configuration wasn't found. Section: %s Variable: %s" % (aSection, aVar))
        sys.exit(88628)
    return result

def getSysParamOrDefault (systemParamsCfg, aSection, aVar, defaultsDictionary):
    
    result = None
    if hasNoneEmptyOption(systemParamsCfg, aSection, aVar):
        result = systemParamsCfg.get(aSection, aVar)
    elif aVar in defaultsDictionary.keys():
        result = defaultsDictionary[aVar]
    
    if str(type(result)).count("str"):
        if len(result)>1:
            if (result[0] == "[") and (result[-1] == "]"):
                return eval(result)

    return result

def hasNoneEmptyOption (systemParamsCfg, section, option):
    return systemParamsCfg.has_option(section, option) and systemParamsCfg.get(section, option)!=""
