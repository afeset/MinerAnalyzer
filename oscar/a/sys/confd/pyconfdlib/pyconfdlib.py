# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

import ctypes
import socket
import threading
import traceback
import copy

from confd_values import ConfdValues
from confd_hkeypath import ConfdHkeypath
import a.infra.process
from a.infra.basic.return_codes import ReturnCodes
from a.infra.misc.init_guard import InitGuard

# Global constants used by this module only
#==========================================
kMaxStringSize=256

# These values match the ones defined in the .cpp file, in #define PYCONFDLIB_LOG_xxx statements
LOG_FATAL = 10
LOG_ERROR = 9
LOG_WARNING = 8 
LOG_NOTICE = 7
LOG_INFO = 6
LOG_DEBUG1 = 5
LOG_DEBUG2 = 4
LOG_DEBUG3 = 3
LOG_DEBUG4 = 2
LOG_DEBUG5 = 1

_initGuard = InitGuard()

def init (logger):
    """
    Must be called before using this module
    """
    global _initGuard
    if _initGuard.isInit():
        # skip init
        return
    _initGuard.startInit()

    global _log
    _log = logger.createLogger("sys_confd","pyconfdlib")

    _initDll(logFuncForDll)
    for logFunc in _log("init-dll-done").debug1Func(): logFunc("_initDll() done")
    #raise Exception("_initDll() done")
    _initTypes()
    for logFunc in _log("init-types-done").debug1Func(): logFunc("_initTypes() done")
    #raise Exception("_initTypes() done")
    _initGlobals()
    for logFunc in _log("init-globals-done").debug1Func(): logFunc("_initGlobals() done")
    #raise Exception("_initGlobals() done")
    _initPrototypes()
    for logFunc in _log("init-prototypes-done").debug1Func(): logFunc("_initPrototypes() done")
    #raise Exception("_initPrototypes() done")
    _initConstants()
    for logFunc in _log("init-constants-done").debug1Func(): logFunc("_initConstants() done")
    #raise Exception("_initConstants() done")
    _initEnums()
    for logFunc in _log("init-enums-done").debug1Func(): logFunc("_initEnums() done")
    #raise Exception("_initEnums() done")

    _initGuard.initDone()



class ConfdLibGuard (object):
    def __init__ (self, logMessage):
        self.logMessage = logMessage

    def __enter__ (self):
        return None

    def __exit__ (self, type, value, traceback):
        if isinstance(value, Exception):
            for logFunc in _log("lib-guard-exit").exceptionFunc():
                logFunc("confd_lib call raised an exception. %s", self.logMessage)


def exceptionGuard(ob):

    # TODO (naamas) - fix this code after getting new logger implementation from 2.6->2.7
    def wrapped(*args, **kwords):
        try:
            ret = ob(*args, **kwords)
        except:
            for logFunc in _log("exception-guard-exception-occured").errorFunc(): logFunc("confd_lib call raise an exception. %s", traceback.format_exc())
            #_log("exception-guard-exception-occured").exception("confd_lib callback raised an exception")
            return CONFD_ERR
        return ret

    return wrapped


# The log function used by the DLL
def logFuncForDll (level, msg):
    if msg.find("Failed to connect to Confd") >= 0:
        level = LOG_INFO
    if level==LOG_FATAL:
        a.infra.process.processFatal(msg)
    elif level==LOG_ERROR:
        for logFunc in _log("dll-error").errorFunc(): logFunc(msg)
    elif level==LOG_WARNING:
        for logFunc in _log("dll-warning").warningFunc(): logFunc(msg)
    elif level==LOG_NOTICE:
        for logFunc in _log("dll-notice").noticeFunc(): logFunc(msg)
    elif level==LOG_INFO:
        for logFunc in _log("dll-info").infoFunc(): logFunc(msg)
    elif level==LOG_DEBUG1:
        for logFunc in _log("dll-debug1").debug1Func(): logFunc(msg)
    elif level==LOG_DEBUG2:
        for logFunc in _log("dll-debug2").debug2Func(): logFunc(msg)
    elif level==LOG_DEBUG3:
        for logFunc in _log("dll-debug3").debug3Func(): logFunc(msg)
    elif level==LOG_DEBUG4:
        for logFunc in _log("dll-debug4").debug4Func(): logFunc(msg)
    elif level==LOG_DEBUG5:
        for logFunc in _log("dll-debug5").debug5Func(): logFunc(msg)
    else:
        for logFunc in _log("dll-invalid").errorFunc(): logFunc(msg)

def _initDll (logFunc):
    # dll is the DLL we wrap. Load it here.
    global dll
    dll=ctypes.CDLL("libsys_confd_pyconfdlib.so")

    # temp for 2.6 - support oper strings
    global libcDll
    libcDll=ctypes.CDLL("libc.so.6")

    # call py_init(), with a logger callback
    
    # This is the type of a callback
    ConfdLogFuncType=ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_char_p)
    # Make sure the Type is never garbage-collected
    global logFuncWrapper
    logFuncWrapper=ConfdLogFuncType(logFunc)
    dll.py_init.argtypes=[ConfdLogFuncType]
    dll.py_init.restype=ctypes.c_longlong

    """try:
        raise Exception('need to catch')
    except:
        for logFunc in _log("init-dll").errorFunc(): logFunc("got initDll. stack-trace is: %s", traceback.format_exc())"""
    rc=dll.py_init(logFuncWrapper)
    if rc != 0:
        raise Exception ("Could not init DLL, py_init() returned rc="+str(rc))

def _initTypes():
    # Type used for 'int64_t'
    global Int64Type
    Int64Type=ctypes.c_longlong

    # Type used for 'int32_t'
    global Int32Type
    Int32Type=ctypes.c_int

    global Int32ArrCreator
    def Int32ArrCreator (arr):
        return (Int32Type * len(arr))(*arr)

    # Type used for 'int16_t'
    global Int16Type
    Int16Type=ctypes.c_short

    # Type used for 'int8_t'
    global Int8Type
    Int8Type=ctypes.c_byte
    global Uint8PType
    Uint8PType=ctypes.POINTER(ctypes.c_ubyte)

    # Type used for 'uint64_t'
    global Uint64Type
    Uint64Type=ctypes.c_ulonglong

    # Type used for 'uint32_t'
    global Uint32Type
    Uint32Type=ctypes.c_uint

    # Type used for 'uint16_t'
    global Uint16Type
    Uint16Type=ctypes.c_ushort

    # Type used for 'uint8_t'
    global Uint8Type
    Uint8Type=ctypes.c_ubyte

    # Type used for 'char*'
    global CharPType
    CharPType = ctypes.c_char_p

    global CharType
    CharType = ctypes.c_char
    global CharTypeP
    CharTypeP = ctypes.POINTER(CharType)

    # Used to pass the object by reference
    global byRef
    byRef = ctypes.byref

    # Used to allocate a string buffer
    global createStringBuffer
    createStringBuffer = ctypes.create_string_buffer

    # Used to get the size of a ctypes object
    global sizeof
    sizeof = ctypes.sizeof

    # A ctypes type of a pointer to confd_value_t
    global ConfdValueTPtr
    ConfdValueTPtr=ctypes.POINTER(ConfdValueT)

    # A ctypes type of a pointer to confd_tag_value_t
    global ConfdTagValueTPtr
    ConfdTagValueTPtr=ctypes.POINTER(ConfdTagValueT)
    
    # A ctypes type of a pointer to confd_hkeypath_t
    global ConfdHkeypathTPtr
    ConfdHkeypathTPtr=ctypes.POINTER(ConfdHkeypathT)

    # A ctypes type of a pointer to confd_snmp_varbind
    global ConfdSnmpVarbindPtr
    ConfdSnmpVarbindPtr=ctypes.POINTER(ConfdSnmpVarbind)

    # A ctypes type of a pointer to confd_hkeypath_t
    global XmlTagTPtr
    XmlTagTPtr=ctypes.POINTER(XmlTagT)

    # A ctypes type of a pointer to struct confd_notification_ctx
    global ConfdNotificationCtxPtr
    ConfdNotificationCtxPtr=ctypes.POINTER(ConfdNotificationCtxStruct)

    global ConfdNotificationCtxPtrPtr
    ConfdNotificationCtxPtrPtr=ctypes.POINTER(ConfdNotificationCtxPtr)

    # A ctypes types of a pointer to struct confd_daemon_ctx
    global ConfdDaemonCtxPtr
    ConfdDaemonCtxPtr=ctypes.POINTER(ConfdDaemonCtxStruct)

    # A ctypes types of a pointer to struct maapi_cursor
    global MaapiCursorTPtr
    MaapiCursorTPtr=ctypes.POINTER(MaapiCursorT)
    
    # A ctypes types of a pointer to struct confd_trans_ctx
    global ConfdTransCtxPtr
    ConfdTransCtxPtr=ctypes.POINTER(ConfdTransCtx)

    # The type of an callback specified by confd_register_trans_cb
    global ConfdTransFuncType
    ConfdTransFuncType=ctypes.CFUNCTYPE(ctypes.c_int, ConfdTransCtxPtr)

    # The type of an callback specified by confd_register_validate_cb
    global ConfdTransValidateFuncType
    ConfdTransValidateFuncType=ctypes.CFUNCTYPE(ctypes.c_int, ConfdTransCtxPtr)

    global ConfdDataGetElemFuncType
    ConfdDataGetElemFuncType=ctypes.CFUNCTYPE(ctypes.c_int, ConfdTransCtxPtr, ConfdHkeypathTPtr)
    global ConfdDataGetNextFuncType
    ConfdDataGetNextFuncType=ctypes.CFUNCTYPE(ctypes.c_int, ConfdTransCtxPtr, ConfdHkeypathTPtr, ctypes.c_long)
    global ConfdDataGetObjFuncType
    ConfdDataGetObjFuncType=ctypes.CFUNCTYPE(ctypes.c_int, ConfdTransCtxPtr, ConfdHkeypathTPtr)
    global ConfdDataSetElemFuncType
    ConfdDataSetElemFuncType=ctypes.CFUNCTYPE(ctypes.c_int, ConfdTransCtxPtr, ConfdHkeypathTPtr, ConfdValueTPtr)
    global ConfdDataCreateFuncType
    ConfdDataCreateFuncType=ctypes.CFUNCTYPE(ctypes.c_int, ConfdTransCtxPtr, ConfdHkeypathTPtr)
    global ConfdDataRemoveFuncType
    ConfdDataRemoveFuncType=ctypes.CFUNCTYPE(ctypes.c_int, ConfdTransCtxPtr, ConfdHkeypathTPtr)

    global ConfdValpointFuncType
    ConfdValpointFuncType=ctypes.CFUNCTYPE(ctypes.c_int, ConfdTransCtxPtr, ConfdHkeypathTPtr, ConfdValueTPtr)

    global ConfdUserInfoPtr
    ConfdUserInfoPtr=ctypes.POINTER(ConfdUserInfo)
    global ConfdActionpointInitFuncType
    ConfdActionpointInitFuncType=ctypes.CFUNCTYPE(ctypes.c_int, ConfdUserInfoPtr)
    global ConfdActionpointAbortFuncType
    ConfdActionpointAbortFuncType=ctypes.CFUNCTYPE(ctypes.c_int, ConfdUserInfoPtr)
    global ConfdActionpointActionFuncType
    ConfdActionpointActionFuncType=ctypes.CFUNCTYPE(ctypes.c_int, ConfdUserInfoPtr, XmlTagTPtr, ConfdHkeypathTPtr, ConfdTagValueTPtr, Int32Type)

    # The type of an iteration callback for cdb_diff_iter
    global CdbDiffIterFuncType
    CdbDiffIterFuncType=ctypes.CFUNCTYPE(Int64Type, ConfdHkeypathTPtr, Int64Type, ConfdValueTPtr, ConfdValueTPtr)

def _initGlobals():
    # A dictionary of mappings between a user-object id() and the user-object itself,
    # used to implement the t_opaque functionality provided by 'struct confd_trans_ctx -> t_opaque'
    # Since this is used potentially from multiple threads, it is guarded by a Lock
    global contextMapping
    contextMapping=ContextMappings()

    # A dictionary of all hashed strings, for caching.
    # Protected by hashedStringsLock for thread safety
    global hashedStrings
    hashedStrings={}
    global prefixStringsHashed
    prefixStringsHashed={}
    global hashedStringsLock
    hashedStringsLock=threading.Lock()
    global stringsHashed
    stringsHashed={}
    global stringHashedLock
    stringHashedLock=threading.Lock()

