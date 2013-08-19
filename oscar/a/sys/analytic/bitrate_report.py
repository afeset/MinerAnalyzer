#!/usr/local/bin/python2.6

# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: alexb
import sys

import datetime
import time
import os
import copy
import bisect

import topper_record_utils as record_utils
import a.infra.format.json

##### global key names #####
### 
KB = 1000 * 8

TOTAL_SITES_KEY = '_allSupported'

### report directory names ###
FIVE_MINUTE_REPORT_DIR_NAME = 'five_minute'
HOUR_REPORT_DIR_NAME        = 'hour'

SESSION_REPORT_DIR_NAME = 'sessions'
TRANSACTION_REPORT_DIR_NAME = 'transactions'

BITRATE_REPORT_DIR_NAME = 'bitrate'

BITRATE_REPORT_TIME_UNIT_LIST = [FIVE_MINUTE_REPORT_DIR_NAME, HOUR_REPORT_DIR_NAME]

BITRATE_REPORT_SUBTYPES_LIST = [SESSION_REPORT_DIR_NAME, TRANSACTION_REPORT_DIR_NAME]





######################### interval generators ###############################
class TimeStampGeneratorInterface:
    def getNextTimeStamp (self):
        return None

class ConstantTimeStampGenerator (TimeStampGeneratorInterface):
    def __init__ (self,constantInterval, startOffsetInSec):
        self.constantInterval = constantInterval
        self.nextTimeStamp = startOffsetInSec

    def getNextTimeStamp (self):
        timeStamp = self.nextTimeStamp
        self.nextTimeStamp += self.constantInterval
        return timeStamp

class GmTimeMonthlyIntervalGenerator (TimeStampGeneratorInterface):
    def __init__ (self, startOffsetInSec, intervalSize):
        self.intervalSize = intervalSize
        self.myTimeStruct = datetime.datetime.fromtimestamp(startOffsetInSec)
        self.myTimeStruct.replace(day = 1, hour = 0, minute = 0, second = 0, microsecond = 0)
        

    def addMonth (self,timeStruct):
        year = timeStruct.year
        month = timeStruct.month
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
        delta = datetime.datetime(year, month, timeStruct.day) - timeStruct
        timeStruct += delta
        return timeStruct

    def getNextTimeStamp (self):
        secondsSinceEpoch = self.myTimeStruct - datetime.datetime(1970,1,1)
        for i in range(self.intervalSize):
            self.myTimeStruct = self.addMonth(self.myTimeStruct)
            self.tmp = i

        return (secondsSinceEpoch.microseconds + (secondsSinceEpoch.seconds + secondsSinceEpoch.days * 24 * 3600) * 10**6) / 10**6

        

class GmTimeYearlyIntervalGenerator (TimeStampGeneratorInterface):
    def __init__ (self,startOffsetInSec):
        self.myTimeStruct = datetime.datetime.fromtimestamp(startOffsetInSec)
        self.myTimeStruct.replace(month = 1, day = 1, hour = 0, minute = 0, second = 0, microsecond = 0)

    def addYear (self,timeStruct):
        delta = datetime.datetime(timeStruct.year + 1, timeStruct.month, timeStruct.day) - timeStruct
        timeStruct += delta
        return timeStruct

    def getNextTimeStamp (self):
        secondsSinceEpoch = self.myTimeStruct - datetime.datetime(1970,1,1)
        self.myTimeStruct = self.addYear(self.myTimeStruct)

        return (secondsSinceEpoch.microseconds + (secondsSinceEpoch.seconds + secondsSinceEpoch.days * 24 * 3600) * 10**6) / 10**6
#############################################################################

def getFileTimeFormat(timeSinceEpoch):
            t = time.gmtime(timeSinceEpoch)            
            return "%04d%02d%02d-%02d-%02d" % (t.tm_year , t.tm_mon , t.tm_mday , t.tm_hour, t.tm_min)

def getTimeFromFileFormat (fileTimeFormat):

    tm_year = 0
    tm_mon = 1
    tm_mday = 1
    tm_hour = 0
    tm_min = 0

    tm_year = int(fileTimeFormat[:4])

    if len(fileTimeFormat) > 4:
        tm_mon = int(fileTimeFormat[4:6])

    if len(fileTimeFormat) > 6:
        tm_mday = int(fileTimeFormat[6:8])

    if len(fileTimeFormat) > 8:
        tm_hour = int(fileTimeFormat[9:11])

    if len(fileTimeFormat) > 11:
        tm_min = int(fileTimeFormat[12:14])

    t = datetime.datetime(tm_year, tm_mon, tm_mday, tm_hour, tm_min) - datetime.datetime(1970,1,1)

    #return calendar.timegm(timeStruct)
    return (t.microseconds + (t.seconds + t.days * 24 * 3600) * 10**6) / 10**6

#####################################
class SessionRecord:
    def __init__ (self):
        self.timeofday = 0
        self.lineVolume = 0
        self.deliveryVolume = 0
        self.sessionDuration = 0
        self.lineTransactionDuration = 0
        self.deliveryTransactionDuration = 0
        self.siteName = ""
        self.sessionStartFlag = 0
        self.sessionEndFlag = 0
        self.hadPreviousDeliveryVolumeFlag = 0
        self.hadPreviousLineVolumeFlag = 0
