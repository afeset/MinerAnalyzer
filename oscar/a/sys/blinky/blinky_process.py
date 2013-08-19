#
# To run confd:
# 1. configure confd.conf with:
#    a. directories
#       1) state
#       2) cdb
#       3) logs
#       4) rollback
#       5) docroot
#    b. ports
#    c. log level
# 2. build directories
# 3. build environment variables
# 4. return confd run command

# TODO(naamas)
# Add self.dorcroot
#
# Confd directories:
# loadPath (/confdConfig/loadPath/dir) (multiple)                                                   | bin/blinky/model/fxs, bin/blinky/model/ccl
# state (/confdConfig/stateDir)                                                                     | app/blinky/data/var/confd/state
# docroot (/confdConfig/webui/docroot)                                                              | bin/blinky/model/confd-web/docroot
# db (/confdConfig/cdb/dbDir)                                                                       | app/blinky/data/confd/db
# init (/confdConfig/cdb/initPath) (multiple)                                                       | app/blinky/data/confd/init + bin/blinky/init
# operational db (/confdConfig/cdb/operational/dbDir)                                               | app/blinky/data/confd/oper-db
# webui access log (/confdConfig/logs/webuiAccessLog/dir) + other logs                              | app/blinky/data/var/logs/confd
# rollback (confdConfig/rollback/directory)                                                         | app/blinky/data/confd/rollback
# (?) show-log (confdConfig/cli/showLogDirectory)                                                   | 
# ssh server key (/confdConfig/aaa/sshServerKeyDir)                                                 | app/blinky/data/ssh-key-dev
# log files wrapping (/confdConfig/notifications/eventStreams/stream/builtinReplayStore/dir         | app/blinky/data/confd/replay
# config template:                                                                                  | bin/blinky/config/
# ld lib path                                                                                       | bin/confd/lib64

import os
#print os.environ['PYTHONPATH']
import os.path
import a.infra.file.utils
#import datetime
from xml.dom.minidom import *
import subprocess
#import sys
from a.sys.net.lnx.device import DeviceUtils
from a.sys.net.lnx.route import RoutingUtils

import json
import glob

