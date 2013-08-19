#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: michaelg
# 

#
# This file represents coal message in picleable format for faster serialization
#

class Flow:
    def __init__(self, gpb):
        self.clientIP = gpb.clientIP.text
        self.clientPort = gpb.clientPort
        self.serverIP = gpb.serverIP.text
        self.serverPort = gpb.serverPort
        #todo (arnon)
        #define vlan in infra/net so that it may log QinQ and other horros

#for either request or response
class Http:
    def __init__(self, gpb):
        #entire request or response data
        self.body = gpb.body
        #the number of packets the request was spanning across
        self.numOfPacketSpan = gpb.numOfPacketSpan
        #did we see entire data 
        self.isDataComplete = gpb.isDataComplete
        #index with regard to the flow is seperate for request and response to support pipeline
        self.index = gpb.index
        #on which adapter did we see the fist packet of this request/response?
        self.adapterOfFirstPacket = gpb.adapterOfFirstPacket
        #packet headers of this HTTP chunk 
        self.L2toL4Headers = gpb.L2toL4Headers


class DecodingResults:
    def __init__(self, gpb):
        self.cgid = gpb.cgid
        self.cid = gpb.cid
        self.wasCidDecodedOnRequest = gpb.wasCidDecodedOnRequest
        self.wasRequestRedirected = gpb.wasRequestRedirected
        self.wasPerformingAcquisitionGood = gpb.wasPerformingAcquisitionGood
        self.wasPerformingAcquisitionBad = gpb.wasPerformingAcquisitionBad
        self.checksum1k = gpb.checksum1k
        self.wasChecksumChanged = gpb.wasChecksumChanged
        #...more


class Data:
    def __init__(self, gpb):
        self.content = gpb.content
        #the start offset in the stream from which the data was taken
        self.startOffset = gpb.startOffset
        #original tcp seq number of this data chunk
        self.tcpSeq = gpb.tcpSeq
        #packet headers of this data chunk 
        self.L2toL4Headers = gpb.L2toL4Headers

class Coal:

    def __init__(self, coalGpb=None):
        if coalGpb:
            #with these 4 we should be able to match request / response
            self.vaId = coalGpb.vaId
            self.flowId = coalGpb.flowId
            self.transactionId = coalGpb.transactionId
            self.sysId = coalGpb.sysId
            #time
            self.unixTime = coalGpb.unixTime
            self.startTimeMili = coalGpb.startTimeMili
            self.DurationMili = coalGpb.DurationMili
            #accounting
            self.numDownloadedBytes = coalGpb.numDownloadedBytes

            self.flow = Flow(coalGpb.flow) if coalGpb.HasField("flow") else None
            self.request = Http(coalGpb.request) if coalGpb.HasField("request") else None
            self.response = Http(coalGpb.response) if coalGpb.HasField("response") else None
            self.decoding = DecodingResults(coalGpb.decoding) if coalGpb.HasField("decoding") else None
            self.data = [] #data(coalGpb.data) if coalGpb.data else None
        else:
            #with these 4 we should be able to match request / response
            self.vaId = 0
            self.flowId = 0
            self.transactionId = 0
            self.sysId = 0
            #time
            self.unixTime = 0
            self.startTimeMili = 0
            self.DurationMili = 0
            #accounting
            self.numDownloadedBytes = 0

            self.flow = None
            self.request = None
            self.response = None
            self.decoding = None
            self.data = []

    


