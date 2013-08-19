# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: nirs (and some effiz on communicate and process group)

import subprocess
import threading
import signal
import os
import time
import datetime
from a.infra.basic.exceptions import TimeOutException


class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        msg  -- explanation of the error
    """

    def __init__(self, msg):
        self.msg = msg

class SubprocessTimeOut(TimeOutException):
    """Exception for when subprocess exceeds a timeout."""
    def __init__ (self,popen,timeOut):
        self.popen = popen
        self.timeOut = timeOut
        TimeOutException.__init__(self,popen.getCommandLine(),timeOut)

class SubprocessDeathBySignal(Exception):
    """Exception to be thrown when a process dies as a result of a signal."""
    def __init__ (self,popen):
        self.popen = popen
        self.msg = "process was terminated by signal (rc=%s)"%popen.getReturnCode()

    def __str__ (self):
        return self.msg


GROUP_NAME = "subprocess"
PIPE = subprocess.PIPE
STDOUT = subprocess.STDOUT

class Subprocess:
    STOP_SLEEP_TIME = 0.1

    def __init__ (self, instanceName, logger):
        self._log = logger.createLoggerSameModule(GROUP_NAME, instance=instanceName)
        self._instanceName = instanceName
        self._popen = None
        self._terminationSignal = signal.SIGTERM
        self._isStarted = False
        self._cmdLine = None
        self._setpgrp = False
        self._wasWarningTimeout = False
        self._wasTerminatingTimeout = False
        self._wasKillingTimeout = False

    def start (self, args, bufsize=0, executable=None, stdin=None, stdout=None, stdoutFileName = None, stderr=None, stderrFileName = None, 
               close_fds=False, shell=False, cwd=None, env=None, umask=0, setpgrp=False):
        """Starts the process
     
        Args:
            args - see subprocess.Popen for additional information
            bufsize - see subprocess.Popen for additional information
            executable - see subprocess.Popen for additional information
            stdin - see subprocess.Popen for additional information
            stdout - see subprocess.Popen for additional information
            stdoutFileName - A standandard output file name. If set, stdout field will be using a file name opened by this module
            stderr - see subprocess.Popen for additional information
            stderrFileName - A error output file name. If set, stderr field will be using a file name opened by this module
            close_fds - see subprocess.Popen for additional information
            shell - see subprocess.Popen for additional information
            cwd - see subprocess.Popen for additional information
            env - see subprocess.Popen for additional information
            umask - umask to set on the new process. set to None if nothing shall be done
            setpgrp -if set to 'True' will run os.setpgrp() in the preExecutionFunction(), this useful when running with shell=True and killing the shell's child is needed.

        Future args:
            stdinFileName
            rootDirectory - for chroot
            uid
            gid
            affinity
            rlimits - a dictionary of fields to couples, to be used in the syntax of resource.setrlimit(resource.RLIMIT_CORE,(maxCoreDump,resource.RLIM_INFINITY)
        
        Skipped args:
            The below args exist in subprocess.Popen but will not be implemented in this class
            stdin - replaced by "stdinFileName"
            stdout -replaced by "stdoutFileName"
            stderr -replaced by "stderrFileName" 
            preexec_fn - currently in use by this module, our inner "preExecutionFunction" can call such a function but we need to decide when
     
        Returns:
            None
     
        Raises:
            See "exceptions" documentation in "subrocess" documentation
            In addition
            OSError: for failure in opening stderr/stdout files
            OSError: for failure in umask
        """
        self._log("launch-params").debug1("starting a process with parameters: args='%s', bufsize=%d, executable='%s', "
                                          "stdin='%s', stdout='%s', stdoutFileName='%s', stderr='%s',stderrFileName='%s', close_fds='%s', shell='%s', cwd='%s', env='%s', umask='%d',setpgrp='%s'", 
                                          str(args), bufsize, executable, stdin, stdout, stdoutFileName, stderr, stderrFileName, close_fds, shell, cwd, env, umask, setpgrp)
        def preExecutionFunction ():
             # We probably don't want the file mode creation mask inherited from the parent, so we give the child complete control over permissions.
            if umask is not None:
                os.umask(umask)
            if setpgrp:
                os.setpgrp()
            #if uid is not None:
            #    os.seteuid(uid)
            #if gid is not None:
            #    os.setegid(gid)
            #if rootDirectory is not None:
            #    os.chroot(rootDirectory)#TODO(nirs) need to check interaction with cwd
            #if affinity is not None:
            #    affinityCmd = "taskset --cpu-list --pid "+str(affinity)+" "+str(os.getpid())#TODO(nirs) check that os.getpid() takes the correct affinity
            #    rc=subprocess.call(affinityCmd)
            #    if rc!=0: raise something and document
            #    verifyAffinityCmd="taskset --cpu-list --pid "+str(os.getpid())
            #    stdout_handle = subprocess.Popen(verifyAffinityCmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=calcExecutionEnvVars()).stdout
            #    tasksetData = stdout_handle.read()
            #    found = tasksetData.find(str(affinity))
            #    if found<0: raise something and document
            #for field in rlimits:
            #    resource.setrlimit(field,rlimits[field])
           
        self._setpgrp = setpgrp

        needToCloseStdoutFile = False
        if stdoutFileName is not None:
            self._log("stdout-file").debug3("opeing file '%s' for stdout", stdout)
            stdout = os.open(stdoutFileName, os.O_WRONLY | os.O_APPEND | os.O_CREAT)
            needToCloseStdoutFile = True

        needToCloseStderrFile = False
        if stderrFileName is not None:
            self._log("stderr-file").debug3("opeing file '%s' for stderr", stderr)
            stderr = os.open(stderrFileName, os.O_WRONLY | os.O_APPEND | os.O_CREAT)
            needToCloseStderrFile = True

        self._popen = subprocess.Popen(args, bufsize=bufsize, executable=executable, preexec_fn = preExecutionFunction,
                                       stdin = stdin, stdout = stdout, stderr = stderr, close_fds=close_fds,  
                                       shell=shell, cwd=cwd, env=env)
        self._isStarted = True
        if needToCloseStdoutFile:
            os.close(stdout)
        if needToCloseStderrFile:
            os.close(stderr)

        self.stdout = self._popen.stdout
        self.stderr = self._popen.stderr

        if isinstance(args,str):
            self._cmdLine = args
        else:
            self._cmdLine = " ".join(map(str,args))
        self._log("launch").debug2("launched process '%s'", self._instanceName)
        self._log("launch-details").debug3("launched process %s using the command: '%s'. PID=%d", self._instanceName, self.getCommandLine(), self.getPid())
        

    #def attach (self, pid):
    #    """
    #    monitor an already existing process (instead of starting one on our own)
    #    """
    #    TODO(nirs)

    def communicate (self, input=None, terminateTimeOut=0, warningTimeOut=None, killTimeOut=None):
        """
        Interact with process: Send data to stdin. Read data from stdout and stderr, until end-of-file is reached. 
        Wait for process to terminate or one of the termination time-outs are exceeded.

        args:
        input            - A string to be sent to the process, or None, if no data should be sent.
        terminateTimeOut - when non-zero (float), the time after which termination (SIGTERM) of the process will be attempted.
        warningTimeOut   - when non-zero (float), the time for a warning log to be issued.
                           when None, a default of 0.5*terminateTimeOut will be used.
        killTimeOut      - when non-zero (float), the time after which killing of the process will be done.
                           when None, a default of 1.2*terminateTimeOut will be used.

        returns:
        stdout - the process's output  string, or None if termination/killing took place
        stderr - the process's error string, or None if termination/killing took place

        * Note that if you want to send data to the process's stdin, you need to start() it with stdin=PIPE. 
          Similarly, to get anything other than None in the result tuple, you need to give stdout=PIPE and/or stderr=PIPE in start() too.

        """
        
        # check inputs and use defaults if needed.
        # warning timeout handling
        if (warningTimeOut != 0):
            if (warningTimeOut != None): # real time out given
                if (warningTimeOut >= terminateTimeOut > 0):
                    raise InputError("warningTimeOut >= terminateTimeOut")
                else:
                    pass
            else: # warningTimeOut == None --> use defaults
                if (terminateTimeOut > 0):
                    warningTimeOut = 0.5*terminateTimeOut
                else:
                    warningTimeOut = 0

        # kill timeout handling
        if (killTimeOut != 0):
            if (killTimeOut != None): # real time out given
                if (killTimeOut <= terminateTimeOut):
                    raise InputError("killTimeOut <= terminateTimeOut")
                else:
                    pass
            else: # killTimeOut == None --> use defaults
                if (terminateTimeOut > 0):
                    killTimeOut = 1.2*terminateTimeOut
                else:
                    killTimeOut = 0

        # define target function to be run by Thread object
        def communicateTargetFunc (startedPopen,stdIn,stdOutErrTuple):
            stdOutErrTuple[:] = startedPopen.communicate(stdIn)

        stdOutErr = [None,None]
        communicateThread = threading.Thread(target=communicateTargetFunc,args=(self._popen,input,stdOutErr))
        communicateThread.daemon = False # make sure this little helper thread is no a daemon
        communicateThread.start()

        tillTermDuration = terminateTimeOut
        tillKillDuration = killTimeOut

        if (warningTimeOut > 0):
            communicateThread.join(warningTimeOut)
            if communicateThread.is_alive():
                self._log("communicate-warning-time-out-exceeded").warning("communicate() for process %s (PID=%d, command=%s) is blocking for %.2f seconds",self._instanceName,self.getPid(),self.getCommandLine(),warningTimeOut)
                self._wasWarningTimeout = True        
                tillTermDuration -= warningTimeOut
                tillKillDuration -= warningTimeOut

        if (tillTermDuration > 0):
            communicateThread.join(tillTermDuration)
            if communicateThread.is_alive():
                self._log("communicate-terminate-time-out-exceeded").error("communicate() for process %s (PID=%d, command=%s) is blocking for %.2f seconds - terminating!",self._instanceName,self.getPid(),self.getCommandLine(),terminateTimeOut)
                self._wasTerminatingTimeout = True        
                self.terminate()
                tillKillDuration -= tillTermDuration

        if (tillKillDuration > 0):
            communicateThread.join(tillKillDuration)
            if communicateThread.is_alive():
                self._log("communicate-kill-time-out-exceeded").error("communicate() for process %s (PID=%d, command=%s) is blocking for %.2f seconds - killing brutally!",self._instanceName,self.getPid(),self.getCommandLine(),killTimeOut)
                self._wasKillingTimeout = True
                self.kill()

        communicateThread.join()
        self._log("communicate-ended").debug2("process %s (PID=%d, command=%s), ended after %.2f seconds in communicate.",self._instanceName,self.getPid(),self.getCommandLine(),0) #TODO: fix the total duration when you have uptime utility

        return stdOutErr
            
    def getPid (self):
        """getthe process pid"""
        return self._popen.pid

    def waitPid (self):
        """Wait for child process to terminate"""
        self._log("wait").debug1("waiting for process '%s' with pid %d", self._instanceName, self.getPid())
        self._popen.wait()

    def sendSignal (self, signal):
        """Sends the signal signal to the child (or group)."""
        self._log("send-signal").debug1("sending signal %d to process '%s'", signal, self._instanceName)
        if self._setpgrp:
            os.killpg(self.getPid(),signal)
        else:
            self._popen.send_signal(signal)

    def setTerminationSignal (self, signal):
        """set the termination signal used by the 'terminate' function"""
        self._log("set-terminate-signal").debug1("setting the termination signal of process '%s' to %d", self._instanceName, signal)
        self._terminationSignal = signal
 
    def stop (self, timeout, terminationSignal = None):
        """stop the process
        call the terminte function and when the timeout is reached call the "kill" function
        args:
            timeout: timeout in seconds
        """
        maxDelta = None
        if not timeout is None:
            maxDelta = datetime.timedelta(0, timeout)
        startTime = datetime.datetime.now()
        #sending a sigterm
        self.terminate(terminationSignal)
        while self.isUp():
            endTime = datetime.datetime.now()
            delta = endTime-startTime
            if (not maxDelta is None) and maxDelta <= delta:
                self._log("stop-timeout").warning("reached stop procedure timeout for process '%s'. killing the process",self._instanceName)
                self.kill()                
                break
            time.sleep(self.STOP_SLEEP_TIME)
        
    def terminate (self, terminationSignal = None):
        """Stop the child using SIGTERM (or other signal set by "setTerminationSignal" """        
        if terminationSignal is None:
            terminationSignal = self._terminationSignal
        self._log("terminate").notice("terminatting process '%s' using signal %d", self._instanceName, self._terminationSignal)
        try:
            self.sendSignal(terminationSignal)
        except OSError, err:
            if self.isUp():
                self._log("terminate-failed").error("failed terminating process '%s' with pid %s (%s)", self._instanceName, self.getPid(), err.strerror)
            else:
                self._log("terminate-failed-but-dead").debug1("failed terminating process '%s' with pid %s (%s) - but the process is down", self._instanceName, self.getPid(), err.strerror)

    def kill (self):
        """ Kills the child - sends SIGKILL """
        self._log("kill").notice("killing process '%s'",self.getPid())
        try:
            self.sendSignal(signal.SIGKILL)
        except OSError, err:
            if self.isUp():
                self._log("kill-failed").error("failed killing process '%s' with pid %s (%s)", self._instanceName, self.getPid(), err.strerror)
            else:
                self._log("kill-failed-but-dead").debug1("failed killing process '%s' with pid %s (%s) - but the process is down", self._instanceName, self.getPid(), err.strerror)

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

    def getCommandLine (self):
        """The child's command line in readable format."""
        return self._cmdLine

        
    def hasTimeoutWarning (self):
        """ Returns: True, when the warning timeout was exceeded """
        return self._wasWarningTimeout

    def hasTimeoutTerminating (self):
        """ Returns: True, when the terminating timeout was exceeded """
        return self._wasTerminatingTimeout

    def hasTimeoutKilling (self):
        """ Returns: True, when the killing timeout was exceeded """
        return self._wasKillingTimeout

