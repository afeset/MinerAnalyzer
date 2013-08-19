# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

import value
import key_path
import tag_values
import snmp_varbind
import pyconfdlib
from confd_values import ConfdValues

from a.infra.basic.return_codes import ReturnCodes

import traceback
import socket

#def confd_data_reply_value_array(tctx, value):
#    """
#    value: a ConfdValues object containing a one or more values
#    """
#
#    if not pyconfdlib.checkTypes({tctx : ConfdTransContext, value : ConfdValues}):
#        return pyconfdlib.CONFD_BAD_PYTHON_USAGE
#
#    return pyconfdlib.dll.py_confd_data_reply_value_array(tctx.getCtypePtr(), value.getCtypePtr(), value.getNumValues())


def confd_data_reply_tag_value_array(tctx, tagValues):
    """
    tagValues: a collection of tag values
    """

    if not pyconfdlib.checkTypes({tctx : pyconfdlib.ConfdTransContext, tagValues : tag_values.TagValues}):
        return pyconfdlib.CONFD_BAD_PYTHON_USAGE

    confdTagValueTPtr = tag_values.TagValuesLow.allocConfdTagValues(tagValues.getLen())
    res = tag_values.TagValuesLow.deepConvertPyTagValuesToConfdTagValues(tagValues, confdTagValueTPtr)
    if res != ReturnCodes.kOk:
        for logFunc in pyconfdlib._log("confd-data-reply-tag-value-array-deep-convert-failed").errorFunc(): logFunc(
            "deepConvertPyTagValuesToConfdTagValues(tagValues=%s, confdTagValueTPtr=%s) res=%s",
            tagValues, str(confdTagValueTPtr), str(res))
        return ReturnCodes.kGeneralError

    for logFunc in pyconfdlib._log("confd-data-reply-tag-value-array-deep-convert-succeeded").debug2Func(): logFunc(
        "deepConvertPyTagValuesToConfdTagValues(tagValues=%s, confdTagValueTPtr=%s, len=%d) succeeded",
        tagValues, str(confdTagValueTPtr), tagValues.getLen())
    res = pyconfdlib.dll.py_confd_data_reply_tag_value_array(tctx.getCtypePtr(), confdTagValueTPtr, tagValues.getLen())

    tag_values.TagValuesLow.deallocConfdTagValue(confdTagValueTPtr)

    return res

def maapi_get_values (sock, thandle, tagValues, keyPath):
    if not pyconfdlib.checkTypes({sock : socket.socket, thandle : int}):
        return pyconfdlib.CONFD_BAD_PYTHON_USAGE

    for logFunc in pyconfdlib._log("maapi-get-values").debug3Func(): logFunc("called. keyPath=%s", keyPath)

    numOfValues = tagValues.getLen()
    confdTagValueTPtr = tag_values.TagValuesLow.allocConfdTagValues(numOfValues)
    res = tag_values.TagValuesLow.deepConvertPyTagValuesToConfdTagValues(tagValues, confdTagValueTPtr)
    if res != ReturnCodes.kOk:
        for logFunc in pyconfdlib._log("maapi-get-values-deep-convert-failed").errorFunc(): logFunc(
            "deepConvertPyTagValuesToConfdTagValues(tagValues=%s, confdTagValueTPtr=%s) res=%s",
            tagValues, str(confdTagValueTPtr), str(res))
        return ReturnCodes.kGeneralError

    for logFunc in pyconfdlib._log("maapi-get-values-calling-library").debug3Func(): logFunc("calling library. keyPath=%s", keyPath)

    res = pyconfdlib.dll.py_maapi_get_values(sock.fileno(), thandle, confdTagValueTPtr, numOfValues, keyPath.getCannonicalStr())
    if res != pyconfdlib.CONFD_OK:
        for logFunc in pyconfdlib._log("maapi-get-values-lib-failed").errorFunc(): logFunc("py_maapi_get_values() failed. res=%s", res)
        return ReturnCodes.kGeneralError

    for logFunc in pyconfdlib._log("maapi-get-values-library-done").debug3Func(): logFunc("library done. keyPath=%s. val=%s", keyPath, tag_values.TagValuesLow.ConfdTagValueToStr(confdTagValueTPtr, 0))

    tagValues.clear()
    res = tag_values.TagValuesLow.deepConvertConfdTagValuesToPyTagValues(confdTagValueTPtr, numOfValues, tagValues)
    if res != ReturnCodes.kOk:
        for logFunc in pyconfdlib._log("maapi-get-values-deep-convert-back-failed").errorFunc(): logFunc(
            "deepConvertConfdTagValuesToPyTagValues(confdTagValueTPtr=%s, numOfValues=%s) res=%s",
            str(confdTagValueTPtr), numOfValues, str(res))
        return ReturnCodes.kGeneralError

    tag_values.TagValuesLow.deallocConfdTagValue(confdTagValueTPtr)

    return ReturnCodes.kOk

def maapi_set_values (sock, thandle, tagValues, keyPath):
    if not pyconfdlib.checkTypes({sock : socket.socket, thandle : int}):
        return pyconfdlib.CONFD_BAD_PYTHON_USAGE

    for logFunc in pyconfdlib._log("maapi-set-values").debug3Func(): logFunc("called. keyPath=%s, thandle=%s", keyPath, thandle)

    numOfValues = tagValues.getLen()
    confdTagValueTPtr = tag_values.TagValuesLow.allocConfdTagValues(numOfValues)
    res = tag_values.TagValuesLow.deepConvertPyTagValuesToConfdTagValues(tagValues, confdTagValueTPtr)
    if res != ReturnCodes.kOk:
        for logFunc in pyconfdlib._log("maapi-set-values-deep-convert-failed").errorFunc(): logFunc(
            "deepConvertPyTagValuesToConfdTagValues(tagValues=%s, confdTagValueTPtr=%s) res=%s",
            tagValues, str(confdTagValueTPtr), str(res))
        return ReturnCodes.kGeneralError

    for logFunc in pyconfdlib._log("maapi-set-values-calling-library").debug3Func(): logFunc("calling library. keyPath=%s", keyPath)

    res = pyconfdlib.dll.py_maapi_set_values(sock.fileno(), thandle, confdTagValueTPtr, numOfValues, keyPath.getCannonicalStr())
    if res != pyconfdlib.CONFD_OK:
        for logFunc in pyconfdlib._log("maapi-set-values-lib-failed").errorFunc(): logFunc("py_maapi_set_values() failed. res=%s", res)
        return ReturnCodes.kGeneralError

    for logFunc in pyconfdlib._log("maapi-set-values-library-done").debug3Func(): logFunc("library done. keyPath=%s. val=%s", keyPath, tag_values.TagValuesLow.ConfdTagValueToStr(confdTagValueTPtr, 0))

    tag_values.TagValuesLow.deallocConfdTagValue(confdTagValueTPtr)

    return ReturnCodes.kOk

