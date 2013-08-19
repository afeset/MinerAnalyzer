
import sys, os     


import optparse 
import time , signal , logging , glob , datetime,resource
import logging.handlers
import shutil
import cPickle
from a.infra import gem
import a.infra.gem.path
import a.sys.analytic.simple_stats_logger
from operator import itemgetter
from a.infra.log.main_logger import MainLogger
from a.stats.stats_comm_over_file_client import StatsCommOverFileClient
from a.infra.daemon import daemonUtils
import a.infra.process.captain

import a.sys.analytic.topper_record_utils
# using from X import in order not to make chenges in code
from a.sys.analytic.topper_record_utils import FlowRecordOffsets
from a.sys.analytic.topper_record_utils import BwRecordOffsets
from a.sys.analytic.topper_record_utils import RawDataRecordValidator
import a.sys.analytic.topper_report_utils as tru
import a.sys.analytic.bitrate_report as bitrate_report
import google.ipaddr  

import multiprocessing as mp
import threading 
import gc
import collections



import struct
#import profile

def myLong(var):
    return long(var)

theSepToken = "\t"


nowString = None
def writeMemoryConsumption():
    global nowString
    openMode = "a"
    if nowString==None:
        openMode = "w"
        t = time.localtime()
        nowString = "%04d%02d%02d-%02d:%02d" % (t.tm_year , t.tm_mon, t.tm_mday, t.tm_hour , t.tm_min)
    fileName = "memory_consumption_%s"%nowString
    fd = open(fileName,openMode)
    
    memCons = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    classCount = {}
    for element in gc.get_objects() :
        if type(element).__name__== 'instance':
            c = element.__class__.__name__;
            if c not in classCount:
                classCount[c] = 0
    
            classCount[c] += 1
    
    lineArr = [memCons]
    
    sortedObj =  sorted(classCount.items(),key = lambda pair: pair[1],reverse=True)
    objArr = []
    for objTuple in sortedObj[:12]:
        objArr += [objTuple[0],objTuple[1]]
    
    if len(objArr)>0:
        lineArr += objArr
    
    line = '\t'.join(map(str,lineArr)) + '\n'
    fd.write(line)
    fd.close()

    


def verbose (*args):
    #if parser.values.verbose:
        output=""
        for arg in args:
            output = output + str(arg)
        print output
        sys.stdout.flush() #get stuff printed on the spot


# tells the main loop to get out
# triggered by the term/quit signals
forever = True
# for orderly shutdown
def userBreak (signum, frame):
    __pychecker__='no-argsused'
    global forever
    forever = False

signal.signal(signal.SIGQUIT, userBreak )
signal.signal(signal.SIGTERM, userBreak )




def makeDirsIfNeeded (path):
    if os.path.exists(path):
        if os.path.isdir(path):
            return
        else:
            raise Exception, "path '"+path+"' exists, refusing to turn it into a directory."
    else:
        os.makedirs(path)


def isIP (hostname):
    startIndex  = 0
    endIndex    = -1
    
    if len(hostname) == 0:
        return False
    
    # ip host enclosed in "[]", e.g.  [172.240.0.10]:80 or [2003:face::1]:80
    if hostname.startswith("[") is True:
        startIndex = 1
        endIndex = hostname.rfind("]")
    
    # ipv6, e.g.  2003:face::1,
    #             ::192.0.2.128 or ::ffff:192.0.2.128 (ipv4-mapped-ipv6)
    elif hostname.count(":") > 1: 
        startIndex = 0
        endIndex = -1
    
    # ipv4, e.g.  172.240.0.10 or 172.240.0.10:80
    else: 
        startIndex = 0
        endIndex  = hostname.rfind(":")
    
    if endIndex != -1:
        ipCandidate = hostname[startIndex:endIndex]
    else:
        ipCandidate = hostname
    
    try:
        ipAddr = google.ipaddr.IPAddress(ipCandidate)
    except ValueError as ex:
        return False
    
    return True


#we build this finite set once outside the function
suffixes=set(["co","net","org","biz","gov","info","ac","edu","int"])
#extract site name from server name
def getSite (hostname):
    arr=hostname.split(".")
    arrLen=len(arr)
    if isIP(hostname):
        return hostname
    if arrLen <= 2:
        return hostname
    offset = arrLen-2
    if arr[arrLen-2] in suffixes:
        offset -= 1
    return ".".join(arr[offset:])

#expect a struct_time
def isFirstWeekDay (t):
    date = datetime.date(t.tm_year , t.tm_mon , t.tm_mday)
    return date.weekday()==0

# 1 liner
def rename (src,dest,logger):
    newName = src
    try:
        os.rename(src ,dest)
        newName = dest
    except Exception,e:
        logger.error("Failed renaming %s to %s - %s" % (src,dest,str(e)))
    return newName

# 1 liner
def copyTree (src,dest,logger):
    try:
        shutil.copytree(src,dest)
        return True
    except Exception,e:
        logger.error("Failed copying folder %s to %s - %s" % (src,dest,str(e)))
    return False

def copyTreeIfExists (src,dest,logger):
    if os.path.exists(src):
        return copyTree (src,dest,logger)
    return False

def copyFile(_src,_dest,logger):
    try:
        shutil.copy(_src,_dest)
        return True
    except Exception,e:
        logger.error("Failed copying  %s to %s - %s" % (_src, _dest,str(e)))
    return False

def copyFileIfExists(src,dest,logger):
    if os.path.exists(src):
        return copyFile(src,dest,logger)
    return False

# 1 liner
def removeTree(src,logger):
    try:
        shutil.rmtree(src)
        return True
    except Exception,e:
        logger.error("Failed deleting folder %s  - %s" % (src,str(e)))
    return False

def removeFile(src,logger):
    try:
        os.remove(src)
        return True
    except Exception,e:
        logger.error("Failed deleting  %s  - %s" % (src,str(e)))
    return False

def compressFolderContent(srcFolder ,dest,logger,files="*.*"):
    filesList = files
    if files != "*.*":
        filesList = " ".join(map(itemgetter(1),map(os.path.split,files)))
    try:
        os.system("cd %s; tar -czf %s %s" % (srcFolder,dest,filesList))
        return True
    except Exception,e:
        logger.error("Failed compressing to  %s  - %s" % (dest,str(e)))
    return False

# 1 liner






#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# This class is only meant to improve readability when accessing a flow record
# which is a tuple
class REC:
    TIMESTAMP = 0
    DATA = 1
    TITLEKEY = 2

# top metrics constants
class TOP:
    BYTES = 1000
    DURATION = 1000
    HITCOUNT = 1000

# readabilty time constants of number of seconds per period
class SECONDS:
    MINUTE = 60
    HOUR = MINUTE * 60
    DAY = HOUR * 24
    WEEK = DAY * 7

class MINUTES:
    DAY = SECONDS.DAY/60


#-------------------------------------------------------------
# basic time management class on top of unix time vs the decomposition to struct_time
class TopperTime:
    SLICE_MINUTE = 0
    SLICE_HOUR = 1
    SLICE_DAY = 2
    SLICE_WEEK = 3
    SLICE_MONTH = 4
    SLICE_YEAR = 5

    theBaseSlice = 1 # in minutes. Must be smaller than one hour - 60.
    theDefaultSliceGranularity = SLICE_MINUTE

    myUnixTime = 0 # raw 
    myStructTime = 0 # struct_time

    

    def __init__(self,unixtime):
        self.myUnixTime = int(unixtime)
        self.myStructTime = time.gmtime(float(self.myUnixTime))

    def clone (self):
        return TopperTime(self.myUnixTime)

    #return a timestamp rounding down this one to the begining of the minute
    def cloneFromSecondZero(self):
        t = self.myStructTime
        toReduce = t.tm_sec 
        return TopperTime(self.myUnixTime - toReduce)

    #return a timestamp rounding down this one to the begining of the hour
#   def cloneFromMinuteZero(self):
#       t = self.myStructTime
#       toReduce = t.tm_sec + t.tm_min * SECONDS.MINUTE
#       return TopperTime(self.myUnixTime - toReduce)

    #return a timestamp rounding down this one to the begining of the day
    def cloneFromHourZero(self):
        t = self.myStructTime
        toReduce = t.tm_sec + t.tm_min*SECONDS.MINUTE + t.tm_hour*SECONDS.HOUR 
        newUnix=self.myUnixTime - toReduce
        newTime=TopperTime(newUnix)
        if newTime.myStructTime.tm_mday != t.tm_mday:
            newUnix += SECONDS.HOUR
            newTime=TopperTime(newUnix)
        return newTime

    #return a timestamp rounding down this one to the begining of the month
    def cloneFromDayOneOfTheMonth(self):
        t = self.myStructTime
        toReduce = t.tm_sec + t.tm_min*SECONDS.MINUTE + t.tm_hour*SECONDS.HOUR + (t.tm_mday - 1)*SECONDS.DAY
        newUnix=self.myUnixTime - toReduce
        newDate=TopperTime(newUnix)
        # march-april transition thing
        if newDate.myStructTime.tm_mon != t.tm_mon:
            newUnix += SECONDS.HOUR
            newDate=TopperTime(newUnix)
        return newDate

    #return a timestamp rounding down this one to the begining of the month
    def cloneFromDayOneOfTheYear(self):
        year = str(self.myStructTime.tm_year)
        newTimeStruct = time.strptime(year,"%Y")
        newUnix=int(time.mktime(newTimeStruct) - time.timezone)
        newDate=TopperTime(newUnix)
        return newDate

    def toString (self):
        return str() + time.strftime("%a, %d %b %Y %H:%M:%S - ", self.myStructTime) +str(self.myUnixTime)

    def UnixTimeString (self):
        return str(self.myUnixTime)

    #timestamp as a field in a line
    def getMinuteLineTimeStamp(self):
        t = self.myStructTime
        return "%04d-%02d-%02d-%02d:%02d" % (t.tm_year , t.tm_mon , t.tm_mday , t.tm_hour , t.tm_min)

    def getHourLineTimeStamp(self):
        t = self.myStructTime
        return "%04d-%02d-%02d-%02d:00" % (t.tm_year , t.tm_mon , t.tm_mday , t.tm_hour )

    def getDayLineTimeStamp(self):
        t = self.myStructTime
        return "%04d-%02d-%02d" % (t.tm_year , t.tm_mon , t.tm_mday)


    def getMinuteFilename (self,suffix = ".tsv"):
        t = self.myStructTime
        return "%04d%02d%02d-%02d:%02d%s" % (t.tm_year , t.tm_mon, t.tm_mday, t.tm_hour , t.tm_min ,suffix)

    def getHourlyFilename (self,suffix = ".tsv"):
        t = self.myStructTime
        return "%04d%02d%02d-%02d%s" % (t.tm_year , t.tm_mon, t.tm_mday, t.tm_hour , suffix)
        
    def getDaylyFilename (self,suffix = ".tsv"):
        t = self.myStructTime
        return "%04d%02d%02d%s" % (t.tm_year , t.tm_mon, t.tm_mday , suffix)

    def getMonthlyFilename (self,suffix = ".tsv"):
        t = self.myStructTime
        return "%04d%02d%s" % (t.tm_year , t.tm_mon , suffix)

    def getYearlyFilename (self,suffix = ".tsv"):
        t = self.myStructTime
        return "%04d%s" % (t.tm_year  , suffix)


    @staticmethod
    def getGranularitySeconds(granularity):
        if granularity == TopperTime.SLICE_MINUTE:
            return 60
        if granularity == TopperTime.SLICE_HOUR:
            return 3600
        raise Exception, "Granularity not supported"

    # modify the timestamp to be -1 minute
    def goBackOneSlice(self,granularity=theDefaultSliceGranularity):
        self.myUnixTime = self.myUnixTime - TopperTime.getGranularitySeconds(granularity)
        self.myStructTime = time.gmtime(float(self.myUnixTime))

    # modify the timestamp to be +1 minute
    def goForwardOneSlice(self,granularity=theDefaultSliceGranularity):
        self.myUnixTime = self.myUnixTime + TopperTime.getGranularitySeconds(granularity)
        self.myStructTime = time.gmtime(float(self.myUnixTime))

    #return positive if I am in a later slice
    #return negative if other is in a later slice
    #zero if in the same slice
    def sliceCompare(self,other,granularity = theDefaultSliceGranularity):
        t1=self.myStructTime
        t2=other.myStructTime
        # year
        if t1.tm_year> t2.tm_year:
            return 1
        if t1.tm_year< t2.tm_year:
            return -1
        if granularity == TopperTime.SLICE_YEAR:
            return 0
        # month
        if t1.tm_mon > t2.tm_mon:
            return 1
        if t1.tm_mon < t2.tm_mon:
            return -1
        if granularity == TopperTime.SLICE_MONTH:
            return 0
        # week
        s1 = (t1.tm_yday/7)*7
        s2 = (t2.tm_yday/7)*7
        if s1 > s2:
            return 1
        if s2 > s1:
            return -1
        if granularity == TopperTime.SLICE_WEEK:
            return 0
        # day
        if t1.tm_mday > t2.tm_mday:
            return 1
        if t1.tm_mday < t2.tm_mday:
            return -1
        if granularity == TopperTime.SLICE_DAY:
            return 0
        # hour
        if t1.tm_hour > t2.tm_hour:
            return 1
        if t1.tm_hour < t2.tm_hour:
            return -1
        if granularity == TopperTime.SLICE_HOUR:
            return 0
        # minute
        s1 = (t1.tm_min/TopperTime.theBaseSlice)*TopperTime.theBaseSlice
        s2 = (t2.tm_min/TopperTime.theBaseSlice)*TopperTime.theBaseSlice
        if s1 > s2:
            return 1
        if s2 > s1:
            return -1
        return 0



#------------------------------------------------------------
# this class manages reading raw data into memory
class RawDataReader:
    myLines = None
    myLogger = None
    myDataValidator = None
    theCleanFlag = False

    @staticmethod
    def setCleanFlag (value):
        RawDataReader.theCleanFlag = value

    @staticmethod
    def getCleanFlag():
        return RawDataReader.theCleanFlag



    def __init__ (self,logger):
        self.myLogger = logger
        self.myLines = collections.deque()
        self.myDataValidator = RawDataRecordValidator(self.myLogger)
        
    def loadFile(self,file,rateThreshold, recordTimeValidUpperBound):
        __pychecker__='no-argsused'
        linesRead = 0
        fd = a.sys.analytic.topper_record_utils.openFileForRead(file,self.myLogger) 
        if fd==None:
            return False

        localLine = 0
        try:
            lines = fd.readlines()
            for line in lines:
                if self.loadLine(line, recordTimeValidUpperBound):
                    linesRead += 1
                    localLine += 1
        except Exception, e:
            self.myLogger.error("Exception while reading from %s line=%d - %s" %( file ,localLine, str(e)))
        fd.close()

      #  # rate check:
      #  if linesRead > 0:
      #      s = self.myLines[0][0].myUnixTime
      #      e = self.myLines[-1][0].myUnixTime
      #      deltaTime = max(e-s,1)
      #      rate = linesRead/deltaTime
      #      if rate > rateThreshold:
      #          self.myLogger.warning("Rate of input records is %s, in file %s!"%(rate,file))

        return linesRead > 0
        
    
    def fix86 (self):
        if len(self.myLines) > 1:
            t0=self.myLines[0][0]
            t1=self.myLines[1][0]
            if t0.myUnixTime > t1.myUnixTime:
                self.myLogger.info("86 reverse performed")
                self.myLines.reverse()


    def deleteFile(self,filename):
        try:
            os.remove(filename)
        except Exception,e:
            self.myLogger.error("Exception while deleting %s - e=%s" % (filename,str(e)))
        #shutil.move(filename,filename.replace("/data","/_ata"))
        

    def loadLine(self, line, recordTimeValidUpperBound):
        arr = line.split("\t")
        length = len(arr)
        if length==1 and arr[0]=="\n":
            return False
        if  length < a.sys.analytic.topper_record_utils.MIN_FIELDS_IN_RECORD:
            self.myLogger.error("Bad input line - " + line)
            return False
        recType = arr[0]
        if len(recType) != 1:
            self.myLogger.error("Bad input line - " + line)
            return False
        #This is the activation record to release a 1000 bloodthirsty zombies through the PC fan
        # and also clean old history.Was cheaper to get them both using the same command
        if recType=="R": 
            RawDataReader.setCleanFlag (True) #a different module will see this flag outside and take care of it 
            return True

        recordTimeStamp = int(arr[1])
        if recordTimeValidUpperBound != None:
            if recordTimeStamp > recordTimeValidUpperBound:
                self.myLogger.warning("Got a record with unrealistic time in the future:  - " + str(arr) +"... discarding the record!")
                return False

        t = TopperTime(recordTimeStamp)
        if self.myDataValidator.verifyData(arr)==True:
            self.myLines.append([t,arr,""]) # A raw flow record: (timestamp , the entire tokenized line , placeholder for title-id)
            return True
        return False
        
    # time of last record
    def getEarlyestTime (self):
        if not self.hasMoreRecords():
            msg = "getCurrentRecordTime called on empty list"
            self.myLogger.error(msg)
            return TopperTime(0xEFFFFFFF) # 31 bit
        latesttRec = self.myLines[0]
        return latesttRec[0]

    def getCurrentRecordTime(self):
        if not self.hasMoreRecords():
            msg = "getCurrentRecordTime called on empty list"
            self.myLogger.error(msg)
            raise Exception,msg
        lastRec = self.myLines[len(self.myLines)-1]
        t=lastRec[0]
        return t

    def popCurrentRecord(self):
        if not self.hasMoreRecords():
            msg = "popCurrentRecord called on empty list"
            self.myLogger.error(msg)
            raise Exception,msg
        return self.myLines.pop()

    def popEaryestRecord(self):
            if not self.hasMoreRecords():
                msg = "popCurrentRecord called on empty list"
                self.myLogger.error(msg)
                raise Exception,msg
            return self.myLines.popleft()
        

    def hasMoreRecords (self):
        return len(self.myLines) > 0


#------------------------------------------------------------
# the next class is for maintaing the L2 data for the over time reports
class PerPortL2Data:

    def __init__ (self):
        self.clear()

    def clear (self):
        self.myTotalBytesDeliveryPort0In  = 0
        self.myTotalBytesDeliveryPort0Out = 0
        self.myTotalBytesDeliveryPort1In  = 0
        self.myTotalBytesDeliveryPort1Out = 0
        self.myTotalBytesLinePort0In      = 0
        self.myTotalBytesLinePort1In      = 0
        self.myTotalBytesLinePort2In      = 0
        self.myTotalBytesLinePort3In      = 0
        self.myTotalBytesLinePort4In      = 0
        self.myTotalBytesLinePort5In      = 0
        self.myTotalBytesLinePort6In      = 0
        self.myTotalBytesLinePort7In      = 0
        self.myVideoBytesDeliveryPort0In  = 0
        self.myVideoBytesDeliveryPort0Out = 0
        self.myVideoBytesDeliveryPort1In  = 0
        self.myVideoBytesDeliveryPort1Out = 0
        self.myVideoBytesLinePort0In      = 0
        self.myVideoBytesLinePort1In      = 0
        self.myVideoBytesLinePort2In      = 0
        self.myVideoBytesLinePort3In      = 0
        self.myVideoBytesLinePort4In      = 0
        self.myVideoBytesLinePort5In      = 0
        self.myVideoBytesLinePort6In      = 0
        self.myVideoBytesLinePort7In      = 0

    def addTotalBytes (self,totalDelvP0In,totalDelvP0Out,totalDelvP1In,totalDelvP1Out,totalLineP0In,totalLineP1In,totalLineP2In,totalLineP3In,totalLineP4In,totalLineP5In,totalLineP6In,totalLineP7In):
        self.myTotalBytesDeliveryPort0In  += totalDelvP0In
        self.myTotalBytesDeliveryPort0Out += totalDelvP0Out
        self.myTotalBytesDeliveryPort1In  += totalDelvP1In
        self.myTotalBytesDeliveryPort1Out += totalDelvP1Out
        self.myTotalBytesLinePort0In      += totalLineP0In
        self.myTotalBytesLinePort1In      += totalLineP1In
        self.myTotalBytesLinePort2In      += totalLineP2In
        self.myTotalBytesLinePort3In      += totalLineP3In
        self.myTotalBytesLinePort4In      += totalLineP4In
        self.myTotalBytesLinePort5In      += totalLineP5In
        self.myTotalBytesLinePort6In      += totalLineP6In
        self.myTotalBytesLinePort7In      += totalLineP7In

    def addVideoBytes (self,videoDelvP0In,videoDelvP0Out,videoDelvP1In,videoDelvP1Out,videoLineP0In,videoLineP1In,videoLineP2In,videoLineP3In,videoLineP4In,videoLineP5In,videoLineP6In,videoLineP7In):
        self.myVideoBytesDeliveryPort0In  += videoDelvP0In
        self.myVideoBytesDeliveryPort0Out += videoDelvP0Out
        self.myVideoBytesDeliveryPort1In  += videoDelvP1In
        self.myVideoBytesDeliveryPort1Out += videoDelvP1Out
        self.myVideoBytesLinePort0In      += videoLineP0In
        self.myVideoBytesLinePort1In      += videoLineP1In
        self.myVideoBytesLinePort2In      += videoLineP2In
        self.myVideoBytesLinePort3In      += videoLineP3In
        self.myVideoBytesLinePort4In      += videoLineP4In
        self.myVideoBytesLinePort5In      += videoLineP5In
        self.myVideoBytesLinePort6In      += videoLineP6In
        self.myVideoBytesLinePort7In      += videoLineP7In

    def addAllTypesOfBytes(self,totalDelvP0In,totalDelvP0Out,totalDelvP1In,totalDelvP1Out,totalLineP0In,totalLineP1In,totalLineP2In,totalLineP3In,totalLineP4In,totalLineP5In,totalLineP6In,totalLineP7In,\
                           videoDelvP0In,videoDelvP0Out,videoDelvP1In,videoDelvP1Out,videoLineP0In,videoLineP1In,videoLineP2In,videoLineP3In,videoLineP4In,videoLineP5In,videoLineP6In,videoLineP7In):
        self.addTotalBytes(totalDelvP0In,totalDelvP0Out,totalDelvP1In,totalDelvP1Out,totalLineP0In,totalLineP1In,totalLineP2In,totalLineP3In,totalLineP4In,totalLineP5In,totalLineP6In,totalLineP7In)
        self.addVideoBytes(videoDelvP0In,videoDelvP0Out,videoDelvP1In,videoDelvP1Out,videoLineP0In,videoLineP1In,videoLineP2In,videoLineP3In,videoLineP4In,videoLineP5In,videoLineP6In,videoLineP7In)

    def addFromOther(self,other):
        self.myTotalBytesDeliveryPort0In  += other.myTotalBytesDeliveryPort0In 
        self.myTotalBytesDeliveryPort0Out += other.myTotalBytesDeliveryPort0Out
        self.myTotalBytesDeliveryPort1In  += other.myTotalBytesDeliveryPort1In 
        self.myTotalBytesDeliveryPort1Out += other.myTotalBytesDeliveryPort1Out
        self.myTotalBytesLinePort0In      += other.myTotalBytesLinePort0In     
        self.myTotalBytesLinePort1In      += other.myTotalBytesLinePort1In     
        self.myTotalBytesLinePort2In      += other.myTotalBytesLinePort2In     
        self.myTotalBytesLinePort3In      += other.myTotalBytesLinePort3In     
        self.myTotalBytesLinePort4In      += other.myTotalBytesLinePort4In     
        self.myTotalBytesLinePort5In      += other.myTotalBytesLinePort5In     
        self.myTotalBytesLinePort6In      += other.myTotalBytesLinePort6In     
        self.myTotalBytesLinePort7In      += other.myTotalBytesLinePort7In     
        self.myVideoBytesDeliveryPort0In  += other.myVideoBytesDeliveryPort0In 
        self.myVideoBytesDeliveryPort0Out += other.myVideoBytesDeliveryPort0Out
        self.myVideoBytesDeliveryPort1In  += other.myVideoBytesDeliveryPort1In 
        self.myVideoBytesDeliveryPort1Out += other.myVideoBytesDeliveryPort1Out
        self.myVideoBytesLinePort0In      += other.myVideoBytesLinePort0In     
        self.myVideoBytesLinePort1In      += other.myVideoBytesLinePort1In     
        self.myVideoBytesLinePort2In      += other.myVideoBytesLinePort2In     
        self.myVideoBytesLinePort3In      += other.myVideoBytesLinePort3In     
        self.myVideoBytesLinePort4In      += other.myVideoBytesLinePort4In     
        self.myVideoBytesLinePort5In      += other.myVideoBytesLinePort5In     
        self.myVideoBytesLinePort6In      += other.myVideoBytesLinePort6In     
        self.myVideoBytesLinePort7In      += other.myVideoBytesLinePort7In     


    # this function spreads the fields in the order in which they will appear in the reports -> order is chronoligical. first to be added first. 
    # this may look like a mess but it preserves backward compatibility of the reports and reports are not meant for human eye anyways.
    def toArray(self):
        return map(str,[self.myTotalBytesDeliveryPort0In,
                        self.myTotalBytesDeliveryPort0Out,
                        self.myTotalBytesLinePort0In,
                        self.myTotalBytesLinePort1In,
                        self.myTotalBytesLinePort2In,
                        self.myTotalBytesLinePort3In,
                        self.myVideoBytesDeliveryPort0In,
                        self.myVideoBytesDeliveryPort0Out,
                        self.myVideoBytesLinePort0In,
                        self.myVideoBytesLinePort1In,
                        self.myVideoBytesLinePort2In,
                        self.myVideoBytesLinePort3In,
                        self.myTotalBytesDeliveryPort1In,
                        self.myTotalBytesDeliveryPort1Out,
                        self.myVideoBytesDeliveryPort1In,
                        self.myVideoBytesDeliveryPort1Out,
                        self.myTotalBytesLinePort4In,
                        self.myTotalBytesLinePort5In,
                        self.myTotalBytesLinePort6In,
                        self.myTotalBytesLinePort7In,
                        self.myVideoBytesLinePort4In,
                        self.myVideoBytesLinePort5In,
                        self.myVideoBytesLinePort6In,
                        self.myVideoBytesLinePort7In])

    @staticmethod
    def toHeader():
        return ['TotalBytesDeliveryPort0In',
                'TotalBytesDeliveryPort0Out',
                'TotalBytesLinePort0In',
                'TotalBytesLinePort1In',
                'TotalBytesLinePort2In',
                'TotalBytesLinePort3In',
                'VideoBytesDeliveryPort0In',
                'VideoBytesDeliveryPort0Out',
                'VideoBytesLinePort0In',
                'VideoBytesLinePort1In',
                'VideoBytesLinePort2In',
                'VideoBytesLinePort3In',
                'TotalBytesDeliveryPort1In',
                'TotalBytesDeliveryPort1Out',
                'VideoBytesDeliveryPort1In',
                'VideoBytesDeliveryPort1Out',
                'TotalBytesLinePort4In',
                'TotalBytesLinePort5In',
                'TotalBytesLinePort6In',
                'TotalBytesLinePort7In',
                'VideoBytesLinePort4In',
                'VideoBytesLinePort5In',
                'VideoBytesLinePort6In',
                'VideoBytesLinePort7In']


    def getTotalsSum(self):
        return  self.myTotalBytesDeliveryPort0Out + self.myTotalBytesLinePort0In + self.myTotalBytesLinePort1In + self.myTotalBytesLinePort2In + self.myTotalBytesLinePort3In     



