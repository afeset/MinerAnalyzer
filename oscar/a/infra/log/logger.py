# 
# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: nirs

if  __package__ is None:
    G_NAME_MODULE_LOG = "unknown"
    G_NAME_GROUP_LOG_LOGGER_MANAGER = "unknown"
else:
    from . import G_NAME_MODULE_LOG
    from . import G_NAME_GROUP_LOG_LOGGER_MANAGER

import logging
import types
import sys
import os
import string
import time
import threading
import datetime
import json
import copy
import a.infra.process
import a.infra.debug.backtrace

#####
#code needs to be run when importing this module
logging.NOTICE = 25
logging.addLevelName(logging.NOTICE, "NOTICE")
logging.DEBUG1 = logging.DEBUG
logging.addLevelName(logging.DEBUG1, "DEBUG1")
logging.DEBUG2 = logging.DEBUG1-1
logging.addLevelName(logging.DEBUG2, "DEBUG2")
logging.DEBUG3 = logging.DEBUG2-1
logging.addLevelName(logging.DEBUG3, "DEBUG3")
logging.DEBUG4 = logging.DEBUG3-1
logging.addLevelName(logging.DEBUG4, "DEBUG4")
logging.DEBUG5 = logging.DEBUG4-1
logging.addLevelName(logging.DEBUG5, "DEBUG5")


G_RECORD_KEY_MSG_MODULE = "msg_module"
G_RECORD_KEY_MSG_GROUP = "msg_group"
G_RECORD_KEY_MSG_NAME = "msg_name"
G_RECORD_KEY_INSTANCE = "instance"
G_RECORD_KEY_PROCESS_NAME = "process_name"
G_RECORD_KEY_PROCESS_ID = "process_id"
G_RECORD_KEY_EXTRA_PROPERTIES = "extra_properties"
G_RECORD_KEY_STACK_TRACE = "stack_trace"
G_RECORD_KEY_CLASS = "class"
G_RECORD_KEY_PY_MODULE = "py_module"
G_RECORD_KEY_GLOBAL_SEQUENCE_NUMBER = "global_sequence_number"
G_RECORD_KEY_MSG_ID_SEQUENCE_NUMBER = "msg_id_sequence_number"
G_RECORD_KEY_KICK_NUMBER = "kick_number"
G_RECORD_KEY_ERRNO = "errno"
G_RECORD_KEY_PLAIN_TEXT_BUFFERS = "plain_text_buffers"
G_RECORD_KEY_JSON_TEXT_BUFFERS = "json_text_buffers"
G_RECORD_KEY_BINARY_BUFFERS = "binary_buffers"
G_RECORD_KEY_GPBS = "gpbs"
G_RECORD_KEY_DECODED_BACKTRACES = "decoded_backtraces"


##################################################################
#code copied from Python logging.Logger
#From my laptop:
#Python 2.6.5 (r265:79096, Mar 19 2010, 21:48:26) [MSC v.1500 32 bit (Intel)] on win32

#
# _srcfile is used when walking the stack to check when we've got the first
# caller stack frame.
#
if hasattr(sys, 'frozen'): #support for py2exe
    _srcfile = "logging%s__init__%s" % (os.sep, __file__[-4:])
elif string.lower(__file__[-4:]) in ['.pyc', '.pyo']:
    _srcfile = __file__[:-4] + '.py'
else:
    _srcfile = __file__
_srcfile = os.path.normcase(_srcfile)

# next bit filched from 1.5.2's inspect.py
def currentframe():
    """Return the frame object for the caller's stack frame."""
    try:
        raise Exception
    except:
        return sys.exc_traceback.tb_frame.f_back

if hasattr(sys, '_getframe'): currentframe = lambda: sys._getframe(3)
# done filching

#end of copied code
##################################################################

class MsgAttributes:#level is not a part from the entry - many messages can be created with the same ID but different levels - we don't block it
    def __init__(self, msgModule, msgGroup, msgName, instance, extraProperties, 
                 isForceStackTrace, isForceExceptionData, someRateLimitData):
        self.msgModule=msgModule
        self.msgGroup=msgGroup
        self.msgName=msgName
        self.instance=instance
        self.extraProperties=extraProperties
        self.isForceStackTrace=isForceStackTrace
        self.isForceExceptionData=isForceExceptionData
        self.someRateLimitData=someRateLimitData

class MsgData:
    def __init__(self, level, msg, args, exc_info, extra, 
                 stackFrames, 
                 text, textList, textDict,
                 toJson, toJsonList, toJsonDict,                 
                 binary, binaryList, binaryDict, 
                 gpb, gpbList, gpbDict, gpbs,
                 decodedBacktrace, decodedBacktraceList, decodedBacktraceDict):
        self.level=level
        self.msg=msg
        self.args=args
        self.stackFrames = stackFrames
        self.exc_info=exc_info
        if extra is not None:
            self.user_extra=extra
        else:
            self.user_extra={}


        self.texts = self._createJointList(text, textList, textDict, None, "text", str)

        def objToJson (data):
            try:
                return json.dumps(data, indent=4, sort_keys=True)
            except:
                return None
        self.jsons = self._createJointList(toJson, toJsonList, toJsonDict, None, "json", objToJson)

        self.binaries = self._createJointList(binary, binaryList, binaryDict, None, "binary", str)

        self.gpbs = self._createJointList(gpb, gpbList, gpbDict, gpbs, "gpb", lambda x: x)

        self.decodedBacktraces = self._createJointList(decodedBacktrace, decodedBacktraceList, decodedBacktraceDict, None, "decoded-backtrace", lambda x: x)

    def _createJointList (self, singleItem, itemsList, itemsDict, unknownStructureForLegacy, basicKey, manipulatingFunction):
        items = []
        if singleItem is not None:
            items.append((basicKey, manipulatingFunction(singleItem)))

        if itemsList is not None:
            if isinstance(itemsList, list):
                try:
                    for i in xrange(len(itemsList)):
                        items.append(("%s%d"%(basicKey,i), manipulatingFunction(itemsList[i])))
                except:
                    items.append(("invalid-%s-list"%basicKey, None))
            else:
                items.append(("invalid-%s-list(%s)"%(basicKey,type(itemsList)), None))


        if itemsDict is not None:
            if isinstance(itemsDict, dict):
                try:
                    for item in sorted(itemsDict):
                        items.append((item, manipulatingFunction(itemsDict[item])))
                except:
                    items.append(("invalid-%s-dict"%basicKey, None))
            else:
                items.append(("invalid-%s-dict(%s)"%(basicKey,type(itemsDict)), None))

        if unknownStructureForLegacy:
            #taking care of gpbs list
            if isinstance(unknownStructureForLegacy, list):
                tempDict = {}
                for i in xrange(len(unknownStructureForLegacy)):
                    tempDict["%s%d"%(basicKey,i)] = unknownStructureForLegacy[i]
                unknownStructureForLegacy = tempDict

            #taking care of a single gpb
            if not isinstance(unknownStructureForLegacy, dict):
                unknownStructureForLegacy={basicKey:unknownStructureForLegacy}

            try:
                for item in sorted(unknownStructureForLegacy):
                    items.append((item, manipulatingFunction(unknownStructureForLegacy[item])))
            except:
                items.append(("%ss"%basicKey, "N/A"))

        return items



