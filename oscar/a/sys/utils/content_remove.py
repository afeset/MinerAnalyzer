#!/usr/local/bin/python2.6
# 
# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# ver 1.0 
#
# Author: Roy Russo
#
########################################################################################################################
#                                                                                                                      #
# This module is for removing old files in a directory and assumes it is called by Oscar 
# Old = files with the oldest(lower) access time
# Passing parameters is by passing an OCR_Params object.
# 
# The MARK concept: files are renamed with ".MARKED suffix and from then on they are treated as if they where removed 
#                   unless they are UNMARKED 
#
# Modules main and only public method - removeOldContent()
#                                                                                                                       #
#########################################################################################################################


import os, time, platform, statvfs, logging
from operator import attrgetter 



# === Globals =====================================================================================#

# Function return flags
OCR_RC_OK = 0
OCR_RC_PROBLEM = 1
# Private function return flag
__OCR_RC_WARN = 2

# Commands for unMarked files
OCR_MARK = "MARK"
OCR_REMOVE = "REMOVE"
OCR_DRY_RUN_REMOVE = "DRY_RUN_REMOVE"
OCR_MOVE = "MOVE"

# Commands for Marked files
OCR_UNMARK = "UNMARK"
OCR_REMOVE_MARKED = "REMOVE_MARKED"
OCR_MOVE_MARKED = "MOVE_MARKED"
OCR_DRY_RUN_REMOVE_MARKED = "DRY_RUN_REMOVE_MARKED"

# Global time stamp
__CURRENT_TIME = None

# Meta file name suffix
__META_SUFFIX = "meta"

# Global statistics
globalStatistics = None

# Logger - in case logger parameter is None.
__myLogger = logging.getLogger(__name__)


# === OCR_Params =====
class OCR_Params:
    """
    Class for holding the parameters:
        -command:
            OCR_MARK - mark the files matching the criteria by adding the suffix '.MARKED" to the end of the filename
            OCR_REMOVE - remove files matching the criteria (marked and unmarked)- can't be undone!
            OCR_DRY_RUN_REMOVE  - same as REMOVE but doesn't thouch the files. just write to the log which files would have been procesed.
            OCR_MOVE - move files matching the criteria (marked and unmarked) to the specified directory path specified in 'destinationPath'.
         
            OCR_UNMARK - unmark all marked files
            OCR_REMOVE_MARKED - remove only marked files (and all of them) - can't be undone!
            OCR_MOVE_MARKED - move only marked files to the destinationPath 
            OCR_DRY_RUN_REMOVE_MARKED - same as REMOVE_MARKED but doesn't thouch the files. just write to the log which files would have been procesed.
         
        -workDirectory: a string specifying the root directory to work on. will process all the directory tree.
        -logger: a logger object
        -numOfFilesToProcess: k oldest files to proccess. only to use with commands  OCR_MARK, OCR_REMOVE, OCR_DRY_RUN_REMOVE and OCR_MOVE. with other commands, ALL marked files are processed.
        -(optional)lastAccessThreshold: files that their time sinced last accessed is smaller then lastAccessThreshold will not be processed.
        -(optional)lastAccessThresholdWarn: files that their time sinced last accessed is smaller then lastAccessThresholdWarn will raise a warning. must be equal or above lastAccessThreshold.
        -(optional)diskUsageLimit: in precentage. If disk usage is below this, no proccessing will accur at all. Default = 0.
        -(optoinal)diskUsageMode: if this is true - will try to remove files until reached diskUsageLimit or fileList is empty
        -(optional)destinationPath: destination directory to move the files to (only with MOVE command)
        -(optional)metaDirectory: The path for the metadata directory files

    The following parameters must be NOT none : command, workDirectory, logger
    """

    command = None
    workDirectory = None
    logger = None
    numOfFilesToProcess = -1
    lastAccessThreshold = 0
    lastAccessThresholdWarn = 0
    diskUsageLimit = 0
    diskUsageMode = False
    destinationPath = None
    metaDirectory = None



