# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

import time

class TimeoutGuard(object):
    def __init__ (self, logger, name, timeoutMili, mildTimeoutMili=None):
        self._log=logger.createLogger("timeout-guard", "TimeoutGuard", instance=name)
        self.name = name
        self.timeoutMili = timeoutMili
        if not mildTimeoutMili:
            mildTimeoutMili = timeoutMili/2
        self.mildTimeoutMili = mildTimeoutMili
        self.startTime = time.time()

    def checkAndLog (self, logStr):
        timeDelta = int((time.time() - self.startTime) *1000)
        if timeDelta < self.mildTimeoutMili:
            self._log("check-and-log-valid").debug4("time delta is valid. timeDelta=%s, self.timeoutMili=%s, logStr=%s", timeDelta, self.timeoutMili, logStr)
        elif timeDelta >= self.timeoutMili:
            self._log("check-and-log-invalid").warning("time delta is longer than timeout. timeDelta=%s, self.timeoutMili=%s, logStr=%s", timeDelta, self.timeoutMili, logStr)
        else:
            self._log("check-and-log-warning").notice("time delta is above mild threshold. timeDelta=%s, self.mildTimeoutMili=%s,  self.timeoutMili=%s, logStr=%s", 
                                                       timeDelta, self.mildTimeoutMili, self.timeoutMili, logStr)

    def __str__ (self):
        return str(self.name)


