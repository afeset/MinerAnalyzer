# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

import pyconfdlib
import copy, socket, struct

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

class Value(object):

    """ 
    A class representing a value. 
    It holds the actual value and its type
    """

    class ValueType(EnumWithValue):
        def __init__ (self, type, name):
            EnumWithValue.__init__(self, type, name)

    kEmpty=ValueType(0,"kEmpty")
    kString=ValueType(1,"kString")
    kBuf=ValueType(2,"kBuf")
    kInt8=ValueType(3,"kInt8")
    kInt16=ValueType(4,"kInt16")
    kInt32=ValueType(5,"kInt32")
    kInt64=ValueType(6,"kInt64")
    kUint8=ValueType(7,"kUint8")
    kUint16=ValueType(8,"kUint16")
    kUint32=ValueType(9,"kUint32")
    kUint64=ValueType(10,"kUint64")
    kBool=ValueType(11,"kBool")
    kEnum=ValueType(12,"kEnum")
    kBinary=ValueType(13,"kBinary")
    kIPv4=ValueType(14,"kIPv4")
    kIPv6=ValueType(15,"kIPv6")
    kIPv4Prefix=ValueType(16,"kIPv4Prefix")
    kIPv6Prefix=ValueType(17,"kIPv6Prefix")
    kXmlTag=ValueType(18, "kXmlTag")
    kXmlBegin=ValueType(19, "kXmlBegin")
    kXmlEnd=ValueType(20, "kXmlEnd")
    kBinary=ValueType(21, "kBinary")
    kOid=ValueType(38, "kOid")
    """
    kEmpty=ValueType(pyconfdlib.C_NOEXISTS,"kEmpty")
    kString=ValueType(pyconfdlib.C_STR,"kString")
    kBuf=ValueType(pyconfdlib.C_BUF,"kBuf")
    kInt8=ValueType(pyconfdlib.C_INT8,"kInt8")
    kInt16=ValueType(pyconfdlib.C_INT16,"kInt16")
    kInt32=ValueType(pyconfdlib.C_INT32,"kInt32")
    kInt64=ValueType(pyconfdlib.C_INT64,"kInt64")
    kUint8=ValueType(pyconfdlib.C_UINT8,"kUint8")
    kUint16=ValueType(pyconfdlib.C_UINT16,"kUint16")
    kUint32=ValueType(pyconfdlib.C_UINT32,"kUint32")
    kUint64=ValueType(pyconfdlib.C_UINT64,"kUint64")
    kBool=ValueType(pyconfdlib.C_BOOL,"kBool")
    kEnum=ValueType(pyconfdlib.C_ENUM_HASH,"kEnum")
    kBinary=ValueType(pyconfdlib.C_BINARY,"kBinary")
    kIPv4=ValueType(pyconfdlib.C_IPV4,"kIPv4")
    kIPv6=ValueType(pyconfdlib.C_IPV6,"kIPv6")
    kIPv4Prefix=ValueType(pyconfdlib.C_IPV4PREFIX,"kIPv4Prefix")
    kIPv6Prefix=ValueType(pyconfdlib.C_IPV6PREFIX,"kIPv6Prefix")
    kXmlTag=ValueType(pyconfdlib.C_XMLTAG, "kXmlTag")
    kXmlEnd=ValueType(pyconfdlib.C_XMLEND, "kXmlEnd)
    """
    def __init__ (self):
        self._type = self.kEmpty
        self._value = None

    def setType (self, type_):
        self._type = type_

    def getType (self):
        return self._type

    def setValue (self, val):
        self._value = val

    def getValue (self):
        return self._value

    def __str__ (self):
        #"""
        #prints type & value
        #"""
        #return "%s <%s>" % (self._value, self._type)
        return ('%s: %s' % (self._type, self.getCannonicalStr()))

    def getCannonicalStr (self):
        """
        prints the value, as confd_pp_value() would have done it
        """
        if self.isXmlTag():
            return self.xmlTagAsStr()
        elif self.isBufferType():
            return self.bufferTypeAsStr()
        elif self.isIpType():
            return self.IpTypeAsStr()
        elif self.isIpPrefixType():
            return self.IpPrefixTypeAsStr()
        return str(self._value)

    def xmlTagAsStr (self):
        (tag, ns, prefix) = self._value
        return tag

    def isEqual (self, other):
        if self._type != other._type:
            return False
        if self._value != other._value:
            return False
        return True

    def isXmlTag (self):
        if self._type == self.kXmlTag:
            return True
        return False

    def isBufferType (self):
        if self._type in \
            [self.kBuf]:
            return True
        return False

    def isIpType (self):
        if self._type in \
            [self.kIPv4, self.kIPv6]:
            return True
        return False

    def isIpPrefixType (self):
        if self._type in \
            [self.kIPv4Prefix, self.kIPv6Prefix]:
            return True
        return False

    def isIp4Type (self):
        if self._type in \
            [self.kIPv4, self.kIPv4Prefix]:
            return True
        return False

    def isIp6Type (self):
        if self._type in \
            [self.kIPv6, self.kIPv6Prefix]:
            return True
        return False

    def bufferTypeAsStr (self):
        (ptr, len_)  = self._value
        return ptr

    def IpTypeAsStr (self):
        if self.isIp6Type():
            return socket.inet_ntop(socket.AF_INET6, self._value)
        return socket.inet_ntop(socket.AF_INET, struct.pack('!L', self._value))

    def IpPrefixTypeAsStr (self):
        (ip, prefix) = self._value
        if self.isIp6Type():
            ipStr = socket.inet_ntop(socket.AF_INET6, ip)
        else:
            ipStr = socket.inet_ntop(socket.AF_INET, struct.pack('!L', ip))
        return "%s/%d" % (ipStr, prefix)

    def setEmpty (self):
        self._type = self.kEmpty
        self._value = None

    def isEmpty (self):
        return self._type == self.kEmpty

    def setString (self, value):
        self._value = value
        self._type = self.kString

    def asString (self):
        if self._type and self._type == self.kString:
            return self._value
        buf = self.asBuf()
        if buf:
            return buf[0]
        else:
            return None

    def setBuf (self, value):
        self._value = value
        self._type = self.kBuf

    def asBuf (self):
        if self._type and self._type == self.kBuf:
            return self._value
        return None

    def setInt8 (self, value):
        self._value = value
        self._type = self.kInt8

    def asInt8 (self):
        if self._type and self._type == self.kInt8:
            return self._value
        return None

    def setInt16 (self, value):
        self._value = value
        self._type = self.kInt16

    def asInt16 (self):
        if self._type and self._type == self.kInt16:
            return self._value
        return None

    def setInt32 (self, value):
        self._value = value
        self._type = self.kInt32

    def asInt32 (self):
        if self._type and self._type == self.kInt32:
            return self._value
        return None

    def setInt64 (self, value):
        self._value = value
        self._type = self.kInt64

    def asInt64 (self):
        if self._type and self._type == self.kInt64:
            return self._value
        return None

    def setUint8 (self, value):
        self._value = value
        self._type = self.kUint8

    def asUint8 (self):
        if self._type and self._type == self.kUint8:
            return self._value
        return None

    def setUint16 (self, value):
        self._value = value
        self._type = self.kUint16

    def asUint16 (self):
        if self._type and self._type == self.kUint16:
            return self._value
        return None

    def setUint32 (self, value):
        self._value = value
        self._type = self.kUint32

    def asUint32 (self):
        if self._type and self._type == self.kUint32:
            return self._value
        return None

    def setUint64 (self, value):
        self._value = value
        self._type = self.kUint64

    def asUint64 (self):
        if self._type and self._type == self.kUint64:
            return self._value
        return None

    def setIPv4 (self, value):
        self._value = value
        self._type = self.kIPv4

    def asIPv4 (self):
        if self._type and self._type == self.kIPv4:
            return self._value
        return None

    def setIPv6 (self, value):
        self._value = value
        self._type = self.kIPv6

    def asIPv6 (self):
        if self._type and self._type == self.kIPv6:
            return self._value
        return None

    def setBool (self, value):
        self._value = value
        self._type = self.kBool

    def asBool (self):
        if self._type and self._type == self.kBool:
            return self._value
        return None

    def setEnum (self, value):
        self._value = value
        self._type = self.kEnum

    def asEnum (self):
        if self._type and self._type == self.kEnum:
            return self._value
        return None

    def setBinary (self, value):
        self._value = value
        self._type = self.kBinary

    def asBinary (self):
        if self._type and self._type == self.kBinary:
            return self._value
        return None

    def setOid (self, value):
        self._value = value
        self._type = self.kOid

    def asOid (self):
        if self._type and self._type == self.kOid:
            return self._value
        return None

    def setIPv4Prefix (self, value):
        self._value = value
        self._type = self.kIPv4Prefix

    def asIPv4Prefix (self):
        if self._type and self._type == self.kIPv4Prefix:
            return self._value
        return None

    def setIPv6Prefix (self, value):
        self._value = value
        self._type = self.kIPv6Prefix

    def asIPv6Prefix (self):
        if self._type and self._type == self.kIPv6Prefix:
            return self._value
        return None

    def setXmlTag (self, value):
        self._value = value
        self._type = self.kXmlTag

    def asXmlTag (self):
        if self._type and self._type == self.kXmlTag:
            return self._value
        return None

    def setXmlBegin (self, value):
        self._value = value
        self._type = self.kXmlBegin

    def asXmlBegin (self):
        if self._type and self._type == self.kXmlBegin:
            return self._value
        return None

    def setXmlEnd (self, value):
        self._value = value
        self._type = self.kXmlEnd

    def asXmlEnd (self):
        if self._type and self._type == self.kXmlEnd:
            return self._value
        return None

