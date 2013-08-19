# Copyright Qwilt, 2013
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: shmulika

import distutils.dir_util
import os
import shutil
import stat
import subprocess as originalsubprocess

import a.infra.subprocess
import a.infra.format.json
import a.sys.secure_digital.utils

# Bypass for PyChecker
if  __package__ is None:
    G_MODULE_NAME_SECURE_DIGITAL                  = "unknown"
    G_GROUP_NAME_SECURE_DIGITAL_RFS_INSTALLER     = "unknown"
else:
    from . import G_MODULE_NAME_SECURE_DIGITAL      
    from . import G_GROUP_NAME_SECURE_DIGITAL_RFS_INSTALLER 



fstabTextTemplate = """
# /etc/fstab created by sd-manager
LABEL=%(sdMainPartitionLabel)s  /                       %(sdMainPartitionFsType)s    defaults        1 1
LABEL=%(sdBootPartitionLabel)s  %(sdBootMountPoint)s    %(sdBootPartitionFsType)s    defaults        1 2
LABEL=%(sdVitalPartitionLabel)s %(sdVitalMountPoint)s   %(sdVitalPartitionFsType)s   defaults        1 2
tmpfs                           /dev/shm                tmpfs                        defaults        0 0 
devpts                          /dev/pts                devpts                       gid=5,mode=620  0 0
sysfs                           /sys                    sysfs                        defaults        0 0
proc                            /proc                   proc                         defaults        0 0
"""


class RfsInstallerError(Exception):
    def __init__ (self, msg):
        Exception.__init__(self, msg)

class RfsInstaller(object):

    RPM_REMOVE_EXPECTED_ERR_MSG = "Stopping system message bus: [FAILED]"
    DEAFULT_KILL_TIMEOUT        = 180
    DEAFULT_WARNING_TIMEOUT     = 90

    # Note: We assume the RFS is in a known & fixed location,
    # we do not "search" for 'rfs-*' because 

    # TODO(shmulika): remove from code commented-out code like "rm -rf" and "cp -f", when sure of changes

    INSTALL_SUB_PKGS_SUFFIX     = "install/0/var/sub-pkgs"

    def __init__ (self, logger, sdUtils):        
        self._log = logger.createLoggerSameModule(G_GROUP_NAME_SECURE_DIGITAL_RFS_INSTALLER)

        self._krustyBaseDir              = a.infra.process.substitueSystemKnownPaths(os.path.join(a.infra.process.captain.Captain.PATH_SUBSITUTION_KEY_APPLICATIONS_PATH, "krusty_install"))
        self._krustyInstallDirectory     = self._krustyBaseDir
        self._krustyInstallDataDirectory = os.path.join(self._krustyInstallDirectory, "data")
        self._krustyInstallDataFile      = os.path.join(self._krustyInstallDirectory, "install-data.json")
        self._servAdminRpmsDirectory     = os.path.join(self._krustyInstallDirectory, "srv-admin")
        self._servAdminRpmsInfoFile      = os.path.join(self._servAdminRpmsDirectory, "info.json")
        self._generalRpmsDirectory     = os.path.join(self._krustyInstallDirectory, "general")
        self._generalRpmsInfoFile      = os.path.join(self._generalRpmsDirectory, "info.json")

        self._installSubPkgs = a.infra.process.substitueSystemKnownPaths(os.path.join(a.infra.process.captain.Captain.PATH_SUBSITUTION_KEY_APPLICATION_SYS_PATH, self.INSTALL_SUB_PKGS_SUFFIX))

        self._sdUtils = sdUtils

        self._progressOut = None

        # Used for doing the RPM actions upon, then copy results to SD
        self._intermediateRfsRoot = "/tmp/rfs_installer/tmp_rfs"


    def initTargetRfsPath (self, targetRfsPath):        
        self._targetRfsPath = targetRfsPath
        self._log("init-target-rfs-path").notice("target RFS path initialized to: %s", self._targetRfsPath)


    def initProgressOut (self, progressOut):
        """ Output stream into which write progress "report" (advancing dots...)
        """
        self._progressOut = progressOut


    def install (self):
        self._log("install").notice("Installing the krusty RFS on %s", self._targetRfsPath)
        self._readInstallData()
        self._createRfsTempDirectory(self._intermediateRfsRoot)
        self._writeProgress(".", newLine = False ,progressOut = self._progressOut)                
        self._extractRfs(self._intermediateRfsRoot)
        self._writeProgress(".", newLine = False ,progressOut = self._progressOut)
        self._removeRpms(self._intermediateRfsRoot) 
        self._writeProgress(".", newLine = False ,progressOut = self._progressOut)
        self._installGeneralRpms(self._intermediateRfsRoot)
        self._writeProgress(".", newLine = False ,progressOut = self._progressOut)
        self._installServAdminRpms(self._intermediateRfsRoot)       
        self._writeProgress(".", newLine = False ,progressOut = self._progressOut)
        self._copyRfs(self._intermediateRfsRoot, self._targetRfsPath)
        self._writeProgress(".", newLine = False ,progressOut = self._progressOut)
        self._removeAllData(self._targetRfsPath)
        self._writeProgress(".", newLine = False ,progressOut = self._progressOut)
        self._addAllData(self._targetRfsPath)        
        self._writeProgress(".", newLine = False ,progressOut = self._progressOut)
        self._addAllSymLinks(self._targetRfsPath)
        self._writeProgress(".", newLine = False ,progressOut = self._progressOut)
        self._writeFstabToRfs(self._targetRfsPath)
        self._writeProgress(".", newLine = False ,progressOut = self._progressOut)
        self._handleServices(self._targetRfsPath)
        self._writeProgress(".", newLine = False ,progressOut = self._progressOut)
        self._makeMountPointsOnRfs(self._targetRfsPath)       
       

