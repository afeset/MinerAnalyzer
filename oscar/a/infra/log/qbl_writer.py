#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 
import a.infra.gpb.chain
import logging
__pychecker__="no-import"
import logger
import get_gpb_workaround
from include.a.infra.log.level_pb2 import LevelGpb
import google.protobuf.message
import a.infra.string

class QblWriter:
    GPB_PLACE_HOLDER = "%GPB"
   
    @classmethod
    def s_logLevelToGpbValue(cls, logLevel):        
        __pychecker__="no-argsused"
        if logLevel == logging.FATAL:
            return LevelGpb.kCritical
        if logLevel == logging.CRITICAL:
            return LevelGpb.kCritical
        if logLevel == logging.ERROR:
            return LevelGpb.kError
        if logLevel == logging.WARNING:
            return LevelGpb.kWarning
        if logLevel == logging.WARN:
            return LevelGpb.kWarning
        if logLevel == logging.NOTICE:
            return LevelGpb.kNotice
        if logLevel == logging.INFO:
            return LevelGpb.kInfo
        if logLevel == logging.DEBUG:
            return LevelGpb.kDebug1
        if logLevel == logging.DEBUG1:
            return LevelGpb.kDebug1
        if logLevel == logging.DEBUG2:
            return LevelGpb.kDebug2
        if logLevel == logging.DEBUG3:
            return LevelGpb.kDebug3
        if logLevel == logging.DEBUG4:
            return LevelGpb.kDebug4
        if logLevel == logging.DEBUG5:
            return LevelGpb.kDebug5
        else:
            print "QBL writer got invalid log level %s, treating as Error."%logLevel
            return LevelGpb.kError
        

    @classmethod
    def s_createMsgGpbs (cls,
                         module, group, name, logLevel, bodyList,
                         timeOfDayGmtNanoSeconds, timeOfDayGmtOffsetMinutes, timeMonotonicNanoSeconds,
                         sourceFileName, sourceLineNumber, functionName,
                         processId, processName, threadId, threadFullName, threadShortName, instanceName,
                         msgIdSequenceNumber, globalSequenceNumber, errno,
                         extraProperties = {},
                         msgIdDropCounter=0, globalDropCounter=0, 
                         loggerRecursionDepth=0, loggerChainReactionLength=0, kickNumber=0):        
        __pychecker__="maxargs=30"
        body = ""
        followingGpbs = []
        for item in bodyList:
            if isinstance(item, str) or isinstance(item, unicode):
                body = body+item
            elif isinstance(item, google.protobuf.message.Message):
                body = body + cls.GPB_PLACE_HOLDER
                followingGpbs.append(item)
            else:
                body = body + "(invalid logged object %s)"%str(item)

                
                


        msgDataGpb = get_gpb_workaround.getMsgDataGpb()
        msgDataGpb.myModule = module
        msgDataGpb.myGroup = group
        msgDataGpb.myName = name
        msgDataGpb.myLogLevel = cls.s_logLevelToGpbValue(logLevel)
        try:
            msgDataGpb.myBody = body
        except ValueError:
            msgDataGpb.myBody = a.infra.string.utils.Utils.s_turnToPrintable(body)

        msgDataGpb.myTimeOfDayGmtNanoseconds = timeOfDayGmtNanoSeconds
        msgDataGpb.myTimeOfDayGmtOffsetMinutes = timeOfDayGmtOffsetMinutes
        msgDataGpb.myTimeMonotonicNanoseconds = timeMonotonicNanoSeconds
        msgDataGpb.myErrno = errno
        
        msgDataGpb.mySourceFileName = sourceFileName
        msgDataGpb.mySourceLineNumber = sourceLineNumber
        msgDataGpb.mySourceFunctionName = functionName

        msgDataGpb.myProcessId = processId
        msgDataGpb.myProcessName = processName
        msgDataGpb.myThreadId = threadId
        msgDataGpb.myThreadFullName = threadFullName
        msgDataGpb.myThreadShortName = threadShortName
        msgDataGpb.myInstanceName = instanceName

        for key in extraProperties:
            msgExtraDataGpb = msgDataGpb.myExtraData.add()
            msgExtraDataGpb.myKey = str(key)
            msgExtraDataGpb.myValue = str(extraProperties[key])


        msgDataGpb.myMsgIdSequenceNumber = msgIdSequenceNumber
        msgDataGpb.myGlobalSequenceNumber = globalSequenceNumber

        msgDataGpb.myMsgIdDropCounter = msgIdDropCounter
        msgDataGpb.myGlobalDropCounter = globalDropCounter

        msgDataGpb.myLoggerRecursionDepth = loggerRecursionDepth
        msgDataGpb.myLoggerChainReactionLength = loggerChainReactionLength

        msgDataGpb.myKickNumber = kickNumber

        return [msgDataGpb] + followingGpbs

    @classmethod
    def s_addMsg (cls, singleMsgGpbsList, gpbChainWriter):
        __pychecker__="no-argsused"
        oChain = a.infra.gpb.chain.oGenericGPBChain(gpbChainWriter)
        for gpb in singleMsgGpbsList[:-1]:
            oChain.append(gpb)
        oChain.append(singleMsgGpbsList[-1], isLast=True)


