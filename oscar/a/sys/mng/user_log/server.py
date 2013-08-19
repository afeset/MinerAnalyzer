#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

import os
import subprocess
import re
import time
import StringIO
import a.api.user_log.msg.sys
import a.infra.gpb.chain
from include.a.sys.mng.user_log.msg_data_pb2 import MsgDataGpb
import infra.log.msg_data_pb2

if  __package__ is None:
    G_NAME_MODULE_SYS_USER_LOG_SERVER = "unknown"
    G_NAME_GROUP_SYS_USER_LOG_SERVER_GENERAL = "unknown"    
    G_NAME_GROUP_SYS_USER_LOG_SERVER_READ = "unknown"    
    G_NAME_GROUP_SYS_USER_LOG_SERVER_WRTIE = "unknown"   
    G_NAME_GROUP_SYS_USER_LOG_SERVER_CLEAR = "unknown"
    G_NAME_GROUP_SYS_USER_LOG_SERVER_MSG_LIST = "unknown"
else:
    from . import G_NAME_MODULE_SYS_USER_LOG_SERVER
    from . import G_NAME_GROUP_SYS_USER_LOG_SERVER_GENERAL
    from . import G_NAME_GROUP_SYS_USER_LOG_SERVER_READ
    from . import G_NAME_GROUP_SYS_USER_LOG_SERVER_WRITE
    from . import G_NAME_GROUP_SYS_USER_LOG_SERVER_CLEAR
    from . import G_NAME_GROUP_SYS_USER_LOG_SERVER_MSG_LIST
    
