 # Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: yoave

G_NAME_MODULE_NET_INTERFACES = "interfaces" 
G_NAME_GROUP_NET_INTERFACES = "interfaces"
G_NAME_GROUP_NET_INTERFACES_INTERFACE_MANAGER = "interface-manager"
G_NAME_GROUP_NET_INTERFACES_INTERFACE = "interface"


from if_table import IfTable
from a.infra.basic.return_codes import ReturnCodes


##############################################
# This class manages the network configuration
##############################################
class IfContainerBase(object):
    """This class manages the network interface configuration"""

#-----------------------------------------------------------------------------------------------------------------------
    def __init__ (self, logger, name, isActiveModule, allowDynamicConfig, lineNicsFile=None, snmpTrapsManager=None):
        self.name = name
        self._log = logger.createLoggerSameModule(G_NAME_GROUP_NET_INTERFACES, instance = self.name)
         
        # holds a list of interfaces
        self.interfaceList = IfTable(self._log, self, isActiveModule, allowDynamicConfig, lineNicsFile, snmpTrapsManager)
        self.blinkyInterfaceList = None
        self.blinkyInterfaces = None

        self.isTrxStart = False
         
#-----------------------------------------------------------------------------------------------------------------------
    def _attachToBlinkyIfList(self, blinkyInterfaceList):
        self._log("attach-blinky-interface-list").debug2("attach to blinky: %s", blinkyInterfaceList)

        self.blinkyInterfaceList = blinkyInterfaceList
        rc = self.interfaceList.attachToBlinky(blinkyInterfaceList)

        return rc    

#-----------------------------------------------------------------------------------------------------------------------
    def createInterfaceList (self, phase, blinkyInterfaceList):
        self._log("create-interface-list").debug2("called: %s", blinkyInterfaceList)
        if phase.isPreparePrivate():
            return self._attachToBlinkyIfList(blinkyInterfaceList)
    
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def destroyInterfaces (self, phase):
        self._log("destroy-interfaces").debug2("called. blinkyObj=%s, phase=%s", self.blinkyInterfaces, phase)
        self.blinkyInterfaces.deactivate()
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def attachToBlinky(self, blinkyInterfaces):
        self._log("attach-blinky-interfaces").debug2("attach to blinky: %s", blinkyInterfaces)

        self.blinkyInterfaces = blinkyInterfaces
        self.blinkyInterfaces.setCreateInterfaceListFunctor(self.createInterfaceList)
        self.blinkyInterfaces.setDestroySelfFunctor(self.destroyInterfaces)

        rc = self.blinkyInterfaces.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-blinky-interfaces-activate-failed").debug2("blinkyInterfaces.activate() failed. blinkyInterfaces=%s", blinkyInterfaces)
            return ReturnCodes.kGeneralError

        return rc    

#-----------------------------------------------------------------------------------------------------------------------
    def attachToBlinkyOper(self):
        pass

#-----------------------------------------------------------------------------------------------------------------------
    def setConfigErrorStr(self, msg):
        if self.blinkyInterfaceList:
            self.blinkyInterfaceList.setConfigErrorStr(msg)

#-----------------------------------------------------------------------------------------------------------------------
    def getInterface(self, key, isRunning=True):
        """Returns a real interface by key, or None if not found"""

        interface = self.interfaceList.getObjectByKey(key, isRunning)
        return interface

#-----------------------------------------------------------------------------------------------------------------------
    def trxProgress (self, progress):

        self._log("trx-progress").debug2("transaction progress: %s", progress)

        rc = ReturnCodes.kOk

        if progress.isPreparePrivateAfter():
            rc = self.preparePrivateAfter()
            if rc == ReturnCodes.kOk:
                self.__startTrx(progress)
        else:
            if self.__hasTrxStarted():

                if progress.isCommitPrivateAfter() and self.isTrxStart:
                    rc = self.commitPrivateAfter()
                    self.__endTrx(progress)

                if progress.isAbortPrivateAfter() and self.isTrxStart:
                    rc = self.abortPrivateAfter()
                    self.__endTrx(progress)
    
        self._log("trx-result").debug3("transaction <%s> result: %s", progress, rc)

        return rc

#-----------------------------------------------------------------------------------------------------------------------
    def __hasTrxStarted(self):
        return self.isTrxStart is True

#-----------------------------------------------------------------------------------------------------------------------
    def __startTrx(self, progress):
        self._log("start-trx").debug2("transaction start: %s", progress)
        self.isTrxStart = True

#-----------------------------------------------------------------------------------------------------------------------
    def __endTrx(self, progress):
        self._log("end-trx").debug2("transaction end: %s", progress)
        self.isTrxStart = False

#-----------------------------------------------------------------------------------------------------------------------
    def preparePrivateAfter(self):
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def commitPrivateAfter(self):
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def abortPrivateAfter(self):
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def __str__(self):
        return str(self.interfaceList)

#-----------------------------------------------------------------------------------------------------------------------  
    def shutdown(self):
        self.interfaceList.shutdown()


