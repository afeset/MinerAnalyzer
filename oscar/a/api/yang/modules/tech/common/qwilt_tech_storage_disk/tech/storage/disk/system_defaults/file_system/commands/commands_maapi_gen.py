


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

from commands_maapi_base_gen import CommandsMaapiBase




class BlinkyCommandsMaapi(CommandsMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-commands")
        self.domain = None

        

        
        self.postMountRequested = False
        self.postMount = None
        self.postMountSet = False
        
        self.preMountExtrasRequested = False
        self.preMountExtras = None
        self.preMountExtrasSet = False
        
        self.preMountRequested = False
        self.preMount = None
        self.preMountSet = False
        
        self.postMountExtrasRequested = False
        self.postMountExtras = None
        self.postMountExtrasSet = False
        
        self.mkfsRequested = False
        self.mkfs = None
        self.mkfsSet = False
        
        self.mkfsExtrasRequested = False
        self.mkfsExtras = None
        self.mkfsExtrasSet = False
        
        self.mountExtrasRequested = False
        self.mountExtras = None
        self.mountExtrasSet = False
        
        self.mountRequested = False
        self.mount = None
        self.mountSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestPostMount(True)
        
        self.requestPreMountExtras(True)
        
        self.requestPreMount(True)
        
        self.requestPostMountExtras(True)
        
        self.requestMkfs(True)
        
        self.requestMkfsExtras(True)
        
        self.requestMountExtras(True)
        
        self.requestMount(True)
        
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestPostMount(True)
        
        self.requestPreMountExtras(True)
        
        self.requestPreMount(True)
        
        self.requestPostMountExtras(True)
        
        self.requestMkfs(True)
        
        self.requestMkfsExtras(True)
        
        self.requestMountExtras(True)
        
        self.requestMount(True)
        
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestPostMount(False)
        
        self.requestPreMountExtras(False)
        
        self.requestPreMount(False)
        
        self.requestPostMountExtras(False)
        
        self.requestMkfs(False)
        
        self.requestMkfsExtras(False)
        
        self.requestMountExtras(False)
        
        self.requestMount(False)
        
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestPostMount(False)
        
        self.requestPreMountExtras(False)
        
        self.requestPreMount(False)
        
        self.requestPostMountExtras(False)
        
        self.requestMkfs(False)
        
        self.requestMkfsExtras(False)
        
        self.requestMountExtras(False)
        
        self.requestMount(False)
        
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setPostMount(None)
        self.postMountSet = False
        
        self.setPreMountExtras(None)
        self.preMountExtrasSet = False
        
        self.setPreMount(None)
        self.preMountSet = False
        
        self.setPostMountExtras(None)
        self.postMountExtrasSet = False
        
        self.setMkfs(None)
        self.mkfsSet = False
        
        self.setMkfsExtras(None)
        self.mkfsExtrasSet = False
        
        self.setMountExtras(None)
        self.mountExtrasSet = False
        
        self.setMount(None)
        self.mountSet = False
        
        

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



    def requestPostMount (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-postmount').debug3Func(): logFunc('called. requested=%s', requested)
        self.postMountRequested = requested
        self.postMountSet = False

    def isPostMountRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-postmount-requested').debug3Func(): logFunc('called. requested=%s', self.postMountRequested)
        return self.postMountRequested

    def getPostMount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-postmount').debug3Func(): logFunc('called. self.postMountSet=%s, self.postMount=%s', self.postMountSet, self.postMount)
        if self.postMountSet:
            return self.postMount
        return None

    def hasPostMount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-postmount').debug3Func(): logFunc('called. self.postMountSet=%s, self.postMount=%s', self.postMountSet, self.postMount)
        if self.postMountSet:
            return True
        return False

    def setPostMount (self, postMount):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-postmount').debug3Func(): logFunc('called. postMount=%s, old=%s', postMount, self.postMount)
        self.postMountSet = True
        self.postMount = postMount

    def requestPreMountExtras (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-premountextras').debug3Func(): logFunc('called. requested=%s', requested)
        self.preMountExtrasRequested = requested
        self.preMountExtrasSet = False

    def isPreMountExtrasRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-premountextras-requested').debug3Func(): logFunc('called. requested=%s', self.preMountExtrasRequested)
        return self.preMountExtrasRequested

    def getPreMountExtras (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-premountextras').debug3Func(): logFunc('called. self.preMountExtrasSet=%s, self.preMountExtras=%s', self.preMountExtrasSet, self.preMountExtras)
        if self.preMountExtrasSet:
            return self.preMountExtras
        return None

    def hasPreMountExtras (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-premountextras').debug3Func(): logFunc('called. self.preMountExtrasSet=%s, self.preMountExtras=%s', self.preMountExtrasSet, self.preMountExtras)
        if self.preMountExtrasSet:
            return True
        return False

    def setPreMountExtras (self, preMountExtras):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-premountextras').debug3Func(): logFunc('called. preMountExtras=%s, old=%s', preMountExtras, self.preMountExtras)
        self.preMountExtrasSet = True
        self.preMountExtras = preMountExtras

    def requestPreMount (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-premount').debug3Func(): logFunc('called. requested=%s', requested)
        self.preMountRequested = requested
        self.preMountSet = False

    def isPreMountRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-premount-requested').debug3Func(): logFunc('called. requested=%s', self.preMountRequested)
        return self.preMountRequested

    def getPreMount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-premount').debug3Func(): logFunc('called. self.preMountSet=%s, self.preMount=%s', self.preMountSet, self.preMount)
        if self.preMountSet:
            return self.preMount
        return None

    def hasPreMount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-premount').debug3Func(): logFunc('called. self.preMountSet=%s, self.preMount=%s', self.preMountSet, self.preMount)
        if self.preMountSet:
            return True
        return False

    def setPreMount (self, preMount):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-premount').debug3Func(): logFunc('called. preMount=%s, old=%s', preMount, self.preMount)
        self.preMountSet = True
        self.preMount = preMount

    def requestPostMountExtras (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-postmountextras').debug3Func(): logFunc('called. requested=%s', requested)
        self.postMountExtrasRequested = requested
        self.postMountExtrasSet = False

    def isPostMountExtrasRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-postmountextras-requested').debug3Func(): logFunc('called. requested=%s', self.postMountExtrasRequested)
        return self.postMountExtrasRequested

    def getPostMountExtras (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-postmountextras').debug3Func(): logFunc('called. self.postMountExtrasSet=%s, self.postMountExtras=%s', self.postMountExtrasSet, self.postMountExtras)
        if self.postMountExtrasSet:
            return self.postMountExtras
        return None

    def hasPostMountExtras (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-postmountextras').debug3Func(): logFunc('called. self.postMountExtrasSet=%s, self.postMountExtras=%s', self.postMountExtrasSet, self.postMountExtras)
        if self.postMountExtrasSet:
            return True
        return False

    def setPostMountExtras (self, postMountExtras):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-postmountextras').debug3Func(): logFunc('called. postMountExtras=%s, old=%s', postMountExtras, self.postMountExtras)
        self.postMountExtrasSet = True
        self.postMountExtras = postMountExtras

    def requestMkfs (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-mkfs').debug3Func(): logFunc('called. requested=%s', requested)
        self.mkfsRequested = requested
        self.mkfsSet = False

    def isMkfsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-mkfs-requested').debug3Func(): logFunc('called. requested=%s', self.mkfsRequested)
        return self.mkfsRequested

    def getMkfs (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-mkfs').debug3Func(): logFunc('called. self.mkfsSet=%s, self.mkfs=%s', self.mkfsSet, self.mkfs)
        if self.mkfsSet:
            return self.mkfs
        return None

    def hasMkfs (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-mkfs').debug3Func(): logFunc('called. self.mkfsSet=%s, self.mkfs=%s', self.mkfsSet, self.mkfs)
        if self.mkfsSet:
            return True
        return False

    def setMkfs (self, mkfs):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-mkfs').debug3Func(): logFunc('called. mkfs=%s, old=%s', mkfs, self.mkfs)
        self.mkfsSet = True
        self.mkfs = mkfs

    def requestMkfsExtras (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-mkfsextras').debug3Func(): logFunc('called. requested=%s', requested)
        self.mkfsExtrasRequested = requested
        self.mkfsExtrasSet = False

    def isMkfsExtrasRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-mkfsextras-requested').debug3Func(): logFunc('called. requested=%s', self.mkfsExtrasRequested)
        return self.mkfsExtrasRequested

    def getMkfsExtras (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-mkfsextras').debug3Func(): logFunc('called. self.mkfsExtrasSet=%s, self.mkfsExtras=%s', self.mkfsExtrasSet, self.mkfsExtras)
        if self.mkfsExtrasSet:
            return self.mkfsExtras
        return None

    def hasMkfsExtras (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-mkfsextras').debug3Func(): logFunc('called. self.mkfsExtrasSet=%s, self.mkfsExtras=%s', self.mkfsExtrasSet, self.mkfsExtras)
        if self.mkfsExtrasSet:
            return True
        return False

    def setMkfsExtras (self, mkfsExtras):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-mkfsextras').debug3Func(): logFunc('called. mkfsExtras=%s, old=%s', mkfsExtras, self.mkfsExtras)
        self.mkfsExtrasSet = True
        self.mkfsExtras = mkfsExtras

    def requestMountExtras (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-mountextras').debug3Func(): logFunc('called. requested=%s', requested)
        self.mountExtrasRequested = requested
        self.mountExtrasSet = False

    def isMountExtrasRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-mountextras-requested').debug3Func(): logFunc('called. requested=%s', self.mountExtrasRequested)
        return self.mountExtrasRequested

    def getMountExtras (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-mountextras').debug3Func(): logFunc('called. self.mountExtrasSet=%s, self.mountExtras=%s', self.mountExtrasSet, self.mountExtras)
        if self.mountExtrasSet:
            return self.mountExtras
        return None

    def hasMountExtras (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-mountextras').debug3Func(): logFunc('called. self.mountExtrasSet=%s, self.mountExtras=%s', self.mountExtrasSet, self.mountExtras)
        if self.mountExtrasSet:
            return True
        return False

    def setMountExtras (self, mountExtras):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-mountextras').debug3Func(): logFunc('called. mountExtras=%s, old=%s', mountExtras, self.mountExtras)
        self.mountExtrasSet = True
        self.mountExtras = mountExtras

    def requestMount (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-mount').debug3Func(): logFunc('called. requested=%s', requested)
        self.mountRequested = requested
        self.mountSet = False

    def isMountRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-mount-requested').debug3Func(): logFunc('called. requested=%s', self.mountRequested)
        return self.mountRequested

    def getMount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-mount').debug3Func(): logFunc('called. self.mountSet=%s, self.mount=%s', self.mountSet, self.mount)
        if self.mountSet:
            return self.mount
        return None

    def hasMount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-mount').debug3Func(): logFunc('called. self.mountSet=%s, self.mount=%s', self.mountSet, self.mount)
        if self.mountSet:
            return True
        return False

    def setMount (self, mount):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-mount').debug3Func(): logFunc('called. mount=%s, old=%s', mount, self.mount)
        self.mountSet = True
        self.mount = mount


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.postMount = 0
        self.postMountSet = False
        
        self.preMountExtras = 0
        self.preMountExtrasSet = False
        
        self.preMount = 0
        self.preMountSet = False
        
        self.postMountExtras = 0
        self.postMountExtrasSet = False
        
        self.mkfs = 0
        self.mkfsSet = False
        
        self.mkfsExtras = 0
        self.mkfsExtrasSet = False
        
        self.mountExtras = 0
        self.mountExtrasSet = False
        
        self.mount = 0
        self.mountSet = False
        

    def _getSelfKeyPath (self, disk
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("commands", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("file-system", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk"))
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

        
        if self.hasPostMount():
            valPostMount = Value()
            if self.postMount is not None:
                valPostMount.setString(self.postMount)
            else:
                valPostMount.setEmpty()
            tagValueList.push(("post-mount", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valPostMount)
        
        if self.hasPreMountExtras():
            valPreMountExtras = Value()
            if self.preMountExtras is not None:
                valPreMountExtras.setString(self.preMountExtras)
            else:
                valPreMountExtras.setEmpty()
            tagValueList.push(("pre-mount-extras", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valPreMountExtras)
        
        if self.hasPreMount():
            valPreMount = Value()
            if self.preMount is not None:
                valPreMount.setString(self.preMount)
            else:
                valPreMount.setEmpty()
            tagValueList.push(("pre-mount", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valPreMount)
        
        if self.hasPostMountExtras():
            valPostMountExtras = Value()
            if self.postMountExtras is not None:
                valPostMountExtras.setString(self.postMountExtras)
            else:
                valPostMountExtras.setEmpty()
            tagValueList.push(("post-mount-extras", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valPostMountExtras)
        
        if self.hasMkfs():
            valMkfs = Value()
            if self.mkfs is not None:
                valMkfs.setString(self.mkfs)
            else:
                valMkfs.setEmpty()
            tagValueList.push(("mkfs", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valMkfs)
        
        if self.hasMkfsExtras():
            valMkfsExtras = Value()
            if self.mkfsExtras is not None:
                valMkfsExtras.setString(self.mkfsExtras)
            else:
                valMkfsExtras.setEmpty()
            tagValueList.push(("mkfs-extras", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valMkfsExtras)
        
        if self.hasMountExtras():
            valMountExtras = Value()
            if self.mountExtras is not None:
                valMountExtras.setString(self.mountExtras)
            else:
                valMountExtras.setEmpty()
            tagValueList.push(("mount-extras", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valMountExtras)
        
        if self.hasMount():
            valMount = Value()
            if self.mount is not None:
                valMount.setString(self.mount)
            else:
                valMount.setEmpty()
            tagValueList.push(("mount", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valMount)
        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isPostMountRequested():
            valPostMount = Value()
            valPostMount.setEmpty()
            tagValueList.push(("post-mount", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valPostMount)
        
        if self.isPreMountExtrasRequested():
            valPreMountExtras = Value()
            valPreMountExtras.setEmpty()
            tagValueList.push(("pre-mount-extras", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valPreMountExtras)
        
        if self.isPreMountRequested():
            valPreMount = Value()
            valPreMount.setEmpty()
            tagValueList.push(("pre-mount", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valPreMount)
        
        if self.isPostMountExtrasRequested():
            valPostMountExtras = Value()
            valPostMountExtras.setEmpty()
            tagValueList.push(("post-mount-extras", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valPostMountExtras)
        
        if self.isMkfsRequested():
            valMkfs = Value()
            valMkfs.setEmpty()
            tagValueList.push(("mkfs", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valMkfs)
        
        if self.isMkfsExtrasRequested():
            valMkfsExtras = Value()
            valMkfsExtras.setEmpty()
            tagValueList.push(("mkfs-extras", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valMkfsExtras)
        
        if self.isMountExtrasRequested():
            valMountExtras = Value()
            valMountExtras.setEmpty()
            tagValueList.push(("mount-extras", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valMountExtras)
        
        if self.isMountRequested():
            valMount = Value()
            valMount.setEmpty()
            tagValueList.push(("mount", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valMount)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isPostMountRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "post-mount") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-postmount').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "postMount", "post-mount", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-post-mount-bad-value').infoFunc(): logFunc('postMount not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPostMount(tempVar)
            for logFunc in self._log('read-tag-values-post-mount').debug3Func(): logFunc('read postMount. postMount=%s, tempValue=%s', self.postMount, tempValue.getType())
        
        if self.isPreMountExtrasRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "pre-mount-extras") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-premountextras').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "preMountExtras", "pre-mount-extras", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-pre-mount-extras-bad-value').infoFunc(): logFunc('preMountExtras not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPreMountExtras(tempVar)
            for logFunc in self._log('read-tag-values-pre-mount-extras').debug3Func(): logFunc('read preMountExtras. preMountExtras=%s, tempValue=%s', self.preMountExtras, tempValue.getType())
        
        if self.isPreMountRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "pre-mount") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-premount').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "preMount", "pre-mount", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-pre-mount-bad-value').infoFunc(): logFunc('preMount not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPreMount(tempVar)
            for logFunc in self._log('read-tag-values-pre-mount').debug3Func(): logFunc('read preMount. preMount=%s, tempValue=%s', self.preMount, tempValue.getType())
        
        if self.isPostMountExtrasRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "post-mount-extras") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-postmountextras').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "postMountExtras", "post-mount-extras", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-post-mount-extras-bad-value').infoFunc(): logFunc('postMountExtras not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPostMountExtras(tempVar)
            for logFunc in self._log('read-tag-values-post-mount-extras').debug3Func(): logFunc('read postMountExtras. postMountExtras=%s, tempValue=%s', self.postMountExtras, tempValue.getType())
        
        if self.isMkfsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "mkfs") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-mkfs').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "mkfs", "mkfs", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-mkfs-bad-value').infoFunc(): logFunc('mkfs not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMkfs(tempVar)
            for logFunc in self._log('read-tag-values-mkfs').debug3Func(): logFunc('read mkfs. mkfs=%s, tempValue=%s', self.mkfs, tempValue.getType())
        
        if self.isMkfsExtrasRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "mkfs-extras") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-mkfsextras').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "mkfsExtras", "mkfs-extras", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-mkfs-extras-bad-value').infoFunc(): logFunc('mkfsExtras not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMkfsExtras(tempVar)
            for logFunc in self._log('read-tag-values-mkfs-extras').debug3Func(): logFunc('read mkfsExtras. mkfsExtras=%s, tempValue=%s', self.mkfsExtras, tempValue.getType())
        
        if self.isMountExtrasRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "mount-extras") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-mountextras').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "mountExtras", "mount-extras", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-mount-extras-bad-value').infoFunc(): logFunc('mountExtras not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMountExtras(tempVar)
            for logFunc in self._log('read-tag-values-mount-extras').debug3Func(): logFunc('read mountExtras. mountExtras=%s, tempValue=%s', self.mountExtras, tempValue.getType())
        
        if self.isMountRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "mount") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-mount').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "mount", "mount", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-mount-bad-value').infoFunc(): logFunc('mount not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMount(tempVar)
            for logFunc in self._log('read-tag-values-mount').debug3Func(): logFunc('read mount. mount=%s, tempValue=%s', self.mount, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "commands", 
        "namespace": "commands", 
        "className": "CommandsMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.system_defaults.file_system.commands.commands_maapi_gen import CommandsMaapi", 
        "baseClassName": "CommandsMaapiBase", 
        "baseModule": "commands_maapi_base_gen"
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
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "name": "file-system"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "yangName": "commands", 
            "namespace": "commands", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "name": "commands"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "postMount", 
            "yangName": "post-mount", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "preMountExtras", 
            "yangName": "pre-mount-extras", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "preMount", 
            "yangName": "pre-mount", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "postMountExtras", 
            "yangName": "post-mount-extras", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "mkfs", 
            "yangName": "mkfs", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "mkfsExtras", 
            "yangName": "mkfs-extras", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "mountExtras", 
            "yangName": "mount-extras", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "mount", 
            "yangName": "mount", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }
    ], 
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
            "memberName": "postMount", 
            "yangName": "post-mount", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "preMountExtras", 
            "yangName": "pre-mount-extras", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "preMount", 
            "yangName": "pre-mount", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "postMountExtras", 
            "yangName": "post-mount-extras", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "mkfs", 
            "yangName": "mkfs", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "mkfsExtras", 
            "yangName": "mkfs-extras", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "mountExtras", 
            "yangName": "mount-extras", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "mount", 
            "yangName": "mount", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


