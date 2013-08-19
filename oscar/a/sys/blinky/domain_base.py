# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

# This Python class mimics the sys::blinky::Domain C++ class

from a.infra.basic.return_codes import ReturnCodes
from a.infra.misc.init_guard import InitGuard
import a.infra.process.captain

class DomainBase (object):

    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky", "domain")
        self.myAgent = None
        self.myNetworkOperationRetryMax=100
        self.myNetworkOperationRetryIntervalMili=100

    def __str__ (self):
        return "name=%s" % self.myName

    def init (self, agent, name):
        self.myInitGuard.crashIfInitDone()
        self.myName=name
        self._log.setInstance(self.myName)
        self.myAgent=agent

        res = self.specificInit()
        if res != ReturnCodes.kOk:
            for logFunc in self._log('init-specific-failed').errorFunc(): logFunc('specificInit() failed. res=%s', res)
            a.infra.process.processFatal("domain %s: specificInif() failed.", self.myName)

        for logFunc in self._log("init").debug2Func(): logFunc("Initialized")
        self.myInitGuard.initDone()

    def destroy(self):
        raise NotImplementedError()
    
    def shutdown (self):
        for logFunc in self._log("shutdown").noticeFunc(): logFunc("shutting down")
        self.specificShutdown()

    def setNetworkOperationRetryLimits(self, maxRetries, retryIntervalMili):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("set-network-operation-retry-limits").debug3Func():
            logFunc("setNetworkOperationRetryLimits(): called: retryIntervalMili=%s, maxRetries=%s",
                    retryIntervalMili, maxRetries)
        self.myNetworkOperationRetryMax = maxRetries
        self.myNetworkOperationRetryIntervalMili = retryIntervalMili
    
    def getName (self):
        self.myInitGuard.isInitOrCrash()
        return self.myName


