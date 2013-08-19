#!/usr/local/bin/python2.6

import os, time, calendar, datetime, sys, hashlib, base64
import a.sys.analytic.topper_report_utils as tru
import a.sys.analytic.bitrate_report as bitrate_report

# Data types names
#==========================================================
SESSIONS      = 'sessions'
VOLUME        = 'volume'
VIEW_TIME     = 'time'

L2_BW         = 'L2BW'
CLIENTS       = 'clients'
PEAK          = 'peak'

BITRATE       = 'bitrate'

dataTypes = [SESSIONS,VIEW_TIME,VOLUME] # L2 is special, should not be included in this list
additionalDataTypes = [CLIENTS]
aggregationDataTypes = [PEAK]

# Data SubType names
#==========================================================
BITRATE__SESSIONS = 'session'
BITRATE__TRANSACTIONS = 'transaction'


# Report types (string values are corresponding directory names)
#===============================================================
OVER_TIME  = 'bw'
TOPPER     = 'top'
RECENT     = 'recent'
TITLES_TSV = 'titles.tsv'

# Granularity units
#============================
SECOND = 's'
MONTH  = 'm'


# Granularity names - (over time requests)
#==========================================
MINUTE_NAME = "minute"
HOUR_NAME   = "hour"
DAY_NAME    = "day"
LAST_NAME   = "last"

# last hour file name
#=========================
LAST_HOUR_FILE_NAME = "hour.tsv"
LAST_HOUR_PARETO_FILE_NAME = "hour.tsv.pareto"

# Top categories
#==================
CLIENTS = "clients"
SITES   = "sites"
TITLES  = "titles"

# Dictionary format
#====================

KEY             = "key"
TIME            = "date"
TOTAL           = "total"
CACHABLE        = "cachable"
DELIVERED       = "delivered"
VIDEO           = "video"
VIDEO_DELIVERED = "videoDelivered"
CONTENT_ID      = "contentId"
CONTENT_LENGTH  = "contentLength"
SITE_ID         = "siteId"
TIMESTAMP       = "timestamp"
CLIENT          = "client"
TOTAL_ID        = "TOTAL" #the Total record id
GRAND_TOTAL     = "grandTotal"
ENTRIES         = "entries"
CUM_ITEMS       = "cumItems"
CUM_VALUE       = "cumValue"
TOTAL_REC_ITEMS = "items"
TOTAL_REC_VALUE = "value"
HOUR_OF_DAY     = "hourOfDay"
GENERIC_VALUE   = "value"

# pareto file index legend
#====================
PERCENTILE = 0
CUM_DATA   = 3
CUM_CNT    = 6

# aggregators (for overtime())
#==============================
MAX = "max"


# global function
#====================
def openFileForRead(filename,logger,openMode="r"):
    try:
        fd = open(filename,openMode)
        return fd
    except Exception, e:
        logger.error("Failed to open %s for read- %s " %( filename , str(e)))
        return None

def safeListDir(dirc,logger=None):
    try:
        files = os.listdir(dirc)
        return files

    except Exception, e:
        if (logger != None):
            logger.error("Failed to listDir %s - %s " %( dirc , str(e)))

        return []

topCategories = [CLIENTS,SITES,TITLES]

# this class contains tools for handeling diffrent granularities in over-time request
#=====================================================================================
class GranularitySet:
    
    def __init__(self,granularity,name,fileNameFormat,recondTimeFormat,rangeOfFileFunc,mayUseLastDir=False):
        self.granularity      = granularity           
        self.name             = name
        self.fileNameFormat   = fileNameFormat
        self.recordTimeFormat = recondTimeFormat
        self.rangeOfFile      = rangeOfFileFunc
        self.mayUseLastDir    = mayUseLastDir
        
    
# GranularitySet scale 
#==========================================================
MINUTE = GranularitySet(60,MINUTE_NAME,"%Y%m%d.tsv","%Y-%m-%d-%H:%M",lambda year,month: 86400 ,mayUseLastDir=True)
HOUR   = GranularitySet(60*60,HOUR_NAME,"%Y%m.tsv","%Y-%m-%d-%H:%M",lambda year,month: 86400*calendar.monthrange(year,month)[1])
DAY    = GranularitySet(24*60*60,DAY_NAME,"%Y.tsv","%Y-%m-%d",lambda year,month: 86400*(calendar.isleap(year)+365))
LAST   = GranularitySet(60,LAST_NAME,"hour.tsv","%Y-%m-%d-%H:%M",3600)
granularitySets = [MINUTE,HOUR,DAY]

# A class representing over-time records data type (session, 
# time, volume) and responsible for manipulating a raw record
#===============================================================
class GenericDataType:

    # static variable
    outputDictionaryLabels = [TIME,TOTAL,CACHABLE,DELIVERED]

    def __init__(self,name,useBgs,logger):
        if name not in (dataTypes + additionalDataTypes + aggregationDataTypes):
            raise Exception,"unrecognized data type '%s'"%name
        
        if useBgs:
            self.selectedIndexes = [0,1,5,7]
        else:
            self.selectedIndexes = [0,1,3,7]

        self.name = name
        self.myLogger = logger

    def splitLine(self,line):
        return line.split('\t') # split by tabs

    def getTotal(self,extendedRecord):
        return 0

    # remove the constant zeros fields (good for session and view time)
    def minimizeRecord(self,extendedRecord):
        pass

    def splitToConstantSizeGroups(self,records,startTime,groupSize):
        recordsLength = len(records)
        groups = [records[i:i+groupSize] for i in xrange(0, (recordsLength-recordsLength%groupSize), groupSize)]
        return groups
        

    def splitToMonthlyGroups(self,records,startTime,groupSize):
        return self._splitToMonthlyGroupsCommon(records,startTime,groupSize,True)


    def _splitToMonthlyGroupsCommon(self,records,startTime,groupSize,strictStart):
        currentGroupStartTime = startTime
        timeObj    = datetime.datetime.utcfromtimestamp(currentGroupStartTime)
        monthToSet = (timeObj.month + groupSize - 1)%12 + 1
        yearToSet  = timeObj.year + ((timeObj.month + groupSize-1)/12)
        originalDay = timeObj.day
        dayToSet   = min(originalDay,calendar.monthrange(yearToSet,monthToSet)[1])# if you cannot set to the exact same day of the next month, take the maximal day possible.

        endDate = timeObj.replace(month = monthToSet, year = yearToSet, day = dayToSet,tzinfo=None)
        currentGroupEndTime = calendar.timegm(endDate.timetuple())
        
        groups = []
        currentGroup = []

        for record in records:
            recordTime = record[0]
            if currentGroupStartTime <= recordTime < currentGroupEndTime:
                currentGroup.append(record)
            else:
                # add last group
                #if self.__isGroupValid(currentGroup,strictStart,currentGroupStartTime):
                #    groups.append(currentGroup)
                if (currentGroup != []):

                    if strictStart: # if start time needs to conform to group - set the first recoed here (not in peak)
                        currentGroup[0][0] = currentGroupStartTime

                    groups.append(currentGroup)

                # start a new group
                while recordTime >= currentGroupEndTime :
                    # find the group start and end time
                    currentGroupStartTime = currentGroupEndTime
                    timeObj    = datetime.datetime.utcfromtimestamp(currentGroupStartTime)
                    monthToSet = (timeObj.month + groupSize - 1)%12 + 1
                    yearToSet  = timeObj.year + ((timeObj.month + groupSize-1)/12)
                    dayToSet   = min(originalDay,calendar.monthrange(yearToSet,monthToSet)[1])# if you cannot set to the exact same day of the next month, take the maximal day possible.
                    endDate = timeObj.replace(month = monthToSet, year = yearToSet, day = dayToSet,tzinfo=None)
                    currentGroupEndTime = calendar.timegm(endDate.timetuple())
                
                currentGroup = [record]

        # finally add the last group
        if (currentGroup != []):
            groups.append(currentGroup)

        return groups

    #def __isGroupValid (self,group,strictStart,startTime):
    #    return ((group != []) and (not strictStart or (group[0][0] == startTime)))

    def recordsToDictionaries (self,records,lables=None):
        # reform into dictionary format
        dictionaryLabels = None
        if lables == None: # by default use the dataType's Labels
            dictionaryLabels = self.outputDictionaryLabels
        else:
            dictionaryLabels = lables

        dictionaryRecords = []
        lablesLen = range(len(dictionaryLabels))

        for record in records:
            dictionaryRecord = {}
            for i in lablesLen:
                dictionaryRecord[dictionaryLabels[i]] = record[i]
        
            dictionaryRecords.append(dictionaryRecord)

        return dictionaryRecords


    def reformRawOverTimeRecords(self,rawRecords,overTimeRequest):
        reformedRecords = []
        
        for batch in rawRecords:
            
            # first, minimize every record i.e. drop unneeded fields
            for record in batch:
                self.minimizeRecord(record)
        
            # second, merge every X records of the same batch to form the necessary amount of points
            # (X is a function of the granularity)
            if overTimeRequest.granularityUnit == SECOND:
                ############################
                # trim first records till batch is aligned with start time of the request
                # then trim the last records to make sure all sub-groups are of the same size
                ############################
                while ((batch[0][0]-overTimeRequest.startTime)%overTimeRequest.granularity != 0):
                    batch.pop(0) #first record not aligned -> pop it
                reformedRecordsBatch = self.aggregateRecords(batch,overTimeRequest.startTime,overTimeRequest.groupSize,False)
            else:
                # TODO - consider alinment code here
                reformedRecordsBatch = self.aggregateRecords(batch,overTimeRequest.startTime,overTimeRequest.groupSize,True)
        
            # add records to grand list
            reformedRecords += reformedRecordsBatch
        
        
        # reform into dictionary format
        dictionaryRecords = self.recordsToDictionaries(reformedRecords)

        return dictionaryRecords

    # the method for uniting every groupSize records (sum the corresponding counters)
    def aggregateRecords(self,records,startTime,groupSize,aggregateMonthly):
        recordsGrouped = None

        if aggregateMonthly == True:
            recordsGrouped = self.splitToMonthlyGroups(records,startTime,groupSize)
        else:
            recordsGrouped = self.splitToConstantSizeGroups(records,startTime,groupSize)

        # aggregate each group and add the aggregated record to the final aggregatedRecords list
        aggregatedRecords = []
        for group in recordsGrouped:
            aggRecord = self.aggregateGroup(group)
            self.alterRecordData(aggRecord)
            aggregatedRecords.append(aggRecord)

        self.myLogger.debug("%s aggregated records where created" %len(aggregatedRecords))
        return aggregatedRecords

      
    # aggregation of several records in a group
    def aggregateGroup(self,group):
        numOfRecordsInGroup = len(group)
        sizeOfRecord = len(group[0])

        # start from an empty record [0,0,0,0,...]
        aggregatedRecord = [0] * sizeOfRecord

        # first record in the group determines the time of the aggregated record time
        aggregatedRecord[0] = group[0][0]

        for record in group:
            for i in xrange(1,sizeOfRecord):
                self.myLogger.debug4('adding record field %s to aggregated field %s'%(record[i],aggregatedRecord[i]))
                aggregatedRecord[i] += int(record[i])
                
        self.myLogger.debug4("aggregated record %s created" %aggregatedRecord)
        return aggregatedRecord

    def alterRecordData(self,record):
        pass