def confd_notification_send_snmp (notificationCtx, notificationName, snmpVarbinds): 
    if not pyconfdlib.checkTypes({notificationName : str}):
        return pyconfdlib.CONFD_BAD_PYTHON_USAGE

    for logFunc in pyconfdlib._log("confd-send-snmp").debug3Func(): logFunc("called. notificationCtx=%s, notificationName=%s, snmpVarbinds=%s", notificationCtx, notificationName, snmpVarbinds)

    numOfVarbinds = snmpVarbinds.getLen()
    confdSnmpVarbindPtr = snmp_varbind.SnmpVarbindLow.allocSnmpVarbind(numOfVarbinds)
    res = snmp_varbind.SnmpVarbindLow.deepConvertPySnmpVarbindToConfdSnmpVarbind(snmpVarbinds, confdSnmpVarbindPtr)
    if res != ReturnCodes.kOk:
        for logFunc in pyconfdlib._log("confd-send-snmp-deep-convert-failed").errorFunc(): logFunc(
            "deepConvertPySnmpVarbindToConfdSnmpVarbind(snmpVarbind=%s, confdSnmpVarbindPtr=%s) res=%s",
            snmpVarbind, str(confdSnmpVarbindPtr), str(res))
        return ReturnCodes.kGeneralError

    for logFunc in pyconfdlib._log("confd-send-snmp-calling-library").debug3Func(): logFunc("calling library. notificationCtx=%s, notificationName=%s, snmpVarbinds=%s", notificationCtx, notificationName, snmpVarbinds)

    res = pyconfdlib.dll.py_confd_notification_send_snmp(notificationCtx, notificationName, confdSnmpVarbindPtr, numOfVarbinds)
    if res != pyconfdlib.CONFD_OK:
        for logFunc in pyconfdlib._log("confd-send-snmp-lib-failed").errorFunc(): logFunc("py_confd_notification_send_snmp() failed. res=%s", res)
        return ReturnCodes.kGeneralError

    for logFunc in pyconfdlib._log("confd-send-snmp-library-done").debug3Func(): logFunc("library done.")

    snmp_varbind.SnmpVarbindLow.deallocSnmpVarbind(confdSnmpVarbindPtr)

    return ReturnCodes.kOk


# A wrapper for struct maapi_cursor
class MaapiCursor:
    """ 
    A High-level wrapper for a struct maapi_cursor*. 
    Always owns the wrapped struct (Until we see sample for user code that gets a cursor owned by libconfd or something)
    """
    def __init__ (self):
        self._myMaapiCursorTPtr=pyconfdlib.dll.py_allocMaapiCursor()

    def destroy (self):
        pyconfdlib.dll.py_maapi_destroy_cursor(self._myMaapiCursorTPtr)

    def getN (self):
        self._fatalIfNull()
        return pyconfdlib.dll.py_maapiCursorGetN(self._myMaapiCursorTPtr)

    def getValue (self, keyIndex=0):
        self._fatalIfNull()
        val=pyconfdlib.dll.py_maapiCursorGetValue(self._myMaapiCursorTPtr, keyIndex)
        if not val:
            msg="MaapiCursor.getValue(): Got a NULL pointer for getValue(keyIndex=%s)" % keyIndex
            for logFunc in pyconfdlib._log("maapi-cursor-null").errorFunc(): logFunc(msg)
            return None
        pyValue = value.Value()
        res = value.ConfdValueLow.deepConvertConfdValueToPyValue(val, pyValue)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("maapi-cursor-get-value-deep-convert-old").errorFunc():
                logFunc("deepConvertConfdValueToPyValue() failed. val=%s, res=%s", str(val), str(res))
            return None

        return pyValue

    def getCtypePtr (self):
        """Provides a lower-level access to the internal pointer"""
        self._fatalIfNull()
        return self._myMaapiCursorTPtr

    def _fatalIfNull (self):
        if not self._myMaapiCursorTPtr:
            msg="MaapiCursor: I have a NULL pointer, sorry"
            for logFunc in pyconfdlib._log("maapi-cursor-null").errorFunc(): logFunc(msg)
            a.infra.process.processFatal(msg)

    def __del__ (self):
        pyconfdlib.dll.py_maapi_destroy_cursor(self._myMaapiCursorTPtr)
        pyconfdlib.dll.py_deallocMaapiCursor(self._myMaapiCursorTPtr)
        self._myMaapiCursorTPtr = None

def maapi_init_cursor(sock, thandle, mc, keyPath):
    if not pyconfdlib.checkTypes({sock : socket.socket, thandle : int, mc : MaapiCursor, keyPath : key_path.KeyPath}):
        return pyconfdlib.CONFD_BAD_PYTHON_USAGE

    return pyconfdlib.dll.py_maapi_init_cursor(sock.fileno(), thandle, mc.getCtypePtr(), keyPath.getCannonicalStr())

def maapi_destroy_cursor(mc):
    if not pyconfdlib.checkTypes({mc : MaapiCursor}):
        return pyconfdlib.CONFD_BAD_PYTHON_USAGE

    pyconfdlib.dll.py_maapi_destroy_cursor(mc.getCtypePtr())

def maapi_get_next(mc):
    if not pyconfdlib.checkTypes({mc : MaapiCursor}):
        return pyconfdlib.CONFD_BAD_PYTHON_USAGE

    return pyconfdlib.dll.py_maapi_get_next(mc.getCtypePtr())


