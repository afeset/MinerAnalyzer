# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

# This class is a handy guard against double initializations

import a.infra.process.captain

class InitGuard (object):
    def __init__ (self):
        self.myWasInit=False
        self.myInitInProgress=False

    def startInit (self):
        self.crashIfInitDone()
        self.myInitInProgress=True

    def initDone (self):
        self.crashIfInitDone(checkInitInProgress=False)
        self.myWasInit=True
        self.myInitInProgress=False

    def isInit (self):
        return self.myWasInit

    def isInitOrCrash (self):
        if (not self.myWasInit):
            a.infra.process.processFatal("InitGuard(): Not initialized")

    def crashIfInitDone (self, checkInitInProgress=True):
        if (self.myWasInit):
            a.infra.process.processFatal("InitGuard(): Already initialized")
        if (checkInitInProgress and self.myInitInProgress):
            a.infra.process.processFatal("InitGuard(): Init started")

