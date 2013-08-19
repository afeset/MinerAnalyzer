
# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: royr
#
# This module holds common records utils for topper and pre-topper. any changes to records fields should be done here.

import os

__pychecker__="no-reuseattr"

MIN_FIELDS_IN_RECORD = 6
DATA_SUB_FOLDER_AND_HEADER_NAME = "vidTransactions"

# make an int variable referenced and not copied
class NumObject:
    myVal = -1
    def __init (self):
        self.myVal = -1


class LogMessageOffsets:
    theMessageOffset = NumObject()

    @staticmethod
    def getOffsets():
        return {"msg":LogMessageOffsets.theMessageOffset}


# Flow records access offsets
class FlowRecordOffsets(object):
    theTimeOfDayOffset = NumObject()
    theSrcIpOffset = NumObject()
    theResponderL2BytesPort0Offset = NumObject()
    theResponderL2BytesPort1Offset = NumObject()
    theDownloadedContentBytesPort0Offset = NumObject()
    theDownloadedContentBytesPort1Offset = NumObject()
    theContentLengthOffset = NumObject()
    thechecksum1Kto10KOffset = NumObject()
    theCidOffset = NumObject()
    theCgidOffset = NumObject()
    theContentTypeOffset = NumObject()
    theHostOffset = NumObject()
    thePathOffset = NumObject()
    theDownloadTimeMsec = NumObject()
    theViewTimeMsec = NumObject()
    theInitiatorPortNumber = NumObject()
    theIsCachableIndicator = NumObject()
    theSessionHitCount  = NumObject()
    theBeginOffset = NumObject()
    theIsDeliveredIndicator = NumObject()
    theAggregationIdOffset = NumObject()
    theTransactionSegmentOffset = NumObject()
    theUnixStartTime = NumObject()
    theHttpRequestRange = NumObject()
    theHttpResponseRange = NumObject()
    #theOrigHostName = NumObject()
    theWasRedirected = NumObject()
    theOrigin = NumObject()
    theOrigHostNameOffset = NumObject()
    thePathOffset = NumObject()
    theSignatureNameOffset = NumObject()
    theTransactionDownloadedContentBytesPort0Offset = NumObject()
    theTransactionDownloadedContentBytesPort1Offset = NumObject()
    theTransactionDownloadTimeMsecOffset = NumObject()
    theCdnIdOffset = NumObject()
    theLlnwdLocationOffset = NumObject()
    theInitialBurstBwKbps = NumObject()
    theInitialBurstSizeKB = NumObject()
    theSustainedBwKbps = NumObject()
    theTitleIdOffset = NumObject()
    theSessionIdOffset = NumObject()
    theSessionIdExtractorIndexOffset = NumObject()
    maxOffset = NumObject()

    @staticmethod
    def getOffsets():
        return {"timeofday":FlowRecordOffsets.theTimeOfDayOffset,
                "srcIP":FlowRecordOffsets.theSrcIpOffset, 
                "responderL2BytesPort0":FlowRecordOffsets.theResponderL2BytesPort0Offset, # L2
                "responderL2BytesPort1":FlowRecordOffsets.theResponderL2BytesPort1Offset, # L2
                "downloadedContentBytesPort0":FlowRecordOffsets.theDownloadedContentBytesPort0Offset, # L7
                "downloadedContentBytesPort1":FlowRecordOffsets.theDownloadedContentBytesPort1Offset, # L7
                "downloadTimeMsec":FlowRecordOffsets.theDownloadTimeMsec,
                "viewTimeMsec":FlowRecordOffsets.theViewTimeMsec,
                "contentLength":FlowRecordOffsets.theContentLengthOffset, 
                "checksum1Kto10K":FlowRecordOffsets.thechecksum1Kto10KOffset ,
                "cid":FlowRecordOffsets.theCidOffset,
                "cgid":FlowRecordOffsets.theCgidOffset,
                "contentType":FlowRecordOffsets.theContentTypeOffset,
                "host":FlowRecordOffsets.theHostOffset,
                "path":FlowRecordOffsets.thePathOffset,
                "initiatorPortNumber":FlowRecordOffsets.theInitiatorPortNumber,
                "isCachable":FlowRecordOffsets.theIsCachableIndicator,
                "sessionHitCount" :FlowRecordOffsets.theSessionHitCount,
                "beginOffset":FlowRecordOffsets.theBeginOffset,
                "isDelivered" :FlowRecordOffsets.theIsDeliveredIndicator,
                "aggregationId":FlowRecordOffsets.theAggregationIdOffset,
                "unixStartTime":FlowRecordOffsets.theUnixStartTime ,
                "httpRequestRange":FlowRecordOffsets.theHttpRequestRange,
                "httpResponseRange":FlowRecordOffsets.theHttpResponseRange,
                "wasRedirected":FlowRecordOffsets.theWasRedirected,
                "origin":FlowRecordOffsets.theOrigin,
                "origHostName":FlowRecordOffsets.theOrigHostNameOffset,
                "path":FlowRecordOffsets.thePathOffset,
                "signatureName":FlowRecordOffsets.theSignatureNameOffset,
                "transactionDownloadedContentBytesPort0":FlowRecordOffsets.theTransactionDownloadedContentBytesPort0Offset,
                "transactionDownloadedContentBytesPort1":FlowRecordOffsets.theTransactionDownloadedContentBytesPort1Offset,
                "transactionDownloadTimeMsec":FlowRecordOffsets.theTransactionDownloadTimeMsecOffset,
                "transactionSegment":FlowRecordOffsets.theTransactionSegmentOffset,
                "cdnId":FlowRecordOffsets.theCdnIdOffset,
                "llnwdLocation":FlowRecordOffsets.theLlnwdLocationOffset,
                "initialBurstBwKbps":FlowRecordOffsets.theInitialBurstBwKbps,
                "initialBurstSizeKB":FlowRecordOffsets.theInitialBurstSizeKB,
                "sustainedBwKbps":FlowRecordOffsets.theSustainedBwKbps,
                "titleId":FlowRecordOffsets.theTitleIdOffset,
                "sessionId":FlowRecordOffsets.theSessionIdOffset,
                "sessionIdExtractorIndex":FlowRecordOffsets.theSessionIdExtractorIndexOffset,
                "maxOffset":FlowRecordOffsets.maxOffset}


    # Call only after loading records offests
    @staticmethod
    def getTokensIndexesToParseToInt():
        tokens = []
        tokens.append(FlowRecordOffsets.theResponderL2BytesPort0Offset.myVal)
        tokens.append(FlowRecordOffsets.theResponderL2BytesPort1Offset.myVal)
        tokens.append(FlowRecordOffsets.theDownloadedContentBytesPort0Offset.myVal)
        tokens.append(FlowRecordOffsets.theDownloadedContentBytesPort1Offset.myVal)
        tokens.append(FlowRecordOffsets.theDownloadTimeMsec.myVal)
        tokens.append(FlowRecordOffsets.theViewTimeMsec.myVal)
        tokens.append(FlowRecordOffsets.theContentLengthOffset.myVal)
        tokens.append(FlowRecordOffsets.theSessionHitCount.myVal)
        return tokens


    # Call only after loading records offests
    @staticmethod
    def getTokensIndexesToAggregate():
        tokens = []
        tokens.append(FlowRecordOffsets.theResponderL2BytesPort0Offset.myVal)
        tokens.append(FlowRecordOffsets.theResponderL2BytesPort1Offset.myVal)
        tokens.append(FlowRecordOffsets.theDownloadedContentBytesPort0Offset.myVal)
        tokens.append(FlowRecordOffsets.theDownloadedContentBytesPort1Offset.myVal)
        tokens.append(FlowRecordOffsets.theDownloadTimeMsec.myVal)
        tokens.append(FlowRecordOffsets.theViewTimeMsec.myVal)
        tokens.append(FlowRecordOffsets.theSessionHitCount.myVal)
        return tokens


    # Call only after loading records offests
    @staticmethod
    def getTokensIndexesToOverwrite():
        tokens = []
        tokens.append(FlowRecordOffsets.theIsCachableIndicator.myVal)
        tokens.append(FlowRecordOffsets.theTimeOfDayOffset.myVal)
        return tokens

    # Call only after loading records offests
    @staticmethod
    def getTransactionSegmentTokenIndex():
        return FlowRecordOffsets.theTransactionSegmentOffset.myVal

    # Call only after loading records offests
    @staticmethod
    def getContentLengthTokenIndex():
        return FlowRecordOffsets.theContentLengthOffset.myVal

    # Call only after loading records offests
    @staticmethod
    def getAggregationKeyIndex ():
        return FlowRecordOffsets.theAggregationIdOffset.myVal

    @staticmethod
    def isTransactionFirstRecord (recordArray):
        return recordArray[FlowRecordOffsets.theTransactionSegmentOffset.myVal] in ['1', '3']

    @staticmethod
    def isTransactionLastRecord (recordArray):
        return recordArray[FlowRecordOffsets.theTransactionSegmentOffset.myVal] in ['2', '3']


