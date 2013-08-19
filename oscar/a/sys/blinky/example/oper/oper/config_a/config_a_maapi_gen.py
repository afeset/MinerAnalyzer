


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

from config_a_maapi_base_gen import ConfigAMaapiBase

from a.sys.blinky.example.oper.oper.config_a.op_n.op_n_maapi_gen import BlinkyOpNMaapi
from a.sys.blinky.example.oper.oper.config_a.op_l.op_l_maapi_gen import BlinkyOpLMaapi
from a.sys.blinky.example.oper.oper.config_a.op_m.op_m_maapi_gen import BlinkyOpMMaapi
from a.sys.blinky.example.oper.oper.config_a.op_b.op_b_maapi_gen import BlinkyOpBMaapi
from a.sys.blinky.example.oper.oper.config_a.config_q.config_q_maapi_gen import BlinkyConfigQMaapi
from a.sys.blinky.example.oper.oper.config_a.config_p.config_p_maapi_list_gen import BlinkyConfigPMaapiList
from a.sys.blinky.example.oper.oper.config_a.config_u.config_u_maapi_list_gen import BlinkyConfigUMaapiList
from a.sys.blinky.example.oper.oper.config_a.op_v.op_v_maapi_list_gen import BlinkyOpVMaapiList



class BlinkyConfigAMaapi(ConfigAMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-configA")
        self.domain = None

        
        self.opNObj = None
        
        self.opLObj = None
        
        self.opMObj = None
        
        self.opBObj = None
        
        self.configQObj = None
        
        self.configPListObj = None
        
        self.configUListObj = None
        
        self.opVListObj = None
        

        
        self.opZRequested = False
        self.opZ = None
        self.opZSet = False
        
        self.opYRequested = False
        self.opY = None
        self.opYSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestOpZ(True)
        
        self.requestOpY(True)
        
        
        if not self.opNObj:
            self.opNObj = self.newOpN()
            self.opNObj.requestConfigAndOper()
        
        if not self.opLObj:
            self.opLObj = self.newOpL()
            self.opLObj.requestConfigAndOper()
        
        if not self.opMObj:
            self.opMObj = self.newOpM()
            self.opMObj.requestConfigAndOper()
        
        if not self.opBObj:
            self.opBObj = self.newOpB()
            self.opBObj.requestConfigAndOper()
        
        if not self.configQObj:
            self.configQObj = self.newConfigQ()
            self.configQObj.requestConfigAndOper()
        
        if not self.configPListObj:
            self.configPListObj = self.newConfigPList()
            self.configPListObj.requestConfigAndOper()
        
        if not self.configUListObj:
            self.configUListObj = self.newConfigUList()
            self.configUListObj.requestConfigAndOper()
        
        if not self.opVListObj:
            self.opVListObj = self.newOpVList()
            self.opVListObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestOpZ(False)
        
        self.requestOpY(False)
        
        
        if not self.opNObj:
            self.opNObj = self.newOpN()
            self.opNObj.requestConfig()
        
        if not self.opLObj:
            self.opLObj = self.newOpL()
            self.opLObj.requestConfig()
        
        if not self.opMObj:
            self.opMObj = self.newOpM()
            self.opMObj.requestConfig()
        
        if not self.opBObj:
            self.opBObj = self.newOpB()
            self.opBObj.requestConfig()
        
        if not self.configQObj:
            self.configQObj = self.newConfigQ()
            self.configQObj.requestConfig()
        
        if not self.configPListObj:
            self.configPListObj = self.newConfigPList()
            self.configPListObj.requestConfig()
        
        if not self.configUListObj:
            self.configUListObj = self.newConfigUList()
            self.configUListObj.requestConfig()
        
        if not self.opVListObj:
            self.opVListObj = self.newOpVList()
            self.opVListObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestOpZ(True)
        
        self.requestOpY(True)
        
        
        if not self.opNObj:
            self.opNObj = self.newOpN()
            self.opNObj.requestOper()
        
        if not self.opLObj:
            self.opLObj = self.newOpL()
            self.opLObj.requestOper()
        
        if not self.opMObj:
            self.opMObj = self.newOpM()
            self.opMObj.requestOper()
        
        if not self.opBObj:
            self.opBObj = self.newOpB()
            self.opBObj.requestOper()
        
        if not self.configQObj:
            self.configQObj = self.newConfigQ()
            self.configQObj.requestOper()
        
        if not self.configPListObj:
            self.configPListObj = self.newConfigPList()
            self.configPListObj.requestOper()
        
        if not self.configUListObj:
            self.configUListObj = self.newConfigUList()
            self.configUListObj.requestOper()
        
        if not self.opVListObj:
            self.opVListObj = self.newOpVList()
            self.opVListObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestOpZ(False)
        
        self.requestOpY(False)
        
        
        if not self.opNObj:
            self.opNObj = self.newOpN()
            self.opNObj.clearAllRequested()
        
        if not self.opLObj:
            self.opLObj = self.newOpL()
            self.opLObj.clearAllRequested()
        
        if not self.opMObj:
            self.opMObj = self.newOpM()
            self.opMObj.clearAllRequested()
        
        if not self.opBObj:
            self.opBObj = self.newOpB()
            self.opBObj.clearAllRequested()
        
        if not self.configQObj:
            self.configQObj = self.newConfigQ()
            self.configQObj.clearAllRequested()
        
        if not self.configPListObj:
            self.configPListObj = self.newConfigPList()
            self.configPListObj.clearAllRequested()
        
        if not self.configUListObj:
            self.configUListObj = self.newConfigUList()
            self.configUListObj.clearAllRequested()
        
        if not self.opVListObj:
            self.opVListObj = self.newOpVList()
            self.opVListObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        
        if self.opNObj:
            self.opNObj.clearAllSet()
        
        if self.opLObj:
            self.opLObj.clearAllSet()
        
        if self.opMObj:
            self.opMObj.clearAllSet()
        
        if self.opBObj:
            self.opBObj.clearAllSet()
        
        if self.configQObj:
            self.configQObj.clearAllSet()
        
        if self.configPListObj:
            self.configPListObj.clearAllSet()
        
        if self.configUListObj:
            self.configUListObj.clearAllSet()
        
        if self.opVListObj:
            self.opVListObj.clearAllSet()
        

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

    def newOpN (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-opn').debug3Func(): logFunc('called.')
        opN = BlinkyOpNMaapi(self._log)
        opN.init(self.domain)
        return opN

    def setOpNObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-opn').debug3Func(): logFunc('called. obj=%s', obj)
        self.opNObj = obj

    def getOpNObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-opn').debug3Func(): logFunc('called. self.opNObj=%s', self.opNObj)
        return self.opNObj

    def hasOpN (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-opn').debug3Func(): logFunc('called. self.opNObj=%s', self.opNObj)
        if self.opNObj:
            return True
        return False

    def newOpL (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-opl').debug3Func(): logFunc('called.')
        opL = BlinkyOpLMaapi(self._log)
        opL.init(self.domain)
        return opL

    def setOpLObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-opl').debug3Func(): logFunc('called. obj=%s', obj)
        self.opLObj = obj

    def getOpLObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-opl').debug3Func(): logFunc('called. self.opLObj=%s', self.opLObj)
        return self.opLObj

    def hasOpL (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-opl').debug3Func(): logFunc('called. self.opLObj=%s', self.opLObj)
        if self.opLObj:
            return True
        return False

    def newOpM (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-opm').debug3Func(): logFunc('called.')
        opM = BlinkyOpMMaapi(self._log)
        opM.init(self.domain)
        return opM

    def setOpMObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-opm').debug3Func(): logFunc('called. obj=%s', obj)
        self.opMObj = obj

    def getOpMObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-opm').debug3Func(): logFunc('called. self.opMObj=%s', self.opMObj)
        return self.opMObj

    def hasOpM (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-opm').debug3Func(): logFunc('called. self.opMObj=%s', self.opMObj)
        if self.opMObj:
            return True
        return False

    def newOpB (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-opb').debug3Func(): logFunc('called.')
        opB = BlinkyOpBMaapi(self._log)
        opB.init(self.domain)
        return opB

    def setOpBObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-opb').debug3Func(): logFunc('called. obj=%s', obj)
        self.opBObj = obj

    def getOpBObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-opb').debug3Func(): logFunc('called. self.opBObj=%s', self.opBObj)
        return self.opBObj

    def hasOpB (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-opb').debug3Func(): logFunc('called. self.opBObj=%s', self.opBObj)
        if self.opBObj:
            return True
        return False

    def newConfigQ (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-configq').debug3Func(): logFunc('called.')
        configQ = BlinkyConfigQMaapi(self._log)
        configQ.init(self.domain)
        return configQ

    def setConfigQObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-configq').debug3Func(): logFunc('called. obj=%s', obj)
        self.configQObj = obj

    def getConfigQObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-configq').debug3Func(): logFunc('called. self.configQObj=%s', self.configQObj)
        return self.configQObj

    def hasConfigQ (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-configq').debug3Func(): logFunc('called. self.configQObj=%s', self.configQObj)
        if self.configQObj:
            return True
        return False

    def newConfigPList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-configplist').debug3Func(): logFunc('called.')
        configPList = BlinkyConfigPMaapiList(self._log)
        configPList.init(self.domain)
        return configPList

    def setConfigPListObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-configplist').debug3Func(): logFunc('called. obj=%s', obj)
        self.configPListObj = obj

    def getConfigPListObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-configplist').debug3Func(): logFunc('called. self.configPListObj=%s', self.configPListObj)
        return self.configPListObj

    def hasConfigPList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-configplist').debug3Func(): logFunc('called. self.configPListObj=%s', self.configPListObj)
        if self.configPListObj:
            return True
        return False

    def newConfigUList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-configulist').debug3Func(): logFunc('called.')
        configUList = BlinkyConfigUMaapiList(self._log)
        configUList.init(self.domain)
        return configUList

    def setConfigUListObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-configulist').debug3Func(): logFunc('called. obj=%s', obj)
        self.configUListObj = obj

    def getConfigUListObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-configulist').debug3Func(): logFunc('called. self.configUListObj=%s', self.configUListObj)
        return self.configUListObj

    def hasConfigUList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-configulist').debug3Func(): logFunc('called. self.configUListObj=%s', self.configUListObj)
        if self.configUListObj:
            return True
        return False

    def newOpVList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-opvlist').debug3Func(): logFunc('called.')
        opVList = BlinkyOpVMaapiList(self._log)
        opVList.init(self.domain)
        return opVList

    def setOpVListObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-opvlist').debug3Func(): logFunc('called. obj=%s', obj)
        self.opVListObj = obj

    def getOpVListObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-opvlist').debug3Func(): logFunc('called. self.opVListObj=%s', self.opVListObj)
        return self.opVListObj

    def hasOpVList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-opvlist').debug3Func(): logFunc('called. self.opVListObj=%s', self.opVListObj)
        if self.opVListObj:
            return True
        return False



    def requestOpZ (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-opz').debug3Func(): logFunc('called. requested=%s', requested)
        self.opZRequested = requested
        self.opZSet = False

    def isOpZRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-opz-requested').debug3Func(): logFunc('called. requested=%s', self.opZRequested)
        return self.opZRequested

    def getOpZ (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-opz').debug3Func(): logFunc('called. self.opZSet=%s, self.opZ=%s', self.opZSet, self.opZ)
        if self.opZSet:
            return self.opZ
        return None

    def hasOpZ (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-opz').debug3Func(): logFunc('called. self.opZSet=%s, self.opZ=%s', self.opZSet, self.opZ)
        if self.opZSet:
            return True
        return False

    def setOpZ (self, opZ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-opz').debug3Func(): logFunc('called. opZ=%s, old=%s', opZ, self.opZ)
        self.opZSet = True
        self.opZ = opZ

    def requestOpY (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-opy').debug3Func(): logFunc('called. requested=%s', requested)
        self.opYRequested = requested
        self.opYSet = False

    def isOpYRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-opy-requested').debug3Func(): logFunc('called. requested=%s', self.opYRequested)
        return self.opYRequested

    def getOpY (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-opy').debug3Func(): logFunc('called. self.opYSet=%s, self.opY=%s', self.opYSet, self.opY)
        if self.opYSet:
            return self.opY
        return None

    def hasOpY (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-opy').debug3Func(): logFunc('called. self.opYSet=%s, self.opY=%s', self.opYSet, self.opY)
        if self.opYSet:
            return True
        return False

    def setOpY (self, opY):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-opy').debug3Func(): logFunc('called. opY=%s, old=%s', opY, self.opY)
        self.opYSet = True
        self.opY = opY


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.opNObj:
            self.opNObj._clearAllReadData()
        
        if self.opLObj:
            self.opLObj._clearAllReadData()
        
        if self.opMObj:
            self.opMObj._clearAllReadData()
        
        if self.opBObj:
            self.opBObj._clearAllReadData()
        
        if self.configQObj:
            self.configQObj._clearAllReadData()
        
        if self.configPListObj:
            self.configPListObj._clearAllReadData()
        
        if self.configUListObj:
            self.configUListObj._clearAllReadData()
        
        if self.opVListObj:
            self.opVListObj._clearAllReadData()
        

        
        self.opZ = 0
        self.opZSet = False
        
        self.opY = 0
        self.opYSet = False
        

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("config-a", "http://qwilt.com/model/oper", "oper"))
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

        
        if self.opNObj:
            res = self.opNObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-op-n-failed').errorFunc(): logFunc('opNObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.opLObj:
            res = self.opLObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-op-l-failed').errorFunc(): logFunc('opLObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.opMObj:
            res = self.opMObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-op-m-failed').errorFunc(): logFunc('opMObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.opBObj:
            res = self.opBObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-op-b-failed').errorFunc(): logFunc('opBObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.configQObj:
            res = self.configQObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-config-q-failed').errorFunc(): logFunc('configQObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.configPListObj:
            res = self.configPListObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-config-p-failed').errorFunc(): logFunc('configPListObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.configUListObj:
            res = self.configUListObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-config-u-failed').errorFunc(): logFunc('configUListObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.opVListObj:
            res = self.opVListObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-op-v-failed').errorFunc(): logFunc('opVListObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        

        
        if self.opNObj:
            valBegin = Value()
            (tag, ns, prefix) = ("op-n" , "http://qwilt.com/model/oper", "oper")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.opNObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-op-n-failed').errorFunc(): logFunc('opNObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.opLObj:
            valBegin = Value()
            (tag, ns, prefix) = ("op-l" , "http://qwilt.com/model/oper", "oper")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.opLObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-op-l-failed').errorFunc(): logFunc('opLObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.opMObj:
            valBegin = Value()
            (tag, ns, prefix) = ("op-m" , "http://qwilt.com/model/oper", "oper")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.opMObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-op-m-failed').errorFunc(): logFunc('opMObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.opBObj:
            valBegin = Value()
            (tag, ns, prefix) = ("op-b" , "http://qwilt.com/model/oper", "oper")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.opBObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-op-b-failed').errorFunc(): logFunc('opBObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.configQObj:
            valBegin = Value()
            (tag, ns, prefix) = ("config-q" , "http://qwilt.com/model/oper", "oper")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.configQObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-config-q-failed').errorFunc(): logFunc('configQObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.configPListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("config-p" , "http://qwilt.com/model/oper", "oper")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.configPListObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-config-p-failed').errorFunc(): logFunc('configPListObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.configUListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("config-u" , "http://qwilt.com/model/oper", "oper")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.configUListObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-config-u-failed').errorFunc(): logFunc('configUListObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.opVListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("op-v" , "http://qwilt.com/model/oper", "oper")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.opVListObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-op-v-failed').errorFunc(): logFunc('opVListObj._fillWriteTagValues() failed. PARAMS')
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

        
        if self.isOpZRequested():
            valOpZ = Value()
            valOpZ.setEmpty()
            tagValueList.push(("op-z", "http://qwilt.com/model/oper"), valOpZ)
        
        if self.isOpYRequested():
            valOpY = Value()
            valOpY.setEmpty()
            tagValueList.push(("op-y", "http://qwilt.com/model/oper"), valOpY)
        

        
        if self.opNObj:
            valBegin = Value()
            (tag, ns, prefix) = ("op-n" , "http://qwilt.com/model/oper", "oper")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.opNObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-op-n-failed').errorFunc(): logFunc('opNObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.opLObj:
            valBegin = Value()
            (tag, ns, prefix) = ("op-l" , "http://qwilt.com/model/oper", "oper")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.opLObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-op-l-failed').errorFunc(): logFunc('opLObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.opMObj:
            valBegin = Value()
            (tag, ns, prefix) = ("op-m" , "http://qwilt.com/model/oper", "oper")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.opMObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-op-m-failed').errorFunc(): logFunc('opMObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.opBObj:
            valBegin = Value()
            (tag, ns, prefix) = ("op-b" , "http://qwilt.com/model/oper", "oper")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.opBObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-op-b-failed').errorFunc(): logFunc('opBObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.configQObj:
            valBegin = Value()
            (tag, ns, prefix) = ("config-q" , "http://qwilt.com/model/oper", "oper")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.configQObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-config-q-failed').errorFunc(): logFunc('configQObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.configPListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("config-p" , "http://qwilt.com/model/oper", "oper")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.configPListObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-config-p-failed').errorFunc(): logFunc('configPListObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.configUListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("config-u" , "http://qwilt.com/model/oper", "oper")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.configUListObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-config-u-failed').errorFunc(): logFunc('configUListObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.opVListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("op-v" , "http://qwilt.com/model/oper", "oper")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.opVListObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-op-v-failed').errorFunc(): logFunc('opVListObj._fillReadTagValues() failed. PARAMS')
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
        
        if self.isOpZRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "op-z") or \
                (ns != "http://qwilt.com/model/oper"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-opz').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "opZ", "op-z", "http://qwilt.com/model/oper", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-op-z-bad-value').infoFunc(): logFunc('opZ not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOpZ(tempVar)
            for logFunc in self._log('read-tag-values-op-z').debug3Func(): logFunc('read opZ. opZ=%s, tempValue=%s', self.opZ, tempValue.getType())
        
        if self.isOpYRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "op-y") or \
                (ns != "http://qwilt.com/model/oper"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-opy').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "opY", "op-y", "http://qwilt.com/model/oper", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-op-y-bad-value').infoFunc(): logFunc('opY not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOpY(tempVar)
            for logFunc in self._log('read-tag-values-op-y').debug3Func(): logFunc('read opY. opY=%s, tempValue=%s', self.opY, tempValue.getType())
        

        
        if self.opNObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "op-n") or \
                (ns != "http://qwilt.com/model/oper") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "op-n", "http://qwilt.com/model/oper", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.opNObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-op-n-failed').errorFunc(): logFunc('opNObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "op-n") or \
                (ns != "http://qwilt.com/model/oper") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "op-n", "http://qwilt.com/model/oper", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.opLObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "op-l") or \
                (ns != "http://qwilt.com/model/oper") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "op-l", "http://qwilt.com/model/oper", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.opLObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-op-l-failed').errorFunc(): logFunc('opLObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "op-l") or \
                (ns != "http://qwilt.com/model/oper") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "op-l", "http://qwilt.com/model/oper", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.opMObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "op-m") or \
                (ns != "http://qwilt.com/model/oper") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "op-m", "http://qwilt.com/model/oper", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.opMObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-op-m-failed').errorFunc(): logFunc('opMObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "op-m") or \
                (ns != "http://qwilt.com/model/oper") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "op-m", "http://qwilt.com/model/oper", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.opBObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "op-b") or \
                (ns != "http://qwilt.com/model/oper") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "op-b", "http://qwilt.com/model/oper", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.opBObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-op-b-failed').errorFunc(): logFunc('opBObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "op-b") or \
                (ns != "http://qwilt.com/model/oper") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "op-b", "http://qwilt.com/model/oper", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.configQObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "config-q") or \
                (ns != "http://qwilt.com/model/oper") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "config-q", "http://qwilt.com/model/oper", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.configQObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-config-q-failed').errorFunc(): logFunc('configQObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "config-q") or \
                (ns != "http://qwilt.com/model/oper") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "config-q", "http://qwilt.com/model/oper", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.configPListObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "config-p") or \
                (ns != "http://qwilt.com/model/oper") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "config-p", "http://qwilt.com/model/oper", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.configPListObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-config-p-failed').errorFunc(): logFunc('configPListObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "config-p") or \
                (ns != "http://qwilt.com/model/oper") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "config-p", "http://qwilt.com/model/oper", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.configUListObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "config-u") or \
                (ns != "http://qwilt.com/model/oper") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "config-u", "http://qwilt.com/model/oper", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.configUListObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-config-u-failed').errorFunc(): logFunc('configUListObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "config-u") or \
                (ns != "http://qwilt.com/model/oper") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "config-u", "http://qwilt.com/model/oper", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.opVListObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "op-v") or \
                (ns != "http://qwilt.com/model/oper") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "op-v", "http://qwilt.com/model/oper", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.opVListObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-op-v-failed').errorFunc(): logFunc('opVListObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "op-v") or \
                (ns != "http://qwilt.com/model/oper") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "op-v", "http://qwilt.com/model/oper", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "configA", 
        "namespace": "config_a", 
        "className": "ConfigAMaapi", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.config_a_maapi_gen import ConfigAMaapi", 
        "baseClassName": "ConfigAMaapiBase", 
        "baseModule": "config_a_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "oper", 
            "yangName": "config-a", 
            "namespace": "config_a", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "name": "config-a"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "oper", 
            "memberName": "opN", 
            "yangName": "op-n", 
            "className": "BlinkyOpNMaapi", 
            "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_n.op_n_maapi_gen import BlinkyOpNMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/oper"
        }, 
        {
            "moduleYangNamespacePrefix": "oper", 
            "memberName": "opL", 
            "yangName": "op-l", 
            "className": "BlinkyOpLMaapi", 
            "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_l.op_l_maapi_gen import BlinkyOpLMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/oper"
        }, 
        {
            "moduleYangNamespacePrefix": "oper", 
            "memberName": "opM", 
            "yangName": "op-m", 
            "className": "BlinkyOpMMaapi", 
            "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_m.op_m_maapi_gen import BlinkyOpMMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/oper"
        }, 
        {
            "moduleYangNamespacePrefix": "oper", 
            "memberName": "opB", 
            "yangName": "op-b", 
            "className": "BlinkyOpBMaapi", 
            "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_b.op_b_maapi_gen import BlinkyOpBMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/oper"
        }, 
        {
            "moduleYangNamespacePrefix": "oper", 
            "memberName": "configQ", 
            "yangName": "config-q", 
            "className": "BlinkyConfigQMaapi", 
            "importStatement": "from a.sys.blinky.example.oper.oper.config_a.config_q.config_q_maapi_gen import BlinkyConfigQMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/oper"
        }, 
        {
            "moduleYangNamespacePrefix": "oper", 
            "memberName": "configPList", 
            "yangName": "config-p", 
            "className": "BlinkyConfigPMaapiList", 
            "importStatement": "from a.sys.blinky.example.oper.oper.config_a.config_p.config_p_maapi_list_gen import BlinkyConfigPMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/oper"
        }, 
        {
            "moduleYangNamespacePrefix": "oper", 
            "memberName": "configUList", 
            "yangName": "config-u", 
            "className": "BlinkyConfigUMaapiList", 
            "importStatement": "from a.sys.blinky.example.oper.oper.config_a.config_u.config_u_maapi_list_gen import BlinkyConfigUMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/oper"
        }, 
        {
            "moduleYangNamespacePrefix": "oper", 
            "memberName": "opVList", 
            "yangName": "op-v", 
            "className": "BlinkyOpVMaapiList", 
            "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_v.op_v_maapi_list_gen import BlinkyOpVMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/oper"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "opZ", 
            "yangName": "op-z", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "opY", 
            "yangName": "op-y", 
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
            "sys", 
            "blinky", 
            "example", 
            "oper", 
            "oper"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "opZ", 
            "yangName": "op-z", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "opY", 
            "yangName": "op-y", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


