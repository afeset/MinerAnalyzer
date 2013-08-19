#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

G_NAME_MODULE_SYS_IPC_SIMPLE_SERVER = "ipc-simple-server"
G_NAME_GROUP_SYS_IPC_SIMPLE_SERVER_GENERAL = "general"
G_NAME_MODULE_SYS_IPC_SIMPLE_CLIENT = "ipc-simple-client"
G_NAME_GROUP_SYS_IPC_SIMPLE_CLIENT_GENERAL = "general"

import os
import time
import datetime
import threading
import shutil
import glob
import a.infra.format.json


class ReturnCode:
    SUCCESS = "success"
    APPLICATION_FAILURE = "application-failure"
    INVALID_COMMAND = "invalid-command"
    BAD_REQUEST = "bad-request"
    BAD_RESPONSE = "bad-response"
    COMMUNICATION_FAILURE = "communication-failure"
    

class _CommunicationUtils:
    OUR_DICT_KEY_VERSION                   = "version"
    OUR_DICT_KEY_CLIENT_ID                 = "client-id"
    OUR_DICT_KEY_COMMAND_NAME              = "command-name"
    OUR_DICT_KEY_REQUEST_APPLICATION_PARAMS  = "request-application-params"
    OUR_DICT_KEY_RESPONSE_APPLICATION_PARAMS = "response-application-params"
    OUR_DICT_KEY_SERVER_RETURN_CODE        = "server-return-code"

    OUR_VERSION = "1"
    OUR_SERVER_STATUS_COMMAND_NAME = "simple-ipc-server-status-internal-command-name"#long so it will not mix with any other cmd
    OUR_CLIENT_COUNTERS_COMMAND_NAME = "simple-ipc-client-counters-internal-command-name"#long so it will not mix with any other cmd
    OUR_CLIENT_COUNTERS_COMMAND_NAME_CLIENT_ID_KEY = "client-id"
    
    
    @classmethod
    def s_getRequestPath (cls, serverPath):
        __pychecker__="no-args"
        return os.path.join(serverPath, "request")

    @classmethod
    def s_getResponsePath (cls, serverPath):
        __pychecker__="no-args"
        return os.path.join(serverPath, "response")

    @classmethod
    def s_generateRequestFileName (cls, serverPath, clientId, dateTime, sequenceNumber):
        messageTimeStr = dateTime.strftime("%Y%m%d-%H%M%S.%f")
        fileBaseName = "%s-%s-%d.json"%(messageTimeStr, clientId, sequenceNumber)
        fileName = os.path.join(cls.s_getRequestPath(serverPath), fileBaseName)
        return fileName

    @classmethod
    def s_getResponseFileName (cls, serverPath, requestFileName):
        fileName = os.path.join(cls.s_getResponsePath(serverPath), os.path.basename(requestFileName))
        return fileName

    @classmethod
    def s_getRequestFileNameGlobPatternForClient (cls, serverPath, clientId):
        messageTimeStr = "????????-??????.??????"
        fileBaseName = "%s-%s-%s.json"%(messageTimeStr, clientId, "*")
        fileName = os.path.join(cls.s_getRequestPath(serverPath), fileBaseName)
        return fileName

    @classmethod
    def s_getRequestFileNameGlobPattern (cls, serverPath):
        return cls.s_getRequestFileNameGlobPatternForClient(serverPath, "*")