# === OCR_Stat ======
class OCR_Stat:
    """
    Statistics struct:
        -totalFilesScanned: number of total files scanned in the directory
        -totalFilesAppended: number of total files appended for proccessing
        -succededFileCount: number of succesfull file proccessing
        -totalSuccededSize: total size of all the succesfull proccessed files
        -failedFileCount: number of failed file proccessing
        -totalFailedSize: total size of all the failed proccessed files
        -totalWarnFileCount: number of file warnings according (due to the lastAccessThresholdWarn argument)
        -totalWarnFileSize: total size of all the files which raised warnings 
    """

    totalFilesScanned = 0
    totalFilesAppended = 0
    succededFileCount = 0
    totalSuccededSize = 0
    failedFileCount = 0
    totalFailedSize = 0
    totalWarnFileCount = 0
    totalWarnFileSize = 0

    def appendStatistics (self, other):
        self.totalFilesScanned += other.totalFilesScanned
        self.totalFilesAppended += other.totalFilesAppended
        self.succededFileCount += other.succededFileCount
        self.totalSuccededSize += other.totalSuccededSize
        self.failedFileCount += other.failedFileCount
        self.totalFailedSize += other.totalFailedSize
        self.totalWarnFileCount += other.totalWarnFileCount
        self.totalWarnFileSize += other.totalWarnFileSize



# === PRIVATE classes =====================================================================================#

# === OCR_File =====
class OCR_File:
    """
    File attributres struct
    """

    fullNamePath = None
    lastAccessTime = 0
    size = 0

 
 
           

# === Module's PUBLIC methods ====================================================================================#