class MsgSender(object):
    def __init__(self, coreLogger, msgAttributes):
        self._coreLogger=coreLogger
        self._msgAttributes=msgAttributes
        
    def log (self, level, msg, *args, **kwargs):
        self._log(False, level, msg, args, **kwargs)

    def debug5 (self, msg, *args, **kwargs):
        self._log(False, logging.DEBUG5, msg, args, **kwargs)

    def debug4 (self, msg, *args, **kwargs):
        self._log(False, logging.DEBUG4, msg, args, **kwargs)

    def debug3 (self, msg, *args, **kwargs):
        self._log(False, logging.DEBUG3, msg, args, **kwargs)

    def debug2 (self, msg, *args, **kwargs):
        self._log(False, logging.DEBUG2, msg, args, **kwargs)

    def debug1 (self, msg, *args, **kwargs):
        self._log(False, logging.DEBUG1, msg, args, **kwargs)

    debug = debug1

    def info (self, msg, *args, **kwargs):
        self._log(False, logging.INFO, msg, args, **kwargs)

    def notice (self, msg, *args, **kwargs):
        self._log(False, logging.NOTICE, msg, args, **kwargs)

    def warning (self, msg, *args, **kwargs):
        self._log(False, logging.WARNING, msg, args, **kwargs)

    def error (self, msg, *args, **kwargs):
        self._log(False, logging.ERROR, msg, args, **kwargs)

    def exception(self, msg, *args, **kwargs):
        """
        Convenience method for logging an ERROR with exception information.
        """
        self._log(False, logging.ERROR, msg, args, **self._joinDicts({'exc_info': 1}, kwargs))

    def _critical (self, msg, *args, **kwargs):
        self._log(False, logging.CRITICAL, msg, args, **kwargs)

    _fatal = _critical


    def _logFunc (self, level, kwargs):
        if (not self._coreLogger._hasCfg) and (level < self._coreLogger._defaultLogLevel):
            return []

        if not self._coreLogger._shallCreateMsg(self._msgAttributes, level, True):
            return []

        def _forceLog (msg, *args, **kwargs1):
            self._log(True, level, msg, args, **self._joinDicts(kwargs, kwargs1))

        return [_forceLog]

    def logFunc (self, level, **kwargs):
        return self._logFunc(level, kwargs)

    def debug5Func (self, **kwargs):
        return self._logFunc(logging.DEBUG5, kwargs)

    def debug4Func (self, **kwargs):
        return self._logFunc(logging.DEBUG4, kwargs)

    def debug3Func (self, **kwargs):
        return self._logFunc(logging.DEBUG3, kwargs)

    def debug2Func (self, **kwargs):
        return self._logFunc(logging.DEBUG2, kwargs)

    def debug1Func (self, **kwargs):
        return self._logFunc(logging.DEBUG1, kwargs)

    debugFunc = debug1Func

    def infoFunc (self, **kwargs):
        return self._logFunc(logging.INFO, kwargs)

    def noticeFunc (self, **kwargs):
        return self._logFunc(logging.NOTICE, kwargs)

    def warningFunc (self, **kwargs):
        return self._logFunc(logging.WARNING, kwargs)

    def errorFunc (self, **kwargs):
        return self._logFunc(logging.ERROR, kwargs)

    def exceptionFunc (self, **kwargs):
        return self._logFunc(logging.ERROR, self._joinDicts({'exc_info': 1}, kwargs))

    def _criticalFunc (self, **kwargs):
        return self._logFunc(logging.CRITICAL, kwargs)

    _fatalFunc = _criticalFunc


    #TODO(nirs) create all functions that appears on LoggerAdapter
    def _log(self, force, level, msg, args, exc_info=None, extra=None,
             stackFrames=None,#None=default behavior. any number override default behavior
             text=None, textList=None, textDict=None,
             json=None, jsonList=None, jsonDict=None, 
             binary=None, binaryList=None, binaryDict=None, 
             gpb=None, gpbList=None, gpbDict=None, gpbs=None,
             decodedBacktrace=None, decodedBacktraceList=None, decodedBacktraceDict=None):
        __pychecker__="maxargs=30"
        try:
            if (not force) and (not self._coreLogger._hasCfg) and (level < self._coreLogger._defaultLogLevel):
                #quick fast test
                return
        
            self._logImpl(force, level, msg, args, exc_info, extra, 
                          stackFrames=stackFrames, 
                          text=text, textList=textList, textDict=textDict,
                          toJson=json, toJsonList=jsonList, toJsonDict=jsonDict,                 
                          binary=binary, binaryList=binaryList, binaryDict=binaryDict, 
                          gpb=gpb, gpbList=gpbList, gpbDict=gpbDict, gpbs=gpbs,
                          decodedBacktrace=decodedBacktrace, decodedBacktraceList=decodedBacktraceList, decodedBacktraceDict=decodedBacktraceDict)
        except:
            try:
                self._logImpl(force, level, "logger failed to create message", (), exc_info = sys.exc_info())
            except:
                logging.exception("Logger encountered unexpected error")

        
    def _logImpl(self, force, level, msg, args, exc_info=None, extra=None, 
                 stackFrames=None,
                 text=None, textList=None, textDict=None,
                 toJson=None, toJsonList=None, toJsonDict=None, 
                 binary=None, binaryList=None, binaryDict=None, 
                 gpb=None, gpbList=None, gpbDict=None, gpbs=None,
                 decodedBacktrace=None, decodedBacktraceList=None, decodedBacktraceDict=None):
        __pychecker__="maxargs=30"
        msgData = MsgData(level, msg, args, exc_info, extra, 
                          stackFrames=stackFrames,
                          text=text, textList=textList, textDict=textDict,
                          toJson=toJson, toJsonList=toJsonList, toJsonDict=toJsonDict,                 
                          binary=binary, binaryList=binaryList, binaryDict=binaryDict, 
                          gpb=gpb, gpbList=gpbList, gpbDict=gpbDict, gpbs=gpbs,
                          decodedBacktrace=decodedBacktrace, decodedBacktraceList=decodedBacktraceList, decodedBacktraceDict=decodedBacktraceDict)

        if (not force) and (not self._coreLogger._shallCreateMsg(self._msgAttributes, level, False)):
            return
        self._coreLogger._send(self._msgAttributes, msgData)

    def __getattr__(self, attr):
        #catching invalid functions call
        def nothing (*args, **kwargs):
            pass
        return nothing
        #TODO(nirs) warning

    def _joinDicts (self, dictA, dictB):
        __pychecker__="no-argsused"
        return dict(dictA.items() + dictB.items())