#####################################

#####################################
class SessionBitrateUnit:
    def __init__ (self):
        self.unitTime = sys.maxint
        self.totalTime = 0
        self.totalVolume = 0
        self.peakBitRate = 0
        self.numOpened = 0
        self.numClosed = 0
        self.numCurrent = 0
        
        

    ### units must not overlap and be progressive in time!
    def combineUnit (self, unit):
        self.unitTime = min(self.unitTime, unit.unitTime)
        self.totalTime += unit.totalTime
        self.totalVolume += unit.totalVolume
        self.peakBitRate = max(self.peakBitRate, unit.peakBitRate)
        #self.numOpened += unit.numOpened
        #self.numClosed += unit.numClosed

        self.numCurrent += unit.numCurrent

        
        

    def getUnitTime (self):
        return self.unitTime

    def getReportList (self):
        return (self.totalTime, self.totalVolume, self.peakBitRate, self.numCurrent)

    def __str__ (self):
        return str(self.getReportList())

    @staticmethod
    def getReportHeader ():
        return ('TotalTime', 'TotalVolume', 'PeakBitRate', 'NumOpenedSessions')

class SessionSiteUnit:
    interfaces = ['line','delivery']
    def __init__ (self):
        self.interfaceDict = {}
        for interface in SessionSiteUnit.interfaces:
            self.interfaceDict[interface] = SessionBitrateUnit()
        ### add total if needed ###
        self.unitTime = 0

    def combineUnit (self, unit):
        for interfaceSession in unit.interfaceDict:
            if interfaceSession not in self.interfaceDict:
                self.interfaceDict[interfaceSession] = SessionBitrateUnit()
                
            self.interfaceDict[interfaceSession].combineUnit(unit.interfaceDict[interfaceSession])


    def getUnitTime (self):
        return self.unitTime

    def getReportList (self):
        line =  []
        newDict = {}
        for key,item in self.interfaceDict.iteritems():
            newDict[key] = item.getReportList()
        line.append(newDict)
        return line

    def __str__ (self):
        return str(self.getReportList())

    @staticmethod
    def getReportHeader ():
        headerDict = {}
        for interface in SessionSiteUnit.interfaces:
            headerDict[interface] = SessionBitrateUnit.getReportHeader()
        return [headerDict]

class SessionUnit:
    def __init__ (self):
        self.siteDict = {}
        self.unitTime = 0
        self.numUnits = 0

        self.siteDict[TOTAL_SITES_KEY] = SessionSiteUnit()

    def combineUnit (self, unit):
        for siteSession in unit.siteDict:
            if siteSession not in self.siteDict:
                self.siteDict[siteSession] = SessionSiteUnit()

            self.siteDict[siteSession].combineUnit(unit.siteDict[siteSession])

        self.numUnits += unit.numUnits

    def getUnitTime (self):
        return self.unitTime

    def setUnitTime (self, timeInSec):
        self.unitTime = timeInSec

    def getNumCurrentArray (self):
        arr = []
        for siteKey in self.siteDict:
            arr.append(self.siteDict[siteKey].numCurrent)
            for interfaceKey in self.siteDict[siteKey].interfaceDict:
                arr.append(self.siteDict[siteKey].interfaceDict[interfaceKey].numCurrent)
        return arr

    def setNumCurrentFromArray (self, array):
        ### array must have value for numCurrent of total,line and delivery per site###
        if len(array) != len(self.siteDict)*3:
            return

        arrIndx = 0
        for siteKey in self.siteDict:
            self.siteDict[siteKey].numCurrent = array[arrIndx]
            arrIndx += 1
            for interfaceKey in self.siteDict[siteKey].interfaceDict:
                self.siteDict[siteKey].interfaceDict[interfaceKey].numCurrent = array[arrIndx]
                arrIndx += 1


    def getReportList (self):
        line = [self.unitTime, self.numUnits]
        newDict = {}
        for key,item in self.siteDict.iteritems():
            newDict[key] = item.getReportList()
        line.append(newDict)
        return line

    def __str__ (self):
        return str(self.getReportList())

    @staticmethod
    def getReportHeader ():
        header = ['GmTime','NumAggregated']
        sites = ['Site']
        headerDict = {}
        for site in sites:
            headerDict[site] = SessionSiteUnit.getReportHeader()
        header.append(headerDict)
        return [header]

################################################### TRANSACTION ########################################################
#####################################
class TransactionBitrateUnit:
    def __init__ (self):
        self.unitTime = sys.maxint
        self.totalTime = 0
        self.totalVolume = 0
        self.peakBitRate = 0
        self.numOpened = 0
        self.numClosed = 0
        self.numCurrent = 0
        
        

    ### units must not overlap and be progressive in time!
    def combineUnit (self, unit):
        self.unitTime = min(self.unitTime, unit.unitTime)
        self.totalTime += unit.totalTime
        self.totalVolume += unit.totalVolume
        self.peakBitRate = max(self.peakBitRate, unit.peakBitRate)
        self.numOpened += unit.numOpened
        self.numClosed += unit.numClosed

        self.numCurrent += unit.numCurrent
        
        

    def getUnitTime (self):
        return self.unitTime

    def getReportList (self):
        return (self.totalTime, self.totalVolume, self.peakBitRate, self.numCurrent)

    def __str__ (self):
        return str(self.getReportList())

    @staticmethod
    def getReportHeader ():
        return ('TotalTime', 'TotalVolume', 'PeakBitRate', 'NumOpenedTransactions')

