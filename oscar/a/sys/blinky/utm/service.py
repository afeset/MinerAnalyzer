# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

import os
import subprocess
import shutil
import socket
import time

import a.sys.blinky.blinky_process
from a.sys.blinky.agent import Agent
from a.sys.confd.pyconfdlib import pyconfdlib
from a.infra.basic.return_codes import ReturnCodes

class BlinkyUtmService (object):
    def __init__ (self, logger):
        self._log=logger.createLogger("sys-blinky-utm", "service")
        self.confdBinPathPostfix = 'ext/confd-dev'
        self.cmdStr = {
            'start' : 'start',
            'stop' : 'stop',
            'cli' : 'cli',
            'waitStarted' : 'waitStarted'
            }
        self.myInteractiveCliUsername = 'admin'
        self.myOptions = None
        self.myNetconfPort = 0
        self.mySshPort = 0
        self.mySnmpPort = 0
        self.myIpcPort = 0
        self.myFxsLoadPath = []
        self.myTestOutDir = None
        self.myTestTempDir = None
        self.mySrcRootDir = None
        self.myOutRootDir = None
        self.utServices = None
        self.maapiSock = None
        self.transactionHandle = None
        self.ignoreInitialValidation = False

    def initUtServices (self, _utServices):
        for logFunc in self._log("init-ut-services").debug1Func(): logFunc('initializing unit-test services')
        self.utServices = _utServices
        self.setOutRootDir(self.utServices.getOutRoot())
        self.setSrcRootDir(self.utServices.getBranchRoot())
        self.setTestTempDir(self.utServices.getTestTempDir())
        self.setTestOutDir(self.utServices.getTestOutDir())

        self.setIpcPort(self.utServices.getNextPort())

        for logFunc in self._log("init-ut-services-ports").debug1Func(): logFunc('ports:ipc=%d, ssh=%d, snmp=%d, netconf=%d',
                                                   self.myIpcPort, self.mySshPort, self.mySnmpPort, self.myNetconfPort)

        (self.myOptions, args) = self.utServices.parseArgs()

    def needSsh (self):
        self.setSshPort(self.utServices.getNextPort())

    def needSnmp (self):
        self.setSnmpPort(self.utServices.getNextPort())

    def needNetconf (self):
        self.setNetconfPort(self.utServices.getNextPort())

    @staticmethod
    def utClientInit (_utServices):
        parser = _utServices.getOptionParser()
        parser.add_option("--run-cli-after-start", action="store_true", dest="runCliAfterStart", default=False, help="Run cli after confd starts")
        parser.add_option("--run-cli-before-end", action="store_true", dest="runCliBeforeEnd", default=False, help="Run cli before confd ends")
        parser.add_option("--run-cli-before-each-script", action="store_true", dest="runCliBeforeEachScript", default=False, help="Run cli before each script")
        parser.add_option("--run-cli-after-each-script", action="store_true", dest="runCliAfterEachScript", default=False, help="Run cli after each script")
        
    def getAgent (self, logger, name):
        for logFunc in self._log("get-agent").debug1Func(): logFunc('getting agent %s', name)
        agent=Agent(logger=logger)
        agent.setName(name)
        agent.initBlinky("127.0.0.1", self.myIpcPort)
        if hasattr(self.myOptions, 'runCliAfterStart'):
            if self.myOptions.runCliAfterStart:
                self.runCli(None, self.myInteractiveCliUsername)
        return agent

    def startMaapiTransaction (self, transactionType, namespace):
        for logFunc in self._log("start-maapi-transaction").debug1Func(): logFunc('called')
        maapiSock = socket.socket()
        self.maapiSock = maapiSock 
        res = pyconfdlib.maapi_connect(self.maapiSock, pyconfdlib.AF_INET, "127.0.0.1", self.myIpcPort)
        # Do not keep useless sockets empty
        if res != pyconfdlib.CONFD_OK:
            for logFunc in self._log("start-maapi-transaction-maapi-connect-failed").debug1Func(): logFunc('maapi_connect failed')
            return ReturnCodes.kGeneralError
        res = pyconfdlib.maapi_load_schemas(self.maapiSock)
        if res != pyconfdlib.CONFD_OK:
            for logFunc in self._log("start-maapi-transaction-load-schemas-failed").errorFunc(): logFunc("maapi_load_schemas() failed")
            return ReturnCodes.kGeneralError
        res = pyconfdlib.maapi_start_user_session(self.maapiSock, None, "system", [], pyconfdlib.AF_INET, "127.0.0.7", 
                                                  pyconfdlib.CONFD_PROTO_TCP)
        if res != pyconfdlib.CONFD_OK:
            for logFunc in self._log("start-maapi-transaction-start-user-session-failed").errorFunc(): logFunc("maapi_start_user_session() failed")
            return ReturnCodes.kGeneralError

        self.transactionHandle = pyconfdlib.maapi_start_trans(self.maapiSock, pyconfdlib.CONFD_RUNNING, transactionType)

        res = pyconfdlib.maapi_set_namespace(self.maapiSock, self.transactionHandle, namespace)
        if res != pyconfdlib.CONFD_OK:
            for logFunc in self._log("start-maapi-transaction-set-namespace-failed").errorFunc(): logFunc("maapi_set_namespace() failed")
            return ReturnCodes.kGeneralError

        for logFunc in self._log("start-maapi-transaction-done").debug2Func(): logFunc("done")
        return ReturnCodes.kOk

    def endMaapiTransaction (self):
        for logFunc in self._log("end-maapi-transaction").debug1Func(): logFunc('called')
        res = pyconfdlib.maapi_finish_trans(self.maapiSock, self.transactionHandle)
        if res != pyconfdlib.CONFD_OK:
            for logFunc in self._log("start-maapi-transaction-finish-transaction-failed").debug1Func(): logFunc('maapi_finish_trans() failed')
            return ReturnCodes.kGeneralError

        res = pyconfdlib.maapi_end_user_session(self.maapiSock)
        if res != pyconfdlib.CONFD_OK:
            for logFunc in self._log("start-maapi-transaction-end-user-session-failed").errorFunc(): logFunc("maapi_end_user_session() failed")
            return ReturnCodes.kGeneralError

        self.maapiSock.close()
        self.maapiSock = None

        for logFunc in self._log("end-maapi-transaction-done").debug2Func(): logFunc("done")
        return ReturnCodes.kOk

    def setInteractiveCliUsername (self, username):
        for logFunc in self._log("set-interactive-cli-username").debug1Func(): logFunc('setting interactive cli username: %s', username)
        self.myInteractiveCliUsername = username

    def calcExecutionEnvVars (self, otherEnv):
        for logFunc in self._log("calc-execution-env-vars").debug1Func(): logFunc('calculating execution environment variables')
        env = os.environ.copy()
        keysToMergeAsPaths=['LD_LIBRARY_PATH']
        for key in otherEnv:
            if key not in env:
                env[key]=otherEnv[key]
            else:
                if key in keysToMergeAsPaths:
                    env[key]=env[key]+":"+otherEnv[key]
                else:
                    raise Exception ("Error: got otherEnv["+str(key)+"]="+str(otherEnv[key])+", entry exists for this key in env, I do not know how to merge this key")
        return env

    def runCliString (self, cliStr, username='tech'):
        tempCliScriptFilename=os.path.join(self.myTestTempDir, 'cliTempScript.txt')
        for logFunc in self._log("run-cli-string").debug1Func(): logFunc('tempCliScriptFilename: %s, as user: %s (dir: %s)', tempCliScriptFilename, username, self.myTestTempDir)
        tempCliScriptFile=open(tempCliScriptFilename, 'w+')
        tempCliScriptFile.write(cliStr)
        tempCliScriptFile.close()
        self.runCli(tempCliScriptFilename, username)
        os.remove(tempCliScriptFilename)
    
    def runCliScriptFromSrc (self, cliScriptName, username='tech'):
        cliScrptFullPath = None
        if cliScriptName:
            cliScrptFullPath = os.path.join(self.utServices.getSourceDir(), cliScriptName)
        self.runCli(cliScrptFullPath, username)

    def runCli (self, cliScriptName, username='tech'):
        confdBinDir = os.path.join(self.myOutRootDir, self.confdBinPathPostfix)
        launchCmd = [os.path.join(confdBinDir, 'bin/confd_cli'),
                     '-C',
                     '-P',
                      self.myIpcPort.__str__()]
        if username:
            launchCmd.append('-u')
            launchCmd.append(username)
        if cliScriptName:
            launchCmd.append(cliScriptName)
            if hasattr(self.myOptions, 'runCliBeforeEachScript'):
                if self.myOptions.runCliBeforeEachScript:
                    self.runCli(None, self.myInteractiveCliUsername)
        for logFunc in self._log("run-cli-command").debug1Func(): logFunc('command is: %s', ' '.join(launchCmd))
        proc = subprocess.Popen(" ".join(launchCmd), shell=True)
        if (proc.returncode != None):
            errStr = 'Failed to launch command: %s. rc=%d' % (launchCmd, proc.returncode)
            print errStr
            raise Exception(errStr)
        proc.wait()
        for logFunc in self._log("run-cli-command-after").debug1Func(): logFunc('after running command is: %s', ' '.join(launchCmd))
        if hasattr(self.myOptions, 'runCliAfterEachScript'):
            if self.myOptions.runCliAfterEachScript and cliScriptName:
                self.runCli(None, self.myInteractiveCliUsername)

    def setOutRootDir (self, _dir):
        self.myOutRootDir = _dir
    
    def setSrcRootDir (self, _dir):
        self.mySrcRootDir = _dir

    def setTestTempDir (self, _dir):
        for logFunc in self._log('set-test-temp-dir').debug3Func(): logFunc('setting test temp directory: %s', _dir)
        self.myTestTempDir = _dir

    def setTestOutDir (self, _dir):
        self.myTestOutDir = _dir

    def setFxsLoadPathRelativeToOut (self, _path):
        self.myFxsLoadPath = [os.path.join(self.utServices.getOutRoot(), _path)]

    def addFxsLoadPathRelativeToOut (self, _path):
        self.myFxsLoadPath.append(os.path.join(self.utServices.getOutRoot(), _path))

    def setAbsoluteFxsLoadPath (self, _path):
        self.myFxsLoadPath = _path

    def setIpcPort (self, _port):
        self.myIpcPort = _port

    def setSshPort (self, _port):
        self.mySshPort = _port

    def setSnmpPort (self, _port):
        self.mySnmpPort = _port

    def setNetconfPort (self, _port):
        self.myNetconfPort = _port

    def getIpcPort (self):
        return self.myIpcPort

    def setIgnoreInitialValidation (self, ignore):
        self.ignoreInitialValidation = ignore

    def runConfdOperation (self, command, persistant=False):
        """
        persistant: If 'False' (default), does not remember confd pid on start, and does not wait() for it to exit on stop.
            This it good for cases in which the 'start' and 'stop' commands are run by different processes (such as what happens
            when running C++ unit tests).
            If 'True', confd pid is remembered on 'start' and during 'stop' we wait for it to exit. This is good for 
            cases in which this module is used by the same process (Such as what happens when running Python unit tests)
        """

        for logFunc in self._log("run-confd-operation").noticeFunc(): logFunc('running confd operation: %s, (persistant: %s)', command, str(persistant))
        confdBinDir = os.path.join(self.myOutRootDir, self.confdBinPathPostfix)
        binDir = os.path.join(self.mySrcRootDir, 'sys/blinky/target_files')
        dataDir = os.path.join(self.myTestTempDir, "data")
        varDir = os.path.join(self.myTestOutDir, "var")
        ramDir = os.path.join(self.myTestTempDir, "ram")
    
        blinkyProcess = a.sys.blinky.blinky_process.BlinkyProcess()
        blinkyProcess.init(binDir, dataDir, varDir, ramDir, confdBinDir)
        blinkyProcess.calcPaths()
    
        for loadpath in self.myFxsLoadPath:
            blinkyProcess.addFxsLoadPath(loadpath)
    
        blinkyProcess.setConfigParams(self.myIpcPort, self.mySshPort, self.mySnmpPort, self.myNetconfPort, 0, varDir)
        blinkyProcess.setAuditLog(True)
        blinkyProcess.setDevelLog(True)
        blinkyProcess.setDevelLogLevel('trace')
        blinkyProcess.setConfdLog(True)
        blinkyProcess.setNetconfLog(True)

        blinkyProcess.setLogNetstat(True)

        blinkyProcess.setIgnoreInitialValidation(self.ignoreInitialValidation)
    
        if (command == self.cmdStr['start']):
            (error, launchCmd, env) = blinkyProcess.start()
        elif (command == self.cmdStr['stop']):
            if hasattr(self.myOptions, 'runCliBeforeEnd'):
                if self.myOptions.runCliBeforeEnd:
                    self.runCli(None, self.myInteractiveCliUsername)
            (error, launchCmd, env) = blinkyProcess.stop()
        elif (command == self.cmdStr['waitStarted']):
            (error, launchCmd, env) = blinkyProcess.waitStarted()
        else:
            errStr = 'illegal command: %s. Must be one of: %s' % (command, [self.cmdStr['start'], self.cmdStr['stop']])
            print errStr
            raise Exception(errStr)
    
        if error is not None:
            errStr = "Failed to get start command. Error is: %s." % str(error)
            print errStr
            raise Exception(errStr)
    
        if not launchCmd:
            errStr = "start command is None."
            print errStr
            raise Exception(errStr)
    
    #        print ("command line is: %s " % " ".join(launchCmd))
        completeEnv = None
        if env:
            completeEnv = self.calcExecutionEnvVars(env)
    #        print "completeEnv=",completeEnv
        proc = subprocess.Popen(" ".join(launchCmd), shell=True, env=completeEnv)
        if (proc.returncode != None):
            errStr = 'Failed to launch command: %s. rc=%d' % (launchCmd, proc.returncode)
            print errStr
            raise Exception(errStr)

        # If we do notneed to remember confd pid on start and wait for it on stop, finish here.
        if not persistant:
            for logFunc in self._log("run-confd-operation-finished-not-persistant").noticeFunc(): logFunc('run confd operation: %s - completed (not persistant)', command)
            return

        # On startup, remember proc. On stop, wait for it
        if (command == self.cmdStr['start']):
            self.startProc=proc
        elif (command == self.cmdStr['waitStarted']):
            proc.wait()
        elif (command == self.cmdStr['stop']):
            # Wait for 'stop' command to finish. 
            # Note, if test is really fast, and does not actually wait for confd to start (for whatever reason)
            # the stop command may fail because confd did not start yet.
            # So we need to retry a few times.
            print "Waiting for 'stop' command to return"
            tryCountDown=10
            while tryCountDown>0:
                proc.wait()
                if proc.returncode != 0:
                    tryCountDown=tryCountDown-1
                    print "stop command failed, retrying..."
                    time.sleep(1)
                    proc = subprocess.Popen(" ".join(launchCmd), shell=True, env=completeEnv)
                    if (proc.returncode != None):
                        errStr = 'Failed to launch command: %s. rc=%d' % (launchCmd, proc.returncode)
                        print errStr
                        raise Exception(errStr)
                else:
                    # Stop the loop
                    print "stop command succeeded."
                    tryCountDown=0

            if proc.returncode != 0:
                raise Exception("Failed to stop confd, stop command returned %s" % proc.returncode)
            # Wait for original confd process to exit
            print "Waiting for confd to exit"
            self.startProc.wait()
            if self.startProc.returncode != 0:
                raise Exception("Failed to stop confd, confd returned %s on exit" % self.startProc.returncode)

            for logFunc in self._log("run-confd-operation-finished").noticeFunc(): logFunc('run confd operation: %s - completed', command)

    def cleanUp (self):
        for logFunc in self._log("cleanup").debug1Func(): logFunc('cleaning up')
        dataDir = os.path.join(self.myTestTempDir, "data")
        #print "cleanUp(): Data dir is: ",dataDir
        for logFunc in self._log("cleanup-data-dir").debug3Func(): logFunc('cleaning up data dir: %s', dataDir)
        if os.path.exists(dataDir):
            for logFunc in self._log("cleanup-data-dir").debug3Func(): logFunc('existing data dir: %s', dataDir)
            shutil.rmtree(dataDir)
            #print "Data dir removed: ",dataDir
        ramDir = os.path.join(self.myTestTempDir, "ram")
        for logFunc in self._log("cleanup-ram-dir").debug3Func(): logFunc('cleaning up ram dir: %s', ramDir)
        #print "cleanUp(): Ram dir is: ",ramDir
        if os.path.exists(ramDir):
            for logFunc in self._log("cleanup-ram-dir").debug3Func(): logFunc('existing ram dir: %s', ramDir)
            shutil.rmtree(ramDir)
            #print "Ram dir removed: ",ramDir