def _initPrototypes ():
    # Utility funcs defined in py-confd.cpp, which are not direct wrappers of a matching confd function :
    #=====================================================================================================

    dll.py_getEnumValue.argtypes = [ctypes.c_char_p, ctypes.POINTER(Int64Type)]
    dll.py_getEnumValue.restype = Int64Type

    dll.py_CONFD_GET_XMLTAG.argtypes = [ConfdValueTPtr, Int64Type, ctypes.POINTER(Int64Type)]
    dll.py_CONFD_GET_XMLTAG.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_GET_XMLTAG_NS.argtypes = [ConfdValueTPtr, Int64Type, ctypes.POINTER(Int64Type)]
    dll.py_CONFD_GET_XMLTAG_NS.restype = ConfdReturnCode.getByValue
    
    dll.py_CONFD_SET_XMLTAG.argtypes = [ConfdValueTPtr, Int64Type, Int64Type, Int64Type]
    dll.py_CONFD_SET_XMLTAG.restype = ConfdReturnCode.getByValue
    
    dll.py_CONFD_GET_XMLBEGIN.argtypes = [ConfdValueTPtr, Int64Type, ctypes.POINTER(Int64Type)]
    dll.py_CONFD_GET_XMLBEGIN.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_GET_XMLBEGIN_NS.argtypes = [ConfdValueTPtr, Int64Type, ctypes.POINTER(Int64Type)]
    dll.py_CONFD_GET_XMLBEGIN_NS.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_SET_XMLBEGIN.argtypes = [ConfdValueTPtr, Int64Type, Int64Type, Int64Type]
    dll.py_CONFD_SET_XMLBEGIN.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_GET_XMLEND.argtypes = [ConfdValueTPtr, Int64Type, ctypes.POINTER(Int64Type)]
    dll.py_CONFD_GET_XMLEND.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_GET_XMLEND_NS.argtypes = [ConfdValueTPtr, Int64Type, ctypes.POINTER(Int64Type)]
    dll.py_CONFD_GET_XMLEND_NS.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_SET_XMLEND.argtypes = [ConfdValueTPtr, Int64Type, Int64Type, Int64Type]
    dll.py_CONFD_SET_XMLEND.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_SET_NOEXISTS.argtypes = [ConfdValueTPtr, Int64Type]
    dll.py_CONFD_SET_NOEXISTS.restype = ConfdReturnCode.getByValue
    
    dll.py_CONFD_GET_STR.argtypes = [ConfdValueTPtr, Int64Type, ctypes.POINTER(ctypes.c_char_p)]
    dll.py_CONFD_GET_STR.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_GET_BUFPTR.argtypes = [ConfdValueTPtr, Int64Type, ctypes.POINTER(ctypes.c_char_p)]
    dll.py_CONFD_GET_BUFPTR.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_GET_OIDPTR.argtypes = [ConfdValueTPtr, Int64Type, ctypes.POINTER(ctypes.POINTER(Int32Type))]
    dll.py_CONFD_GET_OIDPTR.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_GET_BINARY_PTR.argtypes = [ConfdValueTPtr, Int64Type, ctypes.POINTER(ctypes.c_char_p)]
    dll.py_CONFD_GET_BINARY_PTR.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_GET_BINARY_PTR_DUP.argtypes = [ConfdValueTPtr, Int64Type, Int64Type, ctypes.c_char_p]
    dll.py_CONFD_GET_BINARY_PTR_DUP.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_GET_BUFSIZE.argtypes = [ConfdValueTPtr, Int64Type, ctypes.POINTER(Int64Type)]
    dll.py_CONFD_GET_BUFSIZE.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_GET_OIDSIZE.argtypes = [ConfdValueTPtr, Int64Type, ctypes.POINTER(Int64Type)]
    dll.py_CONFD_GET_OIDSIZE.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_GET_BINARY_SIZE.argtypes = [ConfdValueTPtr, Int64Type, ctypes.POINTER(Int64Type)]
    dll.py_CONFD_GET_BINARY_SIZE.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_SET_STR.argtypes = [ConfdValueTPtr, Int64Type, ctypes.c_char_p]
    dll.py_CONFD_SET_STR.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_SET_BUF.argtypes = [ConfdValueTPtr, Int64Type, ctypes.c_char_p, Int32Type]
    dll.py_CONFD_SET_BUF.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_SET_OID_DUP.argtypes = [ConfdValueTPtr, Int64Type, ctypes.POINTER(Int32Type), Int32Type]
    dll.py_CONFD_SET_OID_DUP.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_SET_BINARY.argtypes = [ConfdValueTPtr, Int64Type, ctypes.c_char_p, Int32Type]
    dll.py_CONFD_SET_BINARY.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_SET_STR_DUP.argtypes = [ConfdValueTPtr, Int64Type, ctypes.c_char_p]
    dll.py_CONFD_SET_STR_DUP.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_SET_BUF_DUP.argtypes = [ConfdValueTPtr, Int64Type, ctypes.c_char_p, Int32Type]
    dll.py_CONFD_SET_BUF_DUP.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_SET_BINARY_DUP.argtypes = [ConfdValueTPtr, Int64Type, ctypes.c_char_p, Int32Type]
    dll.py_CONFD_SET_BINARY_DUP.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_SET_INT64.argtypes = [ConfdValueTPtr, Int64Type, Int64Type]
    dll.py_CONFD_SET_INT64.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_GET_INT64.argtypes = [ConfdValueTPtr, Int64Type, ctypes.POINTER(Int64Type)]
    dll.py_CONFD_GET_INT64.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_SET_INT32.argtypes = [ConfdValueTPtr, Int64Type, Int64Type]
    dll.py_CONFD_SET_INT32.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_GET_INT32.argtypes = [ConfdValueTPtr, Int64Type, ctypes.POINTER(Int32Type)]
    dll.py_CONFD_GET_INT32.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_SET_INT16.argtypes = [ConfdValueTPtr, Int64Type, Int64Type]
    dll.py_CONFD_SET_INT16.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_GET_INT16.argtypes = [ConfdValueTPtr, Int64Type, ctypes.POINTER(Int16Type)]
    dll.py_CONFD_GET_INT16.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_SET_INT8.argtypes = [ConfdValueTPtr, Int64Type, Int64Type]
    dll.py_CONFD_SET_INT8.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_GET_INT8.argtypes = [ConfdValueTPtr, Int64Type, ctypes.POINTER(Int8Type)]
    dll.py_CONFD_GET_INT8.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_SET_UINT64.argtypes = [ConfdValueTPtr, Int64Type, Int64Type]
    dll.py_CONFD_SET_UINT64.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_GET_UINT64.argtypes = [ConfdValueTPtr, Int64Type, ctypes.POINTER(Uint64Type)]
    dll.py_CONFD_GET_UINT64.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_SET_UINT32.argtypes = [ConfdValueTPtr, Int64Type, Int32Type]
    dll.py_CONFD_SET_UINT32.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_GET_UINT32.argtypes = [ConfdValueTPtr, Int64Type, ctypes.POINTER(Uint32Type)]
    dll.py_CONFD_GET_UINT32.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_SET_UINT16.argtypes = [ConfdValueTPtr, Int64Type, Int16Type]
    dll.py_CONFD_SET_UINT16.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_GET_UINT16.argtypes = [ConfdValueTPtr, Int64Type, ctypes.POINTER(Uint16Type)]
    dll.py_CONFD_GET_UINT16.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_SET_UINT8.argtypes = [ConfdValueTPtr, Int64Type, Int8Type]
    dll.py_CONFD_SET_UINT8.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_GET_UINT8.argtypes = [ConfdValueTPtr, Int64Type, ctypes.POINTER(Uint8Type)]
    dll.py_CONFD_GET_UINT8.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_GET_IPV4.argtypes = [ConfdValueTPtr, Int64Type, ctypes.POINTER(Uint32Type)]
    dll.py_CONFD_GET_IPV4.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_GET_IPV6.argtypes = [ConfdValueTPtr, Int64Type, ctypes.c_char_p]
    dll.py_CONFD_GET_IPV6.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_SET_IPV4.argtypes = [ConfdValueTPtr, Int64Type, Uint32Type]
    dll.py_CONFD_SET_IPV4.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_SET_IPV6.argtypes = [ConfdValueTPtr, Int64Type, ctypes.POINTER(ctypes.c_char_p)]
    dll.py_CONFD_SET_IPV6.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_SET_IPV4_PREFIX.argtypes = [ConfdValueTPtr, Int64Type, Uint32Type, Uint8Type]
    dll.py_CONFD_SET_IPV4_PREFIX.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_SET_IPV6_PREFIX.argtypes = [ConfdValueTPtr, Int64Type, ctypes.c_char_p, Uint8Type]
    dll.py_CONFD_SET_IPV6_PREFIX.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_GET_IPV4_PREFIX.argtypes = [ConfdValueTPtr, Int64Type, ctypes.POINTER(Uint32Type), ctypes.POINTER(Uint8Type)]
    dll.py_CONFD_GET_IPV4_PREFIX.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_GET_IPV6_PREFIX.argtypes = [ConfdValueTPtr, Int64Type,  ctypes.c_char_p, ctypes.POINTER(Uint8Type)]
    dll.py_CONFD_GET_IPV6_PREFIX.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_GET_BOOL.argtypes = [ConfdValueTPtr, Int64Type, ctypes.POINTER(Int64Type)]
    dll.py_CONFD_GET_BOOL.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_SET_BOOL.argtypes = [ConfdValueTPtr, Int64Type, Int64Type]
    dll.py_CONFD_SET_BOOL.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_GET_ENUM_HASH.argtypes = [ConfdValueTPtr, Int64Type, ctypes.POINTER(Int64Type)]
    dll.py_CONFD_GET_ENUM_HASH.restype = ConfdReturnCode.getByValue

    dll.py_CONFD_SET_ENUM_HASH.argtypes = [ConfdValueTPtr, Int64Type, Int64Type]
    dll.py_CONFD_SET_ENUM_HASH.restype = ConfdReturnCode.getByValue

    dll.py_allocConfdValue.argtypes = [Int64Type]
    dll.py_allocConfdValue.restype = ConfdValueTPtr

    dll.py_deallocConfdValue.argtypes = [ConfdValueTPtr]
    dll.py_deallocConfdValue.restype = None

    dll.py_allocConfdTagValues.argtypes = [Int64Type]
    dll.py_allocConfdTagValues.restype = ConfdTagValueTPtr

    dll.py_deallocConfdTagValues.argtypes = [ConfdTagValueTPtr]
    dll.py_deallocConfdTagValues.restype = None

    dll.py_deallocConfdTagValues.argtypes = [ConfdTagValueTPtr]
    dll.py_deallocConfdTagValues.restype = None

    dll.py_allocSnmpVarbinds.argtypes = [Int64Type]
    dll.py_allocSnmpVarbinds.restype = ConfdSnmpVarbindPtr

    dll.py_deallocSnmpVarbinds.argtypes = [ConfdSnmpVarbindPtr]
    dll.py_deallocSnmpVarbinds.restype = None

    dll.py_setSnmpVarbindVariable.argtypes = [ConfdSnmpVarbindPtr, Int64Type, ctypes.c_char_p]
    dll.py_setSnmpVarbindVariable.restype = ConfdReturnCode.getByValue

    dll.py_setSnmpVarbindOid.argtypes = [ConfdSnmpVarbindPtr, Int64Type, ctypes.POINTER(Uint32Type), Int64Type]
    dll.py_setSnmpVarbindOid.restype = ConfdReturnCode.getByValue

    dll.py_setSnmpVarbindColRow.argtypes = [ConfdSnmpVarbindPtr, Int64Type, ctypes.c_char_p, ctypes.POINTER(Uint32Type), Int64Type]
    dll.py_setSnmpVarbindColRow.restype = ConfdReturnCode.getByValue

    dll.py_getValPtrFromSnmpVarbind.argtypes = [ConfdSnmpVarbindPtr, Int64Type]
    dll.py_getValPtrFromSnmpVarbind.restype = ConfdValueTPtr

    dll.py_confd_notification_send_snmp.argtypes = [ConfdNotificationCtxPtr, ctypes.c_char_p, ConfdSnmpVarbindPtr, Int64Type]
    dll.py_confd_notification_send_snmp.restype = ConfdReturnCode.getByValue

    dll.py_allocConfdHkeypath.argtypes = None
    dll.py_allocConfdHkeypath.restype = ConfdHkeypathTPtr

    dll.py_deallocConfdHkeypath.argtypes = [ConfdHkeypathTPtr]
    dll.py_deallocConfdHkeypath.restype = None

    dll.py_allocMaapiCursor.argtypes = []
    dll.py_allocMaapiCursor.restype = MaapiCursorTPtr

    dll.py_deallocMaapiCursor.argtypes = [MaapiCursorTPtr]
    dll.py_deallocMaapiCursor.restype = None

    dll.py_getConfdErrno.argtypes = []
    dll.py_getConfdErrno.restype = ConfdErrno.getByValue

    dll.py_getValueType.argtypes = [ConfdValueTPtr, Int64Type]
    dll.py_getValueType.restype = ConfdVtype.getByValue

    dll.py_getHkeypathLen.argtypes = [ConfdHkeypathTPtr]
    dll.py_getHkeypathLen.restype = Int64Type

    dll.py_setHkeypathLen.argtypes = [ConfdHkeypathTPtr, Int64Type]
    dll.py_setHkeypathLen.restype = ConfdReturnCode.getByValue
    
    dll.py_getHkeypathValue.argtypes = [ConfdHkeypathTPtr, Int64Type, Int64Type, Int64Type]
    dll.py_getHkeypathValue.restype = ConfdValueTPtr
    
    dll.py_getConfdDaemonCtxDaemonId.argtypes = [ConfdDaemonCtxPtr]
    dll.py_getConfdDaemonCtxDaemonId.restype = Int64Type

    dll.py_getConfdDaemonCtxDaemonName.argtypes = [ConfdDaemonCtxPtr]
    dll.py_getConfdDaemonCtxDaemonName.restype = ctypes.c_char_p

    dll.py_getConfdTransCtxUserContext.argtypes = [ConfdTransCtxPtr]
    dll.py_getConfdTransCtxUserContext.restype = ctypes.c_char_p

    dll.py_getConfdTransCtxTFd.argtypes = [ConfdTransCtxPtr]
    dll.py_getConfdTransCtxTFd.restype = Int64Type

    dll.py_getConfdTransCtxTMode.argtypes = [ConfdTransCtxPtr]
    dll.py_getConfdTransCtxTMode.restype = Int64Type

    dll.py_getConfdTransCtxTDaemonCtx.argtypes = [ConfdTransCtxPtr]
    dll.py_getConfdTransCtxTDaemonCtx.restype = ConfdDaemonCtxPtr
    
    dll.py_getConfdTransCtxTransHandle.argtypes = [ConfdTransCtxPtr]
    dll.py_getConfdTransCtxTransHandle.restype = Int64Type

    dll.py_getConfdTransCtxTOpaque.argtypes = [ConfdTransCtxPtr]
    dll.py_getConfdTransCtxTOpaque.restype = ctypes.c_void_p

    dll.py_setConfdTransCtxTOpaque.argtypes = [ConfdTransCtxPtr, ctypes.c_void_p]
    dll.py_setConfdTransCtxTOpaque.restype = None

    dll.py_getConfdUserInfoFd.argtypes = [ConfdUserInfoPtr]
    dll.py_getConfdUserInfoFd.restype = Int64Type
    
    dll.py_getConfdUserInfoDaemonCtx.argtypes = [ConfdUserInfoPtr]
    dll.py_getConfdUserInfoDaemonCtx.restype = ConfdDaemonCtxPtr

    dll.py_getConfdUserInfoUserSessionId.argtypes = [ConfdUserInfoPtr]
    dll.py_getConfdUserInfoUserSessionId.restype = Int64Type

    dll.py_getConfdUserInfoOpaque.argtypes = [ConfdUserInfoPtr]
    dll.py_getConfdUserInfoOpaque.restype = ctypes.c_void_p

    dll.py_setConfdUserInfoOpaque.argtypes = [ConfdUserInfoPtr, ctypes.c_void_p]
    dll.py_setConfdUserInfoOpaque.restype = None

    # From here on are wrapped confd functions
    #===========================================

    dll.py_confd_free_value.argtypes = [ConfdValueTPtr, Int64Type]
    dll.py_confd_free_value.restype = ConfdReturnCode.getByValue

    dll.py_confd_value_dup_to.argtypes = [ConfdValueTPtr, Int64Type, ConfdValueTPtr, Int64Type]
    dll.py_confd_value_dup_to.restype = ConfdReturnCode.getByValue

    dll.py_confd_hkeypath_dup_len.argtypes = [ConfdHkeypathTPtr, Int64Type]
    dll.py_confd_hkeypath_dup_len.restype = ConfdHkeypathTPtr

    dll.py_confd_pp_kpath.argtypes = [ctypes.c_char_p, Int64Type, ConfdHkeypathTPtr]
    dll.py_confd_pp_kpath.restype = Int64Type

    dll.py_confd_pp_value.argtypes = [ctypes.c_char_p, Int64Type, ConfdValueTPtr, Int64Type]
    dll.py_confd_pp_value.restype = Int64Type

    dll.py_get_confd_value_type.argtypes = [ConfdValueTPtr]
    dll.py_get_confd_value_type.restype = Int64Type

    dll.py_getValPtrFromTagVal.argtypes = [ConfdTagValueTPtr, Int64Type]
    dll.py_getValPtrFromTagVal.restype = ConfdValueTPtr

    dll.py_getNSFromTagVal.argtypes = [ConfdTagValueTPtr, Int64Type]
    dll.py_getNSFromTagVal.restype = Uint32Type

    dll.py_setNSToTagVal.argtypes = [ConfdTagValueTPtr, Int64Type, Uint32Type]
    dll.py_setNSToTagVal.restype = ConfdReturnCode.getByValue

    dll.py_getTagFromTagVal.argtypes = [ConfdTagValueTPtr, Int64Type]
    dll.py_getTagFromTagVal.restype = Uint32Type

    dll.py_setTagToTagVal.argtypes = [ConfdTagValueTPtr, Int64Type, Uint32Type]
    dll.py_setTagToTagVal.restype = ConfdReturnCode.getByValue

    dll.py_confd_strerror.argtypes = [Int64Type]
    dll.py_confd_strerror.restype = ctypes.c_char_p

    dll.py_confd_lasterr.argtypes = []
    dll.py_confd_lasterr.restype = ctypes.c_char_p

    dll.py_confd_init.argtypes = [ctypes.c_char_p, Int64Type]
    dll.py_confd_init.restype = None

    dll.py_confd_init_daemon.argtypes = [ctypes.c_char_p]
    dll.py_confd_init_daemon.restype=ConfdDaemonCtxPtr

    dll.py_confd_str2hash.argtypes = [ctypes.c_char_p]
    dll.py_confd_str2hash.restype = Int64Type

    dll.py_confd_hash2str.argtypes = [Int64Type]
    dll.py_confd_hash2str.restype = ctypes.c_char_p

    dll.py_confd_ns2prefix.argtypes = [Int64Type]
    dll.py_confd_ns2prefix.restype = ctypes.c_char_p

    dll.py_confd_load_schemas.argtypes = [Int64Type, ctypes.c_char_p, Int64Type]
    dll.py_confd_load_schemas.restype = ConfdReturnCode.getByValue

    dll.py_confd_connect.argtypes = [ConfdDaemonCtxPtr, Int64Type, Int64Type, Int64Type, ctypes.c_char_p, Int64Type]
    dll.py_confd_connect.restype = ConfdReturnCode.getByValue

    dll.py_confd_trans_seterr.argtypes = [ConfdTransCtxPtr, ctypes.c_char_p]
    dll.py_confd_trans_seterr.restype = None

    dll.py_confd_action_seterr.argtypes = [ConfdUserInfoPtr, ctypes.c_char_p]
    dll.py_confd_action_seterr.restype = None

    dll.py_confd_register_snmp_notification.argtypes = [ConfdDaemonCtxPtr, Int64Type, ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(ConfdNotificationCtxPtr)]
    dll.py_confd_register_snmp_notification.restype = ConfdReturnCode.getByValue

    dll.py_confd_register_trans_cb.argtypes = [ConfdDaemonCtxPtr, ConfdTransFuncType, ConfdTransFuncType, ConfdTransFuncType]
    dll.py_confd_register_trans_cb.restype = ConfdReturnCode.getByValue

    dll.py_confd_register_trans_validate_cb.argtypes = [ConfdDaemonCtxPtr, ConfdTransValidateFuncType, ConfdTransValidateFuncType]
    dll.py_confd_register_trans_validate_cb.restype = ConfdReturnCode.getByValue

    dll.py_confd_register_transformation_data_cb.argtypes = [ConfdDaemonCtxPtr, ctypes.c_char_p, ConfdDataGetElemFuncType, ConfdDataGetNextFuncType, ConfdDataSetElemFuncType, ConfdDataCreateFuncType, ConfdDataRemoveFuncType]
    dll.py_confd_register_transformation_data_cb.restype = ConfdReturnCode.getByValue

    dll.py_confd_register_data_cb.argtypes = [ConfdDaemonCtxPtr, ctypes.c_char_p, ConfdDataGetElemFuncType, ConfdDataGetNextFuncType, ConfdDataGetObjFuncType]
    dll.py_confd_register_data_cb.restype = ConfdReturnCode.getByValue

    dll.py_confd_register_range_data_cb.argtypes = [ConfdDaemonCtxPtr, ctypes.c_char_p, ConfdDataGetElemFuncType, ConfdDataGetNextFuncType, ConfdDataGetObjFuncType, ConfdValueTPtr, ConfdValueTPtr, Int64Type, ctypes.c_char_p]
    dll.py_confd_register_range_data_cb.restype = ConfdReturnCode.getByValue

    dll.py_confd_register_range_valpoint_cb.argtypes = [ConfdDaemonCtxPtr, ctypes.c_char_p, ConfdValpointFuncType, ConfdValueTPtr, ConfdValueTPtr, ctypes.c_char_p]
    dll.py_confd_register_range_valpoint_cb.restype = ConfdReturnCode.getByValue

    dll.py_confd_register_range_action_cb.argtypes = [ConfdDaemonCtxPtr, ctypes.c_char_p, ConfdActionpointInitFuncType, ConfdActionpointAbortFuncType, ConfdActionpointActionFuncType, 
                                                      ConfdValueTPtr, ConfdValueTPtr, ctypes.c_char_p]
    dll.py_confd_register_range_action_cb.restype = ConfdReturnCode.getByValue

    dll.py_confd_register_action_cb.argtypes = [ConfdDaemonCtxPtr, ctypes.c_char_p, ConfdActionpointInitFuncType, ConfdActionpointAbortFuncType, ConfdActionpointActionFuncType]
    dll.py_confd_register_action_cb.restype = ConfdReturnCode.getByValue

    dll.py_confd_register_valpoint_cb.argtypes = [ConfdDaemonCtxPtr, ctypes.c_char_p, ConfdValpointFuncType]
    dll.py_confd_register_valpoint_cb.restype = ConfdReturnCode.getByValue
    
    dll.py_confd_register_done.argtypes = [ConfdDaemonCtxPtr]
    dll.py_confd_register_done.restype = ConfdReturnCode.getByValue

    dll.py_confd_release_daemon.argtypes = [ConfdDaemonCtxPtr]
    dll.py_confd_release_daemon.restype = None

    dll.py_confd_fd_ready.argtypes = [ConfdDaemonCtxPtr, Int64Type]
    dll.py_confd_fd_ready.restype = ConfdReturnCode.getByValue

    dll.py_confd_trans_set_fd.argtypes = [ConfdTransCtxPtr, Int64Type]
    dll.py_confd_trans_set_fd.restype = None

    dll.py_confd_action_set_fd.argtypes = [ConfdUserInfoPtr, Int64Type]
    dll.py_confd_action_set_fd.restype = None

    dll.py_confd_data_reply_next_key.argtypes = [ConfdTransCtxPtr, ConfdValueTPtr, Int64Type, ctypes.c_long]
    dll.py_confd_data_reply_next_key.restype = ConfdReturnCode.getByValue

    dll.py_confd_data_reply_not_found.argtypes = [ConfdTransCtxPtr]
    dll.py_confd_data_reply_not_found.restype = ConfdReturnCode.getByValue

    dll.py_confd_data_reply_value.argtypes = [ConfdTransCtxPtr, ConfdValueTPtr]
    dll.py_confd_data_reply_value.restype = ConfdReturnCode.getByValue

    dll.py_confd_data_reply_value_array.argtypes = [ConfdTransCtxPtr, ConfdValueTPtr, Int64Type]
    dll.py_confd_data_reply_value_array.restype = ConfdReturnCode.getByValue

    dll.py_confd_data_reply_tag_value_array.argtypes = [ConfdTransCtxPtr, ConfdTagValueTPtr, Int64Type]
    dll.py_confd_data_reply_tag_value_array.restype = ConfdReturnCode.getByValue

    dll.py_confd_action_reply_values_empty.argtypes = [ConfdUserInfoPtr]
    dll.py_confd_action_reply_values_empty.restype = ConfdReturnCode.getByValue
    
    # From here CDB functions

    dll.py_cdb_connect.argtypes = [Int64Type, Int64Type, Int64Type, ctypes.c_char_p, Int64Type]
    dll.py_cdb_connect.restype = ConfdReturnCode.getByValue

    dll.py_cdb_subscribe.argtypes = [Int64Type, Int64Type, Int64Type, ctypes.POINTER(Int64Type), ctypes.c_char_p]
    dll.py_cdb_subscribe.restype = ConfdReturnCode.getByValue

    dll.py_cdb_subscribe2.argtypes = [Int64Type, Int64Type, Int64Type, Int64Type, ctypes.POINTER(Int64Type), Int64Type, ctypes.c_char_p]
    dll.py_cdb_subscribe2.restype = ConfdReturnCode.getByValue

    dll.py_cdb_subscribe_done.argtypes = [Int64Type]
    dll.py_cdb_subscribe_done.restype = ConfdReturnCode.getByValue

    dll.py_cdb_start_session.argtypes = [Int64Type, Int64Type]
    dll.py_cdb_start_session.restype = ConfdReturnCode.getByValue

    dll.py_cdb_start_session2.argtypes = [Int64Type, Int64Type, Int64Type]
    dll.py_cdb_start_session2.restype = ConfdReturnCode.getByValue

    dll.py_cdb_subscribe_done.argtypes = [Int64Type]
    dll.py_cdb_end_session.restype = ConfdReturnCode.getByValue

    dll.py_cdb_read_subscription_socket.argtypes = [Int64Type, ctypes.POINTER(Int64Type), ctypes.POINTER(Int64Type)]
    dll.py_cdb_read_subscription_socket.restype = ConfdReturnCode.getByValue

    dll.py_cdb_read_subscription_socket2.argtypes = [Int64Type, ctypes.POINTER(Int64Type), ctypes.POINTER(Int64Type), ctypes.POINTER(Int64Type), Int64Type,  ctypes.POINTER(Int64Type)]
    dll.py_cdb_read_subscription_socket2.restype = ConfdReturnCode.getByValue

    dll.py_cdb_sub_abort_trans.argtypes = [Int64Type, Int64Type, Int64Type, Int64Type, ctypes.c_char_p]
    dll.py_cdb_sub_abort_trans.restype = ConfdReturnCode.getByValue

    dll.py_cdb_sync_subscription_socket.argtypes = [Int64Type, Int64Type]
    dll.py_cdb_sync_subscription_socket.restype = ConfdReturnCode.getByValue

    dll.py_cdb_trigger_subscriptions.argtypes = [Int64Type, ctypes.POINTER(Int64Type), Int64Type]
    dll.py_cdb_trigger_subscriptions.restype = ConfdReturnCode.getByValue

    dll.py_cdb_set_namespace.argtypes = [Int64Type, Int64Type]
    dll.py_cdb_set_namespace.restype = ConfdReturnCode.getByValue

    dll.py_cdb_cd.argtypes = [Int64Type, ctypes.c_char_p]
    dll.py_cdb_cd.restype = ConfdReturnCode.getByValue

    dll.py_cdb_num_instances.argtypes = [Int64Type, ctypes.c_char_p]
    dll.py_cdb_num_instances.restype = Int64Type

    dll.py_cdb_get.argtypes = [Int64Type, ConfdValueTPtr, ctypes.c_char_p]
    dll.py_cdb_get.restype = ConfdReturnCode.getByValue

    dll.py_cdb_get_str.argtypes = [Int64Type, ctypes.c_char_p, Int64Type, ctypes.c_char_p]
    dll.py_cdb_get_str.restype = ConfdReturnCode.getByValue

    dll.py_cdb_get_int64.argtypes = [Int64Type, ctypes.POINTER(Int64Type), ctypes.c_char_p]
    dll.py_cdb_get_int64.restype = ConfdReturnCode.getByValue

    dll.py_cdb_diff_iterate.argtypes = [Int64Type, Int64Type, CdbDiffIterFuncType, Int64Type]
    dll.py_cdb_diff_iterate.restype = ConfdReturnCode.getByValue

    # From here MAAPI functions

    dll.py_maapi_connect.argtypes = [Int64Type, Int64Type, ctypes.c_char_p, Int64Type]
    dll.py_maapi_connect.restype = ConfdReturnCode.getByValue

    dll.py_maapi_attach.argtypes = [Int64Type, Int64Type, ConfdTransCtxPtr]
    dll.py_maapi_attach.restype = ConfdReturnCode.getByValue

    dll.py_maapi_detach.argtypes = [Int64Type, ConfdTransCtxPtr]
    dll.py_maapi_detach.restype = ConfdReturnCode.getByValue

    dll.py_maapi_reload_config.argtypes = [Int64Type]
    dll.py_maapi_reload_config.restype = ConfdReturnCode.getByValue

    dll.py_maapi_wait_start.argtypes = [Int64Type, Int64Type]
    dll.py_maapi_wait_start.restype = ConfdReturnCode.getByValue

    dll.py_maapi_load_schemas.argtypes = [Int64Type]
    dll.py_maapi_load_schemas.restype = ConfdReturnCode.getByValue

    dll.py_maapi_close.argtypes = [Int64Type]
    dll.py_maapi_close.restype = ConfdReturnCode.getByValue

    dll.py_maapi_start_user_session.argtypes = [Int64Type, ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_char_p), 
                                                Int64Type, Int64Type, ctypes.c_char_p, Int64Type]
    dll.py_maapi_start_user_session.restype = ConfdReturnCode.getByValue

    dll.py_maapi_end_user_session.argtypes = [Int64Type]
    dll.py_maapi_end_user_session.restype = ConfdReturnCode.getByValue

    dll.py_maapi_delete_config.argtypes = [Int64Type, Int64Type]
    dll.py_maapi_delete_config.restype = ConfdReturnCode.getByValue

    dll.py_maapi_start_trans.argtypes = [Int64Type, Int64Type, Int64Type]
    dll.py_maapi_start_trans.restype = Int64Type
    
    dll.py_maapi_apply_trans.argtypes = [Int64Type, Int64Type, Int64Type]
    dll.py_maapi_apply_trans.restype = ConfdReturnCode.getByValue

    dll.py_maapi_finish_trans.argtypes = [Int64Type, Int64Type]
    dll.py_maapi_finish_trans.restype = ConfdReturnCode.getByValue

    dll.py_maapi_get_values.argtypes = [Int64Type, Int64Type, ConfdTagValueTPtr, Int64Type, ctypes.c_char_p]
    dll.py_maapi_get_values.restype = ConfdReturnCode.getByValue
    
    dll.py_maapi_set_values.argtypes = [Int64Type, Int64Type, ConfdTagValueTPtr, Int64Type, ctypes.c_char_p]
    dll.py_maapi_set_values.restype = ConfdReturnCode.getByValue

    dll.py_maapi_set_namespace.argtypes = [Int64Type, Int64Type, Int64Type]
    dll.py_maapi_set_namespace.restype = ConfdReturnCode.getByValue
    
    dll.py_maapi_num_instances.argtypes = [Int64Type, Int64Type, ctypes.c_char_p]
    dll.py_maapi_num_instances.restype = Int64Type

    dll.py_maapi_create.argtypes = [Int64Type, Int64Type, ctypes.c_char_p]
    dll.py_maapi_create.restype = ConfdReturnCode.getByValue

    dll.py_maapi_delete.argtypes = [Int64Type, Int64Type, ctypes.c_char_p]
    dll.py_maapi_delete.restype = ConfdReturnCode.getByValue

    dll.py_maapi_delete_all.argtypes = [Int64Type, Int64Type, Int64Type]
    dll.py_maapi_delete_all.restype = ConfdReturnCode.getByValue

    dll.py_maapi_get_str_elem.argtypes = [Int64Type, Int64Type, ctypes.c_char_p, Int64Type, ctypes.c_char_p]
    dll.py_maapi_get_str_elem.restype = ConfdReturnCode.getByValue
    
    dll.py_maapi_get_int64_elem.argtypes = [Int64Type, Int64Type, ctypes.POINTER(Int64Type), ctypes.c_char_p]
    dll.py_maapi_get_int64_elem.restype = ConfdReturnCode.getByValue

    dll.py_maapi_get_uint64_elem.argtypes = [Int64Type, Int64Type, ctypes.POINTER(Uint64Type), ctypes.c_char_p]
    dll.py_maapi_get_uint64_elem.restype = ConfdReturnCode.getByValue

    dll.py_maapi_get_int8_elem.argtypes = [Int64Type, Int64Type, ctypes.POINTER(Int8Type), ctypes.c_char_p]
    dll.py_maapi_get_int8_elem.restype = ConfdReturnCode.getByValue

    dll.py_maapi_get_enum_hash_elem.argtypes = [Int64Type, Int64Type, ctypes.POINTER(Int32Type), ctypes.c_char_p]
    dll.py_maapi_get_enum_hash_elem.restype = ConfdReturnCode.getByValue
    
    dll.py_maapi_get_ipv4_elem.argtypes = [Int64Type, Int64Type, ctypes.c_char_p, Int64Type, ctypes.c_char_p]
    dll.py_maapi_get_ipv4_elem.restype = ConfdReturnCode.getByValue

    dll.py_maapi_get_ipv4prefix_elem.argtypes = [Int64Type, Int64Type, ctypes.c_char_p, Int64Type, ctypes.POINTER(Uint8Type), ctypes.c_char_p]
    dll.py_maapi_get_ipv4prefix_elem.restype = ConfdReturnCode.getByValue

    dll.py_maapi_set_elem2.argtypes = [Int64Type, Int64Type, ctypes.c_char_p, ctypes.c_char_p]
    dll.py_maapi_set_elem2.restype = ConfdReturnCode.getByValue

    dll.py_maapi_init_cursor.argtypes = [Int64Type, Int64Type, MaapiCursorTPtr, ctypes.c_char_p]
    dll.py_maapi_init_cursor.restype = ConfdReturnCode.getByValue

    dll.py_maapi_destroy_cursor.argtypes = [MaapiCursorTPtr]
    dll.py_maapi_destroy_cursor.restype = None

    dll.py_maapiCursorGetN.argtypes = [MaapiCursorTPtr]
    dll.py_maapiCursorGetN.restype = Int64Type

    dll.py_maapiCursorGetValue.argtypes = [MaapiCursorTPtr, Int64Type]
    dll.py_maapiCursorGetValue.restype = ConfdValueTPtr

    dll.py_maapi_get_next.argtypes = [MaapiCursorTPtr]
    dll.py_maapi_get_next.restype = ConfdReturnCode.getByValue

    # temp for 2.6 - support oper strings
    libcDll.strdup.argtypes = [ctypes.POINTER(ctypes.c_char)]
    libcDll.strdup.restype = ctypes.POINTER(ctypes.c_char)

    libcDll.free.argtypes = [ctypes.POINTER(ctypes.c_char)]
    libcDll.free.restype = None
    
