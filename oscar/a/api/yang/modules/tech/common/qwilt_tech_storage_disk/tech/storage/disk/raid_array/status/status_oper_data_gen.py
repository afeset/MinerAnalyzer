


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



from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import RaidArrayStatusType
from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import RaidArrayStateType


class StatusOperData (object):

    def __init__ (self):

        self.physicalIdList = ""
        self._myHasPhysicalIdList=False
        self._myPhysicalIdListRequested=False
        
        self.status = RaidArrayStatusType.kFailure
        self._myHasStatus=False
        self._myStatusRequested=False
        
        self.stateRaw = ""
        self._myHasStateRaw=False
        self._myStateRawRequested=False
        
        self.readPolicy = ""
        self._myHasReadPolicy=False
        self._myReadPolicyRequested=False
        
        self.badBlocks = False
        self._myHasBadBlocks=False
        self._myBadBlocksRequested=False
        
        self.mediaType = ""
        self._myHasMediaType=False
        self._myMediaTypeRequested=False
        
        self.hotSparePolicyViolation = ""
        self._myHasHotSparePolicyViolation=False
        self._myHotSparePolicyViolationRequested=False
        
        self.id = ""
        self._myHasId=False
        self._myIdRequested=False
        
        self.state = RaidArrayStateType.kReady
        self._myHasState=False
        self._myStateRequested=False
        
        self.statusRaw = ""
        self._myHasStatusRaw=False
        self._myStatusRawRequested=False
        
        self.diskCachePolicy = ""
        self._myHasDiskCachePolicy=False
        self._myDiskCachePolicyRequested=False
        
        self.badBlocksRaw = ""
        self._myHasBadBlocksRaw=False
        self._myBadBlocksRawRequested=False
        
        self.cachePolicy = ""
        self._myHasCachePolicy=False
        self._myCachePolicyRequested=False
        
        self.writePolicy = ""
        self._myHasWritePolicy=False
        self._myWritePolicyRequested=False
        
        self.raidType = ""
        self._myHasRaidType=False
        self._myRaidTypeRequested=False
        
        self.stripeElementSize = ""
        self._myHasStripeElementSize=False
        self._myStripeElementSizeRequested=False
        
        self.sizeRaw = ""
        self._myHasSizeRaw=False
        self._mySizeRawRequested=False
        
        self.size = 0
        self._myHasSize=False
        self._mySizeRequested=False
        


    def copyFrom (self, other):

        self.physicalIdList=other.physicalIdList
        self._myHasPhysicalIdList=other._myHasPhysicalIdList
        self._myPhysicalIdListRequested=other._myPhysicalIdListRequested
        
        self.status=other.status
        self._myHasStatus=other._myHasStatus
        self._myStatusRequested=other._myStatusRequested
        
        self.stateRaw=other.stateRaw
        self._myHasStateRaw=other._myHasStateRaw
        self._myStateRawRequested=other._myStateRawRequested
        
        self.readPolicy=other.readPolicy
        self._myHasReadPolicy=other._myHasReadPolicy
        self._myReadPolicyRequested=other._myReadPolicyRequested
        
        self.badBlocks=other.badBlocks
        self._myHasBadBlocks=other._myHasBadBlocks
        self._myBadBlocksRequested=other._myBadBlocksRequested
        
        self.mediaType=other.mediaType
        self._myHasMediaType=other._myHasMediaType
        self._myMediaTypeRequested=other._myMediaTypeRequested
        
        self.hotSparePolicyViolation=other.hotSparePolicyViolation
        self._myHasHotSparePolicyViolation=other._myHasHotSparePolicyViolation
        self._myHotSparePolicyViolationRequested=other._myHotSparePolicyViolationRequested
        
        self.id=other.id
        self._myHasId=other._myHasId
        self._myIdRequested=other._myIdRequested
        
        self.state=other.state
        self._myHasState=other._myHasState
        self._myStateRequested=other._myStateRequested
        
        self.statusRaw=other.statusRaw
        self._myHasStatusRaw=other._myHasStatusRaw
        self._myStatusRawRequested=other._myStatusRawRequested
        
        self.diskCachePolicy=other.diskCachePolicy
        self._myHasDiskCachePolicy=other._myHasDiskCachePolicy
        self._myDiskCachePolicyRequested=other._myDiskCachePolicyRequested
        
        self.badBlocksRaw=other.badBlocksRaw
        self._myHasBadBlocksRaw=other._myHasBadBlocksRaw
        self._myBadBlocksRawRequested=other._myBadBlocksRawRequested
        
        self.cachePolicy=other.cachePolicy
        self._myHasCachePolicy=other._myHasCachePolicy
        self._myCachePolicyRequested=other._myCachePolicyRequested
        
        self.writePolicy=other.writePolicy
        self._myHasWritePolicy=other._myHasWritePolicy
        self._myWritePolicyRequested=other._myWritePolicyRequested
        
        self.raidType=other.raidType
        self._myHasRaidType=other._myHasRaidType
        self._myRaidTypeRequested=other._myRaidTypeRequested
        
        self.stripeElementSize=other.stripeElementSize
        self._myHasStripeElementSize=other._myHasStripeElementSize
        self._myStripeElementSizeRequested=other._myStripeElementSizeRequested
        
        self.sizeRaw=other.sizeRaw
        self._myHasSizeRaw=other._myHasSizeRaw
        self._mySizeRawRequested=other._mySizeRawRequested
        
        self.size=other.size
        self._myHasSize=other._myHasSize
        self._mySizeRequested=other._mySizeRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isPhysicalIdListRequested():
            self.physicalIdList=other.physicalIdList
            self._myHasPhysicalIdList=other._myHasPhysicalIdList
            self._myPhysicalIdListRequested=other._myPhysicalIdListRequested
        
        if self.isStatusRequested():
            self.status=other.status
            self._myHasStatus=other._myHasStatus
            self._myStatusRequested=other._myStatusRequested
        
        if self.isStateRawRequested():
            self.stateRaw=other.stateRaw
            self._myHasStateRaw=other._myHasStateRaw
            self._myStateRawRequested=other._myStateRawRequested
        
        if self.isReadPolicyRequested():
            self.readPolicy=other.readPolicy
            self._myHasReadPolicy=other._myHasReadPolicy
            self._myReadPolicyRequested=other._myReadPolicyRequested
        
        if self.isBadBlocksRequested():
            self.badBlocks=other.badBlocks
            self._myHasBadBlocks=other._myHasBadBlocks
            self._myBadBlocksRequested=other._myBadBlocksRequested
        
        if self.isMediaTypeRequested():
            self.mediaType=other.mediaType
            self._myHasMediaType=other._myHasMediaType
            self._myMediaTypeRequested=other._myMediaTypeRequested
        
        if self.isHotSparePolicyViolationRequested():
            self.hotSparePolicyViolation=other.hotSparePolicyViolation
            self._myHasHotSparePolicyViolation=other._myHasHotSparePolicyViolation
            self._myHotSparePolicyViolationRequested=other._myHotSparePolicyViolationRequested
        
        if self.isIdRequested():
            self.id=other.id
            self._myHasId=other._myHasId
            self._myIdRequested=other._myIdRequested
        
        if self.isStateRequested():
            self.state=other.state
            self._myHasState=other._myHasState
            self._myStateRequested=other._myStateRequested
        
        if self.isStatusRawRequested():
            self.statusRaw=other.statusRaw
            self._myHasStatusRaw=other._myHasStatusRaw
            self._myStatusRawRequested=other._myStatusRawRequested
        
        if self.isDiskCachePolicyRequested():
            self.diskCachePolicy=other.diskCachePolicy
            self._myHasDiskCachePolicy=other._myHasDiskCachePolicy
            self._myDiskCachePolicyRequested=other._myDiskCachePolicyRequested
        
        if self.isBadBlocksRawRequested():
            self.badBlocksRaw=other.badBlocksRaw
            self._myHasBadBlocksRaw=other._myHasBadBlocksRaw
            self._myBadBlocksRawRequested=other._myBadBlocksRawRequested
        
        if self.isCachePolicyRequested():
            self.cachePolicy=other.cachePolicy
            self._myHasCachePolicy=other._myHasCachePolicy
            self._myCachePolicyRequested=other._myCachePolicyRequested
        
        if self.isWritePolicyRequested():
            self.writePolicy=other.writePolicy
            self._myHasWritePolicy=other._myHasWritePolicy
            self._myWritePolicyRequested=other._myWritePolicyRequested
        
        if self.isRaidTypeRequested():
            self.raidType=other.raidType
            self._myHasRaidType=other._myHasRaidType
            self._myRaidTypeRequested=other._myRaidTypeRequested
        
        if self.isStripeElementSizeRequested():
            self.stripeElementSize=other.stripeElementSize
            self._myHasStripeElementSize=other._myHasStripeElementSize
            self._myStripeElementSizeRequested=other._myStripeElementSizeRequested
        
        if self.isSizeRawRequested():
            self.sizeRaw=other.sizeRaw
            self._myHasSizeRaw=other._myHasSizeRaw
            self._mySizeRawRequested=other._mySizeRawRequested
        
        if self.isSizeRequested():
            self.size=other.size
            self._myHasSize=other._myHasSize
            self._mySizeRequested=other._mySizeRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasPhysicalIdList():
            self.physicalIdList=other.physicalIdList
            self._myHasPhysicalIdList=other._myHasPhysicalIdList
            self._myPhysicalIdListRequested=other._myPhysicalIdListRequested
        
        if other.hasStatus():
            self.status=other.status
            self._myHasStatus=other._myHasStatus
            self._myStatusRequested=other._myStatusRequested
        
        if other.hasStateRaw():
            self.stateRaw=other.stateRaw
            self._myHasStateRaw=other._myHasStateRaw
            self._myStateRawRequested=other._myStateRawRequested
        
        if other.hasReadPolicy():
            self.readPolicy=other.readPolicy
            self._myHasReadPolicy=other._myHasReadPolicy
            self._myReadPolicyRequested=other._myReadPolicyRequested
        
        if other.hasBadBlocks():
            self.badBlocks=other.badBlocks
            self._myHasBadBlocks=other._myHasBadBlocks
            self._myBadBlocksRequested=other._myBadBlocksRequested
        
        if other.hasMediaType():
            self.mediaType=other.mediaType
            self._myHasMediaType=other._myHasMediaType
            self._myMediaTypeRequested=other._myMediaTypeRequested
        
        if other.hasHotSparePolicyViolation():
            self.hotSparePolicyViolation=other.hotSparePolicyViolation
            self._myHasHotSparePolicyViolation=other._myHasHotSparePolicyViolation
            self._myHotSparePolicyViolationRequested=other._myHotSparePolicyViolationRequested
        
        if other.hasId():
            self.id=other.id
            self._myHasId=other._myHasId
            self._myIdRequested=other._myIdRequested
        
        if other.hasState():
            self.state=other.state
            self._myHasState=other._myHasState
            self._myStateRequested=other._myStateRequested
        
        if other.hasStatusRaw():
            self.statusRaw=other.statusRaw
            self._myHasStatusRaw=other._myHasStatusRaw
            self._myStatusRawRequested=other._myStatusRawRequested
        
        if other.hasDiskCachePolicy():
            self.diskCachePolicy=other.diskCachePolicy
            self._myHasDiskCachePolicy=other._myHasDiskCachePolicy
            self._myDiskCachePolicyRequested=other._myDiskCachePolicyRequested
        
        if other.hasBadBlocksRaw():
            self.badBlocksRaw=other.badBlocksRaw
            self._myHasBadBlocksRaw=other._myHasBadBlocksRaw
            self._myBadBlocksRawRequested=other._myBadBlocksRawRequested
        
        if other.hasCachePolicy():
            self.cachePolicy=other.cachePolicy
            self._myHasCachePolicy=other._myHasCachePolicy
            self._myCachePolicyRequested=other._myCachePolicyRequested
        
        if other.hasWritePolicy():
            self.writePolicy=other.writePolicy
            self._myHasWritePolicy=other._myHasWritePolicy
            self._myWritePolicyRequested=other._myWritePolicyRequested
        
        if other.hasRaidType():
            self.raidType=other.raidType
            self._myHasRaidType=other._myHasRaidType
            self._myRaidTypeRequested=other._myRaidTypeRequested
        
        if other.hasStripeElementSize():
            self.stripeElementSize=other.stripeElementSize
            self._myHasStripeElementSize=other._myHasStripeElementSize
            self._myStripeElementSizeRequested=other._myStripeElementSizeRequested
        
        if other.hasSizeRaw():
            self.sizeRaw=other.sizeRaw
            self._myHasSizeRaw=other._myHasSizeRaw
            self._mySizeRawRequested=other._mySizeRawRequested
        
        if other.hasSize():
            self.size=other.size
            self._myHasSize=other._myHasSize
            self._mySizeRequested=other._mySizeRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.physicalIdList=other.physicalIdList
        self._myHasPhysicalIdList=other._myHasPhysicalIdList
        
        self.status=other.status
        self._myHasStatus=other._myHasStatus
        
        self.stateRaw=other.stateRaw
        self._myHasStateRaw=other._myHasStateRaw
        
        self.readPolicy=other.readPolicy
        self._myHasReadPolicy=other._myHasReadPolicy
        
        self.badBlocks=other.badBlocks
        self._myHasBadBlocks=other._myHasBadBlocks
        
        self.mediaType=other.mediaType
        self._myHasMediaType=other._myHasMediaType
        
        self.hotSparePolicyViolation=other.hotSparePolicyViolation
        self._myHasHotSparePolicyViolation=other._myHasHotSparePolicyViolation
        
        self.id=other.id
        self._myHasId=other._myHasId
        
        self.state=other.state
        self._myHasState=other._myHasState
        
        self.statusRaw=other.statusRaw
        self._myHasStatusRaw=other._myHasStatusRaw
        
        self.diskCachePolicy=other.diskCachePolicy
        self._myHasDiskCachePolicy=other._myHasDiskCachePolicy
        
        self.badBlocksRaw=other.badBlocksRaw
        self._myHasBadBlocksRaw=other._myHasBadBlocksRaw
        
        self.cachePolicy=other.cachePolicy
        self._myHasCachePolicy=other._myHasCachePolicy
        
        self.writePolicy=other.writePolicy
        self._myHasWritePolicy=other._myHasWritePolicy
        
        self.raidType=other.raidType
        self._myHasRaidType=other._myHasRaidType
        
        self.stripeElementSize=other.stripeElementSize
        self._myHasStripeElementSize=other._myHasStripeElementSize
        
        self.sizeRaw=other.sizeRaw
        self._myHasSizeRaw=other._myHasSizeRaw
        
        self.size=other.size
        self._myHasSize=other._myHasSize
        


    def setAllNumericToZero (self):
        
        self.size=0
        self.setHasSize()
        
        pass

    def subtractAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasSize():
            if other.hasSize():
                self.size -= other.size
        
        
        pass


    def addAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasSize():
            if other.hasSize():
                self.size += other.size
        
        
        pass


    # has...() methods

    def hasPhysicalIdList (self):
        return self._myHasPhysicalIdList

    def hasStatus (self):
        return self._myHasStatus

    def hasStateRaw (self):
        return self._myHasStateRaw

    def hasReadPolicy (self):
        return self._myHasReadPolicy

    def hasBadBlocks (self):
        return self._myHasBadBlocks

    def hasMediaType (self):
        return self._myHasMediaType

    def hasHotSparePolicyViolation (self):
        return self._myHasHotSparePolicyViolation

    def hasId (self):
        return self._myHasId

    def hasState (self):
        return self._myHasState

    def hasStatusRaw (self):
        return self._myHasStatusRaw

    def hasDiskCachePolicy (self):
        return self._myHasDiskCachePolicy

    def hasBadBlocksRaw (self):
        return self._myHasBadBlocksRaw

    def hasCachePolicy (self):
        return self._myHasCachePolicy

    def hasWritePolicy (self):
        return self._myHasWritePolicy

    def hasRaidType (self):
        return self._myHasRaidType

    def hasStripeElementSize (self):
        return self._myHasStripeElementSize

    def hasSizeRaw (self):
        return self._myHasSizeRaw

    def hasSize (self):
        return self._myHasSize




    # setHas...() methods

    def setHasPhysicalIdList (self):
        self._myHasPhysicalIdList=True

    def setHasStatus (self):
        self._myHasStatus=True

    def setHasStateRaw (self):
        self._myHasStateRaw=True

    def setHasReadPolicy (self):
        self._myHasReadPolicy=True

    def setHasBadBlocks (self):
        self._myHasBadBlocks=True

    def setHasMediaType (self):
        self._myHasMediaType=True

    def setHasHotSparePolicyViolation (self):
        self._myHasHotSparePolicyViolation=True

    def setHasId (self):
        self._myHasId=True

    def setHasState (self):
        self._myHasState=True

    def setHasStatusRaw (self):
        self._myHasStatusRaw=True

    def setHasDiskCachePolicy (self):
        self._myHasDiskCachePolicy=True

    def setHasBadBlocksRaw (self):
        self._myHasBadBlocksRaw=True

    def setHasCachePolicy (self):
        self._myHasCachePolicy=True

    def setHasWritePolicy (self):
        self._myHasWritePolicy=True

    def setHasRaidType (self):
        self._myHasRaidType=True

    def setHasStripeElementSize (self):
        self._myHasStripeElementSize=True

    def setHasSizeRaw (self):
        self._myHasSizeRaw=True

    def setHasSize (self):
        self._myHasSize=True




    # isRequested...() methods

    def isPhysicalIdListRequested (self):
        return self._myPhysicalIdListRequested

    def isStatusRequested (self):
        return self._myStatusRequested

    def isStateRawRequested (self):
        return self._myStateRawRequested

    def isReadPolicyRequested (self):
        return self._myReadPolicyRequested

    def isBadBlocksRequested (self):
        return self._myBadBlocksRequested

    def isMediaTypeRequested (self):
        return self._myMediaTypeRequested

    def isHotSparePolicyViolationRequested (self):
        return self._myHotSparePolicyViolationRequested

    def isIdRequested (self):
        return self._myIdRequested

    def isStateRequested (self):
        return self._myStateRequested

    def isStatusRawRequested (self):
        return self._myStatusRawRequested

    def isDiskCachePolicyRequested (self):
        return self._myDiskCachePolicyRequested

    def isBadBlocksRawRequested (self):
        return self._myBadBlocksRawRequested

    def isCachePolicyRequested (self):
        return self._myCachePolicyRequested

    def isWritePolicyRequested (self):
        return self._myWritePolicyRequested

    def isRaidTypeRequested (self):
        return self._myRaidTypeRequested

    def isStripeElementSizeRequested (self):
        return self._myStripeElementSizeRequested

    def isSizeRawRequested (self):
        return self._mySizeRawRequested

    def isSizeRequested (self):
        return self._mySizeRequested




    # setRequested...() methods

    def setPhysicalIdListRequested (self):
        self._myPhysicalIdListRequested=True

    def setStatusRequested (self):
        self._myStatusRequested=True

    def setStateRawRequested (self):
        self._myStateRawRequested=True

    def setReadPolicyRequested (self):
        self._myReadPolicyRequested=True

    def setBadBlocksRequested (self):
        self._myBadBlocksRequested=True

    def setMediaTypeRequested (self):
        self._myMediaTypeRequested=True

    def setHotSparePolicyViolationRequested (self):
        self._myHotSparePolicyViolationRequested=True

    def setIdRequested (self):
        self._myIdRequested=True

    def setStateRequested (self):
        self._myStateRequested=True

    def setStatusRawRequested (self):
        self._myStatusRawRequested=True

    def setDiskCachePolicyRequested (self):
        self._myDiskCachePolicyRequested=True

    def setBadBlocksRawRequested (self):
        self._myBadBlocksRawRequested=True

    def setCachePolicyRequested (self):
        self._myCachePolicyRequested=True

    def setWritePolicyRequested (self):
        self._myWritePolicyRequested=True

    def setRaidTypeRequested (self):
        self._myRaidTypeRequested=True

    def setStripeElementSizeRequested (self):
        self._myStripeElementSizeRequested=True

    def setSizeRawRequested (self):
        self._mySizeRawRequested=True

    def setSizeRequested (self):
        self._mySizeRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myPhysicalIdListRequested:
            x = "+PhysicalIdList="
            if self._myHasPhysicalIdList:
                leafStr = str(self.physicalIdList)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myStatusRequested:
            x = "+Status="
            if self._myHasStatus:
                leafStr = str(self.status)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myStateRawRequested:
            x = "+StateRaw="
            if self._myHasStateRaw:
                leafStr = str(self.stateRaw)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myReadPolicyRequested:
            x = "+ReadPolicy="
            if self._myHasReadPolicy:
                leafStr = str(self.readPolicy)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myBadBlocksRequested:
            x = "+BadBlocks="
            if self._myHasBadBlocks:
                leafStr = str(self.badBlocks)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myMediaTypeRequested:
            x = "+MediaType="
            if self._myHasMediaType:
                leafStr = str(self.mediaType)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myHotSparePolicyViolationRequested:
            x = "+HotSparePolicyViolation="
            if self._myHasHotSparePolicyViolation:
                leafStr = str(self.hotSparePolicyViolation)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myIdRequested:
            x = "+Id="
            if self._myHasId:
                leafStr = str(self.id)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myStateRequested:
            x = "+State="
            if self._myHasState:
                leafStr = str(self.state)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myStatusRawRequested:
            x = "+StatusRaw="
            if self._myHasStatusRaw:
                leafStr = str(self.statusRaw)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myDiskCachePolicyRequested:
            x = "+DiskCachePolicy="
            if self._myHasDiskCachePolicy:
                leafStr = str(self.diskCachePolicy)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myBadBlocksRawRequested:
            x = "+BadBlocksRaw="
            if self._myHasBadBlocksRaw:
                leafStr = str(self.badBlocksRaw)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myCachePolicyRequested:
            x = "+CachePolicy="
            if self._myHasCachePolicy:
                leafStr = str(self.cachePolicy)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myWritePolicyRequested:
            x = "+WritePolicy="
            if self._myHasWritePolicy:
                leafStr = str(self.writePolicy)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myRaidTypeRequested:
            x = "+RaidType="
            if self._myHasRaidType:
                leafStr = str(self.raidType)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myStripeElementSizeRequested:
            x = "+StripeElementSize="
            if self._myHasStripeElementSize:
                leafStr = str(self.stripeElementSize)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._mySizeRawRequested:
            x = "+SizeRaw="
            if self._myHasSizeRaw:
                leafStr = str(self.sizeRaw)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._mySizeRequested:
            x = "+Size="
            if self._myHasSize:
                leafStr = str(self.size)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{StatusOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+PhysicalIdList="
        if self._myHasPhysicalIdList:
            leafStr = str(self.physicalIdList)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myPhysicalIdListRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+Status="
        if self._myHasStatus:
            leafStr = str(self.status)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myStatusRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+StateRaw="
        if self._myHasStateRaw:
            leafStr = str(self.stateRaw)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myStateRawRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+ReadPolicy="
        if self._myHasReadPolicy:
            leafStr = str(self.readPolicy)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myReadPolicyRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+BadBlocks="
        if self._myHasBadBlocks:
            leafStr = str(self.badBlocks)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myBadBlocksRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+MediaType="
        if self._myHasMediaType:
            leafStr = str(self.mediaType)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myMediaTypeRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+HotSparePolicyViolation="
        if self._myHasHotSparePolicyViolation:
            leafStr = str(self.hotSparePolicyViolation)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myHotSparePolicyViolationRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+Id="
        if self._myHasId:
            leafStr = str(self.id)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myIdRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+State="
        if self._myHasState:
            leafStr = str(self.state)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myStateRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+StatusRaw="
        if self._myHasStatusRaw:
            leafStr = str(self.statusRaw)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myStatusRawRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+DiskCachePolicy="
        if self._myHasDiskCachePolicy:
            leafStr = str(self.diskCachePolicy)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myDiskCachePolicyRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+BadBlocksRaw="
        if self._myHasBadBlocksRaw:
            leafStr = str(self.badBlocksRaw)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myBadBlocksRawRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+CachePolicy="
        if self._myHasCachePolicy:
            leafStr = str(self.cachePolicy)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myCachePolicyRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+WritePolicy="
        if self._myHasWritePolicy:
            leafStr = str(self.writePolicy)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myWritePolicyRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+RaidType="
        if self._myHasRaidType:
            leafStr = str(self.raidType)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myRaidTypeRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+StripeElementSize="
        if self._myHasStripeElementSize:
            leafStr = str(self.stripeElementSize)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myStripeElementSizeRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+SizeRaw="
        if self._myHasSizeRaw:
            leafStr = str(self.sizeRaw)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._mySizeRawRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+Size="
        if self._myHasSize:
            leafStr = str(self.size)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._mySizeRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{StatusOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setPhysicalIdListRequested()
        self.setStatusRequested()
        self.setStateRawRequested()
        self.setReadPolicyRequested()
        self.setBadBlocksRequested()
        self.setMediaTypeRequested()
        self.setHotSparePolicyViolationRequested()
        self.setIdRequested()
        self.setStateRequested()
        self.setStatusRawRequested()
        self.setDiskCachePolicyRequested()
        self.setBadBlocksRawRequested()
        self.setCachePolicyRequested()
        self.setWritePolicyRequested()
        self.setRaidTypeRequested()
        self.setStripeElementSizeRequested()
        self.setSizeRawRequested()
        self.setSizeRequested()
        
        


    def setPhysicalIdList (self, physicalIdList):
        self.physicalIdList = physicalIdList
        self.setHasPhysicalIdList()

    def setStatus (self, status):
        self.status = status
        self.setHasStatus()

    def setStateRaw (self, stateRaw):
        self.stateRaw = stateRaw
        self.setHasStateRaw()

    def setReadPolicy (self, readPolicy):
        self.readPolicy = readPolicy
        self.setHasReadPolicy()

    def setBadBlocks (self, badBlocks):
        self.badBlocks = badBlocks
        self.setHasBadBlocks()

    def setMediaType (self, mediaType):
        self.mediaType = mediaType
        self.setHasMediaType()

    def setHotSparePolicyViolation (self, hotSparePolicyViolation):
        self.hotSparePolicyViolation = hotSparePolicyViolation
        self.setHasHotSparePolicyViolation()

    def setId (self, id):
        self.id = id
        self.setHasId()

    def setState (self, state):
        self.state = state
        self.setHasState()

    def setStatusRaw (self, statusRaw):
        self.statusRaw = statusRaw
        self.setHasStatusRaw()

    def setDiskCachePolicy (self, diskCachePolicy):
        self.diskCachePolicy = diskCachePolicy
        self.setHasDiskCachePolicy()

    def setBadBlocksRaw (self, badBlocksRaw):
        self.badBlocksRaw = badBlocksRaw
        self.setHasBadBlocksRaw()

    def setCachePolicy (self, cachePolicy):
        self.cachePolicy = cachePolicy
        self.setHasCachePolicy()

    def setWritePolicy (self, writePolicy):
        self.writePolicy = writePolicy
        self.setHasWritePolicy()

    def setRaidType (self, raidType):
        self.raidType = raidType
        self.setHasRaidType()

    def setStripeElementSize (self, stripeElementSize):
        self.stripeElementSize = stripeElementSize
        self.setHasStripeElementSize()

    def setSizeRaw (self, sizeRaw):
        self.sizeRaw = sizeRaw
        self.setHasSizeRaw()

    def setSize (self, size):
        self.size = size
        self.setHasSize()


"""
Extracted from the below data: 
{
    "node": {
        "className": "StatusOperData", 
        "namespace": "status", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.raid_array.status.status_oper_data_gen import StatusOperData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "storage", 
            "isCurrent": false
        }, 
        {
            "namespace": "disk", 
            "isCurrent": false
        }, 
        {
            "namespace": "raid_array", 
            "isCurrent": false
        }, 
        {
            "namespace": "status", 
            "isCurrent": true
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "physicalIdList", 
            "yangName": "physical-id-list", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "status", 
            "yangName": "status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "stateRaw", 
            "yangName": "state-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "readPolicy", 
            "yangName": "read-policy", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "badBlocks", 
            "yangName": "bad-blocks", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "mediaType", 
            "yangName": "media-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "hotSparePolicyViolation", 
            "yangName": "hot-spare-policy-violation", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "id", 
            "yangName": "id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "state", 
            "yangName": "state", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "statusRaw", 
            "yangName": "status-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "diskCachePolicy", 
            "yangName": "disk-cache-policy", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "badBlocksRaw", 
            "yangName": "bad-blocks-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "cachePolicy", 
            "yangName": "cache-policy", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "writePolicy", 
            "yangName": "write-policy", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "raidType", 
            "yangName": "raid-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "stripeElementSize", 
            "yangName": "stripe-element-size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "sizeRaw", 
            "yangName": "size-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
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
    "createTime": "2013"
}
"""


