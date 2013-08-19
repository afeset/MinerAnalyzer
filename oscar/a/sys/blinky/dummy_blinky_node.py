# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes
from blinky_config_node import BlinkyConfigNode

class DummyBlinkyNode(BlinkyConfigNode): 
    def __init__ (self, logger):
        BlinkyConfigNode.__init__(self, logger)
        self.myAllowNoDestroySelfFunctor = True

    def findBlinkyNode(self, keyPath, keyDepth_PassByRef, foundAtKeyDepth_PassByRef):
        __pychecker__='no-argsused'
        return None

    def trxElementHelper(self, trxElement, keyDepth, phase):
        __pychecker__='no-argsused'
        return ReturnCodes.kOk

    def activateSpecific(self):
        return ReturnCodes.kOk

    def deactivateSpecific(self):
        return ReturnCodes.kOk

    def allocMyCandidate (self):
        return ReturnCodes.kOk

    def deleteMyCandidate (self):
        pass



