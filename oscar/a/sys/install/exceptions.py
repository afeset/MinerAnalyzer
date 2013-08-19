# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

class InstallException(Exception):
    """This exception should be used together with an error message that should be passed to the user"""

    def __init__ (self, errMsg):
        self.errMsg=errMsg

    def __str__ (self):
        return self.errMsg

    def getErrorMessage (self):
        return self.errMsg

class InvalidPackageFileException(InstallException):
    """This exception signals an invalid package file"""
    def __init__ (self):
        InstallException.__init__(self, "Invalid package file")

