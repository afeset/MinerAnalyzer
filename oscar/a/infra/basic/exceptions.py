# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: effiz



class TimeOutException(Exception):
    def __init__ (self,caller,timeOut):
        self.msg = "'%s' timed out (timeout=%.2f)"%(caller,timeOut)

    def __str__ (self):
        return self.msg

class FunctionTimeOut(TimeOutException):
    def __init__ (self,functionCall,timeOut):
        self.functionCall = functionCall
        self.timeOut = timeOut
        TimeOutException.__init__(self,functionCall,timeOut)

