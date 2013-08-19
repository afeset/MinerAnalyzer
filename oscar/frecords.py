import m.common
from m.io_targets.log_stream import iRaw, oRaw

class FRecord:
    VERSION_UNKNOWN = 0
    VERSION_2_5 = 250
    VERSION_2_7 = 270
    VERSION_PRE_3_0 = 290
    VERSION_3_0 = 300
    def __init__(self, words, version):
        self._flags = None
        if isinstance(version, str):
            self.version = FRecord.convertVersionString(version)
        else:
            self.version = version
        
        if self.version == FRecord.VERSION_2_5: 
            self.convert_2_5(words)
        elif self.version == FRecord.VERSION_2_7: 
            self.convert_2_7(words)
        elif self.version == FRecord.VERSION_PRE_3_0:
            self.convert_pre_3_0(words)
        elif self.version == FRecord.VERSION_3_0:
            self.convert_3_0(words)
        else:
            raise m.common.MiningError("Invalid FRecord version: %s: %d" % (version, self.version))
    
    @staticmethod
    def convertVersionString(version):
        if version <= "2.7" or version.startswith("2.7"):
            return FRecord.VERSION_2_5 
        elif version < "3.":
            return FRecord.VERSION_PRE_3_0
        else:
            return FRecord.VERSION_3_0
    
    @staticmethod
    def isValid(words, version):
        if words[0] != "F":
            return False
        if version == FRecord.VERSION_2_5:
            if len(words) >= 36:
                return True
            else:
                return False
        elif version == FRecord.VERSION_2_7:
            if len(words) >= 39:
                return True
            else:
                return False
        elif version == FRecord.VERSION_PRE_3_0:
            if len(words) >= 46:
                return True
            else:
                return False
        elif version == FRecord.VERSION_3_0:
            if len(words) >= 49:
                return True
            else:
                return False
        else:
            raise m.common.MiningError("Invalid FRecord version: %s" % version)
    
    @staticmethod
    def determineVersion(words):
        if words[0] != "F":
            return FRecord.VERSION_UNKNOWN
        l = len(words)
        if 36 <= l < 39:
            return FRecord.VERSION_2_5
        elif l < 46:
            return FRecord.VERSION_2_7
        elif l == 46:
            return FRecord.VERSION_PRE_3_0
        elif l == 49:
            return FRecord.VERSION_3_0
        else:
            return FRecord.VERSION_UNKNOWN
        
    def _convert_2_5_iter(self, word):
        self.F = word.next()
        self.timeofday = int(word.next())
        self.nanosec = int(word.next())
        self.flowId = int(word.next())
        self.srcIP = word.next()
        self.srcPort = int(word.next())
        self.destIP = word.next()
        self.destPort = int(word.next())
        self.initiatorPortNumber = int(word.next())
        self.responderL2BytesPort0 = int(word.next())
        self.responderL2BytesPort1 = int(word.next())
        self.downloadedContentBytesPort0 = int(word.next())
        self.downloadedContentBytesPort1 = int(word.next())
        self.downloadTimeMsec = int(word.next())
        self.viewTimeMsec = int(word.next())
        self.contentLength = int(word.next())
        self.contentChecksum = word.next()
        self.checksum1Kto10K = word.next()
        self.cid = word.next()
        self.cgid = int(word.next())
        self.beginOffset = int(word.next())
        self.contentType = word.next()
        self.host = word.next()
        self.path = word.next()
        self.isCachable = (word.next()!="0")
        self.isDelivered = (word.next()!="0")
        self.isViewSession = (word.next()!="0")
        self.sessionHitCount = int(word.next()) #for long transactions with multiple reports
        self.sessionId = word.next()
        if self.version == FRecord.VERSION_2_5:
            self.isContinues = (word.next()!="0")
            self.isStart = not self.isContinues
            self.isEnd = False
        else:
            continues = int(word.next())
            self.isStart = (continues&1) != 0
            self.isEnd = continues&2 != 0
            self.isContinues = not self.isStart 
        self.unixStartTime = int(word.next())
        self.httpRequestRange = word.next()
        self.httpResponseRange = word.next()
        self.origHostName = word.next()
        self.wasRedirected = (word.next()!="0")
        self.origin = word.next()

    def _convert_2_7_iter(self, word):
        self._convert_2_5_iter(word)
        self.initialBurstBwKbps = int(word.next())
        self.initialBurstSizeKB = int(word.next())
        self.sustainedBwKbps = int(word.next())
        
    def _convert_pre_3_0_iter(self, word):
        self._convert_2_7_iter(word)
        self.signatureName = word.next()
        self.transactionDownloadedContentBytesPort0 = int(word.next())
        self.transactionDownloadedContentBytesPort1 = int(word.next())
        self.transactionDownloadTimeMsec = int(word.next())
        self.cdnId = int(word.next())
        self.llnwdLocation = word.next()
        self.titleId = word.next()
            
    class Flags:
        def __init__(self, debugFlags):
            self._flags = debugFlags
            #-----------------------------------------
            self.mySawHttpResponse = self.nextBit()
            self.noCidOnRequest = self.nextBit()
            self.isAcquired = self.nextBit()
            self.myAcqIsBroken = self.nextBit()

            self.wasPipeLineDetected = self.nextBit()
            self.hadResponseTokensValidationIncident = self.nextBit()
            self.hadTitleLenValidationIncident = self.nextBit()
            self.hadChecksumValidationConflict = self.nextBit()

            self.hadCgidValidationConflict = self.nextBit()
            self.noRedirRequestNotValid = self.nextBit()
            self.noAcqResponseNotValid = self.nextBit()
            self.noRedirUriOffsetInMilisec = self.nextBit()

            self.noRedirByDigest = self.nextBit()
            self.loadFromLruCidNotFound = self.nextBit()
            self.noAcqFromDigest = self.nextBit()
            self.isContentLengthUnkown = self.nextBit()

            self.isTransferChunked = self.nextBit()
            self.isConnectionClose = self.nextBit()
            self.isEncodingCompressed = self.nextBit()
            self.isChunkedLostSync = self.nextBit()

            self.isCachable = self.nextBit()
            self.sessionHitcoutIndication = self.nextBit()  
            self.pipelineType = self.next2Bits()
           
            self.myAcqInProgress = self.nextBit()     

        def nextBit(self):
            flag = ((self._flags&1) != 0)
            self._flags >>= 1
            return flag
        def next2Bits(self):
            bits = self._flags&3
            self._flags >>= 2
            return bits
    @property
    def flags(self):
        if not self._flags:
            self._flags = FRecord.Flags(self.debugFlags)
        return self._flags

    def _convert_3_0_iter(self, word):
        self.sessionId = word.next()
        self.sessionIdExtractorIndex = int(word.next())
        self.debugFlags = int(word.next(), 16)
        
    def convert_2_5(self, words):
        word = iter(words)
        self._convert_2_5_iter(word)
        # fill some fields from future versions with default values
        self.titleId = self.intCid
    
    def convert_2_7(self, words):
        word = iter(words)
        self._convert_2_7_iter(word)
        # fill some fields from future versions with default values
        self.titleId = self.intCid
    
    def convert_pre_3_0(self, words):
        word = iter(words)
        self._convert_pre_3_0_iter(word)
 
    def convert_3_0(self, words):
        word = iter(words)
        self._convert_3_0_iter(word)

    def dumps(self):
        values = ["F"]
        values.append(str(self.timeofday))
        values.append(str(self.nanosec))
        values.append(str(self.flowId))
        values.append(self.srcIP)
        values.append(str(self.srcPort))
        values.append(self.destIP)
        values.append(str(self.destPort))
        values.append(str(self.initiatorPortNumber))
        values.append(str(self.responderL2BytesPort0))
        values.append(str(self.responderL2BytesPort1))
        values.append(str(self.downloadedContentBytesPort0))
        values.append(str(self.downloadedContentBytesPort1))
        values.append(str(self.downloadTimeMsec))
        values.append(str(self.viewTimeMsec))
        values.append(str(self.contentLength))
        values.append(self.contentChecksum)
        values.append(self.checksum1Kto10K)
        values.append(self.cid)
        values.append(str(self.cgid))
        values.append(str(self.beginOffset))
        values.append(self.contentType)
        values.append(self.host)
        values.append(self.path)
        values.append("1" if self.isCachable else "0" )
        values.append("1" if self.isDelivered else "0" )
        values.append("1" if self.isViewSession else "0" )
        values.append(str(self.sessionHitCount))
        values.append(str(self.sessionId))
        if self.version >= FRecord.VERSION_PRE_3_0:
            v = 0
            if self.isStart:
                v |= 1
            if self.isEnd:
                v |= 2
            values.append(str(v))
        else:
            values.append("1" if self.isContinues else "0")
        values.append(str(self.unixStartTime))
        values.append(self.httpRequestRange)
        values.append(self.httpResponseRange)
        values.append(self.origHostName)
        values.append("1" if self.wasRedirected else  "0")
        values.append(self.origin)
        if self.version >= FRecord.VERSION_2_7:
            values.append(str(self.initialBurstBwKbps))
            values.append(str(self.initialBurstSizeKB))
            values.append(str(self.sustainedBwKbps))
            if self.version >= FRecord.VERSION_PRE_3_0:
                values.append(self.signatureName)
                values.append(str(self.transactionDownloadedContentBytesPort0))
                values.append(str(self.transactionDownloadedContentBytesPort1))
                values.append(str(self.transactionDownloadTimeMsec))
                values.append(str(self.cdnId))
                values.append(self.llnwdLocation)
                values.append(str(self.titleId) if self.titleId!=0 else '')
                if self.version >= FRecord.VERSION_3_0:
                    values.append(str(self.sessionId))
                    values.append(str(self.sessionIdExtractorIndex))
                    values.append(hex(self.debugFlags))
        return "\t".join(values)
    
    def __repr__(self):
        return self.dumps()

    @property
    def responderL2Bytes(self):
        return self.responderL2BytesPort0 + self.responderL2BytesPort1
    
    @property
    def downloadedContentBytes(self):
        return self.downloadedContentBytesPort0 + self.downloadedContentBytesPort1

    @property
    def transactionDownloadedContentBytesPort(self):
        return self.transactionDownloadedContentBytesPort0 + self.transactionDownloadedContentBytesPort1

    @property
    def intCid(self):
        return int(self.cid,16)

    def __str__(self):
        import m.runtime
        cachable = "C" if self.isCachable else "-"
        delivered = "D" if self.isDelivered else "-"
        view = "V" if self.isViewSession else "-"
        redir = "R" if self.wasRedirected else "-"
        zeroLog = "n" if self.isContinues else "0"
        s = "%s %s %s:%d->%s:%d flowId=%d http://%s%s downloaded=%d responderL2=%d cid=%s cgid=%d range=%s flags=%s%s%s%s%s" % (
             m.runtime.gmtime2a(self.unixStartTime), self.origin, self.srcIP, self.srcPort, self.destIP, self.destPort,
             self.flowId, self.origHostName, self.path, self.downloadedContentBytes, self.responderL2Bytes,
             self.cid, self.cgid, self.httpRequestRange,
             cachable, delivered, view, redir, zeroLog)
        return s

    def isFlat(self):
        return self.path == "Flat"

    def byDelivery(self):
        return self.origin.startswith("d")

    def byLine(self):
        return self.origin.startswith("v")

