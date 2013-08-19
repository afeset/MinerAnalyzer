# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from blinky_node import BlinkyNode
from a.infra.basic.return_codes import ReturnCodes

from a.sys.confd.pyconfdlib import pyconfdlib
from a.sys.confd.pyconfdlib.key_path import KeyPath

class BlinkyOperNode(BlinkyNode): 
    def __init__ (self, logger):
        BlinkyNode.__init__(self, logger)
        self.myConfigNode = None
        self.myFunctorsSet = None
        self.myAllowNoDestroySelfFunctor = True

    def _myStr (self):
        if self.myConfigNode != None:
            return (",ConfigNode='%s'" % self.myConfigNode)
        return ""

    def setDomain (self, domain):
        for logFunc in self._log("set-domain").debug1Func(): logFunc("called. domain=%s", domain)
        self.internalSetDomain(domain)

    def setConfigObj (self, configObj):
        for logFunc in self._log("set-config-obj").debug1Func(): logFunc("called. configObj=%s", configObj)
        res = self.distributeConfigObjectToDescendants(configObj)
        if (res != ReturnCodes.kOk):
            for logFunc in self._log("set-config-obj-distribute-failed").errorFunc(): logFunc("distributeConfigObjectToDescendants() failed. configObj=%s. res=%",
                                                                configObj, res)
            return ReturnCodes.kGeneralError

        jointKeyPath = KeyPath()
        jointKeyPath.copyPartial(configObj.getKeyPath(), configObj.getKeyPath().getLen())
        operRelativePath = KeyPath()
        self.getOperRelativePath(operRelativePath)

        jointKeyPath.joinKeyPath(operRelativePath);

        for logFunc in self._log("set-config-obj-joint-keypath").debug3Func(): logFunc("jointKeyPath is: %s", jointKeyPath)

        self.internalSetKeyPath(jointKeyPath)
        self.myConfigNode = configObj

        return ReturnCodes.kOk

    def getObject (self, trxContext, keyPath):
        __pychecker__='no-argsused'
        return ReturnCodes.kOk

    def getElement (self, trxContext, keyPath):
        __pychecker__='no-argsused'
        return ReturnCodes.kOk

    def getNext (self, trxContext, keyPath, next):
        __pychecker__='no-argsused'
        return ReturnCodes.kOk


    def removeCallpointInfo (self, callpointCtx):
        operRelativePath = KeyPath()
        self.getOperRelativePath(operRelativePath)

        for logFunc in self._log("remove-callpoint-info").debug3Func(): logFunc("called. callpoint name=%s, callpoint config keypath=%s, operRelativePath=%s",
                                                  callpointCtx.getCallpointName(), callpointCtx.getConfigKeyPath(), operRelativePath)

        callpointCtx.removeMapping(operRelativePath)
        return ReturnCodes.kOk

    def getCallpointName (self):
        raise NotImplementedError()

    def distributeConfigObjectToDescendants (self, configObj):
        __pychecker__='no-argsused'
        raise NotImplementedError()

    def getOperRelativePath (self, operRelativeKeyPath):
        __pychecker__='no-argsused'
        raise NotImplementedError()

    def activateSpecific (self):
        for logFunc in self._log("activate-specifig").debug3Func(): logFunc("called.")
        if self.myFunctorsSet:
            return self.myConfigNode.registerOperNode(self);
        return ReturnCodes.kOk

    def deactivateSpecific (self):
        for logFunc in self._log("deactivate-specifig").debug3Func(): logFunc("called.")
        if self.myFunctorsSet:
            return self.myConfigNode.unregisterOperNode(self);
        return ReturnCodes.kOk

