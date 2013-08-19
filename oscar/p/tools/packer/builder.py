# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

import json
import os
import random
import subprocess
import time

class CommandRunner(object):
    def _runCommand (self, command):
        self._log.info("Executing: %s" % command)
        pid=subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (outText,errText)=pid.communicate()
        rc=pid.wait()
        if outText:
            self._log.info("Command stdout is:\n%s", outText)
        if errText:
            self._log.info("Command stderr is:\n%s", errText)
        self._log.info("Command returned '%s'", rc)
        return rc

    def _runCommandRaiseIfFail (self, command):
        rc=self._runCommand(command)
        if rc != 0:
            self._log.error("Command failed, rc=%s" % rc)
            raise RuntimeError("Command '"+command+"' failed, rc="+str(rc))


class RpmBuilder(CommandRunner):
    """A class that builds RPMs"""

    def __init__ (self, logger, name, version_, build):
        """
        logger: A standard python logger
        name: Name of package to create
        version_: Version of pacakge to create
        build: Build of package to create (In RPM terminology, build = release number)
        """
        self._log=logger
        self.name = name
        self.version_ = version_
        self.build_ = build

    def build (self, fromDir, tempDir, key, user="root", group="root", prefix=None, description=None, summary=None, 
               provides=None, requires=None, allowSideBySide=True, prefixOwnedByPackage=False,
               postInstallCmds=None, preRemoveCmds=None, verifyScriptCmds=None):
        """
        fromDir: Directory from which we gather the RPM files. Use None to create an RPM with no files
        tempDir: A temp directory in which we can work. RPM file is generated inside this dir. Directory
                 Must be empty or non-existing
        key: Name of key to sign rpm with. In None, rpm is not signed
        user: user name owning all files in the RPM
        group: group name owning of all files in the RPM
        prefix: Directory in target. All rpm files are extracted relative to this dir. Default is '/'
        description: A textual description of the package
        summary: A short description of the package
        provides: A string with a space-separates list of capabilities this RPM provides
        requires: A string with a space-separates list of capabilities this RPM requires
        allowSideBySide: True in order to allow multiple versions/builds of this package to reside in the same box.
        prefixOwnedByPackage: True if package totally owns the dir specified by prefix. If True, package removal causes
           removal of the 'prefix' dir.

        Returns the name of the generated rpmFile. File is inside tempDir. tempDir should be removed after rpm file is used.
        """

        if (fromDir != None) and (not fromDir.startswith(os.path.sep)):
            raise ValueError("fromDir must be an absolute path")
        if not tempDir.startswith(os.path.sep):
            raise ValueError("tempDir must be an absolute path")

        removeMacrosFile=False

        if prefix is None:
            prefix="/"
            if prefixOwnedByPackage:
                raise ValueError("Argument 'prefix' not specified, but argument 'prefixOwnedByPackage' set to True. "\
                                 "I refuse to create a package that implicitly declares that it owns '/'")

        specFileName=tempDir+"/x.spec"
        tempDirRpm=tempDir+"/rpm"
        specParams={'name' : self.name, 'version' : self.version_, 'build' : self.build_, 
                    'tempDirRpm' : tempDirRpm, 'prefix' : prefix, 
                    'user' : user, 'group' : group, 'requires' : "", 'provides' : ""}
        if provides==None:
            provides=""
        if allowSideBySide:
            provides=provides+" qb-allow-side-by-side"
        if provides != "":
            specParams['provides']="Provides: "+provides
    
        if requires!=None:
            specParams['requires']="Requires: "+requires
    
        if description==None:
            description=""
        specParams['description']=description
    
        if summary==None:
            summary=""
        specParams['summary']=summary
    
        specText2=""
        specText4=""
    
        if fromDir != None:
            # Each file/dir is copied (-r) to the target area
            for file_ in os.listdir(fromDir):
                specParams['file']=file_
                specParams['absFile']=os.path.join(fromDir, file_)
                specText2+=self.specTemplate2 % specParams
        
            # For each file and dir we have a line in the %files section
            for root, dirs, files in os.walk(fromDir):
                for file_ in files + dirs:
                    specParams['file']=os.path.join(root, file_).replace(fromDir,"")
                    specParams['absFile']=os.path.join(root, file_)
                    specText4+=self.specTemplate4 % specParams

            # Special treatment for the top-level dir itself
            if prefixOwnedByPackage:
                specParams['file']=""
                specText4+=self.specTemplate4 % specParams
    
        specText=self.specTemplate1 % specParams
        specText+=specText2
        specText+=self.specTemplate3 % specParams
        specText+=specText4
        
        if postInstallCmds:
            specText+="%post\n"
            for line in postInstallCmds:
                specText+=line+"\n"

        if preRemoveCmds:
            specText+="%preun\n"
            for line in preRemoveCmds:
                specText+=line+"\n"

        if verifyScriptCmds:
            specText+="%verifyscript\n"
            for line in verifyScriptCmds:
                specText+=line+"\n"

        self._prepareTempDir(tempDir, tempDirRpm, specFileName, specText)
        self._runCommandRaiseIfFail("rm -rf "+tempDir)
        self._runCommandRaiseIfFail("mkdir -p "+tempDirRpm+"/{BUILD,RPMS,SOURCES,SPECS,SRPMS}")
        f=open(specFileName, "w")
        f.write(specText)
        f.close()
    
        # Todo: protect against multiple invocations: using a soft-link to a temp file and checking that it did not change.
        # retry if soft-link changed or got exception during creation
        homeDir=os.environ["HOME"]
        macrosPath=os.path.join(homeDir, ".rpmmacros")
        macrosTmpFile=".rpmmacros-"+str(random.randint(0, 999999999))
        macrosTmpPath=os.path.join(homeDir, macrosTmpFile)

        # If a link exists, wait up to 120 seconds before concluding that someone got stuck and replacing it with our link
        self._log.info("Setting up link %s -> %s" % (macrosPath, macrosTmpFile))
        if os.path.lexists(macrosPath):
            retries=120
            self._log.notice("%s exists, waiting up to %s seconds for removal..." % (macrosPath, retries))
            while retries>0:
                time.sleep(1)
                retries -= 1
                if not os.path.lexists(macrosPath):
                    self._log.notice("%s got deleted by someone else, proceeding :-)" % macrosPath)
                    retries = -3
                    break

            if retries != -3:
                self._log.info("%s still exists, removing it and proceeding" % macrosPath)


        buildRetries=10
        while buildRetries>0:

            def waitRandom ():
                r=random.randint(1, 120)
                self._log.notice("Waiting %s seconds and retrying" % r)
                time.sleep(r)

            # We put everything in a try block, to handle exceptions due to multiple scripts running
            try:
                if os.path.lexists(macrosPath):
                    os.remove(macrosPath)
                os.symlink(macrosTmpFile, macrosPath)

                # Do the actual work
                f=open(macrosTmpPath, "w")
                f.write("%_topdir "+tempDirRpm+"\n")
                f.close()
                self._runCommandRaiseIfFail("rpmbuild --quiet --root "+tempDirRpm+" -bb "+specFileName)

                l=os.readlink(macrosPath)
                if l != macrosTmpFile:
                    self._log.info("Someone messed with our link, re-trying...")
                    raise RunTimeException("Someone messed with our link")
                else:
                    buildRetries=0   # Exit the while loop

            except KeyboardInterrupt:
                raise
            except:
                self._log.notice("Got exception during building, %s attempts left" % buildRetries)
                self._prepareTempDir(tempDir, tempDirRpm, specFileName, specText)
                buildRetries -= 1
                if buildRetries <= 0:
                    self._log.error("No more attempts left, exiting with failure")
                    raise Excaption("No more attempts left, exiting with failure")
                waitRandom()

        self._log.info("Done building RPM, removing macro files")
        os.remove(macrosTmpPath)
        if os.path.lexists(macrosPath):
            os.remove(macrosPath)

        rpmFileName=self.name+"-"+self.version_+"-"+self.build_+".x86_64.rpm"
        createdRpmFile=os.path.join(tempDirRpm,"RPMS/x86_64",rpmFileName)
        if key != None:
            self._log.info("Signing RPM with key '%s'" % key)
            self._runCommandRaiseIfFail("q-dev-keymaster --sign-rpm %s --key %s" % (createdRpmFile, key))

        self._log.info("RPM file '%s' succesfully signed with key '%s'" % (createdRpmFile, key))

        return createdRpmFile

    def _prepareTempDir(self, tempDir, tempDirRpm, specFileName, specText):
        self._runCommandRaiseIfFail("rm -rf "+tempDir)
        self._runCommandRaiseIfFail("mkdir -p "+tempDirRpm+"/{BUILD,RPMS,SOURCES,SPECS,SRPMS}")
        f=open(specFileName, "w")
        f.write(specText)
        f.close()

    specTemplate1="""
Name: %(name)s

Prefix: /

Version: %(version)s
Release: %(build)s

BuildRoot: /buildroot

Summary: %(summary)s

Vendor: Qwilt Inc.

License: Proprietary

Group: network

%(provides)s
%(requires)s

AutoReq: 0 
AutoProv: 0 
AutoReqProv: 0 

%%description
%(description)s

%%build
echo env var: RPM_BUILD_ROOT=$RPM_BUILD_ROOT

%%install
mkdir -p %(tempDirRpm)s/$RPM_BUILD_ROOT/%(prefix)s
"""

    specTemplate2="""
cp -r %(absFile)s %(tempDirRpm)s/$RPM_BUILD_ROOT/%(prefix)s
"""

    specTemplate3="""
%%clean
rm -rf $RPM_BUILD_ROOT

%%files
%%defattr(-,%(user)s,%(group)s)
"""

    specTemplate4="""
/%(prefix)s/%(file)s
"""

