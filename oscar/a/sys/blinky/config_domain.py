# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from domain_base import DomainBase

from a.sys.confd.pyconfdlib import pyconfdlib
import a.sys.confd.pyconfdlib.pyconfdlib_high
from a.sys.confd.pyconfdlib.key_path import KeyPath
from a.sys.confd.pyconfdlib.snmp_varbind import SnmpVarbind
from a.sys.confd.pyconfdlib.value import Value
from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes
from a.infra.misc.timeout_guard import TimeoutGuard
import a.infra.process.captain

import select
import socket
import threading
import time
import os
import sys
import json

from domain_priority import DomainPriority
from dp_registrations_db import DpRegistrationsDb
from dummy_blinky_node import DummyBlinkyNode
from pass_by_ref import PassByRef
from trx_element import TrxElement
from trx_context import TrxContext
from trx_phase import TrxPhase
from trx_progress import TrxProgress
from utils import Utils,Retry
from callpoint_context import CallpointContext
from dp_trx_context import DpTrxContext

class ConfigDomain (DomainBase):

    class Subscription(object):
        def __init__ (self):
            self.blinkyNode=None
            self.subscriptionId=0
        def __repr__ (self):
            return "{"+str(self.blinkyNode)+","+str(self.subscriptionId)+"}"

    class SyncMessages(EnumWithValue):
        def __init__ (self, value, name):
            EnumWithValue.__init__(self, value, name)

    kWakeUp=SyncMessages(0,"kWakeUp")
    kMaxSyncMessage=SyncMessages(1, "kMaxSyncMessage")


    def __init__ (self, logger):
        super(ConfigDomain, self).__init__(logger)
        self.myPriority=0
        self.myStopListenThread=False
        self.myConfigSubscriptionSocketId=0
        self.myDataSocketId=0
        self.myConfigDataSocketId=0
        self.myNumOfSocketsToListenOn=0
        self.myRegistrationDone=0
        self.mySubscriptionsMutex=None
        self.myTrxContext=None
        self.myBadConfigTrxElement=None
        self.mySubscriptions=[]

        self.mySyncPipeReadFd = 0
        self.mySyncPipeWriteFd = 0
        self.myDpRegistrationsMutex = None
        self.myDpRegDb = None

        self.myConfigErrorStr=""
        self.myIsInTrigger=False
        self.myBadConfigTrxElement=None
        self.myName=""
        self.myNodesToDomainTrxProgressNotification=[]
        self.myNodesToProgressNotificationPendingTrx=[]
        self.configDataSocketConnected=False

        self.snmpRegistrations = {}
        self.defaultNotifyName = ""
        #self.defaultNotifyName = "std_v2_trap"

        self._statsLogger = logger.createLogger("sys-blinky", "stats")

        self._configEventStartTimeKey = 'configEventStartTime'
        self._trxReadEndTime = 'trxReadEndTime'
        self._trxHandleEndTimeKey = 'trxHandleEndTime'
        self._trxElementsNumKey = 'trxElementsNum'
        self._trxValueSetNumKey = 'trxValueSetNum'
        self._trxCreateNumKey = 'trxCreateNum'
        self._trxDeleteNumKey = 'trxDeleteNum'
        self._trxMoveAfterNumKey = 'trxMoveAfterNum'

        self._triggerStartTimeKey = 'triggerStartTime'
        self._triggerEndTimeKey = 'triggerEndTime'
        self._prepareStartTimeKey = 'prepareStartTime'
        self._prepareEndTimeKey = 'prepareEndTime'
        self._commitStartTimeKey = 'commitStartTime'
        self._commitEndTimeKey = 'commitEndTime'

        self._triggerDataDict = {
            self._triggerStartTimeKey : 0,
            self._triggerEndTimeKey : 0,
            self._prepareStartTimeKey : 0,
            self._prepareEndTimeKey : 0,
            self._commitStartTimeKey : 0,
            self._commitEndTimeKey : 0
            }

    def init (self, agent, name, priority):
        super(ConfigDomain, self).init(agent, name)
        self.myPriority = priority

    def specificInit(self):
        for logFunc in self._log("specific-init").debug2Func(): logFunc("called.")
        self.myConfigSubscriptionSocketId=socket.socket()
        self.myDataSocketId=socket.socket()
        self.myNumOfSocketsToListenOn = self.myNumOfSocketsToListenOn+1
        self.myConfigDataSocketId=socket.socket()
        self.mySubscriptionsMutex = threading.Lock()
        self.myDpRegistrationsMutex = threading.Lock()
        (self.mySyncPipeReadFd, self.mySyncPipeWriteFd) = os.pipe()
        self.myDpRegDb = DpRegistrationsDb(self._log, self.myName)
        return ReturnCodes.kOk

    def specificShutdown (self):
        for logFunc in self._log("specific-shutdown").debug2Func(): logFunc("called.")
        self.myStopListenThread = True
        if self.myConfigSubscriptionSocketId:
            self.myConfigDataSocketId.shutdown(socket.SHUT_RDWR)
            self.myConfigDataSocketId.close()
            self.myConfigSubscriptionSocketId.shutdown(socket.SHUT_RDWR)
        try:
            self.myDpRegistrationsMutex.acquire()
            for dpSocket in self.myDpRegDb.getSockets():
                dpSocket.shutdown(socket.SHUT_RDWR)
                dpSocket.close()
        finally:
            self.myDpRegistrationsMutex.release()

    def resetTriggerDataDict (self, dict):
        self.myInitGuard.isInitOrCrash()
        for key in dict.keys():
            dict[key] = 0

    def writeSyncMessage (self, msgType):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("write-sync-message").debug3Func(): logFunc("called. msgType=%s, readFd=%d, writeFd=%d",
                                               msgType, self.mySyncPipeReadFd, self.mySyncPipeWriteFd)
        res = os.write(self.mySyncPipeWriteFd, str(msgType.getValue()))
        if res < len(str(msgType.getValue())):
            for logFunc in self._log("write-sync-message-failed").debug3Func(): logFunc("write() failed. msgType=%s, readFd=%d, writeFd=%d",
                                                          msgType, self.mySyncPipeReadFd, self.mySyncPipeWriteFd)
            return ReturnCodes.kGeneralError
        return ReturnCodes.kOk

    def destroy(self):
        for logFunc in self._log("destroy").infoFunc(): logFunc("destroy() called")
        self.myStopListenThread = True
        res = self.writeSyncMessage(self.kWakeUp)
        if (res != ReturnCodes.kOk):
            for logFunc in self._log("destroy-write-sync-msg-failed").errorFunc(): logFunc("writeSyncMsg(kWakeUp) failed")
            return ReturnCodes.kGeneralError
        return ReturnCodes.kOk

    def confdReloadConfig (self):
        for logFunc in self._log("confd-reload-config").infoFunc(): logFunc("called")
        return self.myAgent.confdReloadConfig()

    def registerNode(self, node):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("register-node").debug3Func(): logFunc("registerNode() called, node-key-path=%s", node.getKeyPath())
        if (self.myRegistrationDone):
            for logFunc in self._log("register-node-post-registration-done").errorFunc():
                logFunc("registerNode() failed because registration already done, node-key-path=%s", node.getKeyPath())
            a.infra.process.processFatal("domain %s: registerNode() failed because registration was already done. keypath=%s", 
                                   self.myName, node.getKeyPath())
    
        
        # make sure the domain priority is valid
        if self.myPriority == DomainPriority.kDummy:
            # this priority should never be used with a subscribing daemon
            for logFunc in self._log("register-node-illegal-priority").errorFunc():
                logFunc("called for a domain with dummy priority. Please set a valid domain priority.")
            a.infra.process.processFatal("domain %s: registerNode() failed because domain has dummy prioirity. Please set a valid domain priority.",
                                         self.myPriority)

                
        # Critical section
        try:
            self.mySubscriptionsMutex.acquire()
            node.addNodesToProgressNotification(self.myNodesToDomainTrxProgressNotification)
            subscription=self.Subscription()
            subscription.blinkyNode = node

            self.mySubscriptions.append(subscription)
            for logFunc in self._log("register-node-registered").debug3Func(): logFunc("registerNode() registered, node-key-path=%s, mySubscriptions=%s",
                                                         node.getKeyPath(), self.mySubscriptions)
        finally:
            self.mySubscriptionsMutex.release()

    def connectConfigDataSocket (self, fatalOnFailure):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("connect-config-data-socket").debug3Func(): logFunc("called")
        if not self.configDataSocketConnected:
            res = pyconfdlib.cdb_connect(self.myConfigDataSocketId, pyconfdlib.CDB_DATA_SOCKET, 
                                         pyconfdlib.AF_INET, self.myAgent.getConfdAddress(), self.myAgent.getConfdPort())
            if (res != pyconfdlib.CONFD_OK):
                for logFunc in self._log("connect-config-data-socket-cdb-connect-config-socket-failed").errorFunc():
                    logFunc("cdb_connect(CDB_DATA_SOCKET) failed, res=%s, confd_error=%s", res,
                           Utils.getConfdErrStr())
                if fatalOnFailure:
                    a.infra.process.processFatal("domain %s: connectConfigDataSocket() cdb_connect(CDB_DATA_SOCKET) failed, error=%s", 
                                           self.myName, Utils.getConfdErrStr())
                else:
                    return ReturnCodes.kGeneralError
            self.configDataSocketConnected = True
        else:
            for logFunc in self._log("connect-config-data-socket-already-connected").noticeFunc(): logFunc("data socket already connected")
        return ReturnCodes.kOk


    def registrationDone(self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("registration-done").debug3Func(): logFunc("registrationDone() called, len(mySubscriptions)=%s",
                                                     len(self.mySubscriptions))

        timeoutGuard = TimeoutGuard(self._log, '%s-registration-done' % (self.myName), 30000)

        res = pyconfdlib.cdb_connect(self.myConfigSubscriptionSocketId, pyconfdlib.CDB_SUBSCRIPTION_SOCKET, 
                                     pyconfdlib.AF_INET, self.myAgent.getConfdAddress(), self.myAgent.getConfdPort())
        if (res != pyconfdlib.CONFD_OK):
            for logFunc in self._log("registration-done-cdb-connect-subscription-socket-failed").errorFunc():
                logFunc("registrationDone() cdb_connect(CDB_SUBSCRIPTION_SOCKET) failed, res=%s, confd_error=%s", res,
                       Utils.getConfdErrStr())
            timeoutGuard.checkAndLog("registrationDone - fatal")
            a.infra.process.processFatal("domain %s: registrationDone() cdb_connect(CDB_SUBSCRIPTION_SOCKET) failed, error=%s", 
                                   self.myName, Utils.getConfdErrStr())

        res = pyconfdlib.cdb_connect(self.myDataSocketId, pyconfdlib.CDB_DATA_SOCKET, 
                                     pyconfdlib.AF_INET, self.myAgent.getConfdAddress(), self.myAgent.getConfdPort())
        if (res != pyconfdlib.CONFD_OK):
            for logFunc in self._log("registration-done-cdb-connect-data-socket-failed").errorFunc():
                logFunc("registrationDone() cdb_connect(CDB_DATA_SOCKET) failed, res=%s, confd_error=%s", res,
                       Utils.getConfdErrStr())
            timeoutGuard.checkAndLog("registrationDone - fatal")
            a.infra.process.processFatal("domain %s: registrationDone() cdb_connect(CDB_DATA_SOCKET) failed, error=%s", 
                                   self.myName, Utils.getConfdErrStr())

        self.connectConfigDataSocket(fatalOnFailure=True)

        for logFunc in self._log("registration-done-config-data-socket-connected").debug3Func(): logFunc("connectConfigDataSocket() succeeded")
    
        # Critical section
        try:    
            self.mySubscriptionsMutex.acquire()
            for logFunc in self._log("registration-done-lock-acquired").debug3Func(): logFunc("lock acquired")
            for subscription in self.mySubscriptions:
                for logFunc in self._log("registration-done-subscription").debug3Func(): logFunc("subscription")
                path_ = subscription.blinkyNode.getKeyPath().getCannonicalStr()
                for logFunc in self._log("registration-done-subscribe-before-1").debug3Func(): logFunc("cdb_subscribe2() before 1. keypath=%s", subscription.blinkyNode.getKeyPath())
                prefix = subscription.blinkyNode.getKeyPath().getPrefix()
                for logFunc in self._log("registration-done-subscribe-before").debug3Func(): logFunc("cdb_subscribe2() before. prefix=%s, path=%s", prefix, subscription.blinkyNode.getKeyPath())
                res = pyconfdlib.cdb_subscribe2(self.myConfigSubscriptionSocketId, pyconfdlib.CDB_SUB_RUNNING_TWOPHASE, 
                                                0, self.myPriority.getValue(), prefix, path_)
                if res[0] != pyconfdlib.CONFD_OK:
                    for logFunc in self._log("registration-done-subscribe2-failed").errorFunc():
                        logFunc("registrationDone() failed to cdb_subscribe2, path=%s, last ret val=%s, confd_error=%s", path_, res[0], Utils.getConfdErrStr())
                    timeoutGuard.checkAndLog("registrationDone - fatal")
                    a.infra.process.processFatal("domain %s: registrationDone() cdb_subscribe2 failed, path=%s, last ret val=%s, confd_error=%s, error=%s", 
                                           self.myName, path_, res[0], Utils.getConfdErrStr())
                #Value is a (rc, subscriptionId) tuple
                subscription.subscriptionId=res[1]
                for logFunc in self._log("registration-done-subscribe-done").debug3Func(): logFunc("cdb_subscribe2() done for path=%s, subscriptionId=%s", path_, subscription.subscriptionId)
            if len(self.mySubscriptions):
                res = pyconfdlib.cdb_subscribe_done(self.myConfigSubscriptionSocketId)
                if res != pyconfdlib.CONFD_OK:
                    for logFunc in self._log("registration-done-subscribe-done-failed").errorFunc():
                        logFunc("registrationDone() failed to cdb_subscribe_done, last ret val=%s, confd_error=%s",
                               res[0], Utils.getConfdErrStr())
                    timeoutGuard.checkAndLog("registrationDone - fatal")
                    a.infra.process.processFatal("domain %s: registrationDone() cdb_subscribe_done failed, last ret val=%s, confd_error=%s", 
                                           self.myName, path_, res[0], Utils.getConfdErrStr())
            
            self.myRegistrationDone = True

        finally:
            self.mySubscriptionsMutex.release()

        res = self.createListenThread()
        if (res != ReturnCodes.kOk):
            for logFunc in self._log("registration-done-create-listen-thread-failed").errorFunc(): logFunc("registrationDone() createListenThread failed")
            a.infra.process.processFatal("domain %s: registrationDone() createListenThread failed")

        timeoutGuard.checkAndLog("registrationDone")

    def createListenThread(self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("create-listen-thread").debug3Func(): logFunc("createListenThread() called")
        listenThread = threading.Thread(target=self.listen, name=self.myName)
        listenThread.daemon = True
        listenThread.start()
        return ReturnCodes.kOk
    
    def listen (self):
        self.myInitGuard.isInitOrCrash()
        try:
            for logFunc in self._log("listen").debug3Func(): logFunc("called")
        
            res = ReturnCodes.kOk
            while not self.myStopListenThread:
                try:
                    pollObj=select.poll()
                    pollObj.register(self.myConfigSubscriptionSocketId, select.POLLIN)
                    for logFunc in self._log("listen-subscription-sockets-registered-config-subscription-socket").debug4Func(): logFunc("registered myConfigSubscriptionSocketId to poll. self.myConfigSubscriptionSocketId=%d", self.myConfigSubscriptionSocketId.fileno())
                    pollObj.register(self.mySyncPipeReadFd, select.POLLIN)
                    self.myDpRegistrationsMutex.acquire()
                    dpFds = self.myDpRegDb.getFds()
                    for logFunc in self._log("listen-subscription-sockets-fds").debug3Func(): logFunc("adding fds to the poll set: %s", dpFds)
                    for dpFd in dpFds:
                        pollObj.register(dpFd, select.POLLIN)
                finally:
                    self.myDpRegistrationsMutex.release()
                x=pollObj.poll()
                if not self.myStopListenThread:
                    for (fd,event) in x:
                        if event == select.POLLIN:
                            for logFunc in self._log("listen-got-poll-event").debug3Func(): logFunc("got poll event")
                            if fd == self.myConfigSubscriptionSocketId.fileno():
                                for logFunc in self._log("listen-got-poll-event-config").debug2Func(): logFunc("got config poll event")
                                res = self.handleConfigSubscriptionSocketEvent()
                                if (res != ReturnCodes.kOk):
                                    for logFunc in self._log("listen-handle-socket-event-failed").errorFunc(): logFunc("handleConfigSubscriptionSocketEvent() failed")
                                    return ReturnCodes.kGeneralError
                            elif fd == self.mySyncPipeReadFd:
                                for logFunc in self._log("listen-got-poll-event-sync").debug2Func(): logFunc("got sync poll event")
                                # no need to do anything, just read the content and continue the loop
                                syncMsgStr = os.read(self.mySyncPipeReadFd, sys.getsizeof(self.kMaxSyncMessage))
                                syncMsg = self.SyncMessages.getByValue(int(syncMsgStr))
                                for logFunc in self._log("listen-got-poll-event-sync-msg").debug3Func(): logFunc("got sync poll event. msg=%s", syncMsg)
                                break
                            else:
                                for logFunc in self._log("listen-poll-exited").debug2Func(): logFunc("poll checking socket. fd=%d", fd)
                                try:
                                    self.myDpRegistrationsMutex.acquire()
                                    callpointCtx = self.myDpRegDb.getByFd(fd)
                                    # make sure the callpoint context exists in the db
                                    if not callpointCtx:
                                        for logFunc in self._log("listen-got-dp-fd-is-unknown").errorFunc(): logFunc("dp fd=%d is not in the callpoint context map", fd)
                                        # skip the error and continue
                                        continue
                                    for logFunc in self._log("listen-got-dp-poll-event").debug2Func(): logFunc("got dp poll event. fd=%d, callpointCtx=%s", fd, callpointCtx)
                                    res = pyconfdlib.confd_fd_ready(callpointCtx.getDaemonCtx(), fd)
                                    for logFunc in self._log("listen-confd-fd-ready-done").debug2Func(): logFunc("confd_fd_ready done. fd=%d, callpointCtx=%s", fd, callpointCtx)
                                    if res == pyconfdlib.CONFD_EOF:
                                        for logFunc in self._log("listen-oper-socket-closed-not-predicted").noticeFunc(): logFunc(
                                            "oper socket was closed. fd=%d, callpointCtx=%s, daemonCtx=%s", 
                                            fd, callpointCtx, callpointCtx.getDaemonCtx())
                                        callpointCtx.markClosedByServer()
                                        continue
                                    elif res != pyconfdlib.CONFD_OK and pyconfdlib.get_confd_errno() != pyconfdlib.CONFD_ERR_EXTERNAL:
                                        for logFunc in self._log("listen-confd-fd-ready-failed").errorFunc(): logFunc(
                                            "confd_fd_ready() failed. fd=%d, callpointCtx=%s, daemonCtx=%s, confdErrStr=%s", 
                                            fd, callpointCtx, callpointCtx.getDaemonCtx(), Utils.getConfdErrStr())
                                        return ReturnCodes.kGeneralError
                                finally:
                                    self.myDpRegistrationsMutex.release()
                        for logFunc in self._log("listen-subscription-sockets-for-loop-end").debug3Func(): logFunc("for loop ended")
                    for logFunc in self._log("listen-subscription-sockets-while-loop-end").debug3Func(): logFunc("while loop ended")
    
            for logFunc in self._log("listen-config-subscription-poll-stopped").noticeFunc(): logFunc("poll stopped")
            if not self.myStopListenThread:
                self.myConfigDataSocketId.shutdown(socket.SHUT_RDWR)
                self.myConfigSubscriptionSocketId.shutdown(socket.SHUT_RDWR)
            # close oper sockets
            try:
                self.myDpRegistrationsMutex.acquire()
                for dpSocket in self.myDpRegDb.getSockets():
                    #dpSocket.shutdown(socket.SHUT_RDWR)
                    dpSocket.close()
            finally:
                self.myDpRegistrationsMutex.release()

        except:
            for logFunc in self._log("listen-caught-exception").errorFunc(): logFunc("Exception in listen()")
            for logFunc in self._log("listen-exception").exceptionFunc(): logFunc("This is the exception:")
            a.infra.process.processFatal("listen caught an exception. domain=%s." % self.myName)

        return ReturnCodes.kOk

    def trxFailed (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("trx-failed").noticeFunc(): logFunc("trxFailed() called")
        errText="internal error"
        if len(self.myConfigErrorStr) > 0:
            errText=self.myConfigErrorStr
        # naamas - we don't want to include keypath in the error message
        #if self.myBadConfigTrxElement:
        #    errText = errText + " (" + self.myBadConfigTrxElement.getKeyPath().getCannonicalStr() + ")"

        res = pyconfdlib.cdb_sub_abort_trans(self.myConfigSubscriptionSocketId, 
                                             pyconfdlib.CONFD_ERRCODE_APPLICATION, 0, 0, errText)
        if (res != pyconfdlib.CONFD_OK):
            for logFunc in self._log("trx-failed-cdb-abort-trans-failed").errorFunc():
                logFunc("trxFailed() cdb_abort_transaction() failed, "
                       "myConfigErrorStr=%s confd_error=%s", 
                       self.myConfigErrorStr, Utils.getConfdErrStr())
        self.trxEnded(pyconfdlib.CDB_SUB_ABORT)
        res = self.endConfigReadSession(fatalOnFailure=False)
        if (res != ReturnCodes.kOk):
            for logFunc in self._log("trx-failed-cdb-end-config-read-session-failed").errorFunc():
                logFunc("trxFailed() endConfigReadSession() failed, "
                       "myConfigErrorStr=%s", self.myConfigErrorStr)
        self.myIsInTrigger = False
        return ReturnCodes.kOk

    def initStatsData (self, statsData):
        statsData[self._configEventStartTimeKey] = 0
        statsData[self._trxReadEndTime] = 0
        statsData[self._trxHandleEndTimeKey] = 0
        statsData[self._trxElementsNumKey] = 0
        statsData[self._trxValueSetNumKey] = 0
        statsData[self._trxCreateNumKey] = 0
        statsData[self._trxDeleteNumKey] = 0
        statsData[self._trxMoveAfterNumKey] = 0

    
    def handleConfigSubscriptionSocketEvent(self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("handle-config-subscription-socket-event").debug3Func(): logFunc("handleConfigSubscriptionSocketEvent() called")

        refPerformanceData = self._statsLogger.getPerformanceData()

        for logFunc in self._statsLogger("config-event-started").debug3Func() : logFunc("config event has started")
        statsData = {}
        self.initStatsData(statsData)

        statsData[self._configEventStartTimeKey] = time.time()

        timeoutGuard = TimeoutGuard(self._log, '%s-handle-config-subscription-event' % (self.myName), 300000, mildTimeoutMili=200000)

        (rc, subPoints, notificationType, flags)=pyconfdlib.cdb_read_subscription_socket2(self.myConfigSubscriptionSocketId)
        if rc != pyconfdlib.CONFD_OK:
            for logFunc in self._log("handle-config-subscription-socket-event-failed-cdb-read-subscription-socket").errorFunc():
                logFunc("handleConfigSubscriptionSocketEvent() - cdb_read_subscription_socket2() failed, rc=%s, confd_error=%s",
                       rc, Utils.getConfdErrStr())
            timeoutGuard.checkAndLog("configEvent - failed")
            return ReturnCodes.kGeneralError

        if flags & pyconfdlib.CDB_SUB_FLAG_TRIGGER:
            self.myIsInTrigger = True

        if self.isInTrigger():
            if (notificationType == pyconfdlib.CDB_SUB_PREPARE):
                self._triggerDataDict[self._prepareStartTimeKey] = time.time()
            elif (notificationType == pyconfdlib.CDB_SUB_COMMIT):
                self._triggerDataDict[self._commitStartTimeKey] = time.time()

        for logFunc in self._log("handle-config-subscription-socket-event-read-notification").debug3Func():
            logFunc("handleConfigSubscriptionSocketEvent() read-notification, notificationType=%s, flags=%s, subPoints=%s", notificationType, flags, subPoints)
        res = self.prepareTrxContext(notificationType)
        if (res != ReturnCodes.kOk):
            for logFunc in self._log("handle-config-subscription-socket-event-prepare-trx-context-failed").errorFunc():
                logFunc("handleConfigSubscriptionSocketEvent() prepareTrxContext() failed, notificationType=%s",
                       notificationType)
            self.myIsInTrigger = False
            timeoutGuard.checkAndLog("configEvent - failed")
            return ReturnCodes.kGeneralError
        
        res = self.startConfigReadSession(fatalOnFailure=False)
        if (res != ReturnCodes.kOk):
            for logFunc in self._log("handle-config-subscription-socket-event-start-config-read-session-failed").errorFunc():
                logFunc("handleConfigSubscriptionSocketEvent() - startConfigReadSession() failed, res=%s, confd_error=%s",
                       res, Utils.getConfdErrStr())
            self.myIsInTrigger = False
            timeoutGuard.checkAndLog("configEvent - failed")
            return ReturnCodes.kGeneralError

        timeoutGuard = TimeoutGuard(self._log, '%s-read-trx' % (self.myName), 90000, mildTimeoutMili=60000)
        for subPoint in subPoints:
            res = self.readTrx(subPoint, notificationType)
            if (res != ReturnCodes.kOk):
                for logFunc in self._log("handle-config-subscription-socket-event-read-trx-failed").errorFunc():
                    logFunc("handleConfigSubscriptionSocketEvent() readTrx() failed, subPoint=%s, notificationType=%s",
                           subPoint, notificationType)
                timeoutGuard.checkAndLog("configEvent - failed")
                return self.trxFailed()
            for logFunc in self._log("handle-config-subscription-socket-event-read-subscription-done").debug3Func():
                logFunc("read transaction: subpoint=%s, priority=%s, notificationType=%s",
                        subPoint, self.myPriority, notificationType)

        for logFunc in self._log("handle-config-subscription-socket-event-read-trx-done").debug3Func():
            logFunc("read complete transaction: subpoints=%s, priority=%s, notificationType=%s",
                    str(subPoints), self.myPriority, notificationType)

        timeoutGuard.checkAndLog("read-transaction-%d-elements" % (self.myTrxContext.getTrxElementsNum()))

        statsData[self._trxReadEndTime] = time.time()
        statsData[self._trxElementsNumKey] = self.myTrxContext.getTrxElementsNum()
        statsData[self._trxValueSetNumKey] = self.myTrxContext.getTrxValueSetElementsNum()
        statsData[self._trxCreateNumKey] = self.myTrxContext.getTrxCreateElementsNum()
        statsData[self._trxDeleteNumKey] = self.myTrxContext.getTrxDeleteElementsNum()
        statsData[self._trxMoveAfterNumKey] = self.myTrxContext.getTrxMovedAfterElementsNum()

        for logFunc in self._statsLogger("config-event-trx-read").debug3Func() : 
            logFunc("transaction was read. notificationType=%s, statsData=%s", 
                    notificationType, jsonDict=statsData)

        for logFunc in self._statsLogger("config-event-detailed-trx").debug3Func():
            self.myTrxContext.logDetailed(logFunc)

        timeoutGuard = TimeoutGuard(self._log, '%s-handle-trx-%d-elements' % (self.myName, self.myTrxContext.getTrxElementsNum()), 300000, mildTimeoutMili=200000)
        res = self.handleTrx(notificationType)
        if (res != ReturnCodes.kOk):
            if (notificationType == pyconfdlib.CDB_SUB_PREPARE):
                for logFunc in self._log("handle-config-subscription-socket-event-handle-trx-failed-prepare").noticeFunc():
                    logFunc("handleTrx() failed, notificationType=%s, res=%s", notificationType, res)
                res = self.handleTrx(pyconfdlib.CDB_SUB_ABORT)
                if (res != ReturnCodes.kOk):
                    for logFunc in self._log("handle-config-subscription-socket-event-handle-trx-failed").errorFunc():
                        logFunc("handleTrx(pyconfdlib.CDB_SUB_ABORT) failed, "\
                               "notificationType=%s, res=%s", notificationType, res)
            else:
                for logFunc in self._log("handle-config-subscription-socket-event-handle-trx-failed").errorFunc():
                    logFunc("handleTrx() failed, notificationType=%s, res=%s", notificationType, res)

            timeoutGuard.checkAndLog("configEvent - failed")
            return self.trxFailed()
        timeoutGuard.checkAndLog("handle-transaction")

        self._statsLogger.logPerformanceData("config event handled (%s)" % notificationType, reference=refPerformanceData,
                                             splitByModule=True, splitByGroup=True, splitByMsg=False, 
                                             splitByLevel=False, splitByInterfaceType=False)

        statsData[self._trxHandleEndTimeKey] = time.time()
        statsData[self._trxElementsNumKey] = self.myTrxContext.getTrxElementsNum()
        statsData[self._trxValueSetNumKey] = self.myTrxContext.getTrxValueSetElementsNum()
        statsData[self._trxCreateNumKey] = self.myTrxContext.getTrxCreateElementsNum()
        statsData[self._trxDeleteNumKey] = self.myTrxContext.getTrxDeleteElementsNum()
        statsData[self._trxMoveAfterNumKey] = self.myTrxContext.getTrxMovedAfterElementsNum()
        if self.isInTrigger():
            logFuncs = self._statsLogger("config-event-trx-handled").noticeFunc()
        else:
            logFuncs = self._statsLogger("config-event-trx-handled").debug1Func()
        for logFunc in logFuncs:
            logFunc("transaction was handled. notificationType=%s, overallDuration=%s, readDuration=%s, handleDuration=%s, statsData=", 
                    notificationType, 
                    int(statsData[self._trxHandleEndTimeKey]-statsData[self._configEventStartTimeKey]),
                    int(statsData[self._trxReadEndTime]-statsData[self._configEventStartTimeKey]),
                    int(statsData[self._trxHandleEndTimeKey]-statsData[self._trxReadEndTime]),
                    jsonDict=statsData)

        res = self.endConfigReadSession(fatalOnFailure=False)
        if (res != ReturnCodes.kOk):
            for logFunc in self._log("handle-config-subscription-socket-event-end-config-read-session-failed").errorFunc():
                logFunc("handleConfigSubscriptionSocketEvent() : endConfigReadSession() failed, res=%s, confd_error=%s",
                       res, Utils.getConfdErrStr())

        if self.isInTrigger():
            if (notificationType == pyconfdlib.CDB_SUB_PREPARE):
                self._triggerDataDict[self._prepareEndTimeKey] = time.time()
            elif (notificationType == pyconfdlib.CDB_SUB_COMMIT):
                self._triggerDataDict[self._commitEndTimeKey] = time.time()

        res = pyconfdlib.cdb_sync_subscription_socket(self.myConfigSubscriptionSocketId, pyconfdlib.CDB_DONE_PRIORITY)
        if (res != pyconfdlib.CONFD_OK):
            for logFunc in self._log("handle-config-subscription-socket-event-sync-socket-failed").errorFunc():
                logFunc("handleConfigSubscriptionSocketEvent() : cdb_sync_subscription_socket() failed, res=%s, confd_error=%s",
                       res, Utils.getConfdErrStr())
            self.myIsInTrigger = False
            timeoutGuard.checkAndLog("configEvent - failed")
            return ReturnCodes.kGeneralError
        
        self.trxEnded(notificationType)

        timeoutGuard.checkAndLog("configEvent")

        return ReturnCodes.kOk
    
        
    def iterConfigTrx(self, keyPath, operation, oldValue, newValue, trxContext, subscriptionId):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("iter-config-trx").debug4Func(): logFunc("iterConfigTrx() called, keyPath=%s, operation=%s, oldValue=%s, "\
                                            "newValue=%s, subscriptionId=%s", 
                                            keyPath, operation, oldValue, newValue, subscriptionId)

        recurse = True
        stop = False
        if ((operation==pyconfdlib.MOP_CREATED) or 
              (operation==pyconfdlib.MOP_DELETED) or 
              (operation==pyconfdlib.MOP_VALUE_SET) or
              (operation==pyconfdlib.MOP_MOVED_AFTER)):

            trxElement = TrxElement(self._log, keyPath, operation, oldValue, newValue, 
                                    subscriptionId)
            for logFunc in self._log("iter-config-trx-value").debug4Func(): logFunc("iterConfigTrx(): trxElement=%s", trxElement)
            if trxElement.isSystemDefault():
                recurse = False
                for logFunc in self._log("iter-config-trx-skipping-sys-default").debug4Func(): logFunc("iterConfigTrx(): trxElement=%s is system-default - skipping", trxElement)
            else:
                elementRegistered = self.isTrxElementRegistered(trxElement)
                if elementRegistered:
                    trxContext.addTrxElement(trxElement)
                else:
                    for logFunc in self._log("iter-config-trx-value").debug3Func(): logFunc("Element not registered: %s", trxElement)
                    recurse = False
                    stop = True
        else:
            for logFunc in self._log("iter-config-trx-skipping").debug3Func(): logFunc("iterConfigTrx() skipping unsupported operation, keyPath=%s, "\
                                                         "operation=%s, oldValue=%s, newValue=%s, subscriptionId=%s", 
                                                         keyPath, operation, oldValue, newValue, subscriptionId)

        if recurse:
            for logFunc in self._log("iter-config-trx-recursing").debug4Func(): logFunc("iterConfigTrx() returning ITER_RECURSE")
            return pyconfdlib.ITER_RECURSE
        else:
            if stop:
                for logFunc in self._log("iter-config-trx-not-recursing").debug4Func(): logFunc("iterConfigTrx() returning ITER_STOP")
                return pyconfdlib.ITER_STOP
            else:
                for logFunc in self._log("iter-config-trx-not-recursing").debug4Func(): logFunc("iterConfigTrx() returning ITER_UP")
                return pyconfdlib.ITER_UP

    def isTrxElementRegistered (self, trxElement):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("is-trx-element-registered").debug3Func(): logFunc("called, trxElement=%s", trxElement)
        elementRegistered = False

        subscriberBlinkyNode_PBR=PassByRef(None)
        res = self.getSubscriberBlinkyNode(trxElement.getSubscriptionId(), subscriberBlinkyNode_PBR)
        if (res != ReturnCodes.kOk):
            for logFunc in self._log("is-trx-element-registered-get-subscriber-failed").errorFunc():
                logFunc("getSubscriberBlinkyNode() failed, trxElement=%s", trxElement)
            return False

        subscriberBlinkyNode=subscriberBlinkyNode_PBR.value()
        if (subscriberBlinkyNode == None):
            for logFunc in self._log("is-trx-element-registered-no-subscriber-blinky-node").errorFunc():
                logFunc("getSubscriberBlinkyNode() returned NULL, trxElement=%s",
                       trxElement)
            return False

        for logFunc in self._log("is-trx-element-registered-subscriber-blinky-node").debug3Func():
            logFunc("getSubscriberBlinkyNode(): trxElement=%s, subscriberBlinkyNode=%s",
                    trxElement, subscriberBlinkyNode)

        keyPath = trxElement.getKeyPath()
        initialKeyDepth = subscriberBlinkyNode.getKeyPath().getLen()
        elementRegistered = subscriberBlinkyNode.isKeyPathRegistered(self._log, keyPath, initialKeyDepth)

        for logFunc in self._log("is-trx-element-registered-done").debug3Func(): logFunc("done, elementRegistered=%s, trxElement=%s", elementRegistered, trxElement)
        return elementRegistered

    
    def readTrx (self, subscriptionId, notificationType):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("read-trx").debug2Func(): logFunc("readTrx(): called, notificationType=%s, subscriptionId=%s",
                                     notificationType, subscriptionId)
    
        if (notificationType == pyconfdlib.CDB_SUB_PREPARE):
            class ConfigTrxIterationContext (object):
                def __init__ (self, domain, subscriptionId, trxContext):
                    self.domain = domain
                    self.subscriptionId = subscriptionId
                    self.trxContext = trxContext

                def iterFunc (self, keyPath, operation, oldValue, newValue):
                    __pychecker__="no-classattr"  # For some reason pychecker complains about this
                    self.domain._log("read-trx-cdb-diff-iterate-callback") \
                        .debug2("readTrx(): iterFunc() called, keyPath=%s, operation=%s, oldValue=%s, newValue=%s", 
                                keyPath, subscriptionId, oldValue, newValue)
                    rc=self.domain.iterConfigTrx(keyPath, operation, oldValue, newValue, self.trxContext, self.subscriptionId)
                    self.domain._log("read-trx-cdb-diff-iterate-callback-returning")\
                        .debug2("readTrx(): returning rc=%s", rc)
                    return rc
            
            iterationContext=ConfigTrxIterationContext(self, subscriptionId, self.myTrxContext)
            res = a.sys.confd.pyconfdlib.pyconfdlib_high.cdb_diff_iterate(
                self.myConfigSubscriptionSocketId, subscriptionId, iterationContext.iterFunc, 
                pyconfdlib.ITER_WANT_ANCESTOR_DELETE.getValue() | pyconfdlib.ITER_WANT_PREV.getValue())
            if (res != pyconfdlib.CONFD_OK):
                for logFunc in self._log("read-trx-cdb-diff-iterate-failed").errorFunc():
                    logFunc("readTrx(): cdb_diff_iterate() failed, notificationType=%s, subscriptionId=%s, "\
                           "res=%s, confd_error=%s", 
                           notificationType, subscriptionId, res, Utils.getConfdErrStr())
                return ReturnCodes.kGeneralError
        # TODO (naamas) - else - verify trxId is the same as what myTrxContext refers to
        return ReturnCodes.kOk

    
    def handleTrx(self, notificationType):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("handle-trx").debug2Func(): logFunc("handleTrx(): called, notificationType=%s", notificationType)
        for logFunc in self._log("handle-trx").debug4Func(): logFunc("handleTrx(): called, myTrxContext=%s", self.myTrxContext)
        isReverse = False
        confdPhase = TrxPhase.kConfdLast
        blinkyPhase = TrxPhase.kBlinkyLast
        if notificationType == pyconfdlib.CDB_SUB_PREPARE:
            confdPhase = TrxPhase.kPrepare
            blinkyPhase = TrxPhase.kBlinky
        elif notificationType == pyconfdlib.CDB_SUB_COMMIT:
            confdPhase = TrxPhase.kCommit
            blinkyPhase = TrxPhase.kPublic
        elif notificationType == pyconfdlib.CDB_SUB_ABORT:
            isReverse = True
            confdPhase = TrxPhase.kAbort
            blinkyPhase = TrxPhase.kPublic
        else:
            for logFunc in self._log("handle-trx-unexpected-notif-type").errorFunc():
                logFunc("handleTrx(): unexpected notification type, notificationType=%s", notificationType)
            return ReturnCodes.kGeneralError
        
        res = ReturnCodes.kOk
        # register all nodes that were pending a transaction
        for node in self.myNodesToProgressNotificationPendingTrx:
            self.myTrxContext.registerNodeToProgressNotification(node)
        self.myNodesToProgressNotificationPendingTrx = []

        phase=TrxPhase(confdPhase, blinkyPhase)
        while (phase.getBlinkyPhase() != TrxPhase.kBlinkyLast):
            for logFunc in self._log("handle-trx-context").debug3Func():
                logFunc("pahse=%s, trx-context: ", phase)
            self.myTrxContext.setTrxPhase(phase)
            for logFunc in self._log("handle-trx-context-details").debug3Func():
                self.myTrxContext.logDetailed(logFunc)
            trxProgressBefore = TrxProgress(phase, TrxProgress.kBefore)
            res = self.notifyProgressToNodes(trxProgressBefore)
            if (res != ReturnCodes.kOk):
                if trxProgressBefore.isPrepare():
                    for logFunc in self._log("handle-trx-notify-progress-to-nodes-before-failed-prepare").noticeFunc():
                        logFunc("handleTrx(): notifyProgressToNodes() failed, notificationType=%s, "\
                                "trxProgressBefore=%s", 
                                notificationType, trxProgressBefore)
                else:
                    for logFunc in self._log("handle-trx-notify-progress-to-nodes-before-failed").errorFunc():
                        logFunc("handleTrx(): notifyProgressToNodes() failed, notificationType=%s, "\
                               "trxProgressBefore=%s", 
                               notificationType, trxProgressBefore)
                return ReturnCodes.kGeneralError

            index=0
            if isReverse:
                index = len(self.myTrxContext.myTrxElements)-1

            while (isReverse and index>=0) or \
                (not isReverse and index < len(self.myTrxContext.myTrxElements)):
                for logFunc in self._log("handle-trx-element-trx-limits").debug3Func(): logFunc("handleTrx(): phase=%s, index=%d, numOfTrxElements=%d",
                                                                  phase, index, len(self.myTrxContext.myTrxElements))
                advance = True
                trxElement = self.myTrxContext.myTrxElements[index]
                responsible = trxElement.getBlinkyNode()
                for logFunc in self._log("handle-trx-element").debug3Func(): logFunc("handleTrx(): phase=%s, trxElement=%s, " \
                                                       "responsible=%s, index=%d", 
                                                       phase, trxElement, responsible, index)
                if (responsible == None):
                    if (phase.getConfdPhase() == TrxPhase.kCommit):
                        for logFunc in self._log("handle-trx-no-responsible").errorFunc():
                            logFunc("handleTrx(): no responsible for trx element, notificationType=%s, "\
                                   "trxElement=%s", 
                                   notificationType, trxElement)
                        self.myBadConfigTrxElement = trxElement
                        return ReturnCodes.kGeneralError

                    elif (phase.getConfdPhase() == TrxPhase.kAbort):
                        for logFunc in self._log("handle-trx-no-responsible-abort").noticeFunc():
                            logFunc("handleTrx(): no responsible for trx element, notificationType=%s, "\
                                    "trxElement=%s", 
                                    notificationType, trxElement)
                    else:
                        advance = False
                        res = self.getResponsibleBlinkyNode(index)
                        if (res != ReturnCodes.kOk):
                            if res == ReturnCodes.kNotFound:
                                for logFunc in self._log("handle-trx-responsible-blinky-node-failed-removing-top").debug1Func():
                                    logFunc("handleTrx(): removing top level elemnt from trx, notificationType=%s, "\
                                           "trxElement=%s", 
                                           notificationType, trxElement)
                                res = self.myTrxContext.removeElementAt(index)
                                if res != ReturnCodes.kOk:
                                    for logFunc in self._log("handle-trx-remove-element-from-context-failed").errorFunc():
                                        logFunc("handleTrx(): myTrxContext.removeElementAt() failed, notificationType=%s, "\
                                               "trxElement=%s, index=%d", 
                                               notificationType, trxElement, index)
                                    return ReturnCodes.kGeneralError
                            else:
                                for logFunc in self._log("handle-trx-responsible-blinky-node-failed").noticeFunc():
                                    logFunc("handleTrx(): getResponsibleBlinkyNode() failed, notificationType=%s, "\
                                            "trxElement=%s", 
                                            notificationType, trxElement)
                                self.myBadConfigTrxElement = trxElement
                                return ReturnCodes.kGeneralError
                else:
                    if ((phase.getConfdPhase() != TrxPhase.kAbort) or (trxElement.hasPreparePassed(phase))):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            trxElement.setPreparePassedOn(phase)
                        res = responsible.handleTrxElement(trxElement, trxElement.getBlinkyNodeKeyDepth(), phase)
                        if (res != ReturnCodes.kOk):
                            if (phase.getConfdPhase() == TrxPhase.kPrepare):
                                for logFunc in self._log("handle-trx-responsible-handle-trx-element-failed-prepare").noticeFunc():
                                    logFunc("handleTrx(): responsible.handleTrxElement() failed - aborting, phase=%s, "\
                                            "trxElement=%s, responsible.getKeyPath()=%s", 
                                            phase, trxElement, responsible.getKeyPath())
                            else:
                                for logFunc in self._log("handle-trx-responsible-handle-trx-element-failed").errorFunc():
                                    logFunc("handleTrx(): responsible.handleTrxElement() failed, phase=%s, "\
                                           "trxElement=%s, responsible.getKeyPath()=%s", 
                                           phase, trxElement, responsible.getKeyPath())
                            self.myBadConfigTrxElement = trxElement;
                            return ReturnCodes.kGeneralError

                if advance:
                    if isReverse:
                        index -= 1
                    else:
                        index += 1
                    
            trxProgressAfter = TrxProgress(phase, TrxProgress.kAfter)
            res = self.notifyProgressToNodes(trxProgressAfter)
            if (res != ReturnCodes.kOk):
                if trxProgressAfter.isPrepare():
                    for logFunc in self._log("handle-trx-notify-progress-to-nodes-after-failed-prepare").noticeFunc():
                        logFunc("handleTrx(): notifyProgressToNodes() failed, notificationType=%s, "\
                                "trxProgressAfter=%s", 
                                notificationType, trxProgressAfter)
                else:
                    for logFunc in self._log("handle-trx-notify-progress-to-nodes-after-failed").errorFunc():
                        logFunc("handleTrx(): notifyProgressToNodes() failed, notificationType=%s, "\
                               "trxProgressAfter=%s", 
                               notificationType, trxProgressAfter)
                return ReturnCodes.kGeneralError
            phase.gotoNextBlinkyPhase()
        
        return ReturnCodes.kOk
    
    def notifyProgressToNodes (self, trxProgress):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("notify-progress-to-nodes").debug3Func():
            logFunc("notifyProgressToNodes(): called, trxProgress=%s", trxProgress)

        if (trxProgress.myTrxPhase.getConfdPhase() != trxProgress.myTrxPhase.kAbort) or (self.myTrxContext.hasPreparePassed(trxProgress)):
            if trxProgress.myTrxPhase.getConfdPhase() == trxProgress.myTrxPhase.kPrepare:
                self.myTrxContext.setPreparePassedOn(trxProgress)
            nodesToNotify = self.myTrxContext.getNodesToProgressNotification()
            for logFunc in self._log("notify-progress-to-nodes-num").debug3Func():
                logFunc("num-of-nodes=%d trxProgress=%s", len(nodesToNotify), trxProgress)
            for node in nodesToNotify:
                res = node.handleTrxProgressNotification(trxProgress)
                if (res != ReturnCodes.kOk):
                    if trxProgress.isPrepare():
                        for logFunc in self._log("notify-progress-to-nodes-activate-failed-prepare").noticeFunc():
                            logFunc("notifyProgressToNodes(): handleTrxProgressNotification() failed, node=%s, trxProgress=%s",
                                    node, trxProgress)
                    else:
                        for logFunc in self._log("notify-progress-to-nodes-activate-failed").errorFunc():
                            logFunc("notifyProgressToNodes(): handleTrxProgressNotification() failed, node=%s, trxProgress=%s",
                                   node, trxProgress)
                    return ReturnCodes.kGeneralError

        return ReturnCodes.kOk
    
    def getResponsibleBlinkyNode(self, index):
        self.myInitGuard.isInitOrCrash()
        trxElement = self.myTrxContext.myTrxElements[index]
        for logFunc in self._log("get-responsible-blinky-node").debug3Func():
            logFunc("getResponsibleBlinkyNode(): called, trxElement=%s, index=%d", trxElement, index)
        subscriberBlinkyNode_PBR=PassByRef(None)
        res = self.getSubscriberBlinkyNode(trxElement.getSubscriptionId(), subscriberBlinkyNode_PBR)
        if (res != ReturnCodes.kOk):
            for logFunc in self._log("get-responsible-blinky-node-get-blinky-nodes-failed").errorFunc():
                logFunc("getResponsibleBlinkyNode(): getSubscriberBlinkyNode() failed, trxElement=%s",
                       trxElement)
            return ReturnCodes.kGeneralError
        
        subscriberBlinkyNode=subscriberBlinkyNode_PBR.value()
        if (subscriberBlinkyNode == None):
            for logFunc in self._log("get-responsible-blinky-node-no-subscriber-blinky-node").errorFunc():
                logFunc("getResponsibleBlinkyNode(): getSubscriberBlinkyNode() returned NULL, trxElement=%s",
                       trxElement)
            return ReturnCodes.kGeneralError
        
        for logFunc in self._log("get-responsible-blinky-node-subscriber-blinky-node").debug3Func():
            logFunc("getResponsibleBlinkyNode(): getSubscriberBlinkyNode(): trxElement=%s, "\
                    "subscriberBlinkyNode=%s", 
                    trxElement, subscriberBlinkyNode)

        """TODO (naamas) - isEqual() fails sometimes because the generator misses the correct namespace
        it happens when the tag belongs to an augmenting module. confd considers the namespace to be of the augmented module, 
        while the generator puts the augmenting one.
        fix this after generator revision is completed
        if subscriberBlinkyNode.getKeyPath().isEqual(trxElement.getKeyPath()):"""
        if subscriberBlinkyNode.getKeyPath().getLen() == trxElement.getKeyPath().getLen():
            for logFunc in self._log("get-responsible-blinky-node-root-created").infoFunc():
                logFunc("getResponsibleBlinkyNode():  root node was created, skipping notification. element=%s",
                      trxElement)
            return ReturnCodes.kNotFound

        keyDepth_PBR = PassByRef(subscriberBlinkyNode.getKeyPath().getLen())
        foundAtKeyDepth_PBR = PassByRef(keyDepth_PBR.value())
        responsible = subscriberBlinkyNode.findBlinkyNode(trxElement.getKeyPath(), keyDepth_PBR, foundAtKeyDepth_PBR)
        for logFunc in self._log("get-responsible-blinky-node-resp").debug3Func():
            logFunc("getResponsibleBlinkyNode(): findBlinkyNode() returned responsible=%s", responsible)
        if (responsible==None):
            for logFunc in self._log("get-responsible-blinky-node-no-responsible").noticeFunc():
                logFunc("getResponsibleBlinkyNode(): findBlinkyNode() didn't find anything, trxElement=%s",
                        trxElement)
            return ReturnCodes.kGeneralError
        
        directResponsibleDepth = trxElement.getKeyPath().getLen() - 1
        for logFunc in self._log("get-responsible-blinky-node-responsible").debug3Func():
            logFunc("getResponsibleBlinkyNode(): findBlinkyNode(): trxElement=%s, "\
                    "subscriberBlinkyNode.getKeyPath()=%s, responsible.getKeyPath()=%s, "\
                    "foundAtKeyDepth=%s, directResponsibleDepth=%s", 
                    trxElement, subscriberBlinkyNode.getKeyPath(), 
                    responsible.getKeyPath(), foundAtKeyDepth_PBR, directResponsibleDepth)

        if (foundAtKeyDepth_PBR.value() >= directResponsibleDepth):
            # found direct responsible
            trxElement.setBlinkyNode(responsible, foundAtKeyDepth_PBR.value())
        else:
            while (foundAtKeyDepth_PBR.value() < directResponsibleDepth):
                for logFunc in self._log("get-responsible-blinky-node-next-to-handle-is").debug3Func():
                    logFunc("getResponsibleBlinkyNode(): index=%d, trxElement=%s",
                            index, self.myTrxContext.myTrxElements[index])
                # found a parent. the real node still needs to be created
                foundAtKeyDepth_PBR.setValue(foundAtKeyDepth_PBR.value()+1)
                createKeyPath=KeyPath()
                createKeyPath.copyPartial(trxElement.getKeyPath(), foundAtKeyDepth_PBR.value())
                newTrxElement = TrxElement(self._log, createKeyPath, pyconfdlib.MOP_CREATED, None, None, 
                                           trxElement.getSubscriptionId())
                for logFunc in self._log("get-responsible-blinky-node-found-parent-adding").debug3Func():
                    logFunc("getResponsibleBlinkyNode(): implicit creating: createKeyPath=%s, trxElement=%s",
                            createKeyPath, trxElement)
                self.myTrxContext.myTrxElements.insert(index, newTrxElement)
                index += 1
            for logFunc in self._log("get-responsible-blinky-node-found-parent-after-addition").debug3Func():
                logFunc("getResponsibleBlinkyNode(): after addition: trxElement=%s"\
                        "now point to: %s", 
                        trxElement, index)


        return ReturnCodes.kOk
    
    
    def prepareTrxContext(self, notificationType):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("prepare-trx-context").debug3Func(): logFunc("prepareTrxContext(): called: notificationType=%s", notificationType)
        if notificationType==pyconfdlib.CDB_SUB_PREPARE:
            self.myTrxContext = TrxContext(self._log)
            self.myConfigErrorStr = ""
        elif (notificationType==pyconfdlib.CDB_SUB_ABORT) or \
             (notificationType==pyconfdlib.CDB_SUB_COMMIT) or \
             (notificationType==pyconfdlib.CDB_SUB_OPER):
            pass
        else:
            for logFunc in self._log("prepare-trx-context-unknown-notification-type").errorFunc():
                logFunc("prepareTrxContext(): unknown notification type: notificationType=%s", notificationType)
            return ReturnCodes.kOk
        return ReturnCodes.kOk

    def getTrxPhase (self):
        if self.myTrxContext:
            return self.myTrxContext.getTrxPhase()
        return TrxPhase(TrxPhase.kConfdLast, TrxPhase.kBlinkyLast)
    
    def trxEnded(self, notificationType):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("trx-ended").debug3Func(): logFunc("trxEnded(): called: tnotificationType=%s", notificationType)
        if (notificationType == pyconfdlib.CDB_SUB_COMMIT) or (notificationType == pyconfdlib.CDB_SUB_ABORT):
            self.myBadConfigTrxElement = None
            self.myTrxContext = None
            self.myIsInTrigger = False
    
    def getSubscriberBlinkyNode(self, subscriptionId, blinkyNode_PBR):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("get-subscriber-blinky-node").debug3Func(): logFunc("called: subscriptionId=%s", subscriptionId)
        
        for subscription in self.mySubscriptions:
            if (subscription.subscriptionId == subscriptionId):
                blinkyNode_PBR.setValue(subscription.blinkyNode)
                break
        return ReturnCodes.kOk
    
    def triggerSubscriptions(self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("trigger-subscriptions").noticeFunc(): logFunc("trigger starting")

        self.resetTriggerDataDict(self._triggerDataDict)
        self._triggerDataDict[self._triggerStartTimeKey] = time.time()

        timeoutGuard = TimeoutGuard(self._log, '%s-trigger-subscriptions' % (self.myName), 300000, mildTimeoutMili=200000)

        if not self.myRegistrationDone:
            for logFunc in self._log("trigger-subscriptions-registration-not-done").errorFunc(): logFunc("triggerSubscriptions(): registration not done yet!")
            timeoutGuard.checkAndLog("trigger-subscriptions - fatal")
            a.infra.process.processFatal("cdb_trigger_subscriptions failed. domain=%s. registration not done!" % self.myName)
        # Critical section
        try:
            self.mySubscriptionsMutex.acquire()
            subscriptions = []
            for subscription in self.mySubscriptions:
                subscriptions.append(subscription.subscriptionId)

            res = pyconfdlib.cdb_trigger_subscriptions(self.myDataSocketId, subscriptions)
            if res != pyconfdlib.CONFD_OK:
                for logFunc in self._log("trigger-subscriptions-failed").errorFunc():
                    logFunc("triggerSubscriptions(): cdb_trigger_subscriptions() failed: res=%s, confd_error=%s",
                           res, Utils.getConfdErrStr())
                timeoutGuard.checkAndLog("trigger-subscriptions - fatal")
                a.infra.process.processFatal("cdb_trigger_subscriptions failed. domain=%s. confd_error=%s"% (self.myName, Utils.getConfdErrStr()))
        finally:
            self.mySubscriptionsMutex.release()

        timeoutGuard.checkAndLog("trigger-subscriptions")

        self._triggerDataDict[self._triggerEndTimeKey] = time.time()

        for logFunc in self._statsLogger("trigger-subscription-duration").noticeFunc():
            logFunc('trigger statistics: trigger-start --> prepare-start=%.2f, prepare-end --> commit-start=%.2f, commit-end --> trigger-end=%.2f',
                    (self._triggerDataDict[self._prepareStartTimeKey]-  self._triggerDataDict[self._triggerStartTimeKey]),
                    (self._triggerDataDict[self._commitStartTimeKey] - self._triggerDataDict[self._prepareEndTimeKey]),
                    (self._triggerDataDict[self._triggerEndTimeKey] - self._triggerDataDict[self._commitEndTimeKey]))

        return ReturnCodes.kOk

    def setConfigErrorStr(self, error):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("set-config-error-str").debug3Func(): logFunc("setConfigErrorStr(): called: error=%s", error)
        if error and (len(error)>0):
            if len(self.myConfigErrorStr):
                self.myConfigErrorStr += ", "
            self.myConfigErrorStr = error

    def setDpErrorStr (self, transCtx, error):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("set-dp-error-str").debug3Func(): logFunc("setDpErrorStr(): called: error=%s, transCtx=%s", error, transCtx)
        if error and (len(error)>0):
            dpTrxContext = transCtx.getTransOpaque()
            dpTrxContext.setErrorStr(error)

    def setActionErrorStr (self, userInfo, error):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("set-action-error-str").debug3Func(): logFunc("setActionErrorStr(): called: error=%s, userInfo=%s", error, userInfo)
        if error and (len(error)>0):
            dpTrxContext = userInfo.getTransOpaque()
            dpTrxContext.setErrorStr(error)

    def isInTrigger (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("is-in-trigger").debug3Func(): logFunc("isInTrigger(): called: myIsInTrigger=%s", self.myIsInTrigger)
        return self.myIsInTrigger

    def registerNotifyTrxProgressFunctor (self, functor):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("register-notify-trx-progress-functor").debug3Func(): logFunc("registerNotifyTrxProgressFunctor(): called")
        if len(self.mySubscriptions):
            a.infra.process.processFatal("Cannot register progress notification functor after nodes have been registered")
        dummyKeyPath = KeyPath()
        dummyNode = DummyBlinkyNode(self._log)
        dummyNode.setParent(None)
        dummyNode.setKeyPath(dummyKeyPath)
        dummyNode.setDomain(self)
        dummyNode.setNotifyTrxProgressFunctor(functor, True)
        res = dummyNode.activate()
        if res != ReturnCodes.kOk:
            a.infra.process.processFatal("Dummy node activation failed")
        self.myNodesToDomainTrxProgressNotification.append(dummyNode)

    def registerNodeToProgressNotification (self, node):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("register-node-to-progress-notification").debug4Func(): logFunc("registerNodeToProgressNotification(): called. node=%s",
                                                                   node)
        if self.myTrxContext:
            self.myTrxContext.registerNodeToProgressNotification(node)
        else:
            # save pending nodes until there is a transaction
            self.myNodesToProgressNotificationPendingTrx.append(node)

    def startConfigReadSession (self, fatalOnFailure):
        for logFunc in self._log("start-config-read-session").debug3Func(): logFunc("called")
        res = pyconfdlib.cdb_start_session2(self.myConfigDataSocketId, pyconfdlib.CDB_RUNNING, 
                                            pyconfdlib.CDB_LOCK_REQUEST)
        if (res != pyconfdlib.CONFD_OK):
            for logFunc in self._log("start-config-read-session-cdb-start-session-failed").errorFunc():
                logFunc("cdb_start_session2() failed, res=%s, confd_error=%s",
                       res, Utils.getConfdErrStr())
            if fatalOnFailure:
                a.infra.process.processFatal("startConfigReadSession() - cdb_start_session2(CDB_RUNNING, CDB_LOCK_REQUEST) failed")
            else:
                return ReturnCodes.kGeneralError
        return ReturnCodes.kOk

    def endConfigReadSession (self, fatalOnFailure):
        for logFunc in self._log("end-config-read-session").debug3Func(): logFunc("called")
        res = pyconfdlib.cdb_end_session(self.myConfigDataSocketId)
        if (res != pyconfdlib.CONFD_OK):
            for logFunc in self._log("end-config-read-session-cdb-end-session-failed").errorFunc():
                logFunc("cdb_end_session() failed, res=%s, confd_error=%s",
                       res, Utils.getConfdErrStr())
            if fatalOnFailure:
                a.infra.process.processFatal("endConfigReadSession() - cdb_end_session() failed")
            else:
                return ReturnCodes.kGeneralError
        return ReturnCodes.kOk

    def readValueFromCdb(self, keyPath, value):
        """
        Reads a value according to 'keyPath' into 'value'
        """
        for logFunc in self._log("read-value-from-cdb").debug3Func(): logFunc("called. keyPath=%s", keyPath)
        # Just a silly type check
        Utils.fatalIfNotInstanceOf(keyPath, KeyPath)
        Utils.fatalIfNotInstanceOf(value, Value)

        self.myInitGuard.isInitOrCrash()

        timeoutGuard = TimeoutGuard(self._log, '%s-read-value-from-cdb-%s' % (self.myName, keyPath), 5000)

        closeSessionOnEnd = False

        if not self.configDataSocketConnected:
            self.connectConfigDataSocket(fatalOnFailure=True)
            self.startConfigReadSession(fatalOnFailure=True)
            closeSessionOnEnd = True
            
        keyPathStr = keyPath.getCannonicalStr()
        for logFunc in self._log("read-value-from-cdb").debug3Func(): logFunc("readValueFromCdb(): keyPathStr=%s", keyPathStr)
    
        res = a.sys.confd.pyconfdlib.pyconfdlib_high.cdb_get(self.myConfigDataSocketId, value, keyPathStr)
        if (res != pyconfdlib.CONFD_OK):
            for logFunc in self._log("read-value-from-cdb-cdb-get-failed").errorFunc():
                logFunc("readValueFromCdb(): cdb_get() failed. keyPathStr=%s, confd_error=%s",
                        keyPathStr, Utils.getConfdErrStr())
            timeoutGuard.checkAndLog("read-value-from-cdb - failed")
            return ReturnCodes.kGeneralError

        for logFunc in self._log("read-value-from-cdb-cdb-succeeded").debug3Func():
            logFunc("readValueFromCdb(): cdb_get() succeeded. keyPathStr=%s, value=%s",
                    keyPathStr, value)

        if closeSessionOnEnd:
            self.endConfigReadSession(fatalOnFailure=True)

        timeoutGuard.checkAndLog("read-value-from-cdb")
        return ReturnCodes.kOk

    def getDpSubscriptions (self):
        return self.myDpRegDb.getNumOfSubscriptions()

    def buildCallpointIndexKey (self, callpointName, configKeyPath):
        return "%s:%s" % (callpointName, str(configKeyPath))

    def getCallpointCtx (self, callpointName, configKeyPath):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("get-callpoint-ctx").debug3Func(): logFunc("called. callpointName=%s, configKeyPath=%s", callpointName, configKeyPath)

        key = self.buildCallpointIndexKey(callpointName, configKeyPath)
        return self.myDpRegDb.getByKey(key)

    def unregisterValidationPoint (self, validationPointName, configNode):
        for logFunc in self._log("unregister-validation-point").debug3Func(): logFunc("called. validationpoint=%s, configNode=%s",
                                                        validationPointName, configNode)
        emptyKeyPath = KeyPath()
        return self.unregisterCallpoint(validationPointName, configNode, emptyKeyPath)

    def unregisterActionPoint(self, actionPointName, configNode):
        for logFunc in self._log("unregister-action-point").debug3Func(): logFunc("called. actionPointName=%s, configNode=%s",
                                                    actionPointName, configNode)
        emptyKeyPath = KeyPath()
        return self.unregisterCallpoint(actionPointName, configNode, emptyKeyPath)

    def unregisterCallpoint (self, callpointName, configKeyPath, dpRelativePath):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("unregister-callpoint").debug3Func(): logFunc("called. callpointName=%s, configKeyPath=%s, dpRelativePath=%s", callpointName, configKeyPath, dpRelativePath)

        # TODO (naamas - split this function (it is too long)
        try:
            self.myDpRegistrationsMutex.acquire()

            callpointCtx = self.getCallpointCtx(callpointName, configKeyPath)
            if not callpointCtx:
                for logFunc in self._log("unregister-callpoint-get-callpoint-ctx-failed").errorFunc(): logFunc("getCallpointCtx(%s, %s) failed. dpRelativePath=%s",
                                                                                 callpointName, configKeyPath, dpRelativePath)
                return ReturnCodes.kGeneralError
            for logFunc in self._log("unregister-callpoint-got-callpoint-ctx").debug3Func(): logFunc("got callpoint ctx. callpointName=%s, configKeyPath=%s, dpRelativePath=%s",
                                                                       callpointName, configKeyPath, dpRelativePath)

            callpointCtx.removeMapping(dpRelativePath)

            shouldUnregister = callpointCtx.shouldUnregisterCallpoint()
            if shouldUnregister:
                for logFunc in self._log("unregister-callpoint-should-unregister-callpoint").debug3Func(): logFunc("should unregister callpoint. callpointName=%s, configKeyPath=%s, dpRelativePath=%s",
                                                                                     callpointName, configKeyPath, dpRelativePath)
                controlSock = callpointCtx.getControlSock()
                self.myDpRegDb.removeByFd(controlSock.fileno())
                workerSock = callpointCtx.getWorkerSock()
                self.myDpRegDb.removeByFd(workerSock.fileno())
                # notify the oper thread
                res = self.writeSyncMessage(self.kWakeUp)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log("unregister-callpoint-write-sync-msg-failed").errorFunc(): logFunc("writeSyncMsg(kWakeUp) failed. res=%s. callpointName=%s, configKeyPath=%s, dpRelativePath=%s",
                                                                                  res, callpointName, configKeyPath, dpRelativePath)
                    return ReturnCodes.kGeneralError

                controlSock.shutdown(socket.SHUT_RDWR)
                workerSock.shutdown(socket.SHUT_RDWR)

                daemonCtx = callpointCtx.getDaemonCtx()
                self.myDpRegDb.removeByDaemonId(daemonCtx.getDaemonId())
                pyconfdlib.confd_release_daemon(daemonCtx)

                key = self.buildCallpointIndexKey(callpointName, configKeyPath)
                self.myDpRegDb.removeByKey(key)
            else:
                for logFunc in self._log("unregister-callpoint-should-not-unregister-callpoint").debug3Func(): logFunc("should NOT unregister callpoint. callpointName=%s, configKeyPath=%s, dpRelativePath=%s",
                                                                                         callpointName, configKeyPath, dpRelativePath)

        finally:
            self.myDpRegistrationsMutex.release()

        return ReturnCodes.kOk

    def buildCallpointCtx (self, configKeyPath, callpointName):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("build-callpoint-ctx").debug3Func(): logFunc("called. configKeyPath=%s, callpointName=%s",
                                                configKeyPath, callpointName)
        # allocate new entry
        callpointCtx = CallpointContext(self._log)
        callpointCtx.setConfigObjKeyPath(configKeyPath)
        callpointCtx.setCallpointName(callpointName)

        key = self.buildCallpointIndexKey(callpointName, configKeyPath)
        res = self.myDpRegDb.storeByKey(key, callpointCtx)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("build-callpoint-ctx-store-new-entry-failed").errorFunc(): logFunc(
                "myDpRegDb.storeByKey() failed. configKeyPath=%s, callpointName=%s", 
                configKeyPath, callpointName)
            return ReturnCodes.kGeneralError
        for logFunc in self._log("build-callpoint-ctx-new-entry").debug3Func(): logFunc(
            "allocated new entry. configKeyPath=%s, callpointName=%s", 
            configKeyPath, callpointName)
        return callpointCtx

    def registerValidationCb (self, configKeyPath, validationPointName, callpointCtx, daemonCtx):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("register-validation-cb").debug3Func(): logFunc("called. configKeyPath=%s, validationPointName=%s, callpointCtx=%s, daemonCtx=%s",
                                                   configKeyPath, validationPointName, callpointCtx, daemonCtx)

        # register validate trans cb
        res = a.sys.confd.pyconfdlib.pyconfdlib.confd_register_validate_cb(daemonCtx, initCb=self.dpInitTrans, stopCb=self.dpTransFinish, callBackData=callpointCtx)
        if (res != pyconfdlib.CONFD_OK):
            for logFunc in self._log("register-validation-cb-confd-register-validate-cb-failed").errorFunc(): logFunc(
                "confd_register_trans_cb() failed. configKeyPath=%s, validationPointName=%s, callpointCtx=%s, daemonCtx=%s, res=%s, confd_error=%s", 
                configKeyPath, validationPointName, callpointCtx, daemonCtx, res, Utils.getConfdErrStr())
            return ReturnCodes.kGeneralError

        # register action cb
        listKeys = configKeyPath.getListKeys()
        if len(listKeys):
            registrationPath = KeyPath()
            registrationPath.copyStaticPartUpToLowestList(configKeyPath)
            res = a.sys.confd.pyconfdlib.pyconfdlib_high.confd_register_range_valpoint_cb(
                daemonCtx, validationPointName,  registrationPath.getCannonicalStr(), listKeys[-1], listKeys[-1], self.dpValidate, callBackData=callpointCtx) 
            if res != pyconfdlib.CONFD_OK:
                for logFunc in self._log("register-validation-cb-validation-cb-range-reigsteration-failed").errorFunc(): logFunc(
                    "confd_register_range_action_cb() failed. configKeyPath=%s, validationPointName=%s, callpointCtx=%s, daemonCtx=%s, daemon_id=%d, daemonCtx=%s, error=%s", 
                    configKeyPath, validationPointName, callpointCtx, daemonCtx, daemonCtx.getDaemonId(), daemonCtx, Utils.getConfdErrStr())
                return ReturnCodes.kGeneralError
            for logFunc in self._log("register-validation-cb-range-validation-cb-range-reigstered").debug3Func(): logFunc(
                "confd_register_range_action_cb() done. configKeyPath=%s, validationPointName=%s, callpointCtx=%s, daemonCtx=%s, daemon_id=%d", 
                configKeyPath, validationPointName, callpointCtx, daemonCtx, daemonCtx.getDaemonId())
        else:
            res = a.sys.confd.pyconfdlib.pyconfdlib_high.confd_register_valpoint_cb(daemonCtx, validationPointName, self.dpValidate, callBackData=callpointCtx) 
            if res != pyconfdlib.CONFD_OK:
                for logFunc in self._log("register-validation-cb-validation-cb-reigsteration-failed").errorFunc(): logFunc(
                    "confd_register_action_cb() failed. configKeyPath=%s, validationPointName=%s, callpointCtx=%s, daemonCtx=%s, daemon_id=%d", 
                    configKeyPath, validationPointName, callpointCtx, daemonCtx, daemonCtx.getDaemonId())
                return ReturnCodes.kGeneralError
            for logFunc in self._log("register-validation-cb-range-validation-cb-reigstered").debug3Func(): logFunc(
                "confd_register_action_cb() done. configKeyPath=%s, validationPointName=%s, callpointCtx=%s, daemonCtx=%s, daemon_id=%d", 
                configKeyPath, validationPointName, callpointCtx, daemonCtx, daemonCtx.getDaemonId())

        return ReturnCodes.kOk

    def registerActionCb (self, configKeyPath, actionPointName, callpointCtx, daemonCtx):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("register-action-cb").debug3Func(): logFunc("called. configKeyPath=%s, actionPointName=%s, callpointCtx=%s, daemonCtx=%s",
                                               configKeyPath, actionPointName, callpointCtx, daemonCtx)

        # register action cb
        listKeys = configKeyPath.getListKeys()
        if len(listKeys):
            registrationPath = KeyPath()
            registrationPath.copyStaticPartUpToLowestList(configKeyPath)
            res = a.sys.confd.pyconfdlib.pyconfdlib_high.confd_register_range_action_cb(
                daemonCtx, actionPointName,  registrationPath.getCannonicalStr(), listKeys[-1], listKeys[-1], self.dpInitAction, self.dpDoAction, callBackData=callpointCtx) 
            if res != pyconfdlib.CONFD_OK:
                for logFunc in self._log("register-action-cb-action-cb-range-reigsteration-failed").errorFunc(): logFunc(
                    "confd_register_range_action_cb() failed. configKeyPath=%s, actionPointName=%s, callpointCtx=%s, daemonCtx=%s, daemon_id=%d, daemonCtx=%s, error=%s", 
                    configKeyPath, actionPointName, callpointCtx, daemonCtx, daemonCtx.getDaemonId(), daemonCtx, Utils.getConfdErrStr())
                return ReturnCodes.kGeneralError
            for logFunc in self._log("register-action-cb-range-action-cb-range-reigstered").debug3Func(): logFunc(
                "confd_register_range_action_cb() done. configKeyPath=%s, actionPointName=%s, callpointCtx=%s, daemonCtx=%s, daemon_id=%d", 
                configKeyPath, actionPointName, callpointCtx, daemonCtx, daemonCtx.getDaemonId())
        else:
            res = a.sys.confd.pyconfdlib.pyconfdlib_high.confd_register_action_cb(daemonCtx, actionPointName, self.dpInitAction, self.dpDoAction, callBackData=callpointCtx) 
            if res != pyconfdlib.CONFD_OK:
                for logFunc in self._log("register-action-cb-action-cb-reigsteration-failed").errorFunc(): logFunc(
                    "confd_register_action_cb() failed. configKeyPath=%s, actionPointName=%s, callpointCtx=%s, daemonCtx=%s, daemon_id=%d, daemonCtx=%s", 
                    configKeyPath, actionPointName, callpointCtx, daemonCtx, daemonCtx.getDaemonId(), daemonCtx)
                return ReturnCodes.kGeneralError
            for logFunc in self._log("register-action-cb-range-action-cb-reigstered").debug3Func(): logFunc(
                "confd_register_action_cb() done. configKeyPath=%s, actionPointName=%s, callpointCtx=%s, daemonCtx=%s, daemon_id=%d", 
                configKeyPath, actionPointName, callpointCtx, daemonCtx, daemonCtx.getDaemonId())

        return ReturnCodes.kOk

    def registerTransformationCbWrapper (self, node):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("register-transformation-cb-wrapper").debug3Func(): logFunc("called. node=%s", node)

        def registerTransformationCb (configKeyPath, callpointName, callpointCtx, daemonCtx):
            self.myInitGuard.isInitOrCrash()
            for logFunc in self._log("register-transformation-cb").debug3Func(): logFunc("called. configKeyPath=%s, callpointName=%s, callpointCtx=%s, daemonCtx=%s, node=%s",
                                                           configKeyPath, callpointName, callpointCtx, daemonCtx, node)
            # register trans cb
            res = pyconfdlib.confd_register_trans_cb(daemonCtx, initCb=self.dpInitTransfomrationTransWrapper(node), finishCb=self.dpTransfomrationTransFinishWrapper(node), callBackData=callpointCtx)
            if res != pyconfdlib.CONFD_OK:
                for logFunc in self._log("register-transformation-cb-register-trans-cb-failed").errorFunc(): logFunc(
                    "confd_register_trans_cb() failed. configKeyPath=%s, callpointName=%s, callpointCtx=%s, daemonCtx=%s, error=%s", 
                    configKeyPath, callpointName, callpointCtx, daemonCtx, Utils.getConfdErrStr())
                return ReturnCodes.kGeneralError
            for logFunc in self._log("register-transformation-cb-trans-cb-reigstered").debug3Func(): logFunc(
                "confd_register_trans_cb() done. configKeyPath=%s, callpointName=%s, callpointCtx=%s, daemonCtx=%s, daemon_id=%s, daemonCtx=%s", 
                configKeyPath, callpointName, callpointCtx, daemonCtx.getDaemonId(), daemonCtx)

            # register data cb
            res = a.sys.confd.pyconfdlib.pyconfdlib_high.confd_register_transformation_data_cb(
                daemonCtx, callpointName, self.dpGetElem, self.dpGetNext, self.dpSetElem, self.dpCreate, self.dpRemove, callBackData=callpointCtx) 
            if res != pyconfdlib.CONFD_OK:
                for logFunc in self._log("register-transformation-cb-data-cb-reigsteration-failed").errorFunc(): logFunc(
                    "confd_register_data_cb() failed. configKeyPath=%s, callpointName=%s, callpointCtx=%s, daemonCtx=%s, daemon_id=%d, daemonCtx=%s", 
                    daemonCtx, daemonCtx.getDaemonId(), daemonCtx)
                return ReturnCodes.kGeneralError
            for logFunc in self._log("register-transformation-cb-range-data-cb-reigstered").debug3Func(): logFunc(
                "confd_register_transformation_data_cb() done. configKeyPath=%s, callpointName=%s, callpointCtx=%s, daemonCtx=%s, daemon_id=%d, daemonCtx=%s", 
                configKeyPath, callpointName, callpointCtx, daemonCtx, daemonCtx.getDaemonId(), daemonCtx)
    
            return ReturnCodes.kOk
        return registerTransformationCb


    def registerOperCb (self, configKeyPath, callpointName, callpointCtx, daemonCtx):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("register-oper-cb").debug3Func(): logFunc("called. configKeyPath=%s, callpointName=%s, callpointCtx=%s, daemonCtx=%s",
                                             configKeyPath, callpointName, callpointCtx, daemonCtx)
        # register trans cb
        res = pyconfdlib.confd_register_trans_cb(daemonCtx, initCb=self.dpInitTrans, finishCb=self.dpTransFinish, callBackData=callpointCtx)
        if res != pyconfdlib.CONFD_OK:
            for logFunc in self._log("register-oper-cb-register-trans-cb-failed").errorFunc(): logFunc(
                "confd_register_trans_cb() failed. configKeyPath=%s, callpointName=%s, callpointCtx=%s, daemonCtx=%s, error=%s", 
                configKeyPath, callpointName, callpointCtx, daemonCtx, Utils.getConfdErrStr())
            return ReturnCodes.kGeneralError
        for logFunc in self._log("register-action-cb-trans-cb-reigstered").debug3Func(): logFunc(
            "confd_register_trans_cb() done. configKeyPath=%s, callpointName=%s, callpointCtx=%s, daemonCtx=%s, daemon_id=%d, daemonCtx=%s", 
            configKeyPath, callpointName, callpointCtx, daemonCtx.getDaemonId(), daemonCtx)

        # register data cb
        listKeys = configKeyPath.getListKeys()
        if len(listKeys):
            registrationPath = KeyPath()
            registrationPath.copyStaticPartUpToLowestList(configKeyPath)
            res = a.sys.confd.pyconfdlib.pyconfdlib_high.confd_register_range_data_cb(
                daemonCtx, callpointName,  registrationPath.getCannonicalStr(), listKeys[-1], listKeys[-1], self.dpGetElem, self.dpGetNext, self.dpGetObj, callBackData=callpointCtx) 
            if res != pyconfdlib.CONFD_OK:
                for logFunc in self._log("register-oper-cb-data-cb-range-reigsteration-failed").errorFunc(): logFunc(
                    "confd_register_range_data_cb() failed. configKeyPath=%s, callpointName=%s, callpointCtx=%s, daemonCtx=%s, daemon_id=%d, daemonCtx=%s, error=%s", 
                    configKeyPath, callpointName, callpointCtx, daemonCtx, daemonCtx.getDaemonId(), daemonCtx, Utils.getConfdErrStr())
                return ReturnCodes.kGeneralError
            for logFunc in self._log("register-oper-cb-range-data-cb-range-reigstered").debug3Func(): logFunc(
                "confd_register_range_data_cb() done. configKeyPath=%s, callpointName=%s, callpointCtx=%s, daemonCtx=%s, daemon_id=%d, daemonCtx=%s", 
                configKeyPath, callpointName, callpointCtx, daemonCtx, daemonCtx.getDaemonId(), daemonCtx)
        else:
            res = a.sys.confd.pyconfdlib.pyconfdlib_high.confd_register_data_cb(daemonCtx, callpointName, self.dpGetElem, self.dpGetNext, self.dpGetObj, callBackData=callpointCtx) 
            if res != pyconfdlib.CONFD_OK:
                for logFunc in self._log("register-oper-cb-data-cb-reigsteration-failed").errorFunc(): logFunc(
                    "confd_register_data_cb() failed. configKeyPath=%s, callpointName=%s, callpointCtx=%s, daemonCtx=%s, daemon_id=%d, daemonCtx=%s", 
                    daemonCtx, daemonCtx.getDaemonId(), daemonCtx)
                return ReturnCodes.kGeneralError
            for logFunc in self._log("register-oper-cb-range-data-cb-reigstered").debug3Func(): logFunc(
                "confd_register_data_cb() done. configKeyPath=%s, callpointName=%s, callpointCtx=%s, daemonCtx=%s, daemon_id=%d, daemonCtx=%s", 
                configKeyPath, callpointName, callpointCtx, daemonCtx, daemonCtx.getDaemonId(), daemonCtx)

        return ReturnCodes.kOk


    def registerCallpointToConfd (self, configKeyPath, callpointName, callpointCtx, dpCbRegistrationFunc):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("register-callpoint-to-confd").debug3Func(): logFunc("called. configKeyPath=%s, callpointName=%s, callpointCtx=%s",
                                                        configKeyPath, callpointName, callpointCtx)

        timeoutGuard = TimeoutGuard(self._log, '%s-register-callpoint-to-confd-%s' % (self.myName, callpointName), 5000)
        listKeys = configKeyPath.getListKeys()
        daemonName = "%s-%s" % (self.myName, callpointName)
        for listKey in listKeys:
            daemonName += "-" + str(listKey)
        daemonName += "-daemon"

        # create the daemon
        daemonCtx = pyconfdlib.confd_init_daemon(daemonName)
        if not daemonCtx:
            for logFunc in self._log("register-callpoint-to-confd-confd-init-daemon-failed").errorFunc(): logFunc(
                "confd_init_daemon(%s) failed. configKeyPath=%s, callpointName=%s, callpointCtx=%s, daemonName=%s, error: %s", 
                configKeyPath, callpointName, callpointCtx, daemonName, Utils.getConfdErrStr())
            timeoutGuard.checkAndLog("register-callpoint-to-confd - failed")
            return ReturnCodes.kGeneralError

        # create control socket
        controlSock = socket.socket()
        # connect control socket
        res = pyconfdlib.confd_connect(daemonCtx, controlSock, pyconfdlib.CONTROL_SOCKET, 
                                       pyconfdlib.AF_INET, self.myAgent.getConfdAddress(), self.myAgent.getConfdPort())
        if res != pyconfdlib.CONFD_OK:
            for logFunc in self._log("register-callpoint-to-confd-confd-connect-control-socket-failed").errorFunc(): logFunc(
                "confd_connect() for control socket failed. configKeyPath=%s, callpointName=%s, callpointCtx=%s, controlSock=%d, error: %s", 
                configKeyPath, callpointName, callpointCtx, controlSock.fileno(), Utils.getConfdErrStr())
            return ReturnCodes.kGeneralError
        for logFunc in self._log("register-callpoint-control-sock-connected").debug3Func(): logFunc(
            "control socket connected. configKeyPath=%s, callpointName=%s, callpointCtx=%s, controlSock=%d, daemonName=%s", 
            configKeyPath, callpointName, callpointCtx, controlSock.fileno(), daemonName)
        # create worker socket
        workerSock = socket.socket()
        # connect worker socket
        res = pyconfdlib.confd_connect(daemonCtx, workerSock, pyconfdlib.WORKER_SOCKET, 
                                       pyconfdlib.AF_INET, self.myAgent.getConfdAddress(), self.myAgent.getConfdPort())
        if res != pyconfdlib.CONFD_OK:
            for logFunc in self._log("register-callpoint-to-confd-confd-connect-worker-socket-failed").errorFunc(): logFunc(
                "confd_connect() for worker socket failed. configKeyPath=%s, callpointName=%s, callpointCtx=%s, workerSock=%d, error: %s", 
                configKeyPath, callpointName, callpointCtx, workerSock.fileno(), Utils.getConfdErrStr())
            timeoutGuard.checkAndLog("register-callpoint-to-confd - failed")
            return ReturnCodes.kGeneralError
        for logFunc in self._log("register-callpoint-worker-sock-connected").debug3Func(): logFunc(
            "worker socket connected. configKeyPath=%s, callpointName=%s, callpointCtx=%s, workerSock=%d, daemonName=%s", 
            configKeyPath, callpointName, callpointCtx, workerSock.fileno(), daemonName)

        res = self.myDpRegDb.storeByDaemonId(daemonCtx.getDaemonId(), callpointCtx)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("register-callpoint-store-by-daemon-id-failed").errorFunc(): logFunc(
                "myDpRegDb.storeByDaemonId() failed. configKeyPath=%s, callpointName=%s, callpointCtx=%s, daemonName=%s, daemon_id=%d, daemonCtx=%s", 
                configKeyPath, callpointName, callpointCtx, daemonName, daemonCtx.getDaemonId(), daemonCtx)
            timeoutGuard.checkAndLog("register-callpoint-to-confd - failed")
            return ReturnCodes.kGeneralError
        for logFunc in self._log("register-callpoint-store-by-daemon-id-succeeded").debug3Func(): logFunc(
            "myDpRegDb.storeByDaemonId() succeeded. configKeyPath=%s, callpointName=%s, callpointCtx=%s, daemonName=%s, daemon_id=%d, daemonCtx=%s", 
            configKeyPath, callpointName, callpointCtx, daemonName, daemonCtx.getDaemonId(), daemonCtx)

        res = dpCbRegistrationFunc(configKeyPath, callpointName, callpointCtx, daemonCtx)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("register-callpoint-cb-registration-func-failed").errorFunc(): logFunc(
                "dpCbRegistrationFunc() failed. configKeyPath=%s, callpointName=%s, callpointCtx=%s, daemonName=%s, daemon_id=%d, daemonCtx=%s", 
                configKeyPath, callpointName, callpointCtx, daemonName, daemonCtx.getDaemonId(), daemonCtx)
            timeoutGuard.checkAndLog("register-callpoint-to-confd - failed")
            return ReturnCodes.kGeneralError

        # store daemon context and sockets on the callpointCtx
        callpointCtx.setDaemonInfo(daemonCtx, controlSock, workerSock)
        # store the callpoint according to socket Ids
        res = self.myDpRegDb.storeByFd(controlSock.fileno(), callpointCtx)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("register-callpoint-to-confd-store-by-control-fd-failed").errorFunc(): logFunc(
                "myDpRegDb.storeByFd(controlSock) failed. configKeyPath=%s, callpointName=%s, callpointCtx=%s, controlSock=%d, workerSock=%d", 
                configKeyPath, callpointName, callpointCtx, controlSock.fileno(), workerSock.fileno())
            timeoutGuard.checkAndLog("register-callpoint-to-confd - failed")
            return ReturnCodes.kGeneralError

        res = self.myDpRegDb.storeByFd(workerSock.fileno(), callpointCtx)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("register-callpoint-to-confd-store-by-worker-fd-failed").errorFunc(): logFunc(
                "myDpRegDb.storeByFd(workerSock) failed. configKeyPath=%s, callpointName=%s, callpointCtx=%s, controlSock=%d, workerSock=%d", 
                configKeyPath, callpointName, callpointCtx, controlSock.fileno(), workerSock.fileno())
            timeoutGuard.checkAndLog("register-callpoint-to-confd - failed")
            return ReturnCodes.kGeneralError

        # registration done
        res = pyconfdlib.confd_register_done(daemonCtx)
        if res != pyconfdlib.CONFD_OK:
            for logFunc in self._log("register-callpoint-to-confd-confd-register-done-failed").errorFunc(): logFunc(
                "confd_register_done() failed. configKeyPath=%s, callpointName=%s, callpointCtx=%s, daemonName=%s, daemonCtx=%s, confdErr=%s", 
                configKeyPath, callpointName, callpointCtx, daemonName, daemonCtx, Utils.getConfdErrStr())
            timeoutGuard.checkAndLog("register-callpoint-to-confd - failed")
            return ReturnCodes.kGeneralError

        # notify the oper thread
        res = self.writeSyncMessage(self.kWakeUp)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("register-callpoint-write-sync-msg-failed").errorFunc(): logFunc(
                "writeSyncMsg(kWakeUp) failed. configKeyPath=%s, callpointName=%s, callpointCtx=%s, daemonName=%s, daemonCtx=%s", 
                configKeyPath, callpointName, callpointCtx, daemonName, daemonCtx)
            timeoutGuard.checkAndLog("register-callpoint-to-confd - failed")
            return ReturnCodes.kGeneralError

        timeoutGuard.checkAndLog("register-callpoint-to-confd")
        return ReturnCodes.kOk

    def registerCallpoint (self, callpointName, configNode, dpRelativePath, dpNode, dpCbRegistrationFunc):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("register-callpoint").debug3Func(): logFunc("called. callpointName=%s, configNode=%s, dpRelativePath=%s, dpNode=%s",
                                               callpointName, configNode.getKeyPath(), dpRelativePath, dpNode.getKeyPath())

        try:
            self.myDpRegistrationsMutex.acquire()

            configKeyPath = configNode.getKeyPath()
            #TODO - naamas - start debugging here - under what keypath is this node registered?
            callpointCtx = self.getCallpointCtx(callpointName, configKeyPath)
            if not callpointCtx:
                callpointCtx = self.buildCallpointCtx(configKeyPath, callpointName)
            else:
                for logFunc in self._log("register-callpoint-already-exists").debug3Func(): logFunc(
                    "callcontext already exists - updating it. callpointName=%s, configNode=%s, dpRelativePath=%s, dpNode=%s, callpointCtx=%s", 
                    callpointName, configNode.getKeyPath(), dpRelativePath, dpNode.getKeyPath(), callpointCtx)

            callpointCtx.addMapping(dpRelativePath, dpNode)

            if callpointCtx.getDaemonCtx():
                for logFunc in self._log("register-callpoint-ctx-callpoint-already-registered").debug3Func(): logFunc(
                    "callpoint already registered. callpointName=%s, configNode=%s, dpRelativePath=%s, dpNode=%s, callpointCtx=%s", 
                    callpointName, configNode.getKeyPath(), dpRelativePath, dpNode.getKeyPath(), callpointCtx)
            else:
                for logFunc in self._log("register-callpoint-got-callpoint-ctx").debug3Func(): logFunc(
                    "got callpoint ctx. callpointName=%s, configNode=%s, dpRelativePath=%s, dpNode=%s, callpointCtx=%s", 
                    callpointName, configNode.getKeyPath(), dpRelativePath, dpNode.getKeyPath(), callpointCtx)

                res = self.registerCallpointToConfd(configKeyPath, callpointName, callpointCtx, dpCbRegistrationFunc)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log("register-callpoint-register-to-confd-failed").errorFunc(): logFunc(
                        "registerCallpointToConfd(%s) failed. callpointName=%s, configKeyPath=%s, dpRelativePath=%s, dpNode=%s, callpointCtx=%s, error: %s", 
                        callpointName, configKeyPath, dpRelativePath, dpNode.getKeyPath(), callpointCtx, Utils.getConfdErrStr())
                    return ReturnCodes.kGeneralError

        finally:
            self.myDpRegistrationsMutex.release()

        return ReturnCodes.kOk

    def registerTransformationCallpoint (self, callpointName, configNode, relativePath, node):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("register-transformation-callpoint").debug3Func(): logFunc("called. callpointName=%s, configNode=%s, relativePath=%s, node=%s",
                                                              callpointName, configNode.getKeyPath(), relativePath, node.getKeyPath())
        return self.registerCallpoint(callpointName, configNode, relativePath, node, self.registerTransformationCbWrapper(node))

    def registerOperCallpoint (self, callpointName, configNode, operRelativePath, operNode):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("register-oper-callpoint").debug3Func(): logFunc("called. callpointName=%s, configNode=%s, operRelativePath=%s, operNode=%s",
                                                    callpointName, configNode.getKeyPath(), operRelativePath, operNode.getKeyPath())
        return self.registerCallpoint(callpointName, configNode, operRelativePath, operNode, self.registerOperCb)

    def registerActionPoint (self, actionPointName, configNode):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("register-action-point").debug3Func(): logFunc(
            "called. actionPointName=%s, configNode=%s", 
            actionPointName, configNode.getKeyPath())
        emptyKeyPath = KeyPath()
        return self.registerCallpoint(actionPointName, configNode, emptyKeyPath, configNode, self.registerActionCb)

    def registerValidationPoint (self, validationPointName, configNode):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("register-validation-point").debug3Func(): logFunc("called. validationPointName=%s, configNode=%s",
                                                      validationPointName, configNode.getKeyPath())
        emptyKeyPath = KeyPath()
        return self.registerCallpoint(validationPointName, configNode, emptyKeyPath, configNode, self.registerValidationCb)

    def dpInitAction (self, userInfo, actionPointName, callpointCtx):
        for logFunc in self._log("dp-init-action").debug3Func(): logFunc("called: userInfo=%s, actionPointName=%s, callpointCtx=%s",
                                           userInfo, actionPointName, callpointCtx)

        dpTrxContext = DpTrxContext(self._log)
        timeoutGuard = TimeoutGuard(self._log, '%s-dp-init-action-%s' % (self.myName, actionPointName), 1000)
        pyconfdlib.confd_action_set_fd(userInfo, callpointCtx.getWorkerSock().fileno())
        userInfo.setOpaque(dpTrxContext)
        timeoutGuard.checkAndLog("dp-init-action")

        return pyconfdlib.CONFD_OK

    def dpInitTrans (self, transCtx, callpointCtx):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("dp-init-trans").debug3Func(): logFunc("called. transCtx=%s, callpointCtx=%s", transCtx, callpointCtx)

        dpTrxContext = DpTrxContext(self._log)
        timeoutGuard = TimeoutGuard(self._log, '%s-dp-init-transaction-%s' % (self.myName, callpointCtx), 1000)
        pyconfdlib.confd_trans_set_fd(transCtx, callpointCtx.getWorkerSock().fileno())
        transCtx.setTransOpaque(dpTrxContext)
        timeoutGuard.checkAndLog("dp-init-transaction")

        return pyconfdlib.CONFD_OK

    def dpInitTransfomrationTransWrapper (self, node):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("dp-init-transformation-trans-wrapper").debug3Func(): logFunc("called. node=%s", node)

        def dpInitTransfomrationTrans (transCtx, callpointCtx):
            self.myInitGuard.isInitOrCrash()
            for logFunc in self._log("dp-init-transformation-trans").debug3Func(): logFunc("called. transCtx=%s, callpointCtx=%s, node=%s", transCtx, callpointCtx, node)
    
            dpTrxContext = DpTrxContext(self._log)
            timeoutGuard = TimeoutGuard(self._log, '%s-dp-init-transfotmaion-transaction-%s' % (self.myName, callpointCtx), 1000)
            pyconfdlib.confd_trans_set_fd(transCtx, callpointCtx.getWorkerSock().fileno())
            transCtx.setTransOpaque(dpTrxContext)
            res = node.initTransformationTrx(transCtx)
            if res != ReturnCodes.kOk:
                for logFunc in self._log("dp-init-transformation-trans-node-failed").errorFunc(): logFunc("node.initTransformationTrx() failed. transCtx=%s, callpointCtx=%s, node=%s", transCtx, callpointCtx, node)
                return pyconfdlib.CONFD_ERR
            timeoutGuard.checkAndLog("dp-init-transfotmaion-transaction")
    
            return pyconfdlib.CONFD_OK

        return dpInitTransfomrationTrans

    def dpTransfomrationTransFinishWrapper (self, node):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("dp-transformation-trans-finish-wrapper").debug3Func(): logFunc("called. node=%s", node)

        def dpTransfomrationTransFinish (transCtx, callpointCtx):
            self.myInitGuard.isInitOrCrash()
            for logFunc in self._log("dp-transformation-trans-finish").debug3Func(): logFunc("called. transCtx=%s, callpointCtx=%s, node=%s", transCtx, callpointCtx, node)

            timeoutGuard = TimeoutGuard(self._log, '%s-dp-finish-transfotmaion-transaction-%s' % (self.myName, callpointCtx), 1000)
            res = node.finishTransformationTrx(transCtx)
            if res != ReturnCodes.kOk:
                for logFunc in self._log("dp-init-transformation-trans-node-failed").errorFunc(): logFunc("node.initTransformationTrx() failed. transCtx=%s, callpointCtx=%s, node=%s", transCtx, callpointCtx, node)
                return pyconfdlib.CONFD_ERR
            timeoutGuard.checkAndLog("dp-finish-transfotmaion-transaction")

            return pyconfdlib.CONFD_OK

        return dpTransfomrationTransFinish

    def dpTransFinish (self, transCtx, callpointCtx):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("dp-trans-finish").debug3Func(): logFunc("called. transCtx=%s, callpointCtx=%s", transCtx, callpointCtx)

        return pyconfdlib.CONFD_OK

    def dpGetResponsibleNode (self, transCtx, callpointCtx, keyPath, leaveLowestKey, responsibleNodes):
        # transCtx here can also be userInfo in case of an action
        for logFunc in self._log("dp-get-responsible-node").debug3Func(): logFunc("called.")
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("dp-get-responsible-node").debug3Func(): logFunc("called. transCtx=%s, callpointCtx=%s, keyPath=%s, leaveLowestKey=%s, resposibleNodes=%s",
                                                    transCtx, callpointCtx, keyPath, leaveLowestKey, responsibleNodes)

        res = callpointCtx.getResponsibleNode(keyPath, leaveLowestKey, responsibleNodes)
        if res != ReturnCodes.kOk or len(responsibleNodes)==0:
            for logFunc in self._log("dp-get-responsible-node-callpoint-implementation-failed").errorFunc(): logFunc(
                "callpointCtx.getResponsibleNode() failed. transCtx=%s, callpointCtx=%s, keyPath=%s, leaveLowestKey%s", 
                transCtx, callpointCtx,keyPath, leaveLowestKey)
            return ReturnCodes.kGeneralError

        for logFunc in self._log("dp-get-responsible-oper-node-succeeded").debug3Func(): logFunc(
            "callpointCtx.getResponsibleNode() succeeded. transCtx=%s, callpointCtx=%s, keyPath=%s, leaveLowestKey%s, responsibleNodes=%s", 
            transCtx, callpointCtx,keyPath, leaveLowestKey, ["%s" % node for node in responsibleNodes])
        return ReturnCodes.kOk

    def registerSnmp (self, notifyName=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("register-snmp").debug3Func(): logFunc("called. notifyName=%s", notifyName)

        if not notifyName:
            notifyName = self.defaultNotifyName

        if notifyName in self.snmpRegistrations.keys():
            # already registered to this notification, no need to do anything
            for logFunc in self._log("register-snmp-already-registered").errorFunc(): logFunc("already registered to notifyName=%s", notifyName)
            return ReturnCodes.kOk

        timeoutGuard = TimeoutGuard(self._log, '%s-register-snmp-%s' % (self.myName, notifyName), 5000)
        # create the daemon
        daemonName = "snmp-daemon-%s-%s" % (self.myName, notifyName)
        snmpDaemonCtx = pyconfdlib.confd_init_daemon(daemonName)
        if not snmpDaemonCtx:
            for logFunc in self._log("register-snmp-confd-init-daemon-failed").errorFunc(): logFunc(
                "confd_init_daemon(%s) failed. error: %s", 
                daemonName, Utils.getConfdErrStr())
            timeoutGuard.checkAndLog("register-snmp - failed")
            return ReturnCodes.kGeneralError

        # create control socket
        controlSock = socket.socket()
        # connect control socket
        res = pyconfdlib.confd_connect(snmpDaemonCtx, controlSock, pyconfdlib.CONTROL_SOCKET, 
                                       pyconfdlib.AF_INET, self.myAgent.getConfdAddress(), self.myAgent.getConfdPort())
        if res != pyconfdlib.CONFD_OK:
            for logFunc in self._log("register-snmp-confd-connect-control-socket-failed").errorFunc(): logFunc(
                "confd_connect() for control socket failed. notifyName=%s, error: %s", 
                notifyName, Utils.getConfdErrStr())
            return ReturnCodes.kGeneralError
        for logFunc in self._log("register-snmp-control-sock-connected").debug3Func(): logFunc(
            "control socket connected. daemonName=%s", daemonName)

        notifyCtx = pyconfdlib.ConfdNotificationCtxPtr()
        notifyCtxPtr = pyconfdlib.ConfdNotificationCtxPtrPtr(notifyCtx)
        res = pyconfdlib.confd_register_snmp_notification(snmpDaemonCtx, controlSock, notifyName, "", notifyCtxPtr)
        if res != pyconfdlib.CONFD_OK:
            for logFunc in self._log("register-snmp-confd-register-snmp-notification-failed").errorFunc(): logFunc(
                "confd_register_snmp_notification() failed. notifyName=%s, error: %s", 
                notifyName, Utils.getConfdErrStr())
            return ReturnCodes.kGeneralError

        res = pyconfdlib.confd_register_done(snmpDaemonCtx)
        if res != pyconfdlib.CONFD_OK:
            for logFunc in self._log("register-snmp-confd-register-done-failed").errorFunc(): logFunc(
                "confd_register_done() failed. daemonName=%s, confdErr=%s", 
                daemonName, Utils.getConfdErrStr())
            timeoutGuard.checkAndLog("register-callpoint-to-confd - failed")
            return ReturnCodes.kGeneralError

        timeoutGuard.checkAndLog("register-snmp - done")
        self.snmpRegistrations[notifyName] = (snmpDaemonCtx, controlSock, notifyCtx)

        for logFunc in self._log("register-snmp-done").debug3Func(): logFunc("done. notifyName=%s", notifyName)
        return ReturnCodes.kOk

    def sendSnmpTrap (self, notifyName, notification, varNames=[], oids=[], colRows=[]):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("send-snmp-trap").debug3Func(): logFunc("called. notifyName=%s, notification=%s, varNames=%s, oids=%s, colRows=%s", notifyName, notification, varNames, oids, colRows)

        if not notifyName:
            notifyName = self.defaultNotifyName

        if notifyName not in self.snmpRegistrations.keys():
            # not registered to this notification, can't send trap
            for logFunc in self._log("send-snmp-trap-not-registered").errorFunc(): logFunc("not registered to notifyName=%s. notification=%s", notifyName, notification)
            return ReturnCodes.kGeneralError

        (snmpDaemonCtx, controlSock, notifyCtx) = self.snmpRegistrations[notifyName]

        snmpVarbinds = SnmpVarbind()
        emptyVal = Value()

        if varNames:
            for varName in varNames:
                snmpVarbinds.appendVariable(varName, emptyVal)
        if oids:
            for oid in oids:
                snmpVarbinds.appendOid(oid, emptyVal)
        if colRows:
            for (col, oid) in colRows:
                snmpVarbinds.appendColRow(col, oid, emptyVal)

        res = a.sys.confd.pyconfdlib.pyconfdlib_high.confd_notification_send_snmp(notifyCtx, notification, snmpVarbinds)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("send-snmp-trap-confd-notification-send").errorFunc(): logFunc("confd_notification_send_snmp() failed. notifyName=%s, varNames=%s, oids=%s, colRows=%s, snmpVarbinds=%s",
                                                                      notifyName, varNames, oids, colRows, snmpVarbinds)
            return ReturnCodes.kGeneralError

        for logFunc in self._log("send-snmp-trap-done").debug1Func(): logFunc("done. notifyName=%s, varNames=%s, oids=%s, colRows=%s", notifyName, varNames, oids, colRows)
        return ReturnCodes.kOk

    def reportDpError (self, transCtx, callpointCtx):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("report-dp-error").debug3Func(): logFunc("called. transCtx=%s, callpointCtx=%s", transCtx, callpointCtx)

        dpTrxContext = transCtx.getTransOpaque()
        errorStr = dpTrxContext.getErrorStr()
        if not errorStr:
            errorStr = "internal error"
        pyconfdlib.confd_trans_seterr(transCtx, errorStr)
        for logFunc in self._log("report-dp-error-done").debug3Func(): logFunc("done. transCtx=%s, callpointCtx=%s, errorStr=%s", transCtx, callpointCtx, errorStr)

    def reportDpActionError (self, userInfo, callpointCtx):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("report-dp-action-error").debug3Func(): logFunc("called. userInfo=%s, callpointCtx=%s", userInfo, callpointCtx)

        errorStr = callpointCtx.getErrorStr()
        if not errorStr:
            errorStr = "internal error"
        pyconfdlib.confd_action_seterr(userInfo, errorStr)
        for logFunc in self._log("report-dp-action-error-done").debug3Func(): logFunc("done. userInfo=%s, callpointCtx=%s, errorStr=%s", userInfo, callpointCtx, errorStr)


    def dpDoAction (self, userInfo, actionPointName, callpointCtx, actionName, keyPath, params, nParams):
        for logFunc in self._log("dp-do-action").debug3Func(): logFunc("called: userInfo=%s, actionPointName=%s, callpointCtx=%s, keyPath=%s",
                                         actionPointName, callpointCtx, keyPath)
        responsibleNodes = []
        res = self.dpGetResponsibleNode(userInfo, callpointCtx, keyPath, False, responsibleNodes)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("dp-do-action-get-responsible-node-faield").errorFunc(): logFunc(
                "getResponsibleNode() failed. userInfo=%s, actionPointName=%s, callpointCtx=%s, keyPath=%s", 
                userInfo, actionPointName, callpointCtx, keyPath)
            self.reportDpActionError(userInfo, callpointCtx)
            return pyconfdlib.CONFD_ERR
        for node in responsibleNodes:
            for logFunc in self._log("dp-do-action-oper-calling-node-do-action").debug3Func(): logFunc(
                "calling operNode.doAction(). userInfo=%s, actionPointName=%s, callpointCtx=%s, keyPath=%s, node=%s", 
                userInfo, actionPointName, callpointCtx, keyPath, node)
            res = node.doAction(userInfo, actionPointName, actionName, keyPath, params, nParams)
            if res != ReturnCodes.kOk:
                for logFunc in self._log("dp-do-action-node-do-action-faield").errorFunc(): logFunc(
                    "node.doAction() failed. userInfo=%s, actionPointName=%s, callpointCtx=%s, keyPath=%s, node=%s", 
                    userInfo, actionPointName, callpointCtx, keyPath, node)
                self.reportDpActionError(userInfo, callpointCtx)
                return pyconfdlib.CONFD_ERR

        for logFunc in self._log("dp-do-action-done").debug3Func(): logFunc("done: userInfo=%s, actionPointName=%s, callpointCtx=%s, keyPath=%s, val=%s",
                                              userInfo, actionPointName, callpointCtx, keyPath)
        a.sys.confd.pyconfdlib.pyconfdlib.confd_action_reply_values_empty(userInfo)
        return pyconfdlib.CONFD_OK

    def dpValidate (self, transCtx, validationPointName, callpointCtx, keyPath, val):
        for logFunc in self._log("dp-validate").debug3Func(): logFunc("called: validationPointName=%s, callpointCtx=%s, keyPath=%s, val=%s",
                                        validationPointName, callpointCtx, keyPath, val)

        timeoutGuard = TimeoutGuard(self._log, '%s-dp-validate-%s' % (self.myName, validationPointName), 5000)
        responsibleNodes = []
        res = self.dpGetResponsibleNode(transCtx, callpointCtx, keyPath, False, responsibleNodes)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("dp-validate-get-responsible-node-faield").errorFunc(): logFunc(
                "getResponsibleNode() failed. transCtx=%s, validationPointName=%s, callpointCtx=%s, keyPath=%s", 
                transCtx, validationPointName, callpointCtx, keyPath)
            timeoutGuard.checkAndLog("dp-validate - failed")
            self.reportDpError(transCtx, callpointCtx)
            return pyconfdlib.CONFD_ERR
        for node in responsibleNodes:
            for logFunc in self._log("dp-validate-oper-calling-node-validate-trx").debug3Func(): logFunc(
                "calling operNode.validateTrx(). transCtx=%s, validationPointName=%s, callpointCtx=%s, keyPath=%s, node=%s", 
                transCtx, validationPointName, callpointCtx, keyPath, node)
            res = node.validateTrx(transCtx, validationPointName, keyPath, val)
            if res != ReturnCodes.kOk:
                for logFunc in self._log("dp-validate-oper-node-validate-trx-faield").errorFunc(): logFunc(
                    "operNode.validateTrx() failed. transCtx=%s, validationPointName=%s, callpointCtx=%s, keyPath=%s, node=%s", 
                    transCtx, validationPointName, callpointCtx, keyPath, node)
                self.reportDpError(transCtx, callpointCtx)
                timeoutGuard.checkAndLog("dp-validate - failed")
                return pyconfdlib.CONFD_ERR

        for logFunc in self._log("dp-validate-done").debug3Func(): logFunc("done: validationPointName=%s, callpointCtx=%s, keyPath=%s, val=%s",
                                             validationPointName, callpointCtx, keyPath, val)
        timeoutGuard.checkAndLog("dp-validate")
        return pyconfdlib.CONFD_OK

    def dpGetElem (self, transCtx, callpointName, callpointCtx, keyPath):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("dp-get-elem").debug3Func(): logFunc("called. transCtx=%s, callpointName=%s, callpointCtx=%s, keyPath=%s",
                                        transCtx, callpointName, callpointCtx, keyPath)
        responsibleNodes = []
        res = self.dpGetResponsibleNode(transCtx, callpointCtx, keyPath, False, responsibleNodes)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("dp-get-elem-get-responsible-node-faield").errorFunc(): logFunc(
                "getResponsibleNode() failed. transCtx=%s, callpointName=%s, callpointCtx=%s, keyPath=%s", 
                transCtx, callpointName, callpointCtx, keyPath)
            self.reportDpError(transCtx, callpointCtx)
            return pyconfdlib.CONFD_ERR

        for node in responsibleNodes:
            for logFunc in self._log("dp-get-elem-oper-calling-node-get-element").debug3Func(): logFunc(
                "calling operNode.getElement(). transCtx=%s, callpointName=%s, callpointCtx=%s, keyPath=%s, node=%s", 
                transCtx, callpointName, callpointCtx, keyPath, node)
            res = node.getElement(transCtx, keyPath)
            if res != ReturnCodes.kOk:
                for logFunc in self._log("dp-get-elem-oper-node-get-element-faield").errorFunc(): logFunc(
                    "operNode.getElement() failed. transCtx=%s, callpointName=%s, callpointCtx=%s, keyPath=%s, node=%s", 
                    transCtx, callpointName, callpointCtx, keyPath, node)
                self.reportDpError(transCtx, callpointCtx)
                return pyconfdlib.CONFD_ERR

        return pyconfdlib.CONFD_OK

    def dpGetObj (self, transCtx, callpointName, callpointCtx, keyPath):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("dp-get-obj").debug3Func(): logFunc("called. transCtx=%s, callpointName=%s, callpointCtx=%s, keyPath=%s",
                                       transCtx, callpointName, callpointCtx, keyPath)
        responsibleNodes = []
        res = self.dpGetResponsibleNode(transCtx, callpointCtx, keyPath, False, responsibleNodes)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("dp-get-obj-get-responsible-node-faield").errorFunc(): logFunc(
                "getResponsibleNode() failed. transCtx=%s, callpointName=%s, callpointCtx=%s, keyPath=%s", 
                transCtx, callpointName, callpointCtx, keyPath)
            self.reportDpError(transCtx, callpointCtx)
            return pyconfdlib.CONFD_ERR

        for logFunc in self._log("dp-get-obj-get-responsible-node-got").debug3Func(): logFunc(
            "getResponsibleNode() succeeded. transCtx=%s, callpointName=%s, callpointCtx=%s, keyPath=%s, responsibleNodes=%s", 
            transCtx, callpointName, callpointCtx, keyPath, responsibleNodes)
        for node in responsibleNodes:
            for logFunc in self._log("dp-get-obj-get-responsible-node-node").debug3Func(): logFunc(
                "node. transCtx=%s, callpointName=%s, callpointCtx=%s, keyPath=%s, node=%s", 
                transCtx, callpointName, callpointCtx, keyPath, node)
            res = node.getObject(transCtx, keyPath)
            if res != ReturnCodes.kOk:
                for logFunc in self._log("dp-get-obj-oper-node-get-object-faield").errorFunc(): logFunc(
                    "operNode.getObject() failed. transCtx=%s, callpointName=%s, callpointCtx=%s, keyPath=%s, node=%s", 
                    transCtx, callpointName, callpointCtx, keyPath, node)
                self.reportDpError(transCtx, callpointCtx)
                return pyconfdlib.CONFD_ERR

        return pyconfdlib.CONFD_OK

    def dpGetNext (self, transCtx, callpointName, callpointCtx, keyPath, next):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("dp-get-next").debug3Func(): logFunc("called. transCtx=%s, callpointName=%s, callpointCtx=%s, keyPath=%s, next=%s",
                                       transCtx, callpointName, callpointCtx, keyPath, next)
        responsibleNodes = []
        res = self.dpGetResponsibleNode(transCtx, callpointCtx, keyPath, False, responsibleNodes)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("dp-get-obj-get-responsible-node-faield").errorFunc(): logFunc(
                "getResponsibleNode() failed. transCtx=%s, callpointName=%s, callpointCtx=%s, keyPath=%s, next=%s", 
                transCtx, callpointName, callpointCtx, keyPath, next)
            self.reportDpError(transCtx, callpointCtx)
            return pyconfdlib.CONFD_ERR

        for node in responsibleNodes:
            res = node.getNext(transCtx, keyPath, next)
            if res != ReturnCodes.kOk:
                for logFunc in self._log("dp-get-obj-oper-node-get-next-faield").errorFunc(): logFunc(
                    "operNode.getNext() failed. transCtx=%s, callpointName=%s, callpointCtx=%s, keyPath=%s, next=%s, node=%s", 
                    transCtx, callpointName, callpointCtx, keyPath, next, node)
                self.reportDpError(transCtx, callpointCtx)
                return pyconfdlib.CONFD_ERR

        return pyconfdlib.CONFD_OK

    def dpSetElem (self, transCtx, callpointName, callpointCtx, keyPath, newValue):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("dp-set-elem").debug3Func(): logFunc("called. transCtx=%s, callpointName=%s, callpointCtx=%s, keyPath=%s, newValue=%s",
                                        transCtx, callpointName, callpointCtx, keyPath, newValue)
        responsibleNodes = []
        res = self.dpGetResponsibleNode(transCtx, callpointCtx, keyPath, False, responsibleNodes)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("dp-set-elem-get-responsible-node-faield").errorFunc(): logFunc(
                "getResponsibleNode() failed. transCtx=%s, callpointName=%s, callpointCtx=%s, keyPath=%s, newValue=%s", 
                transCtx, callpointName, callpointCtx, keyPath, newValue)
            self.reportDpError(transCtx, callpointCtx)
            return pyconfdlib.CONFD_ERR

        for logFunc in self._log("dp-set-elem-get-responsible-node-got").debug3Func(): logFunc(
            "getResponsibleNode() succeeded. transCtx=%s, callpointName=%s, callpointCtx=%s, keyPath=%s, newValue=%s, responsibleNodes=%s", 
            transCtx, callpointName, callpointCtx, keyPath, newValue, responsibleNodes)
        for node in responsibleNodes:
            for logFunc in self._log("dp-set-elem-get-responsible-node-node").debug3Func(): logFunc(
                "node. transCtx=%s, callpointName=%s, callpointCtx=%s, keyPath=%s, newValue=%s, node=%s", 
                transCtx, callpointName, callpointCtx, keyPath, newValue, node)
            res = node.setElement(transCtx, keyPath, newValue)
            if res != ReturnCodes.kOk:
                for logFunc in self._log("dp-set-elem-node-set-element-faield").errorFunc(): logFunc(
                    "node.setElement() failed. transCtx=%s, callpointName=%s, callpointCtx=%s, keyPath=%s, newValue=%s, node=%s", 
                    transCtx, callpointName, callpointCtx, keyPath, newValue, node)
                self.reportDpError(transCtx, callpointCtx)
                return pyconfdlib.CONFD_ERR

        return pyconfdlib.CONFD_OK

    def dpCreate (self, transCtx, callpointName, callpointCtx, keyPath):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("dp-create").debug3Func(): logFunc("called. transCtx=%s, callpointName=%s, callpointCtx=%s, keyPath=%s",
                                      transCtx, callpointName, callpointCtx, keyPath)
        responsibleNodes = []
        res = self.dpGetResponsibleNode(transCtx, callpointCtx, keyPath, False, responsibleNodes)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("dp-create-get-responsible-node-faield").errorFunc(): logFunc(
                "getResponsibleNode() failed. transCtx=%s, callpointName=%s, callpointCtx=%s, keyPath=%s", 
                transCtx, callpointName, callpointCtx, keyPath)
            self.reportDpError(transCtx, callpointCtx)
            return pyconfdlib.CONFD_ERR

        for logFunc in self._log("dp-create-get-responsible-node-got").debug3Func(): logFunc(
            "getResponsibleNode() succeeded. transCtx=%s, callpointName=%s, callpointCtx=%s, keyPath=%s, responsibleNodes=%s", 
            transCtx, callpointName, callpointCtx, keyPath, responsibleNodes)
        for node in responsibleNodes:
            for logFunc in self._log("dp-create-get-responsible-node-node").debug3Func(): logFunc(
                "node. transCtx=%s, callpointName=%s, callpointCtx=%s, keyPath=%s, node=%s", 
                transCtx, callpointName, callpointCtx, keyPath, node)

            res = node.create(transCtx, keyPath)
            if res != ReturnCodes.kOk:
                for logFunc in self._log("dp-create-node-create-faield").errorFunc(): logFunc(
                    "node.create() failed. transCtx=%s, callpointName=%s, callpointCtx=%s, keyPath=%s, node=%s", 
                    transCtx, callpointName, callpointCtx, keyPath, node)
                self.reportDpError(transCtx, callpointCtx)
                return pyconfdlib.CONFD_ERR

        return pyconfdlib.CONFD_OK

    def dpRemove (self, transCtx, callpointName, callpointCtx, keyPath):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("dp-remove").debug3Func(): logFunc("called. transCtx=%s, callpointName=%s, callpointCtx=%s, keyPath=%s",
                                      transCtx, callpointName, callpointCtx, keyPath)
        responsibleNodes = []
        res = self.dpGetResponsibleNode(transCtx, callpointCtx, keyPath, False, responsibleNodes)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("dp-remove-get-responsible-node-faield").errorFunc(): logFunc(
                "getResponsibleNode() failed. transCtx=%s, callpointName=%s, callpointCtx=%s, keyPath=%s", 
                transCtx, callpointName, callpointCtx, keyPath)
            self.reportDpError(transCtx, callpointCtx)
            return pyconfdlib.CONFD_ERR

        for logFunc in self._log("dp-remove-get-responsible-node-got").debug3Func(): logFunc(
            "getResponsibleNode() succeeded. transCtx=%s, callpointName=%s, callpointCtx=%s, keyPath=%s, responsibleNodes=%s", 
            transCtx, callpointName, callpointCtx, keyPath, responsibleNodes)
        for node in responsibleNodes:
            for logFunc in self._log("dp-remove-get-responsible-node-node").debug3Func(): logFunc(
                "node. transCtx=%s, callpointName=%s, callpointCtx=%s, keyPath=%s, node=%s", 
                transCtx, callpointName, callpointCtx, keyPath, node)
            res = node.remove(transCtx, keyPath)
            if res != ReturnCodes.kOk:
                for logFunc in self._log("dp-remove-node-remove-faield").errorFunc(): logFunc(
                    "node.remove() failed. transCtx=%s, callpointName=%s, callpointCtx=%s, keyPath=%s, node=%s", 
                    transCtx, callpointName, callpointCtx, keyPath, node)
                self.reportDpError(transCtx, callpointCtx)
                return pyconfdlib.CONFD_ERR

        return pyconfdlib.CONFD_OK

    def sendTagValues (self, dpTrxCtx, tagValues):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("send-tag-values").debug3Func(): logFunc("called. dpTrxCtx=%s, numOfValues=%d", dpTrxCtx, tagValues.getLen())

        timeoutGuard = TimeoutGuard(self._log, '%s-send-%d-tag-values' % (self.myName, tagValues.getLen()), 5000)
        res = a.sys.confd.pyconfdlib.pyconfdlib_high.confd_data_reply_tag_value_array(dpTrxCtx, tagValues)
        if res != pyconfdlib.CONFD_OK:
            for logFunc in self._log("send-tag-values-reply-failed").errorFunc(): logFunc(
                "confd_data_reply_tag_value_array() failed. dpTrxCtx=%s, numOfValues=%s, res=%s, confd-error=%s", 
                dpTrxCtx, tagValues.getLen(), res, Utils.getConfdErrStr)
            timeoutGuard.checkAndLog("send-tag-values - failed")
            return ReturnCodes.kGeneralError

        timeoutGuard.checkAndLog("send-tag-values")
        return ReturnCodes.kOk

    def sendValue (self, dpTrxCtx, value):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("send-value").debug3Func(): logFunc("called. dpTrxCtx=%s, value=%s", dpTrxCtx, value)

        timeoutGuard = TimeoutGuard(self._log, '%s-send-value' % (self.myName), 2000)
        if value.isEmpty():
            for logFunc in self._log("send-value-empty-value").debug3Func(): logFunc("value is not set - sending not-found reply. dpTrxCtx=%s, value=%s",
                                                       dpTrxCtx, value)
            res = pyconfdlib.confd_data_reply_not_found(dpTrxCtx)
            if res != pyconfdlib.CONFD_OK:
                for logFunc in self._log("send-value-reply-not-found-failed").errorFunc(): logFunc(
                    "confd_data_reply_not_found() failed. dpTrxCtx=%s, value=%s, confd-err=%s", 
                    dpTrxCtx, value, Utils.getConfdErrStr())
                timeoutGuard.checkAndLog("send-value - failed")
                return ReturnCodes.kGeneralError
        else:
            res = a.sys.confd.pyconfdlib.pyconfdlib_high.confd_data_reply_value(dpTrxCtx, value)
            if res != pyconfdlib.CONFD_OK:
                for logFunc in self._log("send-value-reply-failed").errorFunc(): logFunc(
                    "confd_data_reply_value() failed. dpTrxCtx=%s, value=%s, confd-err=%s", 
                    dpTrxCtx, value, Utils.getConfdErrStr())
                timeoutGuard.checkAndLog("send-value - failed")
                return ReturnCodes.kGeneralError

        timeoutGuard.checkAndLog("send-value")
        return ReturnCodes.kOk

    def sendNextKeyValue (self, dpTrxCtx, value, next):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log("send-next-key-value").debug3Func(): logFunc("called. dpTrxCtx=%s, value=%s, next=%s", dpTrxCtx, value, next)

        timeoutGuard = TimeoutGuard(self._log, '%s-send-next-key-value' % (self.myName), 2000)
        if value.isEmpty():
            for logFunc in self._log("send-next-key-value-empty-value").debug3Func(): logFunc(
                "value is not set - sending not-found reply. dpTrxCtx=%s, value=%s", 
                                                       dpTrxCtx, value)
            res = a.sys.confd.pyconfdlib.pyconfdlib_high.confd_data_reply_next_key(dpTrxCtx, None, None)
            if res != pyconfdlib.CONFD_OK:
                for logFunc in self._log("send-next-key-value-reply-next-key-none-failed").errorFunc(): logFunc(
                    "confd_data_reply_next_key(dpTrxCtx, None, None) failed. dpTrxCtx=%s, confd-err=%s", 
                    dpTrxCtx, Utils.getConfdErrStr())
                timeoutGuard.checkAndLog("send-next-key-value - failed")
                return ReturnCodes.kGeneralError
        else:
            res = a.sys.confd.pyconfdlib.pyconfdlib_high.confd_data_reply_next_key(dpTrxCtx, value, next)
            if res != pyconfdlib.CONFD_OK:
                for logFunc in self._log("send-next-key-value-reply-failed").errorFunc(): logFunc(
                    "confd_data_reply_next_key() failed. dpTrxCtx=%s, value=%s, next=%s, confd-err=%s", 
                    dpTrxCtx, value, next, Utils.getConfdErrStr())
                timeoutGuard.checkAndLog("send-next-key-value - failed")
                return ReturnCodes.kGeneralError

        timeoutGuard.checkAndLog("send-next-key-value")
        return ReturnCodes.kOk