def confd_register_range_data_cb(dctx, callpoint, fmt, lowerRangeValue, upperRangeValue, getElemCb=0, getNextCb=0, getObjCb=0, callBackData=None):
    class CbWrapper:
        """
        A wrapper for the python callbacks supplied by the application.
        Wraps each value supplied by confd with a proper Python type, checks return type   
        """
        def __init__(self, callback, callpoint, callBackData):
            self.callBack=callback
            self.callpoint=callpoint
            self.callBackData=callBackData
        # Used for callbacks with a single parameter: tctx
        @pyconfdlib.exceptionGuard
        def func1 (self, tctx, confdKeypathPtr):
            for logFunc in pyconfdlib._log("confd_register_data_cb-func1-called").debug2Func(): logFunc("confd_register_data_cb::func1() called: tctx=%s, confdKeypathPtr=%s", tctx, confdKeypathPtr)
            pyKeyPath = key_path.KeyPath()
            ret = key_path.ConfdHKeyPathLow.deepConvertConfdHKeyPathToPyKeyPath(confdKeypathPtr, pyKeyPath)
            if ret != ReturnCodes.kOk:
                for logFunc in pyconfdlib._log("confd_register_data_cb-func1-failed-convert").errorFunc(): logFunc("confd_register_data_cb::func1() deepConvertConfdHKeyPathToPyKeyPath() failed: tctx=%s, confdKeypathPtr=%s, ret=%s",
                                                                           tctx, confdKeypathPtr, ret)
                return pyconfdlib.CONFD_ERR
            ret=self.callBack(pyconfdlib.ConfdTransContext(tctx), self.callpoint, self.callBackData, pyKeyPath)
            pyconfdlib.checkTypes({ret : pyconfdlib.ConfdReturnCode})
            return ret.getValue()
        # Used for callbacks with 2 parameters: tctx,next
        @pyconfdlib.exceptionGuard
        def func2 (self, tctx, confdKeypathPtr, next):
            for logFunc in pyconfdlib._log("confd_register_data_cb-func2-called").debug2Func(): logFunc("confd_register_data_cb::func2() called: tctx=%s, confdKeypathPtr=%s, next=%s", tctx, confdKeypathPtr, next)
            pyKeyPath = key_path.KeyPath()
            ret = key_path.ConfdHKeyPathLow.deepConvertConfdHKeyPathToPyKeyPath(confdKeypathPtr, pyKeyPath)
            if ret != ReturnCodes.kOk:
                for logFunc in pyconfdlib._log("confd_register_data_cb-func2-failed-convert").errorFunc(): logFunc("confd_register_data_cb::func2() deepConvertConfdHKeyPathToPyKeyPath() failed: tctx=%s, confdKeypathPtr=%s, next=%s,ret=%s",
                                                                           tctx, confdKeypathPtr, next, ret)
                return pyconfdlib.CONFD_ERR
            ret=self.callBack(pyconfdlib.ConfdTransContext(tctx), self.callpoint, self.callBackData, ret, next)
            pyconfdlib.checkTypes({ret : pyconfdlib.ConfdReturnCode})
            return ret.getValue()


    if not pyconfdlib.checkTypes({dctx : pyconfdlib.ConfdDaemonCtx, callpoint : str, fmt : str}):
        return pyconfdlib.CONFD_BAD_PYTHON_USAGE

    # TODO(orens) check that callbacks are indeed callable

    wrapper=0 # By default, we register a NULL function pointer
    if getElemCb:
        wrapper=CbWrapper(getElemCb, callpoint, callBackData).func1
    getElemPtr=pyconfdlib.ConfdDataGetElemFuncType(wrapper)
    dctx.dontGcMe(getElemPtr)  # Protect against GC as long as this context is alive

    getNextPtr=0
    if getNextCb:
        wrapper=CbWrapper(getNextCb, callpoint, callBackData).func2
    getNextPtr=pyconfdlib.ConfdDataGetNextFuncType(wrapper)
    dctx.dontGcMe(getNextPtr)

    getObjPtr=0
    if getObjCb:
        wrapper=CbWrapper(getObjCb, callpoint, callBackData).func1
    getObjPtr=pyconfdlib.ConfdDataGetObjFuncType(wrapper)
    dctx.dontGcMe(getObjPtr)

    if (not lowerRangeValue) or (not upperRangeValue):
        for logFunc in pyconfdlib._log("confd-register-range-data-cb-empty-range-values").errorFunc(): logFunc("empty range values. lowerRangeVal=%s, upperRangeVal=%s",
                                                                      ("%s" % x for x in lowerRangeValue), 
                                                                      ("%s" % x for x in upperRangeValue))
        return pyconfdlib.CONFD_ERR
    for logFunc in pyconfdlib._log("confd-register-range-data-cb").debug3Func(): logFunc(
        "confd_register_data_cb called with values: lowerRangeValue=%s, upperRangeValue=%s",
        lowerRangeValue, upperRangeValue)


    confdLowerRangeVal = value.ConfdValueLow.allocConfdValue()
    res = value.ConfdValueLow.shallowConvertPyValueToConfdValue(lowerRangeValue, confdLowerRangeVal)
    if res != ReturnCodes.kOk:
        for logFunc in pyconfdlib._log("confd-register-range-data-cb-with-values-convert-lower-failed").errorFunc(): logFunc(
            "confd_register_data_cb shallowConvertPyValueToConfdValue(lower) failed: val=%s", lowerRangeValue)
        return pyconfdlib.CONFD_ERR
    confdUpperRangeVal = value.ConfdValueLow.allocConfdValue()
    res = value.ConfdValueLow.shallowConvertPyValueToConfdValue(upperRangeValue, confdUpperRangeVal)
    if res != ReturnCodes.kOk:
        for logFunc in pyconfdlib._log("confd-register-range-data-cb-with-values-convert-upper-failed").errorFunc(): logFunc(
            "confd_register_data_cb shallowConvertPyValueToConfdValue(upper) failed: val=%s", upperRangeValue)
        return pyconfdlib.CONFD_ERR

    for logFunc in pyconfdlib._log("confd-register-range-data-cb-with-values").debug3Func(): logFunc(
        "confd_register_data_cb called with values: confdLowerRangeValues=%s, confdUpperRangeVal=%s", 
        confdLowerRangeVal, confdUpperRangeVal)
    res = pyconfdlib.dll.py_confd_register_range_data_cb(dctx.getPtr(), callpoint, getElemPtr, getNextPtr, getObjPtr, confdLowerRangeVal, confdUpperRangeVal, 1, fmt)

    value.ConfdValueLow.deallocConfdValue(confdUpperRangeVal)
    value.ConfdValueLow.deallocConfdValue(confdLowerRangeVal)
    return res