class TransactionSiteUnit:
    interfaces = ['line','delivery']
    def __init__ (self):
        self.interfaceDict = {}
        for interface in TransactionSiteUnit.interfaces:
            self.interfaceDict[interface] = TransactionBitrateUnit()
        self.unitTime = 0

    def combineUnit (self, unit):
        for interfaceTransaction in unit.interfaceDict:
            if interfaceTransaction not in self.interfaceDict:
                self.interfaceDict[interfaceTransaction] = TransactionBitrateUnit()
                
            self.interfaceDict[interfaceTransaction].combineUnit(unit.interfaceDict[interfaceTransaction])

    def getUnitTime (self):
        return self.unitTime

    def getReportList (self):
        line =  []
        newDict = {}
        for key,item in self.interfaceDict.iteritems():
            newDict[key] = item.getReportList()
        line.append(newDict)
        return line

    def __str__ (self):
        return str(self.getReportList())

    @staticmethod
    def getReportHeader ():
        headerDict = {}
        for interface in TransactionSiteUnit.interfaces:
            headerDict[interface] = TransactionBitrateUnit.getReportHeader()
        return [headerDict]

class TransactionUnit:
    def __init__ (self):
        self.siteDict = {}
        self.unitTime = 0
        self.numUnits = 0

        self.siteDict[TOTAL_SITES_KEY] = TransactionSiteUnit()

    def combineUnit (self, unit):
        for siteTransaction in unit.siteDict:
            if siteTransaction not in self.siteDict:
                self.siteDict[siteTransaction] = TransactionSiteUnit()

            self.siteDict[siteTransaction].combineUnit(unit.siteDict[siteTransaction])

        self.numUnits += unit.numUnits

    def getUnitTime (self):
        return self.unitTime

    def setUnitTime (self, timeInSec):
        self.unitTime = timeInSec

    def getNumCurrentArray (self):
        arr = []
        for siteKey in self.siteDict:
            for interfaceKey in self.siteDict[siteKey].interfaceDict:
                arr.append(self.siteDict[siteKey].interfaceDict[interfaceKey].numCurrent)
        return arr

    def setNumCurrentFromArray (self, array):
        ### array must have value for numCurrent of line and delivery per site###
        if len(array) != len(self.siteDict)*2:
            return

        arrIndx = 0
        for siteKey in self.siteDict:
            for interfaceKey in self.siteDict[siteKey].interfaceDict:
                self.siteDict[siteKey].interfaceDict[interfaceKey].numCurrent = array[arrIndx]
                arrIndx += 1



    def getReportList (self):
        line = [self.unitTime, self.numUnits]
        newDict = {}
        for key,item in self.siteDict.iteritems():
            newDict[key] = item.getReportList()
        line.append(newDict)
        return line

    def __str__ (self):
        return str(self.getReportList())

    @staticmethod
    def getReportHeader ():
        header = ['GmTime','NumAggregated']
        sites = ['Site']
        headerDict = {}
        for site in sites:
            headerDict[site] = TransactionSiteUnit.getReportHeader()
        header.append(headerDict)
        return [header]
################################################### ########### ########################################################

#####################################

#####################################
class UnitProcessor:
    def processUnit (self,unit):
        pass
#####################################

#####################################
class UnitMultiProcessor:
    def __init__ (self):
        self.unitProcessorList = []

    def registerUnitProcessor (self,unitProcessor):
        self.unitProcessorList.append(unitProcessor)

    def processUnit (self,unit):
        for processor in self.unitProcessorList:
            processor.processUnit(unit)
#####################################

#####################################
class ReportPeriodicFileWriter (UnitProcessor):
    def __init__ (self, writeDirectoryPath, fileNamePatternFunc):
        self.writeDirectoryPath = writeDirectoryPath
        self.fileNamePatternFunc = fileNamePatternFunc
        self.fileTimedName = self.fileNamePatternFunc(0)

    def processUnit (self, unit):
        unitTime = unit.getUnitTime()
        fileTimedName = self.fileNamePatternFunc(unitTime)
        fullFileTimedName = os.path.join(self.writeDirectoryPath,fileTimedName)

        #reportFile = open(fullFileTimedName,'w')
        #reportFile.write(unit.getReportLine())
        #reportFile.close()

        a.infra.format.json.writeToFile(None,unit.getReportList(),fullFileTimedName, indent=4)


    
