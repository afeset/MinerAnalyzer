#!/usr/local/bin/python2.6
# 
# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# ver 1.0 
#
# Author: galm
#
########################################################################################################################
#                                                                                                                      #
# This module defines the stats aggregator interface and implement it using rrdtool and SQLite
#                                                                                                                      #
########################################################################################################################

import threading
import tarfile
import time
import sys, os, shutil
import stats_queue_objects 
from stats_values_db import RRDToolValuesDB
from stats_descriptions_db import SQLiteDescriptorsDB
from datetime import datetime as my_datetime
from event_report_limiter import EventReportLimiter
from enums import VariableTypes
from a.infra.file.rotating_file_size_enforcer import RotatingFileSizeEnforcer

# === Globals =====================================================================================
SQLITE_EXTENTION = ".sqlite"
RRD_EXTENTION = ".rrd"
TAR_GZIP_FLAG = "w:gz"
FILE_NAME_TIMESTAMP_FORMAT = "%A-%d%B%Y-%H%M-%s"
MAX_INSERT_TO_DB_TIME_SPAN = 30
# === Implementations =====================================================================================

#Handels all aggregation - the customer in the producer customer Design Pattern (AKA consumer)
#Using RRDTool and SQLite
class StatsAggregator(threading.Thread):

    def __init__ (self):
        pass

    #Finds previous rrd file paths
    def getPreviousRrdPaths (self, rrdDirPath):
        list_of_files = []
        for root, dirs, files in os.walk(rrdDirPath):
            for f in files:
                if f.endswith(RRD_EXTENTION):
                    list_of_files.append(f)
                
        return list_of_files

    def __copyDbsToOldDir (self, dbTimeString):
        tempPath = os.path.join(self.myOldDataDir, str(dbTimeString.strftime(FILE_NAME_TIMESTAMP_FORMAT)))
        self.__delDirsIfNeeded(tempPath)
        self.__moveSubDirsToDir(self.mydbRRdFilesOutputPath, tempPath)
        self.__moveFilesToDir(self.myDescriptionDbFilesPath, tempPath)
        self.__createCompressedTar(tempPath, tempPath+".gzip")
        #Clean
        self.__delDirsIfNeeded(tempPath)

    #countersDBInfo - A dictionary that holds key = counter ID value = counter descriptor object
    #jobsQueue - The queue for the design pattern used, through it the sampled counters are sent to the aggregator to be stored
    #logger - dah
    #dbFilesOutputPath - The path where the db files will be stored
    #dbFilesBaseName - The prefix for the db files' names
    #rrdtoolExePath - The path to the RRDTool .exe file    
    def init (self, countersDBInfo, jobsQueue, logger, baseLogger, dataRunDirPath, descriptionDbFilesPath, dbFilesOutputPath, 
              dbFilesBaseName, rrdtoolExePath, rrdtoolWrapperExePath, oldDataDir, prevRunDir,
              updateBurstCount, updateBurstIntervalMsec, enableRecovery):

        #Initialize memeber variables
        self.myJobsQueue = jobsQueue
        self.myLogger = logger
        self.myDescriptionDbFilesPath = descriptionDbFilesPath
        self.myDataRunDirPath = dataRunDirPath
        self.mydbRRdFilesOutputPath = dbFilesOutputPath
        self.myOldDataDir = oldDataDir
        self.myPrevRunDir = prevRunDir
        self.__makeDirsIfNeeded(self.myPrevRunDir)

        self.myUpdateBurstCount = updateBurstCount
        self.myUpdateBurstInterval = updateBurstIntervalMsec / 1000.0
        self.myEnableRecovery = enableRecovery 

        # The history files rotating file
        self.myHistoryFilePattern = "update-"
        self.myHistoryFileSuffix = ".csv"
        self.myHistoryRotatingFile = RotatingFileSizeEnforcer(
            baseLogger, self.myPrevRunDir, self.myHistoryFilePattern, self.myHistoryFileSuffix)
        self.myHistoryRotatingFile.prepare()

        #Create meta-data DB
        #dbTimeString = datetime.now() #Part of the file name is a date string 
        dbTimeString = my_datetime.now() #Part of the file name is a date string 
        self.myDescriptionsDB = SQLiteDescriptorsDB()
        #Search for an old DB file 
        sqliteDB = [f for f in os.listdir(descriptionDbFilesPath) if f.lower().endswith(SQLITE_EXTENTION)]
        rrdDBs = self.getPreviousRrdPaths(dbFilesOutputPath)

        if len(sqliteDB) == 0:
            if len(rrdDBs) > 0:
                self.myLogger.notice("StatsAggregator - sqlite file wasn't found while " + str(len(rrdDBs)) + " rrd files exist")
                self.__copyDbsToOldDir (dbTimeString)
            else:
                self.myLogger.debug5("StatsAggregator - sqlite and RRD files doesn't exist - ok")
        else:
            if len(rrdDBs) ==0:
                self.myLogger.notice("StatsAggregator - sqlite file found while no rrd files exist")
                self.__copyDbsToOldDir (dbTimeString)
            else:
                self.myLogger.debug5("StatsAggregator - RRD and sqlite files doesn't exist - ok")
        self.myDescriptionsDB.init(self.myLogger, descriptionDbFilesPath, dbFilesBaseName)
        #Distinguish between old and new counters
        previousConfigurations = self.myDescriptionsDB.getConfigurationsFromDB()

        if previousConfigurations is None:
            #notice Error
            self.myLogger.notice("StatsAggregator - existing sqlite file is malformed")
            self.__copyDbsToOldDir (dbTimeString)
            previousConfigurations = []
        self.myLogger.debug2("StatsAggregator old configuration DB loaded")
        #Get only the new counters out of all the configured ones
        newCounters = self.diffAgainstNewConfig(countersDBInfo, previousConfigurations)
        if newCounters is None:
            #There should be no counter changes, if one is found, we copy all previous data to a temp directory and create new DBs
            self.myLogger.notice("An ilegal change was made in the configurations file - all previous data copied to " + self.myOldDataDir + ". Creating new stats DBs")
            self.__copyDbsToOldDir (dbTimeString)
            #All counters are considered new
            newCounters = countersDBInfo
            #Now we need to reCreate the self.myDescriptionsDB sience we moved the file
            self.myDescriptionsDB = SQLiteDescriptorsDB()
            self.myDescriptionsDB.init(self.myLogger, descriptionDbFilesPath, dbFilesBaseName)
            previousConfigurations=[]

        if len(previousConfigurations) > 0:
            previousCountersDbPathList = self.myDescriptionsDB.getPreviousDbPath()
            if len(previousCountersDbPathList) != 1:
                self.myLogger.error("StatsAggregator - too many sqlite files found")
                self.__copyDbsToOldDir (dbTimeString)
                newCounters = countersDBInfo
                self.myLogger.debug2("StatsAggregator - previous counters configuration was empty - creating a new SQLite DB")
                errFlag = self.myDescriptionsDB.createDB(countersDBInfo, dbTimeString, newCounters) 
                if errFlag:
                    self.myLogger.error("StatsAggregator - create db state 1 failed")
                    return errFlag
            else:
                previousCountersDbPath = self.myFileName = os.path.join(descriptionDbFilesPath,previousCountersDbPathList[0])
    
                #If we are here then this is not the first run on this machine
                if newCounters is None:
                    self.myLogger.error("StatsAggregator - error occured while comparing counters from sqlite file and new configured ones")
                    return 3215374
                if len(newCounters) == 0:
                    self.myLogger.debug2("StatsAggregator - no new counters configured")
                    errFlag = self.myDescriptionsDB.createDB(countersDBInfo, dbTimeString, {}, previousCountersDB=previousCountersDbPath)
                    if 0<errFlag:
                        self.myLogger.error("StatsAggregator - create db state 2 failed")
                        return errFlag
                else:
                    self.myLogger.debug2("StatsAggregator - %d new counters configured" % len(newCounters))
                    errFlag = self.myDescriptionsDB.createDB(countersDBInfo, dbTimeString, newCounters, previousCountersDB=previousCountersDbPath)
                    if 0<errFlag:
                        self.myLogger.error("StatsAggregator - create db state 3 failed")
                        return errFlag

                #If we are hear then 1. It is not the first run 2. Some coutners were added to DB in previous run and wasn't updated
                self.myLogger.debug2("StatsAggregator - updating old counters")
                
                errFlag = self.myDescriptionsDB.updateDB(previousConfigurations)
                if 0<errFlag:
                    self.myLogger.error("StatsAggregator - updating previous counters UI settings failed")
                    return errFlag
                errFlag = self.myDescriptionsDB.updateDB(newCounters)
                if 0<errFlag:
                    self.myLogger.error("StatsAggregator - updating new counters UI settings failed")
                    return errFlag
        else:
            newCounters = countersDBInfo
            #If we are here then this is probably the first run on this machine or someone deleted all previous data
            self.myLogger.debug2("StatsAggregator - previous counters configuration was empty - creating a new SQLite DB")
            errFlag = self.myDescriptionsDB.createDB(countersDBInfo, dbTimeString, newCounters) 
            if 0<errFlag:
                self.myLogger.error("StatsAggregator - create db state 4 failed")
                return errFlag

        #Create values DB
        self.myValuesDB = RRDToolValuesDB()        
        self.myValuesDB.init(self.myDescriptionsDB, self.myLogger, self.myDataRunDirPath, dbFilesOutputPath, dbFilesBaseName, rrdtoolExePath, rrdtoolWrapperExePath)
        errFlag = self.myValuesDB.createDB(countersDBInfo, dbTimeString)
        if errFlag:
            self.myLogger.error("StatsAggregator - create db state 5 failed")
            return errFlag

        #SQLite won't allow us to use this cursur from other threads.
        self.myDescriptionsDB.closeDBConnection()
        
        self.myRunFlag = True
        threading.Thread.__init__(self)
        return 0


    def setAggrHistory (self, aggrHistory):
        self.myAggrHistory = aggrHistory
        self.myNumHistoryFiles = 0


    def setNumHistoryFiles (self, numHistoryFiles):
        self.myNumHistoryFiles = numHistoryFiles

    
    def loadHistoryFiles (self):

        # Get a list of history files and sort them in an alphnumeric order.
        # Since kick number and date are encoded in the file name we will get 
        # the files in creation order
        historyFiles = os.listdir(self.myPrevRunDir)
        historyFiles.sort()

        self.myLogger.notice("StatsAggregator load history files. Found %d files in prev run folder %s" % 
                             (len(historyFiles), self.myPrevRunDir))

        # Sort the list of files
        for fileName in historyFiles:
            self.myLogger.debug1("StatsAggregator loading history file %s", fileName)
            fullName = os.path.join(self.myPrevRunDir, fileName)
            with open(fullName) as f:
                lineNum = 0
                for line in f:
                    try:
                        lineNum += 1
                        (name, value, timestamp, valueType) = self.__parseHistoryLine(line.rstrip())
                        self.myAggrHistory.update(name, value, valueType, timestamp)
                    except Exception as ex:
                        self.myLogger.error("Error loading line %d in file %s. Discard rest of the file. %s" %
                                             (lineNum, fileName, ex))
                        break

        self.myLogger.notice("StatsAggregator finished loading history files") 


    def saveHistoryFile (self, allUpdatesStr):
        self.myHistoryRotatingFile.rotate()
        fileName = self.myHistoryRotatingFile.getCurrentFileName()
        self.myLogger.debug1("StatsAggregator save history file %s" % fileName)
        try:
            with open(fileName, 'w') as f:
                f.write(allUpdatesStr)
        except Exception as ex:
            self.myLogger.error("Error write update history to file %s. %s" %
                                 (fileName, ex))

        # To enforce limit on number of history files we delete the oldest files.
        historyFiles = os.listdir(self.myPrevRunDir)
        historyFiles.sort()
        numFiles = len(historyFiles)
        numToDelete = numFiles - self.myNumHistoryFiles
        idx = 0
        self.myLogger.debug3("StatsAggregator enforce history limit: found %s, allowed %d" % (numFiles, self.myNumHistoryFiles))
        while numToDelete > 0:
            fullPath = os.path.join(self.myPrevRunDir, historyFiles[idx])
            try:
                self.myLogger.debug3("StatsAggregator enforce history limit: remove %s" % historyFiles[idx])
                os.remove(fullPath)
            except Exception as ex:
                self.myLogger.error("Enforce history limit: Error delete file %s. %s" % (fullPath, ex))
            idx += 1
            numToDelete -= 1


    # This is the module's main function. It dequeues the jobs from the queue and execute them
    # The jobs ***MUST*** be executed synchronically since in the future the counters might change
    # and a new file has to be created before inserting any value
    def run (self):
        
        self.myLogger.notice("Stats Aggregator running")
        reportLimiter = EventReportLimiter(3600)

        try:
            self.myRunFlag = True
            self.myDescriptionsDB.connectToDb()
    
            while(self.myRunFlag):

                self.myLogger.debug2("StatsAggregator blocking in order to dequeue. Time = %d" % time.time())

                job = self.__dequeue()
                if None == job:
                    self.myLogger.debug1("StatsAggregator dequeued a job from jobs queue. Message is None -> unblock message")
                    continue

                self.myLogger.debug2("StatsAggregator message dequeued successfully. Time = %d" % time.time())

                # If this is a sample result job (The only legal message for v1.0)
                startTime = time.time()

                if (job.quack() == stats_queue_objects.AggregationQueueJobType.VALUES):
                    self.myLogger.debug2("StatsAggregator received values job")

                    # Iterate on all received counters and update global aggr dictionary.
                    # Respect counter burst params

                    allUpdatesStr = "" # This will be saved to a history file

                    counterIdx = 0
                    numCounters = len(job.myCountersArray)
                    while counterIdx < numCounters:
                        burstStartTime = time.time()
                        self.myAggrHistory.lock()
                        i = 0
                        self.myLogger.debug3("Start burts")
                        while i < self.myUpdateBurstCount:
                            counterVal = job.myCountersArray[counterIdx]
                            self.myLogger.debug5("Updating couner id %s values (%s, %s)",
                                                 counterVal.myCounterId, counterVal.myValue, counterVal.myTimeStamp)
                            valueType = type(counterVal.myValue).__name__
                            self.myAggrHistory.update(counterVal.myCounterId, counterVal.myValue, valueType, counterVal.myTimeStamp)

                            allUpdatesStr += self.__formatHistoryLine(counterVal.myCounterId, counterVal.myValue, 
                                                                      counterVal.myTimeStamp, valueType)

                            i += 1
                            counterIdx += 1
                            if counterIdx == numCounters:
                                break
                        self.myAggrHistory.unlock()
                        burstTime = time.time() - burstStartTime
                        self.myLogger.debug3("End burts")

                        # Warn about a long burst, or count it for the next warning
                        maxAllowedBurstTime = self.myUpdateBurstInterval * 0.75
                        if burstTime > maxAllowedBurstTime:
                            (shouldReport, numEvents) = reportLimiter.shouldReport()
                            if shouldReport:
                                self.myLogger.warning("Aggregator update burst took too long: %s seconds, max allowed is %s. (Occured %s times since last reported)",
                                                      burstTime, maxAllowedBurstTime, numEvents)

                        # If we have more counters, sleep
                        if counterIdx < numCounters:
                            remainingTime = self.myUpdateBurstInterval - burstTime
                            if remainingTime > 0:
                                time.sleep(remainingTime)

                    self.saveHistoryFile(allUpdatesStr)

                insertTimeSpan = time.time()-startTime
                if insertTimeSpan > MAX_INSERT_TO_DB_TIME_SPAN:
                    self.myLogger.warning("Execute job exceeds the time limit. Limit is %d sec. Elapsed time is %s sec, numCounters=%s. Queue size is: %d",
                                          MAX_INSERT_TO_DB_TIME_SPAN, insertTimeSpan, numCounters, self.myJobsQueue._qsize())
                else:
                    self.myLogger.notice("Execute job. Elapsed time is %s sec, numCounters=%s. Queue size is: %d",
                                         insertTimeSpan, numCounters, self.myJobsQueue._qsize())
    

            if self.myRunFlag:
                self.myLogger.notice("Stats Aggregator thread ended enexpectedly")
            else:
                self.myLogger.notice("Stats Aggregator thread ended")

            self.myRunFlag = False

        except:
            #Loop ended - thread is shutting down
            self.myRunFlag = False
            self.myLogger.error("UNExpected exception on Stats Aggregator. Exception info: %s" % stats_queue_objects.formatExceptionInfo())

        #When the while loop ended = shutdown - close the DBs
        self.myValuesDB.closeDBConnection()
        self.myDescriptionsDB.closeDBConnection()
        self.myLogger.debug2("StatsAggregator thread ended")

    def __formatHistoryLine (self, name, value, timestamp, valueType):
        return "%s,%s,%s,%s\n" % (name, value, timestamp, valueType)

    def __parseHistoryLine (self, line):
        (name, strValue, timestamp, valueType) = line.split(',')

        floatTimestamp = None
        if timestamp != 'None':
            floatTimestamp = float(timestamp)

        value = strValue
        if valueType == 'int':
            value = int(strValue)
        elif value == 'float':
            value = float(strValue)

        # name is actually a numeric counter id
        return (int(name), value, floatTimestamp, valueType)

    # creates a compressed tar file containing all the files specified + the temp directory
    def __createCompressedTar(self, directory, tarOutputFilePath):
        try:
            tarResultPath = tarOutputFilePath
            tar = tarfile.open(tarResultPath, TAR_GZIP_FLAG)
            #tar.dereference = True - This is too dangerous - Can link to huge files/directories - removed on purpuse - don't add this!
        except:
            self.myLogger.error("Exception occured while creating the Tar file - tar file can't be created" + stats_queue_objects.formatExceptionInfo())
            return False
    
        try:
            tar.add(directory)
        except:
            self.myLogger.error("Exception occured while creating the Tar file" + stats_queue_objects.formatExceptionInfo())
            return False    
        try:
            tar.close()
        except:
            self.myLogger.error("Exception occured while creating the Tar file - tar file can't be closed" + stats_queue_objects.formatExceptionInfo())
            return False
        self.myLogger.debug3("Tar file created successfully")
        return True

    def __delDirsIfNeeded (self, dirPath):
        try:
            if os.path.exists(dirPath):
                if os.path.isdir(dirPath):
                    shutil.rmtree(dirPath)
        except:
            self.myLogger.error("UNExpected exception on Stats Aggregator.__delDirsIfNeeded. Exception info: %s" % stats_queue_objects.formatExceptionInfo())

    def __makeDirsIfNeeded (self, dirPath):
        try:
            if os.path.exists(dirPath):
                if os.path.isdir(dirPath):
                    return True
                else:
                    return False
            else:
                    oldUmask = os.umask(0)
                    os.makedirs(dirPath)
                    os.umask(oldUmask)
                    return True
        except:
            return False

    def __moveSubDirsToDir(self, srcDir, dstDir):
        try:
            self.__makeDirsIfNeeded(dstDir)
            listOfFiles = os.listdir(srcDir)
            for d in listOfFiles:
                srcSubDir = os.path.join(srcDir, d)
                if srcSubDir == dstDir:
                    continue
                if os.path.isdir(srcSubDir):
                    shutil.move(srcSubDir, dstDir)
        except:
            self.myLogger.error("UNExpected exception on Stats Aggregator.__moveSubDirsToDir. Exception info: %s" % stats_queue_objects.formatExceptionInfo())

    def __moveFilesToDir(self, srcDir, dstDir):
        self.__makeDirsIfNeeded(dstDir)
        for root, dirs, files in os.walk(srcDir):
            for f in files:
                srcFile = os.path.join(srcDir, f)
                shutil.copy(srcFile, dstDir)
                os.remove(srcFile)
                

    #The user has to check queue size before
    def __dequeue (self):
        result = self.myJobsQueue.get(True)
        return result

    def isRunning (self):
        #return True;
        return self.myRunFlag

    def end (self):
        self.myLogger.notice("Stats Aggregator request to end thread")
        self.myRunFlag = False
        self.myJobsQueue.put(None)

    def setLogger (self, logger):
        self.myLogger = None
        self.myLogger = logger
        self.myDescriptionsDB.setLogger(logger)
        self.myValuesDB.setLogger(logger)

    
    #returns the changes between the new configuration and the old one
    #If there is an ilegal change logs and exits
    def diffAgainstNewConfig (self, newConfig, previousConfig):
        if newConfig is None:
            self.myLogger.error("Unexpected error occured during comparison between new and old configurations")
            return None

        #This means there aren't any previous configurations
        if len(previousConfig) == 0:
            return newConfig

        #New added counters are not compared
        newCounters = {}
        #Go over all counters in the new configurations
        for counter in newConfig.values():
            #If the counter is new - doesn't exist in previous configuration
            if counter.myCounterId in previousConfig.keys():
                #Check that it wasn't changed. If not mark it as new, otherwise - fail - it is ilegal to change counters without deleting the history / changing directories
                if counter != previousConfig[counter.myCounterId]:
                    #If you got here it means that an ilegal diff was found
                    self.myLogger.error("An ilegal change was made in the configurations file. Counter Info: %s" % counter.toString())
                    return None
            else:
                self.myLogger.debug3("New counter found. Counter = %s" % counter.toString())
                newCounters[counter.myCounterId] = counter

        #We don't check for missing counters since it is legal to disable counters
        return newCounters

        