def confd_register_range_valpoint_cb(dctx, validationPoint, fmt, lowerRangeVal, upperRangeVal, validateCb=0, callBackData=None):
    class CbWrapper:
        """
        A wrapper for the python callbacks supplied by the application.
        Wraps each value supplied by confd with a proper Python type, checks return type   
        """
        def __init__(self, callback, validationPoint, callBackData):
            self.callBack=callback
            self.validationPoint=validationPoint
            self.callBackData=callBackData
        # Used for callbacks with a single parameter: tctx
        @pyconfdlib.exceptionGuard
        def validate(self, tctx, confdKeypathPtr, val):
            for logFunc in pyconfdlib._log("confd_register_range_valpoint_cb-validate-called").debug2Func(): logFunc("confd_register_range_valpoint_cb::validate() called: tctx=%s, confdKeypathPtr=%s, val=%s", tctx, confdKeypathPtr, val)
            pyKeyPath = key_path.KeyPath()
            ret = key_path.ConfdHKeyPathLow.deepConvertConfdHKeyPathToPyKeyPath(confdKeypathPtr, pyKeyPath)
            if ret != ReturnCodes.kOk:
                for logFunc in pyconfdlib._log("confd_register_range_valpoint_cb-validate-failed-convert").errorFunc(): logFunc("confd_register_range_valpoint_cb::validate() deepConvertConfdHKeyPathToPyKeyPath() failed: tctx=%s, confdKeypathPtr=%s, val=%s,ret=%s",
                                                                           tctx, confdKeypathPtr, val, ret)
                return pyconfdlib.CONFD_ERR
            pyValue = None
            if val:
                pyValue = value.Value()
                res = value.ConfdValueLow.deepConvertConfdValueToPyValue(val, pyValue)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log("confd_register_range_valpoint_cb-validate-deep-convert-old").errorFunc():
                        logFunc("deepConvertConfdValueToPyValue() failed. val=%s, pyValue=%s, pyKeyPath=%s, res=%s", str(val), pyValue, pyKeyPath, str(res))
                    return pyconfdlib.CONFD_ERR.getValue()
            ret=self.callBack(pyconfdlib.ConfdTransContext(tctx), self.validationPoint, self.callBackData, pyKeyPath, pyValue)
            pyconfdlib.checkTypes({ret : pyconfdlib.ConfdReturnCode})
            return ret.getValue()

    if not pyconfdlib.checkTypes({dctx : pyconfdlib.ConfdDaemonCtx, validationPoint : str, fmt : str}):
        return pyconfdlib.CONFD_BAD_PYTHON_USAGE

    # TODO(orens) check that callbacks are indeed callable

    wrapper=0 # By default, we register a NULL function pointer
    if validateCb:
        wrapper=CbWrapper(validateCb, validationPoint, callBackData).validate
    validatePtr=pyconfdlib.ConfdValpointFuncType(wrapper)
    dctx.dontGcMe(validatePtr)  # Protect against GC as long as this context is alive

    confdLowerRangeVal = value.ConfdValueLow.allocConfdValue()
    res = value.ConfdValueLow.shallowConvertPyValueToConfdValue(lowerRangeVal, confdLowerRangeVal)
    if res != ReturnCodes.kOk:
        for logFunc in pyconfdlib._log("confd-register-range-valpoint-cb-with-values-convert-lower-vailed").errorFunc(): logFunc("confd_register_valpoint_cb shallowConvertPyValueToConfdValue(lower) failed: lowerRangeVal=%s, upperRangeVal=%s",
                                                                                        lowerRangeVal, upperRangeVal)
        return pyconfdlib.CONFD_ERR
    confdUpperRangeVal = value.ConfdValueLow.allocConfdValue()
    res = value.ConfdValueLow.shallowConvertPyValueToConfdValue(upperRangeVal, confdUpperRangeVal)
    if res != ReturnCodes.kOk:
        for logFunc in pyconfdlib._log("confd-register-range-valpoint-cb-with-values-convert-upper-vailed").errorFunc(): logFunc("confd_register_valpoint_cb shallowConvertPyValueToConfdValue(upper) failed: lowerRangeVal=%s, upperRangeVal=%s",

                                                                                    lowerRangeVal, upperRangeVal)
        return pyconfdlib.CONFD_ERR

    for logFunc in pyconfdlib._log("confd-register-range-valpoint-cb-with-values").debug3Func(): logFunc("confd_register_valpoint_cb called with values: lowerRangeVal=%s, upperRangeVal=%s",
                                                                lowerRangeVal, upperRangeVal)
    res = pyconfdlib.dll.py_confd_register_range_valpoint_cb(dctx.getPtr(), validationPoint, validatePtr, confdLowerRangeVal, confdUpperRangeVal, fmt)

    value.ConfdValueLow.deallocConfdValue(confdUpperRangeVal)
    value.ConfdValueLow.deallocConfdValue(confdLowerRangeVal)

    return res

def confd_register_valpoint_cb(dctx, validationPoint, validateCb=0, callBackData=None):
    class CbWrapper:
        """
        A wrapper for the python callbacks supplied by the application.
        Wraps each value supplied by confd with a proper Python type, checks return type   
        """
        def __init__(self, callback, validationPoint, callBackData):
            self.callBack=callback
            self.validationPoint=validationPoint
            self.callBackData=callBackData
        # Used for callbacks with a single parameter: tctx
        @pyconfdlib.exceptionGuard
        def validate(self, tctx, confdKeypathPtr, val):
            for logFunc in pyconfdlib._log("confd_register_range_valpoint_cb-validate-called").debug2Func(): logFunc("confd_register_range_valpoint_cb::validate() called: tctx=%s, confdKeypathPtr=%s, val=%s", tctx, confdKeypathPtr, val)
            pyKeyPath = key_path.KeyPath()
            ret = key_path.ConfdHKeyPathLow.deepConvertConfdHKeyPathToPyKeyPath(confdKeypathPtr, pyKeyPath)
            if ret != ReturnCodes.kOk:
                for logFunc in pyconfdlib._log("confd_register_range_valpoint_cb-validate-failed-convert").errorFunc(): logFunc("confd_register_range_valpoint_cb::validate() deepConvertConfdHKeyPathToPyKeyPath() failed: tctx=%s, confdKeypathPtr=%s, val=%s,ret=%s",
                                                                           tctx, confdKeypathPtr, val, ret)
                return pyconfdlib.CONFD_ERR
            valP=None
            if val:
                valP=ConfdValues(val)
            ret=self.callBack(pyconfdlib.ConfdTransContext(tctx), self.validationPoint, self.callBackData, pyKeyPath, valP)
            pyconfdlib.checkTypes({ret : pyconfdlib.ConfdReturnCode})
            return ret.getValue()


    if not pyconfdlib.checkTypes({dctx : pyconfdlib.ConfdDaemonCtx, validationPoint : str}):
        return pyconfdlib.CONFD_BAD_PYTHON_USAGE

    # TODO(orens) check that callbacks are indeed callable

    wrapper=0 # By default, we register a NULL function pointer
    if validateCb:
        wrapper=CbWrapper(validateCb, validationPoint, callBackData).validate
    validatePtr=pyconfdlib.ConfdValpointFuncType(wrapper)
    dctx.dontGcMe(validatePtr)  # Protect against GC as long as this context is alive

    return pyconfdlib.dll.py_confd_register_valpoint_cb(dctx.getPtr(), validationPoint, validatePtr)

