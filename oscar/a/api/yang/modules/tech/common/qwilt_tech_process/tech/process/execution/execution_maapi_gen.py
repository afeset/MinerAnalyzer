


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

from execution_maapi_base_gen import ExecutionMaapiBase

from a.api.yang.modules.tech.common.qwilt_tech_process.tech.process.execution.status.status_maapi_gen import BlinkyStatusMaapi
from a.api.yang.modules.tech.common.qwilt_tech_process.tech.process.execution.command.command_maapi_gen import BlinkyCommandMaapi



class BlinkyExecutionMaapi(ExecutionMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-execution")
        self.domain = None

        
        self.statusObj = None
        
        self.commandObj = None
        

        
        self.priorityRequested = False
        self.priority = None
        self.prioritySet = False
        
        self.umaskRequested = False
        self.umask = None
        self.umaskSet = False
        
        self.affinityRequested = False
        self.affinity = None
        self.affinitySet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestPriority(True)
        
        self.requestUmask(True)
        
        self.requestAffinity(True)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.requestConfigAndOper()
        
        if not self.commandObj:
            self.commandObj = self.newCommand()
            self.commandObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestPriority(True)
        
        self.requestUmask(True)
        
        self.requestAffinity(True)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.requestConfig()
        
        if not self.commandObj:
            self.commandObj = self.newCommand()
            self.commandObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestPriority(False)
        
        self.requestUmask(False)
        
        self.requestAffinity(False)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.requestOper()
        
        if not self.commandObj:
            self.commandObj = self.newCommand()
            self.commandObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestPriority(False)
        
        self.requestUmask(False)
        
        self.requestAffinity(False)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.clearAllRequested()
        
        if not self.commandObj:
            self.commandObj = self.newCommand()
            self.commandObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setPriority(None)
        self.prioritySet = False
        
        self.setUmask(None)
        self.umaskSet = False
        
        self.setAffinity(None)
        self.affinitySet = False
        
        
        if self.statusObj:
            self.statusObj.clearAllSet()
        
        if self.commandObj:
            self.commandObj.clearAllSet()
        

    def write (self
              , process
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(process, trxContext)

    def read (self
              , process
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(process, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , process
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(process, 
                                  True,
                                  trxContext)

    def newStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-status').debug3Func(): logFunc('called.')
        status = BlinkyStatusMaapi(self._log)
        status.init(self.domain)
        return status

    def setStatusObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-status').debug3Func(): logFunc('called. obj=%s', obj)
        self.statusObj = obj

    def getStatusObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-status').debug3Func(): logFunc('called. self.statusObj=%s', self.statusObj)
        return self.statusObj

    def hasStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-status').debug3Func(): logFunc('called. self.statusObj=%s', self.statusObj)
        if self.statusObj:
            return True
        return False

    def newCommand (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-command').debug3Func(): logFunc('called.')
        command = BlinkyCommandMaapi(self._log)
        command.init(self.domain)
        return command

    def setCommandObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-command').debug3Func(): logFunc('called. obj=%s', obj)
        self.commandObj = obj

    def getCommandObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-command').debug3Func(): logFunc('called. self.commandObj=%s', self.commandObj)
        return self.commandObj

    def hasCommand (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-command').debug3Func(): logFunc('called. self.commandObj=%s', self.commandObj)
        if self.commandObj:
            return True
        return False



    def requestPriority (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-priority').debug3Func(): logFunc('called. requested=%s', requested)
        self.priorityRequested = requested
        self.prioritySet = False

    def isPriorityRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-priority-requested').debug3Func(): logFunc('called. requested=%s', self.priorityRequested)
        return self.priorityRequested

    def getPriority (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-priority').debug3Func(): logFunc('called. self.prioritySet=%s, self.priority=%s', self.prioritySet, self.priority)
        if self.prioritySet:
            return self.priority
        return None

    def hasPriority (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-priority').debug3Func(): logFunc('called. self.prioritySet=%s, self.priority=%s', self.prioritySet, self.priority)
        if self.prioritySet:
            return True
        return False

    def setPriority (self, priority):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-priority').debug3Func(): logFunc('called. priority=%s, old=%s', priority, self.priority)
        self.prioritySet = True
        self.priority = priority

    def requestUmask (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-umask').debug3Func(): logFunc('called. requested=%s', requested)
        self.umaskRequested = requested
        self.umaskSet = False

    def isUmaskRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-umask-requested').debug3Func(): logFunc('called. requested=%s', self.umaskRequested)
        return self.umaskRequested

    def getUmask (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-umask').debug3Func(): logFunc('called. self.umaskSet=%s, self.umask=%s', self.umaskSet, self.umask)
        if self.umaskSet:
            return self.umask
        return None

    def hasUmask (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-umask').debug3Func(): logFunc('called. self.umaskSet=%s, self.umask=%s', self.umaskSet, self.umask)
        if self.umaskSet:
            return True
        return False

    def setUmask (self, umask):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-umask').debug3Func(): logFunc('called. umask=%s, old=%s', umask, self.umask)
        self.umaskSet = True
        self.umask = umask

    def requestAffinity (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-affinity').debug3Func(): logFunc('called. requested=%s', requested)
        self.affinityRequested = requested
        self.affinitySet = False

    def isAffinityRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-affinity-requested').debug3Func(): logFunc('called. requested=%s', self.affinityRequested)
        return self.affinityRequested

    def getAffinity (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-affinity').debug3Func(): logFunc('called. self.affinitySet=%s, self.affinity=%s', self.affinitySet, self.affinity)
        if self.affinitySet:
            return self.affinity
        return None

    def hasAffinity (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-affinity').debug3Func(): logFunc('called. self.affinitySet=%s, self.affinity=%s', self.affinitySet, self.affinity)
        if self.affinitySet:
            return True
        return False

    def setAffinity (self, affinity):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-affinity').debug3Func(): logFunc('called. affinity=%s, old=%s', affinity, self.affinity)
        self.affinitySet = True
        self.affinity = affinity


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.statusObj:
            self.statusObj._clearAllReadData()
        
        if self.commandObj:
            self.commandObj._clearAllReadData()
        

        
        self.priority = 0
        self.prioritySet = False
        
        self.umask = 0
        self.umaskSet = False
        
        self.affinity = 0
        self.affinitySet = False
        

    def _getSelfKeyPath (self, process
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("execution", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", "qt-proc"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(process);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("process", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", "qt-proc"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        process, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(process, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(process, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       process, 
                       
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

        keyPath = self._getSelfKeyPath(process, 
                                       
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
                               process, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        
        if self.statusObj:
            res = self.statusObj._collectItemsToDelete(process, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-status-failed').errorFunc(): logFunc('statusObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.commandObj:
            res = self.commandObj._collectItemsToDelete(process, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-command-failed').errorFunc(): logFunc('commandObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasPriority():
            valPriority = Value()
            if self.priority is not None:
                valPriority.setString(self.priority)
            else:
                valPriority.setEmpty()
            tagValueList.push(("priority", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"), valPriority)
        
        if self.hasUmask():
            valUmask = Value()
            if self.umask is not None:
                valUmask.setUint64(self.umask)
            else:
                valUmask.setEmpty()
            tagValueList.push(("umask", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"), valUmask)
        
        if self.hasAffinity():
            valAffinity = Value()
            if self.affinity is not None:
                valAffinity.setString(self.affinity)
            else:
                valAffinity.setEmpty()
            tagValueList.push(("affinity", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"), valAffinity)
        

        
        if self.statusObj:
            valBegin = Value()
            (tag, ns, prefix) = ("status" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", "qt-proc")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.statusObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-status-failed').errorFunc(): logFunc('statusObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.commandObj:
            valBegin = Value()
            (tag, ns, prefix) = ("command" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", "qt-proc")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.commandObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-command-failed').errorFunc(): logFunc('commandObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isPriorityRequested():
            valPriority = Value()
            valPriority.setEmpty()
            tagValueList.push(("priority", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"), valPriority)
        
        if self.isUmaskRequested():
            valUmask = Value()
            valUmask.setEmpty()
            tagValueList.push(("umask", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"), valUmask)
        
        if self.isAffinityRequested():
            valAffinity = Value()
            valAffinity.setEmpty()
            tagValueList.push(("affinity", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"), valAffinity)
        

        
        if self.statusObj:
            valBegin = Value()
            (tag, ns, prefix) = ("status" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", "qt-proc")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.statusObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-status-failed').errorFunc(): logFunc('statusObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.commandObj:
            valBegin = Value()
            (tag, ns, prefix) = ("command" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", "qt-proc")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.commandObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-command-failed').errorFunc(): logFunc('commandObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isPriorityRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "priority") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-priority').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "priority", "priority", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-priority-bad-value').infoFunc(): logFunc('priority not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPriority(tempVar)
            for logFunc in self._log('read-tag-values-priority').debug3Func(): logFunc('read priority. priority=%s, tempValue=%s', self.priority, tempValue.getType())
        
        if self.isUmaskRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "umask") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-umask').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "umask", "umask", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-umask-bad-value').infoFunc(): logFunc('umask not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setUmask(tempVar)
            for logFunc in self._log('read-tag-values-umask').debug3Func(): logFunc('read umask. umask=%s, tempValue=%s', self.umask, tempValue.getType())
        
        if self.isAffinityRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "affinity") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-affinity').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "affinity", "affinity", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-affinity-bad-value').infoFunc(): logFunc('affinity not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setAffinity(tempVar)
            for logFunc in self._log('read-tag-values-affinity').debug3Func(): logFunc('read affinity. affinity=%s, tempValue=%s', self.affinity, tempValue.getType())
        

        
        if self.statusObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "status") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.statusObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-status-failed').errorFunc(): logFunc('statusObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "status") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.commandObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "command") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "command", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.commandObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-command-failed').errorFunc(): logFunc('commandObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "command") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "command", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "execution", 
        "namespace": "execution", 
        "className": "ExecutionMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_process.tech.process.execution.execution_maapi_gen import ExecutionMaapi", 
        "baseClassName": "ExecutionMaapiBase", 
        "baseModule": "execution_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-proc", 
            "isCurrent": false, 
            "yangName": "process", 
            "namespace": "process", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "keyLeaf": {
                "varName": "process", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "process"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-proc", 
            "yangName": "execution", 
            "namespace": "execution", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "name": "execution"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-proc", 
            "memberName": "status", 
            "yangName": "status", 
            "className": "BlinkyStatusMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_process.tech.process.execution.status.status_maapi_gen import BlinkyStatusMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-proc", 
            "memberName": "command", 
            "yangName": "command", 
            "className": "BlinkyCommandMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_process.tech.process.execution.command.command_maapi_gen import BlinkyCommandMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "priority", 
            "yangName": "priority", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "umask", 
            "yangName": "umask", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "affinity", 
            "yangName": "affinity", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
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
            "qwilt_tech_process"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "priority", 
            "yangName": "priority", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "umask", 
            "yangName": "umask", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "affinity", 
            "yangName": "affinity", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