# --- removeOldContent -------------------------------------------------------------------------
def removeOldContent (parameters):
    """
    Removes "old" files from the workdirectory and all it's sub-directorys.

    Args:
        -OCR_Params: Object containing parameters for the function. Parameters are described in the OCR_Params class above 

    Returns: 
        -int: OCR_RC_OK | OCR_RC_PROBLEM (return code) 
        -OCR_Stat: Object containing statistics (see details in OCR_Stat class description)
        -float: The disk utilization BEFORE processing the files
        -float: Updated disk utilization in precentage AFTER processing the files
    """


    # Suppressing warning of max returns
    __pychecker__ = 'maxreturns=11'
    
    command = parameters.command
    workDirectory = parameters.workDirectory
    logger = parameters.logger
    numOfFilesToProcess = parameters.numOfFilesToProcess
    lastAccessThreshold = parameters.lastAccessThreshold
    lastAccessThresholdWarn = parameters.lastAccessThresholdWarn
    diskUsageLimit = parameters.diskUsageLimit
    destinationPath = parameters.destinationPath

    # Initialize logger
    if logger != None:
        global __myLogger
        __myLogger = logger

    # Initialize globalStatistics
    global globalStatistics
    globalStatistics = OCR_Stat()

    # Check if the workDirectory parameter is valid
    if (workDirectory == None) or not(os.path.isdir(workDirectory)):
        __myLogger.error("Invalid input - the workDirectory Path is inValid")
        return OCR_RC_PROBLEM, globalStatistics, -1, -1

    # Follow the symblink
    if os.path.islink(workDirectory):
        workDirectory = os.path.normpath(os.readlink(workDirectory))
        parameters.workDirectory = workDirectory

    # Get the disk usage before applying file process
    beforeDiskUsage = getDiskUsage(workDirectory)

    # Check if the diskUsageLimit value is valid
    if not(diskUsageLimit >= 0 and diskUsageLimit <=100):
        __myLogger.error("Invalid input - diskUsageLimit must be between 0 and 100")
        return OCR_RC_PROBLEM, globalStatistics, beforeDiskUsage, beforeDiskUsage

    if beforeDiskUsage != -1 and beforeDiskUsage <= float(diskUsageLimit):
        __myLogger.info("Current Disk usage (%.2f%%) is under the specified limit (%.2f%%). exiting...", beforeDiskUsage, diskUsageLimit)
        # Count files in the directory
        globalStatistics.totalFilesScanned = countFiles(workDirectory)
        return OCR_RC_OK, globalStatistics, beforeDiskUsage, beforeDiskUsage  

    # Check if command parameter is valid
    if not(command in(OCR_DRY_RUN_REMOVE, OCR_DRY_RUN_REMOVE_MARKED, OCR_MARK, OCR_UNMARK, OCR_REMOVE_MARKED, OCR_REMOVE, OCR_MOVE, OCR_MOVE_MARKED)):
        __myLogger.error("Invalid input - unknown command: '%s'", command)
        return OCR_RC_PROBLEM, globalStatistics, beforeDiskUsage, beforeDiskUsage
     

    # Log starting point    
    __myLogger.info("\nStarting content proccessing for command '%s'...", command)

    # Check if the numOfFilesToProcess value is valid. Applys only to commands OCR_MARK, OCR_REMOVE, OCR_DRY_RUN_REMOVE and OCR_MOVE.
    if numOfFilesToProcess < 0 and not(command in(OCR_UNMARK, OCR_REMOVE_MARKED, OCR_DRY_RUN_REMOVE_MARKED, OCR_MOVE_MARKED)):
        __myLogger.error("Invalid input - numOfFilesToProcess must be specified for this command and must be 0 and above")
        return OCR_RC_PROBLEM, globalStatistics, beforeDiskUsage, beforeDiskUsage

    # Check if the lastAccessThreshold value is valid
    if lastAccessThreshold < 0 or lastAccessThresholdWarn < 0:
        __myLogger.error("Invalid input - lastAccessThreshold must be above and/or lastAccessThresholdWarn must be above 0")
        return OCR_RC_PROBLEM, globalStatistics, beforeDiskUsage, beforeDiskUsage

    # Verify that lastAccessThresholdWarn is equal or higher then lastAccessThreshold
    if (lastAccessThreshold > 0) and (lastAccessThresholdWarn > 0) and (lastAccessThresholdWarn < lastAccessThreshold):
        __myLogger.error("Invalid input - lastAccessThresholdWarn parameter must be equal or larger then lastAccessThresholdWarn parameter")
        return OCR_RC_PROBLEM, globalStatistics, beforeDiskUsage, beforeDiskUsage

    # Check if destinationPath parameter is valid
    if command in (OCR_MOVE, OCR_MOVE_MARKED):
        # if parameter is None
        if destinationPath == None:
            __myLogger.error("Invalid input - destinationPath parameter must be specified for the MOVE command")
            return OCR_RC_PROBLEM, globalStatistics, beforeDiskUsage, beforeDiskUsage
        # Make the directory in case it doesn't exists and numOfFilesToProcess > 0
        if numOfFilesToProcess > 0 and not(os.path.isdir(destinationPath)): 
            try:
                os.makedirs(destinationPath)
                __myLogger.info("Destination path '%s' was created", destinationPath)
            except Exception as ex:
                __myLogger.error("Caught exception while trying to create the destination directory '%s':\n%s", destinationPath, ex)
                return OCR_RC_PROBLEM, globalStatistics, beforeDiskUsage, beforeDiskUsage  

    # If numOfFilesToProcess is zero - Return
    if numOfFilesToProcess == 0: 
        # nothing to do - return ok
        # Count files in the directory
        globalStatistics.totalFilesScanned = countFiles(workDirectory)
        return OCR_RC_OK, globalStatistics, beforeDiskUsage, beforeDiskUsage

    # Proccess the work directory and aplly the command on the files
    returnCode, updatedDiskUsage = __proccessDirectory(parameters)
    
    # If OK, print statistics to the log
    if returnCode == OCR_RC_OK:
        __myLogger.info("\nCommand %s results:", command)
        __myLogger.info("Total files scanned: %d", globalStatistics.totalFilesScanned)
        __myLogger.info("Total files appended: %d", globalStatistics.totalFilesAppended)
        __myLogger.info("Total succeeded: %d", globalStatistics.succededFileCount)
        __myLogger.info("Total succeeded files size: %d", globalStatistics.totalSuccededSize)
        __myLogger.info("Total failed: %d", globalStatistics.failedFileCount)
        __myLogger.info("Total failed files size: %d", globalStatistics.totalFailedSize)
        __myLogger.info("Total succeeded files with warnings: %d", globalStatistics.totalWarnFileCount)
        __myLogger.info("Total succeeded files with warnings size: %d", globalStatistics.totalWarnFileSize)
    else:
        __myLogger.error("Content removing faild") 

    # get the updated diskUsage in case __proccessDirectory() didn't return it
    if updatedDiskUsage == -1:
        updatedDiskUsage = getDiskUsage(workDirectory)

    return returnCode, globalStatistics, beforeDiskUsage, updatedDiskUsage
    
        