def _initConstants ():
    def getGlobal (name):
        valueInt64=Int64Type()
        rc=dll.py_getEnumValue(name, ctypes.byref(valueInt64))
        if rc != 0:
            raise Exception ("Could not get global value for "+str(name)+", rc="+str(rc))
        return valueInt64.value

    global MAXDEPTH
    MAXDEPTH=getGlobal('MAXDEPTH')
    global MAXKEYLEN
    MAXKEYLEN=getGlobal('MAXKEYLEN')
    

    # flags #defined for cdb_start_session2
    global CDB_LOCK_WAIT
    CDB_LOCK_WAIT = getGlobal('CDB_LOCK_WAIT')
    global CDB_LOCK_SESSION
    CDB_LOCK_SESSION = getGlobal('CDB_LOCK_SESSION')
    global CDB_LOCK_REQUEST
    CDB_LOCK_REQUEST = getGlobal('CDB_LOCK_REQUEST')

    # flags returned by cdb_read_subscription_socket2
    global CDB_SUB_FLAG_IS_LAST
    CDB_SUB_FLAG_IS_LAST = getGlobal('CDB_SUB_FLAG_IS_LAST')
    global CDB_SUB_FLAG_TRIGGER
    CDB_SUB_FLAG_TRIGGER = getGlobal('CDB_SUB_FLAG_TRIGGER')
    global CDB_SUB_FLAG_REVERT
    CDB_SUB_FLAG_REVERT = getGlobal('CDB_SUB_FLAG_REVERT')

