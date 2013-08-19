



# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

# Must be set here to avoid stupid warnings about stuff in BlinkyOperContainer
__pychecker__="no-classattr"

from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.raid_array.status.status_oper_data_gen import StatusOperData
from a.sys.blinky.blinky_oper_node import BlinkyOperNode
from a.sys.confd.pyconfdlib.key_path import KeyPath
from a.sys.confd.pyconfdlib.value import Value
from a.sys.confd.pyconfdlib.tag_values import TagValues

from a.infra.misc.timeout_guard import TimeoutGuard
from a.infra.basic.return_codes import ReturnCodes
from a.sys.blinky.pass_by_ref import PassByRef






from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import RaidArrayStatusType
from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import RaidArrayStateType



class BlinkyOperStatus(BlinkyOperNode):

    _kCallpointName = "tech-storage-disk-raid-array-status-callpoint"

    GET_OBJ_FUNCTOR = 'GET_OBJ_FUNCTOR'

    


    def __init__ (self, logger):
        BlinkyOperNode.__init__(self, logger)
        self.kCallpointName = "tech-storage-disk-raid-array-status-callpoint"
        
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
        val.setXmlTag(("status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk"))
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
            
                
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "physical-id-list"):
                    for logFunc in self._log("set-oper-data-requested-fields-physicalidlist-requested").debug3Func(): logFunc(
                        "physical-id-list requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setPhysicalIdListRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "status"):
                    for logFunc in self._log("set-oper-data-requested-fields-status-requested").debug3Func(): logFunc(
                        "status requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setStatusRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "state-raw"):
                    for logFunc in self._log("set-oper-data-requested-fields-stateraw-requested").debug3Func(): logFunc(
                        "state-raw requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setStateRawRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "read-policy"):
                    for logFunc in self._log("set-oper-data-requested-fields-readpolicy-requested").debug3Func(): logFunc(
                        "read-policy requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setReadPolicyRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "bad-blocks"):
                    for logFunc in self._log("set-oper-data-requested-fields-badblocks-requested").debug3Func(): logFunc(
                        "bad-blocks requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setBadBlocksRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "media-type"):
                    for logFunc in self._log("set-oper-data-requested-fields-mediatype-requested").debug3Func(): logFunc(
                        "media-type requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setMediaTypeRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "hot-spare-policy-violation"):
                    for logFunc in self._log("set-oper-data-requested-fields-hotsparepolicyviolation-requested").debug3Func(): logFunc(
                        "hot-spare-policy-violation requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setHotSparePolicyViolationRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "id"):
                    for logFunc in self._log("set-oper-data-requested-fields-id-requested").debug3Func(): logFunc(
                        "id requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setIdRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "state"):
                    for logFunc in self._log("set-oper-data-requested-fields-state-requested").debug3Func(): logFunc(
                        "state requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setStateRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "status-raw"):
                    for logFunc in self._log("set-oper-data-requested-fields-statusraw-requested").debug3Func(): logFunc(
                        "status-raw requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setStatusRawRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "disk-cache-policy"):
                    for logFunc in self._log("set-oper-data-requested-fields-diskcachepolicy-requested").debug3Func(): logFunc(
                        "disk-cache-policy requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setDiskCachePolicyRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "bad-blocks-raw"):
                    for logFunc in self._log("set-oper-data-requested-fields-badblocksraw-requested").debug3Func(): logFunc(
                        "bad-blocks-raw requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setBadBlocksRawRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "cache-policy"):
                    for logFunc in self._log("set-oper-data-requested-fields-cachepolicy-requested").debug3Func(): logFunc(
                        "cache-policy requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setCachePolicyRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "write-policy"):
                    for logFunc in self._log("set-oper-data-requested-fields-writepolicy-requested").debug3Func(): logFunc(
                        "write-policy requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setWritePolicyRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "raid-type"):
                    for logFunc in self._log("set-oper-data-requested-fields-raidtype-requested").debug3Func(): logFunc(
                        "raid-type requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setRaidTypeRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "stripe-element-size"):
                    for logFunc in self._log("set-oper-data-requested-fields-stripeelementsize-requested").debug3Func(): logFunc(
                        "stripe-element-size requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setStripeElementSizeRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "size-raw"):
                    for logFunc in self._log("set-oper-data-requested-fields-sizeraw-requested").debug3Func(): logFunc(
                        "size-raw requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setSizeRawRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "size"):
                    for logFunc in self._log("set-oper-data-requested-fields-size-requested").debug3Func(): logFunc(
                        "size requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setSizeRequested()
                
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
        
        if operData.isPhysicalIdListRequested() and operData.hasPhysicalIdList():
            val = Value()
            val.setString(operData.physicalIdList)
            tagValueList.push(("physical-id-list", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isStatusRequested() and operData.hasStatus():
            val = Value()
            val.setEnum(operData.status.getValue())
            tagValueList.push(("status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isStateRawRequested() and operData.hasStateRaw():
            val = Value()
            val.setString(operData.stateRaw)
            tagValueList.push(("state-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isReadPolicyRequested() and operData.hasReadPolicy():
            val = Value()
            val.setString(operData.readPolicy)
            tagValueList.push(("read-policy", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isBadBlocksRequested() and operData.hasBadBlocks():
            val = Value()
            val.setBool(operData.badBlocks)
            tagValueList.push(("bad-blocks", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isMediaTypeRequested() and operData.hasMediaType():
            val = Value()
            val.setString(operData.mediaType)
            tagValueList.push(("media-type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isHotSparePolicyViolationRequested() and operData.hasHotSparePolicyViolation():
            val = Value()
            val.setString(operData.hotSparePolicyViolation)
            tagValueList.push(("hot-spare-policy-violation", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isIdRequested() and operData.hasId():
            val = Value()
            val.setString(operData.id)
            tagValueList.push(("id", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isStateRequested() and operData.hasState():
            val = Value()
            val.setEnum(operData.state.getValue())
            tagValueList.push(("state", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isStatusRawRequested() and operData.hasStatusRaw():
            val = Value()
            val.setString(operData.statusRaw)
            tagValueList.push(("status-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isDiskCachePolicyRequested() and operData.hasDiskCachePolicy():
            val = Value()
            val.setString(operData.diskCachePolicy)
            tagValueList.push(("disk-cache-policy", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isBadBlocksRawRequested() and operData.hasBadBlocksRaw():
            val = Value()
            val.setString(operData.badBlocksRaw)
            tagValueList.push(("bad-blocks-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isCachePolicyRequested() and operData.hasCachePolicy():
            val = Value()
            val.setString(operData.cachePolicy)
            tagValueList.push(("cache-policy", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isWritePolicyRequested() and operData.hasWritePolicy():
            val = Value()
            val.setString(operData.writePolicy)
            tagValueList.push(("write-policy", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isRaidTypeRequested() and operData.hasRaidType():
            val = Value()
            val.setString(operData.raidType)
            tagValueList.push(("raid-type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isStripeElementSizeRequested() and operData.hasStripeElementSize():
            val = Value()
            val.setString(operData.stripeElementSize)
            tagValueList.push(("stripe-element-size", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isSizeRawRequested() and operData.hasSizeRaw():
            val = Value()
            val.setString(operData.sizeRaw)
            tagValueList.push(("size-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isSizeRequested() and operData.hasSize():
            val = Value()
            val.setInt64(operData.size)
            tagValueList.push(("size", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        
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
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "physical-id-list"):
            if operData.isPhysicalIdListRequested():
                 if operData.hasPhysicalIdList():
                     value.setString(operData.physicalIdList)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "status"):
            if operData.isStatusRequested():
                 if operData.hasStatus():
                     value.setEnum(operData.status.getValue())
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "state-raw"):
            if operData.isStateRawRequested():
                 if operData.hasStateRaw():
                     value.setString(operData.stateRaw)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "read-policy"):
            if operData.isReadPolicyRequested():
                 if operData.hasReadPolicy():
                     value.setString(operData.readPolicy)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "bad-blocks"):
            if operData.isBadBlocksRequested():
                 if operData.hasBadBlocks():
                     value.setBool(operData.badBlocks)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "media-type"):
            if operData.isMediaTypeRequested():
                 if operData.hasMediaType():
                     value.setString(operData.mediaType)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "hot-spare-policy-violation"):
            if operData.isHotSparePolicyViolationRequested():
                 if operData.hasHotSparePolicyViolation():
                     value.setString(operData.hotSparePolicyViolation)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "id"):
            if operData.isIdRequested():
                 if operData.hasId():
                     value.setString(operData.id)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "state"):
            if operData.isStateRequested():
                 if operData.hasState():
                     value.setEnum(operData.state.getValue())
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "status-raw"):
            if operData.isStatusRawRequested():
                 if operData.hasStatusRaw():
                     value.setString(operData.statusRaw)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "disk-cache-policy"):
            if operData.isDiskCachePolicyRequested():
                 if operData.hasDiskCachePolicy():
                     value.setString(operData.diskCachePolicy)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "bad-blocks-raw"):
            if operData.isBadBlocksRawRequested():
                 if operData.hasBadBlocksRaw():
                     value.setString(operData.badBlocksRaw)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "cache-policy"):
            if operData.isCachePolicyRequested():
                 if operData.hasCachePolicy():
                     value.setString(operData.cachePolicy)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "write-policy"):
            if operData.isWritePolicyRequested():
                 if operData.hasWritePolicy():
                     value.setString(operData.writePolicy)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "raid-type"):
            if operData.isRaidTypeRequested():
                 if operData.hasRaidType():
                     value.setString(operData.raidType)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "stripe-element-size"):
            if operData.isStripeElementSizeRequested():
                 if operData.hasStripeElementSize():
                     value.setString(operData.stripeElementSize)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "size-raw"):
            if operData.isSizeRawRequested():
                 if operData.hasSizeRaw():
                     value.setString(operData.sizeRaw)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "size"):
            if operData.isSizeRequested():
                 if operData.hasSize():
                     value.setInt64(operData.size)
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
        operData = StatusOperData()

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

        operData = StatusOperData()
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
        "dataImportStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.raid_array.status.status_oper_data_gen import StatusOperData", 
        "callpointResponsible": true, 
        "moduleYangNamespacePrefix": "qt-strg-dsk", 
        "validationPoint": null, 
        "getNextArgsNum": 4, 
        "yangName": "status", 
        "namespace": "status", 
        "logGroupName": "blinky-status-oper", 
        "className": "BlinkyOperStatus", 
        "logModuleName": "a-storage-disk-tech-storage-tech-storage-disk-raid-array-status-blinky-status-oper-gen", 
        "importStatement": "from a.storage.disk.tech_storage.tech.storage.disk.raid_array.status.blinky_status_oper_gen import BlinkyOperStatus", 
        "callpointName": "tech-storage-disk-raid-array-status-callpoint", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
        "dataClassName": "StatusOperData", 
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
            "moduleYangNamespacePrefix": "qt-strg", 
            "yangName": "storage", 
            "namespace": "storage", 
            "isCurrent": false, 
            "isList": false, 
            "isOper": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage", 
            "name": "storage"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "isCurrent": false, 
            "yangName": "disk", 
            "namespace": "disk", 
            "isList": true, 
            "isOper": false, 
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
            "isOper": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "name": "raid-array"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "yangName": "status", 
            "namespace": "status", 
            "isCurrent": true, 
            "isList": false, 
            "isOper": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "name": "status"
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
    "env": [
        "a", 
        "storage", 
        "disk", 
        "tech_storage"
    ], 
    "createTime": "2013"
}
"""


