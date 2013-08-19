# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: alexb

from threading import Lock

class AtomicInt:
    """ An int value that may be updated atomically @ thread-safe
    """
    def __init__ (self, initVal=0):
        self.val = initVal
        self.lock = Lock()

    def add (self, addVal):
        with self.lock:
            self.val += addVal

    def get (self):
        with self.lock:
            return self.val

    def set (self, setVal):
        with self.lock:
            self.val = setVal
