# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: yoave

import subprocess
import shutil 
import os.path
import a.infra.subprocess 

class IpAction:
    """This class holds an enumeration of command actions"""

    ADD = "add"
    SHOW = "show"
    DELETE = "delete"
    SET = "set"
    REPLACE = "replace"
    FLUSH = "flush"

class IpOption:
    """This class holds an enumeration of command options"""

    ADDRESS = "addr"
    LINK = "link"
    ROUTE = "route"
    RULE = "rule"
    NEIGHBOUR = "neigh"

class IpConstant:
    """This class holds an enumeration of command constants"""

    IPV4 = "-4"
    IPV6 = "-6"
    TABLE = "table"
    SCOPE = "scope"
    PROTO = "proto"
    METRIC = "metric"
    SRC = "src"
    DEV = "dev"
    VIA = "via"
    FROM = "from"
    UP = "up"
    DOWN = "down"
    DEFAULT = "default"
    NAME = "name"

class Command(object):

    IP_COMMAND_NAME = "/sbin/ip"

    @staticmethod
    def execute(logger, name, args, cwd=None, timeoutSec=20, blocking=True, verbose=False):
        """This function executes the command described by args through the shell

        Args:
            logger
            name
            args       - args should be a string, or a sequence of program arguments
            cwd        - current directory will be changed to cwd before it is executed
            timeoutSec - the time (in sec) after which termination (SIGTERM) of the process will be attempted
            blocking   -  if True, waits for the command to complete 'timeoutSec' sec
            verbose    - if True, increases details of messages
            
        Return:
            tuple (rc, stdout, stderr)
            
            rc - 0 if OK, <0 indicates an error 
            stdout - standard ouput
            stderr - standard error
        """

        if not type(args) == type(""):
            cmdline = " ".join(args)
        else:
            cmdline = args

        if verbose:
            print cmdline

        logger("cmd-params").debug1("starting a process with command: %s", cmdline)

        # run the command
        subProc = a.infra.subprocess.Subprocess(name,logger)
        subProc.start(cmdline, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, setpgrp=True, cwd=cwd)

        logger("cmd-details").debug2("launched process %s using the command (timeout=%s , blocking=%s): '%s'. PID=%d", 
                                     name, timeoutSec, blocking, args, subProc.getPid())       
        
        if blocking is False:
            logger("cmd-details").debug3("launched non-blokcing process %s using the command: '%s'.", name, args)
            return (0,str(args),"")

        # terminate after Xs, no warning, kill after (X+2)s.
        stdOut,stdErr = subProc.communicate(terminateTimeOut=timeoutSec, warningTimeOut=0, killTimeOut=(timeoutSec+2.0)) 

        # prepare command result and output
        rc = subProc.getReturnCode()  
        stdOut = stdOut.strip()
        stdErr = stdErr.strip()
           
        if rc == 0:
            logger("cmd-stdout").debug3(stdOut)
        else:
            logger("cmd-stderr").debug1(stdErr)

        return (rc, stdOut, stdErr)

    @staticmethod
    def executeIp(logger, option, *cmd):
        """This function executes the ip command described by args through the shell

        Args:
            logger
            option -  option should be an IpOption
            cmd    -  should be a string, or a sequence of program arguments
            
        Return:
            tuple (rc, stdout, stderr)
            
            rc - 0 if OK, <0 indicates an error 
            stdout - standard ouput
            stderr - standard error
        """ 

        args = [Command.IP_COMMAND_NAME, option] + list(cmd)
        rc = Command.execute(logger, option, args)

        return rc

    @staticmethod
    def isReturnOk(rc):
        (returncode, stdout, stderr) = rc

        if returncode != 0:
            return False

        return True


class ConfigFile(object):

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def getValueByKey(logger, filename, key):

        logger("config-file-get").debug1("%s: looking for <%s> in file", filename, key)

        # opens the file for reading
        ifile = open(filename, 'r')

        value = None

        # looks in source for <key>
        for line in ifile:
            if line.startswith(key):
                value = line[len(key):]

        # close file
        ifile.close()

        return value

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def removeKey(logger, filename, key):
        ConfigFile.__setKey(logger, filename, key, "", False, True)

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def addKey(logger, filename, key, value):
        ConfigFile.__setKey(logger, filename, key, value, True, False)

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def changeKey(logger, filename, key, value):
        ConfigFile.__setKey(logger, filename, key, value, False, False)

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def __setKey(logger, filename, key, value, appendIfNotFound, removeIfFound):

        tempfile = ConfigFile.getTempFile(filename)
        if os.path.exists(tempfile):
            filename = tempfile
        
        if logger:
            logger("config-file-set").debug1("%s: setting <%s> to <%s> in file", filename, key, value)

        tempfile = ConfigFile.getTempFile(filename)

        # opens the file for reading
        ifile = open(filename, 'r')
        newlinesList = []

        isKeyFound = False
        shouldAdd = True
        newline = "%s%s\n" % (key,value)

        # looks in source for <key>
        for line in ifile:
            if line.startswith(key):
                logger("new-line-in-file").debug1("%s: <old line>= %s , <new line>= %s", filename, line, newline)
                line = newline
                isKeyFound = True
                shouldAdd = not removeIfFound

            if shouldAdd:
                newlinesList.append(line)
            shouldAdd = True

        if ((not isKeyFound) and appendIfNotFound):
            newlinesList.append(newline)

        # close file
        ifile.close()

        logger("data-to-file").debug2("%s: write to file - %s", filename, newlinesList)

        # writes to the temporary destination
        ofile = open(tempfile, 'w')
        ofile.writelines(newlinesList)
        ofile.close()


#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def commit(filename):

        tempfile = ConfigFile.getTempFile(filename)

        if os.path.exists(tempfile):
            # overrides the original source file with the temporary destination
            shutil.move(tempfile, filename)

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def abort(filename):

        tempfile = ConfigFile.getTempFile(filename)

        if os.path.exists(tempfile):
            # removes temporary file
            os.remove(tempfile)

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def getTempFile(filename):
        tempfile = "%s.tmp" % (filename)
        return tempfile

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def isFileValid(filename):
        # file exists and has read/write permissions
        return os.path.exists(filename) and os.access(filename, os.R_OK and os.W_OK) 
