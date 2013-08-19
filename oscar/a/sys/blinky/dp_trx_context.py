# Copyright Qwilt, 2013
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class DpTrxContext(object):

    def __init__ (self, logger):
        self._log=logger.createLogger("sys-blinky", "dp-trx-context")
        for logFunc in self._log("init").debug2Func(): logFunc("called")

        self.myErrorStr = None

    def setErrorStr (self, errorStr):
        self.myErrorStr = errorStr

    def getErrorStr (self):
        return self.myErrorStr


