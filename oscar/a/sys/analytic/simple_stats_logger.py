#!/usr/bin/python
import logging.handlers
from operator import itemgetter
import time

# This module is a quick and dirty statlogs module
# The assumption is that the number of counters is not very large
# and does not change after "boot"




class StatModule:
    myCounters = None
    myDataFile = None
    myLogger = None
    myFile = None

    #assume using an external logger of the parent app
    def __init__(self,dataFileName, statsCommObj=None, logger=None):
        self.myCounters = []
        self.myLogger=logger
        #we use the logging rotating file for the stat logs
        self.myFile = logging.getLogger(dataFileName)
        self.myFile.setLevel(logging.DEBUG)
        handler = logging.handlers.RotatingFileHandler(dataFileName, maxBytes=1000000, backupCount=10)
        self.myFile.addHandler(handler)
        self.myLaststamp = time.time()
        self.statsCommObj = statsCommObj

    def nameExists(self,name):
        return name in map(itemgetter(0),self.myCounters)

    def logError (self,msg):
        if self.myLogger != None:
            self.myLogger.error(msg)

    def logInfo (self,msg):
        if self.myLogger != None:
            self.myLogger.info(msg)

    def logDebug (self,msg):
        if self.myLogger != None:
            self.myLogger.debug3(msg)

    def createStatCounter(self,name):
        if self.nameExists(name):
            msg = "%start counter %s already exists"%name
            self.logError(msg)
            raise Exception, msg
        counter = StatCounter()
        self.myCounters.append((name,counter))
        return counter

    def createAvgStatCounter(self,name):
        if self.nameExists(name):
            msg = "%start counter %s already exists"%name
            self.logError(msg)
            raise Exception, msg
        counter = AvgStatCounter()
        self.myCounters.append((name,counter))
        return counter


    #return stat headerline
    def makeHeaderFile(self,name):
        try:
            fd=open(name,"w")
        except Exception,e:
            self.logError("Failed to open stats header file %s - %s" % (name,str(e)))
            return
        line = ",".join(["time",] + map(itemgetter(0),self.myCounters))
        fd.write(line)

    def _commWithStats(self):
        if self.statsCommObj:
            counterData = {}
            for (name,counter) in self.myCounters:
                counterData[name] = counter.myValue
    
            self.logDebug("Counters sent to stats: \n%s" % str(counterData))
            self.statsCommObj.send(counterData)
        
    def writeCurrentstats(self,timestamp):
        tmp=time.time()
        self.myLaststamp
        line = ",".join([str(timestamp),] + map(StatCounter.str,map(itemgetter(1),self.myCounters)) + ["%.2f" % (tmp-self.myLaststamp),])
        self.myLaststamp = tmp
        self.myFile.info(line)
        self._commWithStats()
                        


# basic long counter
class StatCounter:
    myValue = None

    def __init__ (self):
        self.myValue = 0
        
    def logValue (self,value):
        self.myValue = value

    def incrementValue (self,inc=1):
        self.myValue = self.myValue + inc
    
    def str(self):
        if isinstance(self.myValue,int):
            return "%d" % self.myValue
        else:
            return "%.2f" % self.myValue


# maintain an ongoing average
class AvgStatCounter(StatCounter):
    myCount = None

    def __init__ (self):
        self.myCount = 0
        self.myValue = 0

    def logValue (self,value):
        self.myCount += 1.0
        if self.myCount > 1:
            rel = (self.myCount-1)/self.myCount
            self.myValue = self.myValue*rel + value/self.myCount
        else:
            self.myValue = value

#-----------------------------------------------------

def unitTest():
    m = StatModule("stats.log")
    c1 = m.createStatCounter("A")
    c2 = m.createAvgStatCounter("B")
    c3 = m.createStatCounter("C")
    m.makeHeaderFile("statsHeader.txt")
    m.writeCurrentstats(1)
    c1.logValue(1)
    c2.logValue(2)
    c3.logValue(3)
    m.writeCurrentstats(2)
    c1.logValue(2)
    c2.logValue(4)
    c3.logValue(6)
    m.writeCurrentstats(3)


