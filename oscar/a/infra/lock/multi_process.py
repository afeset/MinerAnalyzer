#
#Copyright Qwilt, 2010
#
#The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
#Author: nirs
#
import fcntl

class ErrorBase(Exception):
    pass

class LockError(ErrorBase):
    pass

class RedundentUnlockError(ErrorBase):
    pass

class MissingUnlockError(ErrorBase):
    pass

class RLock(object):
    def __init__ (self): 
        self._lockFd = None
        self._lockCount = 0

    def prepare (self, lockFileName):
        """
        Raises:
            OSError - in case of failure in symlink creation of size enforcement
        """
        self._lockFd = open(lockFileName, "w")    

    def shutdown (self):
        if self._lockCount > 0:
            raise MissingUnlockError()
        self._lockFd.close()


    def tryAcquire (self):
        """ lock the multi process file if needed

        Returns:
            None

        Raises:
            LockError - when lock failed
        """
        if self._lockCount <= 0:
            try:    
                fcntl.lockf(self._lockFd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except:
                raise LockError()

        self._lockCount += 1

    def verifyIsMultiProcessLockTaken (self):
        """ Raise if the multi process file is not taken

        Returns:
            None

        Raises:
            LockError - when lock failed
        """

        if self._lockCount <= 0:
            raise LockError()

    def release (self):
        """ release the multi process file if needed

        Returns:
            None

        Raises:
            None
        """
        
        if self._lockCount<=0:
            raise RedundentUnlockError()

        self._lockCount -= 1

        if self._lockCount != 0:
            return #lock shall still be taken

        fcntl.lockf(self._lockFd, fcntl.LOCK_UN)

