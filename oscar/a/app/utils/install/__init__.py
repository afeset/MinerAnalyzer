# 
# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: nirs

import fcntl
import logging
import os     
import signal
import sys
import traceback

import a.infra.format.json
import a.sys.std_process.micro_captain
from a.sys.install.install_manager import InstallManager
from a.sys.install.exceptions import InstallException
from a.sys.install.exceptions import InvalidPackageFileException
import a.sys.mng.user_log.service
import a.sys.mng.user_log.log_infra

G_NAME_MODULE_APP_INSTALL = "install"
G_NAME_GROUP_APP_INSTALL_DEFAULT = "default"

def printError (msg):
    print "Error: "+msg

class InstallOperationsApp(a.sys.std_process.micro_captain.MicroAppInterface):
    INIT_PARAM_FILES_DIR_ENV_VAR_NAME = "INSTALL_OPS_INIT_PARAM_DIR"
    #init params handling
    INIT_PARAM_FILE_NAME = "install-ops-init-params.json"
    #kept fields
    INIT_PARAM_USER_ROOT_DIR="user-root-dir"    
    INIT_PARAM_SYS_VAR_DIR="sys-var-dir"    
    INIT_PARAM_SYS_RUN_DIR="sys-run-dir"    
    INIT_PARAM_DATA_VAR_DIR="data-var-dir"    
    INIT_PARAM_VITAL_DIR="vital-dir"    
    INIT_PARAM_RPMS_DIR="rpms-dir"    
    INIT_PARAM_APP_DIR="app-dir"    
    INIT_PARAM_APP_DIR_REAL="app-dir-real"
    INIT_PARAM_BOOT_DEV_PATH="boot-dev-path"
    INIT_PARAM_GRUB_CONF="grub-conf"    
    INIT_PARAM_SUPPORTED="supported"    
    INIT_PARAM_PREV_RFS_DIR="prev-rfs-dir"    
    INIT_PARAM_USER_LOG_INFRA_LOGGER_DICT = "user-log-infra-logger-dict"

    def __init__ (self):
        pass      

    def initLogger(self, logger):
        self._log = logger.createLogger(G_NAME_MODULE_APP_INSTALL, G_NAME_GROUP_APP_INSTALL_DEFAULT)

    def createCaptainClients (self):
        self._userLogInfraLogger = a.sys.mng.user_log.log_infra.LogInfra()
        self._userLogInfraLogger.initLoggerToUse(self._log)
        self._userLogInfraLogger.initCaptain(self._captain)
        self._userLogInfraLogger.initCaptainClientBehavior(skipInitFromParamFile=True)
        self._captain._addClient(self._userLogInfraLogger.getCaptainClientName(), self._userLogInfraLogger)

        userLogService = a.sys.mng.user_log.service.Service(self._log)
        userLogService.initCaptain(self._captain)
        self._captain._addClient(userLogService.CAPTAIN_CLIENT_NAME, userLogService)   

    def initFromParamFile(self, initParamFilesDirName):
        data = a.infra.format.json.readFromFile(self._log, 
                                                os.path.join(initParamFilesDirName, self.INIT_PARAM_FILE_NAME))
        self.initFromDictionary(data)

    def initFromDictionary(self, data):
        self.init(data[self.INIT_PARAM_USER_ROOT_DIR], data[self.INIT_PARAM_SYS_VAR_DIR],  data[self.INIT_PARAM_SYS_RUN_DIR], 
                  data[self.INIT_PARAM_DATA_VAR_DIR], data[self.INIT_PARAM_RPMS_DIR], 
                  data[self.INIT_PARAM_APP_DIR], data[self.INIT_PARAM_APP_DIR_REAL], 
                  data[self.INIT_PARAM_BOOT_DEV_PATH], data[self.INIT_PARAM_GRUB_CONF], 
                  data[self.INIT_PARAM_SUPPORTED], 
                  data.get(self.INIT_PARAM_PREV_RFS_DIR), # New attribute, Some code paths do not specify it, be forgiving.
                  data[self.INIT_PARAM_USER_LOG_INFRA_LOGGER_DICT],
                  data.get(self.INIT_PARAM_VITAL_DIR))

    def init (self, userRootDir, sysVarDir, sysRunDir, dataVarDir, rpmsDir, appDir, appDirReal, bootDevPath, grubConf, 
              supported, prevRfsDir, userLogInfraLoggerDict, vitalDir):
        self._userRootDir = userRootDir
        self._sysVarDir = sysVarDir
        self._debugFlagFileDontCleanOnError = os.path.join(self._sysVarDir, 'install-dont-clean-on-error')
        self._sysRunDir = sysRunDir
        self._dataVarDir = dataVarDir
        self._rpmsDir = rpmsDir
        self._appDir = appDir
        self._appDirReal = appDirReal
        self._bootDevPath = bootDevPath
        self._grubConf = grubConf
        self._supported = supported
        self._prevRfsDir = prevRfsDir
        self._vitalDir = vitalDir
        self._log("init-params").info("userRootDir=%s, sysVarDir=%s, sysRunDir=%s, dataVarDir=%s, rpmsDir=%s, appDir=%s, "\
                                      "appDirReal=%s, bootDevPath=%s, grubConf=%s, prevRfsDir=%s, vitalDir=%s", 
                                      self._userRootDir, self._sysVarDir, self._sysRunDir, self._dataVarDir, self._rpmsDir, 
                                      self._appDir, self._appDirReal, self._bootDevPath, self._grubConf, self._prevRfsDir, self._vitalDir)
        if not self._sysVarDir.startswith(os.path.sep):
            raise ValueError("sysVarDir must start with '/', given value is %s." % self._sysVarDir)
        if not self._sysRunDir.startswith(os.path.sep):
            raise ValueError("sysRunDir must start with '/', given value is %s." % self._sysRunDir)
        if not self._dataVarDir.startswith(os.path.sep):
            raise ValueError("dataVarDir must start with '/', given value is %s." % self._dataVarDir)
        if not self._rpmsDir.startswith(os.path.sep):
            raise ValueError("rpmsDir must start with '/', given value is %s." % self._rpmsDir)
        if not self._appDir.startswith(os.path.sep):
            raise ValueError("appDir must start with '/', given value is %s." % self._appDir)
        self._installManager = InstallManager(self._log, "qb", self._sysVarDir, self._sysRunDir, self._dataVarDir, 
                                              self._rpmsDir, self._appDir, self._appDirReal, self._bootDevPath, 
                                              self._grubConf, self._prevRfsDir, self._vitalDir)

        self._userLogInfraLogger.manualReplaceCaptainClient_initFromDictionary(userLogInfraLoggerDict)

        self._lockFileName=os.path.join(self._sysRunDir, "lock")



    def addToOptParser(self, optParser):
        optParser.add_option("-c", "--command", dest="cmd", default=None, help="command to run: 'prepare', 'switch', 'cancel', 'validate', 'verify', 'show', 'startup'.")
        optParser.add_option("-f", "--file", dest="file", default=None, help="File to use, needed by 'prepare' and 'validate' commands")
        optParser.add_option("-v", "--version", dest="version", default=None, help="For 'switch', Excpected version to switch to")
        optParser.add_option("-b", "--build", dest="build", default=None, help="For 'switch', Excpected build to switch to")
        optParser.add_option("--keep-file-name", dest="keepFileName", action="store_true",  default=False, help="Do not normalize file name")
        optParser.add_option("--pilot-hints", dest="pilotHints", default=None, help="Set pilot hints")
        optParser.add_option("--use-pilot-version", dest="usePilotVersion", default=None, help="Set pilot version to use")
        optParser.add_option("--debug-no-install", dest="debugNoInstall", action="store_true", default=False, help="Debug mode: Do not install any RPMS")
        optParser.add_option("--install-same-version", dest="installSameVersion", action="store_true", default=False, help="Install the same version")

        optParser.add_option("--sd-first-install", dest="sdFirstInstall", action="store_true", default=False, help="First installation")
        optParser.add_option("--sd-first-install-version", dest="sdFirstInstallVersion", default=None, help="Version being installed in first installation")
        optParser.add_option("--sd-first-install-build", dest="sdFirstInstallBuild", default=None, help="Build being installed in first installation")
        optParser.add_option("--sd-next-rfs-device", dest="sdNextRfsDevice", default=None, help="Next RFS device to be used")
        optParser.add_option("--sd-next-rfs-dir-index", dest="sdNextRfsDirIndex", default=None, help="Next RFS directory index to be used")
        optParser.add_option("--startup-log-dir", dest="startupLogDir", default=None, help="Log dir to be used by startup scripts")


    def parseCmdLine(self, options, args):
        __pychecker__="no-argsused"  # args is not used
        if not options.cmd:
            self._log("missing-cmd").error("command option is missing")
            a.infra.process.processFatal("Missing command")             
        self._cmd =  options.cmd              
        self._options =  options

    # For now, commands return 0 (good) or 1 (bad), and print their errors/output by themselves.
    def run (self):
        self._pilotHints = self._options.pilotHints

        if self._options.sdFirstInstall and (self._cmd == "prepare"):
            if self._options.sdFirstInstallVersion is None or self._options.sdFirstInstallBuild is None:
                self._log("sd-install-version-build-not-specified").error("In --sd-install must also specify both --sd-install-version and --sd-install-build")
                printError("In --sd-first-install must also specify both --sd-first-install-version and --sd-first-install-build")
                return 1

            if self._options.sdNextRfsDevice is None or self._options.sdNextRfsDirIndex is None:
                self._log("sd-install-next-rfs-not-specified").error("In --sd-install must also specify both --sd-next-rfs-device and --sd-next-rfs-dir-index")
                printError("In --sd-install must also specify both --sd-next-rfs-device and --sd-next-rfs-dir-index")
                return 1

            if self._options.pilotHints:
                self._log("sd-install-pilot-hints-not-suppoted").error("In --sd-install --pilot-hints is not supported")
                printError("In --sd-install --pilot-hints is not supported")
                return 1
            self._pilotHints = "sd-install,no-reboot,rfs-dev=%s,rfs-index=%s" % (self._options.sdNextRfsDevice, self._options.sdNextRfsDirIndex)

            self._installManager.initializeSystemFirstInstall(self._options.sdFirstInstallVersion, self._options.sdFirstInstallBuild)

        if self._supported:
            self._installManager.init()

        self._installSameVersion = False
        if self._options.installSameVersion or (self._options.sdFirstInstall and (self._cmd == "prepare")):
            self._installSameVersion = True

        # Ignore SIGSTOP which is passed by confd when user pressed Ctrl-C on the CLI session
        signal.signal(signal.SIGINT, signal.SIG_IGN)

        self._log("run").info("command-line: sys.argv=%s", sys.argv)
        self._log("run").info("command-line: options=%s", self._options)
        self._log("run").info("Running command %s", self._cmd)

        # If install operations are not supported on this platform, show an error message and return
        if not self._supported:
            # But do not show the error message for the 'startup' operation, this operation is run by the system every time oscar starts
            if self._cmd != "startup": 
                self._log("run").info("Operation not supported on this platform")
                printError("Operation not supported on this platform")
            return 0

        if self._installSameVersion and (self._cmd != "prepare"):
            self._log("run").info("Error: --install-same-version can be used only during 'prepare'")
            printError("--install-same-version can be used only during 'prepare'")
            return 0

        self.createLockFileIfNeeded()

        if self._options.debugNoInstall:
            self._installManager.debugSetNoInstallMode()

        self._log("run").info("About to lock()...")
        self.lock()
        self._log("run").info("lock() done.")

        try:
            if self._cmd == "validate": 
                result = self._doValidate()
            elif self._cmd == "prepare": 
                result = self._doPrepare()
            elif self._cmd == "switch": 
                result = self._doSwitch()
            elif self._cmd == "cancel": 
                result = self._doCancel()
            elif self._cmd == "show": 
                result = self._doShow()
            elif self._cmd == "verify": 
                result = self._doVerify()
            elif self._cmd == "startup": 
                result = self._doStartup()
            else:
                printError("invalid command")
                return 1

        except InstallException as e:
            exc=sys.exc_info()
            self._log("install-exception").warning("Got InstallException: %s, %s, tb=%s", exc[0],  exc[1], traceback.format_tb(exc[2]))
            printError(e.getErrorMessage())
            return 1
        except:
            exc=sys.exc_info()
            self._log("some-exception").warning("Got Exception: %s, %s, tb=%s", exc[0],  exc[1], traceback.format_tb(exc[2]))
            printError("Unexpected error: %s, %s" % (exc[0],  exc[1]))
            return 1

        finally:
            self._log("run").info("About to unlock().")
            self.unlock()
            self._log("run").info("unlock() done.")

        if result is None:
            printError("Internal bug - Got NULL result from command")
            return 1

        return result

    # As copied from mng_file.run() :
    def run_todo (self):
        if self._cmd == "prepare": 
            result = self._doPrepare()
        if self._cmd == "validate": 
            result = self._doValidate()
        else:
            printError("invalid command")
            return 1

        if result is None:
            return 1

        if not result.isOk():
            printError(result.getErrorString())
            return 1

        print result.getOutputYangString()       
        return 0


    def processName (self):
        #not set, will get the data from init param file
        return None

    def changedEarlyLogLevel (self):        
        return logging.WARNING

    @classmethod
    def s_getInitParamsFilesDirEnvVarName (cls):        
        return cls.INIT_PARAM_FILES_DIR_ENV_VAR_NAME

    @classmethod
    def s_createInitParamFiles(cls, dbglog, initParamFilesDir, dictionary):        
        a.infra.format.json.writeToFile(dbglog, dictionary, os.path.join(initParamFilesDir, cls.INIT_PARAM_FILE_NAME), indent=4)


    #business logic

    def createLockFileIfNeeded (self):
        if not os.path.exists(self._lockFileName):
            self._log("create-lock-file").info("createLockFileIfNeeded(): Needed. Creating lock file %s." % self._lockFileName)
            f=open(self._lockFileName, "w")
            f.close()

    def lock (self):
        self._lockHandle=open(self._lockFileName, "r")
        fcntl.flock(self._lockHandle, fcntl.LOCK_EX)

    def unlock (self):
        fcntl.flock(self._lockHandle, fcntl.LOCK_UN)
        self._lockHandle.close()

    def raiseIfPendingRestart (self):
        if self._installManager.isPendingRestart():
            raise InstallException("'switch' command was executed, further install commands cannot be executed until system restarts")

    def _doStartup(self):
        self._log("startup").info("startup() called")        
        self._installManager.startup(self._options.startupLogDir)
        self._log("startup").info("startup() done")
        return 0

    def _doPrepare(self):
        self._log("prepare").info("prepare() called")
        # Do not allow running this command after 'switch'
        self.raiseIfPendingRestart()

        fileArg = self._options.file 
        if fileArg == None:
            self._log("missing-file").error("file option is missing")
            a.infra.process.processFatal("Missing file option")             

        self._log("prepare").info("prepare got file: '%s'", fileArg)
        fileNormalized=self._normalizeFile(fileArg, normalize=not self._options.keepFileName)
        self._log("prepare").info("prepare normalized file: '%s'", fileNormalized)

        if not os.path.exists(fileNormalized):
            self._log("prepare").info("prepare: file '%s' does not exist", fileNormalized)
            printError("File does not exist")
            return 1

        print ("This may take some time, please wait")

        readyVersionAndBuild=self._installManager.getReadyVersion()
        self._log("prepare").info("Ready version+build is '%s'", readyVersionAndBuild)
        if readyVersionAndBuild != None:
            self._log("prepare").info("Canceling ready")
            self._installManager.cancel(readyVersionAndBuild[0], readyVersionAndBuild[1])
            self._log("prepare").info("Calling removeVersionAndSubPkgs()")
            self._installManager.removeVersionAndSubPkgs(readyVersionAndBuild[0], readyVersionAndBuild[1])

        self._log("prepare").info("Calling removeUnneededVersionsFromDisk()")
        self._installManager.removeUnneededVersionsFromDisk()

        if self._installSameVersion:
            # Patch: If --install-same-version is specified, we do the following things to allow it:
            # 1. Check that indeed prepared version is the same as the active version
            # 2. Rename the current version from 'v-b' to 'v-99999999'. This is done by changing the state file.
            # 3. Create a fake pilot for the fake build (ln -s pilot-qb-2.6.0.0-21037 /opt/qb/rpms/pilot-qb-2.6.0.0-99999)


            # Make sure that indeed we are installing the same version
            (newVersion, newBuild) = self._installManager.isPackageValid(fileNormalized)
            (activeVersion, activeBuild) = self._installManager.getActiveVersionAndBuild()

            if (newVersion != activeVersion) or (newBuild != activeBuild):
                msg="prepare(): --install-same-version used, but current version = %s-%s != package file version = %s-%s" \
                    % (activeVersion, activeBuild, newVersion, newBuild)
                self._log("prepare").error(msg)
                raise InstallException(msg)

            # Change name of active version
            fakeVersionAndBuild = self._installManager.combineVersion(activeVersion, a.sys.install.install_manager.kFakeBuildNumber)
            self._log("prepare").info("Changing active version name to %s", fakeVersionAndBuild)
            self._installManager.getStateManager().patchChangeNameOfActiveVersion(fakeVersionAndBuild)

            # Create fake pilot for fake build
            newVersionAndBuild = self._installManager.combineVersion(activeVersion, activeBuild)
            existingPilotName=self._installManager.calcPilotName(newVersionAndBuild)
            fakePilotName=self._installManager.calcPilotName(fakeVersionAndBuild)
            fakePilotDirName = os.path.join(self._rpmsDir, fakePilotName)
            self._log("prepare").info("Creating symlink  %s -> %s", fakePilotDirName, existingPilotName)
            if os.path.lexists(fakePilotDirName):
                os.remove(fakePilotDirName)
            os.symlink(existingPilotName, fakePilotDirName)

        self._log("prepare").info("Calling addSubPkgs(%s)", fileNormalized)
        (version_, build) = self._installManager.addSubPkgs(fileNormalized)

        self._log("prepare").info("setting pilot hints to '%s'", self._pilotHints)
        self._installManager.setPilotHints(self._pilotHints)

        self._log("prepare").info("Calling prepare(%s, %s, usePilotVersion=%s)", version_, build, self._options.usePilotVersion)
        try:
            self._installManager.prepare(version_, build, usePilotVersion=self._options.usePilotVersion)
        except:
            exc=sys.exc_info()
            self._log("prepare").error("prepare() caused exception: %s, %s, tb=%s", exc[0], exc[1], traceback.format_tb(exc[2]))
            if os.path.exists(self._debugFlagFileDontCleanOnError):
                self._log("prepare").info("prepare() failed, %s exists, not removing sub-packages", self._debugFlagFileDontCleanOnError)
                removeSubPackages=False
            else:
                removeSubPackages=True
            self._log("prepare").info("prepare() failed, calling removeVersionAndSubPkgs(%s, %s)", version_, build)
            self._installManager.removeVersionAndSubPkgs(version_, build, removeSubPackages=removeSubPackages)
            self._log("prepare").info("removeVersionAndSubPkgs() done")
            raise
        self._log("prepare").info("prepare() done")
        return 0

    def _doSwitch(self):
        self._log("switch").info("switch() called")

        # Do not allow running this command after 'switch'
        self.raiseIfPendingRestart()

        readyVersionAndBuild=self._installManager.getReadyVersion()
        self._log("switch").info("Ready version+build is '%s'", readyVersionAndBuild)
        if readyVersionAndBuild == None:
            printError ("No software version is ready for switch")
            return 1
        (readyVersion, readyBuild) = readyVersionAndBuild
        self._log("switch").info("Ready version is %s, build is %s", readyVersion, readyBuild)

        version_ = self._options.version 
        if version_ != None:
            self._log("switch-version").info("got version '%s'", version_)
            if version_ != readyVersion:
                printError ("Last prepared version is %s, aborting" % readyVersion)
                return 1
            build = self._options.build
            if build != None:
                self._log("switch-build").info("got build '%s'", build)
                if build != readyBuild:
                    printError ("Last prepared build is %s, aborting" % readyBuild)
                    return 1

        self._log("switch").info("Calling switch(%s, %s)", readyVersion, readyBuild)
        self._installManager.switch(readyVersion, readyBuild)
        return 0

    def _doCancel(self):
        self._log("cancel").info("cancel() called")

        # Do not allow running this command after 'switch'
        self.raiseIfPendingRestart()

        readyVersionAndBuild=self._installManager.getReadyVersion()
        self._log("cancel").info("Ready version+build is '%s'", readyVersionAndBuild)
        if readyVersionAndBuild == None:
            printError ("No version is prepared, nothing to do")
            return 1
        (readyVersion, readyBuild) = readyVersionAndBuild
        self._log("cancel").info("Calling cancel()")
        self._installManager.cancel(readyVersion, readyBuild)
        self._log("cancel").info("Calling removeVersionAndSubPkgs()")
        self._installManager.removeVersionAndSubPkgs(readyVersion, readyBuild)
        self._log("cancel").info("cancel() done")
        return 0

    def _doValidate(self):
        self._log("validate").info("validate() called")

        # Do not allow running this command after 'switch'
        self.raiseIfPendingRestart()

        file_ = self._options.file 
        if file_ == None:
            self._log("missing-file").error("file option is missing")
            a.infra.process.processFatal("Missing file option")

        self._log("validate").info("validate got file: '%s'", file_)
        file_=self._normalizeFile(file_, normalize=not self._options.keepFileName)

        self._log("validate").info("validate normalized file: '%s'", file_)
        if not os.path.exists(file_):
            self._log("validate").info("validate(): file does not exist")
            print "File does not exist"
            return 0

        ret=self._installManager.isPackageValid(file_)
        self._log("validate").info("validate(): isPackageValid() returned '%s'", ret)

        if ret == None:
            print "File is NOT a valid package file"
        else:
            print "File is a valid package file, containing version %s, build %s" % (ret[0], ret[1])
        self._log("validate").info("validate() done")
        return 0

    def _doVerify(self):
        self._log("verify").info("verify() called")

        # Do not allow running this command after 'switch'
        self.raiseIfPendingRestart()

        problems=self._installManager.verify()
        if len(problems)==0:
            print "Verify completed successfully"
        else:
            print "Verify operation found problems:"
            for problem in problems:
                print problem
        self._log("verify").info("verify() done")
        return 0

    def _doShow(self):
        self._log("show").info("show() called")

        (activeVersion, activeBuild)=self._installManager.getActiveVersionAndBuild()
        print ("Current QB software version is %s, build %s" % (activeVersion, activeBuild))

        readyVersionAndBuild=self._installManager.getReadyVersion2()
        if readyVersionAndBuild == None:
            print ("No QB software version is ready for switch")
        else:
            (readyVersion, readyBuild, switchType) = readyVersionAndBuild
            print ("QB Software version %s, build %s is ready for switch" % (readyVersion, readyBuild))
            # switchType may be None (Never supposed to happen, since we always use a pilot at least as new as us, but still)
            if switchType:
                print ("Switch type is '%s'" % switchType)

        if self._installManager.isPendingRestart():
            print ("'switch' command was executed, waiting for system to restart")

        return 0


    def _normalizeFile (self, file_, normalize=True):
        self._log("normalize").info("Normalizing file '%s', userRootDir '%s', normalize=%s", file_, self._userRootDir, normalize)
        if normalize:
            if not file_.startswith(self._userRootDir):
                if file_.startswith(os.path.sep):
                    file_ = file_[1:]
                file_ = os.path.join(self._userRootDir, file_)
        self._log("normalize").info("Result: '%s'", file_)
        return file_