#------------------------------------------------------------
# manage data of 2 ports seperately and together
# this only serves total bytes which don't have the servable fields
class PerPortData:
    theBGSFactor = 1.5
    theBGSCap = 0.9


    def clear (self):
        #self.myPort0Data = 0
        #self.myPort1Data = 0
        self.myTotalData = 0

    def __init__ (self):
        self.clear()

    #custom serialization 10x faster than pickle
    def serialize(self,fd):
        fd.write(struct.pack("<Q",self.myTotalData))

    def deSerialize(self,fd):
        rawnum = fd.read(8)
        self.myTotalData = struct.unpack('<Q', rawnum)[0]


    def clone (self):
        obj=PerPortData()
        obj.myTotalData = self.myTotalData 
        return obj


    def addData (self,port0,port1):
        #self.myPort0Data += port0
        #self.myPort1Data += port1
        self.myTotalData += (port0+port1)

    def addSingularData(self,data):
        self.myTotalData += data

    def subtractData(self,port0,port1):
        #self.myPort0Data -= port0
        #self.myPort1Data -= port1
        self.myTotalData -= (port0+port1)

    def subtractSingularData(self,data):
        self.myTotalData -= data

    def addFromOther (self,other):
        #self.myPort0Data += other.myPort0Data
        #self.myPort1Data += other.myPort1Data
        self.myTotalData += other.myTotalData

    def toArray (self):
        return [self.myTotalData]

    def depleated (self):
        return (self.myTotalData <= 0)

#------------------------------------------------------------
# Extends PerPortData to also include servable
class PerPortDataExtended(PerPortData):

    def clear(self):
        PerPortData.clear(self)
        self.myTotalServable = 0
        self.myTotalDelivered = 0
        

    def __init__(self):
        PerPortData.__init__(self)
        self.clear()

    def clone (self):
        obj=PerPortDataExtended()
        obj.myTotalData = self.myTotalData 
        obj.myTotalServable = self.myTotalServable
        obj.myTotalDelivered = self.myTotalDelivered

    def getBGS(self):
        bgs = float(self.myTotalServable)*PerPortData.theBGSFactor 
        cap = max(float(self.myTotalData)*PerPortData.theBGSCap - self.myTotalDelivered,0) # keep the cap between 0 and total-delivered
        
        return long(min(bgs,cap))

    def addServable(self,port0,port1):
        #self.myServablePort0 += port0
        #self.myServablePort1 += port1
        self.myTotalServable += (port0+port1)
        
    def addSingularServable(self,data):
        self.myTotalServable += data

    def subtractServable(self,port0,port1):
        #self.myServablePort0 -= port0
        #self.myServablePort1 -= port1
        self.myTotalServable -= (port0+port1)

    def subtractSingularServable(self,data):
        self.myTotalServable -= data

    def addDelivered(self,port0,port1):
        #self.myDeliveredPort0 += port0
        #self.myDeliveredPort1 += port1
        self.myTotalDelivered += (port0+port1)

    def addSingularDelivered(self,data):
        self.myTotalDelivered += data

    def subtractDelivered(self,port0,port1):
        #self.myDeliveredPort0 -= port0
        #self.myDeliveredPort1 -= port1
        self.myTotalDelivered -= (port0+port1)

    def subtractSingularDelivered(self,data):
        self.myTotalDelivered -= data

    def addFromOther (self,other):
        PerPortData.addFromOther(self,other)
        #self.myServablePort0 += other.myServablePort0 
        #self.myServablePort1 += other.myServablePort1
        self.myTotalServable += other.myTotalServable
        #self.myBGSServable += other.myBGSServable
        #self.myDeliveredPort0 += other.myDeliveredPort0
        #self.myDeliveredPort1 += other.myDeliveredPort1
        self.myTotalDelivered += other.myTotalDelivered

    def toArray (self):
        return PerPortData.toArray(self) + [self.myTotalServable, self.getBGS(), self.myTotalDelivered]

    def totalsArray(self):
        return [self.myTotalData,self.myTotalServable,self.myTotalDelivered]

    #custom serialization 10x faster than pickle
    def serialize(self,fd):
        fd.write(struct.pack("<QQQ",self.myTotalData,self.myTotalServable,self.myTotalDelivered))

    def deSerialize(self,fd):
        rawnum = fd.read(8)
        self.myTotalData = struct.unpack('<Q', rawnum)[0]

        rawnum = fd.read(8)
        self.myTotalServable = struct.unpack('<Q', rawnum)[0]

        rawnum = fd.read(8)
        self.myTotalDelivered = struct.unpack('<Q', rawnum)[0]

    def isCleared (self):
        return (self.myTotalData==0)

#------------------------------------------------------------
# this class handles per-port servable vs total statistics
class BWRecord:
    theMetricMapper = {}

    def __init__ (self):
        self.myL2Bytes = PerPortL2Data() # no servable for total bytes
        self.myVideoBytes = PerPortDataExtended()
        self.mySessions = PerPortDataExtended()
        self.mySeconds = PerPortDataExtended()

    def clear(self):
        self.myL2Bytes.clear() 
        self.myVideoBytes.clear()
        self.mySessions.clear()
        self.mySeconds.clear()


    def addBytesFromOther (self,other):
        self.myL2Bytes.addFromOther(other.myL2Bytes)
        self.myVideoBytes.addFromOther(other.myVideoBytes)

    def addSessionsFromOther(self,other):
        self.mySessions.addFromOther(other.mySessions)

    def addSecondsFromOther(self,other):
        self.mySeconds.addFromOther(other.mySeconds)

    #collected from portions of the servable video coming from flow records
    def addServableVideo (self,port0Servable,port1Servable):
        self.myVideoBytes.addServable(port0Servable,port1Servable)


    #collected from in-memory bw records
    def addFromRawrecord (self,record):
        data = record[REC.DATA]
        relevantOffsets = [BwRecordOffsets.theTotalBytesDeliveryPort0InOffset.myVal,
                           BwRecordOffsets.theTotalBytesDeliveryPort0OutOffset.myVal,
                           BwRecordOffsets.theTotalBytesDeliveryPort1InOffset.myVal,
                           BwRecordOffsets.theTotalBytesDeliveryPort1OutOffset.myVal,
                           BwRecordOffsets.theTotalBytesLinePort0InOffset.myVal,
                           BwRecordOffsets.theTotalBytesLinePort1InOffset.myVal,
                           BwRecordOffsets.theTotalBytesLinePort2InOffset.myVal,
                           BwRecordOffsets.theTotalBytesLinePort3InOffset.myVal,
                           BwRecordOffsets.theTotalBytesLinePort4InOffset.myVal,
                           BwRecordOffsets.theTotalBytesLinePort5InOffset.myVal,
                           BwRecordOffsets.theTotalBytesLinePort6InOffset.myVal,
                           BwRecordOffsets.theTotalBytesLinePort7InOffset.myVal,
                           BwRecordOffsets.theVideoBytesDeliveryPort0InOffset.myVal,
                           BwRecordOffsets.theVideoBytesDeliveryPort0OutOffset.myVal,
                           BwRecordOffsets.theVideoBytesDeliveryPort1InOffset.myVal,
                           BwRecordOffsets.theVideoBytesDeliveryPort1OutOffset.myVal,
                           BwRecordOffsets.theVideoBytesLinePort0InOffset.myVal,
                           BwRecordOffsets.theVideoBytesLinePort1InOffset.myVal,
                           BwRecordOffsets.theVideoBytesLinePort2InOffset.myVal,
                           BwRecordOffsets.theVideoBytesLinePort3InOffset.myVal,
                           BwRecordOffsets.theVideoBytesLinePort4InOffset.myVal,
                           BwRecordOffsets.theVideoBytesLinePort5InOffset.myVal,
                           BwRecordOffsets.theVideoBytesLinePort6InOffset.myVal,
                           BwRecordOffsets.theVideoBytesLinePort7InOffset.myVal]

        bytesArray = map(lambda offset: long(data[offset]),relevantOffsets)

        self.myL2Bytes.addAllTypesOfBytes(*bytesArray)


    #collected from snapshot records which includes also servable data
    #def addFromRawSnapshotrecord (self,record):
    #    data = record[REC.DATA]
    #    self.addFromRawrecord(record)
    #    self.myVideoBytes.addServable(long(data[BwRecordOffsets.thePort0ServableOffset.myVal]) , long(data[BwRecordOffsets.thePort1ServableOffset.myVal]))
    #    self.mySessions.addServable(long(data[BwRecordOffsets.thePort0SessionsServableOffset.myVal]) , long(data[BwRecordOffsets.thePort1SessionsServableOffset.myVal]))
    #    self.mySeconds.addServable(long(data[BwRecordOffsets.thePort0SecondsServableOffset.myVal]) , long(data[BwRecordOffsets.thePort1SecondsServableOffset.myVal]))
     
            
    #we expand the format of the raw V record to also include servable data
    # so that we can use the same mechanism to read it later from disk snapshot
    #def exportToSnapshotRecord (self,unixtime):
    #    last = BwRecordOffsets.thePort1SecondsServableOffset.myVal
    #    data = (last+1)*[long(0)] #preallocate array
    #    data[0] = "W" # used internally only
    #    data[1] = unixtime
    #    data[BwRecordOffsets.thePort0totalOffset.myVal] = self.myBytes.myTotalData
    #    data[BwRecordOffsets.thePort1totalOffset.myVal] = self.myBytes.myPort1Data
    #    data[BwRecordOffsets.thePort0videoOffset.myVal] = self.myVideoBytes.myPort0Data
    #    data[BwRecordOffsets.thePort1videoOffset.myVal] = self.myVideoBytes.myPort1Data
    #    data[BwRecordOffsets.thePort0ServableOffset.myVal] = self.myVideoBytes.myServablePort0
    #    data[BwRecordOffsets.thePort1ServableOffset.myVal] = self.myVideoBytes.myServablePort1
    #    #---------------------------------------------------------------------------------------
    #    data[BwRecordOffsets.thePort0videoSessionsOffset.myVal] = self.mySessions.myPort0Data
    #    data[BwRecordOffsets.thePort1videoSessionsOffset.myVal] = self.mySessions.myPort1Data
    #    data[BwRecordOffsets.thePort0SessionsServableOffset.myVal] = self.mySessions.myServablePort0
    #    data[BwRecordOffsets.thePort1SessionsServableOffset.myVal] = self.mySessions.myServablePort1
    #    #---------------------------------------------------------------------------------------
    #    data[BwRecordOffsets.thePort0videoSecondsOffset.myVal] = self.mySeconds.myPort0Data
    #    data[BwRecordOffsets.thePort1videoSecondsOffset.myVal] = self.mySeconds.myPort1Data
    #    data[BwRecordOffsets.thePort0SecondsServableOffset.myVal] = self.mySeconds.myServablePort0
    #    data[BwRecordOffsets.thePort1SecondsServableOffset.myVal] = self.mySeconds.myServablePort1
    #    return map(str,data)


    #The export functions below are used for the bw reports creation
    # order must be consistent with the matching addXfromStringArray functions below
    def exportVideoBytesData(self):
        #return [self.myBytes.myPort0Data,self.myBytes.myPort1Data,self.myVideoBytes.myPort0Data,self.myVideoBytes.myPort1Data,self.myVideoBytes.myServablePort0,self.myVideoBytes.myServablePort1,self.myVideoBytes.getBGS()]
        # flattened data to report a sum of ports 0,1 on port 0
        totalL2Estimate = self.myL2Bytes.myTotalBytesDeliveryPort0Out + self.myL2Bytes.myTotalBytesLinePort0In + self.myL2Bytes.myTotalBytesLinePort1In + self.myL2Bytes.myTotalBytesLinePort2In + self.myL2Bytes.myTotalBytesLinePort3In
        totalVideo = self.myVideoBytes.myTotalData
        servableUndelivered = self.myVideoBytes.myTotalServable
        servableUndeliveredBGS = self.myVideoBytes.getBGS()
        delivered = self.myVideoBytes.myTotalDelivered
        totalServable = servableUndelivered +delivered
        totalServableBGS = servableUndeliveredBGS +delivered

        return [totalL2Estimate, 0,
                totalVideo, 0,
                totalServable,0,     # last 2 fields are calculated but will not be read in the addXxxFromStringArray (they are redundent)
                totalServableBGS,0,
                delivered, 0,
                servableUndelivered, 0,
                servableUndeliveredBGS] + self.myL2Bytes.toArray()

    @staticmethod
    def exportVideoBytesHeader():
        return ['TotalL2EstimateBytes', 0,
                'TotalVideoBytes', 0,
                'TotalServableBytes',0,
                'TotalServableBGSBytes',0,
                'DeliveredBytes', 0,
                'ServableUndeliveredBytes', 0,
                'ServableUndeliveredBGSBytes'] + PerPortL2Data.toHeader()

    def exportSessionData(self):
        #return [self.mySessions.myPort0Data,self.mySessions.myPort1Data,self.mySessions.myServablePort0,self.mySessions.myServablePort1,self.mySessions.getBGS()]
        # flattened data to report a sum of ports 0,1 on port 0
        totalSessions = self.mySessions.myTotalData
        servableUndelivered = self.mySessions.myTotalServable
        servableUndeliveredBGS = self.mySessions.getBGS()
        delivered = self.mySessions.myTotalDelivered
        totalServable = servableUndelivered +delivered
        totalServableBGS = servableUndeliveredBGS +delivered

        return [totalSessions,0,
                totalServable,0, # these fields are calculated but will not be read in the addXxxFromStringArray (they are redundent)
                totalServableBGS,0,
                delivered,0,
                servableUndelivered,0,
                servableUndeliveredBGS]

    @staticmethod
    def exportSessionHeader():
        return ['TotalSessions',0,
                'TotalServableSessions',0,
                'TotalServableBGSSessions',0,
                'DeliveredSessions',0,
                'ServableUndeliveredSessions',0,
                'ServableUndeliveredBGSSessions']

    def exportSecondsData(self):
        #return [self.mySeconds.myPort0Data,self.mySeconds.myPort1Data,self.mySeconds.myServablePort0,self.mySeconds.myServablePort1,self.mySeconds.getBGS()]
        # flattened data to report a sum of ports 0,1 on port 0
        totalSeconds = self.mySeconds.myTotalData
        servableUndelivered = self.mySeconds.myTotalServable
        servableUndeliveredBGS = self.mySeconds.getBGS()
        delivered = self.mySeconds.myTotalDelivered
        totalServable = servableUndelivered +delivered
        totalServableBGS = servableUndeliveredBGS +delivered

        return [totalSeconds, 0,
                totalServable,0, # these fields are calculated but will not be read in the addXxxFromStringArray (they are redundent)
                totalServableBGS,0,
                delivered,0,
                servableUndelivered,0,
                servableUndeliveredBGS]

    @staticmethod
    def exportSecondsHeader():
        return ['TotalSeconds', 0,
                'TotalServableSeconds',0,
                'TotalServableBGSSeconds',0,
                'DeliveredSeconds',0,
                'ServableUndeliveredSeconds',0,
                'ServableUndeliveredBGSSeconds']


    # *** Order must be preserved and consistent with the export functions above ***
    def addBytesFromStringArray(self,arr):
        self.myVideoBytes.myTotalData += tru.getTotalL7Volume(arr)
        self.myVideoBytes.myTotalServable += tru.getServableUndeliveredL7Volume(arr)
        self.myVideoBytes.myTotalDelivered += tru.getDeliveredL7Volume(arr)

        L2BytesArray = [tru.getDeliveredL2Port0InVolume(arr),
                        tru.getDeliveredL2Port0OutVolume(arr),
                        tru.getDeliveredL2Port1InVolume(arr),
                        tru.getDeliveredL2Port1OutVolume(arr),
                        tru.getLinedL2Port0InVolume(arr),
                        tru.getLinedL2Port1InVolume(arr),
                        tru.getLinedL2Port2InVolume(arr),
                        tru.getLinedL2Port3InVolume(arr),
                        tru.getLinedL2Port4InVolume(arr),
                        tru.getLinedL2Port5InVolume(arr),
                        tru.getLinedL2Port6InVolume(arr),
                        tru.getLinedL2Port7InVolume(arr),
                        tru.getDeliveredL2Port0InVideoVolume(arr),
                        tru.getDeliveredL2Port0OutVideoVolume(arr),
                        tru.getDeliveredL2Port1InVideoVolume(arr),
                        tru.getDeliveredL2Port1OutVideoVolume(arr),
                        tru.getLinedL2Port0InVideoVolume(arr),
                        tru.getLinedL2Port1InVideoVolume(arr),
                        tru.getLinedL2Port2InVideoVolume(arr),
                        tru.getLinedL2Port3InVideoVolume(arr),
                        tru.getLinedL2Port4InVideoVolume(arr),
                        tru.getLinedL2Port5InVideoVolume(arr),
                        tru.getLinedL2Port6InVideoVolume(arr),
                        tru.getLinedL2Port7InVideoVolume(arr)]

        self.myL2Bytes.addAllTypesOfBytes(*L2BytesArray)

        return True

    # *** Order must be preserved and consistent with the export functions above ***
    def addSessionsFromStringArray (self,arr):
        self.mySessions.myTotalData += tru.getTotalSessions(arr)
        self.mySessions.myTotalServable += tru.getServableUndeliveredSessions(arr)
        self.mySessions.myTotalDelivered += tru.getDeliveredSessions(arr)
        return True

    # *** Order must be preserved and consistent with the export functions above ***
    def addSecondsFromStringArray (self,arr):
        self.mySeconds.myTotalData += tru.getTotalSeconds(arr)
        self.mySeconds.myTotalServable += tru.getServableUndeliveredSeconds(arr)
        self.mySeconds.myTotalDelivered += tru.getDeliveredSeconds(arr)
        
        return True

    #will receive as a parameter one of the funcs above
    def exportToStringArray (self,arrayRetrievefunc):
        return map(str,arrayRetrievefunc(self))


#------------------------------------------------------------
# the purpose of this class is to maintain all the data
# we care about in the last hour, but don't want to keep beyond the last hour
# as it consumes too much space
class TopperRecordData:
    def __init__(self):
        self.myBytes = PerPortDataExtended()
        self.mySessions = PerPortDataExtended()
        self.mySeconds = PerPortDataExtended()
        self.myHitCount = 0;# This variable was added (post build 172) to maintain hitcount as sessions no longer have 1:1 relations to hitcount
        self.myAdditionalKeyFields = []


    def depleated (self):
        return self.myBytes.depleated() and self.mySessions.depleated() and self.mySeconds.depleated()

    def clear (self):
        self.myBytes.clear()
        self.mySessions.clear()
        self.mySeconds.clear()
        self.myHitCount = 0;
        self.myAdditionalKeyFields = []

    #custom serialization 10x faster than pickle
    def serialize(self,fd):
        self.myBytes.serialize(fd)
        self.mySessions.serialize(fd)
        self.mySeconds.serialize(fd)
        #no need to serialize hitcount - metric reports do not use it
        # additional tokens handled by titleTopperRecord

    def deSerialize(self,fd):
        self.myBytes.deSerialize(fd)
        self.mySessions.deSerialize(fd)
        self.mySeconds.deSerialize(fd)
        #no need to serialize hitcount - metric reports do not use it
        # additional tokens handled by titleTopperRecord


