#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: amiry
# 

from profile_manager import ProfileManager
from a.infra.basic.return_codes import ReturnCodes

if  __package__ is None:
    G_GROUP_NAME_PROFILE_LIST_MANAGER  = "unknown"
else:
    from . import G_GROUP_NAME_PROFILE_LIST_MANAGER


class ProfileListManager:
    """ Represent a list of content reporting profile entities. """

#-----------------------------------------------------------------------------------------------------------------------
    def __init__ (self, logger):
        self._log = logger.createLoggerSameModule(G_GROUP_NAME_PROFILE_LIST_MANAGER)
        self._configErrorMsgFunctor = None
        self._runningProfileList = {}
        self._candidateProfileList = {}

#-----------------------------------------------------------------------------------------------------------------------
    def setConfigMsgFunctor (self, functor):
        """ Sets the config error message functor - which will be used to report configuration error messages """
        def logAndCallFunctor (message):
            self._log("config-error-msg").debug2("error-msg-functor called with message: %s", message)
            functor(message)    
        self._configErrorMsgFunctor = logAndCallFunctor

#-----------------------------------------------------------------------------------------------------------------------
    def beginTransaction (self):
        self._log("begin-transaction").debug1("Begin transaction")
        self._candidateProfileList = self._runningProfileList.copy()
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def commitTransaction (self):
        self._log("commit-transaction").debug1("Commit transaction")
        self._runningProfileList = self._candidateProfileList.copy()
        self._candidateProfileList = {}
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def abortTransaction (self):
        self._log("abort-transaction").debug1("Abort transaction")
        self._candidateProfileList = {}
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def destroy (self):
        self._log("profile-list-destroy").debug2("Profile list destroy")
        # Do nothing. Blinky will call destroy on all childs.
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def getCandidateProfileList (self):
        self._log("get-candisate-profile-list").debug2("Get candidate profile list")
        if self._candidateProfileList:
            return self._candidateProfileList
        return self._runningProfileList

#-----------------------------------------------------------------------------------------------------------------------
    def createCandidateProfile (self, key):
        self._log("create-candidate-profile").debug2("Create candicate profile. key %s", key)

        if key in self._candidateProfileList:
            self._configErrorMsgFunctor("profile list already contains element with key %s" % key)
            return ReturnCodes.kGeneralError
        self._candidateProfileList[key] = ProfileManager(self._log)
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def deleteCandidateProfile (self, key):
        self._log("delete-candidate-profile").debug2("Delete profile. key %s", key)
        if not key in self._candidateProfileList:
            self._configErrorMsgFunctor("key %s is not in profile list" % key)
            return ReturnCodes.kGeneralError
        del self._candidateProfileList[key]
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def getCandidateProfile (self, key):
        self._log("get-candidate-profile").debug2("Get profile. key %s", key)
        profileList = self.getCandidateProfileList()
        if not key in profileList:
            self._configErrorMsgFunctor("key %s is not in profile list" % key)
            return None
        return profileList[key]

