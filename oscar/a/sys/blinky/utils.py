# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

import time

import a.infra.process.captain
from a.sys.confd.pyconfdlib import pyconfdlib

class Utils:
    @classmethod
    def fatalIfNotInstanceOf(cls, inst, class_, allowNone=False):
        __pychecker__ = 'no-argsused'   # cls is not used
        if allowNone and (inst==None):
            return
        if not isinstance(inst, class_):
            a.infra.process.processFatal("Object %s is not of class %s" % (inst, class_))

    @classmethod
    def getConfdErrStr(cls):
        __pychecker__ = 'no-argsused'   # cls is not used
        return "confd_errno=%s, confd_lasterr=%s."  % (pyconfdlib.get_confd_errno(), pyconfdlib.confd_lasterr())


# stupid pychecker does not understand inner classes, so we define this at global scope instead of inside Retry
# Todo(orens): Move this to infra/basic ?
class RetVal(object):
    def __init__ (self, ok, ret):
        self.__ok=ok
        self.__ret=ret

    def __str__ (self):
        return "{ok=%s, ret=%s}" % (self.__ok, self.__ret)

    def ok (self):
        return self.__ok

    def ret (self):
        return self.__ret

class Retry(object):
    def __init__ (self, logger):
        self._log=logger.createLogger("sys-blinky", "utils-retry")

    def callUntil (self, retryMe, maxRetries, retryIntervalMilli, successValue=None, successFunc=None):
        """ 
        Calls the 'retryMe' callable until it succeeds. 
        Upon failure, call is retried up to maxRetries, waiting retryIntervalMilli between calls.

        Success is determined like this:
        - If 'retryMe' raises an exception it is considered a failure.
        - The return value from 'retryMe', RET, is processed as follows:
        - If 'successValue' and successFunc are not specified, then success is determined by 
          evaluating RET in boolean context: True is a success, False is a failure.
        - If 'successValue' is specified, then success is declared as 'RET == successValue'
        - If 'successFunc' is specified, it is expected to be a callable. Success is determined by 
          evaluating successFunc(RET) in boolean context: True is a success, False is a failure.
        - If both 'successValue' and 'successFunc' are specified, then Success is declared as 
          'successFunc(RET) == successValue'

        Return value is an object with the following method: 
        - ok(): Returns True if the last retryMe() call was successfull, False if all calls failed.
        - ret() Returns the last return value returned by 'retryMe'. If all retryMe() attempts raised 
          an exception, returns the last exception raised.
        """


        currentTry=1
        ret=None  
        while currentTry<=maxRetries:
            try:
                for logFunc in self._log("call-until-calling").debug2Func(): logFunc("callUntil(), try # %d", currentTry)
                ret=retryMe()
                for logFunc in self._log("call-until-got").debug3Func(): logFunc("callUntil(), got ret=%s", ret)

                ret1=ret
                if successFunc != None:
                    ret1=successFunc(ret)
                    for logFunc in self._log("call-until-got-translated").debug3Func(): logFunc("callUntil(), successFunc() returned ret1=", ret1)

                if (successValue==None):
                    success=ret1
                else:
                    success = (ret1==successValue)

                # Success ? Return to caller
                if success:
                    for logFunc in self._log("call-until-done").debug2Func(): logFunc("callUntil(), success after %d calls", currentTry)
                    return RetVal(True, ret)
                else:
                    for logFunc in self._log("call-until-failed").debug2Func(): logFunc("callUntil() failed, got %s, retrying", ret)
            except Exception as ret:
                for logFunc in self._log("call-until-failed-retry").noticeFunc(): logFunc("callUntil() failed, got exception, retrying. Exception is: %s", str(ret))
            finally:
                time.sleep(retryIntervalMilli / 1000.0)
                if int(currentTry) == int(maxRetries/2):
                    for logFunc in self._log("call-until-failed-half").warningFunc(): logFunc("callUntil() failed after %d repetitions which are half of the max allowed (%d)", currentTry, maxRetries)
                currentTry=currentTry+1

        for logFunc in self._log("call-until-failed-final").errorFunc(): logFunc("callUntil() failed after %s retries, returning False", maxRetries)
        return RetVal(False, ret)