class SessionsDataType(GenericDataType):

    def __init__(self,useBgs,logger):
        GenericDataType.__init__(self,SESSIONS,useBgs,logger)

    def minimizeRecord(self,extendedRecord):
        recTime = tru.getTime(extendedRecord)
        totalSessions = tru.getTotalSessions(extendedRecord)
        cachableSessions = tru.getServableSessions(extendedRecord)
        delivedSessions = tru.getDeliveredSessions(extendedRecord)

        extendedRecord[:] = [recTime,totalSessions,cachableSessions,delivedSessions]


# This class is to be used by the hourlySubscriberDistibution function. 
# this data type is only defined in hour granularity (at least for now)
class ClientsDataType(GenericDataType):

    # static variable
    outputDictionaryLabels = [TIME,GENERIC_VALUE]

    def __init__ (self,logger):
        GenericDataType.__init__(self,CLIENTS,None,logger)
        self.selectedIndexes = [0,1]

    def minimizeRecord(self,extendedRecord):
        recTime = tru.getTime(extendedRecord)
        totalClients = tru.getClients(extendedRecord)
        
        extendedRecord[:] = [recTime,totalClients]

# ViewTime data type has different formatting with converting to seconds 
# unit, thus this subclass is granted to proveide the neccessary 
# functionality. note that this class is relevant to OT request only. 
# separate handling is needed in Top request.
#==========================================================================
class TimeDataType(GenericDataType):

    def __init__(self,useBgs,logger):
        GenericDataType.__init__(self,VIEW_TIME,useBgs,logger)
        

    def minimizeRecord(self,extendedRecord):
        recTime = tru.getTime(extendedRecord)
        totalSeconds = tru.getTotalSeconds(extendedRecord)
        cachableSeconds = tru.getServableSeconds(extendedRecord)
        deliveredSeconds = tru.getDeliveredSeconds(extendedRecord)

        extendedRecord[:] = [recTime,totalSeconds,cachableSeconds,deliveredSeconds]


    def alterRecordData(self,record):
        self.myLogger.debug("converting record %s from milliseconds to seconds"%record)
        for i in range(1,len(record)):
            record[i] = int(record[i]/1000) # convert from milliseconds to seconds

# Volume data type has different manipulation needs (conversion to BW and 
# different structure of raw records), thus this subclass is granted to 
# proveide the neccessary functionality.
#==========================================================================
class VolumeDataType(GenericDataType):
    
    def __init__(self,granularitySet,useBgs,logger):
        GenericDataType.__init__(self,VOLUME,useBgs,logger)
        self.granularitySet = granularitySet
        self.selectedIndexes = [0] + map(lambda x: x+2, self.selectedIndexes[1:]) # shift by 2
        

    def minimizeRecord(self,extendedRecord):
        recTime = tru.getTime(extendedRecord)
        totalL7Volume = tru.getTotalL7Volume(extendedRecord)
        cachableL7Volume = tru.getServableL7Volume(extendedRecord)
        deliveredL7Volume = tru.getDeliveredL7Volume(extendedRecord)

        extendedRecord[:] = [recTime,totalL7Volume,cachableL7Volume,deliveredL7Volume]

    # turn volume data to BW data in an aggregated record
    def volumeToBW(self,aggregatedRecord,groupSize,seconds=None):
        if seconds==None:
            seconds = self.granularitySet.granularity*groupSize
        for i in xrange(1,len(aggregatedRecord)):
            aggregatedRecord[i] = int((aggregatedRecord[i]/(float(seconds)))*8)
        self.myLogger.debug5("volume converted to BW to create aggregated record %s" % aggregatedRecord)
            
    # like ancestor, but also convert data to terms of BW
    def aggregateGroup(self,group):
        aggregatedRecord = GenericDataType.aggregateGroup(self,group)
        self.volumeToBW(aggregatedRecord,len(group))
        return aggregatedRecord

    #def alterRecordData(self,record):
    #    for i in range(1,len(record)):
    #        record[i] = int(record[i]*8) # convert from Bytes to bits (per second)


