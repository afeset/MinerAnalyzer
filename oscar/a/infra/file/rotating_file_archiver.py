#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: matanc
# 

# Bypass for PyChecker
if  __package__ is None:
    G_NAME_GROUP_ARCHIVER = "unknown"
else:
    from . import G_NAME_GROUP_ARCHIVER

import datetime
import subprocess
import rotating_file_size_enforcer
import a.infra.file.utils
import a.infra.basic.return_codes
import os
import glob
import threading
import Queue
import time

# Consts
#-------

PROCESSED_FILES_SUFFIX = ".arc"
ZIP_FILES_SUFFIX = ".tgz"
DUMP_FILES_SUFFIX = ".DUMP_FROM_LAST_RUN"
BUFFER_DIR_BASENAME = "archiver-buffer"
MAIN_LOOP_SLEEP_TIME_IN_SEC = 0.1
MAX_QUEUE_SIZE = 300000
MEGA_BYTE = 1024*1024
GIGA_BYTE = 1024 *1024 *1024

# The name of the file that is currently being filled and will be archived when it reached the relevant limitation
PREFIX_FOR_DUMP_FROM_LAST_RUN = "forced_exit_dump_"

class Archiver (object):    
    """ This class should be used to zip files with rotating file mechanism
    """

    def __init__ (self, logger, inputDir, bufferDirSizeLimitInMB, outputDir, archiveFilePrefix = "archive-", bufferDir = BUFFER_DIR_BASENAME):
        """ Archiver's one and only Ctor
    
        Args:   
            Must fill:
            -   logger - An instance of the implementing module's logger to create a logger object from
            -   outputPath - The path where the currently written tar file and the zipped archive file are placed in
    
            Has defaults:
            - outFilePrefix   - What would be the initial string before the timestamp and the suffix of the archive file
            - rotateEveryHour - Should the archiver rotate itself every round hour?
            - archivingActive - Should the archiver should hit the road and archive right away after init?
            - totalFileSize   - The limit size of the tar file, which after it will flush it to zip file and start new one
            - totalDirSize    - The limit of the dir size, only calculates the zip files and not all the files in the directory
        """

        # INITIALIZATIONS & DEFAULTS
        self._logger = logger.createLoggerSameModule(G_NAME_GROUP_ARCHIVER) 
        self._outputPath = outputDir
        self._filesQueue = Queue.Queue(MAX_QUEUE_SIZE) # Size limit for bug proofing
        self._inputDir = inputDir
        self._bufferDir = os.path.join(inputDir, bufferDir)
        self._bufferDirSizeLimit = bufferDirSizeLimitInMB * MEGA_BYTE
        self._sizeOfBufferDir = 0
        self._lockSizeOfBufferDir = threading.Lock()
        self._sizeOfFilesAfterProcessing = 0
        self._outputFileSizeLimit = 0
        self._keepRunning = False # Will be True inside _initCheckForLastRunDump after init is finished
        self._zipFilePrefix = archiveFilePrefix

        self._rotationEnforcer = rotating_file_size_enforcer.RotatingFileSizeEnforcer(self._logger, self._outputPath, self._zipFilePrefix, ZIP_FILES_SUFFIX)
        self._rotationEnforcer.initConsiderSizesOnDisk()
        self._rotationEnforcer.setTotalSize(0)
        self._rotationEnforcer.prepare()


        # Default rotation due to time threshhold to 1 day
        self._timeDeltaThresholdForRotation = datetime.timedelta(days=1)
        self._timeOfLastArchiving = datetime.datetime.now()

        self._patternOfBufferedFiles = os.path.join(self._bufferDir, "*" + PROCESSED_FILES_SUFFIX)
        self._logger("pattern-of-buffered-files").debug1("pattern of buffered files is: %s", self._patternOfBufferedFiles)
        self._fixedFileSize = 0

        self._archivingThread = None
        self._exceptionCallBack = None

        
    def stop (self):
        """ Stops archiving

        -   Stops the archiver thread
        """ 

        self._keepRunning = False
        self._logger("stop-archiving").notice("archiver !!will not!! archive files even when writeFileToArchive is called")



    def isActive (self):
        """ Does the archiver is active right now?

        - True when waiting for files and will archive them

        Returns: archiving status
        """
        return self._keepRunning



    def setFileSizeThresholdMB (self, fileSizeInMB):
        """ Send buffered files to be zipped

        -   Can be co-exist with round hour file rotating mechanism
        -   makes the file rotate on certain size limitation
        -   File size is limited before archiving, actual zipped file size will be less then limit.
        -   Can be changed dynamically during run.

        args: Size limitation in MB, 0 for non-limitation

        returns: None

        raises: None
        """

        # Save limitation in bytes
        self._outputFileSizeLimit = fileSizeInMB * MEGA_BYTE



    def setOutputDirSizeLimitGB (self, dirSizeInGB):
        dirSizeInBytes = dirSizeInGB * GIGA_BYTE
        self._rotationEnforcer.setTotalSize(dirSizeInBytes)



    def setRotationTimeThersholdSeconds (self, secondsBetweenRotations):
        self._timeDeltaThresholdForRotation = datetime.timedelta(seconds = secondsBetweenRotations)



    def setUseFixedFileSize (self, fixedFileSize):
        """
            This should use to avoid using stat systemcall to get the file size.
            Instead the archiver will use the fixed file size givven in this method
            Zero means diabled
        """
        self._fixedFileSize = fixedFileSize


    def archiveFile (self, fileToBeArchived):
        """ sendToArchiveBuffer - Send a file to be archived

        - Send the file to the files queue
        - later the Queue-Processing thread will prepare them for archiving
        - deletes the file, it cannot be used after this call

        args:
         
        fileToArchive -         path of the file to be sent to archive (relative or full path)

        Returns: Success - if not succesful original file will NOT BE DELETED

        """
        # If archiver is active
        if self._keepRunning is True:
            self._logger("file-sent-to-archive").debug3("file <%s> was sent to archive", fileToBeArchived)
            # Aggregate current record file into my output file
            return self._bufferFile(fileToBeArchived)        

        else: # Archiver isn't active
            self._logger("file-sent-to-unactive-archiver").warning("file <%s> was sent to archive on init or shutdown", fileToBeArchived)    

        return False



    def flushBuffer (self):
        """ zip the processed files from the cahce to the archives folder

        -   Might be problematic becuase it does the backworker thread's work

        returns: success (True / False)
        """
        self._logger("send-processed-files-to-archive") \
        .debug3("buffer flushing was called by implementing module, flushing only files that were already processed")

        return self._flushBufferToArchive()