def confd_register_range_action_cb(dctx, actionPoint, fmt, lowerRangeVal, upperRangeVal, initCb, actionCb, abortCb=0, callBackData=None):
    class CbWrapper:
        """
        A wrapper for the python callbacks supplied by the application.
        Wraps each value supplied by confd with a proper Python type, checks return type   
        """
        def __init__(self, callback, actionPoint, callBackData):
            self.callBack=callback
            self.actionPoint=actionPoint
            self.callBackData=callBackData
        # Used for callbacks with a single parameter: userInfo
        @pyconfdlib.exceptionGuard
        def func1 (self, userInfo):
            for logFunc in pyconfdlib._log("confd_register_data_cb-func1-called").debug2Func(): logFunc("confd_register_data_cb::func1() called: userInfo=%s", userInfo)
            ret=self.callBack(pyconfdlib.ConfdUserInfoCtx(userInfo), self.actionPoint, self.callBackData)
            pyconfdlib.checkTypes({ret : pyconfdlib.ConfdReturnCode})
            return ret.getValue()
        # Used for callbacks with 5 parameters: userInfo, name, keypath, params & nuParams
        @pyconfdlib.exceptionGuard
        def func2 (self, userInfo, name, confdKeypathPtr, params, numParams):
            for logFunc in pyconfdlib._log("confd_register_data_cb-func2-called").debug2Func(): logFunc("confd_register_data_cb::func2() called: userInfo=%s, name=%s, confdKeypathPtr=%s, params=%s, numParams=%s",
                                                               userInfo, name, confdKeypathPtr, params, numParams)
            pyKeyPath = key_path.KeyPath()
            ret = key_path.ConfdHKeyPathLow.deepConvertConfdHKeyPathToPyKeyPath(confdKeypathPtr, pyKeyPath)
            if ret != ReturnCodes.kOk:
                for logFunc in pyconfdlib._log("confd_register_data_cb-func2-failed-convert").errorFunc(): logFunc("confd_register_data_cb::func2() deepConvertConfdHKeyPathToPyKeyPath() failed: userInfo=%s, name=%s, confdKeypathPtr=%s, params=%s, numParams=%s, ret=%s",
                                                                   userInfo, name, confdKeypathPtr, params, numParams, ret)
                return pyconfdlib.CONFD_ERR
            ret=self.callBack(pyconfdlib.ConfdUserInfoCtx(userInfo), self.actionPoint, self.callBackData, name, pyKeyPath, params, numParams)
            pyconfdlib.checkTypes({ret : pyconfdlib.ConfdReturnCode})
            return ret.getValue()


    if not pyconfdlib.checkTypes({dctx : pyconfdlib.ConfdDaemonCtx, actionPoint : str, fmt : str}):
        return pyconfdlib.CONFD_BAD_PYTHON_USAGE

    # TODO(orens) check that callbacks are indeed callable

    wrapperInit=0 # By default, we register a NULL function pointer
    if initCb:
        wrapperInit=CbWrapper(initCb, actionPoint, callBackData).func1
    initPtr=pyconfdlib.ConfdActionpointInitFuncType(wrapperInit)
    dctx.dontGcMe(initPtr)  # Protect against GC as long as this context is alive

    wrapperAbort=0 # By default, we register a NULL function pointer
    if abortCb:
        wrapperAbort=CbWrapper(abortCb, actionPoint, callBackData).func1
    abortPtr=pyconfdlib.ConfdActionpointAbortFuncType(wrapperAbort)
    dctx.dontGcMe(abortPtr)  # Protect against GC as long as this context is alive

    wrapperAction=0 # By default, we register a NULL function pointer
    if actionCb:
        wrapperAction=CbWrapper(actionCb, actionPoint, callBackData).func2
    actionPtr=pyconfdlib.ConfdActionpointActionFuncType(wrapperAction)
    dctx.dontGcMe(actionPtr)  # Protect against GC as long as this context is alive

    confdLowerRangeVal = value.ConfdValueLow.allocConfdValue()
    res = value.ConfdValueLow.shallowConvertPyValueToConfdValue(lowerRangeVal, confdLowerRangeVal)
    if res != ReturnCodes.kOk:
        for logFunc in pyconfdlib._log("confd-register-range-action-cb-with-values-convert-lower-vailed").errorFunc(): logFunc("confd_register_action_cb shallowConvertPyValueToConfdValue(lower) failed: lowerRangeVal=%s, upperRangeVal=%s",
                                                                                      lowerRangeVal, upperRangeVal)
        return pyconfdlib.CONFD_ERR
    confdUpperRangeVal = value.ConfdValueLow.allocConfdValue()
    res = value.ConfdValueLow.shallowConvertPyValueToConfdValue(upperRangeVal, confdUpperRangeVal)
    if res != ReturnCodes.kOk:
        for logFunc in pyconfdlib._log("confd-register-range-action-cb-with-values-convert-upper-vailed").errorFunc(): logFunc("confd_register_action_cb shallowConvertPyValueToConfdValue(upper) failed: lowerRangeVal=%s, upperRangeVal=%s",
                                                                                      lowerRangeVal, upperRangeVal)
        return pyconfdlib.CONFD_ERR

    for logFunc in pyconfdlib._log("confd-register-range-action-cb-with-values").debug3Func(): logFunc("confd_register_action_cb called with values: lowerRangeVal=%s, upperRangeVal=%s",
                                                              lowerRangeVal, upperRangeVal)
    res = pyconfdlib.dll.py_confd_register_range_action_cb(dctx.getPtr(), actionPoint, initPtr, abortPtr, actionPtr, confdLowerRangeVal, confdUpperRangeVal, fmt)

    value.ConfdValueLow.deallocConfdValue(confdUpperRangeVal)
    value.ConfdValueLow.deallocConfdValue(confdLowerRangeVal)
    return res

def confd_register_action_cb(dctx, actionPoint, initCb, actionCb, abortCb=0, callBackData=None):
    class CbWrapper:
        """
        A wrapper for the python callbacks supplied by the application.
        Wraps each value supplied by confd with a proper Python type, checks return type   
        """
        def __init__(self, callback, actionPoint, callBackData):
            self.callBack=callback
            self.actionPoint=actionPoint
            self.callBackData=callBackData
        # Used for callbacks with a single parameter: userInfo
        @pyconfdlib.exceptionGuard
        def func1 (self, userInfo):
            for logFunc in pyconfdlib._log("confd_register_data_cb-func1-called").debug2Func(): logFunc("confd_register_data_cb::func1() called: userInfo=%s", userInfo)
            ret=self.callBack(pyconfdlib.ConfdUserInfoCtx(userInfo), self.actionPoint, self.callBackData)
            pyconfdlib.checkTypes({ret : pyconfdlib.ConfdReturnCode})
            return ret.getValue()
        # Used for callbacks with 5 parameters: userInfo, name, keypath, params & nuParams
        @pyconfdlib.exceptionGuard
        def func2 (self, userInfo, name, confdKeypathPtr, params, numParams):
            for logFunc in pyconfdlib._log("confd_register_data_cb-func2-called").debug2Func(): logFunc("confd_register_data_cb::func2() called: userInfo=%s, name=%s, confdKeypathPtr=%s, params=%s, numParams=%s",
                                                               userInfo, name, confdKeypathPtr, params, numParams)
            if params or numParams != 0:
                for logFunc in pyconfdlib._log("confd_register_data_cb-func2-params-not-supported").errorFunc(): logFunc("confd_register_data_cb::func2() called with params - not supported!!!. userInfo=%s, name=%s, confdKeypathPtr=%s, params=%s, numParams=%s",
                                                                                userInfo, name, confdKeypathPtr, params, numParams)
            pyKeyPath = key_path.KeyPath()
            ret = key_path.ConfdHKeyPathLow.deepConvertConfdHKeyPathToPyKeyPath(confdKeypathPtr, pyKeyPath)
            if ret != ReturnCodes.kOk:
                for logFunc in pyconfdlib._log("confd_register_data_cb-func2-failed-convert").errorFunc(): logFunc("confd_register_data_cb::func2() deepConvertConfdHKeyPathToPyKeyPath() failed: userInfo=%s, name=%s, confdKeypathPtr=%s, params=%s, numParams=%s, ret=%s",
                                                                   userInfo, name, confdKeypathPtr, params, numParams, ret)
                return pyconfdlib.CONFD_ERR
            ret=self.callBack(pyconfdlib.ConfdUserInfoCtx(userInfo), self.actionPoint, self.callBackData, name, pyKeyPath, params, numParams)
            pyconfdlib.checkTypes({ret : pyconfdlib.ConfdReturnCode})
            return ret.getValue()

    class ActionFinisher:
        """
        Wraps finish() methods to free objects stored by ConfdUserInfoCtx::setOpaque()
        """
        def __init__(self, callback, actionPoint, callBackData):
            self.callBack=callback
            self.actionPoint=actionPoint
            self.callBackData=callBackData
        # Used for callbacks with a single parameter: userInfo
        @pyconfdlib.exceptionGuard
        def func1 (self, userInfo):
            for logFunc in pyconfdlib._log("confd_register_data_cb-func1-called").debug2Func(): logFunc("confd_register_data_cb::func1() called: userInfo=%s", userInfo)
            userInfoCtx = pyconfdlib.ConfdUserInfoCtx(userInfo)
            ret=self.callBack(userInfoCtx, self.actionPoint, self.callBackData)
            pyconfdlib.checkTypes({ret : pyconfdlib.ConfdReturnCode})
            userInfoCtx.freeOpaque()
            return ret.getValue()

    if not pyconfdlib.checkTypes({dctx : pyconfdlib.ConfdDaemonCtx, actionPoint : str}):
        return pyconfdlib.CONFD_BAD_PYTHON_USAGE

    # TODO(orens) check that callbacks are indeed callable

    wrapperInit=0 # By default, we register a NULL function pointer
    if initCb:
        wrapperInit=CbWrapper(initCb, actionPoint, callBackData).func1
    initPtr=pyconfdlib.ConfdActionpointInitFuncType(wrapperInit)
    dctx.dontGcMe(initPtr)  # Protect against GC as long as this context is alive

    wrapperAbort=0 # By default, we register a NULL function pointer
    if abortCb:
        wrapperAbort=ActionFinisher(abortCb, actionPoint, callBackData).func1
    abortPtr=pyconfdlib.ConfdActionpointAbortFuncType(wrapperAbort)
    dctx.dontGcMe(abortPtr)  # Protect against GC as long as this context is alive

    wrapperAction=0 # By default, we register a NULL function pointer
    if actionCb:
        wrapperAction=CbWrapper(actionCb, actionPoint, callBackData).func2
    actionPtr=pyconfdlib.ConfdActionpointActionFuncType(wrapperAction)
    dctx.dontGcMe(actionPtr)  # Protect against GC as long as this context is alive

    return pyconfdlib.dll.py_confd_register_action_cb(dctx.getPtr(), actionPoint, initPtr, abortPtr, actionPtr)