# topper records tracking all metrics against a certain key
# when tracking title , we use the derived class TitleTopperRecord that behaves a little differently
class TopperRecord:
    def __init__(self,data):
        if data==None:
            self.myData = TopperRecordData()
        else:
            self.myData = data
        self.amICachable = False
        self.amIDelivered = False

    def __str__ (self):
        return str(self.myData)

    # serialization is done here explicitly and not by using cpickle 
    # as I must trade convenience for speed - more than x10
    def serialize(self,fd):
        fd.write(struct.pack("H",0xF1F1)) #object type
        self.myData.serialize(fd)
        
    def deSerialize(self,fd):
        # object type was decoded outside in order to construct the right object
        self.myData.deSerialize(fd)
        
    def monitoredCounters (self):
        return self.myData.myBytes.toArray() + self.myData.mySessions.toArray() +self.myData.mySeconds.toArray()

    # do none on standard record, only on the derived title record
    def addAdditionalKeys(self,record, additionalkeyoffsets):
        pass # do nothing here
        
    def getAdditionalFields(self):
        return [] # nothing here

    #we split the call as titleTopper is updating the video sessions and time during cachable update
    def addVolumeFromRawRecord (self,record):
        p0Bytes = record[REC.DATA][FlowRecordOffsets.theDownloadedContentBytesPort0Offset.myVal]
        p1Bytes = record[REC.DATA][FlowRecordOffsets.theDownloadedContentBytesPort1Offset.myVal]

        self.myData.myBytes.addData(p0Bytes,p1Bytes)
        if record[REC.DATA][FlowRecordOffsets.theIsCachableIndicator.myVal]=="1":
            self.myData.myBytes.addServable(p0Bytes,p1Bytes)
        if record[REC.DATA][FlowRecordOffsets.theIsDeliveredIndicator.myVal]=="1":
            self.myData.myBytes.addDelivered(p0Bytes,p1Bytes)

    #we split the call as titleTopper is updating the video sessions and time during cachable update
    def addSessionAndTimeFromRawRecord (self,record):
        initiatorPort = record[REC.DATA][FlowRecordOffsets.theInitiatorPortNumber.myVal]
        #we only count sessions which are last in transaction (where there are long sessions with periodic reports)
        #also we check the begin offset is 0 in order to count the session
        sessionCounter = record[REC.DATA][FlowRecordOffsets.theSessionHitCount.myVal]
        
        timeArgs    = None
        sessionArgs = None
        if initiatorPort==0: # the flow initiator determines if the hitcount and seconds are counted on port 0 or 1
            sessionArgs = (sessionCounter,0)
            timeArgs    = (record[REC.DATA][FlowRecordOffsets.theDownloadTimeMsec.myVal],0)
        else:
            sessionArgs = (0,sessionCounter)
            timeArgs    = (0,record[REC.DATA][FlowRecordOffsets.theDownloadTimeMsec.myVal])

        # total sessions and time are always added
        self.myData.mySessions.addData(*sessionArgs)
        self.myData.mySeconds.addData(*timeArgs)

        if record[REC.DATA][FlowRecordOffsets.theIsCachableIndicator.myVal]=="1":
            self.myData.mySessions.addServable(*sessionArgs)
            self.myData.mySeconds.addServable(*timeArgs)

        if record[REC.DATA][FlowRecordOffsets.theIsDeliveredIndicator.myVal]=="1":
            self.myData.mySessions.addDelivered(*sessionArgs)
            self.myData.mySeconds.addDelivered(*timeArgs)

    
    def addFromRawRecord (self,record):
        self.myData.myHitCount+=1
        self.addVolumeFromRawRecord(record)
        self.addSessionAndTimeFromRawRecord(record)

    
    def subtractFromRawRecord (self,record):
        if self.myData.myHitCount == 0: # prevent going under zero (if does - it's a bug)
            return self.assertNoneBelowZero()
        self.myData.myHitCount -= 1
        p0Bytes = record[REC.DATA][FlowRecordOffsets.theDownloadedContentBytesPort0Offset.myVal]
        p1Bytes = record[REC.DATA][FlowRecordOffsets.theDownloadedContentBytesPort1Offset.myVal]

        initiatorPort = record[REC.DATA][FlowRecordOffsets.theInitiatorPortNumber.myVal]
        #we only count sessions which are last in transaction (where there are long sessions with periodic reports)
        sessionCounter = record[REC.DATA][FlowRecordOffsets.theSessionHitCount.myVal]

        timeArgs    = None
        sessionArgs = None

        if initiatorPort==0: # the flow initiator determines if the hitcount and seconds are counted on port 0 or 1
            sessionArgs = (sessionCounter,0)
            timeArgs    = (record[REC.DATA][FlowRecordOffsets.theDownloadTimeMsec.myVal] , 0)
        else:
            sessionArgs = (0,sessionCounter)
            timeArgs    = (0,record[REC.DATA][FlowRecordOffsets.theDownloadTimeMsec.myVal])

        # we subtract the total always
        self.myData.myBytes.subtractData(p0Bytes,p1Bytes)
        self.myData.mySessions.subtractData(*sessionArgs)
        self.myData.mySeconds.subtractData(*timeArgs)

        if record[REC.DATA][FlowRecordOffsets.theIsCachableIndicator.myVal]=="1":
            #cachable (servable)
            self.myData.myBytes.subtractServable(p0Bytes,p1Bytes)
            self.myData.mySessions.subtractServable(*sessionArgs)
            self.myData.mySeconds.subtractServable(*timeArgs)

        if record[REC.DATA][FlowRecordOffsets.theIsDeliveredIndicator.myVal]=="1":
            #delivered
            self.myData.myBytes.subtractDelivered(p0Bytes,p1Bytes)
            self.myData.mySessions.subtractDelivered(*sessionArgs)
            self.myData.mySeconds.subtractDelivered(*timeArgs)

        
    def assertNoneBelowZero (self):
        for counter in self.monitoredCounters():
            if counter < 0:
                counter = 0
                return False
        return True

    def subtractFromSliceCounter (self,sliceCounter):
        if not(sliceCounter.isCleared()):
            self.myData.myBytes.subtractSingularData(sliceCounter.myBytes.myTotalData)
            self.myData.myBytes.subtractSingularServable(sliceCounter.myBytes.myTotalServable)
            self.myData.myBytes.subtractSingularDelivered(sliceCounter.myBytes.myTotalDelivered)

            self.myData.mySessions.subtractSingularData(sliceCounter.mySessions.myTotalData)
            self.myData.mySessions.subtractSingularServable(sliceCounter.mySessions.myTotalServable)
            self.myData.mySessions.subtractSingularDelivered(sliceCounter.mySessions.myTotalDelivered)

            self.myData.mySeconds.subtractSingularData(sliceCounter.mySeconds.myTotalData)
            self.myData.mySeconds.subtractSingularServable(sliceCounter.mySeconds.myTotalServable)
            self.myData.mySeconds.subtractSingularDelivered(sliceCounter.mySeconds.myTotalDelivered)

            return self.assertNoneBelowZero()

#----------------------------------------------------------------        
class TitleTopperRecord(TopperRecord):

    # serialization is done here explicitly and not by using cpickle 
    # as I must trade convenience for speed - more than x10
    def serialize(self,fd):
        fd.write(struct.pack("H",0xF2F2)) #object type
        self.myData.serialize(fd)
        num=len(self.myData.myAdditionalKeyFields)
        #how many additional tokens do we have
        fd.write(struct.pack("<H",num))
        for token in self.myData.myAdditionalKeyFields:
            tokenLen=len(token)
            fd.write(struct.pack("<H%ds" % tokenLen,tokenLen,token))

    def deSerialize(self,fd):
        # object type was decoded outside in order to construct the right object
        self.myData.deSerialize(fd)
        rawnum = fd.read(2)
        num = struct.unpack('<H', rawnum)[0]
        for i in range(num):
            rawnum = fd.read(2)
            tokenLen=struct.unpack('<H', rawnum)[0]
            rawnum=fd.read(tokenLen)
            #token=struct.unpack('%ds' % tokenLen, rawnum)[0]
            self.myData.myAdditionalKeyFields.append(rawnum)

    def addAdditionalKeys(self,record, additionalkeyoffsets):
        data = record[REC.DATA]
        datalen = len(data)
        for offset in additionalkeyoffsets:
            if offset < datalen:
                item = data[offset]
                self.myData.myAdditionalKeyFields.append(item)
            else:
                pass # todo - log error

    def getAdditionalFields(self):
        return self.myData.myAdditionalKeyFields + [self.myData.myBytes.myTotalData,self.myData.mySeconds.myTotalData,self.myData.mySessions.myTotalData]

    def getSnapshotData(self,key):
        lastHitTime = 0
        if self.myData is None:
            return [key,self.amICachable,lastHitTime]
        return [key,self.amICachable,lastHitTime] + self.myData.myAdditionalKeyFields

    def setFromSnapshot (self,arr):
        self.amICachable = arr[1]
        self.myData.myAdditionalKeyFields = arr[3:]

#----------------------------------------------------------------

class PerSliceCounters:

    def __init__ (self):
        self.myBytes    = PerPortDataExtended()
        self.mySessions = PerPortDataExtended()
        self.mySeconds  = PerPortDataExtended()

    def isCleared (self):
        return (self.myBytes.isCleared() and self.mySessions.isCleared() and self.mySeconds.isCleared())

    def updateFromRawRecord (self,record):
        
        p0Bytes = record[REC.DATA][FlowRecordOffsets.theDownloadedContentBytesPort0Offset.myVal]
        p1Bytes = record[REC.DATA][FlowRecordOffsets.theDownloadedContentBytesPort1Offset.myVal]
        sessions = record[REC.DATA][FlowRecordOffsets.theSessionHitCount.myVal]
        seconds = record[REC.DATA][FlowRecordOffsets.theDownloadTimeMsec.myVal]
        isCachable = (record[REC.DATA][FlowRecordOffsets.theIsCachableIndicator.myVal]=="1")
        isDelivered = (record[REC.DATA][FlowRecordOffsets.theIsDeliveredIndicator.myVal]=="1")

        self.myBytes.addData(p0Bytes,p1Bytes)
        self.mySessions.addSingularData(sessions)
        self.mySeconds.addSingularData(seconds)

        if isCachable:
            self.myBytes.addServable(p0Bytes,p1Bytes)
            self.mySessions.addSingularServable(sessions)
            self.mySeconds.addSingularServable(seconds)

        if isDelivered:
            self.myBytes.addDelivered(p0Bytes,p1Bytes)
            self.mySessions.addSingularDelivered(sessions)
            self.mySeconds.addSingularDelivered(seconds)



class RawRecordsSlice:

    def __init__(self,toppertime):
        self.myLogger = None
        #self.myRawRecords = []
        #self.myTopperPacks = []
        self.myRepresentingTimeSlice = toppertime.clone()
        self.myBWRecord  = BWRecord()
        self.mySitesCounters = {}


    def updateSiteCounters(self,record):
        siteId = record[REC.DATA][FlowRecordOffsets.theHostOffset.myVal]
        perSliceSiteCounter = None
        if siteId not in self.mySitesCounters:
            perSliceSiteCounter = PerSliceCounters()
            self.mySitesCounters[siteId] = perSliceSiteCounter
        else:
            perSliceSiteCounter = self.mySitesCounters[siteId]

        perSliceSiteCounter.updateFromRawRecord(record)


    def clear(self):
        self.myBWRecord.clear()

    def setLogger(self,logger):
        self.myLogger = logger

    def getMinuteBWRecord (self,exportFunc):
        t=self.myRepresentingTimeSlice
        st = t.getMinuteLineTimeStamp()
        b = self.myBWRecord
        return [st,] + b.exportToStringArray(exportFunc)
        

#------------------------------------------------------------
# each topper maintains the metrics accounting for his key
# the topper holds a limited size table, controlled by an LRU
class Topper(object):
    
    def allocateNewTopperRecord(self,node):
        __pychecker__='no-argsused'
        return TopperRecord(None)

    def __init__(self,logger,cfg,topperName,keyOffset,additionalKeyFieldsOffsets,everyMinuteTop,reasonableProcessingTime,shouldIgnoreIndicator=lambda id:False):
        self.myLogger = logger
        self.myCfg = cfg
        self.myKeyOffset = keyOffset
        self.myTopperName = topperName
        self.myAdditionalKeyOffsets = additionalKeyFieldsOffsets
        self.isLoggingDebug = False
        self.isWritingPareto = False
        self.myReasonableProcessingTime = reasonableProcessingTime
        #init interprocess queues
        self.myVolumeMpQueue = mp.JoinableQueue()
        self.myTimeMpQueue = mp.JoinableQueue()
        self.mySessionMpQueue = mp.JoinableQueue()
        self.myVolumeAckMpQueue = mp.JoinableQueue()
        self.myTimeAckMpQueue = mp.JoinableQueue()
        self.mySessionAckMpQueue = mp.JoinableQueue()
        self.myTasksStatus = {}
        #self.myTaskDoneIndicators = mp.Array("i",3)# shared memory array
        self.myTopReportLineLegend = TopperReportLine()
        self.myEveryMinuteTop = everyMinuteTop
        self.myShouldIgnoreIndicator = shouldIgnoreIndicator

    def removeDoneWithFiles(self):
        # collect used files
        for queue in [self.myVolumeAckMpQueue,self.myTimeAckMpQueue,self.mySessionAckMpQueue]:
            while not queue.empty():
                filename,processingTime = queue.get()
                queue.task_done()
                if filename not in self.myTasksStatus:
                    self.myLogger.error("This is strange, the file %s was supposed to be in %s-topper's myTaskStats dictionary but it isn't"%(filename,self.myTopperName))
                else:
                    self.myTasksStatus[filename]["cntDones"]+=1
                    self.myTasksStatus[filename]["maxProcessingTime"]+= max(self.myTasksStatus[filename]["maxProcessingTime"],processingTime)

        # remove files that are not needed
        filesToRemove = []
        for filename,status in self.myTasksStatus.items():
            if status["cntDones"]==3:
                maxProcessingTime = status["maxProcessingTime"]
                if maxProcessingTime>self.myReasonableProcessingTime:
                    self.myLogger.warning("processing time for file %s was %s!"%(filename,processingTime))
                else:
                    self.myLogger.debug("processing time for file %s was %s"%(filename,processingTime))
                filesToRemove.append(filename)
                
        for fileName in filesToRemove:
            removeFile(fileName,self.myLogger)
            del self.myTasksStatus[fileName]

        # Alert on files that were dispatched a while ago
        now=int(time.time())
        for fileName,status in self.myTasksStatus.items():
            timeSinceDispatch = now-status["dispatchTime"]
            if timeSinceDispatch > TopperManager.reasonableTimeSinceDispatchOfTask:
                self.myLogger.warning("the file %s was dispatched %s seconds ago and still was not fully processed"%(fileName,timeSinceDispatch))


    def initDataContainers(self,lrusize):
        __pychecker__='no-argsused'
        self.initRecordData()

    def initRecordData(self):
        #this builds the hash size so that we don't have to resize and rehash every now and then
        self.myRecords = {} #dict.fromkeys(range(self.myMaxLRUToMaintain*2))
        self.myRecords.clear()#free the keys and leave us with the hashing and capacity

    def getKey (self,record):
        data = record[REC.DATA]
        key = data[self.myKeyOffset]
        return key


    #add new node, or update existing node
    def addRecordData(self,record):
        key = self.getKey(record)
        if ((key==None) or (self.myShouldIgnoreIndicator(key)==True)):
            self.myLogger.debug("%s key=='%s' on addRecordData, record was from time %s" %  (self.myTopperName,key,record[REC.TIMESTAMP].myUnixTime))
            if (key==None):
                key = ""

        rec = None
        if not key in self.myRecords: # introduce new record
            rec = self.allocateNewTopperRecord(None)
            rec.addAdditionalKeys(record,self.myAdditionalKeyOffsets)
            self.myRecords[key] = rec # add to dictionary
        else: # touch existing record - mark as used by jumping to the head of the list
            rec = self.myRecords[key]
            if rec.myData is None: # re-allocate last hour data structure
                rec.myData = TopperRecordData()
                rec.addAdditionalKeys(record,self.myAdditionalKeyOffsets)

        #update data from the raw record to the topper record
        try:
            rec.addFromRawRecord(record)
            return key,rec
        except Exception,e:
            self.logDataRecordError(record,"ADD",e)


    #called when a time slice retires from being accounted for in the last X topper
    def subtractRecordData (self,record):
        key = self.getKey(record)
        if key==None:
            self.myLogger.error("%s key=None on addRecordData" % self.myTopperName)
            return
        if key in self.myRecords: # only subtract if record exists
            rec = self.myRecords[key]
            if rec.myData.myHitCount < 1:
                self.myLogger.error("Topper %s refcount goes below 1 on %s" % (self.myTopperName,key))
            try:
                if rec.subtractFromRawRecord(record)==False:
                    self.myLogger.error("Negative metric detected on topper " + self.myTopperName + " ,key=" + key)
            except Exception,e:
                self.logDataRecordError(record,"SUBTRACT",e)
            #if item is no longer in the active hour - delete it
            if rec.myData.myHitCount==0:
                rec.myData = None
                del self.myRecords[key]
        else:
            self.myLogger.debug("Key not found for Sub: " + key)

    def deleteRecord(self,key):
        try:
            del self.myRecords[key]
        except KeyError,k:
            self.myLogger.debug("in %s-topper Key not found for removal: %s" %(self.myTopperName, str(k))) #log level is low to avoid flud

    def updateRecordsOnRemovedSlice(self,sliceCountersDict):
        for key,counters in sliceCountersDict.items():
            if (key not in self.myRecords):
                if (not counters.isCleared()):
                    self.myLogger.warning("%s was not found in the topper records for update, but indication for data on it was found"%key)
            else:
                topperRec = self.myRecords[key]
                rc = topperRec.subtractFromSliceCounter(counters)
                if rc==False:
                    self.myLogger.debug("after subtraction of %s from slice counters went below 0"%key)
                    
                if topperRec.myData.depleated():
                    self.deleteRecord(key)


    def logDataRecordError(self,record,msg,e):
        self.myLogger.error("%s exception - %s - %s" % (msg,str(e), ",".join(record[REC.DATA])))


    def writeReportsHeader(self,topReportsBase):
        headerFile = os.path.join(topReportsBase,self.myTopperName,"report_header")
        fd = a.sys.analytic.topper_record_utils.openFileForWrite(headerFile,self.myLogger)

        if (fd != None):
            global theSepToken
            line = theSepToken.join(self.myTopReportLineLegend.getReportHeader()) + "\n"
            fd.write(line)
            fd.close()

        else:
            self.myLogger.error("failed to write header file:%s, file could not be opened"% headerFile)


#------------------------------------------------------------

class TitleTopper(Topper):

    def __init__(self,logger,cfg,topperName,keyOffset,additionalKeyFieldsOffsets,everyMinuteTop,reasonableProcessingTime):

        # define the ignore indicator -> if title CID is 0 should ignore it
        super(TitleTopper,self).__init__(logger,cfg,topperName,keyOffset,additionalKeyFieldsOffsets,everyMinuteTop,reasonableProcessingTime,TitleTopper.shouldIgnoreIndicator)
        self.myTopReportLineLegend = TitleTopperReportLine()

    def allocateNewTopperRecord(self,node):
        return TitleTopperRecord(node)

    @staticmethod
    def shouldIgnoreIndicator (cid):
        __pychecker__='no-argsused'
        try:
            return int(cid,16)==0
        except Exception,e:
            return True # ignore the cid



#------------------------------------------------------------
# base class for metric records - the ones that go into and from the disk
class MetricRecord:
    myData = None
    # use this ctor only when reading topper data from disk
    # use the derived ctors when constructing from toppers
    def __init__(self,arr):
        self.myData = arr

    def addData (self,tokkens,topReportLineLegend):
        topReportLineLegend.addLineToMetricRecord(tokkens,self)

#-----------------------------------------------------------------------------------------------------------------
# total volume record
class VolumeMetricRecord(MetricRecord):
    def __init__(self,topperrecord):
        MetricRecord.__init__(self,topperrecord)
        self.myData = topperrecord.myData.myBytes.totalsArray() + topperrecord.getAdditionalFields()
    def generate(self,topperrecord):
        return VolumeMetricRecord(topperrecord)
#-----------------------------------------------------------------------------------------------------------------
# total hitcount record
class ViewsMetricRecord(MetricRecord):
    def __init__(self,topperrecord):
        MetricRecord.__init__(self,topperrecord)
        self.myData = topperrecord.myData.mySessions.totalsArray() + topperrecord.getAdditionalFields()
    def generate(self,topperrecord):
        return ViewsMetricRecord(topperrecord)
#---------------------------------------------------------------------------------------------------------
# total view duration record
class SecondsMetricRecord(MetricRecord):
    def __init__(self,topperrecord):
        MetricRecord.__init__(self,topperrecord)
        self.myData = topperrecord.myData.mySeconds.totalsArray() + topperrecord.getAdditionalFields()
    def generate(self,topperrecord):
        return SecondsMetricRecord(topperrecord)

#---------------------------------------------------------------------------------------------------------
#store intermediate values for pareto files creation from the metric data
class ParetoMetricData:
    def __init__ (self):
        self.clear()

    def clear (self):
        self.myTotalData = 0
        self.myTotalDataCachable = 0
        self.myTotalDataDelivered = 0
        self.myRecordData = []
        self.myNumOfRecords = 0
        self.myTotalContentLengths = 0 # will be used only in title volume

#---------------------------------------------------------------------------------------------------------
# manage aggeregation of last and historic top records
class TopperMetric:

    def __init__ (self,factory,timetype,metricType,reportType,topcount,shouldIgnoreIndicator,topReportLineLegend,logger):
        self.myRecords = {}
        self.myTimeType = timetype # last / hourly / daily / weekly /monthly
        self.myReportType = reportType# volume / views / duration
        self.myMetricType = metricType# sites / titles / subscribers
        self.myRecordFactory = factory
        self.myTopCount = topcount
        self.myLogger = logger
        self.myParetoData = ParetoMetricData()
        self.isCreatingPareto = True
        self.isTitleVolumeMetric = False # we need to know that down deep the SavePareto function
        self.myShouldIgnoreIndicator = shouldIgnoreIndicator
        self.myTopReportLineLegend = topReportLineLegend
        

    #this is meant to generate an data-less metric based on existing metric - only copy the path specifiers
    def cloneWithEmptyData (self):
        metric = TopperMetric(MetricRecord(None),self.myTimeType,self.myMetricType ,self.myReportType ,self.myTopCount,self.myShouldIgnoreIndicator,self.myTopReportLineLegend,self.myLogger)
        return metric

    #from last hour RAW data
    def insertRecords(self,records):

        for key,rec in records:

            if (self.myShouldIgnoreIndicator(key)==True):
                continue

            metricRecord = self.myRecordFactory.generate(rec)
            if (metricRecord.myData[0] > 0): # add this record to calculations only if it holds data>0
                self.myRecords[key] = metricRecord
            
                # update totals
                self.myParetoData.myTotalData += metricRecord.myData[0]
                self.myParetoData.myTotalDataCachable += metricRecord.myData[1]
                self.myParetoData.myTotalDataDelivered += metricRecord.myData[2]


    # for summing up together several metric files of the same type
    def addFromFile (self,filename): # use full path of a single file
        fd = a.sys.analytic.topper_record_utils.openFileForRead(filename,self.myLogger)

        if fd != None:
            for line in fd:
                tokens = line.strip().split(theSepToken)
                if len(tokens) > 2:
                    key = tokens[0]
                    if key == "TOTAL": # the TOTAL line
                        self.myParetoData.myTotalData += int(tokens[2])
                        self.myParetoData.myTotalDataCachable += int(tokens[3])
                        self.myParetoData.myTotalDataDelivered += int(tokens[4])

                    else:
                        rec = None
                        if key not in self.myRecords:
                            rec = self.myTopReportLineLegend.createDefaultMetricRecord()
                            self.myRecords[key] = rec
                        else:
                            rec = self.myRecords[key]

                        rec.addData(tokens,self.myTopReportLineLegend)
            fd.close()

        else:
            self.myLogger.error("Metric add from file: Failed opening %s" % filename)
        


    # path where to save this metric report
    def getSavePath (self,basefolder):
        return os.sep.join([basefolder , self.myReportType , self.myTimeType , self.myMetricType])


    def savePareto(self,origFileName):
        name = origFileName + ".pareto"
        if self.isCreatingPareto == False:
            return
        lineCount = len(self.myParetoData.myRecordData)
        if  lineCount < 2: 
            if os.path.exists(name):#delete previous file if existed
                os.unlink(name)
            return
        #open the file for write, so that if we fail on the next 2 - previous file is purged
        fd = a.sys.analytic.topper_record_utils.openFileForWrite(name + "_",self.myLogger)
        if fd==None:
            if os.path.exists(name):#delete previous file if existed
                os.unlink(name)
            return
        total = self.myParetoData.myTotalData
        if total==0:
            return # no point creating the file if it is all zero
        totalContentLen=self.myParetoData.myTotalContentLengths
        if totalContentLen==0:
            totalContentLen=1
            #return 0 # should not occur, still
        
        jump = lineCount / 100 # number of lines in 1% from total
        if jump==0:
            jump=1
        #percentile = lineCount / jump # number of percentiles - should be 100 if lineCount >= 100
    
        #isTitleVolumeMetric = self.isTitleVolumeMetric     
        line=""
        recordCount = 0
        #percentileCount = 0
        cummData = 0
        #per percentile
        lastPercentileData = 0
        currPercentile = 1
        localCount=0
        cummContentLen=0
        percentContentLenCumm=0.0
        for record in self.myParetoData.myRecordData:
            data=record[1].myData
            if recordCount > 0 and (recordCount % jump)==0 and currPercentile < 100:
                #percentile, data value, data / total, cumulative value, cumulative value / total, amount of items in data, cumulative amount of items
                percentLocal = float(lastPercentileData)/float(total)
                percentCumm = float(cummData)/float(total)
                percentContentLenCumm=float(cummContentLen)/float(totalContentLen)
                line="\t".join(map(str,[currPercentile,lastPercentileData,percentLocal,cummData,percentCumm ,jump,recordCount,cummContentLen,percentContentLenCumm,"\n"]))
                fd.write(line)
                lastPercentileData = 0
                currPercentile += 1
                localCount=0
            lastPercentileData += data[0]
            cummData += data[0]
            recordCount += 1
            localCount+=1
            #if isTitleVolumeMetric:
            #    clen = long(data[-1]) # in title topper last additional field is content length
            #    cummContentLen += clen
        # remainder
        if lastPercentileData > 0:
            percentContentLenCumm=float(cummContentLen)/float(totalContentLen)
            line="\t".join(map(str,[currPercentile,lastPercentileData,lastPercentileData/total,cummData,cummData/total,localCount,recordCount,cummContentLen,percentContentLenCumm,"\n"]))
            fd.write(line)
        fd.close()
        rename(name + "_",name,self.myLogger)


    def debugDuplicate(self,basefolder,basename,suffix,timestamp):
        folder = self.getSavePath(basefolder)
        src = os.sep.join([folder , basename + suffix])
        dest = os.sep.join([folder , "%s.%s%s" % (basename , str(timestamp.myUnixTime) , suffix)])
        copyFile(src,dest,self.myLogger)


    def saveToFile (self,basefolder,name):
        folder = self.getSavePath(basefolder)
        makeDirsIfNeeded(folder)
        # sort according to value
        final =  folder + os.sep + name
        fd = a.sys.analytic.topper_record_utils.openFileForWrite( final + "_",self.myLogger)
        recordCount = 0
        #isTitleVolumeMetric = self.isTitleVolumeMetric
        #contentLen=0
        if fd!=None:
            rank = 1 # generate a new rank based on the current value
            #sort the list and save a reference for a later pareto
            self.myParetoData.myRecordData = sorted(self.myRecords.iteritems(),key=lambda rec: rec[1].myData[0],reverse=True)# sort by total values

            for record in self.myParetoData.myRecordData:
                suffix=""
                data=record[1].myData
                #if isTitleVolumeMetric:
                #    cl=long(data[-1]) # in title topper last additional field is content length
                #    self.myParetoData.myTotalContentLengths += cl# the part of the title key before the '-' is the content length
                # we only write the 'self.myTopCount' records, but sum values from all of them
                # so we do not want to waste ammo on creating the unneeded lines
                recordId = record[0]
                if (self.myShouldIgnoreIndicator(recordId)==True): # if the id is to be ignored skip this iteration
                    continue

                if recordCount < self.myTopCount:
                    line = theSepToken.join([recordId,str(rank)]+ map(str,data))
                    if line[-1]!="\n":
                        suffix="\n"
                    fd.write(line + suffix)
                rank += 1
                recordCount += 1

            # add the last line which is the total values
            line = theSepToken.join(["TOTAL" #id\
                                     ,"0"# rank\
                                     ,str(self.myParetoData.myTotalData)# total\
                                     ,str(self.myParetoData.myTotalDataCachable)# cachable\
                                     ,str(self.myParetoData.myTotalDataDelivered)])# delivered\

            line += '\n'
            fd.write(line)
            fd.close()
            rename(final + "_",final,self.myLogger)
        #update the rest of the pareto data
        self.myParetoData.myNumOfRecords = recordCount
        return final
            
