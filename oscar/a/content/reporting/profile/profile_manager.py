#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: amiry
# 

from a.infra.basic.return_codes import ReturnCodes

if  __package__ is None:
    G_GROUP_NAME_PROFILE_MANAGER  = "unknown"
else:
    from . import G_GROUP_NAME_PROFILE_MANAGER

########################################################################################################################
# TODO(amiry) - TEMPORARY. This should come from Bliky
class ProfileData:

    def copyFrom (self, other):
        __pychecker__ = "unusednames=other"
        copiedProfile = ProfileData()
        return copiedProfile

########################################################################################################################

class ProfileManager:
    """ Represent a single content reporting profile entity. """

#-----------------------------------------------------------------------------------------------------------------------
    def __init__ (self, logger):
        self._log = logger.createLoggerSameModule(G_GROUP_NAME_PROFILE_MANAGER)
        self._runningProfile = ProfileData()
        self._candidateProfile = ProfileData()

#-----------------------------------------------------------------------------------------------------------------------
    def setConfigMsgFunctor (self, functor):
        """ Sets the config error message functor - which will be used to report configuration error messages """
        def logAndCallFunctor (message):
            self._log("config-error-msg").error(message)
            functor(message)
        self._configErrorMsgFunctor = logAndCallFunctor

#-----------------------------------------------------------------------------------------------------------------------
    def beginTransaction (self):
        self._candidateProfile.copyFrom(self._runningProfile)
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def commitTransaction (self):
        self._runningProfile.copyFrom(self._candidateProfile)
        self._candidateProfile = ProfileData()
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def abortTransaction (self):
        self._candidateProfile = ProfileData()
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def valueSet (self, profileData):
        if not self._validateCandidate(profileData):
            return ReturnCodes.kGeneralError
        self._candidateProfile.copyFrom(profileData)
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def destroy (self):
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def _validateCandidate (self, profileData):
        __pychecker__ = "unusednames=profileData"
        return ReturnCodes.kOk