#------------------------------ Public for UT

    def processQueue (self):
        """
        Loop that goes over the buffer queue and handle files

        - Called by mainloop every 1ms
        - Send new files for handling
        - check for triggers

        """

        # Whenever there are files
        while not self._filesQueue.empty():
            self._handleFileFromQueue()

            # Check if flushing is needed
            if (self._checkFlushTimeTrigger() or self._checkFlushZipFileSizeTrigger()):
                self._flushBufferToArchive()
            
    def init (self):
        if (self._keepRunning is True):
            # Notify YOU (a revisionist programmer applying changes to this code) that you're probably abusing this code
            raise Exception("keepRunning supposed to be False on initiation according to original design")

        # Validate input and output exist
        self._logger("init-archiver") \
        .debug1("archiver was started, init is now executed")
        self._initIOPathes()
        self._initCheckForLastRunDump()
        if self._fixedFileSize > 0:
            self._logger("init-archiver").notice("archiver is using fixed file size of %d", self._fixedFileSize)
        self._keepRunning = True

#------------------------------ Private methods


    def _bufferFile (self, filePath):
        """ Adds a file to the queue list

            - Called by front thread
            - Adds timestamp to the file for uniqueness and for identifying it as OK
            - Signals the backworker thread about new file to buffer

            - DOESN'T remove file the original file if handling failed from any reason

            raises: None
        """  
        if self._fixedFileSize > 0:
            fileSize = self._fixedFileSize
        else:
            try:
                # Calc file size
                fileSize = os.stat(filePath).st_blocks * 512 # (it seems that stat().st_blksize isn't working good) 
            except Exception as exc:
                self._logger("couldnt-do-fstat-or-rename").error("call to fstat or rename failed with: %s", exc)
                return False

        # If input dir size limitation is reached, don't except the file
        if self._doesBufferDirFull(fileSize):

            self._logger("file-skipped-buffer").warning("file < %s > was not inserted to buffer because the buffer was full", filePath)

        else: # Buffer dir has enough space for this file
                    
            # Add timestamp to file
            try:
                enforcer = a.infra.file.rotating_file_size_enforcer.RotatingFileSizeEnforcer(self._logger, self._bufferDir, os.path.basename(filePath)+'-', "")
                enforcer.prepare()
                fileNewFullPath = enforcer.getCurrentFileName()
            except:
                self._logger("failed-create-new-file-name").exception("failed to create new file name")      
                return False

            try:
                os.rename(filePath, fileNewFullPath)
                self._logger("new-file-moved-to-buffer"). \
                debug3("input file %s was moved to  <%s>", filePath, fileNewFullPath)
    
            except Exception as exc:
                self._logger("failed-to-move-file").error("failed to move file %s to %s, exc: %s", filePath, fileNewFullPath, exc)      
                return False
                
        
            # Signal backworker using files_queue
            try:
                self._filesQueue.put_nowait((fileNewFullPath, fileSize))
                self._addToSizeOfBufferDir(fileSize)
                self._logger("file-inserted-to-buffer-output").debug3("The file %s was added to signaling queue for backworker thread to handle", fileNewFullPath)
        
            except:
                self._logger("buffer-queue-is-full").warning("backworker thread isn't up to the challenge")
                return False
        
            return True      
           

    def _initCheckForLastRunDump (self):
        """ Finds unarchiving files waiting from last run

            - Doesn't pack files that are not timestamped
        """

        # Collect All files left unprocessed (ends with number because date appended)
        listOfUnprocessedFiles = self._getAllLegalUnprocessedFiles()
        self._logger("files-from-last-run").info("found <%s> files left from last run", len(listOfUnprocessedFiles))
        for unprocessedFile in listOfUnprocessedFiles:
            self._logger("handling-leftover-file").debug1("signing file <%s> as handled (add '.arc')", unprocessedFile)
            self._signFileAsHandled(unprocessedFile)

        # Add dump suffix
        zipFileName = self._rotationEnforcer.getCurrentFileName()
        (root, ext) = os.path.splitext(zipFileName)
        zipFileName = root + DUMP_FILES_SUFFIX + ext
    
        # Zip All left over files and sign them as dump
        self._flushBufferToArchive(zipFileName)



    def start (self, exceptionCallBack):
        """ Start the archive thread

            Calls the mainLoop

            Args:
                exceptionCallBack = callback to run in case of exception
        """
        self.init()
        self._exceptionCallBack = exceptionCallBack

        self._logger("archiver-thread-created") \
        .debug1("initiation finished, processing thread created, main loop will be started")
        self._archivingThread = threading.Thread(target=self._mainLoopWraper)
        self._archivingThread.daemon = True
        self._archivingThread.start()



    def _mainLoopWraper (self):
        try:
            self._mainLoop()
        except Exception as exception:
            self._logger("archiver-thread-exception").error("got exception on thread. exception: %s", exception)
            if self._exceptionCallBack != None:
                self._logger("archiver-module-was-stopped").error("calling exceptionCallBack and terminating the archiver thread")
                self._exceptionCallBack(exception)


    def _mainLoop (self):
        """
        Calls process queue after some rest
        """
        while(self._keepRunning):
            self.processQueue()
            if (self._checkFlushTimeTrigger()):
                self._flushBufferToArchive()
            time.sleep(MAIN_LOOP_SLEEP_TIME_IN_SEC)

        # exit main loop when stop was called, process all the remain files and flush buffer
        self.processQueue()
        self._flushBufferToArchive()
        self._logger("archiver-module-was-stopped") \
        .notice("archiver had gracefull shutdown, bye!")
            

    def _handleFileFromQueue (self):
        """ Gets a file from the caching queue

        - Called by backworker thread
        - Signs the file as processed by adding suffix
        - Add it to queue size
        """

        # Get file from queue
        (fileFromQueue, fileFromQueueSize) = ("str", 0)
        try:
            (fileFromQueue, fileFromQueueSize) = self._filesQueue.get_nowait()
        except:
            self._logger("buffer-queue-is-empty").warning("someone else is getting data from the queue?")

        # Sign the file as handled (add ".arc")
        if self._signFileAsHandled(fileFromQueue):
            self._sizeOfFilesAfterProcessing += fileFromQueueSize



    def _signFileAsHandled (self, fileToSign):
        """
        Signs the file with ".arc" suffix

        -   This way I know i counted it in my calculations
        -   Files are supposed to have timestamp on them
        """
        try:
            os.rename(fileToSign, fileToSign + PROCESSED_FILES_SUFFIX)
            return True
        except Exception as exc:
            if os.path.isfile(fileToSign):
                try:
                    os.remove(fileToSign)
                except Exception as exc2:
                    self._logger("cannot-remove-file-that-cannot-be-handled").warning \
                        ("cannot remove < %s > after it couldnt be renamed, horrible error: %s", fileToSign, exc2)
            else:
                self._logger("file-to-buffer-doesnt-exist").warning("the file < %s > given to buffer doesnt exist failed with exc: %s", fileToSign, exc)
                return False

            self._logger("rename-when-handling-failed"). \
                warning("signing %s as handled (\".arc\") failed. the file will be collected on next startup", file)
            return False


    def _flushBufferToArchive (self, archiveFileName = None):
        """ Executes the actual zip command

        -   Compresses the buffered files created since last rotation until now using linux tar cmd.

        -   Can be called from two thread 

        args:
        archiveFileName -   The name of the output zip, defautls to rotation enforcer name - FULL PATH NEEDED!
        """
        # Because the default name is to be sent dynamically by rotation enfocrcer i use "None" and reassign it
        if  archiveFileName is None:
            archiveFileName = self._rotationEnforcer.getCurrentFileName()

        try:

            # Create archive only if no files exist
            listOfFilesReadyForArchiving = self._getAllProcessedFiles()
            numberOfFilesReadyForArchiving = len(listOfFilesReadyForArchiving)

            if numberOfFilesReadyForArchiving <= 0 :
                self._logger("flush-was-called-on-empty-buffer") \
                    .debug1("flush was called on empty buffer dir, no tgz file will be made")
            
            else : # There are files to archive
                self._logger("found-files-in-buffer") \
                    .debug2("an archive will be created from <%s> \"*.arc\" files on buffer dir", numberOfFilesReadyForArchiving)

                # Build tar cmd string
                tarcmd = "tar --directory %s --create --remove-files --gzip --file %s %s" %  \
                                 (self._bufferDir, archiveFileName, "*" + PROCESSED_FILES_SUFFIX)
    
                # Execute Tar cmd
                self.archiveProcess = subprocess.Popen(tarcmd, cwd = self._bufferDir, shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                retCode = self.archiveProcess.wait()
    
                if a.infra.basic.return_codes.ReturnCode(retCode, "kArchiveOK") != a.infra.basic.return_codes.ReturnCodes.kOk:
                    self._logger("tgz-file-return-no-zero").error("excuted Tar cmd: \n<%s> but it returned: %s" % \
                                                                  (tarcmd, retCode))
                    self._logger("tar-cmd-output").error("This is tar cmd stdout & stderr: %s ", self.archiveProcess.communicate())

                else:
                    self._logger("wrote-content-to-tar-file") \
                        .debug2("archive file %s was created", archiveFileName)
    
                    # Substract size of files from buffer dir
                    self._substractFromSizeOfBufferDir(self._sizeOfFilesAfterProcessing)

                    self._sizeOfFilesAfterProcessing = 0
                    self._timeOfLastArchiving = datetime.datetime.now()
                    # rotate() causes size enforcements on zip files
                    self._rotationEnforcer.rotate()
                    return True

        except Exception as exc:
                self._logger("tgz-file-creation-failed").error("Tried to make Tar file <%s> but it failed with exception: %s" % \
                                                 (archiveFileName, exc))

        return False        
            


    def _doesBufferDirFull (self, sizeOfFileToAdd):
        """
        Checks if buffer dir size is about to be over its limit

        - Isn't suppose
        """
        if self._sizeOfBufferDir + sizeOfFileToAdd > self._bufferDirSizeLimit:
            # Dir is full
            self._logger("buffer-dir-is-full") \
                .debug2("buffer dir size limit had been reached, will not add file. \
                    current size: %s + new file size: %s is over limit %s", self._sizeOfBufferDir, sizeOfFileToAdd, self._bufferDirSizeLimit)
            return True
        # else
        return False

    def _checkFlushTimeTrigger (self):
        """
         Check if passed more time then specified as limit since last archiving
        """
        if (datetime.datetime.now() - self._timeOfLastArchiving) > self._timeDeltaThresholdForRotation:
            return True
        return False

    def _checkFlushZipFileSizeTrigger (self):
        """
        Returns whether the size of all the files that are meant for archiving is bigger than the limit given

        -   This is the extracted files size and not the actual zip file's size
        """
        if (self._outputFileSizeLimit > 0 and (self._sizeOfFilesAfterProcessing > self._outputFileSizeLimit)):
            return True
        return False

    
    def  _getAllLegalUnprocessedFiles(self):
        """
         Returns a list of all unprocessed files that end with timestamp only

         - Files with timestamp were putted in directory by calling bufferfile()
         - Other junk files that got inside my buffer will not be included!
        """
        return glob.glob(os.path.join(self._bufferDir, "*[0-9]"))

    def _getAllProcessedFiles (self):
        """
        Returns a list of all processed files (that are terminated with ".arc")
        """
        return glob.glob(os.path.join(self._bufferDir, "*" + PROCESSED_FILES_SUFFIX))

    def _initIOPathes (self):
        """ Validates (and creates by the way) the output dir
        """
        # Validate output path
        if os.path.isdir(self._outputPath):
            self._logger("output-path-already-exist").debug1("found output path <%s> existing on init", self._outputPath)
        else:
            try:
                a.infra.file.utils.makeDirs(self._outputPath, absMode=0755, reuseExisting = True)
                self._logger("output-dir-created").debug1("created output dir <%s> during init", self._outputPath)
            except IOError:
                 self._logger("Cannot-create-output-folder").error("Tried to create output dir < %s > but failed", self._outputPath)
                 raise


        # Validate Input path
        if os.path.isdir(self._bufferDir):
            self._logger("buffer-path-already-exist").debug1("found buffer path <%s> existing on init", self._bufferDir)
        else:
            try:
                a.infra.file.utils.makeDirs(self._bufferDir, absMode=0755, reuseExisting = True)
                self._logger("buffer-path-already-exist").debug1("created buffer dir <%s> during init", self._bufferDir)
            except IOError:
                 self._logger("Cannot-create-input-folder").error("Tried to create input (buffer) dir < %s > but failed", self._bufferDir)
                 raise

    def _getDirSizeOnlyFiles (self, dirPath):
        """ Get Size of dir
        """
        sizeOfFiles = 0
        for root,dirs,files in os.walk(dirPath):
    
            for f in files:
                fp = os.path.join(root,f)
                sizeOfFiles += os.path.getsize(fp)  
        self._logger("get-dir-size").debug3("get dir size was called and returned: <%s>",sizeOfFiles)
        return sizeOfFiles

    def _substractFromSizeOfBufferDir (self, sizeToSubstract):
        with self._lockSizeOfBufferDir:
            self._sizeOfBufferDir -= sizeToSubstract


    def _addToSizeOfBufferDir (self, sizeToAdd):
        with self._lockSizeOfBufferDir:
            self._sizeOfBufferDir += sizeToAdd