class TopperReportLineElement:

    def __init__(self,indexInLine,indexInMetricRecord,defaultVal,aggFunction,fieldName):

        self.myLineIndex   = indexInLine
        self.myMRIndex     = indexInMetricRecord
        self.myDefaultVal  = defaultVal
        self.myAggFunction = aggFunction
        self.myFieldName   = fieldName


class TopperReportLine:

    def __init__(self):
        #doNothing = lambda x,y : x
        add = lambda metricRecElem,lineElem :metricRecElem+int(lineElem)
        self.myLineElements = []
        #self.myLineElements.append(TopperReportLineElement(0,"defaultCid",doNothing))
        #self.myLineElements.append(TopperReportLineElement(1,"rank",doNothing))
        self.myLineElements.append(TopperReportLineElement(2,0,0,add,"total")) # total
        self.myLineElements.append(TopperReportLineElement(3,1,0,add,"cachable")) # cachable
        self.myLineElements.append(TopperReportLineElement(4,2,0,add,"delivered")) # delivered


    def padLineArrayWithDefaults(self,lineArr):
        lineLen = len(lineArr)
        diff = self.myLineElements[-1].myLineIndex - (lineLen-1) # diff between line array and topper metric record

        i=0
        while (diff>0):
            defaultVal = self.myLineElements[lineLen+i].myDefaultVal
            lineArr.append(defaultVal)
            i += 1
            diff -= 1

    def addLineToMetricRecord(self,lineArr,metricRecord):
        lineLen = len(lineArr)

        for lineElem in self.myLineElements:
            if lineLen<=lineElem.myLineIndex: #update only if the linelen allows it
                break
            metricVal = metricRecord.myData[lineElem.myMRIndex]
            lineVal   = lineArr[lineElem.myLineIndex]
            newVal = lineElem.myAggFunction(metricVal,lineVal)
            metricRecord.myData[lineElem.myMRIndex] = newVal
            

    def createDefaultMetricRecord(self):
        data = []
        for lineElem in self.myLineElements:
            data.append(lineElem.myDefaultVal)

        return MetricRecord(data)


    def getReportHeader(self):
        headerArr = ["id","rank"] # intialize with non functional elements

        for lineElem in self.myLineElements:
            headerArr.append(str(lineElem.myFieldName))

        return headerArr


class TitleTopperReportLine(TopperReportLine):
    
    def __init__(self):
        TopperReportLine.__init__(self)

        unknown = "unknown"
        replaceOnlyUnknown = (lambda metricRecElem,lineElem: metricRecElem==unknown and lineElem or metricRecElem)
        add = lambda metricRecElem,lineElem :metricRecElem+int(lineElem)

        self.myLineElements.append(TopperReportLineElement(5,3,unknown,replaceOnlyUnknown,"siteId"))
        self.myLineElements.append(TopperReportLineElement(6,4,unknown,replaceOnlyUnknown,"pathFirstChar"))
        self.myLineElements.append(TopperReportLineElement(7,5,unknown,replaceOnlyUnknown,"contentLength"))
        self.myLineElements.append(TopperReportLineElement(8,6,0,add,"totalBytes"))
        self.myLineElements.append(TopperReportLineElement(9,7,0,add,"totalViewTime"))
        self.myLineElements.append(TopperReportLineElement(10,8,0,add,"totalSessions"))


# this class arranges the bw subtotals in memory
# currently no flushing out is implemented,
class BWSubtotals:
    

    def __init__(self):
        # track filenames that will later need to be created or updated
        self.myDaysToUpdate = (set(),set(),set())
        self.myMonthsToUpdate = (set(),set(),set())
        self.myYearsToUpdate = (set(),set(),set())
        # save subtotals to be used later by the affectecd files
        self.mySubTotals = ({},{},{})
        


    #remember subtotals upon hour update. use them to update higher level aggregetions
    def rememberAffectedAggeregators(self,t,hourSum,reportRoot,metric):
        metricIndex=metric[4]
        yfilename = os.sep.join([reportRoot,"day",metric[0],t.getYearlyFilename()])
        self.myYearsToUpdate[metricIndex].add((yfilename,t))
        hfilename = os.sep.join([reportRoot,"hour",metric[0],t.getMonthlyFilename()])
        self.myMonthsToUpdate[metricIndex].add((hfilename,t))
        mfilename = os.sep.join([reportRoot,"minute",metric[0],t.getDaylyFilename()])
        self.myDaysToUpdate[metricIndex].add((mfilename,t))
        key=t.getHourLineTimeStamp()
        self.rememberSubtotal(metric,key,hourSum)

    def rememberSubtotal (self,metric,key,sum):
        metricIndex=metric[4]
        self.mySubTotals[metricIndex][key] = sum
        #verbose("remember %s on %s" % (key,metric[0]))
        


#------------------------------------------------------------
# this class is only meant to improve readability and reduce num of params passed to the file update "template" function
class BWUpdateSpec:
    myMakeHeadTimeFunc = None
    myNumOfSecondsToSkip = None
    myTimeCompareGranularity = None
    myTimeKeyFunction = None
    myNumOfCharsToChopForNextLevelKey = None

    theDay = None
    theMonth = None
    theYear = None

    def __init__(self,m,s,g,k,c):
        self.myMakeHeadTimeFunc = m
        self.myNumOfSecondsToSkip = s
        self.myTimeCompareGranularity = g
        self.myTimeKeyFunction = k
        self.myNumOfCharsToChopForNextLevelKey = c

#------------------------------------------------------------
#this class organizes the stat counters for the toppermanager
class StatCounters:

    def __init__ (self,filename,logger,statsCommObj):
        self.myModule = a.sys.analytic.simple_stats_logger.StatModule(filename, statsCommObj, logger)
        self.myNumOfRecordsDropped = self.myModule.createStatCounter("droppedRecords")
        self.myLastHourListSize = self.myModule.createStatCounter("lastHourActiveTitles")

        #resource consumption
        self.myRuMaxRSS = self.myModule.createStatCounter("RuMaxRSS")
        self.myRuIXRSS = self.myModule.createStatCounter("RuIXRSS")
        self.myRuIDRSS = self.myModule.createStatCounter("RuIDRSS")
        self.myRuNSWAP = self.myModule.createStatCounter("RuNSWAP")
        self.myRuUTIME = self.myModule.createStatCounter("RuUTIME")
        self.myRuSTIME = self.myModule.createStatCounter("RuSTIME")


        self.myFlowReportsReceived = self.myModule.createStatCounter("flowReportsReceived")
        self.myRecordsOutOfSlice = self.myModule.createStatCounter("rawRecordsOutOfSlice")
        self.myFlowRecordsOutOfSlice = self.myModule.createStatCounter("flowRecordsOutOfSlice")

        self.myNewSlicesCreated = self.myModule.createStatCounter("numOfSlicesCreated")
        self.myNumOfPeriodicWrites = self.myModule.createStatCounter("numOfPeriodicWrites")

        
        # time transition
        self.myTopRoundHourCount = self.myModule.createStatCounter("topperRoundHourCounter")
        self.myBWRoundHourCount = self.myModule.createStatCounter("bwRoundHourCounter")

        #profiling
        self.mygetReadersTime = self.myModule.createStatCounter("profGetReadersTime")
        self.myWriteBWTime = self.myModule.createStatCounter("profWriteBWTime")
        self.mySaveSnapshotTime = self.myModule.createStatCounter("profSaveSnapshotTime")
        self.myCreateMetricsTime = self.myModule.createStatCounter("profCreateMetricsTime")
        self.myPassMetricsToWorkersTime = self.myModule.createStatCounter("profPassMetricsToWorkersTime")
        
        self.myTitleHitGapAvg = self.myModule.createAvgStatCounter("titleHitGapAvg")
        self.myFlowBytesAvg = self.myModule.createAvgStatCounter("flowByteSizeAvg")
        self.myFlowDurationAvg = self.myModule.createAvgStatCounter("flowDurationAvg")




class DeltaProfiler:
    def __init__ (self):
        self.myLastTime = time.time()
    
    def profileDeltaTime(self):
        tmp = self.myLastTime 
        self.myLastTime = time.time()
        return self.myLastTime  - tmp

#------------------------------------------------------------

class BWFutureStack:

    def __init__(self,updateFunc):
        self.myStackElements = []
        self.myBWRecordUpdateFunc = updateFunc
        self.myLastTimeUsed = -1

    def push(self,timeElem):
        self.myStackElements.append(timeElem)

    def nMinutesUpdate(self,slice,numOfMinutes=1):
        numOfElements = len(self.myStackElements)
        sum = 0

        # must iterate over reversed indices and not elements, for correct efficiant popping
        for i in reversed(range(numOfElements)):
            sum += self.myStackElements[i].decreaseXMinuteTime(numOfMinutes)
            if self.myStackElements[i].isDone():
                self.myStackElements.pop(i)

        # now lets update the BWrecord
        if sum>0:
            self.myBWRecordUpdateFunc(slice.myBWRecord.mySeconds,sum,0) #update port0 only as port1 is irelevant (only the total is considered)

        #update the time the stack was last used
        self.myLastTimeUsed = slice.myRepresentingTimeSlice.clone()

#------------------------------------------------------------

class FutureBWElement:

    kMilisecondsPerSlice = 60000
    
    def __init__(self,milliSeconds):
        self.myMSeconds = milliSeconds


    def decreaseXMinuteTime (self,numOfMinutes):
        msecondsToSubtract = min(self.myMSeconds,FutureBWElement.kMilisecondsPerSlice*numOfMinutes)
        self.myMSeconds -= msecondsToSubtract
        return msecondsToSubtract

    def isDone(self):
        return self.myMSeconds == 0


#------------------------------------------------------------
#------------------------------------------------------------

#class TopperFutureStack:
#
#    def __init__(self):
#        self.myTopperPacks = []
#        self.myLastTimeUsed = -1
#
#    def push(self,topperPack):
#        self.myTopperPacks.append(topperPack)
#
#    def nMinutesUpdate(self,slice,numOfMinutes=1):
#        numOfElements = len(self.myTopperPacks)
#        
#        # must iterate over reversed indices and not elements, for correct efficiant popping
#        for i in reversed(range(numOfElements)):
#            hasMoreFuture = self.myTopperPacks[i].inWindowUpdate(numOfMinutes)
#            if not hasMoreFuture:
#                self.myTopperPacks.pop(i)
#
#        #update the time the stack was last used
#        self.myLastTimeUsed = slice.myRepresentingTimeSlice.clone()

#------------------------------------------------------------

# This class represent a data section of an f-record
class DataSection:

    def __init__(self,oneMinuteDelta,allData,isCachable,isDelivered,initiatorPort,updatedDataGetter,topperRecords):
        self.myOneMinuteDelta    = oneMinuteDelta # how much to decrese/add each minute
        self.myAllData           = allData        # how long will this element sty alive after the first minute it starts exiting the hour-window
        self.myIsCachable        = isCachable
        self.myisDelivered       = isDelivered
        self.myInitiatorPort     = int(initiatorPort)
        self.myUpdatedDataGetter = updatedDataGetter
        self.myTopperRecords     = topperRecords
      
        
    def outOfWindow(self):
        return (self.myAllData <= 0)

    # should return true if it is not exausted yet (myAllData is depleted)
    def endOfWindowUpdate(self,numOfMinutes=1):
        if not self.outOfWindow():
            dataToSuck = min(self.myOneMinuteDelta*numOfMinutes,self.myAllData)
            self.myAllData -= dataToSuck

            portsPair = None
            if (self.myInitiatorPort == 0):
                portsPair = (dataToSuck,0)
            else:
                portsPair = (0,dataToSuck)

            for topperRecord in self.myTopperRecords:
                self.myUpdatedDataGetter(topperRecord).subtractData(*portsPair)
                if self.myIsCachable:
                    self.myUpdatedDataGetter(topperRecord).subtractServable(*portsPair)
                if self.myisDelivered:
                    self.myUpdatedDataGetter(topperRecord).subtractDelivered(*portsPair)

        return not self.outOfWindow()

            
        

#------------------------------------------------------------

class ViewTimeDataSection(DataSection):

    def __init__(self,futureData,oneMinuteDelta,allData,isCachable,isDelivered,initiatorPort,updatedDataGetter,topperRecords):
        DataSection.__init__(self,oneMinuteDelta,allData,isCachable,isDelivered,initiatorPort,updatedDataGetter,topperRecords)
        self.myFutureData = futureData

    def hasMoreFuture(self):
        return (self.myFutureData > 0)

    def inWindowUpdate(self,numOfMinutes=1):
        if self.hasMoreFuture():
            mSecondsToPump = min(self.myOneMinuteDelta*numOfMinutes,self.myFutureData)
            self.myFutureData -= mSecondsToPump # take from the pump and feed the topper record
            
            portsPair = None
            if (self.myInitiatorPort == 0):
                portsPair = (mSecondsToPump,0)
            else:
                portsPair = (0,mSecondsToPump)

            for topperRecord in self.myTopperRecords:
                self.myUpdatedDataGetter(topperRecord).addData(*portsPair)
                if self.myIsCachable:
                    self.myUpdatedDataGetter(topperRecord).addServable(*portsPair)
                if self.myisDelivered:
                    self.myUpdatedDataGetter(topperRecord).addDelivered(*portsPair)
                


    

#------------------------------------------------------------

class TopperPack:

    def __init__(self,topperKeys,topperRecords,RawFRecord):

        isCachable    = RawFRecord[REC.DATA][FlowRecordOffsets.theIsCachableIndicator.myVal] == "1"
        isDelivered   = RawFRecord[REC.DATA][FlowRecordOffsets.theIsDeliveredIndicator.myVal] == "1"
        initiatorPort = RawFRecord[REC.DATA][FlowRecordOffsets.theInitiatorPortNumber.myVal]
        
        downloadTime  = RawFRecord[REC.DATA][FlowRecordOffsets.theDownloadTimeMsec.myVal]
        viewTime      = RawFRecord[REC.DATA][FlowRecordOffsets.theViewTimeMsec.myVal]
        sessions      = RawFRecord[REC.DATA][FlowRecordOffsets.theSessionHitCount.myVal]
        p0Bytes       = RawFRecord[REC.DATA][FlowRecordOffsets.theDownloadedContentBytesPort0Offset.myVal]
        p1Bytes       = RawFRecord[REC.DATA][FlowRecordOffsets.theDownloadedContentBytesPort1Offset.myVal]
        bytes = p0Bytes + p1Bytes
        numOfMinutestoSmear = 1 # since pre topper, there is no more smaering of data
        bytesPerMinuteDelta = bytes

        # create viewTimeDataSection
        futureViewTime = max(viewTime-downloadTime,0)
        viewTimeDataSection = ViewTimeDataSection(futureViewTime,downloadTime,viewTime,isCachable,isDelivered,initiatorPort,TopperPack.secondsGetter,topperRecords)
        volumeDataSection   = DataSection(bytesPerMinuteDelta,bytes,isCachable,isDelivered,initiatorPort,TopperPack.bytesGetter,topperRecords)
        sesionsDataSection  = DataSection(sessions,sessions,isCachable,isDelivered,initiatorPort,TopperPack.sessionsGetter,topperRecords)
        
        self.myTopperKeys          = topperKeys
        self.myTopperRecords       = topperRecords
        self.myDataSections        = [viewTimeDataSection,sesionsDataSection,volumeDataSection]
        self.myViewTimeDataSection = viewTimeDataSection
        self.myNumOfMinutesToSmear = numOfMinutestoSmear

    @staticmethod
    def secondsGetter (record):
        return record.myData.mySeconds

    @staticmethod
    def bytesGetter (record):
        return record.myData.myBytes

    @staticmethod
    def sessionsGetter (record):
        return record.myData.mySessions


    def hangOffsetFromCurrentSlice (self):
        return self.myNumOfMinutesToSmear-1

   # def __init__(self,topperRecords,dataSections):
   #     self.myTopperRecords       = topperRecords
   #     self.myDataSections        = dataSections
   #     self.myViewTimeDataSection = dataSections[0]
   #
    def hasMoreFuture(self):
        return self.myViewTimeDataSection.hasMoreFuture()

    def inWindowUpdate (self,numOfMinutes=1):
        self.myViewTimeDataSection.inWindowUpdate(numOfMinutes)
        return self.myViewTimeDataSection.hasMoreFuture()

    def endOfWindowUpdate(self,numOfMinutes=1):
        stillActiveCnt = 0
        for dataSection in self.myDataSections:
            stillActiveCnt += dataSection.endOfWindowUpdate(numOfMinutes)
        
        return (stillActiveCnt > 0)

    def killTopperRecordsIfNeeded (self,toppers):
        for i in range(3):
            topperRec = self.myTopperRecords[i]
            if topperRec.myData.depleated(): # this topperRecord is exausted - delete topperRecord
                toppers[i].deleteRecord(self.myTopperKeys[i])
#------------------------------------------------------------

class RecentTitle:

    seperator = "\t"

    def __init__(self,record):
        recordData      = record[REC.DATA]
        self.timestamp  = int(record[REC.TIMESTAMP].myUnixTime)
        self.cid        = recordData[FlowRecordOffsets.theCidOffset.myVal]
        self.site       = recordData[FlowRecordOffsets.theHostOffset.myVal]
        self.contentLength   = recordData[FlowRecordOffsets.theContentLengthOffset.myVal]
        self.isCachable      = recordData[FlowRecordOffsets.theIsCachableIndicator.myVal]
        self.isDelivered     = recordData[FlowRecordOffsets.theIsDeliveredIndicator.myVal]
        self.subscriberIp    = recordData[FlowRecordOffsets.theSrcIpOffset.myVal]
        self.downloadedBytes = int(recordData[FlowRecordOffsets.theDownloadedContentBytesPort0Offset.myVal]) + int(recordData[FlowRecordOffsets.theDownloadedContentBytesPort1Offset.myVal])

        # if this is an aggregated record - divide the bytes to the sessions
        sessionCounter = int(recordData[FlowRecordOffsets.theSessionHitCount.myVal])
        if sessionCounter>1:
            self.downloadedBytes = self.downloadedBytes / sessionCounter
        

    def toString(self):
        return RecentTitle.seperator.join([str(self.timestamp),self.cid,self.site,self.contentLength,str(self.downloadedBytes),self.isCachable,self.isDelivered,self.subscriberIp])

#------------------------------------------------------------

class RecentTitlesStack:
    
    def __init__(self,writeSize,file,updateFrequency,toppers,logger):
        self.myRecentTitles = {}
        self.myWriteSize = writeSize
        self.myMaxSize = writeSize + 2*60/updateFrequency #enough for 2 minutes of updates without reading new files
        self.myUpdateFrequency = updateFrequency
        self.myLastWriteTime = -1*updateFrequency
        self.myFile = file
        self.myToppers = toppers
        self.myLogger = logger

    def push(self,record):
        # we need t check that the cid,host,client are valid ones for display in recent titles
        for topper in self.myToppers:
            if topper.myShouldIgnoreIndicator(topper.getKey(record)) == True:
                return
        # create a new RecentTitle Object and insert it to stack
        recentTitleObj = RecentTitle(record)

        # if this is a zero bytes record, skip it
        if (recentTitleObj.downloadedBytes==0):
            return

        self.myRecentTitles[recentTitleObj.cid] = recentTitleObj
        if (len(self.myRecentTitles) > self.myMaxSize):
            self.removeMin()
        

    def removeMin (self):
        sortedItems = sorted(self.myRecentTitles.items(),key=lambda recentTitle: recentTitle[1].timestamp,reverse=True)
        del self.myRecentTitles[sortedItems[-1][0]]

    def periodicWrite(self):
        if (len(self.myRecentTitles) >= self.myWriteSize):
            now = int(time.time())
            if ((now - self.myLastWriteTime) > self.myUpdateFrequency):
                fd = a.sys.analytic.topper_record_utils.openFileForWrite(self.myFile+'_',self.myLogger)
                if (fd != None):
                    sortedItems = sorted(self.myRecentTitles.items(),key=lambda recentTitle:recentTitle[1].timestamp,reverse=True)

                    # write the last 'writeSize' recent titles (the oldest of the stack)
                    for recentTitle in sortedItems[((-1)*self.myWriteSize):]:
                        fd.write(recentTitle[1].toString()+"\n")

                    # we need to clear the oldest title
                    oldestItem = sortedItems.pop()
                    del self.myRecentTitles[oldestItem[0]]

                    fd.close()
                    rename(self.myFile+'_',self.myFile,self.myLogger)
                    self.myLastWriteTime = now
                    

#------------------------------------------------------------

class Peaker:

    def __init__(self,reportsDir,logger):
        self.myPeakReportsDir = reportsDir
        self.myLogger = logger


    def calcGrade(self,rawRecordsSlice):
        # For now calc by total L2, in the future maybe by configuration
        return rawRecordsSlice.myBWRecord.myL2Bytes.getTotalsSum()

    def findPeakSlice(self,rawRecordSlices):
        maxGrade = -sys.maxint
        maxSlice = None

        for slice in rawRecordSlices :
            curGrade = self.calcGrade(slice)
            if curGrade > maxGrade:
                maxGrade = curGrade
                maxSlice = slice

        return maxSlice,maxGrade


    def writePeak(self,rawRecordSlices):
        maxSlice,maxGrade = self.findPeakSlice(rawRecordSlices)
        if maxSlice != None:
            
            # create file name of report
            fileName = os.path.join(self.myPeakReportsDir,maxSlice.myRepresentingTimeSlice.getMonthlyFilename())

            # create record time string
            curTime = maxSlice.myRepresentingTimeSlice.myUnixTime
            t = time.gmtime(curTime)
            recordTime = "%04d-%02d-%02d-%02d:00" % (t.tm_year , t.tm_mon , t.tm_mday , t.tm_hour)

            # create values
            delim = ['|']
            bwRec = maxSlice.myBWRecord
            recordValues = [recordTime,curTime,maxGrade] + delim + bwRec.exportSessionData() + delim + bwRec.exportSecondsData() + delim + bwRec.exportVideoBytesData()
            
            
            # append the file with last hour info
            tempFileName = fileName+'_'
            fd_ = a.sys.analytic.topper_record_utils.openFileForWrite(tempFileName,self.myLogger)
            if fd_ == None:
                self.myLogger.error("periodic write of peak in file %s failed - failed opening file %s!"%(fileName,tempFileName))
                return
    
            if (os.path.exists(fileName)):
                fd = a.sys.analytic.topper_record_utils.openFileForRead(fileName,self.myLogger)
                if (fd != None):
                    for line in fd.readlines():
                        arr = line.split(theSepToken)
                        if arr[0] != recordTime: # write this record only if it wasn't writen before.
                            fd_.write(line)
                        else:
                            # this line was already writen - abort nicely
                            self.myLogger.warning("periodic write of peak in file %s failed - attempted to write an already present record from %s!"%(fileName,recordTime))
                            fd.close()
                            fd_.close()
                            removeFile(tempFileName,self.myLogger)
                            return
    
                    fd.close()
                else:
                    self.myLogger.error("periodic write of peak in file %s failed - failed opening file %s!"%(fileName,fileName))
                    fd_.close()
                    removeFile(tempFileName,self.myLogger)
                    return
    
            line = theSepToken.join(map(str,recordValues))+'\n'
            fd_.write(line)
            fd_.close()

            rename(tempFileName,fileName,self.myLogger)

        # operate every roundhour+x minutes

#------------------------------------------------------------