# BW records access offsets
class BwRecordOffsets:
    theTimeofdayOffset                   = NumObject()
    theTotalBytesDeliveryPort0InOffset   = NumObject()
    theTotalBytesDeliveryPort0OutOffset  = NumObject()
    theTotalBytesDeliveryPort1InOffset   = NumObject()
    theTotalBytesDeliveryPort1OutOffset  = NumObject()
    theTotalBytesLinePort0InOffset       = NumObject()
    theTotalBytesLinePort0OutOffset      = NumObject()
    theTotalBytesLinePort1InOffset       = NumObject()
    theTotalBytesLinePort1OutOffset      = NumObject()
    theTotalBytesLinePort2InOffset       = NumObject()
    theTotalBytesLinePort2OutOffset      = NumObject()
    theTotalBytesLinePort3InOffset       = NumObject()
    theTotalBytesLinePort3OutOffset      = NumObject()
    theTotalBytesLinePort4InOffset       = NumObject()
    theTotalBytesLinePort4OutOffset      = NumObject()
    theTotalBytesLinePort5InOffset       = NumObject()
    theTotalBytesLinePort5OutOffset      = NumObject()
    theTotalBytesLinePort6InOffset       = NumObject()
    theTotalBytesLinePort6OutOffset      = NumObject()
    theTotalBytesLinePort7InOffset       = NumObject()
    theTotalBytesLinePort7OutOffset      = NumObject()

    theVideoBytesDeliveryPort0InOffset   = NumObject()
    theVideoBytesDeliveryPort0OutOffset  = NumObject()
    theVideoBytesDeliveryPort1InOffset   = NumObject()
    theVideoBytesDeliveryPort1OutOffset  = NumObject()
    theVideoBytesLinePort0InOffset       = NumObject()
    theVideoBytesLinePort0OutOffset      = NumObject()
    theVideoBytesLinePort1InOffset       = NumObject()
    theVideoBytesLinePort1OutOffset      = NumObject()
    theVideoBytesLinePort2InOffset       = NumObject()
    theVideoBytesLinePort2OutOffset      = NumObject()
    theVideoBytesLinePort3InOffset       = NumObject()
    theVideoBytesLinePort3OutOffset      = NumObject()
    theVideoBytesLinePort4InOffset       = NumObject()
    theVideoBytesLinePort4OutOffset      = NumObject()
    theVideoBytesLinePort5InOffset       = NumObject()
    theVideoBytesLinePort5OutOffset      = NumObject()
    theVideoBytesLinePort6InOffset       = NumObject()
    theVideoBytesLinePort6OutOffset      = NumObject()
    theVideoBytesLinePort7InOffset       = NumObject()
    theVideoBytesLinePort7OutOffset      = NumObject()

    theTotalVideoL7BytesOffset           = NumObject()
    theCachableVideoL7BytesOffset        = NumObject()
    theDeliveredVideoL7BytesOffset       = NumObject()

    theTotalVideoSessionsOffset          = NumObject()
    theCachableVideoL7SessionsOffset     = NumObject()
    theDeliveredVideoL7SessionsOffset    = NumObject()

    theTotalVideoSecondsOffset           = NumObject()
    theCachableVideoL7SecondsOffset      = NumObject()
    theDeliveredVideoL7SecondsOffset     = NumObject()


    @staticmethod
    def getOffsets():
        return {"timeofday"                 :BwRecordOffsets.theTimeofdayOffset,
                "totalBytesDeliveryPort0In" :BwRecordOffsets.theTotalBytesDeliveryPort0InOffset,
                "totalBytesDeliveryPort0Out":BwRecordOffsets.theTotalBytesDeliveryPort0OutOffset,
                "totalBytesDeliveryPort1In" :BwRecordOffsets.theTotalBytesDeliveryPort1InOffset,
                "totalBytesDeliveryPort1Out":BwRecordOffsets.theTotalBytesDeliveryPort1OutOffset,
                "totalBytesLinePort0In"     :BwRecordOffsets.theTotalBytesLinePort0InOffset,
                "totalBytesLinePort0Out"    :BwRecordOffsets.theTotalBytesLinePort0OutOffset,    
                "totalBytesLinePort1In"     :BwRecordOffsets.theTotalBytesLinePort1InOffset,     
                "totalBytesLinePort1Out"    :BwRecordOffsets.theTotalBytesLinePort1OutOffset,    
                "totalBytesLinePort2In"     :BwRecordOffsets.theTotalBytesLinePort2InOffset,     
                "totalBytesLinePort2Out"    :BwRecordOffsets.theTotalBytesLinePort2OutOffset,    
                "totalBytesLinePort3In"     :BwRecordOffsets.theTotalBytesLinePort3InOffset,     
                "totalBytesLinePort3Out"    :BwRecordOffsets.theTotalBytesLinePort3OutOffset,    
                "totalBytesLinePort4In"     :BwRecordOffsets.theTotalBytesLinePort4InOffset,
                "totalBytesLinePort4Out"    :BwRecordOffsets.theTotalBytesLinePort4OutOffset,    
                "totalBytesLinePort5In"     :BwRecordOffsets.theTotalBytesLinePort5InOffset,     
                "totalBytesLinePort5Out"    :BwRecordOffsets.theTotalBytesLinePort5OutOffset,    
                "totalBytesLinePort6In"     :BwRecordOffsets.theTotalBytesLinePort6InOffset,     
                "totalBytesLinePort6Out"    :BwRecordOffsets.theTotalBytesLinePort6OutOffset,    
                "totalBytesLinePort7In"     :BwRecordOffsets.theTotalBytesLinePort7InOffset,     
                "totalBytesLinePort7Out"    :BwRecordOffsets.theTotalBytesLinePort7OutOffset,    
                "videoBytesDeliveryPort0In" :BwRecordOffsets.theVideoBytesDeliveryPort0InOffset, 
                "videoBytesDeliveryPort0Out":BwRecordOffsets.theVideoBytesDeliveryPort0OutOffset,
                "videoBytesDeliveryPort1In" :BwRecordOffsets.theVideoBytesDeliveryPort1InOffset, 
                "videoBytesDeliveryPort1Out":BwRecordOffsets.theVideoBytesDeliveryPort1OutOffset,
                "videoBytesLinePort0In"     :BwRecordOffsets.theVideoBytesLinePort0InOffset,     
                "videoBytesLinePort0Out"    :BwRecordOffsets.theVideoBytesLinePort0OutOffset,    
                "videoBytesLinePort1In"     :BwRecordOffsets.theVideoBytesLinePort1InOffset,    
                "videoBytesLinePort1Out"    :BwRecordOffsets.theVideoBytesLinePort1OutOffset,    
                "videoBytesLinePort2In"     :BwRecordOffsets.theVideoBytesLinePort2InOffset,     
                "videoBytesLinePort2Out"    :BwRecordOffsets.theVideoBytesLinePort2OutOffset,    
                "videoBytesLinePort3In"     :BwRecordOffsets.theVideoBytesLinePort3InOffset,     
                "videoBytesLinePort3Out"    :BwRecordOffsets.theVideoBytesLinePort3OutOffset,    
                "videoBytesLinePort4In"     :BwRecordOffsets.theVideoBytesLinePort4InOffset,     
                "videoBytesLinePort4Out"    :BwRecordOffsets.theVideoBytesLinePort4OutOffset,    
                "videoBytesLinePort5In"     :BwRecordOffsets.theVideoBytesLinePort5InOffset,    
                "videoBytesLinePort5Out"    :BwRecordOffsets.theVideoBytesLinePort5OutOffset,    
                "videoBytesLinePort6In"     :BwRecordOffsets.theVideoBytesLinePort6InOffset,     
                "videoBytesLinePort6Out"    :BwRecordOffsets.theVideoBytesLinePort6OutOffset,    
                "videoBytesLinePort7In"     :BwRecordOffsets.theVideoBytesLinePort7InOffset,     
                "videoBytesLinePort7Out"    :BwRecordOffsets.theVideoBytesLinePort7OutOffset,    
                "totalVideoL7Bytes"         :BwRecordOffsets.theTotalVideoL7BytesOffset,    
                "cachableVideoL7Bytes"      :BwRecordOffsets.theCachableVideoL7BytesOffset, 
                "deliveredVideoL7Bytes"     :BwRecordOffsets.theDeliveredVideoL7BytesOffset,
                "totalVideoSessions"        :BwRecordOffsets.theTotalVideoSessionsOffset,      
                "cachableVideoL7Sessions"   :BwRecordOffsets.theCachableVideoL7SessionsOffset, 
                "deliveredVideoL7Sessions"  :BwRecordOffsets.theDeliveredVideoL7SessionsOffset,
                "totalVideoSeconds"         :BwRecordOffsets.theTotalVideoSecondsOffset,      
                "cachableVideoL7Seconds"    :BwRecordOffsets.theCachableVideoL7SecondsOffset, 
                "deliveredVideoL7Seconds"   :BwRecordOffsets.theDeliveredVideoL7SecondsOffset}