def confd_data_reply_next_key(tctx, val, next):
    """
    values: a ConfdValues object, or None to signify no next key
    next: Value to supply as 'next' parameter in next callback invocation
    """

    if not pyconfdlib.checkTypes({tctx : pyconfdlib.ConfdTransContext}):
        return pyconfdlib.CONFD_BAD_PYTHON_USAGE

    if val == None:
        return pyconfdlib.dll.py_confd_data_reply_next_key(tctx.getCtypePtr(), None, -1, -1)
    else:
        if not pyconfdlib.checkTypes({val : value.Value, next : int}):
            return pyconfdlib.CONFD_BAD_PYTHON_USAGE

        confdValPtr = value.ConfdValueLow.allocConfdValue()
        res = value.ConfdValueLow.shallowConvertPyValueToConfdValue(val, confdValPtr)
        if res != ReturnCodes.kOk:
            for logFunc in pyconfdlib._log("confd-data-reply-next-key-convert-failed").errorFunc(): logFunc("shallowConvertPyValueToConfdValue(val=%s, confdValPtr=%s) res=%s", val, str(confdValPtr), str(res))
            return ReturnCodes.kGeneralError

        res = pyconfdlib.dll.py_confd_data_reply_next_key(tctx.getCtypePtr(), confdValPtr, 1, next)

        value.ConfdValueLow.deallocConfdValue(confdValPtr)

        return res

def confd_data_reply_value(tctx, val):
    """
    value: a single value
    """

    if not pyconfdlib.checkTypes({tctx : pyconfdlib.ConfdTransContext, val : value.Value}):
        return pyconfdlib.CONFD_BAD_PYTHON_USAGE

    confdValPtr = value.ConfdValueLow.allocConfdValue()
    res = value.ConfdValueLow.shallowConvertPyValueToConfdValue(val, confdValPtr)
    if res != ReturnCodes.kOk:
        for logFunc in pyconfdlib._log("confd-data-reply-value-shallow-convert-failed").errorFunc(): logFunc("shallowConvertPyValueToConfdValue(val=%s, confdValPtr=%s) res=%s", val, str(confdValPtr), str(res))
        return ReturnCodes.kGeneralError

    res = pyconfdlib.dll.py_confd_data_reply_value(tctx.getCtypePtr(), confdValPtr)

    value.ConfdValueLow.deallocConfdValue(confdValPtr)

    return res

def cdb_get(sock, val, fmt):
    """Fills a generic value object with data from the CDB"""
    # pyconfdlib.checkTypes() cannot check value. Oh well.
    if not pyconfdlib.checkTypes({sock : socket.socket, fmt : str}):
        return pyconfdlib.CONFD_BAD_PYTHON_USAGE

    confdVal = value.ConfdValueLow.allocConfdValue()
    res = pyconfdlib.dll.py_cdb_get(sock.fileno(), confdVal, fmt)
    if res != pyconfdlib.CONFD_OK:
        for logFunc in self._log("cdb-get-failed").errorFunc():
            logFunc("py_cdb_get() failed. sock=%d, fmt=%s, res=%s", sock, fmt, res)
        return ReturnCodes.kGeneralError
    res = value.ConfdValueLow.deepConvertConfdValueToPyValue(confdVal, val)
    if res != ReturnCodes.kOk:
        for logFunc in self._log("cdb-get-convert-failed").errorFunc():
            logFunc("cdb_get - deepConvertConfdValueToPyValue() failed. sock=%d, fmt=%s, confdVal=%s, res=%s",
                   sock, fmt, value.ConfdValueLow.ConfdValueToStr(confdVal), res)
        return ReturnCodes.kGeneralError

    value.ConfdValueLow.deallocConfdValue(confdVal)
    return ReturnCodes.kOk