class TopperManager:
    myCfg = None
    myOutputFolder = None
    myLogger = None
    myInputScanRoot = None
    myTopReportRoot = None
    myBWReportRoot = None
    myBitrateReportRoot = None
    myIsSendingFilesToArcive = False
    theBWMetrics = [("volume",BWRecord.exportVideoBytesData,BWRecord.addBytesFromStringArray,BWRecord.addBytesFromOther,0), \
                    ("sessions",BWRecord.exportSessionData,BWRecord.addSessionsFromStringArray,BWRecord.addSessionsFromOther,1), \
                    ("time",BWRecord.exportSecondsData,BWRecord.addSecondsFromStringArray,BWRecord.addSecondsFromOther,2)]
    myDataSubfolder = a.sys.analytic.topper_record_utils.DATA_SUB_FOLDER_AND_HEADER_NAME # this is also the header spec file name
    myDataSuffix = ".adata"
    mySnapshotFilename = "rawDataSnapshot.txt"
    
    theNumberOfHoursTail = 1 # additional slices, to update servable bw retroactively
    theRawDataInMemoryPeriod = 61 # last hour for topper data
    theMaxNumOfSlices = (60 * (theNumberOfHoursTail + 1))+1
    theInterCycleWaitTime = 1

    isRecordHeaderInit = False
    myCurrSliceIterator = 0
    reasonableTimeSinceDispatchOfTask = 3600
    

    def __init__(self,cfg,versionNum):
        self.mygetReadersTime = DeltaProfiler()
        self.myWriteBWTime = DeltaProfiler()
        self.mySaveSnapshotTime = DeltaProfiler()
        self.myCreateMetricsTime = DeltaProfiler()
        self.myPassMetricsToWorkersTime = DeltaProfiler()

        self.myCfg = cfg

        self.systemTimeStamp = cfg.get('systemStartTimeStamp','')

        self.myTimeGuardEnable = self.cfgGetTypedValue(bool,'timeGuardEnable',False)
        self.myTimeGuardToleranceInterval = self.cfgGetTypedValue(int,'timeGuardToleranceInterval', 3600)
        self.myTimeGuardCurrentTime = None

        self.doMinuteSkip=cfg.get('doMinuteSkip')
        
        self.myCfgErrorKeys = set() # maintain a report-once mechanism for error reporting
        self.myRawDataTimeSlices = []
        #shared memory between processes designating timestamps of slices 0 and 1
        self.myPickledTopEnum=0

        self.myToppers = []
        self.myMetricsDoneMutex=mp.Lock()
        self.myOutputFolder = cfg.get('destFolder',None)
        self.myTopReportRoot = os.sep.join([self.myOutputFolder,"reports","top"])
        self.myBWReportRoot = os.sep.join([self.myOutputFolder,"reports","bw"])
        self.myBitrateReportRoot = os.sep.join([self.myOutputFolder,"reports",bitrate_report.BITRATE_REPORT_DIR_NAME])
        self.myInputScanRoot = cfg.get('srcFolder',None)
        self.myIsSendingFilesToArcive = True
        self.initCaptain(kickNumber = int(cfg.get('kickNumber',0)))
        logLevel = cfg.get('logLevel',None)
        if not logLevel is None:
            logLevel = a.infra.log.logger.LevelTranslate.s_getPyLevelFromCpp(logLevel)
        self.initLogger(dirname = cfg.get('logDirName',None),
                        logLevel = logLevel, 
                        logFileSize = int(cfg.get('logFileSize',0)), 
                        logTotalSize= int(cfg.get('logTotalSize',0)),
                        logConfigFile = cfg.get('logConfigFile',None),
                        logConfigPeriod = int(cfg.get('logConfigPeriod',0))
                        )        
        self.myLastPeriodicWriteTime = TopperTime(0)
        self.enablePeriodicWrites=True
        self.isUsingShrinkingTime=self.cfgGetTypedValue(bool,'useShringkingTime',False)
        self.isArchivingV3RawData=self.cfgGetTypedValue(bool,'archiveV3RawData',True)
        self.writePeriodicSnapshots=self.cfgGetTypedValue(bool,'writePeriodicSnapshots',False)
        self.shouldSkipMinutesWhenLaggingBehind=self.cfgGetTypedValue(bool,'shouldSkipMinutesWhenLaggingBehind',True)
        self.useMultiprocess=self.cfgGetTypedValue(bool,'useMultiprocess',True)
        self.makeLastDebugCopies=self.cfgGetTypedValue(bool,'makeLastDebugCopies',True)
        self.selfModifyHost=self.cfgGetTypedValue(bool,'selfModifyHost',False)
        

        # Stats
        self.statsCommunicationDir = cfg.get('statsCommunicationDir',None)

        self.isBasketRecordsReadingOnHold = self.cfgGetTypedValue(bool,'isBasketRecordsReadingOnHold ',False)# pause in report reading
        self.myConditionalPauseQuota = 0 # the number of minutes after which, topper will enter pause
        
        TOP.BYTES = TOP.DURATION = TOP.HITCOUNT = self.cfgGetTypedValue(int,"top",1000)  #int(cfg.get('top',1000))
        if TOP.BYTES==None or TOP.BYTES==0:
            self.myLogger.error("top returned none from cfg. setting back to default")
            TOP.BYTES = TOP.DURATION = TOP.HITCOUNT = 1000
        self.myReportPort0 = self.cfgGetTypedValue(bool,'reportPort0',False)  #cfg.get('reportPort0',False)
        self.myReportPort1 = self.cfgGetTypedValue(bool,'reportPort1',False) #cfg.get('reportPort1',False)
        self.myReportTotalPorts = self.cfgGetTypedValue(bool,'reportTotalPorts',True) #cfg.get('reportTotalPorts',True)
        self.takeNewFilesSnapshot = self.cfgGetTypedValue(bool,'snapNewFiles',False)  
        self.takeRawRecordsSnapshot = self.cfgGetTypedValue(bool,'snapRawRecords',False) 
        BWUpdateSpec.theDay = BWUpdateSpec(TopperTime.cloneFromHourZero,SECONDS.HOUR , TopperTime.SLICE_DAY , TopperTime.getHourLineTimeStamp,6)
        BWUpdateSpec.theMonth = BWUpdateSpec(TopperTime.cloneFromDayOneOfTheMonth,SECONDS.HOUR , TopperTime.SLICE_MONTH , TopperTime.getHourLineTimeStamp,9)
        BWUpdateSpec.theYear = BWUpdateSpec(TopperTime.cloneFromDayOneOfTheYear ,SECONDS.DAY , TopperTime.SLICE_YEAR , TopperTime.getDayLineTimeStamp,3)
        logMsg="  *****  %s Topper %s is up. pid=%d   *****" % ( time.strftime("%d-%b %H:%M:%S",time.gmtime()) ,versionNum,os.getpid())
        self.myLogger.info(logMsg) 
        self.myCfg.dump(None,self.myLogger)# this is a hack to the cfg dump just because I'm lazyy looking at 2 logs
        self.myLogger.info("pid=%d" % os.getpid())
        sys.stderr.write(logMsg+"\n")
        self.myLogger.info("TOP set to %d",TOP.BYTES)
        #initToppers() moved till after record headers init

        #init future stacks
        self.myAllViewTimeStack = BWFutureStack(PerPortData.addData)
        self.myServableViewTimeStack = BWFutureStack(PerPortDataExtended.addServable)
        self.myDeliveredViewTimeStack = BWFutureStack(PerPortDataExtended.addDelivered)
        #self.myTopperFutureStack = TopperFutureStack()

        #init recent titles stack
        recentTitlesWriteSize = self.cfgGetTypedValue(int,'recentTitlesWriteSize',5)
        filePath = os.sep.join([self.myOutputFolder,"reports","recent","titles.tsv"])
        self.myRecentTitleStack = RecentTitlesStack(writeSize=recentTitlesWriteSize,file=filePath,updateFrequency=5,logger=self.myLogger,toppers=self.myToppers)

        #init L2Peaker
        self.myPeakDir = os.sep.join([self.myOutputFolder,"reports","bw","hour","peak"])
        self.myL2Peaker = Peaker(self.myPeakDir,self.myLogger)
        self.myRoundHourTailSize = self.cfgGetTypedValue(int,'roundHourTailSize',2)

        #some thresholds
        self.myInputRateThreshold = self.cfgGetTypedValue(int,'inputRateThreshold',130)
        self.myProcessingTimeThreshold = self.cfgGetTypedValue(int,'processingTimeThreshold',180)
        

    # purpose of this function is to wrap cfg.get() and to make sure we read proper
    # values, hence create a protection against user syntax-error in the cfg values
    def cfgGetTypedValue (self,varType,key,defaultValue,logOnSuccess=False):
        retVal = defaultValue
        msg = ""
        v = ""
        casters = {int:lambda x:int(x) ,bool:lambda x: {"true":True,"false":False}[x.lower()]}
        try:
            strValue = str(self.myCfg.get(key,defaultValue))
            if varType in casters:
                v = casters[varType](strValue)
            else:
                v = strValue
            if isinstance(v,varType): # is this the variable type we are expecting?
                if logOnSuccess:
                    self.myLogger.info("Set value of %s from config file to %s (default=%s)" % (key,strValue,str(defaultValue)))
                return v
        except Exception,e:
            msg = "Exception: %s" % str(e)
        if not key in self.myCfgErrorKeys: # report only once for each key
            self.myCfgErrorKeys.add(key)
            self.myLogger.error("Invalid cfg value %s for %s . %s" % (str(v),key,msg))

    #lauch a process per metric that will wait on its queue for incoming records
    def launchWorkerProcesses (self):
        self.mySubProcesses=[]
        for topper in self.myToppers:
            for f in [TopperManager.doVolumeMetric,TopperManager.doTimeMetrics,TopperManager.doSessionMetrics]:
                p=None
                if self.useMultiprocess==True:
                    p=mp.Process(target=f,args=[self,topper])
                else:
                    p=threading.Thread(target=f,args=[self,topper]) # for using with a debugger 
                self.mySubProcesses.append(p)
                p.start()

    def initBitrateReportModule (self):
        self.myBitrateReportDatabaseWriter = bitrate_report.TopperBitrateReportDatabaseWriter(os.path.join(self.myOutputFolder,"reports", bitrate_report.BITRATE_REPORT_DIR_NAME),self.myLogger)


    def initToppers(self):
        self.myTitleTopper = TitleTopper(self.myLogger,self.myCfg,"titles",FlowRecordOffsets.theCidOffset.myVal,[FlowRecordOffsets.theHostOffset.myVal,FlowRecordOffsets.thePathOffset.myVal,FlowRecordOffsets.theContentLengthOffset.myVal],False,self.myProcessingTimeThreshold)
        self.mySiteTopper = Topper(self.myLogger,self.myCfg,"sites",FlowRecordOffsets.theHostOffset.myVal,None,True,self.myProcessingTimeThreshold,lambda siteId: siteId in [""])
        self.mySubscriberTopper = Topper(self.myLogger,self.myCfg,"clients",FlowRecordOffsets.theSrcIpOffset.myVal,None,False,self.myProcessingTimeThreshold,lambda clientId: clientId in ["0.0.0.0"])
        self.myToppers += [self.mySiteTopper ,  self.mySubscriberTopper , self.myTitleTopper]

        # write reports header file
        #for topper in self.myToppers:
        #    topper.writeReportsHeader(self.myTopReportRoot)

        self.myTitleTopper.isWritingPareto=self.cfgGetTypedValue(bool,'writeTitlePareto',True)
        self.mySiteTopper.isWritingPareto=self.cfgGetTypedValue(bool,'writeSitePareto',False)
        self.mySubscriberTopper.isWritingPareto=self.cfgGetTypedValue(bool,'writeClientPareto',True)
        
        self.mySiteTopper.isLoggingDebug = True

        # limit each topper LRU size
        self.myTitleTopper.initDataContainers(self.cfgGetTypedValue(int,"topper_title_lru_limit",200000))
        self.mySiteTopper.initDataContainers(self.cfgGetTypedValue(int,"topper_site_lru_limit",20000))
        self.mySubscriberTopper.initDataContainers(self.cfgGetTypedValue(int,"topper_client_lru_limit",200000,))

        #init stats and introduce them to the toppers
        self.statsCommObj = StatsCommOverFileClient("topper-stats-comm-obj", self._baseLogger)
        self.statsCommObj.init(self.statsCommunicationDir)

        statsDir = self.myCfg.get('statsDir',"stats")
        self.myStatCounters = StatCounters(os.path.join(statsDir,"topper_stats.log"),self.myLogger, self.statsCommObj)
        self.myStatCounters.myModule.makeHeaderFile(os.path.join(statsDir,"topper_statsHeader.log"))
        for topper in self.myToppers:
            topper.myStatCounters = self.myStatCounters
    
    def initCaptain (self, kickNumber):
        #dummy till topper rise normaly
        self.captain = a.infra.process.captain.Captain()
        self.captain._initKickNumber(kickNumber)
        a.infra.process.setGlobalCaptain(self.captain)
                        
    def initLogger (self,dirname, logLevel, logFileSize, logTotalSize, logConfigFile, logConfigPeriod):
        self._mainLogger = MainLogger(processName = "Topper")
        self._baseLogger = self._mainLogger.getLoggerManager().createLogger("Topper", "Topper")
        self._mainLogger.initLoggerToUse(self._baseLogger)
        self._mainLogger.init(initialLogLevel=logLevel, logDir=dirname, logFileSize=logFileSize, 
                              logTotalSize=logTotalSize,
                              pearlConfigurationFilesFullName=logConfigFile, 
                              pearlConfigurationLoadPeriodInSeconds=logConfigPeriod)
        self.myLogger = self._baseLogger("topper-msg")

    def initRecordHeaders(self,folder):
       global forever
       if self.isRecordHeaderInit == False: # do it once per run
           self.isRecordHeaderInit = True
           headerFile = a.sys.analytic.topper_record_utils.getHeaderFileName(folder)
           headerDetected=False
           # there might be a race condition between topper and Line that the file might still not be there
           for i in range(0,600):
               if os.path.exists(headerFile):
                   self.myLogger.info("Header file detected after waiting %d seconds" % (i*2))
                   headerDetected=True
                   break
               if not forever:
                   return False
               time.sleep(1)
           time.sleep(2)
           if not headerDetected:
               self.myLogger.error("Timeout for waiting for header file to be created by Line/Delivery has expired.Could be Line down or slow DPDK init when links are down")
               return False
           #snapshotFile = a.sys.analytic.topper_record_utils.getHeaderFileName(self.myOutputFolder)# save the spec to the snapshot dir
           if RawDataRecordValidator.initRecordTypes(headerFile,self.myLogger)==False:
               self.myLogger.fatal("Failed processing field header file. topper is aborting")
               return False
           # chicken and egg ugly workaround
           self.mySiteTopper.myKeyOffset = FlowRecordOffsets.theHostOffset.myVal
           self.mySubscriberTopper.myKeyOffset = FlowRecordOffsets.theSrcIpOffset.myVal
           self.myTitleTopper.myKeyOffset = FlowRecordOffsets.theCidOffset.myVal
           self.myTitleTopper.myAdditionalKeyOffsets = [FlowRecordOffsets.theHostOffset.myVal , FlowRecordOffsets.thePathOffset.myVal , FlowRecordOffsets.theContentLengthOffset.myVal]
       return True
           
    def pauseRawRecordReading (self):
        self.isBasketRecordsReadingOnHold = True
        msg=" head slice=%s" % self.headTime().toString()
        if self.doMinuteSkip==True:
            msg += "Warning - Minute skip is on"
        self.myLogger.info("raw records reading PAUSED. %s" % msg)

    def resumeRawRecordReading (self):
        self.isBasketRecordsReadingOnHold = False   
        self.myLogger.info("raw records reading RESUMED." )

    def pauseRawRecordsAfterXminutes (self,numOfMinutes):
        if (numOfMinutes<=0):
            self.myLogger.error("invalid quote of minutes %d" % numOfMinutes)
            return
        self.myConditionalPauseQuota = numOfMinutes
        self.isBasketRecordsReadingOnHold = False
        
    def handlePauseQuota(self):
        if self.myConditionalPauseQuota==1:
            self.pauseRawRecordReading()
        if self.myConditionalPauseQuota > 0:
            self.myConditionalPauseQuota -= 1

    #  load the last produced raw data from all cores into memory
    def getRawReaders(self):
        global forever
        readers = []
        self.shouldSkipSomeMinutes = False
        lineCore0Folder = os.sep.join([self.myInputScanRoot , "video-analyzer","00"])
        deliveryCore0Folder = os.sep.join([self.myInputScanRoot , "delivery","00"])

        core0Folder = lineCore0Folder
        if (not os.path.exists(lineCore0Folder)):
            core0Folder = deliveryCore0Folder

        if self.initRecordHeaders (core0Folder)==False: # happens once
            forever = False # make topper bail out

        endlessLoop=0
        while forever:
            time.sleep(TopperManager.theInterCycleWaitTime)
            self.maintainDebugCommands("exec")
            if self.isBasketRecordsReadingOnHold:
                endlessLoop += 1
                continue

            endlessLoop=0
            self.mygetReadersTime.profileDeltaTime()#start measuring time
            self.myTimeGuardCurrentTime = int(self.mygetReadersTime.myLastTime) # optimize by getting time from this instead of system call
            if forever:
                scanFolder = os.path.join(self.myInputScanRoot,"aggregated")
                pattern = scanFolder + os.sep + "*" + self.myDataSuffix
                
                # Find the aggregated files
                files = glob.glob(pattern)
                if len(files) > 0:
                    if len(files) > 1: # we have more than 1 file, we need to skip some actions later
                        self.shouldSkipSomeMinutes = self.shouldSkipMinutesWhenLaggingBehind
                    file=sorted(files)[0] # take the file with the earlyest timestamp 
                    ###self.myLogger.debug("read from %s" % file)
                    reader = RawDataReader(self.myLogger)
                    recordTimeUpperBound = None
                    if self.myTimeGuardEnable:
                        recordTimeUpperBound = self.myTimeGuardCurrentTime+self.myTimeGuardToleranceInterval
                    if reader.loadFile(file,self.myInputRateThreshold, recordTimeUpperBound)==True:
                        readers.append(reader)
                    if RawDataReader.getCleanFlag()==False and self.isArchivingV3RawData==True: # don't backup clean requests
                        archiveFolderName = "archive"
                        if self.systemTimeStamp != '':
                            archiveFolderName = os.path.join(archiveFolderName, self.systemTimeStamp)
                        newFolder=os.path.join(self.myOutputFolder,archiveFolderName,"vidTransactions") # build the folder name to place it
                        makeDirsIfNeeded(newFolder)
                        archivedFile = newFolder +  os.sep  + os.path.basename(file) + ".tgz"
                        try:
                            os.system("cd %s; tar -czf %s %s" % (scanFolder,archivedFile,os.path.basename(file))) # send file to archive
                        except Exception,e:
                            self.myLogger.error("Failed compressing to  %s  - %s" % (archivedFile,str(e)))
                    removeFile(file,self.myLogger)#remove original from ramdrive after backing it up    
                    if RawDataReader.getCleanFlag(): # after removing the file
                        break
                # -------------------------------
                if len(readers)>0 or not forever:
                    break # handle one folder a time
        self.myStatCounters.mygetReadersTime.logValue(int(self.mygetReadersTime.profileDeltaTime()))
        return readers
    
    def headTime(self):
        if len(self.myRawDataTimeSlices) < 1:
            return TopperTime(0)
        return self.myRawDataTimeSlices[0].myRepresentingTimeSlice
    

# custom serialize/deserialize for performance sake
    def serializeTopperRecords(self,records,filename):
        fd=open(filename,"wb")
        for key,record in records.iteritems():
            keylen=len(key)
            fd.write(struct.pack("<H",keylen)) # record key length
            fd.write(key)
            record.serialize(fd)
        fd.flush()
        fd.close()


    def deSerializeTopperRecords(self,filename):
        d={}
        recordTypes={0xF1F1: TopperRecord , 0xF2F2:TitleTopperRecord}
        fd=open(filename,"rb")
        while True:
            rawnum=fd.read(2)
            if len(rawnum)==0:
                break
            #read key
            keylen=struct.unpack("<H",rawnum)[0]
            key=fd.read(keylen)
            #read record type
            rawnum=fd.read(2)
            recType=struct.unpack("<H",rawnum)[0]
            record = recordTypes[recType](None) # construct matching record 
            record.deSerialize(fd)
            d[key]=record
        fd.close()
        return d


# these are a set of functions seperated from the sequentioal createLastHourMetrics()
# in order to become multiprocess.
    def workerProcessLoop (self,topper,cmpFunc,metric,taskQueue,ackQueue):
        # rename workers process
        daemonUtils.setProcessName("topper_wrkr_%s"%topper.myTopperName)
        execFile="exec-%d" % os.getpid()
        while True:
            #records=queue.get()
            triplet = taskQueue.get() # triplet should be (filename,slice0time,slice1time) or ["quit",]
            taskQueue.task_done()
            if "quit" in triplet:
                break
            
            filename,slice0UnixTime,slice1UnixTime = triplet
            #if TopperManager.skip not in filename:
            for stall in range(10):
                if os.path.exists(filename):
                    break
                time.sleep(1)
            try:
                now=time.time()
                d=self.deSerializeTopperRecords(filename)
                metric.insertRecords(d.iteritems())
                metric.isCreatingPareto = topper.isWritingPareto
                self.mpWriteLastMetricToDisk(metric,slice0UnixTime,slice1UnixTime)
                processingTime = time.time()-now
            except Exception,e:
                sys.stdout.write("%s failed to unpickle %s - %s\n" %(metric.myMetricType,filename,str(e)))
                sys.stdout.flush()
            metric.myRecords.clear()    # since metric is persistent, remove data from last round
            metric.myParetoData.clear() # same here
            ackQueue.put((filename,processingTime))

            self.maintainDebugCommands(execFile)#look for external commands for my worker


    def doVolumeMetric(self,topper):
        T = TopperRecord(None) # dummy for constructing the factories
        m = TopperMetric(VolumeMetricRecord(T),"last","volume",topper.myTopperName,TOP.BYTES,topper.myShouldIgnoreIndicator,topper.myTopReportLineLegend,self.myLogger)
        m.isTitleVolumeMetric = isinstance(topper,TitleTopper)
        cmpFunc=lambda node1,node2: cmp(node1[1].myData.myBytes.myTotalData,node2[1].myData.myBytes.myTotalData)
        self.workerProcessLoop(topper,cmpFunc,m,topper.myVolumeMpQueue,topper.myVolumeAckMpQueue)

    def doTimeMetrics (self,topper):
        T = TopperRecord(None) # dummy for constructing the factories
        m = TopperMetric(SecondsMetricRecord(T),"last","time",topper.myTopperName,TOP.DURATION,topper.myShouldIgnoreIndicator,topper.myTopReportLineLegend,self.myLogger)
        cmpFunc=lambda node1,node2: cmp(node1[1].myData.mySeconds.myTotalData,node2[1].myData.mySeconds.myTotalData)
        self.workerProcessLoop(topper,cmpFunc,m,topper.myTimeMpQueue,topper.myTimeAckMpQueue)

    def doSessionMetrics (self,topper):
        T = TopperRecord(None) # dummy for constructing the factories
        m = TopperMetric(ViewsMetricRecord(T),"last","sessions",topper.myTopperName,TOP.HITCOUNT,topper.myShouldIgnoreIndicator,topper.myTopReportLineLegend,self.myLogger)
        cmpFunc=lambda node1,node2: cmp(node1[1].myData.mySessions.myTotalData,node2[1].myData.mySessions.myTotalData)
        self.workerProcessLoop(topper,cmpFunc,m,topper.mySessionMpQueue,topper.myVolumeAckMpQueue)
