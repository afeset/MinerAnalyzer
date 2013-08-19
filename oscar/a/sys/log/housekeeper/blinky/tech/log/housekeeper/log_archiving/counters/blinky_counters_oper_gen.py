



# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

# Must be set here to avoid stupid warnings about stuff in BlinkyOperContainer
__pychecker__="no-classattr"

from a.api.yang.modules.tech.debug.qwilt_tech_log.tech.log.housekeeper.log_archiving.counters.counters_oper_data_gen import CountersOperData
from a.sys.blinky.blinky_oper_node import BlinkyOperNode
from a.sys.confd.pyconfdlib.key_path import KeyPath
from a.sys.confd.pyconfdlib.value import Value
from a.sys.confd.pyconfdlib.tag_values import TagValues

from a.infra.misc.timeout_guard import TimeoutGuard
from a.infra.basic.return_codes import ReturnCodes
from a.sys.blinky.pass_by_ref import PassByRef









class BlinkyOperCounters(BlinkyOperNode):

    _kCallpointName = "tech-log-housekeeper-log-archiving-counters-callpoint"

    GET_OBJ_FUNCTOR = 'GET_OBJ_FUNCTOR'

    


    def __init__ (self, logger):
        BlinkyOperNode.__init__(self, logger)
        self.kCallpointName = "tech-log-housekeeper-log-archiving-counters-callpoint"
        
        self.myGetObjectFunctor = None
        
        

    def getCallpointName (self):
        return self.kCallpointName

    def setParent (self, parentNode):
        for logFunc in self._log("set-parent").debug2Func(): logFunc("called")
        BlinkyOperNode.setParent(self, parentNode)

        

        return ReturnCodes.kOk

    def distributeConfigObjectToDescendants (self, configObj):
        for logFunc in self._log("distribute-config-object-to-descendants").debug3Func(): logFunc("called. configObj=%s", configObj)

        
        return ReturnCodes.kOk

    def getOperRelativePath (self, operRelativePath):
        for logFunc in self._log("get-oper-relative-path").debug3Func(): logFunc("called")
        
        val = Value()
        val.setXmlTag(("counters", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "qt-log"))
        operRelativePath.addKeyPathPostfix(val)
        
        for logFunc in self._log("getOperRelativePath-done").debug3Func(): logFunc("done. operRelativePath=%s", operRelativePath)


    def setOperDataRequestedFields (self, operData, keyPath):
        __pychecker__="maxbranches=100 maxlines=500"
        for logFunc in self._log("set-oper-data-requested-fields").debug3Func(): logFunc("called. operData=%s, keyPath=%s", operData.debugStr(True), keyPath)
        flattenedSelfKeyPath = self.myKeyPath.getKeyPathPostfixFlattened(self.myConfigNode.getKeyPath(), False)
        requestedKeyPath = keyPath.getKeyPathPostfixFlattened(self.myConfigNode.getKeyPath(), False)
        
        if requestedKeyPath.isEqual(flattenedSelfKeyPath) or (requestedKeyPath.getLen() <= flattenedSelfKeyPath.getLen()):
        
            operData.setAllRequested()
        else:
            
            for logFunc in self._log("set-oper-data-requested-fields-checking-fields").debug3Func(): logFunc("requestedKeyPath=%s, flattenedSelfKeyPath=%s", requestedKeyPath, flattenedSelfKeyPath)
            if requestedKeyPath.getLen() > flattenedSelfKeyPath.getLen():
            
                
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "active-seconds"):
                    for logFunc in self._log("set-oper-data-requested-fields-activeseconds-requested").debug3Func(): logFunc(
                        "active-seconds requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setActiveSecondsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "archived-files"):
                    for logFunc in self._log("set-oper-data-requested-fields-archivedfiles-requested").debug3Func(): logFunc(
                        "archived-files requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setArchivedFilesRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "overall-archive-duration-warning"):
                    for logFunc in self._log("set-oper-data-requested-fields-overallarchivedurationwarning-requested").debug3Func(): logFunc(
                        "overall-archive-duration-warning requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setOverallArchiveDurationWarningRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "one-pending-file"):
                    for logFunc in self._log("set-oper-data-requested-fields-onependingfile-requested").debug3Func(): logFunc(
                        "one-pending-file requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setOnePendingFileRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "file-archive-duration-errors"):
                    for logFunc in self._log("set-oper-data-requested-fields-filearchivedurationerrors-requested").debug3Func(): logFunc(
                        "file-archive-duration-errors requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setFileArchiveDurationErrorsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "overall-archive-duration-errors"):
                    for logFunc in self._log("set-oper-data-requested-fields-overallarchivedurationerrors-requested").debug3Func(): logFunc(
                        "overall-archive-duration-errors requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setOverallArchiveDurationErrorsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "pending-file-count-errors"):
                    for logFunc in self._log("set-oper-data-requested-fields-pendingfilecounterrors-requested").debug3Func(): logFunc(
                        "pending-file-count-errors requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setPendingFileCountErrorsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "pending-file-count-warning"):
                    for logFunc in self._log("set-oper-data-requested-fields-pendingfilecountwarning-requested").debug3Func(): logFunc(
                        "pending-file-count-warning requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setPendingFileCountWarningRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "dir-scans"):
                    for logFunc in self._log("set-oper-data-requested-fields-dirscans-requested").debug3Func(): logFunc(
                        "dir-scans requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setDirScansRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "file-archive-duration-warning"):
                    for logFunc in self._log("set-oper-data-requested-fields-filearchivedurationwarning-requested").debug3Func(): logFunc(
                        "file-archive-duration-warning requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setFileArchiveDurationWarningRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "archived-errors"):
                    for logFunc in self._log("set-oper-data-requested-fields-archivederrors-requested").debug3Func(): logFunc(
                        "archived-errors requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setArchivedErrorsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "dir-scans-errors"):
                    for logFunc in self._log("set-oper-data-requested-fields-dirscanserrors-requested").debug3Func(): logFunc(
                        "dir-scans-errors requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setDirScansErrorsRequested()
                
            else:
                for logFunc in self._log("set-oper-data-requested-fields-bad-keypath").errorFunc(): logFunc(
                    "don't know how to handle this keyPath. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                return ReturnCodes.kGeneralError

        for logFunc in self._log("set-oper-data-requested-fields-done").debug3Func(): logFunc("done. operData=%s, keyPath=%s", operData.debugStr(True), keyPath)
        return ReturnCodes.kOk

    

    def fillTagValues (self, keyPath, tagValueList, operData):
        initialListSize = tagValueList.getLen()
        for logFunc in self._log("fill-tag-values").debug3Func(): logFunc("called. operData=%s, keyPath=%s, initialListSize=%d", operData.debugStr(True), keyPath, initialListSize)
        # fill tag values up to current
        if self.myKeyPath.isEqualLen(keyPath, keyPath.getLen()):
            i = keyPath.getLen()
            while i < self.myKeyPath.getLen():
                valBegin = Value()
                (tag, ns, prefix) = self.myKeyPath.getAt(i).asXmlTag()
                valBegin.setXmlBegin((tag, ns, prefix))
                tagValueList.push((tag, ns), valBegin)
                for logFunc in self._log("fill-tag-values-adding").debug3Func(): logFunc("adding xml begin. i=%d, valBegin=%s, self.myKeyPath.getLen()=%d", i, valBegin, self.myKeyPath.getLen())
                i+=1
        
        if operData.isActiveSecondsRequested() and operData.hasActiveSeconds():
            val = Value()
            val.setInt64(operData.activeSeconds)
            tagValueList.push(("active-seconds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), val)
        
        if operData.isArchivedFilesRequested() and operData.hasArchivedFiles():
            val = Value()
            val.setInt64(operData.archivedFiles)
            tagValueList.push(("archived-files", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), val)
        
        if operData.isOverallArchiveDurationWarningRequested() and operData.hasOverallArchiveDurationWarning():
            val = Value()
            val.setInt64(operData.overallArchiveDurationWarning)
            tagValueList.push(("overall-archive-duration-warning", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), val)
        
        if operData.isOnePendingFileRequested() and operData.hasOnePendingFile():
            val = Value()
            val.setInt64(operData.onePendingFile)
            tagValueList.push(("one-pending-file", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), val)
        
        if operData.isFileArchiveDurationErrorsRequested() and operData.hasFileArchiveDurationErrors():
            val = Value()
            val.setInt64(operData.fileArchiveDurationErrors)
            tagValueList.push(("file-archive-duration-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), val)
        
        if operData.isOverallArchiveDurationErrorsRequested() and operData.hasOverallArchiveDurationErrors():
            val = Value()
            val.setInt64(operData.overallArchiveDurationErrors)
            tagValueList.push(("overall-archive-duration-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), val)
        
        if operData.isPendingFileCountErrorsRequested() and operData.hasPendingFileCountErrors():
            val = Value()
            val.setInt64(operData.pendingFileCountErrors)
            tagValueList.push(("pending-file-count-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), val)
        
        if operData.isPendingFileCountWarningRequested() and operData.hasPendingFileCountWarning():
            val = Value()
            val.setInt64(operData.pendingFileCountWarning)
            tagValueList.push(("pending-file-count-warning", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), val)
        
        if operData.isDirScansRequested() and operData.hasDirScans():
            val = Value()
            val.setInt64(operData.dirScans)
            tagValueList.push(("dir-scans", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), val)
        
        if operData.isFileArchiveDurationWarningRequested() and operData.hasFileArchiveDurationWarning():
            val = Value()
            val.setInt64(operData.fileArchiveDurationWarning)
            tagValueList.push(("file-archive-duration-warning", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), val)
        
        if operData.isArchivedErrorsRequested() and operData.hasArchivedErrors():
            val = Value()
            val.setInt64(operData.archivedErrors)
            tagValueList.push(("archived-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), val)
        
        if operData.isDirScansErrorsRequested() and operData.hasDirScansErrors():
            val = Value()
            val.setInt64(operData.dirScansErrors)
            tagValueList.push(("dir-scans-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), val)
        
        
        if self.myKeyPath.isEqualLen(keyPath, keyPath.getLen()):
            i = self.myKeyPath.getLen() - 1
            while i >= keyPath.getLen():
                valEnd = Value()
                (tag, ns, prefix) = self.myKeyPath.getAt(i).asXmlTag()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
                i-=1

        for logFunc in self._log("fill-tag-values-ended").debug3Func(): logFunc("ended. operData=%s, keyPath=%s, initialListSize=%d, finalListSize=%d",
                                                  operData.debugStr(True), keyPath, initialListSize, tagValueList.getLen())
        return ReturnCodes.kOk

    def fillValue (self, value, keyPath, operData):
        __pychecker__="maxbranches=100 maxlines=500"
        for logFunc in self._log("fill-value").debug3Func(): logFunc("called. keyPath=%s, operData=%s", keyPath, operData.debugStr(True))
        flattenedSelfKeyPath = self.myKeyPath.getKeyPathPostfixFlattened(self.myConfigNode.getKeyPath(), False)
        requestedKeyPath = keyPath.getKeyPathPostfixFlattened(self.myConfigNode.getKeyPath(), False)
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "active-seconds"):
            if operData.isActiveSecondsRequested():
                 if operData.hasActiveSeconds():
                     value.setInt64(operData.activeSeconds)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "archived-files"):
            if operData.isArchivedFilesRequested():
                 if operData.hasArchivedFiles():
                     value.setInt64(operData.archivedFiles)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "overall-archive-duration-warning"):
            if operData.isOverallArchiveDurationWarningRequested():
                 if operData.hasOverallArchiveDurationWarning():
                     value.setInt64(operData.overallArchiveDurationWarning)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "one-pending-file"):
            if operData.isOnePendingFileRequested():
                 if operData.hasOnePendingFile():
                     value.setInt64(operData.onePendingFile)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "file-archive-duration-errors"):
            if operData.isFileArchiveDurationErrorsRequested():
                 if operData.hasFileArchiveDurationErrors():
                     value.setInt64(operData.fileArchiveDurationErrors)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "overall-archive-duration-errors"):
            if operData.isOverallArchiveDurationErrorsRequested():
                 if operData.hasOverallArchiveDurationErrors():
                     value.setInt64(operData.overallArchiveDurationErrors)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "pending-file-count-errors"):
            if operData.isPendingFileCountErrorsRequested():
                 if operData.hasPendingFileCountErrors():
                     value.setInt64(operData.pendingFileCountErrors)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "pending-file-count-warning"):
            if operData.isPendingFileCountWarningRequested():
                 if operData.hasPendingFileCountWarning():
                     value.setInt64(operData.pendingFileCountWarning)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "dir-scans"):
            if operData.isDirScansRequested():
                 if operData.hasDirScans():
                     value.setInt64(operData.dirScans)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "file-archive-duration-warning"):
            if operData.isFileArchiveDurationWarningRequested():
                 if operData.hasFileArchiveDurationWarning():
                     value.setInt64(operData.fileArchiveDurationWarning)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "archived-errors"):
            if operData.isArchivedErrorsRequested():
                 if operData.hasArchivedErrors():
                     value.setInt64(operData.archivedErrors)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "dir-scans-errors"):
            if operData.isDirScansErrorsRequested():
                 if operData.hasDirScansErrors():
                     value.setInt64(operData.dirScansErrors)
                 else:
                     value.setEmpty()
        
        
        for logFunc in self._log("fill-value-ended").debug3Func(): logFunc("ended. keyPath=%s, operData=%s, value=%s", keyPath, operData.debugStr(True), value)
        return ReturnCodes.kOk


    def replyObject (self, dpTrxCtx, keyPath, operData):
        for logFunc in self._log("reply-object").debug3Func(): logFunc("called. dpTrxCtx=%s, operData=%s, keyPath=%s", dpTrxCtx, operData.debugStr(True), keyPath)
        tagValueList = TagValues()
        res = self.fillTagValues(keyPath, tagValueList, operData)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("reply-object-fill-tag-values-failed").errorFunc(): logFunc(
                "fillTagValues() failed. operData=%s, keyPath=%s", operData.debugStr(True), keyPath)
            return ReturnCodes.kGeneralError
        res = self.myDomain.sendTagValues(dpTrxCtx, tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("reply-object-send-tag-values-failed").errorFunc(): logFunc(
                "myDomain.sendTagValues() failed. operData=%s, keyPath=%s", operData.debugStr(True), keyPath)
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def replyElement (self, dpTrxCtx, keyPath, operData):
        for logFunc in self._log("reply-element").debug3Func(): logFunc("called. dpTrxCtx=%s, operData=%s, keyPath=%s", dpTrxCtx, operData.debugStr(True), keyPath)
        val = Value()
        res = self.fillValue(val, keyPath, operData)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("reply-element-fill-value-failed").errorFunc(): logFunc(
                "fillValue() failed. operData=%s, keyPath=%s", operData.debugStr(True), keyPath)
            return ReturnCodes.kGeneralError
        res = self.myDomain.sendValue(dpTrxCtx, val)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("reply-element-send-value-failed").errorFunc(): logFunc(
                "myDomain.sendValue() failed. operData=%s, keyPath=%s, value=%s", operData.debugStr(True), keyPath, val)
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def getObject (self, trxContext, keyPath):
        for logFunc in self._log("get-object").debug3Func(): logFunc("called. trxContext=%s, keyPath=%s", trxContext, keyPath)
        operData = CountersOperData()

        res = self.handleGetRequest(trxContext, keyPath, operData)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("get-object-handle-get-request-failed").errorFunc(): logFunc(
                "handleGetRequest() failed. operData=%s, keyPath=%s, trxContext=%s", operData.debugStr(True), keyPath, trxContext)
            return ReturnCodes.kGeneralError

        res = self.replyObject(trxContext, keyPath, operData)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("get-object-reply-object-failed").errorFunc(): logFunc(
                "handleGetRequest() failed. operData=%s, keyPath=%s, trxContext=%s", operData.debugStr(True), keyPath, trxContext)
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def handleGetRequest (self, trxContext, keyPath, operData):
        for logFunc in self._log("handle-get-request").debug3Func(): logFunc("called. trxContext=%s, keyPath=%s", trxContext, keyPath)

        

        res = self.setOperDataRequestedFields(operData, keyPath)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("handle-get-request-set-oper-data-requested-fields-failed").errorFunc(): logFunc(
                "setOperDataRequestedFields() failed. keyPath=%s, trxContext=%s", keyPath, trxContext)
            return ReturnCodes.kGeneralError

        if self.myIsActive:
            if self.myGetObjectFunctor:
                timeoutGuardName = str(self.myKeyPath) + "-" + "get-object-functor";
                timeoutGuard = TimeoutGuard(self._log, timeoutGuardName, 
                                            self.getFunctorTimeout(self.GET_OBJ_FUNCTOR), 
                                            self.getFunctorMildTimeout(self.GET_OBJ_FUNCTOR))
                
                
                
                
                
                
                
                res = self.myGetObjectFunctor(trxContext, 
                                              
                                              
                                              operData)
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myGetObjectFunctor.__name__)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log("handle-get-request-functor-failed").errorFunc(): logFunc(
                        "functor failed. keyPath=%s, trxContext=%s", keyPath, trxContext)
                    return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def getElement (self, trxContext, keyPath):
        for logFunc in self._log("get-element").debug3Func(): logFunc("called. trxContext=%s, keyPath=%s", trxContext, keyPath)

        operData = CountersOperData()
        res = self.handleGetRequest(trxContext, keyPath, operData)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("get-element-handle-get-request-failed").errorFunc(): logFunc(
                "handleGetRequest() failed. keyPath=%s, trxContext=%s, operData=%s", keyPath, trxContext, operData.debugStr(True))
            return ReturnCodes.kGeneralError

        res = self.replyElement(trxContext, keyPath, operData)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("get-element-reply-element-failed").errorFunc(): logFunc(
                "replyElement() failed. keyPath=%s, trxContext=%s, operData=%s", keyPath, trxContext, operData.debugStr(True))
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk


    def setBasicFunctors (self, getObjFunctor):
        if self.myIsActive:
            for logFunc in self._log("set-basic-functor-active").errorFunc(): logFunc("illegal when blinky active.")
            return

        self.myGetObjectFunctor = getObjFunctor
        self.myFunctorsSet = True







"""
Extracted from the below data: 
{
    "node": {
        "dataImportStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_log.tech.log.housekeeper.log_archiving.counters.counters_oper_data_gen import CountersOperData", 
        "callpointResponsible": true, 
        "moduleYangNamespacePrefix": "qt-log", 
        "validationPoint": null, 
        "getNextArgsNum": 4, 
        "yangName": "counters", 
        "namespace": "counters", 
        "logGroupName": "blinky-counters-oper", 
        "className": "BlinkyOperCounters", 
        "logModuleName": "a-sys-log-housekeeper-blinky-tech-log-housekeeper-log-archiving-counters-blinky-counters-oper-gen", 
        "importStatement": "from a.sys.log.housekeeper.blinky.tech.log.housekeeper.log_archiving.counters.blinky_counters_oper_gen import BlinkyOperCounters", 
        "callpointName": "tech-log-housekeeper-log-archiving-counters-callpoint", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
        "dataClassName": "CountersOperData", 
        "getObjArgsNum": 2, 
        "actionPoint": null
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "qt", 
            "yangName": "tech", 
            "namespace": "tech", 
            "isCurrent": false, 
            "isList": false, 
            "isOper": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech", 
            "name": "tech"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-log", 
            "yangName": "log", 
            "namespace": "log", 
            "isCurrent": false, 
            "isList": false, 
            "isOper": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "name": "log"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-log", 
            "yangName": "housekeeper", 
            "namespace": "housekeeper", 
            "isCurrent": false, 
            "isList": false, 
            "isOper": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "name": "housekeeper"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-log", 
            "yangName": "log-archiving", 
            "namespace": "log_archiving", 
            "isCurrent": false, 
            "isList": false, 
            "isOper": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "name": "log-archiving"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-log", 
            "yangName": "counters", 
            "namespace": "counters", 
            "isCurrent": true, 
            "isList": false, 
            "isOper": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "name": "counters"
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
    "env": [
        "a", 
        "sys", 
        "log", 
        "housekeeper", 
        "blinky", 
        ""
    ], 
    "createTime": "2013"
}
"""


