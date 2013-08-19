#
#Copyright Qwilt, 2010
#
#The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
#Author: nirs
#

if  __package__ is None:
    G_NAME_GROUP_STD_ARCHIVER = "unknown"
else:
    from . import G_NAME_GROUP_STD_ARCHIVER

import os
import glob
import shutil
import subprocess
from a.infra.basic.return_codes import ReturnCodes, ReturnCode

class StdArchiver(object):
    """This class is used to follow a pattern of files and archive them
    """
    COMPRESSION_METHOD_GZIP = "gzip"
    COMPRESSION_METHOD_GZIP_BEST = "gzip-best"
    COMPRESSION_METHOD_GZIP_FAST = "gzip-fast"
    COMPRESSION_METHOD_BZ2  = "bz2"
    COMPRESSION_METHOD_BZ2_BEST  = "bz2-best"
    COMPRESSION_METHOD_BZ2_FAST  = "bz2-fast"
    COMPRESSION_METHOD_NONE = "none"


    def __init__ (self, logger, sourceDir, fileNameGlobPattern): 
        """ctor

        Returns:
            None

        Raises:
            None
        """   
        self._log = logger.createLoggerSameModule(G_NAME_GROUP_STD_ARCHIVER, instance = sourceDir.replace(os.sep, "_"))
        self._log("create").debug2("creating a std archiver")
        self._sourceDir = sourceDir
        self._sourceFileNameGlobPattern = fileNameGlobPattern
        self._fileNameConvertCallback = lambda x: x
        self._targetFilesGlobPattern = None
        self._targetDir = None
        self._deleteEmptyFiles = False
        self._compressionMethod = self.COMPRESSION_METHOD_NONE
        self._addCompressionDefaultExtenssion = False
        self._totalSize = -1
        self._considerBlockSize = False
        self._shallStopFunctor = None

        self._initDone = False
        
        self._log("create").debug2("creating a std archiver")


    def initTargetDir (self, targetDir):
        """Init the target dir, if not called the target dir will be the source dir.
           Function will fail if initDone was already called
        Args:
            targetDir: the directory in which the symlink shall reside. direcotry must exists. if set to none, the use the fileDir as default

        Returns:
            a.infra.basic.return_codes.ReturnCodes

        Raises:
            None
        """
        if self._initDone:
            self._log("init-target-after-done").error("init target dir after init stage was done. targetDir:%s", 
                                                      targetDir)
            return ReturnCodes.kGeneralError

        self._targetDir = targetDir
        return ReturnCodes.kOk

    def initTargetFileNameConversion (self, fileNameConvertCallback):
        """Init the conversion of a source file name of the target file name
        If not called file name will not be changed (but possibly will be added with a compression extension)
        Function will fail if initDone was already called
        Args:
            fileNameConvertCallback: a function that gets a source file name and returns a target file name. 
                                     The conversion function does not need to add the compression extension when flaged to be added automatically in the initCompression function

        Returns:
            a.infra.basic.return_codes.ReturnCodes

        Raises:
            None
        """
        if self._initDone:
            self._log("init-conversion-after-done").error("init target file name conversion after init stage was done. "
                                                          "fileNameConvertCallback:%s", fileNameConvertCallback)
            return ReturnCodes.kGeneralError

        self._fileNameConvertCallback = fileNameConvertCallback
        return ReturnCodes.kOk

    def initCompression (self, compressionMethod, addDefaultExtension):
        """Init the compression of the target file
        If not called files will not be compressed
        Function will fail if initDone was already called
        Args:
            compressionMethod: on of the COMPRESSION_METHOD_... consts 
            addDefaultExtension: add the default extensions to the created files names

        Returns:
            a.infra.basic.return_codes.ReturnCodes

        Raises:
            None
        """
        if self._initDone:
            self._log("init-compression-after-done").error("init compression method after init stage was done. "
                                                           "compressionMethod:%s, addDefaultExtension:%s", 
                                                           compressionMethod, addDefaultExtension)
            return ReturnCodes.kGeneralError

        self._compressionMethod = compressionMethod
        self._addCompressionDefaultExtenssion = addDefaultExtension

        return ReturnCodes.kOk

    def initDeleteEmptyFiles (self):
        """Init so empty files wil not be archived but deleted
        Function will fail if initDone was already called
        Args:
            None

        Returns:
            a.infra.basic.return_codes.ReturnCodes

        Raises:
            None
        """
        if self._initDone:
            self._log("init-after-done").error("init method after init stage was done. ")
            return ReturnCodes.kGeneralError

        self._deleteEmptyFiles = True

        return ReturnCodes.kOk

    def initTotalSize (self, totalSize, targetFilesGlobPattern, considerBlockSize):
        """Init the total allowed size of the target files
        If not called no files size enforcement is set
        Function will fail if initDone was already called
        Args:
            totalSize: total size to be enforced. -1 for no enforcement
            targetFilesGlobPattern: the target file name glob pattern to be used for size enforcment
                                    If the "initTargetFileNameConversion" function is not used, None can be given
                                    The glob pattern does not need to include the compression extension when flaged to 
                                    be added automatically in the initCompression function
            considerBlockSize: when true real size of files on disks will be used

        Returns:
            a.infra.basic.return_codes.ReturnCodes

        Raises:
            None
        """
        if self._initDone:
            self._log("init-size-after-done").error("init total size after init stage was done. totalSize:%d", totalSize)
            return ReturnCodes.kGeneralError

        self._totalSize = totalSize
        self._targetFilesGlobPattern = targetFilesGlobPattern
        self._considerBlockSize = considerBlockSize
        return ReturnCodes.kOk


    def initDone (self):
        """Init the done - must be called before calling the class operational functions
        Args:
            None

        Returns:
            a.infra.basic.return_codes.ReturnCodes

        Raises:
            None
        """
        if self._initDone:
            self._log("init-done-done").warning("init done twice")
            return ReturnCodes.kOk


        if self._sourceDir is None:
            self._log("no-source").error("init done with no source dir")
            return ReturnCodes.kGeneralError

        if self._sourceFileNameGlobPattern is None:
            self._log("no-source-pattern").error("init done with no source pattern")
            return ReturnCodes.kGeneralError

        if self._targetDir is None:
            self._targetDir = self._sourceDir

        if self._targetFilesGlobPattern is None:
            self._targetFilesGlobPattern = self._sourceFileNameGlobPattern

        if self._addCompressionDefaultExtenssion:
            if self._compressionMethod in [self.COMPRESSION_METHOD_GZIP, self.COMPRESSION_METHOD_GZIP_BEST, self.COMPRESSION_METHOD_GZIP_FAST]:
                self._log("add-gz-extension").debug1("Files will be added with the gz extension")
                origCallback = self._fileNameConvertCallback
                self._fileNameConvertCallback = lambda x: origCallback(x)+".gz"
                self._targetFilesGlobPattern = self._targetFilesGlobPattern+".gz"                
            if self._compressionMethod in [self.COMPRESSION_METHOD_BZ2, self.COMPRESSION_METHOD_BZ2_BEST, self.COMPRESSION_METHOD_BZ2_FAST]:
                self._log("add-bz2-extension").debug1("Files will be added with the bz extension")
                origCallback = self._fileNameConvertCallback
                self._fileNameConvertCallback = lambda x: origCallback(x)+".bz2"
                self._targetFilesGlobPattern = self._targetFilesGlobPattern+".bz2"                

        self._initDone = True
        return ReturnCodes.kOk

    def setStopFlagFunctor (self, shallStopFunctor):
        """Provide a functor that if return True or Fail the archive function will stop after the nect file
        Args:
            stopFunctor - functor

        Returns:
            None

        Raises:
            None
        """
        self._shallStopFunctor = shallStopFunctor

    def archive (self, doBeforeEachFile=None, doAfterEachFile=None):
        """Main function of the class
        Function will fail if initDone was not called

        Args:
            doBeforeEachFile - functor to be called before a file archiving. 
                               the function arguments are:
                               sourceDir, sourceFileName, targetDir, targetFileName
            doAfterEachFile  - functor to be called after a file archiving
                               the function arguments are:
                               An object of type a.infra.basic.return_codes.ReturnCodes

        Returns:
            a.infra.basic.return_codes.ReturnCodes. In case of success the value is the amount of pending files

        Raises:
            None
        """

        if not self._initDone:
            self._log("archive-no-init").error("Trying to archive with no-init")
            return ReturnCodes.kGeneralError

        return self._archiveFiles(doBeforeEachFile, doAfterEachFile)

    def enforceSize (self):
        """enforce size the target size
        Function will fail if initDone was not called

        Args:
            None

        Returns:
            a.infra.basic.return_codes.ReturnCodes.

        Raises:
            None
        """

        return self._enforceTargetSize()

    def _archiveFiles (self, doBeforeEachFile, doAfterEachFile):
        if not os.path.exists(self._targetDir):
            try:
                self._log("create-target-dir").debug1("creating the target dir '%s'", self._targetDir)
                os.makedirs(self._targetDir)
            except:
                self._log("failed-create-target-dir").exception("Failed to create the target dir '%s'", self._targetDir)
                return ReturnCodes.kGeneralError

        (rc, sourceFiles) = self._getFilesList(self._sourceDir, self._sourceFileNameGlobPattern)
        if not rc.success():
            self._log("failed-archive-list").error("Failed to create list of directories to archive")
            return ReturnCodes.kGeneralError

        for fileName in sorted(sourceFiles):
            if self._shallStopFunctor is not None:
                try:
                    shallStop = self._shallStopFunctor()
                    if shallStop:
                        self._log("shall-stop").debug1("The stop funcor returned True. stopping")
                        break
                except:
                    self._log("shall-stop-fail").exception("The shall stop functor failed. stopping")
                    break

            sourceFileName = os.path.basename(fileName)
            try:
                targetFileName = self._fileNameConvertCallback(sourceFileName)
            except:
                self._log("failed-convert-file-name").exception("Failed to convert source file name '%s'", sourceFileName)
                return ReturnCodes.kGeneralError
            if not isinstance(targetFileName, str):
                self._log("invalid-convert").exception("Invalid conversion of file name '%s' to '%s'", sourceFileName, targetFileName)
                return ReturnCodes.kGeneralError

            try:
                if doBeforeEachFile:
                    self._log("before").debug3("Calling a function needed before the archiving of file %s", sourceFileName)
                    doBeforeEachFile(self._sourceDir, sourceFileName, self._targetDir, targetFileName)
            except:
                self._log("before-failed").exception("Exception thrown while calling to a function needed before the archiving of file %s", sourceFileName)
                #going on to the other files - we dont want one bad file to stop use from doing the rest our work forever
                continue

            rc = self._archiveFile(self._sourceDir, sourceFileName, self._targetDir, targetFileName)
            if not rc.success():
                #going on to the other files - we dont want one bad file to stop use from doing the rest our work forever
                pass                
            
            try:
                if doAfterEachFile:
                    self._log("after").debug3("Calling a function needed after the archiving of file %s", sourceFileName)
                    doAfterEachFile(rc)
            except:
                self._log("after-failed").exception("Exception thrown while calling to a function needed after the archiving of file %s", sourceFileName)
                #going on to the other files - we dont want one bad file to stop use from doing the rest our work forever
                continue            

        return ReturnCode(len(sourceFiles), "")


    def _archiveFile (self, sourceDir, sourceFileName, targetDir, targetFileName):        
        sourceFileFullName = os.path.join(sourceDir, sourceFileName)

        if self._deleteEmptyFiles:
            fileWasEmpty = False
            try:
                if os.path.getsize(sourceFileFullName) == 0:
                    fileWasEmpty = True
                    os.remove(sourceFileFullName)
            except:
                if os.path.exists(sourceFileFullName):
                    self._log("failed-remove-file").error("Failed to remove empty file: %s", sourceFileFullName)
                    return ReturnCodes.kGeneralError
                else:
                    #file might have been removed by the file creator. This should not happen
                    self._log("failed-remove-no-file").warning("Failed to remove file: %s - likely since it is no longer there", 
                                                               sourceFileFullName)
                    return ReturnCodes.kOk
            else:               
                self._log("deleted").notice("Deleted empty file %s", sourceFileFullName)

            if fileWasEmpty:
                return ReturnCodes.kOk


        targetFileFullName = os.path.join(targetDir, targetFileName)
        if os.path.exists(targetFileFullName):
            self._log("overrun-file").warning("Overruning file '%s'", targetFileFullName)
        targetTempFileFullName = targetFileFullName+".tmp"
        if os.path.exists(targetTempFileFullName):
            self._log("overrun-file").warning("might overrun file '%s'", targetTempFileFullName)

        if self._compressionMethod in [self.COMPRESSION_METHOD_GZIP, self.COMPRESSION_METHOD_GZIP_BEST, self.COMPRESSION_METHOD_GZIP_FAST]:
            cmd = ["gzip"]
            if self._compressionMethod == self.COMPRESSION_METHOD_GZIP_BEST:
                cmd.append("--best")
            if self._compressionMethod == self.COMPRESSION_METHOD_GZIP_FAST:
                cmd.append("--fast")                        
            cmd += ["--stdout", sourceFileName]
            rc = self._runCommand(cmd, sourceDir, targetTempFileFullName)
            if not rc.success():
                if os.path.exists(sourceFileFullName):
                    self._log("failed-zip-file").error("Failed to zip file: %s", sourceFileName)
                    return ReturnCodes.kGeneralError
                else:
                    #file might have been removed by the file creator. This should not happen
                    self._log("failed-zip-no-file").warning("Failed to zip file: %s - likly since it is no longer there", 
                                                            sourceFileName)
            else:
                try:
                    os.rename(targetTempFileFullName, targetFileFullName)
                except:
                    self._log("failed-rename-file").error("Failed to rename target file: %s==>%s", 
                                                          targetTempFileFullName, targetFileFullName)
                    return ReturnCodes.kGeneralError

                try:
                    os.remove(os.path.join(sourceDir, sourceFileName))
                except:
                    if os.path.exists(sourceFileFullName):
                        self._log("failed-remove-file").error("Failed to removezip file: %s", sourceFileName)
                        return ReturnCodes.kGeneralError
                    else:
                        #file might have been removed by the file creator. This should not happen
                        self._log("failed-rempve-no-file").warning("Failed to remove file: %s - likly since it is no longer there", 
                                                                sourceFileName)

        elif self._compressionMethod in [self.COMPRESSION_METHOD_BZ2, self.COMPRESSION_METHOD_BZ2_BEST, self.COMPRESSION_METHOD_BZ2_FAST]:
            cmd = ["bzip2"]
            if self._compressionMethod == self.COMPRESSION_METHOD_BZ2_BEST:
                cmd.append("--best")
            if self._compressionMethod == self.COMPRESSION_METHOD_BZ2_FAST:
                cmd.append("--fast")
            cmd += ["--stdout", sourceFileName]
            rc = self._runCommand(cmd, sourceDir, targetTempFileFullName)
            if not rc.success():
                if os.path.exists(sourceFileFullName):
                    self._log("failed-bz2-file").error("Failed to bz2 file: %s", sourceFileFullName)
                    return ReturnCodes.kGeneralError
                else:
                    #file might have been removed by the file creator. This should not happen
                    self._log("failed-bz2-no-file").warning("Failed to bz2 file: %s - likly since it is no longer there", 
                                                            sourceFileFullName)
            else:
                try:
                    os.rename(targetTempFileFullName, targetFileFullName)
                except:
                    self._log("failed-rename-file").error("Failed to rename target file: %s==>%s", 
                                                          targetTempFileFullName, targetFileFullName)
                    return ReturnCodes.kGeneralError

                try:
                    os.remove(os.path.join(sourceDir, sourceFileName))
                except:
                    if os.path.exists(sourceFileFullName):
                        self._log("failed-remove-file").error("Failed to remove bz2 file: %s", sourceFileFullName)
                        return ReturnCodes.kGeneralError
                    else:
                        #file might have been removed by the file creator. This should not happen
                        self._log("failed-rempve-no-file").warning("Failed to remove file: %s - likly since it is no longer there", 
                                                                   sourceFileFullName)

        elif self._compressionMethod == self.COMPRESSION_METHOD_NONE:
            try:
                shutil.move(os.path.join(sourceDir, sourceFileName), targetFileFullName)
            except:
                if os.path.exists(sourceFileFullName):
                    self._log("failed-move-file").error("Failed to move file: %s", sourceFileFullName)
                    return ReturnCodes.kGeneralError
                else:
                    #file might have been removed by the file creator. This should not happen
                    self._log("failed-move-no-file").warning("Failed to move file: %s - likly since it is no longer there", 
                                                             sourceFileFullName)

        else:
            self._log("no-compression-method").error("Failed to compress file: %s. Method %s is not supported", sourceFileName, self._compressionMethod)
            return ReturnCodes.kGeneralError

        self._log("archived").notice("Archived file: %s to %s", sourceFileFullName, targetFileFullName)
        return ReturnCodes.kOk


    def _runCommand (self, cmd, cwd, outputFileName):
        try:
            with open(outputFileName, "w") as fd:
                popen = subprocess.Popen(cmd, cwd=cwd, stdout=fd, stderr=subprocess.PIPE)
                (stdoutData, stderrData) = popen.communicate()
                rc = popen.returncode
        except:
            self._log("command-call-failed").exception("command '%s' from '%s' excecution failed.", cmd, cwd)
            return ReturnCodes.kGeneralError

        if rc!=0:
            self._log("command-failed").error("command '%s' from '%s' failed. rc=%d. stderr=%s", cmd, cwd, rc, stderrData)
            return ReturnCodes.kGeneralError
        elif stderrData:
            self._log("command-stderr").warning("called command '%s' from '%s' emitted data to stderr. rc=%d. stderr=%s", cmd, cwd, rc, stderrData)
        else:
            self._log("command-called").debug3("called command '%s' from '%s' failed. rc=%d. stderr=%s", cmd, cwd, rc, stderrData)

        return ReturnCodes.kOk

    def _getFilesList (self, dirName, globPattern):
        matchingFiles = []
        try:
            if os.path.exists(dirName):
                matchingPathes = glob.glob(os.path.join(dirName,globPattern))
                for path in matchingPathes:
                    if os.path.isfile(path):
                        matchingFiles.append(path)
        except:
            self._log("list-failed").exception("failed to list dir.", dirName, globPattern)
            return (ReturnCodes.kGeneralError, [])

        toReturn = sorted(matchingFiles)
        self._log("list-dir").debug3("listing dir '%s' resulted with the files: %s", dirName, toReturn)
        return (ReturnCodes.kOk, toReturn)

    def _enforceTargetSize(self):
        """Enforce the total size of the file

        Args:
            None

        Returns:
            None

        Raises:
            OSError
        """

        if self._totalSize < 0:            
            return ReturnCodes.kOk

        self._log("clean").debug1("clean old files")

        (rc, filesInDir) = self._getFilesList(self._targetDir, self._targetFilesGlobPattern)
        if not rc.success():
            self._log("failed-archive-list").error("Failed to create list of directories to enforce size")
            return ReturnCodes.kGeneralError

        numOfFiles = 0
        totalSize = 0        
        filesDict = {}            
        for fullFileName in filesInDir:
            size = self._getFileSize(fullFileName)  
            filesDict[fullFileName]=size
            numOfFiles+=1
            totalSize+=size            
            self._log("clean-dir-found-file").debug4("clean old files: found file '%s' of size %d", fullFileName, size)

        self._log("clean-initial-size").debug2("clean old files: initial num of files '%d' of size '%d'", numOfFiles, totalSize)

        for fileFullName in sorted(filesDict):            
            if totalSize <= self._totalSize:
                self._log("reached-target-size").debug3("reached target size ('%d'<= '%d')", totalSize, self._totalSize)
                break
            
            self._log("removing-file").notice("removing file '%s' of size %d", fileFullName, filesDict[fileFullName])
            try:
                os.remove(fileFullName)
            except:
                if os.path.exists(fileFullName):
                    self._log("failed-remove-file").error("Failed to remove archived file: %s", fileFullName)
                    #going on to the other files - we dont want one bad file to stop use from doing the rest our work forever
                else:
                    #file might have been removed by the file creator. This should not happen
                    self._log("failed-remove-no-file").warning("Failed to remove archived file: %s - likly since it is no longer there", 
                                                               fileFullName)
                

            numOfFiles -=1
            totalSize -= filesDict[fileFullName]            

        self._log("clean-final-size").debug2("clean old files: final size is '%d'", totalSize)
        return ReturnCodes.kOk

    def _getFileSize (self, fileNameFullPath):
        if self._considerBlockSize:
            try:
                return os.stat(fileNameFullPath).st_blocks*512
            except:
                self._log("failed-stat").warning("failed to get file size, will consider as 0")
                return 0
        else:
            try:
                return os.path.getsize(fileNameFullPath)
            except:
                self._log("failed-get-size").warning("failed to get file size, will consider as 0")
                return 0