# end of mp funcs


    def mpCreateLastHourMetrics(self,isRoundHour):
        #update shared memory so that all processes get to know current timefarme
        slice0UnixTime=self.myRawDataTimeSlices[0].myRepresentingTimeSlice.myUnixTime
        slice1UnixTime=self.myRawDataTimeSlices[1].myRepresentingTimeSlice.myUnixTime
        i=0
        self.myPassMetricsToWorkersTime.profileDeltaTime()
        self.myPickledTopEnum += 1

        #submit data to all worker processes


        dispatchTime = int(time.time())
        for topper in self.myToppers:
            if (topper.myEveryMinuteTop or isRoundHour==True):
                filename="%s/%s_%d.pkl" % (self.myInputScanRoot,topper.myTopperName,self.myPickledTopEnum)
                try:
                    self.serializeTopperRecords(topper.myRecords,filename)
                except Exception,e:
                    self.myLogger.error("Failed pickling %s - %s" % (filename,str(e)))

        # clear the topperRecords of the last hours in toppers that work once every hour
                if (not topper.myEveryMinuteTop) and (isRoundHour==True):
                    topper.initRecordData() # drop all records after the round hour

                for q in [topper.myVolumeMpQueue,topper.myTimeMpQueue,topper.mySessionMpQueue]:
                    q.put((filename,slice0UnixTime,slice1UnixTime))
                    topper.myTasksStatus[filename]={"cntDones":0,"dispatchTime":dispatchTime,"maxProcessingTime":0}
                    i += 1

            self.myStatCounters.myPassMetricsToWorkersTime.logValue(int(self.myPassMetricsToWorkersTime.profileDeltaTime()))
            # do some cleaning
            topper.removeDoneWithFiles()



    # return the time work took
    def workWhileWaiting(self):
        t0=time.time()

            # put you idle-time tasks here
        self.myRecentTitleStack.periodicWrite() # only periodic write taking place more than once a minute

        t1=time.time()
        return t1-t0 # the time work took

    def terminateWorkers(self):
        for topper in self.myToppers:
            for q in [topper.myVolumeMpQueue,topper.myTimeMpQueue,topper.mySessionMpQueue]:
                q.put(["quit",])
        for p in self.mySubProcesses:
            p.join()
        # clean remains from inter process communication if any
        for topper in self.myToppers:
            topper.removeDoneWithFiles()
        
        
    # collect top-whatever from the last hour and build metric tables to be written to disk
    def createLastHourMetrics(self,isRoundHour):
        metrics = []
        T = TopperRecord(None) # dummy for constructing the factories
        for topper in self.myToppers:
            if (topper.myEveryMinuteTop or isRoundHour==True):
                if self.myReportTotalPorts == True:
                    m = TopperMetric(VolumeMetricRecord(T,0),"last","volume",topper.myTopperName,TOP.BYTES,topper.myShouldIgnoreIndicator,self.myLogger)
                    m.insertRecords(topper.myRecords.iteritems())
                    m.isCreatingPareto = topper.isWritingPareto
                    m.isTitleVolumeMetric = isinstance(topper,TitleTopper)
                    metrics.append(m)

                    m = TopperMetric(SecondsMetricRecord(T,0),"last","time",topper.myTopperName,TOP.DURATION,topper.myShouldIgnoreIndicator,self.myLogger)
                    m.insertRecords(topper.myRecords.iteritems())
                    m.isCreatingPareto = topper.isWritingPareto
                    metrics.append(m)

                    m = TopperMetric(ViewsMetricRecord(T,0),"last","sessions",topper.myTopperName,TOP.HITCOUNT,topper.myShouldIgnoreIndicator,self.myLogger)
                    m.insertRecords(topper.myRecords.iteritems())
                    m.isCreatingPareto = topper.isWritingPareto
                    metrics.append(m)

                if (not topper.myEveryMinuteTop) and (isRoundHour==True):
                    topper.initRecordData() # drop all records after the round hour
    
        return metrics
    
    

    #mp version
    def mpWriteLastMetricToDisk(self,metric,slice0UnixTime,slice1UnixTime):
        destFolder = ""
 
        toppertime = TopperTime(slice0UnixTime)#read from shared memory 
        prevTopperTime = TopperTime(slice1UnixTime)#read from shared memory 
        isRoundHour = toppertime.sliceCompare(prevTopperTime,TopperTime.SLICE_HOUR) > 0 #do they belong to the same hour

        t2 = toppertime
        t1 = prevTopperTime
        t2t = t2.myStructTime # 
        t1t = t1.myStructTime # 
        currMinute = t2t.tm_min
        prevMinute = t1t.tm_min
    
        try:
            hourlyFile = metric.saveToFile(self.myTopReportRoot ,"hour.tsv")
        except Exception,e:
            self.myLogger.error("Failed writing hourly metric %s for topper %s - %s" % (metric.myMetricType,metric.myReportType,str(e)))
        try:
            metric.savePareto(hourlyFile)
        except Exception,e:
            self.myLogger.error("Failed writing hourly pareto metric %s for topper %s - %s" % (metric.myMetricType,metric.myReportType,str(e)))
        # In the beginned of every new "round hour"
        if  isRoundHour: # instead of 'currMinute==0' incase testing faster time got us past the minute 0
            #self.writeLastFourTwelveHoursTopper(metric,t1,t2t.tm_hour)
            folder = os.sep.join([self.myTopReportRoot , metric.myReportType , metric.myTimeType , metric.myMetricType ])
            destFolder = os.sep.join([self.myTopReportRoot , metric.myReportType , "hourly" , metric.myMetricType ])
            dest = destFolder + os.sep + t1.getHourlyFilename()

            copyFile(folder + os.sep + "hour.tsv",dest,self.myLogger)
            if metric.isCreatingPareto:
                copyFileIfExists(folder  + os.sep + "hour.tsv.pareto",dest+".pareto",self.myLogger)

            if t1t.tm_mday != t2t.tm_mday: # day transition
                destFolder = os.sep.join([self.myTopReportRoot , metric.myReportType , "hourly" , metric.myMetricType ])
                self.doDayTransition(metric,t1,destFolder)
                if isFirstWeekDay(t2t): # week transition - new day is monday
                    destFolder = os.sep.join([self.myTopReportRoot , metric.myReportType , "daily" , metric.myMetricType ])
                    self.doWeeekTransition(metric,t2,destFolder)
                if t1t.tm_mon != t2t.tm_mon: # month transition
                    destFolder = os.sep.join([self.myTopReportRoot , metric.myReportType , "daily" , metric.myMetricType ])
                    self.doMonthTransition(metric,t1,destFolder)
                if t1t.tm_year != t2t.tm_year: # year transition
                    destFolder = os.sep.join([self.myTopReportRoot , metric.myReportType , "monthly" , metric.myMetricType ])
                    self.doYearTransition(metric,t1,destFolder)



    # We keep this function for debug purposes as the pydbg does not like multiprocess. not even multithread
    def writeLastMetricsToDisk(self,metrics):
        destFolder = ""
        toppertime = self.myRawDataTimeSlices[0].myRepresentingTimeSlice
        prevTopperTime = self.myRawDataTimeSlices[1].myRepresentingTimeSlice
        isRoundHour = toppertime.sliceCompare(prevTopperTime,TopperTime.SLICE_HOUR) > 0
        if isRoundHour==True:
            pass
    
        t2 = toppertime
        t1 = prevTopperTime
        t2t = t2.myStructTime #
        t1t = t1.myStructTime #
        currMinute = t2t.tm_min
        prevMinute = t1t.tm_min
    
        for metric in metrics:
            try:
                hourlyFile = metric.saveToFile(self.myTopReportRoot ,"hour.tsv")
            except Exception,e:
                self.myLogger.error("Failed writing hourly metric %s for topper %s - %s" % (metric.myMetricType,metric.myReportType,str(e)))
            try:
                metric.savePareto(hourlyFile)
            except Exception,e:
                self.myLogger.error("Failed writing hourly pareto metric %s for topper %s - %s" % (metric.myMetricType,metric.myReportType,str(e)))
            # In the beginned of every new "round hour"
            if  isRoundHour: # instead of 'currMinute==0' incase testing faster time got us past the minute 0
                folder = os.sep.join([self.myTopReportRoot , metric.myReportType , metric.myTimeType , metric.myMetricType ])
                destFolder = os.sep.join([self.myTopReportRoot , metric.myReportType , "hourly" , metric.myMetricType ])
                dest = os.sep .join([destFolder , t1.getHourlyFilename()])
                src=folder + os.sep + "hour.tsv"
                copyFile(src ,dest,self.myLogger)

                # self.writeLastFourTwelveHoursTopper(metric,t1,t2t.tm_hour) #no need for the last 4, 12, 24 hours files anymore

                if metric.isCreatingPareto:
                    copyFileIfExists(folder  + os.sep + "hour.tsv.pareto",dest+".pareto",self.myLogger)
    
                if t1t.tm_mday != t2t.tm_mday: # day transition
                    destFolder = os.sep.join([self.myTopReportRoot , metric.myReportType , "hourly" , metric.myMetricType ])
                    self.doDayTransition(metric,t1,destFolder)
                    if isFirstWeekDay(t2t): # week transition - new day is monday
                        destFolder = os.sep.join([self.myTopReportRoot , metric.myReportType , "daily" , metric.myMetricType ])
                        self.doWeeekTransition(metric,t2,destFolder)
                    if t1t.tm_mon != t2t.tm_mon: # month transition
                        destFolder = os.sep.join([self.myTopReportRoot , metric.myReportType , "daily" , metric.myMetricType ])
                        self.doMonthTransition(metric,t1,destFolder)
                    if t1t.tm_year != t2t.tm_year: # year transition
                        destFolder = os.sep.join([self.myTopReportRoot , metric.myReportType , "monthly" , metric.myMetricType ])
                        self.doYearTransition(metric,t1,destFolder)
    
        


    def doYearTransition(self,metric,t,folder):
        pattern = folder + os.sep + t.getYearlyFilename ("[0-9][0-9].tsv")
        lastYearDaylyFiles = glob.glob(pattern)
        self.createAggeregatingTopper("monthly","yearly",metric,lastYearDaylyFiles,t,TopperTime.getYearlyFilename)
        # todo - move old yearly to archive?

    def doMonthTransition(self,metric,t,folder):
        pattern = folder + os.sep + t.getMonthlyFilename("[0-9][0-9].tsv")
        lastMonthDaylyFiles = glob.glob(pattern)
        self.createAggeregatingTopper("daily","monthly",metric,lastMonthDaylyFiles,t,TopperTime.getMonthlyFilename)
        #self.sendToArchive(folder,t, SECONDS.DAY*30 ,4,TopperTime.getMonthlyFilename,".tsv","[0-9][0-9][0-9][0-9]*.tsv")

    def doWeeekTransition(self,metric,t2,folder):
        lastWeekFiles = []
        t=0
        for i in range(1,8):
            t=TopperTime(t2.myUnixTime - i*SECONDS.DAY) # go back one day
            pattern = folder + os.sep + t.getDaylyFilename ()
            if os.path.exists(pattern):
                lastWeekFiles.append(pattern)
        self.createAggeregatingTopper("daily","weekly",metric,lastWeekFiles,t,TopperTime.getDaylyFilename)
        
    def doDayTransition(self,metric,t,srcFolder):
        pattern = srcFolder + os.sep + t.getDaylyFilename ("-*.tsv")
        lastDayHourlyFiles = glob.glob(pattern)
        self.createAggeregatingTopper("hourly","daily",metric,lastDayHourlyFiles,t,TopperTime.getDaylyFilename)
        # archive hours older than 7 days - NO MORE ARCHIVING TOP AND PARETO REPORTS
        # self.sendToArchive(srcFolder,t, SECONDS.DAY ,7,TopperTime.getDaylyFilename ,"-[0-9][0-9].tsv","[0-9][0-9][0-9][0-9]*.tsv")
        # self.sendToArchive(srcFolder,t, SECONDS.DAY ,7,TopperTime.getDaylyFilename ,"-[0-9][0-9].tsv","[0-9][0-9][0-9][0-9]*.tsv.pareto")
        
    def createAggeregatingTopper(self,aggFrom,aggName,metric,files,t,nameFunc):
        name = nameFunc(t)
        if len(files)==0:
            self.myLogger.info("%s found no earlyer %s to aggeregate, on %s" % (aggFrom,aggName,name))
            return
        aggMetric = metric.cloneWithEmptyData()
        aggMetric.myTimeType = aggName
        for file in files:
            try:
                aggMetric.addFromFile(file)# sum data from all hours found for that day
            except Exception,e:
                self.myLogger.error("Failed reading %s for %s - %s" % (file,aggName,str(e)))
        try:
            aggMetric.saveToFile(self.myTopReportRoot ,name)
        except Exception,e:
            self.myLogger.error("Failed writing file for %s %s/%s - %s" % (aggName,self.myTopReportRoot,name,str(e)))

    # leave all items matching the ft globpattern x decreaseCount. Move the rest to the archive
    def sendToArchive(self,folder,t,cecreaseAmount,decreaseCount,ftPatternFunc,pattern,allFilesPattern):
        allFiles = glob.glob(folder + os.sep + allFilesPattern) # all general report files in that folder
        if len(allFiles)==0:
            return
        keep = []
        patternsDebug = []
        for i in range(0,decreaseCount):
            t2 = TopperTime(t.myUnixTime - (i*cecreaseAmount))
            ptrn = folder + os.sep + ftPatternFunc(t2,pattern)
            files = glob.glob(ptrn)
            keep += files
        if len(keep)==0 and len(allFiles) >0:
            breakpoint=0
        s1 = set(allFiles)
        s2 = set(keep)
        moved = s1 - s2 # reduce subset of the files you want to keep
        if len(moved) >= 24: #todo - TBD how many files to zip on every such zipping round
            #self.myLogger.info("Archiving %d files from %s" % (len(moved),folder))
            any = moved.pop()
            moved.add(any)
            dest = any.replace("/reports/","/archive/")
            compressFolderContent(folder,dest+".tgz",self.myLogger,moved)
            try:
                os.system("rm -f %s" % " ".join(moved))
            except Exception,e:
                self.myLogger.error("Failed deleting files after archiving %s - %s" % (any+".tgz",str(e)))



    # write to disk per-minute last hour volume
    def writeLastHourVolume(self,filename,offset,metric):
        fd = ""
        sum = BWRecord() # one line hourly
        last = os.sep.join([self.myOutputFolder,"reports","bw","last",metric[0],"hour.tsv"])
        fd = a.sys.analytic.topper_record_utils.openFileForWrite(last + "_",self.myLogger)
        exportFunc = metric[1]
        addFromArrFunc = metric[2]
        addFromOtherfunc = metric[3]
        if fd==None:
            return sum
        try:
            slices = self.myRawDataTimeSlices[offset:offset+60]
            slices.reverse() # invert the order of the slices - oldest is in index 0
            for slice in slices:
                addFromOtherfunc(sum,slice.myBWRecord)
                fd.write(theSepToken.join(slice.getMinuteBWRecord(exportFunc)+["\n",]))

        except Exception,e:
            self.myLogger.error("Failed iterating slices while writing volume file %s starting at offset=%d - %s" % (filename,offset,str(e)))
            fd.close()
            return sum
        fd.close()
        fd = ""
        copyFrom = last  + "_"
        # write hour.tsv only for the first hour slices
        if offset==1:
            copyFrom = rename(last  + "_",last,self.myLogger)
        if len(filename) > 0: # create file only on round hours
            try:
                shutil.copy(copyFrom,filename)
            except Exception,e:
                self.myLogger.error("Failed copying %s to %s - %s" % (last,filename,str(e)))
        return sum
    
    # 4/12 hours for the topper containers
    def writeLastFourTwelveHoursTopper(self,metric,t1,hour):
        hourlyFolder = os.sep.join([self.myTopReportRoot , metric.myReportType , "hourly" , metric.myMetricType ])
        for i in range(1,24): # start with 1 as the last hour already existing in memory
            t=TopperTime(t1.myUnixTime - i*3600)
            filename = hourlyFolder + os.sep + t.getHourlyFilename()
            if os.path.exists(filename):
                metric.addFromFile(filename)
            if i==3:
                metric.saveToFile(self.myTopReportRoot ,"4hours.tsv")
            if i==11:
                metric.saveToFile(self.myTopReportRoot ,"12hours.tsv")
            if i==23:
                metric.saveToFile(self.myTopReportRoot ,"24hours.tsv")
                #if self.makeLastDebugCopies==True:
                    #metric.debugDuplicate(self.myTopReportRoot ,"24hours",".tsv",t1)
    


    # 4/12 hours for time-based volume data
    def writeLastFourTwelveHoursVolume(self,metric):
        if len(self.myRawDataTimeSlices)==0:
            return
        t = self.myRawDataTimeSlices[0].myRepresentingTimeSlice
        last4tmp = os.sep.join([self.myBWReportRoot ,  "last",metric[0],"4hours_tmp_.tsv"])
        last12tmp = os.sep.join([self.myBWReportRoot ,  "last",metric[0],"12hours_tmp_.tsv"])
        last24tmp = os.sep.join([self.myBWReportRoot ,  "last",metric[0],"24hours_tmp_.tsv"])
    
        fd4= a.sys.analytic.topper_record_utils.openFileForWrite(last4tmp,self.myLogger)
        fd12=a.sys.analytic.topper_record_utils.openFileForWrite(last12tmp,self.myLogger)
        fd24=a.sys.analytic.topper_record_utils.openFileForWrite(last24tmp,self.myLogger)
        if fd4==None or fd12==None or fd24==None:
            return

        exportFunc = metric[1]
        addFromArrFunc = metric[2]
        addFromOtherfunc = metric[3]

        hours = range(24,0,-1)
        for i in hours: # iterate all 12
            t2=TopperTime(t.myUnixTime - i*3600)
            filename = os.sep.join([self.myBWReportRoot , "minute",metric[0],t2.getHourlyFilename()])
            if os.path.exists(filename): # read from existing file
                fd=a.sys.analytic.topper_record_utils.openFileForRead(filename,self.myLogger)
                if fd==None:
                    continue
                try:
                    for line in fd:
                        fd24.write(line)
                        if i<= 12:
                            fd12.write(line)
                        if i <= 4:
                            fd4.write(line)
                except Exception,e:
                    self.myLogger.error("Failed while reading from %s - %s"%(filename,str(e)))
                    fd.close()
                    continue
                fd.close()
            else: # no such existing file - generate an empty file
                fd=a.sys.analytic.topper_record_utils.openFileForWrite(filename,self.myLogger)
                if fd==None:
                    continue
                try:
                    empty = RawRecordsSlice(t2)
                    for j in range(0,60):
                        t2 = TopperTime(t2.myUnixTime-60)
                        empty.myRepresentingTimeSlice = t2
                        line = theSepToken.join(empty.getMinuteBWRecord(exportFunc)+["\n",])
                        fd.write(line)
                        fd12.write(line)
                        if i <= 4:
                            fd4.write(line)
                except Exception,e:
                    self.myLogger.error("Failed while writing blank data to %s - %s"%(filename,str(e)))
                fd.close()
        fd4.close()
        fd12.close()
        fd24.close()

        rename(last4tmp,last4tmp.replace("_tmp_",""),self.myLogger)
        rename(last12tmp,last12tmp.replace("_tmp_",""),self.myLogger)
        rename(last24tmp,last24tmp.replace("_tmp_",""),self.myLogger)