#-----------------------------------------------------------------------------#
    ######################################
    # PRIVATE MAIN LOGIC
    ######################################
 
    def _createRfsTempDirectory (self, targetRfsPath):
        self._log("create-rfs-temp-directory").notice("creating temp rfs directory at %s", targetRfsPath)
        if os.path.exists(targetRfsPath):
            shutil.rmtree(targetRfsPath) #self._runCommandRaiseIfFail("rm -rf %s" % targetRfsPath)
        os.makedirs(targetRfsPath)       #self._runCommandRaiseIfFail("mkdir -p %s" % targetRfsPath)


    def _readInstallData (self):
        self._log("read-install-data").notice("Reading install data from %s", self._krustyInstallDataFile)
        self._installData = a.infra.format.json.readFromFile(self._log, self._krustyInstallDataFile)

        self._dataToAdd    = self._installData["data"]
        self._symLinks     = self._installData["sym-links"]
        self._dataToRemove = self._installData["delete"]
        self._rpmsToRemove = self._installData["rpms-remove"]
        self._rfsInfo      = self._installData["rfs"]
        self._services     = self._installData["services"]


    def _extractRfs (self, targetRfsPath):
        # Note: extracting the tar on the secure-digital might be long (SD has slow IO)
        rfsTarFile = os.path.join(self._installSubPkgs, self._rfsInfo["tar-path-relative-to-sub-pkgs"])
        self._log("extract-rfs").notice("Extracting rfs tar file %s onto %s", rfsTarFile, targetRfsPath)
        self._runCommandRaiseIfFail("tar x --bzip2 -f %s -C %s" % (rfsTarFile, targetRfsPath), killTimeout = 600, warningTimeout = 300) 


    def _removeAllData (self, targetRfsPath):
        self._log("remove-all-data").notice("removing data from the krusty RFS:")
        for name in self._dataToRemove:
            target = self._dataNameToTarget(name, targetRfsPath)
            self._removeData(target)


    def _addAllData (self, targetRfsPath):        
        self._log("add-all-data").notice("adding data to the krusty RFS:")
        for name, data in self._dataToAdd.items():
            target = self._dataNameToTarget(name, targetRfsPath)
            source = self._dataNameToSource(name)

            if self._isDataItemDir(data):
                self._addDirectory(target, data)
            else:
                self._addFile(source, target, data)


    def _addAllSymLinks (self, targetRfsPath):
        self._log("add-all-sym-links").notice("adding symlinks to the krusty RFS:")
        for linkFrom, linkTo in self._symLinks.items():            
            linkFromTarget = self._dataNameToTarget(linkFrom, targetRfsPath)
            self._addSymLink(linkFromTarget, linkTo)
            

    def _removeRpms (self, targetRfsPath):
        self._log("remove-rpms").notice("removing rpms from the krusty RFS:")
        self._log("remove-rpms").debug1("rpms to be removed are: %s", self._rpmsToRemove)

        rpmsString = " ".join(self._rpmsToRemove)

        # Removing unrequired RPMS that bloat up the RFS (rpm throws a known error, although it succesfully removes the packages)
        rc,outText,errText = self._runCommand("rpm --root=%s -e %s" % (targetRfsPath, rpmsString), killTimeout = 1200, warningTimeout = 300)
        if rc != 0:
            if errText is None:
                self._logErrorAndRaise("Unexpected error when reducing rpms from SD RFS. stdout=%s, errText=%s" % (outText, errText))
            elif errText.rfind(self.RPM_REMOVE_EXPECTED_ERR_MSG) < 0:
                self._logErrorAndRaise("Unexpected error when reducing rpms from SD RFS. stdout=%s, errText=%s" % (outText, errText))


    def _writeFstabToRfs (self, targetRfsPath):
        self._log("write-fstab-to-rfs").debug1("Writing /etc/fstab to SD RFS:")
        fstabText = self._getFstabText()
        self._log("write-fstab-to-rfs").debug1("contents of /etc/fstab='%s'", fstabText)

        fstabPath = os.path.join(targetRfsPath, "etc/fstab")
        with open(fstabPath, 'a') as fileOut:
            fileOut.write(fstabText)

        self._log("write-fstab-to-rfs").debug1("Succesfuly wrote /etc/fstab to SD RFS.")


    def _handleServices (self, targetRfsPath):
        self._log("handle-services").debug1("Enabling services: %s", self._services)

        for service in self._services:
            name   = service["name"]
            action = service["action"]
            self._runCommandRaiseIfFail("chroot %s chkconfig --%s %s" % (targetRfsPath, action, name))

        self._log("handle-services").debug1("Succesfuly enabled services.")
        


    def _makeMountPointsOnRfs (self, targetRfsPath):        
        sdBootMountPoint       = self._getBootMountPoint()
        sdVitalMountPoint      = self._getVitalMountPoint()

        # Notice: we create directories inside the sd-main mount-point, which is "/" for the sd fstab
        sdBootMountPointOnRfs  = os.path.join(targetRfsPath, self._removeRootFromPath(sdBootMountPoint))
        sdVitalMountPointOnRfs = os.path.join(targetRfsPath, self._removeRootFromPath(sdVitalMountPoint))
        
        if not os.path.exists(sdBootMountPointOnRfs):
            os.makedirs(sdBootMountPointOnRfs) # self._runCommandRaiseIfFail("mkdir -p %s" % (sdBootMountPointOnRfs))

        if not os.path.exists(sdVitalMountPointOnRfs):
            os.makedirs(sdVitalMountPointOnRfs) # self._runCommandRaiseIfFail("mkdir -p %s" % (sdVitalMountPointOnRfs))

        self._log("make-mount-points-on-rfs").notice("Created these directories (mount point) on the rfs: %s", [sdBootMountPointOnRfs, sdVitalMountPointOnRfs])


    def _installGeneralRpms (self, targetRfsPath):
        self._log("install-general-rmps").notice("Installing general rpms:")
        self._installRpms(self._generalRpmsDirectory, self._generalRpmsInfoFile, targetRfsPath)


    def _installServAdminRpms (self, targetRfsPath):
        self._log("install-serv-admin-rmps").notice("Installing srv-admin rpms:")
        self._installRpms(self._servAdminRpmsDirectory, self._servAdminRpmsInfoFile, targetRfsPath)


    def _copyRfs (self, sourceRfsPath, targetRfsPath):
        self._log("copy-rfs").notice("copying rfs content from %s to %s" % (sourceRfsPath, targetRfsPath))
        self._runCommandRaiseIfFail("sync", killTimeout = 900)
        distutils.dir_util.copy_tree(sourceRfsPath, targetRfsPath, preserve_symlinks = 1)
        self._runCommandRaiseIfFail("sync", killTimeout = 900)