class RequestHandle:
    def __init__ (self, logger, clientId, serverPath, dateTime, sequenceNumber):
        self._log = logger.createLogger(G_NAME_MODULE_SYS_IPC_SIMPLE_CLIENT, G_NAME_GROUP_SYS_IPC_SIMPLE_CLIENT_GENERAL)
        self._clientId = clientId
        self._serverPath = serverPath
        self._sequenceNumber = sequenceNumber
        self._dateTime = dateTime
        self._returnCode = None
        self._reponseData = None

    def getResponse (self):
        #one of the ReturnCode values, or None if transaction did not complete       
        self._log("get-response").debug3("called")
        return self.poll()

    def poll (self):
        #one of the ReturnCode values, or None if transaction did not complete 
        #the response data is valid only if        
        if self._returnCode is None:
            self._log("poll-no-rc-yet").debug3("poll with no return code yet. trying to read values")
            self._poll()

        if self._returnCode is None:
            self._log("poll-return-none").debug3("poll returns none")
        else:
            self._log("poll-returns").debug1("poll returns value: rc=%s", self._returnCode)
            self._log("poll-returns-full").debug3("poll returns value: rc=%s, data=%s", 
                                                  self._returnCode, self._reponseData)
        return (self._returnCode, self._reponseData)

    def wait (self, timeout, testInterval = 0.1):
        """0 is sleep forever"""
        #kiss implementation
        if self._returnCode is None:
            self._log("wait-no-rc-yet").debug3("poll with no return code yet. trying to read values")
            self._poll()
        roundNum=0
        while self._returnCode is None:
            self._log("sleep-for-rc").debug5("sleeping for rc to be found. round=%d", roundNum)
            time.sleep(testInterval)      
            self._poll()      
            roundNum += 1
            if 0 < timeout <= roundNum*testInterval:                
                self._log("sleep-for-rc").debug1("wait reached timeout. round=%d", roundNum)
                break

        if self._returnCode is None:
            self._log("wait-return-none").debug3("wait returns none")
        else:
            self._log("wait-returns").debug1("wait returns value: rc=%s", self._returnCode)
            self._log("wait-returns-full").debug3("wait returns value: rc=%s, data=%s", 
                                                  self._returnCode, self._reponseData)
        return (self._returnCode, self._reponseData)


    def _send (self, commandName, parameters):
        self._commandName = commandName
        self._requestData = {_CommunicationUtils.OUR_DICT_KEY_VERSION: _CommunicationUtils.OUR_VERSION,
                             _CommunicationUtils.OUR_DICT_KEY_CLIENT_ID: self._clientId,
                             _CommunicationUtils.OUR_DICT_KEY_COMMAND_NAME: self._commandName,
                             _CommunicationUtils.OUR_DICT_KEY_REQUEST_APPLICATION_PARAMS: parameters}
        try:
            self._requestFileName = _CommunicationUtils.s_generateRequestFileName(self._serverPath, 
                                                                                  self._clientId, 
                                                                                  self._dateTime,
                                                                                  self._sequenceNumber)
            self._responseFileName = _CommunicationUtils.s_getResponseFileName(self._serverPath,
                                                                               self._requestFileName)
            self._log("sending").debug2("sending a message via file '%s': %s", 
                                        self._requestFileName, self._responseFileName)
            a.infra.format.json.writeToFile(self._log, self._requestData,
                                            self._requestFileName, tempFileName = "%s.tmp"%self._requestFileName, 
                                            mkdir=False, indent=4)
        except:
            self._log("sent-fail").exception("failed to send message %d ('%s') from client '%s'",
                                             self._sequenceNumber, self._commandName, self._clientId)
            self._returnCode = ReturnCode.COMMUNICATION_FAILURE


    def _poll (self):
        try:
            if not os.path.exists(self._responseFileName):
                self._log("no-response-yet").debug5("response file '%s' does not exists",self._responseFileName)
                return
            data = a.infra.format.json.readFromFile(self._log, self._responseFileName)
            self._log("data-read").debug3("data read %s",data)
        except:
            self._log("response-fail").exception("failed to get response for message %d ('%s')",
                                                 self._sequenceNumber, self._commandName)
            self._returnCode = ReturnCode.COMMUNICATION_FAILURE
            return

        try:
            self._returnCode  = data[_CommunicationUtils.OUR_DICT_KEY_SERVER_RETURN_CODE]
            if self._returnCode == ReturnCode.SUCCESS:
                self._reponseData = data[_CommunicationUtils.OUR_DICT_KEY_RESPONSE_APPLICATION_PARAMS]
        except:
            self._log("invalid-resonse").exception("failed to parse response for message %d ('%s'), data=%s",
                                                 self._sequenceNumber, self._commandName, data)
            self._returnCode = ReturnCode.BAD_RESPONSE
            return

        try:
            os.remove(self._responseFileName)
        except:
            self._log("failed-remove-res").warning("failed to remove response file '%s'",
                                                   self._responseFileName, exc_info=True)
            pass



