


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

# Must be set here to avoid stupid warnings about stuff in BlinkyContainer
__pychecker__="no-classattr"

from a.infra.basic.return_codes import ReturnCodes
from a.infra.misc.timeout_guard import TimeoutGuard
import a.infra.process.captain
from a.sys.blinky.blinky_container import BlinkyContainer
from a.sys.blinky.trx_phase import TrxPhase
from a.sys.confd.pyconfdlib import pyconfdlib
from a.sys.confd.pyconfdlib.key_path import KeyPath
from a.sys.confd.pyconfdlib.value import Value
import copy

from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.system_defaults.file_system.file_system_data_gen import FileSystemData


from a.storage.disk.tech_storage.tech.storage.disk.system_defaults.file_system.commands.blinky_commands_gen import BlinkyCommands

from a.storage.disk.tech_storage.tech.storage.disk.system_defaults.file_system.timeouts.blinky_timeouts_gen import BlinkyTimeouts


from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import FileSystemTypeType


class BlinkyFileSystem(BlinkyContainer):
    ourNamespace="http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"
    #leaves
    
    ourXmlTagAutoInit="auto-init"
    
    ourXmlTagCheckUuid="check-uuid"
    
    ourXmlTagReadAhead="read-ahead"
    
    ourXmlTagFileSystemType="file-system-type"
    

    #descendants
    
    ourXmlTagCommands="commands"
    
    ourXmlTagTimeouts="timeouts"
    

    _validationPointId=None
    
    _actionPointId=None
    

    
    COMMANDS_CREATE_FUNCTOR = 'COMMANDS_CREATE_FUNCTOR'
    COMMANDS_DELETE_FUNCTOR = 'COMMANDS_DELETE_FUNCTOR'
    
    TIMEOUTS_CREATE_FUNCTOR = 'TIMEOUTS_CREATE_FUNCTOR'
    TIMEOUTS_DELETE_FUNCTOR = 'TIMEOUTS_DELETE_FUNCTOR'
    
    VALUE_SET_FUNCTOR = 'VALUE_SET_FUNCTOR'
    VALIDATE_TRX_FUNCTOR = 'VALIDATE_TRX_FUNCTOR'
    DO_ACTION_FUNCTOR = 'DO_ACTION_FUNCTOR'

    # Improve performance: Store hashed values of these strings here as well.

    def __init__ (self, logger):
        BlinkyContainer.__init__(self, logger)
        
        self.myCreateCommandsFunctor=None
        self.myDeleteCommandsFunctor=None
        self.myCommands=None
        
        self.myCreateTimeoutsFunctor=None
        self.myDeleteTimeoutsFunctor=None
        self.myTimeouts=None
        
        self.myValueSetFunctor=None
        self.myCandidateData=None
        self.myRunningData=None
        self.isInDestroy = False
        
        self.validateRegistrationDone = False
        self.actionRegistrationDone=False
        
        

    @classmethod
    def s_create (cls, logger, 
                  
                  
                  
                  disk, 
                  
                  
                  domain):
        __pychecker__="no-argsused"

        logger('s-create-blinkyfilesystem').info('called. domain=%s, _validationPointId=%s, _actionPointId=%s', domain, BlinkyFileSystem._validationPointId, BlinkyFileSystem._actionPointId)

        confd_key=KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("file-system", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(disk);
        confd_key.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("disk", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("storage", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage", "qt-strg"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        newNode=BlinkyFileSystem(logger)
        logger("s-create-keypath").info("confd_key=%s", confd_key)
        newNode.setParent(None)
        newNode.setKeyPath(confd_key)
        newNode.setDomain(domain)
        res = newNode.internalInit()
        if (res != ReturnCodes.kOk):
            logger("s-create-internal-init-failed")\
                .error("internalInit() failed. confd_key=%s", confd_key)

        if newNode._validationPointId:
            res = domain.registerValidationPoint(newNode._validationPointId, newNode)
            if (res != ReturnCodes.kOk):
                logger("s-create-register-validation-node--failed")\
                    .error("registerValidationNode(%s) failed",  newNode._validationPointId)
                return None
        newNode.validateRegistrationDone = True
        if newNode._actionPointId:
            res = domain.registerActionPoint(newNode._actionPointId, newNode)
            if (res != ReturnCodes.kOk):
                logger("s-create-register-action-node--failed")\
                    .error("registerActionNode(%s) failed",  newNode._actionPointId)
                return None
        newNode.actionRegistrationDone = True

        return newNode

    
    def setCreateCommandsFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-commands-functor-active").errorFunc():
                logFunc("setCreateCommandsFunctor() is illegal when blinky node is active")
        self.myCreateCommandsFunctor = functor

    def setDeleteCommandsFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-commands-functor-active").errorFunc():
                logFunc("setDeleteCommandsFunctor() is illegal when blinky node is active")
        self.myDeleteCommandsFunctor = functor
    
    def setCreateTimeoutsFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-timeouts-functor-active").errorFunc():
                logFunc("setCreateTimeoutsFunctor() is illegal when blinky node is active")
        self.myCreateTimeoutsFunctor = functor

    def setDeleteTimeoutsFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-timeouts-functor-active").errorFunc():
                logFunc("setDeleteTimeoutsFunctor() is illegal when blinky node is active")
        self.myDeleteTimeoutsFunctor = functor
    

    

    

    def trxElementUpdateCandidate(self, trxElement, keyDepth):
        keyPath = trxElement.getKeyPath()
        for logFunc in self._log("trx-element-update-candidate").debug3Func():
            logFunc("trxElementUpdateCandidate(): called, keyPath=%s, keyDepth=%s, trxElement=%s", keyPath, keyDepth, trxElement)
        
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagAutoInit)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.autoInit = newValue.asBool()
                self.myCandidateData.setHasAutoInit()
                
            else:
                self.setAutoInitDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagCheckUuid)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.checkUuid = newValue.asBool()
                self.myCandidateData.setHasCheckUuid()
                
            else:
                self.setCheckUuidDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagReadAhead)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.readAhead = newValue.asInt64()
                self.myCandidateData.setHasReadAhead()
                
            else:
                self.setReadAheadDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagFileSystemType)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                if not FileSystemTypeType.isValidValue(newValue.asEnum()):
                    self._log("trx-element-update-candidate-illegal-enum-filesystemtype-failed")\
                        .error("illegal enum value %s for fileSystemType", newValue.asEnum())
                    return ReturnCodes.kGeneralError
                self.myCandidateData.fileSystemType = FileSystemTypeType.getByValue(newValue.asEnum())
                self.myCandidateData.setHasFileSystemType()
                
            else:
                self.setFileSystemTypeDefaultValue(True)
            
        for logFunc in self._log("trx-element-update-candidate-done").debug3Func():
            logFunc("trxElementUpdateCandidate(): After update, candidate is %s", self.myCandidateData)
    
    def getDescendant(self, keyPath, keyDepth_PBR):
        for logFunc in self._log("get-descendant").debug3Func(): logFunc("getDescendant(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth_PBR)
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagCommands)):
            return self.myCommands
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagTimeouts)):
            return self.myTimeouts
        
        for logFunc in self._log("get-descendant-unknown").debug3Func(): logFunc("getDescendant(): unknown, keyPath=%s, keyDepth=%s", keyPath, keyDepth_PBR)
        return None
    
    @classmethod
    def isKeyPathRegistered (cls, logger, keyPath, keyDepth):
        __pychecker__="no-argsused no-local"
        logger('is-key-path-registered-blinkyfilesystem').debug3('isKeyPathRegistered() called. keyPath=%s, keyDepth=%d, I am: from a.storage.disk.tech_storage.tech.storage.disk.system_defaults.file_system.blinky_file_system_gen import BlinkyFileSystem', keyPath, keyDepth)
        keyPathRegistered = False
        found = False
        
        if not found:
            if keyPath.getLen() > keyDepth+1:
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagCommands)):
                    keyPathRegistered = BlinkyCommands.isKeyPathRegistered(logger, keyPath, keyDepth+1)
                    found = True
            else:
                keyPathRegistered = True
                found = True
        
        if not found:
            if keyPath.getLen() > keyDepth+1:
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagTimeouts)):
                    keyPathRegistered = BlinkyTimeouts.isKeyPathRegistered(logger, keyPath, keyDepth+1)
                    found = True
            else:
                keyPathRegistered = True
                found = True
        
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagAutoInit)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagCheckUuid)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagReadAhead)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagFileSystemType)):
                keyPathRegistered = True
                found = True
        
        logger('is-key-path-registered-blinkyfilesystem-done').debug3('isKeyPathRegistered() done. registered=%s. keyPath=%s, keyDepth=%d, I am: from a.storage.disk.tech_storage.tech.storage.disk.system_defaults.file_system.blinky_file_system_gen import BlinkyFileSystem', keyPathRegistered, keyPath, keyDepth)
        return keyPathRegistered

    def prepareMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("prepare-my-blinky-node").debug3Func(): logFunc("prepareMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagCommands)):
            if (self.myCommands):
                for logFunc in self._log("prepare-my-blinky-node-commands-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.myCommands = BlinkyCommands(self._log)
            self.myCommands.setParent(self)
            self.myCommands.setKeyPath(keyPath)
            self.myCommands.setDomain(self.myDomain)

            return self.myCommands
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagTimeouts)):
            if (self.myTimeouts):
                for logFunc in self._log("prepare-my-blinky-node-timeouts-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.myTimeouts = BlinkyTimeouts(self._log)
            self.myTimeouts.setParent(self)
            self.myTimeouts.setKeyPath(keyPath)
            self.myTimeouts.setDomain(self.myDomain)

            return self.myTimeouts
        
        for logFunc in self._log("prepare-my-blinky-not-found").errorFunc():
            logFunc("prepareMyBlinkyNode(): not found, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        return None
    
    def abortMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("abort-my-blinky-node").debug3Func(): logFunc("abortMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        self.deleteMyBlinkyNode(keyPath, keyDepth)
    
    def deleteMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("delete-my-blinky-node").debug3Func(): logFunc("deleteMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagCommands)):
            self.myCommands = None
            return
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagTimeouts)):
            self.myTimeouts = None
            return
        

    def handleTrxElementCreate(self, trxElement, keyDepth, phase):
        for logFunc in self._log("handle-trx-element-create-details").debug3Func():
            logFunc("handleTrxElementCreate(): called, element-key-path=%s, element-op-code=%s, keyDepth=%s, phase=%s",
                   trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase)
        if (self.myIsActive):
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagCommands)):
                if (self.myCreateCommandsFunctor):
                    if (not self.myCommands):
                        for logFunc in self._log("handle-trx-element-create-commands-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): commands not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-commands-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.COMMANDS_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.COMMANDS_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreateCommandsFunctor(phase, self.myCommands)
                    except:
                        for logFunc in self._log("handle-trx-element-create-commands-functor-exception").exceptionFunc():
                            logFunc("Commands's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreateCommandsFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-commands-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): commands functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-commands-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): commands functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagTimeouts)):
                if (self.myCreateTimeoutsFunctor):
                    if (not self.myTimeouts):
                        for logFunc in self._log("handle-trx-element-create-timeouts-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): timeouts not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-timeouts-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.TIMEOUTS_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.TIMEOUTS_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreateTimeoutsFunctor(phase, self.myTimeouts)
                    except:
                        for logFunc in self._log("handle-trx-element-create-timeouts-functor-exception").exceptionFunc():
                            logFunc("Timeouts's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreateTimeoutsFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-timeouts-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): timeouts functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-timeouts-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): timeouts functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
            
            pass
        return ReturnCodes.kOk
    
    def handleTrxElementPrepareBlinkyDelete(self, trxElement, keyDepth):
        for logFunc in self._log("handle-trx-element-prepare-blinky-delete-called").debug2Func():
            logFunc("called: element-key-path=%s, element-op-code=%s, keyDepth=%s",
                    trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth)

        self.notifyDescendantsPrepareBlinkyDelete()

        # if deleted item is a leaf - clear it in the data
        return self.handleTrxElementPrepareBlinkyValueSet(trxElement, keyDepth)

    def notifyDescendantsPrepareBlinkyDelete(self):
        for logFunc in self._log("notify-descendants-prepare-blinky-delete-called").debug2Func(): logFunc("called")

        self.myDomain.registerNodeToProgressNotification(self)

        
        if (self.myCommands):
            self.myCommands.notifyDescendantsPrepareBlinkyDelete()
        
        if (self.myTimeouts):
            self.myTimeouts.notifyDescendantsPrepareBlinkyDelete()
        

        for logFunc in self._log("notify-descendants-prepare-blinky-delete-done").debug2Func(): logFunc("done")

    def handleTrxElementDelete(self, trxElement, keyDepth, phase):
        for logFunc in self._log("handle-trx-element-delete-details").debug3Func():
            logFunc("handleTrxElementDelete(): called, element-key-path=%s, element-op-code=%s, keyDepth=%s, phase=%s",
                   trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase)
        if (self.myIsActive):
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagCommands)):
                res = self.activateDeleteCommandsFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-commands-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): commands functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-commands-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): commands functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                    return ReturnCodes.kGeneralError
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagTimeouts)):
                res = self.activateDeleteTimeoutsFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-timeouts-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): timeouts functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-timeouts-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): timeouts functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                    return ReturnCodes.kGeneralError
            
        # if a leaf is deleted - notify candidate date changed
        return self.notifyWithCandidate(phase)

    
    def removeCommands(self):
        self.myCommands = None

    def activateDeleteCommandsFunctor(self, phase):
        for logFunc in self._log("activate-delete-commands-functor").debug3Func(): logFunc("activateDeleteCommandsFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeleteCommandsFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-commands-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.COMMANDS_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.COMMANDS_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeleteCommandsFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-commands-functor-exception").exceptionFunc():
                        logFunc("Commands's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeleteCommandsFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-commands-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeleteCommandsFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-commands-functor-functor-failed").errorFunc():
                            logFunc("activateDeleteCommandsFunctor(): functor failed, phase=%s", phase)
                    return ReturnCodes.kGeneralError
        return ReturnCodes.kOk
    
    def removeTimeouts(self):
        self.myTimeouts = None

    def activateDeleteTimeoutsFunctor(self, phase):
        for logFunc in self._log("activate-delete-timeouts-functor").debug3Func(): logFunc("activateDeleteTimeoutsFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeleteTimeoutsFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-timeouts-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.TIMEOUTS_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.TIMEOUTS_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeleteTimeoutsFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-timeouts-functor-exception").exceptionFunc():
                        logFunc("Timeouts's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeleteTimeoutsFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-timeouts-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeleteTimeoutsFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-timeouts-functor-functor-failed").errorFunc():
                            logFunc("activateDeleteTimeoutsFunctor(): functor failed, phase=%s", phase)
                    return ReturnCodes.kGeneralError
        return ReturnCodes.kOk
    

    

    def setValueSetFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-value-set-functor-not-active").errorFunc():
                logFunc("setValueSetFunctor(): is illegal when blinky container is active")
        self.myValueSetFunctor = functor
    
    def activateValueSetFunctor(self, phase, data):
        for logFunc in self._log("activate-value-set-functor").debug3Func():
            logFunc("activateValueSetFunctor(): called, myIsActive=%s, phase=%s, data=%s, candidate=%s, running=%s, functor=%s",
                   self.myIsActive, phase, data, self.myCandidateData, self.myRunningData, self.myValueSetFunctor)
        res = ReturnCodes.kOk
        if (self.myIsActive):
            if (self.myValueSetFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-value-set-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.VALUE_SET_FUNCTOR, phase),
                                            self.getFunctorMildTimeoutForPhase(self.VALUE_SET_FUNCTOR, phase))
                try:
                    res = self.myValueSetFunctor(phase, data)
                except:
                    for logFunc in self._log("activate-value-set-functor-functor-exception").exceptionFunc():
                        logFunc("functor raised an exception. phase=%s, data=%s", phase, data)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myValueSetFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-value-set-functor-failed-prepare").noticeFunc():
                            logFunc("activateValueSetFunctor(): functor failed, phase=%s, data=%s, res=%s",
                                   phase, data, res)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-value-set-functor-failed").errorFunc():
                            logFunc("activateValueSetFunctor(): functor failed, phase=%s, data=%s, res=%s",
                                  phase, data, res)
                    return ReturnCodes.kGeneralError
        return res
    
    def notifyWithCandidate(self, phase):
        for logFunc in self._log("notify-with-candidate").debug3Func(): logFunc("notifyWithCandidate(): called, candidate=%s, phase=%s",
                                                              self.myCandidateData, phase)
        return self.activateValueSetFunctor(phase, self.myCandidateData)
    
    def allocMyCandidate(self):
        for logFunc in self._log("alloc-my-candidate").debug3Func():
            logFunc("called")
        self.myCandidateData = FileSystemData()
        
        res = self.setAutoInitDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-autoinit-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setAutoInitDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setCheckUuidDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-checkuuid-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setCheckUuidDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setReadAheadDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-readahead-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setReadAheadDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setFileSystemTypeDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-filesystemtype-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setFileSystemTypeDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        return ReturnCodes.kOk

    def setAutoInitDefaultValue (self, setHas):
        for logFunc in self._log("set-autoinit-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.autoInit = False
            
        if setHas:
            self.myCandidateData.setHasAutoInit()

        return ReturnCodes.kOk

    def setCheckUuidDefaultValue (self, setHas):
        for logFunc in self._log("set-checkuuid-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.checkUuid = False
            
        if setHas:
            self.myCandidateData.setHasCheckUuid()

        return ReturnCodes.kOk

    def setReadAheadDefaultValue (self, setHas):
        for logFunc in self._log("set-readahead-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.readAhead = 0
            
        if setHas:
            self.myCandidateData.setHasReadAhead()

        return ReturnCodes.kOk

    def setFileSystemTypeDefaultValue (self, setHas):
        for logFunc in self._log("set-filesystemtype-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.fileSystemType = FileSystemTypeType.kNone
            
        if setHas:
            self.myCandidateData.setHasFileSystemType()

        return ReturnCodes.kOk

    
    def copyRunningToCandidate(self):
        for logFunc in self._log("copy-running-to-candidate").debug3Func(): logFunc("copyRunningToCandidate(): called, candidate=%s, running=%s",
                                                              self.myCandidateData, self.myRunningData)
        if (self.myCandidateData != None):
            # already coppied - skip
            return

        if (self.myRunningData != None):
            self.myCandidateData = FileSystemData()
            self.myCandidateData.copyFrom(self.myRunningData)
            
        else:
            for logFunc in self._log("copy-running-to-candidate-no-running").debug3Func(): logFunc("copyRunningToCandidate(): myRunningData is None")
            res = self.allocMyCandidate()
            if res != ReturnCodes.kOk:
                for logFunc in self._log("copy-running-to-candidate-alloc-my-candidate-failed").errorFunc(): logFunc("copyRunningToCandidate(): myRunningData is None and allocMyCandidate() failed. aborting")
                a.infra.process.processFatal("copyRunningToCandidate(): myRunningData is None and allocMyCandidate() failed")
    
    def deleteMyCandidate(self):
        for logFunc in self._log("delete-my-candidate").debug3Func(): logFunc("deleteMyCandidate(): called, candidate=%s, running=%s",
                                                     self.myCandidateData, self.myRunningData)
        self.myCandidateData = None
    
    def activateCandidate(self):
        phase=TrxPhase(TrxPhase.kCommit, TrxPhase.kBlinky)
        for logFunc in self._log("activate-candidate").debug3Func(): logFunc("activateCandidate(): called, candidate=%s, running=%s, isPhaseDone()=%s",
                                               self.myCandidateData, self.myRunningData, self.myState.isPhaseDone(phase))
        if (self.myState.isPhaseDone(phase)):
            # running config already updated - skip
            return
        self.myRunningData = FileSystemData()
        self.myRunningData.copyFrom(self.myCandidateData)
        self.myCandidateData = None
        self.myState.setPhaseDone(phase)
        for logFunc in self._log("activate-candidate-done").debug3Func(): logFunc("activateCandidate(): done, candidate=%s, running=%s, isPhaseDone()=%s",
                                                    self.myCandidateData, self.myRunningData, self.myState.isPhaseDone(phase))

    

    

    def getRunningCfgData (self):
        if self.myRunningData:
            return copy.copy(self.myRunningData)
        elif self.myCandidateData:
            # running is not yet initialized. getting the candidate that will soon be running
            return copy.copy(self.myCandidateData)
        for logFunc in self._log("get-running-cfg-data").errorFunc(): logFunc("both running and candidate data are none")
        return None

    def getCandidateCfgData (self):
        if self.myCandidateData:
            # when there is no active transaction, there will be no candidate configuration - give the running instead
            if not self.myRunningData:
                for logFunc in self._log("get-candidate-cfg-data").errorFunc(): logFunc("no running and no candidate")
                return None
            return copy.copy(self.myRunningData)
        else:
            # running is not yet initialized. getting the candidate that will soon be running
            return copy.copy(self.myCandidateData)

    def activateSpecific(self):
        for logFunc in self._log("activate-specific").debug3Func(): logFunc("called")
        if self._actionPointId:
            if not self.actionRegistrationDone:
                
                pass
                
        return ReturnCodes.kOk

    def handleTrxProgressNotificationSpecific (self, progress):
        for logFunc in self._log("handle-trx-progress-notification-specific").debug3Func(): logFunc("called. progress=%s, isInDestroy=%s", progress, self.isInDestroy)
        if progress.isCommitBlinkyBefore() or progress.isAbortBlinkyBefore():
            if self.isInDestroy:
                if self._validationPointId and self.validateRegistrationDone:
                    res = self.myDomain.unregisterValidationPoint(self._validationPointId, self)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-trx-progress-notification-specitic-unregister-validation-point-blinkyfilesystem-failed").errorFunc():
                            logFunc("handleTrxProgressNotificationSpecific(): unregisterValidationPoint(%s) failed, progress=%s",  self._validationPointId, progress)
                        return ReturnCodes.kGeneralError
                if self._actionPointId and self.actionRegistrationDone:
                    res = self.myDomain.unregisterActionPoint(self, self._actionPointId)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-trx-progress-notification-specitic-unregister-action-point-blinkyfilesystem-failed").errorFunc():
                            logFunc("handleTrxProgressNotificationSpecific(): unregisterActionPoint(%s) failed, progress=%s",  self._actionPointId, progress)
                        return ReturnCodes.kGeneralError
        return ReturnCodes.kOk


    def handleInternalDestroy(self, phase):
        __pychecker__ = 'maxreturns=100 maxlines=1000 maxbranches=100'
        for logFunc in self._log("internal-prepare-destroy-helper").debug3Func(): logFunc("handleInternalDestroy(): called, phase=%s", phase)
        res = ReturnCodes.kOk
        self.isInDestroy = True
        if (phase.getConfdPhase() == TrxPhase.kPrepare):
            self.myDomain.registerNodeToProgressNotification(self)
            if (phase.getBlinkyPhase() == TrxPhase.kBlinky):
                
                if (self.myCommands):
                    res = self.myCommands.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-commands-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-commands-recursion-failed-prepare-blinky, phase=%s",
                                  phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myTimeouts):
                    res = self.myTimeouts.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-timeouts-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-timeouts-recursion-failed-prepare-blinky, phase=%s",
                                  phase)
                        return ReturnCodes.kGeneralError
                
                pass
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                 (phase.getBlinkyPhase() == TrxPhase.kPublic):
                res = self.activateDestroySelfFunctor(phase)
                if (res != ReturnCodes.kOk):
                    for logFunc in self._log("handle-internal-destroy-delete-destroy-self-functor-failed-prepare").noticeFunc():
                        logFunc("handleInternalDestroy(): activateDestroySelfFunctor() failed, res=%s, phase=%s",
                               res, phase)
                    self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    return ReturnCodes.kGeneralError
                
                if (self.myCommands):
                    res = self.activateDeleteCommandsFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-commands-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeleteCommandsFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.myCommands):
                    res = self.myCommands.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-commands-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myCommands.handleInternalDestroy() failed, res=%s, phase=%s",
                                   res, phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myTimeouts):
                    res = self.activateDeleteTimeoutsFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-timeouts-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeleteTimeoutsFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.myTimeouts):
                    res = self.myTimeouts.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-timeouts-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myTimeouts.handleInternalDestroy() failed, res=%s, phase=%s",
                                   res, phase)
                        return ReturnCodes.kGeneralError
                
            else:
                for logFunc in self._log("handle-internal-destroy-delete-prepare-illegal-blinky").noticeFunc():
                    logFunc("handleInternalDestroy(): prepare-illegal-blinky, res=%s, phase=%s",
                           res, phase)
                return ReturnCodes.kGeneralError
        elif (phase.getConfdPhase() == TrxPhase.kCommit):
            if (phase.getBlinkyPhase() == TrxPhase.kBlinky):
                
                if (self.myCommands):
                    res = self.myCommands.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-commands-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myCommands.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removeCommands()
                
                if (self.myTimeouts):
                    res = self.myTimeouts.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-timeouts-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myTimeouts.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removeTimeouts()
                
                pass
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                 (phase.getBlinkyPhase() == TrxPhase.kPublic):
                
                if (self.myCommands):
                    res = self.myCommands.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-commands-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myCommands.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteCommandsFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-commands-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteCommandsFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeleteCommandsFunctor failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                
                if (self.myTimeouts):
                    res = self.myTimeouts.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-timeouts-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myTimeouts.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteTimeoutsFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-timeouts-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteTimeoutsFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeleteTimeoutsFunctor failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                
                res = self.activateDestroySelfFunctor(phase)
                if (res != ReturnCodes.kOk):
                    for logFunc in self._log("handle-internal-destroy-delete-destroy-self-functor-failed-commit").errorFunc():
                        logFunc("handleInternalDestroy(): activateDestroySelfFunctor() failed, res=%s, phase=%s",
                              res, phase)
                    a.infra.process.processFatal("destroy self functor failed in commit")
                    return ReturnCodes.kGeneralError
            else:
                for logFunc in self._log("handle-internal-destroy-delete-commit-illegal-blinky").noticeFunc():
                    logFunc("handleInternalDestroy(): commit-illegal-blinky, res=%s, phase=%s",
                           res, phase)
                return ReturnCodes.kGeneralError
        elif (phase.getConfdPhase() == TrxPhase.kAbort):
            if (phase.getBlinkyPhase() == TrxPhase.kBlinky):
                
                if (self.myCommands):
                    res = self.myCommands.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-commands-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myCommands.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myTimeouts):
                    res = self.myTimeouts.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-timeouts-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myTimeouts.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                pass
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                 (phase.getBlinkyPhase() == TrxPhase.kPublic):
                
                if (self.myCommands):
                    res = self.myCommands.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-commands-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myCommands.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.myCommands):
                    res = self.activateDeleteCommandsFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-commands-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteCommandsFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("delete functor failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myTimeouts):
                    res = self.myTimeouts.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-timeouts-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myTimeouts.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.myTimeouts):
                    res = self.activateDeleteTimeoutsFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-timeouts-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteTimeoutsFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("delete functor failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                res = self.activateDestroySelfFunctor(phase)
                if (res != ReturnCodes.kOk):
                    for logFunc in self._log("handle-internal-destroy-activate-destroy-self-functor-failed-abort").errorFunc():
                        logFunc("handleInternalDestroy(): activateDestroySelfFunctor() failed, res=%s, phase=%s",
                              res, phase)
                    a.infra.process.processFatal("destroy self functor failed in abort")
                    return ReturnCodes.kOk
            else:
                for logFunc in self._log("handle-internal-destroy-delete-abort-illegal-blinky").noticeFunc():
                    logFunc("handleInternalDestroy(): abort-illegal-blinky, res=%s, phase=%s", res, phase)
                return ReturnCodes.kGeneralError
        else:
            for logFunc in self._log("handle-internal-destroy-delete-illegal-confd").noticeFunc():
                logFunc("handleInternalDestroy(): illegal-confd, res=%s, phase=%s", res, phase)
            return ReturnCodes.kGeneralError
    
        return ReturnCodes.kOk
    
"""
Extracted from the below data: 
{
    "node": {
        "dataImportStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.system_defaults.file_system.file_system_data_gen import FileSystemData", 
        "moduleYangNamespacePrefix": "qt-strg-dsk", 
        "validationPoint": null, 
        "yangName": "file-system", 
        "namespace": "file_system", 
        "logGroupName": "blinky-file-system", 
        "className": "BlinkyFileSystem", 
        "logModuleName": "a-storage-disk-tech-storage-tech-storage-disk-system-defaults-file-system-blinky-file-system-gen", 
        "importStatement": "from a.storage.disk.tech_storage.tech.storage.disk.system_defaults.file_system.blinky_file_system_gen import BlinkyFileSystem", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
        "dataClassName": "FileSystemData", 
        "actionPoint": null
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
            "moduleYangNamespacePrefix": "qt-strg", 
            "yangName": "storage", 
            "namespace": "storage", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage", 
            "name": "storage"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "isCurrent": false, 
            "yangName": "disk", 
            "namespace": "disk", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "keyLeaf": {
                "varName": "disk", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "disk"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "name": "system-defaults"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "yangName": "file-system", 
            "namespace": "file_system", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "name": "file-system"
        }
    ], 
    "descendants": [
        {
            "className": "BlinkyCommands", 
            "memberName": "Commands", 
            "yangName": "commands", 
            "importStatement": "from a.storage.disk.tech_storage.tech.storage.disk.system_defaults.file_system.commands.blinky_commands_gen import BlinkyCommands"
        }, 
        {
            "className": "BlinkyTimeouts", 
            "memberName": "Timeouts", 
            "yangName": "timeouts", 
            "importStatement": "from a.storage.disk.tech_storage.tech.storage.disk.system_defaults.file_system.timeouts.blinky_timeouts_gen import BlinkyTimeouts"
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "autoInit", 
            "yangName": "auto-init", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "checkUuid", 
            "yangName": "check-uuid", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "readAhead", 
            "yangName": "read-ahead", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "fileSystemType", 
            "yangName": "file-system-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "none", 
            "hasDefaultRef": false
        }
    ], 
    "module": {}, 
    "env": [
        "a", 
        "storage", 
        "disk", 
        "tech_storage"
    ], 
    "createTime": "2013"
}
"""

