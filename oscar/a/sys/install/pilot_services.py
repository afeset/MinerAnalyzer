# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens
import os

from a.sys.install.exceptions import InstallException
from a.sys.install.utils import Utils


class PilotServices(object):
    """
    ######################################################################################################
    # NOTE: ALL public funcs are part of the pilot API, changes must be considered carefully  !
    #       Better not to change anything, only add
    ######################################################################################################
    """

    def __init__ (self, logger, stateManager, installManager, pilotVersion, pilotDir, logDir, workDir, apiDir, startupScriptsDir, 
                  rpmActiveRfs, yumActiveRfs, yumConfForActiveRfs, yumConfForNewVersionOnly, prevRfsDir, sdUtils, bootUtils):
        self._log = logger.createLogger("sys-install","pilot-services")
        self._utils = Utils(self._log)
        self._stateManager = stateManager
        self._installManager = installManager
        self._pilotVersion = pilotVersion
        self._pilotDir = pilotDir
        self._logDir = logDir
        self._workDir = workDir
        self._apiDir = apiDir
        self._startupScriptsDir = startupScriptsDir
        self._rpmActiveRfs = rpmActiveRfs
        self._yumActiveRfs = yumActiveRfs
        self._yumConfForActiveRfs = yumConfForActiveRfs
        self._yumConfForNewVersionOnly = yumConfForNewVersionOnly
        self._debugNoInstallMode = False
        self._otherPilot = None
        self._pilotHints = None
        self._prevRfsDir = prevRfsDir
        self._sdUtils    = sdUtils
        self._bootUtils  = bootUtils

    def debugSetNoInstallMode (self):
        self._debugNoInstallMode=True

    def setOtherPilot (self, otherPilot):
        """NOT FOR USE BY PILOT !!!"""
        self._otherPilot = otherPilot

    def setPilotHints (self, hints):
        """NOT FOR USE BY PILOT !!!"""
        self._pilotHints = hints

    def logInfo (self, msg):
        """Logs an info message"""
        self._log("pilot-info").info(msg)

    def logWarning (self, msg):
        """Logs a warning message"""
        self._log("pilot-warning").warning(msg)

    def logError (self, msg):
        """Logs an error message"""
        self._log("pilot-error").error(msg)

    def raiseException (self, msg):
        """Raises an exception to abort current pilot operation with an error"""

        self._log("raise-exception").info("raiseException() called,  msg = %s", msg)
        raise InstallException(msg)

    def getPilotHints (self):
        """Returns the pilot hints, None if none"""
        return self._pilotHints

    def getStateManager (self):
        return self._stateManager

    def getPilotVersion (self):
        """Returns Version of pilot being serviced"""

        self._log("get-pilot-version").info("getPilotVersion() called,  returning %s", self._pilotVersion)
        return self._pilotVersion

    def getPilotDir (self):
        """Returns absolute path to pilot directory, for use by pilot to access other files"""

        self._log("get-pilot-dir").info("getPilotDir() called,  returning %s", self._pilotDir)
        return self._pilotDir

    def getOtherPilot (self):
        """Returns the other pilot. Use this only during prepare() !!!"""
        return self._otherPilot

    def getSubPackages (self):
        """
        Returns a dict of all sub-packages installed.
        For each sub-package: sub-package name is key, value is a dict with the content of the info file of the sub-package
        """
        self._log("get-sub-packages").info("getSubPackages() called")
        return self._installManager.getSubPkgManager().getSubPkgs()

    def getSubPkgsDir (self):
        """Returns the directory in which all sub-packages are installed"""
        self._log("get-sub-packages-dir").info("getSubPkgsDir() called")
        return self._installManager.getSubPkgManager().getSubPkgsDir()
        
    def getBootDevPath (self):
        """Returns the path to the boot device"""
        bd=self._installManager.getBootDevPath()
        self._log("get-boot-dev-path").info("getBootDevPath() called, returning %s", bd)
        return bd

    def getVitalDir (self):
        """Returns the path to the vital dir"""
        vd=self._installManager.getVitalDir()
        self._log("get-vital-dir").info("getVitalDir() called, returning %s", vd)
        return vd

    def getGrubConf (self):
        """Returns the name of the grub.conf file"""
        gc=self._installManager.getGrubConf()
        self._log("get-grub-conf").info("getGrubConf() called, returning %s", gc)
        return gc

    def getAppDir (self):
        """Returns absolute path to app directory"""

        self._log("get-app-dir").info("getAppDir() called")
        appDir=self._installManager.getAppDir()
        self._log("get-app-dir").info("getAppDir() returning %s", appDir)
        return appDir

    def getAppDirReal (self):
        """Returns absolute path to real app directory"""

        self._log("get-app-dir-real").info("getAppDirReal() called")
        appDirReal=self._installManager.getAppDirReal()
        self._log("get-app-dir-real").info("getAppDirReal() returning %s", appDirReal)
        return appDirReal

    def getRpmsDir (self):
        """Returns absolute path to rpms directory"""

        self._log("get-app-dir").info("getRpmsDir() called")
        rpmsDir=self._installManager.getRpmsDir()
        self._log("get-app-dir").info("getRpmsDir() returning %s", rpmsDir)
        return rpmsDir

    def getLogDir (self):
        """Returns absolute path to log directory, for use by pilot to create log files"""

        self._log("get-log-dir").info("getLogDir() called,  returning %s", self._logDir)
        return self._logDir

    def getWorkDir (self):
        """Returns absolute path to work directory, for use by pilot to create scripts and such"""

        self._log("get-work-dir").info("getWorkDir() called,  returning %s", self._workDir)
        return self._workDir

    def getApiDir (self):
        """Returns absolute path to api directory, for use by pilot to store information available to other modules/processes"""

        self._log("get-api-dir").info("getApiDir() called,  returning %s", self._apiDir)
        return self._apiDir

    def getStartupScriptsDir (self):
        """
        Returns absolute path to startup scripts directory, for use by pilot to create scripts executed 
        by oscar on the next system start
        """

        self._log("get-startup-scripts-dir").info("getStartupScriptsDir() called,  returning %s", self._startupScriptsDir)
        return self._startupScriptsDir

    def getPrevRfsDir (self):
        self._log("get-prev-rfs-dir").info("getPrevRfsDir() called,  returning %s", self._prevRfsDir)
        return self._prevRfsDir


    def getSdUtils (self):
        self._log("get-sd-utils").info("getSdUtils() called,  returning object %s", self._sdUtils)
        return self._sdUtils

    def getBootUtils (self):
        self._log("get-boot-utils").info("getBootUtils() called,  returning object %s", self._bootUtils)
        return self._bootUtils

    def getPreparedPackageFilePath (self):
        fp = self._installManager.getPreparedPackageFilePath()
        self._log("get-prepared-package-file-path").info("getPreparedPackageFilePath() called,  returning object %s", fp)
        return fp

    def rpmListRequiresActiveRfs (self, package):
        """
        Gets list of required capabilities of a package installed in the active RFS. 
        package: Package name

        Returns List of tuples: (capName, capCondition, capVersion)
        """
        self._log("rpm-list-required-active-rfs-called").info("rpmListRequiredActiveRfs() called, package=%s", package)
        ret = self._rpmActiveRfs.doListRequires(package)
        self._log("rpm-list-required-active-rfs-returning").info("rpmListRequiredActiveRfs() returning %s", ret)
        return ret

    def yumTestInstallActiveRfs (self, packages):
        """
        Test-Install a set of packages on the active RFS. 
        packages: A space-separated string of package names

        Returns True if OK, False if not
        """
        self._log("yum-test-install-active-rfs-called").info("yumTestInstallActiveRfs() called,  packages=%s", packages)
        ret = self._yumActiveRfs.doTestInstall(packages)
        self._log("yum-test-install-active-rfs-returning").info("yumTestInstallActiveRfs() returning %s", ret)
        return ret

    def yumInstallActiveRfs (self, packages):
        """
        Installs a set of packages on the active RFS. 
        packages: A space-separated string of package names
        """
        self._log("yum-install-active-rfs-called").info("yumInstallActiveRfs() called,  packages=%s", packages)
        if not self._debugNoInstallMode:
            self._yumActiveRfs.doInstall(packages)
        self._log("yum-install-active-rfs-done").info("yumInstallActiveRfs() done")

    def getYumConfigFileActiveRfs (self):
        """
        Gets the name of a yum config file, configured for all current repositories (found in sub-packages)
        """
        self._log("get-yum-config-file-active-rfs-called").info("getYumConfigFileActiveRfs() called, returning %s", self._yumConfForActiveRfs)
        return self._yumConfForActiveRfs

    def getYumConfigFileNewVersionOnly (self):
        """
        Gets the name of a yum config file, configured for one repository: The one that came with the currently installed version
        """
        self._log("get-yum-config-file-new-version-only-called").info("getYumConfigFileNewVersionOnly() called, returning %s", self._yumConfForNewVersionOnly)
        return self._yumConfForNewVersionOnly

        
    def getAvailableSize (self, path_):
        """
        Returns available size in bytes on a given path
        """
        self._log("get-avail-size").info("getAvailableSize() called, path=%s", path_)
        return self._utils.getAvailableSize(path_)

    def hook_runYumActiveRfs (self, command):
        """Emergency use only. Allows pilot to run any yum command"""

        self._log("hook-run-yum-active-rfs-called").info("hook_runYumActiveRfs() called,  command=%s", command)
        (rc, outText, errText)=self._rpmActiveRfs._runRpm(command)
        self._log("hook-run-yum-active-rfs-returning").info("hook_runYumActiveRfs() returning rc=%s, outText=%s, errText=%s", 
                                                            rc, outText, errText)
        return (rc, outText, errText)

    def hook_runRpmActiveRfs (self, command):
        """Emergency use only. Allows pilot to run any rpm command"""

        self._log("hook-run-rpm-active-rfs-called").info("hook_runRpmActiveRfs() called,  command=%s", command)
        (rc, outText, errText)=self._yumActiveRfs._runYum(command)
        self._log("hook-run-rpm-active-rfs-returning").info("hook_runRpmActiveRfs() returning rc=%s, outText=%s, errText=%s", 
                                                            rc, outText, errText)
        return (rc, outText, errText)

    def hook_runCommand (self, command):
        """
        Allows pilot to run any command.
        Returns (rc, outText, errText)
        """

        self._log("hook-run-command-called").info("hook_runCommand() called,  command=%s", command)
        (rc, outText, errText)=self._utils.runCommand(command)
        self._log("hook-run-command-returning").info("hook_runCommand() returning rc=%s", rc)
        return (rc, outText, errText)




