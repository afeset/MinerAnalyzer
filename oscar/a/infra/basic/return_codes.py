# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

# This Python class mimics the basic::ReturnCodes class

from a.infra.misc.enum_with_value import EnumWithValue

class ReturnCode (EnumWithValue):
    """contains a single return code"""
    def __init__ (self, value, name):
        EnumWithValue.__init__(self, value, name)

    def success (self):
        return self.getValue() >= 0



class ReturnCodes (object):
    """ Standard error codes. We keep the numerical values identical to the C++ values, for peace of mind """
    kOk = ReturnCode(0, "kOk")
    kGeneralError = ReturnCode(-1, "kGeneralError")
    kNotFound = ReturnCode(-2, "kNotFound")
    kNoRoom = ReturnCode(-3, "kNoRoom")
    kTimeOut = ReturnCode(-4, "kTimeOut")
    kBadParameter = ReturnCode(-5, "kBadParameter")
    kBadState = ReturnCode(-6, "kBadState")
    kUnSupported = ReturnCode(-7, "kUnSupported")
    kAlreadyExists = ReturnCode(-8,"kAlreadyExists")