def _initEnums():
    AddressFamily.add()
    ConfdReturnCode.add()
    ConfdErrno.add()
    ConfdVtype.add()
    ConfdDebugLevel.add()
    CdbSockType.add()
    CdbDbType.add()
    ConfdIterRet.add()
    ConfdIterOp.add()
    ConfdIterFlags.add()
    CdbSubType.add()
    CdbSubNotification.add()
    CdbSubscriptionSyncType.add()
    ConfdSockType.add()
    ConfdProto.add()
    ConfdDbName.add()
    ConfdTransMode.add()
    ConfdErrcode.add()
    MaapiDeleteHow.add()


# Enum support
#===================

class PyEnum:
    """A generic enumeration class. See usage examples below."""
    @classmethod
    def addEnum (cls, name):
        """Adds an enumerated value"""
        # We create the class dictionary upon the first call to addEnum().
        # We cannot do it earlier because we need to have the 'cls' instance
        # (There is a way to do it with type() or something like that, but I want to KISS)
        if '_ourValueToObj' not in cls.__dict__:
            cls._ourValueToObj={}
        valueInt64=Int64Type()
        rc=dll.py_getEnumValue(name, ctypes.byref(valueInt64))
        if rc != 0:
            raise Exception ("Could not get enum value for "+str(name)+", rc="+str(rc))
        value=valueInt64.value
        if value in cls._ourValueToObj:
            raise Exception ("Duplicate value "+str(value)+" received for name "+str(name)+", it exists for name "+cls._ourValueToObj[value].getName())
        newObj=cls(name, value)
        cls._ourValueToObj[value]=newObj
        return newObj

    @classmethod
    def getByValue (cls, value):
        """
        Gets an enumerated object by a numeric value.
        If value is not defined in this class, returne None
        """
        if cls.isValueValid(value):
            return cls._ourValueToObj[value]
        return None

    @classmethod
    def isValueValid (cls, value):
        """
        If value is defined in this class, returns True
        Otherwise, returns False
        """
        return value in cls._ourValueToObj

    @classmethod
    def getNameByValue(cls, value):
        """
        Gets a name by a numeric value.
        If value is not defined in this class, returns "N/A"
        """
        if cls.isValueValid(value):
            return cls._ourValueToObj[value]._myName
        return "N/A"

    def getValue (self):
        return self._myValue

    def getName (self):
        return self._myName

    def __init__ (self, name, value):
        self._myName=name
        self._myValue=value

    def __str__ (self):
        return self._myName

    def __repr__ (self):
        return str(self.__class__) + ":" + str(self)


# Binary Buffer Support
def getBufAsString (startPtr, type_, len_):
    l = ""
    for i in range(len_):
        cur = ctypes.cast(ctypes.addressof(startPtr.contents)+i, type_)
        l += (chr(cur.contents.value))

    #cur = ctypes.cast(ctypes.addressof(startPtr.contents), type_*len_)
    return l


# Classes with ENUM values which have parallel definitions in py-confd.cpp
# Any change here must be reflected in py-confd.cpp
#=============================================================

class AddressFamily(PyEnum):

    @classmethod
    def add (cls):
        global AF_INET
        AF_INET = cls.addEnum('AF_INET')
        global AF_INET6
        AF_INET6 = cls.addEnum('AF_INET6')

# confd return code values
class ConfdReturnCode(PyEnum):

    @classmethod
    def add (cls):
        global CONFD_DELAYED_RESPONSE
        CONFD_DELAYED_RESPONSE = cls.addEnum('CONFD_DELAYED_RESPONSE')
        global CONFD_ACCUMULATE
        CONFD_ACCUMULATE       = cls.addEnum('CONFD_ACCUMULATE')
        global CONFD_OK
        CONFD_OK               = cls.addEnum('CONFD_OK')
        global CONFD_ERR
        CONFD_ERR              = cls.addEnum('CONFD_ERR')
        global CONFD_EOF
        CONFD_EOF              = cls.addEnum('CONFD_EOF')
        global CONFD_VALIDATION_WARN
        CONFD_VALIDATION_WARN  = cls.addEnum('CONFD_VALIDATION_WARN')
        global CONFD_ALREADY_LOCKED
        CONFD_ALREADY_LOCKED   = cls.addEnum('CONFD_ALREADY_LOCKED')
        global CONFD_IN_USE
        CONFD_IN_USE           = cls.addEnum('CONFD_IN_USE')
        # Invented a new confd return code - don't tell anyone !
        global CONFD_BAD_PYTHON_USAGE
        CONFD_BAD_PYTHON_USAGE = cls('CONFD_BAD_PYTHON_USAGE', -99)

# confd errno values
class ConfdErrno(PyEnum):
    @classmethod
    def add (cls):
        global CONFD_ERR_NOEXISTS
        CONFD_ERR_NOEXISTS = cls.addEnum('CONFD_ERR_NOEXISTS')
        global CONFD_ERR_ALREADY_EXISTS
        CONFD_ERR_ALREADY_EXISTS = cls.addEnum('CONFD_ERR_ALREADY_EXISTS')
        global CONFD_ERR_ACCESS_DENIED
        CONFD_ERR_ACCESS_DENIED = cls.addEnum('CONFD_ERR_ACCESS_DENIED')
        global CONFD_ERR_NOT_WRITABLE
        CONFD_ERR_NOT_WRITABLE = cls.addEnum('CONFD_ERR_NOT_WRITABLE')
        global CONFD_ERR_BADTYPE
        CONFD_ERR_BADTYPE = cls.addEnum('CONFD_ERR_BADTYPE')
        global CONFD_ERR_NOTCREATABLE
        CONFD_ERR_NOTCREATABLE = cls.addEnum('CONFD_ERR_NOTCREATABLE')
        global CONFD_ERR_NOTDELETABLE
        CONFD_ERR_NOTDELETABLE = cls.addEnum('CONFD_ERR_NOTDELETABLE')
        global CONFD_ERR_BADPATH
        CONFD_ERR_BADPATH = cls.addEnum('CONFD_ERR_BADPATH')
        global CONFD_ERR_NOSTACK
        CONFD_ERR_NOSTACK = cls.addEnum('CONFD_ERR_NOSTACK')
        global CONFD_ERR_LOCKED
        CONFD_ERR_LOCKED = cls.addEnum('CONFD_ERR_LOCKED')
        global CONFD_ERR_INUSE
        CONFD_ERR_INUSE = cls.addEnum('CONFD_ERR_INUSE')
        global CONFD_ERR_NOTSET
        CONFD_ERR_NOTSET = cls.addEnum('CONFD_ERR_NOTSET')
        global CONFD_ERR_NON_UNIQUE
        CONFD_ERR_NON_UNIQUE = cls.addEnum('CONFD_ERR_NON_UNIQUE')
        global CONFD_ERR_BAD_KEYREF
        CONFD_ERR_BAD_KEYREF = cls.addEnum('CONFD_ERR_BAD_KEYREF')
        global CONFD_ERR_TOO_FEW_ELEMS
        CONFD_ERR_TOO_FEW_ELEMS = cls.addEnum('CONFD_ERR_TOO_FEW_ELEMS')
        global CONFD_ERR_TOO_MANY_ELEMS
        CONFD_ERR_TOO_MANY_ELEMS = cls.addEnum('CONFD_ERR_TOO_MANY_ELEMS')
        global CONFD_ERR_BADSTATE
        CONFD_ERR_BADSTATE = cls.addEnum('CONFD_ERR_BADSTATE')
        global CONFD_ERR_INTERNAL
        CONFD_ERR_INTERNAL = cls.addEnum('CONFD_ERR_INTERNAL')
        global CONFD_ERR_EXTERNAL
        CONFD_ERR_EXTERNAL = cls.addEnum('CONFD_ERR_EXTERNAL')
        global CONFD_ERR_MALLOC
        CONFD_ERR_MALLOC = cls.addEnum('CONFD_ERR_MALLOC')
        global CONFD_ERR_PROTOUSAGE
        CONFD_ERR_PROTOUSAGE = cls.addEnum('CONFD_ERR_PROTOUSAGE')
        global CONFD_ERR_NOSESSION
        CONFD_ERR_NOSESSION = cls.addEnum('CONFD_ERR_NOSESSION')
        global CONFD_ERR_TOOMANYTRANS
        CONFD_ERR_TOOMANYTRANS = cls.addEnum('CONFD_ERR_TOOMANYTRANS')
        global CONFD_ERR_OS
        CONFD_ERR_OS = cls.addEnum('CONFD_ERR_OS')
        global CONFD_ERR_HA_CONNECT
        CONFD_ERR_HA_CONNECT = cls.addEnum('CONFD_ERR_HA_CONNECT')
        global CONFD_ERR_HA_CLOSED
        CONFD_ERR_HA_CLOSED = cls.addEnum('CONFD_ERR_HA_CLOSED')
        global CONFD_ERR_HA_BADFXS
        CONFD_ERR_HA_BADFXS = cls.addEnum('CONFD_ERR_HA_BADFXS')
        global CONFD_ERR_HA_BADTOKEN
        CONFD_ERR_HA_BADTOKEN = cls.addEnum('CONFD_ERR_HA_BADTOKEN')
        global CONFD_ERR_HA_BADNAME
        CONFD_ERR_HA_BADNAME = cls.addEnum('CONFD_ERR_HA_BADNAME')
        global CONFD_ERR_HA_BIND
        CONFD_ERR_HA_BIND = cls.addEnum('CONFD_ERR_HA_BIND')
        global CONFD_ERR_HA_NOTICK
        CONFD_ERR_HA_NOTICK = cls.addEnum('CONFD_ERR_HA_NOTICK')
        global CONFD_ERR_VALIDATION_WARNING
        CONFD_ERR_VALIDATION_WARNING = cls.addEnum('CONFD_ERR_VALIDATION_WARNING')
        global CONFD_ERR_SUBAGENT_DOWN
        CONFD_ERR_SUBAGENT_DOWN = cls.addEnum('CONFD_ERR_SUBAGENT_DOWN')
        global CONFD_ERR_LIB_NOT_INITIALIZED
        CONFD_ERR_LIB_NOT_INITIALIZED = cls.addEnum('CONFD_ERR_LIB_NOT_INITIALIZED')
        global CONFD_ERR_TOO_MANY_SESSIONS
        CONFD_ERR_TOO_MANY_SESSIONS = cls.addEnum('CONFD_ERR_TOO_MANY_SESSIONS')
        global CONFD_ERR_BAD_CONFIG
        CONFD_ERR_BAD_CONFIG = cls.addEnum('CONFD_ERR_BAD_CONFIG')
        global CONFD_ERR_RESOURCE_DENIED
        CONFD_ERR_RESOURCE_DENIED = cls.addEnum('CONFD_ERR_RESOURCE_DENIED')
        global CONFD_ERR_INCONSISTENT_VALUE
        CONFD_ERR_INCONSISTENT_VALUE = cls.addEnum('CONFD_ERR_INCONSISTENT_VALUE')
        global CONFD_ERR_APPLICATION_INTERNAL
        CONFD_ERR_APPLICATION_INTERNAL = cls.addEnum('CONFD_ERR_APPLICATION_INTERNAL')
        global CONFD_ERR_UNSET_CHOICE
        CONFD_ERR_UNSET_CHOICE = cls.addEnum('CONFD_ERR_UNSET_CHOICE')
        global CONFD_ERR_MUST_FAILED
        CONFD_ERR_MUST_FAILED = cls.addEnum('CONFD_ERR_MUST_FAILED')
        global CONFD_ERR_MISSING_INSTANCE
        CONFD_ERR_MISSING_INSTANCE = cls.addEnum('CONFD_ERR_MISSING_INSTANCE')
        global CONFD_ERR_INVALID_INSTANCE
        CONFD_ERR_INVALID_INSTANCE = cls.addEnum('CONFD_ERR_INVALID_INSTANCE')
        global CONFD_ERR_UNAVAILABLE
        CONFD_ERR_UNAVAILABLE = cls.addEnum('CONFD_ERR_UNAVAILABLE')
        global CONFD_ERR_EOF
        CONFD_ERR_EOF = cls.addEnum('CONFD_ERR_EOF')
        global CONFD_ERR_NOTMOVABLE
        CONFD_ERR_NOTMOVABLE = cls.addEnum('CONFD_ERR_NOTMOVABLE')
        global CONFD_ERR_HA_WITH_UPGRADE
        CONFD_ERR_HA_WITH_UPGRADE = cls.addEnum('CONFD_ERR_HA_WITH_UPGRADE')
        global CONFD_ERR_TIMEOUT
        CONFD_ERR_TIMEOUT = cls.addEnum('CONFD_ERR_TIMEOUT')
        global CONFD_ERR_ABORTED
        CONFD_ERR_ABORTED = cls.addEnum('CONFD_ERR_ABORTED')
        global CONFD_ERR_XPATH
        CONFD_ERR_XPATH = cls.addEnum('CONFD_ERR_XPATH')
        global CONFD_ERR_NOT_IMPLEMENTED
        CONFD_ERR_NOT_IMPLEMENTED = cls.addEnum('CONFD_ERR_NOT_IMPLEMENTED')
        global CONFD_ERR_HA_BADVSN
        CONFD_ERR_HA_BADVSN = cls.addEnum('CONFD_ERR_HA_BADVSN')
        global CONFD_ERR_POLICY_FAILED
        CONFD_ERR_POLICY_FAILED = cls.addEnum('CONFD_ERR_POLICY_FAILED')
        global CONFD_ERR_POLICY_COMPILATION_FAILED
        CONFD_ERR_POLICY_COMPILATION_FAILED = cls.addEnum('CONFD_ERR_POLICY_COMPILATION_FAILED')
        global CONFD_ERR_POLICY_EVALUATION_FAILED
        CONFD_ERR_POLICY_EVALUATION_FAILED = cls.addEnum('CONFD_ERR_POLICY_EVALUATION_FAILED')
        global CONFD_ERR_START_FAILED
        CONFD_ERR_START_FAILED = cls.addEnum('CONFD_ERR_START_FAILED')

