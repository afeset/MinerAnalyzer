# 
# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: nirs

import subprocess
import threading
import signal
import os

KRUSTY_SUBPROCESS_GROUP_NAME = "subprocess"

class Subprocess:
    def __init__ (self, instanceName, logger):
        self._log = logger.createLoggerSameModule(KRUSTY_SUBPROCESS_GROUP_NAME, instance=instanceName)
        self._instanceName = instanceName
        self._popen = None
        self._isStarted = False

    def start (self, args, executable=None, stdin=None, dont_close_fds=False, shell=False, cwd=None, env=None, umask=0):
        self._log("launch-params").debug1("starting a process with parameters: args='%s', executable='%s', "
                                          "stdin='%s', dont_close_fds='%s', shell='%s', cwd='%s', env='%s', umask='%d'", 
                                          str(args), executable, stdin, dont_close_fds, shell, cwd, env, umask)
        def preExecutionFunction ():
             # We probably don't want the file mode creation mask inherited from the parent, so we give the child complete control over permissions.
            if umask is not None:
                os.umask(umask)

        self._popen=subprocess.Popen(args, executable=executable, preexec_fn = preExecutionFunction,
                                     stdout = subprocess.PIPE, stderr = subprocess.PIPE, close_fds=not dont_close_fds,  
                                     shell=shell, cwd=cwd, env=env)
        self._isStarted = True

        if isinstance(args,str):
            cmdLine = args
        else:
            cmdLine = " ".join(map(str,args))
        self._log("launch-details").debug1("launched using the command: '%s'. Pid=%s", cmdLine, self.getPid())
        

    def communicate (self, input=None, killTimeout=None):
        timer = None
        if killTimeout is not None:
            def kill ():
                self._log("kill-timeout").error("Killing process due to timeout. Pid=%s", self.getPid())
                self.kill()
            timer = threading.Timer(killTimeout, kill)
            timer.start()
            
        (outData, errData) = self._popen.communicate(input)
        if timer is not None:
            timer.cancel()
        self._log("process-returned").debug1("Pid %s returned: rc=%s", self.getPid(), self.getReturnCode())
        self._log("process-stdout").debug1("Pid %s returned: stdout=%s", self.getPid(), outData)
        self._log("process-stderr").debug1("Pid %s returned: stderr=%s", self.getPid(), errData)
        return (outData, errData)

    def getPid (self):
        """getthe process pid"""
        return self._popen.pid

    def sendSignal (self, signal):
        """Sends the signal signal to the child (or group)."""
        self._log("send-signal").debug1("sending signal %d to pid %s", signal, self.getPid())
        self._popen.send_signal(signal)

 
    def kill (self):
        """ Kills the child - sends SIGKILL """
        self._log("kill").notice("killing pid '%s'",self.getPid())
        try:
            self.sendSignal(signal.SIGKILL)
        except OSError, err:
            if self.isUp():
                self._log("kill-failed").error("failed killing pid %s (%s)", self.getPid(), err.strerror)
            else:
                self._log("kill-failed-but-dead").debug1("failed killing pid %s (%s) - but the process is down", self.getPid(), err.strerror)
    


    def isUp (self):
        """Check if child process has terminated"""
        if not self._isStarted:
            return False
        return self._popen.poll()==None

    def getReturnCode (self):
        """The child return code. A None value indicates that the process hasn't terminated yet.
        A negative value -N indicates that the child was terminated by signal N (Unix only).
        """
        return self._popen.returncode

 