#create a non existing file, insert blank records or from map if exists
# stop on current time or transition
    def createUpdateBWFile(self,headSilceTime,currTime,filename,spec,metric):
        fd=a.sys.analytic.topper_record_utils.openFileForWrite(filename,self.myLogger)
        if fd==None:
            return False
        sum = BWRecord()
        key=""
        exportFunc = metric[1]
        addFromArrFunc = metric[2]
        addFromOtherfunc = metric[3]
        try:
            t = currTime.clone()
            empty = BWRecord()
            while t.sliceCompare(currTime,spec.myTimeCompareGranularity)==0:
                key = spec.myTimeKeyFunction(t)
                if key in self.myBWSubtotals.mySubTotals[metric[4]]: # do we have an updated information in memory for this line?
                    sub = self.myBWSubtotals.mySubTotals[metric[4]][key]
                    line = theSepToken.join([key,] + sub.exportToStringArray(exportFunc)) + "\n"
                    addFromOtherfunc(sum,sub)
                else:
                    line = theSepToken.join([key,] + empty.exportToStringArray(exportFunc)) + "\n"
                fd.write(line)
                t=TopperTime(t.myUnixTime + spec.myNumOfSecondsToSkip)
                if t.sliceCompare(currTime) < 0:
                    pass
                    #break
            fd.close()
        except Exception,e:
            self.myLogger.error("CreateUpdate: failed while writing to %s - %s" % (filename,str(e)))
            return False
        key = key[0:len(key)-3] # use last key of lower level to generate key of this level
        self.myBWSubtotals.rememberSubtotal(metric,key, sum) # update for the next level
        return True


    #load bw data file into a dictionary where the timestamp is the key
    def loadBWFileDict(self,filename,origDict=None):
        fd=a.sys.analytic.topper_record_utils.openFileForRead(filename,self.myLogger)
        dict = {}
        if origDict != None:
            dict = origDict
        if fd==None:
            return dict
        try:
            for line in fd:
                tokens=line.strip().split(theSepToken)
                line.strip()
                if len(tokens) < 2:
                    continue
                    
                key = tokens[0]
                dict[key]=tokens
            fd.close()
        except Exception,e:
            self.myLogger.error("Update: Failed while reading line %s from %s_  - %s" % (key,filename,str(e)))
        return dict



    #use the values stored in 'myBWSubtotals' to update higher level files
    #and store higher level subtotals for even higher subtotals
    # used for month/year
    def updateBWFile(self,filename,timestamp,spec,metric):
        headSilceTime = self.myRawDataTimeSlices[0].myRepresentingTimeSlice
        if not os.path.exists(filename):
            return self.createUpdateBWFile(headSilceTime,timestamp,filename,spec,metric)
        fileData = self.loadBWFileDict(filename)

        wfd=a.sys.analytic.topper_record_utils.openFileForWrite(filename + "_",self.myLogger )
        if wfd==None:
            return

        sum = BWRecord()
        empty = BWRecord()
        exportFunc = metric[1]
        addFromArrFunc = metric[2]
        addFromOtherfunc = metric[3]
        # read line by line and decie if to keep or modify. Always add to sum
        key=""
        t = spec.myMakeHeadTimeFunc(timestamp)
        firstKey = spec.myTimeKeyFunction(t)
        try:
            while t.sliceCompare(timestamp,spec.myTimeCompareGranularity)==0:
                key = spec.myTimeKeyFunction(t)
                if key in self.myBWSubtotals.mySubTotals[metric[4]]: # do we have an updated information in memory for this line?
                    sub = self.myBWSubtotals.mySubTotals[metric[4]][key]
                    addFromOtherfunc(sum,sub)
                    line = theSepToken.join([key,] + sub.exportToStringArray(exportFunc))
                elif key in fileData: # do we have it in the original file
                    tokens = fileData[key]
                    addFromArrFunc(sum,tokens)
                    line = theSepToken.join(tokens)
                else: # No history. let's make up an empty one. Nothing to add into sum
                    line = theSepToken.join([key,] + empty.exportToStringArray(exportFunc))

                if line[-1] != '\n':
                    line += "\n"
                wfd.write(line)
                t = TopperTime(t.myUnixTime + spec.myNumOfSecondsToSkip)
                if t.sliceCompare(headSilceTime) >= 0:#as this is an update - don't create entries in the future
                    break
            wfd.close()
        except Exception,e:
            self.myLogger.error("Update: Failed while writing  line %s to %s_  - %s" % (key,filename,str(e)))
        wfd = ""
        rename(filename + "_",filename,self.myLogger)
        key = firstKey[0:len(firstKey)-spec.myNumOfCharsToChopForNextLevelKey] # use last key of lower level to generate key of this level
        self.myBWSubtotals.rememberSubtotal(metric,key, sum) # update for the next level



    #daily differs from monthly/yearly as it builds from concatenation of hourly files 
    #and not from subtotals of lower levels
    #create/update daily file containing per-minute records
    def updateDailyBWFile(self,filename,timestamp,metric):
        headSilceTime = self.myRawDataTimeSlices[0].myRepresentingTimeSlice
        fileData = {} # all lines from all files in the relevant 24 hrs
        exportFunc = metric[1]
        addFromArrFunc = metric[2]
        addFromOtherfunc = metric[3]
        # load to memory minutes from hour files already on disk
        for i in range(0,24):
            daily=timestamp.getDaylyFilename("-%02d.tsv"%i)
            minutesFile = os.sep.join([self.myBWReportRoot,"minute",metric[0],daily])
            if os.path.exists(minutesFile): #load existing file to memory
                fileData = self.loadBWFileDict(minutesFile,fileData)
        #open destination file
        wfd=a.sys.analytic.topper_record_utils.openFileForWrite(filename + "_",self.myLogger )
        if wfd==None:
            return
        sum = BWRecord()
        empty = BWRecord()
        key=""
        t = timestamp.cloneFromHourZero()
        firstKey = t.getMinuteLineTimeStamp()
        try:
            while t.myStructTime.tm_mday == timestamp.myStructTime.tm_mday:#iterate all minutes in this 24 hours
                key = t.getMinuteLineTimeStamp()
                if key in fileData: # do we have it in the original file
                    tokens = fileData[key]
                    addFromArrFunc(sum,tokens)
                    line = theSepToken.join(tokens)
                else: # No history. make up an empty one. Nothing to add into sum
                    line = theSepToken.join([key,] + empty.exportToStringArray(exportFunc))

                if line[-1] != '\n':
                    line += "\n"
                wfd.write(line)
                t = TopperTime(t.myUnixTime + SECONDS.MINUTE)
                if t.sliceCompare(headSilceTime) >= 0:#as this is an update - don't create entries in the future
                    break
            wfd.close()
        except Exception,e:
            self.myLogger.error("Update: Failed while writing  line %s to %s_  - %s" % (key,filename,str(e)))
        wfd = ""
        rename(filename + "_",filename,self.myLogger)
        key = firstKey[0:len(firstKey)-6] # use last key of minute level to generate key of daily level
        self.myBWSubtotals.rememberSubtotal(metric,key, sum) # update for the next levels
        (srcFolder,name) = os.path.split(filename)

        # archive hourly files with minute records (temp files, archived for debugging purposes)
        self.sendToArchive(srcFolder,headSilceTime, SECONDS.DAY ,7,TopperTime.getDaylyFilename ,"-[0-9][0-9].tsv","[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]-*.tsv")

        # from now (2.0.5) do not archive
        #self.sendToArchive(srcFolder,headSilceTime, SECONDS.DAY*30 ,3,TopperTime.getMonthlyFilename ,"[0-9][0-9].tsv","[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9].tsv")


        

    #after having data of a certain hour updated - the update propagates to the relevant day/month/year
    def updateAffectedAggregators(self,metric):
        metricIndex=metric[4]
        spec = BWUpdateSpec.theDay
        for filename,timestamp in self.myBWSubtotals.myDaysToUpdate[metricIndex]: # update day files
            self.updateDailyBWFile(filename,timestamp,metric)
        spec = BWUpdateSpec.theMonth
        for filename,timestamp in self.myBWSubtotals.myMonthsToUpdate[metricIndex]: # update month files
            self.updateBWFile(filename,spec.myMakeHeadTimeFunc(timestamp),spec,metric) 
        spec = BWUpdateSpec.theYear
        for filename,timestamp in self.myBWSubtotals.myYearsToUpdate[metricIndex]: # update year files
            self.updateBWFile(filename,spec.myMakeHeadTimeFunc(timestamp),spec,metric)

    

    def writeLastMinuteOverTime(self):
        # write per-minute lines into hourly files
        self.myBWSubtotals = BWSubtotals()          
        numOfSlices = len(self.myRawDataTimeSlices)
        hours = numOfSlices / 60
        offset = (hours-1)*60 + 1
        headSilceTime = self.myRawDataTimeSlices[0].myRepresentingTimeSlice
        prevHead = self.myRawDataTimeSlices[1].myRepresentingTimeSlice
        # round hour will be indicated the first time we cross the line of round hour. Covers dt time leaps
        # if we did not have time shrinking, we could have just compared the minutes field to zero.
        isRoundHour = headSilceTime.sliceCompare(prevHead , TopperTime.SLICE_HOUR) > 0 
        # update all history minutes we hold in memory
        while hours > 0:
            t = self.myRawDataTimeSlices[offset].myRepresentingTimeSlice # point the hour that just finished
            #-------------------------------------------------------------------------------------------------------
            for metric in self.theBWMetrics: # volume,sessions,seconds
                lastHourFile = "" # if not a round hour, will not copy "last" into a named hour file
                if isRoundHour: #round hour
                    lastHourFile = os.sep.join([self.myBWReportRoot,"minute",metric[0],t.getHourlyFilename()])
                hourSum = self.writeLastHourVolume(lastHourFile,offset,metric) 
                if isRoundHour:
                    self.myBWSubtotals.rememberAffectedAggeregators(t,hourSum,self.myBWReportRoot,metric)
            #-------------------------------------------------------------------------------------------------------
            hours -= 1 
            offset = (hours-1)*60 + 1
        if isRoundHour: #the foloowing take place only once every round hour
            self.myStatCounters.myBWRoundHourCount.incrementValue()
            for metric in self.theBWMetrics:
                self.updateAffectedAggregators(metric)
                self.writeLastFourTwelveHoursVolume(metric)

    # update the clients over time file
    def writeClientsOverTime(self):

        # compose relevant file name
        curTime = self.myRawDataTimeSlices[0].myRepresentingTimeSlice.myUnixTime
        curTime -= 3600 # the relevant hour
        t = time.gmtime(curTime)
        fileName = os.path.join(self.myClientsOverTimeDir,"%04d%02d.tsv"%(t.tm_year,t.tm_mon))
        recordTime = "%04d-%02d-%02d-%02d:00" % (t.tm_year , t.tm_mon , t.tm_mday , t.tm_hour)
        recordValue = len(self.mySubscriberTopper.myRecords)
        
        
        # append the file with last hour info
        tempFileName = fileName+'_'
        fd_ = a.sys.analytic.topper_record_utils.openFileForWrite(tempFileName,self.myLogger)
        if fd_ == None:
            self.myLogger.error("periodic write of clients overTime in %s failed!"%self.myRawDataTimeSlices[0].myRepresentingTimeSlice.getMinuteFilename(""))
            return

        if (os.path.exists(fileName)):
            fd = a.sys.analytic.topper_record_utils.openFileForRead(fileName,self.myLogger)
            if (fd != None):
                for line in fd.readlines():
                    arr = line.split(theSepToken)
                    if arr[0]==recordTime:
                        if arr[1][-1]=='\n':
                           arr[1] = arr[1][:-1]
                        try:
                            recordValue += int(arr[1])
                        except Exception,e:
                            self.myLogger.error("failed to convert %s to int in clients over time  periodic write"%arr[1])

                    else:
                        fd_.write(line)

                fd.close()

        fd_.write("%s%s%s\n"%(recordTime,theSepToken,recordValue))
        fd_.close()

        rename(tempFileName,fileName,self.myLogger)


    # all topper and bw writes happen here
    def doPeriodicDiskWrites (self):
        # writeMemoryConsumption() # debug function for analyzing memory consumption and object counting
        global forever
        metrics= []
        if len(self.myRawDataTimeSlices) < self.theRawDataInMemoryPeriod: # wait until we have atleast 1 hour of slices
            return

        t = self.myRawDataTimeSlices[0].myRepresentingTimeSlice
        prevT = self.myRawDataTimeSlices[1].myRepresentingTimeSlice
        isRoundHour = t.sliceCompare(prevT , TopperTime.SLICE_HOUR) > 0 
        if isRoundHour:
            self.myStatCounters.myTopRoundHourCount.incrementValue()

        # This should occur every minute, but when we lag behind, we skip some minutes as needed
        # to allow recovering from this lagging behind. We will never skip round hour or a peak writing point, as it has a long chain reaction
        if self.shouldSkipSomeMinutes==False or isRoundHour==True or (t.myStructTime.tm_min%2)==0 or self.doMinuteSkip==False or (t.myStructTime.tm_min==self.myRoundHourTailSize):
            self.myStatCounters.myNumOfPeriodicWrites.incrementValue()
            if forever:
                self.myWriteBWTime.profileDeltaTime()
                #if round hour - will write hourly/daily/monthly etc BW records to reports/bw 
                self.writeLastMinuteOverTime()# writing the last minute with all resulting implications (BW only)
                self.myStatCounters.myWriteBWTime.logValue(int(self.myWriteBWTime.profileDeltaTime()))
            self.mySaveSnapshotTime.profileDeltaTime()
            self.myStatCounters.mySaveSnapshotTime.logValue(int(self.mySaveSnapshotTime.profileDeltaTime())) # TODO: remove this

            if forever and (t.myStructTime.tm_min==self.myRoundHourTailSize): # write every hour, not on round hour (after myRoundHourTailSize minutes)
                self.writePeak()

            # write to reports/bw/hour/clients
            # TODO add logging here
            if forever and isRoundHour:
                self.writeClientsOverTime()

            #write reports to reports/top
            self.myCreateMetricsTime.profileDeltaTime()
            if forever:
                if self.useMultiprocess==True:
                    self.mpCreateLastHourMetrics(isRoundHour)# assign tasks to worker processes which are already up
                else:
                    metrics = self.createLastHourMetrics(isRoundHour)
                    self.writeLastMetricsToDisk(metrics) # history also maintained inside
            createMetricsTime = self.myCreateMetricsTime.profileDeltaTime()
            self.myStatCounters.myCreateMetricsTime.logValue(int(createMetricsTime))
            # log the the time of top  calculation if this is an extreem value


            # This end the cpu consuming part that we may skip in odd minutes not on round hour
        
        self.myStatCounters.myLastHourListSize.logValue(len(self.myTitleTopper.myRecords))
        #update some stats counters before we write them
        self.updateResourceConsumption()
        self.myStatCounters.myModule.writeCurrentstats(t.myUnixTime)
        
    def writePeak(self):
        offset = self.myRoundHourTailSize + 1
        relevantSlices = self.myRawDataTimeSlices[offset:offset+60]
        self.myL2Peaker.writePeak(relevantSlices)

    def updateResourceConsumption(self):
        x=resource.getrusage(resource.RUSAGE_SELF)
        self.myStatCounters.myRuMaxRSS.logValue(x.ru_maxrss)
        self.myStatCounters.myRuIXRSS.logValue(x.ru_ixrss)
        self.myStatCounters.myRuIDRSS.logValue(x.ru_idrss)
        self.myStatCounters.myRuNSWAP.logValue(x.ru_nswap)
        self.myStatCounters.myRuUTIME.logValue(int(x.ru_utime))
        self.myStatCounters.myRuSTIME.logValue(int(x.ru_stime))

    # insert a new timeslice at the place of the iterator
    def insertNewSlice(self,toppertime):
        slice = RawRecordsSlice(toppertime)
        # update the BWRecord within the slice according to the future time stack
        self.myAllViewTimeStack.nMinutesUpdate(slice)
        self.myServableViewTimeStack.nMinutesUpdate(slice)
        self.myDeliveredViewTimeStack.nMinutesUpdate(slice)

        self.myStatCounters.myNewSlicesCreated.incrementValue()
        slice.setLogger(self.myLogger)
        self.myRawDataTimeSlices.insert(self.myCurrSliceIterator,slice)
        # clear topper data after 1 hour but leave the slice for another hour to track bw
        if len(self.myRawDataTimeSlices) > self.theRawDataInMemoryPeriod:
            toRemove = self.myRawDataTimeSlices[self.theRawDataInMemoryPeriod]
            newLast = self.myRawDataTimeSlices[self.theRawDataInMemoryPeriod-1]
            self.removeSliceTopperData(toRemove,newLast)
            gc.collect()
        if len(self.myRawDataTimeSlices) > self.theMaxNumOfSlices:
            self.myRawDataTimeSlices.pop()
        # every time we insert a new slice at location zero, that means a new minute
        # we write periodic reports unless we are in a quick future-minute-padding state
        if self.myCurrSliceIterator==0 and self.enablePeriodicWrites==True:
            self.doPeriodicDiskWrites()
        self.handlePauseQuota()

        # work the topper future stack - as one minute passed
        #self.myTopperFutureStack.nMinutesUpdate(slice)
        

    def removeSliceTopperData(self,slice,prevSlice):
        self.mySiteTopper.updateRecordsOnRemovedSlice(slice.mySitesCounters)
        
       # while (slice.mySitesCounters != []):
       #     topperPack = slice.myTopperPacks.pop()
       #     stillActive = topperPack.endOfWindowUpdate()
       #     if stillActive == True: # we need to re-hang this topperPack on the previous slice
       #         prevSlice.insertTopperPack(topperPack)
       #
       #     else: # topperPack is depleated. this is a potential spot for killing some topper records
       #         topperPack.killTopperRecordsIfNeeded(self.myToppers)
                

    def modifySiteName(self,record):
        data = record[REC.DATA]

        if self.selfModifyHost:
            name = data[FlowRecordOffsets.theHostOffset.myVal]
            record[REC.DATA][FlowRecordOffsets.theHostOffset.myVal] = getSite(name)

        shortnedPathUrl = data[FlowRecordOffsets.thePathOffset.myVal][:1]
        record[REC.DATA][FlowRecordOffsets.thePathOffset.myVal] = shortnedPathUrl

    def intifyRelevantFields(self,RawFRecord):
        RawFRecord[REC.DATA][FlowRecordOffsets.theInitiatorPortNumber.myVal] = max(0,int(RawFRecord[REC.DATA][FlowRecordOffsets.theInitiatorPortNumber.myVal]))
        RawFRecord[REC.DATA][FlowRecordOffsets.theDownloadTimeMsec.myVal]    = max(0,int(RawFRecord[REC.DATA][FlowRecordOffsets.theDownloadTimeMsec.myVal]))
        RawFRecord[REC.DATA][FlowRecordOffsets.theViewTimeMsec.myVal]        = max(0,int(RawFRecord[REC.DATA][FlowRecordOffsets.theViewTimeMsec.myVal]))
        RawFRecord[REC.DATA][FlowRecordOffsets.theSessionHitCount.myVal]     = max(0,int(RawFRecord[REC.DATA][FlowRecordOffsets.theSessionHitCount.myVal]))
        RawFRecord[REC.DATA][FlowRecordOffsets.theBeginOffset.myVal]         = max(0,int(RawFRecord[REC.DATA][FlowRecordOffsets.theBeginOffset.myVal]))
        RawFRecord[REC.DATA][FlowRecordOffsets.theDownloadedContentBytesPort0Offset.myVal] = max(0,int(RawFRecord[REC.DATA][FlowRecordOffsets.theDownloadedContentBytesPort0Offset.myVal]))
        RawFRecord[REC.DATA][FlowRecordOffsets.theDownloadedContentBytesPort1Offset.myVal] = max(0,int(RawFRecord[REC.DATA][FlowRecordOffsets.theDownloadedContentBytesPort1Offset.myVal]))


    # if title is cachable by qwilt - update the bw record of the relevant slices                
    def updateServableByQwilt(self,record):
        bytesPort0 = 0
        bytesPort1 = 0

        bytesPort0 = record[REC.DATA][FlowRecordOffsets.theDownloadedContentBytesPort0Offset.myVal]
        bytesPort1 = record[REC.DATA][FlowRecordOffsets.theDownloadedContentBytesPort1Offset.myVal]
        endTime = record[REC.TIMESTAMP]
        downMilisecs = record[REC.DATA][FlowRecordOffsets.theDownloadTimeMsec.myVal]
        initiatorPort = record[REC.DATA][FlowRecordOffsets.theInitiatorPortNumber.myVal]
        #we only count sessions which are last in transaction (where there are long sessions with periodic reports)
        sessionCounter = record[REC.DATA][FlowRecordOffsets.theSessionHitCount.myVal]

        viewMilisecs = record[REC.DATA][FlowRecordOffsets.theViewTimeMsec.myVal]
        #future miliseconds are the difference between viewtime and downloadtime
        futureMilisecs = viewMilisecs-downMilisecs
        
        isCachable  = (record[REC.DATA][FlowRecordOffsets.theIsCachableIndicator.myVal]=="1")
        isDelivered = (record[REC.DATA][FlowRecordOffsets.theIsDeliveredIndicator.myVal]=="1")

        clientId = record[REC.DATA][FlowRecordOffsets.theSrcIpOffset.myVal]
        
        if (futureMilisecs > 0): # is view time in the future
            # handle future data that is already in the past
            offset = self.myCurrSliceIterator
            allVTElem = FutureBWElement(futureMilisecs)
            cachVTElem = FutureBWElement(futureMilisecs)
            delvVTElem = FutureBWElement(futureMilisecs)

            while ((offset > 0) and (not allVTElem.isDone())):
                offset -= 1
                slice = self.myRawDataTimeSlices[offset]
                slice.myBWRecord.mySeconds.addData(allVTElem.decreaseXMinuteTime(1),0)
                if isDelivered:
                    slice.myBWRecord.mySeconds.addDelivered(delvVTElem.decreaseXMinuteTime(1),0)
                elif isCachable:
                    slice.myBWRecord.mySeconds.addServable(cachVTElem.decreaseXMinuteTime(1),0)

                
            if (not allVTElem.isDone()):
                self.myAllViewTimeStack.push(allVTElem)
                if isDelivered:
                    self.myDeliveredViewTimeStack.push(delvVTElem)
                elif isCachable:
                    self.myServableViewTimeStack.push(cachVTElem)

            viewMilisecs = downMilisecs

        # how many slices should we update backwards
        slices = 1 # pre-topper removes the need for smearing of data.

        if clientId=="0.0.0.0":
            slices = 1

        # calculate div and residue for bytes and seconds
        milisecondsPerSlice = viewMilisecs/slices # at this point viewMilisecs is <= downMilisecs
        milisecRes = viewMilisecs%slices

        bytesPort0perSlice =  bytesPort0 / slices
        bytesPort1perSlice =  bytesPort1 / slices
        bytesPort0res =  bytesPort0 % slices
        bytesPort1res =  bytesPort1 % slices
        

        #this tuple will revert directions if needed
        directions = (0,1)
        hits = (sessionCounter,0)
        if initiatorPort != 0:
            directions = (1,0)

        # first slice gets an explicit treatment due to residue
        iter = self.myCurrSliceIterator
        sliceCount = 0
        milisecs = (milisecondsPerSlice,0)

        # go through the entire duration of the flow and update all relevant slices
        while sliceCount < slices and iter < len(self.myRawDataTimeSlices):
            slice = self.myRawDataTimeSlices[iter]
            
            # Update backwards sessionns and views of all transactions
            # march2011 - no more smearing the session count backwards - only per the termination minute
            slice.myBWRecord.myVideoBytes.addData(bytesPort0perSlice , bytesPort1perSlice)
            slice.myBWRecord.mySeconds.addData(milisecs[directions[0]],milisecs[directions[1]])
            
            if isDelivered: #update backword delivered
                slice.myBWRecord.myVideoBytes.addDelivered( bytesPort0perSlice ,  bytesPort1perSlice)
                slice.myBWRecord.mySeconds.addDelivered(milisecs[directions[0]],milisecs[directions[1]])

            elif isCachable: #update backwards cachable
                slice.myBWRecord.myVideoBytes.addServable(bytesPort0perSlice , bytesPort1perSlice)
                slice.myBWRecord.mySeconds.addServable(milisecs[directions[0]],milisecs[directions[1]])
            
            iter += 1
            sliceCount += 1

        #last slice has to hold resadu as well + session data
        slice = self.myRawDataTimeSlices[self.myCurrSliceIterator]
        milisecs = (milisecRes ,0)
        #count session only on this slice
        slice.myBWRecord.mySessions.addData(hits[directions[0]],hits[directions[1]])#direction is set above according to theInitiatorPortNumber
        slice.myBWRecord.myVideoBytes.addData(bytesPort0res, bytesPort1res)
        slice.myBWRecord.mySeconds.addData(milisecs[directions[0]],milisecs[directions[1]])
        #update backwards cachable/deliverable residue
        if isDelivered:
           slice.myBWRecord.myVideoBytes.addDelivered( bytesPort0res ,  bytesPort1res )
           slice.myBWRecord.mySessions.addDelivered(hits[directions[0]],hits[directions[1]])#direction is set above according to theInitiatorPortNumber
           slice.myBWRecord.mySeconds.addDelivered(milisecs[directions[0]],milisecs[directions[1]])
        
        #if not delivered maybe it's just cached (serveblr undelivered)
        elif isCachable:
           slice.myBWRecord.myVideoBytes.addServable( bytesPort0res ,  bytesPort1res)
           slice.myBWRecord.mySessions.addServable(hits[directions[0]],hits[directions[1]])#direction is set above according to theInitiatorPortNumber
           slice.myBWRecord.mySeconds.addServable(milisecs[directions[0]],milisecs[directions[1]])




    def updateRecordStats(self,record):
        data = record[REC.DATA]
        bytes= long(data[FlowRecordOffsets.theDownloadedContentBytesPort0Offset.myVal]) + long(data[FlowRecordOffsets.theDownloadedContentBytesPort1Offset.myVal])
        milisec = long(data[FlowRecordOffsets.theDownloadTimeMsec.myVal])
        self.myStatCounters.myFlowBytesAvg.logValue(int(bytes))
        self.myStatCounters.myFlowDurationAvg.logValue(int(milisec))
        

    def insertRawRecordIntoCurrSlice (self,record):
        recType = record[REC.DATA][0]
        slice = self.myRawDataTimeSlices[self.myCurrSliceIterator]

        # some stats of unexpected records
        if self.myCurrSliceIterator >= self.theRawDataInMemoryPeriod: 
            self.myStatCounters.myRecordsOutOfSlice.incrementValue()

        if recType=="F":
            try:
                self.myStatCounters.myFlowReportsReceived.incrementValue()
                self.modifySiteName(record) # change long server name to short site name
                self.intifyRelevantFields(record)
                
                # prepare topperpack ingredients
                topperRecordsKeys = []
                relevantTopperRecords = []

                # update toppers only if the record is relevant for last hour
                if (self.myCurrSliceIterator < self.theRawDataInMemoryPeriod):
                    # update only in toppers that this record is relevant to. (titles and subscribers only if the record is from within the current hour)
                    shouldUpdateHourlyWorkingToppers = (self.myRawDataTimeSlices[0].myRepresentingTimeSlice.myStructTime.tm_hour == self.myRawDataTimeSlices[self.myCurrSliceIterator].myRepresentingTimeSlice.myStructTime.tm_hour)
                    for topper in self.myToppers:
                        if (topper.myEveryMinuteTop or shouldUpdateHourlyWorkingToppers): # update only the toppers that are working every minute (sites topper)
                            key,topperRecord = topper.addRecordData(record) # each topper will add selectivly - title and subscriber toppers will add only if the recordd is within the hour boundries
                    #topperRecordsKeys.append(key)
                    #relevantTopperRecords.append(topperRecord)

                    self.myRawDataTimeSlices[self.myCurrSliceIterator].updateSiteCounters(record)
                    
                # create a topper pack
                #topperPack = TopperPack(topperRecordsKeys,relevantTopperRecords,record)

                # push it into the time axis
                #offsetFromCurSlice = topperPack.hangOffsetFromCurrentSlice()
                #hangingIndex = self.myCurrSliceIterator + offsetFromCurSlice

                # Future smearing is of for now 13/5/12
                # in case we need to hang in an index that is not 0 - an update to the topperPack is needed
                #if self.myCurrSliceIterator>0:
                #    topperPack.inWindowUpdate(self.myCurrSliceIterator) # moves the time forward by myCurrSliceIterator minutes
                
                #if(hangingIndex > self.theRawDataInMemoryPeriod-1): 
                #    # we need to hang this outside of the hourly window
                #    # but that is impossible, so hand it on the last slice and update the topperPack
                #    minutesAboveHourlyWindow = hangingIndex - (self.theRawDataInMemoryPeriod-1)
                #    isRelevantTopperPack = topperPack.endOfWindowUpdate(minutesAboveHourlyWindow)
                #    if isRelevantTopperPack:
                #        self.myRawDataTimeSlices[self.theRawDataInMemoryPeriod-1].insertTopperPack(topperPack)
                #    else:
                #        # this topper pack has no purpose anymore but it may have createrd a topperRecord that needs to die
                #        topperPack.killTopperRecordsIfNeeded(self.myToppers)

                #else: # hang within the window
                #    self.myRawDataTimeSlices[hangingIndex].insertTopperPack(topperPack)
                
               # # if the topperpack still has future data, let it be heard -> put it in the future stack
               # if topperPack.hasMoreFuture():
               #         self.myTopperFutureStack.push(topperPack)

                # update recent titles - only if content length is valid - i.e not negative
                # todo - arnon , need to find a proper filter for invalid content len
                #if record[REC.DATA][theContentLengthOffset.myVal] != "-1":
                self.myRecentTitleStack.push(record)
                self.myRecentTitleStack.periodicWrite() # only periodic write taking place more than once a minute

                if self.myCurrSliceIterator >= self.theRawDataInMemoryPeriod:
                    ###self.myLogger.debug("drop: head=%s sliceIter=%d t=%s" % (self.myRawDataTimeSlices[0].myRepresentingTimeSlice.toString(),self.myCurrSliceIterator,record[0].toString()))
                    self.myStatCounters.myFlowRecordsOutOfSlice.incrementValue()

                self.updateRecordStats(record)
                # update servable on all slices
                self.updateServableByQwilt(record)

                

            except Exception,e:
                self.myLogger.error("Exception reading from Flow record " + str(e) + ",".join(map(str,record[REC.DATA])))

        if recType=="V":
                try:
                    slice.myBWRecord.addFromRawrecord(record)
                except Exception,e:
                    self.myLogger.error("Exception reading from BW record " + str(e) + ",".join(map(str,record[REC.DATA])))
        #if recType=="W": ### ENOUGH OF THIS SNAPSHOT STUFF
        #        try:
        #            slice.myBWRecord.addFromRawSnapshotrecord(record)
        #        except Exception,e:
        #            self.myLogger.error("Exception reading from BW record " + str(e) + ",".join(record[REC.DATA]))



    def getUnixTimeFromReportLineTime (self, reportTimeLine):    
        try:
            timeStruct = time.strptime(reportTimeLine,"%Y-%m-%d-%H:%M")
        except:
            self.myLogger.error("Bad report line timestamp: " % reportTimeLine)
            return None

        t = datetime.datetime(timeStruct.tm_year, timeStruct.tm_mon, timeStruct.tm_mday, timeStruct.tm_hour, timeStruct.tm_min) - datetime.datetime(1970,1,1)
            
        return (t.microseconds + (t.seconds + t.days * 24 * 3600) * 10**6) / 10**6

    def getLastReportTime (self):
        name=os.sep.join([self.myBWReportRoot,"last","volume","hour.tsv"])
        if os.path.exists(name):
            d=self.loadBWFileDict(name,None)
        else:
            return None

        sortedReportTimes = []
        for key in d:
            sortedReportTimes.append(key)
        sortedReportTimes.sort()
        ### return last report time ###
        return self.getUnixTimeFromReportLineTime(sortedReportTimes[-1])

    #load last 3 hours over-time data as much as possible
    def loadFromLastRecords (self):
        v,s,t={},{},{}
        for d,f in (v,"volume"),(t,"time"),(s,"sessions"):
            name=os.sep.join([self.myBWReportRoot,"last",f,"4hours.tsv"])
            if os.path.exists(name):
                d=self.loadBWFileDict(name,d)
            # truncate newer values from last 4 with last hour
            name=os.sep.join([self.myBWReportRoot,"last",f,"hour.tsv"])
            if os.path.exists(name):
                d=self.loadBWFileDict(name,d)
        for slice in self.myRawDataTimeSlices:
            timestamp=slice.myRepresentingTimeSlice
            key=timestamp.getMinuteLineTimeStamp()
            rec=slice.myBWRecord
            for metric,updateFunc in (v,BWRecord.addBytesFromStringArray),(s,BWRecord.addSessionsFromStringArray),(t,BWRecord.addSecondsFromStringArray):
                if key in metric:
                    arr=metric[key]
                    updateFunc(rec,arr)


    #upon first record insertion, build an empty history
    def buildFullEmptySlicesTail(self,recordTime):
        t=TopperTime(recordTime.myUnixTime - 60*self.theMaxNumOfSlices)
        for i in range(0,self.theMaxNumOfSlices):
            slice = RawRecordsSlice(t)
            slice.setLogger(self.myLogger)
            self.myRawDataTimeSlices.insert(self.myCurrSliceIterator,slice)
            t=TopperTime(t.myUnixTime + 60)
        self.loadFromLastRecords() # restore as much as possible from last 3 hours
        
        

    def sendUserMessageToLogger(self,record):
        rec = record[REC.DATA]
        msgOffset = LogMessageOffsets.theMessageOffset.myVal
        self.myLogger.info("USER: %s",rec[msgOffset])
        return True

    def handleFutureStamps(self,record):
        global forever
        if self.myCurrSliceIterator != 0:
            self.myLogger.error("Future timestamp when iterator=%d" % self.myCurrSliceIterator)
            return False
        recordTime = record[REC.TIMESTAMP]
        head = self.myRawDataTimeSlices[0].myRepresentingTimeSlice
        delta = recordTime.myUnixTime - head.myUnixTime

        relation = self.myRawDataTimeSlices[0].myRepresentingTimeSlice.sliceCompare(recordTime)
        watchdog = 0
        currEnable=self.enablePeriodicWrites # store incase we need to do some padding quickly without writing logs
        self.setPeriodicWriteEnable(self.enablePeriodicWrites or self.isUsingShrinkingTime)
        while relation < 0:
            stamp = self.myRawDataTimeSlices[0].myRepresentingTimeSlice.clone()
            stamp.goForwardOneSlice()
            self.myCurrSliceIterator = 0
            self.insertNewSlice(stamp)
            relation = stamp.sliceCompare(recordTime)    
            watchdog += 1
            if watchdog%10000==0:
                self.myLogger.info("Accelerated rate gap is %d" % watchdog)
            if not forever: # if we are to stay here for a while - see that we can respond to sigterm
                break
        self.setPeriodicWriteEnable(currEnable)
        ###self.myLogger.debug("padded %d future slices head=%d" % (watchdog,self.myRawDataTimeSlices[0].myRepresentingTimeSlice.myUnixTime))
        return True


    # shorter code for debug prints
    def sliceStamp(self,indx):
        if len(self.myRawDataTimeSlices)<=indx:
            return TopperTime(0)
        return self.myRawDataTimeSlices[indx].myRepresentingTimeSlice

    #timestamp debug logging
    def debugStamp (self,timestamp,reference=0):
        refTime=self.sliceStamp(reference)
        relation =  refTime.sliceCompare(timestamp)
        self.myLogger.info("R=%d indx=%d t=%s " % (relation,reference,timestamp.toString()))
        
    # do not pad all the entries if we had a considerable down time
    def isFutureJumpLongerThanWindow (self,recordTime):
        if self.isUsingShrinkingTime:
            return False
        t0 = self.sliceStamp(0).myUnixTime
        r0 = recordTime.myUnixTime
        if t0 >= r0:
            return False
        minutes = (r0 - t0)/60
        if minutes > self.theMaxNumOfSlices:
            #we now need to flush out all the window
            self.myLogger.info("Flushing out existing entries. Gap was %d minutes" % minutes)
            while len(self.myRawDataTimeSlices)>0:
                slice = self.myRawDataTimeSlices.pop() # tail slice
                prevSlice = self.myRawDataTimeSlices[-1]
                self.removeSliceTopperData(slice,prevSlice)
            return True
        return False
        

    # the heart of this leaky bucket record insertion
    # we try finding a matching slice and crawl backwrds in time.
    # if there are holes, we pad them with empty slices
    def insertRecord(self,record):
        global forever
        recordTime = record[REC.TIMESTAMP]
        recType = record[REC.DATA][0]
        dt=0
        if len(self.myRawDataTimeSlices)>0:
            dt=self.myRawDataTimeSlices[0].myRepresentingTimeSlice.myUnixTime
        ###self.myLogger.debug("insert %s %d h=%d" % (recType,recordTime.myUnixTime,dt))
        if recType=="L": # log message - do not insert into raw
            return self.sendUserMessageToLogger(record)


        #all empty - first slice
        if len(self.myRawDataTimeSlices)==0 :
            lastReportTime = self.getLastReportTime()
            if lastReportTime != None:
                ### pass same class with modified time ###
                recordTime.myUnixTime = lastReportTime
            self.buildFullEmptySlicesTail(recordTime)
            ### now that we have initialized the slice tail, we process the new record regulary ###
            return self.insertRecord(record)

        self.myCurrSliceIterator = 0 # always attempt to insert at the head
        refTime = self.myRawDataTimeSlices[self.myCurrSliceIterator].myRepresentingTimeSlice
        relation =  refTime.sliceCompare(recordTime)
        
        hadSmaller=False
        #future record - do we need padding
        if relation < 0 and self.myCurrSliceIterator==0:
            if self.handleFutureStamps(record)==False:
                return False
            # recalculate reftime and releation as they have changed inside 
            refTime = self.myRawDataTimeSlices[self.myCurrSliceIterator].myRepresentingTimeSlice
            relation =  refTime.sliceCompare(recordTime)
            hadSmaller=True
            # if not - relation has now turned 0
    
        # that's an easy one - we are in the slice pointed by the iterator
        if relation == 0:
            self.insertRawRecordIntoCurrSlice(record)
            return True

        if hadSmaller:
            self.myLogger.error("Relation is still < at this point. that is fishy")
            return False

        # should I pad or do I get a matching slice by walking the iterator
        prevSliceTime = self.myRawDataTimeSlices[self.myCurrSliceIterator].myRepresentingTimeSlice
        while self.myCurrSliceIterator < (TopperManager.theMaxNumOfSlices - 1):
            self.myCurrSliceIterator += 1

            if self.myCurrSliceIterator < len(self.myRawDataTimeSlices):
                refTime = self.myRawDataTimeSlices[self.myCurrSliceIterator].myRepresentingTimeSlice
                relation =  refTime.sliceCompare(recordTime)
            else:
                relation = 1 #current slice is later than the inserted record

            if relation == 0: # this is the right slice for this record
                self.insertRawRecordIntoCurrSlice(record)
                return True
            if not forever:
                break
            # we expect that all slices from here till the end are continious
        ###self.myLogger.debug("Insert rec is False: t=%s it=%d t0=%s " % (recordTime.toString(),self.myCurrSliceIterator,self.myRawDataTimeSlices[0].myRepresentingTimeSlice.toString()))
        return False
        


    #save title topper entries
    def saveTitleTopperSnapshot(self,filename,srcLRU):
        file = self.myOutputFolder + os.sep + filename
        fd = a.sys.analytic.topper_record_utils.openFileForWrite(file + "_",self.myLogger)
        if fd != None: #myNewbiesLRU
            node = srcLRU.myHead 
            arr=[]
            boundary = len(srcLRU)
            watchdog = 0
            while node != None:
                rec = node.myRecord
                arr.insert(0,rec.getSnapshotData(node.myKey))
                node = node.myNext 
                watchdog += 1
                if watchdog > boundary:
                    break
            cPickle.dump(arr,fd)
            rename(file+"_",file,self.myLogger)
            
    

    #we load title topper only for the files, so all data is reset upon load
    def loadTitleTopperSnapshot(self,filename,destLRU):
        return
        #@@#
        global forever
        file = self.myOutputFolder + os.sep + filename
        if os.path.exists(file):
            fd = a.sys.analytic.topper_record_utils.openFileForRead(file,self.myLogger)
            allItems = []
            if fd != None:
                try:
                    allItems = cPickle.load(fd)
                except Exception,e:
                    self.myLogger.error("Failed to unpickle titleTopper %s: %s" % (filename,str(e)))
                plen=len(allItems)
                counter=0
                currTime = 0 # todo - serealize time into file
                for arr in allItems :
                    key = arr[0]
                    counter+=1
                    rec = self.myTitleTopper.createNewRecordNode(key,destLRU)
                    rec.setFromSnapshot(arr)
                    if not forever:
                        break
        

    def saveSlicesSnapshotToDisk(self):
        pass
        #return #@@#
        #self.saveTitleTopperSnapshot("titles2.pkl",self.myTitleTopper.myActiveLRU)
        #if self.takeNewFilesSnapshot: # 
        #    self.saveTitleTopperSnapshot("titles1.pkl",self.myTitleTopper.myNewbiesLRU)
        #if self.takeRawRecordsSnapshot==False:
        #    return
        #file = self.myOutputFolder + os.sep + self.mySnapshotFilename
        #fd = a.sys.analytic.topper_record_utils.openFileForWrite(file + "_",self.myLogger)
        #if fd != None:
        #    try:
        #        for slice in reversed(self.myRawDataTimeSlices):
        #            for record in slice.myRawRecords:
        #                fd.write("\t".join(record[REC.DATA]))
        #            if len(slice.myRawRecords)==0: #no raw data for that slice
        #                fd.write("\t".join(slice.myBWRecord.exportToSnapshotRecord(slice.myRepresentingTimeSlice.myUnixTime) + ["\n",]))
        #        rename(file+"_",file,self.myLogger)
        #    except Exception ,e:
        #        self.myLogger.error("Failed to write snapshot file - %s" % str(e))


    def readSlicesSnapshotFromDisk (self):
        #return#@@#
        #self.loadTitleTopperSnapshot("titles2.pkl",self.myTitleTopper.myActiveLRU)
        #if self.takeNewFilesSnapshot: # 
        #    self.loadTitleTopperSnapshot("titles1.pkl",self.myTitleTopper.myNewbiesLRU)
        if self.takeRawRecordsSnapshot==False:
            return
        reader = RawDataReader(self.myLogger)
        file = self.myOutputFolder + os.sep + self.mySnapshotFilename
        if os.path.exists(file):
            if reader.loadFile(file,self.myInputRateThreshold)==True:
                reader.fix86()
                self.processRawData([reader,])
                if len(self.myRawDataTimeSlices) > 0:
                    latestTime = self.myRawDataTimeSlices[0].myRepresentingTimeSlice
                    self.myLogger.info("Read last hour snapshot from disk. Latest timeslice is " + latestTime.toString())
      


    # read last slice raw output from each of the Line/Delivery proccesses
    def processRawData(self,readers):
        self.myCurrSliceIterator = 0 
        while len(readers) > 0:  # if any readers removed, i.e. finished their records - proceed with the remainng
            earlyestTime = TopperTime(0xEFFFFFFFF) # one of the timestamps is bound to be higher
            #locate the latest timestamp ammyLong the readers as base
            for reader in readers:
                t = reader.getEarlyestTime() #t = reader.getCurrentRecordTime()
                if earlyestTime.sliceCompare(t) > 0: #There is an earlyer time
                    earlyestTime = t
            anyReaderHad = True # records for the current slice
            while anyReaderHad == True: # read as long as the records bemyLong to the same slice
                anyReaderHad = False
                blacklist = []
                for reader in readers: # collect all records in the current slice from multiple cores
                    t = reader.getEarlyestTime ()
                    if earlyestTime.sliceCompare(t) == 0: #from same slice
                        anyReaderHad = True
                        record = reader.popEaryestRecord()
                        if self.insertRecord(record)==False:# and that means also drop all earlyer records
                            remaining = sum(map(lambda r : len(r.myLines), readers))
                            #self.myLogger.warning("Stopped processing current batch. Discarded %d records" % remaining)
                            self.myStatCounters.myNumOfRecordsDropped.incrementValue(remaining)
                            return 
                        if reader.hasMoreRecords()==False:
                            blacklist.append(reader) # no more records for this reader in this slice 
                #do removals AFTER iterating all readers, not to break iteration
                for reader in blacklist:
                    readers.remove(reader)



    #upon startup, check that all report paths exist and create them if they are not
    def createDirectoryTree(self):
        #makeDirsIfNeeded (self.myOutputFolder + os.sep + "fixed")

        port0Dirs = []
        port1Dirs = []
        if self.myReportPort0 == True:
            port0Dirs = ["volumep0","sessionsp0","timep0"]

        if self.myReportPort1 == True:
            port1Dirs = ["volumep1","sessionsp1","timep1"]

        for a in ["reports","archive"]:

            # top directory tree
            for x in ["sites","clients","titles"]:
                for y in ["last","hourly","daily","weekly","monthly","yearly"]:
                    for z in (["volume","sessions","time"] + port0Dirs + port1Dirs):
                        makeDirsIfNeeded(os.sep.join([self.myOutputFolder,a,"top",x,y,z]))

            # bw directory tree
            for x in ["last","minute","hour","day"]:
                for y in self.theBWMetrics:
                    makeDirsIfNeeded(os.sep.join([self.myOutputFolder,a,"bw",x,y[0]]))

            # bitrate directory tree
            for x in bitrate_report.BITRATE_REPORT_SUBTYPES_LIST:
                for y in bitrate_report.BITRATE_REPORT_TIME_UNIT_LIST:
                    makeDirsIfNeeded(os.sep.join([self.myOutputFolder,a,bitrate_report.BITRATE_REPORT_DIR_NAME,x,y]))

        makeDirsIfNeeded(os.sep.join([self.myOutputFolder,"archive",self.myDataSubfolder]))

        # recent titles
        makeDirsIfNeeded(os.sep.join([self.myOutputFolder,"reports","recent"]))

        # clients overtime
        self.myClientsOverTimeDir = os.sep.join([self.myOutputFolder,"reports","bw","hour","clients"])
        makeDirsIfNeeded(self.myClientsOverTimeDir)

        # peak
        makeDirsIfNeeded(self.myPeakDir)


    #if triggered by the user, all output data will be removed
    def performCleanIfNeeded(self):
        cleanFile = os.sep.join([self.myInputScanRoot,"topperCleanNow"]) # debug backdoor.out of spec..
        if os.path.exists(cleanFile) or RawDataReader.getCleanFlag()==True:
            RawDataReader.setCleanFlag(False) # put the flag back down
            if os.path.exists(cleanFile):
                removeFile(cleanFile,self.myLogger) # reset clear request
            self.myRawDataTimeSlices = [] # clear memory data
            for topper in self.myToppers:
                topper.initRecordData()#clear topper memory data
            removeTree(self.myOutputFolder,self.myLogger) # delete output folder
            self.createDirectoryTree()
            doneFile = os.sep.join([self.myInputScanRoot,"rotate","removedData"])
            self.myLogger.info("Performed a clear action")
            fd = a.sys.analytic.topper_record_utils.openFileForWrite(doneFile,self.myLogger)
            if fd: 
                fd.flush()
                fd.close()
            return True
        return False



    def createWorkersCommand(self,cmd):
        count=0
        for p in self.mySubProcesses:
            if p.pid:
                mfile = os.sep.join([self.myInputScanRoot,"exec-%d"%p.pid]) # debug
                fd=a.sys.analytic.topper_record_utils.openFileForWrite(mfile,self.myLogger)
                if fd:
                    fd.write("%s\n" % cmd)
                    fd.close()
                    count+=1
        self.myLogger.info("submitted command to %d workers" % count)


    # inject debug commands in the context of topperManager without taking the app down
    # with great power comes great responsibility
    # use with caution!
    def maintainDebugCommands(self,filename):
        mfile = os.sep.join([self.myInputScanRoot,filename]) # debug
        if os.path.exists(mfile):
            try:
                fd=open(mfile)
                commands = fd.readlines()
            except Exception,e:
                self.myLogger.error("Failed reading %s - %s" % (mfile,str(e)))
                fd.close()
                removeFile(mfile,self.myLogger)
                return
            fd.close()
            removeFile(mfile,self.myLogger)
            if os.path.exists(mfile):
                return # when playing with fire, take extra caution
            #excecute lines, one by one
            for cmd in commands:
                try:
                    exec (cmd)
                    if not "self.myLogger.info" in cmd:
                        self.myLogger.info("Excecuted command: %s " % cmd)
                except Exception,e: 
                    self.myLogger.error("Failed excecuting %s - %s" % (cmd,str(e)))

    def setPeriodicWriteEnable(self,value,msg=""):
        self.enablePeriodicWrites=value
        #self.myLogger.info("PeriodicEnable=%s %s" % (str(self.enablePeriodicWrites),msg))

    def writeReportHeaders (self):
        # write top reports header file, unchanged from previous versions
        for topper in self.myToppers:
            topper.writeReportsHeader(self.myTopReportRoot)

        # write bw & bitrate reports header
        bwHeadersParams = [(self.myBWReportRoot,self.theBWMetrics[0][0]+"_",BWRecord.exportVideoBytesHeader),(self.myBWReportRoot,self.theBWMetrics[1][0]+"_",BWRecord.exportSessionHeader),(self.myBWReportRoot,self.theBWMetrics[2][0]+"_",BWRecord.exportSecondsHeader)]

        bitrateHeadersParams = [(os.path.join(self.myBitrateReportRoot,bitrate_report.SESSION_REPORT_DIR_NAME),"",bitrate_report.SessionUnit.getReportHeader),(os.path.join(self.myBitrateReportRoot,bitrate_report.TRANSACTION_REPORT_DIR_NAME),"",bitrate_report.TransactionUnit.getReportHeader)]

        headersParameters = bwHeadersParams
        headersParameters.extend(bitrateHeadersParams)

        for headerParam in headersParameters:
            headerFile = os.path.join(headerParam[0],headerParam[1]+"report_header")
            fd = a.sys.analytic.topper_record_utils.openFileForWrite(headerFile,self.myLogger)
    
            if (fd != None):
                global theSepToken
                line = theSepToken.join(map(str,headerParam[2]())) + "\n"
                fd.write(line)
                fd.close()
            else:
                self.myLogger.error("failed to write header file:%s, file could not be opened"% headerFile)


    def run (self):
        global forever #may be modified outside by sigterm
        self.performCleanIfNeeded()
        self.createDirectoryTree()
        snapshotFile = a.sys.analytic.topper_record_utils.getHeaderFileName(self.myOutputFolder)# save the spec to the snapshot dir
        shouldReadFromHitory = False # you are guilty until proven otherwise
        if os.path.exists(snapshotFile) :
            shouldReadFromHitory = True # looks like there is something to read there
            if RawDataRecordValidator.initRecordTypes(snapshotFile,self.myLogger)==False:
                shouldReadFromHitory = False #nop. crappy data or non-backward compatible
                self.myLogger.info("skipping history reading.starting up fresh")

        if forever:
            self.initToppers()
            self.initBitrateReportModule()
            self.launchWorkerProcesses()
            self.writeReportHeaders() #write report headers
            if shouldReadFromHitory:
                self.setPeriodicWriteEnable(False)
                self.myBitrateReportDatabaseWriter.syncWithDatabase()
                self.readSlicesSnapshotFromDisk() # if there is any after the last run
                self.setPeriodicWriteEnable(True)

            self.myLogger.info("Starting to read live data")
            # Welcome to the eternity loop
            while forever:
                self.mygetReadersTime.profileDeltaTime()#profiling - start counting time for this round
                readers = self.getRawReaders() # blocking until data arrives
                self.myStatCounters.mygetReadersTime.logValue(int(self.mygetReadersTime.profileDeltaTime())) 
                if self.performCleanIfNeeded()==True: # check for clean instructions we may have received within the records
                    continue # so that we block waiting for new input and not cereate any new data
                if not forever:
                    break
                ### pop & process s records here ###
                self.processSessionRecords(readers)
                self.processRawData(readers)#here we parse the raw data and place it in the proper minute buckets
            self.saveSlicesSnapshotToDisk()
        self.terminateWorkers()
        self.myLogger.info(" -+-+-+-+- Topper " + str(os.getpid()) + " is down -+-+-+-+-")


    def processSessionRecords(self, readers):
        ### for now, we need to extract S records from the readers
        ### because they are not time synced with the rest of the records
        ### which will confuse topper if he attempts to process them regulary
        sessionRecords = collections.deque()
        filteredRecords = collections.deque()
        for reader in readers:
            while reader.hasMoreRecords():
                record = reader.myLines.pop()
                #if record[0] == 'S':
                #self.myLogger.error(record[REC.DATA])
                #self.myLogger.error("type = " + record[REC.DATA][0])
                if record[REC.DATA][0] == 'S':
                    sessionRecords.append(record)
                else:
                    filteredRecords.append(record)
            while len(filteredRecords) > 0:
                reader.myLines.append(filteredRecords.pop())
            ### remove empty readers from future processing ###
            if reader.hasMoreRecords() == False:
                readers.remove(reader)



        ### process all gathered sessison records ###
        while len(sessionRecords) > 0:
            #self.myLogger.error("PROCESSING S RECORD!")
            record = sessionRecords.pop()[REC.DATA]
           
            
            self.myBitrateReportDatabaseWriter.processRecord(record)




        