# confd_vtype values
class ConfdVtype(PyEnum):
    @classmethod
    def add (cls):
        global C_NOEXISTS
        C_NOEXISTS = cls.addEnum('C_NOEXISTS')
        global C_XMLTAG
        C_XMLTAG = cls.addEnum('C_XMLTAG')
        global C_SYMBOL
        C_SYMBOL = cls.addEnum('C_SYMBOL')
        global C_STR
        C_STR = cls.addEnum('C_STR')
        global C_BUF
        C_BUF = cls.addEnum('C_BUF')
        global C_INT8
        C_INT8 = cls.addEnum('C_INT8')
        global C_INT16
        C_INT16 = cls.addEnum('C_INT16')
        global C_INT32
        C_INT32 = cls.addEnum('C_INT32')
        global C_INT64
        C_INT64 = cls.addEnum('C_INT64')
        global C_UINT8
        C_UINT8 = cls.addEnum('C_UINT8')
        global C_UINT16
        C_UINT16 = cls.addEnum('C_UINT16')
        global C_UINT32
        C_UINT32 = cls.addEnum('C_UINT32')
        global C_UINT64
        C_UINT64 = cls.addEnum('C_UINT64')
        global C_DOUBLE
        C_DOUBLE = cls.addEnum('C_DOUBLE')
        global C_IPV4
        C_IPV4 = cls.addEnum('C_IPV4')
        global C_IPV6
        C_IPV6 = cls.addEnum('C_IPV6')
        global C_BOOL
        C_BOOL = cls.addEnum('C_BOOL')
        global C_QNAME
        C_QNAME = cls.addEnum('C_QNAME')
        global C_DATETIME
        C_DATETIME = cls.addEnum('C_DATETIME')
        global C_DATE
        C_DATE = cls.addEnum('C_DATE')
        global C_GYEARMONTH
        C_TIME = cls.addEnum('C_TIME')
        global C_GDAY
        C_DURATION = cls.addEnum('C_DURATION')
        global C_ENUM_HASH
        C_ENUM_HASH = cls.addEnum('C_ENUM_HASH')
        global C_BIT32
        C_BIT32 = cls.addEnum('C_BIT32')
        global C_BIT64
        C_BIT64 = cls.addEnum('C_BIT64')
        global C_LIST
        C_LIST = cls.addEnum('C_LIST')
        global C_XMLBEGIN
        C_XMLBEGIN = cls.addEnum('C_XMLBEGIN')
        global C_XMLEND
        C_XMLEND = cls.addEnum('C_XMLEND')
        global C_OBJECTREF
        C_OBJECTREF = cls.addEnum('C_OBJECTREF')
        global C_UNION
        C_UNION = cls.addEnum('C_UNION')
        global C_PTR
        C_PTR = cls.addEnum('C_PTR')
        global C_CDBBEGIN
        C_CDBBEGIN = cls.addEnum('C_CDBBEGIN')
        global C_OID
        C_OID = cls.addEnum('C_OID')
        global C_BINARY
        C_BINARY = cls.addEnum('C_BINARY')
        global C_IPV4PREFIX
        C_IPV4PREFIX = cls.addEnum('C_IPV4PREFIX')
        global C_IPV6PREFIX
        C_IPV6PREFIX = cls.addEnum('C_IPV6PREFIX')
        global C_DEFAULT
        C_DEFAULT = cls.addEnum('C_DEFAULT')
        global C_DECIMAL64
        C_DECIMAL64 = cls.addEnum('C_DECIMAL64')
        global C_IDENTITYREF
        C_IDENTITYREF = cls.addEnum('C_IDENTITYREF')
        global C_MAXTYPE
        C_MAXTYPE = cls.addEnum('C_MAXTYPE')


# enum confd_debug_level
class ConfdDebugLevel(PyEnum):
    @classmethod
    def add (cls):
        global CONFD_SILENT
        CONFD_SILENT      = cls.addEnum('CONFD_SILENT')
        global CONFD_DEBUG
        CONFD_DEBUG       = cls.addEnum('CONFD_DEBUG')
        global CONFD_TRACE
        CONFD_TRACE       = cls.addEnum('CONFD_TRACE')
        global CONFD_PROTO_TRACE
        CONFD_PROTO_TRACE = cls.addEnum('CONFD_PROTO_TRACE')

# enum cdb_sock_type
class CdbSockType(PyEnum):
    @classmethod
    def add (cls):
        global CDB_READ_SOCKET
        CDB_READ_SOCKET         = cls.addEnum('CDB_READ_SOCKET')
        global CDB_SUBSCRIPTION_SOCKET
        CDB_SUBSCRIPTION_SOCKET = cls.addEnum('CDB_SUBSCRIPTION_SOCKET')
        global CDB_DATA_SOCKET
        CDB_DATA_SOCKET         = cls.addEnum('CDB_DATA_SOCKET')

# enum cdb_db_type
class CdbDbType(PyEnum):
    @classmethod
    def add (cls):
        global CDB_RUNNING
        CDB_RUNNING            = cls.addEnum('CDB_RUNNING')
        global CDB_STARTUP
        CDB_STARTUP            = cls.addEnum('CDB_STARTUP')
        global CDB_OPERATIONAL
        CDB_OPERATIONAL        = cls.addEnum('CDB_OPERATIONAL')
        global CDB_PRE_COMMIT_RUNNING
        CDB_PRE_COMMIT_RUNNING = cls.addEnum('CDB_PRE_COMMIT_RUNNING')

# enum confd_iter_ret
class ConfdIterRet(PyEnum):
    @classmethod
    def add (cls):
        global ITER_STOP
        ITER_STOP     = cls.addEnum('ITER_STOP')
        global ITER_RECURSE
        ITER_RECURSE  = cls.addEnum('ITER_RECURSE')
        global ITER_CONTINUE
        ITER_CONTINUE = cls.addEnum('ITER_CONTINUE')
        global ITER_SUSPEND
        ITER_SUSPEND  = cls.addEnum('ITER_SUSPEND')
        global ITER_UP
        ITER_UP = cls.addEnum('ITER_UP')

# enum confd_iter_op and cdb_iter_op
class ConfdIterOp(PyEnum):
    @classmethod
    def add (cls):
        global MOP_CREATED
        MOP_CREATED     = cls.addEnum('MOP_CREATED')
        global MOP_DELETED
        MOP_DELETED     = cls.addEnum('MOP_DELETED')
        global MOP_MODIFIED
        MOP_MODIFIED    = cls.addEnum('MOP_MODIFIED')
        global MOP_VALUE_SET
        MOP_VALUE_SET   = cls.addEnum('MOP_VALUE_SET')
        global MOP_MOVED_AFTER
        MOP_MOVED_AFTER = cls.addEnum('MOP_MOVED_AFTER')
        global MOP_ATTR_SET
        MOP_ATTR_SET    = cls.addEnum('MOP_ATTR_SET')  # maapi_diff_iterate() only

# enum confd_iter_flags and cdb_iter_flags
# TODO(orens): Create a class PyBitFlags, inheriting from PyEnum, that allows bit-manipulations.
# Or maybe not, because it is not KISS
# Until then, application will use getValue() and '|' on these enums
class ConfdIterFlags(PyEnum):
    @classmethod
    def add (cls):
        global ITER_WANT_PREV
        ITER_WANT_PREV            = cls.addEnum('ITER_WANT_PREV')
        global ITER_WANT_ANCESTOR_DELETE
        ITER_WANT_ANCESTOR_DELETE = cls.addEnum('ITER_WANT_ANCESTOR_DELETE')
        global ITER_WANT_ATTR
        ITER_WANT_ATTR            = cls.addEnum('ITER_WANT_ATTR')
        global ITER_WANT_CLI_STR
        ITER_WANT_CLI_STR         = cls.addEnum('ITER_WANT_CLI_STR')
        global ITER_WANT_SCHEMA_ORDER
        ITER_WANT_SCHEMA_ORDER    = cls.addEnum('ITER_WANT_SCHEMA_ORDER')

# enum cdb_sub_type
class CdbSubType(PyEnum):
    @classmethod
    def add (cls):
        global CDB_SUB_RUNNING
        CDB_SUB_RUNNING           = cls.addEnum('CDB_SUB_RUNNING')
        global CDB_SUB_RUNNING_TWOPHASE
        CDB_SUB_RUNNING_TWOPHASE  = cls.addEnum('CDB_SUB_RUNNING_TWOPHASE')
        global CDB_SUB_OPERATIONAL
        CDB_SUB_OPERATIONAL       = cls.addEnum('CDB_SUB_OPERATIONAL')

# enum cdb_sub_notification
class CdbSubNotification(PyEnum):
    @classmethod
    def add (cls):
        global CDB_SUB_PREPARE
        CDB_SUB_PREPARE    = cls.addEnum('CDB_SUB_PREPARE')
        global CDB_SUB_COMMIT
        CDB_SUB_COMMIT      = cls.addEnum('CDB_SUB_COMMIT')
        global CDB_SUB_ABORT
        CDB_SUB_ABORT = cls.addEnum('CDB_SUB_ABORT')
        global CDB_SUB_OPER
        CDB_SUB_OPER = cls.addEnum('CDB_SUB_OPER')

# enum cdb_subscription_sync_type
class CdbSubscriptionSyncType(PyEnum):
    @classmethod
    def add (cls):
        global CDB_DONE_PRIORITY
        CDB_DONE_PRIORITY    = cls.addEnum('CDB_DONE_PRIORITY')
        global CDB_DONE_SOCKET
        CDB_DONE_SOCKET      = cls.addEnum('CDB_DONE_SOCKET')
        global CDB_DONE_TRANSACTION
        CDB_DONE_TRANSACTION = cls.addEnum('CDB_DONE_TRANSACTION')
        global CDB_DONE_OPERATIONAL
        CDB_DONE_OPERATIONAL = cls.addEnum('CDB_DONE_OPERATIONAL')

# enum confd_sock_type 
class ConfdSockType(PyEnum):
    @classmethod
    def add (cls):
        global CONTROL_SOCKET
        CONTROL_SOCKET = cls.addEnum('CONTROL_SOCKET')
        global WORKER_SOCKET
        WORKER_SOCKET  = cls.addEnum('WORKER_SOCKET')

# enum confd_proto 
class ConfdProto(PyEnum):
    @classmethod
    def add (cls):
        global CONFD_PROTO_UNKNOWN
        CONFD_PROTO_UNKNOWN = cls.addEnum('CONFD_PROTO_UNKNOWN')
        global CONFD_PROTO_TCP
        CONFD_PROTO_TCP = cls.addEnum('CONFD_PROTO_TCP')
        global CONFD_PROTO_SSH
        CONFD_PROTO_SSH = cls.addEnum('CONFD_PROTO_SSH')
        global CONFD_PROTO_SYSTEM
        CONFD_PROTO_SYSTEM = cls.addEnum('CONFD_PROTO_SYSTEM')
        global CONFD_PROTO_CONSOLE
        CONFD_PROTO_CONSOLE = cls.addEnum('CONFD_PROTO_CONSOLE')
        global CONFD_PROTO_SSL
        CONFD_PROTO_SSL = cls.addEnum('CONFD_PROTO_SSL')
        global CONFD_PROTO_HTTP
        CONFD_PROTO_HTTP = cls.addEnum('CONFD_PROTO_HTTP')
        global CONFD_PROTO_HTTPS
        CONFD_PROTO_HTTPS = cls.addEnum('CONFD_PROTO_HTTPS')
        global CONFD_PROTO_UDP
        CONFD_PROTO_UDP = cls.addEnum('CONFD_PROTO_UDP')