class Server(object):

    INPUT_GENERATION_COMMAND_START_TIME_PLACE_HOLDER = "%start-time"

    _STATE_FILE_KEY_START_TIME = "start-time"

    def __init__(self, logger):
        self._logGeneral = logger.createLogger(G_NAME_MODULE_SYS_USER_LOG_SERVER, G_NAME_GROUP_SYS_USER_LOG_SERVER_GENERAL)
        self._logRead = logger.createLogger(G_NAME_MODULE_SYS_USER_LOG_SERVER, G_NAME_GROUP_SYS_USER_LOG_SERVER_READ)
        self._logWrite = logger.createLogger(G_NAME_MODULE_SYS_USER_LOG_SERVER, G_NAME_GROUP_SYS_USER_LOG_SERVER_WRITE)
        self._logClear = logger.createLogger(G_NAME_MODULE_SYS_USER_LOG_SERVER, G_NAME_GROUP_SYS_USER_LOG_SERVER_CLEAR)
        self._logMsgList = logger.createLogger(G_NAME_MODULE_SYS_USER_LOG_SERVER, G_NAME_GROUP_SYS_USER_LOG_SERVER_MSG_LIST)

        self._inputGenerationCommandPattern = None
        self._outputFd = None
        self._stateFileName = None
        self._msgsPythonFilesFileName = None

    def initInputGenerationCommandPattern (self, inputGenerationCommandPattern):
        self._inputGenerationCommandPattern = inputGenerationCommandPattern

    def initOutputFd (self, outputFd):
        self._outputFd = outputFd

    def initStateFile (self, state):
        self._stateFileName = state

    def initMsgsFiles (self, msgsPythonFilesFileName):
        self._msgsPythonFilesFileName = msgsPythonFilesFileName

    def viewLog (self):
        self._logGeneral("start").info("starting")

        inputGenerationCommand = self._calcInputGenerationCommand()
        self._logGeneral("input-generation-command").info("input generation command: %s", inputGenerationCommand)

        popen = subprocess.Popen(inputGenerationCommand.split(), stderr=subprocess.PIPE, stdout = subprocess.PIPE )#not sending stderr to the same file 
                                                                                                                   #as we dont want to mix binary data with text
        output, notused = popen.communicate()
        rc = self._readChainFile(StringIO.StringIO(output), self._outputFd)
        return rc

    def clearLog (self):
        newStartTime = time.time()
        if self._stateFileName is None:
            self._logClear("no-file-set").error("failed to clear log file - no state file was set")
            return False

        if not os.path.exists(os.path.dirname(self._stateFileName)):
            try:
                os.makedirs(os.path.dirname(self._stateFileName))
            except:
                self._logClear("failed-create-state-dir").exception("failed to create state file directory")
                return False
        
        data = {}
        if os.path.exists(self._stateFileName):
            try:
                data = a.infra.format.json.readFromFile (self._logClear, self._stateFileName)
            except:
                self._logClear("failed-read-prev-state").exception("failed to read prev state file")
                return False

        if not isinstance(data,dict):
            self._logClear("failed-read-prev-state").error("prev state file is of invalid structure: %s", data)
            return False

        data[self._STATE_FILE_KEY_START_TIME] = newStartTime

        try:
            data = a.infra.format.json.writeToFile (self._logClear, data, self._stateFileName, indent=4)
        except:
            self._logClear("failed-write-state-file").exception("failed to write prev file")
            return False

        time.sleep(1)#sleep for one second to avoid delta T issues working withn q-lv (none expected but Gaash wanted to stay on the safe side)
        self._logClear("cleared-log").notice("cleared user log")
        self._logClear("cleared-log-d").debug1("cleared user log - new start time is %d", newStartTime)

        a.infra.process.logUserMessage(a.api.user_log.msg.sys.ClearUserLog())

        return True

    @classmethod
    def s_writeStateFileIfNoneExists (cls, stateFileName):
        if os.path.exists(stateFileName):
            return

        stateDir = os.path.dirname(stateFileName)
        if not os.path.exists(stateDir):
            os.makedirs(stateDir)
        
        data = {}
        data[cls._STATE_FILE_KEY_START_TIME] = time.time()

        a.infra.format.json.writeToFile (None, data, stateFileName, indent=4)
        

    def viewMsgsList (self, includeDeclared, includeActive):
        self._logMsgList("start-list").info("starting viewing messages list")
        if not self._msgsPythonFilesFileName:
            self._logMsgList("no-file-set").error("cannot list messages - no file supplying the messages files list")
            return False
        if not os.path.exists(self._msgsPythonFilesFileName):
            self._logMsgList("no-file").error("cannot list messages - file '%s' does not exists", self._msgsPythonFilesFileName)
            return False
        
        try:
            msgList = a.infra.format.json.readFromFile(self._logMsgList, self._msgsPythonFilesFileName)
        except:
            self._logMsgList("read-file-fail").exception("Failed to read json from file '%s'", self._msgsPythonFilesFileName)
            return False

        if not isinstance(msgList, list):
            self._logMsgList("no-list").error("File '%s' does not contain a list of file", self._msgsPythonFilesFileName)
            return False

        totalNumOfMsgs = 0
        for fileName in sorted(msgList):
            self._logMsgList("read-file").debug1("Reading file '%s'", fileName)
            totalNumOfMsgs += self._viewMsgListOfFile(fileName, includeDeclared, includeActive)        
        print "======================================================================================="
        print "Total number of messages: %s"%(totalNumOfMsgs)
        print "======================================================================================="
        return True

    def _calcInputGenerationCommand (self):
        startTime = 0
        if not self._stateFileName is None:
            try:
                if os.path.exists(self._stateFileName):
                    stateFileData = a.infra.format.json.readFromFile (self._logRead, self._stateFileName)
                    if self._STATE_FILE_KEY_START_TIME in stateFileData:
                        startTime = stateFileData[self._STATE_FILE_KEY_START_TIME]
                        self._logRead("read-start-time").debug1("read start time to be %d", startTime)
                    else:
                        self._logRead("no-start-time-flag").debug2("no start time flag in file %s", self._stateFileName)
                else:
                    self._logRead("no-state-file").debug2("no state file %s", self._stateFileName)
            except:
                self._logRead("failed-reading-state-file").warning("failed to read state file for logging start time", exc_info=1)
        else:
            self._logRead("no-state-file-set").debug2("no state file set")

        timeString = time.strftime("%Y%m%d-%H%M%S", time.gmtime(startTime))

        cmd = self._inputGenerationCommandPattern
        cmd = cmd.replace(self.INPUT_GENERATION_COMMAND_START_TIME_PLACE_HOLDER, timeString)
        return cmd

       
    def _readChainFile(self, inputFileD, outputFileD):                
        try:                
            self._logRead("read-next").debug4("reading next message.")
            msgs = self._readChunk(inputFileD)                
        except Exception as exception:
            self._logRead("read-chain-failed").exception("failed to read msg: %s", str(exception))
            msgs = []
            #not returning - printing what we have

        if msgs:
            msgs = msgs[-1000:]#print up to 1000 (last) messages. if you want to change it, please chage also the q-lv command in OSCAR_CORE!!!!!!!!!! 
            self._logWrite("write-msgs").debug4("writing %d messages", len(msgs))
            self._logWrite("write-msgs-data").debug5("writing messages: %s", str(msgs))
            try:
                outputFileD.writelines(msgs)
            except:
                self._logWrite("write-failed").exception("Failed to write messages")
                return False
        else:
            self._logWrite("no-msgs").debug4("no-messages to write")

    def _readChunk(self, inputFileD):
        ichain = a.infra.gpb.chain.ifGPBChain(inputFileD)
        # populate chain with known message types
        ichain.addFactoryMessage(MsgDataGpb())
        ichain.addFactoryMessage(infra.log.msg_data_pb2.MsgDataGpb())

        msgs = []
        for message in ichain:
            if not isinstance(message, MsgDataGpb):
                self._logRead("irrelevant-gpb").debug5("skip gpb not of the proper type")
                continue
            self._logRead("relevant-gpb").debug4("found proper GPB")
            msgs.append(self._getMsgString(message))
                    
        return msgs

    def _getMsgString (self, msgDataGpb):
        creationTime = msgDataGpb.myTimeOfDayGmtNanoseconds / (1000.0*1000*1000)
        creationTime += msgDataGpb.myTimeOfDayGmtOffsetMinutes * 60
        timeString = time.strftime("%b %e %H:%M:%S", time.gmtime(int(creationTime)))
        timeString = timeString + ".%03d"%(int((creationTime-int(creationTime))*1000))
        msgString = "%s: %%%s-%s-%d-%s: %s\n"%(timeString, 
            msgDataGpb.myCategory, msgDataGpb.myGroup, msgDataGpb.mySeverity, msgDataGpb.myCode, 
            msgDataGpb.myBody)
        return msgString

    def _viewMsgListOfFile (self, fileName, includeDeclared, includeActive):       

        try:
            moduleName = ".".join(fileName.replace("/", ".").split(".")[1:-1]) #removing the "python" and the "py"
        except:
            self._logMsgList("failed-modulize").exception("failed turning '%s' into a module name", fileName)

        try:
            __import__(moduleName)
            a.api.user_log.msg.message_base.MessageBase.s_clearMessagesList()
            reload(eval(moduleName))#reload for the case the module was already imported before and need to be inported now again
        except:
            self._logMsgList("failed-import").exception("failed importing module '%s'", moduleName)

        msgs = a.api.user_log.msg.message_base.MessageBase.s_getMessagesList()        

        self._logMsgList("unfiltered-num").debug3("unfiltered num of messages for module '%s' is", moduleName, len(msgs))
        msgs = self._filterMessages(msgs, includeDeclared, includeActive)
        self._logMsgList("filtered-num").debug3("filtered num of messages for module '%s' is", moduleName, len(msgs))
        if msgs:
            print "======================================================================================="
            print "module: %s (%d messages)"%(moduleName, len(msgs))
            print "======================================================================================="
        for msg in msgs:
            print self._getMessageDescriptionString(msg)
            print "---------------------------------------------------------------------------------------"    
            
        return len(msgs)    

    def _getMessageDescriptionString (self, msg): 
        formatStr = None 
        for line in msg.devComment.split("\n"):
            match = re.search("^@format:(.*)$", line.strip())
            if match:
                try:
                    formatStr = match.group(1).strip()
                    break
                except:
                    self._logMsgList("exception").warning("", exc_info=1)
        if formatStr is None:
            self._logMsgList("format-missing").error("The message format is missing for message %s-%s-%s-%s", 
                                                      msg.category, msg.group, msg.severity, msg.code)
        elif re.sub("\[[^\]]*\]","%s",formatStr) != msg.text.replace("%d","%s").strip():
            self._logMsgList("format-mismatch").error("The message format (%s) for message %s-%s-%s-%s does not match the message text (%s)", 
                                                      formatStr, msg.category, msg.group, msg.severity, msg.code, msg.text.strip())
        return "%s-%s-%s-%s (state: %s):%s"%(msg.category, msg.group, msg.severity, msg.code, msg.getStateStr(), msg.devComment)

    def _filterMessages (self, msgsList, includeDeclared, includeActive):
        finalList = []
        for msg in msgsList:
            if msg.state == a.api.user_log.msg.message_base.MessageBase.STATE_DECLARED:
                if includeDeclared:
                    self._logMsgList("including-declared").debug4("message '%s-%s-%s-%s' is declared and will be included",
                                                                  msg.category, msg.group, msg.severity, msg.code)
                    finalList.append(msg)
                else:
                    self._logMsgList("skip-declared").debug4("message '%s-%s-%s-%s' is declared and will be skipped",
                                                             msg.category, msg.group, msg.severity, msg.code)

            elif msg.state == a.api.user_log.msg.message_base.MessageBase.STATE_ACTIVE:
                if not re.search("@version:[\s]*\d[\d]*\.\d[\d]*\.\d[\d]*\.\d[\d]*", msg.devComment):
                    self._logMsgList("no-version").error("message '%s-%s-%s-%s' is marked as active with no proper version (\d\.\d\.\d\.\d) set",
                                                         msg.category, msg.group, msg.severity, msg.code)
                if includeActive:
                    self._logMsgList("including-active").debug4("message '%s-%s-%s-%s' is active and will be included",
                                                                msg.category, msg.group, msg.severity, msg.code)
                    finalList.append(msg)
                else:
                    self._logMsgList("skip-active").debug4("message '%s-%s-%s-%s' is active and will be skipped",
                                                           msg.category, msg.group, msg.severity, msg.code)

        return finalList




