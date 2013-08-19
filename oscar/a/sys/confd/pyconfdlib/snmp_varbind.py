# Copyright Qwilt, 2013
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

import pyconfdlib

from a.infra.basic.return_codes import ReturnCodes
from a.sys.confd.pyconfdlib.value import Value
from a.sys.confd.pyconfdlib.value import ConfdValueLow

class SnmpVarbind(object):

    """ 
    A class representing an ordered collection of tag values. 
    It holds the actual value and their tags
    """
    def __init__ (self):
        self.clear()

    def __str__ (self):
        #"""
        #prints a list of tag & value
        #"""
        #return "%s <%s>" % (self._value, self._type)
        str_ = "[\nvariables:\n"
        for (var, val) in self._variables:
            str_ += "(%s, %s)\n" % (str(var), str(val))
        str_ += "oids:\n"
        for (oid, val) in self._oids:
            str_ += "(%s, %s)\n" % (str(oid), str(val))
        str_ += "col-rows:\n"
        for (colRow, val) in self._colRows:
            str_ += "(%s, %s)\n" % (str(colRow), str(val))
        str_ += "]"
        return str_

    def getLen (self):
        return len(self._variables) + len(self._oids) + len(self._colRows)

    def appendVariable (self, variable, val):
        self._variables.append((variable, val))

    def appendOid (self, oid, val):
        self._oids.append((oid, val))

    def appendColRow (self, col, oid, val):
        self._colRows.append(((col, oid), val))

    def clear (self):
        self._variables = []
        self._oids = []
        self._colRows = []

