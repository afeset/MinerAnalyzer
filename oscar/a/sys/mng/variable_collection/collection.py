#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

if  __package__ is None:
    G_NAME_MODULE_SYS_MNG_VARIABLE_COLLECTION = "unknown"
    G_NAME_MODULE_SYS_MNG_VARIABLE_COLLECTION_COLLECTION = "unknown"
else:
    from . import G_NAME_MODULE_SYS_MNG_VARIABLE_COLLECTION
    from . import G_NAME_MODULE_SYS_MNG_VARIABLE_COLLECTION_COLLECTION


import os
from a.infra.basic.return_codes import ReturnCodes
import variable
import a.infra.process

class CollectionBase(object):
    ORIG_VALUES_FILE_DICT_KEY_VERSION = "file-version"
    ORIG_VALUES_FILE_DICT_KEY_ORIG_VALUES = "orig-values"

    def __init__ (self, logger, fullName):
        self._fullName = fullName
        self._log = logger.createLogger(G_NAME_MODULE_SYS_MNG_VARIABLE_COLLECTION, G_NAME_MODULE_SYS_MNG_VARIABLE_COLLECTION_COLLECTION, instance = fullName)
        # active map
        self._runningVariables = {}
        # candidate map (is consturcted of running map + changes made in the current transaction. only exists during a transaction
        self._candidateVariables = None
        self._origValuesFileName = None

    def initUseOrigValuesFile (self, fileName):
        self._origValuesFileName = fileName

    def getFullName (self):        
        return self._fullName

    def configStartTransaction (self):
        """
        duplicates the content of the running map to the candidate map
        """
        self._log("copy-running-to-candidate").debug2("copying running to candidate")
        for variable in self._runningVariables:
            self._log("specific-copy-running-to-candidate").debug4("copying running (%s: %s) to candidate", variable, self._runningVariables[variable])

        if self._runningVariables:
            self._candidateVariables = self._runningVariables.copy()
        else:
            self._candidateVariables = {}

        return ReturnCodes.kOk

    def configCommitTransaction (self):
        """
        duplicates the content of the running person map to the running person map and clear the candidate
        """

        self._log("commit").debug2("commit")

        if not self._origValuesFileName is None:
            self._log("write-orig-data-file").debug2("writing orig data file: %s", self._origValuesFileName)
            origValuesDictionary = {}
            for variableName in self._candidateVariables:
                origVal = self._candidateVariables[variableName].getOrigValue()
                self._log("specific-write-orig-data-file").debug4("writing orig for variable %s=%s", variableName, origVal)
                origValuesDictionary[variableName] = origVal
            dictionaryToWrite = {self.ORIG_VALUES_FILE_DICT_KEY_VERSION : 1,
                                 self.ORIG_VALUES_FILE_DICT_KEY_ORIG_VALUES : origValuesDictionary}
            try:
                a.infra.format.json.writeToFile(self._log, dictionaryToWrite, self._origValuesFileName, indent = 4)
            except:
                self._log("failed-write-orig").exception("failed to write orig values file")

        self._log("copy-candidate-to-running").debug2("copying candidate of len %d to running", len(self._candidateVariables))
        self._runningVariables = self._candidateVariables
        self._candidateVariables = None

        self._log("commit-done").debug2("commit done")
        return ReturnCodes.kOk

    def configAbortTransaction (self):
        """
        clears the candidate map
        """
        self._log("abort-candidate").debug2("aborting candidate")
        for variable in self._candidateVariables:
            self._log("specific-abort-candidate").debug4("aborting candidate (%s: %s)", variable, self._candidateVariables[variable])
        self._candidateVariables = None
        return ReturnCodes.kOk


    def prepareCandidateAddVariable(self, name):
        self._log("create").debug1("prepareCandidateAddVariable(): called. name=%s", name)
        if name in self._candidateVariables:
            self._log("name-already-exists").error("cannot re-add name: %s", name)
            return (ReturnCodes.kGeneralError, "cannot re-add variable: %s"%name)

        variable = self._createVariable(name)
        (rc, errorMsg) = variable.preparePrivateOnAdd()
        if (rc!=ReturnCodes.kOk) or errorMsg:
            self._log("prepare-add-failed").error("failed to prepare '%s' on add (%s): %s", name, rc, errorMsg)
            return (ReturnCodes.kGeneralError, errorMsg)
            
        if not self._origValuesFileName is None:
            if not os.path.exists(self._origValuesFileName):
                self._log("orig-file-not-exists").debug3("adding new variable '%s', not reading from orig file '%s' as it does not exists", name, self._origValuesFileName)
            else:
                try:
                    dictionaryRead = a.infra.format.json.readFromFile(self._log, self._origValuesFileName)
                    origValuesDictionary = dictionaryRead[self.ORIG_VALUES_FILE_DICT_KEY_ORIG_VALUES]
                except:
                    self._log("failed-read-orig").exception("faile to read orig value file '%s' while adding variable '%s'", self._origValuesFileName, name)
                    return (ReturnCodes.kGeneralError, "")
                else:
                    if name in origValuesDictionary:
                        self._log("set-orig-val").debug3("setting the orig value of variable '%s' to '%s' after reading it from file '%s'", 
                                                         name, origValuesDictionary[name], self._origValuesFileName)
                        variable.setOrigValue(origValuesDictionary[name])
                    else:
                        self._log("no-orig-val-in-file").debug3("not setting the orig value of variable '%s' as the dictionary in '%s' does not refer to it", 
                                                                name, self._origValuesFileName)
           

        self._candidateVariables[name]=variable

        # this return also covers phases that we don't need to support
        return (ReturnCodes.kOk, None)

    def getCandidateVariable(self, name):
        if name in self._candidateVariables:
            return self._candidateVariables[name]
        return None

    def prepareCandidateDeleteVariable(self, name):
        self._log("delete").debug1("prepareCandidateDeleteVariable(): called. name=%s", name)
        if name not in self._candidateVariables:
            self._log("name-not-exists").warning("trying to delete non existing name: %s", name)
            return (ReturnCodes.kOk, None)
        self._candidateVariables.pop(name)

        return (ReturnCodes.kOk, None)

    #functions to be implemented by the derived class
    def _createVariable (self, name):
        return None


class PathVariablesCollection(CollectionBase):

    def __init__ (self, logger, pathPrefix):
        CollectionBase.__init__(self, logger, pathPrefix)
        self._pathPrefix = pathPrefix

    def _createVariable (self, name):
        return variable.PathVariable(self._log, name, self.getFullName()+"/"+name, self._pathPrefix)

