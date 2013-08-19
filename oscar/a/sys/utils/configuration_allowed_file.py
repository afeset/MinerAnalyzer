#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: naamas
# 

import json
import os

class ConfigurationAllowedFile: 
    """
    A module for reading & writing configuration-allowed file
    Used by config_validation daemon to validate configuration changes only if system is "happy"
    Code is NOT thread safe
    """

    NAME_MODULE_CONFIGURATION_ALLOWED_FILE = "configuration-allowed-file"
    NAME_GROUP_CONFIGURATION_ALLOWED_FILE_GENERAL = "general"

    ACTUAL_CONFIGURATION_ALLOWED_FILE = "actual_configuration_allowed.json"
    FORCE_CONFIGURATION_ALLOWED_FILE = "force_configuration_allowed.json"

    CONFIGURATION_ALLOWED = "configuration-allowed"

    def __init__ (self, systemStatusDir, logger=None):
        if logger:
            self.log = logger.createLogger(self.NAME_MODULE_CONFIGURATION_ALLOWED_FILE, 
                                           self.NAME_GROUP_CONFIGURATION_ALLOWED_FILE_GENERAL)

        self.systemStatusDir = systemStatusDir
        self.actualConfigurationAllowedFile = os.path.join(self.systemStatusDir, self.ACTUAL_CONFIGURATION_ALLOWED_FILE)
        self.forceConfigurationAllowedFile = os.path.join(self.systemStatusDir, self.FORCE_CONFIGURATION_ALLOWED_FILE)

    def writeConfigrationAllowedToFile (self, filename, allowed):
        tempFileName = '%s.temp' % filename
        content = {
            self.CONFIGURATION_ALLOWED : allowed
            }
        try:
            tempFile = open(tempFileName, 'w')
            tempFile.write(json.dumps(content, indent=4, sort_keys=True))
            tempFile.close()

            # replace the file
            os.rename(tempFileName, filename)

        except Exception, err:
            raise err

    def readConfigrationAllowedFromFile (self, filename, raiseException=True):
        allowed = False
        try:
            statusFile = open(filename, 'r')
            content = json.load(statusFile)
            statusFile.close()
            allowed = content[self.CONFIGURATION_ALLOWED]

        except Exception, err:
            if raiseException:
                self.log("read-configuration-allowed-from-file").error('failed to read %s. exception: %s', filename, err)
                raise err
            else:
                self.log("read-configuration-allowed-from-file").info('failed to read %s. exception: %s', filename, err)
                return False

        return allowed


    def writeConfigurationAllowedActual (self, allowed):
        self.writeConfigrationAllowedToFile(self.actualConfigurationAllowedFile, allowed)

    def writeConfigurationAllowedForce (self, allowed):
        self.writeConfigrationAllowedToFile(self.forceConfigurationAllowedFile, allowed)

    def readConfigurationAllowed (self):
        allowed = self.readConfigrationAllowedFromFile(self.forceConfigurationAllowedFile, raiseException=False)
        if not allowed:
            allowed = self.readConfigrationAllowedFromFile(self.actualConfigurationAllowedFile)

        return allowed