class iFrecordTarget(iRaw):
    def __init__(self, fileHandler, version=None):
        iRaw.__init__(self, fileHandler)
        self.version = version

    def next(self):
        while True:
            record = iRaw.next(self)
            line = record[0]
            words = line.split("\t")
            if not self.version:
                version = FRecord.determineVersion(words)
                if version == FRecord.VERSION_UNKNOWN:
                    continue
                return (FRecord(words, version),)
            else:
                vesion = self.version
            if FRecord.isValid(words, version):
                return (FRecord(words, version),)

    def getVariableNames(self):
        return ["frecord"]

class oFrecordTarget(oRaw):
    def __init__(self, fileName, variableNames):
        oRaw.__init__(self, fileName, variableNames)
        self.frecordIndex = self.myVars.index("frecord")
        if self.frecordIndex == -1:
            raise m.common.InvalidOutputVariables("frecord stream requires frecord varable at output")
    def recordToString(self, record):
        return record[self.frecordIndex].dumps() + "\n"

def parseUriFromFrecord(frecord):
    from m.http import Uri
    return Uri(frecord.path)

import zlib
from collections import deque

class FRecordsAccumulator:
    def __init__(self, timeout = 120):
        self.orderedByDelivery = deque()
        self.recordsByDelivery = {}
        self.orderedByLine = deque()
        self.recordsByLine = {}
        self.timeout = timeout*1000*1000*1000
    def accumulate(self, frecord):
        if frecord.byDelivery():
            ordered = self.orderedByDelivery
            records = self.recordsByDelivery
        else:
            ordered = self.orderedByLine
            records = self.recordsByLine
        # ignore flat records
        if frecord.isFlat() or frecord.cid=="0" or frecord.cid=="0x0":
            return [frecord]
        keyStr =  "%s:%d %s %d %s %s" % \
             (frecord.srcIP, frecord.srcPort, frecord.destIP, frecord.beginOffset, frecord.cid, frecord.httpRequestRange) #zlib.adler32(frecord.path + " " + frecord.httpRequestRange))
        key = zlib.adler32(keyStr)
        curTime = frecord.nanosec
        existing = records.get(key, None)
        if existing:
            existing.responderL2BytesPort0 += frecord.responderL2BytesPort0
            existing.responderL2BytesPort1 += frecord.responderL2BytesPort1
            existing.downloadedContentBytesPort0 += frecord.downloadedContentBytesPort0
            existing.downloadedContentBytesPort1 += frecord.downloadedContentBytesPort1
            existing.downloadTimeMsec += frecord.downloadTimeMsec
            existing.viewTimeMsec += frecord.viewTimeMsec
            existing.lastSeenNanosec = curTime
            existing.timeofday = frecord.timeofday
        else:
            if frecord.isContinues:
                # accumulation starts from first record in transaction
                return [frecord]
            frecord.lastSeenNanosec = curTime
            records[key] = frecord
            
        res = []
        while len(ordered) and (curTime-ordered[0][0])>self.timeout:
            seenTime, seenKey = ordered.popleft()
            stored = records[seenKey]
            if stored.lastSeenNanosec == seenTime:
                res.append(stored)
                del records[seenKey]
        ordered.append( (curTime, key) )
        return res
    
    def finish(self):
        return sorted(self.recordsByDelivery.values()+self.recordsByLine.values(),key=lambda r: r.lastSeenNanosec)

