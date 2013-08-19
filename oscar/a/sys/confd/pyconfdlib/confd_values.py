import ctypes
import pyconfdlib

import a.infra.process.captain

class ConfdValues:
    """ 
    A Wrapper for a bunch of confd_value_t structs. 

    If initialized by ConfdValues(), then this object allocates a new confd_value_t object array and frees it on death.
        On death, confd_free_value() is called before the de-allocation. See the documentation of confd_free_value() for details.
    If initialized by ConfdValues(v), then v should be an existing confd_value_t, and this object does not own it.
        Thus, it is not deallocated on death, and confd_free_value() is not called for it.
    """
    def __init__ (self, confdValueTPtr=None, numValues=1):
        if confdValueTPtr is None:
            self._myValuePtr=pyconfdlib.dll.py_allocConfdValue(numValues)
            self._myIsMine=True
        else:
            self._myValuePtr=confdValueTPtr
            self._myIsMine=False
        self._mySize=numValues

    def __del__ (self):
        if self._myValuePtr and self._myIsMine:
            self.freeValues()
            pyconfdlib.dll.py_deallocConfdValue(self._myValuePtr)
            self._myValuePtr = None

    def __str__ (self):
        if not self._myValuePtr:
            return "(NULL)"
        buf=ctypes.create_string_buffer(pyconfdlib.kMaxStringSize)
        res=""
        if self._mySize > 1:
            res="["
        for i in range(0, self._mySize):
            len_=pyconfdlib.dll.py_confd_pp_value(buf, ctypes.sizeof(buf), self._myValuePtr, i)
            if len_ >= ctypes.sizeof(buf):
                buf=ctypes.create_string_buffer(len_+1)
                len_=pyconfdlib.dll.py_confd_pp_value(buf, ctypes.sizeof(buf), self._myValuePtr, i)
            if i != 0:
                res += ","
            res += buf.value[:len_]
        if self._mySize > 1:
            res += "]"
        return res


    # XML tag
    def CONFD_GET_XMLTAG (self, index=0):
        self._raiseIfNullOrBadIndex(index)
        value=pyconfdlib.Int64Type()
        pyconfdlib.dll.py_CONFD_GET_XMLTAG(self._myValuePtr, index, ctypes.byref(value))
        return value.value

    def CONFD_GET_XMLTAG_NS (self, index=0):
        self._raiseIfNullOrBadIndex(index)
        value=pyconfdlib.Int64Type()
        pyconfdlib.dll.py_CONFD_GET_XMLTAG_NS(self._myValuePtr, index, ctypes.byref(value))
        return value.value

    def CONFD_SET_XMLTAG (self, tag, ns, index=0):
        self._raiseIfNullOrBadIndex(index)
        hashedTag=pyconfdlib.hashIfString(tag)
        hashedNs=pyconfdlib.hashIfString(ns)
        pyconfdlib.dll.py_CONFD_SET_XMLTAG(self._myValuePtr, index, hashedTag, hashedNs)

    def CONFD_SET_NOEXISTS (self, index=0):
        self._raiseIfNullOrBadIndex(index)
        pyconfdlib.dll.py_CONFD_SET_NOEXISTS(self._myValuePtr, index)
        

    # Buffer and string
    def CONFD_GET_BUF (self, index=0):
        self._raiseIfNullOrBadIndex(index)
        bufPtr=ctypes.pointer(ctypes.c_char())
        pyconfdlib.dll.py_CONFD_GET_BUFPTR(self._myValuePtr, index, ctypes.cast(ctypes.byref(bufPtr), ctypes.POINTER(ctypes.c_char_p)) )
        bufSize=pyconfdlib.Int64Type()
        pyconfdlib.dll.py_CONFD_GET_BUFSIZE(self._myValuePtr, index, ctypes.byref(bufSize))
        ret=bufPtr[:bufSize.value]
        for logFunc in pyconfdlib._log("get-buf").debug4Func(): logFunc("ConfdValues.CONFD_GET_BUF(index=%s) returning %s.",index, ret)
        return ret

    def CONFD_GET_STR(self, index=0):
        self._raiseIfNullOrBadIndex(index)
        bufPtr=ctypes.c_char_p()
        pyconfdlib.dll.py_CONFD_GET_BUFPTR(self._myValuePtr, index, ctypes.byref(bufPtr))
        # Null-terminated string, ctypes does all the work by itself
        ret=bufPtr.value
        for logFunc in pyconfdlib._log("get-buf").debug4Func(): logFunc("ConfdValues.CONFD_GET_STR(index=%s) returning %s.",index, ret)
        return ret

    def CONFD_SET_STR (self, value, index=0):
        self._raiseIfNullOrBadIndex(index)
        pyconfdlib.dll.py_CONFD_SET_STR(self._myValuePtr, index, value)


    # int64
    def CONFD_GET_INT64 (self, index=0):
        self._raiseIfNullOrBadIndex(index)
        value=pyconfdlib.Int64Type()
        pyconfdlib.dll.py_CONFD_GET_INT64(self._myValuePtr, index, ctypes.byref(value))
        return value.value

    def CONFD_SET_INT64 (self, value, index=0):
        self._raiseIfNullOrBadIndex(index)
        pyconfdlib.dll.py_CONFD_SET_INT64(self._myValuePtr, index, value)

    # int32
    def CONFD_GET_INT32 (self, index=0):
        self._raiseIfNullOrBadIndex(index)
        value=pyconfdlib.Int32Type()
        pyconfdlib.dll.py_CONFD_GET_INT32(self._myValuePtr, index, ctypes.byref(value))
        return value.value

    def CONFD_SET_INT32 (self, value, index=0):
        self._raiseIfNullOrBadIndex(index)
        pyconfdlib.dll.py_CONFD_SET_INT32(self._myValuePtr, index, value)

    # int16
    def CONFD_GET_INT16 (self, index=0):
        self._raiseIfNullOrBadIndex(index)
        value=pyconfdlib.Int16Type()
        pyconfdlib.dll.py_CONFD_GET_INT16(self._myValuePtr, index, ctypes.byref(value))
        return value.value

    def CONFD_SET_INT16 (self, value, index=0):
        self._raiseIfNullOrBadIndex(index)
        pyconfdlib.dll.py_CONFD_SET_INT16(self._myValuePtr, index, value)

    # int8
    def CONFD_GET_INT8 (self, index=0):
        self._raiseIfNullOrBadIndex(index)
        value=pyconfdlib.Int8Type()
        pyconfdlib.dll.py_CONFD_GET_INT8(self._myValuePtr, index, ctypes.byref(value))
        return value.value

    def CONFD_SET_INT8 (self, value, index=0):
        self._raiseIfNullOrBadIndex(index)
        pyconfdlib.dll.py_CONFD_SET_INT8(self._myValuePtr, index, value)

    # uint64
    def CONFD_GET_UINT64 (self, index=0):
        self._raiseIfNullOrBadIndex(index)
        value=pyconfdlib.Uint64Type()
        pyconfdlib.dll.py_CONFD_GET_UINT64(self._myValuePtr, index, ctypes.byref(value))
        return value.value

    def CONFD_SET_UINT64 (self, value, index=0):
        self._raiseIfNullOrBadIndex(index)
        pyconfdlib.dll.py_CONFD_SET_UINT64(self._myValuePtr, index, value)

    # uint32
    def CONFD_GET_UINT32 (self, index=0):
        self._raiseIfNullOrBadIndex(index)
        value=pyconfdlib.Uint32Type()
        pyconfdlib.dll.py_CONFD_GET_UINT32(self._myValuePtr, index, ctypes.byref(value))
        return value.value

    def CONFD_SET_UINT32 (self, value, index=0):
        self._raiseIfNullOrBadIndex(index)
        pyconfdlib.dll.py_CONFD_SET_UINT32(self._myValuePtr, index, value)

    # uint16
    def CONFD_GET_UINT16 (self, index=0):
        self._raiseIfNullOrBadIndex(index)
        value=pyconfdlib.Uint16Type()
        pyconfdlib.dll.py_CONFD_GET_UINT16(self._myValuePtr, index, ctypes.byref(value))
        return value.value

    def CONFD_SET_UINT16 (self, value, index=0):
        self._raiseIfNullOrBadIndex(index)
        pyconfdlib.dll.py_CONFD_SET_UINT16(self._myValuePtr, index, value)

    # uint8
    def CONFD_GET_UINT8 (self, index=0):
        self._raiseIfNullOrBadIndex(index)
        value=pyconfdlib.Uint8Type()
        pyconfdlib.dll.py_CONFD_GET_UINT8(self._myValuePtr, index, ctypes.byref(value))
        return value.value

    def CONFD_SET_UINT8 (self, value, index=0):
        self._raiseIfNullOrBadIndex(index)
        pyconfdlib.dll.py_CONFD_SET_IUNT8(self._myValuePtr, index, value)


    # enum
    def CONFD_GET_ENUM_HASH (self, index=0):
        self._raiseIfNullOrBadIndex(index)
        value=pyconfdlib.Int64Type()
        pyconfdlib.dll.py_CONFD_GET_ENUM_HASH(self._myValuePtr, index, ctypes.byref(value))
        return value.value
    
    def CONFD_SET_ENUM_HASH (self, value, index=0):
        self._raiseIfNullOrBadIndex(index)
        pyconfdlib.dll.py_CONFD_SET_ENUM_HASH(self._myValuePtr, index, value)
    
            
    # bool
    def CONFD_GET_BOOL (self, index=0):
        self._raiseIfNullOrBadIndex(index)
        value=pyconfdlib.Int64Type()
        pyconfdlib.dll.py_CONFD_GET_BOOL(self._myValuePtr, index, ctypes.byref(value))
        if value.value==0:
            return False
        elif value.value==1:
            return True
        else:
            raise Exception("Bad value for boolean: "+value.value)

    def CONFD_SET_BOOL (self, value, index=0):
        self._raiseIfNullOrBadIndex(index)
        pyconfdlib.dll.py_CONFD_SET_BOOL(self._myValuePtr, index, value)


    # IP address, get/set as a dotted-decimal string
    def CONFD_GET_IPV4(self, index=0):
        # todo(orens): change to return proper IP address type
        self._raiseIfNullOrBadIndex(index)
        buf=ctypes.create_string_buffer(20)
        pyconfdlib.dll.py_CONFD_GET_IPV4(self._myValuePtr, index, buf, ctypes.sizeof(buf))
        return buf.value

    def CONFD_SET_IPV4 (self, addr, index=0):
        # todo(orens): change to get proper IP address type
        self._raiseIfNullOrBadIndex(index)
        pyconfdlib.dll.py_CONFD_SET_IPV4(self._myValuePtr, index, addr)

    def getType (self, index=0):
        self._raiseIfNullOrBadIndex(index)
        return pyconfdlib.dll.py_getValueType(self._myValuePtr, index)

    def isString (self, index=0):
        if self.getType()  == pyconfdlib.C_STR:
            return True
        return False

    def isBuf (self, index=0):
        if self.getType()  == pyconfdlib.C_BUF:
            return True
        return False

    def isInt8(self, index=0):
        if self.getType()  == pyconfdlib.C_INT8:
            return True
        return False

    def isInt16(self, index=0):
        if self.getType()  == pyconfdlib.C_INT16:
            return True
        return False

    def isInt32(self, index=0):
        if self.getType()  == pyconfdlib.C_INT32:
            return True
        return False

    def isInt64(self, index=0):
        if self.getType()  == pyconfdlib.C_INT64:
            return True
        return False

    def isUint8(self, index=0):
        if self.getType()  == pyconfdlib.C_UINT8:
            return True
        return False

    def isUint16(self, index=0):
        if self.getType()  == pyconfdlib.C_UINT16:
            return True
        return False

    def isUint32(self, index=0):
        if self.getType()  == pyconfdlib.C_UINT32:
            return True
        return False

    def isUint64(self, index=0):
        if self.getType()  == pyconfdlib.C_UINT64:
            return True
        return False

    def isDouble(self, index=0):
        if self.getType()  == pyconfdlib.C_DOUBLE:
            return True
        return False

    def isIPv4(self, index=0):
        if self.getType()  == pyconfdlib.C_IPV4:
            return True
        return False

    def isIPv6(self, index=0):
        if self.getType()  == pyconfdlib.C_IPV6:
            return True
        return False

    def isBool(self, index=0):
        if self.getType()  == pyconfdlib.C_BOOL:
            return True
        return False

    def isEnum(self, index=0):
        if self.getType()  == pyconfdlib.C_ENUM_HASH:
            return True
        return False

    def isBinary(self, index=0):
        if self.getType()  == pyconfdlib.C_BINARY:
            return True
        return False

    def isIPv4Prefix(self, index=0):
        if self.getType()  == pyconfdlib.C_IPV4PREFIX:
            return True
        return False

    def isIPv6Prefix(self, index=0):
        if self.getType()  == pyconfdlib.C_IPV6PREFIX:
            return True
        return False

    def asInt64 (self, index=0):
        self._raiseIfNullOrBadIndex(index)
        type_=self.getType()
        if type_==pyconfdlib.C_INT64:
            ret=self.CONFD_GET_INT64(index)
        else:
            errorMsg="ConfdValues::asInt64() called, type is %s"
            for logFunc in pyconfdlib._log("as-int64-bad").errorFunc(): logFunc(errorMsg, type_)
            a.infra.process.processFatal(errorMsg % type_)
        return ret

    def setInt64 (self, val, index=0):
        self._raiseIfNullOrBadIndex(index)
        self.CONFD_SET_INT64(val)

    def asInt32 (self, index=0):
        self._raiseIfNullOrBadIndex(index)
        type_=self.getType()
        if type_==pyconfdlib.C_INT32:
            ret=self.CONFD_GET_INT32(index)
        else:
            errorMsg="ConfdValues::asInt32() called, type is %s"
            for logFunc in pyconfdlib._log("as-int32-bad").errorFunc(): logFunc(errorMsg, type_)
            a.infra.process.processFatal(errorMsg % type_)
        return ret

    def setInt32 (self, val, index=0):
        self._raiseIfNullOrBadIndex(index)
        self.CONFD_SET_INT32(val)

    def asInt16 (self, index=0):
        self._raiseIfNullOrBadIndex(index)
        type_=self.getType()
        if type_==pyconfdlib.C_INT16:
            ret=self.CONFD_GET_INT16(index)
        else:
            errorMsg="ConfdValues::asInt16() called, type is %s"
            for logFunc in pyconfdlib._log("as-int16-bad").errorFunc(): logFunc(errorMsg, type_)
            a.infra.process.processFatal(errorMsg % type_)
        return ret

    def setInt16 (self, val, index=0):
        self._raiseIfNullOrBadIndex(index)
        self.CONFD_SET_INT16(val)

    def asInt8 (self, index=0):
        self._raiseIfNullOrBadIndex(index)
        type_=self.getType()
        if type_==pyconfdlib.C_INT8:
            ret=self.CONFD_GET_INT8(index)
        else:
            errorMsg="ConfdValues::asInt8() called, type is %s"
            for logFunc in pyconfdlib._log("as-int8-bad").errorFunc(): logFunc(errorMsg, type_)
            a.infra.process.processFatal(errorMsg % type_)
        return ret

    def setInt8 (self, val, index=0):
        self._raiseIfNullOrBadIndex(index)
        self.CONFD_SET_INT8(val)

    def asUint64 (self, index=0):
        self._raiseIfNullOrBadIndex(index)
        type_=self.getType()
        if type_==pyconfdlib.C_UINT64:
            ret=self.CONFD_GET_UINT64(index)
        else:
            errorMsg="ConfdValues::asUint64() called, type is %s"
            for logFunc in pyconfdlib._log("as-uint64-bad").errorFunc(): logFunc(errorMsg, type_)
            a.infra.process.processFatal(errorMsg % type_)
        return ret

    def setUint64 (self, val, index=0):
        self._raiseIfNullOrBadIndex(index)
        self.CONFD_SET_UINT64(val)

    def asUint32 (self, index=0):
        self._raiseIfNullOrBadIndex(index)
        type_=self.getType()
        if type_==pyconfdlib.C_UINT32:
            ret=self.CONFD_GET_UINT32(index)
        else:
            errorMsg="ConfdValues::asUint32() called, type is %s"
            for logFunc in pyconfdlib._log("as-uint32-bad").errorFunc(): logFunc(errorMsg, type_)
            a.infra.process.processFatal(errorMsg % type_)
        return ret

    def setUint32 (self, val, index=0):
        self._raiseIfNullOrBadIndex(index)
        self.CONFD_SET_UINT32(val)

    def asUint16 (self, index=0):
        self._raiseIfNullOrBadIndex(index)
        type_=self.getType()
        if type_==pyconfdlib.C_UINT16:
            ret=self.CONFD_GET_UINT16(index)
        else:
            errorMsg="ConfdValues::asUint16() called, type is %s"
            for logFunc in pyconfdlib._log("as-uint16-bad").errorFunc(): logFunc(errorMsg, type_)
            a.infra.process.processFatal(errorMsg % type_)
        return ret

    def setUint16 (self, val, index=0):
        self._raiseIfNullOrBadIndex(index)
        self.CONFD_SET_UINT16(val)

    def asUint8 (self, index=0):
        self._raiseIfNullOrBadIndex(index)
        type_=self.getType()
        if type_==pyconfdlib.C_UINT8:
            ret=self.CONFD_GET_UINT8(index)
        else:
            errorMsg="ConfdValues::asUint8() called, type is %s"
            for logFunc in pyconfdlib._log("as-uint8-bad").errorFunc(): logFunc(errorMsg, type_)
            a.infra.process.processFatal(errorMsg % type_)
        return ret

    def setUint8 (self, val, index=0):
        self._raiseIfNullOrBadIndex(index)
        self.CONFD_SET_UINT8(val)

    def asString (self, index=0):
        self._raiseIfNullOrBadIndex(index)
        type_=self.getType()
        if (type_==pyconfdlib.C_STR) or (type_==pyconfdlib.C_BUF):
            ret=self.CONFD_GET_STR(index)
        elif (type_ == pyconfdlib.C_IPV4) or \
            (type_ == pyconfdlib.C_IPV6) or \
            (type_ == pyconfdlib.C_IPV4PREFIX) or \
            (type_ == pyconfdlib.C_IPV6PREFIX):
            ret=str(self)
        else:
            errorMsg="ConfdValues::asString() called, type is %s"
            for logFunc in pyconfdlib._log("as-string-bad").errorFunc(): logFunc(errorMsg, type_)
        return ret

    def asBuf(self, index=0):
        self._raiseIfNullOrBadIndex(index)
        type_=self.getType()
        if (type_==pyconfdlib.C_BUF):
            ret=self.CONFD_GET_STR(index)
        else:
            errorMsg="ConfdValues::asBuf() called, type is %s"
            for logFunc in pyconfdlib._log("as-buf-bad").errorFunc(): logFunc(errorMsg, type_)
            Captain().processFatal(errorMsg % type_)
        return ret

    def asIPv4(self, index=0):
        self._raiseIfNullOrBadIndex(index)
        type_=self.getType()
        if (type_ == pyconfdlib.C_IPV4):
            ret=str(self)
        else:
            errorMsg="ConfdValues::asIPv4() called, type is %s"
            for logFunc in pyconfdlib._log("as-ipv4-bad").errorFunc(): logFunc(errorMsg, type_)
            Captain().processFatal(errorMsg % type_)
        return ret

    def asIPv6(self, index=0):
        self._raiseIfNullOrBadIndex(index)
        type_=self.getType()
        if (type_ == pyconfdlib.C_IPV6):
            ret=str(self)
        else:
            errorMsg="ConfdValues::asIPv6() called, type is %s"
            for logFunc in pyconfdlib._log("as-ipv6-bad").errorFunc(): logFunc(errorMsg, type_)
            Captain().processFatal(errorMsg % type_)
        return ret

    def asIPv4Prefix(self, index=0):
        self._raiseIfNullOrBadIndex(index)
        type_=self.getType()
        if (type_ == pyconfdlib.C_IPV4PREFIX):
            ret=str(self)
        else:
            errorMsg="ConfdValues::asIPv4Prefix() called, type is %s"
            for logFunc in pyconfdlib._log("as-ipv4-prefix-bad").errorFunc(): logFunc(errorMsg, type_)
            Captain().processFatal(errorMsg % type_)
        return ret

    def asIPv6Prefix(self, index=0):
        self._raiseIfNullOrBadIndex(index)
        type_=self.getType()
        if (type_ == pyconfdlib.C_IPV6PREFIX):
            ret=str(self)
        else:
            errorMsg="ConfdValues::asIPv6Prefix() called, type is %s"
            for logFunc in pyconfdlib._log("as-ipv6-prefix-bad").errorFunc(): logFunc(errorMsg, type_)
            Captain().processFatal(errorMsg % type_)
        return ret

    def setString (self, val, index=0):
        self._raiseIfNullOrBadIndex(index)
        self.CONFD_SET_STR(val)

    def asEnum (self, index=0):
        self._raiseIfNullOrBadIndex(index)
        type_=self.getType()
        if type_==pyconfdlib.C_ENUM_HASH:
            ret=self.CONFD_GET_ENUM_HASH(index)
        else:
            errorMsg="ConfdValues::asEnum() called, type is %s"
            for logFunc in pyconfdlib._log("as-enum-bad").errorFunc(): logFunc(errorMsg, type_)
            a.infra.process.processFatal(errorMsg % type_)
        return ret

    def setEnum (self, val, index=0):
        self._raiseIfNullOrBadIndex(index)
        self.CONFD_SET_ENUM_HASH(val)

    def asBool (self, index=0):
        self._raiseIfNullOrBadIndex(index)
        type_=self.getType()
        if type_==pyconfdlib.C_BOOL:
            ret=self.CONFD_GET_BOOL(index)
        else:
            errorMsg="ConfdValues::asBool() called, type is %s"
            for logFunc in pyconfdlib._log("as-bool-bad").errorFunc(): logFunc(errorMsg, type_)
            a.infra.process.processFatal(errorMsg % type_)
        return ret

    def setBool (self, val, index=0):
        self._raiseIfNullOrBadIndex(index)
        self.CONFD_SET_BOOL(val)

    def setFrom (self, other, index=0):
        """
        other may be a string or an int
        """
        if isinstance(other,str):
            self.CONFD_SET_STR(other, index)
        elif isinstance(other,int):
            self.CONFD_SET_INT64(other, index)
        else:
            raise NotImplementedError("setFrom() class %s not supported" % other.__class__)

    def copyTo (self, toValue, fromIndex=0, toIndex=0):
        self._raiseIfNullOrBadIndex(fromIndex)
        toValue._raiseIfNullOrBadIndex(toIndex)
        pyconfdlib.dll.py_confd_value_dup_to(self._myValuePtr, fromIndex, toValue._myValuePtr, toIndex)

    def clone (self):
        """
        Returns a new instance with the same values as this instance.
        The new instance owns the wrapped confd_value_t struct.
        """
        # If we are wrapping a NULL pointer, create a similar object
        if not self._myValuePtr:
            newObject=ConfdValues(confdValueTPtr=pyconfdlib.ConfdValueTPtr(), numValues=self._mySize)
        else:
            newObject=ConfdValues(numValues=self._mySize)
            for i in range(0, self._mySize):
                pyconfdlib.dll.py_confd_value_dup_to(self._myValuePtr, i, newObject._myValuePtr, i)
        for logFunc in pyconfdlib._log("cloned-null").debug5Func(): logFunc("clone() done: self=%s, newObject=%s", self, newObject)
        return newObject

    def getNumValues (self):
        return self._mySize

    def freeValues (self):
        """
        Frees variable-length data that may be contained in the wrapped value.
        Calls confd_free_value(). See the documentation of confd_free_value() for details.
        """
        if self._myIsMine:
            if self._myValuePtr:
                for i in range(0, self._mySize):
                    pyconfdlib.dll.py_confd_free_value(self._myValuePtr, i)
        else:
            raise Exception("freeValues() called when _isMine is False")

    def getCtypePtr (self):
        """Provides a lower-level access to the internal pointer"""
        return self._myValuePtr

    def _raiseIfNull (self):
        if not self._myValuePtr:
            raise Exception("I have a NULL pointer, sorry.")

    def _raiseIfNullOrBadIndex (self, index):
        self._raiseIfNull()
        if (self._mySize <= index) or (index < 0):
            raise Exception("Invalid index "+str(index)+", my size is "+str(self._mySize))


