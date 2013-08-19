
#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: hagaia
# 

import os.path
import time

import a.infra.file.utils
from a.infra.time.monotonic_clock import monotonicTimeNano

import utils

if  __package__ is None:
    G_NAME_MODULE_DELIVERY = "unknown"
    G_NAME_GROUP_DELIVERY_TOPPER_REPORTER = "unknown"
else:
    from . import G_NAME_MODULE_DELIVERY 
    from . import G_NAME_GROUP_DELIVERY_TOPPER_REPORTER


#-------------------------------------------------------------------------------------------------
class TopperReporter(object):
   
    def __init__ (self, name, logger):

        self.__name = name        
        self.__log = logger.createLogger(G_NAME_MODULE_DELIVERY, G_NAME_GROUP_DELIVERY_TOPPER_REPORTER)
        self.__outputString   = ""
        self.__fieldSeperator = "\t"
        self.__lineFeed       = "\t\t\n"
        self.__filePrefix     = "data"
        self.__isActive       = False
        self.__dataFileFd     = 0
                        
    #-------------------------------------------------------------------------------------------------
    def init (self, conf):

        self.__conf = conf

        if not self.__createTopperDirectories():
            return False

        return True

        
    #-------------------------------------------------------------------------------------------------
    def start (self):
               
        return self.__openFile()   
        
    #-------------------------------------------------------------------------------------------------
    def repoen (self):

        oldFd = self.__dataFileFd
        
        if not self.__openFile():
            return False

        os.close(oldFd)
        self.__log("close-fd").debug1("Close FD = %s",str(oldFd))

        return True


    #-------------------------------------------------------------------------------------------------
    def end (self):
        
        if self.__isActive:
            self.__log("close-records-file").debug1("Close Records Data File, Path - %s", self.__conf.actualNgxRecordsLogFile)
            os.close(self.__dataFileFd)
            self.__dataFileFd = 0
    
    #------------------------------------------------------------------------------------------------- 
    def reportVolume (self, bw):

        if not self.__isActive:
            return False

        self.__beginCommonRecord("V")

        # totalBytesDeliveryPort0In
        self.__appendField(bw.volumeCounters[0].bytesIn)
        # totalBytesDeliveryPort0Out
        self.__appendField(bw.volumeCounters[0].bytesOut)           
       
        # Line Total Bytes
        self.__appendField(0)
        self.__appendField(0)
        self.__appendField(0)
        self.__appendField(0)
        self.__appendField(0)
        self.__appendField(0)
        self.__appendField(0)
        self.__appendField(0)
     
       
        # videoBytesDeliveryPort0In
        self.__appendField(bw.volumeCounters[0].bytesIn)
        # videoBytesDeliveryPort0Out
        self.__appendField(bw.volumeCounters[0].bytesOut)

       
        # Line Video Bytes        
        self.__appendField(0)
        self.__appendField(0)
        self.__appendField(0)
        self.__appendField(0)
        self.__appendField(0)
        self.__appendField(0)
        self.__appendField(0)
        self.__appendField(0)
       
        self.__appendField(0)
        self.__appendField(0)
        self.__appendField(0)
       
        self.__appendField(0)
        self.__appendField(0)
        self.__appendField(0)
       
        self.__appendField(0)
        self.__appendField(0)
        self.__appendField(0)
       
        # is delivery
        self.__appendField(1)

        # totalBytesDeliveryPort1In
        self.__appendField(bw.volumeCounters[1].bytesIn)
        # totalBytesDeliveryPort1Out
        self.__appendField(bw.volumeCounters[1].bytesOut) 

                # videoBytesDeliveryPort1In
        self.__appendField(bw.volumeCounters[1].bytesIn)
        # videoBytesDeliveryPort1Out
        self.__appendField(bw.volumeCounters[1].bytesOut)
        
        # Line Total Bytes ports 4 - 7        
        self.__appendField(0)
        self.__appendField(0)
        self.__appendField(0)
        self.__appendField(0)
        self.__appendField(0)
        self.__appendField(0)
        self.__appendField(0)
        self.__appendField(0)  

        # Line Video Bytes ports 4 - 7        
        self.__appendField(0)
        self.__appendField(0)
        self.__appendField(0)
        self.__appendField(0)
        self.__appendField(0)
        self.__appendField(0)
        self.__appendField(0)
        self.__appendField(0)

        self.__writeRecord()

        return True
        

    #private
    #-------------------------------------------------------------------------------------------------
    def __openFile (self):
   
   
        fileName = self.__conf.actualNgxRecordsLogFile
   
        # Create Data File - this file shoud be rotated
        #-------------------------------------------------
        try:
            self.__dataFileFd = os.open(fileName,os.O_WRONLY|os.O_APPEND|os.O_CREAT,0644)            
            self.__log("records-file-ok").debug1("Create/Open Records Data File, Path - %s - FD - %s", fileName,str(self.__dataFileFd))
            self.__isActive = True
        except (OSError,IOError) as e:
            self.__log("records-file-err").error("Failed to Create/Open Records Data File, Path - %s - %s",fileName,utils.parseErrnoToString(e))
            self.__isActive = False
       
        return self.__isActive

    #-------------------------------------------------------------------------------------------------
    # Create Topper Data and Headers Directories
    def  __createTopperDirectories(self):


        # Create Topper Data Directory
        #--------------------------------------
        dataDir = os.path.join(self.__conf.topperDir, self.__conf.kConf.kTopperDataDir)

        try:
            a.infra.file.utils.makeDirs(dataDir,reuseExisting = True)
            self.__log("create-topper-dir").info("create Topper data directory - %s",dataDir)

        except OSError, e:
            self.__log("create-topper-dir-err").error("Failed to create Topper data directory - %s",dataDir,utils.parseErrnoToString(e))
            return False


        # Create Topper Headers Directory and Write Headers File
        #---------------------------------------------------------
        headersFile = os.path.join(self.__conf.topperDir, self.__conf.kConf.kTopperHeadersDir)

        headersDir = os.path.dirname(headersFile)

        try:
            a.infra.file.utils.makeDirs(headersDir,reuseExisting = True)
            self.__log("create-topper-hdr-dir").debug2("create Topper header directory - %s",headersDir)
        except OSError, e:
            self.__log("create-topper-hdr-err").error("Failed to create Topper Headers directory - %s",headersDir,utils.parseErrnoToString(e))
            return False

        self.__createFlowRecordHeaderFile(headersFile)
        
        return True

   
    #-------------------------------------------------------------------------------------------------
    def __createFlowRecordHeaderFile(self, headersFilePath) :


        try:
            headersFile = open(headersFilePath,'wb')
            self.__log("header-file").debug1("Open/Create Topper Headers File, Path - %s", headersFilePath)
        except IOError, e:
            self.__log("header-file-failed").error("Failed to Open/Create Topper Headers File, Path - %s - %s",headersFilePath,utils.parseErrnoToString(e))
            return False

    
        #--- F Record Header
        self.__createFlowCommonHeader("F")
        self.__addHeadrField("srcIP","F")
        self.__addHeadrField("srcPort","F")
        self.__addHeadrField("destIP","F")
        self.__addHeadrField("destPort","F")
        self.__addHeadrField("initiatorPortNumber","F")
        self.__addHeadrField("responderL2BytesPort0","F")
        self.__addHeadrField("responderL2BytesPort1","F")
        self.__addHeadrField("downloadedContentBytesPort0","F")
        self.__addHeadrField("downloadedContentBytesPort1","F")
        self.__addHeadrField("downloadTimeMsec","F")
        self.__addHeadrField("viewTimeMsec","F")
        self.__addHeadrField("contentLength","F")
        self.__addHeadrField("contentChecksum","F")
        self.__addHeadrField("checksum1Kto10K","F")
        self.__addHeadrField("cid","F")
        self.__addHeadrField("cgid","F")
        self.__addHeadrField("beginOffset","F")
        self.__addHeadrField("contentType","F")
        self.__addHeadrField("host","F")
        self.__addHeadrField("path","F")
        self.__addHeadrField("isCachable","F")
        self.__addHeadrField("isDelivered","F")
        self.__addHeadrField("isViewSession","F")
        self.__addHeadrField("sessionHitCount","F")#for long transactions with multiple reports
        self.__addHeadrField("aggregationId","F")
        self.__addHeadrField("transactionSegment","F")
        self.__addHeadrField("unixStartTime","F")
        self.__addHeadrField("httpRequestRange","F")
        self.__addHeadrField("httpResponseRange","F")
        self.__addHeadrField("origHostName","F")
        self.__addHeadrField("wasRedirected","F")
        self.__addHeadrField("origin","F")
        self.__addHeadrField("initialBurstBwKbps","F")
        self.__addHeadrField("initialBurstSizeKB","F")
        self.__addHeadrField("sustainedBwKbps","F")
        self.__addHeadrField("signatureName","F");
        self.__addHeadrField("transactionDownloadedContentBytesPort0","F");
        self.__addHeadrField("transactionDownloadedContentBytesPort1","F");
        self.__addHeadrField("transactionDownloadTimeMsec","F");
        self.__addHeadrField("cdnId","F");
        self.__addHeadrField("llnwdLocation","F");
        self.__addHeadrField("titleId","F")
        self.__addHeadrField("sessionId","F")
        self.__addHeadrField("sessionIdExtractorIndex","F")
        self.__addHeadrField("debugFlags","F")
        self.__outputString += "\n"
        headersFile.write(self.__outputString)
        #--------------------------
        
        
        #--- V Record
        self.__createCommonHeader("V")
        self.__addHeadrField("totalBytesDeliveryPort0In","V")
        self.__addHeadrField("totalBytesDeliveryPort0Out","V")        
        self.__addHeadrField("totalBytesLinePort0In","V")
        self.__addHeadrField("totalBytesLinePort0Out","V")
        self.__addHeadrField("totalBytesLinePort1In","V")
        self.__addHeadrField("totalBytesLinePort1Out","V")
        self.__addHeadrField("totalBytesLinePort2In","V")
        self.__addHeadrField("totalBytesLinePort2Out","V")
        self.__addHeadrField("totalBytesLinePort3In","V")
        self.__addHeadrField("totalBytesLinePort3Out","V")        
        self.__addHeadrField("videoBytesDeliveryPort0In","V")
        self.__addHeadrField("videoBytesDeliveryPort0Out","V") 
        self.__addHeadrField("videoBytesLinePort0In","V")
        self.__addHeadrField("videoBytesLinePort0Out","V")
        self.__addHeadrField("videoBytesLinePort1In","V")
        self.__addHeadrField("videoBytesLinePort1Out","V")
        self.__addHeadrField("videoBytesLinePort2In","V")
        self.__addHeadrField("videoBytesLinePort2Out","V")
        self.__addHeadrField("videoBytesLinePort3In","V")
        self.__addHeadrField("videoBytesLinePort3Out","V")
        self.__addHeadrField("totalVideoL7Bytes","V")
        self.__addHeadrField("cachableVideoL7Bytes","V")
        self.__addHeadrField("deliveredVideoL7Bytes","V")
        self.__addHeadrField("totalVideoSessions","V")
        self.__addHeadrField("cachableVideoL7Sessions","V")
        self.__addHeadrField("deliveredVideoL7Sessions","V")
        self.__addHeadrField("totalVideoSeconds","V")
        self.__addHeadrField("cachableVideoL7Seconds","V")
        self.__addHeadrField("deliveredVideoL7Seconds","V")
        self.__addHeadrField("isDelivery","V")
        self.__addHeadrField("totalBytesDeliveryPort1In","V")
        self.__addHeadrField("totalBytesDeliveryPort1Out","V")
        self.__addHeadrField("videoBytesDeliveryPort1In","V")
        self.__addHeadrField("videoBytesDeliveryPort1Out","V")
        self.__addHeadrField("totalBytesLinePort4In","V")
        self.__addHeadrField("totalBytesLinePort4Out","V")
        self.__addHeadrField("totalBytesLinePort5In","V")
        self.__addHeadrField("totalBytesLinePort5Out","V")
        self.__addHeadrField("totalBytesLinePort6In","V")
        self.__addHeadrField("totalBytesLinePort6Out","V")
        self.__addHeadrField("totalBytesLinePort7In","V")
        self.__addHeadrField("totalBytesLinePort7Out","V")
        self.__addHeadrField("videoBytesLinePort4In","V")
        self.__addHeadrField("videoBytesLinePort4Out","V")
        self.__addHeadrField("videoBytesLinePort5In","V")
        self.__addHeadrField("videoBytesLinePort5Out","V")
        self.__addHeadrField("videoBytesLinePort6In","V")
        self.__addHeadrField("videoBytesLinePort6Out","V")
        self.__addHeadrField("videoBytesLinePort7In","V")
        self.__addHeadrField("videoBytesLinePort7Out","V")
        self.__outputString += "\n"
        headersFile.write(self.__outputString)

        #--- S Record Header
        self.__createCommonHeader("S")
        self.__addHeadrField("sessionId","S")
        self.__addHeadrField("titleId","S")
        self.__addHeadrField("siteName","S")
        self.__addHeadrField("lineVolume","S")
        self.__addHeadrField("deliveryVolume","S")
        self.__addHeadrField("duration","S")
        self.__addHeadrField("isSessionStart","S")
        self.__addHeadrField("isSessionEnd","S")
        self.__addHeadrField("sumLineTransactionDuration","S")
        self.__addHeadrField("sumDeliveryTransactionDuration","S")
        self.__addHeadrField("numLineStartTransaction","S")
        self.__addHeadrField("numLineEndTransaction","S")
        self.__addHeadrField("numLineContinuingTransaction","S");
        self.__addHeadrField("numDeliveryStartTransaction","S")
        self.__addHeadrField("numDeliveryEndTransaction","S")
        self.__addHeadrField("numDeliveryContinuingTransaction","S")
        self.__addHeadrField("sessionIdExtractorIndex","S")
        self.__outputString += "\n"
        headersFile.write(self.__outputString)

        headersFile.close()

        self.__log("header-file").debug1("Write and Close Topper Headers to File, Path - %s", headersFilePath)

        return True


    #-------------------------------------------------------------------------------------------------
    def __createFlowCommonHeader (self, type):
        self.__createCommonHeader(type)
        self.__addHeadrField("flowId",type)

    #-------------------------------------------------------------------------------------------------
    def __createCommonHeader(self, type):
        self.__outputString = ""
        self.__outputString = self.__outputString + type + self.__fieldSeperator
        self.__addHeadrField("timeofday",type)
        self.__addHeadrField("nanosec",type)
    
    #-------------------------------------------------------------------------------------------------
    def __addHeadrField (self,fieldName,type):

        self.dummy = type
        self.__outputString = self.__outputString + fieldName + self.__fieldSeperator
    
    #-------------------------------------------------------------------------------------------------
    def __beginCommonRecord(self, type):

        self.__outputString = ""        

        # return time in sec.xxx
        curTime = time.time();
        timeOfDaySec  = long(curTime)
        monotonicNano = monotonicTimeNano()
        
        self.__appendField(type)
        self.__appendField(timeOfDaySec) # time of day in seconds    
        self.__appendField(monotonicNano) # monotonic style in nano


    #-------------------------------------------------------------------------------------------------
    def __appendField(self, field):
    
        self.__outputString = self.__outputString + str(field)
        self.__outputString = self.__outputString + self.__fieldSeperator        
    
    #-------------------------------------------------------------------------------------------------
    def __writeRecord(self):

       self.__outputString = self.__outputString + self.__lineFeed

       try:
           self.__log("write-v-record").debug3("Start Write V Record to FD = %s",self.__dataFileFd)
           os.write(self.__dataFileFd,self.__outputString)
           self.__log("finish-write").debug3("Finish Write V Record %s to FD = %s",self.__outputString, self.__dataFileFd)           
       except (IOError,OSError) as e:
            self.__log("write-v-record-err").error("Failed to write V Record - %s - FD = %d",utils.parseErrnoToString(e),self.__dataFileFd)         
       