# L2Volume data type has different manipulation needs (conversion to BW and 
# different indexes are erquired from the raw records), thus this subclass
# is granted to proveide the neccessary functionality.
#==========================================================================
class L2VolumeDataType(VolumeDataType):

    # static variable
    outputDictionaryLabels = [TIME,TOTAL,VIDEO,VIDEO_DELIVERED]
    relevantLinePorts = [0,2]
    totalLineL2Getters = [tru.getLinedL2Port0InVolume,tru.getLinedL2Port1InVolume,tru.getLinedL2Port2InVolume,tru.getLinedL2Port3InVolume,tru.getLinedL2Port4InVolume,tru.getLinedL2Port5InVolume,tru.getLinedL2Port6InVolume,tru.getLinedL2Port7InVolume]
    videoLineL2Getters = [tru.getLinedL2Port0InVideoVolume,tru.getLinedL2Port1InVideoVolume,tru.getLinedL2Port2InVideoVolume,tru.getLinedL2Port3InVideoVolume,tru.getLinedL2Port4InVideoVolume,tru.getLinedL2Port5InVideoVolume,tru.getLinedL2Port6InVideoVolume,tru.getLinedL2Port7InVideoVolume]
    totalDeliveryL2Getters = [tru.getDeliveredL2Port0OutVolume,tru.getDeliveredL2Port1OutVolume]
    videoDeliveryL2Getters = [tru.getDeliveredL2Port0OutVideoVolume,tru.getDeliveredL2Port1OutVideoVolume]

    def __init__(self,granularitySet,useBgs,logger,addDelivryToTotal=True):
        VolumeDataType.__init__(self,granularitySet,useBgs,logger)
        #                    time,totalDelivery         ,totalLinePorts                         ,videoDelivery          ,videoLine
        self.selectedIndexes = [0,15] + map(lambda x:x+16,L2VolumeDataType.relevantLinePorts) + [21] + map(lambda x:x+22,L2VolumeDataType.relevantLinePorts)
        self.addDeliveryToTotal = addDelivryToTotal


    def getTotal (self,extendedRecord):
        return self._findTotalOnRelevantPorts(extendedRecord)

    def _findTotalOnRelevantPorts (self,extendedRecord):
        total = 0
        for portIndex in self.relevantLinePorts:
            total += self.totalLineL2Getters[portIndex](extendedRecord)
            
        if (self.addDeliveryToTotal == True): 
            for getter in self.totalDeliveryL2Getters:
                total += getter(extendedRecord)

        return total

    def _findVideoOnRelevantPorts (self,extendedRecord):
        lineVideo = 0
        for portIndex in self.relevantLinePorts:
            lineVideo += self.videoLineL2Getters[portIndex](extendedRecord)

        return lineVideo

    def minimizeRecord(self,extendedRecord):
        
        recTime = tru.getTime(extendedRecord)

        total = self._findTotalOnRelevantPorts(extendedRecord)
        lineVideo = self._findVideoOnRelevantPorts(extendedRecord)        

        deliveredVideo = 0
        for getter in self.videoDeliveryL2Getters:
            deliveredVideo += getter(extendedRecord)

        # set the values in the record
        extendedRecord[:] = [recTime,total,lineVideo+deliveredVideo,deliveredVideo]


# Peak data type has different manipulation needs (aggregation of records by 
# max and  different indexes are erquired from the raw records), thus this subclass
# is granted to proveide the neccessary functionality.
#==========================================================================
class PeakDataType(GenericDataType):

    theDataTypesIndexLegend = {SESSIONS:1,VIEW_TIME:2,VOLUME:3}

    def __init__ (self,dataType,peakCriteriaDataType,granularity,granularityUnit,logger):
        GenericDataType.__init__(self,PEAK,None,logger)
        secondsInHour = 3600
        if (granularityUnit == SECOND and granularity%secondsInHour != 0):
            raise Exception,"granularity (=%s) is not aligned with whole hour in overtime(aggregator=PEAK)"%granularity

        self.secondaryDataType = dataType
        self.dataTypeIndexInRecordLine = PeakDataType.theDataTypesIndexLegend[dataType.name]
        self.peakCriteriaDataType = peakCriteriaDataType
        self.peakCriteriaDataTypeIndexInRecordLine = PeakDataType.theDataTypesIndexLegend[peakCriteriaDataType.name]
        self.minimalCmplxRecordLength = max(self.dataTypeIndexInRecordLine,self.peakCriteriaDataTypeIndexInRecordLine)
        self.selectedIndexes = [0,1] + map(lambda i: i+2 ,dataType.selectedIndexes) # first two indexs are for the record time and the grade (peak criteria)

    def splitLine(self,line):
        complexRecord = line.split('|') # split by '|' to separate data types
        
        while ((len(complexRecord)-1) < self.minimalCmplxRecordLength):
            complexRecord.append('0')

        # take just the relevant data type section
        peakCriteriaRecordSection = [0] + complexRecord[self.peakCriteriaDataTypeIndexInRecordLine].strip().split('\t')
        peakGrade = self.peakCriteriaDataType.getTotal(peakCriteriaRecordSection)
        revisedRecord = complexRecord[0].strip().split('\t') + complexRecord[self.dataTypeIndexInRecordLine].strip().split('\t')
        revisedRecord[2] = peakGrade
        return revisedRecord


    def minimizeRecord(self,extendedRecord):
        recordTime = extendedRecord[0]
        peakTime   = extendedRecord[1]
        peakGrade  = extendedRecord[2]

        subRecord = [peakTime] + extendedRecord[3:] # identical in structure to a regular data type record
        self.secondaryDataType.minimizeRecord(subRecord)
        subRecord.append(peakGrade)
        extendedRecord[:] = subRecord


    def reformRawOverTimeRecords(self,rawRecords,overTimeRequest):
        reformedRecords = []

        # unite all batches
        unifiedRawRecords = []
        for batch in rawRecords:
            unifiedRawRecords += batch

        # minimize records
        for record in unifiedRawRecords:
            self.minimizeRecord(record)

        # aggregate record groups (create aggregated records)
        monthlyGrouping = (overTimeRequest.granularityUnit == MONTH)
        aggregatedRecords = self.aggregateRecords(unifiedRawRecords,overTimeRequest.startTime,overTimeRequest.groupSize,monthlyGrouping)

        # records (lists) to dictionaries
        dictionaryRecords = self.recordsToDictionaries(aggregatedRecords,self.secondaryDataType.outputDictionaryLabels)

        return dictionaryRecords


    def splitToConstantSizeGroups(self,records,startTime,groupSize):
        secondsInHour = 3600 # in peak reports interval is always hourly
        betweenGroupsInterval = secondsInHour*groupSize
        currentGroupStartTime = startTime
        currentGroupEndTime = currentGroupStartTime + betweenGroupsInterval
        groups = []
        currentGroup = []
        for record in records:
            recordTime = record[0]
            if currentGroupStartTime <= recordTime < currentGroupEndTime:
                currentGroup.append(record)
                self.myLogger.debug4("adding record %s to group %s"%(record,currentGroup))
            else:
                # add last group
                if currentGroup!=[]:
                    groups.append(currentGroup)
                    self.myLogger.debug3("adding the record group %s"%groups)
                
                # start a new group
                currentGroupStartTime = ((recordTime-startTime)/betweenGroupsInterval)*betweenGroupsInterval+startTime # flooring the recordTime to it's group startTime
                currentGroupEndTime = currentGroupStartTime + betweenGroupsInterval
                currentGroup = [record]

        # finally add the last group
        if currentGroup != []:
            groups.append(currentGroup)

        return groups


    def splitToMonthlyGroups(self,records,startTime,groupSize):
        return self._splitToMonthlyGroupsCommon(records,startTime,groupSize,False)


    def aggregateGroup(self,group):
        # agrregation is finding the max grade - which is the last field (defined in minimize record of this class)
        self.myLogger.debug3("about to aggregate group %s"%group)
        peakRecord = max(group,key=lambda rec:int(rec[-1]))
        
        # intify all fields
        peakRecord = map(int,peakRecord)

        # in Volume and L2Volume - do the BW conversion
        if self.secondaryDataType.name == VOLUME:
            self.secondaryDataType.volumeToBW(peakRecord,1,60) # in peak the data always reffers to a single peak minute - thus convert with devision by 60 

        self.myLogger.debug3("the peak record is %s"%peakRecord)

        return peakRecord

    def alterRecordData(self,record):
        record.pop() # remove last field (peak grade)
        self.secondaryDataType.alterRecordData(record)