class SessionRecordOffsets(object):
    theTimeofdayOffset                = NumObject()
    theNanoSecOffset                   = NumObject()
    theSessionIdOffset                = NumObject()
    theTitleIdOffset                  = NumObject()
    theSiteNameOffset                 = NumObject()
    theLineVolumeOffset               = NumObject()
    theDeliveryVolumeOffset           = NumObject()
    theDurationOffset                 = NumObject()
    theIsSessionStartOffset           = NumObject()
    theIsSessionEndOffset             = NumObject()
    theSumLineTransactionDurationOffset     = NumObject()
    theSumDeliveryTransactionDurationOffset = NumObject()
    theNumLineStartTransactionOffset        = NumObject()
    theNumLineEndTransactionOffset          = NumObject()
    theNumLineContinuingTransactionOffset   = NumObject()
    theNumDeliveryStartTransactionOffset    = NumObject()
    theNumDeliveryEndTransactionOffset      = NumObject()
    theNumDeliveryContinuingTransactionOffset= NumObject()
    theSessionIdExtractorIndexOffset        = NumObject()
    maxOffset                               = NumObject() # used for allocation of an array for a new record

    @staticmethod
    def getOffsets():
        return {"timeofday"                      :SessionRecordOffsets.theTimeofdayOffset,
                "nanosec"                        :SessionRecordOffsets.theNanoSecOffset,
                "sessionId"                      :SessionRecordOffsets.theSessionIdOffset,
                "titleId"                        :SessionRecordOffsets.theTitleIdOffset,
                "siteName"                       :SessionRecordOffsets.theSiteNameOffset,
                "lineVolume"                     :SessionRecordOffsets.theLineVolumeOffset,
                "deliveryVolume"                 :SessionRecordOffsets.theDeliveryVolumeOffset,
                "duration"                       :SessionRecordOffsets.theDurationOffset,
                "isSessionStart"                 :SessionRecordOffsets.theIsSessionStartOffset,
                "isSessionEnd"                   :SessionRecordOffsets.theIsSessionEndOffset,
                "sumLineTransactionDuration"     :SessionRecordOffsets.theSumLineTransactionDurationOffset,
                "sumDeliveryTransactionDuration" :SessionRecordOffsets.theSumDeliveryTransactionDurationOffset,
                "numLineStartTransaction"        :SessionRecordOffsets.theNumLineStartTransactionOffset,
                "numLineEndTransaction"          :SessionRecordOffsets.theNumLineEndTransactionOffset,
                "numLineContinuingTransaction"   :SessionRecordOffsets.theNumLineContinuingTransactionOffset,
                "numDeliveryStartTransaction"    :SessionRecordOffsets.theNumDeliveryStartTransactionOffset,
                "numDeliveryEndTransaction"      :SessionRecordOffsets.theNumDeliveryEndTransactionOffset,
                "numDeliveryContinuingTransaction":SessionRecordOffsets.theNumDeliveryContinuingTransactionOffset,
                "sessionIdExtractorIndex"        :SessionRecordOffsets.theSessionIdExtractorIndexOffset,
                "maxOffset"                      :SessionRecordOffsets.maxOffset}


