#!/usr/local/bin/python2.6
# 
# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# ver 1.0 
#
# Author: nirs
#

from a.infra.file.rotating_file_size_enforcer import RotatingFileSizeEnforcer
import shutil, os
import traceback, sys
import subprocess
import time
from datetime import datetime
from optparse import OptionParser, OptionGroup
import fnmatch
import glob
import re
import logging
import pprint
import json

#might be nice to make a func for every command I call etc' with all the format etc'
# most important: con string

# === Globals =====================================================================================

class SupportFileLevels:
    OUR_LEVEL_MINIMAL = 10
    OUR_LEVEL_STANDARD = 40
    OUR_LEVEL_EXTENDED = 70
    OUR_LEVEL_MAXIMAL = 100

  

class SupportFileMarkers:
    TARGET_DIR = "%TARGET"
    TEMP_DIR_TO_USE = "%TEMP"
    SUB_SYSTEM_BASE_DIR = "%SUB_SYSTEM_BASE_DIR"
    SUB_SYSTEM_CONST_DIR = "%SUB_SYSTEM_CONST_DIR"
    Q_SHELL_PROCESS = "%Q_SHELL_PROCESS"
    PID = "%PID"
    NETWORK_INTERFACE = "%NETWORK_INTERFACE"

class SupportFileCfg:
    DESCRIPTION_KEY_SHUT_ITEMS = "shut-items"
    DESCRIPTION_KEY_FORCED_ITEMS = "forced-items"
    DESCRIPTION_KEY_DEFUALT_LEVEL = "default-level"
    DESCRIPTION_KEY_SUBSYSTEMS_LEVELS = "subsystems-levels"
    DESCRIPTION_KEY_IS_UNSAFE = "is-unsafe"
    DESCRIPTION_KEY_REQUIRED_DISK_SPACE = "required-disk-space"

    def __init__ (self):
        self._shutFullIdPatterns = {}
        self._forcedFullIdPatterns = {}        
        self._defaultLevel = SupportFileLevels.OUR_LEVEL_STANDARD
        self._subSystemLevels = {}
        self._isUnsafe = False
        self._requiredDiskSpace = None

    def getShutDegree (self, subSystem, category, id):
        degree = 0
        fullId = SupportFileItem.s_getFullId(subSystem, category, id)
        for fullIdPattern in self._shutFullIdPatterns:
            if fnmatch.fnmatch(fullId, fullIdPattern):
                newDegree = self._shutFullIdPatterns[fullIdPattern]
                if newDegree > degree:
                    degree = newDegree                
        return degree

    def getForcedDegree (self, subSystem, category, id):
        degree = 0
        fullId = SupportFileItem.s_getFullId(subSystem, category, id)
        for fullIdPattern in self._forcedFullIdPatterns:
            if fnmatch.fnmatch(fullId, fullIdPattern):
                newDegree = self._forcedFullIdPatterns[fullIdPattern]
                if newDegree > degree:
                    degree = newDegree                
        return degree

    def isUnsafe (self):        
        return self._isUnsafe

    def getLevel (self, subSystem):
        if subSystem in self._subSystemLevels:
            return self._subSystemLevels[subSystem]
        return self._defaultLevel

    def getRequiredDiskSpace (self):
        return self._requiredDiskSpace

    def setUnsafe (self, isUnsafe):        
        self._isUnsafe = isUnsafe

    def shut (self, degree, subSystem="*", category="*", id="*"):
        fullId = SupportFileItem.s_getFullId(subSystem, category, id)
        self._shutFullIdPatterns[fullId]=degree

    def force (self, degree, subSystem="*", category="*", id="*"):
        fullId = SupportFileItem.s_getFullId(subSystem, category, id)
        self._forcedFullIdPatterns[fullId]=degree

    def setLevel (self, subSystem, level):
        self._subSystemLevels[subSystem] = level

    def setDefaultLevel (self, level):
        self._defaultLevel = level

    def setRequiredDiskSpace(self, requiredDiskSpace):
        self._requiredDiskSpace = requiredDiskSpace

    def describeAsDictionary (self):
        toReturn = {}
        toReturn[self.DESCRIPTION_KEY_SHUT_ITEMS] = self._shutFullIdPatterns
        toReturn[self.DESCRIPTION_KEY_FORCED_ITEMS] = self._forcedFullIdPatterns
        toReturn[self.DESCRIPTION_KEY_DEFUALT_LEVEL] = self._defaultLevel
        toReturn[self.DESCRIPTION_KEY_SUBSYSTEMS_LEVELS] = self._subSystemLevels
        toReturn[self.DESCRIPTION_KEY_IS_UNSAFE] = self._isUnsafe
        toReturn[self.DESCRIPTION_KEY_REQUIRED_DISK_SPACE] = self._requiredDiskSpace
        return toReturn