# --- createOptionParser --------------------------------------------------------------------------
def createOptionParser(prog, version):
    """ Returns optparse parser object with application and gem options """

    # Calc version and usage strings
    usage ="""
    %s [options]
    """ % prog
    versionStr = "%s %s" % (prog, version)

    # Create parser object
    parser = optparse.OptionParser(usage=usage, version=versionStr)

    # Add gem options
    gem.addOptparseOptions(parser)

    #topper options
#
    parser.add_option("-l","--topper-log-dir", dest="logDirName",help="Log directory")
    parser.add_option("-S","--topper-stats-dir", dest="statsDir",help="stats directory")
    parser.add_option("-s", "--src-folder", dest="srcFolder" , help="source files root folder")
    parser.add_option("-d", "--dest-folder", dest="destFolder" , help="output files root folder")
    parser.add_option("--no-minute-skip", dest="doMinuteSkip", action="store_false", help="do not use minute skip when under load")
    parser.add_option("--single-process", dest="useMultiprocess", action="store_false", help="run topper as a single python process")
    parser.add_option("--archive-v3-raw-data", dest="archiveV3RawData", action="store_true",default = False, help="enable topper archive")
    parser.add_option("--system-start-time-string", dest="systemStartTimeStamp", help="system start time stamp")
    parser.add_option("--stats-comm-dir",dest="statsCommunicationDir",help="Directory used for passing information to stats process")
    parser.add_option("--log-level",dest="logLevel",help="Logging level")
    parser.add_option("--log-file-size",dest="logFileSize",help="Size of each log file")
    parser.add_option("--log-total-size",dest="logTotalSize",help="Maximal total log size")
    parser.add_option("--log-config-file",dest="logConfigFile",help="Log config file to be tested periodically")
    parser.add_option("--log-config-load-period",dest="logConfigPeriod",help="Log config file load period")
    parser.add_option("--captain-kick-number",dest="kickNumber",help="kick number")
    parser.add_option("--self-host-modify", dest="selfModifyHost", action="store_true", help="perform self hostname trimming instead of relying on the line")
    parser.add_option("--time-guard-enable", dest="timeGuardEnable", help="Protects Topper from records with abnormal time in the future")
    parser.add_option("--time-guard-tolerance-interval", dest="timeGuardToleranceInterval", help="If timeGuard is enabled, any record which has greater time then the tolerance interval will be discarded")

    # Done
    return parser

# --- buildCfg ------------------------------------------------------------------------------------
def buildCfg(parser, appCfgDefaults):

    # Parse commnad line options
    (options, argsLeft) = parser.parse_args()      

    # Update infra configuration with command line options (for early verbose, for example)
    gem.updateCmdlineOptions(options)

    # Read user's & system's configuration files and update the configuration
    gem.readConfigFiles()

    # Update with the application configuration defaults
    gem.updateAppCfgDefaults(appCfgDefaults)

    # Set infra internal defaults
    gem.updateInternalCfgDefaults()

    # Configuration is done, notify infra
    gem.notifyCfgDone()

    # Return command line left args
    return argsLeft

