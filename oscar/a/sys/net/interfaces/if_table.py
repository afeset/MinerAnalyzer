# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: yoave

from a.infra.basic.return_codes import ReturnCodes
from a.sys.blinky.util.simple_list_wrapper import SimpleStringList
from a.sys.blinky.util.simple_container_wrapper import SimpleContainerWrapper
from interface import Interface

class IfTable(SimpleStringList):
    """An interface table object.
    """

    class CreateIfFunc(object):
        def __init__ (self, isActiveModule, allowDynamicConfig, lineNicsFile, snmpTrapsManager):
            self.isActiveModule = isActiveModule
            self.allowDynamicConfig = allowDynamicConfig
            self.lineNicsFile = lineNicsFile
            self.snmpTrapsManager = snmpTrapsManager

        def __call__(self, logger, name):

            interface = Interface(logger, name)

            if self.isActiveModule:
                interface.setAsActiveModule()

            if self.allowDynamicConfig:
                interface.setAllowDynamicConfig()

            if self.lineNicsFile is not None:
                interface.setLineNicsFile(self.lineNicsFile)

            if self.snmpTrapsManager is not None:
                interface.setSnmpTrapsManager(self.snmpTrapsManager)

            ifWrapper = SimpleContainerWrapper(logger, interface, 
                                               notifyTrxProgressFunctor=self.isActiveModule, 
                                               notifyDescendantsModifications=True,
                                               setOperDataFunctor=self.isActiveModule)

            return ifWrapper

#-----------------------------------------------------------------------------------------------------------------------
    def __init__ (self, logger, owner, isActiveModule, allowDynamicConfig, lineNicsFile, snmpTrapsManager):
        
        createIfFunctor = self.CreateIfFunc(isActiveModule, allowDynamicConfig, lineNicsFile, snmpTrapsManager)
        SimpleStringList.__init__(self, logger, createIfFunctor)

        self.owner = owner
        self._log("trx-progress-mode").debug3("isActiveModule mode: %s", isActiveModule)

#-----------------------------------------------------------------------------------------------------------------------
    def preparePrivateOnCreate(self, name, blinkyIfTable):

        # interface creation after trigger is not premitted
        if blinkyIfTable.isInTrigger() is False:
            self._log("interface-create-after-trigger").error("%s: create interface after trigger", name)
            blinkyIfTable.setConfigErrorStr("Interface '%s' cannot be created" % name)
            
            return ReturnCodes.kGeneralError

        return SimpleStringList.preparePrivateOnCreate(self, name, blinkyIfTable)

#-----------------------------------------------------------------------------------------------------------------------
    def trxProgress(self, progress):

        rc = SimpleStringList.trxProgress(self, progress)

        if rc != ReturnCodes.kOk:
            return rc

        return self.owner.trxProgress(progress)

#-----------------------------------------------------------------------------------------------------------------------  
    def shutdown(self):
        runningInterfaces = self.runningValues()
        for currentI in runningInterfaces:
            currentI.shutdown()

        candidateInterfaces = self.candidateValues()
        for currentI in candidateInterfaces:
            currentI.shutdown()