#-----------------------------------------------------------------------------#
    ######################################
    # PRIVATE LOGIC UTILS
    ######################################


    def _addDirectory (self, target, data):
        if not os.path.exists(target):
            os.makedirs(target) # self._runCommandRaiseIfFail("mkdir -p %s" % target)
        self._setPermissions(target, data)


    def _addFile (self, source, target, data):
        shutil.copyfile(source, target) #self._runCommandRaiseIfFail("cp -f %s %s" % (source, target))
        self._setPermissions(target, data)


    def _addSymLink (self, linkFrom, linkTo):
        if os.path.exists(linkFrom):
            os.remove(linkFrom)

        os.symlink(linkTo, linkFrom) #self._runCommandRaiseIfFail("ln -s %s %s" % (linkTo, linkFrom))


    def _setPermissions (self, target, data):
        permissions = self._getDataItemPerm(data)
        os.chmod(target, permissions)


    def _removeData (self, target):
        if not os.path.exists(target):
            return

        if os.path.isdir(target):
            shutil.rmtree(target)
        else:
            os.remove(target)

        #self._runCommandRaiseIfFail("rm -rf %s" % target)


    def _installRpms (self, rpmsDirectory, rpmsInfoFile, targetRfsPath):
        self._log("install-rmps").notice("Installing rpms according to info file %s:", rpmsInfoFile)
        rpmsInfo = a.infra.format.json.readFromFile(self._log, rpmsInfoFile)
        self._log("install-rmps").notice("rpms info file contents = %s:", rpmsInfo)
        rpms = rpmsInfo["rpms"]

        rpmsFullPath = [os.path.join(rpmsDirectory, rpm["filename"]) for rpm in rpms]
        allRpms = " ".join(rpmsFullPath)
        self._runCommandRaiseIfFail("rpm --root %s -i %s" % (targetRfsPath, allRpms), killTimeout = 1200, warningTimeout = 300)


    # Gets permissions string, check if it is a directory
    def _isDataItemDir (self, dataAttr):
        perm=dataAttr['perm']
        return perm.startswith('d')

    # Gets permissions string, check if it is a file
    def _isDataItemFile (self, dataAttr):
        perm=dataAttr['perm']
        return perm.startswith('-')

    # Returns permission bits from a perm string
    def _getDataItemPerm (self, dataAttr):
        perm=dataAttr['perm']
        res=0
        if perm[1]=='r':
            res |= stat.S_IRUSR
        if perm[2]=='w':
            res |= stat.S_IWUSR
        if perm[3]=='x':
            res |= stat.S_IXUSR
        if perm[4]=='r':
            res |= stat.S_IRGRP
        if perm[5]=='w':
            res |= stat.S_IWGRP
        if perm[6]=='x':
            res |= stat.S_IXGRP
        if perm[7]=='r':
            res |= stat.S_IROTH
        if perm[8]=='w':
            res |= stat.S_IWOTH
        if perm[9]=='x':
            res |= stat.S_IXOTH
        return res


    def _dataNameToTarget (self, name, targetRfsPath):
        return os.path.join(targetRfsPath, name)


    def _dataNameToSource (self, name):
        return os.path.join(self._krustyInstallDataDirectory, name)


    def _getFstabText (self):
        sdMainPartitionLabel   = self._sdUtils.getMainPartitionFileSystemLabel()
        sdMainPartitionFsType  = self._sdUtils.getMainPartitionFileSystemType()
                               
        sdBootPartitionLabel   = self._sdUtils.getBootPartitionFileSystemLabel()
        sdBootPartitionFsType  = self._sdUtils.getBootPartitionFileSystemType() 
        sdBootMountPoint       = self._getBootMountPoint()

        sdVitalPartitionLabel  = self._sdUtils.getVitalPartitionFileSystemLabel()
        sdVitalPartitionFsType = self._sdUtils.getVitalPartitionFileSystemType() 
        sdVitalMountPoint      = self._getVitalMountPoint()
        
        textTokens = {'sdMainPartitionLabel'   : sdMainPartitionLabel,
                      'sdMainPartitionFsType'  : sdMainPartitionFsType,
                      'sdBootPartitionLabel'   : sdBootPartitionLabel,
                      'sdBootPartitionFsType'  : sdBootPartitionFsType,
                      'sdBootMountPoint'       : sdBootMountPoint,
                      'sdVitalPartitionLabel'  : sdVitalPartitionLabel,
                      'sdVitalPartitionFsType' : sdVitalPartitionFsType,
                      'sdVitalMountPoint'      : sdVitalMountPoint}

        return fstabTextTemplate % textTokens


    def _getBootMountPoint (self):
        return self._sdUtils.getBootPartitionMountPoint(noPrefix = True)

    def _getVitalMountPoint (self):
        return self._sdUtils.getVitalPartitionMountPoint(noPrefix = True)