class CoreLogger(object):
    _STATISTICS_KEY_SENT = "sent"
    _STATISTICS_KEY_FILTERED = "filtered"
    def __init__(self, name, processName, defaultLogLevel):
        self._stdPyLogger = logging.Logger(name,logging.NOTSET)#Calling the ctor and not "logging.getLogger"-->this logger is not a son of the root logger
                                                              #setting the log level to the minimum - we will control it ourself
              
        self._processName = processName
        self._defaultLogLevel = defaultLogLevel        
        self._globalMsgCounter = 0
        self._collectKickNumber = False
        self._perMsgCounter = {}
        self._countersLock = threading.Lock()
        self._configurationLock = threading.Lock()

        self._clearCfg(hasCfgFlagValue = False)
        self._msgsStatistics = {}

    def setProcessName (self, processName):
        self._processName = processName

    def findCallerExtended(self, maxFrameIndex, maxFrameWithArgsIndex):     
        """
        Find the stack frame of the caller so that we can note the source
        file name, line number and function name.
        """

        backtrace = a.infra.debug.backtrace.Backtrace()
        try:
            f = currentframe()
            #On some versions of IronPython, currentframe() returns None if
            #IronPython isn't run with -X:Frames.
            if f is not None:
                f = f.f_back        

            #looking for the right frame to start with
            while hasattr(f, "f_code"):
                co = f.f_code
                filename = os.path.normcase(co.co_filename)
                if _srcfile.endswith(filename):            
                    f = f.f_back
                    continue
                break

            backtrace.initFromPythonFrame(f, currentFrameIndex=0,
                                          maxFrameIndex=maxFrameIndex, 
                                          maxFrameIndexIncludingArgs=maxFrameWithArgsIndex)
        except:
            pass# in case of error we use what we have

        if backtrace.getFrames() == [] or (len(backtrace.getFrames()) <= backtrace.getCurrentFrameIndex()): #we must have the current frame for caller data
            print backtrace.getFrames()
            collectedFrame = a.infra.debug.backtrace.Frame(fileName="(unknown file)", 
                                                           lineNum=0, 
                                                           pyModuleName="(unknown module)", 
                                                           className="(unknown class)", 
                                                           function="(unknown function)", 
                                                           argsList=[])
            backtrace.initByFrame(collectedFrame)
        return backtrace


    def _send(self, msgAttributes, msgData):

        extra = dict(msgAttributes.extraProperties.items()) 
        extra[G_RECORD_KEY_EXTRA_PROPERTIES] = msgAttributes.extraProperties #putting it also for keeping in GPBs
        extra[G_RECORD_KEY_MSG_MODULE]=msgAttributes.msgModule
        extra[G_RECORD_KEY_MSG_GROUP]=msgAttributes.msgGroup
        extra[G_RECORD_KEY_MSG_NAME]=msgAttributes.msgName
        extra[G_RECORD_KEY_INSTANCE]=msgAttributes.instance
        extra[G_RECORD_KEY_PROCESS_NAME]=self._processName
        extra[G_RECORD_KEY_PROCESS_ID]=a.infra.process.getProcessId()

        #if the message is marked to take an exception, we collect it here before other exceptions can be thrown                                                         
        extra[G_RECORD_KEY_ERRNO]=0              
        if msgData.exc_info:
            if type(msgData.exc_info) != types.TupleType:
                msgData.exc_info = sys.exc_info()
            if hasattr(msgData.exc_info[1], "errno"):                                                     
                try:                                                                              
                    extra[G_RECORD_KEY_ERRNO]=int(msgData.exc_info[1].errno)                              
                except:                                                                           
                    pass                                                                          

        collectStackTrace = msgAttributes.isForceStackTrace or msgData.level >= logging.ERROR
        maxFrameIndex = 0#standard trace
        maxFrameWithArgsIndex = -1
        if collectStackTrace:
            maxFrameIndex = sys.maxint
            maxFrameWithArgsIndex = 0
        if msgData.stackFrames is not None:#override default decision
            maxFrameWithArgsIndex = msgData.stackFrames-1
            if maxFrameWithArgsIndex >= 0:
                collectStackTrace = True


        backtrace = self.findCallerExtended(maxFrameIndex, maxFrameWithArgsIndex)
        callingFrame = backtrace.getFrames()[backtrace.getCurrentFrameIndex()]

        fn            = callingFrame.fileName
        lno           = callingFrame.lineNum
        func          = callingFrame.function
        className     = callingFrame.className
        pyModuleName  = callingFrame.pyModuleName

        extra[G_RECORD_KEY_STACK_TRACE]=None
        if collectStackTrace:
            extra[G_RECORD_KEY_STACK_TRACE]=backtrace

        extra[G_RECORD_KEY_CLASS]=className
        extra[G_RECORD_KEY_PY_MODULE]=pyModuleName
        msgIdKey="%s.%s.%s"%(msgAttributes.msgModule,msgAttributes.msgGroup,msgAttributes.msgName)        

        with self._countersLock:
            if not msgIdKey in self._perMsgCounter:
                self._perMsgCounter[msgIdKey] = 0
            extra[G_RECORD_KEY_MSG_ID_SEQUENCE_NUMBER]=self._perMsgCounter[msgIdKey]
            self._perMsgCounter[msgIdKey] += 1
            extra[G_RECORD_KEY_GLOBAL_SEQUENCE_NUMBER]=self._globalMsgCounter
            self._globalMsgCounter += 1

        if self._collectKickNumber:
            extra[G_RECORD_KEY_KICK_NUMBER]=a.infra.process.getKickNumber()

        #data prepare for record creation
        level    = msgData.level
        msg      = msgData.msg
        args     = msgData.args
        exc_info = msgData.exc_info  
        extra[G_RECORD_KEY_PLAIN_TEXT_BUFFERS] = msgData.texts
        extra[G_RECORD_KEY_JSON_TEXT_BUFFERS] = msgData.jsons
        extra[G_RECORD_KEY_BINARY_BUFFERS] = msgData.binaries
        extra[G_RECORD_KEY_GPBS] = msgData.gpbs
        extra[G_RECORD_KEY_DECODED_BACKTRACES] = msgData.decodedBacktraces
        extra    = dict(extra.items() + msgData.user_extra.items()) #merging user_extra with extra.user_extra my override our data

        try:
            if len(args) > 0:
                dummy = msg % args
        except:
            excepted = sys.exc_info()
            #most likely the arguments does not match the msg
            ErrorMessage = str(excepted[0])+": '"+str(excepted[1])+"'"
            newMsg = "Trying to log message: '"+str(msg)+"' with args '"+str(args)+"' failed due to "+ErrorMessage
            record = self._createRecord (level, fn, lno, newMsg, (), exc_info, func, extra)
        else:
            record = self._createRecord (level, fn, lno, msg, args, exc_info, func, extra)

        if time.localtime(record.created).tm_isdst and time.daylight:
            record.gmt_offset_seconds = -time.altzone
        else:
            record.gmt_offset_seconds = -time.timezone

        self._sendRecord(record)


    def _createRecord (self, level, fn, lno, msg, args, exc_info, func, extra):
        record = self._stdPyLogger.makeRecord(self._stdPyLogger.name, level, fn, lno, msg, args, exc_info, func, extra)  
        return record                                                                             
                                                                                                  
    def _sendRecord (self, record):                                                               
        self._stdPyLogger.handle(record)                                           

    def createMsgSender (self, msgModule, msgGroup, msgName, instance, extraProperties, isForceStackTrace=False, isForceExceptionData=False, someRateLimitData=None):
        #minimal work here - data and filtering shall be gathered in the "_send" function
        #as the _send function is the one to be called ate the logging place for cases in which we give
        #the logger to another module as simulated standard python logger
        msgAttributes = MsgAttributes(msgModule, msgGroup, msgName, instance, extraProperties, isForceStackTrace, isForceExceptionData, someRateLimitData)
        return MsgSender(self, msgAttributes)

    def _getStdPyLogger (self):
        return self._stdPyLogger

    def collectKickNumber (self):
        self._collectKickNumber = True

    def setDefaultLogLevel (self, logLevel):        
        self._defaultLogLevel = logLevel        


    def getConfigurationLock (self):
        return self._configurationLock

    def _clearCfg (self, hasCfgFlagValue):        
        self._hasCfg = hasCfgFlagValue
        self._configuredLogLevel = None
        self._configuredIsEnablePerformanceData = False
        self._modulesShutLevels = {}
        self._modulesForceLevels = {}
        self._groupsShutLevels = {}
        self._groupsForceLevels = {}
        self._msgIdShutLevels = {}
        self._msgIdForceLevels = {}

    def _setLogCfgLevel (self, logLevel):
        self._configuredLogLevel = logLevel        

    def _setLogCfgEnablePerformanceData (self, isEnabled):        
        self._configuredIsEnablePerformanceData = isEnabled        

    def _setModuleForceLevel (self, moduleName, aMinLevel):
        self._modulesForceLevels[moduleName] = aMinLevel

    def _setModuleShutLevel (self, moduleName, aMaxLevel):
        self._modulesShutLevels[moduleName] = aMaxLevel

    def _setGroupForceLevel (self, moduleName, groupName, aMinLevel):
        self._groupsForceLevels[moduleName+"."+groupName] = aMinLevel

    def _setGroupShutLevel (self, moduleName, groupName, aMaxLevel):
        self._groupsShutLevels[moduleName+"."+groupName] = aMaxLevel

    def _setMsgIdForceLevel (self, moduleName, groupName, msgName, aMinLevel):
        self._msgIdForceLevels[moduleName+"."+groupName+"."+msgName] = aMinLevel

    def _setMsgIdShutLevel (self, moduleName, groupName, msgName, aMaxLevel):
        self._msgIdShutLevels[moduleName+"."+groupName+"."+msgName] = aMaxLevel

    def _shallCreateMsg (self, msgAttributes, level, isEffiecientInterface):        
        with self._configurationLock:
            decision = self._shallCreateMsgLogic(msgAttributes, level)
            if self._configuredIsEnablePerformanceData:
                key = (msgAttributes.msgModule, msgAttributes.msgGroup, msgAttributes.msgName, level, isEffiecientInterface)
                if not key in self._msgsStatistics:
                    statistics = {self._STATISTICS_KEY_SENT: 0,
                                  self._STATISTICS_KEY_FILTERED: 0}
                    self._msgsStatistics[key] = statistics
                else:
                    statistics = self._msgsStatistics[key]
    
                if decision:
                    statistics[self._STATISTICS_KEY_SENT]+=1
                else:
                    statistics[self._STATISTICS_KEY_FILTERED]+=1

        return decision

    def _shallCreateMsgLogic (self, msgAttributes, level):
        msgModule = msgAttributes.msgModule
        msgModuleAndGroup = msgModule + "." + msgAttributes.msgGroup
        msgFullId = msgModuleAndGroup + "." + msgAttributes.msgName

        if msgFullId in self._msgIdShutLevels:
            if self._msgIdShutLevels[msgFullId] >= level:
                return False
        if msgFullId in self._msgIdForceLevels:
            if self._msgIdForceLevels[msgFullId] <= level:
                return True

        if msgModuleAndGroup in self._groupsShutLevels:
            if self._groupsShutLevels[msgModuleAndGroup] >= level:
                return False
        if msgModuleAndGroup in self._groupsForceLevels:
            if self._groupsForceLevels[msgModuleAndGroup] <= level:
                return True

        if msgModule in self._modulesShutLevels:
            if self._modulesShutLevels[msgModule] >= level:
                return False
        if msgModule in self._modulesForceLevels:
            if self._modulesForceLevels[msgModule] <= level:
                return True

        logLevel = self._configuredLogLevel            
        if logLevel is None:
            logLevel = self._defaultLogLevel

        if logLevel > level:
            return False

        #rate limit example
        if msgAttributes.someRateLimitData is not None:
            return False

        return True
    
    def _getMessagesStatistics (self):
        with self._configurationLock:
            return copy.deepcopy(self._msgsStatistics)

