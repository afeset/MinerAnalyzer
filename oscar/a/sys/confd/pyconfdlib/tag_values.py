# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

import pyconfdlib

import collections

from a.infra.basic.return_codes import ReturnCodes
from a.sys.confd.pyconfdlib.value import Value
from a.sys.confd.pyconfdlib.value import ConfdValueLow

class TagValues(object):

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
        str_ = "[\n"
        for tagVal in self._tagValues:
            (xmlTag, val) = tagVal
            (tag, ns) = xmlTag
            str_ += "(%s, %s)\n" % ((tag, ns), str(val))
        str_ += "]"
        return str_

    def getLen (self):
        return len(self._tagValues)

    def getAt (self, pos):
        if pos < len(self._tagValues):
            return self._tagValues[pos]
        return None

    def push (self, xmlTag, val):
        self._tagValues.append((xmlTag, val))

    def pop (self):
        return self._tagValues.pop()

    def popFront (self):
        return self._tagValues.popleft()

    def clear (self):
        self._tagValues = collections.deque()

class TagValuesLow(object):

    @staticmethod
    def allocConfdTagValues (numOfValues):
        confdTagValuePtr = pyconfdlib.dll.py_allocConfdTagValues(numOfValues)
        for logFunc in pyconfdlib._log("alloc-confd-tag-value").debug4Func(): logFunc("allocConfdTagValue called. numOfValues=%d, confdTagValuePtr=%s", numOfValues, str(confdTagValuePtr))
        return confdTagValuePtr

    @staticmethod
    def deallocConfdTagValue (confdTagValuePtr):
        for logFunc in pyconfdlib._log("dealloc-confd-tag-value").debug4Func(): logFunc("deallocConfdTagValue called. confdTagValuePtr=%s", str(confdTagValuePtr))
        pyconfdlib.dll.py_deallocConfdTagValues(confdTagValuePtr)

    @staticmethod
    def ConfdTagValueToStr (confdTagValuePtr, index):
        if not confdTagValuePtr:
            return "(NULL)"
        buf=pyconfdlib.createStringBuffer(pyconfdlib.kMaxStringSize)
        confdValPtr = pyconfdlib.dll.py_getValPtrFromTagVal(confdTagValuePtr, index)
        len_=pyconfdlib.dll.py_confd_pp_value(buf, pyconfdlib.sizeof(buf), confdValPtr, 0)
        if len_ >= pyconfdlib.sizeof(buf):
            buf=pyconfdlib.createStringBuffer(len_+1)
            len_=pyconfdlib.dll.py_confd_pp_value(buf, pyconfdlib.sizeof(buf), confdValPtr, 0)
        ns = pyconfdlib.hashToStr(pyconfdlib.dll.py_getNSFromTagVal(confdTagValuePtr, index))
        tag = pyconfdlib.hashToStr(pyconfdlib.dll.py_getTagFromTagVal(confdTagValuePtr, index))
        return ("(%s, %s)") % ((tag, ns), buf.value[:len_])

    @staticmethod
    def deepConvertPyTagValuesToConfdTagValues (pyTagValues, confdTagValuePtr):
        """
        This function performs a deep convertion of a python TagValues object to an array of confd_tag_value_t objects.
        It reallocates data memory, making the confd_tag_value_t object its owner.
        Note: When using this function the it is NOT mandatory for the python TagValues object to exist as long as the confd_tag_value_t object exists
        Note 2: confd_free_value MUST be activated on the confd_value_t object filled by this function as it is the owner of allocated memory
        confdTagValuePtr must be pre-allocated
        """
        for logFunc in pyconfdlib._log("deep-convert-py-tagvalues-to-confd-tag-values").debug4Func(): logFunc(
            "deepConvertPyTagValuesToConfdTagValues called. pyTagValues=%s, confdTagValuePtr=%s", 
            str(pyTagValues), str(confdTagValuePtr))
        if not pyTagValues or not confdTagValuePtr:
            for logFunc in pyconfdlib._log("deep-convert-py-tagvalues-to-confd-tag-values-invalid-args").errorFunc(): logFunc(
                "deepConvertPyTagValuesToConfdTagValues invalid args: pyTagValues=%s, confdTagValuePtr=%s", 
                pyTagValues, str(confdTagValuePtr))
            return ReturnCodes.kGeneralError

        confdValPtr = None
        for (i, pyTV) in enumerate(pyTagValues._tagValues):
            (xmlTag, val) = pyTV
            (tag, ns) = xmlTag
            rc = pyconfdlib.dll.py_setTagToTagVal(confdTagValuePtr, i, pyconfdlib.hashIfString(tag))
            if rc != pyconfdlib.CONFD_OK:
                for logFunc in pyconfdlib._log("deep-convert-confd-value-to-pyvalue-set-tag-failed").errorFunc(): logFunc(
                    "deepConvertConfdValueToPyValue py_setTagToTagVal() failed: confdTagValuePtr=%s, pyTagValues=%s, i=%d, tag=%d, rc=%s", 
                    ConfdValueLow.ConfdValueToStr(confdTagValuePtr), pyTagValues, i, tag, str(rc))
                return ReturnCodes.kGeneralError
            rc = pyconfdlib.dll.py_setNSToTagVal(confdTagValuePtr, i, pyconfdlib.hashIfString(ns))
            if rc != pyconfdlib.CONFD_OK:
                for logFunc in pyconfdlib._log("deep-convert-confd-value-to-pyvalue-set-ns-failed").errorFunc(): logFunc(
                    "deepConvertConfdValueToPyValue py_setTagToTagVal() failed: confdTagValuePtr=%s, pyTagValues=%s, i=%d, ns=%d, rc=%s", 
                    ConfdValueLow.ConfdValueToStr(confdTagValuePtr), pyTagValues, i, ns, str(rc))
                return ReturnCodes.kGeneralError
            confdValPtr = pyconfdlib.dll.py_getValPtrFromTagVal(confdTagValuePtr, i)
            rc = ConfdValueLow.deepConvertPyValueToConfdValue(val, confdValPtr)
            if rc != ReturnCodes.kOk:
                for logFunc in pyconfdlib._log("deep-convert-confd-value-to-pyvalue-deep-convert-value-failed").errorFunc(): logFunc(
                    "deepConvertConfdValueToPyValue deepConvertPyValueToConfdValue() failed: confdTagValuePtr=%s, pyTagValues=%s, i=%d, rc=%s", 
                    ConfdValueLow.ConfdValueToStr(confdTagValuePtr), pyTagValues, i, str(rc))
                return ReturnCodes.kGeneralError

        for logFunc in pyconfdlib._log("deep-convert-py-tagvalues-to-confd-tag-values-done").debug4Func(): logFunc(
            "deepConvertPyTagValuesToConfdTagValues done. pyTagValues=%s, confdTagValuePtr=%s", 
            pyTagValues, str(confdTagValuePtr))
        return ReturnCodes.kOk

    @staticmethod
    def deepConvertConfdTagValuesToPyTagValues (confdTagValuePtr, numOfValues, pyTagValues):
        """
        This function performs a deep convertion of an array of confd_tag_value_t objects to a python TagValues object.
        It reallocates data memory, making the python TagValues object its owner.
        Note: When using this function the it is NOT mandatory for the confd_tag_value_t object to exist as long as the python TagValues object exists
        pyTagValues must be pre-constructed
        """
        for logFunc in pyconfdlib._log("deep-convert-confd-tag-values-to-py-tagvalues").debug4Func(): logFunc(
            "deepConvertConfdTagValuesToPyTagValues called. pyTagValues=%s, numOfValues=%d, confdTagValuePtr=%s", 
            str(pyTagValues), numOfValues, str(confdTagValuePtr))
        if not pyTagValues or not confdTagValuePtr:
            for logFunc in pyconfdlib._log("deep-convert-confd-tag-values-to-py-tagvalues-invalid-args").errorFunc(): logFunc(
                "deepConvertPyTagValuesToConfdTagValues invalid args: pyTagValues=%s, numOfValues=%d, confdTagValuePtr=%s", 
                pyTagValues, numOfValues, str(confdTagValuePtr))
            return ReturnCodes.kGeneralError

        confdTagVal = None
        for i in range(numOfValues):
            for logFunc in pyconfdlib._log("deep-convert-confd-tag-values-to-py-tagvalues-iteration").debug4Func(): logFunc(
                "iteration %d", i)
            confdVal = pyconfdlib.dll.py_getValPtrFromTagVal(confdTagValuePtr, i)
            pyValue = Value()
            rc = ConfdValueLow.deepConvertConfdValueToPyValue(confdVal, pyValue)
            if rc != ReturnCodes.kOk:
                for logFunc in pyconfdlib._log("deep-convert-confd-tag-values-to-py-tagvalues-deep-convert-value-failed").errorFunc(): logFunc(
                    "deepConvertConfdValueToPyValue() failed. confdVal=%s, i=%d",
                    ConfdValueLow(ConfdValueToStr(confdVal), i))
                return ReturnCodes.kGeneralError
            tag = pyconfdlib.dll.py_getTagFromTagVal(confdTagValuePtr, i)
            tagStr = pyconfdlib.hashToStr(tag)
            ns = pyconfdlib.dll.py_getNSFromTagVal(confdTagValuePtr, i)
            nsStr = pyconfdlib.hashToStr(ns)
            for logFunc in pyconfdlib._log("deep-convert-confd-tag-values-to-py-tagvalues-adding").debug4Func(): logFunc(
                "adding tag-value %d. pyValue=%s, tagStr=%s, nsStr=%s", i, pyValue, tagStr, nsStr)
            pyTagValues.push((tagStr, nsStr), pyValue)

        for logFunc in pyconfdlib._log("deep-convert-confd-tag-values-to-py-tagvalues-done").debug4Func(): logFunc(
            "deepConvertPyTagValuesToConfdTagValues done. pyTagValues=%s, numOfValues=%d, confdTagValuePtr=%s", 
            pyTagValues, numOfValues, str(confdTagValuePtr))
        return ReturnCodes.kOk

