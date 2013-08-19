# 
# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: nirs

import os
import a.sys.blinky.agent

class AgentCaptainClient(a.sys.blinky.agent.Agent):
    OSEF_KEY_BLINKY_AGENT = "blinky-agent"
    CAPTAIN_CLIENT_NAME = OSEF_KEY_BLINKY_AGENT

    #init param data
    INIT_PARAM_DATA_CONFD_DEBUG_LEVEL = "confd-debug-level"
    INIT_PARAM_DATA_CONFD_IPC_IP = "confd-ipc-ip"
    INIT_PARAM_DATA_CONFD_IPC_PORT = "confd-ipc-port"

    def __init__ (self, logger, skipInitFromParamFile=False):
        a.sys.blinky.agent.Agent.__init__(self, logger=logger)
        self._skipInitFromParamFile = skipInitFromParamFile

    def initCaptain (self, captain):
        self._captain = captain

    def getInitParamFileName (self):
        return self.__s_getInitParamFileName()

    def captainClient_setProcessName(self):
        self._initDataProcessName = self._captain.getProcessName()

    def captainClient_dormant2Passive (self):
        self.setName("agent - %s" % self._initDataProcessName)
        self.setConfdDebugLevel(self._initDataDict[self.INIT_PARAM_DATA_CONFD_DEBUG_LEVEL])
        self.initBlinky(self._initDataDict[self.INIT_PARAM_DATA_CONFD_IPC_IP], 
                        self._initDataDict[self.INIT_PARAM_DATA_CONFD_IPC_PORT])

    def initFromDictionary (self, data):
        self._initDataDict = data

    def captainClient_initFromParamFile (self):
        if self._skipInitFromParamFile:
            return
        initParamFilesDirName = self._captain.getInitParamFilesDirName()
        try:
            data = a.infra.format.json.readFromFile(self._log, 
                                                    os.path.join(initParamFilesDirName, self.getInitParamFileName()))
        except Exception as exception:
            a.infra.process.processFatal("Failed to get blinky init data: %s", str(exception))

        self.initFromDictionary(data)

    def captainClient_addToOsef (self):
        self._captain.getOsef()[self.OSEF_KEY_BLINKY_AGENT] = self

    @classmethod
    def s_createInitParamFile (cls, dbgLog, initParamFilesDirName, dictionary):
        a.infra.format.json.writeToFile(dbgLog, dictionary, 
                                        os.path.join(initParamFilesDirName, cls.__s_getInitParamFileName()), 
                                        indent=4)

    @classmethod
    def s_getFromOsefUnsafe (cls, osef):
        return a.infra.log.generic_instance.GenericInstance._s_getFromOsefUnsafe(osef, cls.OSEF_KEY_BLINKY_AGENT)        

    @classmethod
    def s_getFromOsefOrCrash (cls, osef):
        return a.infra.log.generic_instance.GenericInstance._s_getFromOsefOrCrash(osef, cls.OSEF_KEY_BLINKY_AGENT)        

    @staticmethod
    def __s_getInitParamFileName ():
        return "blinky-agent-init-params.json"





