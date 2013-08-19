# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: effiz

import time
from a.infra.basic.exceptions import FunctionTimeOut
import a.infra.subprocess



# Class for measuring time left of total duration
# TODO: use uptime utility when available
# TODO: put this class outside since dell_controller is using the same
TIME_TO_KILL_AFTER_TERMINATE = 20
MINIMAL_TERMINATE_TIME = 5

class Timer(object):
    def __init__ (self,duration):
        self._startTime = time.time()
        self._duration = duration

    def getTimeLeft (self):
        delta = (time.time() - self._startTime)
        timeLeft = max((self._duration - delta),0.0)
        return timeLeft
    
    def __str__ (self):
        return "%.2f"%self.getTimeLeft()


def lunchCommand (logger,cmdString,timer):
    
    # check timeout is valid or raise exception
    terminateTimeOut = timer.getTimeLeft()
    if (terminateTimeOut <= MINIMAL_TERMINATE_TIME):
        logger("timeout-before-running").error("running command '%s' failed before running on timeout=%.2f<%.2f=MINIMAL_TERMINATE_TIME",cmdString,terminateTimeOut,MINIMAL_TERMINATE_TIME)
        raise FunctionTimeOut("_runCommand(cmdString=%s,terminateTimeOut=%.2f)"%(cmdString,terminateTimeOut),terminateTimeOut)

    # instantiate a process to excute the command
    proc = a.infra.subprocess.Subprocess("fs-cmd",logger)

    # start the process
    proc.start(cmdString,stdout=a.infra.subprocess.PIPE,stderr=a.infra.subprocess.PIPE,shell=True,setpgrp=True)
    logger("run-command").debug2("running command '%s'",cmdString)

    return proc


def waitForCommandEnd (logger,proc,timer):

    # communicate (i.e. wait for command end or timeout)
    terminateTimeOut = timer.getTimeLeft()
    killTimeOut = terminateTimeOut + TIME_TO_KILL_AFTER_TERMINATE
    stdout,stderr = proc.communicate(terminateTimeOut=terminateTimeOut,killTimeOut=killTimeOut)

    rc = proc.getReturnCode()
    cmdString = proc.getCommandLine()
    if (rc >= 0):
        # execution ended normally (with success or failure) - parse output
        if (rc==0):
            logger("command-successful").debug3("the command '%s' ended successfully, stdout=%s",cmdString,stdout)
        else:
            logger("command-unsuccessful").debug2("the command '%s' ended but was unsuccessful, stdout=%s, stderr=%s",cmdString,stdout,stderr)
        return stdout,stderr,rc
    else:
        # command failed (signal sent) - log and rais exception
        logger("command-failed-on-signal").error("the command '%s' failed (signal %d sent)",cmdString,rc)
        raise a.infra.subprocess.SubprocessDeathBySignal(proc)


def runCommand (logger,cmdString,timer):
    """
    Run a shell command. 
    Command is represented as string and will be run with shell=True.
    """
    proc = lunchCommand(logger,cmdString,timer)
    return waitForCommandEnd(logger,proc,timer)