class FRecordHelper(FlowRecordOffsets):
    def __init__(self, record):
        self.setRecord(record)

    def setRecord(self, record):
        self.record = record
        self._setShadowValuesForOptimization()

    def createNewRecord(self):
        record = [""] * FRecordHelper.maxOffset.myVal # create an array of size max offset
        self.setRecord(record)
        
    def setValues(self, vals):
        offsets = self.getOffsets()

        for name,val in vals.iteritems():
            if name in offsets:
                self.record[offsets[name].myVal] = val

        self._setShadowValuesForOptimization()

    def _setShadowValuesForOptimization(self):
        if self.record:
            self.timeOfDayShadow = int(self.record[FRecordHelper.theTimeOfDayOffset.myVal])
            self.sessionIdShadow = long(self.record[FRecordHelper.theSessionIdOffset.myVal])
            self.unixStartTimeShadow = long(self.record[FRecordHelper.theUnixStartTime.myVal])

    def getVolume(self):
        return int(self.record[FRecordHelper.theDownloadedContentBytesPort0Offset.myVal]) + int(self.record[FRecordHelper.theDownloadedContentBytesPort1Offset.myVal])

    @property
    def timeOfDay(self):
        return self.timeOfDayShadow

    @property
    def siteName(self):
        return self.record[FRecordHelper.theHostOffset.myVal]

    @property
    def unixStartTime(self):
        return self.unixStartTimeShadow

    @property
    def downloadTimeMsec(self):
        return int(self.record[FRecordHelper.theDownloadTimeMsec.myVal])

    @property
    def transactionDownloadTimeMsec(self):
        return int(self.record[FRecordHelper.theTransactionDownloadTimeMsecOffset.myVal])

    @property
    def isDelivered(self):
        return self.record[FRecordHelper.theIsDeliveredIndicator.myVal] == "1"

    @property
    def wasRedirected(self):
        return self.record[FRecordHelper.theWasRedirected.myVal] == "1"

    @property
    def isTransactionStart(self):
        return (int(self.record[FRecordHelper.theTransactionSegmentOffset.myVal]) & 1) != 0

    @property
    def isTransactionEnd(self):
        return (int(self.record[FRecordHelper.theTransactionSegmentOffset.myVal]) & 2) != 0

    @property
    def sessionId(self):
        return self.sessionIdShadow

    @property
    def titleId(self):
        return long(self.record[FRecordHelper.theTitleIdOffset.myVal])
        
    @property
    def sessionIdExtractorIndex(self):
        # For performance perpoces the value is not converted to int
        return self.record[FRecordHelper.theSessionIdExtractorIndexOffset.myVal]
                        