#####################################
class SessionReportPeriodicFileReader():
    def __init__ (self):
        pass
    def constructUnitFromReport (self, reportPath):

        data = a.infra.format.json.readFromFile(None, reportPath)
        ### for now we assume it's always a session bitrate report! ###
        sessionUnit = SessionUnit()
        sessionUnit.unitTime = data[0]
        sessionUnit.numUnits = data[1]
        for siteDict in data[2]:
            sessionSiteUnit = SessionSiteUnit()
            for interfaceDict in data[2][siteDict][0]:
                bitrateUnit = SessionBitrateUnit()
                bitrateUnit.totalTime = data[2][siteDict][0][interfaceDict][0]
                bitrateUnit.totalVolume = data[2][siteDict][0][interfaceDict][1]
                bitrateUnit.peakBitRate = data[2][siteDict][0][interfaceDict][2]
                bitrateUnit.numCurrent = data[2][siteDict][0][interfaceDict][3]
                sessionSiteUnit.interfaceDict[interfaceDict] = bitrateUnit
            sessionUnit.siteDict[siteDict] = sessionSiteUnit

        return sessionUnit


class TransactionReportPeriodicFileReader():
    def __init__ (self):
        pass
    def constructUnitFromReport (self, reportPath):

        data = a.infra.format.json.readFromFile(None, reportPath)
        ### for now we assume it's always a session bitrate report! ###
        transactionUnit = TransactionUnit()
        transactionUnit.unitTime = data[0]
        transactionUnit.numUnits = data[1]
        for siteDict in data[2]:
            transactionSiteUnit = TransactionSiteUnit()
            for interfaceDict in data[2][siteDict][0]:
                #print interfaceDict
                bitrateUnit = TransactionBitrateUnit()
                bitrateUnit.totalTime = data[2][siteDict][0][interfaceDict][0]
                bitrateUnit.totalVolume = data[2][siteDict][0][interfaceDict][1]
                bitrateUnit.peakBitRate = data[2][siteDict][0][interfaceDict][2]
                bitrateUnit.numCurrent = data[2][siteDict][0][interfaceDict][3]
                transactionSiteUnit.interfaceDict[interfaceDict] = bitrateUnit
            transactionUnit.siteDict[siteDict] = transactionSiteUnit

        return transactionUnit
        


#####################################
class SessionUnitAggregatedBuilder:
    def __init__ (self):
        self.sessionUnit = SessionUnit()

    def processUnit (self, unit):
        self.sessionUnit.combineUnit(unit)

        
    def buildUnit (self):
        builtSessionUnit = self.sessionUnit
        self.sessionUnit = SessionUnit()
        #for siteSession in builtSessionUnit.siteDict:
        #    builtSessionUnit.siteDict[siteSession].numCurrentSessions += builtSessionUnit.siteDict[siteSession].numOpenedSessions  

        #    self.sessionUnit.siteDict[siteSession] = SessionSiteUnit()
        #    self.sessionUnit.siteDict[siteSession].numCurrentSessions = builtSessionUnit.siteDict[siteSession].numCurrentSessions - builtSessionUnit.siteDict[siteSession].numClosedSessions

        return builtSessionUnit

    def getUnit (self):
        return self.sessionUnit

    def setUnitTime (self,timeInSec):
        self.sessionUnit.unitTime = timeInSec


class TransactionUnitAggregatedBuilder:
    def __init__ (self):
        self.transactionUnit = TransactionUnit()

    def processUnit (self, unit):
        self.transactionUnit.combineUnit(unit)

        
    def buildUnit (self):
        builtTransactionUnit = self.transactionUnit
        self.transactionUnit = TransactionUnit()
        
        #for site in builtTransactionUnit.siteDict:
        #    self.transactionUnit.siteDict[site] = TransactionSiteUnit()
        #    for interfaceKey in builtTransactionUnit.siteDict[site].interfaceDict:
        #        builtTransactionUnit.siteDict[site].interfaceDict[interfaceKey].numCurrentTransactions += builtTransactionUnit.siteDict[site].interfaceDict[interfaceKey].numOpenedTransactions
        #        self.transactionUnit.siteDict[site].interfaceDict[interfaceKey].numCurrentTransactions = builtTransactionUnit.siteDict[site].interfaceDict[interfaceKey].numCurrentTransactions - builtTransactionUnit.siteDict[site].interfaceDict[interfaceKey].numClosedTransactions

        return builtTransactionUnit

    def getUnit (self):
        return self.transactionUnit

    def setUnitTime (self,timeInSec):
        self.transactionUnit.unitTime = timeInSec

#class AveragedCountUnitAggregatedBuilder:
#    def __init__ (self, unitBuilder):
#        self.unitBuilder = unitBuilder
#        self.inputCount = 0
#
#    def processUnit (self, unit):
#        self.unitBuilder.processUnit(unit)
#        self.inputCount += 1
#
#    def buildUnit (self):
#        numCurrentArray = self.unitBuilder.getUnit().getNumCurrentArray()
#        averagedNumCurrentArray = [a/self.inputCount for a in numCurrentArray]
#
#        self.unitBuilder.getUnit().setNumCurrentFromArray(averagedNumCurrentArray)
#
#        return self.unitBuilder.buildUnit()



