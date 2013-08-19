# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

# Base class for enums with name and value
#
# Derived classes only need to define __init__.
# 
# EnumWithValue values can be compared only with EnumWithValue values of the same class

class EnumWithValue(object):

    @classmethod
    def initOurDict (cls):
        if '_ourDict' not in cls.__dict__:
            cls._ourDict={}

    @classmethod
    def iteritems(cls):
        """
        Gets an iterable object over all enumerated objects.
        """
        return cls._ourDict.values()

    @classmethod
    def getByValue (cls, value):
        """
        Gets an enumerated object by a numeric value.
        If value is not defined in this class, returne None
        """
        if cls.isValueValid(value):
            return cls._ourDict[value]
        return None

    @classmethod
    def isValueValid (cls, value):
        """
        If value is defined in this class, returns True
        Otherwise, returns False
        """
        return value in cls._ourDict

    def __init__ (self, value, name):
        __pychecker__ ='no-classattr'
        self._myValue = value
        self._myName = name
        self.initOurDict()
        self._ourDict[value] = self


    def getValue (self):
        return self._myValue

    def getName (self):
        return self._myName

    def __str__ (self):
        return str(self._myName)

    def __repr__ (self):
        return '%s(%r)' % (self.__class__.__name__, str(self))

    def __eq__ (self, other):
        self._raiseIfOtherIsNotSameClass(other)
        return self._myValue == other._myValue

    def __ne__ (self, other):
        self._raiseIfOtherIsNotSameClass(other)
        return self._myValue != other._myValue

    def __ge__ (self, other):
        self._raiseIfOtherIsNotSameClass(other)
        return self._myValue >= other._myValue

    def __gt__ (self, other):
        self._raiseIfOtherIsNotSameClass(other)
        return self._myValue > other._myValue

    def __le__ (self, other):
        self._raiseIfOtherIsNotSameClass(other)
        return self._myValue <= other._myValue

    def __lt__ (self, other):
        self._raiseIfOtherIsNotSameClass(other)
        return self._myValue < other._myValue

    # Allow comparing enums only if they are of the same class
    # Comaring enums from different classes is an abomination
    def _raiseIfOtherIsNotSameClass (self, other):
        if self.__class__ != other.__class__:
            raise TypeError("other is of type %s (%s), should be of type %s (%s)" % (other.__class__, other , self.__class__, self))