class SRecordHelper(SessionRecordOffsets):
    def __init__(self, record):
        self.record = record

    def __str__(self):
        return ",".join(self.record)

    def createNewRecord(self):
        self.record = [""] * (SRecordHelper.maxOffset.myVal + 1)  # create an array of size max offset
        self.record[0] = "S"
        self.record[SRecordHelper.maxOffset.myVal] = "\n"

    @property
    def timeOfDay(self):
        return int(self.record[SRecordHelper.theTimeofdayOffset.myVal])

    @timeOfDay.setter  
    def timeOfDay(self, val):
        self.record[SRecordHelper.theTimeofdayOffset.myVal] = str(val)

    @property
    def nanosec(self):
        return long(self.record[SRecordHelper.theNanoSecOffset.myVal])

    @nanosec.setter  
    def nanosec(self, val):
        self.record[SRecordHelper.theNanoSecOffset.myVal] = str(val)

    @property
    def sessionId(self):
        return long(self.record[SRecordHelper.theSessionIdOffset.myVal])

    @sessionId.setter
    def sessionId(self, val):
        self.record[SRecordHelper.theSessionIdOffset.myVal] = str(val)

    @property
    def titleId(self):
        return long(self.record[SRecordHelper.theTitleIdOffset.myVal])

    @titleId.setter
    def titleId(self, val):
        self.record[SRecordHelper.theTitleIdOffset.myVal] = str(val)

    @property
    def siteName(self):
        return self.record[SRecordHelper.theSiteNameOffset.myVal]

    @siteName.setter
    def siteName(self, val):
        self.record[SRecordHelper.theSiteNameOffset.myVal] = str(val)

    @property
    def lineVolume(self):
        return int(self.record[SRecordHelper.theLineVolumeOffset.myVal])

    @lineVolume.setter
    def lineVolume(self, val):
        self.record[SRecordHelper.theLineVolumeOffset.myVal] = str(val)

    @property
    def deliveryVolume(self):
        return int(self.record[SRecordHelper.theDeliveryVolumeOffset.myVal])

    @deliveryVolume.setter
    def deliveryVolume(self, val):
        self.record[SRecordHelper.theDeliveryVolumeOffset.myVal] = str(val)

    @property
    def duration(self):
        return int(self.record[SRecordHelper.theDurationOffset.myVal])

    @duration.setter
    def duration(self, val):
        self.record[SRecordHelper.theDurationOffset.myVal] = str(val)

    @property
    def isSessionStart(self):
        return self.record[SRecordHelper.theIsSessionStartOffset.myVal] == "1"

    @isSessionStart.setter
    def isSessionStart(self, val):
        self.record[SRecordHelper.theIsSessionStartOffset.myVal] = str(int(val))

    @property
    def isSessionEnd(self):
        return self.record[SRecordHelper.theIsSessionEndOffset.myVal] == "1"

    @isSessionEnd.setter
    def isSessionEnd(self, val):
        self.record[SRecordHelper.theIsSessionEndOffset.myVal] = str(int(val))

    @property
    def sumLineTransactionDuration(self):
        return int(self.record[SRecordHelper.theSumLineTransactionDurationOffset.myVal])

    @sumLineTransactionDuration.setter
    def sumLineTransactionDuration(self, val):
        self.record[SRecordHelper.theSumLineTransactionDurationOffset.myVal] = str(val)

    @property
    def sumDeliveryTransactionDuration(self):
        return int(self.record[SRecordHelper.theSumDeliveryTransactionDurationOffset.myVal])

    @sumDeliveryTransactionDuration.setter
    def sumDeliveryTransactionDuration(self, val):
        self.record[SRecordHelper.theSumDeliveryTransactionDurationOffset.myVal] = str(val)

    @property
    def numLineStartTransaction(self):
        return int(self.record[SRecordHelper.theNumLineStartTransactionOffset.myVal])

    @numLineStartTransaction.setter
    def numLineStartTransaction(self, val):
        self.record[SRecordHelper.theNumLineStartTransactionOffset.myVal] = str(val)

    @property
    def numDeliveryStartTransaction(self):
        return int(self.record[SRecordHelper.theNumDeliveryStartTransactionOffset.myVal])

    @numDeliveryStartTransaction.setter
    def numDeliveryStartTransaction(self, val):
        self.record[SRecordHelper.theNumDeliveryStartTransactionOffset.myVal] = str(val)

    @property
    def numLineEndTransaction(self):
        return int(self.record[SRecordHelper.theNumLineEndTransactionOffset.myVal])

    @numLineEndTransaction.setter
    def numLineEndTransaction(self, val):
        self.record[SRecordHelper.theNumLineEndTransactionOffset.myVal] = str(val)

    @property
    def numDeliveryEndTransaction(self):
        return int(self.record[SRecordHelper.theNumDeliveryEndTransactionOffset.myVal])

    @numDeliveryEndTransaction.setter
    def numDeliveryEndTransaction(self, val):
        self.record[SRecordHelper.theNumDeliveryEndTransactionOffset.myVal] = str(val)

    @property
    def numLineContinuingTransaction(self):
        return int(self.record[SRecordHelper.theNumLineContinuingTransactionOffset.myVal])

    @numLineContinuingTransaction.setter
    def numLineContinuingTransaction(self, val):
        self.record[SRecordHelper.theNumLineContinuingTransactionOffset.myVal] = str(val)

    @property
    def numDeliveryContinuingTransaction(self):
        return int(self.record[SRecordHelper.theNumDeliveryContinuingTransactionOffset.myVal])

    @numDeliveryContinuingTransaction.setter
    def numDeliveryContinuingTransaction(self, val):
        self.record[SRecordHelper.theNumDeliveryContinuingTransactionOffset.myVal] = str(val)

    @property
    def sessionIdExtractorIndex(self):
        return int(self.record[SRecordHelper.theSessionIdExtractorIndexOffset.myVal])

    @sessionIdExtractorIndex.setter
    def sessionIdExtractorIndex(self, val):
        self.record[SRecordHelper.theSessionIdExtractorIndexOffset.myVal] = str(val)

