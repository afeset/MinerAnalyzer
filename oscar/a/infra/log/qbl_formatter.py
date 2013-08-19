#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 
import qbl_writer
import logger
import logging
import cStringIO
import types
import sys
import json
import pprint
import StringIO
import get_gpb_workaround
import a.infra.debug.backtrace
    
class QblFormatter(logging.Formatter):
    class ChainWriter:
        def __init__ (self):
            self._strIo = cStringIO.StringIO()
        def write (self, data):
            self._strIo.write(data)
        def getValue (self):
            return self._strIo.getvalue()

    def __init__(self):
        logging.Formatter.__init__(self, "nada")

    def _appendGpbs (self, itemsList, gpbCreator, body):
        for item in itemsList:
            if item[1] is None:
                body.append(" %s=N/A"%item[0])
            else:
                try:
                    gbpToStore = gpbCreator()
                    gbpToStore.myData = item[1]
                    gbpToStore.myMetaData.myIsPartialData=False;
                    gbpToStore.myMetaData.myWasForced=False;
                    gbpToStore.myMetaData.myName=item[0];
                    gbpToStore.myMetaData.myFormatVersion=100;
                    body.append(gbpToStore)
                except:
                    body.append(" %s=N/A"%item[0])

    def _backtraceToGpb (self, name, backtrace, isExceptionTrace=False):
        decodedStackTraceGpb = get_gpb_workaround.getMsgBodyFragmentGpbDecodedBacktrace ()
        decodedStackTraceGpb.myMetaData.myIsPartialData=False
        decodedStackTraceGpb.myMetaData.myWasForced=False
        decodedStackTraceGpb.myMetaData.myName=name
        decodedStackTraceGpb.myMetaData.myFormatVersion=100
        decodedStackTraceGpb.myIsExceptionTrace=isExceptionTrace             
        decodedStackTraceGpb.myCurrentFrameIndex=backtrace.getCurrentFrameIndex()
        for frame in backtrace.getFrames():
            frameGpb = decodedStackTraceGpb.myFrames.add()
            frameGpb.myFileName      = frame.fileName
            frameGpb.myLineNumber    = frame.lineNum;
            frameGpb.myPyModuleName  = frame.pyModuleName;
            frameGpb.myClassName     = frame.className;
            frameGpb.myFunctionName  = frame.function;
            for arg in frame.argsList:
                argsGpb = frameGpb.myArgs.add()
                argsGpb.myArgName=arg[0]
                try:#trying to json if possible
                    argValue = json.dumps(arg[1], indent=4, sort_keys=True)
                except:
                    try:#failed with json, try pretty print
                        outputStream = StringIO.StringIO()
                        pprint.pprint(arg[1], stream=outputStream, indent=4)
                        argValue=outputStream.getvalue().strip()
                        outputStream.close()
                    except:#last resort. maybe not nessecary
                        argValue=str(arg[1])
                argsGpb.myArgValue=argValue
        return decodedStackTraceGpb


    def format(self, record):
         body = str(record.getMessage())
         bodyLen = len(body)
         if bodyLen > 64*1024:##irresnable message size. lets trim it. the value must be smaller than 120*1024 for q-lv to be able to read it
             body = ("invalid too long message (%d): "%bodyLen)+body[:200]+" ... "+body[-100:]
         
         body = [body]

         self._appendGpbs(record.__dict__[logger.G_RECORD_KEY_PLAIN_TEXT_BUFFERS], 
                          get_gpb_workaround.getMsgBodyFragmentGpbPlainTextBuffer, 
                          body)

         self._appendGpbs(record.__dict__[logger.G_RECORD_KEY_JSON_TEXT_BUFFERS], 
                          get_gpb_workaround.getMsgBodyFragmentGpbJsonTextBuffer, 
                          body)

         self._appendGpbs(record.__dict__[logger.G_RECORD_KEY_BINARY_BUFFERS], 
                          get_gpb_workaround.getMsgBodyFragmentGpbSimpleBuffer, 
                          body)

         gpbs = record.__dict__[logger.G_RECORD_KEY_GPBS]
         for item in gpbs:
             if item[1] is None:
                body.append(" %s=N/A"%item[0])
             else:
                 body += [" %s="%item[0], item[1]]

         decodedBacktraces = record.__dict__[logger.G_RECORD_KEY_DECODED_BACKTRACES]
         for item in decodedBacktraces:
             if item[1] is None:
                body.append(" %s=N/A"%item[0])
             else:
                 body.append(self._backtraceToGpb(item[0], item[1]))



         #collecting the exception. This code is extra careful as we added this code late in 2.6.0
         try:#this "try" is just in case
             excInfo = record.exc_info
             if excInfo:                 
                 if type(excInfo) == types.TupleType:
                     try:
                         exceptionData = excInfo[1]
                         body +=["\nCollected exception: %s"%exceptionData]                     

                         try:                             
                             tb = excInfo[2]
                             backtrace = a.infra.debug.backtrace.Backtrace()
                             try:
                                 currentFrameIndex=0
                                 while tb.tb_next is not None:#getting deeper into the stack trace
                                     tb = tb.tb_next
                                     currentFrameIndex += 1
                                 frame = tb.tb_frame

                                 backtrace.initFromPythonFrame(frame, 
                                                               currentFrameIndex=currentFrameIndex,
                                                               maxFrameIndex=sys.maxint, 
                                                               maxFrameIndexIncludingArgs=currentFrameIndex)
                             except:
                                 decodedStackTraceGpb = self._backtraceToGpb("partial-exception-backtrace", backtrace)                                               
                                 body.append(decodedStackTraceGpb)
                             finally:
                                 decodedStackTraceGpb = self._backtraceToGpb("exception-backtrace", backtrace)                                               
                                 body.append(decodedStackTraceGpb)

                         except:
                             body +=["Invalid exception tuple (no stack-trace): %s\n"%excInfo]
                     except:
                         body +=["\nInvalid exception tuple: %s\n"%excInfo]                     
                 else:
                     body +=["\nUnsupported exception class: %s\n"%excInfo]
         except:
             body +=["\n<Missing exception data>\n"]                     

         #collecting the stack trace
         stackTrace = record.__dict__[logger.G_RECORD_KEY_STACK_TRACE]
         if stackTrace:
             decodedStackTraceGpb = self._backtraceToGpb("msg-backtrace",stackTrace)             
             body.append(decodedStackTraceGpb)


         msg = qbl_writer.QblWriter.s_createMsgGpbs (module = record.__dict__[logger.G_RECORD_KEY_MSG_MODULE], 
                                                     group = record.__dict__[logger.G_RECORD_KEY_MSG_GROUP], 
                                                     name = record.__dict__[logger.G_RECORD_KEY_MSG_NAME], 
                                                     logLevel = record.levelno, 
                                                     bodyList = body,
                                                     timeOfDayGmtNanoSeconds = long(record.created*1000*1000*1000), 
                                                     timeOfDayGmtOffsetMinutes = record.gmt_offset_seconds/60, 
                                                     timeMonotonicNanoSeconds = long(record.relativeCreated*1000*1000*1000),
                                                     sourceFileName = record.pathname, 
                                                     sourceLineNumber = record.lineno, 
                                                     functionName = record.__dict__[logger.G_RECORD_KEY_PY_MODULE]+"."+record.__dict__[logger.G_RECORD_KEY_CLASS]+"."+record.funcName,
                                                     processId = record.__dict__[logger.G_RECORD_KEY_PROCESS_ID], 
                                                     processName = record.__dict__[logger.G_RECORD_KEY_PROCESS_NAME],                                                      
                                                     threadId = record.thread, 
                                                     threadFullName = record.threadName, 
                                                     threadShortName = record.threadName,
                                                     instanceName = record.__dict__[logger.G_RECORD_KEY_INSTANCE], 
                                                     errno = record.__dict__[logger.G_RECORD_KEY_ERRNO], 
                                                     extraProperties = record.__dict__[logger.G_RECORD_KEY_EXTRA_PROPERTIES], 
                                                     msgIdSequenceNumber = record.__dict__[logger.G_RECORD_KEY_MSG_ID_SEQUENCE_NUMBER], 
                                                     globalSequenceNumber = record.__dict__[logger.G_RECORD_KEY_GLOBAL_SEQUENCE_NUMBER], 
                                                     kickNumber = record.__dict__[logger.G_RECORD_KEY_KICK_NUMBER])

         writer = self.ChainWriter()
         qbl_writer.QblWriter.s_addMsg(msg, writer)
         return writer.getValue()