class TimeSlicedUnitProcessor:
    def __init__ (self,timeStampGenerator, numSlices, unitBuilderClass, unitOutputProcessor, logger):
        self.logger = logger
        self.unitBuilders = [unitBuilderClass()] * numSlices

        self.sliceTimeRangesInSec = []
        self.timeStampGenerator = timeStampGenerator
        self.numSlices = numSlices
        self.unitOutputProcessor = unitOutputProcessor

        self._setSliceNextTimeRanges()

    def _setSliceNextTimeRanges (self):
        lastSliceTime = 0
        if len(self.sliceTimeRangesInSec) > 0:
            lastSliceTime = self.sliceTimeRangesInSec[-1]
        else:
            lastSliceTime = self.timeStampGenerator.getNextTimeStamp()
        self.sliceTimeRangesInSec = [lastSliceTime]
        #for sliceIter in range(1,self.numSlices+1):
        #    self.sliceTimeRangesInSec.append(self.timeStampGenerator.getNextTimeStamp())
        self.sliceTimeRangesInSec.extend([self.timeStampGenerator.getNextTimeStamp()] * self.numSlices)
        #print self.sliceTimeRangesInSec


    def processUnit (self, unit):
        newUnitTime = unit.getUnitTime()

        ### check if unit fits into our time range
        if newUnitTime >= self.sliceTimeRangesInSec[0] and newUnitTime < self.sliceTimeRangesInSec[self.numSlices]:
            ### map unit to builder
            builderIndex = 0
            for sliceIndx in range(self.numSlices):
                if newUnitTime < self.sliceTimeRangesInSec[sliceIndx+1]:
                    builderIndex = sliceIndx
                    break
        
            self.unitBuilders[builderIndex].processUnit(unit)
            return

        ### unit is in the past, sorry, time does not move backward(?)... discard this unit
        elif newUnitTime < self.sliceTimeRangesInSec[0]:
            if self.logger != None:
                self.logger.warning("got a unit with a time of " + str(newUnitTime) + ", skipping it because it is out of current time range [" + str(self.sliceTimeRangesInSec[0]) +"," + str(self.sliceTimeRangesInSec[self.numSlices]) + "]")
            return

        ### unit time exceeded our current time range, submit builders, init new builders for next time range 
        ### and attempt to process the unit at the next time range by calling this function again
        while newUnitTime >= self.sliceTimeRangesInSec[self.numSlices]:
            ### submit builders, also inits a clear report in builders
            self.submitBuilderUnits()

        ### process unit in next time range
        self.processUnit(unit)

        

    def submitBuilderUnits (self):
        for builder,sliceIndex in zip(self.unitBuilders, range(len(self.unitBuilders))):
            builder.setUnitTime(self.sliceTimeRangesInSec[sliceIndex])
            ### pass unit to output processor
            sliceBuiltUnit = builder.buildUnit()
            self.unitOutputProcessor.processUnit(sliceBuiltUnit)

        ### proceed to next time range
        self._setSliceNextTimeRanges()


######## temporary for tests ########
class UnitList (UnitProcessor):
    def __init__ (self):
        self.clear()
    def processUnit (self, unit):
        self.unitList.append(unit)
    def getUnits (self):
        return self.unitList
    def clear (self):
        self.unitList = []
#####################################

class TopperTimeSlicedReportWriter:
    def __init__ (self, reportRootPath, startOffsetInSec, unitBuilder, logger):
        self.logger = logger
        self.sessionReportPaths = {}
        sessionReportRootPath = reportRootPath
        self.sessionReportPaths['root'] = sessionReportRootPath
        for interval in BITRATE_REPORT_TIME_UNIT_LIST:
            self.sessionReportPaths[interval] = os.path.join(sessionReportRootPath,interval)

        ### temporary for tests ###
        self.unitMinuteReportWriter = ReportPeriodicFileWriter(self.sessionReportPaths[FIVE_MINUTE_REPORT_DIR_NAME], lambda t: getFileTimeFormat(t)) 
        self.unitHourReportWriter = ReportPeriodicFileWriter(self.sessionReportPaths[HOUR_REPORT_DIR_NAME], lambda t: getFileTimeFormat(t)[:-3])
        #self.unitDayReportWriter = ReportPeriodicFileWriter(self.sessionReportPaths['day'], lambda t: getFileTimeFormat(t)[:-6])
        #self.unitWeekReportWriter = ReportPeriodicFileWriter(self.sessionReportPaths['week'], lambda t: getFileTimeFormat(t)[:-6])
        #self.unitMonthReportWriter = ReportPeriodicFileWriter(self.sessionReportPaths['month'], lambda t: getFileTimeFormat(t)[:-8])
        #self.unitYearReportWriter = ReportPeriodicFileWriter(self.sessionReportPaths['year'], lambda t: getFileTimeFormat(t)[:-10])

        ###########################
        ### create a multiprocessor to feed output minute slices into reportWriter and other slices ###
        
        ### we need to use a 5 min average bitrate as a peak (instead of session/transaction bitrate), thus we override
        ### the 5 min unit peak bitrate to be it's average bitrate and other slices will compute peak according to a 5 min average.
        ### now we also need to make the 5 min unit "atomic" so we modify its unit count to be 1 so we'll be able to use it as a base
        ### unit for average transaction/session count
        class PeakAndUnitCountModifier(UnitMultiProcessor):
            def processUnit (self,unit):
                for siteKey in unit.siteDict:
                    for interfaceKey in unit.siteDict[siteKey].interfaceDict:
                        if unit.siteDict[siteKey].interfaceDict[interfaceKey].totalTime == 0:
                            unit.siteDict[siteKey].interfaceDict[interfaceKey].peakBitRate = 0
                        else:
                            unit.siteDict[siteKey].interfaceDict[interfaceKey].peakBitRate = (unit.siteDict[siteKey].interfaceDict[interfaceKey].totalVolume * KB) / unit.siteDict[siteKey].interfaceDict[interfaceKey].totalTime
                        #unit.siteDict[siteKey].interfaceDict[interfaceKey].numUnits = 1
                unit.numUnits = 1
                UnitMultiProcessor.processUnit(self,unit)



        minuteOutputProcessor = PeakAndUnitCountModifier()
        minuteOutputProcessor.registerUnitProcessor(self.unitMinuteReportWriter)
        
        ###########################

        self.timeSlices = []
        self.timeSlices.append(TimeSlicedUnitProcessor(ConstantTimeStampGenerator(60 * 5, (startOffsetInSec / (60 *5)) * 60*5), 1, unitBuilder,minuteOutputProcessor, self.logger))    # 5 mins
        self.timeSlices.append(TimeSlicedUnitProcessor(ConstantTimeStampGenerator(60 * 60, (startOffsetInSec / (60 *60)) * 60*60), 1, unitBuilder,self.unitHourReportWriter, self.logger))   # hour       
        
        ### connect the rest of the time slices to recieve their input from the minute slice ###
        for sliceUnitProcessor in self.timeSlices[1:]:
            minuteOutputProcessor.registerUnitProcessor(sliceUnitProcessor)

    def processUnit (self, unit):
        ### process only in the 5 minute bucket, the rest will be fed input from it ###
        self.timeSlices[0].processUnit(unit)


