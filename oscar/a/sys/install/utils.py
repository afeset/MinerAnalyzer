# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

import os
import statvfs
import subprocess

class Utils(object):

    def __init__ (self, logger):
        self._log=logger.createLogger("sys-install","utils")

    def runCommand (self, cmd, shell=False):
        """
        cmd: Either a string with the command (when shell=True), or an array with tokens (when shell=False.

        Returns a tuple (rc, outText,errText)
        """

        if not shell:
            cmd=cmd.split()
        self._log("run-command").info("Running command '%s'", cmd)
        pid=subprocess.Popen(cmd, shell=shell, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (outText,errText)=pid.communicate()
        rc=pid.wait()
        if outText:
            self._log("run-command-out").info("Command stdout is:\n%s", outText)
        if errText:
            self._log("run-command-err").info("Command stderr is:\n%s", errText)
        self._log("run-command-rc").info("Command returned '%s'", rc)
        return (rc,outText,errText)

    def runCommandRaiseIfFail (self, command, shell=False):
        """Returns a tuple (outText,errText)"""
        (rc,outText,errText)=self.runCommand(command, shell=shell)
        if rc != 0:
            self._log("run-command-raising").warning("Command returned '%s', raising exception", rc)
            raise RuntimeError("")
        return (outText,errText)

    def getAvailableSize (self, path_):
        self._log("get-avail-size").info("getAvailableSize() called, path_=%s", path_)
        f = os.statvfs(path_)
        self._log("get-avail-size").info("getAvailableSize(): os.statvfs() returned %s", f)
        availBytes = f[statvfs.F_BAVAIL] * f[statvfs.F_BSIZE]
        self._log("get-avail-size").info("getAvailableSize(): Path %s has %s available bytes", path_, availBytes)
        return availBytes


