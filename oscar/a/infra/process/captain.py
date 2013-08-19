#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

import logging
import os
import sys
import traceback
import time
from optparse import OptionParser
import a.infra.debug.backtrace
import a.infra.log.get_gpb_workaround
import a.infra.log.main_logger
import a.api.user_log.msg.message_base

if  __package__ is None:
    G_NAME_MODULE_INFRA_PROCESS = "unknown"
    G_NAME_GROUP_INFRA_PROCESS_CAPTAIN = "unknown"
else:
    from . import G_NAME_MODULE_INFRA_PROCESS 
    from . import G_NAME_GROUP_INFRA_PROCESS_CAPTAIN


class Captain(object):
    STOP_SEQUENCE_TYPE_NONE      = 0
    STOP_SEQUENCE_TYPE_STD       = 1
    STOP_SEQUENCE_TYPE_EMERGENCY = 2

    #opt parser
    OPTION_INIT_PARAM_FILES_DIR_STR = "--init-param-files-dir"
    OPTION_PROCESS_NAME = "--process-name"

    INIT_PARAM_FILE_NAME = "process-captain-init-params.json"
    #init params    
    INIT_PARAM_DATA_PROCESS_NAME = "process-name"
    INIT_PARAM_DATA_CONST_DIR_PATH = "const-dir-path"
    INIT_PARAM_DATA_VITAL_PATH = "vital-path"
    INIT_PARAM_DATA_USER_PATH = "user-path"
    INIT_PARAM_DATA_APPLICATIONS_PATH = "applications-path"
    INIT_PARAM_DATA_APPLICATION_SYS_PATH = "application-sys-path"
    INIT_PARAM_DATA_APPLICATION_DATA_PATH = "application-data-path"
    INIT_PARAM_DATA_KICK_NUMBER = "kick-number"
    INIT_PARAM_DATA_APPLICATION_VERSION = "application-version"
    INIT_PARAM_DATA_EXTRA_SLEEP_ON_FATAL = "extra-sleep-on-fatal"
    
    #init param dicts    
    INIT_PARAM_DICT_KEY_PROCESS_CAPTAIN = "process-captain"
    INIT_PARAM_DICT_KEY_MAIN_LOGGER = "main-logger"

    #Path substitution keys
    PATH_SUBSITUTION_KEY_CONST_DIR = "%(const-dir)s"
    PATH_SUBSITUTION_KEY_VITAL_PATH = "%(vital-path)s"
    PATH_SUBSITUTION_KEY_USER_PATH  = "%(user-path)s"
    PATH_SUBSITUTION_KEY_APPLICATIONS_PATH = "%(applications-path)s"
    PATH_SUBSITUTION_KEY_APPLICATION_SYS_PATH = "%(application-sys-path)s"
    PATH_SUBSITUTION_KEY_APPLICTAION_DATA_PATH  = "%(application-data-path)s"

    class ClientEntry:
        def __init__ (self, name, clientObject):
            self.name = name
            self.clientObject = clientObject

    def __init__ (self, processName = None, earlyLogLevel = None, initParamFilesDirEnvVar = None, kickNumber=None): 
        """ctor

        Args:
            earlyLoggerLevel - if not None, change the early logger level to the given value
            initParamFilesDirEnvVar - the env var to read the init params dir from. if set to None the value will be taken from command line

        Raises:
            None
        """       
        self._osef = {}        
        self._clients = [self.ClientEntry("captain", self)] #adding the captain itself as a client for the sake of the derived childs
        self._argv = None 
        self._processName = None
        self._ctorProcessName = processName
        self._earlyLogLevel = earlyLogLevel
        self._initParamFilesDirEnvVar = initParamFilesDirEnvVar
        self._isRelaxedMode = False
        self._isRelaxModeRead = False
        self._kickNumber = None
        self._ctorKickNumber = kickNumber
        self._processId = os.getpid()
        self._activeStopSequenceType = self.STOP_SEQUENCE_TYPE_NONE
        self._constDirPath = None
        self._vitalPath = None
        self._userPath = None
        self._applicationsPath = None
        self._applicationSysPath = None
        self._applicationDataPath = None
        self._applicationVersion = None
        self._extraSleepOnFatal = 0


    def getProcessName (self):
        if self._processName is None:
            a.infra.process.processFatal("Trying to get process name before data was init")
        return str(self._processName)

    def init (self):
        pass

    def _genesis (self):
        if self._earlyLogLevel is None:
            self._main_logger = a.infra.log.main_logger.MainLogger()    
        else:
            self._main_logger = a.infra.log.main_logger.MainLogger(earlyLogLevel = self._earlyLogLevel) 
               
        self._log = self._main_logger.getLoggerManager().createLogger(G_NAME_MODULE_INFRA_PROCESS, G_NAME_GROUP_INFRA_PROCESS_CAPTAIN)
        self._main_logger.initLoggerToUse (self._log)
        if not self._ctorProcessName is None:
            self._initProcessName(self._ctorProcessName)
        if not self._ctorKickNumber is None:
            self._initKickNumber(self._ctorKickNumber)

    def _addClient (self, name, clientObject):
        self._log("add-client").debug1("adding captain client '%s'", name)
        for clientEntry in self._clients:
            if clientEntry.name == name:
                a.infra.process.processFatal("trying to readd captain client '%s'", name)
        newEntry = self.ClientEntry(name, clientObject)
        self._clients += [newEntry]

    def _removeClient (self, name):
        foundEntry = None
        for clientEntry in self._clients:
            if clientEntry.name == name:
                foundEntry = clientEntry
        if foundEntry is None:
            a.infra.process.processFatal("failed to remove captain client '%s' - no such client", name)

        self._log("removing-client").debug1("removing captain client '%s'", name)
        self._clients.remove(foundEntry)
        return
        

    def _replaceClient (self, name, newClientObject, newName = None):
        if newName is None:
            newName = name
        for clientEntry in self._clients:
            if clientEntry.name == name:
                self._log("replacing-client").debug1("replacing captain client '%s' (new name is '%s')", name, newName)
                clientEntry.name = newName
                clientEntry.clientObject = newClientObject
                return
        a.infra.process.processFatal("failed to replace captain client '%s' - no such client", name)

    def _createClients (self):
        self._log("create-clients").debug1("creating captain clients")
        self._main_logger.initCaptain(self)
        self._addClient(self._main_logger.getCaptainClientName(), self._main_logger)        

    def _callOnClients (self, functionName, onExecutionLogLevel = logging.DEBUG2, onNotFoundLogLevel = logging.DEBUG3, **kwargs):
        for clientEntry in self._clients:
            if hasattr(clientEntry.clientObject.__class__, functionName):
                self._log("call-on-client").log(onExecutionLogLevel, "calling function '%s' on client object '%s'", functionName, clientEntry.name)
                getattr(clientEntry.clientObject.__class__, functionName)(clientEntry.clientObject, **kwargs)
            else:
                self._log("call-on-client").log(onNotFoundLogLevel, "client object '%s' has no function named %s", clientEntry.name, functionName)

    def initSimulatedCommnadLine (self, argv):
        self._argv = argv

    def __addToOptParser (self):
        self._optParser = OptionParser()
        self._callOnClients("captainClient_addToOptParser")

    def captainClient_addToOptParser (self):
        if self._initParamFilesDirEnvVar is None:
            self.getOptParser().add_option(self.OPTION_INIT_PARAM_FILES_DIR_STR, type="string",
                                           action="store", dest="initParamFilesDir", 
                                           help="The directory in which we find the init param files")
        if self._processName is None:
            self.getOptParser().add_option(self.OPTION_PROCESS_NAME, type="string",
                                               action="store", dest="processName", 
                                               help="The process name")        

    def getOptParser(self):
        return self._optParser

    def __parseCmdLine (self):       
        if self._argv is None:
            self._argv = sys.argv
        (self._optParseOptions, self._optParseArgs) = self._optParser.parse_args(args = self._argv)
        
        self._log("cmd-line-data").debug2("command line options: '%s'; args:'%s'", self._optParseOptions, self._optParseArgs)
        self._callOnClients("captainClient_parseCmdLine")

    def captainClient_parseCmdLine (self):
        (options, args) = self.getParsedCmd()
        if self._initParamFilesDirEnvVar is None:
            self._initParamFilesDirName = options.initParamFilesDir
        else:
            if not self._initParamFilesDirEnvVar in os.environ:
                a.infra.process.processFatal("Missing env var '%s'", self._initParamFilesDirEnvVar)                
            self._initParamFilesDirName = os.environ[self._initParamFilesDirEnvVar]

        if self._processName is None and hasattr(options, "processName"):            
            self._initProcessName(options.processName)

    def getParsedCmd(self):
        return (self._optParseOptions, self._optParseArgs)

    def getInitParamFilesDirName (self):
        if self._initParamFilesDirName is None:
            a.infra.process.processFatal("Trying to get init param files dir which is None")
        return self._initParamFilesDirName

    def _initProcessName (self, processName):
        self._processName = processName
        if self._processName is not None:
            self._main_logger.setProcessName(self.getProcessName())

    def _initConstDirPath (self, constDirPath):
        self._constDirPath = constDirPath

    def _initVitalPath (self, vitalPath):
        self._vitalPath = vitalPath

    def _initUserPath (self, userPath):
        self._userPath = userPath

    def _initApplicationsPath (self, applicationsPath):
        self._applicationsPath = applicationsPath

    def _initApplicationSysPath (self, applicationSysPath):
        self._applicationSysPath = applicationSysPath

    def _initApplicationDataPath (self, applicationDataPath):
        self._applicationDataPath = applicationDataPath

    def _initApplicationVersion (self, applicationVersion):
        self._applicationVersion = applicationVersion

    def _initKickNumber (self, kickNumber):
        self._kickNumber = kickNumber

    def __addToOsef (self):
        self._log("add-to-osef").debug1("start adding to osef")
        self._callOnClients("captainClient_addToOsef")

    def captainClient_addToOsef (self):
        pass

    def _clientsGetFromOsef (self):
        self._log("get-from-osef").debug1("start getting elements from osef")
        self._callOnClients("captainClient_getFromOsef")

    def captainClient_getFromOsef (self):
        pass

    def _initFromParamFiles (self):
        self._log("init-from-param-files").notice("start init from param files")
        self._callOnClients("captainClient_initFromParamFile")

    def captainClient_initFromParamFile (self):
        initParamData = {}
        initParamFileName = os.path.join(self.getInitParamFilesDirName(), self.INIT_PARAM_FILE_NAME)
        if os.path.exists(initParamFileName):
            initParamData = a.infra.format.json.readFromFile(self._log, initParamFileName)
        self._captainClient_initFromParamFile(initParamData)

    def _captainClient_initFromParamFile (self, initParamData):
        if self._processName is None:
            if not self.INIT_PARAM_DATA_PROCESS_NAME in initParamData:
                a.infra.process.processFatal("Missing process name")       
            self._initProcessName(initParamData[self.INIT_PARAM_DATA_PROCESS_NAME])  

        if self._constDirPath is None:
            if self.INIT_PARAM_DATA_CONST_DIR_PATH in initParamData:
                self._initConstDirPath(initParamData[self.INIT_PARAM_DATA_CONST_DIR_PATH])

        if self._vitalPath is None:
            if self.INIT_PARAM_DATA_VITAL_PATH in initParamData:
                self._initVitalPath(initParamData[self.INIT_PARAM_DATA_VITAL_PATH])

        if self._userPath is None:
            if self.INIT_PARAM_DATA_USER_PATH in initParamData:
                self._initUserPath(initParamData[self.INIT_PARAM_DATA_USER_PATH])

        if self._applicationsPath is None:
            if self.INIT_PARAM_DATA_APPLICATIONS_PATH in initParamData:
                self._initApplicationsPath(initParamData[self.INIT_PARAM_DATA_APPLICATIONS_PATH])

        if self._applicationSysPath is None:
            if self.INIT_PARAM_DATA_APPLICATION_SYS_PATH in initParamData:
                self._initApplicationSysPath(initParamData[self.INIT_PARAM_DATA_APPLICATION_SYS_PATH])

        if self._applicationDataPath is None:
            if self.INIT_PARAM_DATA_APPLICATION_DATA_PATH in initParamData:
                self._initApplicationDataPath(initParamData[self.INIT_PARAM_DATA_APPLICATION_DATA_PATH])

        if self._applicationVersion is None:
            if self.INIT_PARAM_DATA_APPLICATION_VERSION in initParamData:
                self._initApplicationVersion(initParamData[self.INIT_PARAM_DATA_APPLICATION_VERSION])

        if self._kickNumber is None:            
            if self.INIT_PARAM_DATA_KICK_NUMBER in initParamData:
                self._initKickNumber(initParamData[self.INIT_PARAM_DATA_KICK_NUMBER])                        
            else:
                self._initKickNumber(0)#backward compatibility for install operations

        if self.INIT_PARAM_DATA_EXTRA_SLEEP_ON_FATAL in initParamData:
            self._extraSleepOnFatal = initParamData[self.INIT_PARAM_DATA_EXTRA_SLEEP_ON_FATAL]

    def __setProcessName (self):
        self._callOnClients("captainClient_setProcessName")        

    def captainClient_setProcessName (self):
        pass

    def getIsRelaxMode (self):
        self._isRelaxModeRead = True
        return self._isRelaxedMode

    def getKickNumber (self):
        if self._kickNumber is None:
            a.infra.process.processFatal("No kick number set yet")       
        return self._kickNumber

    def getPlatformBasicData (self):   
        """
        get the platform basic data class.
        Return None if unknown
        """         
        self._log("unsupported").error("trying to get the platform basic data from a none supporting captain")
        return None

    def setIsRelaxMode (self, isRelaxMode):
        if self._isRelaxModeRead:
            #currently assuming "relax mode" value must not changed - so if someone already read it and kept the value it will be protected
            #if this command is called in a to early stage we will crash... I dont care - it is a launch time error 
            self._log("relax-mode-already-read").error("trying to set the relaxed mode to '%s' after the prev value was already read", isRelaxMode)
            return
        self._isRelaxedMode = isRelaxMode    
               
    def earlyInit (self):
        self._genesis()
        self._createClients()
        self.__addToOptParser()        
        self.__parseCmdLine()
        self.__addToOsef()
        self._clientsGetFromOsef()
        self._initFromParamFiles()
        self.__setProcessName()
        self._callOnClients("captainClient_infraEarlyInit")

    def captainClient_infraEarlyInit (self):
        pass

    def dormant2Passive (self):
        self._log("dormant-to-passive").notice("moving from state dormant to state passive")
        self._callOnClients("captainClient_dormant2Passive")

    def captainClient_dormant2Passive (self):
        pass

    def passive2Active (self):
        self._log("passive-to-active").notice("moving from state passive to state active")
        self._callOnClients("captainClient_passive2Active")

    def captainClient_passive2Active (self):
        pass

    def active2Up (self):
        self._log("active-to-up").notice("moving from state active to state up")
        self._callOnClients("captainClient_active2Up")

    def captainClient_active2Up (self):
        pass

    def up2Active (self):
        self._log("up-to-active").notice("moving from state up to state active")
        self.promoteStopSequenceType(self.STOP_SEQUENCE_TYPE_STD)#for the case the application is done 
                                                                 #and not exited due to a signal
        self._callOnClients("captainClient_up2Active")

    def captainClient_up2Active (self):
        pass

    def active2Passive (self):
        self._log("active-to-passive").notice("moving from state active to state passive")
        self._callOnClients("captainClient_active2Passive")

    def captainClient_active2Passive (self):
        pass

    def passive2Dormant (self):
        self._log("passive-to-dormant").notice("moving from state passive to state dormant")
        self._callOnClients("captainClient_passive2Dormant")

    def captainClient_passive2Dormant (self):
        pass

    def lateShutdown (self):
        self._log("late-shudown").notice("late shutdown is called")
        self._callOnClients("captainClient_lateShutdown")

    def captainClient_lateShutdown (self):
        pass

    def fullStart (self):
        self.dormant2Passive()
        self.passive2Active()
        self.active2Up()

    def fullStop (self):
        self.up2Active()
        self.active2Passive()
        self.passive2Dormant()

    def checkOk (self):
        self._log("check-ok").debug4("chacking the state of the different clients")
        self._callOnClients("captainClient_checkOk",  onExecutionLogLevel = logging.DEBUG4, onNotFoundLogLevel = logging.DEBUG5)

    def captainClient_checkOk (self):
        pass

    def getOsef (self):
        return self._osef   

    def getActiveStopSequenceType (self):
        return self._activeStopSequenceType

    def getWasStopped (self):
        self._log("stop-test").debug4("stop test: %s", self._getStopSequenceTypeName(self._activeStopSequenceType))
        return self._activeStopSequenceType != self.STOP_SEQUENCE_TYPE_NONE


    def promoteStopSequenceType (self, stopSequenceType):        
        beforeValue = self._activeStopSequenceType
        if stopSequenceType > beforeValue:
            #while for multi threading
            while stopSequenceType > self._activeStopSequenceType:
                self._activeStopSequenceType = stopSequenceType

            #####This function is also called from a context of signal handling. 
            #just set the stop flag or you will get into deep shit
            try:
                self._log("stop-sequence").notice("stop sequence type modified: %s ==> %s (final value: %s)",
                                                  self._getStopSequenceTypeName(beforeValue),
                                                  self._getStopSequenceTypeName(stopSequenceType),
                                                  self._getStopSequenceTypeName(self._activeStopSequenceType))
            except:
                pass

    def _getStopSequenceTypeName (self, stopSequenceTypeName):
        try:
            return {self.STOP_SEQUENCE_TYPE_NONE: "none",
                    self.STOP_SEQUENCE_TYPE_STD : "std",
                    self.STOP_SEQUENCE_TYPE_EMERGENCY: "emergency"}[stopSequenceTypeName]
        except:
            return "Invalid"

    def stopRequest (self):
        self.promoteStopSequenceType(self.STOP_SEQUENCE_TYPE_STD)
        self.__backtraceAllThreads(True, False)

    def processFatal (self, msg, *args):
        """create a fatal message        
        If the message is created from a context of an exception
        Args:
            msg - a string, possibly containing arguments place holders (e.g "%s")
                       

        Returns:
            the data previously written

        Raises:
            same as "readFromFile" funcition            
        """
        try:
            fatalMessage = (msg % args)
        except:
            #we have a problem in the msg creation - recovering the best way we can
            fatalMessage = "msg: %s; args: %s".format(msg, args)
        print >> sys.stderr, fatalMessage

        try:
            traceback.print_stack()
        except:
            print >> sys.stderr, "Failed to extrace stack trace"

        try:
            self._log("fatal")._fatal(msg, *args, **{'exc_info': 1, "stackFrames": sys.maxint})
            self.__backtraceAllThreads(True, True)
        except:
            pass

        if self._extraSleepOnFatal != 0:
            try:
                self._log("sleep-on-fata")._fatal("Fatal: sleeping for '%s' seconds before rising the flag due to configuration", 
                                                  self._extraSleepOnFatal)
            except:
                pass
            time.sleep(self._extraSleepOnFatal)

        self.promoteStopSequenceType(self.STOP_SEQUENCE_TYPE_EMERGENCY)

        exitCode = 1
        exitThreadSleepTime = 2

        time.sleep(exitThreadSleepTime)

        try:
            self._log("fatal-os-exit")._fatal("Fatal: calling os._exit. return code = %s", exitCode)
        except:
            print >> sys.stderr, "Fatal: calling os._exit. return code = %s"%exitCode
        os._exit(exitCode)

    def getProcessId (self):
        return self._processId


    def logUserMessage (self, userLogMessage):
        """create a user log message
        """
        (isValid, msgText) = self._verifyUserMessage(userLogMessage)
        if not isValid:
            return

        self._log("no-user-log-service-support").error("trying to log user message with no existing user log service supported:  %s-%s-%s-%s: %s",
                                                       userLogMessage.category, userLogMessage.group, userLogMessage.severity, 
                                                       userLogMessage.code, msgText)

    def substitueSystemKnownPaths (self, pathPattern):
        finalPath = pathPattern

        if self.PATH_SUBSITUTION_KEY_CONST_DIR in finalPath:
            if self._constDirPath is None:
                self._log("no-const-dir").error("trying to set const dir in pattern '%s' while const-dir is unknown. orig path pattern: '%s'",
                                                finalPath, pathPattern)
                return None
            finalPath = finalPath.replace(self.PATH_SUBSITUTION_KEY_CONST_DIR, self._constDirPath)

        if self.PATH_SUBSITUTION_KEY_VITAL_PATH in finalPath:
            if self._vitalPath is None:
                self._log("no-vital-dir").error("trying to set vital path in pattern '%s' while vital-path is unknown. orig path pattern: '%s'",
                                                finalPath, pathPattern)
                return None
            finalPath = finalPath.replace(self.PATH_SUBSITUTION_KEY_VITAL_PATH, self._vitalPath)

        if self.PATH_SUBSITUTION_KEY_USER_PATH in finalPath:
            if self._userPath is None:
                self._log("no-user-dir").error("trying to set user path in pattern '%s' while user-path is unknown. orig path pattern: '%s'",
                                                finalPath, pathPattern)
                return None
            finalPath = finalPath.replace(self.PATH_SUBSITUTION_KEY_USER_PATH, self._userPath)

        if self.PATH_SUBSITUTION_KEY_APPLICATIONS_PATH in finalPath:
            if self._applicationsPath is None:
                self._log("no-applications-dir").error("trying to set applications path in pattern '%s' while applications-path is unknown. orig path pattern: '%s'",
                                                finalPath, pathPattern)
                return None
            finalPath = finalPath.replace(self.PATH_SUBSITUTION_KEY_APPLICATIONS_PATH, self._applicationsPath)

        if self.PATH_SUBSITUTION_KEY_APPLICATION_SYS_PATH in finalPath:
            if self._applicationSysPath is None:
                self._log("no-sys-dir").error("trying to set sys path in pattern '%s' while sys path is unknown. orig path pattern: '%s'",
                                                finalPath, pathPattern)
                return None
            finalPath = finalPath.replace(self.PATH_SUBSITUTION_KEY_APPLICATION_SYS_PATH, self._applicationSysPath)

        if self.PATH_SUBSITUTION_KEY_APPLICTAION_DATA_PATH in finalPath:
            if self._applicationDataPath is None:
                self._log("no-data-dir").error("trying to set data path in pattern '%s' while data path is unknown. orig path pattern: '%s'",
                                                finalPath, pathPattern)
                return None
            finalPath = finalPath.replace(self.PATH_SUBSITUTION_KEY_APPLICTAION_DATA_PATH, self._applicationDataPath)

        return finalPath

    def getApplicationVersion (self):
        return self._applicationVersion

    def _verifyUserMessage (self, userLogMessage):
        if not isinstance(userLogMessage, a.api.user_log.msg.message_base.MessageBase):
            self._log("invalid-log-object").error("trying to log user message with an invalid object: %s", userLogMessage)
            return (False, "")

        try:
            if len(userLogMessage.args) > 0:
                msgText = userLogMessage.text % userLogMessage.args
            else:
                msgText = userLogMessage.text
        except:
            self._log("failed-parse-log").exception("trying to log user message - failed to create message string. %s-%s-%s-%s: %s",
                                                    userLogMessage.category, userLogMessage.group, userLogMessage.severity, 
                                                    userLogMessage.code, userLogMessage.msg, str(userLogMessage.args))
            return (False, "")

        return (True, msgText)


    def __backtraceAllThreads (self, toLog, toStderr):
        for threadId, stack in sys._current_frames().items():
            try:

                backtrace = a.infra.debug.backtrace.Backtrace()
                backtrace.initFromPythonFrame(stack, currentFrameIndex=0,
                                              maxFrameIndex=sys.maxint, 
                                              maxFrameIndexIncludingArgs=sys.maxint)
                try:
                    if toLog:
                        self._log("stack-trace").notice("Collected backtrace: from thread id %s",threadId, 
                                                        decodedBacktrace=backtrace)
                except:
                    print >> sys.stderr, "failed sending thread %s stack trace to the log"%threadId
    
                if toStderr:
                    print >> sys.stderr,"\n# ThreadID: %s" % threadId
                    frameIndex = 0
                    for frame in backtrace.getFrames():
                        print >> sys.stderr, "ST:[%02d]:%s#%s(%s:%s:%s)"%(frameIndex-backtrace.getCurrentFrameIndex(),frame.fileName, frame.lineNum, frame.pyModuleName, frame.className, frame.function)
                        frameIndex +=1

            except:
                print >> sys.stderr, "failed to collect thread %s stack trace"%threadId




    @classmethod
    def s_infraCaptainCreateInitParamFiles(cls, dbglog, initParamFilesDir, dataDictionary):
        a.infra.format.json.writeToFile(dbglog, dataDictionary[cls.INIT_PARAM_DICT_KEY_PROCESS_CAPTAIN], os.path.join(initParamFilesDir, cls.INIT_PARAM_FILE_NAME), indent=4)
        a.infra.log.main_logger.MainLogger.s_createInitParamFile(dbglog, initParamFilesDir, dataDictionary[cls.INIT_PARAM_DICT_KEY_MAIN_LOGGER])