class ConfdValueLow(object):

    @staticmethod
    def allocConfdValue (numOfValues=1):
        confdValuePtr = pyconfdlib.dll.py_allocConfdValue(numOfValues)
        for logFunc in pyconfdlib._log("alloc-confd-value").debug4Func(): logFunc("allocConfdValue called. numOfValues=%d, confdValuePtr=%s", numOfValues, str(confdValuePtr))
        return confdValuePtr

    @staticmethod
    def deallocConfdValue (confdValuePtr):
        for logFunc in pyconfdlib._log("dealloc-confd-value").debug4Func(): logFunc("deallocConfdValue called. confdValuePtr=%s", str(confdValuePtr))
        pyconfdlib.dll.py_deallocConfdValue(confdValuePtr)

    @staticmethod
    def ConfdValueToStr (confdValuePtr):
        if not confdValuePtr:
            return "(NULL)"
        buf=pyconfdlib.createStringBuffer(pyconfdlib.kMaxStringSize)
        len_=pyconfdlib.dll.py_confd_pp_value(buf, pyconfdlib.sizeof(buf), confdValuePtr, 0)
        if len_ >= pyconfdlib.sizeof(buf):
            buf=pyconfdlib.createStringBuffer(len_+1)
            len_=pyconfdlib.dll.py_confd_pp_value(buf, pyconfdlib.sizeof(buf), confdValuePtr, 0)
        return buf.value[:len_]

    @staticmethod
    def getConfdValueType (confdValuePtr):
        return pyconfdlib.dll.py_get_confd_value_type(confdValuePtr)

    @staticmethod
    def shallowConvertPyValueToConfdValue (pyValue, confdValuePtr, confdValIndex=0):
        """
        This function performs a shallow convertion of a python Value object to a confd_value_t object.
        It does not reallocate data memory, merely sets the confd_value_t members to point to it.
        confdValuePtr must be pre-allocated
        Note: When using this function the it is MANDATORY for the python Value object to exist as long as the confd_value_t object exists
        Note 2: DO NOT!!! activate confd_free_value on the confd_value_t object filled by this function as it is not responsible for any allocated memory
        """
        for logFunc in pyconfdlib._log("shallow-convert-pyvalue-to-confd-value").debug3Func(): logFunc("shallowConvertPyValueToConfdValue called. pyValue=%s, confdValuePtr=%s, confdValIndex=%d", pyValue, str(confdValuePtr), confdValIndex)
        if not pyValue or not confdValuePtr:
            for logFunc in pyconfdlib._log("shallow-convert-pyvalue-to-confd-value-invalid-args").errorFunc(): logFunc("shallowConvertPyValueToConfdValue invalid args: pyValue=%s, confdValuePtr=%s", pyValue, str(confdValuePtr))
            return ReturnCodes.kGeneralError

        type_ = pyValue.getType()

        if (type_ == Value.kEmpty):
            pyconfdlib.dll.py_CONFD_SET_NOEXISTS(confdValuePtr, confdValIndex)
        elif (type_ == Value.kString):
            pyconfdlib.dll.py_CONFD_SET_STR(confdValuePtr, confdValIndex, pyValue._value)
        elif (type_ == Value.kBuf):
            (buf, len_) = pyValue._value
            pyconfdlib.dll.py_CONFD_SET_BUF(confdValuePtr, confdValIndex, buf, len_)
        elif (type_ == Value.kInt8):
            pyconfdlib.dll.py_CONFD_SET_INT8(confdValuePtr, confdValIndex, pyValue._value)
        elif (type_ == Value.kInt16):
            pyconfdlib.dll.py_CONFD_SET_INT16(confdValuePtr, confdValIndex, pyValue._value)
        elif (type_ == Value.kInt32):
            pyconfdlib.dll.py_CONFD_SET_INT32(confdValuePtr, confdValIndex, pyValue._value)
        elif (type_ == Value.kInt64):
            pyconfdlib.dll.py_CONFD_SET_INT64(confdValuePtr, confdValIndex, pyValue._value)
        elif (type_ == Value.kUint8):
            pyconfdlib.dll.py_CONFD_SET_UINT8(confdValuePtr, confdValIndex, pyValue._value)
        elif (type_ == Value.kUint16):
            pyconfdlib.dll.py_CONFD_SET_UINT16(confdValuePtr, confdValIndex, pyValue._value)
        elif (type_ == Value.kUint32):
            pyconfdlib.dll.py_CONFD_SET_UINT32(confdValuePtr, confdValIndex, pyValue._value)
        elif (type_ == Value.kUint64):
            pyconfdlib.dll.py_CONFD_SET_UINT64(confdValuePtr, confdValIndex, pyValue._value)
        elif (type_ == Value.kBool):
            boolVal = 0
            if pyValue._value:
                boolVal = 1
            pyconfdlib.dll.py_CONFD_SET_BOOL(confdValuePtr, confdValIndex, boolVal)
        elif (type_ == Value.kEnum):
            pyconfdlib.dll.py_CONFD_SET_ENUM_HASH(confdValuePtr, confdValIndex, pyValue._value)
        elif (type_ == Value.kBinary):
            buf = pyValue._value
            pyconfdlib.dll.py_CONFD_SET_BINARY(confdValuePtr, confdValIndex, buf, len(buf))
        elif (type_ == Value.kIPv4):
            pyconfdlib.dll.py_CONFD_SET_IPV4(confdValuePtr, confdValIndex, pyValue._value)
        elif (type_ == Value.kIPv6):
            pyconfdlib.dll.py_CONFD_SET_IPV6(confdValuePtr, confdValIndex, pyValue._value)
        elif (type_ == Value.kIPv4Prefix):
            (address, len_) = pyValue._value
            pyconfdlib.dll.py_CONFD_SET_IPV4_PREFIX(confdValuePtr, confdValIndex, address, len_)
        elif (type_ == Value.kIPv6Prefix):
            (address, len_) = pyValue._value
            pyconfdlib.dll.py_CONFD_SET_IPV6_PREFIX(confdValuePtr, confdValIndex, address, len_)
        elif (type_ == Value.kXmlTag):
            (tag, ns, prefix) = pyValue._value
            hashedTag=pyconfdlib.hashIfString(tag)
            hashedNs=pyconfdlib.hashIfString(ns)
            pyconfdlib.dll.py_CONFD_SET_XMLTAG(confdValuePtr, confdValIndex, hashedTag, hashedNs)
        elif (type_ == Value.kXmlBegin):
            (tag, ns, prefix) = pyValue._value
            hashedTag=pyconfdlib.hashIfString(tag)
            hashedNs=pyconfdlib.hashIfString(ns)
            pyconfdlib.dll.py_CONFD_SET_XMLBEGIN(confdValuePtr, confdValIndex, hashedTag, hashedNs)
        elif (type_ == Value.kXmlEnd):
            (tag, ns, prefix) = pyValue._value
            hashedTag=pyconfdlib.hashIfString(tag)
            hashedNs=pyconfdlib.hashIfString(ns)
            pyconfdlib.dll.py_CONFD_SET_XMLEND(confdValuePtr, confdValIndex, hashedTag, hashedNs)
        elif (type_ == Value.kOid):
            (buf, len_) = pyValue._value
            pyconfdlib.dll.py_CONFD_SET_OID(confdValuePtr, confdValIndex, buf, len_)
        else:
            for logFunc in pyconfdlib._log("shallow-convert-pyvalue-to-confd-value-unsupported-type").errorFunc(): logFunc(
                "shallowConvertPyValueToConfdValue unsupported type: %s. pyValue=%s, confdValuePtr=%s, confdValIndex=%d", 
                type_, pyValue, str(confdValuePtr), confdValIndex)
            return ReturnCodes.kGeneralError

        for logFunc in pyconfdlib._log("shallow-convert-pyvalue-to-confd-value-done").debug3Func(): logFunc("shallowConvertPyValueToConfdValue done. pyValue=%s, confdValuePtr=%s, type=%d, confdValIndex=%d",
                                                                              pyValue, ConfdValueLow.ConfdValueToStr(confdValuePtr), ConfdValueLow.getConfdValueType(confdValuePtr), confdValIndex)
        return ReturnCodes.kOk

    @staticmethod
    def deepConvertPyValueToConfdValue (pyValue, confdValuePtr, confdValIndex=0):
        """
        This function performs a deep convertion of a python Value object to a confd_value_t object.
        It reallocates data memory, making the confd_value_t object its owner.
        Note: When using this function the it is NOT mandatory for the python Value object to exist as long as the confd_value_t object exists
        Note 2: confd_free_value MUST be activated on the confd_value_t object filled by this function as it is the owner of allocated memory
        confdValuePtr must be pre-allocated
        """
        for logFunc in pyconfdlib._log("deep-convert-pyvalue-to-confd-value").debug4Func(): logFunc("deepConvertPyValueToConfdValue called. pyValue=%s, confdValuePtr=%s, confdValIndex=%d", pyValue, str(confdValuePtr), confdValIndex)
        if not pyValue or not confdValuePtr:
            for logFunc in pyconfdlib._log("deep-convert-pyvalue-to-confd-value-invalid-args").errorFunc(): logFunc("deepConvertPyValueToConfdValue invalid args: pyValue=%s, confdValuePtr=%s", pyValue, str(confdValuePtr))
            return ReturnCodes.kGeneralError

        type_ = pyValue.getType()

        if (type_ == Value.kString):
            pyconfdlib.dll.py_CONFD_SET_STR_DUP(confdValuePtr, confdValIndex, pyValue._value)
        elif (type_ == Value.kBuf):
            (buf, len_) = pyValue._value
            pyconfdlib.dll.py_CONFD_SET_BUF_DUP(confdValuePtr, confdValIndex, buf, len_)
        elif (type_ == Value.kBinary):
            pyconfdlib.dll.py_CONFD_SET_BINARY_DUP(confdValuePtr, confdValIndex, pyValue._value, len(pyValue._value))
        elif (type_ == Value.kOid):
            buf = pyValue._value
            arr = pyconfdlib.Int32ArrCreator(buf)
            pyconfdlib.dll.py_CONFD_SET_OID_DUP(confdValuePtr, confdValIndex, arr, len(buf))
        else:
            ConfdValueLow.shallowConvertPyValueToConfdValue(pyValue, confdValuePtr, confdValIndex)

        for logFunc in pyconfdlib._log("deep-convert-pyvalue-to-confd-value-done").debug4Func(): logFunc(
            "deepConvertPyValueToConfdValue done. pyValue=%s, confdValuePtr=%s, type=%d, confdValIndex=%d", 
            pyValue, ConfdValueLow.ConfdValueToStr(confdValuePtr), ConfdValueLow.getConfdValueType(confdValuePtr), confdValIndex)
        return ReturnCodes.kOk

    @staticmethod
    def deepConvertConfdValueToPyValue (confdValuePtr, pyValue, confdValIndex=0):
        """
        This function performs a deep convertion of a confd_value_t object to a python Value object.
        It reallocates data memory, making the python Value object its owner.
        Note: When using this function the it is NOT mandatory for the confd_value_t object to exist as long as the python Value object exists
        pyValue must be pre-constructed
        """
        #for logFunc in pyconfdlib._log("deep-convert-confd-value-to-pyvalue").debug4Func(): logFunc("deepConvertConfdValueToPyValue called. confdValuePtr=%s, pyValue=%s, confdValIndex=%d", ConfdValueLow.ConfdValueToStr(confdValuePtr), pyValue, confdValIndex)
        if not pyValue or not confdValuePtr:
            for logFunc in pyconfdlib._log("deep-convert-confd-value-to-pyvalue-invalid-args").errorFunc(): logFunc("deepConvertConfdValueToPyValue invalid args: confdValuePtr=%s, pyValue=%s", ConfdValueLow.ConfdValueToStr(confdValuePtr), pyValue)
            return ReturnCodes.kGeneralError
        type_ = pyconfdlib.dll.py_getValueType(confdValuePtr, confdValIndex)
        value = None
        if type_ == pyconfdlib.C_NOEXISTS:
            pyValue.setType(Value.kEmpty)
            value = None
        elif type_ == pyconfdlib.C_STR:
            pyValue.setType(Value.kString)
            strPtr=pyconfdlib.CharPType()
            rc=pyconfdlib.dll.py_CONFD_GET_STR(confdValuePtr, confdValIndex, pyconfdlib.byRef(strPtr))
            if rc != pyconfdlib.CONFD_OK:
                for logFunc in pyconfdlib._log("deep-convert-confd-value-to-pyvalue-get-str-failed").errorFunc(): logFunc("deepConvertConfdValueToPyValue py_CONFD_GET_STR() failed: confdValuePtr=%s, pyValue=%s, rc=%s", ConfdValueLow.ConfdValueToStr(confdValuePtr), pyValue, str(rc))
                return ReturnCodes.kGeneralError
            value = strPtr.value[:]
        elif type_ == pyconfdlib.C_BUF:
            pyValue.setType(Value.kBuf)
            bufPtr=pyconfdlib.CharPType()
            rc = pyconfdlib.dll.py_CONFD_GET_BUFPTR(confdValuePtr, confdValIndex, pyconfdlib.byRef(bufPtr))
            if rc != pyconfdlib.CONFD_OK:
                for logFunc in pyconfdlib._log("deep-convert-confd-value-to-pyvalue-get-bufptr-failed").errorFunc(): logFunc("deepConvertConfdValueToPyValue py_CONFD_GET_BUFPTR() failed: confdValuePtr=%s, pyValue=%s, rc=%s", ConfdValueLow.ConfdValueToStr(confdValuePtr), pyValue, str(rc))
                return ReturnCodes.kGeneralError
            bufLen = pyconfdlib.Int64Type()
            rc = pyconfdlib.dll.py_CONFD_GET_BUFSIZE(confdValuePtr, confdValIndex, pyconfdlib.byRef(bufLen))
            if rc != pyconfdlib.CONFD_OK:
                for logFunc in pyconfdlib._log("deep-convert-confd-value-to-pyvalue-get-bufsize-failed").errorFunc(): logFunc("deepConvertConfdValueToPyValue py_CONFD_GET_BUFSIZW() failed: confdValuePtr=%s, pyValue=%s, rc=%s", ConfdValueLow.ConfdValueToStr(confdValuePtr), pyValue, str(rc))
                return ReturnCodes.kGeneralError
            value = (bufPtr.value[:bufLen.value], bufLen.value)
        elif type_ == pyconfdlib.C_INT8:
            pyValue.setType(Value.kInt8)
            tempVal = pyconfdlib.Int8Type()
            rc = pyconfdlib.dll.py_CONFD_GET_INT8(confdValuePtr, confdValIndex, pyconfdlib.byRef(tempVal))
            if rc != pyconfdlib.CONFD_OK:
                for logFunc in pyconfdlib._log("deep-convert-confd-value-to-pyvalue-get-int8-failed").errorFunc(): logFunc("deepConvertConfdValueToPyValue py_CONFD_GET_INT8() failed: confdValuePtr=%s, pyValue=%s, rc=%s", ConfdValueLow.ConfdValueToStr(confdValuePtr), pyValue, str(rc))
                return ReturnCodes.kGeneralError
            value = tempVal.value
        elif type_ == pyconfdlib.C_INT16:
            pyValue.setType(Value.kInt16)
            tempVal = pyconfdlib.Int16Type()
            rc = pyconfdlib.dll.py_CONFD_GET_INT16(confdValuePtr, confdValIndex, pyconfdlib.byRef(tempVal))
            if rc != pyconfdlib.CONFD_OK:
                for logFunc in pyconfdlib._log("deep-convert-confd-value-to-pyvalue-get-int16-failed").errorFunc(): logFunc("deepConvertConfdValueToPyValue py_CONFD_GET_INT16() failed: confdValuePtr=%s, pyValue=%s, rc=%s", ConfdValueLow.ConfdValueToStr(confdValuePtr), pyValue, str(rc))
                return ReturnCodes.kGeneralError
            value = tempVal.value
        elif type_ == pyconfdlib.C_INT32:
            pyValue.setType(Value.kInt32)
            tempVal = pyconfdlib.Int32Type()
            rc = pyconfdlib.dll.py_CONFD_GET_INT32(confdValuePtr, confdValIndex, pyconfdlib.byRef(tempVal))
            if rc != pyconfdlib.CONFD_OK:
                for logFunc in pyconfdlib._log("deep-convert-confd-value-to-pyvalue-get-int32-failed").errorFunc(): logFunc("deepConvertConfdValueToPyValue py_CONFD_GET_INT32() failed: confdValuePtr=%s, pyValue=%s, rc=%s", ConfdValueLow.ConfdValueToStr(confdValuePtr), pyValue, str(rc))
                return ReturnCodes.kGeneralError
            value = tempVal.value
        elif type_ == pyconfdlib.C_INT64:
            pyValue.setType(Value.kInt64)
            tempVal = pyconfdlib.Int64Type()
            rc = pyconfdlib.dll.py_CONFD_GET_INT64(confdValuePtr, confdValIndex, pyconfdlib.byRef(tempVal))
            if rc != pyconfdlib.CONFD_OK:
                for logFunc in pyconfdlib._log("deep-convert-confd-value-to-pyvalue-get-int64-failed").errorFunc(): logFunc("deepConvertConfdValueToPyValue py_CONFD_GET_INT64() failed: confdValuePtr=%s, pyValue=%s, rc=%s", ConfdValueLow.ConfdValueToStr(confdValuePtr), pyValue, str(rc))
                return ReturnCodes.kGeneralError
            value = tempVal.value
        elif type_ == pyconfdlib.C_UINT8:
            pyValue.setType(Value.kUint8)
            tempVal = pyconfdlib.Uint8Type()
            rc = pyconfdlib.dll.py_CONFD_GET_UINT8(confdValuePtr, confdValIndex, pyconfdlib.byRef(tempVal))
            if rc != pyconfdlib.CONFD_OK:
                for logFunc in pyconfdlib._log("deep-convert-confd-value-to-pyvalue-get-uint8-failed").errorFunc(): logFunc("deepConvertConfdValueToPyValue py_CONFD_GET_UINT8() failed: confdValuePtr=%s, pyValue=%s, rc=%s", ConfdValueLow.ConfdValueToStr(confdValuePtr), pyValue, str(rc))
                return ReturnCodes.kGeneralError
            value = tempVal.value
        elif type_ == pyconfdlib.C_UINT16:
            pyValue.setType(Value.kUint16)
            tempVal = pyconfdlib.Uint16Type()
            rc = pyconfdlib.dll.py_CONFD_GET_UINT16(confdValuePtr, confdValIndex, pyconfdlib.byRef(tempVal))
            if rc != pyconfdlib.CONFD_OK:
                for logFunc in pyconfdlib._log("deep-convert-confd-value-to-pyvalue-get-uint16-failed").errorFunc(): logFunc("deepConvertConfdValueToPyValue py_CONFD_GET_UINT16() failed: confdValuePtr=%s, pyValue=%s, rc=%s", ConfdValueLow.ConfdValueToStr(confdValuePtr), pyValue, str(rc))
                return ReturnCodes.kGeneralError
            value = tempVal.value
        elif type_ == pyconfdlib.C_UINT32:
            pyValue.setType(Value.kUint32)
            tempVal = pyconfdlib.Uint32Type()
            rc = pyconfdlib.dll.py_CONFD_GET_UINT32(confdValuePtr, confdValIndex, pyconfdlib.byRef(tempVal))
            if rc != pyconfdlib.CONFD_OK:
                for logFunc in pyconfdlib._log("deep-convert-confd-value-to-pyvalue-get-uint32-failed").errorFunc(): logFunc("deepConvertConfdValueToPyValue py_CONFD_GET_UINT32() failed: confdValuePtr=%s, pyValue=%s, rc=%s", ConfdValueLow.ConfdValueToStr(confdValuePtr), pyValue, str(rc))
                return ReturnCodes.kGeneralError
            value = tempVal.value
        elif type_ == pyconfdlib.C_UINT64:
            pyValue.setType(Value.kUint64)
            tempVal = pyconfdlib.Uint64Type()
            rc = pyconfdlib.dll.py_CONFD_GET_UINT64(confdValuePtr, confdValIndex, pyconfdlib.byRef(tempVal))
            if rc != pyconfdlib.CONFD_OK:
                for logFunc in pyconfdlib._log("deep-convert-confd-value-to-pyvalue-get-uint64-failed").errorFunc(): logFunc("deepConvertConfdValueToPyValue py_CONFD_GET_UINT64() failed: confdValuePtr=%s, pyValue=%s, rc=%s", ConfdValueLow.ConfdValueToStr(confdValuePtr), pyValue, str(rc))
                return ReturnCodes.kGeneralError
            value = tempVal.value
        elif type_ == pyconfdlib.C_BOOL:
            pyValue.setType(Value.kBool)
            tempVal = pyconfdlib.Int64Type()
            rc = pyconfdlib.dll.py_CONFD_GET_BOOL(confdValuePtr, confdValIndex, pyconfdlib.byRef(tempVal))
            if rc != pyconfdlib.CONFD_OK:
                for logFunc in pyconfdlib._log("deep-convert-confd-value-to-pyvalue-get-bool-failed").errorFunc(): logFunc("deepConvertConfdValueToPyValue py_CONFD_GET_BOOL() failed: confdValuePtr=%s, pyValue=%s, rc=%s", ConfdValueLow.ConfdValueToStr(confdValuePtr), pyValue, str(rc))
                return ReturnCodes.kGeneralError
            if tempVal.value == 0:
                value = False
            else:
                value = True
        elif type_ == pyconfdlib.C_ENUM_HASH:
            pyValue.setType(Value.kEnum)
            tempVal = pyconfdlib.Int64Type()
            rc = pyconfdlib.dll.py_CONFD_GET_ENUM_HASH(confdValuePtr, confdValIndex, pyconfdlib.byRef(tempVal))
            if rc != pyconfdlib.CONFD_OK:
                for logFunc in pyconfdlib._log("deep-convert-confd-value-to-pyvalue-get-enum-hash-failed").errorFunc(): logFunc("deepConvertConfdValueToPyValue py_CONFD_GET_ENUM_HASH() failed: confdValuePtr=%s, pyValue=%s, rc=%s", ConfdValueLow.ConfdValueToStr(confdValuePtr), pyValue, str(rc))
                return ReturnCodes.kGeneralError
            value = tempVal.value
        elif type_ == pyconfdlib.C_BINARY:
            pyValue.setType(Value.kBinary)
            bufLen = pyconfdlib.Int64Type()
            rc = pyconfdlib.dll.py_CONFD_GET_BINARY_SIZE(confdValuePtr, confdValIndex, pyconfdlib.byRef(bufLen))
            if rc != pyconfdlib.CONFD_OK:
                for logFunc in pyconfdlib._log("deep-convert-confd-value-to-pyvalue-get-binary-size-failed").errorFunc(): logFunc(
                    "deepConvertConfdValueToPyValue py_CONFD_GET_BINARY_SIZE() failed: confdValuePtr=%s, pyValue=%s, rc=%s", 
                    ConfdValueLow.ConfdValueToStr(confdValuePtr), pyValue, str(rc))
                return ReturnCodes.kGeneralError
            buf=pyconfdlib.createStringBuffer(bufLen.value+1)
            rc = pyconfdlib.dll.py_CONFD_GET_BINARY_PTR_DUP(confdValuePtr, confdValIndex, bufLen.value, buf)
            if rc != pyconfdlib.CONFD_OK:
                for logFunc in pyconfdlib._log("deep-convert-confd-value-to-pyvalue-get-binary-ptr-dup-failed").errorFunc(): logFunc("deepConvertConfdValueToPyValue py_CONFD_GET_BINARY_PTR_DUP() failed: confdValuePtr=%s, pyValue=%s, rc=%s", ConfdValueLow.ConfdValueToStr(confdValuePtr), pyValue, str(rc))
                return ReturnCodes.kGeneralError
            for logFunc in pyconfdlib._log("deep-convert-confd-value-to-pyvalue-get-binary-succeeded").debug2Func(): logFunc(
                "deepConvertConfdValueToPyValue py_CONFD_BINARY...(): bufLen=%s, confdValuePtr=%s, pyValue=%s, rc=%s, len(buf.raw[:bufLen.value]=%d)", 
                bufLen.value, ConfdValueLow.ConfdValueToStr(confdValuePtr), pyValue, str(rc), len(buf.raw[:bufLen.value]))
            value = buf.raw[:bufLen.value]
        elif type_ == pyconfdlib.C_OID:
            pyValue.setType(Value.kOid)
            oidPtr=pyconfdlib.CharPType()
            rc = pyconfdlib.dll.py_CONFD_GET_OIDPTR(confdValuePtr, confdValIndex, pyconfdlib.byRef(oidPtr))
            if rc != pyconfdlib.CONFD_OK:
                for logFunc in pyconfdlib._log("deep-convert-confd-value-to-pyvalue-get-oidptr-failed").errorFunc(): logFunc("deepConvertConfdValueToPyValue py_CONFD_GET_OIDPTR() failed: confdValuePtr=%s, pyValue=%s, rc=%s", ConfdValueLow.ConfdValueToStr(confdValuePtr), pyValue, str(rc))
                return ReturnCodes.kGeneralError
            oidLen = pyconfdlib.Int64Type()
            rc = pyconfdlib.dll.py_CONFD_GET_OIDSIZE(confdValuePtr, confdValIndex, pyconfdlib.byRef(oidLen))
            if rc != pyconfdlib.CONFD_OK:
                for logFunc in pyconfdlib._log("deep-convert-confd-value-to-pyvalue-get-oidsize-failed").errorFunc(): logFunc("deepConvertConfdValueToPyValue py_CONFD_GET_OIDSIZE() failed: confdValuePtr=%s, pyValue=%s, rc=%s", ConfdValueLow.ConfdValueToStr(confdValuePtr), pyValue, str(rc))
                return ReturnCodes.kGeneralError
            value = (oidPtr.value[:oidLen.value], oidLen.value)
        elif type_ == pyconfdlib.C_IPV4:
            pyValue.setType(Value.kIPv4)
            tempVal = pyconfdlib.Uint32Type()
            rc = pyconfdlib.dll.py_CONFD_GET_IPV4(confdValuePtr, confdValIndex, pyconfdlib.byRef(tempVal))
            if rc != pyconfdlib.CONFD_OK:
                for logFunc in pyconfdlib._log("deep-convert-confd-value-to-pyvalue-get-ipv4-failed").errorFunc(): logFunc("deepConvertConfdValueToPyValue py_CONFD_GET_IPV4() failed: confdValuePtr=%s, pyValue=%s, rc=%s", ConfdValueLow.ConfdValueToStr(confdValuePtr), pyValue, str(rc))
                return ReturnCodes.kGeneralError
            value = tempVal.value
        elif type_ == pyconfdlib.C_IPV6:
            pyValue.setType(Value.kIPv6)
            bufPtr = buf=pyconfdlib.createStringBuffer(16)
            rc = pyconfdlib.dll.py_CONFD_GET_IPV6(confdValuePtr, confdValIndex, bufPtr)
            if rc != pyconfdlib.CONFD_OK:
                for logFunc in pyconfdlib._log("deep-convert-confd-value-to-pyvalue-get-ipv6-failed").errorFunc(): logFunc("deepConvertConfdValueToPyValue py_CONFD_GET_IPV6() failed: confdValuePtr=%s, pyValue=%s, rc=%s", ConfdValueLow.ConfdValueToStr(confdValuePtr), pyValue, str(rc))
                return ReturnCodes.kGeneralError
            value = bufPtr.raw
        elif type_ == pyconfdlib.C_IPV4PREFIX:
            pyValue.setType(Value.kIPv4Prefix)
            tempAddr = pyconfdlib.Uint32Type()
            tempPrefixLen = pyconfdlib.Uint8Type()
            rc = pyconfdlib.dll.py_CONFD_GET_IPV4_PREFIX(confdValuePtr, confdValIndex, pyconfdlib.byRef(tempAddr), pyconfdlib.byRef(tempPrefixLen))
            if rc != pyconfdlib.CONFD_OK:
                for logFunc in pyconfdlib._log("deep-convert-confd-value-to-pyvalue-get-ipv4-failed").errorFunc(): logFunc("deepConvertConfdValueToPyValue py_CONFD_GET_IPV4() failed: confdValuePtr=%s, pyValue=%s, rc=%s", ConfdValueLow.ConfdValueToStr(confdValuePtr), pyValue, str(rc))
                return ReturnCodes.kGeneralError
            value = (tempAddr.value, tempPrefixLen.value)
        elif type_ == pyconfdlib.C_IPV6PREFIX:
            pyValue.setType(Value.kIPv6Prefix)
            bufPtr = buf=pyconfdlib.createStringBuffer(16)
            tempPrefixLen = pyconfdlib.Uint8Type()
            rc = pyconfdlib.dll.py_CONFD_GET_IPV6_PREFIX(confdValuePtr, confdValIndex, bufPtr, pyconfdlib.byRef(tempPrefixLen))
            if rc != pyconfdlib.CONFD_OK:
                for logFunc in pyconfdlib._log("deep-convert-confd-value-to-pyvalue-get-ipv6-failed").errorFunc(): logFunc("deepConvertConfdValueToPyValue py_CONFD_GET_IPV6_PREFIX() failed: confdValuePtr=%s, pyValue=%s, rc=%s", ConfdValueLow.ConfdValueToStr(confdValuePtr), pyValue, str(rc))
                return ReturnCodes.kGeneralError
            value = (bufPtr.raw, tempPrefixLen.value)
        elif type_ == pyconfdlib.C_XMLTAG:
            pyValue.setType(Value.kXmlTag)
            tag = pyconfdlib.Int64Type()
            ns = pyconfdlib.Int64Type()
            rc = pyconfdlib.dll.py_CONFD_GET_XMLTAG(confdValuePtr, confdValIndex, pyconfdlib.byRef(tag))
            if rc != pyconfdlib.CONFD_OK:
                for logFunc in pyconfdlib._log("deep-convert-confd-value-to-pyvalue-get-xmltag-failed").errorFunc(): logFunc("deepConvertConfdValueToPyValue py_CONFD_GET_XMLTAG() failed: confdValuePtr=%s, pyValue=%s, rc=%s", ConfdValueLow.ConfdValueToStr(confdValuePtr), pyValue, str(rc))
                return ReturnCodes.kGeneralError
            rc = pyconfdlib.dll.py_CONFD_GET_XMLTAG_NS(confdValuePtr, confdValIndex, pyconfdlib.byRef(ns))
            if rc != pyconfdlib.CONFD_OK:
                for logFunc in pyconfdlib._log("deep-convert-confd-value-to-pyvalue-get-xmltag-ns-failed").errorFunc(): logFunc("deepConvertConfdValueToPyValue py_CONFD_GET_XMLTAG_NS() failed: confdValuePtr=%s, pyValue=%s, rc=%s", ConfdValueLow.ConfdValueToStr(confdValuePtr), pyValue, str(rc))
                return ReturnCodes.kGeneralError
            tagStr = pyconfdlib.hashToStr(tag.value)
            nsStr = pyconfdlib.hashToStr(ns.value)
            prefix = pyconfdlib.nsToPrefix(ns.value)
            value = (tagStr, nsStr, prefix)
        elif type_ == pyconfdlib.C_XMLBEGIN:
            pyValue.setType(Value.kXmlBegin)
            tag = pyconfdlib.Int64Type()
            ns = pyconfdlib.Int64Type()
            rc = pyconfdlib.dll.py_CONFD_GET_XMLBEGIN(confdValuePtr, confdValIndex, pyconfdlib.byRef(tag))
            if rc != pyconfdlib.CONFD_OK:
                for logFunc in pyconfdlib._log("deep-convert-confd-value-to-pyvalue-get-xmlbegin-failed").errorFunc(): logFunc("deepConvertConfdValueToPyValue py_CONFD_GET_XMLBEGIN() failed: confdValuePtr=%s, pyValue=%s, rc=%s", ConfdValueLow.ConfdValueToStr(confdValuePtr), pyValue, str(rc))
                return ReturnCodes.kGeneralError
            rc = pyconfdlib.dll.py_CONFD_GET_XMLBEGIN_NS(confdValuePtr, confdValIndex, pyconfdlib.byRef(ns))
            if rc != pyconfdlib.CONFD_OK:
                for logFunc in pyconfdlib._log("deep-convert-confd-value-to-pyvalue-get-xmlbegin-ns-failed").errorFunc(): logFunc("deepConvertConfdValueToPyValue py_CONFD_GET_XMLBEGIN_NS() failed: confdValuePtr=%s, pyValue=%s, rc=%s", ConfdValueLow.ConfdValueToStr(confdValuePtr), pyValue, str(rc))
                return ReturnCodes.kGeneralError
            tagStr = pyconfdlib.hashToStr(tag.value)
            nsStr = pyconfdlib.hashToStr(ns.value)
            prefix = pyconfdlib.nsToPrefix(ns.value)
            value = (tagStr, nsStr, prefix)
        elif type_ == pyconfdlib.C_XMLEND:
            pyValue.setType(Value.kXmlEnd)
            tag = pyconfdlib.Int64Type()
            ns = pyconfdlib.Int64Type()
            rc = pyconfdlib.dll.py_CONFD_GET_XMLEND(confdValuePtr, confdValIndex, pyconfdlib.byRef(tag))
            if rc != pyconfdlib.CONFD_OK:
                for logFunc in pyconfdlib._log("deep-convert-confd-value-to-pyvalue-get-xmlend-failed").errorFunc(): logFunc("deepConvertConfdValueToPyValue py_CONFD_GET_XMLEND() failed: confdValuePtr=%s, pyValue=%s, rc=%s", ConfdValueLow.ConfdValueToStr(confdValuePtr), pyValue, str(rc))
                return ReturnCodes.kGeneralError
            rc = pyconfdlib.dll.py_CONFD_GET_XMLEND_NS(confdValuePtr, confdValIndex, pyconfdlib.byRef(ns))
            if rc != pyconfdlib.CONFD_OK:
                for logFunc in pyconfdlib._log("deep-convert-confd-value-to-pyvalue-get-xmlend-ns-failed").errorFunc(): logFunc("deepConvertConfdValueToPyValue py_CONFD_GET_XMLEND_NS() failed: confdValuePtr=%s, pyValue=%s, rc=%s", ConfdValueLow.ConfdValueToStr(confdValuePtr), pyValue, str(rc))
                return ReturnCodes.kGeneralError
            tagStr = pyconfdlib.hashToStr(tag.value)
            nsStr = pyconfdlib.hashToStr(ns.value)
            prefix = pyconfdlib.nsToPrefix(ns.value)
            value = (tagStr, nsStr, prefix)
        else:
            for logFunc in pyconfdlib._log("deep-convert-confd-value-to-pyvalue-unsupported-type").errorFunc(): logFunc("deepConvertConfdValueToPyValue unsupported type: %s. confdValuePtr=%s, pyValue=%s, confdValIndex=%d", str(type_), ConfdValueLow.ConfdValueToStr(confdValuePtr), pyValue, confdValIndex)
            return ReturnCodes.kGeneralError

        pyValue.setValue(value)
        for logFunc in pyconfdlib._log("deep-convert-confd-value-to-pyvalue-done").debug4Func(): logFunc("deepConvertConfdValueToPyValue done. confdValuePtr=%s, pyValue=%s, confdValIndex=%d", ConfdValueLow.ConfdValueToStr(confdValuePtr), pyValue, confdValIndex)
        return ReturnCodes.kOk

