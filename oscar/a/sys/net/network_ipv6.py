# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: alexb

from a.infra.basic.return_codes import ReturnCodes
from neighbors import NeighborsContainer
from a.sys.blinky.util.simple_container_wrapper import SimpleContainerWrapper

if  __package__ is None:
    G_NAME_GROUP_NET_NETWORK_IPV6 = "unknown"
else:
    from . import G_NAME_GROUP_NET_NETWORK_IPV6

class NetworkIpv6Container(object):
    def __init__ (self, logger):
        self._log = logger.createLoggerSameModule(G_NAME_GROUP_NET_NETWORK_IPV6)

        self.blinkyNetworkIpv6 = None

        self.isNeighborsWrapperCreated = False
        self.neighbors = NeighborsContainer(self._log)

        self._log("create-network-ipv6-container").debug3("create network ipv6 container called")


    def notifyAttachToBlinky(self, blinkyNetworkIpv6):
        # --- /tech/network/ipv6/neighbors
        blinkyNetworkIpv6.setCreateNeighborsFunctor(self.createNeighbors)
        blinkyNetworkIpv6.setDeleteNeighborsFunctor(self.deleteNeighbors)

        self.blinkyNetworkIpv6 = blinkyNetworkIpv6

    def createNeighbors (self, phase, blinkyNeighbors):
        self._log("create-neighbors").debug3("%s: blinkyNeighbors=%s", phase, blinkyNeighbors)
        if (phase.isPreparePrivate()):
    
            self.neighbors = SimpleContainerWrapper(self._log, self.neighbors)
            self.isNeighborsWrapperCreated = True
            self.neighbors.attachToBlinky(blinkyNeighbors)
    
        elif (phase.isAbortPrivate()):
            if self.isNeighborsWrapperCreated is True:
                self.neighbors = self.neighbors.realObject
    
        return ReturnCodes.kOk

    def deleteNeighbors (self, phase):
        self._log("delete-neighbors").debug3("phase=%s", phase)
    
        if (phase.isCommitPrivate()):
            if self.isNeighborsWrapperCreated is True:
                self.neighbors = self.neighbors.realObject
    
        return ReturnCodes.kOk
