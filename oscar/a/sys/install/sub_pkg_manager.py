# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

import json
import os
import re
import subprocess

from a.sys.install.exceptions import InstallException
from yum.yum import Yum
from rpm.rpm import Rpm
from a.sys.install.utils import Utils

class SubPkgManager(object):

    def __init__ (self, logger):
        self._log=logger.createLogger("sys-install","sub-pkg-mng")
        self.utils=Utils(self._log)
        self.useFakeChrootMode=False
        self.rootDir=None
        self.subPkgDir=None
        self.subPkgTempDir=None

    def setDirs (self, rootDir, subPkgDir, subPkgTempDir, rpmKeysDir, useFakeChrootMode=False):
        self._raiseIfNotAbsPath(subPkgDir, "subPkgDir")
        self._raiseIfNotAbsPath(subPkgTempDir, "subPkgTempDir")
        self.rootDir=rootDir
        self.subPkgDir=subPkgDir
        self.subPkgTempDir=subPkgTempDir
        self.rpmKeysDir=rpmKeysDir
        self.useFakeChrootMode=useFakeChrootMode
        self.infoDir=os.path.join(self.subPkgDir, "info")

        # During first install, sub-packages dir may not exist
        if not os.path.exists(self.subPkgDir):
            self.utils.runCommandRaiseIfFail("mkdir -p "+self.subPkgDir)


    def findVersionInFile (self, product, r2pmFile):
        """
        Expects an r2pm file with exactly one sub-pkg called 'qb-VVV-BBB'.
        File must be below root dir

        Returns version found in r2pm file (i.e. the string VVV-BBB).
        If not exactly one such sub-pkg is found, returns None (="Invalid package file")
        """

        self._log("find-version-called").info("findVersionInFile() called, product=%s, r2pmFile=%s", product, r2pmFile)
        self._raiseIfNotAbsPath(r2pmFile, "r2pmFile")

        # Find version
        rpm=Rpm(self._log)
        if self.useFakeChrootMode:
            rpm.setRoot(self.rootDir, self.useFakeChrootMode)
            r2pmFile=self._getFilePathFromRoot(r2pmFile)
        files=rpm.doListFiles(r2pmFile)

        self._log("find-version-files").info("findVersionInFile(): files=%s", files)
        version_=None
        count_=0
        for file_ in files:
            mo=re.match("^/info/"+product+"-(.*)\.info$",file_)
            if mo != None:
                version_=mo.group(1)
                count_+=1
        if count_ != 1:
            self._log("find-version-bad-count").error("findVersionInFile(): File %s has %s sub-pkgs called "
                                                       "'%s-...', should have exactly one", r2pmFile, count_, product)
            return None
        return version_

    def add (self, r2pmFile=None, httpRepo=None, packageName=None):
        """
        Adds sub-packages, either from a r2pm file or from an http repo.
        To install from file:
        r2pmFile : file name

        To install from an http repo:
        httpRepo : repo address
        packageName : Name of package containing the sub-packages

        Returns a tuple (subPkgs, subPkgstoRemove).
        subPkgs: list of sub-pkgs included in this version. 
        subPkgstoRemove: list of new sub-pkgs (Replaced sub-pkgs are not included in that list). These sub-pkgs
        will be removed if 'prepare' operation is canceled
        """

        self._log("add-called").info("add() called, r2pmFile=%s, httpRepo=%s, packageName=%s", r2pmFile, httpRepo, packageName)

        # Check that our input makes sense
        if (r2pmFile == None) == (httpRepo == None):
            msg = "add(): bad parameters, must use either r2pmFile or httpRepo"
            self._log("add-called-bad").error(msg)
            raise InstallException(msg)

        if r2pmFile != None:
            self._raiseIfNotAbsPath(r2pmFile, "r2pmFile")
        else:
            if packageName == None:
                msg = "add(): bad parameters, httpRepo must come with packageName"
                self._log("add-called-bad").error(msg)
                raise InstallException(msg)

        # Clean the temp dir and create it
        if not self.useFakeChrootMode:
            # In ut fakechroot mode we do not remove this, because this dir has chroot soft links
            self._cleanTempDir()
        self.utils.runCommandRaiseIfFail("mkdir -p "+self.subPkgTempDir)

        # Import RPM public keys
        # In unit tests, it is impossible to get keys from outside of the chroot. Instead, the test does rpm --import
        # in this chroot for us.
        if not self.useFakeChrootMode:
            rpm=Rpm(self._log)
            rpm.setRoot(self.subPkgTempDir)
            for keyFile in os.listdir(self.rpmKeysDir):
                rpm.doImport(os.path.join(self.rpmKeysDir, keyFile))

        # Check space - must have at least 4GB free
        availableSize=self.utils.getAvailableSize(self.subPkgTempDir)
        if availableSize < 4e9:
            raise InstallException("Internal error: Not enough space on system disk")

        # Read all existing sub-pkgs
        oldInfoDict=self._readInfoFiles(self.infoDir)
        self._log("add-sub-pkg").info("add(): Found old sub-pkgs %s", oldInfoDict)
        oldSubPkgs=oldInfoDict.keys()

        # Create temp dir for yum (for config file and such)
        if not self.useFakeChrootMode:
            yumTempDir=os.path.join(self.subPkgTempDir, "tmp")
        else:
            yumTempDir="/tmp"

        # Extract r2pm into temp dir
        try:
            if r2pmFile != None:
                # Install from file
                removeFile=False
                if not self.useFakeChrootMode:
                    r2pmNameToYum=r2pmFile
                    # In CentOS6.2, package files must end with '.rpm'
                    if not r2pmNameToYum.endswith('.rpm'):
                        r2pmNameToYum=os.path.join(self.subPkgTempDir, 'package.rpm')
                        self._log("add-sub-pkg-copy").info("add(): Copying %s to %s to have a file name that ends with .rpm", r2pmFile, r2pmNameToYum)
                        self.utils.runCommandRaiseIfFail("cp -f %s %s" % (r2pmFile, r2pmNameToYum))
                        removeFile=True

                else:
                    self.utils.runCommandRaiseIfFail("cp "+r2pmFile+" "+self.subPkgTempDir)
                    r2pmNameToYum="/"+os.path.basename(r2pmFile)
                yum=Yum(self._log, yumTempDir)
                yum.setRoot(self.subPkgTempDir, useFakeChrootMode=self.useFakeChrootMode)
                yum.doLocalInstall(r2pmNameToYum)
                if removeFile:
                    self._log("add-sub-pkg-remove").info("add(): Removing file that was copied")
                    self.utils.runCommandRaiseIfFail("rm -f %s" % r2pmNameToYum)
            else:
                # Install from http repo
                yum=Yum(self._log, yumTempDir)
                yum.setRoot(self.subPkgTempDir, useFakeChrootMode=self.useFakeChrootMode)
                yum.addHttpRepo("network", httpRepo)
                yum.doInstall(packageName)


            # Now, move/replace new sub-pkgs into subPkgDir.
            # We do this according to a very specific sequence, so that in case we abort in the middle (power failure or whatever),
            # A call to TBD() will restore things the way they were before this operation
            # Todo(orens): TBD -> Real function
            # Sequence is:
            # 1. Copy all existing sub-packages to self.subPkgTempDir, except for those found there already (i.e. new copy
            #    is better tahn old copy)
            # 2. Rename self.subPkgDir with a '.tmp' suffix
            # 3. Rename self.subPkgTempDir to become self.subPkgDir
            # 4. Remove self.subPkgDir + '.tmp'

            # System is always stable, excelt for the split-second between 2 and 3.

            # Read list of new sub-packages
            newInfoDict=self._readInfoFiles(os.path.join(self.subPkgTempDir, "info"))
            self._log("add-sub-pkg").info("add(): Found new sub-pkgs %s", newInfoDict)
            newSubPkgs=newInfoDict.keys()

            # Sanity-check the new info: Make sure new sub-pkgs have all the data we need in their .info files
            for subPkg in newSubPkgs:
                info=newInfoDict[subPkg]
                if not 'dir' in info:
                    self._log("add-bad-info-dir").error("add(): sub-pkg %s info does not have 'dir'", subPkg)
                    return None
                infoDirPath=os.path.join(self.subPkgTempDir, info['dir'])
                if not os.path.isdir(infoDirPath):
                    self._log("add-missing-dir").error("add(): sub-pkg %s info has 'dir'->%s, does not exist", 
                                                                 subPkg, infoDirPath)
                    return None
                if not 'name' in info:
                    self._log("add-bad-info-name").error("add(): sub-pkg %s info does not have 'name'", subPkg)
                    return None
                if info['name'] != subPkg:
                    self._log("add-bad-name").error("add(): sub-pkg %s info has 'name'=%s, should be identical", 
                                                              subPkg, info['name'])
                    return None

            # Step 1: Copy all old sub-packages, which are not found in the new dir, to the new dir
            for subPkg in oldSubPkgs:
                if subPkg not in newSubPkgs:
                    oldInfoFile=self._getInfoFileName(self.subPkgDir, subPkg)
                    newInfoFile=self._getInfoFileName(self.subPkgTempDir, subPkg)
                    oldSubPkgDir=os.path.join(self.subPkgDir, oldInfoDict[subPkg]['dir'])
                    newSubPkgDir=os.path.join(self.subPkgTempDir, oldInfoDict[subPkg]['dir'])
                    if os.path.exists(newSubPkgDir):
                        self._log("add-bad-name").error("add(): old sub-pkg %s not found in new sub-packages, but %s exists", 
                                                        subPkg, newSubPkgDir)
                        return None
                    self.utils.runCommandRaiseIfFail("cp -vpf %s %s" % (oldInfoFile, newInfoFile))
                    self.utils.runCommandRaiseIfFail("cp -vrpf %s %s" % (oldSubPkgDir, newSubPkgDir))
            
            # Steps 2-4: Copy all old sub-packages, which are not found in the new dir, to the new dir
            tmpOldName = self.subPkgDir+'.tmp'
            self.utils.runCommandRaiseIfFail("mv -vf %s %s" % (self.subPkgDir, tmpOldName))
            self.utils.runCommandRaiseIfFail("mv -vf %s %s" % (self.subPkgTempDir, self.subPkgDir))
            self.utils.runCommandRaiseIfFail("rm -vrf %s" % (tmpOldName))

        finally:
            # Remove the install-temp directory, no sense in leaving it here
            self._cleanTempDir()

        # oldInfoDict.keys() holds the list of subPkgs before the install. Let's find out what was added.
        newInfoDict=self._readInfoFiles(self.infoDir)

        # Sorting makes it easy on unit tests :-)
        addedSubPkgs=sorted(list(set(newInfoDict.keys())-set(oldInfoDict.keys())))
        return (sorted(newSubPkgs), addedSubPkgs)

    def removeSubPackages (self, subPackages):
        """
        Removes a set of existing sub-pkgs
        """
        self._log("remove-sub-packages").info("removeSubPackages() called, subPackages=%s", subPackages)
        infoDict=self._readInfoFiles(self.infoDir)
        for subPkg in subPackages:
            if not subPkg in infoDict:
                self._log("remove-sub-packages").error("removeSubPackages(): sub-package %s not found", subPkg)
                continue
            subPkgDir=os.path.join(self.subPkgDir, infoDict[subPkg]['dir'])
            self.utils.runCommandRaiseIfFail("rm -rf %s" % subPkgDir)
            infoFileName=self._getInfoFileName(self.subPkgDir, subPkg)
            self.utils.runCommandRaiseIfFail("rm %s" % infoFileName)

    def addReposToYum (self, yum, repoFilter=None):
        self._log("add-repos-to-yum").info("addReposToYum() called, repoFilter=%s", repoFilter)
        infoDict=self._readInfoFiles(self.infoDir)
        for info in infoDict.keys():
            infoData=infoDict[info]
            if infoData['type'] == 'repository':
                repoDir=os.path.join(self.subPkgDir, infoData['dir'])
                repoName=infoData['name']
                if (repoFilter is None) or (repoName.find(repoFilter) != -1):
                    self._log("add-repos-to-yum").info("addReposToYum(): Adding repoDir=%s", repoDir)
                    yum.addDiskRepo(repoName, repoDir)

    def getSubPkgs (self):
        return self._readInfoFiles(self.infoDir)

    def getSubPkgsDir (self):
        return self.subPkgDir

    def _getFilePathFromRoot (self, r2pmFile):
        if not self.useFakeChrootMode:
            return r2pmFile

        if r2pmFile.startswith(self.rootDir):
            return r2pmFile[len(self.rootDir):]
        raise ValueError("File %s not in root dir %s" % (r2pmFile, self.rootDir))


    def _readInfoFiles (self, fromDir):
        """
        Returns a dict of all info files found in fromDir.
        For each file <fromDir>/X.info: X is key, value is a dict with the content of the info file
        """

        self._raiseIfNotAbsPath(fromDir, "fromDir")

        # No directory ? No sub-pkgs !
        if not os.path.exists(fromDir):
            return {}

        files=os.listdir(fromDir)
        ret={}
        for file_ in files:
            mo=re.match("^(.*)\.info$",file_)
            if mo != None:
                subPkg=mo.group(1)
                ret[subPkg]=self._readInfoFile(os.path.join(fromDir, file_))
        return ret
                
    def _readInfoFile (self, infoFileName):
        f=open(infoFileName,"r")
        text=f.read()
        f.close()
        self._log("read-info-file").info("_readInfoFile(): Info file %s has text %s", infoFileName, text)
        return json.loads(text)

    def _getInfoFileName (self, root, subPkg):
        return os.path.join(root, "info", subPkg+".info")

    def _cleanTempDir (self):
        self.utils.runCommandRaiseIfFail("rm -rf "+self.subPkgTempDir)

    def _raiseIfNotAbsPath (self, pathToCheck, name):
        if not pathToCheck.startswith('/'):
            raise ValueError("%s must start with '/', value given is '%s'" % (name, pathToCheck))

        