# === Module's PRIVATE methods =====================================================================================


# --- __proccessDirectory -------------------------------------------------------------------------
def __proccessDirectory (parameters):
    """
    Proccess the work directory and collects files pending for removel. 
    """

    command = parameters.command
    workDirectory = parameters.workDirectory
    lastAccessThreshold = parameters.lastAccessThreshold
    diskUsageLimit = parameters.diskUsageLimit
    diskUsageMode = parameters.diskUsageMode

    # Get current time stamp to compare with
    global __CURRENT_TIME
    __CURRENT_TIME = time.time()

    # Initialize counters
    totalFilesScanned = 0
    totalFilesAppended = 0
    
    # Gather files to a list
    filesList = []

    # Boolean for specifying what kind of command we are dealing with
    isCommandForMarkedFiles =  command in (OCR_UNMARK, OCR_REMOVE_MARKED, OCR_DRY_RUN_REMOVE_MARKED, OCR_MOVE_MARKED)

    # Walk in the directory tree
    for (currentRoot,dirnames,filenames) in os.walk(workDirectory):

        # Count total files scanned
        totalFilesScanned += len(filenames)

        # For each file (if there is any):
        for filename in filenames:

            # Check whether or not to collect the marked or unmarked file
            if (filename.split('.')[-1:][0]=="MARKED") != isCommandForMarkedFiles: 
                # If the file is marked and the command is for unMarked OR the file is UnMarked and the command if for marked - Skip the file!
                continue

            # Don't collect any metadata files!!! Also remove it from statistics.
            if (filename.split('.')[-1:][0]==__META_SUFFIX):
                totalFilesScanned -= 1
                continue

            # Get the statistics of the file
            fileFullNamePath = os.path.join(currentRoot,filename)
            fileStatistics = os.stat(fileFullNamePath)
            
            # Discare files that their time sinced last accessed is smaller then the given threshold
            if not(isCommandForMarkedFiles) and (__CURRENT_TIME - fileStatistics.st_atime < lastAccessThreshold):
                continue 

            # Create and fill a file object
            myFile = OCR_File()
            myFile.fullNamePath = fileFullNamePath
            myFile.lastAccessTime = fileStatistics.st_atime
            myFile.size = fileStatistics.st_size

            # Append the file object to the list
            filesList.append(myFile)

            # Count total files apeended to the list
            totalFilesAppended += 1


    # TODO!! - just to see if importent for testing!! not importent for implementation
    # First sort the files by file name (secondary key)
    #filesList.sort(key=attrgetter('fullNamePath'))

    # Sort the files by accesnding access time - Oldest accessed are first (primary key)
    filesList.sort(key=attrgetter('lastAccessTime'))

    # Declare the global in oreder to update it
    global globalStatistics

    # Append relavent statistics to the statistics object
    globalStatistics.totalFilesScanned += totalFilesScanned
    globalStatistics.totalFilesAppended += totalFilesAppended

    # Initialize currentDiskUsage parameter
    currentDiskUsage = -1

    # Use __processFilesList() at least once 
    while True:

        # Process the files list
        returnCode, statistics =  __processFilesList(filesList, isCommandForMarkedFiles, parameters)

        # Append the statistics        
        globalStatistics.appendStatistics(statistics)
        
        # Break point
        if diskUsageMode and returnCode == OCR_RC_OK:
            # If we are in diskUsageMode and returnCode is OK - check fileslist size and current disk usage
            currentDiskUsage = getDiskUsage(workDirectory)
            if len(filesList) == 0 or currentDiskUsage <= diskUsageLimit:
                # If we reached the diskUsageLimit OR fileList is empty - break
                break
        else:
            # We are not in diskUsageMode or returnCode is PROBLEM
            break

    return returnCode, currentDiskUsage



