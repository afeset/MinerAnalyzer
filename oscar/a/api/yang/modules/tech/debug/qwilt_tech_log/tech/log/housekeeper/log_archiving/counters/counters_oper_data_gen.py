


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

# Must be set here to avoid stupid warnings about stuff in BlinkyOperData
__pychecker__="no-classattr"

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket





class CountersOperData (object):

    def __init__ (self):

        self.activeSeconds = 0
        self._myHasActiveSeconds=False
        self._myActiveSecondsRequested=False
        
        self.archivedFiles = 0
        self._myHasArchivedFiles=False
        self._myArchivedFilesRequested=False
        
        self.overallArchiveDurationWarning = 0
        self._myHasOverallArchiveDurationWarning=False
        self._myOverallArchiveDurationWarningRequested=False
        
        self.onePendingFile = 0
        self._myHasOnePendingFile=False
        self._myOnePendingFileRequested=False
        
        self.fileArchiveDurationErrors = 0
        self._myHasFileArchiveDurationErrors=False
        self._myFileArchiveDurationErrorsRequested=False
        
        self.overallArchiveDurationErrors = 0
        self._myHasOverallArchiveDurationErrors=False
        self._myOverallArchiveDurationErrorsRequested=False
        
        self.pendingFileCountErrors = 0
        self._myHasPendingFileCountErrors=False
        self._myPendingFileCountErrorsRequested=False
        
        self.pendingFileCountWarning = 0
        self._myHasPendingFileCountWarning=False
        self._myPendingFileCountWarningRequested=False
        
        self.dirScans = 0
        self._myHasDirScans=False
        self._myDirScansRequested=False
        
        self.fileArchiveDurationWarning = 0
        self._myHasFileArchiveDurationWarning=False
        self._myFileArchiveDurationWarningRequested=False
        
        self.archivedErrors = 0
        self._myHasArchivedErrors=False
        self._myArchivedErrorsRequested=False
        
        self.dirScansErrors = 0
        self._myHasDirScansErrors=False
        self._myDirScansErrorsRequested=False
        


    def copyFrom (self, other):

        self.activeSeconds=other.activeSeconds
        self._myHasActiveSeconds=other._myHasActiveSeconds
        self._myActiveSecondsRequested=other._myActiveSecondsRequested
        
        self.archivedFiles=other.archivedFiles
        self._myHasArchivedFiles=other._myHasArchivedFiles
        self._myArchivedFilesRequested=other._myArchivedFilesRequested
        
        self.overallArchiveDurationWarning=other.overallArchiveDurationWarning
        self._myHasOverallArchiveDurationWarning=other._myHasOverallArchiveDurationWarning
        self._myOverallArchiveDurationWarningRequested=other._myOverallArchiveDurationWarningRequested
        
        self.onePendingFile=other.onePendingFile
        self._myHasOnePendingFile=other._myHasOnePendingFile
        self._myOnePendingFileRequested=other._myOnePendingFileRequested
        
        self.fileArchiveDurationErrors=other.fileArchiveDurationErrors
        self._myHasFileArchiveDurationErrors=other._myHasFileArchiveDurationErrors
        self._myFileArchiveDurationErrorsRequested=other._myFileArchiveDurationErrorsRequested
        
        self.overallArchiveDurationErrors=other.overallArchiveDurationErrors
        self._myHasOverallArchiveDurationErrors=other._myHasOverallArchiveDurationErrors
        self._myOverallArchiveDurationErrorsRequested=other._myOverallArchiveDurationErrorsRequested
        
        self.pendingFileCountErrors=other.pendingFileCountErrors
        self._myHasPendingFileCountErrors=other._myHasPendingFileCountErrors
        self._myPendingFileCountErrorsRequested=other._myPendingFileCountErrorsRequested
        
        self.pendingFileCountWarning=other.pendingFileCountWarning
        self._myHasPendingFileCountWarning=other._myHasPendingFileCountWarning
        self._myPendingFileCountWarningRequested=other._myPendingFileCountWarningRequested
        
        self.dirScans=other.dirScans
        self._myHasDirScans=other._myHasDirScans
        self._myDirScansRequested=other._myDirScansRequested
        
        self.fileArchiveDurationWarning=other.fileArchiveDurationWarning
        self._myHasFileArchiveDurationWarning=other._myHasFileArchiveDurationWarning
        self._myFileArchiveDurationWarningRequested=other._myFileArchiveDurationWarningRequested
        
        self.archivedErrors=other.archivedErrors
        self._myHasArchivedErrors=other._myHasArchivedErrors
        self._myArchivedErrorsRequested=other._myArchivedErrorsRequested
        
        self.dirScansErrors=other.dirScansErrors
        self._myHasDirScansErrors=other._myHasDirScansErrors
        self._myDirScansErrorsRequested=other._myDirScansErrorsRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isActiveSecondsRequested():
            self.activeSeconds=other.activeSeconds
            self._myHasActiveSeconds=other._myHasActiveSeconds
            self._myActiveSecondsRequested=other._myActiveSecondsRequested
        
        if self.isArchivedFilesRequested():
            self.archivedFiles=other.archivedFiles
            self._myHasArchivedFiles=other._myHasArchivedFiles
            self._myArchivedFilesRequested=other._myArchivedFilesRequested
        
        if self.isOverallArchiveDurationWarningRequested():
            self.overallArchiveDurationWarning=other.overallArchiveDurationWarning
            self._myHasOverallArchiveDurationWarning=other._myHasOverallArchiveDurationWarning
            self._myOverallArchiveDurationWarningRequested=other._myOverallArchiveDurationWarningRequested
        
        if self.isOnePendingFileRequested():
            self.onePendingFile=other.onePendingFile
            self._myHasOnePendingFile=other._myHasOnePendingFile
            self._myOnePendingFileRequested=other._myOnePendingFileRequested
        
        if self.isFileArchiveDurationErrorsRequested():
            self.fileArchiveDurationErrors=other.fileArchiveDurationErrors
            self._myHasFileArchiveDurationErrors=other._myHasFileArchiveDurationErrors
            self._myFileArchiveDurationErrorsRequested=other._myFileArchiveDurationErrorsRequested
        
        if self.isOverallArchiveDurationErrorsRequested():
            self.overallArchiveDurationErrors=other.overallArchiveDurationErrors
            self._myHasOverallArchiveDurationErrors=other._myHasOverallArchiveDurationErrors
            self._myOverallArchiveDurationErrorsRequested=other._myOverallArchiveDurationErrorsRequested
        
        if self.isPendingFileCountErrorsRequested():
            self.pendingFileCountErrors=other.pendingFileCountErrors
            self._myHasPendingFileCountErrors=other._myHasPendingFileCountErrors
            self._myPendingFileCountErrorsRequested=other._myPendingFileCountErrorsRequested
        
        if self.isPendingFileCountWarningRequested():
            self.pendingFileCountWarning=other.pendingFileCountWarning
            self._myHasPendingFileCountWarning=other._myHasPendingFileCountWarning
            self._myPendingFileCountWarningRequested=other._myPendingFileCountWarningRequested
        
        if self.isDirScansRequested():
            self.dirScans=other.dirScans
            self._myHasDirScans=other._myHasDirScans
            self._myDirScansRequested=other._myDirScansRequested
        
        if self.isFileArchiveDurationWarningRequested():
            self.fileArchiveDurationWarning=other.fileArchiveDurationWarning
            self._myHasFileArchiveDurationWarning=other._myHasFileArchiveDurationWarning
            self._myFileArchiveDurationWarningRequested=other._myFileArchiveDurationWarningRequested
        
        if self.isArchivedErrorsRequested():
            self.archivedErrors=other.archivedErrors
            self._myHasArchivedErrors=other._myHasArchivedErrors
            self._myArchivedErrorsRequested=other._myArchivedErrorsRequested
        
        if self.isDirScansErrorsRequested():
            self.dirScansErrors=other.dirScansErrors
            self._myHasDirScansErrors=other._myHasDirScansErrors
            self._myDirScansErrorsRequested=other._myDirScansErrorsRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasActiveSeconds():
            self.activeSeconds=other.activeSeconds
            self._myHasActiveSeconds=other._myHasActiveSeconds
            self._myActiveSecondsRequested=other._myActiveSecondsRequested
        
        if other.hasArchivedFiles():
            self.archivedFiles=other.archivedFiles
            self._myHasArchivedFiles=other._myHasArchivedFiles
            self._myArchivedFilesRequested=other._myArchivedFilesRequested
        
        if other.hasOverallArchiveDurationWarning():
            self.overallArchiveDurationWarning=other.overallArchiveDurationWarning
            self._myHasOverallArchiveDurationWarning=other._myHasOverallArchiveDurationWarning
            self._myOverallArchiveDurationWarningRequested=other._myOverallArchiveDurationWarningRequested
        
        if other.hasOnePendingFile():
            self.onePendingFile=other.onePendingFile
            self._myHasOnePendingFile=other._myHasOnePendingFile
            self._myOnePendingFileRequested=other._myOnePendingFileRequested
        
        if other.hasFileArchiveDurationErrors():
            self.fileArchiveDurationErrors=other.fileArchiveDurationErrors
            self._myHasFileArchiveDurationErrors=other._myHasFileArchiveDurationErrors
            self._myFileArchiveDurationErrorsRequested=other._myFileArchiveDurationErrorsRequested
        
        if other.hasOverallArchiveDurationErrors():
            self.overallArchiveDurationErrors=other.overallArchiveDurationErrors
            self._myHasOverallArchiveDurationErrors=other._myHasOverallArchiveDurationErrors
            self._myOverallArchiveDurationErrorsRequested=other._myOverallArchiveDurationErrorsRequested
        
        if other.hasPendingFileCountErrors():
            self.pendingFileCountErrors=other.pendingFileCountErrors
            self._myHasPendingFileCountErrors=other._myHasPendingFileCountErrors
            self._myPendingFileCountErrorsRequested=other._myPendingFileCountErrorsRequested
        
        if other.hasPendingFileCountWarning():
            self.pendingFileCountWarning=other.pendingFileCountWarning
            self._myHasPendingFileCountWarning=other._myHasPendingFileCountWarning
            self._myPendingFileCountWarningRequested=other._myPendingFileCountWarningRequested
        
        if other.hasDirScans():
            self.dirScans=other.dirScans
            self._myHasDirScans=other._myHasDirScans
            self._myDirScansRequested=other._myDirScansRequested
        
        if other.hasFileArchiveDurationWarning():
            self.fileArchiveDurationWarning=other.fileArchiveDurationWarning
            self._myHasFileArchiveDurationWarning=other._myHasFileArchiveDurationWarning
            self._myFileArchiveDurationWarningRequested=other._myFileArchiveDurationWarningRequested
        
        if other.hasArchivedErrors():
            self.archivedErrors=other.archivedErrors
            self._myHasArchivedErrors=other._myHasArchivedErrors
            self._myArchivedErrorsRequested=other._myArchivedErrorsRequested
        
        if other.hasDirScansErrors():
            self.dirScansErrors=other.dirScansErrors
            self._myHasDirScansErrors=other._myHasDirScansErrors
            self._myDirScansErrorsRequested=other._myDirScansErrorsRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.activeSeconds=other.activeSeconds
        self._myHasActiveSeconds=other._myHasActiveSeconds
        
        self.archivedFiles=other.archivedFiles
        self._myHasArchivedFiles=other._myHasArchivedFiles
        
        self.overallArchiveDurationWarning=other.overallArchiveDurationWarning
        self._myHasOverallArchiveDurationWarning=other._myHasOverallArchiveDurationWarning
        
        self.onePendingFile=other.onePendingFile
        self._myHasOnePendingFile=other._myHasOnePendingFile
        
        self.fileArchiveDurationErrors=other.fileArchiveDurationErrors
        self._myHasFileArchiveDurationErrors=other._myHasFileArchiveDurationErrors
        
        self.overallArchiveDurationErrors=other.overallArchiveDurationErrors
        self._myHasOverallArchiveDurationErrors=other._myHasOverallArchiveDurationErrors
        
        self.pendingFileCountErrors=other.pendingFileCountErrors
        self._myHasPendingFileCountErrors=other._myHasPendingFileCountErrors
        
        self.pendingFileCountWarning=other.pendingFileCountWarning
        self._myHasPendingFileCountWarning=other._myHasPendingFileCountWarning
        
        self.dirScans=other.dirScans
        self._myHasDirScans=other._myHasDirScans
        
        self.fileArchiveDurationWarning=other.fileArchiveDurationWarning
        self._myHasFileArchiveDurationWarning=other._myHasFileArchiveDurationWarning
        
        self.archivedErrors=other.archivedErrors
        self._myHasArchivedErrors=other._myHasArchivedErrors
        
        self.dirScansErrors=other.dirScansErrors
        self._myHasDirScansErrors=other._myHasDirScansErrors
        


    def setAllNumericToZero (self):
        
        self.activeSeconds=0
        self.setHasActiveSeconds()
        self.archivedFiles=0
        self.setHasArchivedFiles()
        self.overallArchiveDurationWarning=0
        self.setHasOverallArchiveDurationWarning()
        self.onePendingFile=0
        self.setHasOnePendingFile()
        self.fileArchiveDurationErrors=0
        self.setHasFileArchiveDurationErrors()
        self.overallArchiveDurationErrors=0
        self.setHasOverallArchiveDurationErrors()
        self.pendingFileCountErrors=0
        self.setHasPendingFileCountErrors()
        self.pendingFileCountWarning=0
        self.setHasPendingFileCountWarning()
        self.dirScans=0
        self.setHasDirScans()
        self.fileArchiveDurationWarning=0
        self.setHasFileArchiveDurationWarning()
        self.archivedErrors=0
        self.setHasArchivedErrors()
        self.dirScansErrors=0
        self.setHasDirScansErrors()
        
        pass

    def subtractAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasActiveSeconds():
            if other.hasActiveSeconds():
                self.activeSeconds -= other.activeSeconds
        
        if self.hasArchivedFiles():
            if other.hasArchivedFiles():
                self.archivedFiles -= other.archivedFiles
        
        if self.hasOverallArchiveDurationWarning():
            if other.hasOverallArchiveDurationWarning():
                self.overallArchiveDurationWarning -= other.overallArchiveDurationWarning
        
        if self.hasOnePendingFile():
            if other.hasOnePendingFile():
                self.onePendingFile -= other.onePendingFile
        
        if self.hasFileArchiveDurationErrors():
            if other.hasFileArchiveDurationErrors():
                self.fileArchiveDurationErrors -= other.fileArchiveDurationErrors
        
        if self.hasOverallArchiveDurationErrors():
            if other.hasOverallArchiveDurationErrors():
                self.overallArchiveDurationErrors -= other.overallArchiveDurationErrors
        
        if self.hasPendingFileCountErrors():
            if other.hasPendingFileCountErrors():
                self.pendingFileCountErrors -= other.pendingFileCountErrors
        
        if self.hasPendingFileCountWarning():
            if other.hasPendingFileCountWarning():
                self.pendingFileCountWarning -= other.pendingFileCountWarning
        
        if self.hasDirScans():
            if other.hasDirScans():
                self.dirScans -= other.dirScans
        
        if self.hasFileArchiveDurationWarning():
            if other.hasFileArchiveDurationWarning():
                self.fileArchiveDurationWarning -= other.fileArchiveDurationWarning
        
        if self.hasArchivedErrors():
            if other.hasArchivedErrors():
                self.archivedErrors -= other.archivedErrors
        
        if self.hasDirScansErrors():
            if other.hasDirScansErrors():
                self.dirScansErrors -= other.dirScansErrors
        
        
        pass


    def addAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasActiveSeconds():
            if other.hasActiveSeconds():
                self.activeSeconds += other.activeSeconds
        
        if self.hasArchivedFiles():
            if other.hasArchivedFiles():
                self.archivedFiles += other.archivedFiles
        
        if self.hasOverallArchiveDurationWarning():
            if other.hasOverallArchiveDurationWarning():
                self.overallArchiveDurationWarning += other.overallArchiveDurationWarning
        
        if self.hasOnePendingFile():
            if other.hasOnePendingFile():
                self.onePendingFile += other.onePendingFile
        
        if self.hasFileArchiveDurationErrors():
            if other.hasFileArchiveDurationErrors():
                self.fileArchiveDurationErrors += other.fileArchiveDurationErrors
        
        if self.hasOverallArchiveDurationErrors():
            if other.hasOverallArchiveDurationErrors():
                self.overallArchiveDurationErrors += other.overallArchiveDurationErrors
        
        if self.hasPendingFileCountErrors():
            if other.hasPendingFileCountErrors():
                self.pendingFileCountErrors += other.pendingFileCountErrors
        
        if self.hasPendingFileCountWarning():
            if other.hasPendingFileCountWarning():
                self.pendingFileCountWarning += other.pendingFileCountWarning
        
        if self.hasDirScans():
            if other.hasDirScans():
                self.dirScans += other.dirScans
        
        if self.hasFileArchiveDurationWarning():
            if other.hasFileArchiveDurationWarning():
                self.fileArchiveDurationWarning += other.fileArchiveDurationWarning
        
        if self.hasArchivedErrors():
            if other.hasArchivedErrors():
                self.archivedErrors += other.archivedErrors
        
        if self.hasDirScansErrors():
            if other.hasDirScansErrors():
                self.dirScansErrors += other.dirScansErrors
        
        
        pass


    # has...() methods

    def hasActiveSeconds (self):
        return self._myHasActiveSeconds

    def hasArchivedFiles (self):
        return self._myHasArchivedFiles

    def hasOverallArchiveDurationWarning (self):
        return self._myHasOverallArchiveDurationWarning

    def hasOnePendingFile (self):
        return self._myHasOnePendingFile

    def hasFileArchiveDurationErrors (self):
        return self._myHasFileArchiveDurationErrors

    def hasOverallArchiveDurationErrors (self):
        return self._myHasOverallArchiveDurationErrors

    def hasPendingFileCountErrors (self):
        return self._myHasPendingFileCountErrors

    def hasPendingFileCountWarning (self):
        return self._myHasPendingFileCountWarning

    def hasDirScans (self):
        return self._myHasDirScans

    def hasFileArchiveDurationWarning (self):
        return self._myHasFileArchiveDurationWarning

    def hasArchivedErrors (self):
        return self._myHasArchivedErrors

    def hasDirScansErrors (self):
        return self._myHasDirScansErrors




    # setHas...() methods

    def setHasActiveSeconds (self):
        self._myHasActiveSeconds=True

    def setHasArchivedFiles (self):
        self._myHasArchivedFiles=True

    def setHasOverallArchiveDurationWarning (self):
        self._myHasOverallArchiveDurationWarning=True

    def setHasOnePendingFile (self):
        self._myHasOnePendingFile=True

    def setHasFileArchiveDurationErrors (self):
        self._myHasFileArchiveDurationErrors=True

    def setHasOverallArchiveDurationErrors (self):
        self._myHasOverallArchiveDurationErrors=True

    def setHasPendingFileCountErrors (self):
        self._myHasPendingFileCountErrors=True

    def setHasPendingFileCountWarning (self):
        self._myHasPendingFileCountWarning=True

    def setHasDirScans (self):
        self._myHasDirScans=True

    def setHasFileArchiveDurationWarning (self):
        self._myHasFileArchiveDurationWarning=True

    def setHasArchivedErrors (self):
        self._myHasArchivedErrors=True

    def setHasDirScansErrors (self):
        self._myHasDirScansErrors=True




    # isRequested...() methods

    def isActiveSecondsRequested (self):
        return self._myActiveSecondsRequested

    def isArchivedFilesRequested (self):
        return self._myArchivedFilesRequested

    def isOverallArchiveDurationWarningRequested (self):
        return self._myOverallArchiveDurationWarningRequested

    def isOnePendingFileRequested (self):
        return self._myOnePendingFileRequested

    def isFileArchiveDurationErrorsRequested (self):
        return self._myFileArchiveDurationErrorsRequested

    def isOverallArchiveDurationErrorsRequested (self):
        return self._myOverallArchiveDurationErrorsRequested

    def isPendingFileCountErrorsRequested (self):
        return self._myPendingFileCountErrorsRequested

    def isPendingFileCountWarningRequested (self):
        return self._myPendingFileCountWarningRequested

    def isDirScansRequested (self):
        return self._myDirScansRequested

    def isFileArchiveDurationWarningRequested (self):
        return self._myFileArchiveDurationWarningRequested

    def isArchivedErrorsRequested (self):
        return self._myArchivedErrorsRequested

    def isDirScansErrorsRequested (self):
        return self._myDirScansErrorsRequested




    # setRequested...() methods

    def setActiveSecondsRequested (self):
        self._myActiveSecondsRequested=True

    def setArchivedFilesRequested (self):
        self._myArchivedFilesRequested=True

    def setOverallArchiveDurationWarningRequested (self):
        self._myOverallArchiveDurationWarningRequested=True

    def setOnePendingFileRequested (self):
        self._myOnePendingFileRequested=True

    def setFileArchiveDurationErrorsRequested (self):
        self._myFileArchiveDurationErrorsRequested=True

    def setOverallArchiveDurationErrorsRequested (self):
        self._myOverallArchiveDurationErrorsRequested=True

    def setPendingFileCountErrorsRequested (self):
        self._myPendingFileCountErrorsRequested=True

    def setPendingFileCountWarningRequested (self):
        self._myPendingFileCountWarningRequested=True

    def setDirScansRequested (self):
        self._myDirScansRequested=True

    def setFileArchiveDurationWarningRequested (self):
        self._myFileArchiveDurationWarningRequested=True

    def setArchivedErrorsRequested (self):
        self._myArchivedErrorsRequested=True

    def setDirScansErrorsRequested (self):
        self._myDirScansErrorsRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myActiveSecondsRequested:
            x = "+ActiveSeconds="
            if self._myHasActiveSeconds:
                leafStr = str(self.activeSeconds)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myArchivedFilesRequested:
            x = "+ArchivedFiles="
            if self._myHasArchivedFiles:
                leafStr = str(self.archivedFiles)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myOverallArchiveDurationWarningRequested:
            x = "+OverallArchiveDurationWarning="
            if self._myHasOverallArchiveDurationWarning:
                leafStr = str(self.overallArchiveDurationWarning)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myOnePendingFileRequested:
            x = "+OnePendingFile="
            if self._myHasOnePendingFile:
                leafStr = str(self.onePendingFile)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myFileArchiveDurationErrorsRequested:
            x = "+FileArchiveDurationErrors="
            if self._myHasFileArchiveDurationErrors:
                leafStr = str(self.fileArchiveDurationErrors)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myOverallArchiveDurationErrorsRequested:
            x = "+OverallArchiveDurationErrors="
            if self._myHasOverallArchiveDurationErrors:
                leafStr = str(self.overallArchiveDurationErrors)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myPendingFileCountErrorsRequested:
            x = "+PendingFileCountErrors="
            if self._myHasPendingFileCountErrors:
                leafStr = str(self.pendingFileCountErrors)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myPendingFileCountWarningRequested:
            x = "+PendingFileCountWarning="
            if self._myHasPendingFileCountWarning:
                leafStr = str(self.pendingFileCountWarning)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myDirScansRequested:
            x = "+DirScans="
            if self._myHasDirScans:
                leafStr = str(self.dirScans)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myFileArchiveDurationWarningRequested:
            x = "+FileArchiveDurationWarning="
            if self._myHasFileArchiveDurationWarning:
                leafStr = str(self.fileArchiveDurationWarning)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myArchivedErrorsRequested:
            x = "+ArchivedErrors="
            if self._myHasArchivedErrors:
                leafStr = str(self.archivedErrors)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myDirScansErrorsRequested:
            x = "+DirScansErrors="
            if self._myHasDirScansErrors:
                leafStr = str(self.dirScansErrors)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{CountersOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+ActiveSeconds="
        if self._myHasActiveSeconds:
            leafStr = str(self.activeSeconds)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myActiveSecondsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+ArchivedFiles="
        if self._myHasArchivedFiles:
            leafStr = str(self.archivedFiles)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myArchivedFilesRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+OverallArchiveDurationWarning="
        if self._myHasOverallArchiveDurationWarning:
            leafStr = str(self.overallArchiveDurationWarning)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myOverallArchiveDurationWarningRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+OnePendingFile="
        if self._myHasOnePendingFile:
            leafStr = str(self.onePendingFile)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myOnePendingFileRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+FileArchiveDurationErrors="
        if self._myHasFileArchiveDurationErrors:
            leafStr = str(self.fileArchiveDurationErrors)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myFileArchiveDurationErrorsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+OverallArchiveDurationErrors="
        if self._myHasOverallArchiveDurationErrors:
            leafStr = str(self.overallArchiveDurationErrors)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myOverallArchiveDurationErrorsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+PendingFileCountErrors="
        if self._myHasPendingFileCountErrors:
            leafStr = str(self.pendingFileCountErrors)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myPendingFileCountErrorsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+PendingFileCountWarning="
        if self._myHasPendingFileCountWarning:
            leafStr = str(self.pendingFileCountWarning)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myPendingFileCountWarningRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+DirScans="
        if self._myHasDirScans:
            leafStr = str(self.dirScans)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myDirScansRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+FileArchiveDurationWarning="
        if self._myHasFileArchiveDurationWarning:
            leafStr = str(self.fileArchiveDurationWarning)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myFileArchiveDurationWarningRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+ArchivedErrors="
        if self._myHasArchivedErrors:
            leafStr = str(self.archivedErrors)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myArchivedErrorsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+DirScansErrors="
        if self._myHasDirScansErrors:
            leafStr = str(self.dirScansErrors)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myDirScansErrorsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{CountersOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setActiveSecondsRequested()
        self.setArchivedFilesRequested()
        self.setOverallArchiveDurationWarningRequested()
        self.setOnePendingFileRequested()
        self.setFileArchiveDurationErrorsRequested()
        self.setOverallArchiveDurationErrorsRequested()
        self.setPendingFileCountErrorsRequested()
        self.setPendingFileCountWarningRequested()
        self.setDirScansRequested()
        self.setFileArchiveDurationWarningRequested()
        self.setArchivedErrorsRequested()
        self.setDirScansErrorsRequested()
        
        


    def setActiveSeconds (self, activeSeconds):
        self.activeSeconds = activeSeconds
        self.setHasActiveSeconds()

    def setArchivedFiles (self, archivedFiles):
        self.archivedFiles = archivedFiles
        self.setHasArchivedFiles()

    def setOverallArchiveDurationWarning (self, overallArchiveDurationWarning):
        self.overallArchiveDurationWarning = overallArchiveDurationWarning
        self.setHasOverallArchiveDurationWarning()

    def setOnePendingFile (self, onePendingFile):
        self.onePendingFile = onePendingFile
        self.setHasOnePendingFile()

    def setFileArchiveDurationErrors (self, fileArchiveDurationErrors):
        self.fileArchiveDurationErrors = fileArchiveDurationErrors
        self.setHasFileArchiveDurationErrors()

    def setOverallArchiveDurationErrors (self, overallArchiveDurationErrors):
        self.overallArchiveDurationErrors = overallArchiveDurationErrors
        self.setHasOverallArchiveDurationErrors()

    def setPendingFileCountErrors (self, pendingFileCountErrors):
        self.pendingFileCountErrors = pendingFileCountErrors
        self.setHasPendingFileCountErrors()

    def setPendingFileCountWarning (self, pendingFileCountWarning):
        self.pendingFileCountWarning = pendingFileCountWarning
        self.setHasPendingFileCountWarning()

    def setDirScans (self, dirScans):
        self.dirScans = dirScans
        self.setHasDirScans()

    def setFileArchiveDurationWarning (self, fileArchiveDurationWarning):
        self.fileArchiveDurationWarning = fileArchiveDurationWarning
        self.setHasFileArchiveDurationWarning()

    def setArchivedErrors (self, archivedErrors):
        self.archivedErrors = archivedErrors
        self.setHasArchivedErrors()

    def setDirScansErrors (self, dirScansErrors):
        self.dirScansErrors = dirScansErrors
        self.setHasDirScansErrors()


"""
Extracted from the below data: 
{
    "node": {
        "className": "CountersOperData", 
        "namespace": "counters", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_log.tech.log.housekeeper.log_archiving.counters.counters_oper_data_gen import CountersOperData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "log", 
            "isCurrent": false
        }, 
        {
            "namespace": "housekeeper", 
            "isCurrent": false
        }, 
        {
            "namespace": "log_archiving", 
            "isCurrent": false
        }, 
        {
            "namespace": "counters", 
            "isCurrent": true
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "activeSeconds", 
            "yangName": "active-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "archivedFiles", 
            "yangName": "archived-files", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallArchiveDurationWarning", 
            "yangName": "overall-archive-duration-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "onePendingFile", 
            "yangName": "one-pending-file", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "fileArchiveDurationErrors", 
            "yangName": "file-archive-duration-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallArchiveDurationErrors", 
            "yangName": "overall-archive-duration-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "pendingFileCountErrors", 
            "yangName": "pending-file-count-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "pendingFileCountWarning", 
            "yangName": "pending-file-count-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "dirScans", 
            "yangName": "dir-scans", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "fileArchiveDurationWarning", 
            "yangName": "file-archive-duration-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "archivedErrors", 
            "yangName": "archived-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "dirScansErrors", 
            "yangName": "dir-scans-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "module": {}, 
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "debug", 
            "qwilt_tech_log"
        ]
    }, 
    "createTime": "2013"
}
"""


