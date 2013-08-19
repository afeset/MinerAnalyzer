# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: yoave


from a.infra.basic.return_codes import ReturnCodes
from name_resolution import NameResolutionContainer
import a.sys.net.lnx.name
import a.sys.net.lnx.common

import re

if  __package__ is None:
    G_NAME_GROUP_NET_SYSTEM = "unknown"
else:
    from . import G_NAME_GROUP_NET_SYSTEM


##############################################
# This class manages the global system network
##############################################
class SystemContainer(object):
    """This class represents the system"""

    HOSTNAME_MAX_LENGTH = 64 # run 'getconf HOST_NAME_MAX'
    HOSTNAME_VALIDATION_REGEX = re.compile("(?!-)[A-Z\d-]{1,63}(?<!-)$", re.IGNORECASE)

    def __init__ (self, logger):
        """Instantiate a new a system network object.

        Args:
            name: the interface name

        Raises:
            None
        """

        self._log = logger.createLoggerSameModule(G_NAME_GROUP_NET_SYSTEM)
        self.name = "network-system"

        self.allowDynamicConfig = False
        self.candidateHostname = ""
        self.hostname = ""
        self.nameResolution = None

        self.blinkySystem = None

#-----------------------------------------------------------------------------------------------------------------------  
    def setAllowDynamicConfig(self):
        self.allowDynamicConfig = True
                         
#-----------------------------------------------------------------------------------------------------------------------  
    def __str__(self):
        strList = []
        strList.append("hostname:" % self.hostname)
        strList.append("ipv4: %s" % self.nameResolution)

        return '\t'.join(strList) 

#-----------------------------------------------------------------------------------------------------------------------
    def notifyAttachToBlinky(self, blinkySystem):

        # --- /tech/system/name-resolution
        blinkySystem.setCreateNameResolutionFunctor(self.createNameResolution)
        blinkySystem.setDeleteNameResolutionFunctor(self.deleteNameResolution)

        self.blinkySystem = blinkySystem


#-----------------------------------------------------------------------------------------------------------------------
    def setConfigErrorStr(self, msg):
        if self.blinkySystem:
            self.blinkySystem.setConfigErrorStr(msg)

#-----------------------------------------------------------------------------------------------------------------------
    def preparePrivateValueSet(self, data):
        """the interface is being evaluated and verified for correctness"""

        self._log("sys-prepare-private-value-set").debug4("%s: prepare data - %s", self.name, data)

        if data.hasHostname():
            if self.allowDynamicConfig is True:
                # contains at least one character
                if len(data.hostname) == 0:
                    self._log("empty-hostname").warning("hostname is empty: %s", data)
                    self.setConfigErrorStr("hostname must contain at least one character")
                    return ReturnCodes.kGeneralError

                # contains a maximum of 64 characters
                if len(data.hostname) > self.HOSTNAME_MAX_LENGTH:
                    self._log("long-hostname").warning("hostname is too long: %s", data)
                    self.setConfigErrorStr("hostname exceeded a maximum of %s characters" % self.HOSTNAME_MAX_LENGTH)
                    return ReturnCodes.kGeneralError

                hostname = data.hostname
                if hostname[-1:] == ".":
                    hostname = hostname[:-1] # strip exactly one dot from the end (if exists)

                # ensures that each segment
                # 1) contains at least one character and a maximum of 63 characters
                # 2) consists only of allowed characters 
                # 3) doesn't begin or end with a hyphen
                # note: allowed characters are 'a'-'z', 'A'-'Z', the digits '0'-'9' and the hyphen ('-')
                if all(self.HOSTNAME_VALIDATION_REGEX.match(x) for x in hostname.split(".")) is False:
                    self._log("invalid-hostname").warning("hostname is invalid: %s", data)
                    self.setConfigErrorStr("hostname is invalid")
                    return ReturnCodes.kGeneralError

            else:
                if len(data.hostname) != 0:
                    rc = a.sys.net.lnx.name.Hostname.showHostname(self._log)
                    if not a.sys.net.lnx.common.Command.isReturnOk(rc):
                        a.infra.process.processFatal("%s: Failed retrieving hostname", self.name)
                    
                    staticHost = rc[1]
    
                    if data.hostname != staticHost:
                        self._log("bad-hostname").warning("hostname must be %s", staticHost)
                        self.setConfigErrorStr("in this platform, hostname must be %s" % staticHost)
                        return ReturnCodes.kGeneralError

        self.candidateHostname = data.hostname

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def abortPrivateValueSet(self, data):
        """the interface changes are being aborted

            Raises:
                FATAL if fails
        """

        self._log("sys-abort-private-value-set").debug4("%s: abort data - %s", self.name, data)

        self.candidateHostname = self.hostname
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def commitPrivateValueSet(self, data):
        """the interface changes are being commited

            Raises:
                FATAL if fails
        """

        self._log("sys-commit-private-value-set").debug4("%s: commit data - %s", self.name, data)

        self.hostname = self.candidateHostname

        if data.hasHostname():
            if self.allowDynamicConfig is True:
                self.__setHostname()
                                    
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def getHostname(self, running=True):
        if running is True:
            return self.hostname
        else:
            return self.candidateHostname

        return None

#-----------------------------------------------------------------------------------------------------------------------
    def __setHostname(self):
        rc = a.sys.net.lnx.name.Hostname.setHostname(self._log, self.hostname)
        self._log("set-hostname").debug2("Set hostname to %s", self.hostname)

        if not a.sys.net.lnx.common.Command.isReturnOk(rc):
            a.infra.process.processFatal("%s: Failed setting hostname", self.name)

#-----------------------------------------------------------------------------------------------------------------------
    def createNameResolution(self, phase, blinkyNameResolution):
        self._log("create-name-resolution").debug2("%s: blinkyNameResolution=%s", phase, blinkyNameResolution)
    
        if (phase.isPreparePrivate()):
    
            nameResolution = NameResolutionContainer(self._log)
            self.nameResolution = a.sys.blinky.util.simple_container_wrapper.SimpleContainerWrapper(self._log, nameResolution)
            self.nameResolution.attachToBlinky(blinkyNameResolution)
    
        elif (phase.isAbortPrivate()):
            self.nameResolution = None
    
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def deleteNameResolution(self, phase):
        self._log("delete-name-resolution").debug2("phase=%s", phase)
    
        if (phase.isCommitPrivate()):
            self.nameResolution = None
    
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def getNameResolution (self):
        return self.nameResolution