class PerformanceData:
    DICT_KEY_STATISTICS_SENT = "sent"
    DICT_KEY_STATISTICS_FILTERED = "filtered"

    STATISTICS_INTERFACE_TYPE_VALUE_NAIVE_LOGGING = "naive-logging"
    STATISTICS_INTERFACE_TYPE_VALUE_ADVANCED_LOGGING = "advanced-logging"

    def __init__ (self, rawStatistics):
        self._rawStatistics = rawStatistics

    def isEmpty (self):
        if self._rawStatistics:
            return False
        return True

    def getStatisticsDictionary (self, reference=None, 
                                 splitByModule=False, splitByGroup=False, splitByMsg=False, 
                                 splitByLevel=False, splitByInterfaceType=False):
        def keyReduction (key):
            newKey = []
            if splitByModule:
                newKey.append(key[0])
            if splitByGroup:
                newKey.append(key[1])
            if splitByMsg:
                newKey.append(key[2])
            if splitByLevel:
                newKey.append(logging.getLevelName(key[3]))
            if splitByInterfaceType:
                if key[4]:
                    newKey.append(self.STATISTICS_INTERFACE_TYPE_VALUE_ADVANCED_LOGGING)
                else:
                    newKey.append(self.STATISTICS_INTERFACE_TYPE_VALUE_NAIVE_LOGGING)
            return ".".join(newKey)

        jointStatistics = copy.deepcopy(self._rawStatistics)        
        try:
            if reference is not None:
                for key in reference._rawStatistics:                    
                    if key not in jointStatistics:
                        statistics = {CoreLogger._STATISTICS_KEY_SENT: 0,
                                      CoreLogger._STATISTICS_KEY_FILTERED: 0}
                        jointStatistics[key] = statistics
                    else:
                        statistics = jointStatistics[key]

                    statisticsToClear = reference._rawStatistics[key]
                    for counter in statisticsToClear:
                        statistics[counter] -= statisticsToClear[counter]
        except:
            return None

        outcomeStatistics = {}
        for key in jointStatistics:
            newKey = keyReduction(key)
            if newKey not in outcomeStatistics:
                statistics = {CoreLogger._STATISTICS_KEY_SENT: 0,
                              CoreLogger._STATISTICS_KEY_FILTERED: 0}
                outcomeStatistics[newKey] = statistics
            else:
                statistics = outcomeStatistics[newKey]

            statisticsToAdd = jointStatistics[key]
            for counter in statisticsToAdd:
                statistics[counter]+=statisticsToAdd[counter]

        keysToRemove=[]
        for key in outcomeStatistics:
            statistics = outcomeStatistics[key]
            isZero = True
            for counter in statistics:
                if statistics[counter] != 0:
                    isZero = False
            if isZero:
                keysToRemove.append(key)

        for key in keysToRemove:
            outcomeStatistics.pop(key)

        return outcomeStatistics

