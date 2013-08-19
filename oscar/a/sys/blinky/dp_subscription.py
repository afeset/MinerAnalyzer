# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

class DpSubscription(object):
    def __init__ (self, logger, modelPoints, blinkyNode, fmt, lowerRangeVal, upperRangeVal):
        self._log=logger.createLogger("sys-blinky", "dp-subscription")
        for logFunc in self._log("init").debug3Func(): logFunc("called: modelPoints=%s, blinkyNode=%s, lowerRangeVal=%s, upperRangeVal=%s, fmt=%s",
                                 modelPoints, blinkyNode, lowerRangeVal, upperRangeVal, fmt)
        self.daemonCtx = None
        self.controlSockId = None
        self.workerSockId = None
        self.daemonName = None
        self.modelPoints = modelPoints
        self.blinkyNode=blinkyNode
        self.lowerRangeVal = lowerRangeVal
        self.upperRangeVal = upperRangeVal
        self.destroyed = False

    def unregister (self):
        for logFunc in self._log("unregister").debug3Func(): logFunc("called")
        self.destroyed = True
        self.daemonCtx = None
        self.controlSockId = None
        self.workerSockId = None

    def __repr__ (self):
        if self.controlSockId and self.workerSockId:
            return '{daemonName=%s, node=%s, modelPoints=%s, controlSockId=%d, workerSockIt=%d' % (self.daemonName, self.blinkyNode, self.modelPoints, self.controlSockId.fileno(), self.workerSockId.fileno())
        else:
            return '{daemonName=%s, node=%s, modelPoints=%s' % (self.daemonName, self.blinkyNode, self.modelPoints)

