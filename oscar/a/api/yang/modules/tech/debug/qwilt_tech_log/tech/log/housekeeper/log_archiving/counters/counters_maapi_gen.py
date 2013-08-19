


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes
from a.infra.misc.init_guard import InitGuard

from a.sys.confd.pyconfdlib.tag_values import TagValues
from a.sys.confd.pyconfdlib.value import Value
from a.sys.confd.pyconfdlib.key_path import KeyPath

from counters_maapi_base_gen import CountersMaapiBase




class BlinkyCountersMaapi(CountersMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-counters")
        self.domain = None

        

        
        self.activeSecondsRequested = False
        self.activeSeconds = None
        self.activeSecondsSet = False
        
        self.archivedFilesRequested = False
        self.archivedFiles = None
        self.archivedFilesSet = False
        
        self.overallArchiveDurationWarningRequested = False
        self.overallArchiveDurationWarning = None
        self.overallArchiveDurationWarningSet = False
        
        self.onePendingFileRequested = False
        self.onePendingFile = None
        self.onePendingFileSet = False
        
        self.fileArchiveDurationErrorsRequested = False
        self.fileArchiveDurationErrors = None
        self.fileArchiveDurationErrorsSet = False
        
        self.overallArchiveDurationErrorsRequested = False
        self.overallArchiveDurationErrors = None
        self.overallArchiveDurationErrorsSet = False
        
        self.pendingFileCountErrorsRequested = False
        self.pendingFileCountErrors = None
        self.pendingFileCountErrorsSet = False
        
        self.pendingFileCountWarningRequested = False
        self.pendingFileCountWarning = None
        self.pendingFileCountWarningSet = False
        
        self.dirScansRequested = False
        self.dirScans = None
        self.dirScansSet = False
        
        self.fileArchiveDurationWarningRequested = False
        self.fileArchiveDurationWarning = None
        self.fileArchiveDurationWarningSet = False
        
        self.archivedErrorsRequested = False
        self.archivedErrors = None
        self.archivedErrorsSet = False
        
        self.dirScansErrorsRequested = False
        self.dirScansErrors = None
        self.dirScansErrorsSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestActiveSeconds(True)
        
        self.requestArchivedFiles(True)
        
        self.requestOverallArchiveDurationWarning(True)
        
        self.requestOnePendingFile(True)
        
        self.requestFileArchiveDurationErrors(True)
        
        self.requestOverallArchiveDurationErrors(True)
        
        self.requestPendingFileCountErrors(True)
        
        self.requestPendingFileCountWarning(True)
        
        self.requestDirScans(True)
        
        self.requestFileArchiveDurationWarning(True)
        
        self.requestArchivedErrors(True)
        
        self.requestDirScansErrors(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestActiveSeconds(False)
        
        self.requestArchivedFiles(False)
        
        self.requestOverallArchiveDurationWarning(False)
        
        self.requestOnePendingFile(False)
        
        self.requestFileArchiveDurationErrors(False)
        
        self.requestOverallArchiveDurationErrors(False)
        
        self.requestPendingFileCountErrors(False)
        
        self.requestPendingFileCountWarning(False)
        
        self.requestDirScans(False)
        
        self.requestFileArchiveDurationWarning(False)
        
        self.requestArchivedErrors(False)
        
        self.requestDirScansErrors(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestActiveSeconds(True)
        
        self.requestArchivedFiles(True)
        
        self.requestOverallArchiveDurationWarning(True)
        
        self.requestOnePendingFile(True)
        
        self.requestFileArchiveDurationErrors(True)
        
        self.requestOverallArchiveDurationErrors(True)
        
        self.requestPendingFileCountErrors(True)
        
        self.requestPendingFileCountWarning(True)
        
        self.requestDirScans(True)
        
        self.requestFileArchiveDurationWarning(True)
        
        self.requestArchivedErrors(True)
        
        self.requestDirScansErrors(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestActiveSeconds(False)
        
        self.requestArchivedFiles(False)
        
        self.requestOverallArchiveDurationWarning(False)
        
        self.requestOnePendingFile(False)
        
        self.requestFileArchiveDurationErrors(False)
        
        self.requestOverallArchiveDurationErrors(False)
        
        self.requestPendingFileCountErrors(False)
        
        self.requestPendingFileCountWarning(False)
        
        self.requestDirScans(False)
        
        self.requestFileArchiveDurationWarning(False)
        
        self.requestArchivedErrors(False)
        
        self.requestDirScansErrors(False)
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        

    def write (self
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(trxContext)

    def read (self
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(
                                  True,
                                  trxContext)



    def requestActiveSeconds (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-activeseconds').debug3Func(): logFunc('called. requested=%s', requested)
        self.activeSecondsRequested = requested
        self.activeSecondsSet = False

    def isActiveSecondsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-activeseconds-requested').debug3Func(): logFunc('called. requested=%s', self.activeSecondsRequested)
        return self.activeSecondsRequested

    def getActiveSeconds (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-activeseconds').debug3Func(): logFunc('called. self.activeSecondsSet=%s, self.activeSeconds=%s', self.activeSecondsSet, self.activeSeconds)
        if self.activeSecondsSet:
            return self.activeSeconds
        return None

    def hasActiveSeconds (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-activeseconds').debug3Func(): logFunc('called. self.activeSecondsSet=%s, self.activeSeconds=%s', self.activeSecondsSet, self.activeSeconds)
        if self.activeSecondsSet:
            return True
        return False

    def setActiveSeconds (self, activeSeconds):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-activeseconds').debug3Func(): logFunc('called. activeSeconds=%s, old=%s', activeSeconds, self.activeSeconds)
        self.activeSecondsSet = True
        self.activeSeconds = activeSeconds

    def requestArchivedFiles (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-archivedfiles').debug3Func(): logFunc('called. requested=%s', requested)
        self.archivedFilesRequested = requested
        self.archivedFilesSet = False

    def isArchivedFilesRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-archivedfiles-requested').debug3Func(): logFunc('called. requested=%s', self.archivedFilesRequested)
        return self.archivedFilesRequested

    def getArchivedFiles (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-archivedfiles').debug3Func(): logFunc('called. self.archivedFilesSet=%s, self.archivedFiles=%s', self.archivedFilesSet, self.archivedFiles)
        if self.archivedFilesSet:
            return self.archivedFiles
        return None

    def hasArchivedFiles (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-archivedfiles').debug3Func(): logFunc('called. self.archivedFilesSet=%s, self.archivedFiles=%s', self.archivedFilesSet, self.archivedFiles)
        if self.archivedFilesSet:
            return True
        return False

    def setArchivedFiles (self, archivedFiles):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-archivedfiles').debug3Func(): logFunc('called. archivedFiles=%s, old=%s', archivedFiles, self.archivedFiles)
        self.archivedFilesSet = True
        self.archivedFiles = archivedFiles

    def requestOverallArchiveDurationWarning (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-overallarchivedurationwarning').debug3Func(): logFunc('called. requested=%s', requested)
        self.overallArchiveDurationWarningRequested = requested
        self.overallArchiveDurationWarningSet = False

    def isOverallArchiveDurationWarningRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-overallarchivedurationwarning-requested').debug3Func(): logFunc('called. requested=%s', self.overallArchiveDurationWarningRequested)
        return self.overallArchiveDurationWarningRequested

    def getOverallArchiveDurationWarning (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-overallarchivedurationwarning').debug3Func(): logFunc('called. self.overallArchiveDurationWarningSet=%s, self.overallArchiveDurationWarning=%s', self.overallArchiveDurationWarningSet, self.overallArchiveDurationWarning)
        if self.overallArchiveDurationWarningSet:
            return self.overallArchiveDurationWarning
        return None

    def hasOverallArchiveDurationWarning (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-overallarchivedurationwarning').debug3Func(): logFunc('called. self.overallArchiveDurationWarningSet=%s, self.overallArchiveDurationWarning=%s', self.overallArchiveDurationWarningSet, self.overallArchiveDurationWarning)
        if self.overallArchiveDurationWarningSet:
            return True
        return False

    def setOverallArchiveDurationWarning (self, overallArchiveDurationWarning):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-overallarchivedurationwarning').debug3Func(): logFunc('called. overallArchiveDurationWarning=%s, old=%s', overallArchiveDurationWarning, self.overallArchiveDurationWarning)
        self.overallArchiveDurationWarningSet = True
        self.overallArchiveDurationWarning = overallArchiveDurationWarning

    def requestOnePendingFile (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-onependingfile').debug3Func(): logFunc('called. requested=%s', requested)
        self.onePendingFileRequested = requested
        self.onePendingFileSet = False

    def isOnePendingFileRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-onependingfile-requested').debug3Func(): logFunc('called. requested=%s', self.onePendingFileRequested)
        return self.onePendingFileRequested

    def getOnePendingFile (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-onependingfile').debug3Func(): logFunc('called. self.onePendingFileSet=%s, self.onePendingFile=%s', self.onePendingFileSet, self.onePendingFile)
        if self.onePendingFileSet:
            return self.onePendingFile
        return None

    def hasOnePendingFile (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-onependingfile').debug3Func(): logFunc('called. self.onePendingFileSet=%s, self.onePendingFile=%s', self.onePendingFileSet, self.onePendingFile)
        if self.onePendingFileSet:
            return True
        return False

    def setOnePendingFile (self, onePendingFile):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-onependingfile').debug3Func(): logFunc('called. onePendingFile=%s, old=%s', onePendingFile, self.onePendingFile)
        self.onePendingFileSet = True
        self.onePendingFile = onePendingFile

    def requestFileArchiveDurationErrors (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-filearchivedurationerrors').debug3Func(): logFunc('called. requested=%s', requested)
        self.fileArchiveDurationErrorsRequested = requested
        self.fileArchiveDurationErrorsSet = False

    def isFileArchiveDurationErrorsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-filearchivedurationerrors-requested').debug3Func(): logFunc('called. requested=%s', self.fileArchiveDurationErrorsRequested)
        return self.fileArchiveDurationErrorsRequested

    def getFileArchiveDurationErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-filearchivedurationerrors').debug3Func(): logFunc('called. self.fileArchiveDurationErrorsSet=%s, self.fileArchiveDurationErrors=%s', self.fileArchiveDurationErrorsSet, self.fileArchiveDurationErrors)
        if self.fileArchiveDurationErrorsSet:
            return self.fileArchiveDurationErrors
        return None

    def hasFileArchiveDurationErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-filearchivedurationerrors').debug3Func(): logFunc('called. self.fileArchiveDurationErrorsSet=%s, self.fileArchiveDurationErrors=%s', self.fileArchiveDurationErrorsSet, self.fileArchiveDurationErrors)
        if self.fileArchiveDurationErrorsSet:
            return True
        return False

    def setFileArchiveDurationErrors (self, fileArchiveDurationErrors):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-filearchivedurationerrors').debug3Func(): logFunc('called. fileArchiveDurationErrors=%s, old=%s', fileArchiveDurationErrors, self.fileArchiveDurationErrors)
        self.fileArchiveDurationErrorsSet = True
        self.fileArchiveDurationErrors = fileArchiveDurationErrors

    def requestOverallArchiveDurationErrors (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-overallarchivedurationerrors').debug3Func(): logFunc('called. requested=%s', requested)
        self.overallArchiveDurationErrorsRequested = requested
        self.overallArchiveDurationErrorsSet = False

    def isOverallArchiveDurationErrorsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-overallarchivedurationerrors-requested').debug3Func(): logFunc('called. requested=%s', self.overallArchiveDurationErrorsRequested)
        return self.overallArchiveDurationErrorsRequested

    def getOverallArchiveDurationErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-overallarchivedurationerrors').debug3Func(): logFunc('called. self.overallArchiveDurationErrorsSet=%s, self.overallArchiveDurationErrors=%s', self.overallArchiveDurationErrorsSet, self.overallArchiveDurationErrors)
        if self.overallArchiveDurationErrorsSet:
            return self.overallArchiveDurationErrors
        return None

    def hasOverallArchiveDurationErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-overallarchivedurationerrors').debug3Func(): logFunc('called. self.overallArchiveDurationErrorsSet=%s, self.overallArchiveDurationErrors=%s', self.overallArchiveDurationErrorsSet, self.overallArchiveDurationErrors)
        if self.overallArchiveDurationErrorsSet:
            return True
        return False

    def setOverallArchiveDurationErrors (self, overallArchiveDurationErrors):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-overallarchivedurationerrors').debug3Func(): logFunc('called. overallArchiveDurationErrors=%s, old=%s', overallArchiveDurationErrors, self.overallArchiveDurationErrors)
        self.overallArchiveDurationErrorsSet = True
        self.overallArchiveDurationErrors = overallArchiveDurationErrors

    def requestPendingFileCountErrors (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-pendingfilecounterrors').debug3Func(): logFunc('called. requested=%s', requested)
        self.pendingFileCountErrorsRequested = requested
        self.pendingFileCountErrorsSet = False

    def isPendingFileCountErrorsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-pendingfilecounterrors-requested').debug3Func(): logFunc('called. requested=%s', self.pendingFileCountErrorsRequested)
        return self.pendingFileCountErrorsRequested

    def getPendingFileCountErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-pendingfilecounterrors').debug3Func(): logFunc('called. self.pendingFileCountErrorsSet=%s, self.pendingFileCountErrors=%s', self.pendingFileCountErrorsSet, self.pendingFileCountErrors)
        if self.pendingFileCountErrorsSet:
            return self.pendingFileCountErrors
        return None

    def hasPendingFileCountErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-pendingfilecounterrors').debug3Func(): logFunc('called. self.pendingFileCountErrorsSet=%s, self.pendingFileCountErrors=%s', self.pendingFileCountErrorsSet, self.pendingFileCountErrors)
        if self.pendingFileCountErrorsSet:
            return True
        return False

    def setPendingFileCountErrors (self, pendingFileCountErrors):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-pendingfilecounterrors').debug3Func(): logFunc('called. pendingFileCountErrors=%s, old=%s', pendingFileCountErrors, self.pendingFileCountErrors)
        self.pendingFileCountErrorsSet = True
        self.pendingFileCountErrors = pendingFileCountErrors

    def requestPendingFileCountWarning (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-pendingfilecountwarning').debug3Func(): logFunc('called. requested=%s', requested)
        self.pendingFileCountWarningRequested = requested
        self.pendingFileCountWarningSet = False

    def isPendingFileCountWarningRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-pendingfilecountwarning-requested').debug3Func(): logFunc('called. requested=%s', self.pendingFileCountWarningRequested)
        return self.pendingFileCountWarningRequested

    def getPendingFileCountWarning (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-pendingfilecountwarning').debug3Func(): logFunc('called. self.pendingFileCountWarningSet=%s, self.pendingFileCountWarning=%s', self.pendingFileCountWarningSet, self.pendingFileCountWarning)
        if self.pendingFileCountWarningSet:
            return self.pendingFileCountWarning
        return None

    def hasPendingFileCountWarning (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-pendingfilecountwarning').debug3Func(): logFunc('called. self.pendingFileCountWarningSet=%s, self.pendingFileCountWarning=%s', self.pendingFileCountWarningSet, self.pendingFileCountWarning)
        if self.pendingFileCountWarningSet:
            return True
        return False

    def setPendingFileCountWarning (self, pendingFileCountWarning):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-pendingfilecountwarning').debug3Func(): logFunc('called. pendingFileCountWarning=%s, old=%s', pendingFileCountWarning, self.pendingFileCountWarning)
        self.pendingFileCountWarningSet = True
        self.pendingFileCountWarning = pendingFileCountWarning

    def requestDirScans (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-dirscans').debug3Func(): logFunc('called. requested=%s', requested)
        self.dirScansRequested = requested
        self.dirScansSet = False

    def isDirScansRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-dirscans-requested').debug3Func(): logFunc('called. requested=%s', self.dirScansRequested)
        return self.dirScansRequested

    def getDirScans (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-dirscans').debug3Func(): logFunc('called. self.dirScansSet=%s, self.dirScans=%s', self.dirScansSet, self.dirScans)
        if self.dirScansSet:
            return self.dirScans
        return None

    def hasDirScans (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-dirscans').debug3Func(): logFunc('called. self.dirScansSet=%s, self.dirScans=%s', self.dirScansSet, self.dirScans)
        if self.dirScansSet:
            return True
        return False

    def setDirScans (self, dirScans):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-dirscans').debug3Func(): logFunc('called. dirScans=%s, old=%s', dirScans, self.dirScans)
        self.dirScansSet = True
        self.dirScans = dirScans

    def requestFileArchiveDurationWarning (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-filearchivedurationwarning').debug3Func(): logFunc('called. requested=%s', requested)
        self.fileArchiveDurationWarningRequested = requested
        self.fileArchiveDurationWarningSet = False

    def isFileArchiveDurationWarningRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-filearchivedurationwarning-requested').debug3Func(): logFunc('called. requested=%s', self.fileArchiveDurationWarningRequested)
        return self.fileArchiveDurationWarningRequested

    def getFileArchiveDurationWarning (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-filearchivedurationwarning').debug3Func(): logFunc('called. self.fileArchiveDurationWarningSet=%s, self.fileArchiveDurationWarning=%s', self.fileArchiveDurationWarningSet, self.fileArchiveDurationWarning)
        if self.fileArchiveDurationWarningSet:
            return self.fileArchiveDurationWarning
        return None

    def hasFileArchiveDurationWarning (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-filearchivedurationwarning').debug3Func(): logFunc('called. self.fileArchiveDurationWarningSet=%s, self.fileArchiveDurationWarning=%s', self.fileArchiveDurationWarningSet, self.fileArchiveDurationWarning)
        if self.fileArchiveDurationWarningSet:
            return True
        return False

    def setFileArchiveDurationWarning (self, fileArchiveDurationWarning):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-filearchivedurationwarning').debug3Func(): logFunc('called. fileArchiveDurationWarning=%s, old=%s', fileArchiveDurationWarning, self.fileArchiveDurationWarning)
        self.fileArchiveDurationWarningSet = True
        self.fileArchiveDurationWarning = fileArchiveDurationWarning

    def requestArchivedErrors (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-archivederrors').debug3Func(): logFunc('called. requested=%s', requested)
        self.archivedErrorsRequested = requested
        self.archivedErrorsSet = False

    def isArchivedErrorsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-archivederrors-requested').debug3Func(): logFunc('called. requested=%s', self.archivedErrorsRequested)
        return self.archivedErrorsRequested

    def getArchivedErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-archivederrors').debug3Func(): logFunc('called. self.archivedErrorsSet=%s, self.archivedErrors=%s', self.archivedErrorsSet, self.archivedErrors)
        if self.archivedErrorsSet:
            return self.archivedErrors
        return None

    def hasArchivedErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-archivederrors').debug3Func(): logFunc('called. self.archivedErrorsSet=%s, self.archivedErrors=%s', self.archivedErrorsSet, self.archivedErrors)
        if self.archivedErrorsSet:
            return True
        return False

    def setArchivedErrors (self, archivedErrors):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-archivederrors').debug3Func(): logFunc('called. archivedErrors=%s, old=%s', archivedErrors, self.archivedErrors)
        self.archivedErrorsSet = True
        self.archivedErrors = archivedErrors

    def requestDirScansErrors (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-dirscanserrors').debug3Func(): logFunc('called. requested=%s', requested)
        self.dirScansErrorsRequested = requested
        self.dirScansErrorsSet = False

    def isDirScansErrorsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-dirscanserrors-requested').debug3Func(): logFunc('called. requested=%s', self.dirScansErrorsRequested)
        return self.dirScansErrorsRequested

    def getDirScansErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-dirscanserrors').debug3Func(): logFunc('called. self.dirScansErrorsSet=%s, self.dirScansErrors=%s', self.dirScansErrorsSet, self.dirScansErrors)
        if self.dirScansErrorsSet:
            return self.dirScansErrors
        return None

    def hasDirScansErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-dirscanserrors').debug3Func(): logFunc('called. self.dirScansErrorsSet=%s, self.dirScansErrors=%s', self.dirScansErrorsSet, self.dirScansErrors)
        if self.dirScansErrorsSet:
            return True
        return False

    def setDirScansErrors (self, dirScansErrors):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-dirscanserrors').debug3Func(): logFunc('called. dirScansErrors=%s, old=%s', dirScansErrors, self.dirScansErrors)
        self.dirScansErrorsSet = True
        self.dirScansErrors = dirScansErrors


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.activeSeconds = 0
        self.activeSecondsSet = False
        
        self.archivedFiles = 0
        self.archivedFilesSet = False
        
        self.overallArchiveDurationWarning = 0
        self.overallArchiveDurationWarningSet = False
        
        self.onePendingFile = 0
        self.onePendingFileSet = False
        
        self.fileArchiveDurationErrors = 0
        self.fileArchiveDurationErrorsSet = False
        
        self.overallArchiveDurationErrors = 0
        self.overallArchiveDurationErrorsSet = False
        
        self.pendingFileCountErrors = 0
        self.pendingFileCountErrorsSet = False
        
        self.pendingFileCountWarning = 0
        self.pendingFileCountWarningSet = False
        
        self.dirScans = 0
        self.dirScansSet = False
        
        self.fileArchiveDurationWarning = 0
        self.fileArchiveDurationWarningSet = False
        
        self.archivedErrors = 0
        self.archivedErrorsSet = False
        
        self.dirScansErrors = 0
        self.dirScansErrorsSet = False
        

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("counters", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "qt-log"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("log-archiving", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "qt-log"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("housekeeper", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "qt-log"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("log", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "qt-log"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       
                       readAllOrFail,
                       trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-read').debug3Func(): logFunc('called. PARAMS, readAllOrFail=%s', readAllOrFail)

        if readAllOrFail:
            self._clearAllReadData()

        tagValueList = TagValues()

        res = self._fillReadTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-fill-read-tag-value-failed').errorFunc(): logFunc('_fillReadTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(
                                       None)

        res = self.domain.readMaapi(tagValueList, keyPath, trxContext)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-domain-failed').errorFunc(): logFunc('domain.readMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        res = self._readTagValues(tagValueList, readAllOrFail)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-read-tag-values-failed').errorFunc(): logFunc('_readTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-read-done').debug3Func(): logFunc('done. PARAMS, readAllOrFail=%s', readAllOrFail)
        return ReturnCodes.kOk

    def _collectItemsToDelete (self,
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isActiveSecondsRequested():
            valActiveSeconds = Value()
            valActiveSeconds.setEmpty()
            tagValueList.push(("active-seconds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valActiveSeconds)
        
        if self.isArchivedFilesRequested():
            valArchivedFiles = Value()
            valArchivedFiles.setEmpty()
            tagValueList.push(("archived-files", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valArchivedFiles)
        
        if self.isOverallArchiveDurationWarningRequested():
            valOverallArchiveDurationWarning = Value()
            valOverallArchiveDurationWarning.setEmpty()
            tagValueList.push(("overall-archive-duration-warning", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valOverallArchiveDurationWarning)
        
        if self.isOnePendingFileRequested():
            valOnePendingFile = Value()
            valOnePendingFile.setEmpty()
            tagValueList.push(("one-pending-file", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valOnePendingFile)
        
        if self.isFileArchiveDurationErrorsRequested():
            valFileArchiveDurationErrors = Value()
            valFileArchiveDurationErrors.setEmpty()
            tagValueList.push(("file-archive-duration-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valFileArchiveDurationErrors)
        
        if self.isOverallArchiveDurationErrorsRequested():
            valOverallArchiveDurationErrors = Value()
            valOverallArchiveDurationErrors.setEmpty()
            tagValueList.push(("overall-archive-duration-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valOverallArchiveDurationErrors)
        
        if self.isPendingFileCountErrorsRequested():
            valPendingFileCountErrors = Value()
            valPendingFileCountErrors.setEmpty()
            tagValueList.push(("pending-file-count-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valPendingFileCountErrors)
        
        if self.isPendingFileCountWarningRequested():
            valPendingFileCountWarning = Value()
            valPendingFileCountWarning.setEmpty()
            tagValueList.push(("pending-file-count-warning", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valPendingFileCountWarning)
        
        if self.isDirScansRequested():
            valDirScans = Value()
            valDirScans.setEmpty()
            tagValueList.push(("dir-scans", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valDirScans)
        
        if self.isFileArchiveDurationWarningRequested():
            valFileArchiveDurationWarning = Value()
            valFileArchiveDurationWarning.setEmpty()
            tagValueList.push(("file-archive-duration-warning", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valFileArchiveDurationWarning)
        
        if self.isArchivedErrorsRequested():
            valArchivedErrors = Value()
            valArchivedErrors.setEmpty()
            tagValueList.push(("archived-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valArchivedErrors)
        
        if self.isDirScansErrorsRequested():
            valDirScansErrors = Value()
            valDirScansErrors.setEmpty()
            tagValueList.push(("dir-scans-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valDirScansErrors)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isActiveSecondsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "active-seconds") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-activeseconds').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "activeSeconds", "active-seconds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-active-seconds-bad-value').infoFunc(): logFunc('activeSeconds not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setActiveSeconds(tempVar)
            for logFunc in self._log('read-tag-values-active-seconds').debug3Func(): logFunc('read activeSeconds. activeSeconds=%s, tempValue=%s', self.activeSeconds, tempValue.getType())
        
        if self.isArchivedFilesRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "archived-files") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-archivedfiles').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "archivedFiles", "archived-files", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-archived-files-bad-value').infoFunc(): logFunc('archivedFiles not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setArchivedFiles(tempVar)
            for logFunc in self._log('read-tag-values-archived-files').debug3Func(): logFunc('read archivedFiles. archivedFiles=%s, tempValue=%s', self.archivedFiles, tempValue.getType())
        
        if self.isOverallArchiveDurationWarningRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "overall-archive-duration-warning") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-overallarchivedurationwarning').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "overallArchiveDurationWarning", "overall-archive-duration-warning", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-overall-archive-duration-warning-bad-value').infoFunc(): logFunc('overallArchiveDurationWarning not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOverallArchiveDurationWarning(tempVar)
            for logFunc in self._log('read-tag-values-overall-archive-duration-warning').debug3Func(): logFunc('read overallArchiveDurationWarning. overallArchiveDurationWarning=%s, tempValue=%s', self.overallArchiveDurationWarning, tempValue.getType())
        
        if self.isOnePendingFileRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "one-pending-file") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-onependingfile').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "onePendingFile", "one-pending-file", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-one-pending-file-bad-value').infoFunc(): logFunc('onePendingFile not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOnePendingFile(tempVar)
            for logFunc in self._log('read-tag-values-one-pending-file').debug3Func(): logFunc('read onePendingFile. onePendingFile=%s, tempValue=%s', self.onePendingFile, tempValue.getType())
        
        if self.isFileArchiveDurationErrorsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "file-archive-duration-errors") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-filearchivedurationerrors').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "fileArchiveDurationErrors", "file-archive-duration-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-file-archive-duration-errors-bad-value').infoFunc(): logFunc('fileArchiveDurationErrors not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setFileArchiveDurationErrors(tempVar)
            for logFunc in self._log('read-tag-values-file-archive-duration-errors').debug3Func(): logFunc('read fileArchiveDurationErrors. fileArchiveDurationErrors=%s, tempValue=%s', self.fileArchiveDurationErrors, tempValue.getType())
        
        if self.isOverallArchiveDurationErrorsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "overall-archive-duration-errors") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-overallarchivedurationerrors').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "overallArchiveDurationErrors", "overall-archive-duration-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-overall-archive-duration-errors-bad-value').infoFunc(): logFunc('overallArchiveDurationErrors not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOverallArchiveDurationErrors(tempVar)
            for logFunc in self._log('read-tag-values-overall-archive-duration-errors').debug3Func(): logFunc('read overallArchiveDurationErrors. overallArchiveDurationErrors=%s, tempValue=%s', self.overallArchiveDurationErrors, tempValue.getType())
        
        if self.isPendingFileCountErrorsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "pending-file-count-errors") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-pendingfilecounterrors').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "pendingFileCountErrors", "pending-file-count-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-pending-file-count-errors-bad-value').infoFunc(): logFunc('pendingFileCountErrors not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPendingFileCountErrors(tempVar)
            for logFunc in self._log('read-tag-values-pending-file-count-errors').debug3Func(): logFunc('read pendingFileCountErrors. pendingFileCountErrors=%s, tempValue=%s', self.pendingFileCountErrors, tempValue.getType())
        
        if self.isPendingFileCountWarningRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "pending-file-count-warning") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-pendingfilecountwarning').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "pendingFileCountWarning", "pending-file-count-warning", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-pending-file-count-warning-bad-value').infoFunc(): logFunc('pendingFileCountWarning not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPendingFileCountWarning(tempVar)
            for logFunc in self._log('read-tag-values-pending-file-count-warning').debug3Func(): logFunc('read pendingFileCountWarning. pendingFileCountWarning=%s, tempValue=%s', self.pendingFileCountWarning, tempValue.getType())
        
        if self.isDirScansRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "dir-scans") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-dirscans').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "dirScans", "dir-scans", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-dir-scans-bad-value').infoFunc(): logFunc('dirScans not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setDirScans(tempVar)
            for logFunc in self._log('read-tag-values-dir-scans').debug3Func(): logFunc('read dirScans. dirScans=%s, tempValue=%s', self.dirScans, tempValue.getType())
        
        if self.isFileArchiveDurationWarningRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "file-archive-duration-warning") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-filearchivedurationwarning').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "fileArchiveDurationWarning", "file-archive-duration-warning", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-file-archive-duration-warning-bad-value').infoFunc(): logFunc('fileArchiveDurationWarning not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setFileArchiveDurationWarning(tempVar)
            for logFunc in self._log('read-tag-values-file-archive-duration-warning').debug3Func(): logFunc('read fileArchiveDurationWarning. fileArchiveDurationWarning=%s, tempValue=%s', self.fileArchiveDurationWarning, tempValue.getType())
        
        if self.isArchivedErrorsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "archived-errors") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-archivederrors').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "archivedErrors", "archived-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-archived-errors-bad-value').infoFunc(): logFunc('archivedErrors not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setArchivedErrors(tempVar)
            for logFunc in self._log('read-tag-values-archived-errors').debug3Func(): logFunc('read archivedErrors. archivedErrors=%s, tempValue=%s', self.archivedErrors, tempValue.getType())
        
        if self.isDirScansErrorsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "dir-scans-errors") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-dirscanserrors').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "dirScansErrors", "dir-scans-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-dir-scans-errors-bad-value').infoFunc(): logFunc('dirScansErrors not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setDirScansErrors(tempVar)
            for logFunc in self._log('read-tag-values-dir-scans-errors').debug3Func(): logFunc('read dirScansErrors. dirScansErrors=%s, tempValue=%s', self.dirScansErrors, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "counters", 
        "namespace": "counters", 
        "className": "CountersMaapi", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_log.tech.log.housekeeper.log_archiving.counters.counters_maapi_gen import CountersMaapi", 
        "baseClassName": "CountersMaapiBase", 
        "baseModule": "counters_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "qt", 
            "yangName": "tech", 
            "namespace": "tech", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech", 
            "name": "tech"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-log", 
            "yangName": "log", 
            "namespace": "log", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "name": "log"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-log", 
            "yangName": "housekeeper", 
            "namespace": "housekeeper", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "name": "housekeeper"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-log", 
            "yangName": "log-archiving", 
            "namespace": "log_archiving", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "name": "log-archiving"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-log", 
            "yangName": "counters", 
            "namespace": "counters", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "name": "counters"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "activeSeconds", 
            "yangName": "active-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "archivedFiles", 
            "yangName": "archived-files", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallArchiveDurationWarning", 
            "yangName": "overall-archive-duration-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "onePendingFile", 
            "yangName": "one-pending-file", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "fileArchiveDurationErrors", 
            "yangName": "file-archive-duration-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallArchiveDurationErrors", 
            "yangName": "overall-archive-duration-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pendingFileCountErrors", 
            "yangName": "pending-file-count-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pendingFileCountWarning", 
            "yangName": "pending-file-count-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "dirScans", 
            "yangName": "dir-scans", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "fileArchiveDurationWarning", 
            "yangName": "file-archive-duration-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "archivedErrors", 
            "yangName": "archived-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
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
    "configLeaves": [], 
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
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "activeSeconds", 
            "yangName": "active-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "archivedFiles", 
            "yangName": "archived-files", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallArchiveDurationWarning", 
            "yangName": "overall-archive-duration-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "onePendingFile", 
            "yangName": "one-pending-file", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "fileArchiveDurationErrors", 
            "yangName": "file-archive-duration-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallArchiveDurationErrors", 
            "yangName": "overall-archive-duration-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pendingFileCountErrors", 
            "yangName": "pending-file-count-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pendingFileCountWarning", 
            "yangName": "pending-file-count-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "dirScans", 
            "yangName": "dir-scans", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "fileArchiveDurationWarning", 
            "yangName": "file-archive-duration-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "archivedErrors", 
            "yangName": "archived-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "dirScansErrors", 
            "yangName": "dir-scans-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