class R2pmBuilder(CommandRunner):
    """A class that builds r2pm files, which are Qwilt package files"""

    def __init__ (self, logger, name, version_, build):
        """
        logger: A standard python logger
        name: Name of package to create
        version_: Version of pacakge to create
        build: Build of package to create (In RPM terminology, build = release number)
        """
        self._log=logger
        self.name = name
        self.version_ = version_
        self.build_ = build

    def createR2pm (self, tempDir, subPkgs, key=None, description=None, summary=None):
        """
        tempDir: A temp directory in which we can work. R2PM file is generated inside this dir. Directory
                 Must be empty or non-existing
        subPkgs: An array of dictionaries. Each dist describes a sub-package. Dict keys: 
            name: sub-pkg name. 
            dir: Path below which which all files are to be installed
            type: sub-package type. Currently two types are supported: 'repository' and 'data. 
                  For type 'repository', dict must contain the key 'rpms'.
                  For type 'data', dict must contain the key 'from-dir'.
            rpms: Used for sub-packages of type 'repository'. Holds list of absolute paths to rpm files to put in the repository.
            from-dir: Used for sub-packages of type 'data'. Contains abs path on disk from which to take this sub-pkg. 
        key: Name of key to sign r2pm with. In None, r2pm is not signed
        description: A textual description of the package
        summary: A short description of the package

        Returns: Name of resulting RPM. File is inside tempDir. tempDir should be removed after rpm file is used.
        """

        if not tempDir.startswith(os.path.sep):
            raise ValueError("tempDir must be an absolute path")

        self._runCommandRaiseIfFail("rm -rf "+tempDir)
        os.makedirs(tempDir)

        rpmBuildDir=os.path.join(tempDir, "build-rpm")
        os.mkdir(rpmBuildDir)
        filesDir=os.path.join(tempDir, "r2pm-files")
        os.mkdir(filesDir)
        infoDir=os.path.join(filesDir, "info")
        os.mkdir(infoDir)

        for subPkg in subPkgs:
            subPkgName=subPkg['name']
            subPkgDir=subPkg['dir']
            subPkgType=subPkg['type']
            subPkgDirFullPath=os.path.join(filesDir, subPkgDir)
            if subPkgType=='repository':
                os.makedirs(subPkgDirFullPath)
                rpms=subPkg['rpms']
                for rpm in rpms:
                    self._runCommandRaiseIfFail("cp "+rpm+" "+subPkgDirFullPath)
                self._runCommandRaiseIfFail("createrepo "+subPkgDirFullPath)
            elif subPkgType=='data':
                fromDir=subPkg['from-dir']
                self._runCommandRaiseIfFail("mkdir -p "+os.path.dirname(subPkgDirFullPath))
                self._runCommandRaiseIfFail("cp -rp "+fromDir+" "+subPkgDirFullPath)
            else:
                raise ValueError("Sub-pkg '%s' has unsupported type '%s'" % (subPkgName, subPkgType))


            info={}
            info['name']=subPkgName
            info['dir']=subPkgDir
            info['type']=subPkgType
            infoText=json.dumps(info, sort_keys=True, indent=4)
            infoFile=open(os.path.join(infoDir, subPkgName+".info"),"w")
            infoFile.write(infoText)
            infoFile.close()

        b=RpmBuilder(self._log, name=self.name, version_=self.version_, build=self.build_)
        rpmFile=b.build(fromDir=filesDir, tempDir=rpmBuildDir, 
                        key=key, description=description, summary=summary)
        return rpmFile