def cdb_diff_iterate(sock, subid, iter, flags):
    """Iterates a transaction based on subid, calling the callback for each change"""
    if not pyconfdlib.checkTypes({sock : socket.socket, subid : int, flags : [pyconfdlib.ConfdIterFlags, int]}):
        return pyconfdlib.CONFD_BAD_PYTHON_USAGE

    # TODO(orens) check that iter is indeed callable

    class IterWrapper:
        """
        A wrapper for the python callback supplied by the application.
        Wraps each value supplied by confd with a proper Python type   
        """
        def __init__(self, logger, callback):
            self.myCallBack=callback
            self._log=logger

        @pyconfdlib.exceptionGuard
        def func (self, confdKeypathPtr, iterOp, oldv, newv):
            for logFunc in self._log("cdb-diff-iterate-iter-wrapper-got").debug3Func(): logFunc("cdb_diff_iterate cb got: confdKeypathPtr=%s, oldv=%s, newv=%s", confdKeypathPtr, oldv, newv)

            try:
                pyOldVal = None
                pyNewVal = None
                if oldv:
                    pyOldVal = value.Value()
                    res = value.ConfdValueLow.deepConvertConfdValueToPyValue(oldv, pyOldVal)
                    if res != ReturnCodes.kOk:
                        for logFunc in self._log("cdb-diff-iterate-iter-wrapper-deep-convert-old").errorFunc():
                            logFunc("deepConvertConfdValueToPyValue() failed. confdKeypathPtr=%s, oldv=%s, pyOldVal=%s, res=%s", confdKeypathPtr, str(oldv), pyOldVal, str(res))
                        return pyconfdlib.CONFD_ERR.getValue()
                if newv:
                    pyNewVal = value.Value()
                    res = value.ConfdValueLow.deepConvertConfdValueToPyValue(newv, pyNewVal)
                    if res != ReturnCodes.kOk:
                        for logFunc in self._log("cdb-diff-iterate-iter-wrapper-deep-convert-new").errorFunc():
                            logFunc("deepConvertConfdValueToPyValue() failed. confdKeypathPtr=%s, newv=%s, pyNewVal=%s, res=%s",
                                   key_path.ConfdHKeyPathLow.ConfdHKeyPathToStr(confdKeypathPtr), value.ConfdValueLow.ConfdValueToStr(newv), pyNewVal, str(res))
                        return pyconfdlib.CONFD_ERR.getValue()

                pyKeyPath = key_path.KeyPath()
                ret = key_path.ConfdHKeyPathLow.deepConvertConfdHKeyPathToPyKeyPath(confdKeypathPtr, pyKeyPath)
                if ret != ReturnCodes.kOk:
                    for logFunc in self._log("cdb-diff-iterate-iter-wrapper-failed-convert").errorFunc():
                        logFunc("deepConvertConfdHKeyPathToPyKeyPath() failed. confdKeypathPtr=%s, newv=%s, pyNewVal=%s, ret=%s", confdKeypathPtr, str(newv), pyNewVal, ret)
                ret=self.myCallBack(pyKeyPath, pyconfdlib.ConfdIterOp.getByValue(iterOp), pyOldVal, pyNewVal)
                pyconfdlib.checkTypes({ret : pyconfdlib.ConfdIterRet})
                return ret.getValue()
            except:
                self._log("cdb-diff-iterate-iter-wrapper-bad", isForceExceptionInfo=True)\
                    .error("Got exception from cdb_diff_iterate iterator: %s", traceback.format_exc())
                return pyconfdlib.CONFD_ERR.getValue()

    iterWrapper=IterWrapper(pyconfdlib._log, iter)
    flagsValue=flags
    if isinstance(flags, pyconfdlib.ConfdIterFlags):
        flagsValue=flags.getValue()

    return pyconfdlib.dll.py_cdb_diff_iterate(sock.fileno(), subid, pyconfdlib.CdbDiffIterFuncType(iterWrapper.func), flagsValue)

def confd_register_data_cb(dctx, callpoint, getElemCb=0, getNextCb=0, getObjCb=0, callBackData=None):
    class CbWrapper:
        """
        A wrapper for the python callbacks supplied by the application.
        Wraps each value supplied by confd with a proper Python type, checks return type   
        """
        def __init__(self, callback, callpoint, callBackData):
            self.callBack=callback
            self.callpoint=callpoint
            self.callBackData=callBackData
        # Used for callbacks with a single parameter: tctx
        @pyconfdlib.exceptionGuard
        def func1 (self, tctx, confdKeypathPtr):
            for logFunc in pyconfdlib._log("confd_register_data_cb-func1-called").debug2Func(): logFunc("confd_register_data_cb::func1() called: tctx=%s, confdKeypathPtr=%s", tctx, confdKeypathPtr)
            pyKeyPath = key_path.KeyPath()
            ret = key_path.ConfdHKeyPathLow.deepConvertConfdHKeyPathToPyKeyPath(confdKeypathPtr, pyKeyPath)
            if ret != ReturnCodes.kOk:
                for logFunc in pyconfdlib._log("confd_register_data_cb-func1-failed-convert").errorFunc(): logFunc("confd_register_data_cb::func1() deepConvertConfdHKeyPathToPyKeyPath() failed: tctx=%s, confdKeypathPtr=%s, ret=%s",
                                                                           tctx, confdKeypathPtr, ret)
                return pyconfdlib.CONFD_ERR
            ret=self.callBack(pyconfdlib.ConfdTransContext(tctx), self.callpoint, self.callBackData, pyKeyPath)
            pyconfdlib.checkTypes({ret : pyconfdlib.ConfdReturnCode})
            return ret.getValue()
        # Used for callbacks with 2 parameters: tctx,next
        @pyconfdlib.exceptionGuard
        def func2 (self, tctx, confdKeypathPtr, next):
            for logFunc in pyconfdlib._log("confd_register_data_cb-func2-called").debug2Func(): logFunc("confd_register_data_cb::func2() called: tctx=%s, confdKeypathPtr=%s, next=%s", tctx, confdKeypathPtr, next)
            pyKeyPath = key_path.KeyPath()
            ret = key_path.ConfdHKeyPathLow.deepConvertConfdHKeyPathToPyKeyPath(confdKeypathPtr, pyKeyPath)
            if ret != ReturnCodes.kOk:
                for logFunc in pyconfdlib._log("confd_register_data_cb-func2-failed-convert").errorFunc(): logFunc("confd_register_data_cb::func2() deepConvertConfdHKeyPathToPyKeyPath() failed: tctx=%s, confdKeypathPtr=%s, next=%s,ret=%s",
                                                                           tctx, confdKeypathPtr, next, ret)
                return pyconfdlib.CONFD_ERR
            ret=self.callBack(pyconfdlib.ConfdTransContext(tctx), self.callpoint, self.callBackData, pyKeyPath, next)
            pyconfdlib.checkTypes({ret : pyconfdlib.ConfdReturnCode})
            return ret.getValue()


    if not pyconfdlib.checkTypes({dctx : pyconfdlib.ConfdDaemonCtx, callpoint : str}):
        return pyconfdlib.CONFD_BAD_PYTHON_USAGE

    # TODO(orens) check that callbacks are indeed callable

    wrapper=0 # By default, we register a NULL function pointer
    if getElemCb:
        wrapper=CbWrapper(getElemCb, callpoint, callBackData).func1
    getElemPtr=pyconfdlib.ConfdDataGetElemFuncType(wrapper)
    dctx.dontGcMe(getElemPtr)  # Protect against GC as long as this context is alive

    getNextPtr=0
    if getNextCb:
        wrapper=CbWrapper(getNextCb, callpoint, callBackData).func2
    getNextPtr=pyconfdlib.ConfdDataGetNextFuncType(wrapper)
    dctx.dontGcMe(getNextPtr)

    getObjPtr=0
    if getObjCb:
        wrapper=CbWrapper(getObjCb, callpoint, callBackData).func1
    getObjPtr=pyconfdlib.ConfdDataGetObjFuncType(wrapper)
    dctx.dontGcMe(getObjPtr)

    res = pyconfdlib.dll.py_confd_register_data_cb(dctx.getPtr(), callpoint, getElemPtr, getNextPtr, getObjPtr)

    return res