def aggregateUnits (intervalGenerator, inputUnits, unitBuilder, logger):
    outputUnits = UnitList()
    timeSliceProcessor = TimeSlicedUnitProcessor(intervalGenerator, 1, unitBuilder, outputUnits, logger)
    for unit in inputUnits:
        timeSliceProcessor.processUnit(unit)

    timeSliceProcessor.submitBuilderUnits()

    #endUnitBuilder = unitBuilder()
    #endUnitBuilder.setUnitTime(intervalGenerator.getNextTimeStamp())
    #timeSliceProcessor.processUnit(endUnitBuilder.buildUnit())

    return outputUnits.getUnits()

class TopperBitrateReportDatabaseReader:
    def __init__ (self, reportRootDirectory, logger):
        self.reportRootDirectory = reportRootDirectory
        self.logger = logger

    def getLatestReportTime (self):
        #print self.reportRootDirectory
        #print os.path.join(self.reportRootDirectory,'minute')
        minuteReportFiles = os.listdir(os.path.join(self.reportRootDirectory,BITRATE_REPORT_SUBTYPES_LIST[0], BITRATE_REPORT_TIME_UNIT_LIST[0]))

        if len(minuteReportFiles) == 0:
            return 0

        minuteReportFiles.sort()

        return getTimeFromFileFormat(minuteReportFiles[-1])

    ### mainly for ux_module ###
    def getSessionOvertimeFromReports (self, startTimeInSec, endTimeInSec, granularity, granularityUnit):
        reportPath = os.path.join(self.reportRootDirectory,SESSION_REPORT_DIR_NAME)
        return self._getUnitListFromReports(SessionUnitAggregatedBuilder, SessionReportPeriodicFileReader, reportPath,startTimeInSec,endTimeInSec,granularity,granularityUnit)

    def getTransactionOvertimeFromReports (self, startTimeInSec, endTimeInSec, granularity, granularityUnit):
        reportPath = os.path.join(self.reportRootDirectory,TRANSACTION_REPORT_DIR_NAME)
        return self._getUnitListFromReports(TransactionUnitAggregatedBuilder, TransactionReportPeriodicFileReader,reportPath,startTimeInSec,endTimeInSec,granularity,granularityUnit)

    def _getUnitListFromReports (self,unitBuilder,bitrateReportReader, subtypeDir, startTimeInSec, endTimeInSec, granularity, granularityUnit):
        reportDir = ''
        fileToTimeFunc = lambda f: getTimeFromFileFormat(f)
        timeToFileFunc = None

        ### if not month then seconds ###
        if granularityUnit != 'm':

            if (startTimeInSec%3600 == 0) and (endTimeInSec%3600 == 0) and (granularity%3600 == 0):
                reportDir = os.path.join(subtypeDir,HOUR_REPORT_DIR_NAME)
                timeToFileFunc = lambda t: getFileTimeFormat(t)[:-3]
            else:
                reportDir = os.path.join(subtypeDir,FIVE_MINUTE_REPORT_DIR_NAME)           
                timeToFileFunc = lambda t: getFileTimeFormat(t)

        else:
            reportDir = os.path.join(subtypeDir,HOUR_REPORT_DIR_NAME)
            timeToFileFunc = lambda t: getFileTimeFormat(t)[:-3]

        reportFileNames = os.listdir(reportDir)

        #self.logger.error("s reports = " + str(reportFileNames))

        if reportFileNames == []:
            return []

        reportTimes = map(fileToTimeFunc,reportFileNames)
        reportTimes.sort()

        #self.logger.error("s times = " + str(reportTimes))

        startReportIndex = bisect.bisect_left(reportTimes, startTimeInSec)
        #startReportIndex = 0
        #if reportTimes.count(startTimeInSec) == 1:
        #    startReportIndex = reportTimes.index(startTimeInSec)
        #elif startTimeInSec > reportTimes[-1]:
        #    startReportIndex = -1

        endReportIndex = bisect.bisect_left(reportTimes, endTimeInSec)
        #endReportIndex = len(reportTimes)#-1
        #if reportTimes.count(endTimeInSec) == 1:
        #    endReportIndex = reportTimes.index(endTimeInSec)
        #elif endTimeInSec < reportTimes[0]:
        #    endReportIndex = 0

        wantedReportTimes = reportTimes[startReportIndex:endReportIndex]

        #self.logger.error("wanted s reports = " + str(wantedReportTimes))

        if wantedReportTimes == []:
            return []

        wantedReportFiles = map(timeToFileFunc,wantedReportTimes)

        reportReader = bitrateReportReader()

        units = []
        for reportFile in wantedReportFiles:
            units.append(reportReader.constructUnitFromReport(os.path.join(reportDir,reportFile)))

        ### align to correct offset for startTime & interval
        startUnitTime = (((units[0].getUnitTime() - startTimeInSec)/ granularity)*granularity) + startTimeInSec

        ### make interval generator ###
        intervalGenerator = None
        if granularityUnit != 'm':
            intervalGenerator = ConstantTimeStampGenerator(granularity,startUnitTime)
        else:
            intervalGenerator = GmTimeMonthlyIntervalGenerator(startUnitTime, granularity)

        return aggregateUnits(intervalGenerator,units,unitBuilder, self.logger)


