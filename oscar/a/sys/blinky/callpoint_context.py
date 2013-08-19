# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.sys.confd.pyconfdlib.key_path import KeyPath

from a.infra.basic.return_codes import ReturnCodes

import copy

class CallpointContext(object):

    class Mapping(object):
        def __init__ (self):
            self.keyPath = None
            self.node = None

    def __init__ (self, logger):
        self._log=logger.createLogger("sys-blinky", "callpoint-context")
        self.myConfigKeyPath = None
        self.myDaemonCtx = None
        self.myControlSock = 0
        self.myWorkerSock = 0
        self.myClosedByServer = False
        self.myMappings = []
        self.myErrorStr = ""
        for logFunc in self._log("init").debug2Func(): logFunc("called")

    def __str__ (self):
        ss = "%s" % self.myConfigKeyPath
        return ss

    def addMapping (self, keyPath, node):
        for logFunc in self._log("add-mapping").debug2Func(): logFunc("called. keyPath=%s, node=%s", keyPath, node)
        newMapping = self.Mapping()
        newMapping.keyPath = keyPath
        newMapping.node = node
        self.myMappings.append(newMapping)

    def removeMapping (self, keyPath):
        for logFunc in self._log("remove-mapping").debug2Func(): logFunc("called. keyPath=%s", keyPath)
        for mapping in self.myMappings:
            if mapping.keyPath.isEqual(keyPath):
                self.myMappings.remove(mapping)

    def getNumOfMappings (self):
        return len(self.myMappings)

    def shouldUnregisterCallpoint (self):
        if len(self.myMappings) == 0:
            return True
        return False

    def getResponsibleNode (self, keyPath, leaveLowestKey,  responsibleNodes):
        for logFunc in self._log("get-responsible-node").debug3Func(): logFunc("called. keyPath=%s, leavLowestKey=%s, responsibleNodes=%s",
                                                 keyPath, leaveLowestKey, responsibleNodes)
        operNode = None
        responsibleKeyPath = None
        operKeyPath = keyPath.getKeyPathPostfixFlattened(self.myConfigKeyPath, leaveLowestKey)
        matchLen = 0
        for mapping in self.myMappings:
            if operKeyPath.getLen():
                for logFunc in self._log("get-responsible-node-checking-item").debug3Func(): logFunc(
                    "checking mapping item. keyPath=%s, operKeyPath=%s, mapping=%s, mapping-node=%s", 
                    keyPath, operKeyPath, mapping.keyPath, mapping.node.getKeyPath())
                if operKeyPath.isEqual(mapping.keyPath) or mapping.keyPath.isDescendantOf(operKeyPath):
                    for logFunc in self._log("get-responsible-node-found-matching-item").debug3Func(): logFunc(
                        "found matching item. keyPath=%s, operKeyPath=%s, mapping=%s, mapping-node=%s", 
                        keyPath, operKeyPath, mapping.keyPath, mapping.node.getKeyPath())
                    if (mapping.keyPath.getLen() > matchLen) or (matchLen == 0):
                        for logFunc in self._log("get-responsible-node-replacing").debug3Func(): logFunc(
                            "replacing responsible node. keyPath=%s, operKeyPath=%s, mapping=%s, mapping-node=%s, previos-respobsible-node=%s", 
                            keyPath, operKeyPath, mapping.keyPath, mapping.node.getKeyPath(), responsibleKeyPath)
                        matchLen = mapping.keyPath.getLen()
                        operNode = mapping.node
                        responsibleKeyPath = operNode.getKeyPath()
            else:
                for logFunc in self._log("get-responsible-node-taking-everything").debug3Func(): logFunc("taking everything. node=%s", mapping.node)
                # take everything from here down
                responsibleNodes.append(mapping.node)

        if operNode and (len(responsibleNodes) == 0):
            responsibleNodes.append(operNode)

        for logFunc in self._log("get-responsible-node-done").debug3Func(): logFunc(
            "done. keyPath=%s, operKeyPath=%s, responsibleNodes=%s", 
            keyPath, operKeyPath, responsibleNodes)
        return ReturnCodes.kOk

    def setErrorStr (self, errorStr):
        self.myErrorStr = errorStr

    def getErrorStr (self):
        return self.myErrorStr

    def setCallpointName (self, callpointName):
        self.myCallpointName = callpointName

    def setConfigObjKeyPath (self, keyPath):
        self.myConfigKeyPath = copy.deepcopy(keyPath)

    def detailedStr (self):
        detailedStr = ""
        if self.myClosedByServer:
            detailedStr += "<<closed-by-server>>"

        detailedStr += "myCallpointName=%s" % self.myCallpointName
        detailedStr += ", myConfigKeyPath=%s" % self.myConfigKeyPath

        for (i, mapping) in enumerate(self.myMappings):
            detailedStr += ", mapping[%d]: keypath=%s, node=%s" & (i, mapping.keypath, mapping.node.getKeyPath())

        return detailedStr

    def setDaemonInfo(self, daemonCtx, controlSock, workerSock):
        for logFunc in self._log("set-daemon-info").debug3Func(): logFunc("called. daemonCtx=%s, controlSock=%s, workerSock=%s",
                                            daemonCtx, controlSock, workerSock)

        self.myDaemonCtx = daemonCtx
        self.myControlSock = controlSock
        self.myWorkerSock = workerSock

    def getDaemonCtx (self):
        return self.myDaemonCtx

    def getControlSock (self):
        return self.myControlSock

    def getWorkerSock (self):
        return self.myWorkerSock

    def markClosedByServer (self):
        self.myClosedByServer = True

    def isClosedByServer (self):
        return self.myClosedByServer