# --- __processFilesList -------------------------------------------------------------------------
def __processFilesList(filesList, isHandlingMarkedFiles, parameters):
    """
    Proccess files list - applys the command on the file list and collect statistics.
    """

    numOfFilesToProcess = parameters.numOfFilesToProcess
    lastAccessThresholdWarn = parameters.lastAccessThresholdWarn
    command = parameters.command
    destinationPath = parameters.destinationPath
    metaDir = parameters.metaDirectory
    workDirectory = parameters.workDirectory


    # Get the work directory path length (for rebuilding the meta file path)
    workDirLength = __getPathLength(workDirectory)

    # Get statistics object
    statistics = OCR_Stat()

    # Save the files Indexes so we can remove them later from the list
    fileIndex = 0
    filesToBeRemovedIndexes = []

    # Process files list 
    for myFile in filesList:
        # Get the meta data full name path
        metaFileNamePath = __getMetaFileName(workDirLength, metaDir, myFile.fullNamePath)

        # If we are handling with list that contains unmarked files, check is lastAccessTime has changes. If so - ignore the file
        if isHandlingMarkedFiles: 
            returnCode = __proccessMarkedFile(command, myFile, destinationPath, metaFileNamePath)
        else:
            returnCode = __proccessUnMarkedFile(command, myFile, lastAccessThresholdWarn, destinationPath, metaFileNamePath)

        # Check the return code
        if returnCode == OCR_RC_OK :
            # Everything is ok
            statistics.succededFileCount += 1
            statistics.totalSuccededSize += myFile.size
        elif returnCode == OCR_RC_PROBLEM:
            # Failed to process file
            statistics.failedFileCount += 1
            statistics.totalFailedSize += myFile.size
        else:
            # Everything is ok but lastAccessLimit threshold warning was raised (according to the lastAccessThresholdWarn parameter)
            statistics.succededFileCount += 1
            statistics.totalSuccededSize += myFile.size
            statistics.totalWarnFileCount += 1
            statistics.totalWarnFileSize += myFile.size

        # We have processed that file - Append it's index so we can remove it later
        filesToBeRemovedIndexes.append(fileIndex)
        fileIndex += 1

        # Breaking Point (only for unMarkedFiles)
        # If handling with unMarked files and we proccessed numOfFilesToProcess - Break
        if not(isHandlingMarkedFiles) and (statistics.succededFileCount + statistics.failedFileCount >= numOfFilesToProcess):
            break
        
    # Remove processed file from the fileslist
    filesToBeRemovedIndexes.reverse()
    for i in filesToBeRemovedIndexes:
        filesList.pop(i)

    # If all files failed - return OCR_RC_PROBLEM
    if fileIndex > 0 and fileIndex == statistics.failedFileCount:
        return OCR_RC_PROBLEM, statistics

    return OCR_RC_OK, statistics



# --- __proccessUnMarkedFile -------------------------------------------------------------------------
def __proccessUnMarkedFile (command, file, lastAccessThresholdWarn, destinationPath, metaFileNamePath):
    """
    Proccess file that is not '.MARKED'
    For commands OCR_DRY_RUN_REMOVE, OCR_MARK, OCR_REMOVE, OCR_MOVE.
    """

    # If lastAccessTime parameter has changed since last time - Skip the file
    currentLastAccessTime = os.stat(file.fullNamePath).st_atime
    if file.lastAccessTime != currentLastAccessTime:
        # Skip this file
        return OCR_RC_OK

    # Choose method to invoke on files
    if command ==OCR_DRY_RUN_REMOVE:
        func = __logRemoveFile
    elif command == OCR_MARK: 
        func = __markFile
    elif command == OCR_REMOVE: 
        func = __removeFile
    elif command == OCR_MOVE: 
        func = __moveFile
    else:
        __myLogger.error("Unknown command: '%s'", command) 
        return OCR_RC_PROBLEM

    # Apply the command on the file
    returnCode = func(file, metaFileNamePath, destinationPath)

    # Is succesfull and time since last accessed is lower then lastAccessThresholdWarn, return warning
    if returnCode == OCR_RC_OK and (__CURRENT_TIME - file.lastAccessTime < lastAccessThresholdWarn):
        returnCode = __OCR_RC_WARN

    return returnCode



