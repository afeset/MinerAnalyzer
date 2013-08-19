from a.infra.gpb.chain import *

from include.a.line.report.coal_report_pb2 import CoalRecordGpb

from infra.log.msg_data_pb2 import MsgDataGpb
from line.va.transaction_pb2 import TransactionSummaryGpb

from miner_globals import isScriptParameterDefined

# To be added if we ever want to actually processe these messages
#
#from line.va.acquisition_manager_pb2 import AcquisitionSummaryGpb
#from line.va.acquisition_manager_pb2 import Acqm_DiskUsageGpb
#from line.va.line_pb2 import Line_StatusGbp

import time

from m.common import *

class InvalidType(InvalidInputFiles):
    def __init__(self, expectedTypeName):
        self.expectedTypeName = expectedTypeName
    def __str__(self):
        return "isinstance failed - expected: %s" % self.expectedTypeName

class NotLastRecord(InvalidInputFiles):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "%s is not last record in chain" % self.name

class iQdl(GeneratorBase):
    def __init__(self, fileHandler, attachmentTypes=None):
        GeneratorBase.__init__(self)
        self.myFileHandler = fileHandler
        self.myIChain = ifGPBChain(self.myFileHandler)
        self.myIChain.addFactoryMessage(MsgDataGpb())
        if attachmentTypes:
            for a in attachmentTypes:
                self.myIChain.addFactoryMessage(a())
    def close(self):
        self.myFileHandler.close()
    def __iter__(self):
        return self
    def next(self):
        msgData = self.myIChain.next()
        if not isinstance(msgData, MsgDataGpb):
            print msgData
            raise InvalidType("MsgDataGpb")
        attachments = []
        while not self.myIChain.isLastMessageInChain():
            try:
                nextMsg = self.myIChain.next()
                attachments.append(nextMsg)
            except:
                pass

        return (msgData, attachments)

    def getVariableNames(self):
        return ["msgData", "attachments"]

class iQblTargetBase(GeneratorBase):
    def __init__(self, fileHandler, varName, classObject, raiseException=False):
        GeneratorBase.__init__(self)
        self.myFileHandler = fileHandler
        self.myClassObject = classObject
        self.myVarName = varName
        self.myRaiseException = raiseException
        self.myIChain = ifGPBChain(self.myFileHandler)
        self.myIChain.addFactoryMessage(MsgDataGpb())
        self.myIChain.addFactoryMessage(self.myClassObject())
    def close(self):
        self.myFileHandler.close()
    def __iter__(self):
        return self
    def next(self):
        # Read all messages in chain. Skip invalid chains.
        # - If an UnknownGPBMessageException is raised: chain is invalid, skip it.
        # - If chain size != 2, chain is invalid
        # - If first chain element is not MsgDataGpb, raise InvalidType
        # 
        # A loop iteration reads a complete chain, loop used to skips invalid chains
        while True:
            try:
                msgData = self.myIChain.next()
            except NotCompleteMessageException as e:
                print e
                raise StopIteration 
            # If first chain element is not MsgDataGpb, it is a severe error
            if not isinstance(msgData, MsgDataGpb):
                print msgData
                raise InvalidType("MsgDataGpb")

            second=None
            numMessages=1
            unknownFound=False
            # keep reading chain until last
            while not self.myIChain.isLastMessageInChain():
                try:
                    record=self.myIChain.next()
                    # Remember second record
                    if not second:
                        second=record
                except UnknownGPBMessageException:
                    if self.myRaiseException:
                        raise InvalidType(self.myClassObject.__name__)
                    else:
                        unknownFound=True
                except NotCompleteMessageException as e:
                    print e
                    raise StopIteration
                numMessages += 1

            # We finished reading the chain. Skip invalid chains
            if (numMessages != 2) or unknownFound:
                continue

            # Return the second message found in chain
            return (msgData, second)

    def getVariableNames(self):
        return ["msgData", self.myVarName]

class iCoal(iQblTargetBase):
    def __init__(self, fileHandler, headers=None):
        iQblTargetBase.__init__(self, fileHandler, "coal", CoalRecordGpb, raiseException=True)

class iTransaction(iQblTargetBase):
    def __init__(self, fileHandler, headers=None):
        iQblTargetBase.__init__(self, fileHandler, "transaction", TransactionSummaryGpb, raiseException=False)

class oCoal:
    def __init__(self, fileName, variableNames):
        self.myFileName = fileName
        self.myFileHandler = open(fileName, "wb")
        self.myVars = variableNames
        self.myCoalId = self.myVars.index("coal")
        self.myOChain = ofGPBChain(self.myFileHandler)
        self.myMsgCnt = 1

    def save(self, record):
        coal = record[self.myCoalId]
        msgData = MsgDataGpb()
        msgData.myModule = "line"
        msgData.myGroup = "coal"
        msgData.myName = "coal-record"
        msgData.mySourceFileName = "miner/io_targets/qbl_coal.py"
        msgData.mySourceLineNumber = 66
        msgData.mySourceFunctionName = "save()"
        #msgData.myLogLevel = kNotice
        msgData.myMsgIdSequenceNumber = self.myMsgCnt
        msgData.myGlobalSequenceNumber = self.myMsgCnt
        msgData.myTimeOfDayGmtNanoseconds = int(time.time()*1000*1000*1000)
        msgData.myTimeOfDayGmtOffsetMinutes = time.altzone/60
        msgData.myTimeMonotonicNanoseconds = int(time.clock()*1000*1000*1000)
        msgData.myBody = "%GPB"
        msgData.myThreadId = 0
        msgData.myThreadFullName = "miner"
        msgData.myThreadShortName = "miner"
        msgData.myProcessName = "miner"
        msgData.myInstanceName = ""
        msgData.myErrno = 0
        msgData.myMsgIdDropCounter = 0
        msgData.myGlobalDropCounter = 0
        self.myMsgCnt += 1

        self.myOChain.append(msgData);
        self.myOChain.append(coal, isLast=True)

    def close(self):
        self.myFileHandler.close()

class oGPBChain:
    def __init__(self, fileName, variableNames):
        self.myFileName = fileName
        self.myFileHandler = open(fileName, "wb")
        self.myVars = variableNames
        self.myOChain = ofGPBChain(self.myFileHandler)
        self.myMsgCnt = 1

    def save(self, record):
        self.myMsgCnt += 1
        recordLen = len(record)
        for i in range(len(record)):
            self.myOChain.append(record[i], isLast=(i==recordLen-1));

    def close(self):
        self.myFileHandler.close()

def parseRequestFromCoal(coal):
    import m.http
    try:
        if coal.HasField("request"):
            return m.http.HttpRequest(coal.request.body)
        else:
            return None
    except:
        if isScriptParameterDefined("IGNORE_HTTP_PARSE_ERRORS"):
            return None
        else:
            raise

def parseResponseFromCoal(coal):
    import m.http
    try:
        if coal.HasField("response"):
            return m.http.HttpResponse(coal.response.body)
        else:
            return None
    except:
        if isScriptParameterDefined("IGNORE_HTTP_PARSE_ERRORS"):
            return None
        else:
            raise

