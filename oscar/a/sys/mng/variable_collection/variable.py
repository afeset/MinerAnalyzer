#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

if  __package__ is None:
    G_NAME_MODULE_SYS_MNG_VARIABLE_COLLECTION = "unknown"
    G_NAME_MODULE_SYS_MNG_VARIABLE_COLLECTION_VARIABLE = "unknown"
else:
    from . import G_NAME_MODULE_SYS_MNG_VARIABLE_COLLECTION
    from . import G_NAME_MODULE_SYS_MNG_VARIABLE_COLLECTION_VARIABLE

from a.infra.basic.return_codes import ReturnCodes

import os

class VariableData:
    def __init__ (self, name, value):
        self.name = name
        self.value = value

    def getAsString (self):
        return "(%s:=%s)"%(self.name, self.value)

class VariableStatus:
    def __init__ (self, actualValue, initialValue):
        self.actualValue = actualValue
        self.initialValue = initialValue

    def getActualValue (self):
        return self.actualValue

    def getInitialValue (self):
        return self.initialValue

class VariableBase (object):
    def __init__ (self, logger, name, fullName):
        self._fullName = fullName
        self._name = name
        self._log=logger.createLogger(G_NAME_MODULE_SYS_MNG_VARIABLE_COLLECTION, G_NAME_MODULE_SYS_MNG_VARIABLE_COLLECTION_VARIABLE, instance=fullName)
        self._variableData = None
        self._origValue = None        

    def getFullName (self):
        return self._fullName

    def getOrigValue (self):
        return self._origValue

    def setOrigValue (self, value):
        self._origValue = value

    def preparePrivateOnAdd (self):
        self._log("prepare-private-on-add").debug2("preparePrivateOnAdd() called")
        if not self._isSupportedByTarget():
            self._log("prepare-private-add-not-supported").error("variable %s is not supported", self.getFullName())
            return (ReturnCodes.kGeneralError, ("variable %s is not supported"%self.getFullName()))
        return (ReturnCodes.kOk, None)

    def preparePrivateValueSet(self, variableData):
        self._log("prepare-private").debug2("preparePrivateValueSet() called, data=%s", variableData.getAsString())

        if variableData.name is not None and variableData.name != self._name:
            self._log("name-to-path-mismatch").warning("name and path are different (%s Vs. %s)", self._name, variableData.name)            

        if self._origValue is None:
            #first time writing the variable. lets take the orig value
            (rc, val) = self._readTargetCurrentValue()
            if rc != ReturnCodes.kOk:
                self._log("prepare-private-cannot-read").error("failed to get orig value for variable %s. rc = %s", self.getFullName(), rc)
                return (ReturnCodes.kGeneralError, ("cannot read original value for %s"%self.getFullName()))

            self._log("orig-value").debug1("orig value for %s is %s", self.getFullName(), val)
            self._origValue = val

        self._log("prepare-private-done").debug2("preparePrivateValueSet() done")

        return (ReturnCodes.kOk, None)

    def commitPrivateValueSet(self, variableData):        
        self._log("commit-private").debug2("commitPrivateValueSet() called, data=%s", variableData.getAsString())

        self._variableData = variableData
        value = variableData.value
        if value == "":
            if self._origValue is None:
                self._log("set-to-default-no-orig-value").error("cannot set back '%s' to orig value, value unknown", self.getFullName())
                #NOT returning failure code as we do not want to crash the process
                return ReturnCodes.kOk
            else:
                value = self._origValue
                self._log("commit-private-write-orig-value").notice("setting '%s' to be '%s' (original value')", self.getFullName(), value)
        else:
            self._log("commit-private-write-value").notice("setting '%s' to be '%s' (original value is '%s')", self.getFullName(), value, self._origValue)

        rc = self._writeValueToTarget(value)
        if rc != ReturnCodes.kOk:
            self._log("commit-private-failed-write-value").error("failed to write value for variable %s. rc = %s", self.getFullName(), rc)
            #NOT returning failure code as we do not want to crash the process

        return ReturnCodes.kOk

    def commitPrivateOnDelete(self):        
        self._log("commit-private-before-deletion").debug2("commitPrivateBeforeDeletion() called, data=%s")
        if self._origValue is None:
            self._log("delete-no-orig-value").error("cannot set back '%s' to orig value, value unknown", self.getFullName())
            #NOT returning failure code as we do not want to crash the process
        else:
            self._log("commit-private-del").notice("setting '%s' to be '%s' (original value')", self.getFullName(), self._origValue)
            rc = self._writeValueToTarget(self._origValue)
            if rc != ReturnCodes.kOk:
                self._log("commit-private-delete-failed-write-value").error("failed to write value for variable %s. rc = %s", self.getFullName(), rc)
                #NOT returning failure code as we do not want to crash the process

        return ReturnCodes.kOk

    def getStatus (self):
        actualValue = None
        if self._variableData is None:
            self._log("get-actual-value-not-set").info("trying to get variable actual value when it is not set yet. variable %s", self.getFullName())
        else:            
            actualValue = self._variableData.value
            self._log("get-actual-value").debug2("get variable actual value: %s=%s", self.getFullName(), actualValue)

        initialValue = None
        if self._origValue is None:
            self._log("get-initial-value-not-set").info("trying to get variable initial value when it is not set yet. variable %s", self.getFullName())
        else:
            initialValue = self._origValue
            self._log("get-initial-value").debug2("get variable initial value: %s=%s", self.getFullName(), initialValue)
        return VariableStatus(actualValue, initialValue)

    #protected functions to be implemented by the derived classes
    def _isSupportedByTarget (self):
        return False

    def _readTargetCurrentValue (self):
        return (ReturnCodes.kGeneralError, None)

    def _writeValueToTarget (self, value):
        __pychecker__ = 'unusednames=value' 
        return ReturnCodes.kGeneralError


class PathVariable(VariableBase):
    def __init__ (self, logger, name, instanceName, pathPrefix):
        VariableBase.__init__(self, logger, name, instanceName)
        self._pathPrefix = pathPrefix

    def __getFullPath (self):
        return os.path.join(self._pathPrefix, self._name.replace('.','/'))#assuming self._name == self._variableData.name. we use this data before we have the _variableData (in _isSupportedByTarget)
        
    def _isSupportedByTarget (self):
        return os.path.exists(self.__getFullPath())

    def _readTargetCurrentValue (self):
        try:
            fd = open(self.__getFullPath(), "r")
            value = fd.read().strip()
            self._log("read-from-file").debug1("read from file '%s', the value '%s'", self.__getFullPath(), value)
            fd.close()
        except IOError as (errno, strerror):            
            self._log("failed-read-from-file").exception("Failed to read from file %s: I/O error(%d): {%s}", self.__getFullPath(), errno, strerror)
            return (ReturnCodes.kGeneralError, None)
        
        return (ReturnCodes.kOk, value)

    def _writeValueToTarget (self, value):
        self._log("write-to-file").debug1("writing to file '%s', the value '%s'", self.__getFullPath(), value)
        try:
            fd = open(self.__getFullPath(), "w")
            strToWrite = value+"\n"
            fd.write(strToWrite)            
            fd.close()
        except IOError as (errno, strerror):            
            self._log("failed-write-to-file").exception("Failed to write to file %s: I/O error(%d): {%s}", self.__getFullPath(), errno, strerror)
            return ReturnCodes.kGeneralError
        return ReturnCodes.kOk