# --- __proccessMarkedFile -------------------------------------------------------------------------
def __proccessMarkedFile (command, file, destinationPath, metaFileNamePath):
    """
    Proccess files that allready have '.MARKED' suffix
    For commands OCR_DRY_RUN_REMOVE_MARKED, OCR_REMOVE_MARKED, OCR_UNMARK, OCR_MOVE_MARKED.
    """

    # Choose method to invoke on files
    if command == OCR_DRY_RUN_REMOVE_MARKED:
        func = __logRemoveFile
    elif command == OCR_UNMARK:
        func = __unMarkFile
    elif command == OCR_REMOVE_MARKED: 
        func = __removeFile
    elif command == OCR_MOVE_MARKED:
        func = __moveFile
    else:
        __myLogger.error("Unknown command: '%s'", command) 
        return OCR_RC_PROBLEM

    return func(file, metaFileNamePath, destinationPath)


# --- __logRemoveFile -------------------------------------------------------------------------
def __logRemoveFile (file, metaFileNamePath, destinationPath = None): 
    """
    Only log file that should have been removed.
    Used for the DRY_RUNs
    """

    # Suppressing warning of unsed parameter 'destinationPath'. This method is used in a generic way (see __proccessMarkedFile / __proccessUnMarkedFile)
    __pychecker__ = 'unusednames=destinationPath' 

    __myLogger.debug("DRY_RUN: File '%s' would have been removed. File LastAccessTime: %d , File size: %d", file.fullNamePath, file.lastAccessTime, file.size)

    # Check if metadata file exists. If so - remove it.
    if metaFileNamePath != None:
        if os.path.isfile(metaFileNamePath):
            __myLogger.debug("Metadata file '%s' would have been removed.", metaFileNamePath)
        else:
            __myLogger.debug("DRY_RUN: Could not find metadata file '%s'.", metaFileNamePath)


    return OCR_RC_OK


# --- __markFile -------------------------------------------------------------------------
def __markFile (file, metaFileNamePath, destinationPath = None):
    """
    Mark a file - add '.MARKED' suffix to the file name.
    """

    # Suppressing warning of unsed parameter 'destinationPath','metaFileNamePath'. This method is used in a generic way (see __proccessMarkedFile / __proccessUnMarkedFile)
    __pychecker__ = 'unusednames=destinationPath,metaFileNamePath' 

    try:
        # Add '.MARKED' suffix to the file
        newName = file.fullNamePath + ".MARKED"
        os.rename(file.fullNamePath, newName)
        __myLogger.debug("File '%s' has been MARKED. File LastAccessTime: %d , File size: %d", file.fullNamePath, file.lastAccessTime, file.size)
        return OCR_RC_OK
    except Exception as ex:
        __myLogger.error("Caught exception while trying renaming (MARKING) the file '%s':\n%s", file.fullNamePath, ex)
        return OCR_RC_PROBLEM



# --- __removeFile -------------------------------------------------------------------------
def __unMarkFile (file, metaFileNamePath, destinationPath = None):
    """
    UnMarkes a file - remove the '.MARKED' suffix from the file name.
    """

    # Suppressing warning of unsed parameter 'destinationPath','metaFileNamePath'. This method is used in a generic way (see __proccessMarkedFile / __proccessUnMarkedFile)
    __pychecker__ = 'unusednames=destinationPath,metaFileNamePath' 

    try:
        # Remove the '.MARKED' suffix from the file
        newName = '.'.join(file.fullNamePath.split('.')[:-1])
        os.rename(file.fullNamePath, newName)
        __myLogger.debug("File '%s' has been UNMARKED. File LastAccessTime: %d , File size: %d", file.fullNamePath, file.lastAccessTime, file.size)
        return OCR_RC_OK
    except Exception as ex:
        __myLogger.error("Caught exception while trying renaming (UNMARKING) the file '%s':\n%s", file.fullNamePath, ex)
        return OCR_RC_PROBLEM



# --- __removeFile -------------------------------------------------------------------------
def __removeFile (file, metaFileNamePath, destinationPath = None):
    """
    Removes a file.
    """

    # Suppressing warning of unsed parameter 'destinationPath'. This method is used in a generic way (see __proccessMarkedFile / __proccessUnMarkedFile)
    __pychecker__ = 'unusednames=destinationPath' 

    try:
        # Remove the file
        os.remove(file.fullNamePath)
        __myLogger.debug("File '%s' has been removed. File LastAccessTime: %d , File size: %d", file.fullNamePath, file.lastAccessTime, file.size)

        # Check if metadata file exists. If so - remove it.
        if metaFileNamePath != None:
           if os.path.isfile(metaFileNamePath):
               os.remove(metaFileNamePath)
               __myLogger.debug("Metadata file '%s' has been removed.", metaFileNamePath)
           else:
               __myLogger.debug("Could not find metadata file '%s'.", metaFileNamePath)

        return OCR_RC_OK

    except Exception as ex:
        __myLogger.error("Caught exception while trying removing the file '%s':\n%s", file.fullNamePath, ex)
        return OCR_RC_PROBLEM



