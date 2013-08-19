# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: amiry

G_NAME_GROUP_NET_NAME_RESOLUTION = "name-resolution"

from a.infra.basic.return_codes import ReturnCodes
from a.sys.blinky.util.simple_container_wrapper import SimpleContainerWrapper
from dns import DnsContainer
from static_resolution import StaticResolutionContainer

class NameResolutionContainer(object):
    """This class manages the system name resolution information"""

    def __init__ (self, logger):
        self._log = logger.createLoggerSameModule(G_NAME_GROUP_NET_NAME_RESOLUTION)
        self.name = "network-name-resolution"
        self.blinkyNameResolution = None
        self.dns = None
        self.static = None

    #-----------------------------------------------------------------------------------------------------------------------
    def notifyAttachToBlinky(self, blinkyNameResolution):
        # --- /tech/system/name-resolution/dns
        blinkyNameResolution.setCreateDnsFunctor(self.createDns)
        blinkyNameResolution.setDeleteDnsFunctor(self.deleteDns)
        # --- /tech/system/name-resolution/static
        blinkyNameResolution.setCreateStaticResolutionFunctor(self.createStaticResolution)
        blinkyNameResolution.setDeleteStaticResolutionFunctor(self.deleteStaticResolution)
        self.blinkyNameResolution = blinkyNameResolution

    #-----------------------------------------------------------------------------------------------------------------------
    def createDns(self, phase, blinkyDns):
        self._log("create-dns").debug2("%s: blinkyDns=%s", phase, blinkyDns)
        if (phase.isPreparePrivate()):
            dns = DnsContainer(self._log)
            self.dns = SimpleContainerWrapper(self._log, dns, 
                                              notifyTrxProgressFunctor = True,
                                              notifyDescendantsModifications = True)
            self.dns.attachToBlinky(blinkyDns)
        elif (phase.isAbortPrivate()):
            self.dns = None
        return ReturnCodes.kOk

    #-----------------------------------------------------------------------------------------------------------------------
    def deleteDns(self, phase):
        self._log("delete-dns").debug2("phase=%s", phase)
        if (phase.isCommitPrivate()):
            self.dns = None
        return ReturnCodes.kOk

    #-----------------------------------------------------------------------------------------------------------------------
    def createStaticResolution(self, phase, blinkyStaticResolution):
        self._log("create-static-resolution").debug2("%s: blinkyStaticResolution=%s", phase, blinkyStaticResolution)
        if (phase.isPreparePrivate()):
            staticResolution = StaticResolutionContainer(self._log)
            self.static = SimpleContainerWrapper(self._log, staticResolution)
            self.static.attachToBlinky(blinkyStaticResolution)
        elif (phase.isAbortPrivate()):
            self.static = None
        return ReturnCodes.kOk

    #-----------------------------------------------------------------------------------------------------------------------
    def deleteStaticResolution(self, phase):
        self._log("delete-static-resolution").debug2("phase=%s", phase)
        if (phase.isCommitPrivate()):
            self.static = None
        return ReturnCodes.kOk

    #-----------------------------------------------------------------------------------------------------------------------
    def getDnsNameServers(self):
        return self.dns.getNameServers()

    #-----------------------------------------------------------------------------------------------------------------------
    def getDnsSearchDomains(self):
        return self.dns.getSearchDomains()

    #-----------------------------------------------------------------------------------------------------------------------
    def getDnsEnabled(self):
        return self.dns.getEnabled()

    #-----------------------------------------------------------------------------------------------------------------------
    def getStaticHosts(self):
        hosts = []
        if self.static:
            hosts = self.static.getHosts()
        return hosts


