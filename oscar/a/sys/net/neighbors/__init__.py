# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: alexb

G_NAME_GROUP_NET_NEIGHBORS = "neighbors"

from a.infra.basic.return_codes import ReturnCodes
from a.sys.blinky.util.simple_container_wrapper import SimpleContainerWrapper
from application_initiated_discovery import ApplicationInitiatedDiscoveryContainer

class NeighborsContainer(object):
    """This class manages the network neighbor information"""

    def __init__ (self, logger):
        self._log = logger.createLoggerSameModule(G_NAME_GROUP_NET_NEIGHBORS)

        self.blinkyNeighbors = None

        self.isApplicationInitiatedDiscoveryWrapperCreated = False
        self.applicationInitiatedDiscovery = ApplicationInitiatedDiscoveryContainer(self._log)

    def notifyAttachToBlinky(self, blinkyNeighbors):
        # --- /tech/network/ipv6/neighbors/application-initiated-discovery
        blinkyNeighbors.setCreateApplicationInitiatedDiscoveryFunctor(self.createApplicationInitiatedDiscovery)
        blinkyNeighbors.setDeleteApplicationInitiatedDiscoveryFunctor(self.deleteApplicationInitiatedDiscovery)
        self.blinkyNeighbors = blinkyNeighbors

    def createApplicationInitiatedDiscovery (self, phase, blinkyApplicationInitiatedDiscovery):
        self._log("create-application-initiated-discovery").debug3("%s: blinkyApplicationInitiatedDiscovery=%s", phase, blinkyApplicationInitiatedDiscovery)
        if (phase.isPreparePrivate()):
            self.applicationInitiatedDiscovery = SimpleContainerWrapper(self._log, self.applicationInitiatedDiscovery, 
                                                                        setOperDataFunctor=True)
            self.isApplicationInitiatedDiscoveryWrapperCreated = True
            self.applicationInitiatedDiscovery.attachToBlinky(blinkyApplicationInitiatedDiscovery)
        elif (phase.isCommitPublic()):
            self.applicationInitiatedDiscovery.attachToBlinkyOper()
        elif (phase.isAbortPrivate()):
            if self.isApplicationInitiatedDiscoveryWrapperCreated is True:
                self.applicationInitiatedDiscovery = self.applicationInitiatedDiscovery.realObject
        return ReturnCodes.kOk

    def deleteApplicationInitiatedDiscovery (self, phase):
        self._log("delete-application-initiated-discovery").debug3("phase=%s", phase)
        if (phase.isCommitPrivate()):
            if self.isApplicationInitiatedDiscoveryWrapperCreated is True:
                self.applicationInitiatedDiscovery = self.applicationInitiatedDiscovery.realObject
        return ReturnCodes.kOk