def confd_register_transformation_data_cb(dctx, callpoint, getElemCb=0, getNextCb=0, setElemCb=0, createCb=0, removeCb=0, callBackData=None):
    class CbWrapper:
        """
        A wrapper for the python callbacks supplied by the application.
        Wraps each value supplied by confd with a proper Python type, checks return type   
        """
        def __init__(self, callback, callpoint, callBackData):
            self.callBack=callback
            self.callpoint=callpoint
            self.callBackData=callBackData
        # Used for callbacks with a 2 parameters: tctx, keypath
        @pyconfdlib.exceptionGuard
        def func1 (self, tctx, confdKeypathPtr):
            for logFunc in pyconfdlib._log("confd_register_data_cb-func1-called").debug2Func(): logFunc("confd_register_data_cb::func1() called: tctx=%s, confdKeypathPtr=%s", tctx, confdKeypathPtr)
            pyKeyPath = key_path.KeyPath()
            ret = key_path.ConfdHKeyPathLow.deepConvertConfdHKeyPathToPyKeyPath(confdKeypathPtr, pyKeyPath)
            if ret != ReturnCodes.kOk:
                for logFunc in pyconfdlib._log("confd_register_data_cb-func1-failed-convert").errorFunc(): logFunc("confd_register_data_cb::func1() deepConvertConfdHKeyPathToPyKeyPath() failed: tctx=%s, confdKeypathPtr=%s, ret=%s",
                                                                           tctx, confdKeypathPtr, ret)
                return pyconfdlib.CONFD_ERR
            ret=self.callBack(pyconfdlib.ConfdTransContext(tctx), self.callpoint, self.callBackData, pyKeyPath)
            pyconfdlib.checkTypes({ret : pyconfdlib.ConfdReturnCode})
            return ret.getValue()
        # Used for callbacks with 3 parameters: tctx, keypath, next
        @pyconfdlib.exceptionGuard
        def func2 (self, tctx, confdKeypathPtr, next):
            for logFunc in pyconfdlib._log("confd_register_data_cb-func2-called").debug2Func(): logFunc("confd_register_data_cb::func2() called: tctx=%s, confdKeypathPtr=%s, next=%s", tctx, confdKeypathPtr, next)
            pyKeyPath = key_path.KeyPath()
            ret = key_path.ConfdHKeyPathLow.deepConvertConfdHKeyPathToPyKeyPath(confdKeypathPtr, pyKeyPath)
            if ret != ReturnCodes.kOk:
                for logFunc in pyconfdlib._log("confd_register_data_cb-func2-failed-convert").errorFunc(): logFunc("confd_register_data_cb::func2() deepConvertConfdHKeyPathToPyKeyPath() failed: tctx=%s, confdKeypathPtr=%s, next=%s,ret=%s",
                                                                           tctx, confdKeypathPtr, next, ret)
                return pyconfdlib.CONFD_ERR
            ret=self.callBack(pyconfdlib.ConfdTransContext(tctx), self.callpoint, self.callBackData, pyKeyPath, next)
            pyconfdlib.checkTypes({ret : pyconfdlib.ConfdReturnCode})
            return ret.getValue()
        # Used for callbacks with a 3 parameters: tctx, keypath, value
        @pyconfdlib.exceptionGuard
        def func3 (self, tctx, confdKeypathPtr, confdValueTPtr):
            for logFunc in pyconfdlib._log("confd_register_data_cb-func3-called").debug2Func(): logFunc("confd_register_data_cb::func3() called: tctx=%s, confdKeypathPtr=%s, confdValueTPtr=%s", tctx, confdKeypathPtr, confdValueTPtr)
            pyKeyPath = key_path.KeyPath()
            ret = key_path.ConfdHKeyPathLow.deepConvertConfdHKeyPathToPyKeyPath(confdKeypathPtr, pyKeyPath)
            if ret != ReturnCodes.kOk:
                for logFunc in pyconfdlib._log("confd_register_data_cb-func3-failed-convert").errorFunc(): logFunc("confd_register_data_cb::func3() deepConvertConfdHKeyPathToPyKeyPath() failed: tctx=%s, confdKeypathPtr=%s, confdValueTPtr=%s, ret=%s",
                                                                           tctx, confdKeypathPtr, confdValueTPtr, ret)
                return pyconfdlib.CONFD_ERR
            pyValue = value.Value()
            ret = value.ConfdValueLow.deepConvertConfdValueToPyValue(confdValueTPtr, pyValue)
            if ret != ReturnCodes.kOk:
                for logFunc in pyconfdlib._log("confd_register_data_cb-func3-failed-convert").errorFunc(): logFunc("confd_register_data_cb::func3() deepConvertConfdValueToPyValue() failed: tctx=%s, confdKeypathPtr=%s, confdValueTPtr=%s, ret=%s",
                                                                           tctx, confdKeypathPtr, confdValueTPtr, ret)
                return pyconfdlib.CONFD_ERR
            ret=self.callBack(pyconfdlib.ConfdTransContext(tctx), self.callpoint, self.callBackData, pyKeyPath, pyValue)
            pyconfdlib.checkTypes({ret : pyconfdlib.ConfdReturnCode})
            return ret.getValue()


    if not pyconfdlib.checkTypes({dctx : pyconfdlib.ConfdDaemonCtx, callpoint : str}):
        return pyconfdlib.CONFD_BAD_PYTHON_USAGE

    # TODO(orens) check that callbacks are indeed callable

    wrapper=0 # By default, we register a NULL function pointer
    if getElemCb:
        wrapper=CbWrapper(getElemCb, callpoint, callBackData).func1
    getElemPtr=pyconfdlib.ConfdDataGetElemFuncType(wrapper)
    dctx.dontGcMe(getElemPtr)  # Protect against GC as long as this context is alive

    wrapper=0
    getNextPtr=0
    if getNextCb:
        wrapper=CbWrapper(getNextCb, callpoint, callBackData).func2
    getNextPtr=pyconfdlib.ConfdDataGetNextFuncType(wrapper)
    dctx.dontGcMe(getNextPtr)

    wrapper=0
    setElemPtr=0
    if setElemCb:
        wrapper=CbWrapper(setElemCb, callpoint, callBackData).func3
    setElemPtr=pyconfdlib.ConfdDataSetElemFuncType(wrapper)
    dctx.dontGcMe(setElemPtr)

    wrapper=0
    createPtr=0 # By default, we register a NULL function pointer
    if createCb:
        wrapper=CbWrapper(createCb, callpoint, callBackData).func1
    createPtr=pyconfdlib.ConfdDataCreateFuncType(wrapper)
    dctx.dontGcMe(createPtr)  # Protect against GC as long as this context is alive

    wrapper=0
    removePtr=0 # By default, we register a NULL function pointer
    if removeCb:
        wrapper=CbWrapper(removeCb, callpoint, callBackData).func1
    removePtr=pyconfdlib.ConfdDataRemoveFuncType(wrapper)
    dctx.dontGcMe(removePtr)  # Protect against GC as long as this context is alive

    res = pyconfdlib.dll.py_confd_register_transformation_data_cb(dctx.getPtr(), callpoint, getElemPtr, getNextPtr, setElemPtr, createPtr, removePtr)

    return res