class Logger(object):
    def __init__(self, loggerManager, coreLogger, msgModule, msgGroup, instance = None, extraProperties = None, permanentExtraProperties = None):
        self._loggerManager = loggerManager
        self._coreLogger = coreLogger
        self._msgModule = msgModule
        self._msgGroup = msgGroup
        self._instance = instance
        self._extraProperties = extraProperties
        self._permanentExtraProperties = permanentExtraProperties

    def createLogger(self, msgModule, msgGroup, instance = None, extraProperties = None, permanentExtraProperties = None):
        if extraProperties is None:
            extraProperties = {}
        if permanentExtraProperties is None:
            permanentExtraProperties = {}
        if instance is None:
            instance = self._instance
        #Protection via try catch is not needed - problems in the parameters will be captured on UT
        #the "dict(xxx.items())" also helps us to protect the __call__ function from invalid dictionaries
        return Logger(self._loggerManager, self._coreLogger, msgModule, msgGroup, instance, dict(extraProperties.items()),
                      dict(self._permanentExtraProperties.items() + permanentExtraProperties.items()))#new permanent properties may override old ones     
        
    def createLoggerSameModule(self, msgGroup, instance = None, extraProperties = None, permanentExtraProperties = None):
        if instance is None:
            instance = self._instance
        return self.createLogger(self._msgModule, msgGroup, instance, extraProperties, permanentExtraProperties)

    def createLoggerSameProperties(self, extraProperties = None, permanentExtraProperties = None):
        return self.createLogger(self._msgModule, self._msgGroup, self._instance, extraProperties, permanentExtraProperties)

    def setInstance (self, instance):
        self._instance = instance


    def getPerformanceData (self):
        rawStatistics = self._coreLogger._getMessagesStatistics()
        return PerformanceData(rawStatistics)

    def logPerformanceData (self, msg, reference=None, onlyIfNotEmpty = False, 
                            splitByModule=False, splitByGroup=False, splitByMsg=False, 
                            splitByLevel=False, splitByInterfaceType=False):

        performaceData = self.getPerformanceData()
        if onlyIfNotEmpty and performaceData.isEmpty():
            return
        outcomeStatistics = performaceData.getStatisticsDictionary(reference  = reference, 
                                                                   splitByModule        = splitByModule, 
                                                                   splitByGroup         = splitByGroup, 
                                                                   splitByMsg           = splitByMsg, 
                                                                   splitByLevel         = splitByLevel, 
                                                                   splitByInterfaceType = splitByInterfaceType)        

        self("logger-statistics").notice(msg, jsonDict={"statistics":outcomeStatistics})



    def __call__ (self, msgName, isForceStackTrace=False, isForceExceptionData=False, someRateLimitData=None, **kwargs): 
        self._loggerManager.pearlLoadConfigurationIfNeeded()             
        #the **kwargs come to catch typos in the keywords. 
        loggerInvalidCallArguments = {"logger-invalid-call-arguments": str(kwargs)}      
        #currently protection via try catch is not needed - user must give a msgName (and we "str" it)
        #we use many str() - protecting ourself
        instance = self._instance
        if instance is None:
            instance = ""
        return self._coreLogger.createMsgSender(str(self._msgModule), str(self._msgGroup), str(msgName), str(instance), 
                                                dict(self._permanentExtraProperties.items() + self._extraProperties.items() +
                                                loggerInvalidCallArguments.items()), isForceStackTrace, isForceExceptionData, someRateLimitData)
    
    

    createLoggerForStdLoggerSimulation = __call__


