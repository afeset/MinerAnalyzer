# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from callpoint_context import CallpointContext

from a.infra.basic.return_codes import ReturnCodes

class DpRegistrationsDb(object):

    def __init__ (self, logger, name):
        self._log=logger.createLogger("sys-blinky", "dp-registration-db-%s" % name)

        self.myCallpointCtxMap = {}
        self.myFdToCallpointCtxMap = {}
        self.myDaemonIdToCallpointCtxMap = {}

    def getByKey (self, key):
        for logFunc in self._log("get-by-key").debug3Func(): logFunc("called. key=%s", key)
        if key in self.myCallpointCtxMap:
            for logFunc in self._log("get-by-key-found").debug3Func(): logFunc("found. key=%s, ctx=%s", key, self.myCallpointCtxMap[key])
            return self.myCallpointCtxMap[key]
        else:
            for logFunc in self._log("get-by-key-not-found").debug3Func(): logFunc("not found. key=%s", key)
            return None

    def storeByKey (self, key, callpointCtx):
        for logFunc in self._log("store-by-key").debug3Func(): logFunc("called. key=%s, callpointCtx=%s", key, callpointCtx)
        if key in self.myCallpointCtxMap:
            if callpointCtx == self.myCallpointCtxMap[key]:
                equalStr = "same callpoint context"
            else:
                equalStr = "different calpoint context"
            for logFunc in self._log("store-by-key-already-found").errorFunc(): logFunc("Already stored. equal?=%s key=%s, callpointCtx=%s, old=%s",
                                                          equalStr, key, callpointCtx, self.myCallpointCtxMap[key])
            return ReturnCodes.kGeneralError
        else:
            for logFunc in self._log("store-by-key-inserting").debug3Func(): logFunc("inserting. key=%s, callpointCtx=%s", key, callpointCtx)
            self.myCallpointCtxMap[key] = callpointCtx
        return ReturnCodes.kOk

    def removeByKey(self, key):
        for logFunc in self._log("remove-by-key").debug3Func(): logFunc("called. key=%s", key)
        if key in self.myCallpointCtxMap:
            for logFunc in self._log("remove-by-key-found").debug3Func(): logFunc("found. key=%s, ctx=%s", key, self.myCallpointCtxMap[key])
            del self.myCallpointCtxMap[key]
        else:
            for logFunc in self._log("remove-by-key-not-found").errorFunc(): logFunc("not found. key=%s", key)

    def getByFd (self, fd):
        for logFunc in self._log("get-by-fd").debug3Func(): logFunc("called. fd=%s", fd)
        if fd in self.myFdToCallpointCtxMap:
            for logFunc in self._log("get-by-fd-found").debug3Func(): logFunc("found. fd=%s, ctx=%s", fd, self.myFdToCallpointCtxMap[fd])
            return self.myFdToCallpointCtxMap[fd]
        else:
            for logFunc in self._log("get-by-fd-not-found").debug3Func(): logFunc("not found. fd=%s", fd)
            return None

    def storeByFd (self, fd, callpointCtx):
        for logFunc in self._log("store-by-fd").debug3Func(): logFunc("called. fd=%s, callpointCtx=%s", fd, callpointCtx)
        if fd in self.myFdToCallpointCtxMap:
            if callpointCtx == self.myFdToCallpointCtxMap[fd]:
                equalStr = "same callpoint context"
            else:
                equalStr = "different calpoint context"
            for logFunc in self._log("store-by-fd-already-found").errorFunc(): logFunc("Already stored. equal?=%s fd=%s, callpointCtx=%s, old=%s",
                                                          equalStr, fd, callpointCtx, self.myFdToCallpointCtxMap[fd])
            return ReturnCodes.kGeneralError
        else:
            for logFunc in self._log("store-by-fd-inserting").debug3Func(): logFunc("inserting. fd=%s, callpointCtx=%s", fd, callpointCtx)
            self.myFdToCallpointCtxMap[fd] = callpointCtx
        return ReturnCodes.kOk

    def removeByFd (self, fd):
        for logFunc in self._log("remove-by-fd").debug3Func(): logFunc("called. fd=%s", fd)
        if fd in self.myFdToCallpointCtxMap:
            for logFunc in self._log("remove-by-fd-found").debug3Func(): logFunc("found. fd=%s, ctx=%s", fd, self.myFdToCallpointCtxMap[fd])
            del self.myFdToCallpointCtxMap[fd]
        else:
            for logFunc in self._log("remove-by-fd-not-found").errorFunc(): logFunc("not found. fd=%s", fd)

    def getByDaemonId (self, daemonId):
        for logFunc in self._log("get-by-daemon-id").debug3Func(): logFunc("called. daemonId=%s", daemonId)
        if daemonId in self.myDaemonIdToCallpointCtxMap:
            for logFunc in self._log("get-by-daemon-id-found").debug3Func(): logFunc("found. daemonId=%s, ctx=%s", daemonId, self.myDaemonIdToCallpointCtxMap[daemonId])
            return self.myDaemonIdToCallpointCtxMap[daemonId]
        else:
            for logFunc in self._log("get-by-daemon-id-not-found").debug3Func(): logFunc("not found. daemonId=%s", daemonId)
            return None

    def storeByDaemonId (self, daemonId, callpointCtx):
        for logFunc in self._log("store-by-daemon-id").debug3Func(): logFunc("called. daemonId=%s, callpointCtx=%s", daemonId, callpointCtx)
        if daemonId in self.myDaemonIdToCallpointCtxMap:
            if callpointCtx == self.myDaemonIdToCallpointCtxMap[daemonId]:
                equalStr = "same callpoint context"
            else:
                equalStr = "different calpoint context"
            for logFunc in self._log("store-by-daemon-id-already-found").errorFunc(): logFunc("Already stored. equal?=%s daemonId=%s, callpointCtx=%s, old=%s",
                                                          equalStr, daemonId, callpointCtx, self.myDaemonIdToCallpointCtxMap[daemonId])
            return ReturnCodes.kGeneralError
        else:
            for logFunc in self._log("store-by-daemon-id-inserting").debug3Func(): logFunc("inserting. daemonId=%s, callpointCtx=%s", daemonId, callpointCtx)
            self.myDaemonIdToCallpointCtxMap[daemonId] = callpointCtx
        return ReturnCodes.kOk

    def removeByDaemonId (self, daemonId):
        for logFunc in self._log("remove-by-daemon-id").debug3Func(): logFunc("called. daemonId=%s", daemonId)
        if daemonId in self.myDaemonIdToCallpointCtxMap:
            for logFunc in self._log("remove-by-daemon-id-found").debug3Func(): logFunc("found. daemonId=%s, ctx=%s", daemonId, self.myDaemonIdToCallpointCtxMap[daemonId])
            del self.myDaemonIdToCallpointCtxMap[daemonId]
        else:
            for logFunc in self._log("remove-by-daemon-id-not-found").errorFunc(): logFunc("not found. daemonId=%s", daemonId)

    def getFds (self):
        for logFunc in self._log("get-fds").debug3Func(): logFunc("called")
        fds = []
        for fd in self.myFdToCallpointCtxMap.keys():
            if not self.myFdToCallpointCtxMap[fd].isClosedByServer():
                fds.append(fd)

        return fds

    def getSockets (self):
        sockets = []
        for logFunc in self._log("get-fds").debug3Func(): logFunc("called")
        for callpointCtx in self.myCallpointCtxMap.values():
            if not callpointCtx.isClosedByServer():
                sockets.append(callpointCtx.getControlSock())
                sockets.append(callpointCtx.getWorkerSock())

        return sockets

    def getNumOfSubscriptions (self):
        subscriptions = 0
        for callpointCtx in self.myCallpointCtxMap.values():
            subscriptions += callpointCtx.getNumOfMappings()
        return subscriptions