# This class represent an over-time request
class OverTimeRequest:
    
    def __init__ (self,reportsProcessor,startTime,endTime,granularity,granularityUnit,dataTypeName,logger,aggregator,useBGS,addDeliveryToTotal,loose):

        # time shift comming from above (configuration)
        startTime += reportsProcessor.myTimeShift
        endTime   += reportsProcessor.myTimeShift

        self.endTime = reportsProcessor.alignEndTimeToReportsEnd(endTime)
        self.granularityUnit = granularityUnit

        if (granularityUnit == MONTH): # granularity pronounced in months
            self.granularitySet = HOUR # there is no day granularity for peak, only hour
            self.granularity = granularity
            self.groupSize = granularity

        else: # granularity pronounced in seconds - thus minute is the finest granularity
            self.granularity = max(granularity,MINUTE.granularity)

            # granularity set
            if (self.granularity < HOUR.granularity):
                self.granularitySet = MINUTE
            else:
                self.granularitySet = HOUR

            self.groupSize = granularity/self.granularitySet.granularity
            self.granularity = self.granularitySet.granularity * self.groupSize

        if (self.groupSize < 1):
            logger.error("group size is less then 1!")


        # set the start time
        baseGranularity = self.granularitySet.granularity
        self.startTime = (startTime+baseGranularity-1)/baseGranularity*baseGranularity
        

        if (loose == False): # strict mode -> throw an exception if needed
            # if the interval is not in terms of whole minutes,hours,days corespondingly to the selected granularitySet -> FAIL
            if (granularityUnit==SECOND and ((granularity==0) or (granularity!=self.granularity))):
                logger.error("in strict mode, a %s interval is not aligned with %s units"%(granularity,self.granularitySet.name))
                raise ValueError,"in strict mode, a %s interval is not aligned with %s units"%(granularity,self.granularitySet.name)

            if self.startTime != startTime:
                logger.error("in strict mode, startTime %s is not aligned with %s units"%(startTime,self.granularitySet.name))
                raise ValueError,"in strict mode, startTime %s is not aligned with %s units"%(startTime,self.granularitySet.name)

        
        # data type factory
        if dataTypeName == VOLUME:
            self.dataType = VolumeDataType(self.granularitySet,useBGS,logger)
        elif dataTypeName == VIEW_TIME:
            self.dataType = TimeDataType(useBGS,logger)
        elif dataTypeName == L2_BW:
            self.dataType = L2VolumeDataType(self.granularitySet,useBGS,logger,addDeliveryToTotal)
        elif dataTypeName == CLIENTS:
            self.dataType = ClientsDataType(logger)
        elif dataTypeName == SESSIONS:
            self.dataType = SessionsDataType(useBGS,logger)
        else:
            self.dataType = GenericDataType(dataTypeName,useBGS,logger)

        logger.debug('request: start=%s , end=%s , dataType=%s , granularity=%s%s ,granularitySet=%s, useBGS=%s, loose=%s, aggregator = %s'%\
                     (self.startTime,self.endTime,self.dataType.name,self.granularity,self.granularityUnit,self.granularitySet.name,useBGS,loose,aggregator))

        if aggregator == MAX:
            self.secondaryDataType = self.dataType
            self.peakCriteriaDataType = L2VolumeDataType(self.granularitySet,useBGS,logger,addDeliveryToTotal)
            self.dataType = PeakDataType(self.secondaryDataType,self.peakCriteriaDataType,self.granularity,self.granularityUnit,logger)
        
        
class TopperRequest:

    #CTOR
    def __init__(self,startTime,endTime,category,dataTypeName,cnt,logger):
        self.startTime    = startTime
        self.endTime      = endTime
        
        if category not in topCategories:
            raise Exception,"unrecognized category '%s'"%category
        self.category     = category
        if category == TITLES:
            self.lineLegend = TitleTopperReportLine()
        else:
            self.lineLegend = TopperReportLine()

        if dataTypeName not in dataTypes:
            raise Exception,"unrecognized data type '%s'"%dataTypeName
        self.dataTypeName = dataTypeName

        self.cnt = cnt


class TopperReportLineElement:
    #CTOR
    def __init__(self,indexInLine,indexInResponse,defaultVal,aggFunction):

        self.myLineIndex        = indexInLine
        self.myResponseIndex    = indexInResponse
        self.myDefaultVal       = defaultVal
        self.myAggFunction      = aggFunction

class TopperReportLine:

    def __init__(self):

        add = lambda metricRecElem,lineElem :metricRecElem+int(lineElem)
        self.myLineElements = []
        self.myLineElements.append(TopperReportLineElement(2,0,0,add)) # total
        self.myLineElements.append(TopperReportLineElement(3,1,0,add)) # cachable
        self.myLineElements.append(TopperReportLineElement(4,2,0,add)) # delivered


    def padLineArrayWithDefaults(self,lineArr):
        lineLen = len(lineArr)
        diff = self.myLineElements[-1].myLineIndex - (lineLen-1) # diff between line array and topper metric record

        i=0
        while (diff>0):
            defaultVal = self.myLineElements[lineLen+i].myDefaultVal
            lineArr.append(defaultVal)
            i += 1
            diff -= 1

    def addLineToDataArray(self,lineArr,dataArr):
        lineLen = len(lineArr)
        i = 0

        for lineElem in self.myLineElements:
            if lineLen<=lineElem.myLineIndex: #update only if the linelen allows it
                break
            dataVal = dataArr[lineElem.myResponseIndex]
            lineVal = lineArr[lineElem.myLineIndex]
            newVal = lineElem.myAggFunction(dataVal,lineVal)
            dataArr[lineElem.myResponseIndex] = newVal
            

    def createDefaultDataArray(self):
        data = []
        for lineElem in self.myLineElements:
            data.append(lineElem.myDefaultVal)

        return data

class TitleTopperReportLine(TopperReportLine):
    
    def __init__(self):
        TopperReportLine.__init__(self)

        unknown = "unknown"
        replaceOnlyUnknown = (lambda metricRecElem,lineElem: metricRecElem==unknown and lineElem or metricRecElem)
        add = lambda metricRecElem,lineElem :metricRecElem+int(lineElem)

        self.myLineElements.append(TopperReportLineElement(5,3,unknown,replaceOnlyUnknown))# siteId
        self.myLineElements.append(TopperReportLineElement(8,4,0,add))# bytes
        self.myLineElements.append(TopperReportLineElement(9,5,0,add))# seconds
        self.myLineElements.append(TopperReportLineElement(10,6,0,add))# sessions


class TopperTimeWindow:
    
    #CTOR
    def __init__(self,name,fileNameFormat,timeRangeFunc):

        self.name           = name
        self.fileNameFormat = fileNameFormat
        self.timeRange      = timeRangeFunc
        self.files          = []


    
topperTimeWindows = [TopperTimeWindow("yearly","%Y.tsv",lambda year,month: (calendar.isleap(year)+365)*86400), # days_in_year*60*60*24
                     TopperTimeWindow("monthly","%Y%m.tsv",lambda year,month: calendar.monthrange(year,month)[1]*86400),# days_in_month*60*60*24
                     TopperTimeWindow("weekly","%Y%m%d.tsv",lambda year,month: 604800),# 60*60*24*7
                     TopperTimeWindow("daily","%Y%m%d.tsv",lambda year,month: 86400),  # 60*60*24
                     TopperTimeWindow("hourly","%Y%m%d-%H.tsv",lambda year,month: 3600)]   # 60*60


# This class represents a distribution bucket that needs to accumulate records 
# data that belong to same ditribution group (e.g. an hour of the day in the hourly distribution case)
class DistributionBucket:

    # CTOR
    def __init__ (self,logger,*tags):
        self.myNumOfDropsInBucket = 0
        self.myLogger             = logger
        self.mySum                = {}
        self.myTagsSet = set(tags)

        for tag in tags:
            self.mySum[tag] = 0

    def addDropToBucket (self,drop):
        if set(drop.keys()) != self.myTagsSet:
            self.myLogger.error("record's tags (%s) mismatch ditribution bucket's tags %s - dropping record!"%(drop.keys(),self.myTagsSet))
            return False

        for k,v in drop.items():
            self.mySum[k] += v

        self.myNumOfDropsInBucket += 1
        return True

    def getAverage (self):
        curSum = {}
        if (self.myNumOfDropsInBucket > 0):
            for k,v in self.mySum.items():
                curSum[k] = v/self.myNumOfDropsInBucket

        else:
            curSum = self.mySum

        return curSum
        

# This class is used originally for the hourly distribution functions of the ReportsProcessor class
# it holds buckets of distrbuting that are objects of DistributionBucket class. each of these objects
# is requested to accumulate the values in the addRecord() function, and produce the distribution 
# average in the getAverageDistribution() function
class Grouper:

    # CTOR
    def __init__ (self,betweenBucketsInterval,numOfBuckets,logger,groupingTag,*valueTags):
        self.myWholeCycle             = numOfBuckets*betweenBucketsInterval
        self.myBetweenBucketsInterval = betweenBucketsInterval
        self.myGroupingTag            = groupingTag
        self.myValueTags              = valueTags
        self.myBuckets                = []
        self.myLogger                 = logger

        for i in range(numOfBuckets):
            self.myBuckets.append(DistributionBucket(logger,*valueTags))

    def addRecords(self,records):
        for record in records:
            recTime = record.pop(TIME)
            bucketIndex = (recTime%self.myWholeCycle)/self.myBetweenBucketsInterval
            if (self.myBuckets[bucketIndex].addDropToBucket(record)==True):
                self.myLogger.debug2("record %s was added to bucket %s"%(record,bucketIndex))
            else:
                self.myLogger.debug2("failed to add record %s to bucket %s"%(record,bucketIndex))


    def getAverageDistribution(self):
        distribution = []
        bucketIndex   = 0
        for bucket in self.myBuckets:
            bucketAverage = bucket.getAverage()
            bucketAverage[self.myGroupingTag]=bucketIndex
            distribution.append(bucketAverage)
            self.myLogger.debug("added bucket %s to distribution"%bucketAverage)
            bucketIndex += 1

        return distribution