# --- __moveFile -------------------------------------------------------------------------
def __moveFile (file, metaFileNamePath, destinationPath):
    """
    Move a file to the destinationPath.
    """

    # Suppressing warning of unsed parameter 'metaFileNamePath'. This method is used in a generic way (see __proccessMarkedFile / __proccessUnMarkedFile)
    __pychecker__ = 'unusednames=metaFileNamePath' 

    try:
        # Move the file to the destination directory (rename)
        fileName = os.path.split(file.fullNamePath)[1]
        newFileFullNamePath = os.path.join(destinationPath, fileName)
        os.rename(file.fullNamePath, newFileFullNamePath) 
        __myLogger.debug("File '%s' has been moved to '%s'. File LastAccessTime: %d , File size: %d", file.fullNamePath, newFileFullNamePath, file.lastAccessTime, file.size)
        return OCR_RC_OK
    except Exception as ex:
        __myLogger.error("Caught exception while trying moving the file '%s' to '%s':\n%s", file.fullNamePath, destinationPath, ex)
        return OCR_RC_PROBLEM



# --- getDiskUsage -------------------------------------------------------------------------
def getDiskUsage (workDirectory):
    """
    Get the disk usage for the fileSystem of the given workDirectory. Works only for linux.
    Returns -1 if not linux
    returns:
        -float: diskUsage in precentage
    """

    if platform.system() == "Linux":
        # Get the statistics for the file system
        st = os.statvfs(workDirectory)
        # Calculate the current disk usage and compare to the diskUsageLimit argument
        DiskUsage = 100*(1-(float(st[statvfs.F_BAVAIL])/st[statvfs.F_BLOCKS]))
    else:
        DiskUsage = -1

    return DiskUsage



# --- countFiles -------------------------------------------------------------------------
def countFiles (workDirectory, suffixFilter = None):

    totalFiles = 0

    if suffixFilter == None:
        # Walk in the directory tree
        for (currentRoot,dirnames,filenames) in os.walk(workDirectory):
            # Count total files scanned
            totalFiles += len(filenames)
    else:
        # Walk in the directory tree
        for (currentRoot,dirnames,filenames) in os.walk(workDirectory):
            # Walk in the directory tree
            for filename in filenames:
                # Count only files which doesn't have the suffix
                if (filename.split('.')[-1:][0]!=suffixFilter):
                    totalFiles += 1
 
    return totalFiles

# same as above - exclude all suffixes
def countSuffixLessFiles (workDirectory):
    totalFiles = 0
    # Walk in the directory tree
    for (currentRoot,dirnames,filenames) in os.walk(workDirectory):
        # Walk in the directory
        for filename in filenames:
            # Count only files which doesn't have a suffix at all assuming no dot is in the filename
            if '.' not in filename:
                totalFiles += 1
    return totalFiles



# --- __getMetaFileName -------------------------------------------------------------------------
def __getMetaFileName (workDirlength, metaDir, fileNamePath):

    if metaDir == None:
        return None

    fileNamePathSplited = fileNamePath.split('/')
    if fileNamePathSplited[0] == '':
        fileNamePathSplited.pop(0)
    
    metaFullName = '/'.join(fileNamePathSplited[workDirlength:]) + '.' + __META_SUFFIX
    metaFullNamePath = os.path.join(metaDir, metaFullName)

    return metaFullNamePath




# --- __getPathLength -------------------------------------------------------------------------
def __getPathLength (workDir):

    workDirSplited = workDir.split('/')
    if workDirSplited[0] == '':
        workDirSplited.pop(0)

    if workDirSplited[len(workDirSplited)-1] == '':
        workDirSplited.pop(len(workDirSplited)-1)
    
    return len(workDirSplited)   
    

       