# This class loads the record header structure, for fast access and asserts that data records are valid
class RawDataRecordValidator:
    myLogger = None
    theRecordTypeOffset = 0
    theRecordTypes = {}
    theAllowedRecordTypes = ["F","V","W","L","S"]
    

    @staticmethod
    def loadRecordOffsets(d,recordHeader,logger):
        i = 0
        #store offsets
        for token in recordHeader:
            if token in d:
                d[token].myVal = i
            i += 1

        if "maxOffset" in d:
            d["maxOffset"].myVal = i

        #assert all needed fields have been initialized
        for k,v in d.iteritems():
            if v.myVal == -1: # any uninitialized member
                logger.error("In record type " + recordHeader[0] + " no header offset found for " + k)
                return False
        return True


    @staticmethod
    def initRecordTypes(filename,logger):
        #if snapshotFile != None:
        #    sfd = openFileForWrite(snapshotFile,logger)
        try:
            fd = openFileForRead(filename,logger)
            for line in fd:
                #if snapshotFile != None:
                #    sfd.write(line)
                arr = line.split("\t")
                if len(arr) > 1:
                    arr.pop()
                recType = arr[0]
                arr[0] = "recType"
                RawDataRecordValidator.theRecordTypes[recType] = arr

                # load relevant field offsets
                if recType == "F":
                    if not RawDataRecordValidator.loadRecordOffsets(FlowRecordOffsets.getOffsets(),arr,logger):
                        return False
                if recType == "L":
                    if not RawDataRecordValidator.loadRecordOffsets(LogMessageOffsets.getOffsets(),arr,logger):
                        return False
                if recType == "V":
                    if not RawDataRecordValidator.loadRecordOffsets(BwRecordOffsets.getOffsets(),arr,logger):
                        return False
                if recType == "S":
                    if not RawDataRecordValidator.loadRecordOffsets(SessionRecordOffsets.getOffsets(),arr,logger):
                        return False


        except Exception,e:
            print ("Failed to open record specs %s - %s" % (filename,str(e)))#+ " e=" + str(e))
            return False
        #write structure of the internal W record
        dictionary={}
        for key,val in BwRecordOffsets.getOffsets().iteritems():
            dictionary[val.myVal]=key
        #line="\t".join(["W","unixtime"]+dictionary.values())
        #if snapshotFile != None:
        #    sfd.write(line)
        return True



    def __init__ (self,logger):
        self.myLogger = logger

    def verifyData (self,arr):

        self.myLogger.debug3("proccessing record: %s, len(arr)=%d", str(arr), len(arr))

        if len(arr) < 1:
            self.myLogger.error("Empty record detected")
            return False
        #---------------------------------------------
        recType = arr[0]
        # check for valid type
        if not recType in RawDataRecordValidator.theAllowedRecordTypes:
            self.myLogger.error("Unknown record type " + recType)
            return False
        # check for consistent length
        #arr = arr[:len(arr)-2]
        recordFieldsCount = len(arr) -1
        recordHeaderFieldCount = len(RawDataRecordValidator.theRecordTypes[recType])
        if recType != "W" and ((recordFieldsCount < recordHeaderFieldCount) or (recType != "V" and recordFieldsCount > recordHeaderFieldCount)):
            self.myLogger.error("Invalid "+ recType +" record detected: recordFieldCount="+str(recordFieldsCount) + " , headerFieldCount=" + str(recordHeaderFieldCount) + ", record:\n" + str(arr))
            return False
        return True


# Some global methods
def getHeaderFileName(folder):
    return folder + os.sep + "fixed" + os.sep + DATA_SUB_FOLDER_AND_HEADER_NAME


def openFileForRead (filename,logger,openMode="r"):
    try:
        fd = open(filename,openMode)
        return fd
    except Exception, e:
        logger.error("Failed to open %s for read- %s " %( filename , str(e)))
        return None


def openFileForWrite (filename,logger,openMode="w"):
    try:
        fd = open(filename,openMode)
        return fd
    except Exception, e:
        logger.error("Failed to open %s for write- %s " %( filename , str(e)))
        return None