class TopperBitrateReportDatabaseWriter:
    def __init__ (self, bitrateReportRootDirectory, logger):
        
        self.bitrateReportRootDirectory = bitrateReportRootDirectory
        self.sessionReportRootDirectory = os.path.join(self.bitrateReportRootDirectory,SESSION_REPORT_DIR_NAME)
        self.transactionReportRootDirectory = os.path.join(self.bitrateReportRootDirectory,TRANSACTION_REPORT_DIR_NAME)

        self.topperSessionReportWriter = None
        self.topperTransactionReportWriter = None

        self.logger = logger


    def syncWithDatabase (self):
        databaseReader = TopperBitrateReportDatabaseReader(self.bitrateReportRootDirectory, self.logger)

        latestReportTime = databaseReader.getLatestReportTime()
        if latestReportTime == 0:
            return

        self.topperSessionReportWriter = TopperTimeSlicedReportWriter(self.sessionReportRootDirectory, latestReportTime, SessionUnitAggregatedBuilder, self.logger)
        self.topperTransactionReportWriter = TopperTimeSlicedReportWriter(self.transactionReportRootDirectory, latestReportTime, TransactionUnitAggregatedBuilder, self.logger)

        #return
        ### sync hour bucket from 5 mins ###
        units = databaseReader.getSessionOvertimeFromReports(((latestReportTime/3600) * 3600), latestReportTime,60*5, 's')
        for unit in units:
            self.topperSessionReportWriter.processUnit(unit)

        units = databaseReader.getTransactionOvertimeFromReports(((latestReportTime/3600) * 3600), latestReportTime,60*5, 's')
        for unit in units:
            self.topperTransactionReportWriter.processUnit(unit)

    def setStartTime (self, startTime):
        self.topperSessionReportWriter = TopperTimeSlicedReportWriter(self.sessionReportRootDirectory, startTime, SessionUnitAggregatedBuilder, self.logger)
        self.topperTransactionReportWriter = TopperTimeSlicedReportWriter(self.transactionReportRootDirectory, startTime, TransactionUnitAggregatedBuilder, self.logger)
        

    def processRecord (self, record):
        if record[0] != 'S':
            if self.logger != None:
                self.logger.warning(self.__class__.__name__ + " got a non-S Record, this should not happen! record is: " + record)
            return

        ### convert record to session unit ###
        sRecord = record_utils.SRecordHelper(record)


        sessionUnit = None
        transactionUnit = None
        ### catch any exceptions while reading the file
        try:
            ### lets add this just in case sync goes wrong for now ###
            if self.topperSessionReportWriter == None or self.topperTransactionReportWriter == None:
                self.setStartTime(sRecord.timeOfDay)

            ### check if we have an 'empty' record ###
            if sRecord.sessionId == 0:
                ### make empty units & advance their time ###
                sessionUnit = SessionUnit()
                sessionUnit.unitTime = sRecord.timeOfDay

                transactionUnit = TransactionUnit()
                transactionUnit.unitTime = sRecord.timeOfDay


            else:
                ### -- process session fields -- ###
                if sRecord.sessionIdExtractorIndex != 0:
                    ### raw bitrate data per interface ###
                    lineBitrateUnit = SessionBitrateUnit()
                    deliveryBitrateUnit = SessionBitrateUnit()
            
                    lineBitrateUnit.totalVolume = sRecord.lineVolume
                    deliveryBitrateUnit.totalVolume = sRecord.deliveryVolume
            
                    ###handle zero division!@ ###
                    duration = sRecord.duration
            
                    if (lineBitrateUnit.totalVolume + deliveryBitrateUnit.totalVolume) == 0:
                        lineBitrateUnit.totalTime = 0
                        deliveryBitrateUnit.totalTime = 0
            
                        lineBitrateUnit.peakBitRate = 0
                        deliveryBitrateUnit.peakBitRate = 0
            
                    else:
                        lineBitrateUnit.totalTime = duration * lineBitrateUnit.totalVolume / (lineBitrateUnit.totalVolume + deliveryBitrateUnit.totalVolume)
                        deliveryBitrateUnit.totalTime = duration * deliveryBitrateUnit.totalVolume / (lineBitrateUnit.totalVolume + deliveryBitrateUnit.totalVolume)
            
                        if lineBitrateUnit.totalTime == 0:
                            lineBitrateUnit.peakBitRate = 0
                        else:
                            lineBitrateUnit.peakBitRate = (lineBitrateUnit.totalVolume * KB) / lineBitrateUnit.totalTime
            
                        if deliveryBitrateUnit.totalTime == 0:
                            deliveryBitrateUnit.peakBitRate = 0
                        else:
                            deliveryBitrateUnit.peakBitRate = (deliveryBitrateUnit.totalVolume * KB) / deliveryBitrateUnit.totalTime
    
                    ### count session if it had any volume in line or delivery ###
                    if lineBitrateUnit.totalVolume != 0:
                        lineBitrateUnit.numCurrent = 1
    
                    if deliveryBitrateUnit.totalVolume != 0:
                        deliveryBitrateUnit.numCurrent = 1
            
                    ### session interface data for sites ###
                    sessionSiteUnit = SessionSiteUnit()
            
                    sessionSiteUnit.interfaceDict['line'] = lineBitrateUnit
                    sessionSiteUnit.interfaceDict['delivery'] = deliveryBitrateUnit
            
            
                    ### Session aggregated unit ###
                    sessionUnit = SessionUnit()
            
                    sessionUnit.unitTime = sRecord.timeOfDay
                    sessionUnit.siteDict[sRecord.siteName] = sessionSiteUnit
            
                    sessionUnit.siteDict[TOTAL_SITES_KEY] = copy.deepcopy(sessionSiteUnit)

                ### sRecord.sessionIdExtractorIndex == 0 ###
                else:
                    ### make empty units & advance their time ###
                    sessionUnit = SessionUnit()
                    sessionUnit.unitTime = sRecord.timeOfDay
                
                ### -- process transaction fields -- ###
                #
                ### raw bitrate data per interface ###
                lineBitrateUnit = TransactionBitrateUnit()
                deliveryBitrateUnit = TransactionBitrateUnit()
        
                lineBitrateUnit.totalVolume = sRecord.lineVolume
                deliveryBitrateUnit.totalVolume = sRecord.deliveryVolume
        
                lineBitrateUnit.totalTime = sRecord.sumLineTransactionDuration
                deliveryBitrateUnit.totalTime = sRecord.sumDeliveryTransactionDuration
        
                if lineBitrateUnit.totalTime == 0:
                    lineBitrateUnit.peakBitRate = 0
                else:
                    lineBitrateUnit.peakBitRate = (lineBitrateUnit.totalVolume * KB) / lineBitrateUnit.totalTime
        
                if deliveryBitrateUnit.totalTime == 0:
                    deliveryBitrateUnit.peakBitRate = 0
                else:
                    deliveryBitrateUnit.peakBitRate = (deliveryBitrateUnit.totalVolume * KB) / deliveryBitrateUnit.totalTime
        
                lineBitrateUnit.numCurrent = sRecord.numLineContinuingTransaction + sRecord.numLineStartTransaction

                deliveryBitrateUnit.numCurrent = sRecord.numDeliveryContinuingTransaction + sRecord.numDeliveryStartTransaction
        
                ### transaction interface data for sites ###
                transactionSiteUnit = TransactionSiteUnit()
        
                transactionSiteUnit.interfaceDict['line'] = lineBitrateUnit
                transactionSiteUnit.interfaceDict['delivery'] = deliveryBitrateUnit
        
                ### Transaction aggregated unit ###
                transactionUnit = TransactionUnit()
        
                transactionUnit.unitTime = sRecord.timeOfDay
                transactionUnit.siteDict[sRecord.siteName] = transactionSiteUnit
        
                transactionUnit.siteDict[TOTAL_SITES_KEY] = copy.deepcopy(transactionSiteUnit)

        except:
            if self.logger != None:
                self.logger.error("Unexpected error while parsing S record: " + sRecord)

        ### process unit if there were no exceptions ###
        else:
            ### process unit to report ###
            self.topperTransactionReportWriter.processUnit(transactionUnit)

            ### process unit to report ###
            self.topperSessionReportWriter.processUnit(sessionUnit)
        



