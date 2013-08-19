# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.basic.return_codes import ReturnCodes

from blinky_config_node import BlinkyConfigNode

class BlinkyList(BlinkyConfigNode):
    def __init__ (self, logger):
        BlinkyConfigNode.__init__(self, logger)
        pass

    def activateSpecific (self):
        return ReturnCodes.kOk

    def deactivateSpecific (self):
        return ReturnCodes.kOk


