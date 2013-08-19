# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

# This Python class wraps a single object to make it easy to pass variables 'by ref'

class PassByRef(object):
    def __init__ (self, value=None):
        self._myValue=value

    def value (self):
        return self._myValue

    def setValue (self, value):
        self._myValue=value

    def __str__ (self):
        return str(self._myValue)


