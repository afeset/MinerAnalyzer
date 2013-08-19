# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

import re
import subprocess

from a.sys.install.utils import Utils

class Rpm(object):
    def __init__ (self, logger):
        self._log=logger.createLogger("sys-install","rpm-rpm")
        self.utils=Utils(self._log)
        self.rootDir=None
        self.useFakeChrootMode=False
        self._updateCommand()

    def setRoot (self, rootDir, useFakeChrootMode=False):
        self._raiseIfNotAbsPath(rootDir, "rootDir")
        self.rootDir=rootDir
        self.useFakeChrootMode=useFakeChrootMode
        self._updateCommand()

    def doImport (self, keyPath):
        """
        Imports a public key (from an armoured ascii file) into the RPM db
        """

        self._log("do-import-called").info("doImport(%s) called", keyPath)
        self._raiseIfNotAbsPath(keyPath, "keyPath")
        self._runRpmRaiseIfFail("--import "+keyPath)

    def doValidateRpm (self, rpmPath):
        """
        Checks that a given RPM file is properly signed
        Returns True if file is properly signed
        """

        self._log("do-validate-rpm-called").info("doValidateRpm(%s) called", rpmPath)
        self._raiseIfNotAbsPath(rpmPath, "rpmPath")
        (rc,outText,_)=self._runRpm("--checksig "+rpmPath)
        if rc != 0:
            self._log("do-validate-rpm-called").warning("doValidateRpm(%s): rpm returned %s", rpmPath, rc)
            return False
        if re.search("rsa ", outText) == None:
            self._log("do-validate-rpm-called").warning("doValidateRpm(%s): rpm output is '%s', no 'rsa ' found", rpmPath, outText)
            return False
        if re.search(" pgp ", outText) == None:
            self._log("do-validate-rpm-called").warning("doValidateRpm(%s): rpm output is '%s', no ' gpg ' found", rpmPath, outText)
            return False
        return True

    def doVerifyAllInstalled (self):
        """
        Verifies all install packages, comparing files on disk against md5sums remembered from package. 
        Returns list of strings with problems. If no problems, returns empty string
        """

        self._log("do-verify-all-installed-called").info("doVerifyAllInstalled() called")
        cmd=" --verify --all"

        # --nomode is required due to the fakeroot thing used for unit testing: a file with -r--r--r-- permissions
        # inside the RPM is generated as a -rw-r--r-- file when installed
        if self.useFakeChrootMode:
            cmd=cmd+" --nomode"
        (rc, outText, _)=self._runRpm(cmd)
        if rc==0:
            return []
        return filter(lambda x: x.strip() != "", outText.split('\n'))

    def isInstalled (self, package):
        self._log("is-installed-called").info("isInstalled(%s) called", package)
        (rc,outText,errText)=self._runRpm("-q "+package)
        if (rc==1) and (outText.find("is not installed") != -1):
            return False
        if rc==0:
            return True
        raise RuntimeError("RPM command 'rpm -q %s' failed" % package)

    def doInstall (self, rpmPath):
        self._log("do-install-called").info("doInstall(%s) called", rpmPath)
        self._raiseIfNotAbsPath(rpmPath, "rpmPath")
        self._runRpmRaiseIfFail("--install "+rpmPath)

    def doRemove (self, package):
        self._log("do-remove-called").info("doRemove(%s) called", package)
        self._runRpmRaiseIfFail("--erase "+package)

    def doListFiles (self, rpmPath):
        """Returns a list of files in an RPM file"""
        self._log("do-list-files-called").info("doListFiles(%s) called", rpmPath)
        self._raiseIfNotAbsPath(rpmPath, "rpmPath")
        (outText,errText)=self._runRpmRaiseIfFail("-qpl "+rpmPath)
        files=outText.split()
        self._log("do-list-files-returning").info("doListFiles(%s) returning '%s'", rpmPath, files)
        return sorted(files)

    def doListRequires (self, package):
        """
        Returns a list of capabilities that a package required. Package should be installed.
        If package is not installed, returns an empty list
        List is made of (capName, capCondition, capVersion) tuples: 
          capName is name of capability
          capCondition is the '=', '<=' string, or None if no condition was specified
          capVersion is the required version, or None if no condition was specified
        """
        self._log("do-list-requires-called").info("doListRequires(%s) called", package)
        (rc, outText, errText)=self._runRpm("-q --requires "+package)
        if (rc==1) and (outText.find("is not installed") != -1):
            return []
        ret=self._parseCapabilities(outText)
        self._log("do-list-requires-returning").info("doListRequires(%s) returning '%s'", package, ret)
        return ret

    def doListRequiresFile (self, rpmFile):
        """
        Returns a list of capabilities that a package required. Package is an RPM file.
        List is in the same format as returned by doListRequires()
        """
        self._log("do-list-requires-file-called").info("doListRequiresFile(%s) called", rpmFile)
        (outText, errText)=self._runRpmRaiseIfFail("-qp --requires "+rpmFile)
        ret=self._parseCapabilities(outText)
        self._log("do-list-requires-file-returning").info("doListRequiresFile(%s) returning '%s'", rpmFile, ret)
        return ret

    def doListProvides (self, package):
        """
        Returns a list of capabilities that a package provides. Package should be installed.
        If package is not installed, returns an empty list
        List is in the same format as returned by doListRequires()
        """
        self._log("do-list-provides-called").info("doListProvides(%s) called", package)
        (rc, outText, errText)=self._runRpm("-q --provides "+package)
        if (rc==1) and (outText.find("is not installed") != -1):
            return []
        ret=self._parseCapabilities(outText)
        self._log("do-list-provides-returning").info("doListProvides(%s) returning '%s'", package, ret)
        return ret

    def doListProvidesFile (self, rpmFile):
        """
        Returns a list of capabilities that a package required. Package is an RPM file.
        List is in the same format as returned by doListRequires()
        """
        self._log("do-list-provides-file-called").info("doListProvidesFile(%s) called", rpmFile)
        (outText, errText)=self._runRpmRaiseIfFail("-qp --provides "+rpmFile)
        ret=self._parseCapabilities(outText)
        self._log("do-list-provides-file-returning").info("doListProvidesFile(%s) returning '%s'", rpmFile, ret)
        return ret

    def doGetInstalledPackages (self):
        """Returns a list of installed packages"""
        self._log("do-get-installed-packages-called").info("doGetInstalledPackages() called")
        (outText,errText)=self._runRpmRaiseIfFail("-qa")
        packages=outText.split()
        self._log("do-get-installed-packages-returning").info("doGetInstalledPackages() returning '%s'", packages)
        return sorted(packages)

    def _parseCapabilities(self, outText):
        lines=outText.strip().split('\n')
        ret=[]
        for line in lines:
            # Sometimes RPM files the DB locked, as a result of a killed -9 yum command, and as a result,
            # it prints such lines as part of the output. We ignre these lines
            if line.startswith("Freeing read locks"):
                continue
            tokens=line.strip().split()
            if len(tokens)==3:
                ret.append((tokens[0], tokens[1], tokens[2]))
            elif len(tokens)==1:
                ret.append((tokens[0], None, None))
            else:
                self._log("parse-capabilities-error").error("_parseCapabilities() got a line '%s', un-parsable", line)
                raise RuntimeError("_parseCapabilities() got a line '%s', un-parsable" % line)
        return ret

    def _raiseIfNotAbsPath (self, pathToCheck, name):
        if not pathToCheck.startswith('/'):
            raise ValueError("%s must start with '/', value given is '%s'" % (name, pathToCheck))

    def _runRpm (self, command):
        """
        Returns a tuple (rc, outText,errText)

        NOTE: This function is used by pilot services to allow pilot to run the rpm command
        """
        cmd=self.command+" "+command
        (rc,outText,errText)=self.utils.runCommand(cmd)
        return (rc,outText,errText)

    def _runRpmRaiseIfFail (self, command):
        """Returns a tuple (outText,errText)"""
        (rc,outText,errText)=self._runRpm(command)
        if rc != 0:
            raise RuntimeError("RPM command '%s' failed" % command)
        return (outText,errText)

    def _updateCommand (self):
        self.command="rpm"
        if self.useFakeChrootMode:
            self.command="fakeroot fakechroot /usr/sbin/chroot "+self.rootDir+" "+self.command
        elif (self.rootDir != None) and (self.rootDir != '/'): 
            self.command = self.command+" --root "+self.rootDir

