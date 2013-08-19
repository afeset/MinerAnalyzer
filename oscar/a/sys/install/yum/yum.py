# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

import os
import re
import subprocess

from a.sys.install.utils import Utils

class Yum(object):

    configTemplate="""
[main]
cachedir=/var/cache/yum
# We do not want to waste space: cache should be clear after installation
keepcache=0
debuglevel=2
logfile=/var/log/yum.log
exactarch=1
obsoletes=1
plugins=1
pluginpath=%(pluginpath)s
pluginconfpath=%(pluginpath)s
#rpmverbosity=debug

# List of 'provides' of packages that are allowed to be installed multiple versions side by side
installonlypkgs=qb-allow-side-by-side 
# install-only packages are allowed until the sun burns down
installonly_limit=999

gpgcheck=1
localpkg_gpgcheck=1
"""

    configRepoTemplate="""
[%(repoName)s]
name=%(repoName)s
baseurl=%(baseurl)s
"""


    def __init__ (self, logger, tempDir):
        self._log=logger.createLogger("sys-install","yum-yum")
        self.utils=Utils(self._log)
        self.rootDir="/"
        self.useFakeChrootMode=False
        self.diskRepos=[]
        self.httpRepos=[]
        self.tempDir=tempDir
        # tempDir MUST begin with '/', see _getConfPath
        self._raiseIfNotAbsPath(tempDir, "tempDir")
        self.yumConfPath=os.path.join(self.tempDir, "yum.conf")
        self.yumConfPluginDir=os.path.join(self.tempDir, "yum.pluginconf.d")
        self._updateCommand()

    def setRoot (self, rootDir, useFakeChrootMode=False):
        self._raiseIfNotAbsPath(rootDir, "rootDir")
        self.rootDir=rootDir
        self.useFakeChrootMode=useFakeChrootMode
        self._updateCommand()

    def addDiskRepo (self, repoName, repoDir):
        self._raiseIfNotAbsPath(repoDir, "repoDir")
        self.diskRepos.append((repoName, repoDir))
        if self.useFakeChrootMode:
            self._testModeAddRpms(repoName, repoDir)

    def addHttpRepo (self, repoName, repoAddr):
        self.httpRepos.append((repoName, repoAddr))

    def doInstall (self, package):
        self._log("do-install-called").info("doInstall(%s) called", package)
        self._createYumConf()
        cmd="--assumeyes install "+package
        #Work around to the ANNOYING problem of yum refusing to install a leader because it requires an oscar which is older
        # than some installed oscar. Instead of raising if install fails, we check the output, and if it failed due to 
        # some 'newer' package which is already installed, we install that package first, and retry
        #self._runYumRaiseIfFail("--assumeyes install "+package)


        retry=True
        numLoops=0
        while retry:
            retry=False
            (rc,outText,errText)=self._runYum(cmd)
            if rc==0:
                return
            # This is a sample of the error message we get from yum:
            #package oscar-2.1.0.1-12386.x86_64 (which is newer than oscar-2.1.0.0-20120320133848.x86_64) is already installed
            mo=re.search("which is newer than (.*)\) is already installed", errText)
            if mo != None:
                rpmToInstall=mo.group(1)
                self._log("do-install-workaround").info("doInstall(%s) workaround: Found package %s that needs to be installed first", package, rpmToInstall)
                # We assume that this package must be installed properly, without tricks
                self._runYumRaiseIfFail("--assumeyes install "+rpmToInstall)
                numLoops += 1
                if numLoops < 10:
                    retry=True
            else:
                self._log("do-install-workaround").info("doInstall(%s) workaround: Did not find any package that needs to be installed first", package)
        raise RuntimeError("Yum install failed: returned %s" % rc)


    def doReinstall (self, package):
        self._log("do-reinstall-called").info("doReinstall(%s) called", package)
        self._createYumConf()
        self._runYumRaiseIfFail("--assumeyes reinstall "+package)

    def doUpdate (self, package):
        self._log("do-update-called").info("doUpdate(%s) called", package)
        self._createYumConf()
        self._runYumRaiseIfFail("--assumeyes update "+package)

    def doRemove (self, package):
        self._log("do-remove-called").info("doRemove(%s) called", package)
        self._createYumConf()
        self._runYumRaiseIfFail("--assumeyes remove "+package)

    def doUpgrade (self, package):
        self._log("do-upgrade-called").info("doUpgrade(%s) called", package)
        self._createYumConf()
        self._runYumRaiseIfFail("--assumeyes upgrade "+package)

    # localinstall is needed because 'yum install' with a file name works only if file anme ends with .rpm
    def doLocalInstall (self, package):
        self._log("do-local-install-called").info("doLocalInstall(%s) called", package)
        self._createYumConf()
        self._runYumRaiseIfFail("--assumeyes localinstall "+package)

    def doTestInstall (self, package):

        """Checks that an install would work. Returns True if OK, False if not"""

        self._log("do-local-install-called").info("doTestInstall(%s) called", package)
        self._createYumConf()
        (rc,outText,errText)=self._runYum("--assumeyes --downloadonly install "+package)
        # 0 means nothing to do. Message in output means exit due to plugin, not due to errors
        ret = ((rc==0) or (errText.find("exiting because --downloadonly specified") != -1))
        self._log("do-local-install-done").info("doTestInstall() returning %s", ret)
        return ret


    def createYumConfAt (self, yumConfDir):
        """
        Given a directory name, creates a yum.conf file in it (Plus plugins, as needed).
        Returns name of generated yum.conf file (To be passed to 'yum -c')
        """
        self._log("create-yum-conf-at-called").info("createYumConfAt() called, dir=%s", yumConfDir)

        pathToYumConf=os.path.join(yumConfDir, "yum.conf")
        if not os.path.exists(yumConfDir):
            os.makedirs(yumConfDir)

        pathToYumPluginConf = os.path.join(yumConfDir, "yum.pluginconf.d")
        if not os.path.exists(pathToYumPluginConf):
            os.makedirs(pathToYumPluginConf)

        confText=self._getConfText() % {'pluginpath' : pathToYumPluginConf}
        self._writeTextToFile(confText, pathToYumConf)
        self._log("create-yum-conf-at-text").info("createYumConfAt() called, conf text is '%s'", confText)

        self._createYumPlugins(pathToYumPluginConf)
        self._log("create-yum-conf-at-done").info("createYumConfAt() done")
        return pathToYumConf

    def _testModeAddRpms (self, repoName, repoDir):
        """For unit tests only, copies rpms to yum cache to avoid bug"""
        # This is needed to overcome a bug in fakechroot (apparently): If the rpm itself is not found in the cache,
        # Then yum checks for the space available on disk before 'downloading it', and it uses the statvfs() for that,
        # and apparently this function is not covered by fakechroot. See this strace output:
        # 
        # 10887 stat("/users/eng/orens/testRpm/rfs1/var/cache/yum/x86_64/centos6/box/packages/sugar-2.0-2.x86_64.rpm", 0x7fffa3a72260) = -1 ENOENT (No such file or directory)
        # 10887 statfs("/var/cache/yum/x86_64/centos6/box/packages", 0x7fffa3a722d0) = -1 ENOENT (No such file or directory)
        #
        # This is the result of code at /usr/lib/python2.6/site-packages/yum/__init__.py, line 1600.
        self._log("test-mode-add-rpms").info("_testModeAddRpms(repoName=%s, repoDir=%s) called, self.rootDir=%s", repoName, repoDir, self.rootDir)
        self._raiseIfNotAbsPath(repoDir, "repoDir")
        if not self.useFakeChrootMode:
            raise ValueError("Never call this func in production code")
        repoCachePackagesDirFromOutside=os.path.join(self.rootDir, "var/cache/yum/"+repoName+"/packages")
        self.utils.runCommandRaiseIfFail("mkdir -p "+repoCachePackagesDirFromOutside)
        if repoDir.startswith(self.rootDir):
            repoDir = repoDir.replace(self.rootDir, "")
        repoDirFromOutside=self.rootDir+repoDir
        for file_ in os.listdir(repoDirFromOutside):
            if file_.endswith(".rpm"):
                fileFromOutside=os.path.join(repoDirFromOutside, file_)
                self.utils.runCommandRaiseIfFail("cp "+fileFromOutside+" "+repoCachePackagesDirFromOutside)

    def _getConfPath (self):
        pathToYumConf=os.path.join(self.rootDir, self.yumConfPath[1:])  # Remove leading '/' from 
        return pathToYumConf

    def _getPluginConfPath (self):
        pathToYumPluginConf=os.path.join(self.rootDir, self.yumConfPluginDir[1:])  # Remove leading '/' from 
        return pathToYumPluginConf
        
    def _getConfText (self):
        text=self.configTemplate
        for (repoName, repoDir) in self.diskRepos:
            text += self.configRepoTemplate % {'repoName' : repoName, 'baseurl' : 'file://'+repoDir}
        for (repoName, repoAddr) in self.httpRepos:
            text += self.configRepoTemplate % {'repoName' : repoName, 'baseurl' : 'http://'+repoAddr}
        return text

    def _createYumPlugins (self, pluginConfDir):
        downloadonlyConfText="""
[main]
enabled=1
"""

        downloadonlyPyText="""
from yum.plugins import PluginYumExit, TYPE_INTERACTIVE

requires_api_version = '2.1'
plugin_type = (TYPE_INTERACTIVE,)

def config_hook(conduit):
    parser = conduit.getOptParser()
    if hasattr(parser, 'plugin_option_group'):
        parser = parser.plugin_option_group

    parser.add_option('', '--downloadonly', dest='dlonly', action='store_true',
           default=False, help="don't update, just download")
    parser.add_option('', '--downloaddir', dest='dldir',
                      action='store', default=None,
                      help="specifies an alternate directory to store packages")

def postreposetup_hook(conduit):
    opts, commands = conduit.getCmdLine()
    if opts.dldir:
        repos = conduit.getRepos()
        rlist = repos.listEnabled()
        for repo in rlist:
            repo.setAttribute('pkgdir',opts.dldir)


def postdownload_hook(conduit):
    opts, commands = conduit.getCmdLine()
    # Don't die on errors, or we'll never see them.
    if not conduit.getErrors() and opts.dlonly:
        raise PluginYumExit('exiting because --downloadonly specified ')
"""
        self._writeTextToFile(downloadonlyConfText, os.path.join(pluginConfDir, "downloadonly.conf"))
        self._writeTextToFile(downloadonlyPyText, os.path.join(pluginConfDir, "downloadonly.py"))


    def _createYumConf (self):
        pathToYumConf=self._getConfPath()
        self._log("create-yum-conf").info("_createYumConf() called, writing to %s", pathToYumConf)

        dir_=os.path.dirname(pathToYumConf)
        if not os.path.exists(dir_):
            os.makedirs(dir_)

        pathToYumPluginConf = self._getPluginConfPath()
        if not os.path.exists(pathToYumPluginConf):
            os.makedirs(pathToYumPluginConf)

        confText=self._getConfText() % {'pluginpath' : self.yumConfPluginDir}
        self._writeTextToFile(confText, pathToYumConf)
        self._log("create-yum-conf-text").info("_createYumConf() called, conf text is '%s'", confText)

        self._createYumPlugins(pathToYumPluginConf)
        self._log("create-yum-conf-done").info("_createYumConf() done")

    def _writeTextToFile (self, text, fileName):
        f=open(fileName, "w")
        f.write(text)
        f.close()

    def _removeYumConf (self):
        os.remove(self._getConfPath())
        self.utils.runCommandRaiseIfFail("rm -rf "+self._getPluginConfPath())

    def _raiseIfNotAbsPath (self, pathToCheck, name):
        if not pathToCheck.startswith('/'):
            raise ValueError("%s must start with '/', value given is '%s'" % (name, pathToCheck))

    def _runYum (self, cmd):
        """
        NOTE: This function is used by pilot services to allow pilot to run the yum command
        """
        cmd=self.command+" "+cmd
        (rc,outText,errText)=self.utils.runCommand(cmd)
        return (rc,outText,errText)

    def _runYumRaiseIfFail (self, cmd):
        (rc,outText,errText)=self._runYum(cmd)
        if rc != 0:
            raise RuntimeError("Yum command '%s' failed: returned %s" % (cmd, rc))
        return (outText,errText)

    def _updateCommand (self):
        self.command="yum -c "+self.yumConfPath
        if self.useFakeChrootMode:
            self.command="fakeroot fakechroot /usr/sbin/chroot "+self.rootDir+" "+self.command
        elif self.rootDir != "/":
            self.command = self.command+" --installroot "+self.rootDir

