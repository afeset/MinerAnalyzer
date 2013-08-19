


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

from status_maapi_base_gen import StatusMaapiBase


from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import RaidArrayStatusType
from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import RaidArrayStateType


class BlinkyStatusMaapi(StatusMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-status")
        self.domain = None

        

        
        self.physicalIdListRequested = False
        self.physicalIdList = None
        self.physicalIdListSet = False
        
        self.statusRequested = False
        self.status = None
        self.statusSet = False
        
        self.stateRawRequested = False
        self.stateRaw = None
        self.stateRawSet = False
        
        self.readPolicyRequested = False
        self.readPolicy = None
        self.readPolicySet = False
        
        self.badBlocksRequested = False
        self.badBlocks = None
        self.badBlocksSet = False
        
        self.mediaTypeRequested = False
        self.mediaType = None
        self.mediaTypeSet = False
        
        self.hotSparePolicyViolationRequested = False
        self.hotSparePolicyViolation = None
        self.hotSparePolicyViolationSet = False
        
        self.idRequested = False
        self.id = None
        self.idSet = False
        
        self.stateRequested = False
        self.state = None
        self.stateSet = False
        
        self.statusRawRequested = False
        self.statusRaw = None
        self.statusRawSet = False
        
        self.diskCachePolicyRequested = False
        self.diskCachePolicy = None
        self.diskCachePolicySet = False
        
        self.badBlocksRawRequested = False
        self.badBlocksRaw = None
        self.badBlocksRawSet = False
        
        self.cachePolicyRequested = False
        self.cachePolicy = None
        self.cachePolicySet = False
        
        self.writePolicyRequested = False
        self.writePolicy = None
        self.writePolicySet = False
        
        self.raidTypeRequested = False
        self.raidType = None
        self.raidTypeSet = False
        
        self.stripeElementSizeRequested = False
        self.stripeElementSize = None
        self.stripeElementSizeSet = False
        
        self.sizeRawRequested = False
        self.sizeRaw = None
        self.sizeRawSet = False
        
        self.sizeRequested = False
        self.size = None
        self.sizeSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestPhysicalIdList(True)
        
        self.requestStatus(True)
        
        self.requestStateRaw(True)
        
        self.requestReadPolicy(True)
        
        self.requestBadBlocks(True)
        
        self.requestMediaType(True)
        
        self.requestHotSparePolicyViolation(True)
        
        self.requestId(True)
        
        self.requestState(True)
        
        self.requestStatusRaw(True)
        
        self.requestDiskCachePolicy(True)
        
        self.requestBadBlocksRaw(True)
        
        self.requestCachePolicy(True)
        
        self.requestWritePolicy(True)
        
        self.requestRaidType(True)
        
        self.requestStripeElementSize(True)
        
        self.requestSizeRaw(True)
        
        self.requestSize(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestPhysicalIdList(False)
        
        self.requestStatus(False)
        
        self.requestStateRaw(False)
        
        self.requestReadPolicy(False)
        
        self.requestBadBlocks(False)
        
        self.requestMediaType(False)
        
        self.requestHotSparePolicyViolation(False)
        
        self.requestId(False)
        
        self.requestState(False)
        
        self.requestStatusRaw(False)
        
        self.requestDiskCachePolicy(False)
        
        self.requestBadBlocksRaw(False)
        
        self.requestCachePolicy(False)
        
        self.requestWritePolicy(False)
        
        self.requestRaidType(False)
        
        self.requestStripeElementSize(False)
        
        self.requestSizeRaw(False)
        
        self.requestSize(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestPhysicalIdList(True)
        
        self.requestStatus(True)
        
        self.requestStateRaw(True)
        
        self.requestReadPolicy(True)
        
        self.requestBadBlocks(True)
        
        self.requestMediaType(True)
        
        self.requestHotSparePolicyViolation(True)
        
        self.requestId(True)
        
        self.requestState(True)
        
        self.requestStatusRaw(True)
        
        self.requestDiskCachePolicy(True)
        
        self.requestBadBlocksRaw(True)
        
        self.requestCachePolicy(True)
        
        self.requestWritePolicy(True)
        
        self.requestRaidType(True)
        
        self.requestStripeElementSize(True)
        
        self.requestSizeRaw(True)
        
        self.requestSize(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestPhysicalIdList(False)
        
        self.requestStatus(False)
        
        self.requestStateRaw(False)
        
        self.requestReadPolicy(False)
        
        self.requestBadBlocks(False)
        
        self.requestMediaType(False)
        
        self.requestHotSparePolicyViolation(False)
        
        self.requestId(False)
        
        self.requestState(False)
        
        self.requestStatusRaw(False)
        
        self.requestDiskCachePolicy(False)
        
        self.requestBadBlocksRaw(False)
        
        self.requestCachePolicy(False)
        
        self.requestWritePolicy(False)
        
        self.requestRaidType(False)
        
        self.requestStripeElementSize(False)
        
        self.requestSizeRaw(False)
        
        self.requestSize(False)
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        

    def write (self
              , disk
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(disk, trxContext)

    def read (self
              , disk
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(disk, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , disk
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(disk, 
                                  True,
                                  trxContext)



    def requestPhysicalIdList (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-physicalidlist').debug3Func(): logFunc('called. requested=%s', requested)
        self.physicalIdListRequested = requested
        self.physicalIdListSet = False

    def isPhysicalIdListRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-physicalidlist-requested').debug3Func(): logFunc('called. requested=%s', self.physicalIdListRequested)
        return self.physicalIdListRequested

    def getPhysicalIdList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-physicalidlist').debug3Func(): logFunc('called. self.physicalIdListSet=%s, self.physicalIdList=%s', self.physicalIdListSet, self.physicalIdList)
        if self.physicalIdListSet:
            return self.physicalIdList
        return None

    def hasPhysicalIdList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-physicalidlist').debug3Func(): logFunc('called. self.physicalIdListSet=%s, self.physicalIdList=%s', self.physicalIdListSet, self.physicalIdList)
        if self.physicalIdListSet:
            return True
        return False

    def setPhysicalIdList (self, physicalIdList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-physicalidlist').debug3Func(): logFunc('called. physicalIdList=%s, old=%s', physicalIdList, self.physicalIdList)
        self.physicalIdListSet = True
        self.physicalIdList = physicalIdList

    def requestStatus (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-status').debug3Func(): logFunc('called. requested=%s', requested)
        self.statusRequested = requested
        self.statusSet = False

    def isStatusRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-status-requested').debug3Func(): logFunc('called. requested=%s', self.statusRequested)
        return self.statusRequested

    def getStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-status').debug3Func(): logFunc('called. self.statusSet=%s, self.status=%s', self.statusSet, self.status)
        if self.statusSet:
            return self.status
        return None

    def hasStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-status').debug3Func(): logFunc('called. self.statusSet=%s, self.status=%s', self.statusSet, self.status)
        if self.statusSet:
            return True
        return False

    def setStatus (self, status):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-status').debug3Func(): logFunc('called. status=%s, old=%s', status, self.status)
        self.statusSet = True
        self.status = status

    def requestStateRaw (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-stateraw').debug3Func(): logFunc('called. requested=%s', requested)
        self.stateRawRequested = requested
        self.stateRawSet = False

    def isStateRawRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-stateraw-requested').debug3Func(): logFunc('called. requested=%s', self.stateRawRequested)
        return self.stateRawRequested

    def getStateRaw (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-stateraw').debug3Func(): logFunc('called. self.stateRawSet=%s, self.stateRaw=%s', self.stateRawSet, self.stateRaw)
        if self.stateRawSet:
            return self.stateRaw
        return None

    def hasStateRaw (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-stateraw').debug3Func(): logFunc('called. self.stateRawSet=%s, self.stateRaw=%s', self.stateRawSet, self.stateRaw)
        if self.stateRawSet:
            return True
        return False

    def setStateRaw (self, stateRaw):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-stateraw').debug3Func(): logFunc('called. stateRaw=%s, old=%s', stateRaw, self.stateRaw)
        self.stateRawSet = True
        self.stateRaw = stateRaw

    def requestReadPolicy (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-readpolicy').debug3Func(): logFunc('called. requested=%s', requested)
        self.readPolicyRequested = requested
        self.readPolicySet = False

    def isReadPolicyRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-readpolicy-requested').debug3Func(): logFunc('called. requested=%s', self.readPolicyRequested)
        return self.readPolicyRequested

    def getReadPolicy (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-readpolicy').debug3Func(): logFunc('called. self.readPolicySet=%s, self.readPolicy=%s', self.readPolicySet, self.readPolicy)
        if self.readPolicySet:
            return self.readPolicy
        return None

    def hasReadPolicy (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-readpolicy').debug3Func(): logFunc('called. self.readPolicySet=%s, self.readPolicy=%s', self.readPolicySet, self.readPolicy)
        if self.readPolicySet:
            return True
        return False

    def setReadPolicy (self, readPolicy):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-readpolicy').debug3Func(): logFunc('called. readPolicy=%s, old=%s', readPolicy, self.readPolicy)
        self.readPolicySet = True
        self.readPolicy = readPolicy

    def requestBadBlocks (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-badblocks').debug3Func(): logFunc('called. requested=%s', requested)
        self.badBlocksRequested = requested
        self.badBlocksSet = False

    def isBadBlocksRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-badblocks-requested').debug3Func(): logFunc('called. requested=%s', self.badBlocksRequested)
        return self.badBlocksRequested

    def getBadBlocks (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-badblocks').debug3Func(): logFunc('called. self.badBlocksSet=%s, self.badBlocks=%s', self.badBlocksSet, self.badBlocks)
        if self.badBlocksSet:
            return self.badBlocks
        return None

    def hasBadBlocks (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-badblocks').debug3Func(): logFunc('called. self.badBlocksSet=%s, self.badBlocks=%s', self.badBlocksSet, self.badBlocks)
        if self.badBlocksSet:
            return True
        return False

    def setBadBlocks (self, badBlocks):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-badblocks').debug3Func(): logFunc('called. badBlocks=%s, old=%s', badBlocks, self.badBlocks)
        self.badBlocksSet = True
        self.badBlocks = badBlocks

    def requestMediaType (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-mediatype').debug3Func(): logFunc('called. requested=%s', requested)
        self.mediaTypeRequested = requested
        self.mediaTypeSet = False

    def isMediaTypeRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-mediatype-requested').debug3Func(): logFunc('called. requested=%s', self.mediaTypeRequested)
        return self.mediaTypeRequested

    def getMediaType (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-mediatype').debug3Func(): logFunc('called. self.mediaTypeSet=%s, self.mediaType=%s', self.mediaTypeSet, self.mediaType)
        if self.mediaTypeSet:
            return self.mediaType
        return None

    def hasMediaType (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-mediatype').debug3Func(): logFunc('called. self.mediaTypeSet=%s, self.mediaType=%s', self.mediaTypeSet, self.mediaType)
        if self.mediaTypeSet:
            return True
        return False

    def setMediaType (self, mediaType):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-mediatype').debug3Func(): logFunc('called. mediaType=%s, old=%s', mediaType, self.mediaType)
        self.mediaTypeSet = True
        self.mediaType = mediaType

    def requestHotSparePolicyViolation (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-hotsparepolicyviolation').debug3Func(): logFunc('called. requested=%s', requested)
        self.hotSparePolicyViolationRequested = requested
        self.hotSparePolicyViolationSet = False

    def isHotSparePolicyViolationRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-hotsparepolicyviolation-requested').debug3Func(): logFunc('called. requested=%s', self.hotSparePolicyViolationRequested)
        return self.hotSparePolicyViolationRequested

    def getHotSparePolicyViolation (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-hotsparepolicyviolation').debug3Func(): logFunc('called. self.hotSparePolicyViolationSet=%s, self.hotSparePolicyViolation=%s', self.hotSparePolicyViolationSet, self.hotSparePolicyViolation)
        if self.hotSparePolicyViolationSet:
            return self.hotSparePolicyViolation
        return None

    def hasHotSparePolicyViolation (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-hotsparepolicyviolation').debug3Func(): logFunc('called. self.hotSparePolicyViolationSet=%s, self.hotSparePolicyViolation=%s', self.hotSparePolicyViolationSet, self.hotSparePolicyViolation)
        if self.hotSparePolicyViolationSet:
            return True
        return False

    def setHotSparePolicyViolation (self, hotSparePolicyViolation):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-hotsparepolicyviolation').debug3Func(): logFunc('called. hotSparePolicyViolation=%s, old=%s', hotSparePolicyViolation, self.hotSparePolicyViolation)
        self.hotSparePolicyViolationSet = True
        self.hotSparePolicyViolation = hotSparePolicyViolation

    def requestId (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-id').debug3Func(): logFunc('called. requested=%s', requested)
        self.idRequested = requested
        self.idSet = False

    def isIdRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-id-requested').debug3Func(): logFunc('called. requested=%s', self.idRequested)
        return self.idRequested

    def getId (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-id').debug3Func(): logFunc('called. self.idSet=%s, self.id=%s', self.idSet, self.id)
        if self.idSet:
            return self.id
        return None

    def hasId (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-id').debug3Func(): logFunc('called. self.idSet=%s, self.id=%s', self.idSet, self.id)
        if self.idSet:
            return True
        return False

    def setId (self, id):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-id').debug3Func(): logFunc('called. id=%s, old=%s', id, self.id)
        self.idSet = True
        self.id = id

    def requestState (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-state').debug3Func(): logFunc('called. requested=%s', requested)
        self.stateRequested = requested
        self.stateSet = False

    def isStateRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-state-requested').debug3Func(): logFunc('called. requested=%s', self.stateRequested)
        return self.stateRequested

    def getState (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-state').debug3Func(): logFunc('called. self.stateSet=%s, self.state=%s', self.stateSet, self.state)
        if self.stateSet:
            return self.state
        return None

    def hasState (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-state').debug3Func(): logFunc('called. self.stateSet=%s, self.state=%s', self.stateSet, self.state)
        if self.stateSet:
            return True
        return False

    def setState (self, state):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-state').debug3Func(): logFunc('called. state=%s, old=%s', state, self.state)
        self.stateSet = True
        self.state = state

    def requestStatusRaw (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-statusraw').debug3Func(): logFunc('called. requested=%s', requested)
        self.statusRawRequested = requested
        self.statusRawSet = False

    def isStatusRawRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-statusraw-requested').debug3Func(): logFunc('called. requested=%s', self.statusRawRequested)
        return self.statusRawRequested

    def getStatusRaw (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-statusraw').debug3Func(): logFunc('called. self.statusRawSet=%s, self.statusRaw=%s', self.statusRawSet, self.statusRaw)
        if self.statusRawSet:
            return self.statusRaw
        return None

    def hasStatusRaw (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-statusraw').debug3Func(): logFunc('called. self.statusRawSet=%s, self.statusRaw=%s', self.statusRawSet, self.statusRaw)
        if self.statusRawSet:
            return True
        return False

    def setStatusRaw (self, statusRaw):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-statusraw').debug3Func(): logFunc('called. statusRaw=%s, old=%s', statusRaw, self.statusRaw)
        self.statusRawSet = True
        self.statusRaw = statusRaw

    def requestDiskCachePolicy (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-diskcachepolicy').debug3Func(): logFunc('called. requested=%s', requested)
        self.diskCachePolicyRequested = requested
        self.diskCachePolicySet = False

    def isDiskCachePolicyRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-diskcachepolicy-requested').debug3Func(): logFunc('called. requested=%s', self.diskCachePolicyRequested)
        return self.diskCachePolicyRequested

    def getDiskCachePolicy (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-diskcachepolicy').debug3Func(): logFunc('called. self.diskCachePolicySet=%s, self.diskCachePolicy=%s', self.diskCachePolicySet, self.diskCachePolicy)
        if self.diskCachePolicySet:
            return self.diskCachePolicy
        return None

    def hasDiskCachePolicy (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-diskcachepolicy').debug3Func(): logFunc('called. self.diskCachePolicySet=%s, self.diskCachePolicy=%s', self.diskCachePolicySet, self.diskCachePolicy)
        if self.diskCachePolicySet:
            return True
        return False

    def setDiskCachePolicy (self, diskCachePolicy):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-diskcachepolicy').debug3Func(): logFunc('called. diskCachePolicy=%s, old=%s', diskCachePolicy, self.diskCachePolicy)
        self.diskCachePolicySet = True
        self.diskCachePolicy = diskCachePolicy

    def requestBadBlocksRaw (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-badblocksraw').debug3Func(): logFunc('called. requested=%s', requested)
        self.badBlocksRawRequested = requested
        self.badBlocksRawSet = False

    def isBadBlocksRawRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-badblocksraw-requested').debug3Func(): logFunc('called. requested=%s', self.badBlocksRawRequested)
        return self.badBlocksRawRequested

    def getBadBlocksRaw (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-badblocksraw').debug3Func(): logFunc('called. self.badBlocksRawSet=%s, self.badBlocksRaw=%s', self.badBlocksRawSet, self.badBlocksRaw)
        if self.badBlocksRawSet:
            return self.badBlocksRaw
        return None

    def hasBadBlocksRaw (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-badblocksraw').debug3Func(): logFunc('called. self.badBlocksRawSet=%s, self.badBlocksRaw=%s', self.badBlocksRawSet, self.badBlocksRaw)
        if self.badBlocksRawSet:
            return True
        return False

    def setBadBlocksRaw (self, badBlocksRaw):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-badblocksraw').debug3Func(): logFunc('called. badBlocksRaw=%s, old=%s', badBlocksRaw, self.badBlocksRaw)
        self.badBlocksRawSet = True
        self.badBlocksRaw = badBlocksRaw

    def requestCachePolicy (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-cachepolicy').debug3Func(): logFunc('called. requested=%s', requested)
        self.cachePolicyRequested = requested
        self.cachePolicySet = False

    def isCachePolicyRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-cachepolicy-requested').debug3Func(): logFunc('called. requested=%s', self.cachePolicyRequested)
        return self.cachePolicyRequested

    def getCachePolicy (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-cachepolicy').debug3Func(): logFunc('called. self.cachePolicySet=%s, self.cachePolicy=%s', self.cachePolicySet, self.cachePolicy)
        if self.cachePolicySet:
            return self.cachePolicy
        return None

    def hasCachePolicy (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-cachepolicy').debug3Func(): logFunc('called. self.cachePolicySet=%s, self.cachePolicy=%s', self.cachePolicySet, self.cachePolicy)
        if self.cachePolicySet:
            return True
        return False

    def setCachePolicy (self, cachePolicy):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-cachepolicy').debug3Func(): logFunc('called. cachePolicy=%s, old=%s', cachePolicy, self.cachePolicy)
        self.cachePolicySet = True
        self.cachePolicy = cachePolicy

    def requestWritePolicy (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-writepolicy').debug3Func(): logFunc('called. requested=%s', requested)
        self.writePolicyRequested = requested
        self.writePolicySet = False

    def isWritePolicyRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-writepolicy-requested').debug3Func(): logFunc('called. requested=%s', self.writePolicyRequested)
        return self.writePolicyRequested

    def getWritePolicy (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-writepolicy').debug3Func(): logFunc('called. self.writePolicySet=%s, self.writePolicy=%s', self.writePolicySet, self.writePolicy)
        if self.writePolicySet:
            return self.writePolicy
        return None

    def hasWritePolicy (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-writepolicy').debug3Func(): logFunc('called. self.writePolicySet=%s, self.writePolicy=%s', self.writePolicySet, self.writePolicy)
        if self.writePolicySet:
            return True
        return False

    def setWritePolicy (self, writePolicy):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-writepolicy').debug3Func(): logFunc('called. writePolicy=%s, old=%s', writePolicy, self.writePolicy)
        self.writePolicySet = True
        self.writePolicy = writePolicy

    def requestRaidType (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-raidtype').debug3Func(): logFunc('called. requested=%s', requested)
        self.raidTypeRequested = requested
        self.raidTypeSet = False

    def isRaidTypeRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-raidtype-requested').debug3Func(): logFunc('called. requested=%s', self.raidTypeRequested)
        return self.raidTypeRequested

    def getRaidType (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-raidtype').debug3Func(): logFunc('called. self.raidTypeSet=%s, self.raidType=%s', self.raidTypeSet, self.raidType)
        if self.raidTypeSet:
            return self.raidType
        return None

    def hasRaidType (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-raidtype').debug3Func(): logFunc('called. self.raidTypeSet=%s, self.raidType=%s', self.raidTypeSet, self.raidType)
        if self.raidTypeSet:
            return True
        return False

    def setRaidType (self, raidType):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-raidtype').debug3Func(): logFunc('called. raidType=%s, old=%s', raidType, self.raidType)
        self.raidTypeSet = True
        self.raidType = raidType

    def requestStripeElementSize (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-stripeelementsize').debug3Func(): logFunc('called. requested=%s', requested)
        self.stripeElementSizeRequested = requested
        self.stripeElementSizeSet = False

    def isStripeElementSizeRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-stripeelementsize-requested').debug3Func(): logFunc('called. requested=%s', self.stripeElementSizeRequested)
        return self.stripeElementSizeRequested

    def getStripeElementSize (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-stripeelementsize').debug3Func(): logFunc('called. self.stripeElementSizeSet=%s, self.stripeElementSize=%s', self.stripeElementSizeSet, self.stripeElementSize)
        if self.stripeElementSizeSet:
            return self.stripeElementSize
        return None

    def hasStripeElementSize (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-stripeelementsize').debug3Func(): logFunc('called. self.stripeElementSizeSet=%s, self.stripeElementSize=%s', self.stripeElementSizeSet, self.stripeElementSize)
        if self.stripeElementSizeSet:
            return True
        return False

    def setStripeElementSize (self, stripeElementSize):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-stripeelementsize').debug3Func(): logFunc('called. stripeElementSize=%s, old=%s', stripeElementSize, self.stripeElementSize)
        self.stripeElementSizeSet = True
        self.stripeElementSize = stripeElementSize

    def requestSizeRaw (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-sizeraw').debug3Func(): logFunc('called. requested=%s', requested)
        self.sizeRawRequested = requested
        self.sizeRawSet = False

    def isSizeRawRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-sizeraw-requested').debug3Func(): logFunc('called. requested=%s', self.sizeRawRequested)
        return self.sizeRawRequested

    def getSizeRaw (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-sizeraw').debug3Func(): logFunc('called. self.sizeRawSet=%s, self.sizeRaw=%s', self.sizeRawSet, self.sizeRaw)
        if self.sizeRawSet:
            return self.sizeRaw
        return None

    def hasSizeRaw (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-sizeraw').debug3Func(): logFunc('called. self.sizeRawSet=%s, self.sizeRaw=%s', self.sizeRawSet, self.sizeRaw)
        if self.sizeRawSet:
            return True
        return False

    def setSizeRaw (self, sizeRaw):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-sizeraw').debug3Func(): logFunc('called. sizeRaw=%s, old=%s', sizeRaw, self.sizeRaw)
        self.sizeRawSet = True
        self.sizeRaw = sizeRaw

    def requestSize (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-size').debug3Func(): logFunc('called. requested=%s', requested)
        self.sizeRequested = requested
        self.sizeSet = False

    def isSizeRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-size-requested').debug3Func(): logFunc('called. requested=%s', self.sizeRequested)
        return self.sizeRequested

    def getSize (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-size').debug3Func(): logFunc('called. self.sizeSet=%s, self.size=%s', self.sizeSet, self.size)
        if self.sizeSet:
            return self.size
        return None

    def hasSize (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-size').debug3Func(): logFunc('called. self.sizeSet=%s, self.size=%s', self.sizeSet, self.size)
        if self.sizeSet:
            return True
        return False

    def setSize (self, size):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-size').debug3Func(): logFunc('called. size=%s, old=%s', size, self.size)
        self.sizeSet = True
        self.size = size


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.physicalIdList = 0
        self.physicalIdListSet = False
        
        self.status = 0
        self.statusSet = False
        
        self.stateRaw = 0
        self.stateRawSet = False
        
        self.readPolicy = 0
        self.readPolicySet = False
        
        self.badBlocks = 0
        self.badBlocksSet = False
        
        self.mediaType = 0
        self.mediaTypeSet = False
        
        self.hotSparePolicyViolation = 0
        self.hotSparePolicyViolationSet = False
        
        self.id = 0
        self.idSet = False
        
        self.state = 0
        self.stateSet = False
        
        self.statusRaw = 0
        self.statusRawSet = False
        
        self.diskCachePolicy = 0
        self.diskCachePolicySet = False
        
        self.badBlocksRaw = 0
        self.badBlocksRawSet = False
        
        self.cachePolicy = 0
        self.cachePolicySet = False
        
        self.writePolicy = 0
        self.writePolicySet = False
        
        self.raidType = 0
        self.raidTypeSet = False
        
        self.stripeElementSize = 0
        self.stripeElementSizeSet = False
        
        self.sizeRaw = 0
        self.sizeRawSet = False
        
        self.size = 0
        self.sizeSet = False
        

    def _getSelfKeyPath (self, disk
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("raid-array", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(disk);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("disk", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("storage", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage", "qt-strg"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        disk, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(disk, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(disk, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       disk, 
                       
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

        keyPath = self._getSelfKeyPath(disk, 
                                       
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
                               disk, 
                               
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

        
        if self.isPhysicalIdListRequested():
            valPhysicalIdList = Value()
            valPhysicalIdList.setEmpty()
            tagValueList.push(("physical-id-list", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valPhysicalIdList)
        
        if self.isStatusRequested():
            valStatus = Value()
            valStatus.setEmpty()
            tagValueList.push(("status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valStatus)
        
        if self.isStateRawRequested():
            valStateRaw = Value()
            valStateRaw.setEmpty()
            tagValueList.push(("state-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valStateRaw)
        
        if self.isReadPolicyRequested():
            valReadPolicy = Value()
            valReadPolicy.setEmpty()
            tagValueList.push(("read-policy", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valReadPolicy)
        
        if self.isBadBlocksRequested():
            valBadBlocks = Value()
            valBadBlocks.setEmpty()
            tagValueList.push(("bad-blocks", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valBadBlocks)
        
        if self.isMediaTypeRequested():
            valMediaType = Value()
            valMediaType.setEmpty()
            tagValueList.push(("media-type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valMediaType)
        
        if self.isHotSparePolicyViolationRequested():
            valHotSparePolicyViolation = Value()
            valHotSparePolicyViolation.setEmpty()
            tagValueList.push(("hot-spare-policy-violation", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valHotSparePolicyViolation)
        
        if self.isIdRequested():
            valId = Value()
            valId.setEmpty()
            tagValueList.push(("id", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valId)
        
        if self.isStateRequested():
            valState = Value()
            valState.setEmpty()
            tagValueList.push(("state", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valState)
        
        if self.isStatusRawRequested():
            valStatusRaw = Value()
            valStatusRaw.setEmpty()
            tagValueList.push(("status-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valStatusRaw)
        
        if self.isDiskCachePolicyRequested():
            valDiskCachePolicy = Value()
            valDiskCachePolicy.setEmpty()
            tagValueList.push(("disk-cache-policy", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valDiskCachePolicy)
        
        if self.isBadBlocksRawRequested():
            valBadBlocksRaw = Value()
            valBadBlocksRaw.setEmpty()
            tagValueList.push(("bad-blocks-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valBadBlocksRaw)
        
        if self.isCachePolicyRequested():
            valCachePolicy = Value()
            valCachePolicy.setEmpty()
            tagValueList.push(("cache-policy", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valCachePolicy)
        
        if self.isWritePolicyRequested():
            valWritePolicy = Value()
            valWritePolicy.setEmpty()
            tagValueList.push(("write-policy", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valWritePolicy)
        
        if self.isRaidTypeRequested():
            valRaidType = Value()
            valRaidType.setEmpty()
            tagValueList.push(("raid-type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valRaidType)
        
        if self.isStripeElementSizeRequested():
            valStripeElementSize = Value()
            valStripeElementSize.setEmpty()
            tagValueList.push(("stripe-element-size", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valStripeElementSize)
        
        if self.isSizeRawRequested():
            valSizeRaw = Value()
            valSizeRaw.setEmpty()
            tagValueList.push(("size-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valSizeRaw)
        
        if self.isSizeRequested():
            valSize = Value()
            valSize.setEmpty()
            tagValueList.push(("size", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valSize)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isPhysicalIdListRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "physical-id-list") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-physicalidlist').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "physicalIdList", "physical-id-list", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-physical-id-list-bad-value').infoFunc(): logFunc('physicalIdList not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPhysicalIdList(tempVar)
            for logFunc in self._log('read-tag-values-physical-id-list').debug3Func(): logFunc('read physicalIdList. physicalIdList=%s, tempValue=%s', self.physicalIdList, tempValue.getType())
        
        if self.isStatusRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "status") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-status').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "status", "status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-status-bad-value').infoFunc(): logFunc('status not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setStatus(tempVar)
            for logFunc in self._log('read-tag-values-status').debug3Func(): logFunc('read status. status=%s, tempValue=%s', self.status, tempValue.getType())
        
        if self.isStateRawRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "state-raw") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-stateraw').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "stateRaw", "state-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-state-raw-bad-value').infoFunc(): logFunc('stateRaw not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setStateRaw(tempVar)
            for logFunc in self._log('read-tag-values-state-raw').debug3Func(): logFunc('read stateRaw. stateRaw=%s, tempValue=%s', self.stateRaw, tempValue.getType())
        
        if self.isReadPolicyRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "read-policy") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-readpolicy').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "readPolicy", "read-policy", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-read-policy-bad-value').infoFunc(): logFunc('readPolicy not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setReadPolicy(tempVar)
            for logFunc in self._log('read-tag-values-read-policy').debug3Func(): logFunc('read readPolicy. readPolicy=%s, tempValue=%s', self.readPolicy, tempValue.getType())
        
        if self.isBadBlocksRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "bad-blocks") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-badblocks').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "badBlocks", "bad-blocks", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-bad-blocks-bad-value').infoFunc(): logFunc('badBlocks not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setBadBlocks(tempVar)
            for logFunc in self._log('read-tag-values-bad-blocks').debug3Func(): logFunc('read badBlocks. badBlocks=%s, tempValue=%s', self.badBlocks, tempValue.getType())
        
        if self.isMediaTypeRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "media-type") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-mediatype').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "mediaType", "media-type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-media-type-bad-value').infoFunc(): logFunc('mediaType not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMediaType(tempVar)
            for logFunc in self._log('read-tag-values-media-type').debug3Func(): logFunc('read mediaType. mediaType=%s, tempValue=%s', self.mediaType, tempValue.getType())
        
        if self.isHotSparePolicyViolationRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "hot-spare-policy-violation") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-hotsparepolicyviolation').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "hotSparePolicyViolation", "hot-spare-policy-violation", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-hot-spare-policy-violation-bad-value').infoFunc(): logFunc('hotSparePolicyViolation not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setHotSparePolicyViolation(tempVar)
            for logFunc in self._log('read-tag-values-hot-spare-policy-violation').debug3Func(): logFunc('read hotSparePolicyViolation. hotSparePolicyViolation=%s, tempValue=%s', self.hotSparePolicyViolation, tempValue.getType())
        
        if self.isIdRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "id") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-id').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "id", "id", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-id-bad-value').infoFunc(): logFunc('id not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setId(tempVar)
            for logFunc in self._log('read-tag-values-id').debug3Func(): logFunc('read id. id=%s, tempValue=%s', self.id, tempValue.getType())
        
        if self.isStateRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "state") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-state').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "state", "state", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-state-bad-value').infoFunc(): logFunc('state not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setState(tempVar)
            for logFunc in self._log('read-tag-values-state').debug3Func(): logFunc('read state. state=%s, tempValue=%s', self.state, tempValue.getType())
        
        if self.isStatusRawRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "status-raw") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-statusraw').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "statusRaw", "status-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-status-raw-bad-value').infoFunc(): logFunc('statusRaw not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setStatusRaw(tempVar)
            for logFunc in self._log('read-tag-values-status-raw').debug3Func(): logFunc('read statusRaw. statusRaw=%s, tempValue=%s', self.statusRaw, tempValue.getType())
        
        if self.isDiskCachePolicyRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "disk-cache-policy") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-diskcachepolicy').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "diskCachePolicy", "disk-cache-policy", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-disk-cache-policy-bad-value').infoFunc(): logFunc('diskCachePolicy not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setDiskCachePolicy(tempVar)
            for logFunc in self._log('read-tag-values-disk-cache-policy').debug3Func(): logFunc('read diskCachePolicy. diskCachePolicy=%s, tempValue=%s', self.diskCachePolicy, tempValue.getType())
        
        if self.isBadBlocksRawRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "bad-blocks-raw") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-badblocksraw').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "badBlocksRaw", "bad-blocks-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-bad-blocks-raw-bad-value').infoFunc(): logFunc('badBlocksRaw not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setBadBlocksRaw(tempVar)
            for logFunc in self._log('read-tag-values-bad-blocks-raw').debug3Func(): logFunc('read badBlocksRaw. badBlocksRaw=%s, tempValue=%s', self.badBlocksRaw, tempValue.getType())
        
        if self.isCachePolicyRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "cache-policy") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-cachepolicy').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "cachePolicy", "cache-policy", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-cache-policy-bad-value').infoFunc(): logFunc('cachePolicy not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setCachePolicy(tempVar)
            for logFunc in self._log('read-tag-values-cache-policy').debug3Func(): logFunc('read cachePolicy. cachePolicy=%s, tempValue=%s', self.cachePolicy, tempValue.getType())
        
        if self.isWritePolicyRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "write-policy") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-writepolicy').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "writePolicy", "write-policy", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-write-policy-bad-value').infoFunc(): logFunc('writePolicy not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setWritePolicy(tempVar)
            for logFunc in self._log('read-tag-values-write-policy').debug3Func(): logFunc('read writePolicy. writePolicy=%s, tempValue=%s', self.writePolicy, tempValue.getType())
        
        if self.isRaidTypeRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "raid-type") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-raidtype').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "raidType", "raid-type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-raid-type-bad-value').infoFunc(): logFunc('raidType not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setRaidType(tempVar)
            for logFunc in self._log('read-tag-values-raid-type').debug3Func(): logFunc('read raidType. raidType=%s, tempValue=%s', self.raidType, tempValue.getType())
        
        if self.isStripeElementSizeRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "stripe-element-size") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-stripeelementsize').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "stripeElementSize", "stripe-element-size", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-stripe-element-size-bad-value').infoFunc(): logFunc('stripeElementSize not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setStripeElementSize(tempVar)
            for logFunc in self._log('read-tag-values-stripe-element-size').debug3Func(): logFunc('read stripeElementSize. stripeElementSize=%s, tempValue=%s', self.stripeElementSize, tempValue.getType())
        
        if self.isSizeRawRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "size-raw") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-sizeraw').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "sizeRaw", "size-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-size-raw-bad-value').infoFunc(): logFunc('sizeRaw not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setSizeRaw(tempVar)
            for logFunc in self._log('read-tag-values-size-raw').debug3Func(): logFunc('read sizeRaw. sizeRaw=%s, tempValue=%s', self.sizeRaw, tempValue.getType())
        
        if self.isSizeRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "size") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-size').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "size", "size", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-size-bad-value').infoFunc(): logFunc('size not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setSize(tempVar)
            for logFunc in self._log('read-tag-values-size').debug3Func(): logFunc('read size. size=%s, tempValue=%s', self.size, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "status", 
        "namespace": "status", 
        "className": "StatusMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.raid_array.status.status_maapi_gen import StatusMaapi", 
        "baseClassName": "StatusMaapiBase", 
        "baseModule": "status_maapi_base_gen"
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
            "yangName": "raid-array", 
            "namespace": "raid_array", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "name": "raid-array"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "yangName": "status", 
            "namespace": "status", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "name": "status"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "physicalIdList", 
            "yangName": "physical-id-list", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "status", 
            "yangName": "status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "stateRaw", 
            "yangName": "state-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "readPolicy", 
            "yangName": "read-policy", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "badBlocks", 
            "yangName": "bad-blocks", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "mediaType", 
            "yangName": "media-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "hotSparePolicyViolation", 
            "yangName": "hot-spare-policy-violation", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "id", 
            "yangName": "id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "state", 
            "yangName": "state", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "statusRaw", 
            "yangName": "status-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "diskCachePolicy", 
            "yangName": "disk-cache-policy", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "badBlocksRaw", 
            "yangName": "bad-blocks-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "cachePolicy", 
            "yangName": "cache-policy", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "writePolicy", 
            "yangName": "write-policy", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "raidType", 
            "yangName": "raid-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "stripeElementSize", 
            "yangName": "stripe-element-size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "sizeRaw", 
            "yangName": "size-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "size", 
            "yangName": "size", 
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
            "common", 
            "qwilt_tech_storage_disk"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "physicalIdList", 
            "yangName": "physical-id-list", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "status", 
            "yangName": "status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "stateRaw", 
            "yangName": "state-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "readPolicy", 
            "yangName": "read-policy", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "badBlocks", 
            "yangName": "bad-blocks", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "mediaType", 
            "yangName": "media-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "hotSparePolicyViolation", 
            "yangName": "hot-spare-policy-violation", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "id", 
            "yangName": "id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "state", 
            "yangName": "state", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "statusRaw", 
            "yangName": "status-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "diskCachePolicy", 
            "yangName": "disk-cache-policy", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "badBlocksRaw", 
            "yangName": "bad-blocks-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "cachePolicy", 
            "yangName": "cache-policy", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "writePolicy", 
            "yangName": "write-policy", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "raidType", 
            "yangName": "raid-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "stripeElementSize", 
            "yangName": "stripe-element-size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "sizeRaw", 
            "yangName": "size-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "size", 
            "yangName": "size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