# enum confd_dbname 
class ConfdDbName(PyEnum):
    @classmethod
    def add (cls):
        global CONFD_NO_DB
        CONFD_NO_DB = cls.addEnum('CONFD_NO_DB')
        global CONFD_CANDIDATE
        CONFD_CANDIDATE = cls.addEnum('CONFD_CANDIDATE')
        global CONFD_RUNNING
        CONFD_RUNNING = cls.addEnum('CONFD_RUNNING')
        global CONFD_STARTUP
        CONFD_STARTUP = cls.addEnum('CONFD_STARTUP')
        global CONFD_OPERATIONAL
        CONFD_OPERATIONAL = cls.addEnum('CONFD_OPERATIONAL')

# enum confd_trans_mode 
class ConfdTransMode(PyEnum):
    @classmethod
    def add (cls):
        global CONFD_READ
        CONFD_READ = cls.addEnum('CONFD_READ')
        global CONFD_READ_WRITE
        CONFD_READ_WRITE = cls.addEnum('CONFD_READ_WRITE')

# enum confd_errcode 
class ConfdErrcode(PyEnum):
    @classmethod
    def add (cls):
        global CONFD_ERRCODE_IN_USE
        CONFD_ERRCODE_IN_USE = cls.addEnum('CONFD_ERRCODE_IN_USE')
        global CONFD_ERRCODE_RESOURCE_DENIED
        CONFD_ERRCODE_RESOURCE_DENIED = cls.addEnum('CONFD_ERRCODE_RESOURCE_DENIED')
        global CONFD_ERRCODE_INCONSISTENT_VALUE
        CONFD_ERRCODE_INCONSISTENT_VALUE = cls.addEnum('CONFD_ERRCODE_INCONSISTENT_VALUE')
        global CONFD_ERRCODE_ACCESS_DENIED
        CONFD_ERRCODE_ACCESS_DENIED = cls.addEnum('CONFD_ERRCODE_ACCESS_DENIED')
        global CONFD_ERRCODE_APPLICATION
        CONFD_ERRCODE_APPLICATION = cls.addEnum('CONFD_ERRCODE_APPLICATION')
        global CONFD_ERRCODE_APPLICATION_INTERNAL
        CONFD_ERRCODE_APPLICATION_INTERNAL = cls.addEnum('CONFD_ERRCODE_APPLICATION_INTERNAL')
        global CONFD_ERRCODE_PROTO_USAGE
        CONFD_ERRCODE_PROTO_USAGE = cls.addEnum('CONFD_ERRCODE_PROTO_USAGE')
        global CONFD_ERRCODE_INTERNAL
        CONFD_ERRCODE_INTERNAL = cls.addEnum('CONFD_ERRCODE_INTERNAL')

# enum maapi_delete_how
class MaapiDeleteHow(PyEnum):
    @classmethod
    def add (cls):
        global MAAPI_DEL_SAFE
        MAAPI_DEL_SAFE = cls.addEnum('MAAPI_DEL_SAFE')
        global MAAPI_DEL_ALL
        MAAPI_DEL_ALL = cls.addEnum('MAAPI_DEL_ALL')
        global MAAPI_DEL_EXPORTED
        MAAPI_DEL_EXPORTED = cls.addEnum('MAAPI_DEL_EXPORTED')

# temp for 2.6 - support oper strings
def py_strdup (val):
    return libcDll.strdup(val)

def py_free (ptr):
    libcDll.free(ptr)

# Utility funcs
#===================

def checkTypes(dict):
    """
    Given a dictionary, checks that each key is an instance of the class specified as it's value
    If value is a single item, then key must be of that class
    If value is a list, key should be of one of the classes

    Returns True if OK, False if error
    """
    for key in dict :
        value=dict[key]
        if isinstance (value, list):
            for cls in value:
                if isinstance(key, cls):
                    return True
            # Not an instance of any of the classes in the list ?
            for logFunc in _log("check-types").errorFunc(): logFunc("key %s is not an instance of %s, it is an instance of %s ", key, join(map(str, value)), type(key))
            return False
        else:
            if isinstance(key, value):
                return True
            else:
                for logFunc in _log("check-types").errorFunc(): logFunc("key %s is not an instance of %s, it is an instance of %s ", key, value, type(key))
                return False

def hashIfString (value):
    if isinstance(value, str):
        return strToHash(value)
    return value


# Various C types we need to use
#===================================

# A ctypes type for confd_value_t
# Dummy class to represent a confd_value_t. The list of fields is dummy,
# we do this just to make ctypes let us define a pointer to this struct,
# so that we can properly describe the C functions getting a confd_value_t*
# with a proper unique type, so that ctypes will detect the common error of 
# using the wrong pointer type
class ConfdValueT(ctypes.Structure):
    _fields_ = [("dummy", ctypes.c_int)]

# A ctypes type for confd_hkeypath_t
class ConfdHkeypathT(ctypes.Structure):
    _fields_ = [("dummy", ctypes.c_int)]

# A ctypes type for xml_tag
class XmlTagT(ctypes.Structure):
    _fields_ = [("dummy", ctypes.c_int)]

# A ctypes type for confd_tag_value_t
class ConfdTagValueT(ctypes.Structure):
    _fields_ = [("dummy", ctypes.c_int)]

# A ctypes type for confd_snmp_varbind
class ConfdSnmpVarbind(ctypes.Structure):
    _fields_ = [("dummy", ctypes.c_int)]

# A ctypes type for struct confd_notification_ctx
class ConfdNotificationCtxStruct(ctypes.Structure):
    _fields_ = [("dummy", ctypes.c_int)]

# A ctypes type for struct confd_daemon_ctx
class ConfdDaemonCtxStruct(ctypes.Structure):
    _fields_ = [("dummy", ctypes.c_int)]

# A class for holding a pointer to struct confd_daemon_ctx and some data
class ConfdDaemonCtx:
    def __init__(self, ptr):
        self._myPtr=ptr
        self._myDontGc=[]

    def __str__ (self):
        if self._myPtr:
            return "daemon %d" % (self.getDaemonId())

    def _fatalIfNull (self):
        if not self._myPtr:
            msg="ConfdDaemonCtx: I have a NULL pointer, sorry"
            for logFunc in _log("confd-daemon-context-null").errorFunc(): logFunc(msg)
            a.infra.process.processFatal(msg)

    def getPtr (self):
        return self._myPtr

    def getDaemonId (self):
        self._fatalIfNull()
        daemonId=dll.py_getConfdDaemonCtxDaemonId(self._myPtr)
        for logFunc in _log("getdaemonid-called").debug4Func(): logFunc("Got daemonId %s", daemonId)
        return daemonId

    def getDaemonName (self):
        self._fatalIfNull()
        daemonName=dll.py_getConfdDaemonCtxDaemonName(self._myPtr)
        for logFunc in _log("getdaemonname-called").debug4Func(): logFunc("Got daemonName %s", daemonName)
        return daemonName

    def dontGcMe (self, obj):
        """Call this when some object needs to be protected against being garbage-collected during the life of this context"""
        self._myDontGc.append(obj)


class ContextMappings(object):

    def __init__ (self):
        self._mapping = {}
        self._lock = threading.Lock()

    def storeObject (self, objId, obj):
        #self._lock.acquire()
        if objId in self._mapping.keys():
            self._mapping[objId]['refCount'] += 1
        else:
            self._mapping[objId] = {'object' : obj, 'refCount' : 1}
        #self._lock.release()

    def getObject (self, objId):
        obj = None
        #self._lock.acquire()
        if objId in self._mapping.keys():
            obj = self._mapping[objId]['object']
        #self._lock.release()
        return obj

    def removeMapping (self, objId):
        #self._lock.acquire()
        if objId in self._mapping.keys():
            self._mapping[objId]['refCount'] -= 1
            if self._mapping[objId]['refCount'] == 0:
                del self._mapping[objId]
        #self._lock.release()

# A ctypes type for struct confd_trans_ctx
class ConfdTransCtx(ctypes.Structure):
    _fields_ = [("dummy", ctypes.c_int)]

class ConfdTransContext:
    """ 
    A Wrapper for a struct confd_trans_ctx*. 
    Never owns the wrapped struct (Until we see sample for user code that needs to allocate such a struct)
    """

    def __init__ (self, confdTransCtxPtr):
        self._myConfdTransCtxPtr=confdTransCtxPtr

    def __str__ (self):
        return ("transaction-handle=%s, mode=%s" % (dll.py_getConfdTransCtxTransHandle(self._myConfdTransCtxPtr), dll.py_getConfdTransCtxTMode(self._myConfdTransCtxPtr)))

    def getUserContext (self):
        self._fatalIfNull()
        userContext=dll.py_getConfdTransCtxUserContext(self._myConfdTransCtxPtr)
        for logFunc in _log("getusercontext-called").debug4Func(): logFunc("Got user context %s", userContext)
        return userContext

    def getFd (self):
        self._fatalIfNull()
        fd=dll.py_getConfdTransCtxTFd(self._myConfdTransCtxPtr)
        for logFunc in _log("getfd-called").debug4Func(): logFunc("Got fd %s", fd)
        return fd

    def getMode (self):
        self._fatalIfNull()
        mode=dll.py_getConfdTransCtxTMode(self._myConfdTransCtxPtr)
        for logFunc in _log("getmode-called").debug4Func(): logFunc("Got mode %s", mode)
        return mode

    def getDaemonId (self):
        self._fatalIfNull()
        daemonCtx=dll.py_getConfdTransCtxTDaemonCtx(self._myConfdTransCtxPtr)
        if not daemonCtx:
            for logFunc in _log("get-daemon-id-null-ctx").errorFunc(): logFunc("Got NULL daemon context")
            return -1
        daemonCtxObj = ConfdDaemonCtx(daemonCtx)
        for logFunc in _log("get-daemon-id-called").debug4Func(): logFunc("Got daemonId=%s", daemonCtxObj.getDaemonId())
        return daemonCtxObj.getDaemonId()

    def getTransHandle (self):
        self._fatalIfNull()
        handle=dll.py_getConfdTransCtxTransHandle(self._myConfdTransCtxPtr)
        for logFunc in _log("gettranshandle-called").debug4Func(): logFunc("Got trans handle %s", handle)
        return handle

    def getTransOpaque (self):
        self._fatalIfNull()
        objId=dll.py_getConfdTransCtxTOpaque(self._myConfdTransCtxPtr)
        for logFunc in _log("gettransopaque-called").debug4Func(): logFunc("Got objId %s", objId)
        res = contextMapping.getObject(objId)
        if res:
            return res
        for logFunc in _log("confd-trans-context-null").errorFunc(): logFunc("ConfdTransContext.getTransOpaque(): I have a NULL pointer, sorry")
        a.infra.process.processFatal("ConfdTransContext.getTransOpaque(): I have a NULL pointer, sorry")

    def setTransOpaque (self, obj):
        self._fatalIfNull()
        objId=id(obj)
        contextMapping.storeObject(objId, obj)
        for logFunc in _log("settransopaque-called").debug4Func(): logFunc("Setting obj %s, id=%s in tctx %s", obj, objId, self._myConfdTransCtxPtr)
        dll.py_setConfdTransCtxTOpaque(self._myConfdTransCtxPtr, objId)

    def freeTransOpaque (self):
        objId=dll.py_getConfdTransCtxTOpaque(self._myConfdTransCtxPtr)
        for logFunc in _log("freetransopaque-called").debug4Func(): logFunc("Freeing obj %s", objId)
        contextMapping.removeMapping(objId)

    def getCtypePtr (self):
        """Provides a lower-level access to the internal pointer"""
        self._fatalIfNull()
        return self._myConfdTransCtxPtr

    def _fatalIfNull (self):
        if not self._myConfdTransCtxPtr:
            msg="ConfdTransContext: I have a NULL pointer, sorry"
            for logFunc in _log("confd-trans-context-null").errorFunc(): logFunc(msg)
            a.infra.process.processFatal(msg)

# A ctypes type for struct confd_trans_ctx
class ConfdUserInfo(ctypes.Structure):
    _fields_ = [("dummy", ctypes.c_int)]

class ConfdUserInfoCtx:
    """ 
    A Wrapper for a struct confd_user_info*. 
    Never owns the wrapped struct (Until we see sample for user code that needs to allocate such a struct)
    """
    def __init__ (self, confdUserInfoPtr):
        self._myConfdUserInfoPtr=confdUserInfoPtr

    def __str__ (self):
        return ("user-session0id=%s" % dll.py_getConfdUserInfoUserSessionId(self._myConfdUserInfoPtr))

    def getFd (self):
        self._fatalIfNull()
        fd=dll.py_getConfdUserInfoFd(self._myConfdUserInfoPtr)
        for logFunc in _log("getfd-called").debug4Func(): logFunc("Got fd %s", fd)
        return fd

    def getDaemonCtx (self):
        self._fatalIfNull()
        daemonCtx=dll.py_getConfdUserInfoDaemonCtx(self._myConfdUserInfoPtr)
        for logFunc in _log("get-daemon-ctx-called").debug4Func(): logFunc("Got daemon ctx %s", daemonCtx)
        return daemonCtx

    def getUserSessionId (self):
        self._fatalIfNull()
        userSessionId=dll.py_getConfdUserInfoUserSessionId(self._myConfdUserInfoPtr)
        for logFunc in _log("get-user-session-id-called").debug4Func(): logFunc("Got user session id %s", userSessionId)
        return userSessionId

    def getOpaque (self):
        self._fatalIfNull()
        objId=dll.py_getConfdUserInfoOpaque(self._myConfdUserInfoPtr)
        for logFunc in _log("getopaque-called").debug4Func(): logFunc("Got objId %s", objId)
        res = contextMapping.getObject(objId)
        if res:
            return res
        for logFunc in _log("confd-opaque-null").errorFunc(): logFunc("ConfdUserInfo.getOpaque(): I have a NULL pointer, sorry")
        a.infra.process.processFatal("ConfdUserInfo.getOpaque(): I have a NULL pointer, sorry")

    def setOpaque (self, obj):
        self._fatalIfNull()
        objId=id(obj)
        contextMapping.storeObject(objId, obj)
        for logFunc in _log("setopaque-called").debug4Func(): logFunc("Setting obj %s, id=%s in tctx %s", obj, objId, self._myConfdUserInfoPtr)
        dll.py_setConfdUserInfoOpaque(self._myConfdUserInfoPtr, objId)

    def freeOpaque (self):
        objId=dll.py_getConfdTransCtxTOpaque(self._myConfdUserInfoPtr)
        for logFunc in _log("freeopaque-called").debug4Func(): logFunc("Freeing obj %s", objId)
        contextMapping.removeMapping(objId)

    def getCtypePtr (self):
        """Provides a lower-level access to the internal pointer"""
        self._fatalIfNull()
        return self._myConfdUserInfoPtr

    def _fatalIfNull (self):
        if not self._myConfdUserInfoPtr:
            msg="ConfdUserInfoCtx: I have a NULL pointer, sorry"
            for logFunc in _log("confd-user-info-ctx-null").errorFunc(): logFunc(msg)
            a.infra.process.processFatal(msg)


# A ctypes type for struct maapi_cursor
class MaapiCursorT(ctypes.Structure):
    _fields_ = [("dummy", ctypes.c_int)]
        
# Functions for the user code, not wrapping confd functions
#==============================================

