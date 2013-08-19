# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

import re
import os, sys
import json
 
from a.sys.boot.utils import BootUtils
from a.sys.platform_basic.platform_basic import PlatformBasic
from a.sys.secure_digital.utils import SdUtils
from a.sys.install.exceptions import InstallException
from a.sys.install.exceptions import InvalidPackageFileException
from a.sys.install.utils import Utils
from sub_pkg_manager import SubPkgManager
from pilot_services import PilotServices
from state_manager import StateManager
from yum.yum import Yum
from rpm.rpm import Rpm
import a.api.user_log.msg.install
import a.infra.process

kFakeBuildNumber = "99999999"

"""
Here is the story of how we manage the installed versions:
StateManager holds a dict for each version. Each version has the following data:
- state: May be 'active', 'ready', or 'on-disk'.
- sub-packages: List of sub-packages that this version depends on. By 'depends on' we mean 'needs them for proper installation'.
     The sub-packages include the repository from which this version came from, and the RFS and kernel sub-packages that it needs.
- sub-packages-to-remove: List of the sub-packages that were added during the 'prepare' of this version. If
     the prepare is canceled, these sub-packages are deleted.
- rpms-to-remove: List of RPMs installed on the current RFS during the 'prepare' of this version. If the
     prepare is canceled, these rpms are deleted
- leaders: List of leaders of this version. Together, they make up all the RPMs this version required in order to work.

Various operations do this:

addSubPkgs() / addSubPkgsFromHttp(): 
- Extract sub-packages for some version from the file/http
- Create a new version in the state manager, with the following attributes:
  state: on-disk
  sub-packages: The sub-package from which this vesion was installed
  sub-packages-to-remove: List of sub-packages added by this version during 'add'

removeVersionAndSubPkgs(): This is the opposite of the add...() functions.  
- Remove the sub-packages added by this version during the add...() function,
- Remove the version itself from the state table

prepare():
- Install pilots of active and new versions
- Select pilot
- Run pilot.doPrepare()
  Pilot does this:
  - Update version state sub-pkgs with the RFS/Kernel sub-packages required by this version
- Update state of version like this:
  state: ready
  rpms-to-remove: List of RPMs just installed by pilot

cancel(): This is the opposite of the prepare() function
- Find the (single) ready version that should be removed
- Deletes rpms-to-remove of that version
- Sets state of this version to 'on-disk'

removeUnneededVersionsFromDisk():
- Scan all versions in state 'on-disk'
- Find all sub-pkgs and rpms of these versions, which are not needed by current active/ready versions, or by versions
  we may rollback to. 
  We use the 'sub-pkgs' list of each version as found in the state, hence the active/ready versions
  make sure we do not remove sub-pkgs which they need.
- Remove all RPMs and sub-pkgs found from the disk, and the (on-disk) versions themselves from the state table

"""