class ReportsProcessor:

    # CTOR
    def __init__(self, reportsRoot, parameters, logger):

        self.myReportsRoot      = reportsRoot
        self.myLogger           = logger
        self.myParameters       = parameters
        self.myObfuscateSubscriberIp = parameters.getBooleanParameter("obfuscate-subscriber-ip",False)
        self.myAddDeliveryToTotal = True # once was user param. since 2.6 constant.
        self.myRelevantLinePorts = sorted(parameters.getIntListParameter("relevant-line-ports",[0,2]))
        self.myTimeShift        = parameters.getIntParameter("time-shift",0)*86400 # time shift is given in days
        self.myOTRequest        = None
        self.myTopperRequest    = None

        
    def updateRelevantLinePorts(self):
        for port in self.myRelevantLinePorts:
            if not (0 <= port <= 7):
                self.myLogger.warning("bad configuration for line ports %s, out of range port %s, using defaults"% (self.myRelevantLinePorts,port))
                self.myRelevantLinePorts = [0,2] # use defaults
                break
        s = set(self.myRelevantLinePorts)
        if (len(s) != len(self.myRelevantLinePorts)):
            self.myLogger.warning("bad configuration for line ports %s, duplicates were found"% self.myRelevantLinePorts)
            self.myRelevantLinePorts = sorted(list(s))

        # update L2VolumeDataType static member
        L2VolumeDataType.relevantLinePorts = self.myRelevantLinePorts

    # construct the path where relevant files for the current over-time request are located (over time reports)
    def getSuitableOverTimeReportsDir(self):
        return os.path.join(self.myReportsRoot,OVER_TIME,self.myOTRequest.granularitySet.name,self.myOTRequest.dataType.name)

    def getSuitableOverTimeLastHourFile(self,dataType):
        global LAST
        return os.path.join(self.myReportsRoot,OVER_TIME,LAST.name,dataType,LAST.fileNameFormat)

    # must align end time becase topper sometimes shows
    def alignEndTimeToReportsEnd (self,endTime):
        fileStartTime,fileEndTime,file = self.getLastHourTimeFrame()
        endTime = min(endTime,fileEndTime)
        self.myLogger.debug("end time is %s"%endTime)
        return endTime

                                                            # the next two cases demonstrate overlapping
    # returns true if two time sections, described by       #                               
    # start and end points, overlap                         #       |-------|               
    def isOverlappingTime(self,start1,end1,start2,end2):    #           |-------|           
        # two lines overlap iff:                            #                               
        return ((start1 < end2) and (start2 < end1))        #   |------|                    
                                                            #    |----|                     
         
    def findRelevantFilesByTime(self,directory,fileNameFormat,rangeFunc,startTime,endTime):
        allFiles = safeListDir(directory,self.myLogger)
        relevantFiles = {}
        for file in allFiles:
            try:
                # obtain the start time of the file (or at least try to)
                timeObj = time.strptime(file,fileNameFormat)
                year = timeObj.tm_year
                month = timeObj.tm_mon
                fileStartTime = calendar.timegm(timeObj) # epoch time
                fileEndTime = fileStartTime + rangeFunc(year,month) # epoch time
                self.myLogger.debug4("trying to analyze file '%s' startTime=%s, endTime=%s" %(file,fileStartTime,fileEndTime))
                if self.isOverlappingTime(fileStartTime,fileEndTime,startTime,endTime):
                    self.myLogger.debug2("adding relevant file '%s'" %file)
                    relevantFiles[fileStartTime] = os.path.join(directory,file)

            except ValueError:
                self.myLogger.debug4("failed analyzing file '%s'" %file)
                continue

        return relevantFiles


    def getRelevantOverTimeFiles(self,reportsDir):

        # first part is an ugly patch to change the request's end time to minus 5 minutes 
        # if it reaches to the end of the reports where there is a knee
        #fileStartTime,fileEndTime,file = self.getLastHourTimeFrame()
        #self.myOTRequest.endTime = min(self.myOTRequest.endTime,fileEndTime-300)
        # end of ugly patch

        granularitySet = self.myOTRequest.granularitySet
        relevantFiles = self.findRelevantFilesByTime(reportsDir,granularitySet.fileNameFormat,granularitySet.rangeOfFile,self.myOTRequest.startTime,self.myOTRequest.endTime)
        
        lastFile=None
        # if the last hour file "hour.tsv" is relevant include it as well
        # first, is it even relevant to this granularity set
        if granularitySet.mayUseLastDir == True:
            fileStartTime,fileEndTime,file = self.getLastHourTimeFrame(self.myOTRequest.dataType.name)
            if self.isOverlappingTime(fileStartTime,fileEndTime,self.myOTRequest.startTime,self.myOTRequest.endTime):
                self.myLogger.debug2("adding relevant file of last hour")
                global LAST_NAME
                lastFile = file # string is always sorted after int, thus this file wiil be last

        # now, sort the the files by start time
        relevantFileAsSortedTuples = sorted(relevantFiles.items())
        self.myLogger.debug("relevant files are %s" %relevantFiles.values())
        relevantFileSorted = map(lambda pair:pair[1],relevantFileAsSortedTuples)
        if lastFile != None:
            relevantFileSorted.append(lastFile)

        return relevantFileSorted

      
    # extracts the records from the files (each line is a record) to lists of records
    # first element is converted to epoch time format, constant zero fields are removed:
    # 
    # example:
    # 2011-07-10-00:00  1584  0  392  0  980 ==> [1310169600,1584,392,980] 
    #
    # the output is a list of lists of records. each list of records is the maximal 
    # consecutive list of records, made of as many files as possible
    def getRelevantOverTimeRecordsFromFiles(self,relevantFiles,reportsDir):
        allFilesRecords = []
        normalDiffBetweenFiles = self.myOTRequest.granularitySet.granularity

        # for each file insert the relevant records to a list (fileRecords)
        # later try to combine all small lists to a master list (doable only
        # if there is a normal difference between two files (last and first records))
        for file in relevantFiles:
            fd = openFileForRead(file,self.myLogger)
            if (fd != None):
                fileRecords = []
                for line in fd.readlines():
                    record = self.myOTRequest.dataType.splitLine(line.strip())
                    recordTimeFormatStr = self.myOTRequest.granularitySet.recordTimeFormat
                    recordTimeObj = time.strptime(record[0],recordTimeFormatStr)
                    recordStartTime = int(calendar.timegm(recordTimeObj))
                    recordEndTime = recordStartTime + self.myOTRequest.granularitySet.granularity
                    record[0] = recordStartTime # swap original time string for epoch time
    
                    if (recordStartTime >= self.myOTRequest.startTime) and (recordEndTime <= self.myOTRequest.endTime):
                        # found a relevant record add it to file's records
                        self.myLogger.debug5("raw record %s found in requested time range" % record)
                        fileRecords.append(record)
                    else:
                        self.myLogger.debug5("raw record %s outside the requested time range" % record)
                        
                     
                fd.close()
            # time for combining elements. check if the last batch is a continuence of the one before it.
            # if it is combine the two batches, otherwise close the previouse batch and add the last one 
            # as a new sequence
            if len(fileRecords)==0: 
                # if no relevant records where found skip this file in combining
                continue

            if len(allFilesRecords)>0 and (fileRecords[0][0] - allFilesRecords[-1][-1][0] <= normalDiffBetweenFiles):
                sliceOutCnt = 0

                # the next loop is to prevent duplicates that my come from joining the 'last' file
                while (sliceOutCnt<len(fileRecords)) and (len(allFilesRecords[-1])>0) and (fileRecords[0][0] - allFilesRecords[-1][-1][0] < normalDiffBetweenFiles):
                    sliceOutCnt += 1
                    allFilesRecords[-1].pop() # remove redundent records from previous batch (to be replaced by new records from more updated records)

                if sliceOutCnt>0:
                    self.myLogger.debug("%s records were sliced out prior to addend file '%s' to the batch" %(sliceOutCnt,file))

                allFilesRecords[-1] +=fileRecords
                self.myLogger.debug("file '%s' was joind with the previous file" %file)

            else:
                allFilesRecords.append(fileRecords)
                self.myLogger.debug("file '%s' began a new sequence of records" %file)

            self.myLogger.debug("file '%s' supplied %s records" % (file, len(fileRecords)))

        return allFilesRecords


    def unshiftRecordTime (self,dictionaryRecords):
        global TIME

        if (self.myTimeShift != 0):
            for record in dictionaryRecords:
                record[TIME] -= self.myTimeShift


    # perform some cleaning on records: 
    # * remove unneeded fields
    # * merge records if needed (depending on granularity and data-type)
    # * desegregate batches to one continues batch
    def reformRawOverTimeRecords(self,rawRecords):

        dictionaryRecords = self.myOTRequest.dataType.reformRawOverTimeRecords(rawRecords,self.myOTRequest)

        # regradless of data type, handle artificial time shift if needed
        self.unshiftRecordTime(dictionaryRecords)

        return dictionaryRecords


    def overTimeCommon(self,startTime,endTime,granularity,granularityUnit,dataTypeName,aggregator,useBGS,addDeliveryToTotal,loose):
        
        # we need the relevant line ports if this request involves the L@ data type or this is a peak request (peak criteria is L2 bytes)
        if ((aggregator == MAX) or (dataTypeName == L2_BW)):
            self.updateRelevantLinePorts()

        self.myOTRequest = OverTimeRequest(self,startTime,endTime,granularity,granularityUnit,dataTypeName,self.myLogger,aggregator,useBGS,addDeliveryToTotal,loose)
        
        reportsDir     = self.getSuitableOverTimeReportsDir()

        relevantFiles  = self.getRelevantOverTimeFiles(reportsDir)

        rawRecords     = self.getRelevantOverTimeRecordsFromFiles(relevantFiles,reportsDir)

        records        = self.reformRawOverTimeRecords(rawRecords)

        return records


    def overTime (self,startTime,endTime,granularity,granularityUnit,dataTypeName,aggregator=None,useBGS=False,loose=False):
        if dataTypeName in dataTypes:
            return self.overTimeCommon(startTime,endTime,granularity,granularityUnit,dataTypeName,aggregator,useBGS,None,loose)
        else:
            raise Exception,"unsupported data type '%s for overTime() function'"%dataTypeName

    def l2BWOverTime (self,startTime,endTime,granularity,granularityUnit,aggregator=None,loose=False):
        return self.overTimeCommon(startTime,endTime,granularity,granularityUnit,L2_BW,aggregator,None,self.myAddDeliveryToTotal,loose)

    ### call for bitrate overtime requests ###
    def bitrateOverTime (self, dataSubType, siteList, startTime, endTime, granularity, granularityUnit, loose=False):

        ### everything must be at least aligned to 5 minutes ###
        fiveMinutes = 60 * 5
        #if startTime % fiveMinutes != 0 or endTime % fiveMinutes != 0:
        #    raise Exception,"bitrate overtime request MUST be aligned to 5 minutes"

        alignedStartTime = (((startTime +fiveMinutes - 1) / fiveMinutes) * fiveMinutes)
        alignedEndTime = ((endTime / fiveMinutes) * fiveMinutes)

        if granularityUnit != MONTH:
            alignedGranularity = ((granularity / fiveMinutes) * fiveMinutes)

        if loose == True:
            startTime = alignedStartTime
            endTIme = alignedEndTime
            granularity = alignedGranularity
        else:
            if startTime != alignedStartTime:
                self.myLogger("unaligned startTime param in bitrateOverTime request with strict mode, discarding request!")
                return []
            if endTime != alignedEndTime:
                self.myLogger("unaligned endTime param in bitrateOverTime request with strict mode, discarding request!")
                return []
            if granularity != alignedGranularity:
                self.myLogger("unaligned granularity param in bitrateOverTime request with strict mode, discarding request!")
                return []

        ### don't align start time ###
        # ### offset startTime by interval ###
        # #startTime = (startTime/granularity)*granularity

        ### aggregate reports to requested range & interval units ###
        topperReportDatabaseReader = bitrate_report.TopperBitrateReportDatabaseReader(os.path.join(self.myReportsRoot,bitrate_report.BITRATE_REPORT_DIR_NAME), self.myLogger)

        units = []
        unitClassConstructor = None
        if dataSubType == BITRATE__SESSIONS:
            unitClassConstructor = bitrate_report.SessionSiteUnit
            units = topperReportDatabaseReader.getSessionOvertimeFromReports(startTime,endTime,granularity, granularityUnit)
        else:
            unitClassConstructor = bitrate_report.TransactionSiteUnit
            units = topperReportDatabaseReader.getTransactionOvertimeFromReports(startTime,endTime,granularity, granularityUnit)

        siteListArr = siteList.split(",")

        ### filter sites ###
        for unit in units:
            filterList = []
            for site in unit.siteDict:
                if site not in siteListArr:
                    filterList.append(site)

            for site in filterList:
                del unit.siteDict[site]

            ### fill empty gaps ###
            for site in siteListArr:
                if site not in unit.siteDict:
                    unit.siteDict[site] = unitClassConstructor()

        return units




    def getRelevantTopperFiles(self):
        
        category = self.myTopperRequest.category
        dataType = self.myTopperRequest.dataTypeName

        # set the proper topper window directory
        for timeWindow in topperTimeWindows:

            # clear timeWindow.files before filling since we are on a new request
            timeWindow.files = []

            curDir = os.path.join(self.myReportsRoot,TOPPER,category,timeWindow.name,dataType)
            if os.path.exists(curDir):
                self.myLogger.debug("the directory '%s' is a potential topper directories"%curDir)

                for file in safeListDir(curDir,self.myLogger):
                    try:
                        timeObj = time.strptime(file,timeWindow.fileNameFormat)
                        year = timeObj.tm_year
                        month = timeObj.tm_mon
                        fileStartTime = calendar.timegm(timeObj) # epoch time
                        fileEndTime = fileStartTime + timeWindow.timeRange(year,month) # epoch time
                        fileTuple = (fileStartTime,fileEndTime,os.path.join(curDir,file))
                        timeWindow.files.append(fileTuple)
                        self.myLogger.debug4("added file tuple %s to time window '%s'" %(fileTuple,timeWindow.name))

                    except ValueError:
                        self.myLogger.debug4("failed analyzing file '%s'" %file)
                        continue
                
                # sort the files by start time
                timeWindow.files = sorted(timeWindow.files)
                         
            else:
                self.myLogger.debug("the directory '%s' does not exist, time-window %s will not be inspected"%(curDir,timeWindow.name))

        # the next part is the process of finding the relevant files for the topper request
        #t1 = calendar.timegm(time.gmtime(self.myTopperRequest.startTime))
        t1 = self.myTopperRequest.startTime
        t2 = self.myTopperRequest.endTime

        skipAnHour = False
        
        minimalDiff = 3600 # there are no topper files of less then one hour, thus we cannot request less than an hour's difference

        relevantFiles = []
        i=0
        while ((t2-t1) >= minimalDiff):
            if skipAnHour:
                t1 += 3600
                self.myLogger.debug2("skipping an hour to t1=%s" %t1)
                skipAnHour = False
            else:
                skipAnHour = True #until you porove you are worthy of not skipping hours, you are skipping an hour!
                for timeWindow in topperTimeWindows:
                    files = timeWindow.files
                    for file in files:
                        x1 = file[0]
                        x2 = file[1]
                        if ((x1 >= t1) and (x1 < t1+minimalDiff) and (x2 <= t2 )):
                            relevantFiles.append(file[2]) # file[2] = the file's path
                            self.myLogger.debug3("added file '%s' to the relevant files list" % file[2])
                            self.myLogger.debug3("topper request start time updated from %s to %s" %(t1,x2))
                            t1 = x2
                            # some progress was made thus carry on collecting files without skipping hours
                            #(you have proven yourself to be worthy of not skipping)
                            skipAnHour = False 
                            break
                    # if you are here because you found a piece of the puzzle break to the outer loop and 
                    # look for another piece, otherwise you have exausted this time window's files so 
                    # move on to the next time window
                    if skipAnHour == False :
                        break

        # if no files were collected, as a last resort check the last directory.
        # but the request time frame must overlap the 'hour.tsv' file time frame 
        # (note that this is a weaker criteria from what we used for other 
        # files- overlap is easier to achive than complete containment)
        if relevantFiles == []:
            start,end,OTfile = self.getLastHourTimeFrame()
            t1 = self.myTopperRequest.startTime
            t2 = self.myTopperRequest.endTime
            if self.isOverlappingTime(start,end,t1,t2):
                TopLastFile = os.path.join(self.myReportsRoot,TOPPER,category,LAST_NAME,dataType,LAST_HOUR_FILE_NAME)
                relevantFiles.append(TopLastFile)
                self.myLogger.debug3("finally, added file '%s' to the relevant files list" % TopLastFile)

            else: # no overlap with last hour - final attempt aline to round hour -> this is a patch
                if (3600 <= (t2-t1) < 7200) :
                    remainder = t1 % 3600
                    if ((remainder) < 1800):
                        t1 = t1 - remainder # round down
                    else:
                        t1 = t1 + 3600 - remainder # round up
                    
                    hourlyTimeWindow = topperTimeWindows[-1]
                    if hourlyTimeWindow.name == "hourly": # making sure it wasn't eliminated in previous stages
                        for file in hourlyTimeWindow.files:
                            if file[0]==t1:
                                relevantFiles.append(file[2]) # file[2] = the file's path
                                self.myLogger.debug3("finally, after times adjustment (%s->%s), added file '%s' to the relevant files list" % (self.myTopperRequest.startTime,t1,file[2]))
                                break

        return relevantFiles


    def getLastHourTimeFrame(self,dataType=VIEW_TIME):
        global LAST
        file = self.getSuitableOverTimeLastHourFile(dataType)
        fd = openFileForRead(file,self.myLogger)
        if (fd == None):
            return -1,-1,None

        line = fd.readline()
        record = line.strip().split('\t')
        recordTimeObj = time.strptime(record[0],LAST.recordTimeFormat)
        fileStartTime = int(calendar.timegm(recordTimeObj))
        fileEndTime = fileStartTime + LAST.rangeOfFile
        fd.close()
        return fileStartTime,fileEndTime,file
        
    
    def insertOrUpdate(self,id,values,dict):
        if id in dict:
            self.myLogger.debug4('the record %s is already in the dictionary for top request, updating'%id)
            for i in range(len(values)) :
                dict[id][i] += values[i]
        else:
            self.myLogger.debug4('the record %s wasn\'t in the dictionary for top request, adding'%id)
            dict[id] = values

    def padWithZeros(self,sizeLimit,array):
        while len(array)<sizeLimit:
            array.append(0)


    def fileToDictionary(self,file,dictionary):
        fd = openFileForRead(file,self.myLogger)
        if (fd != None):

            sawTotal = False # to indicate if we saw a total or not (if we didn't see we'll 
                             # use the best aproximation derived from the records in the file)
            totalAproximation = 0
            totalCachableApproximation = 0
            totalDeliveredApproximation = 0

            for line in fd.readlines():
                record = line.strip().split('\t') # strip is for removing trailing sapces and such
                id = record[0]
                
                if (id==TOTAL_ID):
                    # the TOTAL record
                    values = map(int,record[2:])
                    self.insertOrUpdate(id,values,dictionary)
                    sawTotal = True

                else: # normal key (not TOTAL_ID)
                    data = None
                    if id not in dictionary:
                        data = self.myTopperRequest.lineLegend.createDefaultDataArray()
                        dictionary[id] = data
                    else:
                        data = dictionary[id]
                        
                    
                    self.myTopperRequest.lineLegend.addLineToDataArray(record,data)

                # maintain Total approximation
                if (len(record)>4):
                    totalAproximation += int(record[2])
                    totalCachableApproximation += int(record[3])
                    totalDeliveredApproximation += int(record[4])

            if sawTotal==False:
                # the 'TOTAL' record was not seen -> use approximation
                self.myLogger.debug2("The TOTAL record was not seen in file %s using approximation obtained from file's records" %file)
                values = [totalAproximation,totalCachableApproximation,totalDeliveredApproximation]
                self.insertOrUpdate(TOTAL_ID,values,dictionary)

            fd.close()

        else:
            self.myLogger.error("faild analyzing file '%s' for top response"%file)


    def sumTopperFiles(self,files):
        totalTop = {}

        # first thing first - insert the initialized TOTAL record
        self.insertOrUpdate(TOTAL_ID,[0,0,0],totalTop)

        # now iterate the files
        for file in files:
            self.fileToDictionary(file,totalTop)

        # sort by value
        totalRec = totalTop.pop(TOTAL_ID)
        sortedListOfTuples = [(TOTAL_ID,totalRec)]+sorted(totalTop.items(), key=lambda x: x[1][0], reverse=True)

        # this would be the place to cut as many records as you want from the topper report
        topNList = sortedListOfTuples[:self.myTopperRequest.cnt+1] # the +1 is for the TOTAL record (should always be first)

        indexesToAlter = []
        if self.myTopperRequest.dataTypeName == VIEW_TIME:
            indexesToAlter += [0,1,2] # total, cachable, delivered (view time)
        if self.myTopperRequest.category == TITLES:
            indexesToAlter += [5] # total view time
        
        for i in indexesToAlter :
            for record in topNList:
                self.myLogger.debug('converting record %s from msec to sec', record)
                if len(record[1])>i:
                    record[1][i] = record[1][i]/1000 # convert from milliseconds to seconds

        return topNList


    def topperRecordsToDictionary(self,records):
        
        dictionaryRecords = []

        for rec in records:
            dicRec = {KEY:rec[0],TOTAL:rec[1][0],CACHABLE:rec[1][1],DELIVERED:rec[1][2]}
            if (rec[0]!=TOTAL_ID):

                # obfuscate ips if needed
                if (self.myObfuscateSubscriberIp and (self.myTopperRequest.category == CLIENTS)):
                    dicRec[KEY] = base64.b64encode(hashlib.sha1(dicRec[KEY]).digest())

                elif (self.myTopperRequest.category == TITLES):
                    dicRec[SITE_ID] = rec[1][3]
                    dicRec[VOLUME] = rec[1][4]
                    dicRec[VIEW_TIME] = rec[1][5]
                    dicRec[SESSIONS] = rec[1][6]
    
                    if dicRec[self.myTopperRequest.dataTypeName]!=rec[1][0]:
                        # if there was old format - new format mix, there might be uncorresponding values, fix what you can
                        self.myLogger.debug2("uncorresponding values in top record %s - using zeros"%dicRec)
                        dicRec[VOLUME] = 0
                        dicRec[VIEW_TIME] = 0
                        dicRec[SESSIONS] = 0

            dictionaryRecords.append(dicRec)


        finalDictionary = {}
        if ((len(dictionaryRecords)>0) and (dictionaryRecords[0][KEY] == TOTAL_ID)):
            # TOTAL was found - we should always pass thrugh this 'if'
            dictionaryRecords[0].pop(KEY)
            finalDictionary = {GRAND_TOTAL:dictionaryRecords[0],ENTRIES:dictionaryRecords[1:]}

        else:
            self.myLogger.error("expected a TOTAL record, but didn't find one in %s"%records)
            finalDictionary = {GRAND_TOTAL:{TOTAL:0,CACHABLE:0,DELIVERED:0},ENTRIES:[]}

        return finalDictionary


    def top(self,startTime,endTime,category,dataTypeName,cnt):

        self.myTopperRequest = TopperRequest(startTime,endTime,category,dataTypeName,cnt,self.myLogger)

        relevantFiles = self.getRelevantTopperFiles()

        topRecords = self.sumTopperFiles(relevantFiles)

        return self.topperRecordsToDictionary(topRecords)


    def getAllRecentTitlesFromFile(self):

        pathToRecentFile = os.path.join(self.myReportsRoot,RECENT,TITLES_TSV)
        recentTitles = []

        if os.path.exists(pathToRecentFile):
            fd = open(pathToRecentFile,"r")

            for line in fd.readlines():
                titleRecord = line.strip().split('\t')
                self.myLogger.debug("fetched recent title %s" % titleRecord)
                recentTitles.append(titleRecord)

        else:
            self.myLogger.error("the file %s does not exist!" %pathToRecentFile)

        return recentTitles


    def reformRecentTitlesToDictionary(self,recentTitlesLists):
        recentTitlesDictionaries = []

        for recentTitle in recentTitlesLists:
            curDict = {TIMESTAMP:       int(recentTitle[0]),
                       CONTENT_ID:      recentTitle[1],
                       SITE_ID:         recentTitle[2],
                       CONTENT_LENGTH:  int(recentTitle[3]),
                       DELIVERED:       bool(int(recentTitle[6])),
                       CLIENT:          recentTitle[7]}
            self.myLogger.debug("recent title dict add - %s" % curDict)
            recentTitlesDictionaries.append(curDict)

        return recentTitlesDictionaries


    def recentTitles(self,cnt):

        # get all the recent titles
        allRecentTitles = self.getAllRecentTitlesFromFile()

        # slice and reform to dictionary
        return self.reformRecentTitlesToDictionary(allRecentTitles[:cnt])


    def getParetoPointsFromFile(self, paretoFile):

        fd = openFileForRead(paretoFile,self.myLogger)

        # first point is always (0,0)
        paretoPoints = [[0,0]]

        if fd != None:
            for line in fd.readlines():
                record = line.strip().split('\t') # strip is for removing trailing sapces and such
                paretoPoints.append([int(record[CUM_CNT]),int(record[CUM_DATA])]) # the cummulative X and cummulative Y in a pareto record

        if len(paretoPoints) == 1:
            self.myLogger.error('no pareto points were retrieved from %s' %paretoFile)

        return paretoPoints


    def paretoPointsToDictionary(self,paretoPoints):
        
        totalRec = None

        # next if-else is so that there will always be a TOTAL record even when everything went wrong for some reason
        if len(paretoPoints)==0:
            self.myLogger.error("something went wrong in retreiving pareto data, len(paretoPoints) == 0")
            totalRec = {TOTAL_REC_ITEMS:0, TOTAL_REC_VALUE:0}

        else:
            totalRec = {TOTAL_REC_ITEMS:paretoPoints[-1][0], TOTAL_REC_VALUE:paretoPoints[-1][1]}

        entries = []
        for paretoPoint in paretoPoints:
            entries.append({CUM_ITEMS:paretoPoint[0], CUM_VALUE:paretoPoint[1]})

        return {ENTRIES:entries, GRAND_TOTAL:totalRec}


    def paretoCategoryAndDataTypeInputCheck(self,category,dataTypeName):

        if (category not in [CLIENTS,TITLES]):
            raise Exception,"category = %s is illegal for pareto request!"%category
            
        if (dataTypeName not in [VOLUME]):
            raise Exception,"dataType = %s is illegal for pareto request!"%dataTypeName


    def pareto(self,category,dataTypeName):

        #input check
        self.paretoCategoryAndDataTypeInputCheck(category,dataTypeName)

        # construct relevant 'last' pareto file path
        paretoLastFile = os.path.join(self.myReportsRoot,TOPPER,category,LAST_NAME,dataTypeName,LAST_HOUR_PARETO_FILE_NAME)

        # get the pareto points from the file
        paretoPoints = self.getParetoPointsFromFile(paretoLastFile)

        # format to response suitable dictionary
        paretoDictionary = self.paretoPointsToDictionary(paretoPoints)

        return paretoDictionary


    def hourlyDistributionCommon(self,startTime,endTime,dataType,useBgs,loose):
        
        secondsInHour = 3600
        bucketCnt     = 24

        # create over time records
        records = self.overTimeCommon(startTime,endTime,secondsInHour,SECOND,dataType,None,useBgs,None,loose)

        # create grouper - creator of the distribution from records
        hourlyGrouper = Grouper(secondsInHour,bucketCnt,self.myLogger,HOUR_OF_DAY,*self.myOTRequest.dataType.outputDictionaryLabels[1:])

        # add records to grouper object
        hourlyGrouper.addRecords(records)

        # create distribution
        dist = hourlyGrouper.getAverageDistribution()

        return dist



    def hourlySubscriberDistribution(self,startTime,endTime,loose=True):

        dist = self.hourlyDistributionCommon(startTime,endTime,CLIENTS,None,loose)

        return dist


    def hourlyDistribution(self,startTime,endTime,dataType,useBgs=False,loose=True):
        if dataType in dataTypes:
            dist = self.hourlyDistributionCommon(startTime,endTime,dataType,useBgs,loose)
            return dist
        else:
            raise Exception,"unsupported data type '%s for hourlyDistribution() function'"%dataType


    def paretoOverTimeInputCheck(self,startTime,granularity,category,dataType,percentiles):
        # check percentiles
        isGoodInput = True
        for per in percentiles:
            if not (1 <= per <= 100):
                self.myLogger.error("bad percentiles input - %s is not between 1 and 100"%per)
                isGoodInput = False
                
        if isGoodInput == False:
            raise Exception,"bad percentiles for paretoOverTime()"

        # check start time
        secondsInHour = 3600
        if (startTime%secondsInHour != 0):
            raise Exception,"startTime (=%s) is not aligned with whole hour in paretoOverTime()"%startTime

        # check interval
        if (granularity%secondsInHour != 0):
            raise Exception,"granularity (=%s) is not aligned with whole hour in paretoOverTime()"%granularity

        self.paretoCategoryAndDataTypeInputCheck(category,dataType)
            
        return True


    def getParetoPointsFromFiles(self,startTime,endTime,granularity,files,percentiles):
        points = []
        secondsInHour = 3600
        percentiles = sorted(percentiles) # just in case

        while (startTime+secondsInHour <= endTime):
            # find the files that fit (startTime + i*granularity and fileEndTime<endtime)
            if startTime in files:
                file = files[startTime]
                self.myLogger.debug2("pareto file %s with start time %s was found to be in the pareto overtime request range" %(file,startTime))
                point = self.getPointFromFile(file,percentiles)
                if (point != None):
                    point[TIME] = (startTime - self.myTimeShift) # update point's time and take into consideration the artificial time shift
                    points.append(point)
                    self.myLogger.debug2("pareto file %s was converted to a pareto point %s" %(file,point))

            startTime += granularity

        return points
                

    def  getPointFromFile(self,file,percentiles):

        percentilesCopy = list(percentiles)

        fd = openFileForRead(file,self.myLogger)
        if fd == None:
            self.myLogger.error("file %s could not be opened for conversion to a pareto point"%file)
            return None
            
        allLines = fd.readlines()
        numOfLines = len(allLines)
        # check we have 100 percentiles
        if (numOfLines < 100):
            self.myLogger.debug("file %s contained only %s lines, 100 is needed! ignoring file"%(file,numOfLines))
            return None

        # construct point from relevent percentiles data
        point = {}
        record = None
        for line in allLines:
            record = line.strip().split('\t')
            curPercentile = int(record[PERCENTILE])
            if curPercentile in percentilesCopy:
                point[curPercentile] = int(record[CUM_DATA])
                percentilesCopy.remove(curPercentile)
        
        # check we have all percentiles
        if (len(percentilesCopy)>0):
            self.myLogger.error("could not retrieve the percentiles %s from file %s! ignoring file"%(percentilesCopy,file))
            return None
        
        # add totalCnt (last record is at hand)
        point[TOTAL_REC_ITEMS] = int(record[CUM_CNT])

        fd.close()

        return point

        
        

    def paretoOverTime(self,startTime,endTime,granularity,category,dataType,percentiles):

        # time shift comming from above (configuration)
        startTime += self.myTimeShift
        endTime   += self.myTimeShift
        
        # input check (TODO: should I throw an exception or just return empty)
        self.paretoOverTimeInputCheck(startTime,granularity,category,dataType,percentiles)

        # get the pareto reports directory
        reportsDir = os.path.join(self.myReportsRoot,TOPPER,category,"hourly",dataType)

        # get the relevent files by time range
        relevantFiles = self.findRelevantFilesByTime(reportsDir,"%Y%m%d-%H.tsv.pareto",(lambda year,month: 3600),startTime,endTime)

        # extract dictionary-points from files
        points = self.getParetoPointsFromFiles(startTime,endTime,granularity,relevantFiles,percentiles)

        return points
        


def getReportsInfo(reportsRoot):
    # find min and max times of reports
    global granularitySets
    minTime = sys.maxint
    maxTime = -1
    
    volumeDir = os.path.join(reportsRoot,OVER_TIME,HOUR.name,VOLUME)
    for file in safeListDir(volumeDir):
        try:
            timeObj = time.strptime(file,HOUR.fileNameFormat)
            year = timeObj.tm_year
            month = timeObj.tm_mon
            fileStartTime = calendar.timegm(timeObj) # epoch time
            fileEndTime = fileStartTime + HOUR.rangeOfFile(year,month) # epoch time
            
            # update the maximum if possible
            if (fileEndTime > maxTime):
                maxTime = fileEndTime

            # update the minimum if possible
            if (fileStartTime < minTime):
                minTime = fileStartTime
            

        except ValueError:
            # just bad files in reports dir...do not stop...
            continue

    reportsInfo = {}
    reportsInfo["startTime"] = minTime
    reportsInfo["endTime"]   = maxTime

    return reportsInfo

    

