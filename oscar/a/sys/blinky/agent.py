# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

# This Python class mimics the sys::blinky::Agent C++ class

import functools
import socket
import time

from a.sys.confd.pyconfdlib import pyconfdlib
from a.infra.misc.init_guard import InitGuard
import a.infra.process
from config_domain import ConfigDomain
from maapi_domain import MaapiDomain
from utils import Utils,Retry
from trx_phase import TrxPhase
from a.infra.basic.return_codes import ReturnCodes

class Agent (object):
    def __init__ (self, logger):
        self.mySetNameGuard = InitGuard()
        self.myInitBlinkyGuard = InitGuard()

        self._log=logger.createLogger("sys-blinky", "agent")
        for logFunc in self._log('ctor').debug2Func(): logFunc("called")
        pyconfdlib.init(self._log)
        self.myConfdDebugLevel=pyconfdlib.CONFD_PROTO_TRACE
        self.myNetworkOperationRetryMax=100
        self.myNetworkOperationRetryIntervalMili=100
        self.myConfdAddress=None
        self.myConfdPort=None
        self.myMaapiSocketId=0

    def setName (self, name):
        self.mySetNameGuard.crashIfInitDone()
        self.myName=name
        self._log.setInstance(name)
        for logFunc in self._log("init").debug2Func(): logFunc("Initialized")
        TrxPhase.setLogger(self._log)
        self.mySetNameGuard.initDone()

    def setConfdDebugLevel(self, debugLevel):
        self.mySetNameGuard.isInitOrCrash()
        self.myInitBlinkyGuard.crashIfInitDone()
        self.myConfdDebugLevel = pyconfdlib.ConfdDebugLevel.getByValue(debugLevel)

    def connectToConfd (self):
        self.myMaapiSocketId=socket.socket()
        return pyconfdlib.maapi_connect(self.myMaapiSocketId, pyconfdlib.AF_INET, self.myConfdAddress, self.myConfdPort)

    def confdReloadConfig (self):
        if not self.myMaapiSocketId:
            for logFunc in self._log("confd-reload-config-no-maapi-socket").errorFunc(): logFunc("maapi socket not initialized, cannot reload config!")
            return ReturnCodes.kGeneralError
        
        res = pyconfdlib.maapi_reload_config(self.myMaapiSocketId)
        if res != pyconfdlib.CONFD_OK:
            for logFunc in self._log("confd-reload-config-lib-failed").errorFunc(): logFunc("maappi_reload_config failed, last error is %s, confd_error=%s", res.ret(),
                                                              Utils.getConfdErrStr())
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def initBlinky (self, confdAddress, confdPort):
        self.mySetNameGuard.isInitOrCrash()
        self.myInitBlinkyGuard.crashIfInitDone()
        pyconfdlib.confd_init(self.myName, self.myConfdDebugLevel)

        self.myConfdAddress=confdAddress
        self.myConfdPort=confdPort

        # wait for confd to start up
        connectToConfdFunctor=functools.partial(self.connectToConfd)
        res=Retry(self._log).callUntil(connectToConfdFunctor, self.myNetworkOperationRetryMax, 
                                       self.myNetworkOperationRetryIntervalMili, successValue=pyconfdlib.CONFD_OK)
        if not res.ok():
            for logFunc in self._log("connect-to-confd-failed").errorFunc(): logFunc("connectToConfd failed, last error is %s, confd_error=%s", res.ret(),
                                                    Utils.getConfdErrStr())
            a.infra.process.processFatal("Could not connect to confd (connectToConfd failed), confd_error=%s" % Utils.getConfdErrStr())

        for logFunc in self._log("connect-to-confd-succeeded").debug1Func(): logFunc("connectToConfd succeeded")

        res = pyconfdlib.maapi_wait_start(self.myMaapiSocketId, 2)
        if res != pyconfdlib.CONFD_OK:
            for logFunc in self._log("maapi-wait-start-failed").errorFunc(): logFunc("maapi_wait_start failed, last error is %s, confd_error=%s", res.ret(),
                                                       Utils.getConfdErrStr())
            a.infra.process.processFatal("Could not wait for confd to start (maapi_wait_start failed), confd_error=%s" % Utils.getConfdErrStr())

        for logFunc in self._log("maapi-wait-start-succeeded").noticeFunc(): logFunc("Connected to CONFD")

        res = pyconfdlib.confd_load_schemas(pyconfdlib.AF_INET, self.myConfdAddress, self.myConfdPort)
        if res != pyconfdlib.CONFD_OK:
            for logFunc in self._log("load-schemas-failed").errorFunc(): logFunc("Failed loading schemas, last error is %s, confd_error=%s", res.ret(),
                                                   Utils.getConfdErrStr())
            a.infra.process.processFatal("Could not load schemas, confd_error=%s" % Utils.getConfdErrStr())

        for logFunc in self._log("init-blonky-done").debug2Func(): logFunc("initBlinky(): Done loading schemas")
        self.myInitBlinkyGuard.initDone()

    def getConfdAddress (self):
        self.myInitBlinkyGuard.isInitOrCrash()
        return self.myConfdAddress

    def getConfdPort (self):
        self.myInitBlinkyGuard.isInitOrCrash()
        return self.myConfdPort

    def createConfigDomain (self, domainName, priority):
        for logFunc in self._log("create-config-domain").debug2Func(): logFunc("Called. domainName=%s priority=%s", domainName, priority)
        domain = ConfigDomain(logger=self._log)
        domain.init(self, domainName, priority)
        domain.setNetworkOperationRetryLimits(self.myNetworkOperationRetryMax, self.myNetworkOperationRetryIntervalMili)
        return domain

    def createMaapiDomain (self, domainName):
        for logFunc in self._log("create-maapi-domain").debug2Func(): logFunc("Called. domainName=%s", domainName)
        domain = MaapiDomain(logger=self._log)
        domain.init(self, domainName)
        domain.setNetworkOperationRetryLimits(self.myNetworkOperationRetryMax, self.myNetworkOperationRetryIntervalMili)
        return domain