class InstallManager(object):
    """
    This is the main install manager
    """

    def __init__ (self, logger, product, sysVarDir, sysRunDir, dataVarDir, rpmsDir, 
                  appDir, appDirReal, bootDevPath, grubConf, prevRfsDir=None, vitalDir=None, systemRoot="/", useFakeChrootMode=False):
        """
        product : Name of product we handle, e.g. 'qb'.
        sysVarDir : path to sys dir relative to root, e.g. '/opt/qb/sys/oscar/install/0/var'. 
        sysRunDir : path to sys dir relative to root, e.g. '/opt/qb/sys/oscar/install/0/run'. 
        dataVarDir : path to data dir relative to root, e.g. '/opt/qb/data/oscar/install/0/var'. 
        rpmsDir : path to rpms dir relative to root, e.g. '/opt/qb/rpms'. 
        appDir : path to app dir relative to root, e.g. '/opt/qb/app'. 
        appDirReal : real path to app dir relative to root, e.g. '/opt/qb/sys/rfs/sys/0/var/app'. 
        bootDevPath : Path to boot device, e.g. '/boot'
        grubConf : name of grub.conf file relative to boot device, e.g. 'grub/grub.conf'.
        systemRoot : For unit tests, specifies location of the file-system root.
        useFakeChrootMode : For unit tests, True to use fakechroot instead of chroot (via rpm --root or yum --installroot)
        prevRfsDir : Location to copy some RFS data to during OS install
        vitalDir : Path to vital dir.
        """

        self._raiseIfNotAbsPath(systemRoot, "systemRoot")
        self._log = logger.createLogger("sys-install", "install-manager")
        self._log.setInstance(product)
        self._utils = Utils(self._log)
        self._product = product
        self._bootDevPath = bootDevPath
        self._grubConf = grubConf
        self._systemRoot = systemRoot
        self._useFakeChrootMode = useFakeChrootMode
        self._vitalDir = vitalDir

        self._rpmsDir = os.path.join(systemRoot, self._chopLeadingSlashIfFound(rpmsDir))

        self._sysVarDir = os.path.join(systemRoot, self._chopLeadingSlashIfFound(sysVarDir))
        self._sysRunDir = os.path.join(systemRoot, self._chopLeadingSlashIfFound(sysRunDir))
        self._dataVarDir = os.path.join(systemRoot, self._chopLeadingSlashIfFound(dataVarDir))
        self._logDir=os.path.join(self._dataVarDir, 'log')
        self._stateDir = os.path.join(self._sysVarDir, "state")
        self._yumConfActiveRfsDir = os.path.join(self._sysVarDir, "yum-conf-active-rfs")
        self._yumConfNewVersionDir = os.path.join(self._sysVarDir, "yum-conf-new-version")
        self._appDir = os.path.join(systemRoot, self._chopLeadingSlashIfFound(appDir))
        self._appDirReal = os.path.join(systemRoot, self._chopLeadingSlashIfFound(appDirReal))
        self._installDir = os.path.join(self._sysVarDir,"sub-pkgs")
        self._workDir=os.path.join(self._sysVarDir, 'work')
        self._apiDir=os.path.join(self._sysVarDir, 'api')
        self._startupScriptsDir=os.path.join(self._sysVarDir, 'startup')
        self._startupScriptsPrevDir=os.path.join(self._startupScriptsDir, 'prev')
        self._rpmKeysDir = os.path.join(self._sysVarDir, "rpm/keys")
        self._tempDir = os.path.join(self._sysRunDir, "tmp")
        self._installTempDir = os.path.join(self._tempDir, "sub-pkgs")  # install-temp can be cleared between runs
        self._subPkgManager = SubPkgManager(self._log)
        self._subPkgManager.setDirs(self._systemRoot, self._installDir, self._installTempDir, self._rpmKeysDir, self._useFakeChrootMode)

        self._stateFile = os.path.join(self._stateDir, product+"-state")
        self._stateManager = StateManager(self._log)
        self._stateManager.setFile(self._stateFile)
        self._pilotHints=""
        self._prevRfsDir = prevRfsDir
        self._preparedPackageFilePath = None

        self._log("init").info("InstallManager::__init__() called, self._product=%s, self._sysVarDir=%s, self._sysRunDir=%s, "\
                               "self._dataVarDir=%s, self._rpmsDir=%s, self._appDir=%s, self._bootDevPath=%s, "\
                               "self._grubConf=%s, self._prevRfsDir=%s, self._vitalDir=%s", 
                               self._product, self._sysVarDir, self._sysRunDir, self._dataVarDir, self._rpmsDir, 
                               self._appDir, self._bootDevPath, self._grubConf, self._prevRfsDir, self._vitalDir)

        # If true, we will not actually install RPMs. This helps modify this module in-box and testing the 
        # changes, to avoid having to create a package file each time
        self._debugNoInstallMode=False

    def unit_test_initializeSystemFirstInstall (self, curVersion, curBuild, keys):
        """
        Should be called once after first install to initialize the state file and keys.
        Used only by unit tests. In real life, the extract_pkg script does this.
        
        curVersion : Name of the current version
        curBuild : Name of the current build
        keys : listof paths to ascii armoured files with gpg keys for rpm validation
        """
        self.initializeSystemFirstInstall(curVersion, curBuild)
        
        # Import rpm keys
        rpm=self._createRpmForActiveRfs()
        for key in keys:
           rpm.doImport(key)


    def initializeSystemFirstInstall (self, curVersion, curBuild):
        """
        Should be called once after first install to initialize the state file and keys.
        
        curVersion : Name of the current version
        curBuild : Name of the current build
        """
        self._log("initial-set-cur-version").info("initialSetCurVersion() called, curVersion=%s", curVersion)
        
        # Create initial dirs
        self._utils.runCommandRaiseIfFail("mkdir -p "+self._stateDir)
        
        # Set initial state
        self._stateManager.initialSetCurVersion(self.combineVersion(curVersion, curBuild))



    def init (self):
        """
        Must be called after creating this object, to initialize it, on a system that has been initialized 
        (i.e. has a state file on disk)
        """
        self._log("init").info("init() called")
        
        # Make sure these dirs exist. If not, create them.
        self._utils.runCommandRaiseIfFail("mkdir -p "+self._sysRunDir)
        self._utils.runCommandRaiseIfFail("mkdir -p "+self._logDir)
        self._utils.runCommandRaiseIfFail("mkdir -p "+self._workDir)
        self._utils.runCommandRaiseIfFail("mkdir -p "+self._apiDir)        
        self._utils.runCommandRaiseIfFail("mkdir -p "+self._startupScriptsDir)
        self._utils.runCommandRaiseIfFail("mkdir -p "+self._startupScriptsPrevDir)

        #TODO(orens): catch InstallException that might be raised during load, reset state and restart oscar
        self._log("init").info("init() loading state")
        self._stateManager.load()

        self._initPlatformBasic()
        self._initSdUtils()
        self._initBootUtils()

    def isPendingRestart (self):
        """
        Returns true if 'switch' was executed, we are not waiting for system to restart.
        """
        return self._stateManager.isLocked()

    def setPilotHints (self, hints):
        self._log("setPilotHints").info("setPilotHints(hints=%s) called", hints)
        self._pilotHints = hints

    def startup (self, logDir = None):
        """
        Must be called during startup of an installed system, i,e, upon every Oscar start.
        Call this after callint init()
        When logDir is passed, the start-up script writes its logs into that directory, otherwise default directory is used.
        """
        self._log("startup").info("startup() called")

        #TODO(orens): In the future, when we do not need to support upgrading from EFT versions,
        # remove this call, and all the setVersionToActivateOnStartup() support from StateManager
        self._stateManager.startup()

        # Run all scripts from the startup dir, move them to 'prev' later
        self._log("startup-running").info("startup(): Scanning directory %s for startup scripts", self._startupScriptsDir)
        files=os.listdir(self._startupScriptsDir)
        for file_ in files:
            fullPath=os.path.join(self._startupScriptsDir, file_)

            if logDir is not None:
                startupCommand = fullPath + " --log-dir " + logDir
            else:
                startupCommand = fullPath

            # Do not run .tmp files or directories :-)
            if (not fullPath.endswith(".tmp")) and os.path.isfile(fullPath):
                self._log("startup-running").info("startup(): running startup script '%s'", startupCommand)
                # If script fails, raise and get out of here. This should fail oscar start
                self._utils.runCommandRaiseIfFail(startupCommand)
                # Move used script to 'prev' dir, to lay there forever shamed.
                self._utils.runCommandRaiseIfFail("mv -f %s %s" % (fullPath, self._startupScriptsPrevDir))

    def getActiveVersionAndBuild (self):
        """
        Returns the current active (version, build)
        """
        self._log("get-active-version").info("getActiveVersionAndBuid() called")
        versionAndBuild=self._stateManager.getActiveVersion()
        (version_, build) = self.splitVersion(versionAndBuild)
        self._log("get-active-version").info("getActiveVersionAndBuid() got %s, returning %s, %s", 
                                             versionAndBuild, version_, build)
        return (version_, build)

    def getReadyVersion (self):
        """
        Returns (version, build) of currently ready version. 
        If no version is ready, returns None
        """
        versionCombined = self._stateManager.getReadyVersion()
        if versionCombined==None:
            return None

        (version_, build) = self.splitVersion(versionCombined, raiseIfInvalid=True)
        return (version_, build)

    def getReadyVersion2 (self):
        """
        Returns (version, build, switch type, install direction) of currently ready version. 
        If no version is ready, returns None
        """
        versionCombined = self._stateManager.getReadyVersion()
        if versionCombined==None:
            return None
        switchType = self._stateManager.getSwitchType(versionCombined)

        (version_, build) = self.splitVersion(versionCombined, raiseIfInvalid=True)
        return (version_, build, switchType)

    def getStateManager (self):
        return self._stateManager

    def getPreparedPackageFilePath (self):
        return self._preparedPackageFilePath
        
    def isPackageValid (self, fileName):
        """
        Checks that an RPM file is a signed, and contains a proper version for our product.
        Returns None if invalid, or (version, build) if valid
        """
        self._log("is-valid").info("isPackageValid(fileName=%s) called", fileName)
        if not self._isPackageSigned(fileName):
            self._log("is-valid").warning("isPackageValid() returning false, fileName=%s not signed", fileName)
            return None
        versionCombined = self._subPkgManager.findVersionInFile(self._product, fileName)
        if versionCombined is None:
            self._log("is-valid").warning("isPackageValid() returning false, no version of product %s found in it", self._product)
            return None
        (version_, build) = self.splitVersion(versionCombined)
        if version_ is None:
            self._log("is-valid").warning("isPackageValid() returning false, no version of product %s found in it", self._product)
            return None
        return (version_, build)

    def addSubPkgs (self, fileName):
        """
        Adds a package file to the repos. Raises InvalidPackageFileException if not a valid package file for this product

        Returns (version, build)
        """

        self._log("add").info("addSubPkgs(fileName=%s) called", fileName)
        self._raiseIfNotAbsPath(fileName, "fileName")

        valid=self._isPackageSigned(fileName)
        if not valid:
            self._log("add-bad-rpm").error("addSubPkgs() got bad package file, not properly signed", self._product)
            raise InvalidPackageFileException()

        versionCombined = self._subPkgManager.findVersionInFile(self._product, fileName)
        if versionCombined is None:
            self._log("add-bad-version").error("addSubPkgs() got bad package file, no version of product %s found in it", self._product)
            raise InvalidPackageFileException()
        (version_, build) = self.splitVersion(versionCombined)
        if version_ is None:
            self._log("add-bad-version").error("addSubPkgs() got versionInFile '%s', cannot split.", versionCombined)
            raise InvalidPackageFileException()

        # Check if version is active or ready. If yes, raise exception
        self._raiseIfVersionActiveOrReady(versionCombined)

        # Extract package file into sub-pkgs dir
        (subPkgs, newSubPkgs)=self._subPkgManager.add(fileName)
        self._log("add-got-subpkgs").info("addSubPkgs() returning newSubPkgs=%s", newSubPkgs)

        self._stateManager.addVersion(versionCombined, subPkgs=subPkgs, subPkgsToRemove=newSubPkgs)

        # Remember the file path
        self._preparedPackageFilePath = fileName

        self._log("add").info("addSubPkgs() returning version=%s, build=%s", version_, build)
        return (version_, build)

    def addSubPkgsFromHttp (self, repoHttpAddr, version_, build):
        """
        Adds a package file to the repos. Raises InstallException if package not found.
        """

        self._log("add-from-http").info("addSubPkgsFromHttp(repoHttpAddr=%s, version_=%s, build=%s) called", repoHttpAddr, version_, build)

        versionCombined = self.combineVersion(version_, build)
        if versionCombined is None:
            self._log("add-from-http-bad-version").error("addSubPkgsFromHttp() got bad version(=%s) or build(=%s) parameters", version_, build)
            raise InstallException("Invalid version '%s', build '%s' specificaion" % (version_, build))

        # Check if version is active or ready. If yes, raise exception
        self._raiseIfVersionActiveOrReady(versionCombined)

        packageName = "%s-%s" % (self._product, versionCombined)
        self._log("add-from-http-package").info("addSubPkgsFromHttp(): installing package %s", packageName)

        # Extract package file into sub-pkgs dir
        (subPkgs, newSubPkgs)=self._subPkgManager.add(httpRepo=repoHttpAddr, packageName=packageName)
        self._log("add-from-http-got-subpkgs").info("addSubPkgsFromHttp() got newSubPkgs=%s", newSubPkgs)

        self._stateManager.addVersion(versionCombined, subPkgs=subPkgs, subPkgsToRemove=newSubPkgs)

        self._log("add-from-http-done").info("addSubPkgsFromHttp() done")

    def removeVersionAndSubPkgs (self, version_, build, removeSubPackages=True):
        """
        Removes sub-pkgs added by a version during 'prepare', and the version itself.
        Version must have state 'on-disk'
        """
        self._log("remove-subpkgs").info("removeVersionAndSubPkgs(version=%s, build=%s) called", version_, build)

        versionCombined = self.combineVersion(version_, build)
        versionState = self._stateManager.getVersionState(versionCombined)
        if (versionState != StateManager.kStateOnDisk):
            msg = "removeVersionAndSubPkgs(): Version %s is not on-disk, it is in state '%s'" % (versionCombined, versionState)
            self._log("remove-subpkgs").error(msg)
            raise InstallException(msg)

        if removeSubPackages:
            subPkgsToRemove = self._stateManager.getSubPkgsToRemoveOnRemoval(versionCombined)
            self._log("remove-subpkgs").info("Removing sub-packages: %s", subPkgsToRemove)
            if len(subPkgsToRemove):
                self._subPkgManager.removeSubPackages(subPkgsToRemove)

        self._log("remove-subpkgs").info("Removing version %s from state", versionCombined)
        self._stateManager.removeVersion(versionCombined)

    def removeUnneededVersionsFromDisk (self):
        """
        Removes old versions from disk.
        Scans all versions maintained in the state, and for each version which is 'on-disk', if it is not needed (i.e. 
        for a possible rollback command), removes sub-packages and RPMs installed by it and not required by the active versions
        """

        self._log("remove-undeeded-vers-called").info("removeUnneededVersionsFromDisk() called")
        # Find things needed by the current active and ready versions
        # Currently no rollback support, hence nothing else is needed.
        versions = self._stateManager.getVersions()
        versionsToRemove=[]
        versionsToKeep=[]
        for ver in versions:
            state=self._stateManager.getVersionState(ver)
            # TODO(orens): When we add rollback support, keep also the 'on-disk' version we may rollback into.
            if state==StateManager.kStateOnDisk:
                versionsToRemove.append(ver)
            else:
                versionsToKeep.append(ver)

        # Find list of RPMs and list of subpackages we must keep
        (rpmsToKeep, subPkgsToKeep)=self._getRpmsAndSubPkgsOfVersions(versionsToKeep)

        # Find list of RPMs used by versions we remove
        (rpmsToRemove, subPkgsToRemove)=self._getRpmsAndSubPkgsOfVersions(versionsToRemove)

        # The crucial moment
        rpmsToRemove -= rpmsToKeep
        subPkgsToRemove -= subPkgsToKeep

        # Filter rpms in order to check which ones are not installed- only installed ones should be removed
        self._log("ruv-filtering1").info("removeUnneededVersionsFromDisk(): Filtering RPMs %s for not installed packages", rpmsToRemove)
        rpm=self._createRpmForActiveRfs()
        rpmsToRemove = filter(rpm.isInstalled, rpmsToRemove)

        # Check if pilot wants to modify RPM list
        activeVersion = self._stateManager.getActiveVersion()
        self._log("ruv-filtering3").info("removeUnneededVersionsFromDisk(): activeVersion is %s", activeVersion)
        (pilot, _) = self._createPilot(activeVersion, None)
        if hasattr(pilot, "hookModifyRpmsForRemovalOld"):
            rpmsToRemove=pilot.hookModifyRpmsForRemovalOld(rpmsToRemove)
            self._log("ruv-filtering5").info("removeUnneededVersionsFromDisk(): pilot hookModifyRpmsForRemovalOld() returned %s", rpmsToRemove)
        else:
            self._log("ruv-filtering6").info("removeUnneededVersionsFromDisk(): pilot hookModifyRpmsForRemovalOld() not implemented")

        # We do not need to filter sub-pkgs for existance - only existing ones would be removed

        self._log("ruv-removing-ver").info("removeUnneededVersionsFromDisk(): Removing RPMs %s", rpmsToRemove)
        self._log("ruv-removing-ver").info("removeUnneededVersionsFromDisk(): Removing sub-pkgs %s", subPkgsToRemove)

        if len(rpmsToRemove)>0:
            yum=self._createYumWithAllRepos()
            yum.doRemove(" ".join(rpmsToRemove))
        self._subPkgManager.removeSubPackages(subPkgsToRemove)
        self._log("ruv-removing-ver").info("removeUnneededVersionsFromDisk(): Removing versions %s from state", versionsToRemove)
        for ver in versionsToRemove:
            self._stateManager.removeVersion(ver)

    def _getRpmsAndSubPkgsOfVersions(self, versions):
        """
        Returns a tuple with two sets: (rpmsOfVersions, subPkgsOfVersions)
        """
        rpmsOfVersions=set()
        subPkgsOfVersions=set()
        for ver in versions:
            self._log("get-rpms-and-subpkgs").info("_getRpmsAndSubPkgsOfVersions() Handling version %s", ver)
            leaders=self._stateManager.getLeaders(ver)
            self._log("get-rpms-and-subpkgs").info("_getRpmsAndSubPkgsOfVersions(): leaders=%s", leaders)
            for leader in leaders.values():
                rpmsOfVersions.add(leader)

            subPkgs=self._stateManager.getSubPkgs(ver)
            self._log("get-rpms-and-subpkgs").info("_getRpmsAndSubPkgsOfVersions(): subPkgs=%s", subPkgs)
            for subPkg in subPkgs:
                subPkgsOfVersions.add(subPkg)

            # The pilot of a version is always called like this:
            rpmsOfVersions.add(self.calcPilotName(ver))

        # Expand set by adding all required packages
        rpmsOfVersions=self._expandRpmsUsingReqires(rpmsOfVersions)
        self._log("get-rpms-and-subpkgs").info("_getRpmsAndSubPkgsOfVersions(): Returning rpmsOfVersions=%s", rpmsOfVersions)
        self._log("get-rpms-and-subpkgs").info("_getRpmsAndSubPkgsOfVersions(): Returning subPkgsOfVersions=%s", subPkgsOfVersions)
        return (rpmsOfVersions, subPkgsOfVersions)

    def _expandRpmsUsingReqires (self, packages):
        """
        Gets an iterable with a list of packages (Some may not be installed it is OK).
        Returns a set with the same packages, plus all installed packages required by these installed packages
        """

        self._log("expand-requires").info("_expandRpmsUsingReqires(packages=%s) called, ", packages)
        rpm=self._createRpmForActiveRfs()

        doIt=True
        ret=set(packages)
        while doIt:
            self._log("expand-requires").info("_expandRpmsUsingReqires() ret=%s", ret)
            doIt=False
            addedPackages=set()
            for package in packages:
                requires=rpm.doListRequires(package)
                for (capName, capCondition, capVersion) in requires:
                    # Ignore 'rpmxxx' capabilities
                    if capName.startswith('rpm'):
                        continue
                    # Ignore capabilities which are not '='.
                    if capCondition != '=':
                        continue
                    addedPackages.add(capName+'-'+capVersion)

            # Found something new ? Add to result and continue iterating
            self._log("expand-requires").info("_expandRpmsUsingReqires() addedPackages=%s, ret=%s", addedPackages, ret)
            newPackages = addedPackages-ret
            self._log("expand-requires").info("_expandRpmsUsingReqires() newPackages=%s", newPackages)
            if len(newPackages) > 0:
                doIt=True
                ret |= newPackages
                packages = newPackages
        self._log("expand-requires").info("_expandRpmsUsingReqires() returning %s", ret)
        return ret


    def prepare (self, version_, build, usePilotVersion=None):
        """
        Prepares a version for installation.
        If a version is already prepared, raises InstallException().

        usePilotVersion: If != None, sets pilot version to be used instead of auto-selecting.
        """
        self._log("prepare").info("prepare(version=%s, build=%s) called", version_, build)

        if self._stateManager.getReadyVersion() != None:
            msg="prepare(): A version is ready"
            self._log("prepare").error(msg)
            raise InstallException(msg)

        if build == kFakeBuildNumber:
            msg="prepare(): Invalid build number. Build '%s' is reserved for fake builds" % kFakeBuildNumber
            self._log("prepare").error(msg)
            raise InstallException(msg)

        newVersion=self.combineVersion(version_, build)
        activeVersion=self._stateManager.getActiveVersion()

        self._installPilot(newVersion)
        self._log("prepare").info("Creating pilot for new version %s", newVersion)
        (newVersionPilot, newVersionPs) = self._createPilot(newVersion, newVersion)
        self._log("prepare").info("Creating pilot for active version %s", activeVersion)
        (activeVersionPilot, activeVersionPs) = self._createPilot(activeVersion, newVersion)

        # Teach each pilot services about the other pilot
        newVersionPs.setOtherPilot(activeVersionPilot)
        activeVersionPs.setOtherPilot(newVersionPilot)

        if usePilotVersion != None:
            self._log("prepare").info("Creating pilot for version %s, manually selected", usePilotVersion)
            if (usePilotVersion != newVersion) and (usePilotVersion != activeVersion):
                msg="Manually selected pilot should be one of %s or %s, not %s" % (newVersion, activeVersion, usePilotVersion)
                self._log("prepare").error("prepare(): %s", msg)
                raise InstallException(msg)
            selectedVersion=usePilotVersion
        else:
            self._log("prepare").info("Running pilot selection")
            # old pilot selection logic uses 'selectPilot'
            # new pilot selection logic uses 'getPilotGeneration'
            # If new version pilot supports new logic, use it.
            # If new version pilot does not support new logic, then this is downgrade, we choose our pilot.
            if hasattr(newVersionPilot, "getPilotGeneration"):
                newPilotGeneration=newVersionPilot.getPilotGeneration()
                activePilotGeneration=activeVersionPilot.getPilotGeneration()
                self._log("prepare").info("prepare(): pilot selection: newVersion=%s, activeVersion=%s, newPilotGeneration=%s, activePilotGeneration=%s",
                                          newVersion, activeVersion, newPilotGeneration, activePilotGeneration)
        
                if newPilotGeneration > activePilotGeneration:
                    selectedVersion = newVersion
                elif newPilotGeneration < activePilotGeneration:
                    selectedVersion = activeVersion
                else:   # Pilot generations are equal, choose according to version numbers
                    selectedVersion=self._selectLatestVersion(newVersion, activeVersion)
            else: # Downgrading, choose our pilot
                selectedVersion = activeVersion

        if selectedVersion == newVersion:
            pilot = newVersionPilot
        elif selectedVersion == activeVersion:
            pilot = activeVersionPilot
        else:
            msg="Bad pilot: newVersion=%s, activeVersion=%s, selectedVersion=%s" % (newVersion, activeVersion, selectedVersion)
            self._log("prepare").error("prepare(): pilot selection: %s", msg)
            raise InstallException(msg)

        # Version is selected, We have a pilot, let's take off
        self._log("prepare").info("prepare(): Selected pilot version is %s", selectedVersion)

        self._stateManager.setPilotName(newVersion, selectedVersion)

        rpm = self._createRpmForActiveRfs()
        installedRpmsBefore=rpm.doGetInstalledPackages()
        self._log("prepare").info("prepare(): Installed RPMs before prepare() are: %s", installedRpmsBefore)

        # As last, Run pilot 'prepare' function !

        # Pilot is executed in try block. In case of failure, we clear pilot name.
        self._log("prepare").info("prepare(): running pilot...")
        try:
            # Old pilots do not have doPrepare2(), but we should never call old pilots from new code,
            # because the active version pilot should win.
            pilot.doPrepare2(newVersion, newVersionPilot, activeVersionPilot)
        except:
            self._stateManager.setPilotName(newVersion, None)
            raise

        installedRpmsAfter=rpm.doGetInstalledPackages()
        self._log("prepare").info("prepare(): Installed RPMs after prepare() are: %s", installedRpmsBefore)
        newRpms = sorted(list(set(installedRpmsAfter)-set(installedRpmsBefore)))

        self._log("prepare").info("prepare(): New RPMs: %s", newRpms)
        self._stateManager.setRpmsToRemoveOnRemoval(newVersion, newRpms)

        # Pilot prepare went ok - time to mark this version as 'ready' !
        self._log("prepare").info("prepare(): pilot did good, marking version as ready")
        self._stateManager.setReadyVersion(newVersion)

    def cancel (self, version_, build):
        self._log("cancel").info("cancel(version=%s, build=%s) called", version_, build)

        versionCombined = self.combineVersion(version_, build)
        versionState = self._stateManager.getVersionState(versionCombined)
        if (versionState != StateManager.kStateReady):
            msg = "cancel(): Version %s is not ready, it is in state '%s'" % (versionCombined, versionState)
            self._log("cancel").error(msg)
            raise InstallException(msg)

        self._log("cancel").info("Creating pilot for version %s", versionCombined)
        (pilot,_)=self._createPilot(self._stateManager.getPilotName(versionCombined), versionCombined)
        if hasattr(pilot, "hookCancelBeforeRemove"):
            self._log("cancel").info("Calling pilot hookCancelBeforeRemove()")
            pilot.hookCancelBeforeRemove(versionCombined)

        rpmsToRemove = self._stateManager.getRpmsToRemoveOnRemoval(versionCombined)
        rpm = self._createRpmForActiveRfs()
        self._log("cancel").info("Removing rpms: %s", rpmsToRemove)
        if len(rpmsToRemove):
            rpm.doRemove(" ".join(rpmsToRemove))

        if hasattr(pilot, "hookCancelAfterRemove"):
            self._log("cancel").info("Calling pilot hookCancelAfterRemove()")
            pilot.hookCancelAfterRemove(versionCombined)

        self._log("cancel").info("Changing state of version %s to 'on-disk'", versionCombined)
        self._stateManager.setVersionStateOnDisk(versionCombined)

    def switch (self, version_, build):
        """
        version_, build are parameters of the ready version

        On success, returns pilot doSwitch() return code.
        On failure, raises something
        """
        self._log("switch-called").info("switch(version=%s, build=%s) called", version_, build)
        versionCombined = self.combineVersion(version_, build)
        versionState = self._stateManager.getVersionState(versionCombined)
        if (versionState != StateManager.kStateReady):
            msg = "cancel(): Version %s is not ready, it is in state '%s'" % (versionCombined, versionState)
            self._log("cancel").error(msg)
            raise InstallException(msg)

        self._log("switch").info("switch() creating pilot for version %s", versionCombined)
        pilotName=self._stateManager.getPilotName(versionCombined)
        (pilot,_)=self._createPilot(pilotName, versionCombined)

        self._log("switch").info("switch() forgetting things to remove on removal for version %s", versionCombined)
        self._stateManager.setSubPkgsToRemoveOnRemoval(versionCombined, None)
        self._stateManager.setRpmsToRemoveOnRemoval(versionCombined, None)

        # Get params needed to determine which user-log message to emit, and emit it
        activeVersion=self._stateManager.getActiveVersion()
        switchType = self._stateManager.getSwitchType(versionCombined)
        installDirection = self._stateManager.getInstallDirection(versionCombined)
        self._log("switch").info("switch() got switchType='%s', installDirection='%s'", switchType, installDirection)

        if (switchType == "OS Restart") and (installDirection == "upgrade"):
            a.infra.process.logUserMessage(a.api.user_log.msg.install.OsUpgrade(activeVersion, versionCombined))
        elif (switchType == "OS Restart") and (installDirection == "downgrade"):
            a.infra.process.logUserMessage(a.api.user_log.msg.install.OsDowngrade(activeVersion, versionCombined))
        elif (switchType == "Application Restart") and (installDirection == "upgrade"):
            a.infra.process.logUserMessage(a.api.user_log.msg.install.AppUpgrade(activeVersion, versionCombined))
        elif (switchType == "Application Restart") and (installDirection == "downgrade"):
            a.infra.process.logUserMessage(a.api.user_log.msg.install.AppDowngrade(activeVersion, versionCombined))

        self._log("switch").info("switch() calling pilot doSwitch(%s)", versionCombined)

        # Returned value from pilot should signal caller something (Probably exit code).
        ret = pilot.doSwitch(versionCombined)

        # State is now locked. Let's check it, in case pilot was sloppy.
        if not self._stateManager.isLocked():
            msg="ERROR: switch() expecting state to be locked after pilot doSwitch()"
            self._log("switch").error(msg)
            raise InstallException(msg)

        return ret
        

    def verify (self):
        """
        Verifies all installed RPMs.
        Returns list of problems, empty list if OK
        """
        self._log("verify-called").info("verify() called")
        rpm=self._createRpmForActiveRfs()
        problems = rpm.doVerifyAllInstalled()
        self._log("verify-returning").info("verify() returning %s", problems)
        # We skip problems about some files which normally change after being installed
        filteredProblems = []
        for problem in problems:
            # /etc and /var files onbviously should not be checked
            if " /etc/" in problem:
                continue
            if " /var/" in problem:
                continue
            # .ini and .cfg files in /opt/dell seem to be changing
            if (" /opt/dell/" in problem) and (problem.endswith(".ini") or problem.endswith(".cfg")):
                continue
            # .pyc files in Oscar seem to be changing
            if (" /opt/qb/rpms/oscar-" in problem) and problem.endswith(".pyc"):
                continue
            # We over-ride firmware files when upgrading the kernel
            if " /lib/firmware/" in problem:
                continue
            # Handle a few specific files
            if (" /opt/MegaRAID/MegaCli/MegaCli" in problem) or (" /root/.bash_profile" in problem):
                continue
            filteredProblems.append(problem)
        return filteredProblems

    def getRpmsDir (self):
        return self._rpmsDir

    def getAppDir (self):
        return self._appDir

    def getAppNextDir (self):
        return self._appDir+".next"

    def getAppPrevDir (self):
        return self._appDir+".prev"

    def getAppDirReal (self):
        return self._appDirReal

    def getBootDevPath (self):
        return self._bootDevPath

    def getGrubConf (self):
        return self._grubConf

    def getVitalDir (self):
        return self._vitalDir

    def getSubPkgManager (self):
        return self._subPkgManager

    def debugSetNoInstallMode (self):
        self._log("debug-no-install-mode").notice("debugSetNoInstallMode() called, NO RPMS WILL BE INSTALLED")
        self._debugNoInstallMode=True

    def unit_test_ExtractPackageFile (self, fileName):
        self._subPkgManager.add(r2pmFile=fileName)

    def unit_test_InstallPilot (self, version_, build):
        versionCombined=self.combineVersion(version_, build)
        self._installPilot(versionCombined)

    def unit_test_InstallRpm (self, name):
        yum=self._createYumWithAllRepos()
        self._log("debug-install-rpm").info("debugInstallRpm(): installing %s", name)
        if not self._debugNoInstallMode:
            yum.doInstall(name)

    def unit_test_GetInstallTempDir (self):
        """Helper for unit tests"""
        return self._installTempDir

    def unit_test_GetStateFile (self):
        """Helper for unit tests"""
        self._log("get-state-file").info("unit_test_GetStateFile(): returning %s", self._stateFile)
        return self._stateFile


    def _initPlatformBasic (self):
        self._log("init-platform-basic").info("initializing the platform-basic")
        self._platformBasic = a.infra.process.getPlatformBasicDataOrCrash()


    def _initSdUtils (self):
        self._log("init-sd-utils").info("initializing the sd-utils")        
        self._sdUtils = SdUtils(self._log)


    def _initBootUtils (self):
        self._log("init-boot-utils").info("initializing the boot-utils")
        self._bootUtils = BootUtils.s_getFromOsefOrCrash(a.infra.process.getOsef())


    def _installPilot(self, versionCombined):
        yum=self._createYumWithAllRepos()
        pilotPackageName = self.calcPilotName(versionCombined)
        self._log("install-pilot").info("_installPilot(): pilotPackageName=%s", pilotPackageName)
        if not self._debugNoInstallMode:
            yum.doInstall(pilotPackageName)

    def _createPilot (self, versionCombined, newVersionCombined):
        """
        Returns (pilot, pilotServices)

        versionCombined - name of pilot to create
        newVersionCombined - name of version being installed ('v-b')
        """
        self._log("create-pilot").info("_createPilot() called, versionCombined = %s", versionCombined)
        pilotRpmDirName = self.calcPilotName(versionCombined)
        pilotDirName = os.path.join(self._rpmsDir, pilotRpmDirName)
        pilotFileName = os.path.join(pilotDirName, "pilot.py")
        self._log("create-pilot").info("_createPilot(): pilotFileName = %s", pilotFileName)
        if not os.path.exists(pilotFileName):
            self._log("create-pilot").error("_createPilot() Could not find pilot file %s", pilotFileName)
            raise InstallException("Could not find pilot file %s" % pilotFileName)

        # Keep a copy of sys.path
        oldSysPath=list(sys.path)
        try:
            sys.path.append(pilotDirName)
            self._log("create-pilot").info("_createPilot(): about to import, sys.path=%s", sys.path)
            import pilot
            reload(pilot)
            p=pilot.Pilot()
        except:
            self._log("create-pilot").error("_createPilot(): Got exception when importing and creating pilot")
            raise
        finally:
            # Restore old sys.path
            sys.path=oldSysPath
            self._log("create-pilot").info("_createPilot(): Restored sys.path to %s", sys.path)

        self._log("create-pilot").info("_createPilot(): creating pilot services, pilotDirName=%s", pilotDirName)
        pilotServices=self._createPilotServices(versionCombined, pilotDirName, newVersionCombined)
        p.setPilotServices(pilotServices)
        self._log("create-pilot-returning").info("_createPilot() returning pilot")
        return (p, pilotServices)
        

    def calcPilotName (self, versionCombined):
        pilotName="pilot-%s-%s" % (self._product, versionCombined)
        return pilotName

    def _isPackageSigned (self, fileName):
        """
        Checks that an RPM file is a signed
        """
        rpm=self._createRpmForActiveRfs()
        return rpm.doValidateRpm(fileName)

    def combineVersion (self, version_, build):
        """Combines version and build into a single string "v-b". version and buil cannot contain '-' chars. """
        if version_.find("-") != -1:
            self._log("combine-version-bad").error("combineVersion() got version='%s', invalid", version_)
            raise InstallException("combineVersion(): bad version '%s'" % version_)
        if build.find("-") != -1:
            self._log("combine-version-bad").error("combineVersion() got build='%s', invalid", build)
            raise InstallException("combineVersion(): bad build '%s'" % build)
        return version_+"-"+build

    def splitVersion (self, versionCombined, raiseIfInvalid=False):
        """
        Splits versionCombined into a version and a build. versionCombined must contain exactly 1 '-' char. 
        Returns (version, build), or (None, None) if versionCombined is invalid
        if raiseIfInvalid is True, then instead of returning (None, None), raises InstallException
        """
        if versionCombined.count("-") != 1:
            self._log("version-split-bad").error("splitVersion() got '%s', cannot split", versionCombined)
            if raiseIfInvalid:
                raise InstallException("splitVersion(): bad versionCombined '%s'" % versionCombined)
            return (None, None)
        (version_,build) = versionCombined.split("-")
        return (version_,build)

    def _createPilotServices (self, pilotVersion, pilotDir, newVersionCombined): 
        self._log("create-pilot-services").info("_createPilotServices(): Called, pilotVersion = %s, newVersionCombined = %s", 
                                                pilotVersion, newVersionCombined)
        rpmActiveRfs=self._createRpmForActiveRfs()
        yumActiveRfs=self._createYumWithAllRepos()
        yumNewVersionOnly=self._createYumWithAllRepos(repoFilter=newVersionCombined)

        self._log("create-pilot-services").info("_createPilotServices(): creating yum.conf for active RFS and yum.conf "\
                                                "for new version %s", newVersionCombined)

        yumConfActiveRfs=yumActiveRfs.createYumConfAt(self._yumConfActiveRfsDir)
        yumConfNewVersionOnly=yumNewVersionOnly.createYumConfAt(self._yumConfNewVersionDir)

        self._log("create-pilot-services").info("_createPilotServices(): got yum.conf at %s, yum.conf for new versiom only at %s", 
                                                yumConfActiveRfs, yumConfNewVersionOnly)
        pilotServices=PilotServices(self._log, self._stateManager, self, pilotVersion, pilotDir, self._logDir, self._workDir, self._apiDir,
                                    self._startupScriptsDir, rpmActiveRfs, yumActiveRfs, yumConfActiveRfs, yumConfNewVersionOnly,
                                    self._prevRfsDir, self._sdUtils, self._bootUtils)
        pilotServices.setPilotHints(self._pilotHints)
        return pilotServices 

    def _createRpmForActiveRfs (self):
        rpm=Rpm(self._log)
        rpm.setRoot(self._systemRoot, useFakeChrootMode=self._useFakeChrootMode)
        return rpm

    def _createYumWithAllRepos (self, repoFilter=None):
        """
        Returns a yum object configured to see all repos

        if repoFilter != None, yum is configured to see only repos which contain the subs-string repoFilter:
        """

        self._log("create-yum-with-all-repos").info("createYumWithAllRepos() called, repoFilter=%s", repoFilter)
        if self._useFakeChrootMode:
            yum=Yum(self._log, self._tempDir.replace(self._systemRoot, ""))
            yum.setRoot(self._systemRoot, useFakeChrootMode=True)
        else:
            yum=Yum(self._log, os.path.join(self._tempDir, "yum"))
        self._subPkgManager.addReposToYum(yum, repoFilter)
        return yum

    def _chopLeadingSlashIfFound (self, path_):
        if path_.startswith('/'):
            return path_[1:]
        return path_

    def _selectLatestVersion(self, version1, version2):
        # Split versions to version name and build number
        self._log("select-latest-version").info("_selectLatestVersion() called, version1=%s, version2=%s", version1, version2)

        # Versions must look like this: "v-b"

        vb1=version1.split('-')
        if len(vb1) != 2:
            raise InstallException("Invalid version number: %s is invalid" % version1)
        vb2=version2.split('-')
        if len(vb2) != 2:
            raise InstallException("Invalid version number: %s is invalid" % version2)

        ver1=vb1[0]
        b1=vb1[1]
        ver2=vb2[0]
        b2=vb2[1]

        # A version is official if it is made from numbers and dots only
        onlyDigitsAndDots="^[\d\.]+$"
        ver1IsOfficial=bool(re.match(onlyDigitsAndDots, version1))
        ver2IsOfficial=bool(re.match(onlyDigitsAndDots, version2))

        # Official versions beat private versions
        if ver1IsOfficial != ver2IsOfficial:
            if ver1IsOfficial:
                return version1
            return version2

        # Now we have either two official versions, or two private versions.
        if ver1 != ver2:
            # Versions are not identical. Split version into elements
            v1=ver1.split(".")
            v2=ver2.split(".")
            len1=len(v1)
            len2=len(v2)
    
            # Numerically compare the numbers, as long as both versions have them
            minLen=min(len1, len2)
            for i in range(minLen):
                # Both version elements are the same ? no need to compare
                if v1[i] == v2[i]:
                    continue
    
                # Need to compare version elements. Convert to integers.
                try:
                    ve1=int(v1[i])
                    ve2=int(v2[i])
                except:
                    # Not an integer ? Cannot compare. Choose first version arbitrarily
                    return version1
    
                # Different numbers ? We have a winner !
                if ve1<ve2:
                    return version2
                if ve1>ve2:
                    return version1
                # Note that we may get here despite the 'if' that prevented comparing the same strings.
                # For example, 04 and 4 are the same.
    
            # Out of the loop with no decision ? Let's see if the version lengths want to talk
            # 
            # Longer length wins: 2.1.0.0 is 'later' than 2.1.0

            if len1<len2:
                return version2
            if len1>len2:
                return version1

            # If we are here, then versions are not identical, but all their components are the same
            # AND they are the same length ? This could happen with versions like 2.04 vs 2.4.
            # Choose arbitrarily
            return version1

        # Versions are the same. We need to decide based on build numbers
         
        # Make sure build number is an integer
        try:
            b1n=int(b1)
            b2n=int(b2)
        except:
            raise InstallException("Invalid build number: Both '%s' and '%s' should be numeric" % (b1, b2))

        # Decide according to the build number
        if b1n<b2n:
            return version2
        return version1

    def _raiseIfVersionActiveOrReady(self, versionCombined):
        # Do not allow adding an existing version
        curState=self._stateManager.getVersionState(versionCombined)
        if curState == StateManager.kStateActive:
            self._log("add-existing-version").error("_raiseIfVersionActiveOrReady() Found existing active version '%s'", versionCombined)
            raise InstallException("Version %s is the currently active version" % versionCombined)
        if curState == StateManager.kStateReady:
            self._log("add-existing-version").error("_raiseIfVersionActiveOrReady() Found existing ready version '%s'", versionCombined)
            raise InstallException("Version %s is already ready" % versionCombined)

    def _raiseIfAbsPath (self, pathToCheck, name):
        if pathToCheck.startswith(os.path.sep):
            raise ValueError("Parameter '%s' must not start with '/', value given is '%s'" % (name, pathToCheck))

    def _raiseIfNotAbsPath (self, pathToCheck, name):
        if not pathToCheck.startswith(os.path.sep):
            raise ValueError("Parameter '%s' must start with '/', value given is '%s'" % (name, pathToCheck))

