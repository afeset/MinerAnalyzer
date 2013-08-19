#
#Copyright Qwilt, 2010
#
#The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
#Author: nirs
#

if  __package__ is None:
    G_NAME_GROUP_ROTATING_FILE_SIZE_ENFORCER = "unknown"
else:
    from . import G_NAME_GROUP_ROTATING_FILE_SIZE_ENFORCER

import os
from datetime import datetime
import re
import glob
import a.infra.lock.multi_process
import a.infra.process

class RotatingFileSizeEnforcer(object):
    """This class is used to monitor rotating files
     IT allows to get the next file name, rotate them, monitor the overall size of the files and create a symlink to the latest file

     Limitations:
        File deletion operations assumes that the file name pattern create string in a rising
        lexicographic order

    """

    ##constant used to specify a the file name pattern
    KICK_NUM_4 = "%(k)s"
    YEAR_4 = "%(Y)s"
    MONTH_2 = "%(m)s"
    DAY_IN_MONTH_2 = "%(d)s"
    HOUR_2 = "%(H)s"
    MINUTE_2 = "%(M)s"
    SECOND_2 = "%(S)s"
    MILLI_SECOND_3 = "%(f)s"
    MICRO_SECOND_3 = "%(u)s"
    NANO_SECOND_3 = "%(n)s"
    EPOCH_SECONDS_10 = "%(s)s"
    _OPTIONAL_PHASE_NAME = "%(p)s"


    PHASE_CURRENT = "current"
    PHASE_PENDING = "pending"
    PHASE_ALL     = "all"
    PHASE_NONE    = "none"

    _OPTIONAL_PHASE_STRING_CURRENT  = ".current"
    _OPTIONAL_PHASE_STRING_PENDING  = ".pending"
    _OPTIONAL_PHASE_STRING_GLOB     = "*"


    @classmethod
    def s_getDefaultBaseNamePattern (cls, fileBaseNamePrefix, fileBaseNameSuffix, usePhases):
        """Return the default file pattern for the given file prefix and suffix

        Args:
            fileBaseNamePrefix
            fileBaseNameSuffix
            usePhases - shall the new files names have a phase (current/pending)

        Returns:
            fileNamePattern: file name pattern matching the prefix, suffix and including the defualt time format

        Raises:
            None
        """

        defaultPattern = "%s.%s%s%s-%s%s%s.%s"%(cls.KICK_NUM_4,
                                                cls.YEAR_4,
                                                cls.MONTH_2,
                                                cls.DAY_IN_MONTH_2,
                                                cls.HOUR_2,
                                                cls.MINUTE_2,
                                                cls.SECOND_2,
                                                cls.MILLI_SECOND_3                                                   
                                               )
        if usePhases:
            defaultPattern = defaultPattern+"%s"%cls._OPTIONAL_PHASE_NAME

        defaultPattern = fileBaseNamePrefix+defaultPattern+fileBaseNameSuffix
        return defaultPattern

    def __init__ (self, logger, fileDir, fileBaseNamePrefix, fileBaseNameSuffix, includeExtraExtensions = False): 
        """ctor
        Creating the rotating file size enforcer for action.
        Assuming file name pattern to be the default one

        Args:
            logger: logger to log log messages to
            fileDir: the direcotry in which the file will be placed. direcotry must exists
            fileBaseNamePrefix: the file name prefix
            fileBaseNameSuffix: the file anme suffix
            includeExtraExtensions: shall the size enforcement catch also files with additional suffix. 
                                     e.g. not only 1.txt but also 1.txt.gz

        Returns:
            None

        Raises:
            None
        """   
        self._fileDir = fileDir
        self._includeExtraExtensions = includeExtraExtensions
        self._fileBaseNamePrefix = fileBaseNamePrefix
        self._fileBaseNameSuffix = fileBaseNameSuffix
        self._log = logger.createLoggerSameModule(G_NAME_GROUP_ROTATING_FILE_SIZE_ENFORCER, 
                                                  instance = self._fileBaseNamePrefix+self._fileBaseNameSuffix)
        self.initFileBaseNamePattern(self.s_getDefaultBaseNamePattern(self._fileBaseNamePrefix, self._fileBaseNameSuffix, False))
        self._isStandardFileNamePatternWithPhases = False
        self._createSymlink = False
        self._useBlockSize = False
        self._processLock = None
        self._controlFileName = None

        self._currentFileName = None
        self._totalSize = 0
        self._controlFileWasPrepared = False
        self._multiProcessLockAcquiredCount = 0

    def initFileBaseNamePatternToDefault (self, usePhases):
        """Change the file name pattern to the default one.
        Args:
            usePhases: shall the new files names have a phase (current/pending). 
                       size enforcement is done on "unphased" files also

        Returns:
            None

        Raises:
            None
        """
        self.initFileBaseNamePattern(self.s_getDefaultBaseNamePattern(self._fileBaseNamePrefix, self._fileBaseNameSuffix, usePhases))
        self._isStandardFileNamePatternWithPhases = usePhases

    def initFileBaseNamePattern (self, fileBaseNamePattern):
        """Change the file name pattern from the default one.
        Args:
            fileBaseNamePattern: the pattern of the base file name (including time flags etc. from the RotatingFileSizeEnforcer)

        Returns:
            None

        Raises:
            None
        """
        self._fileBaseNamePattern = fileBaseNamePattern
        self._currentFileBaseNameGlobPattern = self.s_calcFilesGlobPattern(self._fileBaseNamePattern, self.PHASE_CURRENT)
        self._pendingFileBaseNameGlobPattern = self.s_calcFilesGlobPattern(self._fileBaseNamePattern, self.PHASE_PENDING)        
        self._allFileBaseNameGlobPattern     = self.s_calcFilesGlobPattern(self._fileBaseNamePattern, self.PHASE_ALL)   
        if self._includeExtraExtensions:
            self._currentFileBaseNameGlobPattern += "*"
            self._pendingFileBaseNameGlobPattern += "*"
            self._allFileBaseNameGlobPattern     += "*"

    def initFileRotatingPattern (self, fileTimePattern):
        """Change the file rotating pattern from the default one without changing the prefix and suffix
        Args:
            fileBaseNamePattern: the time pattern of the base file name (including time flags etc. from the RotatingFileSizeEnforcer)

        Returns:
            None

        Raises:
            None
        """
        self.initFileBaseNamePattern(self._fileBaseNamePrefix + fileTimePattern + self._fileBaseNameSuffix)

    def initSymlink (self, symlinkDir=None, symlinkBaseName = None, symlinkUseAbsPath = False):
        """Enable the symlink capability of the class
        If called, a symlink to the latest opened file will be created upon "prepare" or "rotate"
        This function must be called before the "prepare" function is called
        Args:
            symlinkDir: the directory in which the symlink shall reside. direcotry must exists. if set to none, the use the fileDir as default
            symlinkBaseName: the symlinky base name. if set to None the default of "prefix"+"suffix" will be used
            symlinkUseAbsPath: use absolute path as symlink target

        Returns:
            None

        Raises:
            None
        """
        self._createSymlink=True
        if symlinkDir is None:
            self._symlinkDir = self._fileDir
        else:
            self._symlinkDir = symlinkDir        
        if symlinkBaseName:
            self._symlinkBaseName = symlinkBaseName
        else:
            self._symlinkBaseName = self._fileBaseNamePrefix + self._fileBaseNameSuffix
        self._symlinkUseAbsPath = symlinkUseAbsPath

    def initConsiderSizesOnDisk (self, considerBlockSize=True):
        """Should we calculate the actual disk usage of the file (blocks allocated * block size) instead of the size of the file

        Args:
            considerBlockSize: use allocated block size to calculate file size.

        Returns:
            None

        Raises:
            None
        """
        self._useBlockSize = considerBlockSize

    def initMultiProcessControl (self, controlFileName):
        """Move to mode that deals with multi processes writes to the file

        Args:
            controlFileName: a file name to use as a lock file

        Returns:
            None

        Raises:
            None
        """
        self._processLock = a.infra.lock.multi_process.RLock()
        if controlFileName is None:
            a.infra.process.processFatal("Control file name cannot be None")            
        self._controlFileName = controlFileName

    def setTotalSize (self, totalSize, minNumOfFilesToKeep=1):
        """set the max total size of the file
        Total size is the sum of all the files matching the glob pattern for matching the file.
        The size is enforced upon when this function is called, as well as when 
        upon "enforceSize" or "prepare" and "rotate" functions

        Args:
            totalSize: Max total size of all the files. "0" for no size enforcement
            minNumOfFilesToKeep: number of files to keep even if target size was not reached. 
                                 default is 1 for not deleting the current file

        Returns:
            None

        Raises:
            OSError
            a.infra.lock.multi_process.LockError - when lock failed (only working in multi processes mode)
        """
        self._totalSize = totalSize
        self._minNumOfFilesToKeep = minNumOfFilesToKeep
        self.enforceSize()

    def prepare (self):
        """create the first file name. 
        Also enforce size and create symlink if configured to

        Args:
            None

        Returns:
            None

        Raises:
            OSError - in case of failure in symlink creation of size enforcement
            a.infra.lock.multi_process.LockError - when lock failed (only working in multi processes mode)
        """
        

        #cannot fail as it called from above
        self._tryAcquireMultiProcessLockIfActivated()
        
        try:
            newFileName = None
            if self._processLock:
                self.learnCurrentFileName()    
                newFileName = self.getCurrentFileName()    
            if newFileName is None:
                newFileName = self._calcNextFileName() 
            self._rotate(newFileName)

        finally:
            self._releaseMultiProcessLockIfActivated()            


    def shutdown (self):
        if self._processLock:
            self._processLock.shutdown()

    def rotate (self):
        """move to the next file
        Also enforce size and update symlink if configured to

        Args:
            None

        Returns:
            None

        Raises:
            OSError - in case of failure in symlink creation of size enforcement
            a.infra.lock.multi_process.LockError - when lock failed (only working in multi processes mode)
        """
        self._tryAcquireMultiProcessLockIfActivated()
        try:
            newFileName = self._calcNextFileName()
            if  (self._currentFileName is None) or \
                ((not self._processLock) and newFileName != self._currentFileName) or \
                ((self._processLock) and newFileName > self._currentFileName): #for the case the kick number changed 
                                                                               #in the middle of the operation - we dont want to make a mess
                self._rotate(newFileName)
            else:
                pass
        finally:
            self._releaseMultiProcessLockIfActivated()            


    def getCurrentFileName (self):
        """get the current file name

        Args:
            None

        Returns:
            file full path. None if "prepare" was not called

        Raises:
            None
        """
        return self._currentFileName

    def learnCurrentFileName (self):   
        """learn the current file name
        
        Args:
            None

        Returns:
            file full path. None if "prepare" was not called

        Raises:
            a.infra.lock.multi_process.LockError - when lock failed (only working in multi processes mode)
        """

        if (self._currentFileName is not None) and os.path.exists(self._currentFileName):
            return

        self._tryAcquireMultiProcessLockIfActivated()
        try:
            newFileName = None
            filesInDir = self.getFilesList(self.PHASE_CURRENT)
            if filesInDir:
                foundCurrentFileName = os.path.basename(filesInDir[-1])
                expectedPatten = "([0-9]{4}\.[0-9]{8}-[0-9]{6})"
                match = re.search(expectedPatten,foundCurrentFileName)
                if match is not None:
                    kickNumber = int(match.group(0)[:4])
                    if kickNumber >= min(a.infra.process.getKickNumber(),9999): #>= and not == as a patch for service oscar restart for which the kick number is replace on the middle
                        newFileName = os.path.join(self._fileDir, foundCurrentFileName)

            self._currentFileName = newFileName
        finally:
            self._releaseMultiProcessLockIfActivated()            




    def getSymlinkFullName (self):
        """get the current file name

        Args:
            None

        Returns:
            symlink full path. None if synlink creation mode is off

        Raises:
            None
        """
        if  not self._createSymlink:
            return None
        return os.path.join(self._symlinkDir, self._symlinkBaseName)
        

    def getCurrentFileSize (self):
        """get the current file size

        Args:
            None

        Returns:
            file size. None if "prepare" function was not called

        Raises:
            OSError: e.g. if file does not exists
            a.infra.lock.multi_process.LockError - when lock failed (only working in multi processes mode)
        """
        if self._currentFileName is None:
            return 0

        self._tryAcquireMultiProcessLockIfActivated()
        try:
            if not os.path.exists(self._currentFileName):
                return 0
    
            return self._getFileSize(self._currentFileName)
        finally:
            self._releaseMultiProcessLockIfActivated()            

    def getFilesList (self, phase):
        """get the list of files matching the input glob pattern

        Args:
            None

        Returns:
            a sorted list of file

        Raises:
            OSError
            a.infra.lock.multi_process.LockError - when lock failed (only working in multi processes mode)
        """

        self._tryAcquireMultiProcessLockIfActivated()
        try:
            if os.path.exists(self._fileDir):
                if phase == self.PHASE_CURRENT:
                    baseNameGlobPattern = self._currentFileBaseNameGlobPattern
                elif phase == self.PHASE_CURRENT:
                    baseNameGlobPattern = self._pendingFileBaseNameGlobPattern
                elif phase == self.PHASE_ALL:
                    baseNameGlobPattern = self._allFileBaseNameGlobPattern
                else:
                    self._log("unsupported-phase").error("unsupported phase %s on list files", phase)
                    return []
    
                matchingPathes = glob.glob(os.path.join(self._fileDir, baseNameGlobPattern))
                matchingFiles = []
                for path in matchingPathes:
                    if os.path.isfile(path):
                        matchingFiles.append(path)
            toReturn = sorted(matchingFiles)
            self._log("list-dir").debug3("listing dir '%s' resulted with the files: %s", self._fileDir, toReturn)
            return toReturn

        finally:
            self._releaseMultiProcessLockIfActivated()            


    def enforceSize(self):
        """Enforce the total size of the file

        Args:
            None

        Returns:
            None

        Raises:
            OSError
            a.infra.lock.multi_process.LockError - when lock failed (only working in multi processes mode)
        """
        if self._totalSize == 0:
            self._log("no-max").debug4("max total files size is not set. not cleaning files")
            return


        self._tryAcquireMultiProcessLockIfActivated()
        try:
            self._log("clean").debug1("clean old files")
            
            filesInDir = self.getFilesList(self.PHASE_ALL)
    
            numOfFiles = 0
            totalSize = 0        
            filesDict = {}            
            for fullFileName in filesInDir:
                try:
                    size = self._getFileSize(fullFileName)  
                except OSError:#file does no longer exists
                    continue
                filesDict[fullFileName]=size
                numOfFiles+=1
                totalSize+=size            
                self._log("clean-dir-found-file").debug4("clean old files: found file '%s' of size %d", fullFileName, size)
    
            self._log("clean-initial-size").debug2("clean old files: initial num of files '%d' of size '%d'", numOfFiles, totalSize)
    
            for fileFullName in sorted(filesDict):            
                if numOfFiles <= self._minNumOfFilesToKeep:
                    self._log("reached-target-num-of-files").debug3("reached min num of files ('%d'<= '%d')", numOfFiles, self._minNumOfFilesToKeep)
                    break
                if totalSize <= self._totalSize:
                    self._log("reached-target-size").debug3("reached target size ('%d'<= '%d')", totalSize, self._totalSize)
                    break
                if self.getCurrentFileName() == fileFullName:
                    self._log("skip-current").debug3("skipping current file '%s' while cleaning files", fileFullName)
                    continue                
                self._log("removing-file").debug2("removing file '%s' of size '%d", fileFullName, filesDict[fileFullName])
                try:
                    os.remove(fileFullName)
                except:
                    if os.path.exists(fileFullName):
                        self._log("failed-removing-file").exception("failed removing file '%s' of size '%d", fileFullName, filesDict[fileFullName])
                    else:
                        #maybe the archiver moved the file
                        self._log("failed-removing-file-ok").debug2("failed removing file '%s' of size '%d. but it is no longer there", 
                                                                    fileFullName, filesDict[fileFullName],exc_info=True)
    
    
                numOfFiles -=1
                totalSize -= filesDict[fileFullName]            
    
            self._log("clean-final-size").debug2("clean old files: final size is '%d'", totalSize)
    
            if totalSize > self._totalSize:
                self._log("cannot-clean").error("could not reach target size of '%d'. current size is '%d'", self._totalSize, totalSize)

        finally:
            self._releaseMultiProcessLockIfActivated()            


    def moveCurrentToPending (self):
        """Move the marked "current" files to state "pending". Not including the current file

        Args:
            None

        Returns:
            None

        Raises:
            OSError
            a.infra.lock.multi_process.LockError - when lock failed (only working in multi processes mode)
        """
        if not self._OPTIONAL_PHASE_NAME in self._fileBaseNamePattern:
            self._log("no-phase").debug1("no phases to rotate by")
            return

        self._tryAcquireMultiProcessLockIfActivated()
        try:
            filesInDir = self.getFilesList(self.PHASE_CURRENT)
            for fileName in filesInDir:
                fileBaseName = os.path.basename(fileName)
                if self._currentFileName == fileName:
                    self._log("rename-phase-skip").debug2("skipping current file in rename currents to pending (%s)", fileName)
                    continue
                if self._OPTIONAL_PHASE_STRING_CURRENT in fileBaseName:#must be
                    if fileBaseName.count(self._OPTIONAL_PHASE_STRING_CURRENT) > 1:
                        self._log("current-more-than-once").error("The string '%s' appears more than once in file '%s'. cannot take care of it", self._OPTIONAL_PHASE_STRING_CURRENT, fileBaseName)
                        continue
                    fileNewBaseName = fileBaseName.replace(self._OPTIONAL_PHASE_STRING_CURRENT, self._OPTIONAL_PHASE_STRING_PENDING)
                    newFileName = os.path.join(os.path.dirname(fileName), fileNewBaseName)
                    self._log("rename-phase").debug1("rename: %s to %s", fileName, newFileName)
                    try:
                        os.rename(fileName, newFileName)
                    except:
                        self._log("failed-rename-phase").exception("failed rename: %s to %s", fileName, newFileName)
        finally:
            self._releaseMultiProcessLockIfActivated()            


    def tryAcquireMultiProcessLock (self):
        """ lock the multi process file if needed

        Returns:
            None

        Raises:
            a.infra.lock.multi_process.LockError - when lock failed
        """
        self._tryAcquireMultiProcessLockIfActivated()

    def verifyIsMultiProcessLockTaken (self):
        """ Raise if lock is not taken

        Returns:
            None

        Raises:
            a.infra.lock.multi_process.LockError - when lock ius not taken
        """
        if not self._processLock:
            return
        self._processLock.verifyIsMultiProcessLockTaken()        

    def releaseMultiProcessLock (self):
        """ release the multi process file if needed

        Returns:
            None

        Raises:
            a.infra.lock.multi_process.RedundentUnlockError - when lock is not balanced
        """
        self._releaseMultiProcessLockIfActivated()

    @classmethod
    def s_getFileNameRemovePhase (cls, fileBaseNamePattern, fileName):
        """Get the file name without the "phase"

        Args:
            None

        Returns:
            the new name. None in case of failure

        Raises:
            None
        """
        if not cls._OPTIONAL_PHASE_NAME in fileBaseNamePattern:
            return fileName

        replaces = 0;
        if cls._OPTIONAL_PHASE_STRING_CURRENT in fileName:
            replaces += fileName.count(cls._OPTIONAL_PHASE_STRING_CURRENT)
            fileName = fileName.replace(cls._OPTIONAL_PHASE_STRING_CURRENT, "")
        if cls._OPTIONAL_PHASE_STRING_PENDING in fileName:
            replaces += fileName.count(cls._OPTIONAL_PHASE_STRING_PENDING)
            fileName = fileName.replace(cls._OPTIONAL_PHASE_STRING_PENDING, "")

        if replaces!=1:
            return None

        return fileName

    def _rotate (self, newFileName):
        self._tryAcquireMultiProcessLockIfActivated()
        try:
            self._currentFileName = newFileName
            if self._createSymlink:
                symlinkFullName = self.getSymlinkFullName()
    
                if os.path.lexists(symlinkFullName) and not os.path.islink(symlinkFullName):
                    #the symlink we are about to create already exists as a file
                    if not os.path.lexists(self._currentFileName):
                        self._log("symlink-exists-as-file").warning("symlink '%s' already exists as a file. old file is deleted", symlinkFullName)
                        os.remove(symlinkFullName)
    
                symlinkDir = os.path.dirname(symlinkFullName)
                if not os.path.exists(symlinkDir):
                    self._log("symlink-dir-not-exists").warning("symlink directory '%s' does not exists", symlinkDir)
    
                #calc symlink
                if self._symlinkUseAbsPath:
                    symlinkTarget = os.path.abspath(self._currentFileName)
                else:
                    symlinkTarget = os.path.relpath(self._currentFileName, symlinkDir)
    
                #moving through a temp file to avoid a period of time in which the symlink does not exists            
                tempSymlinkFullName = symlinkFullName+".tmp.qb.rfse"
                if os.path.lexists(tempSymlinkFullName):
                    #old file from prev rounds. lets delete it
                    os.remove(tempSymlinkFullName)            
                os.symlink(symlinkTarget, tempSymlinkFullName)
                os.rename(tempSymlinkFullName, symlinkFullName)            
    
            self.enforceSize()

        finally:
            self._releaseMultiProcessLockIfActivated()            


    def _calcNextFileName (self):
        dateTime = datetime.utcnow()
        kickNum = a.infra.process.getKickNumber()
        if kickNum > 9999:
            self._log("kick-num-to-big").debug3("launc num %d is to large. using 9999", kickNum)
            kickNum = 9999

        fileBaseName = self._fileBaseNamePattern%{self.KICK_NUM_4[2:-2] : "%04d"%kickNum,
                                                  self.YEAR_4[2:-2] : dateTime.strftime("%Y"),
                                                  self.MONTH_2[2:-2] : dateTime.strftime("%m"),
                                                  self.DAY_IN_MONTH_2[2:-2] : dateTime.strftime("%d"),
                                                  self.HOUR_2[2:-2] : dateTime.strftime("%H"),
                                                  self.MINUTE_2[2:-2] : dateTime.strftime("%M"),
                                                  self.SECOND_2[2:-2] : dateTime.strftime("%S"),
                                                  self.MILLI_SECOND_3[2:-2] : dateTime.strftime("%f")[:3],
                                                  self.MICRO_SECOND_3[2:-2] : dateTime.strftime("%f")[3:],
                                                  self.EPOCH_SECONDS_10[2:-2] : dateTime.strftime('%010s'),
                                                  self._OPTIONAL_PHASE_NAME[2:-2] : self._OPTIONAL_PHASE_STRING_CURRENT
                                                  }
        self._log("next-file-name").debug3("new file name '%s'", fileBaseName)
        return os.path.join(self._fileDir, fileBaseName)

    def _tryAcquireMultiProcessLockIfActivated (self):
        if not self._processLock:
            return
        if not self._controlFileWasPrepared:
            if not self._isStandardFileNamePatternWithPhases:
                #verify file name has a current string for the first time rotation to work
                #Even better - verify standard file structure so we will not get into correntes of 
                #file names and we will be able to choose the control file as we wish
                raise a.infra.lock.multi_process.LockError()
            self._processLock.prepare(self._controlFileName) 
            self._controlFileWasPrepared = True           

        self._processLock.tryAcquire()
 
    def _releaseMultiProcessLockIfActivated (self):
        if not self._processLock:
            return
        self._processLock.release()

    @classmethod
    def s_calcFilesGlobPattern (cls, fileBaseNamePattern, phase):
        phaseString = cls._OPTIONAL_PHASE_STRING_GLOB
        if phase == cls.PHASE_CURRENT:
            phaseString = cls._OPTIONAL_PHASE_STRING_CURRENT
        if phase == cls.PHASE_PENDING:
            phaseString = cls._OPTIONAL_PHASE_STRING_PENDING

        globPattern = fileBaseNamePattern%{cls.KICK_NUM_4[2:-2] : "????",
                                           cls.YEAR_4[2:-2] : "????",
                                           cls.MONTH_2[2:-2] : "??",
                                           cls.DAY_IN_MONTH_2[2:-2] : "??",
                                           cls.HOUR_2[2:-2] : "??",
                                           cls.MINUTE_2[2:-2] : "??",
                                           cls.SECOND_2[2:-2] : "??",
                                           cls.MILLI_SECOND_3[2:-2] : "???",
                                           cls.MICRO_SECOND_3[2:-2] : "???",
                                           cls.EPOCH_SECONDS_10[2:-2] : "??????????",
                                           cls._OPTIONAL_PHASE_NAME[2:-2] : phaseString
                                           }
        return globPattern

    @staticmethod
    def s_compareFileTimeStamp (gmtTimeInSec, standardFileName):
        """return True if the file timetamp is higher then or equal to the GMT time. False o.w., None in case of bad file name"""
        #####################Q&D
        expectedPatten = "([0-9]{4}\.[0-9]{8}-[0-9]{6})"
        match = re.search(expectedPatten,standardFileName)
        if match is None:
            return None
        #kickNumber = int(match.group(0)[:4])
        timeStampString = match.group(0)[5:]
    
        dateTimeObj = datetime.utcfromtimestamp(gmtTimeInSec)
        inputTimeStamp = dateTimeObj.strftime("%Y%m%d-%H%M%S")
    
        return timeStampString >= inputTimeStamp


    def _getFileSize (self, fileNameFullPath):
        if self._useBlockSize:
            return os.stat(fileNameFullPath).st_blocks*512
        return os.path.getsize(fileNameFullPath)
         