def strToHash (str_):
    """
    Used by application to convert a string to a hashed value. Caches values for efficiency.
    """
    ret=None
    hashedStringsLock.acquire()
    if str_ in hashedStrings:
        ret=hashedStrings[str_]
        for logFunc in _log("strtohash-from-cache").debug4Func(): logFunc("Returning %s for str %s from cache", ret, str_)
    else:
        ret=confd_str2hash(str_)
        hashedStrings[str_]=ret
        for logFunc in _log("strtohash-updated-cache").debug4Func(): logFunc("Added %s for str %s to cache", ret, str_)
    hashedStringsLock.release()
    return ret

def nsToPrefix (ns):
    """
    Used by application to convert a hashed value to a namespace prefix string. Caches values for efficiency.
    """
    ret=None
    stringHashedLock.acquire()
    if ns in prefixStringsHashed:
        ret=prefixStringsHashed[ns]
        #for logFunc in _log("hashtostr-from-cache").debug4Func(): logFunc("Returning %s for ns %d from cache", ret, ns)
    else:
        ret=confd_ns2prefix(ns)
        prefixStringsHashed[ns]=copy.deepcopy(ret)
        #for logFunc in _log("hashtostr-updated-cache").debug4Func(): logFunc("Added %s for ns %d to cache", ret, ns)
    stringHashedLock.release()
    return ret

def hashToStr (hash_):
    """
    Used by application to convert a hashed value to a string. Caches values for efficiency.
    """
    ret=None
    stringHashedLock.acquire()
    if hash_ in stringsHashed:
        ret=stringsHashed[hash_]
        for logFunc in _log("hashtostr-from-cache").debug4Func(): logFunc("Returning %s for hash %d from cache", ret, hash_)
    else:
        ret=confd_hash2str(hash_)
        stringsHashed[hash_]=copy.deepcopy(ret)
        for logFunc in _log("hashtostr-updated-cache").debug4Func(): logFunc("Added %s for hash %d to cache", ret, hash_)
    stringHashedLock.release()
    return ret

def get_confd_errno ():
    return dll.py_getConfdErrno()

# From here on are wrapped confd functions
#===========================================

def confd_strerror (confd_errno):
    buf=dll.py_confd_strerror(confd_errno)
    return str(buf)

def confd_lasterr ():
    buf=dll.py_confd_lasterr()
    return str(buf)

def confd_init(name, debugLevel):
    checkTypes({name: str, debugLevel : ConfdDebugLevel})
    dll.py_confd_init(name, debugLevel.getValue())

def confd_init_daemon(name):
    checkTypes({name: str})
    dctx=dll.py_confd_init_daemon(name)
    if not dctx:
        for logFunc in _log("confd-init-daemon-bad").errorFunc(): logFunc("confd_init_daemon() returned NULL")
    return ConfdDaemonCtx(dctx)

def confd_str2hash(str_):
    if not checkTypes({str_: str}):
        return -1
    return dll.py_confd_str2hash(str_)

def confd_hash2str (hash_):
    if not checkTypes({hash_: [int, long]}):
        return -1
    return dll.py_confd_hash2str(hash_)

def confd_ns2prefix (ns_):
    if not checkTypes({ns_: [int, long]}):
        return -1
    return dll.py_confd_ns2prefix(ns_)

def confd_load_schemas(addrFamily, ipAddress, port):
    if not checkTypes({addrFamily : AddressFamily, ipAddress : str, port : int}):
        return CONFD_BAD_PYTHON_USAGE
    return dll.py_confd_load_schemas(addrFamily.getValue(), ipAddress, port)

def confd_connect(dctx, sock, sockType, addrFamily, ipAddress, port):
    if not checkTypes({dctx : ConfdDaemonCtx, sock : socket.socket, sockType: ConfdSockType, addrFamily : AddressFamily, 
                      ipAddress : str, port : int}):
        return CONFD_BAD_PYTHON_USAGE
    return dll.py_confd_connect(dctx.getPtr(), sock.fileno(), sockType.getValue(), addrFamily.getValue(), ipAddress, port)

def confd_trans_seterr (tctx, error):
    checkTypes({tctx: ConfdTransContext , error: str})
    dll.py_confd_trans_seterr(tctx.getCtypePtr(), error)

def confd_action_seterr (userInfo, error):
    checkTypes({userInfo: ConfdUserInfoCtx, error: str})
    dll.py_confd_action_seterr(userInfo.getCtypePtr(), error)

def confd_register_snmp_notification (dx, fd, notifyName, ctxName, nctx):
    checkTypes({dx: ConfdDaemonCtx, fd: socket.socket, notifyName: str, ctxName: str})
    return dll.py_confd_register_snmp_notification(dx.getPtr(), fd.fileno(), notifyName, ctxName, nctx)


def confd_register_trans_cb(dctx, initCb=0, transLockCb=0, finishCb=0, callBackData=None):
    class CbWrapper:
        """
        A wrapper for the python callbacks supplied by the application.
        Wraps each value supplied by confd with a proper Python type, checks return type   
        """
        def __init__(self, callback, callBackData):
            self.callBack=callback
            self.callBackData=callBackData
        @exceptionGuard
        def func (self, tctx):
            ret=self.callBack(ConfdTransContext(tctx), self.callBackData)
            checkTypes({ret : ConfdReturnCode})
            return ret.getValue()

    class TransactionFinisher:
        """
        Wraps finish() methods to free objects stored by ConfdTransContext::setTransOpaque()
        """
        def __init__ (self, finishCb):
            self.finishCb = finishCb

        def func (self, tctx, callBackData):
            if self.finishCb==0:
                ret=CONFD_OK
            else:
                ret=self.finishCb(tctx, callBackData)
            tctx.freeTransOpaque()
            return ret


    if not checkTypes({dctx : ConfdDaemonCtx}):
        return CONFD_BAD_PYTHON_USAGE

    # TODO(orens) check that callbacks are indeed callable

    wrapper=0 # By default, we register a NULL function pointer
    if initCb != 0:
        wrapper=CbWrapper(initCb, callBackData).func
    initPtr=ConfdTransFuncType(wrapper)
    dctx.dontGcMe(initPtr)  # Protect against GC as long as this context is alive

    wrapper=0
    if transLockCb != 0:
        wrapper=CbWrapper(transLockCb, callBackData).func
    transLockPtr=ConfdTransFuncType(wrapper)
    dctx.dontGcMe(transLockPtr)

    # The finish callback is special, we call it through the TransactionFinisher object so that any
    # t_opaque objects stored by the user are freed. So, we always register a call-back, even if the user did not supply any
    wrapper=CbWrapper(TransactionFinisher(finishCb).func, callBackData).func
    finishPtr=ConfdTransFuncType(wrapper)
    dctx.dontGcMe(finishPtr)

    #with ConfdLibGuard("py_confd_register_trans_cb"):
        #return dll.py_confd_register_trans_cb(dctx.getPtr(), initPtr, transLockPtr, finishPtr)
    return dll.py_confd_register_trans_cb(dctx.getPtr(), initPtr, transLockPtr, finishPtr)

def confd_register_validate_cb(dctx, initCb=0, stopCb=0, callBackData=None):
    class CbWrapper:
        """
        A wrapper for the python callbacks supplied by the application.
        Wraps each value supplied by confd with a proper Python type, checks return type   
        """
        def __init__(self, callback, callBackData):
            self.callBack=callback
            self.callBackData=callBackData
        @exceptionGuard
        def func (self, tctx):
            ret=self.callBack(ConfdTransContext(tctx), self.callBackData)
            checkTypes({ret : ConfdReturnCode})
            return ret.getValue()

    class TransactionStopper:
        """
        Wraps stop() methods to free objects stored by ConfdTransContext::setTransOpaque()
        """
        def __init__ (self, stopCb):
            self.stopCb = stopCb
        def func (self, tctx, callBackData):
            if self.stopCb==0:
                ret=CONFD_OK
            else:
                ret=self.stopCb(tctx, callBackData)
            tctx.freeTransOpaque()
            return ret


    if not checkTypes({dctx : ConfdDaemonCtx}):
        return CONFD_BAD_PYTHON_USAGE

    # TODO(orens) check that callbacks are indeed callable

    wrapper=0 # By default, we register a NULL function pointer
    if initCb != 0:
        wrapper=CbWrapper(initCb, callBackData).func
    initPtr=ConfdTransValidateFuncType(wrapper)
    dctx.dontGcMe(initPtr)  # Protect against GC as long as this context is alive

    # The finish callback is special, we call it through the TransactionFinisher object so that any
    # t_opaque objects stored by the user are freed. So, we always register a call-back, even if the user did not supply any
    wrapper=CbWrapper(TransactionStopper(stopCb).func, callBackData).func
    stopPtr=ConfdTransValidateFuncType(wrapper)
    dctx.dontGcMe(stopPtr)

    #with ConfdLibGuard("py_confd_register_trans_validate_cb"):
        #return dll.py_confd_register_trans_validate_cb(dctx.getPtr(), initPtr, transLockPtr, finishPtr)
    return dll.py_confd_register_trans_validate_cb(dctx.getPtr(), initPtr, stopPtr)

def confd_register_done(dctx):
    if not checkTypes({dctx : ConfdDaemonCtx}):
        return CONFD_BAD_PYTHON_USAGE
    return dll.py_confd_register_done(dctx.getPtr())

def confd_release_daemon(dctx):
    if not checkTypes({dctx : ConfdDaemonCtx}):
        return CONFD_BAD_PYTHON_USAGE
    return dll.py_confd_release_daemon(dctx.getPtr())

def confd_fd_ready(dctx, fd):
    if not checkTypes({dctx : ConfdDaemonCtx, fd : int}):
        return CONFD_BAD_PYTHON_USAGE
    for logFunc in _log("confd-fd-ready").debug3Func(): logFunc("called. fd=%d", fd)
    return dll.py_confd_fd_ready(dctx.getPtr(), fd)

def confd_trans_set_fd(tctx, fd):
    if not checkTypes({tctx : ConfdTransContext, fd : int}):
        return CONFD_BAD_PYTHON_USAGE
    dll.py_confd_trans_set_fd(tctx.getCtypePtr(), fd)

def confd_action_set_fd(userInfo, fd):
    if not checkTypes({userInfo : ConfdUserInfoCtx, fd : int}):
        return CONFD_BAD_PYTHON_USAGE
    dll.py_confd_action_set_fd(userInfo.getCtypePtr(), fd)

def confd_data_reply_not_found(tctx):
    if not checkTypes({tctx : ConfdTransContext}):
        return CONFD_BAD_PYTHON_USAGE

    return dll.py_confd_data_reply_not_found(tctx.getCtypePtr())

def confd_action_reply_values_empty (userInfo):
    """
    calls confd_action_reply_values with no values
    """

    if not checkTypes({userInfo: ConfdUserInfoCtx}):
        return CONFD_BAD_PYTHON_USAGE

    return dll.py_confd_action_reply_values_empty(userInfo.getCtypePtr())

def cdb_connect(sock, sockType, addrFamily, ipAddress, port):
    if not checkTypes({sock : socket.socket, sockType : CdbSockType, addrFamily : AddressFamily, ipAddress : str, port : int}):
        return CONFD_BAD_PYTHON_USAGE

    return dll.py_cdb_connect(sock.fileno(), sockType.getValue(), addrFamily.getValue(), ipAddress, port)

def cdb_subscribe(sock, priority, argNspace, fmt):
    """ Returns a tuple: (rc, value of subscription point) """
    """ Returns value of subscription point """
    if not checkTypes({sock : socket.socket, priority : int, argNspace : [int, str], fmt : str}):
        return (CONFD_BAD_PYTHON_USAGE, -1)

    nspace=hashIfString(argNspace)
    spoint=Int64Type()
    rc=dll.py_cdb_subscribe(sock.fileno(), priority, nspace, ctypes.byref(spoint), fmt)
    return (rc, spoint.value)

def cdb_subscribe2(sock, subType, flags, priority, argNspace, fmt):
    """ Returns a tuple: (rc, value of subscription point) """
    if not checkTypes({sock : socket.socket, subType : CdbSubType, flags : int, priority : int, argNspace : [int, str], fmt : str}):
        return (CONFD_BAD_PYTHON_USAGE, -1)

    nspace=hashIfString(argNspace)
    spoint=Int64Type()
    for logFunc in _log("cdb-subscribe-2-called").debug2Func(): logFunc("py_cdb_subscribe2(sock=%s, subType=%s, priority=%s, argNspace=%s, nspace=%s, fmt=%s)",
                                          sock.fileno(), subType, priority, argNspace, nspace, fmt)
    rc=dll.py_cdb_subscribe2(sock.fileno(), subType.getValue(), flags, priority, ctypes.byref(spoint), nspace, fmt)
    return (rc, spoint.value)

def cdb_subscribe_done(sock):
    if not checkTypes({sock : socket.socket}):
        return CONFD_BAD_PYTHON_USAGE

    return dll.py_cdb_subscribe_done(sock.fileno())

def cdb_start_session(sock, db):
    if not checkTypes({sock : socket.socket, db : CdbDbType}):
        return CONFD_BAD_PYTHON_USAGE

    return dll.py_cdb_start_session(Int64Type(sock.fileno()), Int64Type(db.getValue()))

def cdb_start_session2(sock, db, flags):
    """For flags, use .getValue() and do a logical or """
    if not checkTypes({sock : socket.socket, db : CdbDbType, flags : int}):
        return CONFD_BAD_PYTHON_USAGE

    for logFunc in _log("cdb-start-session2-called").debug2Func(): logFunc("cdb_start_session2(sock=%s) called, db=%s, flags=%s", sock.fileno(), db, flags)
    rc=dll.py_cdb_start_session2(Int64Type(sock.fileno()), Int64Type(db.getValue()), Int64Type(flags))
    for logFunc in _log("cdb-start-session2-done").debug2Func(): logFunc("cdb_start_session2() done, rc=%s", rc)
    return rc

def cdb_end_session(sock):
    if not checkTypes({sock : socket.socket}):
        return CONFD_BAD_PYTHON_USAGE

    return dll.py_cdb_end_session(Int64Type(sock.fileno()))

def cdb_read_subscription_socket(sock):
    """
    Returns a tuple with 2 elements:
    - return code (If != CONFD_OK, next value is an empty list)
    - list of subscription points
    """
    if not checkTypes({sock : socket.socket}):
        return (CONFD_BAD_PYTHON_USAGE, [])

    maxSubPoints=ctypes.c_int.in_dll(dll, "cdb_active_subscriptions")
    subPoints=(Int64Type * maxSubPoints.value)()
    resultLen=Int64Type()
    for logFunc in _log("cdb-read-subscription-socket-called").debug2Func(): logFunc("cdb_read_subscription_socket(sock=%s) called", sock.fileno())
    rc=dll.py_cdb_read_subscription_socket(sock.fileno(), subPoints, ctypes.byref(resultLen))
    if rc != CONFD_OK:
        for logFunc in _log("cdb_read_subscription_socket-error").errorFunc(): logFunc("cdb_read_subscription_socket() got rc=%s", rc)
        return(rc,[])
    for logFunc in _log("cdb-read-subscription-socket-called").debug2Func(): logFunc("cdb_read_subscription_socket() got resultLen %s", resultLen)
    ret=subPoints[0:resultLen.value]
    return (rc,ret)

