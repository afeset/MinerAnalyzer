# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: amiry

# A time based sliding window. Can count multiple named counters

from time import time

class SlidingWindow(object):

    def __init__(self, windowSizeSec, numFrames):
        self.windowSizeSec = windowSizeSec
        self.numFrames = numFrames
        self.frameSizeSec = windowSizeSec / (numFrames * 1.0)
        self.reset()
        
    def reset(self):
        self.frames = [{} for _ in range(self.numFrames)]
        self.lastFrameStartSec = time()

        # The reference count dictionary contains the number of frames in which the key exists.
        # Its purpose is to implement the getNumKeys() method.
        # Every time we insert a new key to the first frame you increment the key's ref count.
        # Every time we drop the last frame we decrement the ref  counts for all the keys in that frame.
        # The length of the dictionary is the number of keys in the sliding window.
        self.keysRefCount = {}
        
    def add(self, name, value):
        self.__slide()    
        frame = self.frames[self.numFrames-1]
        count = frame.get(name, None)
        if count is None:
            refCount = self.keysRefCount.get(name, 0)
            self.keysRefCount[name] = refCount + 1
            count = 0
        count = count + value
        frame[name] = count

    def addMulti(self, **kwargs):
        self.__slide()    
        for name in kwargs:
            self.add(name, kwargs[name])
                
    def getCount(self, name):
        self.__slide()
        count = 0
        for frame in self.frames:
            count = count + frame.get(name, 0)
        return count

    def getNumKeys (self):
        self.__slide()
        return len(self.keysRefCount)

    def __slide(self):
        delta = time() - self.lastFrameStartSec
        if delta - self.windowSizeSec > 0:
            self.reset()
            return

        while delta - self.frameSizeSec > 0:
            self.__decrementKeysRefCount()
            for i in range(0, self.numFrames-1):
                self.frames[i] = self.frames[i+1]
            self.frames[self.numFrames-1] = {}
            delta = delta - self.frameSizeSec
            self.lastFrameStartSec += self.frameSizeSec                

    def __decrementKeysRefCount (self):
        for key in self.frames[0]:
            if self.keysRefCount[key] == 1:
                del(self.keysRefCount[key])
            else:
                self.keysRefCount[key] -= 1


        