class SupportFileCreator:
    def __init__ (self):        
        self._subSystems = {}
        self._logLevel = logging.INFO
        self._supportFileCfg = SupportFileCfg()

    #########################################support file definition##################################################
    def settingsAddSubSystem (self, subSystemName, subSystemBaseDir, subSystemConstDir):       
        if subSystemName in self._subSystems:
            print "trying to re-add sub-system %s, skipping"%subSystemName
            return
        subSystem = SupportFileSubSystemSettings(subSystemName,                                                  
                                                 subSystemBaseDir = subSystemBaseDir, 
                                                 subSystemConstDir = subSystemConstDir)
        self._subSystems[subSystemName]=subSystem

    def settingsAddDirToList (self, subSystemName, id, level, directory, isRecursive, directoryToExclude, isSafe = False):
        if not subSystemName in self._subSystems:
            fullId = SupportFileItem.s_getFullId(subSystemName, SupportFileCategories.OUR_CAREGORY_DIRS_TO_LIST, id)
            print "trying to add item %s to sub-system %s. no such sub-system. skipping. "%(fullId, subSystemName)
            return
        self._subSystems[subSystemName].settingsAddDirToList (id=id, level=level, directory=directory, 
                                                              isRecursive=isRecursive, directoryToExclude=directoryToExclude, 
                                                              isSafe=isSafe)

    def settingsAddDirToCopy (self, subSystemName, id, level, directory, directoryToExclude, maxSizeToInclude, timeFilterStartEpoch, isSafe):
        if not subSystemName in self._subSystems:
            fullId = SupportFileItem.s_getFullId(subSystemName, SupportFileCategories.OUR_CAREGORY_DIRS_TO_COPY, id)
            print "trying to add item %s to sub-system %s. no such sub-system. skipping. "%(fullId, subSystemName)
            return
        self._subSystems[subSystemName].settingsAddDirToCopy (id=id, level=level, directory=directory, directoryToExclude=directoryToExclude, maxSizeToInclude=maxSizeToInclude, 
                                                              timeFilterStartEpoch=timeFilterStartEpoch, isSafe=isSafe)


    def settingsAddCmdToRun (self, subSystemName, id, level, cmd, additionalEnv, isSafe = False):
        if not subSystemName in self._subSystems:
            fullId = SupportFileItem.s_getFullId(subSystemName, SupportFileCategories.OUR_CAREGORY_LINUX_SHELL_CMDS, id)
            print "trying to add item %s to sub-system %s. no such sub-system. skipping. "%(fullId, subSystemName)
            return
        self._subSystems[subSystemName].settingsAddCmdToRun (id=id, level=level, cmd=cmd, 
                                                             additionalEnv=additionalEnv, isSafe=isSafe)

    def settingsAddQshellCmdToRun (self, subSystemName, id, level, processPattern, qShellCmd):
        if not subSystemName in self._subSystems:
            fullId = SupportFileItem.s_getFullId(subSystemName, SupportFileCategories.OUR_CAREGORY_Q_SHELL_CMDS, id)
            print "trying to add item %s to sub-system %s. no such sub-system. skipping. "%(fullId, subSystemName)
            return
        self._subSystems[subSystemName].settingsAddQshellCmdToRun (id=id, level=level, processPattern=processPattern, qShellCmd=qShellCmd)

    def settingsAddCliCmdToRun (self, subSystemName, id, level, cliCmd):
        if not subSystemName in self._subSystems:
            fullId = SupportFileItem.s_getFullId(subSystemName, SupportFileCategories.OUR_CAREGORY_CLI_CMDS, id)
            print "trying to add item %s to sub-system %s. no such sub-system. skipping. "%(fullId, subSystemName)
            return
        self._subSystems[subSystemName].settingsAddCliCmdToRun (id=id, level=level, cliCmd=cliCmd)


    def createSettingsDictionary (self):
        subsystems = {}
        for subsystem in self._subSystems:
            subsystems[subsystem] = self._subSystems[subsystem].describeAsDictionary(True)
        return subsystems

    def loadSettingsFromDictionary (self, subsystems):
        for subsystem in subsystems:            
             self._subSystems[subsystem] = SupportFileSubSystemSettings.s_createFromDictionary(subsystem, subsystems[subsystem])


    #########################################support file creation##################################################
    def initAddProcessInfo (self, subSystemName, process, obj):
        if not subSystemName in self._subSystems:
            print "trying to add daemon info of process %s to sub-system %s. no such sub-system. skipping. "%(process, subSystemName)
            return
        self._subSystems[subSystemName].initAddProcessInfo(process=process, obj=obj)

    def initAddNetworkInterfaceInfo (self, subSystemName, interfaceName, obj):
        if not subSystemName in self._subSystems:
            print "trying to add daemon info of network-interface %s to sub-system %s. no such sub-system. skipping. "%(interfaceName, subSystemName)
            return
        self._subSystems[subSystemName].initAddNetworkInterfaceInfo(interfaceName=interfaceName, obj=obj)

    def initSetCli (self, subSystemName, cliConnectionCommand):
        if not subSystemName in self._subSystems:
            print "trying to add cli info to sub-system %s. no such sub-system. skipping. "%(subSystemName)
            return
        self._subSystems[subSystemName].initSetCli(cliConnectionCommand)


    def initSetConfdCliConnection (self, subSystemName, process, obj):
        if not subSystemName in self._subSystems:
            print "trying to add daemon info of process %s to sub-system %s. no such sub-system. skipping. "%(process, subSystemName)
            return
        self._subSystems[subSystemName].initAddProcessInfo(process=process, obj=obj)

    def initSetLogLevel (self, logLevel):
        self._logLevel = logLevel

    def initCfg (self, supportFileCfg):
        self._supportFileCfg = supportFileCfg

    def initDirectories (self, gatheredFilesDir, tempDirToUse):        
        self._gatheredFilesDir = gatheredFilesDir
        self._supportDataDir = os.path.join(self._gatheredFilesDir, "support-data")
        self._tempDirToUse = tempDirToUse
        self._logDir = os.path.join(self._supportDataDir, "log")

    def createSupportFile (self, targetFileName):
        try:
            if os.path.exists(self._gatheredFilesDir): 
                shutil.rmtree(self._gatheredFilesDir)
            os.makedirs(self._gatheredFilesDir)
            os.makedirs(self._supportDataDir)

            if os.path.exists(self._tempDirToUse):                
                shutil.rmtree(self._tempDirToUse)
            os.makedirs(self._tempDirToUse)

            if not os.path.exists(self._logDir):                
                os.makedirs(self._logDir)        
        except:
            print "Failed to create base directories: %s.\naborting."%traceback.format_exc() 
            return 1

        if not self._supportFileCfg.getRequiredDiskSpace() is None:
            try:
                diskStats = os.statvfs(os.path.dirname(targetFileName))
                diskFreeSpace = (diskStats.f_bavail * diskStats.f_frsize)
                requiredDiskFreeSpace = int(self._supportFileCfg.getRequiredDiskSpace())
                if diskFreeSpace < requiredDiskFreeSpace:
                    print "Target disk space has only %d bytes free. %d bytes are required.\naborting."%(diskFreeSpace, requiredDiskFreeSpace)
                    return 1
            except:
                print "Failed to retrieve disk space for target file: %s.\naborting."%traceback.format_exc() 
                return 1

        self._initInternalsLogger()
        self._initSizesFile()
        self._initSetDirectories()
        self._initProcesses()
        self._initNetworkInterfaces()
        self._initCli()
        self._initCfg()
        self._createSubsysDirectories()
        self._createSupportFileDescription()
        self._filterItems()
        self._calcDirectories()
        self._replaceMarkers()
        self._createDirectories()
        self._createBaseDirSymlinks()
        self._createFiles()        
        
        tarMultiRecords = self._getTarMultiRecords()       
        gatheredDataTarRecord = SupportFileItem.TarRecord(".", self._gatheredFilesDir)
        gatheredDataTarMultiRecord = SupportFileItem.TarMultiRecord("gathered-files")
        gatheredDataTarMultiRecord.addRecord(gatheredDataTarRecord)
        #last files - including the logs. will be taken last. 
        tarMultiRecords.append(gatheredDataTarMultiRecord)

        try:
            fd = open(self._sizesFileName, "w")
            fd.write("%s,%s,%s,%s\n"%("item", "sub-items", "size", "tar-duratrion"))
            fd.close()
        except:
            self._log.exception("%s: Failed to update sizes file")

        for tarMultiRecord in tarMultiRecords:
            self._addToTar(targetFileName+".tar", tarMultiRecord)

        gzipCmd = "gzip %s"%targetFileName+".tar"
        rc = subprocess.call(gzipCmd, shell=True)
        if rc!=0:
            print "failed to compress tar file %s"%targetFileName
        

        try:
            shutil.rmtree(self._tempDirToUse)
            shutil.rmtree(self._gatheredFilesDir)
        except:
            #can no longer log. let it be
            pass

        return 0

    ###################################################private###############################
    def _addToTar (self, tempTarFileName, tarMultiRecord):
        sizeBefore = 0
        timeBefore = time.time()
        if os.path.exists(tempTarFileName):
            sizeBefore = os.path.getsize(tempTarFileName)
        self._log.info("start tar commands for item '%s' (%d sub items)", tarMultiRecord.itemId, len(tarMultiRecord.records))
        for tarRecord in tarMultiRecord.records:
            
            try:
                if not os.path.lexists(os.path.join(tarRecord.relativeTo,tarRecord.path)):
                    self._log.warning("%s: Cannot tar file '%s'. no such file", tarMultiRecord.itemId, tarRecord.path)
                    continue
                tarCommand = "tar --append --file %s --directory %s %s"%(tempTarFileName, tarRecord.relativeTo, tarRecord.path)
                for excludedPath in tarRecord.excluded:
                    tarCommand = tarCommand + " --exclude %s"%excludedPath
                self._log.debug("%s: Calling tar command: %s", tarMultiRecord.itemId, tarCommand)
                popen = subprocess.Popen(tarCommand, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                output = popen.communicate()[0]
                if popen.returncode!=0:
                    self._log.error("%s: Failed to tar file '%s'. output %s", tarMultiRecord.itemId, tarRecord.path, output)
                elif output!="":
                    self._log.info("%s: output while taring file '%s': %s", tarMultiRecord.itemId, tarRecord.path, output)
            except:
                self._log.exception("%s: Failed to tar record '%s'", tarMultiRecord.itemId, tarRecord)

        timeAfter = time.time()
        sizeAfter = 0
        if os.path.exists(tempTarFileName):
            sizeAfter = os.path.getsize(tempTarFileName)
        try:
            fd = open(self._sizesFileName, "a")
            fd.write("%s,%s,%d,%f\n"%(tarMultiRecord.itemId, len(tarMultiRecord.records), sizeAfter-sizeBefore, timeAfter-timeBefore))
            fd.close()
        except:
            self._log.exception("%s: Failed to update sizes file")

    

    def _initInternalsLogger (self):
        self._log = logging.Logger("support-file",logging.NOTSET)
        self._log.setLevel(self._logLevel)
        handler = logging.FileHandler(os.path.join(self._logDir,'support.log'))
        handler.setLevel(logging.NOTSET)
        formatter = logging.Formatter('%(levelname)s: %(asctime)s.%(msecs)03d %(message)s')
        handler.setFormatter(formatter)
        self._log.addHandler(handler)
        for subSystemName in sorted(self._subSystems):
            self._subSystems[subSystemName].initInternalsLogger(self._log)

    def _initSizesFile (self):
        self._sizesFileName = os.path.join(self._logDir, "statistics.csv")

    def _initSetDirectories (self):
        for subSystemName in sorted(self._subSystems):
            self._subSystems[subSystemName].initSetDirectories(gatheredFilesDir = os.path.join(self._supportDataDir, subSystemName), 
                                                               tempDirToUse = os.path.join(self._tempDirToUse, subSystemName))

    def _initProcesses (self):
        for subSystemName in sorted(self._subSystems):
            self._subSystems[subSystemName].initProcesses()

    def _initNetworkInterfaces (self):
        for subSystemName in sorted(self._subSystems):
            self._subSystems[subSystemName].initNetworkInterfaces()

    def _initCli (self):
        for subSystemName in sorted(self._subSystems):
            self._subSystems[subSystemName].initCli()

    def _initCfg (self):
        self._log.debug("calling SupportFileCreator:initCfg()") 
        for subSystemName in sorted(self._subSystems):
            self._subSystems[subSystemName].initCfg(self._supportFileCfg)

    
    def _createSubsysDirectories(self):
        for subSystemName in sorted(self._subSystems):
            self._subSystems[subSystemName].createSubsysDirectories()

    def _createSupportFileDescription(self):
        try:
            fileName = os.path.join(self._logDir, "cfg-description.txt")
            fd = open(fileName, "w")
            dataDict = self._supportFileCfg.describeAsDictionary()
            pprint.PrettyPrinter(stream=fd).pprint(dataDict)
            fd.close()
        except:
            self._log.exception("failed to create cfg description file")

        try:
            fileName = os.path.join(self._logDir, "settings.json")
            fd = open(fileName, "w")
            json.dump(self.createSettingsDictionary(), fd)            
            fd.close()
        except:
            self._log.exception("failed to create settings file")


        for subSystemName in sorted(self._subSystems):
            self._subSystems[subSystemName].createSupportFileDescription()


    def _filterItems (self):
        self._log.debug("calling SupportFileCreator:filterItems()") 
        for subSystemName in sorted(self._subSystems):
            self._subSystems[subSystemName].filterItems()


    def _calcDirectories (self):
        self._log.debug("calling SupportFileCreator:calcDirectories()") 
        for subSystemName in sorted(self._subSystems):
            self._subSystems[subSystemName].calcDirectories()


    def _replaceMarkers (self):
        self._log.debug("calling SupportFileCreator:replaceMarkers()") 
        for subSystemName in sorted(self._subSystems):
            self._subSystems[subSystemName].replaceMarkers()

    def _createDirectories (self):
        self._log.debug("calling SupportFileCreator:createDirectories()") 
        for subSystemName in sorted(self._subSystems):
            self._subSystems[subSystemName].createDirectories()

    def _createFiles (self):
        self._log.debug("calling SupportFileCreator:createFiles()") 
        for subSystemName in sorted(self._subSystems):
            self._subSystems[subSystemName].createFiles()

    def _createBaseDirSymlinks (self):
        self._log.debug("calling SupportFileCreator:_createBaseDirSymlinks()")         
        for subSystemName in sorted(self._subSystems):            
            self._subSystems[subSystemName].createBaseDirSymlinks(self._gatheredFilesDir)
            

    def _getTarMultiRecords (self):
        self._log.debug("calling SupportFileCreator:_getTarMultiRecords()") 

        toReturn = []

        for subSystemName in sorted(self._subSystems):
            toReturn += self._subSystems[subSystemName].getTarMultiRecords()            

        return toReturn

    


class SupportFileSubSystemSettings:
    DESCRIPTION_KEY_SUB_SYSTEM_BASE_DIR = "subsystem-base-dir"
    DESCRIPTION_KEY_SUB_SYSTEM_CONST_DIR = "subsystem-const-dir"
    DESCRIPTION_KEY_SUPPORT_FILE_ITEMS = "support-file-items"
    DESCRIPTION_KEY_SUPPORT_FILE_PROCESSES = "support-file-processes"
    DESCRIPTION_KEY_SUPPORT_FILE_NETWORK_INTERFACES = "support-network-interfaces"

    def __init__ (self, subSystem, subSystemBaseDir, subSystemConstDir):
        self._subSystem = subSystem
        self._subSystemBaseDir = subSystemBaseDir
        self._subSystemConstDir = subSystemConstDir
        self._supportFileItems = {}
        self._processInfos = {}
        self._networkInterfaceInfos = {}
        self._cliConnectionCommand = None


    def settingsAddDirToList (self, id, level, directory, isRecursive, directoryToExclude, isSafe = False):
        item = SupportFileItemDirToList(subSystem=self._subSystem, 
                                        id=id, level=level, 
                                        directory=directory, 
                                        isRecursive=isRecursive, 
                                        directoryToExclude=directoryToExclude,
                                        isSafe=isSafe)
        self._addSupportFileItem(item)

    def settingsAddDirToCopy (self, id, level, directory, directoryToExclude, maxSizeToInclude, timeFilterStartEpoch, isSafe):
        item = SupportFileItemDirToCopy(subSystem=self._subSystem, 
                                        id=id, level=level, directory=directory, directoryToExclude=directoryToExclude,
                                        maxSizeToInclude=maxSizeToInclude, timeFilterStartEpoch=timeFilterStartEpoch, isSafe=isSafe)
        self._addSupportFileItem(item)

    def settingsAddCmdToRun (self, id, level, cmd, additionalEnv, isSafe = False):
        item = SupportFileItemCmd(subSystem=self._subSystem, id=id, level=level, cmd=cmd, 
                                  additionalEnv=additionalEnv, isSafe = isSafe)
        self._addSupportFileItem(item)

    def settingsAddQshellCmdToRun (self, id, level, processPattern, qShellCmd):
        item = SupportFileItemQshellCmd(subSystem=self._subSystem, id=id, level=level, 
                                        processPattern=processPattern, 
                                        qShellCmd=qShellCmd, isSafe=False)
        self._addSupportFileItem(item)

    def settingsAddCliCmdToRun (self, id, level, cliCmd):
        item = SupportFileItemCliCmd(subSystem=self._subSystem, id=id, level=level, 
                                        cliCmd=cliCmd, isSafe=False)
        self._addSupportFileItem(item)

    def describeAsDictionary (self, settingsOnly):
        toReturn = {}
        toReturn[self.DESCRIPTION_KEY_SUB_SYSTEM_BASE_DIR] = self._subSystemBaseDir
        toReturn[self.DESCRIPTION_KEY_SUB_SYSTEM_CONST_DIR] = self._subSystemConstDir
        toReturn[self.DESCRIPTION_KEY_SUPPORT_FILE_ITEMS] = {}
        if not settingsOnly:
            toReturn[self.DESCRIPTION_KEY_SUPPORT_FILE_PROCESSES] = {}
            for process in self._processInfos:
                toReturn[self.DESCRIPTION_KEY_SUPPORT_FILE_PROCESSES][process] = self._processInfos[process].describeAsDictionary()
        if not settingsOnly:
            toReturn[self.DESCRIPTION_KEY_SUPPORT_FILE_NETWORK_INTERFACES] = {}
            for interface in self._networkInterfaceInfos:
                toReturn[self.DESCRIPTION_KEY_SUPPORT_FILE_NETWORK_INTERFACES][interface] = self._networkInterfaceInfos[interface].describeAsDictionary()
        for itemKey in sorted(self._supportFileItems):
            item = self._supportFileItems[itemKey]
            try:
                data = item.describeAsDictionary(settingsOnly)
            except:
                self._log.exception("failed to create description for %s", item.getFullId()) 
                data = "N/A"
            toReturn[self.DESCRIPTION_KEY_SUPPORT_FILE_ITEMS][item.getFullId()] = data
        return toReturn

    @classmethod
    def s_createFromDictionary (cls, subSystemName, dictionary):
        obj = SupportFileSubSystemSettings(subSystem = subSystemName, 
                                           subSystemBaseDir = dictionary[cls.DESCRIPTION_KEY_SUB_SYSTEM_BASE_DIR], 
                                           subSystemConstDir = dictionary[cls.DESCRIPTION_KEY_SUB_SYSTEM_CONST_DIR])
        for itemKey in dictionary[cls.DESCRIPTION_KEY_SUPPORT_FILE_ITEMS]:
            itemDictionary = dictionary[cls.DESCRIPTION_KEY_SUPPORT_FILE_ITEMS][itemKey]
            item = SupportFileItem.s_createFromDictionary(itemDictionary)
            obj._supportFileItems[item.getFullId()] = item

        return obj



    def _addSupportFileItem (self, item):
        if item.getFullId() in sorted(self._supportFileItems):
            print "trying to re-add item %s, skipping"%item.getFullId()
            return
        self._supportFileItems[item.getFullId()]=item


    def createSupportFileDescription (self):
        try:
            fileName = os.path.join(self._gatheredFilesDir, "description.txt")
            fd = open(fileName, "w")
            dataDict = self.describeAsDictionary(False)
            pprint.PrettyPrinter(stream=fd).pprint(dataDict)
            fd.close()
        except:
            self._log.exception("failed to create description file for subsystem %s", self._subSystem) 
            

    def initAddProcessInfo (self, process, obj):
        self._processInfos[process] = obj

    def initAddNetworkInterfaceInfo (self, interfaceName, obj):
        self._networkInterfaceInfos[interfaceName] = obj

    def initSetCli (self, cliConnectionCommand):
        self._cliConnectionCommand = cliConnectionCommand

    def initInternalsLogger (self, logger):
        self._log = logger
        for item in sorted(self._supportFileItems):
            self._supportFileItems[item].initLogger(logger)

    def initSetDirectories (self, gatheredFilesDir, tempDirToUse):
        self._log.debug("calling SupportFileSubSystemSettings:initSetDirectories(%s, %s) for subSystem %s", 
                         gatheredFilesDir, tempDirToUse, self._subSystem) 
        self._gatheredFilesDir = gatheredFilesDir
        self._tempDirToUse = tempDirToUse
        self._createdFilesTargetDir = os.path.join(self._gatheredFilesDir, "files")

    def initProcesses (self):
        for item in sorted(self._supportFileItems):
            self._supportFileItems[item].initProcesses(self._processInfos)

    def initNetworkInterfaces (self):
        for item in sorted(self._supportFileItems):
            self._supportFileItems[item].initNetworkInterfaces(self._networkInterfaceInfos)

    def initCli (self):
        if not self._cliConnectionCommand is None:
            for item in sorted(self._supportFileItems):
                self._supportFileItems[item].initCli(self._cliConnectionCommand)
    

    def initCfg (self, supportFileCfg):
        self._log.debug("calling SupportFileSubSystemSettings:initCfg() for subSystem %s", self._subSystem) 
        self._supportFileCfg = supportFileCfg
        for item in sorted(self._supportFileItems):
            self._supportFileItems[item].initCfg(supportFileCfg)

    def createSubsysDirectories (self):
        self._log.debug("calling SupportFileSubSystemSettings:createSubsysDirectories() for subSystem %s", self._subSystem) 
        try:
            if not os.path.exists(self._gatheredFilesDir):
                self._log.debug("creating directory '%s'", self._gatheredFilesDir)        
                os.makedirs(self._gatheredFilesDir)
            else:
                self._log.debug("directory '%s' already exists", self._gatheredFilesDir) 
    
            if not os.path.exists(self._tempDirToUse):
                self._log.debug("creating directory '%s'", self._tempDirToUse)        
                os.makedirs(self._tempDirToUse)
            else:
                self._log.debug("directory '%s' already exists", self._tempDirToUse) 

            if not os.path.exists(self._createdFilesTargetDir):
                self._log.debug("creating directory '%s'", self._createdFilesTargetDir)        
                os.makedirs(self._createdFilesTargetDir)
            else:
                self._log.debug("directory '%s' already exists", self._createdFilesTargetDir) 
        except:
            self._log.exception("failed to create direcotries for subsystem %s", self._subSystem) 



    def filterItems (self):
        self._log.debug("calling SupportFileSubSystemSettings:filterItems() for subSystem %s", self._subSystem) 
        filteredItems = {}
        for itemKey in sorted(self._supportFileItems):
            item = self._supportFileItems[itemKey]
            if item.shallRun():
                self._log.info("support file will include item '%s'", item.getFullId())
                filteredItems[itemKey] = item
            else:
                self._log.info("support file will NOT include item '%s'", item.getFullId())

        self._supportFileItems = filteredItems


    def calcDirectories (self):
        self._log.debug("calling SupportFileSubSystemSettings:calcDirectories() for subSystem %s", self._subSystem) 

        filteredItems = {}
        for itemKey in sorted(self._supportFileItems):
            item = self._supportFileItems[itemKey]
            try:
                item.calcDirectories (targetDir=self._gatheredFilesDir, 
                                      tempDirToUse=self._tempDirToUse, 
                                      createdFilesTargetDir=self._createdFilesTargetDir,
                                      subSystemBaseDir=self._subSystemBaseDir, 
                                      subSystemConstDir=self._subSystemConstDir)
                filteredItems[itemKey] = item
            except:
                self._log.exception("clac subdirectories failed on '%s'", item.getFullId()) 

        self._supportFileItems = filteredItems


    def replaceMarkers (self):
        self._log.debug("calling SupportFileSubSystemSettings:replaceMarkers() for subSystem %s", self._subSystem) 

        filteredItems = {}
        for itemKey in sorted(self._supportFileItems):
            item = self._supportFileItems[itemKey]
            try:
                item.replaceMarkers()
                filteredItems[itemKey] = item
            except:
                self._log.exception("markers replacement failed on '%s'", item.getFullId()) 

        self._supportFileItems = filteredItems

    def createDirectories (self):
        self._log.debug("calling SupportFileSubSystemSettings:createDirectories() for subSystem %s", self._subSystem) 

        filteredItems = {}
        for itemKey in sorted(self._supportFileItems):
            item = self._supportFileItems[itemKey]
            try:
                item.createDirectories()
                filteredItems[itemKey] = item
            except:
                self._log.exception("directories creation failed on '%s'", item.getFullId()) 

        self._supportFileItems = filteredItems

    def createBaseDirSymlinks (self, broughtFilesDir):
        self._log.debug("calling SupportFileSubSystemSettings:createBaseDirSymlinks()") 
        try:
            subSystemBaseDirRelPath = os.path.abspath(self.getSubSystemBaseDir())[1:]#removing the "/"
            supportFileRootRelPath = os.path.relpath(broughtFilesDir, self._createdFilesTargetDir)
            symlinkTargetPath = os.path.normpath(os.path.join(supportFileRootRelPath, subSystemBaseDirRelPath))
            os.symlink(symlinkTargetPath, 
                       os.path.join(self._createdFilesTargetDir, "base-dir"))
        except:
            self._log.exception("failed to create symlink to base dir for subsystem %s", 
                                self.getSubSystemName()) 


    def createFiles (self):
        self._log.debug("calling SupportFileSubSystemSettings:createFiles() for subSystem %s", self._subSystem) 

        filteredItems = {}
        for itemKey in sorted(self._supportFileItems):
            item = self._supportFileItems[itemKey]
            try:
                item.createFiles()
                filteredItems[itemKey] = item
            except:
                self._log.exception("files creation failed on '%s'", item.getFullId()) 

        self._supportFileItems = filteredItems

    def getTarMultiRecords (self):
        self._log.debug("calling SupportFileSubSystemSettings:getTarMultiRecords() for subSystem %s", self._subSystem) 

        records = [] 
        filteredItems = {}
        for itemKey in sorted(self._supportFileItems):
            item = self._supportFileItems[itemKey]
            try:
                record = item.getTarMultiRecord()
                if record is not None:
                    records.append(record)
                filteredItems[itemKey] = item
            except:
                self._log.exception("get list of files to copy failed on '%s'", item.getFullId()) 

        self._supportFileItems = filteredItems
        return records

    def getSubSystemName (self):
        return self._subSystem

    def getSubSystemBaseDir (self):
        return self._subSystemBaseDir

    def getSubSystemConstDir (self):
        return self._subSystemConstDir

    def getGatheredFilesDir (self):
        return self._gatheredFilesDir



class SupportFileItem:
    OUT_ID_SEP = "."

    DESCRIPTION_KEY_LEVEL = "level"
    DESCRIPTION_KEY_SUBSYS_LEVEL = "cfg-level-subsystem"
    DESCRIPTION_KEY_IS_SAFE = "is-safe"
    DESCRIPTION_KEY_FORCED_DEGREE = "cfg-degree-forced"
    DESCRIPTION_KEY_SHUT_DEGREE = "cfg-degree-shut"
    DESCRIPTION_KEY_IS_INCLUDED = "is-included"
    DESCRIPTION_KEY_CATEGORY = "category"
    DESCRIPTION_KEY_SUBSYSTEM = "subsystem"
    DESCRIPTION_KEY_ID = "id"
    DESCRIPTION_KEY_CATEGORY_DATA = "category-data"

    class TarRecord:
        def __init__ (self, path, relativeTo):
            self.path = path
            self.relativeTo = relativeTo
            self.excluded = []

        def addExcludedPath (self, pathToExclude):
            self.excluded.append(pathToExclude)

        def __repr__(self):
            return 'tar %s relative to %s (exclude %s)'%(self.path, self.relativeTo, self.excluded)

    class TarMultiRecord:
        def __init__ (self, itemId):
            self.itemId = itemId
            self.records = []

        def addRecord (self, tarRecord):
            self.records.append(tarRecord)

        def __repr__(self):
            return '%s: %s'%(self.itemId, self.records)


    @classmethod
    def s_getFullId (cls, subSystem, category, id):
        return cls.OUT_ID_SEP.join([subSystem, category, id])        

    def __init__ (self, subSystem, category, id, level, isSafe):
        self._category = category
        self._subSystem = subSystem
        self._id = id
        self._level = level
        self._isSafe = isSafe

        self._processInfos = {}
        self._networkInterfaceInfos = {}
        self._cliConnectionCommand = None

        self._requiresCreatedFilesDir = False
        self._requiresTempFilesDir = False

    def initLogger (self, logger):
        self._log = logger

    def initProcesses (self, processInfos):
        self._processInfos = processInfos

    def initNetworkInterfaces (self, networkInterfaceInfos):
        self._networkInterfaceInfos = networkInterfaceInfos

    def initCli (self, cliConnectionCommand):
        self._cliConnectionCommand = cliConnectionCommand

    def getFullId (self):
        return self.s_getFullId(self._subSystem, self._category, self._id)

    def initCfg (self, supportFileCfg):
        self._log.debug("calling SupportFileItem:initCfg(). id=%s", self.getFullId())     
        self._shutDegree = supportFileCfg.getShutDegree(self._subSystem, self._category, self._id)
        self._forcedDegree = supportFileCfg.getForcedDegree(self._subSystem, self._category, self._id)        
        self._subSystemLevel = supportFileCfg.getLevel(self._subSystem)

        if not self._isSafe and not supportFileCfg.isUnsafe():
            self._log.debug("Item '%s' is unsafe - will be omitted due to safe mode", self.getFullId())
            self._shallRun = False
        elif self._shutDegree > self._forcedDegree:
            self._log.debug("Item '%s' is shut (shut degree=%d, forced degree = %d)", self.getFullId(), self._shutDegree, self._forcedDegree)
            self._shallRun = False
        elif self._forcedDegree > self._shutDegree:
            self._log.debug("Item '%s' is forced (shut degree=%d, forced degree = %d)", self.getFullId(), self._shutDegree, self._forcedDegree)
            self._shallRun = True
        elif self._subSystemLevel < self._level:
            self._log.debug("Item '%s' level %d is below the threshold %d", self.getFullId(), self._level, self._subSystemLevel)
            self._shallRun = False
        else:
            self._log.debug("Item '%s' level %d is above the threshold %d and will be included", self.getFullId(), self._level, self._subSystemLevel)
            self._shallRun = True


    def shallRun (self):
        return self._shallRun
        

    def calcDirectories (self, targetDir, tempDirToUse, createdFilesTargetDir, subSystemBaseDir, subSystemConstDir):
        self._log.debug("calling SupportFileItem:calcDirectories(%s, %s, %s, %s, %s). id=%s", 
                        targetDir, tempDirToUse, createdFilesTargetDir, subSystemBaseDir, subSystemConstDir, self.getFullId())     
        self._targetDir = targetDir           
        self._subSystemBaseDir = subSystemBaseDir
        self._subSystemConstDir = subSystemConstDir
        self._createdFilesTargetDir = os.path.join(createdFilesTargetDir, self.getFullId())  
        self._tempDirToUse = os.path.join(tempDirToUse, self.getFullId())    


    def replaceMarkers (self):
        self._log.debug("calling SupportFileItem:replaceMarkers(). id=%s", self.getFullId())         

    def createDirectories (self):
        self._log.debug("calling SupportFileItem:createDirectories(). id=%s", self.getFullId()) 
        self._createDirIfNeeded(self._targetDir)   
        if self._requiresCreatedFilesDir:
            self._createDirIfNeeded(self._createdFilesTargetDir)         
        if self._requiresTempFilesDir:
            self._createDirIfNeeded(self._tempDirToUse)
        

    def createFiles(self):
        self._log.debug("calling SupportFileItem:createFiles(). id=%s", self.getFullId())        

    def getTarMultiRecord (self):
        self._log.debug("calling SupportFileItem:getTarMultiRecord(). will return None. id=%s", self.getFullId())
        return None

    def describeAsDictionary (self, settingsOnly):
        toReturn = {}
        toReturn[self.DESCRIPTION_KEY_LEVEL]=self._level
        toReturn[self.DESCRIPTION_KEY_IS_SAFE]=self._isSafe
        toReturn[self.DESCRIPTION_KEY_CATEGORY]=self._category
        toReturn[self.DESCRIPTION_KEY_SUBSYSTEM]=self._subSystem
        toReturn[self.DESCRIPTION_KEY_ID]=self._id
        toReturn[self.DESCRIPTION_KEY_CATEGORY_DATA]=self.describeAsDictionaryCategorySpecific(settingsOnly)
        if not settingsOnly:
            toReturn[self.DESCRIPTION_KEY_SUBSYS_LEVEL]=self._subSystemLevel
            toReturn[self.DESCRIPTION_KEY_FORCED_DEGREE]=self._forcedDegree
            toReturn[self.DESCRIPTION_KEY_SHUT_DEGREE]=self._shutDegree
            toReturn[self.DESCRIPTION_KEY_IS_INCLUDED]=self._shallRun
        return toReturn


    def describeAsDictionaryCategorySpecific (self, settingsOnly):
        __pychecker__ = 'no-argsused'        
        return {}

    @classmethod
    def s_createFromDictionary (cls, dictionary):
        category = dictionary[cls.DESCRIPTION_KEY_CATEGORY]
        return SupportFileCategories.classes[category].s_createFromDictionary(dictionary)
    
    def _getAsList(self, obj):
        if isinstance(obj, list):
            return obj
        return [obj]

    def _runCommands (self, commands, outputFileName, cwd = None, env = None):
        fd = open(outputFileName, "w")
        for command in commands:
            fd.write("output of command: %s\n"%command)
            fd.flush()
            self._log.debug("calling command '%s' (cwd = %s, env=%s). output will be written to '%s'", command, cwd, env, outputFileName)
            rc = subprocess.call(command, shell=True, stdout=fd, stderr=subprocess.STDOUT, cwd = cwd, env = env)
            if rc != 0:
                self._log.error("command '%s' failed. Return code %d", command, rc)
            else:
                self._log.debug("command '%s' succeed", command)
            fd.write("rc = %d\n"%rc)
        fd.close()

    def _replaceMarkers (self, list):
        newList1 = []
        for string in list:
            newStr = str(string)
            newStr = re.sub(SupportFileMarkers.TARGET_DIR, self._createdFilesTargetDir, newStr)
            newStr = re.sub(SupportFileMarkers.TEMP_DIR_TO_USE, self._tempDirToUse, newStr)
            newStr = re.sub(SupportFileMarkers.SUB_SYSTEM_BASE_DIR, self._subSystemBaseDir, newStr)
            newStr = re.sub(SupportFileMarkers.SUB_SYSTEM_CONST_DIR, self._subSystemConstDir, newStr)
            newList1.append(newStr)        

        newList2 = []
        for string in newList1:
            if string.find(SupportFileMarkers.PID) == -1:
                newList2.append(string)
            else:
                for process in self._processInfos:
                    pid = self._processInfos[process].getPid()
                    if not pid is None:
                        self._log.debug("found matching process for flag PID: %s. updating command %s", process, string)
                        newStr = re.sub(SupportFileMarkers.PID, str(pid), string)
                        newList2.append(newStr)
            
        newList3 = []
        for string in newList2:
            if string.find(SupportFileMarkers.NETWORK_INTERFACE) == -1:
                newList3.append(string)
            else:
                for networkInterface in self._networkInterfaceInfos:
                    interfaceName = self._networkInterfaceInfos[networkInterface].getInterfaceName()
                    if not interfaceName is None:
                        self._log.debug("found matching network interface for flag NETWORK_INTERFACE: %s. updating command %s", interfaceName, string)
                        newStr = re.sub(SupportFileMarkers.NETWORK_INTERFACE, str(interfaceName), string)
                        newList3.append(newStr)
            
        if list != newList3:
            self._log.debug("replaced %s ==> %s", list, newList3)

        return newList3


    def _createDirIfNeeded (self, directory):
        if not os.path.exists(directory):
            self._log.debug("creating directory '%s'", directory)        
            os.makedirs(directory)
        else:
            self._log.debug("directory '%s' already exists", directory) 




class SupportFileItemDirToList(SupportFileItem):
    DESCRIPTION_KEY_DIR_PATTERN = "directory-pattern"
    DESCRIPTION_KEY_DIR_TO_EXCLUDE = "directory-to-exclude"
    DESCRIPTION_KEY_IS_RECURSIVE = "is-recursive"

    def __init__ (self, subSystem, id, level, directory, isRecursive, directoryToExclude, isSafe = False):
        SupportFileItem.__init__(self, subSystem=subSystem,
                                 category=SupportFileCategories.OUR_CAREGORY_DIRS_TO_LIST, 
                                 id=id, level=level, isSafe=isSafe)
        self._directories = self._getAsList(directory)        
        self._isRecursive = isRecursive
        self._directoriesToExclude = self._getAsList(directoryToExclude)

    @classmethod
    def s_createFromDictionary (cls, dictionary):        
        return SupportFileItemDirToList(subSystem = dictionary[cls.DESCRIPTION_KEY_SUBSYSTEM], 
                                        id = dictionary[cls.DESCRIPTION_KEY_ID], 
                                        level = dictionary[cls.DESCRIPTION_KEY_LEVEL], 
                                        directory = dictionary[cls.DESCRIPTION_KEY_CATEGORY_DATA][cls.DESCRIPTION_KEY_DIR_PATTERN], 
                                        isRecursive = dictionary[cls.DESCRIPTION_KEY_CATEGORY_DATA][cls.DESCRIPTION_KEY_IS_RECURSIVE], 
                                        directoryToExclude = dictionary[cls.DESCRIPTION_KEY_CATEGORY_DATA][cls.DESCRIPTION_KEY_DIR_TO_EXCLUDE], 
                                        isSafe = dictionary[cls.DESCRIPTION_KEY_IS_SAFE])

    def calcDirectories (self, targetDir, tempDirToUse, createdFilesTargetDir, subSystemBaseDir, subSystemConstDir):
        SupportFileItem.calcDirectories(self, targetDir, tempDirToUse, createdFilesTargetDir, subSystemBaseDir, subSystemConstDir)    
        self._log.debug("calling SupportFileItemDirToList:calcDirectories(%s, %s, %s, %s, %s). id=%s", 
                        targetDir, tempDirToUse, createdFilesTargetDir, subSystemBaseDir, subSystemConstDir, self.getFullId())         
        self._targetDir = os.path.join(targetDir, "listed-dirs")
        self._log.debug("target dir for id='%s' is: %s", self.getFullId(), self._targetDir)           


    def replaceMarkers (self):
        SupportFileItem.replaceMarkers(self)
        self._log.debug("calling SupportFileItemDirToList:replaceMarkers(). id=%s", self.getFullId())  
        self._directories = self._replaceMarkers(self._directories)
        self._directoriesToExclude = self._replaceMarkers(self._directoriesToExclude)

    def createFiles(self):  
        SupportFileItem.createFiles(self)
        self._log.debug("calling SupportFileItemDirToList:createFiles(). id=%s", self.getFullId())                        

        outputFileName = os.path.join(self._targetDir, self.getFullId()+".txt")
        commands = []
        for directoryPattern in self._directories:
            for directory in glob.glob(directoryPattern):
                self._log.debug("%s dirs to list - found directory '%s'", self.getFullId(), directory)   
                if self._isRecursive:
                    pruneFlag = ""
                    if self._directoriesToExclude:
                        dirsToSkipStrs = []                        
                        for pattern in self._directoriesToExclude:
                            dirsToSkipStrs.append(' -wholename "%s" '%pattern)
                        pruneFlag = "-o".join(dirsToSkipStrs)
                        pruneFlag = "\("+pruneFlag+"\) -prune -o"

                    commands.append("find %s %s -ls"%(directory, pruneFlag))
                else:
                    commands.append("find %s -maxdepth 1 -ls"%directory)

        self._runCommands(commands, outputFileName)

    def describeAsDictionaryCategorySpecific (self, settingsOnly):
        toReturn = SupportFileItem.describeAsDictionaryCategorySpecific (self, settingsOnly)
        toReturn[self.DESCRIPTION_KEY_DIR_PATTERN]=self._directories
        toReturn[self.DESCRIPTION_KEY_DIR_TO_EXCLUDE]=self._directoriesToExclude
        toReturn[self.DESCRIPTION_KEY_IS_RECURSIVE]=self._isRecursive
        return toReturn



class SupportFileItemDirToCopy(SupportFileItem):
    DESCRIPTION_KEY_DIR_PATTERN = "directory-pattern"
    DESCRIPTION_KEY_DIR_TO_EXCLUDE_PATTERN = "directory-to-exclude-pattern"
    DESCRIPTION_KEY_MAX_SIZE_TO_INCLUDE = "max-size-to-include"
    DESCRIPTION_KEY_TIME_LIMIT = "time-limit"

    def __init__ (self, subSystem, id, level, directory, directoryToExclude, maxSizeToInclude, timeFilterStartEpoch, isSafe):
        SupportFileItem.__init__(self, subSystem=subSystem,
                                 category=SupportFileCategories.OUR_CAREGORY_DIRS_TO_COPY, 
                                 id=id, level=level, isSafe=isSafe)
        self._directories = self._getAsList(directory)
        self._directoriesToExclude = self._getAsList(directoryToExclude)
        self._maxSizeToInclude = maxSizeToInclude
        self._timeFilterStartEpoch = timeFilterStartEpoch 

    @classmethod
    def s_createFromDictionary (cls, dictionary):        
        return SupportFileItemDirToCopy(subSystem = dictionary[cls.DESCRIPTION_KEY_SUBSYSTEM], 
                                        id = dictionary[cls.DESCRIPTION_KEY_ID], 
                                        level = dictionary[cls.DESCRIPTION_KEY_LEVEL], 
                                        directory = dictionary[cls.DESCRIPTION_KEY_CATEGORY_DATA][cls.DESCRIPTION_KEY_DIR_PATTERN], 
                                        directoryToExclude = dictionary[cls.DESCRIPTION_KEY_CATEGORY_DATA][cls.DESCRIPTION_KEY_DIR_TO_EXCLUDE_PATTERN], 
                                        isSafe = dictionary[cls.DESCRIPTION_KEY_IS_SAFE],
                                        maxSizeToInclude = dictionary[cls.DESCRIPTION_KEY_CATEGORY_DATA][cls.DESCRIPTION_KEY_MAX_SIZE_TO_INCLUDE],
                                        timeFilterStartEpoch = dictionary[cls.DESCRIPTION_KEY_CATEGORY_DATA][cls.DESCRIPTION_KEY_TIME_LIMIT])


    def replaceMarkers (self):
        self._log.debug("calling SupportFileItemDirToCopy:replaceMarkers(). id=%s", self.getFullId())  
        SupportFileItem.replaceMarkers(self)
        self._directories = self._replaceMarkers(self._directories)
        self._directoriesToExclude = self._replaceMarkers(self._directoriesToExclude)

    def getTarMultiRecord (self):
        toReturn = SupportFileItem.getTarMultiRecord(self)
        if toReturn is None:
            toReturn = self.TarMultiRecord(self.getFullId())

        directoriesToExclude = []
        for directoryPattern in self._directoriesToExclude:
            directoriesToExclude += glob.glob(directoryPattern)
        directoriesToExcludeTmp = []
        for dirToExc in directoriesToExclude:#yuck, need to use map here
            directoriesToExcludeTmp.append(os.path.abspath(dirToExc))
        directoriesToExclude = directoriesToExcludeTmp

        for directoryPattern in self._directories:
            for directory in glob.glob(directoryPattern):
                directory = os.path.abspath(directory)
                if self._maxSizeToInclude or self._timeFilterStartEpoch:
                    self._log.info("Element ID %s: maxSizeToInclude: %s time filter: %s", self._id, self._maxSizeToInclude, self._timeFilterStartEpoch)
                    listDir = os.listdir(directory)
                    for entry in listDir:
                        entryPath = os.path.join(directory, entry)
                        addRecord = True
                        if os.path.isfile(entryPath):
                            if self._timeFilterStartEpoch and (RotatingFileSizeEnforcer.s_compareFileTimeStamp(self._timeFilterStartEpoch, entryPath) is False):
                                addRecord = False
                                self._log.info("Element ID %s: Excluding file %s due to time", self._id, entryPath)
                            if addRecord and self._maxSizeToInclude:
                                try:
                                    fileSize = os.path.getsize(entryPath)
                                except os.error as e:
                                    self._log.warning("%s: os.path.getsize() threw an exception: %s", entryPath, e)
                                    continue
                                else:
                                    if fileSize > self._maxSizeToInclude:
                                        #create two new files: tail and head of the existing oversize file 
                                        self._log.info("Element ID %s: Trimming file %s due to size=%s, larger than %s", self._id, entryPath, fileSize, self._maxSizeToInclude)
                                        addRecord = False
                                        self._cutFileAndAddToTarRecords (entryPath, 0, self._maxSizeToInclude/2, 'HEAD_FOR_SUPPORT_FILE', toReturn, self._tempDirToUse)
                                        self._cutFileAndAddToTarRecords (entryPath, fileSize - self._maxSizeToInclude/2, self._maxSizeToInclude/2, 
                                                                         'TAIL_FOR_SUPPORT_FILE', toReturn, self._tempDirToUse) 
                        else: # entryPath is directory
                            for dirToExclude in directoriesToExclude:
                                if self._shouldDirBeExcluded (dirToExclude, entryPath):
                                    addRecord = False
                                    break
                        if addRecord:
                            self._log.info("Element ID %s: Packing file  %s, relative to /", self._id, entryPath[1:])
                            toReturn.addRecord(self.TarRecord(entryPath[1:], "/"))
                else:
                    tarRecord = self.TarRecord(directory[1:], "/")
                    for dirToExclude in directoriesToExclude:
                        if self._shouldDirBeExcluded (dirToExclude, directory):
                            tarRecord.addExcludedPath(dirToExclude[1:])
                    toReturn.addRecord(tarRecord)
        self._log.debug("calling SupportFileItemDirToCopy:getTarMultiRecord(). id=%s. will return: %s", self.getFullId(), str(toReturn))
        return toReturn

    def describeAsDictionaryCategorySpecific (self, settingsOnly):
        toReturn = SupportFileItem.describeAsDictionaryCategorySpecific (self, settingsOnly)
        toReturn[self.DESCRIPTION_KEY_DIR_PATTERN]=self._directories
        toReturn[self.DESCRIPTION_KEY_DIR_TO_EXCLUDE_PATTERN]=self._directoriesToExclude
        toReturn[self.DESCRIPTION_KEY_MAX_SIZE_TO_INCLUDE]=self._maxSizeToInclude
        toReturn[self.DESCRIPTION_KEY_TIME_LIMIT]=self._timeFilterStartEpoch
        return toReturn

    def _shouldDirBeExcluded (self, dirToExclude, directory):
        #test if subpath
        retVal = False
        directoryL = directory.rstrip(os.sep).split(os.sep)
        dirToExcludeL = dirToExclude.rstrip(os.sep).split(os.sep)
        if len(directoryL) <= len(dirToExcludeL) and dirToExcludeL[:len(directoryL)] == directoryL:
            retVal = True
        return retVal

    def _cutFileAndAddToTarRecords (self, filePath, seekPos, size, suffix, recordsList, relativePath):
        try:
            orgFile = open(filePath, 'r')
        except IOError as e:
            self._log.warning("file='%s' mode=%s open raised exception=%s", filePath, 'r', e) 
            return

        self._log.info("Element ID %s: _cutFileAndAddToTarRecords(): filePath=%s, suffix=%s, relativePath=%s", self._id, filePath, suffix, relativePath)
        newFileName = filePath + '.' + suffix
        # Make sure newFileName is not absolute, we want it as a relative path
        while newFileName[0] == os.sep:
            newFileName = newFileName[1:]

        fullPath = os.path.join(relativePath, newFileName)
        dirName = os.path.dirname(fullPath)

        try:
            if not os.path.exists(dirName): 
                self._log.info("Element ID %s: Creating dir %s", self._id, dirName)
                os.makedirs(dirName)       
        except os.error as e:
            self._log.warning("Failed to create directories='%s' for the absolute file path='%s'", dirName, fullPath)
            orgFile.close() 
            return 
        
        try:
            newFile = open(fullPath, 'w')
        except IOError as e:
            self._log.warning("file='%s' mode=%s open raised exception=%s", newFileName, 'w', e) 
            orgFile.close()
            return

        orgFile.seek(seekPos)
        newFile.write(orgFile.read(size))
        orgFile.close()
        newFile.close()
        self._log.info("Element ID %s: _cutFileAndAddToTarRecords(): Adding record, newFileName=%s, relativePath=%s", self._id, newFileName, relativePath)
        recordsList.addRecord(self.TarRecord(newFileName, relativePath))

class SupportFileItemCmd(SupportFileItem):
    DESCRIPTION_KEY_CMD = "cmd"
    DESCRIPTION_KEY_ADDITIONAL_ENV = "additional-env"

    def __init__ (self, subSystem, id, level, cmd, additionalEnv = {}, isSafe = False):
        SupportFileItem.__init__(self, subSystem=subSystem,
                                 category=SupportFileCategories.OUR_CAREGORY_LINUX_SHELL_CMDS, 
                                 id=id, level=level,isSafe=isSafe)
        self._cmds = self._getAsList(cmd)
        self._additionalEnv = additionalEnv
        self._requiresCreatedFilesDir = (self._cmds[0].find(SupportFileMarkers.TARGET_DIR)!=-1)
        self._requiresTempFilesDir = (self._cmds[0].find(SupportFileMarkers.TEMP_DIR_TO_USE)!=-1)        


    @classmethod
    def s_createFromDictionary (cls, dictionary):        
        return SupportFileItemCmd(subSystem = dictionary[cls.DESCRIPTION_KEY_SUBSYSTEM], 
                                  id = dictionary[cls.DESCRIPTION_KEY_ID], 
                                  level = dictionary[cls.DESCRIPTION_KEY_LEVEL], 
                                  cmd = dictionary[cls.DESCRIPTION_KEY_CATEGORY_DATA][cls.DESCRIPTION_KEY_CMD], 
                                  additionalEnv = dictionary[cls.DESCRIPTION_KEY_CATEGORY_DATA][cls.DESCRIPTION_KEY_ADDITIONAL_ENV], 
                                  isSafe = dictionary[cls.DESCRIPTION_KEY_IS_SAFE])



    def calcDirectories (self, targetDir, tempDirToUse, createdFilesTargetDir, subSystemBaseDir, subSystemConstDir):
        SupportFileItem.calcDirectories(self, targetDir, tempDirToUse, createdFilesTargetDir, subSystemBaseDir, subSystemConstDir)    
        self._log.debug("calling SupportFileItemCmd:calcDirectories(%s, %s, %s, %s, %s). id=%s", 
                        targetDir, tempDirToUse, createdFilesTargetDir, subSystemBaseDir, subSystemConstDir, self.getFullId())   

        self._targetDir = os.path.join(targetDir, "commands") 


    def replaceMarkers (self):
        SupportFileItem.replaceMarkers(self)
        self._log.debug("calling SupportFileItemCmd:replaceMarkers(). id=%s", self.getFullId())  
        self._cmds = self._replaceMarkers(self._cmds)
        for key in self._additionalEnv:
            vals = [self._additionalEnv[key]]
            vals = self._replaceMarkers(vals)
            if len(vals)>1:
                self._log.warning("env var '%s' was expanded to more then one item (%s), taking only the first. id=%s", 
                                  key, vals, self.getFullId())  
            self._additionalEnv[key] = vals[0]

    def createFiles(self):  
        SupportFileItem.createFiles(self)
        self._log.debug("calling SupportFileItemCmd:createFiles(). id=%s", self.getFullId())                        
        outputFileName = os.path.join(self._targetDir, self.getFullId()+".txt")
        env = dict(os.environ.items() + self._additionalEnv.items())
        self._runCommands(self._cmds, outputFileName, env = env)

    def describeAsDictionaryCategorySpecific (self, settingsOnly):
        toReturn = SupportFileItem.describeAsDictionaryCategorySpecific (self, settingsOnly)
        toReturn[self.DESCRIPTION_KEY_CMD]=self._cmds     
        toReturn[self.DESCRIPTION_KEY_ADDITIONAL_ENV]=self._additionalEnv     
        return toReturn


class SupportFileItemQshellCmd(SupportFileItem):
    DESCRIPTION_KEY_Q_SHELL_CMD = "q-shell-cmd"
    DESCRIPTION_KEY_PROCESS_PATTERN = "process-pattern"

    def __init__ (self, subSystem, id, level, processPattern, qShellCmd, isSafe=False):
        SupportFileItem.__init__(self, subSystem=subSystem,
                                 category=SupportFileCategories.OUR_CAREGORY_Q_SHELL_CMDS, 
                                 id=id, level=level, isSafe=isSafe)
        self._processPattern = processPattern
        self._qShellCmds = self._getAsList(qShellCmd)
        self._requiresCreatedFilesDir = (self._qShellCmds[0].find(SupportFileMarkers.TARGET_DIR)!=-1)
        self._requiresTempFilesDir = (self._qShellCmds[0].find(SupportFileMarkers.TEMP_DIR_TO_USE)!=-1)        
        
    @classmethod
    def s_createFromDictionary (cls, dictionary):        
        return SupportFileItemQshellCmd(subSystem = dictionary[cls.DESCRIPTION_KEY_SUBSYSTEM], 
                                        id = dictionary[cls.DESCRIPTION_KEY_ID], 
                                        level = dictionary[cls.DESCRIPTION_KEY_LEVEL], 
                                        processPattern = dictionary[cls.DESCRIPTION_KEY_CATEGORY_DATA][cls.DESCRIPTION_KEY_PROCESS_PATTERN], 
                                        qShellCmd = dictionary[cls.DESCRIPTION_KEY_CATEGORY_DATA][cls.DESCRIPTION_KEY_Q_SHELL_CMD], 
                                        isSafe = dictionary[cls.DESCRIPTION_KEY_IS_SAFE])

    def calcDirectories (self, targetDir, tempDirToUse, createdFilesTargetDir, subSystemBaseDir, subSystemConstDir):
        SupportFileItem.calcDirectories(self, targetDir, tempDirToUse, createdFilesTargetDir, subSystemBaseDir, subSystemConstDir)    
        self._log.debug("calling SupportFileItemQshellCmd:calcDirectories(%s, %s, %s, %s, %s). id=%s", 
                        targetDir, tempDirToUse, createdFilesTargetDir, subSystemBaseDir, subSystemConstDir, self.getFullId())         
        self._targetDir = os.path.join(targetDir, "q-shell-commands")
        self._log.debug("target dir for id='%s' is: %s", self.getFullId(), self._targetDir)           


    def replaceMarkers (self):
        SupportFileItem.replaceMarkers(self)
        self._log.debug("calling SupportFileItemQshellCmd:replaceMarkers(). id=%s", self.getFullId())  
        self._qShellCmds = self._replaceMarkers(self._qShellCmds)

    def createFiles(self):  
        SupportFileItem.createFiles(self)
        self._log.debug("calling SupportFileItemQshellCmd:createFiles(). id=%s", self.getFullId())                        

        outputFileName = os.path.join(self._targetDir, self.getFullId()+".txt")

        mathchingProcesses = []
        for process in self._processInfos:
            if self._processInfos[process].isSupportQShell() and fnmatch.fnmatch(process, self._processPattern):
                mathchingProcesses.append(process)
        
        self._log.debug("calling q-shell commands '%s' on processes %s. output will be written to '%s'", 
                        self._qShellCmds, mathchingProcesses, outputFileName)


        outputFile = open(outputFileName, 'w')
        for qShellCmd in self._qShellCmds:
            for process in mathchingProcesses:
                command = re.sub(SupportFileMarkers.Q_SHELL_PROCESS, process, qShellCmd)
                outputFile.write("running command: %s\n"%command)
                outputFile.flush()
                (error, output) = self._processInfos[process].runShellCmd(command)
                if not error is None:
                    self._log.error("q-shell command '%s' failed. %s", command, error)
                    outputFile.write("error:\n"+error+"\n\n")
                else:
                    self._log.debug("q-shell command '%s' succeed", command)
                
                outputFile.write("output:\n"+output+"\n\n")
        
        outputFile.close()

    def describeAsDictionaryCategorySpecific (self, settingsOnly):
        toReturn = SupportFileItem.describeAsDictionaryCategorySpecific (self, settingsOnly)
        toReturn[self.DESCRIPTION_KEY_Q_SHELL_CMD]=self._qShellCmds        
        toReturn[self.DESCRIPTION_KEY_PROCESS_PATTERN]=self._processPattern
        return toReturn

        
class SupportFileItemCliCmd(SupportFileItem):
    DESCRIPTION_KEY_CLI_CMD = "cli-cmd"

    def __init__ (self, subSystem, id, level, cliCmd, isSafe=False):
        SupportFileItem.__init__(self, subSystem=subSystem,
                                 category=SupportFileCategories.OUR_CAREGORY_CLI_CMDS, 
                                 id=id, level=level, isSafe=isSafe)
        self._cliCmds = self._getAsList(cliCmd)
        self._requiresCreatedFilesDir = (self._cliCmds[0].find(SupportFileMarkers.TARGET_DIR)!=-1)
        self._requiresTempFilesDir = (self._cliCmds[0].find(SupportFileMarkers.TEMP_DIR_TO_USE)!=-1)        

    @classmethod
    def s_createFromDictionary (cls, dictionary):        
        return SupportFileItemCliCmd(subSystem = dictionary[cls.DESCRIPTION_KEY_SUBSYSTEM], 
                                        id = dictionary[cls.DESCRIPTION_KEY_ID], 
                                        level = dictionary[cls.DESCRIPTION_KEY_LEVEL], 
                                        cliCmd = dictionary[cls.DESCRIPTION_KEY_CATEGORY_DATA][cls.DESCRIPTION_KEY_CLI_CMD], 
                                        isSafe = dictionary[cls.DESCRIPTION_KEY_IS_SAFE])

    def calcDirectories (self, targetDir, tempDirToUse, createdFilesTargetDir, subSystemBaseDir, subSystemConstDir):
        SupportFileItem.calcDirectories(self, targetDir, tempDirToUse, createdFilesTargetDir, subSystemBaseDir, subSystemConstDir)    
        self._log.debug("calling SupportFileItemCliCmd:calcDirectories(%s, %s, %s, %s, %s). id=%s", 
                        targetDir, tempDirToUse, createdFilesTargetDir, subSystemBaseDir, subSystemConstDir, self.getFullId())         
        self._targetDir = os.path.join(targetDir, "cli-commands")
        self._log.debug("target dir for id='%s' is: %s", self.getFullId(), self._targetDir)           


    def replaceMarkers (self):
        SupportFileItem.replaceMarkers(self)
        self._log.debug("calling SupportFileItemCliCmd:replaceMarkers(). id=%s", self.getFullId())  
        self._cliCmds = self._replaceMarkers(self._cliCmds)

    def createFiles(self):  
        SupportFileItem.createFiles(self)
        self._log.debug("calling SupportFileItemCliCmd:createFiles(). id=%s", self.getFullId())                        

        if self._cliConnectionCommand is None:
            self._log.error("calling SupportFileItemCliCmd:createFiles() without a cli connection. id=%s", self.getFullId())
            return
        

        outputFileName = os.path.join(self._targetDir, self.getFullId()+".txt")

        self._log.debug("calling cli commands '%s'. output will be written to '%s'", 
                        self._cliCmds, outputFileName)


        outputFile = open(outputFileName, 'w')
        for cliCmd in self._cliCmds:
            cliCmd=cliCmd.strip()
            outputFile.write("running command: %s\n"%cliCmd)
            outputFile.flush()
            cliCmd += "\n"
            popen = subprocess.Popen(self._cliConnectionCommand, shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            output = popen.communicate(input=cliCmd)[0]
            outputFile.write("output:\n")
            outputFile.write(output)
            outputFile.write("\nreturn code: %d\n"%popen.returncode)
            if popen.returncode != 0 :
                self._log.error("cli command '%s' failed. return-code: %d", cliCmd, popen.returncode)                
            else:
                self._log.debug("cli command '%s' succeed", cliCmd)

        outputFile.close()

    
    def describeAsDictionaryCategorySpecific (self, settingsOnly):
        toReturn = SupportFileItem.describeAsDictionaryCategorySpecific (self, settingsOnly)
        toReturn[self.DESCRIPTION_KEY_CLI_CMD]=self._cliCmds        
        return toReturn

        
        
                
class SupportFileCategories:
    OUR_CAREGORY_DIRS_TO_LIST   = "dirs-to-list"
    OUR_CAREGORY_DIRS_TO_COPY = "dirs-to-copy"
    OUR_CAREGORY_LINUX_SHELL_CMDS = "linux-shell-cmds"
    OUR_CAREGORY_Q_SHELL_CMDS = "q-shell-cmds"
    OUR_CAREGORY_CLI_CMDS = "cli-cmds"
    classes={}
    classes[OUR_CAREGORY_DIRS_TO_LIST] = SupportFileItemDirToList
    classes[OUR_CAREGORY_DIRS_TO_COPY] = SupportFileItemDirToCopy
    classes[OUR_CAREGORY_LINUX_SHELL_CMDS] = SupportFileItemCmd
    classes[OUR_CAREGORY_Q_SHELL_CMDS] = SupportFileItemQshellCmd
    classes[OUR_CAREGORY_CLI_CMDS] = SupportFileItemCliCmd

# === SupportFileProcessInfo Class =====================================================================================

# Used to connect to q-shell
class ProcessInfo(object):
    DESCRIPTION_KEY_PID = "pid"
    DESCRIPTION_KEY_SUPPORT_Q_SHELL = "support-q-shell"

    def __init__ (self, aQshellConnectionObject=None, aPid=None):
        self.myqShellObj = aQshellConnectionObject
        self.myPid = aPid

    def getPid(self):
        return self.myPid
    
    def isSupportQShell (self):        
        return self.myqShellObj != None

    def runShellCmd(self, command):
        if self.myqShellObj != None:
            return self.myqShellObj.runShellCmd(command)
        else:
            return ("Process is down. qShell object is none ", "")

    def describeAsDictionary (self):
        toReturn = {}
        toReturn[self.DESCRIPTION_KEY_PID]=str(self.myPid)        
        toReturn[self.DESCRIPTION_KEY_SUPPORT_Q_SHELL]=self.myqShellObj != None
        return toReturn

    
# === SupportFileNetworkInterfaceInfo Class =====================================================================================

class NetworkInterfaceInfo(object):
    DESCRIPTION_KEY_INTERFACE_NAME = "interface-name"

    def __init__ (self, aInterfaceName=None):        
        self.myInterfaceName = aInterfaceName

    def getInterfaceName(self):
        return self.myInterfaceName

    def describeAsDictionary (self):
        toReturn = {}
        toReturn[self.DESCRIPTION_KEY_INTERFACE_NAME]=str(self.myInterfaceName)        
        return toReturn
            