class LoggerManager(object):
    PEARL_CONFIG_LOG_LEVEL = "log-level"
    PEARL_CONFIG_PERFORMACE_DATA_COLLECT = "performace-data-collect"
    PEARL_CONFIG_MODULES_FORCE_LEVEL = "modules-force-min-level"
    PEARL_CONFIG_MODULES_SHUT_LEVEL  = "modules-shut-max-level"
    PEARL_CONFIG_GROUPS_FORCE_LEVEL = "groups-force-min-level"
    PEARL_CONFIG_GROUPS_SHUT_LEVEL  = "groups-shut-max-level"
    PEARL_CONFIG_MSG_IDS_FORCE_LEVEL = "msg-ids-force-min-level"
    PEARL_CONFIG_MSG_IDS_SHUT_LEVEL  = "msg-ids-shut-max-level"

    def __init__(self, loggerName, processName, defaultLogLevel):
        self._processName = processName
        if not self._processName:
            self._processName = str(os.getpid())
        self._coreLogger = CoreLogger(loggerName, processName, defaultLogLevel)
        self._myHandlers = {}
        self._pearlConfigFiles = []
        self._pearlConfigLoadDelta = datetime.timedelta(seconds=0)
        self._pearlConfigUsePeriodicLoad = False
        self._pearlLastConfigDate = datetime.datetime.now()#value will not be used since we load configuration on "setConfigFile" but, just in case
        self._loggerToUse=None

    def initLoggerToUse (self, logger):
        self._loggerToUse = logger.createLoggerSameModule(G_NAME_MODULE_LOG, G_NAME_GROUP_LOG_LOGGER_MANAGER)

    def setProcessName (self, processName):
        self.logSelfMsg(logging.NOTICE, "changing logged process name from '%s' to '%s'", self._processName, processName)
        self._coreLogger.setProcessName(processName)

    def createLogger(self, defaultMsgModule, defaultMsgGroup, extraProperties = None, permanentExtraProperties = None):
        if permanentExtraProperties is None:
            permanentExtraProperties = {}
        if extraProperties is None:
            extraProperties = {}        
        return Logger(self, self._coreLogger, defaultMsgModule, defaultMsgGroup, 
                      extraProperties = dict(extraProperties.items()), 
                      permanentExtraProperties = dict(permanentExtraProperties.items()))

    #exposing functions
    def addHandler(self, handlerMngName, handler):
        self._myHandlers[handlerMngName] = handler
        self._coreLogger._getStdPyLogger().addHandler(handler)

    def removeHandler(self, handlerMngName):
        self._coreLogger._getStdPyLogger().removeHandler(self._myHandlers[handlerMngName])

    def removeAllHandlers(self):
        for handlerMngName in self._myHandlers:
            self._coreLogger._getStdPyLogger().removeHandler(self._myHandlers[handlerMngName])

    def getHandler(self, handlerMngName):
        return self._myHandlers[handlerMngName]

    def replaceHandler(self, handlerMngName, newHandler):
        self._coreLogger._getStdPyLogger().addHandler(newHandler)
        self._coreLogger._getStdPyLogger().removeHandler(self._myHandlers[handlerMngName])
        self._myHandlers[handlerMngName]=newHandler

    def initCollectKickNumber (self):
        self._coreLogger.collectKickNumber()

    def setDefaultLogLevel (self, logLevel):
        self._coreLogger.setDefaultLogLevel(logLevel)

    def logSelfMsg (self, level, msg, *args):
        self.createLogger("logger", "self-msg")(LevelTranslate.s_getLongCppFromPy(level)).log(level, msg, *args)

    def logPerformanceData (self, msg, **kwargs):#same interface as the "logger.logPerformanceData" 
        self.createLogger("logger", "self-msg").logPerformanceData(msg, **kwargs)

    def pearlSetConfigurationFiles (self, fullFileNamesList, loadPeriodInSeconds):
        """
        loadPeriodInSeconds == 0/None ==> no periodic load - (load only once)
        """
        #input normalization
        if fullFileNamesList is None:
            fullFileNamesList = []
        if loadPeriodInSeconds is None:
            loadPeriodInSeconds = 0

        self._pearlConfigFiles = fullFileNamesList
        if not isinstance(self._pearlConfigFiles, list): #a single file - backward competability for install_operations
            self._pearlConfigFiles = [self._pearlConfigFiles]
        if loadPeriodInSeconds < 3 and loadPeriodInSeconds!=0:#allowing only 3 seconds and above - not to create log messages due to the operation
            a.infra.process.processFatal("loadPeriodInSeconds was set to a to small value '%s'. min value is '3'", loadPeriodInSeconds)
        self._pearlConfigLoadDelta = datetime.timedelta(seconds=loadPeriodInSeconds)
        self._pearlConfigUsePeriodicLoad = loadPeriodInSeconds>0
        self.pearlLoadConfigurationIfNeeded(force=True)

    #not working well as pprint using ' instead of "
    #def pearlCreateConfigurationTemplateFile (self, fullFileName):
    #    cfg = {}
    #    cfg[self.PEARL_CONFIG_LOG_LEVEL] = "N"
    #    cfg[self.PEARL_CONFIG_MODULES_FORCE_LEVEL] = {}
    #    cfg[self.PEARL_CONFIG_MODULES_FORCE_LEVEL]["my-module1"] = "N"
    #    cfg[self.PEARL_CONFIG_MODULES_FORCE_LEVEL]["my-module2"] = "N"
    #    cfg[self.PEARL_CONFIG_MODULES_FORCE_LEVEL]["my-module3"] = "N"
    #    cfg[self.PEARL_CONFIG_MODULES_SHUT_LEVEL] = {}
    #    cfg[self.PEARL_CONFIG_MODULES_SHUT_LEVEL]["my-module1"] = "I"
    #    cfg[self.PEARL_CONFIG_MODULES_SHUT_LEVEL]["my-module2"] = "I"
    #    cfg[self.PEARL_CONFIG_MODULES_SHUT_LEVEL]["my-module3"] = "I"
    #    cfg[self.PEARL_CONFIG_GROUPS_FORCE_LEVEL] = {}
    #    cfg[self.PEARL_CONFIG_GROUPS_FORCE_LEVEL]["my-module.my-group1"] = "N"
    #    cfg[self.PEARL_CONFIG_GROUPS_FORCE_LEVEL]["my-module.my-group2"] = "N"
    #    cfg[self.PEARL_CONFIG_GROUPS_FORCE_LEVEL]["my-module.my-group3"] = "N"
    #    cfg[self.PEARL_CONFIG_GROUPS_SHUT_LEVEL] = {}
    #    cfg[self.PEARL_CONFIG_GROUPS_SHUT_LEVEL]["my-module.my-group1"] = "I"
    #    cfg[self.PEARL_CONFIG_GROUPS_SHUT_LEVEL]["my-module.my-group2"] = "I"
    #    cfg[self.PEARL_CONFIG_GROUPS_SHUT_LEVEL]["my-module.my-group3"] = "I"
    #    cfg[self.PEARL_CONFIG_MSG_IDS_FORCE_LEVEL] = {}
    #    cfg[self.PEARL_CONFIG_MSG_IDS_FORCE_LEVEL]["my-module.my-group.my-name1"] = "N"
    #    cfg[self.PEARL_CONFIG_MSG_IDS_FORCE_LEVEL]["my-module.my-group.my-name2"] = "N"
    #    cfg[self.PEARL_CONFIG_MSG_IDS_FORCE_LEVEL]["my-module.my-group.my-name3"] = "N"
    #    cfg[self.PEARL_CONFIG_MSG_IDS_SHUT_LEVEL] = {}
    #    cfg[self.PEARL_CONFIG_MSG_IDS_SHUT_LEVEL]["my-module.my-group.my-name1"] = "I"
    #    cfg[self.PEARL_CONFIG_MSG_IDS_SHUT_LEVEL]["my-module.my-group.my-name2"] = "I"
    #    cfg[self.PEARL_CONFIG_MSG_IDS_SHUT_LEVEL]["my-module.my-group.my-name3"] = "I"
    #
    #    try:
    #        with open(fullFileName, "w") as fd:
    #            pprint.pprint(cfg, fd)
    #    except:
    #        self._loggerToUse("failed-wrting-template").exception("Failed to write template file '%s'", fullFileName)



    def pearlLoadConfigurationIfNeeded(self, force=False):
        if not self._pearlConfigFiles:#list is empty, nothing to load
            return

        if not force and not self._pearlConfigUsePeriodicLoad:
            return

        if not (force or (datetime.datetime.now()-self._pearlLastConfigDate) >= self._pearlConfigLoadDelta):
            return

        configurationLock = self._coreLogger.getConfigurationLock()
                
        #the time test is also after the lock so no 2 messages can reach it
        self._pearlLastConfigDate = datetime.datetime.now()

        #as we know this area is called only once in a while, we allow log messages here (even due we have no protection)        
        choosenFileName = None
        #choosing last existing file in the list
        for fileName in self._pearlConfigFiles:
            if not os.path.exists(fileName):
                continue
            choosenFileName = fileName

        if choosenFileName is not None:
            try:
                fd = open(choosenFileName)
            except:
                configurationLock.acquire()
                self._coreLogger._clearCfg(hasCfgFlagValue = False)#cfg is cleared only when required, so the global hasCfg flag will not be unset temporarily
                configurationLock.release()
                self._loggerToUse("cfg-open-failed").exception("Failed to open config file '%s'", choosenFileName)
                return
            try:
                cfg = json.load(fd)
            except:
                configurationLock.acquire()
                self._coreLogger._clearCfg(hasCfgFlagValue = False)#cfg is cleared only when required, so the global hasCfg flag will not be unset temporarily
                configurationLock.release()
                self._loggerToUse("cfg-load-failed").exception("Failed to parse config file '%s'", choosenFileName)
                return
            finally:
                fd.close()

            (errorMessages, isEmpty) = self._pearlLoadConfigurationDict(cfg, True)
            if errorMessages:
                configurationLock.acquire()
                self._coreLogger._clearCfg(hasCfgFlagValue = False)#cfg is cleared only when required, so the global hasCfg flag will not be unset temporarily
                configurationLock.release()
                for errorMessage in errorMessages:
                    self._loggerToUse("bad-cfg").error("%s", errorMessage)
                self._loggerToUse("bad-total-cfg").error("Failed to load config file '%s' due to bad configuration", choosenFileName)
                return

            if isEmpty:#cfg is cleared only when required, so the global hasCfg flag will not be unset temporarily
                configurationLock.acquire()
                self._coreLogger._clearCfg(hasCfgFlagValue = False)#cfg is cleared only when required, so the global hasCfg flag will not be unset temporarily
                configurationLock.release()
                return

            configurationLock.acquire()
            #keeping the flag True all the time, so if somebody tests
            #to see if there a cfg and if ihe needs to wait for the lock, 
            #he will not get temporarily "fasle"
            self._coreLogger._clearCfg(hasCfgFlagValue = True)
            self._pearlLoadConfigurationDict(cfg, False)            
            configurationLock.release()

        else:
            configurationLock.acquire()
            self._coreLogger._clearCfg(hasCfgFlagValue = False)#cfg is cleared only when required, so the global hasCfg flag will not be unset temporarily
            configurationLock.release()

        return


    def _pearlLoadConfigurationDict(self, cfg, isOnlyValidate):
        isEmpty=True
        errorMessages = []
        if self.PEARL_CONFIG_LOG_LEVEL in cfg:
            isEmpty = False
            inputLogLevel = cfg[self.PEARL_CONFIG_LOG_LEVEL]
            logLevel = LevelTranslate.s_getPyLevelFromCpp(inputLogLevel)
            if logLevel is None:
                errorMessages.append("unfamiliar log level '%s'"%inputLogLevel)
            elif not isOnlyValidate:
                self._coreLogger._setLogCfgLevel(logLevel)

        if self.PEARL_CONFIG_PERFORMACE_DATA_COLLECT in cfg:
            isEmpty = False
            inputIsEnabled = cfg[self.PEARL_CONFIG_PERFORMACE_DATA_COLLECT]
            if inputIsEnabled not in [False, True]:
                errorMessages.append("invalid '%s' value '%s'"%(self.PEARL_CONFIG_PERFORMACE_DATA_COLLECT, inputIsEnabled))
            elif not isOnlyValidate:
                self._coreLogger._setLogCfgEnablePerformanceData(inputIsEnabled)

        if self.PEARL_CONFIG_MODULES_FORCE_LEVEL in cfg:
            data=cfg[self.PEARL_CONFIG_MODULES_FORCE_LEVEL]
            for module in data:
                isEmpty = False
                inputLogLevel = data[module]
                logLevel = LevelTranslate.s_getPyLevelFromCpp(inputLogLevel)
                if logLevel is None:
                    errorMessages.append("unfamiliar log level '%s'"%inputLogLevel)
                    
                if not isOnlyValidate:
                    self._coreLogger._setModuleForceLevel(module,logLevel)

        if self.PEARL_CONFIG_MODULES_SHUT_LEVEL in cfg:
            data=cfg[self.PEARL_CONFIG_MODULES_SHUT_LEVEL]
            for module in data:
                isEmpty = False
                inputLogLevel = data[module]
                logLevel = LevelTranslate.s_getPyLevelFromCpp(inputLogLevel)
                if logLevel is None:
                    errorMessages.append("unfamiliar log level '%s'"%inputLogLevel)
                    continue
                if not isOnlyValidate:
                    self._coreLogger._setModuleShutLevel(module,logLevel)

        if self.PEARL_CONFIG_GROUPS_FORCE_LEVEL in cfg:
            data=cfg[self.PEARL_CONFIG_GROUPS_FORCE_LEVEL]
            for moduleAndGroup in data:
                isEmpty = False
                key = moduleAndGroup.split(".")
                if len(key)!=2:
                    errorMessages.append("unsupported group name '%s'"%moduleAndGroup)
                    continue
                inputLogLevel = data[moduleAndGroup]
                logLevel = LevelTranslate.s_getPyLevelFromCpp(inputLogLevel)
                if logLevel is None:
                    errorMessages.append("unfamiliar log level '%s'"%inputLogLevel)
                    continue
                if not isOnlyValidate:
                    module = key[0]
                    group = key[1]
                    self._coreLogger._setGroupForceLevel(module, group, logLevel)

        if self.PEARL_CONFIG_GROUPS_SHUT_LEVEL in cfg:
            data=cfg[self.PEARL_CONFIG_GROUPS_SHUT_LEVEL]
            for moduleAndGroup in data:
                isEmpty = False
                key = moduleAndGroup.split(".")
                if len(key)!=2:
                    errorMessages.append("unsupported group name '%s'"% moduleAndGroup)
                    continue
                inputLogLevel = data[moduleAndGroup]
                logLevel = LevelTranslate.s_getPyLevelFromCpp(inputLogLevel)
                if logLevel is None:
                    errorMessages.append("unfamiliar log level '%s'"%inputLogLevel)
                    continue
                if not isOnlyValidate:
                    module = key[0]
                    group = key[1]
                    self._coreLogger._setGroupShutLevel(module, group, logLevel)

        if self.PEARL_CONFIG_MSG_IDS_FORCE_LEVEL in cfg:
            data=cfg[self.PEARL_CONFIG_MSG_IDS_FORCE_LEVEL]
            for msgId in data:
                isEmpty = False
                key = msgId.split(".")
                if len(key)!=3:
                    errorMessages.append("unsupported msg name '%s'"%msgId)
                    continue
                inputLogLevel = data[msgId]
                logLevel = LevelTranslate.s_getPyLevelFromCpp(inputLogLevel)
                if logLevel is None:
                    errorMessages.append("unfamiliar log level '%s'"%inputLogLevel)
                    continue
                if not isOnlyValidate:
                    module = key[0]
                    group = key[1]
                    name = key[2]
                    self._coreLogger._setMsgIdForceLevel(module, group, name, logLevel)

        if self.PEARL_CONFIG_MSG_IDS_SHUT_LEVEL in cfg:
            data=cfg[self.PEARL_CONFIG_MSG_IDS_SHUT_LEVEL]
            for msgId in data:
                isEmpty = False
                key = msgId.split(".")
                if len(key)!=3:
                    errorMessages.append("unsupported msg name '%s'"%msgId)
                    continue
                inputLogLevel = data[msgId]
                logLevel = LevelTranslate.s_getPyLevelFromCpp(inputLogLevel)
                if logLevel is None:
                    errorMessages.append("unfamiliar log level '%s'"%inputLogLevel)
                    continue
                if not isOnlyValidate:
                    module = key[0]
                    group = key[1]
                    name = key[2]
                    self._coreLogger._setMsgIdShutLevel(module, group, name, logLevel)

        return (errorMessages, isEmpty)