# === BlinkyProcess ===================================================================================================
class BlinkyProcess():

    # --- init --------------------------------------------------------------------------------------------------------
    def init(self, binDir, sysVarDir, sysRunDir, dataVarDir, confdBinDir, platformCdbInitDir=None, confdConfInitDir=None, device=None, timeString = None, sshEnabled = False, netconfEnabled = False, verbose = False):
        # binDir is bin/blinky
        # dataDir is app/blinky/data
        # varDir is app/blinky/data/var
        # confdBinDir is bin/confd
        self.binDir         = binDir
        self.dataVarDir     = dataVarDir
        self.sysVarDir      = sysVarDir
        self.sysRunDir      = sysRunDir
        self.sshKeyDir      = None
        if (timeString is not None):
            self.timeString = "-%s" % timeString
        else:
            self.timeString = ""
        self.confdBinDir    = confdBinDir
        self.platformCdbInitDir = platformCdbInitDir
        self.confdConfInitDir = confdConfInitDir
        self.device         = device
        self.sshEnabled     = sshEnabled

        self.confdExecutable = "confd"

        self.verbose = verbose

        self.fxsLoadPath = []

        self._swVersionStr = "Unknown"
        self._mspVersionStr = "Unknown"

        self.netconfEnabled = netconfEnabled
        self.netconfEnabledTraceLog = None

        self.confdLogEnabled = False
        self.develLogEnabled = False
        self.snmpLogEnabled = False
        self.auditLogEnabled = True
        self.binErrorLogEnabled = False
        self.binErrorLogMaxSizeMB = 50
        self.netconfLogEnabled = False
        self.xpathTraceLogEnabled = False

        self.logNetstatOn = False

        self.develLogLevel = "info"
        self.snmpLogLevel = "info"

        self.myWaitStartedTryTime = 10

        self.platformInitDir = ''

        self._objId = None

        self.ignoreInitialValidation = False

    def setConfigParams(self, ipcPort, sshPort, snmpPort, netconfSshPort, webuiPort, userHomeDir, mngIp=None, webuiIp=None, sshKeyDir=None):
        self.ipcPort    = ipcPort
        self.mngIp      = mngIp
        self.sshPort    = sshPort
        self.snmpPort   = snmpPort 
        self.netconfSshPort = netconfSshPort
        self.webuiIp    = webuiIp
        self.webuiPort  = webuiPort
        self.userHomeDir = userHomeDir
        if sshKeyDir:
            self.sshKeyDir = sshKeyDir        

    def setConfdLog (self, logOn):
        self.confdLogEnabled = logOn

    def setDevelLog (self, logOn):
        self.develLogEnabled = logOn

    def setDevelLogLevel (self, logLevel):
        self.develLogLevel = logLevel

    def setSnmpLog (self, logOn):
        self.snmpLogEnabled = logOn

    def setSnmpLogLevel (self, logLevel):
        self.snmpLogLevel = logLevel

    def setAuditLog (self, logOn):
        self.auditLogEnabled = logOn

    def setBinErrorLog (self, logOn):
        self.binErrorLogEnabled = logOn

    def setBinErrorLogMaxSizeMB (self, size):
        self.binErrorLogMaxSizeMB = size

    def setNetconfLog (self, logOn):
        self.netconfLogEnabled = logOn

    def setNetconfTraceLog (self, traceLogOn):
        self.netconfEnabledTraceLog = traceLogOn

    def setXPathTraceLog (self, logOn):
        self.xpathTraceLogEnabled = logOn

    def addFxsLoadPath(self, fxsLoadPath):
        self.fxsLoadPath.append(fxsLoadPath)

    def setPlatformInitDir (self, platformInitDir):
        self.platformInitDir = os.path.join(os.path.join(self.binDir, 'init'), platformInitDir)

    def setMyWaitStartedTryTime (self, tryTime):
        self.myWaitStartedTryTime = tryTime

    def setIgnoreInitialValidation (self, ignore):
        self.ignoreInitialValidation = ignore

    def setLogNetstat (self, logOn):
        self.logNetstatOn = logOn

    def setSwVersionStr (self, versionStr):
        self._swVersionStr = versionStr

    def setMspVersionStr (self, versionStr):
        self._mspVersionStr = versionStr

    # --- install -----------------------------------------------------------------------------------------------------
    def install(self):
        error = None
        cmd   = None
        return (error, cmd)

    # --- start -------------------------------------------------------------------------------------------------------
    def start(self):

        self.printDirsAndFiles()

        self._createDirsAndFiles()

        self._buildAaaInit()

        self._buildInterfacesInit()

        self._perPlatformInit()

        self._buildConfdConfig()

        if self.logNetstatOn:
            self._logNetstat()

        # Set start command 
        cmd   = [self.confdExecutablePath, "-c", self.runningConfFile, "--foreground", "--nolog", "--ignore-initial-validation"]
        if self.ignoreInitialValidation:
            cmd.append("--ignore-initial-validation")
        if (self.verbose):
            cmd.append("-v")
        error = None
        return (error, cmd, None)
        
    # --- stop --------------------------------------------------------------------------------------------------------
    def stop(self):

        # Set stop command 
        cmd   = [self.confdExecutablePath, " --stop"]
        appendToEnv = {"CONFD_IPC_PORT" : str(self.ipcPort)}
        error = None
        return (error, cmd, appendToEnv)

    # --- waitStarted --------------------------------------------------------------------------------------------------------
    def waitStarted (self):

        # Set wait-started command 
        cmd   = [self.confdExecutablePath, " --wait-started", str(self.myWaitStartedTryTime)]
        appendToEnv = {"CONFD_IPC_PORT" : str(self.ipcPort)}
        error = None
        return (error, cmd, appendToEnv)

    # --- getConfdExecPath --------------------------------------------------------------------------------------------------
    def getConfdExecPath(self):
        return self.confdExecutablePath

    # --- getConfdExecPath --------------------------------------------------------------------------------------------------
    def getConfdCliExecPath(self):
        return self.confdCliExecutionPath


    # --- getLogDirs --------------------------------------------------------------------------------------------------
    def getLogDirs(self):

        # Returns a list of directories containing log files 
        return [self.logsConfdDir]

    # --- getLogDirs --------------------------------------------------------------------------------------------------
    def getAuditLogDir(self):
        return self.logsConfdDir

    # --- getLogDir --------------------------------------------------------------------------------------------------
    def getLogDir(self, entity):
        dirPerEntity = self.getLogDirsPerEntity()
        if entity in dirPerEntity:
            return dirPerEntity[entity]
        return None

    def getLogDirsPerEntity (self):
        return {"confd": self.logsConfdDir}

    def clearConfdDb(self):
        a.infra.file.utils.removeFile(os.path.join(self.dbDir, "A.cdb"), True)
        a.infra.file.utils.removeFile(os.path.join(self.dbDir, "C.cdb"), True)
        a.infra.file.utils.removeFile(os.path.join(self.candidateDbDir, "candidate.db"), True)
        a.infra.file.utils.removeFile(os.path.join(self.operDbDir, "O.cdb"), True)

    def getStatusString (self):
        isActive = False
        cmd   = [self.confdExecutablePath, "--status"]
        envDict = {"CONFD_IPC_PORT" : "%s" % self.ipcPort}
        p = subprocess.Popen(cmd, env = envDict, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out,dummy = p.communicate()
        rc=p.wait()
        if rc != 0:
            return ("down", isActive)
        lines = out.splitlines(True)
        for line in lines:
            statMarker = "status:"
            pos = line.find(statMarker)
            if (pos == 0):
                statusString = line[len("status:")+1:-1]
                if statusString.find("started") != -1:
                    isActive = True
                return (statusString, isActive)
        return ("down", isActive)

    # --- calcPaths --------------------------------------------------------------------------------------------------
    def calcPaths(self):

        self.modelDir      = os.path.join(self.binDir, "model")
        self.fxsDir        = os.path.join(self.modelDir, "fxs")
        self.cclDir        = os.path.join(self.modelDir, "ccl")
        self.confdFxsDir   = os.path.join(self.confdBinDir, "etc/confd")
        self.snmpFxsDir   = os.path.join(self.confdBinDir, "etc/confd/snmp")
        self.docrootDir    = os.path.join(self.modelDir, "confd-web/docroot")

        self.dbDir          = os.path.join(self.sysVarDir, "cdb")
        self.candidateDbDir = os.path.join(self.sysVarDir, "candidate-db")
        self.operDbDir     = os.path.join(self.sysVarDir, "oper-db")
        self.rollbackDir   = os.path.join(self.sysVarDir, "rollback")
        self.dynamicInitDir = os.path.join(self.sysRunDir, "init")
        self.staticInitDir = os.path.join(self.binDir, "init")
        

        if not self.sshKeyDir:
            self.sshKeyDir     = os.path.join(self.binDir, "ssh-key-dev")
        
        self.stateDir      = os.path.join(self.sysVarDir, "state")

        self.logsConfdDir       = os.path.join(self.dataVarDir, "log/confd")

        self.configTemplateDir = os.path.join(self.binDir, "config")
        self.configDir         = os.path.join(self.sysRunDir, "conf")

        self.xmlInitTemplateDir = os.path.join(self.binDir, "init")

        # Log files
        self.confdLog      = os.path.join(self.logsConfdDir, "confd%s.log" % self.timeString)
        self.develLog      = os.path.join(self.logsConfdDir, "devel%s.log" % self.timeString)
        self.snmpLog       = os.path.join(self.logsConfdDir, "snmp%s.log" % self.timeString)
        self.auditLog      = os.path.join(self.logsConfdDir, "audit%s.log" % self.timeString)
        self.binErrorLog   = os.path.join(self.logsConfdDir, "binerror%s.log" % self.timeString)
        self.netconfLog    = os.path.join(self.logsConfdDir, "netconf%s.log" % self.timeString)
        self.netconfTraceLog = os.path.join(self.logsConfdDir, "netconfTrace%s.log" % self.timeString)
        self.xpathTraceLog = os.path.join(self.logsConfdDir, "xpathTrace%s.log" % self.timeString)

        # netstat log file
        # this file is saved under test's out dir, not temp, as it is needed for debugging of successful tests also
        self.netstatLogDir = os.path.join(self.sysRunDir, "netstat")
        self.netstatLogFile = os.path.join(self.netstatLogDir, "netstat_output.log")

        # Configuration
        self.templateConfFile = os.path.join(self.configTemplateDir, "confd.conf.template")
        self.runningConfFile = os.path.join(self.configDir, "confd.conf")

        # aaa
        self.templateAaaInitFile = os.path.join(self.xmlInitTemplateDir, "aaa_init.xml.template")
        self.runningAaaInitFile = os.path.join(self.dynamicInitDir, "aaa_init.xml")

        # interfaces
        self.templateInterfaceInitFile = os.path.join(self.xmlInitTemplateDir, "qwilt-tech-interfaces-init.xml.template")
        self.runningInterfaceInitFile = os.path.join(self.dynamicInitDir, "qwilt-tech-interfaces-init.xml")

        self.confdExecutablePath = os.path.join(self.confdBinDir, "bin/confd")
        self.confdCliExecutionPath = os.path.join(self.confdBinDir, "bin/confd_cli")
    
    def getConfdConfFile (self):
        return self.runningConfFile

    def printDirsAndFiles (self):
        if self.verbose:            
            print "self.modelDir      :", self.modelDir      
            print "self.fxsDir        :", self.fxsDir        
            print "self.cclDir        :", self.cclDir        
            print "self.confdFxsDir   :", self.confdFxsDir   
            print "self.snmpFxsDir    :", self.snmpFxsDir
            print "self.docrootDir    :", self.docrootDir                
            print "self.dbDir         :", self.dbDir         
            print "self.candidateDbDir :", self.candidateDbDir 
            print "self.operDbDir     :", self.operDbDir     
            print "self.dynamicInitDir :", self.dynamicInitDir
            print "self.staticInitDir :", self.staticInitDir
            print "self.rollbackDir   :", self.rollbackDir   
            print "self.sshKeyDir     :", self.sshKeyDir                 
            print "self.rollbackDir   :", self.rollbackDir   
            print "self.stateDir      :", self.stateDir      
            print "self.logsConfdDir       :", self.logsConfdDir       
            print "self.configTemplateDir :", self.configTemplateDir 
            print "self.configDir         :", self.configDir         
            print "self.confdLog      :", self.confdLog      
            print "self.develLog      :", self.develLog      
            print "self.snmpLog       :", self.snmpLog      
            print "self.auditLog      :", self.auditLog      
            print "self.binErrorLog   :", self.binErrorLog
            print "self.netconfLog    :", self.netconfLog    
            print "self.netconfTraceLog :", self.netconfTraceLog
            print "self.xpathTraceLog :", self.xpathTraceLog
            print "self.netstatLogDir: ", self.netstatLogDir
            print "self.netstatLogFile: ", self.netstatLogFile
            print "self.templateConfFile :", self.templateConfFile 
            print "self.runningConfFile :", self.runningConfFile 
            print "self.templateAaaInitFile :", self.templateAaaInitFile
            print "self.runningAaaInitFile :", self.runningAaaInitFile 
            print "self.templateInterfaceInitFile :", self.templateInterfaceInitFile
            print "self.runningInterfaceInitFile :", self.runningInterfaceInitFile 
            print "self.platformCdbInitDir :", self.platformCdbInitDir
            print "self.confdConfInitDir: ", self.confdConfInitDir
            for iPath in self.fxsLoadPath:
                print "fxsLoadPath: ", iPath

    # --- _createDirsAndFiles -----------------------------------------------------------------------------------------
    def _createDirsAndFiles(self):

        # Create general dirs        
        a.infra.file.utils.makeDirs(self.dbDir, reuseExisting=True)
        a.infra.file.utils.makeDirs(self.candidateDbDir, reuseExisting=True)
        a.infra.file.utils.makeDirs(self.operDbDir, reuseExisting=True)
        a.infra.file.utils.makeDirs(self.dynamicInitDir, reuseExisting=True)        
        a.infra.file.utils.makeDirs(self.rollbackDir, reuseExisting=True)
        a.infra.file.utils.makeDirs(self.stateDir, reuseExisting=True)
        a.infra.file.utils.makeDirs(self.logsConfdDir, reuseExisting=True)
        a.infra.file.utils.makeDirs(self.configDir, reuseExisting=True)
        if self.logNetstatOn:
            a.infra.file.utils.makeDirs(self.netstatLogDir, reuseExisting=True)

    def _logNetstat (self):
        cmd   = ["netstat", "-tnp"]
        out_file = open(self.netstatLogFile, 'w')
        out_file.write('IPC port is: %s' % self.ipcPort)
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (stdoutData, stderrData) = p.communicate()
        for line in stdoutData:
            if line.find('%s' % self.ipcPort) > -1:
                out_file.write(line)
        out_file.close()

    def _makeAbsolutePath (self, val):
        # check it val is a string
        if not isinstance(val, basestring):
            return val
        # check if val is a path
        if val.find('/') < 0:
            return val
        # check it val is an absolute path
        if os.path.isabs(val):
            return val
        # join bin dir with val
        return os.path.join(self.binDir, val)

                
    def _setXmlElement (self, dom, rootNode, element, val, append=False):
        val = self._makeAbsolutePath(val)
        parent=rootNode
        child = None
        nodeExists = True
        for node in element:
            if len(parent.getElementsByTagName(node)) == 0:
                child = dom.createElement(node)
                parent.appendChild(child)
                parent = child
                nodeExists = False
            else:
                child = parent.getElementsByTagName(node)[0]
                parent = child

        valueSet = False
        if (nodeExists):
            if (append):
                parent = child.parentNode
                child = dom.createElement(element[-1])
                parent.appendChild(child)
            else:
                child.firstChild.nodeValue = val
                valueSet = True
        if (not valueSet):
            finalNode = dom.createTextNode(val)
            child.appendChild(finalNode)

    # --- _buildConfdConfig --------------------------------------------------------------------------------------------------
    def _buildConfdConfig(self):
        # read xml file
        dom = parse(self.templateConfFile)
        configElement = dom.getElementsByTagName("confdConfig")[0]
        # write values to the xml
        # directories
        self._setXmlElement(dom, configElement, ["loadPath", "dir"], self.confdFxsDir, True)
        self._setXmlElement(dom, configElement, ["loadPath", "dir"], self.snmpFxsDir, True)
        for iPath in self.fxsLoadPath:
            self._setXmlElement(dom, configElement, ["loadPath", "dir"], iPath, True)
        # TODO (naamas) - remove this statement which disables webui
        self._setXmlElement(dom, configElement, ["webui", "enabled"], "false")
        self._setXmlElement(dom, configElement, ["webui", "docroot"], self.docrootDir)
        self._setXmlElement(dom, configElement, ["loadPath", "dir"], self.fxsDir, True)
        self._setXmlElement(dom, configElement, ["loadPath", "dir"], self.cclDir, True)
        self._setXmlElement(dom, configElement, ["stateDir"], self.stateDir)
        self._setXmlElement(dom, configElement, ["cdb", "dbDir"], self.dbDir)
        self._setXmlElement(dom, configElement, ["cdb", "initPath", "dir"], self.dynamicInitDir, True)
        if self.platformInitDir:
            self._setXmlElement(dom, configElement, ["cdb", "initPath", "dir"], self.platformInitDir, True)
        self._setXmlElement(dom, configElement, ["datastores", "candidate", "filename"], os.path.join(self.candidateDbDir, "candidate.db"))
        self._setXmlElement(dom, configElement, ["cdb", "operational", "dbDir"], self.operDbDir)
        self._setXmlElement(dom, configElement, ["rollback", "directory"], self.rollbackDir)
        self._setXmlElement(dom, configElement, ["logs", "webuiAccessLog", "dir"], self.logsConfdDir)

        if (self.sshEnabled):
            self._setXmlElement(dom, configElement, ["aaa", "sshServerKeyDir"], self.sshKeyDir)
            self._setXmlElement(dom, configElement, ["cli", "ssh", "enabled"], "true")
        else:
            self._setXmlElement(dom, configElement, ["cli", "ssh", "enabled"], "false")

#        self._setXmlElement(dom, configElement, ["notifications", "eventStream", "stream", "builtinReplayStore", "dir"], self.replay)
        # logging
        if self.confdLogEnabled:
            self._setXmlElement(dom, configElement, ["logs", "confdLog", "file", "name"], self.confdLog)
            self._setXmlElement(dom, configElement, ["logs", "confdLog", "enabled"], "true")
        if self.develLogEnabled:
            self._setXmlElement(dom, configElement, ["logs", "developerLog", "file", "name"], self.develLog)
            self._setXmlElement(dom, configElement, ["logs", "developerLog", "enabled"], "true")
        if self.snmpLogEnabled:
            self._setXmlElement(dom, configElement, ["logs", "snmpLog", "file", "name"], self.snmpLog)
            self._setXmlElement(dom, configElement, ["logs", "snmpLog", "enabled"], "true")
        if self.auditLogEnabled:
            self._setXmlElement(dom, configElement, ["logs", "auditLog", "file", "name"], self.auditLog)
            self._setXmlElement(dom, configElement, ["logs", "auditLog", "enabled"], "true")
        if self.binErrorLogEnabled:
            self._setXmlElement(dom, configElement, ["logs", "errorLog", "filename"], self.binErrorLog)
            self._setXmlElement(dom, configElement, ["logs", "errorLog", "enabled"], "true")
            self._setXmlElement(dom, configElement, ["logs", "errorLog", "maxSize"], "S%sM" % self.binErrorLogMaxSizeMB)
        if self.netconfLogEnabled:
            self._setXmlElement(dom, configElement, ["logs", "netconfLog", "file", "name"], self.netconfLog)
            self._setXmlElement(dom, configElement, ["logs", "netconfLog", "enabled"], "true")
        if self.netconfEnabledTraceLog:
            self._setXmlElement(dom, configElement, ["logs", "netconfTraceLog", "enabled"], "true")
            self._setXmlElement(dom, configElement, ["logs", "netconfTraceLog", "filename"], self.netconfTraceLog)
        if self.xpathTraceLogEnabled:
            self._setXmlElement(dom, configElement, ["logs", "xpathTraceLog", "enabled"], "true")
            self._setXmlElement(dom, configElement, ["logs", "xpathTraceLog", "filename"], self.xpathTraceLog)
        
        # log level
        self._setXmlElement(dom, configElement, ["logs", "developerLogLevel"], self.develLogLevel)
        self._setXmlElement(dom, configElement, ["logs", "snmpLogLevel"], self.snmpLogLevel)

        # ports
        self._setXmlElement(dom, configElement, ["confdIpcAddress", "port"], str(self.ipcPort))
        self._setXmlElement(dom, configElement, ["cli", "ssh", "port"], str(self.sshPort))
        self._setXmlElement(dom, configElement, ["snmpAgent", "port"], str(self.snmpPort))
        self._setXmlElement(dom, configElement, ["netconf", "transport", "ssh", "port"], self.netconfSshPort)
        self._setXmlElement(dom, configElement, ["webui", "transport", "tcp", "port"], str(self.webuiPort))

        # addresses
        if (self.mngIp):
            self._setXmlElement(dom, configElement, ["cli", "ssh", "ip"], self.mngIp)
            if self.netconfEnabled:
                self._setXmlElement(dom, configElement, ["netconf", "transport", "ssh", "ip"], self.mngIp)

        if self.mngIp != '0.0.0.0':
            self._setXmlElement(dom, configElement, ["cli", "ssh", "extraIpPorts"], '%s:%s' % ('127.0.0.1', str(self.sshPort)))
            if self.netconfEnabled:
                self._setXmlElement(dom, configElement, ["netconf", "transport", "ssh", "extraIpPorts"], '%s:%s' % ('127.0.0.1', str(self.netconfSshPort)))

        if (self.webuiIp):
            self._setXmlElement(dom, configElement, ["webui", "transport", "tcp", "ip"], self.webuiIp)

        #netconf
        if self.netconfEnabled:
            self._setXmlElement(dom, configElement, ["netconf", "enabled"], "true")
            self._setXmlElement(dom, configElement, ["netconf", "transport", "tcp", "enabled"], "false")
            self._setXmlElement(dom, configElement, ["netconf", "transport", "ssh", "enabled"], "true")

        #restricted file access
        self._setXmlElement(dom, configElement, ["cli", "restrictedFileAccess"], "true")

        #snmpAgent - system
        if self._objId:
            self._setXmlElement(dom, configElement, ["snmpAgent", "system", "sysObjectID"], self._objId)

        sysDescrStr = "Qwilt QwOS Software, QB series software version %s\nCopyright (c) 2010-%s by Qwilt, Inc" % (self._swVersionStr, 2013)
        #TODO (naamas) make build year dynamic instead of hard-coded 2013.
        self._setXmlElement(dom, configElement, ["snmpAgent", "system", "sysDescr"], sysDescrStr)

        # configuration from info file
        try:
            infoFilePath = os.path.join(self.binDir, "info.json")
            infoFile = open(infoFilePath)
            infoDict = json.load(infoFile)
            if "confdConfigurationItems" in infoDict.keys():
                configItems = infoDict["confdConfigurationItems"]
                self.parseAndSetConfigItems(dom, configElement, [], configItems)
            else:
                raise Exception("didn't find confdConfigurationItems")
            infoFile.close()
        except:
            # no info.file exists
            #print "info.json file could not be opened in: %s. skipping." % (infoFilePath)
            pass

        # write updated xml file
        out_file = open(self.runningConfFile, 'w')
        out_file.write(dom.toxml())
        out_file.close()

    def parseAndSetConfigItems (self, dom, configElement, hierarchy, configItemsDict):
        if isinstance(configItemsDict,basestring):
            print "setting element: %s, %s" % (json.dumps(hierarchy), configItemsDict)
            self._setXmlElement(dom, configElement, hierarchy, configItemsDict)
        else:
            for k in configItemsDict:
                if type(configItemsDict) is dict:
                    hierarchy.append(k)
                    self.parseAndSetConfigItems(dom, configElement, hierarchy, configItemsDict[k])
                elif type(configItemsDict) is list:
                    self._setXmlElement(dom, configElement, hierarchy, k, True)
                    print "setting list element: %s, %s" % (json.dumps(hierarchy), k)

    def _createAndAddChildNode (self, dom, parentNode, nodeName, value):
        newNode = dom.createElement(nodeName)
        valNode = dom.createTextNode(value)
        newNode.appendChild(valNode)
        parentNode.appendChild(newNode)

    def _addXmlUser (self, dom, authenticationElement, userName, uid, gid, password, homeDir, sshKeyDir=''):
        userNode = dom.createElement('aaa:user')
        self._createAndAddChildNode(dom, userNode, 'aaa:name', userName)
        self._createAndAddChildNode(dom, userNode, 'aaa:uid', uid)
        self._createAndAddChildNode(dom, userNode, 'aaa:gid', gid)
        self._createAndAddChildNode(dom, userNode, 'aaa:password', password)
        self._createAndAddChildNode(dom, userNode, 'aaa:homedir', homeDir)
        self._createAndAddChildNode(dom, userNode, 'aaa:ssh_keydir', sshKeyDir)
        usersNode = authenticationElement.getElementsByTagName('aaa:users')
        if not usersNode:
            raise Exception('failed to get aaa:users node')
        usersNode[0].appendChild(userNode)

    def _addXmlGroup (self, dom, authenticationElement, groupName, users):
        groupNode = dom.createElement('aaa:group')
        self._createAndAddChildNode(dom, groupNode, 'aaa:name', groupName)
        self._createAndAddChildNode(dom, groupNode, 'aaa:users', ' '.join(users))
        groupsNode = authenticationElement.getElementsByTagName('aaa:groups')
        if not groupsNode:
            raise Exception('failed to get aaa:groups node')
        groupsNode[0].appendChild(groupNode)

    # --- _buildAaaInit --------------------------------------------------------------------------------------------------
    def _buildAaaInit(self):
        # read xml file
        dom = parse(self.templateAaaInitFile)
        authenticationElement = dom.getElementsByTagName("aaa:authentication")[0]
        # write values to the xml
        # users
        uid=str(os.geteuid())
        gid=str(os.getegid())
        self._addXmlUser(dom, authenticationElement, 'admin', uid, gid, 'admin', self.userHomeDir)
        self._addXmlUser(dom, authenticationElement, 'viewer', uid, gid, '$1$disabled-disabled-disable', self.userHomeDir)
        self._addXmlUser(dom, authenticationElement, 'tech', uid, gid, '$1$disabled-disabled-disable', self.userHomeDir)
        # groups
        self._addXmlGroup(dom, authenticationElement, 'admin', ['admin'])
        self._addXmlGroup(dom, authenticationElement, 'tech', ['tech'])
        self._addXmlGroup(dom, authenticationElement, 'viewer', ['viewer'])
        # write updated xml file
        out_file = open(self.runningAaaInitFile, 'w')
        out_file.write(dom.toxml())
        out_file.close()

    # --- _perPlatformInit-----------------------------------------------------------------------------------------------------------
    def _perPlatformInit (self):

        self._createPlatformInitFiles()

        self._configureSnmpAgentSystem()

    # --- _configureSnmpAgentSystem --------------------------------------------------------------------------------------------------
    def _configureSnmpAgentSystem (self):
        if not self.confdConfInitDir:
            return

        jsonFileName = os.path.join(self.confdConfInitDir, 'snmp_agent_system.json')
        jsonFile = open(jsonFileName)
        params = json.load(jsonFile)
        platformOID = params['sysObjectID']
        self._objId = '1.3.6.1.4.1.36418.2.%s' % platformOID

    # --- _createPlatformInitFiles --------------------------------------------------------------------------------------------------
    def _createPlatformInitFiles (self):

        if not self.platformCdbInitDir:
            return

        xmlFilesDir = self.dynamicInitDir

        # remove old platform init files
        oldPlatformInitFiles = glob.glob(os.path.join(xmlFilesDir, "cdb-init-platform-*.xml"))
        for f in oldPlatformInitFiles:
            a.infra.file.utils.removeFile(f, True)

        # create new symlink for interfaces init file
        a.infra.file.utils.symlink(os.path.join(self.platformCdbInitDir, 'interfaces.xml'), os.path.join(self.dynamicInitDir, 'cdb-init-platform-interfaces.xml'))

        print "linking %s to %s" % (os.path.join(self.platformCdbInitDir, 'interfaces.xml'), os.path.join(self.dynamicInitDir, 'cdb-init-platform-interfaces.xml'))

    # --- _buildInterfacesInit --------------------------------------------------------------------------------------------------
    def _buildInterfacesInit(self):

        if self.device is None:
            return 

        # on qm10 platform only
        dummyLogger = a.infra.log.generic_instance.TempJunkDummyLogger()
        ipAddress = DeviceUtils.getIpAddress(dummyLogger, self.device)
        defaultGateway = RoutingUtils.getDefaultGateway(dummyLogger, RoutingUtils.MAIN_TABLE_NAME)

        # read xml file
        dom = parse(self.templateInterfaceInitFile)
        interfaces = dom.getElementsByTagName("interface")

        # i=1
        # write values to the xml
        for ifNode in interfaces:

            # TODO (yoave) - change the way mib-index is calculated
            # TODO (naamas) - change the way mib-index is calculated
            # self._createAndAddChildNode(dom, ifNode, 'mib-index', str(i))
            # i+=1

            ipv4NodeList = ifNode.getElementsByTagName("ipv4")

            if len(ipv4NodeList) == 0:
                # skip interface
                continue

            ipv4Node = ipv4NodeList[0]
            
            # add ip config (if needed)
            addressNode = ipv4Node.getElementsByTagName("address")[0]
            if addressNode.firstChild is None:
                # add default gateway
                self._createAndAddChildNode(dom, ipv4Node, 'default-gateway', defaultGateway)

                # add ip address
                self._createAndAddChildNode(dom, addressNode, 'ip', ipAddress)



        # write updated xml file
        out_file = open(self.runningInterfaceInitFile, 'w')
        out_file.write(dom.toxml())
        out_file.close()

    def getPathesForSupportFile (self):
        toReturn = {}
        toReturn["confd-cdb"]=self.dbDir
        toReturn["confd-candidate-db"]=self.candidateDbDir
        toReturn["confd-oper-db"]=self.operDbDir 
        toReturn["confd-rollback"]=self.rollbackDir 
        return toReturn




