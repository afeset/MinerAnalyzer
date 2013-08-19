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
# This module defines the stats aggregator numeric DB interface (Currently RRDTool) and implements it
#                                                                                                                      #
########################################################################################################################

from my_hash import myHash
from datetime import datetime
from UserString import MutableString
from stats_queue_objects import createDirIfNeeded, deleteFileIfNeeded, formatExceptionInfo
from enums import AggregationConsolidationFunctionType, VariableTypes, AggregationCounterType
import subprocess
import os
import re
import sys
import time
import traceback

# === Globals =====================================================================================

MISSED_SAMPLE_FACTOR = 2
FILE_NAME_TIMESTAMP_FORMAT = "%A-%d%B%Y-%H%M-%s"
NUMBER_OF_COUNTERS_PER_ONE_RRD = 50
RRDTOOL_EXE_PATH_RELATIVE_TO_ROOT = 'rrdtool'
RRDTOOL_COMMANDS_FILES_DIR = 'rrdtool_command_files'
# === Implementations =====================================================================================
class RRDToolValuesDB(object):

    def __init__ (self):
        pass
        
    def init (self, rrdFileMappingObject, logger, dataRunDirPath, dbFilesOutputPath, dbFilesBaseName,
              rrdtoolExePath, rrdtoolWrapperExePath):

        self.myDbFilesOutputPath = dbFilesOutputPath
        self.myDbFilesBaseName = dbFilesBaseName
        self.myLogger = logger
        self.myRRDToolExe = rrdtoolExePath
        self.myRRDToolWrapperExe = rrdtoolWrapperExePath
        self.myCreatedStatus = False
        self.myRrdFilesMappingObject = rrdFileMappingObject
        self.myDataRunDirPath = dataRunDirPath
        self.myNumOfCounterWrites = 0
        self.myCommandsFileIndex = 0
        self.myCommandsFileHandle = None
        self.myRRDComandFilesDirPath = os.path.join(self.myDataRunDirPath, RRDTOOL_COMMANDS_FILES_DIR)
        self.myCountersDBInfo = None
        # RE to find data from a line such as this one:    ds[325528256665529272].minimal_heartbeat = 120
        self.myReHeartbeat = re.compile("ds\[[^\]]+\]\.minimal_heartbeat\s*=\s*(\d+)")
        self.myLogger.debug2("RRDToolValuesDB initialized")


    def closeDBConnection (self):
        return


    def getCounterById (self, counterId):
        if self.myCountersDBInfo is None:
            return None
        return self.myCountersDBInfo.get(counterId)


    def getDesiredHeartbeatForId (self, counterId):
        counter = self.getCounterById(counterId)
        if counter:
            return counter.myMinHeartbeat
        return None


    def isCounterIdExists (self, counterId):
        return counterId in self.myRrdFilesMappingDictionary
        

    def getRrdFilePath (self, counterId):
        rrdRelativePath = self.myRrdFilesMappingDictionary[counterId]
        rrdPath = os.path.join(self.myDbFilesOutputPath, rrdRelativePath)
        return rrdPath


    def formatTuneHeartbeatCommand (self, counterId, heartbeat):
        rrdPath = self.getRrdFilePath(counterId)
        cmd = "tune %s --heartbeat %s:%s" % (rrdPath, counterId, heartbeat)
        return cmd


    def formatUpdateCommand (self, counterId, timeStamp, value, valueType):
        rrdPath = self.getRrdFilePath(counterId)
        commandFormat = "update %s %s:" + VariableTypes.FORMAT_BY_NAMES[valueType] 
        cmd = commandFormat % (rrdPath, timeStamp, value)
        return cmd


    def formatInfoCommand (self, counterId):
        rrdPath = self.getRrdFilePath(counterId)
        cmd = "info %s" % rrdPath
        return cmd


    def formatCreateCommand (self, counter, rrdPath):

        cmd = "create %s --step %d" % (rrdPath, counter.mySamplingRate)

        #Format archaives string
        archaivesString = MutableString()
        for archaive in counter.myArchaives:
            archaivesString.append(" RRA:%s:%f:%d:%d" % (archaive.myArchaiveType, archaive.myErrorsAllowed,archaive.myConsolidationSpan,archaive.myRowsToKeep))

        #Format DS
        cmd += " DS:%d:%s:%d:%s:%s %s" % \
            (counter.myCounterId,
             counter.myCounterType,
             counter.myMinHeartbeat,
             counter.getMinStr(),
             counter.getMaxStr(),
             archaivesString.data)

        return cmd



    def executeRrdCommands (self, commands):
        """
        Given a list of commands, runs rrd and returns output for each command.
        commands is a list of elements, each element is (Opaque-Object, command).
          Opaque-Object is returned in the output
          command is the actual RRD command, usually created by a formatXxxCommand() function above
        Returns a list whose length is always identical to len(commands).
        Each element of the returned list is (Opaque-Object, (success, outputStr))
          Opaque-Object is the same thing given in the input
          success is True for command success, False otherwise
          outputStr is the output of the command
        """

        numCommands = len(commands)
        if numCommands == 0:
            return []

        isFirst = True
        i = 0
        self.myLogger.debug4("Start, commands=%s", commands)
        while i < numCommands:
            command = commands[i][1]
            isLast = (i == numCommands-1)
            self.__addCommandToFile(isFirst, isLast, command)
            isFirst = False
            i += 1

        result = self.__executeRRDCommandsFile()
        self.myLogger.debug4("result=%s", result)
        rrdSuccess = result[0]
        rrdOutputString = result[1]
        if not rrdSuccess:
            self.myLogger.error("Can't get info from rrdtool. Error Message: %s. commands=%s", rrdOutputString, commands)
            return map(lambda x: (x[0], (False, "RRD-FAILED")), commands)

        self.myLogger.debug4("Executed. rrdSuccess=%s", rrdSuccess)
        self.myLogger.debug4("%s", rrdOutputString)

        # Split command output for each command. We expect a block of text for each command, plus one last block 
        # with a summary message
        commandOutputs = rrdOutputString.split("COMMAND-DELIMITER\n")
        if len(commandOutputs) != numCommands+1:
            self.myLogger.error("Can't parse output into %s elements: commands=%s. output=%s", numCommands+1, commands, rrdOutputString)
            return map(lambda x: (x[0], (False, "PARSE-FAILED")), commands)

        i = 0
        retValues = []
        while i < numCommands:
            commandOutput = commandOutputs[i]
            success = commandOutput.endswith(":Q_OK:")
            retValues.append((commands[i][0], (success, commandOutput)))
            i += 1

        self.myLogger.debug4("Returning retValues=%s", retValues)
        return retValues


    # This function creates a new round robin DB file 
    # It can only be called once for each new instance
    def createDB (self, countersDBInfo, timeStamp):
        self.myLogger.debug3("RRDToolValuesDB.createDB() was called")
        if self.myCreatedStatus:
            self.myLogger.error("RRDToolValuesDB.createDB() was called twice for one instance - ilegal")
            return 1785196
        else:
            self.myCreatedStatus = True

        if not createDirIfNeeded (self.myRRDComandFilesDirPath):
            self.myLogger.error("RRDToolValuesDB createDB error - can't create dir %s" % self.myRRDComandFilesDirPath)
            return 589864
        self.myTimeStampString = timeStamp.strftime(FILE_NAME_TIMESTAMP_FORMAT)
        self.myCountersDBInfo = countersDBInfo
        #Get rrd files mapping
        self.myRrdFilesMappingDictionary = self.myRrdFilesMappingObject.getRRDFilesMapping()
        if not self.__validateFilesMappingDictionary(self.myRrdFilesMappingDictionary):
            return 6342343

        commands = []

        for counter in countersDBInfo.values():

            # TODO galm check if related to bug OSC-323
            if counter.myCounterId in self.myRrdFilesMappingDictionary.keys():
                # A file already exists
                continue

            # Create the sub directory
            rrdDir = os.path.join(self.myDbFilesOutputPath, counter.myCounterProcess)
            if createDirIfNeeded(rrdDir):
                self.myLogger.debug2("RRDTool object created the directory %s" % rrdDir)
            else:
                self.myLogger.debug2("RRDTool object failed to create the directory %s" % rrdDir)
                return 340809

            rrdRelativePath = '%s.rrd' % os.path.join(counter.myCounterProcess, self.myDbFilesBaseName + str(counter.myCounterId) + '-' +self.myTimeStampString)
            rrdPath = os.path.join(self.myDbFilesOutputPath, rrdRelativePath)
            createCommand = self.formatCreateCommand(counter, rrdPath)
            commands.append(((counter, rrdRelativePath), createCommand))

        if commands:
            # Execute the commands
            retValues = self.executeRrdCommands(commands)

            for retValue in retValues:
                opValue = retValue[0]
                commandSuccess = retValue[1][0]
                commandOutput = retValue[1][1]
                if not commandSuccess:
                    self.myLogger.error("RRD 'create' command failed: commandOutput=%s", commandOutput)
                else:
                    counter = opValue[0]
                    rrdRelativePath = opValue[1]
                    errFlag = self.myRrdFilesMappingObject.setCounterRRDFileMapping(counter.myCounterId, rrdRelativePath)
                    if errFlag:
                        self.myLogger.error("Erros setting file napping, counterId=%s, counterName=%s, rrdRelativePath=%s",
                                            counter.myCounterId, counter.myCounterPath + "/" + counter.myCounterName, 
                                            rrdRelativePath)
                    else:
                        self.myRrdFilesMappingDictionary[counter.myCounterId] = rrdRelativePath

            self.myLogger.notice("RRD db created successfully with %s new files" % len(commands))
        else:
            self.myLogger.debug3("RRD db created successfully - empty rrd create command")

        return 0


    def getMinHeartbeatFromDbForIds (self, ids):
        """
        Given a list of counter IDs, runs 'rrd info' for each counter, and returns a list of the current min-heartbeat
        value for each counter.
        ids is a list of elements, each element is (Opaque-Object, counterId).
          Opaque-Object is returned in the output
          counterId is counter ID
        Length of returned list is always identical to len(ids).
        Each element of returned list is a tuple (opaque-value, actualHeartbeat)
        If parsing of 'rrd info' output fails, returns None for each failed counter id.
        """

        self.myLogger.info("Execute RRD 'info' commands for %s counters", len(ids))

        self.myLogger.debug4("Start, ids=%s", ids)
        rrdUpdates = map(lambda x: (x[0], self.formatInfoCommand(x[1])), ids)
        self.myLogger.debug4("rrdUpdates=%s", rrdUpdates)
        retValues = self.executeRrdCommands(rrdUpdates)
        self.myLogger.debug4("executeRrdCommands() returned %s", retValues)

        heartbeats = []
        for retValue in retValues:
            opValue = retValue[0]
            commandSuccess = retValue[1][0]
            commandOutput = retValue[1][1]
            if not commandSuccess:
                self.myLogger.error("RRD 'info' command failed: commandOutput=%s", commandOutput)
                heartbeats.append((opValue, None))
            else:
                match = self.myReHeartbeat.search(commandOutput)
                if match:
                    heartbeats.append((opValue, int(match.group(1))))
                else:
                    self.myLogger.error("Can't parse heartbeat for rrd file: opValue=%s. commandOutput=%s", opValue, commandOutput)
                    heartbeats.append((opValue, None))

        self.myLogger.debug4("Returning heartbeats=%s", heartbeats)
        return heartbeats


    def __addCommandToFile (self, createNewFile, closeFileAfter, commandToBeAdded):
        try:
            # Start new file if requested
            if createNewFile:
                self.myCommandsFileIndex += 1
                fileName = os.path.join(self.myRRDComandFilesDirPath, str(self.myCommandsFileIndex))
                self.myCommandsFileHandle = open(fileName,"w")
                self.myLogger.debug5("Opened file index %s" % (self.myCommandsFileIndex))

            #Write
            self.myCommandsFileHandle.write("%s\n" % commandToBeAdded)
            self.myLogger.debug5("Wrote %s to file index %s" % (commandToBeAdded, self.myCommandsFileIndex))

            # Close file if requested
            if closeFileAfter:
                self.__closeCommandFile()

        except:
            self.myLogger.error("Failed. Exception info: %s" % formatExceptionInfo())
            return 11236


    def __closeCommandFile (self):
        self.myLogger.debug5("Closed file index %s" % (self.myCommandsFileIndex))
        self.myCommandsFileHandle.close()
        self.myCommandsFileHandle = None


    def __executeRRDCommandsFile (self):
        fileName = os.path.join(self.myRRDComandFilesDirPath, str(self.myCommandsFileIndex))
        command = "%s %s" % (self.myRRDToolWrapperExe, fileName)
        self.myLogger.debug1("Execute RRD command: %s" % command)

        startTime = time.time()
        commandResult = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
        (stdoutStr, stderrStr) = commandResult.communicate()
        execEndTime = time.time()
        execSpan = execEndTime - startTime
        self.myLogger.debug1("rrdtool execution time span %s" % execSpan)
        if not deleteFileIfNeeded (fileName):
            return (False, "Could not delete rrdtool commands file %s" % str(fileName))
        delEndTime = time.time()
        delSpan = delEndTime - execEndTime
        self.myLogger.debug1("Delete rrdfiles time span %s" % delSpan)
        if (stderrStr):
            return (False, stderrStr)
        if (stdoutStr):
            return (True, stdoutStr)
        # If we got here it means that no message was presented either in stdout & stderr = OK
        return (True, "ok")


    def __validateFilesMappingDictionary (self, rrdFileMapping):
        if rrdFileMapping is None:
            self.myLogger.notice("A problem occured while querying for the rrd files mapping - this will cause the script to exit")
            return False
        return True


    def setLogger (self, logger):
        self.myLogger = None
        self.myLogger = logger