class Client:
    def __init__ (self, logger, clientId, serverPath):
        self._log = logger.createLogger(G_NAME_MODULE_SYS_IPC_SIMPLE_CLIENT, 
                                        G_NAME_GROUP_SYS_IPC_SIMPLE_CLIENT_GENERAL, 
                                        instance = clientId)
        self._clientId = clientId
        self._serverPath = serverPath
        self._sequenceNumber = 0
        self._lock = threading.Lock()
        self._log("created").debug3("client created")

    def send (self, commandName, parameters):       
        self._lock.acquire()
        self._sequenceNumber += 1
        sequenceNumber = self._sequenceNumber
        dateTime = datetime.datetime.utcnow()
        self._lock.release()
        self._log("send").debug1("sending a message(%d) '%s': '%s'", sequenceNumber, commandName, parameters)
        requestHandle = RequestHandle(self._log, self._clientId, self._serverPath, dateTime, sequenceNumber)
        requestHandle._send(commandName, parameters)
        return requestHandle

    def getServerStatus (self, timeout):
        self._log("get-status").debug3("trying to get the server status")
        request = self.send(_CommunicationUtils.OUR_SERVER_STATUS_COMMAND_NAME, {})
       
        (rc, data) = request.wait(timeout)
        if rc != ReturnCode.SUCCESS:
            self._log("get-status-failed").warning("failed to get the server status, rc=%s", rc)
            return None
        try:
            status = ServerCounters()
            status.fromDict(data)
        except:
            self._log("get-status-failed-ex").exception("failed to get the server status")
            return None        
        return status

    def getServerClientCounters (self, timeout):
        self._log("get-status").debug3("trying to get the server client counters")
        request = self.send(_CommunicationUtils.OUR_CLIENT_COUNTERS_COMMAND_NAME, 
                            {_CommunicationUtils.OUR_CLIENT_COUNTERS_COMMAND_NAME_CLIENT_ID_KEY: self._clientId})
        (rc, data) = request.wait(timeout)
        if rc != ReturnCode.SUCCESS:
            self._log("get-status-failed").warning("failed to get the server status, rc=%s", rc)
            return None
        try:
            status = ServerCounters()
            status.fromDict(data)
        except:
            self._log("get-status-failed-ex").exception("failed to get the server status")
            return None        
        return status


class ServerCounters:
    _OUR_DICT_KEY_REQUEST_PROCESSED = "processed-requests"
    _OUR_DICT_KEY_REQUEST_SUCCESS   = "successful-requests"
    _OUR_DICT_KEY_REQUEST_FAILED    = "failed-requests"
    _OUR_DICT_KEY_RESPONSE_SUCCESS  = "successful-responses"
    _OUR_DICT_KEY_RESPONSE_FAILED   = "failed-responses"

    def __init__ (self):
        self.processedRequests = 0
        self.successfullRequests = 0
        self.failedRequests = 0
        self.successfullResponses = 0
        self.failedResponses = 0        

    def countRequest (self, success):
        self.processedRequests += 1
        if success:
            self.successfullRequests += 1
        else:
            self.failedRequests += 1
    
    def countResponse (self, success):
        if success:
            self.successfullResponses += 1
        else:
            self.failedResponses += 1

    def toDict(self):
        data = {}
        data[self._OUR_DICT_KEY_REQUEST_PROCESSED] = self.processedRequests
        data[self._OUR_DICT_KEY_REQUEST_SUCCESS  ] = self.successfullRequests
        data[self._OUR_DICT_KEY_REQUEST_FAILED   ] = self.failedRequests
        data[self._OUR_DICT_KEY_RESPONSE_SUCCESS ] = self.successfullResponses
        data[self._OUR_DICT_KEY_RESPONSE_FAILED  ] = self.failedResponses
        return data

    def fromDict(self, data):
        self.processedRequests    = data[self._OUR_DICT_KEY_REQUEST_PROCESSED]  
        self.successfullRequests  = data[self._OUR_DICT_KEY_REQUEST_SUCCESS  ]  
        self.failedRequests       = data[self._OUR_DICT_KEY_REQUEST_FAILED   ]  
        self.successfullResponses = data[self._OUR_DICT_KEY_RESPONSE_SUCCESS ]  
        self.failedResponses      = data[self._OUR_DICT_KEY_RESPONSE_FAILED  ]  


