#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

if  __package__ is None:
    G_NAME_GROUP_FILE = "unknown"
else:
    from . import G_NAME_GROUP_FILE

class File(object):
    """This class is a wrapper for the python built in "file" object.

     It implements the same interface and can be used as a base for other derived 
     classes that need trasparently replace a "file" object
    """
    def __init__ (self, logger, fileName, mode = "r", buffering = None):
        """open the file
        This ctor is equivalent to the python built in "open" command
        
        Args:
            logger: logger used by this class for logging
            fileName: same as in the built-in "open" command
            mode: same as in the built-in "open" command
            buffering: same as in the built-in "open" command
        
        Raises:
            IOError: same as in the built-in "open" command
        """
        self._fileDescriptor = None
        if not hasattr(self, "_log"):
            self._log = logger.createLoggerSameModule(G_NAME_GROUP_FILE, instance = fileName)
        self._openFd(fileName, mode, buffering)

    def close (self):
        """close the file
        Any operation which requires that the file be open will raise a ValueError after the file has been closed. 
        Calling close() more than once is allowed.

        Args:
            None

        Returns:
            None

        Raises:
            IOError: same as in the built-in "close" command
        """
        self._closeFd()

    def getFileSize(self):
        """Get the current file size. Valid only if the file is opened
        In case of a failure, the file will be closed automatically
        Args:
            None

        Returns:
            The current file size. 
            "None" in case of failure (e.g. a closed file)

        Raises:
            None
        """

        __pychecker__ = "no-classattr"
        if self.closed:
            self._log("size-on-closed", isForceStackTrace=True).error("Trying to get a file size for a closed file '%s'", self._fileName)
            return None
        try:
            currentPossition = self.tell()
            self._log("get-file-size-current-possition").debug3("getting file size - current possition %d.", currentPossition)
            self.seek(0, 2) 
            toReturn = self.tell()
            self._log("get-file-size-last-possition").debug3("getting file size - last possition %d.", toReturn)
            self.seek(currentPossition, 0)
            self._log("get-file-size-return").debug1("getting file size: returning %d", toReturn)
            return toReturn
        except:
            self._log("fail-to-size").exception("Failed to test file '%s' size. closing file", self._fileName)
            self._closeOnFailure()
            return None

    def getFileName (self):
        """Get the file name. 

        Args:
            None

        Returns:
            The file name. 

        Raises:
            None
        """
        self._log("get-file-name").debug4("getting file name: returning %s", self._fileName)
        return self._fileName


    def _openFd (self, fileName, mode, buffering):
        self._fileName = fileName
        self._log("open").debug1("Opening file '%s', mode=%s, buffering=%s.", self._fileName, mode, str(buffering))
        try:
            if buffering is None:
                self._fileDescriptor = open(fileName, mode)
            else:
                self._fileDescriptor = open(fileName, mode, buffering)
        except:
            self._log("open-failed").exception("Failed to open file '%s'.", self._fileName)
            raise

    def _closeFd (self):
        self._log("close").debug1("Closing file '%s'.", self._fileName)
        self._fileDescriptor.close()

    def __getattr__(self, item):
        """Maps values to attributes.
        Only called if there isn't an attribute with this name
        Comes to cover basinc file operations
        """
        if item == "_fileDescriptor":
            return self.__dict__[item]
        try:
            attribute = getattr(self._fileDescriptor, item)
        except KeyError:
            raise AttributeError(item)

        return attribute

    def _closeOnFailure (self):
        self._log("emerg-close", isForceStackTrace = True).debug1("Closing file %s due to a failure.", self._fileName)

        try:
            self._fileDescriptor.close()
        except:
            self._log("emerg-close-failed").exception("Failed to emergency close file %s.", self._fileName)