def cdb_read_subscription_socket2(sock):
    """
    Returns a tuple with 4 elements:
    - return code (If != CONFD_OK, next 3 values are invalid)
    - list of subscription points
    - type of subscription points 
    - flags
    """
    if not checkTypes({sock : socket.socket}):
        return (CONFD_BAD_PYTHON_USAGE,[],None,0)

    maxSubPoints=100
    subPoints=(Int64Type * maxSubPoints)()
    type_=Int64Type()
    flags=Int64Type()
    resultLen=Int64Type()
    for logFunc in _log("cdb_read_subscription_socket2-called").debug2Func(): logFunc("cdb_read_subscription_socket2(sock=%s) called", sock.fileno())
    rc=dll.py_cdb_read_subscription_socket2(sock.fileno(), ctypes.byref(type_), ctypes.byref(flags), 
                                            subPoints, maxSubPoints, ctypes.byref(resultLen))
    if rc != CONFD_OK:
        for logFunc in _log("cdb_read_subscription_socket2-error").errorFunc(): logFunc("cdb_read_subscription_socket2() got rc=%s", rc)
        return(rc,[],None,0)
    # Now we know that rc is OK
    for logFunc in _log("cdb_read_subscription_socket2-good").debug2Func(): logFunc("cdb_read_subscription_socket2() got resultLen %s", resultLen)
    retPoints=subPoints[0:resultLen.value]
    typeFrog=CdbSubNotification.getByValue(type_.value)
    if typeFrog==None:
        for logFunc in _log("cdb_read_subscription_socket2-bad-type").errorFunc(): logFunc("cdb_read_subscription_socket2() got type_.value=%s, not a value type", type_.value)
        a.infra.process.processFatal("cdb_read_subscription_socket2() got type_.value=%s, not a value type" % type_.value)
    return (rc, retPoints, typeFrog, flags.value)

def cdb_sub_abort_trans (sock, code, apptag_ns, apptag_tag, fmt):
    if not checkTypes({sock : socket.socket, code : ConfdErrcode, apptag_ns : int, apptag_tag : int, fmt : str}):
        return CONFD_BAD_PYTHON_USAGE

    return dll.py_cdb_sub_abort_trans(sock.fileno(), code.getValue(), apptag_ns, apptag_tag, fmt)

def cdb_sync_subscription_socket(sock, cdbSubscriptionSyncTypePy):
    if not checkTypes({sock : socket.socket, cdbSubscriptionSyncTypePy : CdbSubscriptionSyncType}):
        return CONFD_BAD_PYTHON_USAGE

    return dll.py_cdb_sync_subscription_socket(sock.fileno(), cdbSubscriptionSyncTypePy.getValue())

def cdb_trigger_subscriptions(sock, sub_points):
    if not checkTypes({sock : socket.socket}):
        return CONFD_BAD_PYTHON_USAGE

    subPoints=(Int64Type * len(sub_points))()
    for index in range(len(sub_points)):
        subPoints[index] = sub_points[index]
    return dll.py_cdb_trigger_subscriptions(sock.fileno(), subPoints, len(sub_points))

def cdb_set_namespace(sock, argNspace):
    if not checkTypes({sock : socket.socket, argNspace : [int, str]}):
        return CONFD_BAD_PYTHON_USAGE

    nspace=hashIfString(argNspace)
    return dll.py_cdb_set_namespace(sock.fileno(), nspace)

def cdb_cd(sock, fmt):
    if not checkTypes({sock : socket.socket, fmt : str}):
        return CONFD_BAD_PYTHON_USAGE

    return dll.py_cdb_cd(sock.fileno(), fmt)

def cdb_num_instances(sock, fmt):
    """
    Returns an integer holding the number of instances. 
    To detect errors, check if <0, or compare to specific values like this:  

        if pyconfdlib.cdb_num_instances() == pyconfdlib.CONFD_ERR.getValue():
            <error-handling code>
    """
    if not checkTypes({sock : socket.socket, fmt : str}):
        return CONFD_BAD_PYTHON_USAGE

    num=dll.py_cdb_num_instances(sock.fileno(), fmt)
    return num

def cdb_get_str(sock, fmt):
    """Returns a tuple: (rc, string from the CDB)"""
    if not checkTypes({sock : socket.socket, fmt : str}):
        return (CONFD_BAD_PYTHON_USAGE, "")

    buf=ctypes.create_string_buffer(kMaxStringSize)
    rc=dll.py_cdb_get_str(sock.fileno(), buf, ctypes.sizeof(buf), fmt)
    # todo(orens): If string is too long, use cdb_get() to get it
    #if (rc==CONFD_ERR) and (dll.get_confd_errno() == CONFD_ERR_PROTOUSAGE):
    #    value=cdb_get(sock, fmt)
    #    something
    return (rc, buf.value)

def cdb_get_int64(sock, fmt):
    """Returns a tuple: (rc, int64 from the CDB)"""
    if not checkTypes({sock : socket.socket, fmt : str}):
        return (CONFD_BAD_PYTHON_USAGE, 0)

    value=Int64Type()
    rc=dll.py_cdb_get_int64(sock.fileno(), ctypes.byref(value), fmt)
    return (rc, value.value)

def maapi_connect(sock, addrFamily, ipAddress, port):
    if not checkTypes({sock : socket.socket, addrFamily : AddressFamily, ipAddress : str, port : int}):
        return CONFD_BAD_PYTHON_USAGE

    return dll.py_maapi_connect(sock.fileno(), addrFamily.getValue(), ipAddress, port)

def maapi_attach(sock, ns, tctx):
    if not checkTypes({sock : socket.socket, ns : int, tctx: ConfdTransContext}):
        return CONFD_BAD_PYTHON_USAGE

    return dll.py_maapi_attach(sock.fileno(), ns, tctx.getCtypePtr())

def maapi_detach(sock, tctx):
    if not checkTypes({sock : socket.socket, tctx: ConfdTransContext}):
        return CONFD_BAD_PYTHON_USAGE

    return dll.py_maapi_detach(sock.fileno(), tctx.getCtypePtr())

def maapi_reload_config(sock):
    if not checkTypes({sock : socket.socket}):
        return CONFD_BAD_PYTHON_USAGE

    return dll.py_maapi_reload_config(sock.fileno())

def maapi_wait_start(sock, phase):
    if not checkTypes({sock : socket.socket, phase : int}):
        return CONFD_BAD_PYTHON_USAGE

    return dll.py_maapi_wait_start(sock.fileno(), phase)

def maapi_load_schemas(sock):
    if not checkTypes({sock : socket.socket}):
        return CONFD_BAD_PYTHON_USAGE

    return dll.py_maapi_load_schemas(sock.fileno())

def maapi_close(sock):
    if not checkTypes({sock : socket.socket}):
        return CONFD_BAD_PYTHON_USAGE

    return dll.py_maapi_close(sock.fileno())

def maapi_start_user_session(sock, username, context, groups, srcAddrFamily, srcIpAddr, prot):
    """
    groups : A list of groups that the user participates in
    """
    if not checkTypes({sock : socket.socket, context: str, srcAddrFamily : AddressFamily, srcIpAddr : str, prot : ConfdProto}):
        return CONFD_BAD_PYTHON_USAGE

    groupsLen=len(groups)
    groupPointers=None
    if groupsLen:
        for logFunc in _log("maapi_start_user_session-called").debug2Func(): logFunc("maapi_start_user_session() called: groupsLen=%s", groupsLen)
        if groupsLen == 0:
            msg="maapi_start_user_session() groups must be non-empty"
            for logFunc in _log("maapi_start_user_session-bad-groups").errorFunc(): logFunc(msg)
            a.infra.process.processFatal(msg)
        groupPointers=(ctypes.c_char_p * groupsLen)();
        for i in range(0, groupsLen):
            groupPointers[i]=ctypes.cast(ctypes.create_string_buffer(groups[i]), ctypes.c_char_p)
    return dll.py_maapi_start_user_session(sock.fileno(), username, context, groupPointers, groupsLen, 
                                           srcAddrFamily.getValue(), srcIpAddr, prot.getValue())

def maapi_end_user_session (sock):
    if not checkTypes({sock : socket.socket}):
        return CONFD_BAD_PYTHON_USAGE

    return dll.py_maapi_end_user_session(sock.fileno())


def maapi_delete_config(sock, dbName):
    if not checkTypes({sock : socket.socket, dbName : ConfdDbName}):
        return CONFD_BAD_PYTHON_USAGE

    return dll.py_maapi_delete_config(sock.fileno(), dbName.getValue())

def maapi_start_trans(sock, dbName, transMode):
    """
    Returns thandle, which should be supplied to all other maapi transaction functions

    To detect errors, check if <0, or compare to specific values like this:  

        if pyconfdlib.maapi_start_trans() == pyconfdlib.CONFD_ERR.getValue():
            <error-handling code>
    """
    if not checkTypes({sock : socket.socket, dbName : ConfdDbName, transMode : ConfdTransMode}):
        return CONFD_BAD_PYTHON_USAGE

    thandle=dll.py_maapi_start_trans(sock.fileno(), dbName.getValue(), transMode.getValue())
    return thandle

def maapi_apply_trans(sock, thandle, keepOpen):
    if not checkTypes({sock : socket.socket, thandle : int, keepOpen : int}):
        return CONFD_BAD_PYTHON_USAGE

    return dll.py_maapi_apply_trans(sock.fileno(), thandle, keepOpen)

def maapi_finish_trans(sock, thandle):
    if not checkTypes({sock : socket.socket, thandle : int}):
        return CONFD_BAD_PYTHON_USAGE

    return dll.py_maapi_finish_trans(sock.fileno(), thandle)

def maapi_set_namespace(sock, thandle, argNspace):
    if not checkTypes({sock : socket.socket, thandle : int, argNspace : [int, str]}):
        return CONFD_BAD_PYTHON_USAGE

    nspace=hashIfString(argNspace)
    return dll.py_maapi_set_namespace(sock.fileno(), thandle, nspace)

def maapi_num_instances(sock, thandle, fmt):
    """
    Returns an integer holding the number of instances. 
    To detect errors, check if <0, or compare to specific values like this:  

        if pyconfdlib.maapi_num_instances() == pyconfdlib.CONFD_ERR.getValue():
            <error-handling code>
    """
    if not checkTypes({sock : socket.socket, thandle : int, fmt : str}):
        return CONFD_BAD_PYTHON_USAGE

    return dll.py_maapi_num_instances(sock.fileno(), thandle, fmt)

def maapi_create(sock, thandle, fmt):
    if not checkTypes({sock : socket.socket, thandle : int, fmt : str}):
        return CONFD_BAD_PYTHON_USAGE

    return dll.py_maapi_create(sock.fileno(), thandle, fmt)

def maapi_delete(sock, thandle, fmt):
    if not checkTypes({sock : socket.socket, thandle : int, fmt : str}):
        return CONFD_BAD_PYTHON_USAGE

    return dll.py_maapi_delete(sock.fileno(), thandle, fmt)

def maapi_delete_all(sock, thandle, how):
    if not checkTypes({sock : socket.socket, thandle : int, how : MaapiDeleteHow}):
        return CONFD_BAD_PYTHON_USAGE

    return dll.py_maapi_delete_all(sock.fileno(), thandle, how.getValue())

def maapi_get_enum_hash_elem (sock, thandle, fmt):
    """Returns a tuple: (rc, enumValue)"""
    if not checkTypes({sock : socket.socket, thandle : int, fmt : str}):
        return (CONFD_BAD_PYTHON_USAGE, "")

    value=Int32Type()
    rc=dll.py_maapi_get_enum_hash_elem(sock.fileno(), thandle, ctypes.byref(value), fmt)
    return (rc, value.value)

def maapi_get_str_elem(sock, thandle, fmt):
    """Returns a tuple: (rc, stringValue)"""
    if not checkTypes({sock : socket.socket, thandle : int, fmt : str}):
        return (CONFD_BAD_PYTHON_USAGE, "")

    for logFunc in _log("maapi-get-str-elem").debug2Func(): logFunc("called. sock=%s, thandle=%s, fmt=%s, fileno=%s", sock, thandle, fmt, sock.fileno())
    buf=ctypes.create_string_buffer(kMaxStringSize)
    rc=dll.py_maapi_get_str_elem(sock.fileno(), thandle, buf, ctypes.sizeof(buf), fmt)
    # todo(orens): If error, check if this is due to a too-long string. 
    # If so, use maapi_get_elem() to get it
    return (rc, buf.value)

def maapi_get_int64_elem(sock, thandle, fmt):
    """Returns a tuple: (rc, int64Value)"""
    if not checkTypes({sock : socket.socket, thandle : int, fmt : str}):
        return (CONFD_BAD_PYTHON_USAGE, 0)

    value=Int64Type()
    rc=dll.py_maapi_get_int64_elem(sock.fileno(), thandle, ctypes.byref(value), fmt)
    return (rc, value.value)

def maapi_get_uint64_elem(sock, thandle, fmt):
    """Returns a tuple: (rc, uint64Value)"""
    if not checkTypes({sock : socket.socket, thandle : int, fmt : str}):
        return (CONFD_BAD_PYTHON_USAGE, 0)

    value=Uint64Type()
    rc=dll.py_maapi_get_uint64_elem(sock.fileno(), thandle, ctypes.byref(value), fmt)
    return (rc, value.value)

def maapi_get_int8_elem(sock, thandle, fmt):
    """Returns a tuple: (rc, int8Value)"""
    if not checkTypes({sock : socket.socket, thandle : int, fmt : str}):
        return (CONFD_BAD_PYTHON_USAGE, 0)

    value=Int8Type()
    rc=dll.py_maapi_get_int8_elem(sock.fileno(), thandle, ctypes.byref(value), fmt)
    return (rc, value.value)

def maapi_get_ipv4_elem(sock, thandle, fmt):
    """Returns a tuple: (rc, ipValue)"""
    if not checkTypes({sock : socket.socket, thandle : int, fmt : str}):
        return (CONFD_BAD_PYTHON_USAGE, "")

    buf=ctypes.create_string_buffer(kMaxStringSize)
    rc=dll.py_maapi_get_ipv4_elem(sock.fileno(), thandle, buf, ctypes.sizeof(buf), fmt)
    # todo(orens): change to proper IP address type
    return (rc, buf.value)

def maapi_get_ipv4prefix_elem(sock, thandle, fmt):
    """Returns a tuple: (rc, ipValue)"""
    if not checkTypes({sock : socket.socket, thandle : int, fmt : str}):
        return (CONFD_BAD_PYTHON_USAGE, "")

    buf=ctypes.create_string_buffer(kMaxStringSize)
    len_ = Uint8Type()
    rc=dll.py_maapi_get_ipv4prefix_elem(sock.fileno(), thandle, buf, ctypes.sizeof(buf), len_, fmt)
    # todo(orens): change to proper IP address type
    return (rc, (buf.value, len_.value))

def maapi_set_elem2(sock, thandle, value, fmt):
    if not checkTypes({sock : socket.socket, thandle : int, value : str, fmt : str}):
        return CONFD_BAD_PYTHON_USAGE

    return dll.py_maapi_set_elem2(sock.fileno(), thandle, value, fmt)