class Server:
    def __init__ (self, logger, serverName, serverPath):
        self._log = logger.createLogger(G_NAME_MODULE_SYS_IPC_SIMPLE_SERVER, 
                                        G_NAME_GROUP_SYS_IPC_SIMPLE_SERVER_GENERAL,
                                        instance = serverName)
        self._serverPath = serverPath
        self._commands = {}
        self._serverName = serverName
        self._shallRun = True
        self._perClientCounters = {}
        self._processingThread = None
        self._overAllCounter = ServerCounters()


    def initAddCommand (self, commandName, callable):#init as it is not protected by a lock
        #function throws an exception if failed
        if commandName in self._commands:
            a.infra.process.processFatal("trying to re-add command '%s'. new '%s', prev '%s'", 
                                         commandName, callable, self._commands[commandName])
            pass
        self._log("adding-command").debug1("add command '%s: '%s'", commandName, callable)
        self._commands[commandName] = callable

    def initRemoveCommand (self, commandName):#init as it is not protected by a lock
        if not commandName in self._commands:
            self._log("remove-no-command").warning("trying remove inexisting command '%s: '%s'", commandName)
            return
        self._log("remove-command").debug1("remove command '%s: '%s'", commandName)
        self._commands.pop(commandName)

    def init (self):
        try:
            if os.path.exists(self._serverPath):
                self._log("init-server-rmdir").debug1("remove server existing directory '%s", self._serverPath)
                shutil.rmtree(self._serverPath)
            os.makedirs(_CommunicationUtils.s_getResponsePath(self._serverPath))
            os.makedirs(_CommunicationUtils.s_getRequestPath(self._serverPath))
        except:
            a.infra.process.processFatal("Failed to init server")

        def getServerStatus(data):
            __pychecker__="no-args"
            return self.getServerStatus().toDict()
        self.initAddCommand(_CommunicationUtils.OUR_SERVER_STATUS_COMMAND_NAME, getServerStatus)

        def getClientCounters(data):
            return self.getClientCounters(data[_CommunicationUtils.OUR_CLIENT_COUNTERS_COMMAND_NAME_CLIENT_ID_KEY]).toDict()
        self.initAddCommand(_CommunicationUtils.OUR_CLIENT_COUNTERS_COMMAND_NAME, getClientCounters)

    def processNextRequest (self):        
        requestFile = self._getNextRequest()
        if requestFile is None:
            self._log("no-pend-req").debug5("no pending request")
            return
        self._log("found-request").debug3("Found pending request '%s'", requestFile)
        self._processRequest(requestFile)        

    def stop (self):
        self._log("shall-stop").info("marked to stop")
        self._shallRun = False

    def processMessages (self):
        self._log("start").info("start processing messages")
        self._shallRun = True
        while self._shallRun:
            requestFile = self._getNextRequest()
            if requestFile is None:
                self._log("no-pend-req").debug5("no request found. sleeping")
                time.sleep(0.1)
            else:
                self._log("found-request").debug3("Found pending request '%s'", requestFile)
                self._processRequest(requestFile)                


    def start (self):
        self._processingThread = self._ProcessingThread(self)
        self._processingThread.start()

    def join (self, timeout):
        """
        wait for the processing theard to exit. Use None for "wait for ever"
        """
        if self._processingThread is None:
            self._log("join-none").warning("join with no processing thread active")
            return
        self._processingThread.join(timeout)
        if self._processingThread.isAlive():
            self._log("join-failed").error("processing thread is still alive (join timeout)")

    def getServerStatus (self):
        return self._overAllCounter

    def getClientCounters (self, clientId):
        if clientId not in self._perClientCounters:
            self._perClientCounters[clientId] = ServerCounters()
        return self._perClientCounters[clientId]

    def _countRequest (self, clientId, success):
        self._overAllCounter.countRequest(success)
        if clientId is not None:
            if clientId not in self._perClientCounters:
                self._perClientCounters[clientId] = ServerCounters()
            self._perClientCounters[clientId].countRequest(success)

    def _countResponse (self, clientId, success):
        self._overAllCounter.countResponse(success)
        if clientId is not None:
            if clientId not in self._perClientCounters:
                self._perClientCounters[clientId] = ServerCounters()
            self._perClientCounters[clientId].countResponse(success)

    def _getNextRequest (self):
        try:
            requests = sorted(glob.glob(_CommunicationUtils.s_getRequestFileNameGlobPattern(self._serverPath)))
        except:
            #error
            return
        if len(requests)==0:
            return None
        return requests[0]

    def _clearRequest (self, requestFile):
        try:
            os.remove(requestFile)
        except:
            if os.path.exists(requestFile):
                a.infra.process.processFatal("Server '%s' failed to remove request file '%s'", self._serverName, requestFile)
            else:
                self._log("exception-deleting").warning("exception while deleting request file '%s'", requestFile, exc_info=True)

    def _processRequest (self, requestFile):
        self._log("process-request").debug3("processing request file '%s'", requestFile)
        responseFile = _CommunicationUtils.s_getResponseFileName(self._serverPath, requestFile)
        clientName = None
        data = None
        try:
            data = a.infra.format.json.readFromFile(self._log, requestFile)
        except:
            self._log("failed-read-request").exception("failed to read request file '%s'", requestFile)
            responseData = {_CommunicationUtils.OUR_DICT_KEY_SERVER_RETURN_CODE: ReturnCode.BAD_REQUEST}
            self._sendResponse(clientName, responseFile, responseData)
            self._clearRequest(requestFile)
            self._countRequest(clientName, False)
            return

        self._clearRequest(requestFile)
        
        try:
            clientName = data[_CommunicationUtils.OUR_DICT_KEY_CLIENT_ID]
            commandName = data[_CommunicationUtils.OUR_DICT_KEY_COMMAND_NAME]
            requestParams = data[_CommunicationUtils.OUR_DICT_KEY_REQUEST_APPLICATION_PARAMS]
        except:
            self._log("invalid-file").exception("invalid data read from file '%s': %s", requestFile, data)
            responseData = {_CommunicationUtils.OUR_DICT_KEY_SERVER_RETURN_CODE: ReturnCode.BAD_REQUEST}
            self._sendResponse(clientName, responseFile, responseData)
            self._clearRequest(requestFile)
            self._countRequest(clientName, False)
            return

        if not commandName in self._commands:
            self._log("no-such-command").error("got invalid command '%s' in request file '%s'", commandName, requestFile)
            responseData = {_CommunicationUtils.OUR_DICT_KEY_SERVER_RETURN_CODE: ReturnCode.INVALID_COMMAND}
            self._sendResponse(clientName, responseFile, responseData)
            self._countRequest(clientName, False)
            return

        command = self._commands[commandName]#assuming the self._commands does not change
        try:
            responseParams = command(requestParams)
        except:            
            self._log("application-failed").exception("application failed to run command '%s' from file '%s'", commandName, requestFile)
            responseData = {_CommunicationUtils.OUR_DICT_KEY_SERVER_RETURN_CODE: ReturnCode.APPLICATION_FAILURE}
            self._sendResponse(clientName, responseFile, responseData)
            self._countRequest(clientName, False)
            return

        responseData = {_CommunicationUtils.OUR_DICT_KEY_SERVER_RETURN_CODE: ReturnCode.SUCCESS,
                        _CommunicationUtils.OUR_DICT_KEY_RESPONSE_APPLICATION_PARAMS: responseParams}
        self._log("success").debug2("great success: command '%s' from file '%s'", commandName, requestFile)
        self._sendResponse(clientName, responseFile, responseData)
        self._countRequest(clientName, True)
        return

    def _sendResponse (self, clientName, responseFile, responseData):
        try:
            a.infra.format.json.writeToFile(self._log, responseData,
                                            responseFile, tempFileName = "%s.tmp"%responseData, 
                                            mkdir=False, indent=4)
        except:
            self._log("sent-fail").exception("failed to send response '%s'", responseFile)
            self._countResponse(clientName, False)
            return

        self._countResponse(clientName, True)

    class _ProcessingThread(threading.Thread):
         def __init__ (self, server):
             threading.Thread.__init__(self)
             self.daemon = True
             self._server = server

         def run(self):
             self._server.processMessages()