class SnmpVarbindLow(object):

    @staticmethod
    def allocSnmpVarbind (numOfSnmpVarbinds):
        snmpVarbindPtr = pyconfdlib.dll.py_allocSnmpVarbinds(numOfSnmpVarbinds)
        for logFunc in pyconfdlib._log("alloc-snmp-varbind").debug4Func(): logFunc("allocSnmpVarbind() called. numOfSnmpVarbinds=%d, snmpVarbindPtr=%s", numOfSnmpVarbinds, str(snmpVarbindPtr))
        return snmpVarbindPtr

    @staticmethod
    def deallocSnmpVarbind (snmpVarbindPtr):
        for logFunc in pyconfdlib._log("dealloc-snmp-varbind").debug4Func(): logFunc("py_deallocSnmpVarbinds called. snmpVarbindPtr=%s", str(snmpVarbindPtr))
        pyconfdlib.dll.py_deallocSnmpVarbinds(snmpVarbindPtr)

    @staticmethod
    def SnmpVarbindToStr (snmpVarbindPtr, index):
        if not snmpVarbindPtr:
            return "(NULL)"
        buf=pyconfdlib.createStringBuffer(pyconfdlib.kMaxStringSize)
        len_=pyconfdlib.dll.py_snmp_pp_snmp_varbind(bif, pyconfdlib.size(buf), snmpVarbindPtr, index)
        if len_ >= pyconfdlib.sizeof(buf):
            buf=pyconfdlib.createStringBuffer(len_+1)
            len_=pyconfdlib.dll.py_snmp_pp_snmp_varbind(bif, pyconfdlib.size(buf), snmpVarbindPtr, index)
        return buf.value[:len_]

    @staticmethod
    def deepConvertPySnmpVarbindToConfdSnmpVarbind (pySnmpVarbind, confdSnmpVarbindPtr):
        """
        This function performs a deep convertion of a python SnmpVarbind object to an array of confd_snmp_varbind objects.
        It reallocates data memory, making the confd_snmp_varbind object its owner.
        Note: When using this function the it is NOT mandatory for the python SnmpVarbind object to exist as long as the confd_snmp_varbind object exists
        Note 2: confd_free_value MUST be activated on the confd_value_t object filled by this function as it is the owner of allocated memory
        confdTagValuePtr must be pre-allocated
        """
        for logFunc in pyconfdlib._log("deep-convert-py-snmp-varbind-to-confd-snmp-varbinds").debug4Func(): logFunc(
            "deepConvertPySnmpVarbindToConfdSnmpVarbind called. pySnmpVarbind=%s, confdSnmpVarbindPtr=%s", 
            str(pySnmpVarbind), str(confdSnmpVarbindPtr))
        if not pySnmpVarbind or not confdSnmpVarbindPtr:
            for logFunc in pyconfdlib._log("deep-convert-py-snmp-varbinds-to-confd-snmp-varbinds-invalid-args").errorFunc(): logFunc(
                "deepConvertPySnmpVarbindToConfdSnmpVarbind invalid args: pySnmpVarbind=%s, confdSnmpVarbindPtr=%s", 
                pySnmpVarbind, str(confdSnmpVarbindPtr))
            return ReturnCodes.kGeneralError

        confdValPtr = None
        indexOffset = 0
        for (i, v) in enumerate(pySnmpVarbind._variables):
            (var, val) = v
            rc = pyconfdlib.dll.py_setSnmpVarbindVariable(confdSnmpVarbindPtr, i+indexOffset, var)
            if rc != pyconfdlib.CONFD_OK:
                for logFunc in pyconfdlib._log("deep-convert-py-snmp-varbinds-to-confd-snmp-varbinds-set-variable-failed").errorFunc(): logFunc(
                    "deepConvertPySnmpVarbindToConfdSnmpVarbind py_setSnmpVarbindVariable() failed: pySnmpVarbind=%s, i=%d, indexOffset=%d, var=%d, rc=%s", 
                    pySnmpVarbind, i, indexOffset, var, str(rc))
                return ReturnCodes.kGeneralError
            confdValPtr = pyconfdlib.dll.py_getValPtrFromSnmpVarbind(confdSnmpVarbindPtr, i+indexOffset)
            rc = ConfdValueLow.deepConvertPyValueToConfdValue(val, confdValPtr)
            if rc != ReturnCodes.kOk:
                for logFunc in pyconfdlib._log("deep-convert-py-snmp-varbinds-to-confd-snmp-varbinds-deep-convert-value-failed").errorFunc(): logFunc(
                    "deepConvertPySnmpVarbindToConfdSnmpVarbind deepConvertPyValueToConfdValue() failed: pySnmpVarbind=%s, i=%d, indexOffset=%d, val=%d, rc=%s", 
                    pySnmpVarbind, i, indexOffset, val, str(rc))
                return ReturnCodes.kGeneralError

        indexOffset += len(pySnmpVarbind._variables)

        for (i, v) in enumerate(pySnmpVarbind._oids):
            (oid, val) = v
            oidArray=(pyconfdlib.Uint32Type * len(oid))()
            for index in range(len(oid)):
                oidArray[index] = oid[index]
            rc = pyconfdlib.dll.py_setSnmpVarbindOid(confdSnmpVarbindPtr, i+indexOffset, oidArray, len(oid))
            if rc != pyconfdlib.CONFD_OK:
                for logFunc in pyconfdlib._log("deep-convert-py-snmp-varbinds-to-confd-snmp-varbinds-set-oid-failed").errorFunc(): logFunc(
                    "deepConvertPySnmpVarbindToConfdSnmpVarbind py_setSnmpVarbindOid() failed: pySnmpVarbind=%s, i=%d, indexOffset=%d, oid=%d, rc=%s", 
                    pySnmpVarbind, i, indexOffset, oid, str(rc))
                return ReturnCodes.kGeneralError
            confdValPtr = pyconfdlib.dll.py_getValPtrFromSnmpVarbind(confdSnmpVarbindPtr, i+indexOffset)
            rc = ConfdValueLow.deepConvertPyValueToConfdValue(val, confdValPtr)
            if rc != ReturnCodes.kOk:
                for logFunc in pyconfdlib._log("deep-convert-py-snmp-varbinds-to-confd-snmp-varbinds-deep-convert-value-failed").errorFunc(): logFunc(
                    "deepConvertPySnmpVarbindToConfdSnmpVarbind deepConvertPyValueToConfdValue() failed: pySnmpVarbind=%s, i=%d, indexOffset=%d, val=%d, rc=%s", 
                    pySnmpVarbind, i, indexOffset, val, str(rc))
                return ReturnCodes.kGeneralError

        indexOffset += len(pySnmpVarbind._oids)

        for (i, v) in enumerate(pySnmpVarbind._colRows):
            ((column, oid), val) = v
            oidArray=(pyconfdlib.Uint32Type * len(oid))()
            for index in range(len(oid)):
                oidArray[index] = oid[index]
            rc = pyconfdlib.dll.py_setSnmpVarbindColRow(confdSnmpVarbindPtr, i+indexOffset, column, oidArray, len(oid))
            if rc != pyconfdlib.CONFD_OK:
                for logFunc in pyconfdlib._log("deep-convert-py-snmp-varbinds-to-confd-snmp-varbinds-set-col -row-failed").errorFunc(): logFunc(
                    "deepConvertPySnmpVarbindToConfdSnmpVarbind py_setSnmpVarbindColRow() failed: pySnmpVarbind=%s, i=%d, indexOffset=%d, oid=%d, rc=%s", 
                    pySnmpVarbind, i, indexOffset, oid, str(rc))
                return ReturnCodes.kGeneralError
            confdValPtr = pyconfdlib.dll.py_getValPtrFromSnmpVarbind(confdSnmpVarbindPtr, i+indexOffset)
            rc = ConfdValueLow.deepConvertPyValueToConfdValue(val, confdValPtr)
            if rc != ReturnCodes.kOk:
                for logFunc in pyconfdlib._log("deep-convert-py-snmp-varbinds-to-confd-snmp-varbinds-deep-convert-value-failed").errorFunc(): logFunc(
                    "deepConvertPySnmpVarbindToConfdSnmpVarbind deepConvertPyValueToConfdValue() failed: pySnmpVarbind=%s, i=%d, indexOffset=%d, val=%d, rc=%s", 
                    pySnmpVarbind, i, indexOffset, val, str(rc))
                return ReturnCodes.kGeneralError

        for logFunc in pyconfdlib._log("deep-convert-py-snmp-varbinds-to-confd-snmp-varbinds-done").debug4Func(): logFunc(
            "deepConvertPySnmpVarbindToConfdSnmpVarbind done. pySnmpVarbind=%s, confdSnmpVarbindPtr=%s", 
            pySnmpVarbind, str(confdSnmpVarbindPtr))
        return ReturnCodes.kOk

