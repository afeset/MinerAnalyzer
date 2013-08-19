# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

import os
import a.infra.format.json

# TODO(orens): Why can't I simply write 'from exceptions import ...' ?
from a.sys.install.exceptions import InstallException


class StateManager(object):
    """
    The StateManager tracks the state of versions as installed in /opt/qb/rpms. The repos are not directly tracked
    by the StateManager

    ######################################################################################################
    NOTE: ALL state manager public funcs are part of the pilot API, changes must be strictly controlled !
    ######################################################################################################
    """

    kStateActive='active'  # The currently active version
    kStateReady='ready'    # Passed 'prepare', ready for switch
    kStateOnDisk='on-disk' # Found on disk for other reasons. Maybe only components are found, maybe RPMs as well.

    kTokenState='state'
    kTokenPilotName='pilot-name'
    kTokenPilotData='pilot-data'
    kTokenSubPkgs='subpkgs'
    kTokenSubPkgsToRemove='subpkgs-to-remove'
    kTokenRpmsToRemove='rpms-to-remove'
    kTokenLeaders='leaders'
    kTokenSwitchType='switch-type'               # String: 'OS Restart' or 'Application Restart'
    kTokenInstallDirection='install-direction'   # String: 'upgrade' or 'downgrade'

    kTokenVersions='versions'
    kTokenActivateOnStartup='activate-on-startup'
    kTokenLocked='locked'

    def __init__ (self, logger):
        self._log=logger.createLogger("sys-install","state-manager")
        self.versions={}
        self.versionToActivateOnStartup=None
        self._locked=False

    def setFile (self, file):
        """Should be called once after init"""
        self._raiseIfNotAbsPath(file, "file")
        self._stateFile=file
        self._stateFileNext=file+".next"

    def initialSetCurVersion (self, curVersion):
        """Should be called once after first install to init the state file"""
        self.versions={curVersion : {self.kTokenState : self.kStateActive}}
        self.save()

    def lockAndWriteNextStateFile (self, nextActiveVersion):
        """
        Locks the state, writes a state with the new active version to the .next file
        Locked means 'switch was performed, waiting for switch to occur'
        """
        # Write a new state with 'Locked':True
        self._locked=True
        self.save()
        # Write a state.next file with the new version as active, and without 'Locked':True
        self._stateFile = self._stateFileNext
        self._locked=False
        self.setActiveVersion(nextActiveVersion)
        # Remember that state is locked now
        self._locked=True

    def isLocked (self):
        return self._locked

    def getStateFileName (self):
        """Returns name of state file"""
        return self._stateFile

    def getStateFileNameNext (self):
        """Returns name of next state file"""
        return self._stateFileNext

    def startup (self):
        self._log("startup").info("startup() called")
        if self.versionToActivateOnStartup != None:
            vta=self.versionToActivateOnStartup
            self._log("startup").info("startup() activating version %s", vta)
            self.setActiveVersion(self.versionToActivateOnStartup)
            self.versionToActivateOnStartup=None
            self.save()

            # Patch to cover-up for a bug in 2.1.0: If current version has only a single component in the 'sub-packages'
            # list, copy the list from 'sub-packages-to-remove'
            subPkgs=self.getSubPkgs(vta)
            if len(subPkgs)==1:
                self.addSubPkgs(vta, self.getSubPkgsToRemoveOnRemoval(vta))

    def getVersions (self):
        """Returns list with current versions"""
        self._log("get-versions").info("getVersions() returning %s", self.versions.keys())
        return self.versions.keys()

    def setActiveVersion (self, version_):
        """Changes ready->active and active->on-disk"""
        self._log("set-active-version").info("setActiveVersion(version_=%s) called", version_)
        if version_ not in self.versions:
            self._log("set-active-version").error("setActiveVersion() called, version %s not found", version_)
            raise InstallException("Internal error detected in setActiveVersion()")
        if self.versions[version_][self.kTokenState] != self.kStateReady:
            self._log("set-active-version").error("setActiveVersion() called, version %s not ready, it is %s", 
                                                  version_, self.versions[version_][self.kTokenState])
            raise InstallException("Internal error detected in setActiveVersion()")
        curActive=self.getActiveVersion()
        self.versions[version_][self.kTokenState] = self.kStateActive
        self.versions[curActive][self.kTokenState] = self.kStateOnDisk
        self._log("set-active-version").info("setActiveVersion() called, version %s is now active, prev one was %s", 
                                               version_, curActive)
        self.save()

    def getActiveVersion (self):
        """Returns the currently active version"""
        for version_ in self.versions:
            if self.versions[version_][self.kTokenState] == self.kStateActive:
                return version_
        self._log("get-active-version").error("getActiveVersion() called, no active version found")
        raise InstallException("Internal error detected in getActiveVersion()")

    def setReadyVersion (self, version_):
        """Changes on-disk->ready"""
        self._log("set-active-version").info("setReadyVersion(version_=%s) called", version_)
        if version_ not in self.versions:
            self._log("set-ready-version").error("setReadyVersion() called, version %s not found", version_)
            raise InstallException("Internal error detected in setReadyVersion()")

        curReady=self.getReadyVersion()
        if curReady == version_:
            self._log("set-ready-version").info("setReadyVersion(%s) called, version is already ready, nothing to do ", version_)
            return

        if curReady != None:
            self._log("set-ready-version").error("setReadyVersion(%s) called, found a different ready version %s", 
                                                 version_, curReady)
            raise InstallException("Internal error detected in setReadyVersion()")

        curState=self.versions[version_][self.kTokenState]
        if curState != self.kStateOnDisk:
            self._log("set-ready-version").error("setReadyVersion() called, version %s not on disk, it is '%s'", version_, curState)
            raise InstallException("Internal error detected in setReadyVersion()")

        self.versions[version_][self.kTokenState]=self.kStateReady
        self._log("set-active-version").info("setReadyVersion() called, version %s is now ready", version_)
        self.save()

    def setVersionStateOnDisk (self, version_):
        """Changes version state to on-disk"""
        if version_ not in self.versions:
            self._log("set-version-state-ondisk").error("setVersionStateOnDisk() called, version %s not found", version_)
            raise InstallException("Internal error detected in setVersionStateOnDisk()")

        curState=self.versions[version_][self.kTokenState]
        self._log("set-version-state-ondisk").info("setVersionStateOnDisk() called, version %s current state is '%s'", version_, curState)
        if curState == self.kStateOnDisk:
            return

        self.versions[version_][self.kTokenState]=self.kStateOnDisk
        self._log("set-version-state-ondisk").info("setVersionStateOnDisk() called, version %s is now on-disk", version_)
        self.save()

    def getReadyVersion (self):
        """Returns the currently ready version, or None if no version is ready"""
        for version_ in self.versions:
            if self.versions[version_][self.kTokenState] == self.kStateReady:
                return version_
        return None

    def getVersionState (self, version_):
        """
        Returns the state of a given version, or None if no version is not known
        state is one of the kState... constants defined above
        """

        if version_ in self.versions:
            return self.versions[version_][self.kTokenState]
        return None

    def addVersion (self, version_, subPkgs=None, subPkgsToRemove=None, rpmsToRemove=None):
        """Adds a version with state 'on-disk' """
        curState=self.getVersionState(version_)
        if (curState == self.kStateActive) or (curState == self.kStateReady):
            self._log("add-version").error("addVersion() called, version %s already known, in state %s", version_, curState)
            raise InstallException("Internal error detected in addVersion()")

        self.versions[version_] = {self.kTokenState : self.kStateOnDisk}
        if subPkgs!=None:
            self.versions[version_][self.kTokenSubPkgs]=subPkgs
        if subPkgsToRemove!=None:
            self.versions[version_][self.kTokenSubPkgsToRemove]=subPkgsToRemove
        if rpmsToRemove!=None:
            self.versions[version_][self.kTokenRpmsToRemove]=rpmsToRemove

        self._log("add-version").info("addVersion() called, version %s added (subPkgs=%s, sptr=%s, rtr=%s)", version_, subPkgs, subPkgsToRemove, rpmsToRemove)
        self.save()

    def removeVersion(self, version_):
        """ Removes a version (Must have state != 'active') """
        if not version_ in self.versions:
            self._log("remove-version").error("removeVersion() called, version %s unknown", version_)
            raise InstallException("Internal error detected in removeVersion()")
        
        curState=self.versions[version_][self.kTokenState]
        if curState == self.kStateActive:
            self._log("remove-version").error("removeVersion() called, version %s is active", version_)
            raise InstallException("Internal error detected in removeVersion()")

        #TODO(orens): think about failing here instead of warning
        subPkgsToRemove=self.getSubPkgsToRemoveOnRemoval(version_)
        if len(subPkgsToRemove)>0:
            self._log("remove-version").warning("removeVersion() called, version %s has sub-pkgs to remove: %s", 
                                                version_, subPkgsToRemove)
        rpmsToRemove=self.getRpmsToRemoveOnRemoval(version_)
        if len(rpmsToRemove)>0:
            self._log("remove-version").warning("removeVersion() called, version %s has RPMs to remove: %s", 
                                                version_, rpmsToRemove)
        del self.versions[version_]
        self._log("remove-version").info("removeVersion() called, version %s removed", version_)
        self.save()

    def setPilotName (self, version_, pilotName):
        """ Sets pilot name for a given version. If pilotName==None, removes the pilot name"""
        if not version_ in self.versions:
            self._log("set-pilot-name").error("setPilotName() called, version %s unknown", version_)
            raise InstallException("Internal error detected in setPilotName()")
        self.versions[version_][self.kTokenPilotName]=pilotName
        if pilotName is None:
            del self.versions[version_][self.kTokenPilotName]
        self._log("set-pilot-name").info("setPilotName() called, version %s has pilotName=%s", 
                                                version_, pilotName)
        self.save()

    def getPilotName (self, version_):
        """ Gets pilot name. If none, returns None """
        if not version_ in self.versions:
            self._log("get-pilot-name").error("getPilotName() called, version %s unknown", version_)
            raise InstallException("Internal error detected in getPilotName()")
        return self.versions[version_].get(self.kTokenPilotName)

    def setPilotData (self, version_, pilotData):
        """ Sets pilot data for a given version. If pilotData==None, removes the pilot data """
        if not version_ in self.versions:
            self._log("set-pilot-data").error("setPilotData() called, version %s unknown", version_)
            raise InstallException("Internal error detected in setPilotData()")
        self.versions[version_][self.kTokenPilotData]=pilotData
        if pilotData is None:
            del self.versions[version_][self.kTokenPilotData]
        self._log("set-pilot-data").info("setPilotData(version=%s) called, pilotData set to='%s'", 
                                                version_, pilotData)
        self.save()

    def getPilotData (self, version_):
        """ Gets pilot data. If none, returns None """
        if not version_ in self.versions:
            self._log("get-pilot-data").error("getPilotData() called, version %s unknown", version_)
            raise InstallException("Internal error detected in getPilotData()")
        data = self.versions[version_].get(self.kTokenPilotData)
        self._log("get-pilot-data").info("getPilotData(version=%s) returning '%s'", version_, data)
        return data

    def setSwitchType (self, version_, switchType):
        """ Sets switch type for a given version. If switchType==None, removes the information """
        if not version_ in self.versions:
            self._log("set-switch-type").error("setSwitchType() called, version %s unknown", version_)
            raise InstallException("Internal error detected in setSwitchType()")
        self.versions[version_][self.kTokenSwitchType]=switchType
        if switchType is None:
            del self.versions[version_][self.kTokenSwitchType]
        self._log("set-switch-type").info("setSwitchType(version=%s) called, switchType set to='%s'", 
                                                version_, switchType)
        self.save()

    def getSwitchType (self, version_):
        """ Gets switch type. If none, returns None """
        if not version_ in self.versions:
            self._log("get-switch-type").error("getSwitchType() called, version %s unknown", version_)
            raise InstallException("Internal error detected in getSwitchType()")
        switchType = self.versions[version_].get(self.kTokenSwitchType)
        self._log("get-switch-type").info("getSwitchType(version=%s) returning '%s'", version_, switchType)
        return switchType
    
    def setInstallDirection (self, version_, installDirection):
        """ Sets install direction for a given version (upgrade or downgrade). If installDirection==None, removes the information """
        if not version_ in self.versions:
            self._log("set-install-direction").error("setInstallDirection() called, version %s unknown", version_)
            raise InstallException("Internal error detected in setInstallDirection()")
        self.versions[version_][self.kTokenInstallDirection]=installDirection
        if installDirection is None:
            del self.versions[version_][self.kTokenInstallDirection]
        self._log("set-install-direction").info("setInstallDirection(version=%s) called, installDirection set to='%s'", 
                                                version_, installDirection)
        self.save()

    def getInstallDirection (self, version_):
        """ Gets install direction. If none, returns None """
        if not version_ in self.versions:
            self._log("get-install-direction").error("getInstallDirection() called, version %s unknown", version_)
            raise InstallException("Internal error detected in getInstallDirection()")
        installDirection = self.versions[version_].get(self.kTokenInstallDirection)
        self._log("get-install-direction").info("getInstallDirection(version=%s) returning '%s'", version_, installDirection)
        return installDirection
        
    def addSubPkgs (self, version_, subPkgsToAdd):
        """ Adds subpkgs to a version """
        if not version_ in self.versions:
            self._log("add-subpkgs").error("addSubPkgs() called, version %s unknown", version_)
            raise InstallException("Internal error detected in addSubPkgs()")
        # Version must have some sub packages already
        subPkgs=self.versions[version_][self.kTokenSubPkgs]
        for sb in subPkgsToAdd:
            if not sb in subPkgs:
                subPkgs.append(sb)
        self._log("add-subpkgs").info("addSubPkgs(version=%s) called, sub-pkgs now are set to='%s'", 
                                                version_, subPkgs)
        self.save()

    def getSubPkgs (self, version_):
        """ Gets subpkgs related to this version """
        if not version_ in self.versions:
            self._log("get-subpkgs").error("getSubPkgs() called, version %s unknown", version_)
            raise InstallException("Internal error detected in getSubPkgs()")
        return self.versions[version_].get(self.kTokenSubPkgs, [])

    def setSubPkgsToRemoveOnRemoval (self, version_, subPkgsToRemove):
        """ Sets subpkgs to remove for a given version. Prev subpkgs to remove are forgotten """
        if not version_ in self.versions:
            self._log("set-subpkgs-to-remove").error("setSubPkgsToRemoveOnRemoval() called, version %s unknown", version_)
            raise InstallException("Internal error detected in setSubPkgsToRemoveOnRemoval()")
        self.versions[version_][self.kTokenSubPkgsToRemove]=subPkgsToRemove
        if (subPkgsToRemove is None) or (len(subPkgsToRemove)==0):
            del self.versions[version_][self.kTokenSubPkgsToRemove]
        self._log("set-subpkgs-to-remove").info("setSubPkgsToRemoveOnRemoval() called, version %s has subPkgsToRemove=%s", 
                                                version_, subPkgsToRemove)
        self.save()

    def getSubPkgsToRemoveOnRemoval (self, version_):
        """ Gets subpkgs to remove. If none, returns an empty list """
        if not version_ in self.versions:
            self._log("get-subpkgs-to-remove").error("getSubPkgsToRemoveOnRemoval() called, version %s unknown", version_)
            raise InstallException("Internal error detected in getSubPkgsToRemoveOnRemoval()")
        return self.versions[version_].get(self.kTokenSubPkgsToRemove, [])

    def setRpmsToRemoveOnRemoval (self, version_, rpmsToRemove):
        """ Sets RPMs to remove for a given version. Prev RPMs to remove are forgotten """
        if not version_ in self.versions:
            self._log("set-rpms-to-remove").error("setRpmsToRemoveOnRemoval() called, version %s unknown", version_)
            raise InstallException("Internal error detected in setRpmsToRemoveOnRemoval()")
        self.versions[version_][self.kTokenRpmsToRemove]=rpmsToRemove
        if (rpmsToRemove is None) or (len(rpmsToRemove)==0):
            del self.versions[version_][self.kTokenRpmsToRemove]
        self._log("set-rpms-to-remove").info("setRpmsToRemoveOnRemoval() called, version %s has rpmsToRemove=%s", 
                                                version_, rpmsToRemove)
        self.save()

    def getRpmsToRemoveOnRemoval (self, version_):
        """ Gets RPMs to remove. If none, returns an empty list """
        if not version_ in self.versions:
            self._log("get-rpms-to-remove").error("getRpmsToRemoveOnRemoval() called, version %s unknown", version_)
            raise InstallException("Internal error detected in getRpmsToRemoveOnRemoval()")
        return self.versions[version_].get(self.kTokenRpmsToRemove, [])

    def setLeaders (self, version_, leaders):
        """ 
        Sets leaders for a given version. 
        leaders is a dict with 'prepare' and 'switch' entries, mapping them to a full package name of the leader
        """
        if not version_ in self.versions:
            self._log("set-leaders").error("setLeaders() called, version %s unknown", version_)
            raise InstallException("Internal error detected in setLeaders()")
        self.versions[version_][self.kTokenLeaders]=leaders
        self._log("set-leaders").info("setLeaders() called, version %s has leaders=%s", version_, leaders)
        self.save()

    def getLeaders (self, version_):
        """ Gets leaders. """
        if not version_ in self.versions:
            self._log("get-leaders").error("getLeaders() called, version %s unknown", version_)
            raise InstallException("Internal error detected in getLeaders()")
        return self.versions[version_].get(self.kTokenLeaders)

    def save (self):
        data={self.kTokenVersions : self.versions}
        if self.versionToActivateOnStartup != None:
            data[self.kTokenActivateOnStartup] = self.versionToActivateOnStartup
        if self.isLocked():
            data[self.kTokenLocked] = True

        a.infra.format.json.writeToFile (self._log, data, self._stateFile, indent=4)
        self._log("save").info("save() wrote to file %s this: %s", self._stateFile, data)

    def load (self):
        """
        Loads state from file. If file does not exist or invalid, raises InstallException
        """

        self._log("load-called").info("load() called, reading state from %s", self._stateFile)

        if not os.path.exists(self._stateFile):
            self._log("load-no-file").error("load() called, no file '%s' found", self._stateFile)
            raise InstallException("State file not found: %s" % self._stateFile)

        dict_=a.infra.format.json.readFromFile(self._log, self._stateFile)
        if not self.kTokenVersions in dict_:
            self._log("load-invalid-text").error("load() could not find '%s'", self.kTokenVersions)
            raise InstallException("State file is invalid: %s " % self._stateFile)
        versions=dict_[self.kTokenVersions]

        # Parse versions into newVersions
        newVersions={}
        numActive=0
        numReady=0
        for version_ in versions:
            versionInfo=versions[version_]

            # state is checked thorrowly
            if not self.kTokenState in versionInfo:
                self._log("load-invalid-version").error("load() could not find state for version '%s'", version_)
                raise InstallException("State file is invalid: %s " % self._stateFile)
            state=versionInfo[self.kTokenState]
            if (state != self.kStateActive) and (state != self.kStateReady) and (state != self.kStateOnDisk):
                self._log("load-invalid-state").error("load() got invalid state '%s' for version '%s'", state, version_)
                raise InstallException("State file is invalid: %s " % self._stateFile)

            newVersions[version_]={self.kTokenState: state}
            newVersionInfo=newVersions[version_]
            if state == self.kStateActive:
                numActive += 1
            if state == self.kStateReady:
                numReady += 1

            # Other data is simple copied
            if self.kTokenPilotName in versionInfo:
                newVersionInfo[self.kTokenPilotName] = versionInfo[self.kTokenPilotName]
            if self.kTokenPilotData in versionInfo:
                newVersionInfo[self.kTokenPilotData] = versionInfo[self.kTokenPilotData]
            if self.kTokenSwitchType in versionInfo:
                newVersionInfo[self.kTokenSwitchType] = versionInfo[self.kTokenSwitchType]
            if self.kTokenInstallDirection in versionInfo:
                newVersionInfo[self.kTokenInstallDirection] = versionInfo[self.kTokenInstallDirection]

            if self.kTokenSubPkgsToRemove in versionInfo:
                newVersionInfo[self.kTokenSubPkgsToRemove] = versionInfo[self.kTokenSubPkgsToRemove]
            if self.kTokenRpmsToRemove in versionInfo:
                newVersionInfo[self.kTokenRpmsToRemove] = versionInfo[self.kTokenRpmsToRemove]

            if self.kTokenSubPkgs in versionInfo:
                newVersionInfo[self.kTokenSubPkgs] = versionInfo[self.kTokenSubPkgs]
            else:
                # 2.1.0.0 does not maintain the 'sub-packages' info. Hence, we 'guess' it :-)
                newVersionInfo[self.kTokenSubPkgs]=['qb-'+version_]

            if self.kTokenLeaders in versionInfo:
                newVersionInfo[self.kTokenLeaders] = versionInfo[self.kTokenLeaders]
            else:
                # 2.1.0.0 does not maintain the 'leaders' info. Hence, we 'guess' it :-)
                newVersionInfo[self.kTokenLeaders]={'prepare':'qb-leader-prepare-'+version_, 'switch':'qb-leader-switch-'+version_}

        if (numActive != 1) or (numReady > 1):
            self._log("load-invalid-states").error("load() found %s active versions, %s ready versions, impossible", 
                                                   numActive, numReady)
            raise InstallException("State file is invalid: %s " % self._stateFile)

        # Check 'versionToActivateOnStartup'
        newVersionToActivate=None
        if self.kTokenActivateOnStartup in dict_:
            newVersionToActivate=dict_[self.kTokenActivateOnStartup]
            if not newVersionToActivate in newVersions:
                self._log("load-invalid-vta").error("load() found invalid version to activate = '%s', not in list", 
                                                    newVersionToActivate)
                raise InstallException("State file is invalid: %s" % self._stateFile)
            vtaState=newVersions[newVersionToActivate][self.kTokenState]
            if vtaState != self.kStateReady:
                self._log("load-invalid-vta").error("load() found invalid version to activate = '%s', has state '%s', not ready", 
                                                    newVersionToActivate, vtaState)
                raise InstallException("State file is invalid: %s" % self._stateFile)

        # Check 'locked'
        newLocked=False
        if self.kTokenLocked in dict_:
            newLocked=True

        # Now that we are sure that the state we got is valid, we rememebr it
        self.versions=newVersions
        self.versionToActivateOnStartup=newVersionToActivate
        self._locked=newLocked
        self._log("load-got-state").info("load() got a new state: versions='%s', versionToActivateOnStartup='%s', locked=%s", 
                                         self.versions, self.versionToActivateOnStartup, self._locked)

    def patchChangeNameOfActiveVersion (self, newName):
        self._log("patch-change-name-active").info("patchChangeNameOfActiveVersion: new name=%s", newName)
        activeVersion = self.getActiveVersion()
        self.versions[newName] = self.versions[activeVersion]
        del self.versions[activeVersion]

    def _raiseIfNotAbsPath (self, pathToCheck, name):
        if not pathToCheck.startswith('/'):
            raise ValueError("%s must start with '/', value given is '%s'" % (name, pathToCheck))

