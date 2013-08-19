# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas


from domain_base import DomainBase

from a.sys.confd.pyconfdlib import pyconfdlib
import a.sys.confd.pyconfdlib.pyconfdlib_high
from a.sys.confd.pyconfdlib.key_path import KeyPath
from a.sys.confd.pyconfdlib.value import Value
from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket
from utils import Utils,Retry

class MaapiDomain (DomainBase):

    REF_COUNT_KEY_NAME = 'ref-count'
    ATTACHED_KEY_NAME = 'attached'

    def __init__ (self, logger):
        super(MaapiDomain, self).__init__(logger)
        self._maapiUserSocket=None # socket for user transaction operations (hooks, transformations, etc)
        self._maapiSystemSocket=None # socket for system operations (read, etc)

        self._userTrx = {}

    def specificInit(self):
        for logFunc in self._log("specific-init").debug2Func(): logFunc("called.")
        res = self.buildMaapiConnection()
        if res != ReturnCodes.kOk:
            for logFunc in self._log('specific-init-build-maapi-connection-failed').errorFunc(): logFunc('buildMaapiConnection() failed. res=%s', res)
            return ReturnCodes.kGeneralError
        return ReturnCodes.kOk

    def specificShutdown (self):
        for logFunc in self._log("specific-shutdown").debug2Func(): logFunc("called.")
        res = self.endMaapiSystemSession()
        if res != ReturnCodes.kOk:
            for logFunc in self._log("specific-shutdown-end-maapi-session-failed").errorFunc(): logFunc("endMaapiSystemSession() failed")
            # do not stop the shutdown process
        self._maapiUserSocket.close()
        self._maapiUserSocket = None
        self._maapiSystemSocket.close()
        self._maapiSystemSocket = None

    def buildMaapiConnection (self):
        for logFunc in self._log("build-maapi-connection").debug2Func(): logFunc("called.")

        self._maapiUserSocket=socket.socket()
        self._maapiSystemSocket=socket.socket()

        for logFunc in self._log("build-maapi-connection-sockets").debug2Func(): logFunc("sockets: user-socket=%s, system-socket=%s", self._maapiUserSocket.fileno(), self._maapiSystemSocket.fileno())

        socketList = [self._maapiUserSocket, self._maapiSystemSocket]

        for sock in socketList:
            res = pyconfdlib.maapi_connect(sock, pyconfdlib.AF_INET, self.myAgent.getConfdAddress(), self.myAgent.getConfdPort())
            if res != pyconfdlib.CONFD_OK:
                for logFunc in self._log("build-maapi-connection-maapi-connect-failed").errorFunc(): logFunc('maapi_connect() failed. error=%s', Utils.getConfdErrStr())
                return ReturnCodes.kGeneralError
            res = pyconfdlib.maapi_load_schemas(sock)
            if res != pyconfdlib.CONFD_OK:
                for logFunc in self._log("build-maapi-connection-load-schemas-failed").errorFunc(): logFunc("maapi_load_schemas() failed. error=%s", Utils.getConfdErrStr())
                return ReturnCodes.kGeneralError

        res = self.startMaapiSystemSession()
        if res != ReturnCodes.kOk:
            for logFunc in self._log("build-maapi-connection-start-system-session-failed").errorFunc(): logFunc("startMaapiSystemSession() failed.")
            return ReturnCodes.kGeneralError

        for logFunc in self._log("build-maapi-connection").debug2Func(): logFunc("done.")
        return ReturnCodes.kOk

    def attachMaapi (self, trxContext):
        for logFunc in self._log("attach-maapi").debug3Func(): logFunc("called. trxContext=%s, self._userTrx=%s", trxContext, self._userTrx)

        transactionHandle = trxContext.getTransHandle()
        if transactionHandle in self._userTrx.keys():
            self._userTrx[transactionHandle][self.REF_COUNT_KEY_NAME] += 1
            if self._userTrx[transactionHandle][self.ATTACHED_KEY_NAME]:
                for logFunc in self._log("attach-maapi-already-attached").debug3Func(): logFunc(
                    "trx already atthaced. not calling maapi_attach. trxContext=%s, user-transactions=%s", 
                    trxContext, self._userTrx[transactionHandle])
                return ReturnCodes.kOk
        else:
            self._userTrx[transactionHandle] = {
                self.REF_COUNT_KEY_NAME : 1,
                self.ATTACHED_KEY_NAME : False
                }

        res = pyconfdlib.maapi_attach(self._maapiUserSocket, 0, trxContext)
        if res != pyconfdlib.CONFD_OK:
            for logFunc in self._log("attach-maapi-lib-failed").errorFunc(): logFunc("maapi_attach() failed. trxContext=%s, error=%s", trxContext, Utils.getConfdErrStr())
            return ReturnCodes.kGeneralError

        self._userTrx[transactionHandle][self.ATTACHED_KEY_NAME] = True

        for logFunc in self._log("attach-maapi-done").debug3Func(): logFunc("done. trxContext=%s, self._userTrx=%s", trxContext, self._userTrx)
        return ReturnCodes.kOk

    def detachMaapi (self, trxContext):
        for logFunc in self._log("detach-maapi").debug3Func(): logFunc("called. trxContext=%s, self._userTrx=%s", trxContext, self._userTrx)

        allowFailure = False

        transactionHandle = trxContext.getTransHandle()
        if transactionHandle not in self._userTrx.keys():
            # trying to detach a transaction that is not the currently attached one.
            for logFunc in self._log("detach-maapi-detaching-unknown-trx").debug1Func(): logFunc(
                "Trying to detach an unknown trx. trxContext=%s, userTrx=%s", trxContext, self._userTrx)
            return ReturnCodes.kOk

        if self._userTrx[transactionHandle][self.ATTACHED_KEY_NAME]:
            res = pyconfdlib.maapi_detach(self._maapiUserSocket, trxContext)
            if res != pyconfdlib.CONFD_OK:
                for logFunc in self._log("detach-maapi-lib-failed").errorFunc(): logFunc("maapi_detach() failed. trxContext=%s, error=%s", trxContext, Utils.getConfdErrStr())
                return ReturnCodes.kGeneralError
            self._userTrx[transactionHandle][self.ATTACHED_KEY_NAME] = False

        self._userTrx[transactionHandle][self.REF_COUNT_KEY_NAME] -= 1
        if self._userTrx[transactionHandle][self.REF_COUNT_KEY_NAME] == 0:
            del self._userTrx[transactionHandle]

        for logFunc in self._log("detach-maapi-done").debug3Func(): logFunc("done. trxContext=%s, self._userTrx=%s", trxContext, self._userTrx)

        return ReturnCodes.kOk

    def startMaapiSystemSession (self):
        for logFunc in self._log("start-maapi-system-session").debug2Func(): logFunc("called.")
        res = pyconfdlib.maapi_start_user_session(self._maapiSystemSocket, None, "system", [], pyconfdlib.AF_INET, self.myAgent.getConfdAddress(), 
                                                  pyconfdlib.CONFD_PROTO_TCP)
        if res != pyconfdlib.CONFD_OK:
            for logFunc in self._log("start-maapi-system-session-start-user-session-failed").errorFunc(): logFunc("maapi_start_user_session() failed. error=%s", Utils.getConfdErrStr())
            return ReturnCodes.kGeneralError

        for logFunc in self._log("start-maapi-system-session").debug2Func(): logFunc("done.")
        return ReturnCodes.kOk

    def endMaapiSystemSession (self):
        for logFunc in self._log("end-maapi-system-session").debug2Func(): logFunc("called.")
        res = pyconfdlib.maapi_end_user_session(self._maapiSystemSocket)
        if res != pyconfdlib.CONFD_OK:
            for logFunc in self._log("end-maapi-system-session-end-user-session-failed").errorFunc(): logFunc("maapi_end_user_session() failed. error=%s", Utils.getConfdErrStr())
            return ReturnCodes.kGeneralError

        for logFunc in self._log("end-maapi-system-session").debug2Func(): logFunc("done.")
        return ReturnCodes.kOk

    def startMaapiReadTransaction (self, socket):
        for logFunc in self._log("start-maapi-read-transaction").debug2Func(): logFunc("called. socket=%s", socket.fileno())

        db = pyconfdlib.CONFD_RUNNING
        transactionHandle = pyconfdlib.maapi_start_trans(socket, db, pyconfdlib.CONFD_READ)
        if not transactionHandle:
            for logFunc in self._log('start-maapi-read-transaction').errorFunc(): logFunc('pyconfdlib.maapi_start_trans() failed. error=%s', Utils.getConfdErrStr())
            return None

        for logFunc in self._log("start-maapi-read-transaction").debug2Func(): logFunc("done. socket=%s", socket.fileno())
        return transactionHandle

    def startMaapiWriteTransaction (self, socket):
        for logFunc in self._log("start-maapi-write-transaction").debug2Func(): logFunc("called.")

        transactionHandle = pyconfdlib.maapi_start_trans(socket, pyconfdlib.CONFD_RUNNING, pyconfdlib.CONFD_READ_WRITE)
        if not transactionHandle:
            for logFunc in self._log('start-maapi-write-transaction').errorFunc(): logFunc('pyconfdlib.maapi_start_trans() failed. error=%s', Utils.getConfdErrStr())
            return None

        for logFunc in self._log("start-maapi-write-transaction").debug2Func(): logFunc("done.")
        return transactionHandle

    def endMaapiTransaction (self, transactionHandle, socket):
        for logFunc in self._log("end-maapi-transaction").debug2Func(): logFunc("called. transactionHandle=%s, socket=%s", transactionHandle, socket)

        res = pyconfdlib.maapi_finish_trans(socket, transactionHandle)
        if res != pyconfdlib.CONFD_OK:
            for logFunc in self._log("end-maapi-finish-transaction-failed").debug1Func(): logFunc('maapi_finish_trans() failed')
            return ReturnCodes.kGeneralError

        for logFunc in self._log("end-maapi-transaction").debug2Func(): logFunc("done.")
        return ReturnCodes.kOk

    def getTrxHandle (self, trxContext):
        for logFunc in self._log("get-trx-handle").debug3Func(): logFunc("called. trxContext=%s", trxContext)
        transactionHandle = trxContext.getTransHandle()
        if transactionHandle not in self._userTrx.keys() or not self._userTrx[transactionHandle][self.ATTACHED_KEY_NAME]:
            res = self.attachMaapi(trxContext)
            if res != ReturnCodes.kOk:
                for logFunc in self._log("get-trx-handle-attach-maapi-failed").errorFunc(): logFunc(
                    "attachMaapi() failed, trxContext=%s",trxContext)
                return None

        for logFunc in self._log("get-trx-handle-done").debug3Func(): logFunc("done. trxContext=%s, transactionHandle=%s", trxContext, transactionHandle)
        return transactionHandle

    def readMaapi (self, tagValueList, keyPath, trxContext):
        for logFunc in self._log("read-maapi").debug3Func(): logFunc("called. keyPath=%s, tagValueList=%s, trxContext=%s", keyPath, tagValueList, trxContext)
        if trxContext:
            return self._readMaapiInUserTrx(tagValueList, keyPath, trxContext)
        else:
            return self._readMaapiInSystemTrx(tagValueList, keyPath)

    def _readMaapiInSystemTrx (self, tagValueList, keyPath):
        for logFunc in self._log("read-maapi-in-system-trx").debug3Func(): logFunc("called. keyPath=%s, tagValueList=%s", keyPath, tagValueList)

        transactionHandle = self.startMaapiReadTransaction(self._maapiSystemSocket)
        if not transactionHandle:
            for logFunc in self._log("read-maapi-in-system-trx-start-transaction-failed").errorFunc(): logFunc("startMaapiReadTransaction() failed")
            return ReturnCodes.kGeneralError
            
        res = self._doReadMaapi(tagValueList, keyPath, transactionHandle, self._maapiSystemSocket)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("read-maapi-in-system-trx-do-read-maapi-failed").errorFunc(): logFunc(
                "_doReadMaapi() failed. tagValueList=%s, keyPath=%s, transactionHandle=%s, socket=%s",
                tagValueList, keyPath, transactionHandle, self._maapiSystemSocket.fileno())
            res = self.endMaapiTransaction(transactionHandle, self._maapiSystemSocket)
            if res != ReturnCodes.kOk:
                for logFunc in self._log("read-maapi-in-system-trx-do-failed-end-transaction-failed").errorFunc(): logFunc(
                    "endMaapiTransaction() failed. tagValueList=%s, keyPath=%s, transactionHandle=%s, socket=%s",
                    tagValueList, keyPath, transactionHandle, self._maapiSystemSocket.fileno())
            return ReturnCodes.kGeneralError

        res = self.endMaapiTransaction(transactionHandle, self._maapiSystemSocket)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("read-maapi-in-system-trx-end-transaction-failed").errorFunc(): logFunc(
                "endMaapiTransaction() failed. tagValueList=%s, keyPath=%s, transactionHandle=%s, socket=%s",
                tagValueList, keyPath, transactionHandle, self._maapiSystemSocket.fileno())
            return ReturnCodes.kGeneralError

        for logFunc in self._log("read-maapi-in-system-trx-done").debug3Func(): logFunc("done. keyPath=%s, tagValueList=%s", keyPath, tagValueList)
        return ReturnCodes.kOk


    def _readMaapiInUserTrx (self, tagValueList, keyPath, trxContext):
        for logFunc in self._log("read-maapi-in-user-trx").debug3Func(): logFunc("called. keyPath=%s, tagValueList=%s, trxContext=%s", keyPath, tagValueList, trxContext)

        transactionHandle = self.getTrxHandle(trxContext)
        if not transactionHandle:
            for logFunc in self._log("read-maapi-in-user-trx-get-trx-handle-failed").errorFunc(): logFunc(
                "getTrxHandle() failed. trxContext=%s",trxContext)
            return ReturnCodes.kGeneralError

        res = self._doReadMaapi(tagValueList, keyPath, transactionHandle, self._maapiUserSocket)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("read-maapi-in-user-trx-do-read-maapi-failed").errorFunc(): logFunc(
                "_doReadMaapi() failed. tagValueList=%s, keyPath=%s, transactionHandle=%s, socket=%s",
                tagValueList, keyPath, transactionHandle, self._maapiUserSocket.fileno())
            return ReturnCodes.kGeneralError

        for logFunc in self._log("read-maapi-in-user-trx-done").debug3Func(): logFunc("done. keyPath=%s, tagValueList=%s, trxContext=%s", keyPath, tagValueList, trxContext)
        return ReturnCodes.kOk

    def _doReadMaapi (self, tagValueList, keyPath, transactionHandle, socket):
        for logFunc in self._log("do-read-maapi").debug3Func(): logFunc("called. keyPath=%s, tagValueList=%s, transactionHandler=%s, socket=%s",
                                          keyPath, tagValueList, transactionHandle, socket.fileno())

        if keyPath.getLen() == 0 and tagValueList.getLen() != 0:
            (xmlTag, val) = tagValueList.getAt(0)
            (tag, ns) = xmlTag
            res = pyconfdlib.maapi_set_namespace(socket, transactionHandle, ns)
            if res != pyconfdlib.CONFD_OK:
                for logFunc in self._log("do-read-maapi-set-namespace-failed").errorFunc(): logFunc("maapi_set_namespace() failed. ns=%s, error=%s", ns, Utils.getConfdErrStr())
                return ReturnCodes.kGeneralError

        res = a.sys.confd.pyconfdlib.pyconfdlib_high.maapi_get_values(socket, transactionHandle, tagValueList, keyPath)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("do-read-maapi-get-values-failed").errorFunc(): logFunc("maapi_get_values() failed. error=%s", Utils.getConfdErrStr())
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def writeMaapi (self, tagValueList, keyPath, trxContext, itemsToDelete=[]):
        for logFunc in self._log("write-maapi").debug3Func(): logFunc("called. keyPath=%s, tagValueList=%s, trxContext=%s, itemsToDelete=%s", keyPath, tagValueList, trxContext, ['%s' % x for x in itemsToDelete])
        if trxContext:
            return self._writeMaapiInUserTrx(tagValueList, keyPath, trxContext, itemsToDelete)
        else:
            return self._writeMaapiInSystemTrx(tagValueList, keyPath, itemsToDelete)

    def _writeMaapiInSystemTrx (self, tagValueList, keyPath, itemsToDelete):
        for logFunc in self._log("write-maapi-in-system-trx").debug3Func(): logFunc("called. keyPath=%s, tagValueList=%s, itemsToDelete=%s",
                                                      keyPath, tagValueList, ['%s' % x for x in itemsToDelete])

        transactionHandle = self.startMaapiWriteTransaction(self._maapiSystemSocket)
        if not transactionHandle:
            for logFunc in self._log("write-maapi-in-system-trx-start-transaction-failed").errorFunc(): logFunc("startMaapiWriteTransaction() failed")
            return ReturnCodes.kGeneralError

        res = self._doWriteMaapi(tagValueList, keyPath, transactionHandle, self._maapiSystemSocket, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("write-maapi-in-system-trx-do-write-maapi-failed").errorFunc(): logFunc(
                "_doWriteMaapi() failed. tagValueList=%s, keyPath=%s, transactionHandle=%s, socket=%s",
                tagValueList, keyPath, transactionHandle, self._maapiSystemSocket.fileno())
            res = self.endMaapiTransaction(transactionHandle, self._maapiSystemSocket)
            if res != ReturnCodes.kOk:
                for logFunc in self._log("write-maapi-in-system-trx-do-failed-end-transaction-failed").errorFunc(): logFunc(
                    "endMaapiTransaction() failed. tagValueList=%s, keyPath=%s, transactionHandle=%s, socket=%s",
                    tagValueList, keyPath, transactionHandle, self._maapiSystemSocket.fileno())
            return ReturnCodes.kGeneralError

        res = a.sys.confd.pyconfdlib.pyconfdlib.maapi_apply_trans(self._maapiSystemSocket, transactionHandle, False)
        if res != pyconfdlib.CONFD_OK:
            for logFunc in self._log("write-maapi-in-system-trx-prepare-transaction-failed").errorFunc(): logFunc("maapi_apply_trans() failed")
            res = self.endMaapiTransaction(transactionHandle, self._maapiSystemSocket)
            if res != ReturnCodes.kOk:
                for logFunc in self._log("write-maapi-in-system-trx-prepare-transaction-failed-end-transaction-failed").errorFunc(): logFunc("endMaapiTransaction() failed")
            return ReturnCodes.kGeneralError

        res = self.endMaapiTransaction(transactionHandle, self._maapiSystemSocket)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("write-maapi-in-system-trx-end-transaction-failed").errorFunc(): logFunc("endMaapiTransaction() failed")
            return ReturnCodes.kGeneralError

        for logFunc in self._log("write-maapi-in-system-trx-done").debug3Func(): logFunc(
            "done. keyPath=%s, tagValueList=%s, itemsToDelete=%s", 
            keyPath, tagValueList, ['%s' % x for x in itemsToDelete])
        return ReturnCodes.kOk

    def _writeMaapiInUserTrx (self, tagValueList, keyPath, trxContext, itemsToDelete):
        for logFunc in self._log("write-maapi-in-user-trx").debug3Func(): logFunc(
            "called. keyPath=%s, tagValueList=%s, itemsToDelete=%s, trxContext=%s", 
            keyPath, tagValueList, ['%s' % x for x in itemsToDelete], trxContext)

        transactionHandle = self.getTrxHandle(trxContext)
        if not transactionHandle:
            for logFunc in self._log("write-maapi-in-user-trx-get-trx-handle-failed").errorFunc(): logFunc(
                "getTrxHandle() failed. trxContext=%s", trxContext)
            return ReturnCodes.kGeneralError

        res = self._doWriteMaapi(tagValueList, keyPath, transactionHandle, self._maapiUserSocket, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("write-maapi-in-user-trx-do-write-maapi-failed").errorFunc(): logFunc(
                "_doWriteMaapi() failed. tagValueList=%s, keyPath=%s, transactionHandle=%s, socket=%s",
                tagValueList, keyPath, transactionHandle, self._maapiUserSocket.fileno())
            return ReturnCodes.kGeneralError

        for logFunc in self._log("write-maapi-in-user-trx-done").debug3Func(): logFunc("done. keyPath=%s, tagValueList=%s, itemsToDelete=%s",
                                                             keyPath, tagValueList, ['%s' % x for x in itemsToDelete])
        return ReturnCodes.kOk

    def _doWriteMaapi (self, tagValueList, keyPath, transactionHandle, socket, itemsToDelete):
        for logFunc in self._log("do-write-maapi").debug3Func(): logFunc("called. keyPath=%s, tagValueList=%s, itemsToDelete=%s",
                                           keyPath, tagValueList, ['%s' % x for x in itemsToDelete])

        if keyPath and keyPath.getLen() == 0 and tagValueList and tagValueList.getLen() != 0:
            (xmlTag, val) = tagValueList.getAt(0)
            (tag, ns) = xmlTag
            res = pyconfdlib.maapi_set_namespace(socket, transactionHandle, ns)
            if res != pyconfdlib.CONFD_OK:
                for logFunc in self._log("do-write-maapi-set-namespace-failed").errorFunc(): logFunc("maapi_set_namespace() failed. ns=%s, error=%s", ns, Utils.getConfdErrStr())
                return ReturnCodes.kGeneralError

        if keyPath and tagValueList:
            res = a.sys.confd.pyconfdlib.pyconfdlib_high.maapi_set_values(socket, transactionHandle, tagValueList, keyPath)
            if res != ReturnCodes.kOk:
                for logFunc in self._log("do-write-maapi-set-values-failed").errorFunc(): logFunc("maapi_set_values() failed. error=%s", Utils.getConfdErrStr())
                return ReturnCodes.kGeneralError

        for item in itemsToDelete:
            for logFunc in self._log("do-write-maapi-going-to-delete-item").debug3Func(): logFunc("going to delete an item: %s", item)
            res = a.sys.confd.pyconfdlib.pyconfdlib.maapi_delete(socket, transactionHandle, item.getCannonicalStr())
            if res != pyconfdlib.CONFD_OK:
                for logFunc in self._log("do-write-maapi-maapi-delete-failed").errorFunc(): logFunc("maapi_delete(%s) failed. error=%s", item, Utils.getConfdErrStr())
                return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def deleteMaapiByStringKeyPath (self, itemsToDelete, trxContext):
        """
        This method is a workaround for cases where we must access multiple keys paths (like SNMP-VIEW-BASED-ACM-MIB vacmSecurityToGroup table) 
        """
        for logFunc in self._log("delete-maapi-by-string-key-path").debug3Func(): logFunc("called. itemsToDelete=%s", ['%s' % x for x in itemsToDelete])

        socket = self._maapiUserSocket
        transactionHandle = self.getTrxHandle(trxContext)
        if not transactionHandle:
            for logFunc in self._log("delete-maapi-by-string-key-path-get-trx-handle-failed").errorFunc(): logFunc(
                "getTrxHandle() failed. trxContext=%s", trxContext)
            return ReturnCodes.kGeneralError

        for item in itemsToDelete:
            for logFunc in self._log("delete-maapi-by-string-key-path-going-to-delete-item").debug3Func(): logFunc("going to delete an item: %s", item)
            res = a.sys.confd.pyconfdlib.pyconfdlib.maapi_delete(self._maapiUserSocket, transactionHandle, item)
            if res != pyconfdlib.CONFD_OK:
                for logFunc in self._log("delete-maapi-by-string-key-path-maapi-delete-failed").errorFunc(): logFunc("maapi_delete(%s) failed. error=%s", item, Utils.getConfdErrStr())
                return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def destroyMaapiCursor (self, cursor):
        for logFunc in self._log("destroy-maapi-cursor").debug3Func(): logFunc("called")

        a.sys.confd.pyconfdlib.pyconfdlib_high.maapi_destroy_cursor(cursor)

    def getNextMaapiCursor (self, cursor):
        for logFunc in self._log("get-next-maapi-cursor").debug3Func(): logFunc("called")

        res = a.sys.confd.pyconfdlib.pyconfdlib_high.maapi_get_next(cursor)
        if res != pyconfdlib.CONFD_OK:
            for logFunc in self._log("get-next-maapi-cursor-get-next-first-failed").errorFunc(): logFunc("maapi_get_next() failed. error=%s", Utils.getConfdErrStr())
            return ReturnCodes.kGeneralError
        return ReturnCodes.kOk

    def readMaapiKeys (self, keyPath, keys, trxContext):
        for logFunc in self._log("read-maapi-keys").debug3Func(): logFunc("called. keyPath=%s, keys=%s, trxContext=%s", keyPath, keys, trxContext)
        if trxContext:
            return self._readMaapiKeysInUserTrx(keyPath, keys, trxContext)
        else:
            return self._readMaapiKeysInSystemTrx(keyPath, keys)

    def _readMaapiKeysInSystemTrx (self, keyPath, keys):
        for logFunc in self._log("read-maapi-keys-in-system-trx").debug3Func(): logFunc("called. keyPath=%s", keyPath)

        transactionHandle = self.startMaapiReadTransaction(self._maapiSystemSocket)
        if not transactionHandle:
            for logFunc in self._log("read-maapi-keys-in-system-trx-start-transaction-failed").errorFunc(): logFunc("startMaapiReadTransaction() failed")
            return ReturnCodes.kGeneralError

        res = self._doReadMaapiKeys(keyPath, keys, transactionHandle, self._maapiSystemSocket)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("read-maapi-keys-in-system-trx-do-failed").errorFunc(): logFunc(
                "_doReadMaapiKeys() failed. keyPath=%s, transactionHandle=%s, socket=%s",
                keyPath, transactionHandle, self._maapiSystemSocket.fileno())
            res = self.endMaapiTransaction(transactionHandle, self._maapiSystemSocket)
            if res != ReturnCodes.kOk:
                for logFunc in self._log("read-maapi-keys-in-system-trx-maapi-keys-do-failed-end-transaction-failed").errorFunc(): logFunc(
                    "endMaapiTransaction() failed. keyPath=%s, transactionHandle=%s, socket=%s",
                    keyPath, transactionHandle, self._maapiSystemSocket.fileno())
            return ReturnCodes.kGeneralError

        res = self.endMaapiTransaction(transactionHandle, self._maapiSystemSocket)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("read-maapi-keys-in-system-trx-end-transaction-failed").errorFunc(): logFunc("endMaapiTransaction() failed")
            return ReturnCodes.kGeneralError

        for logFunc in self._log("read-maapi-keys-in-system-trx-done").debug3Func(): logFunc("done. keyPath=%s, keys", keyPath, keys)
        return ReturnCodes.kOk

    def _readMaapiKeysInUserTrx (self, keyPath, keys, trxContext):
        for logFunc in self._log("read-maapi-keys-in-user-trx").debug3Func(): logFunc("called. keyPath=%s, trxContext=%s", keyPath, trxContext)

        transactionHandle = self.getTrxHandle(trxContext)
        if not transactionHandle:
            for logFunc in self._log("read-maapi-keys-in-user-trx-get-trx-handle-failed").errorFunc(): logFunc(
                "getTrxHandle() failed. trxContext=%s", trxContext)
            return ReturnCodes.kGeneralError

        res = self._doReadMaapiKeys(keyPath, keys, transactionHandle, self._maapiUserSocket)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("read-maapi-keys-in-user-trx-do-failed").errorFunc(): logFunc("_doReadMaapiKeys() failed. keyPath=%s, transactionHandle=%s, socket=%s",
                                                                     keyPath, transactionHandle, self._maapiUserSocket.fileno())
            return ReturnCodes.kGeneralError

        for logFunc in self._log("read-maapi-keys-in-user-trx-done").debug3Func(): logFunc("done. keyPath=%s, keys=%s, trxContext=%s", keyPath, keys, trxContext)
        return ReturnCodes.kOk

    def _doReadMaapiKeys (self, keyPath, keys, transactionHandle, socket):
        for logFunc in self._log("do-read-maapi-keys").debug3Func(): logFunc("called. keyPath=%s, trxContext=%s, transactionHandle=%s, socket=%s", keyPath, transactionHandle, transactionHandle, socket)

        cursor = a.sys.confd.pyconfdlib.pyconfdlib_high.MaapiCursor()
        res = a.sys.confd.pyconfdlib.pyconfdlib_high.maapi_init_cursor(socket, transactionHandle, cursor, keyPath)
        if res != pyconfdlib.CONFD_OK:
            for logFunc in self._log("do-read-maapi-keys-init-cursor-failed").errorFunc(): logFunc("maapi_init_cursor() failed. keyPath=%s, transactionHandle=%s, error=%s",
                                                                     keyPath, transactionHandle, Utils.getConfdErrStr())
            return ReturnCodes.kGeneralError

        res = a.sys.confd.pyconfdlib.pyconfdlib_high.maapi_get_next(cursor)
        if res != pyconfdlib.CONFD_OK:
            for logFunc in self._log("do-read-maapi-keys-get-next-first-failed").errorFunc(): logFunc("maapi_get_next() (first time) failed. keyPath=%s, error=%s", keyPath, Utils.getConfdErrStr())
            a.sys.confd.pyconfdlib.pyconfdlib_high.maapi_destroy_cursor(cursor)
            return ReturnCodes.kGeneralError

        while cursor.getN() != 0:
            currentKey = cursor.getValue()
            if not currentKey:
                for logFunc in self._log("do-read-maapi-keys-empty-cursor").errorFunc(): logFunc("maapi_get_next() return an empty cursor. keyPath=%s, keys=%s", keyPath, [x for x in keys])
                a.sys.confd.pyconfdlib.pyconfdlib_high.maapi_destroy_cursor(cursor)
                return ReturnCodes.kGeneralError
            keys.append(currentKey)

            res = a.sys.confd.pyconfdlib.pyconfdlib_high.maapi_get_next(cursor)
            if res != pyconfdlib.CONFD_OK:
                for logFunc in self._log("do-read-maapi-keys-get-next-failed").errorFunc(): logFunc("maapi_get_next() failed. keyPath=%s, keys=%s, error=%s", keyPath, [x for x in keys], Utils.getConfdErrStr())
                a.sys.confd.pyconfdlib.pyconfdlib_high.maapi_destroy_cursor(cursor)
                return ReturnCodes.kGeneralError

        a.sys.confd.pyconfdlib.pyconfdlib_high.maapi_destroy_cursor(cursor)

        for logFunc in self._log("do-read-maapi-keys-done").debug3Func(): logFunc("done. keyPath=%s, keys=%s, transactionHandle=%s", keyPath, [str(x) for x in keys], transactionHandle)
        return ReturnCodes.kOk

