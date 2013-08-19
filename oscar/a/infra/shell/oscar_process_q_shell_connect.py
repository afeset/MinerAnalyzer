# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
#
########################################################################################################################
#                                                                                                                      #
# This module is for sending commands to a q-shell of an oscar process
#                                                                                                                      #
########################################################################################################################

import os    
import time
import subprocess
from datetime import datetime

class OscarProcessQShellConnect:
    def __init__(self):
        self.myShellExecPath = None
        self.myPortNum = None
        self.myIp = None
        self.myDomainSocket = None
        self.myWaitForRunTestInterval=0.010#10 milli
        #If true runs in early log state
        self.myEarlyLogEnable = False
        #If true, the stderr will be written to parent process stderr and will not appear in this process sderr or stdout
        self.myStderrMask = False

    def initIpConnection(self, aShellExecPath, aPortNum, aIp = "127.0.0.1"):
        """
        Init the calss for the case the connection is via a IP:port
        """
        self.myShellExecPath=aShellExecPath
        self.myPortNum=aPortNum
        self.myIp=aIp

    def initDomainSocketConnection(self, aShellExecPath, aDomainSocket):
        """
        Init the calss for the case the connection is via a domain socket
        """
        self.myShellExecPath=aShellExecPath
        self.myDomainSocket=aDomainSocket

    def getQshellConnectionInfo(self):
        """
        returns a couple (connectionList, workingDirectory) that can be used in order to connect to the process shell
        The connection list is a list of string buildin the command opening the shell.
        The working directory (if not None) is the current working directory to be set when calling the connection command
        """
        if self.myShellExecPath == None:
            return (None,None)#Not init
        #assuming init was done to one of the options
        if self.myPortNum!=None:
            connectionString = [self.myShellExecPath, "--socket", "0","--port",str(self.myPortNum),"--address",str(self.myIp)]
            workingDirectory = None
        elif self.myDomainSocket!=None:
            #moving to domain socket direcoty as unix domain sockets support limited file size
            workingDirectory = os.path.abspath(os.path.dirname(self.myDomainSocket))
            newQshellExecutable = os.path.relpath(self.myShellExecPath,workingDirectory)
            newDomainSocketFile = os.path.basename(self.myDomainSocket)
            connectionString = [newQshellExecutable,"--socket","1","--address",newDomainSocketFile]
        else:
            return (None,None)
        #Adds early log flag to the connections string if flagged. This was added to shorten the time it takes to send a query message to the q-shell since
        #the log assumes 1 sec run for each process and delays the query to last at least one second
        if self.myEarlyLogEnable:
            connectionString += ["--early-log"]
        return (connectionString, workingDirectory)

    def runShellCmd(self, cmd, stdoutFile = None):
        """
        run the input shell command
        returns a couple (error, output)
        if "error" is not none - the command failed, otherwise it succeded
        the output is anyhow given in the output "parameter"
        """
        error = None
        output = None
        (connectionList, workingDirectory) = self.getQshellConnectionInfo()
        if connectionList == None:
            return (error, output)

        stdoutOutput = subprocess.PIPE
        if stdoutFile is not None:
            stdoutOutput = stdoutFile

        if self.myStderrMask:
            stderrOutput = None
        else:
            stderrOutput = subprocess.STDOUT

        p2 = subprocess.Popen(connectionList, shell=False, stdin=subprocess.PIPE, stdout=stdoutOutput, stderr=stderrOutput, 
                              cwd=workingDirectory, close_fds=True)

        cmd=cmd.strip()+"\n"
        output = p2.communicate(input=cmd)[0]

        if stdoutFile is None:
            outputLines = output.split("\n")
            for line in outputLines:
                if line.startswith("Error: "):
                    if error is None:
                        error =""
                    else:
                        error +=";"
                    error += line[7:]
            return (error, output)
        else:
            return (None, None)



    def waitForQshellRunningIndicationOrTimeout (self, shellCommandPrefix, timeoutTargetTime):
        """
        sleep and test from time to time if the process is responding to "q-shell" and if it is in a "running" phase
        Return True if the responding stage arrived before provided absolute time given as input.
        shellCommandPrefix is the prefix starting any shell command in the process. usually it is the process name. If set to "", will assume no prefix is needed
        """
        return self._waitForQshellRunningIndicationOrTimeout(shellCommandPrefix=shellCommandPrefix, timeoutTargetTime=timeoutTargetTime)[0]

    def waitForQshellRunningIndicationOrTimeoutWithOutput (self, shellCommandPrefix, timeoutTargetTime):
        """
        sleep and test from time to time if the process is responding to "q-shell" and if it is in a "running" phase
        Return True if the responding stage arrived before provided absolute time given as input.
        shellCommandPrefix is the prefix starting any shell command in the process. usually it is the process name. If set to "", will assume no prefix is needed
        """
        return self._waitForQshellRunningIndicationOrTimeout(shellCommandPrefix=shellCommandPrefix, timeoutTargetTime=timeoutTargetTime)


    def _waitForQshellRunningIndicationOrTimeout (self, shellCommandPrefix, timeoutTargetTime):
        """
        #code allowing to figure out the prefix on our own - currently unsupported
        while shellCommandPrefix == None:
            cmd = "?"
            (error,output) = self.runShellCmd(cmd)
            if error is None:
                outputLines = output.split("\n")
                for i in range(0,len(outputLines)):
                    if "Qwilt>?" in outputLines[i]:
                        shellCommandPrefix = outputLines[i+1].strip()
                        break
                break
            if not timeoutTargetTime > datetime.now():
                return False#timeout  
            time.sleep(self.myWaitForRunTestInterval)
        """

        testRunningCmd = ""
        if shellCommandPrefix!="":
            testRunningCmd += shellCommandPrefix+"/"
        testRunningCmd+="captain.isInRunningStage()"
        while True:
            (error,output) = self.runShellCmd(testRunningCmd)
            if error is None and "isRunning=true" in output.split("\n"):
                return (True, output)#success
            if not timeoutTargetTime > datetime.now():
                return (False, output)#timeout  
            time.sleep(self.myWaitForRunTestInterval)

        return (False, output)

    def openQshellConnection (self):
        """
        open a q-shell connection to the process
        return None zero in case of a failure
        """
        (connectionList, workingDir) = self.getQshellConnectionInfo()
        if connectionList is None:
            return 1
        rc=subprocess.call(" ".join(connectionList), shell=True, cwd=workingDir)
        return rc