#-----------------------------------------------------------------------------#
    ######################################
    # SUB PROCESS PRIVATE UTILS
    ######################################


    def _runCommand (self, cmd, killTimeout = DEAFULT_KILL_TIMEOUT, warningTimeout = DEAFULT_WARNING_TIMEOUT, shell = False):
        subprocess = a.infra.subprocess.Subprocess("boot-utils", self._log)
        args = cmd
        if not shell:
            args = cmd.split()
        
        try:
            self._log("run-command").notice("running command, args=%s", args)
            subprocess.start(args, stdout = originalsubprocess.PIPE, stderr = originalsubprocess.PIPE, shell = shell)
            omreportStdout, omreportStderr = subprocess.communicate(killTimeOut = killTimeout, warningTimeOut = warningTimeout)
            self._log("run-command").notice("command stdout = %s, stderr = %s", omreportStdout, omreportStderr)
        except Exception as exception:
            self._log("run-command").error("Failed executing cmd %s, error=%s", args, exception, exc_info = 1)
            return (1, "", "")
        
        returnCode = subprocess.getReturnCode()                
        self._log("run-command").notice("command rc = %s", returnCode)
        return (returnCode, omreportStdout, omreportStderr)


    def _runCommandRaiseIfFail (self, command, killTimeout = DEAFULT_KILL_TIMEOUT, warningTimeout = DEAFULT_WARNING_TIMEOUT, shell=False):
        """Returns a tuple (outText,errText)"""
        (rc,outText,errText) = self._runCommand(command, killTimeout = killTimeout, warningTimeout = warningTimeout, shell = shell)
        if rc != 0:
            self._log("run-command-raising").warning("Command returned '%s', stderr=%s, raising exception", rc, errText)
            raise RfsInstallerError("Failed running command %s" % command)
        return (outText,errText)


#-----------------------------------------------------------------------------#
    ######################################
    # MISC PRIVATE UTILS
    ######################################

    def _writeProgress (self, message, newLine ,progressOut = None):
        if progressOut is not None:
            progressOut.write(message)
            if newLine:
                progressOut.write("\n")
            progressOut.flush()


    def _logErrorAndRaise (self, msg):        
        msg = "krusty-rfs-install error occured: %s" % msg
        self._log("log-error-and-raise").error(msg)
        raise RfsInstallerError(msg) 


    def _removeRootFromPath (self, pathString):
        if len(pathString) == 0:
            return pathString
        if pathString[0] == "/":
            return pathString[1:]
        else:
            return pathString