class LevelTranslate:
    _ourShortCppToPy = {"D5":logging.DEBUG5, "D4":logging.DEBUG4, "D3":logging.DEBUG3, "D2":logging.DEBUG2, "D1":logging.DEBUG1,
                        "I":logging.INFO, "N":logging.NOTICE, "W":logging.WARNING, "E":logging.ERROR, 
                        "CR":logging.CRITICAL, "AL":logging.CRITICAL, "EM":logging.CRITICAL}

    _ourLongCppToShortCpp = {"DEBUG5":"D5", "DEBUG4":"D4", "DEBUG3":"D3", "DEBUG2":"D2", "DEBUG1":"D1",
                             "INFO":"I", "NOTICE":"N", "WARNING":"W", "ERR":"E",
                             "CRIT":"CR", "ALERT":"AL", "EMERG":"EM", "INFINIT":"IN"}

    _ourPyToLongCpp = {logging.DEBUG5:"DEBUG5", logging.DEBUG4:"DEBUG4", logging.DEBUG3:"DEBUG3", logging.DEBUG2:"DEBUG2", logging.DEBUG1:"DEBUG1", logging.DEBUG:"DEBUG1",
                       logging.INFO:"INFO", logging.NOTICE:"NOTICE", logging.WARNING:"WARNING", logging.ERROR:"ERR",
                       logging.CRITICAL:"CRIT"}

    @classmethod
    def s_getPyLevelFromCpp (cls, cppLevel):
        if cppLevel in cls._ourShortCppToPy:
            return cls._ourShortCppToPy[cppLevel]
        if cppLevel in cls._ourLongCppToShortCpp:
            return cls._ourShortCppToPy[cls._ourLongCppToShortCpp[cppLevel]]
        return None

    @classmethod
    def s_getLongCppFromPy (cls, pyLevel):
        if pyLevel in cls._ourPyToLongCpp:
            return cls._ourPyToLongCpp[pyLevel]
        return "None"

