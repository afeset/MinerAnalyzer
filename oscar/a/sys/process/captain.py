#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

from optparse import OptionParser
import os

import a.infra.process.captain
import a.sys.blinky.pearl

class ManagedCaptain(a.infra.process.captain.Captain):
    #captian init params handling
    INIT_PARAM_DICT_KEY_BLINKY = "blinky"

    def __init__ (self):
        a.infra.process.captain.Captain.__init__(self)

    def _genesis (self):
        a.infra.process.captain.Captain._genesis(self)
        #create system fatal object?
        pass

    def earlyInit (self):
        a.infra.process.captain.Captain.earlyInit(self)
        self._callOnClients("captainClient_sysEarlyInit")

    def _createClients (self):
        a.infra.process.captain.Captain._createClients(self)
        blinky = a.sys.blinky.pearl.Blinky(self._log)
        blinky.initCaptain(self)
        self._addClient(a.sys.blinky.pearl.Blinky.CAPTAIN_CLIENT_NAME, blinky)

    def _initFromParamFiles (self):
        a.infra.process.captain.Captain._initFromParamFiles(self)
        #possibly:
        #initParamFileName = os.path.join(self.getInitParamFilesDirName(), self.INIT_PARAM_FILE_NAME)
        #data = a.infra.format.json.readFromFile(self._log, initParamFileName)
        #self._xxx = data[self.INIT_PARAM_DATA_XXX]

    @classmethod
    def s_createInitParamFiles(cls, dbglog, initParamFilesDir, dataDictionary):
        a.infra.process.captain.Captain.s_createInitParamFiles(dbglog, initParamFilesDir, dataDictionary)
        a.sys.blinky.pearl.Blinky.s_createInitParamFile(dbglog, initParamFilesDir, dataDictionary[cls.INIT_PARAM_DICT_KEY_BLINKY])

