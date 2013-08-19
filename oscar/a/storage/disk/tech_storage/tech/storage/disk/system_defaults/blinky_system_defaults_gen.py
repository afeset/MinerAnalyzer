


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

from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.system_defaults.system_defaults_data_gen import SystemDefaultsData


from a.storage.disk.tech_storage.tech.storage.disk.system_defaults.raid_array.blinky_raid_array_gen import BlinkyRaidArray

from a.storage.disk.tech_storage.tech.storage.disk.system_defaults.file_system.blinky_file_system_gen import BlinkyFileSystem

from a.storage.disk.tech_storage.tech.storage.disk.system_defaults.physical.blinky_physical_gen import BlinkyPhysical


from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import DiskTypesType
from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import DiskFunctionalTypesType


class BlinkySystemDefaults(BlinkyContainer):
    ourNamespace="http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"
    #leaves
    
    ourXmlTagDiskType="disk-type"
    
    ourXmlTagEnabled="enabled"
    
    ourXmlTagFunctionalType="functional-type"
    
    ourXmlTagStorageModule="storage-module"
    
    ourXmlTagTmpForceInit="tmp-force-init"
    

    #descendants
    
    ourXmlTagRaidArray="raid-array"
    
    ourXmlTagFileSystem="file-system"
    
    ourXmlTagPhysical="physical"
    

    _validationPointId=None
    
    _actionPointId=None
    

    
    RAIDARRAY_CREATE_FUNCTOR = 'RAIDARRAY_CREATE_FUNCTOR'
    RAIDARRAY_DELETE_FUNCTOR = 'RAIDARRAY_DELETE_FUNCTOR'
    
    FILESYSTEM_CREATE_FUNCTOR = 'FILESYSTEM_CREATE_FUNCTOR'
    FILESYSTEM_DELETE_FUNCTOR = 'FILESYSTEM_DELETE_FUNCTOR'
    
    PHYSICAL_CREATE_FUNCTOR = 'PHYSICAL_CREATE_FUNCTOR'
    PHYSICAL_DELETE_FUNCTOR = 'PHYSICAL_DELETE_FUNCTOR'
    
    VALUE_SET_FUNCTOR = 'VALUE_SET_FUNCTOR'
    VALIDATE_TRX_FUNCTOR = 'VALIDATE_TRX_FUNCTOR'
    DO_ACTION_FUNCTOR = 'DO_ACTION_FUNCTOR'

    # Improve performance: Store hashed values of these strings here as well.

    def __init__ (self, logger):
        BlinkyContainer.__init__(self, logger)
        
        self.myCreateRaidArrayFunctor=None
        self.myDeleteRaidArrayFunctor=None
        self.myRaidArray=None
        
        self.myCreateFileSystemFunctor=None
        self.myDeleteFileSystemFunctor=None
        self.myFileSystem=None
        
        self.myCreatePhysicalFunctor=None
        self.myDeletePhysicalFunctor=None
        self.myPhysical=None
        
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

        logger('s-create-blinkysystemdefaults').info('called. domain=%s, _validationPointId=%s, _actionPointId=%s', domain, BlinkySystemDefaults._validationPointId, BlinkySystemDefaults._actionPointId)

        confd_key=KeyPath()
        
        
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
        
        newNode=BlinkySystemDefaults(logger)
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

    
    def setCreateRaidArrayFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-raid-array-functor-active").errorFunc():
                logFunc("setCreateRaidArrayFunctor() is illegal when blinky node is active")
        self.myCreateRaidArrayFunctor = functor

    def setDeleteRaidArrayFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-raid-array-functor-active").errorFunc():
                logFunc("setDeleteRaidArrayFunctor() is illegal when blinky node is active")
        self.myDeleteRaidArrayFunctor = functor
    
    def setCreateFileSystemFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-file-system-functor-active").errorFunc():
                logFunc("setCreateFileSystemFunctor() is illegal when blinky node is active")
        self.myCreateFileSystemFunctor = functor

    def setDeleteFileSystemFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-file-system-functor-active").errorFunc():
                logFunc("setDeleteFileSystemFunctor() is illegal when blinky node is active")
        self.myDeleteFileSystemFunctor = functor
    
    def setCreatePhysicalFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-physical-functor-active").errorFunc():
                logFunc("setCreatePhysicalFunctor() is illegal when blinky node is active")
        self.myCreatePhysicalFunctor = functor

    def setDeletePhysicalFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-physical-functor-active").errorFunc():
                logFunc("setDeletePhysicalFunctor() is illegal when blinky node is active")
        self.myDeletePhysicalFunctor = functor
    

    

    

    def trxElementUpdateCandidate(self, trxElement, keyDepth):
        keyPath = trxElement.getKeyPath()
        for logFunc in self._log("trx-element-update-candidate").debug3Func():
            logFunc("trxElementUpdateCandidate(): called, keyPath=%s, keyDepth=%s, trxElement=%s", keyPath, keyDepth, trxElement)
        
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagDiskType)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                if not DiskTypesType.isValidValue(newValue.asEnum()):
                    self._log("trx-element-update-candidate-illegal-enum-disktype-failed")\
                        .error("illegal enum value %s for diskType", newValue.asEnum())
                    return ReturnCodes.kGeneralError
                self.myCandidateData.diskType = DiskTypesType.getByValue(newValue.asEnum())
                self.myCandidateData.setHasDiskType()
                
            else:
                self.setDiskTypeDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagEnabled)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.enabled = newValue.asBool()
                self.myCandidateData.setHasEnabled()
                
            else:
                self.setEnabledDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagFunctionalType)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                if not DiskFunctionalTypesType.isValidValue(newValue.asEnum()):
                    self._log("trx-element-update-candidate-illegal-enum-functionaltype-failed")\
                        .error("illegal enum value %s for functionalType", newValue.asEnum())
                    return ReturnCodes.kGeneralError
                self.myCandidateData.functionalType = DiskFunctionalTypesType.getByValue(newValue.asEnum())
                self.myCandidateData.setHasFunctionalType()
                
            else:
                self.setFunctionalTypeDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagStorageModule)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.storageModule = newValue.asString()
                self.myCandidateData.setHasStorageModule()
                
            else:
                self.setStorageModuleDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagTmpForceInit)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.tmpForceInit = newValue.asBool()
                self.myCandidateData.setHasTmpForceInit()
                
            else:
                self.setTmpForceInitDefaultValue(True)
            
        for logFunc in self._log("trx-element-update-candidate-done").debug3Func():
            logFunc("trxElementUpdateCandidate(): After update, candidate is %s", self.myCandidateData)
    
    def getDescendant(self, keyPath, keyDepth_PBR):
        for logFunc in self._log("get-descendant").debug3Func(): logFunc("getDescendant(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth_PBR)
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagRaidArray)):
            return self.myRaidArray
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagFileSystem)):
            return self.myFileSystem
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagPhysical)):
            return self.myPhysical
        
        for logFunc in self._log("get-descendant-unknown").debug3Func(): logFunc("getDescendant(): unknown, keyPath=%s, keyDepth=%s", keyPath, keyDepth_PBR)
        return None
    
    @classmethod
    def isKeyPathRegistered (cls, logger, keyPath, keyDepth):
        __pychecker__="no-argsused no-local"
        logger('is-key-path-registered-blinkysystemdefaults').debug3('isKeyPathRegistered() called. keyPath=%s, keyDepth=%d, I am: from a.storage.disk.tech_storage.tech.storage.disk.system_defaults.blinky_system_defaults_gen import BlinkySystemDefaults', keyPath, keyDepth)
        keyPathRegistered = False
        found = False
        
        if not found:
            if keyPath.getLen() > keyDepth+1:
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagRaidArray)):
                    keyPathRegistered = BlinkyRaidArray.isKeyPathRegistered(logger, keyPath, keyDepth+1)
                    found = True
            else:
                keyPathRegistered = True
                found = True
        
        if not found:
            if keyPath.getLen() > keyDepth+1:
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagFileSystem)):
                    keyPathRegistered = BlinkyFileSystem.isKeyPathRegistered(logger, keyPath, keyDepth+1)
                    found = True
            else:
                keyPathRegistered = True
                found = True
        
        if not found:
            if keyPath.getLen() > keyDepth+1:
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagPhysical)):
                    keyPathRegistered = BlinkyPhysical.isKeyPathRegistered(logger, keyPath, keyDepth+1)
                    found = True
            else:
                keyPathRegistered = True
                found = True
        
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagDiskType)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagEnabled)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagFunctionalType)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagStorageModule)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagTmpForceInit)):
                keyPathRegistered = True
                found = True
        
        logger('is-key-path-registered-blinkysystemdefaults-done').debug3('isKeyPathRegistered() done. registered=%s. keyPath=%s, keyDepth=%d, I am: from a.storage.disk.tech_storage.tech.storage.disk.system_defaults.blinky_system_defaults_gen import BlinkySystemDefaults', keyPathRegistered, keyPath, keyDepth)
        return keyPathRegistered

    def prepareMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("prepare-my-blinky-node").debug3Func(): logFunc("prepareMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagRaidArray)):
            if (self.myRaidArray):
                for logFunc in self._log("prepare-my-blinky-node-raidarray-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.myRaidArray = BlinkyRaidArray(self._log)
            self.myRaidArray.setParent(self)
            self.myRaidArray.setKeyPath(keyPath)
            self.myRaidArray.setDomain(self.myDomain)

            return self.myRaidArray
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagFileSystem)):
            if (self.myFileSystem):
                for logFunc in self._log("prepare-my-blinky-node-filesystem-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.myFileSystem = BlinkyFileSystem(self._log)
            self.myFileSystem.setParent(self)
            self.myFileSystem.setKeyPath(keyPath)
            self.myFileSystem.setDomain(self.myDomain)

            return self.myFileSystem
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagPhysical)):
            if (self.myPhysical):
                for logFunc in self._log("prepare-my-blinky-node-physical-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.myPhysical = BlinkyPhysical(self._log)
            self.myPhysical.setParent(self)
            self.myPhysical.setKeyPath(keyPath)
            self.myPhysical.setDomain(self.myDomain)

            return self.myPhysical
        
        for logFunc in self._log("prepare-my-blinky-not-found").errorFunc():
            logFunc("prepareMyBlinkyNode(): not found, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        return None
    
    def abortMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("abort-my-blinky-node").debug3Func(): logFunc("abortMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        self.deleteMyBlinkyNode(keyPath, keyDepth)
    
    def deleteMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("delete-my-blinky-node").debug3Func(): logFunc("deleteMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagRaidArray)):
            self.myRaidArray = None
            return
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagFileSystem)):
            self.myFileSystem = None
            return
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagPhysical)):
            self.myPhysical = None
            return
        

    def handleTrxElementCreate(self, trxElement, keyDepth, phase):
        for logFunc in self._log("handle-trx-element-create-details").debug3Func():
            logFunc("handleTrxElementCreate(): called, element-key-path=%s, element-op-code=%s, keyDepth=%s, phase=%s",
                   trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase)
        if (self.myIsActive):
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagRaidArray)):
                if (self.myCreateRaidArrayFunctor):
                    if (not self.myRaidArray):
                        for logFunc in self._log("handle-trx-element-create-raidarray-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): raidarray not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-raidarray-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.RAIDARRAY_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.RAIDARRAY_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreateRaidArrayFunctor(phase, self.myRaidArray)
                    except:
                        for logFunc in self._log("handle-trx-element-create-raidarray-functor-exception").exceptionFunc():
                            logFunc("RaidArray's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreateRaidArrayFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-raidarray-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): raidarray functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-raidarray-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): raidarray functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagFileSystem)):
                if (self.myCreateFileSystemFunctor):
                    if (not self.myFileSystem):
                        for logFunc in self._log("handle-trx-element-create-filesystem-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): filesystem not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-filesystem-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.FILESYSTEM_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.FILESYSTEM_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreateFileSystemFunctor(phase, self.myFileSystem)
                    except:
                        for logFunc in self._log("handle-trx-element-create-filesystem-functor-exception").exceptionFunc():
                            logFunc("FileSystem's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreateFileSystemFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-filesystem-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): filesystem functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-filesystem-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): filesystem functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagPhysical)):
                if (self.myCreatePhysicalFunctor):
                    if (not self.myPhysical):
                        for logFunc in self._log("handle-trx-element-create-physical-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): physical not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-physical-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.PHYSICAL_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.PHYSICAL_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreatePhysicalFunctor(phase, self.myPhysical)
                    except:
                        for logFunc in self._log("handle-trx-element-create-physical-functor-exception").exceptionFunc():
                            logFunc("Physical's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreatePhysicalFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-physical-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): physical functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-physical-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): physical functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
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

        
        if (self.myRaidArray):
            self.myRaidArray.notifyDescendantsPrepareBlinkyDelete()
        
        if (self.myFileSystem):
            self.myFileSystem.notifyDescendantsPrepareBlinkyDelete()
        
        if (self.myPhysical):
            self.myPhysical.notifyDescendantsPrepareBlinkyDelete()
        

        for logFunc in self._log("notify-descendants-prepare-blinky-delete-done").debug2Func(): logFunc("done")

    def handleTrxElementDelete(self, trxElement, keyDepth, phase):
        for logFunc in self._log("handle-trx-element-delete-details").debug3Func():
            logFunc("handleTrxElementDelete(): called, element-key-path=%s, element-op-code=%s, keyDepth=%s, phase=%s",
                   trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase)
        if (self.myIsActive):
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagRaidArray)):
                res = self.activateDeleteRaidArrayFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-raidarray-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): raidarray functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-raidarray-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): raidarray functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                    return ReturnCodes.kGeneralError
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagFileSystem)):
                res = self.activateDeleteFileSystemFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-filesystem-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): filesystem functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-filesystem-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): filesystem functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                    return ReturnCodes.kGeneralError
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagPhysical)):
                res = self.activateDeletePhysicalFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-physical-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): physical functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-physical-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): physical functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                    return ReturnCodes.kGeneralError
            
        # if a leaf is deleted - notify candidate date changed
        return self.notifyWithCandidate(phase)

    
    def removeRaidArray(self):
        self.myRaidArray = None

    def activateDeleteRaidArrayFunctor(self, phase):
        for logFunc in self._log("activate-delete-raidarray-functor").debug3Func(): logFunc("activateDeleteRaidArrayFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeleteRaidArrayFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-raidarray-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.RAIDARRAY_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.RAIDARRAY_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeleteRaidArrayFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-raidarray-functor-exception").exceptionFunc():
                        logFunc("RaidArray's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeleteRaidArrayFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-raidarray-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeleteRaidArrayFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-raidarray-functor-functor-failed").errorFunc():
                            logFunc("activateDeleteRaidArrayFunctor(): functor failed, phase=%s", phase)
                    return ReturnCodes.kGeneralError
        return ReturnCodes.kOk
    
    def removeFileSystem(self):
        self.myFileSystem = None

    def activateDeleteFileSystemFunctor(self, phase):
        for logFunc in self._log("activate-delete-filesystem-functor").debug3Func(): logFunc("activateDeleteFileSystemFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeleteFileSystemFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-filesystem-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.FILESYSTEM_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.FILESYSTEM_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeleteFileSystemFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-filesystem-functor-exception").exceptionFunc():
                        logFunc("FileSystem's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeleteFileSystemFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-filesystem-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeleteFileSystemFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-filesystem-functor-functor-failed").errorFunc():
                            logFunc("activateDeleteFileSystemFunctor(): functor failed, phase=%s", phase)
                    return ReturnCodes.kGeneralError
        return ReturnCodes.kOk
    
    def removePhysical(self):
        self.myPhysical = None

    def activateDeletePhysicalFunctor(self, phase):
        for logFunc in self._log("activate-delete-physical-functor").debug3Func(): logFunc("activateDeletePhysicalFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeletePhysicalFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-physical-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.PHYSICAL_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.PHYSICAL_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeletePhysicalFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-physical-functor-exception").exceptionFunc():
                        logFunc("Physical's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeletePhysicalFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-physical-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeletePhysicalFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-physical-functor-functor-failed").errorFunc():
                            logFunc("activateDeletePhysicalFunctor(): functor failed, phase=%s", phase)
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
        self.myCandidateData = SystemDefaultsData()
        
        res = self.setDiskTypeDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-disktype-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setDiskTypeDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setEnabledDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-enabled-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setEnabledDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setFunctionalTypeDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-functionaltype-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setFunctionalTypeDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setStorageModuleDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-storagemodule-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setStorageModuleDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setTmpForceInitDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-tmpforceinit-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setTmpForceInitDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        return ReturnCodes.kOk

    def setDiskTypeDefaultValue (self, setHas):
        for logFunc in self._log("set-disktype-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.diskType = DiskTypesType.kRaid0Disk
            
        if setHas:
            self.myCandidateData.setHasDiskType()

        return ReturnCodes.kOk

    def setEnabledDefaultValue (self, setHas):
        for logFunc in self._log("set-enabled-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.enabled = False
            
        if setHas:
            self.myCandidateData.setHasEnabled()

        return ReturnCodes.kOk

    def setFunctionalTypeDefaultValue (self, setHas):
        for logFunc in self._log("set-functionaltype-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.functionalType = DiskFunctionalTypesType.kContent
            
        if setHas:
            self.myCandidateData.setHasFunctionalType()

        return ReturnCodes.kOk

    def setStorageModuleDefaultValue (self, setHas):
        for logFunc in self._log("set-storagemodule-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.storageModule = ""
            
        if setHas:
            self.myCandidateData.setHasStorageModule()

        return ReturnCodes.kOk

    def setTmpForceInitDefaultValue (self, setHas):
        for logFunc in self._log("set-tmpforceinit-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.tmpForceInit = False
            
        if setHas:
            self.myCandidateData.setHasTmpForceInit()

        return ReturnCodes.kOk

    
    def copyRunningToCandidate(self):
        for logFunc in self._log("copy-running-to-candidate").debug3Func(): logFunc("copyRunningToCandidate(): called, candidate=%s, running=%s",
                                                              self.myCandidateData, self.myRunningData)
        if (self.myCandidateData != None):
            # already coppied - skip
            return

        if (self.myRunningData != None):
            self.myCandidateData = SystemDefaultsData()
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
        self.myRunningData = SystemDefaultsData()
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
                        for logFunc in self._log("handle-trx-progress-notification-specitic-unregister-validation-point-blinkysystemdefaults-failed").errorFunc():
                            logFunc("handleTrxProgressNotificationSpecific(): unregisterValidationPoint(%s) failed, progress=%s",  self._validationPointId, progress)
                        return ReturnCodes.kGeneralError
                if self._actionPointId and self.actionRegistrationDone:
                    res = self.myDomain.unregisterActionPoint(self, self._actionPointId)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-trx-progress-notification-specitic-unregister-action-point-blinkysystemdefaults-failed").errorFunc():
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
                
                if (self.myRaidArray):
                    res = self.myRaidArray.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-raidarray-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-raidarray-recursion-failed-prepare-blinky, phase=%s",
                                  phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myFileSystem):
                    res = self.myFileSystem.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-filesystem-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-filesystem-recursion-failed-prepare-blinky, phase=%s",
                                  phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myPhysical):
                    res = self.myPhysical.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-physical-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-physical-recursion-failed-prepare-blinky, phase=%s",
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
                
                if (self.myRaidArray):
                    res = self.activateDeleteRaidArrayFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-raidarray-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeleteRaidArrayFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.myRaidArray):
                    res = self.myRaidArray.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-raidarray-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myRaidArray.handleInternalDestroy() failed, res=%s, phase=%s",
                                   res, phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myFileSystem):
                    res = self.activateDeleteFileSystemFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-filesystem-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeleteFileSystemFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.myFileSystem):
                    res = self.myFileSystem.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-filesystem-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myFileSystem.handleInternalDestroy() failed, res=%s, phase=%s",
                                   res, phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myPhysical):
                    res = self.activateDeletePhysicalFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-physical-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeletePhysicalFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.myPhysical):
                    res = self.myPhysical.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-physical-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myPhysical.handleInternalDestroy() failed, res=%s, phase=%s",
                                   res, phase)
                        return ReturnCodes.kGeneralError
                
            else:
                for logFunc in self._log("handle-internal-destroy-delete-prepare-illegal-blinky").noticeFunc():
                    logFunc("handleInternalDestroy(): prepare-illegal-blinky, res=%s, phase=%s",
                           res, phase)
                return ReturnCodes.kGeneralError
        elif (phase.getConfdPhase() == TrxPhase.kCommit):
            if (phase.getBlinkyPhase() == TrxPhase.kBlinky):
                
                if (self.myRaidArray):
                    res = self.myRaidArray.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-raidarray-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myRaidArray.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removeRaidArray()
                
                if (self.myFileSystem):
                    res = self.myFileSystem.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-filesystem-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myFileSystem.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removeFileSystem()
                
                if (self.myPhysical):
                    res = self.myPhysical.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-physical-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myPhysical.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removePhysical()
                
                pass
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                 (phase.getBlinkyPhase() == TrxPhase.kPublic):
                
                if (self.myRaidArray):
                    res = self.myRaidArray.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-raidarray-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myRaidArray.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteRaidArrayFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-raidarray-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteRaidArrayFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeleteRaidArrayFunctor failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                
                if (self.myFileSystem):
                    res = self.myFileSystem.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-filesystem-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myFileSystem.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteFileSystemFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-filesystem-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteFileSystemFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeleteFileSystemFunctor failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                
                if (self.myPhysical):
                    res = self.myPhysical.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-physical-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myPhysical.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeletePhysicalFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-physical-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeletePhysicalFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeletePhysicalFunctor failed in commit phase (private/public)")
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
                
                if (self.myRaidArray):
                    res = self.myRaidArray.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-raidarray-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myRaidArray.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myFileSystem):
                    res = self.myFileSystem.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-filesystem-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myFileSystem.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myPhysical):
                    res = self.myPhysical.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-physical-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myPhysical.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                pass
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                 (phase.getBlinkyPhase() == TrxPhase.kPublic):
                
                if (self.myRaidArray):
                    res = self.myRaidArray.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-raidarray-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myRaidArray.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.myRaidArray):
                    res = self.activateDeleteRaidArrayFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-raidarray-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteRaidArrayFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("delete functor failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myFileSystem):
                    res = self.myFileSystem.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-filesystem-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myFileSystem.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.myFileSystem):
                    res = self.activateDeleteFileSystemFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-filesystem-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteFileSystemFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("delete functor failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myPhysical):
                    res = self.myPhysical.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-physical-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myPhysical.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.myPhysical):
                    res = self.activateDeletePhysicalFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-physical-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeletePhysicalFunctor() failed, res=%s, phase=%s",
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
        "dataImportStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.system_defaults.system_defaults_data_gen import SystemDefaultsData", 
        "moduleYangNamespacePrefix": "qt-strg-dsk", 
        "validationPoint": null, 
        "yangName": "system-defaults", 
        "namespace": "system_defaults", 
        "logGroupName": "blinky-system-defaults", 
        "className": "BlinkySystemDefaults", 
        "logModuleName": "a-storage-disk-tech-storage-tech-storage-disk-system-defaults-blinky-system-defaults-gen", 
        "importStatement": "from a.storage.disk.tech_storage.tech.storage.disk.system_defaults.blinky_system_defaults_gen import BlinkySystemDefaults", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
        "dataClassName": "SystemDefaultsData", 
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
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "name": "system-defaults"
        }
    ], 
    "descendants": [
        {
            "className": "BlinkyRaidArray", 
            "memberName": "RaidArray", 
            "yangName": "raid-array", 
            "importStatement": "from a.storage.disk.tech_storage.tech.storage.disk.system_defaults.raid_array.blinky_raid_array_gen import BlinkyRaidArray"
        }, 
        {
            "className": "BlinkyFileSystem", 
            "memberName": "FileSystem", 
            "yangName": "file-system", 
            "importStatement": "from a.storage.disk.tech_storage.tech.storage.disk.system_defaults.file_system.blinky_file_system_gen import BlinkyFileSystem"
        }, 
        {
            "className": "BlinkyPhysical", 
            "memberName": "Physical", 
            "yangName": "physical", 
            "importStatement": "from a.storage.disk.tech_storage.tech.storage.disk.system_defaults.physical.blinky_physical_gen import BlinkyPhysical"
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "diskType", 
            "yangName": "disk-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "raid0-disk", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "functionalType", 
            "yangName": "functional-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "content", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "storageModule", 
            "yangName": "storage-module", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "tmpForceInit", 
            "yangName": "tmp-force-init", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
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

