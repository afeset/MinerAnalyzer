#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

#this is a temp class that is used to move sys-param information to different oscar daemons
class SysParamContainer:
    def __init__ (self, configParser, logger):
        self._log = logger.createLoggerSameModule("sys-param")
        self._configParserDictionary = {}
        for section in configParser.sections():
            fields = {}
            for (name, value) in configParser.items(section):
                for logFunc in self._log("copy-sys-param-value").debug2Func(): logFunc("copy [%s][%s]=%s", section, name, value)
                fields[name] = value
            self._configParserDictionary[section]=fields

    def getInt (self, section, variable, default):
        return int(self._getValueOrDefault(section, variable, default))

    def getFloat (self, section, variable, default):
        return float(self._getValueOrDefault(section, variable, default))

    def getBool (self, section, variable, default):
        data = self._getValueOrDefault(section, variable, default)
        return str(data) in ["True", "true"]

    def getString (self, section, variable, default):
        return str(self._getValueOrDefault(section, variable, default))

    def _getValueOrDefault (self, section, variable, default):
        value = default
        if section in self._configParserDictionary:
            if variable in self._configParserDictionary[section]:
                data = self._configParserDictionary[section][variable]
                if data != "":
                    value = data
                    for logFunc in self._log("get-data").debug3Func(): logFunc("read sys param [%s][%s]=%s", section, variable, value)
                else:
                    for logFunc in self._log("get-data-not-set").debug3Func(): logFunc("read sys param [%s][%s]. data is an empty string, therefore using default (%s)", section, variable, value)
            else:
                for logFunc in self._log("get-no-data").debug3Func(): logFunc("read sys param [%s][%s]. data is not in sys-param therefore using default (%s)", section, variable, value)
        else:
            for logFunc in self._log("get-no-section").debug3Func(): logFunc("read sys param [%s][%s]. section is not in sys-param therefore using default (%s)", section, variable, value)
        return value
