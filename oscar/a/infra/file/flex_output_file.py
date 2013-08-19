#
#Copyright Qwilt, 2010
#
#The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
#Author: nirs
#

if  __package__ is None:
    G_NAME_GROUP_FLEX_OUTPUT_FILE = "unknown"
else:
    from . import G_NAME_GROUP_FLEX_OUTPUT_FILE

import rotating_file_size_enforcer
from file import File


class FlexOutputFile(File):
    """This class is an extension of the File (and therefore the built-in "file") object.

     It implements the same interface and can be used as a base for other derived 
     classes that need trasparently replace a "file" object
     It addtionally provide the ability to use file name patterns, rotate the file,
     control its total size and more.

     An instance of the class is a valid file only after calling the after calling "open" function

     Limitations:
        File deletion operations assumes that the file name pattern create string in a rising
        lexicographic order

    """

    def __init__ (self, logger, fileDir, fileBaseNamePrefix, fileBaseNameSuffix, includeExtraExtensions = False): 
        """ctor
        Creating the flex output file.
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
        self._log = logger.createLoggerSameModule(G_NAME_GROUP_FLEX_OUTPUT_FILE, instance = fileBaseNamePrefix+fileBaseNameSuffix)
        self._log("create").debug2("creating a flex output file with: fileDir='%s', fileBaseNamePrefix='%s', "
                                   "fileBaseNameSuffix='%s'", fileDir, fileBaseNamePrefix, fileBaseNameSuffix)
        self._rotatingFileSizeEnforcer = rotating_file_size_enforcer.RotatingFileSizeEnforcer(logger = logger,
                                                                                              fileDir=fileDir, 
                                                                                              fileBaseNamePrefix=fileBaseNamePrefix, 
                                                                                              fileBaseNameSuffix=fileBaseNameSuffix,
                                                                                              includeExtraExtensions=includeExtraExtensions)
        self._isMultiProcessControl = False
        self._wasOpened = False

    def initFileBaseNamePatternToDefault (self, usePhases):
        """Change the file name pattern to the default one.
        Args:
            usePhases: include phases in the file name

        Returns:
            None

        Raises:
            None
        """
        self._rotatingFileSizeEnforcer.initFileBaseNamePatternToDefault(usePhases)

    def initFileBaseNamePattern (self, fileBaseNamePattern):
        """Change the file name pattern from the default one.
        Args:
            fileBaseNamePattern: the pattern of the base file name (including time flags etc. from the RotatingFileSizeEnforcer)

        Returns:
            None

        Raises:
            None
        """
        self._log("init-pattern").debug2("initFileBaseNamePattern='%s'", fileBaseNamePattern)
        self._rotatingFileSizeEnforcer.initFileBaseNamePattern(fileBaseNamePattern=fileBaseNamePattern)

    def initSymlink (self, symlinkDir=None, symlinkBaseName = None, symlinkUseAbsPath = False):
        """Enable the symlink capability of the class
        If called, a symlink to the latest opened file will be created upon "open" or "reopenNextFile"
        This function must be called before the "open" function is called
        Args:
            symlinkDir: the directory in which the symlink shall reside. direcotry must exists. if set to none, the use the fileDir as default
            symlinkBaseName: the symlinky base name. if set to None the default of "prefix"+"suffix" will be used
            symlinkUseAbsPath: use absolute path as symlink target

        Returns:
            None

        Raises:
            None
        """
        self._rotatingFileSizeEnforcer.initSymlink(symlinkDir=symlinkDir, 
                                                   symlinkBaseName = symlinkBaseName, 
                                                   symlinkUseAbsPath = symlinkUseAbsPath)

    def initMultiProcessControl (self, controlFileName):
        """Move to mode that deals with multi processes writes to the file

        Args:
            controlFileName: a file name to use as a lock file.

        Returns:
            None

        Raises:
            None
        """
        self._isMultiProcessControl = True
        self._rotatingFileSizeEnforcer.initMultiProcessControl(controlFileName=controlFileName)        

    def open (self, mode = "a", buffering = None):  
        """open the file

        Args:
            mode: file open mode for the first file to be opened. other files will be opened in "w" mode
            buffering: same as in the built-in "open" command

        Returns:
            None

        Raises:
            IOError: same as in the built-in "open" command
            a.infra.lock.multi_process.LockError - when lock is not taken when required (only working in multi processes mode). 
        """
        
        self._verifyLockTakenIfNeeded()
        self._buffering = buffering            
        self._rotatingFileSizeEnforcer.prepare()
        self._rotatingFileSizeEnforcer.moveCurrentToPending()
        newFileName = self._rotatingFileSizeEnforcer.getCurrentFileName()
        self._log("open").debug1("first file name '%s'", newFileName)
        File.__init__(self, logger = self._log, fileName = newFileName, mode = mode, buffering = buffering)
        self._wasOpened = True

    def _closeFd (self):        
        File._closeFd(self)

    def beginMultiProcessFileOperations (self):
        """
        reopen the file if we are in a multi process mode

        Returns:
            None

        Raises:
            OSError
            a.infra.lock.multi_process.LockError - when lock failed (only working in multi processes mode)
        """
        self._tryAcquireMultiProcessLockIfActivated()
        if not self._wasOpened:
            return

        fileName = self._rotatingFileSizeEnforcer.getCurrentFileName()
        try:
            fd = open(fileName)
        except:#file became pending
            self._rotatingFileSizeEnforcer.learnCurrentFileName()
            newFileName = self._rotatingFileSizeEnforcer.getCurrentFileName() #TODO(NBS): need to verify not None
            self._log("reopen-another").debug1("Flex output file reopen another file: old %s, new %s", fileName, newFileName)
            fileName = newFileName
        else:
            fd.close()

        self._openFd(fileName = fileName, mode = "a", buffering = self._buffering)


    def endMultiProcessFileOperations (self):
        """
        reopen the file if we are in a multi process mode

        Returns:
            None

        Raises:
            OSError
            a.infra.lock.multi_process.LockError - when lock failed (only working in multi processes mode)
        """
        if self._wasOpened:
            self._closeFd()
        self._releaseMultiProcessLockIfActivated()

        

    def setTotalSize (self, totalSize):
        """set the max total size of the file
        Total size is the sum of all the files matching the glob pattern given in the ctor.
        The size is enforced upon when this function is called, as well as when 
        calling to the "enforceSize" or "reopenNextFile" functions

        Args:
            totalSize: Max total size of all the files. "0" for no size enforcement

        Returns:
            None

        Raises:
            OSError
            a.infra.lock.multi_process.LockError - when lock is not taken when required (only working in multi processes mode). 
        """

        self._verifyLockTakenIfNeeded()
        self._log("set-max-size").debug2("setting flex file max total size to '%d'", totalSize)
        #important: minNumOfFilesToKeep>=1. o.w. we will not have a chance to close the file properly+other bugs
        self._rotatingFileSizeEnforcer.setTotalSize(totalSize, minNumOfFilesToKeep=1)


    def reopenNextFile(self, dontReopenSameFile = False):
        """close the current file and open the next file.
        This function also enforce the total size of the file

        Args:
            dontReopenOnSameFile - don't reopen the file if the file name created based on the file name pattern did not changed

        Returns:
            True if file name was changed. False o.w.

        Raises:
            IOError: same as in the built-in "open"+"close" commands
            OSError: in case of a faliure in the enforce size operation
            a.infra.lock.multi_process.LockError - when lock is not taken when required (only working in multi processes mode)
        """

        self._verifyLockTakenIfNeeded()
        self._rotatingFileSizeEnforcer.rotate()
        newFileName = self._rotatingFileSizeEnforcer.getCurrentFileName()
        if newFileName == self.getFileName() and dontReopenSameFile:
            self._log("reopen-skipped").debug1("Flex output file skipped reopen: old and new files name are identical (%s)", newFileName)
            return False

        self._log("reopen").debug1("Flex output file reopen: old %s, new %s", self.getFileName(), newFileName)
        self._closeFd()        
        self._rotatingFileSizeEnforcer.moveCurrentToPending()
        self._openFd(fileName = newFileName, mode = "w", buffering = self._buffering)
        return True
        

    def close (self):
        self._wasOpened = False
        File.close(self)
        self._rotatingFileSizeEnforcer.shutdown()

    def enforceSize(self):
        """Enforce the total size of the file.
        One file is kept even if total size exceeded

        Args:
            None

        Returns:
            None

        Raises:
            OSError
            a.infra.lock.multi_process.LockError - when lock is not taken when required (only working in multi processes mode)
        """

        self._verifyLockTakenIfNeeded()
        self._log("enforce-size").debug1("enforce size")
        self._rotatingFileSizeEnforcer.enforceSize()


    def _tryAcquireMultiProcessLockIfActivated (self):
        if self._isMultiProcessControl:
            self._rotatingFileSizeEnforcer.tryAcquireMultiProcessLock()
 
    def _releaseMultiProcessLockIfActivated (self):
        if self._isMultiProcessControl:
            self._rotatingFileSizeEnforcer.releaseMultiProcessLock()

    def _verifyLockTakenIfNeeded (self):
        if self._isMultiProcessControl:
            self._rotatingFileSizeEnforcer.verifyIsMultiProcessLockTaken()



