


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

from line_maapi_base_gen import LineMaapiBase

from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.analyzer.analyzer_maapi_gen import BlinkyAnalyzerMaapi
from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.q_shell.q_shell_maapi_gen import BlinkyQShellMaapi
from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.system_defaults.system_defaults_maapi_gen import BlinkySystemDefaultsMaapi
from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.dispatcher.dispatcher_maapi_gen import BlinkyDispatcherMaapi

from a.api.yang.modules.tech.common.qwilt_tech_types.qwilt_tech_types_module_gen import DecisionType
from a.api.yang.modules.tech.content.qwilt_tech_content_line_types.qwilt_tech_content_line_types_module_gen import AcquisitionAlgorithmType


class BlinkyLineMaapi(LineMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-line")
        self.domain = None

        
        self.analyzerObj = None
        
        self.qShellObj = None
        
        self.systemDefaultsObj = None
        
        self.dispatcherObj = None
        

        
        self.descriptionRequested = False
        self.description = None
        self.descriptionSet = False
        
        self.tempJunkThreadPriority2Requested = False
        self.tempJunkThreadPriority2 = None
        self.tempJunkThreadPriority2Set = False
        
        self.tempJunkAcquisitionAlgorithmRequested = False
        self.tempJunkAcquisitionAlgorithm = None
        self.tempJunkAcquisitionAlgorithmSet = False
        
        self.tempJunkDecision2Requested = False
        self.tempJunkDecision2 = None
        self.tempJunkDecision2Set = False
        
        self.tempJunkDecisionRequested = False
        self.tempJunkDecision = None
        self.tempJunkDecisionSet = False
        
        self.numberRequested = False
        self.number = None
        self.numberSet = False
        
        self.tempJunkThreadPriorityRequested = False
        self.tempJunkThreadPriority = None
        self.tempJunkThreadPrioritySet = False
        
        self.tempJunkAcquisitionAlgorithm2Requested = False
        self.tempJunkAcquisitionAlgorithm2 = None
        self.tempJunkAcquisitionAlgorithm2Set = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestDescription(True)
        
        self.requestTempJunkThreadPriority2(True)
        
        self.requestTempJunkAcquisitionAlgorithm(True)
        
        self.requestTempJunkDecision2(True)
        
        self.requestTempJunkDecision(True)
        
        self.requestNumber(True)
        
        self.requestTempJunkThreadPriority(True)
        
        self.requestTempJunkAcquisitionAlgorithm2(True)
        
        
        
        if not self.analyzerObj:
            self.analyzerObj = self.newAnalyzer()
            self.analyzerObj.requestConfigAndOper()
        
        if not self.qShellObj:
            self.qShellObj = self.newQShell()
            self.qShellObj.requestConfigAndOper()
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.requestConfigAndOper()
        
        if not self.dispatcherObj:
            self.dispatcherObj = self.newDispatcher()
            self.dispatcherObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestDescription(True)
        
        self.requestTempJunkThreadPriority2(True)
        
        self.requestTempJunkAcquisitionAlgorithm(True)
        
        self.requestTempJunkDecision2(True)
        
        self.requestTempJunkDecision(True)
        
        self.requestNumber(True)
        
        self.requestTempJunkThreadPriority(True)
        
        self.requestTempJunkAcquisitionAlgorithm2(True)
        
        
        
        if not self.analyzerObj:
            self.analyzerObj = self.newAnalyzer()
            self.analyzerObj.requestConfig()
        
        if not self.qShellObj:
            self.qShellObj = self.newQShell()
            self.qShellObj.requestConfig()
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.requestConfig()
        
        if not self.dispatcherObj:
            self.dispatcherObj = self.newDispatcher()
            self.dispatcherObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestDescription(False)
        
        self.requestTempJunkThreadPriority2(False)
        
        self.requestTempJunkAcquisitionAlgorithm(False)
        
        self.requestTempJunkDecision2(False)
        
        self.requestTempJunkDecision(False)
        
        self.requestNumber(False)
        
        self.requestTempJunkThreadPriority(False)
        
        self.requestTempJunkAcquisitionAlgorithm2(False)
        
        
        
        if not self.analyzerObj:
            self.analyzerObj = self.newAnalyzer()
            self.analyzerObj.requestOper()
        
        if not self.qShellObj:
            self.qShellObj = self.newQShell()
            self.qShellObj.requestOper()
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.requestOper()
        
        if not self.dispatcherObj:
            self.dispatcherObj = self.newDispatcher()
            self.dispatcherObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestDescription(False)
        
        self.requestTempJunkThreadPriority2(False)
        
        self.requestTempJunkAcquisitionAlgorithm(False)
        
        self.requestTempJunkDecision2(False)
        
        self.requestTempJunkDecision(False)
        
        self.requestNumber(False)
        
        self.requestTempJunkThreadPriority(False)
        
        self.requestTempJunkAcquisitionAlgorithm2(False)
        
        
        
        if not self.analyzerObj:
            self.analyzerObj = self.newAnalyzer()
            self.analyzerObj.clearAllRequested()
        
        if not self.qShellObj:
            self.qShellObj = self.newQShell()
            self.qShellObj.clearAllRequested()
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.clearAllRequested()
        
        if not self.dispatcherObj:
            self.dispatcherObj = self.newDispatcher()
            self.dispatcherObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setDescription(None)
        self.descriptionSet = False
        
        self.setTempJunkThreadPriority2(None)
        self.tempJunkThreadPriority2Set = False
        
        self.setTempJunkAcquisitionAlgorithm(None)
        self.tempJunkAcquisitionAlgorithmSet = False
        
        self.setTempJunkDecision2(None)
        self.tempJunkDecision2Set = False
        
        self.setTempJunkDecision(None)
        self.tempJunkDecisionSet = False
        
        self.setNumber(None)
        self.numberSet = False
        
        self.setTempJunkThreadPriority(None)
        self.tempJunkThreadPrioritySet = False
        
        self.setTempJunkAcquisitionAlgorithm2(None)
        self.tempJunkAcquisitionAlgorithm2Set = False
        
        
        if self.analyzerObj:
            self.analyzerObj.clearAllSet()
        
        if self.qShellObj:
            self.qShellObj.clearAllSet()
        
        if self.systemDefaultsObj:
            self.systemDefaultsObj.clearAllSet()
        
        if self.dispatcherObj:
            self.dispatcherObj.clearAllSet()
        

    def write (self
              , line
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(line, trxContext)

    def read (self
              , line
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(line, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , line
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(line, 
                                  True,
                                  trxContext)

    def newAnalyzer (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-analyzer').debug3Func(): logFunc('called.')
        analyzer = BlinkyAnalyzerMaapi(self._log)
        analyzer.init(self.domain)
        return analyzer

    def setAnalyzerObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-analyzer').debug3Func(): logFunc('called. obj=%s', obj)
        self.analyzerObj = obj

    def getAnalyzerObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-analyzer').debug3Func(): logFunc('called. self.analyzerObj=%s', self.analyzerObj)
        return self.analyzerObj

    def hasAnalyzer (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-analyzer').debug3Func(): logFunc('called. self.analyzerObj=%s', self.analyzerObj)
        if self.analyzerObj:
            return True
        return False

    def newQShell (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-qshell').debug3Func(): logFunc('called.')
        qShell = BlinkyQShellMaapi(self._log)
        qShell.init(self.domain)
        return qShell

    def setQShellObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-qshell').debug3Func(): logFunc('called. obj=%s', obj)
        self.qShellObj = obj

    def getQShellObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-qshell').debug3Func(): logFunc('called. self.qShellObj=%s', self.qShellObj)
        return self.qShellObj

    def hasQShell (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-qshell').debug3Func(): logFunc('called. self.qShellObj=%s', self.qShellObj)
        if self.qShellObj:
            return True
        return False

    def newSystemDefaults (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-systemdefaults').debug3Func(): logFunc('called.')
        systemDefaults = BlinkySystemDefaultsMaapi(self._log)
        systemDefaults.init(self.domain)
        return systemDefaults

    def setSystemDefaultsObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-systemdefaults').debug3Func(): logFunc('called. obj=%s', obj)
        self.systemDefaultsObj = obj

    def getSystemDefaultsObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-systemdefaults').debug3Func(): logFunc('called. self.systemDefaultsObj=%s', self.systemDefaultsObj)
        return self.systemDefaultsObj

    def hasSystemDefaults (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-systemdefaults').debug3Func(): logFunc('called. self.systemDefaultsObj=%s', self.systemDefaultsObj)
        if self.systemDefaultsObj:
            return True
        return False

    def newDispatcher (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-dispatcher').debug3Func(): logFunc('called.')
        dispatcher = BlinkyDispatcherMaapi(self._log)
        dispatcher.init(self.domain)
        return dispatcher

    def setDispatcherObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-dispatcher').debug3Func(): logFunc('called. obj=%s', obj)
        self.dispatcherObj = obj

    def getDispatcherObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-dispatcher').debug3Func(): logFunc('called. self.dispatcherObj=%s', self.dispatcherObj)
        return self.dispatcherObj

    def hasDispatcher (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-dispatcher').debug3Func(): logFunc('called. self.dispatcherObj=%s', self.dispatcherObj)
        if self.dispatcherObj:
            return True
        return False



    def requestDescription (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-description').debug3Func(): logFunc('called. requested=%s', requested)
        self.descriptionRequested = requested
        self.descriptionSet = False

    def isDescriptionRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-description-requested').debug3Func(): logFunc('called. requested=%s', self.descriptionRequested)
        return self.descriptionRequested

    def getDescription (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-description').debug3Func(): logFunc('called. self.descriptionSet=%s, self.description=%s', self.descriptionSet, self.description)
        if self.descriptionSet:
            return self.description
        return None

    def hasDescription (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-description').debug3Func(): logFunc('called. self.descriptionSet=%s, self.description=%s', self.descriptionSet, self.description)
        if self.descriptionSet:
            return True
        return False

    def setDescription (self, description):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-description').debug3Func(): logFunc('called. description=%s, old=%s', description, self.description)
        self.descriptionSet = True
        self.description = description

    def requestTempJunkThreadPriority2 (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-tempjunkthreadpriority2').debug3Func(): logFunc('called. requested=%s', requested)
        self.tempJunkThreadPriority2Requested = requested
        self.tempJunkThreadPriority2Set = False

    def isTempJunkThreadPriority2Requested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-tempjunkthreadpriority2-requested').debug3Func(): logFunc('called. requested=%s', self.tempJunkThreadPriority2Requested)
        return self.tempJunkThreadPriority2Requested

    def getTempJunkThreadPriority2 (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-tempjunkthreadpriority2').debug3Func(): logFunc('called. self.tempJunkThreadPriority2Set=%s, self.tempJunkThreadPriority2=%s', self.tempJunkThreadPriority2Set, self.tempJunkThreadPriority2)
        if self.tempJunkThreadPriority2Set:
            return self.tempJunkThreadPriority2
        return None

    def hasTempJunkThreadPriority2 (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-tempjunkthreadpriority2').debug3Func(): logFunc('called. self.tempJunkThreadPriority2Set=%s, self.tempJunkThreadPriority2=%s', self.tempJunkThreadPriority2Set, self.tempJunkThreadPriority2)
        if self.tempJunkThreadPriority2Set:
            return True
        return False

    def setTempJunkThreadPriority2 (self, tempJunkThreadPriority2):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-tempjunkthreadpriority2').debug3Func(): logFunc('called. tempJunkThreadPriority2=%s, old=%s', tempJunkThreadPriority2, self.tempJunkThreadPriority2)
        self.tempJunkThreadPriority2Set = True
        self.tempJunkThreadPriority2 = tempJunkThreadPriority2

    def requestTempJunkAcquisitionAlgorithm (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-tempjunkacquisitionalgorithm').debug3Func(): logFunc('called. requested=%s', requested)
        self.tempJunkAcquisitionAlgorithmRequested = requested
        self.tempJunkAcquisitionAlgorithmSet = False

    def isTempJunkAcquisitionAlgorithmRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-tempjunkacquisitionalgorithm-requested').debug3Func(): logFunc('called. requested=%s', self.tempJunkAcquisitionAlgorithmRequested)
        return self.tempJunkAcquisitionAlgorithmRequested

    def getTempJunkAcquisitionAlgorithm (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-tempjunkacquisitionalgorithm').debug3Func(): logFunc('called. self.tempJunkAcquisitionAlgorithmSet=%s, self.tempJunkAcquisitionAlgorithm=%s', self.tempJunkAcquisitionAlgorithmSet, self.tempJunkAcquisitionAlgorithm)
        if self.tempJunkAcquisitionAlgorithmSet:
            return self.tempJunkAcquisitionAlgorithm
        return None

    def hasTempJunkAcquisitionAlgorithm (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-tempjunkacquisitionalgorithm').debug3Func(): logFunc('called. self.tempJunkAcquisitionAlgorithmSet=%s, self.tempJunkAcquisitionAlgorithm=%s', self.tempJunkAcquisitionAlgorithmSet, self.tempJunkAcquisitionAlgorithm)
        if self.tempJunkAcquisitionAlgorithmSet:
            return True
        return False

    def setTempJunkAcquisitionAlgorithm (self, tempJunkAcquisitionAlgorithm):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-tempjunkacquisitionalgorithm').debug3Func(): logFunc('called. tempJunkAcquisitionAlgorithm=%s, old=%s', tempJunkAcquisitionAlgorithm, self.tempJunkAcquisitionAlgorithm)
        self.tempJunkAcquisitionAlgorithmSet = True
        self.tempJunkAcquisitionAlgorithm = tempJunkAcquisitionAlgorithm

    def requestTempJunkDecision2 (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-tempjunkdecision2').debug3Func(): logFunc('called. requested=%s', requested)
        self.tempJunkDecision2Requested = requested
        self.tempJunkDecision2Set = False

    def isTempJunkDecision2Requested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-tempjunkdecision2-requested').debug3Func(): logFunc('called. requested=%s', self.tempJunkDecision2Requested)
        return self.tempJunkDecision2Requested

    def getTempJunkDecision2 (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-tempjunkdecision2').debug3Func(): logFunc('called. self.tempJunkDecision2Set=%s, self.tempJunkDecision2=%s', self.tempJunkDecision2Set, self.tempJunkDecision2)
        if self.tempJunkDecision2Set:
            return self.tempJunkDecision2
        return None

    def hasTempJunkDecision2 (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-tempjunkdecision2').debug3Func(): logFunc('called. self.tempJunkDecision2Set=%s, self.tempJunkDecision2=%s', self.tempJunkDecision2Set, self.tempJunkDecision2)
        if self.tempJunkDecision2Set:
            return True
        return False

    def setTempJunkDecision2 (self, tempJunkDecision2):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-tempjunkdecision2').debug3Func(): logFunc('called. tempJunkDecision2=%s, old=%s', tempJunkDecision2, self.tempJunkDecision2)
        self.tempJunkDecision2Set = True
        self.tempJunkDecision2 = tempJunkDecision2

    def requestTempJunkDecision (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-tempjunkdecision').debug3Func(): logFunc('called. requested=%s', requested)
        self.tempJunkDecisionRequested = requested
        self.tempJunkDecisionSet = False

    def isTempJunkDecisionRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-tempjunkdecision-requested').debug3Func(): logFunc('called. requested=%s', self.tempJunkDecisionRequested)
        return self.tempJunkDecisionRequested

    def getTempJunkDecision (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-tempjunkdecision').debug3Func(): logFunc('called. self.tempJunkDecisionSet=%s, self.tempJunkDecision=%s', self.tempJunkDecisionSet, self.tempJunkDecision)
        if self.tempJunkDecisionSet:
            return self.tempJunkDecision
        return None

    def hasTempJunkDecision (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-tempjunkdecision').debug3Func(): logFunc('called. self.tempJunkDecisionSet=%s, self.tempJunkDecision=%s', self.tempJunkDecisionSet, self.tempJunkDecision)
        if self.tempJunkDecisionSet:
            return True
        return False

    def setTempJunkDecision (self, tempJunkDecision):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-tempjunkdecision').debug3Func(): logFunc('called. tempJunkDecision=%s, old=%s', tempJunkDecision, self.tempJunkDecision)
        self.tempJunkDecisionSet = True
        self.tempJunkDecision = tempJunkDecision

    def requestNumber (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-number').debug3Func(): logFunc('called. requested=%s', requested)
        self.numberRequested = requested
        self.numberSet = False

    def isNumberRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-number-requested').debug3Func(): logFunc('called. requested=%s', self.numberRequested)
        return self.numberRequested

    def getNumber (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-number').debug3Func(): logFunc('called. self.numberSet=%s, self.number=%s', self.numberSet, self.number)
        if self.numberSet:
            return self.number
        return None

    def hasNumber (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-number').debug3Func(): logFunc('called. self.numberSet=%s, self.number=%s', self.numberSet, self.number)
        if self.numberSet:
            return True
        return False

    def setNumber (self, number):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-number').debug3Func(): logFunc('called. number=%s, old=%s', number, self.number)
        self.numberSet = True
        self.number = number

    def requestTempJunkThreadPriority (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-tempjunkthreadpriority').debug3Func(): logFunc('called. requested=%s', requested)
        self.tempJunkThreadPriorityRequested = requested
        self.tempJunkThreadPrioritySet = False

    def isTempJunkThreadPriorityRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-tempjunkthreadpriority-requested').debug3Func(): logFunc('called. requested=%s', self.tempJunkThreadPriorityRequested)
        return self.tempJunkThreadPriorityRequested

    def getTempJunkThreadPriority (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-tempjunkthreadpriority').debug3Func(): logFunc('called. self.tempJunkThreadPrioritySet=%s, self.tempJunkThreadPriority=%s', self.tempJunkThreadPrioritySet, self.tempJunkThreadPriority)
        if self.tempJunkThreadPrioritySet:
            return self.tempJunkThreadPriority
        return None

    def hasTempJunkThreadPriority (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-tempjunkthreadpriority').debug3Func(): logFunc('called. self.tempJunkThreadPrioritySet=%s, self.tempJunkThreadPriority=%s', self.tempJunkThreadPrioritySet, self.tempJunkThreadPriority)
        if self.tempJunkThreadPrioritySet:
            return True
        return False

    def setTempJunkThreadPriority (self, tempJunkThreadPriority):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-tempjunkthreadpriority').debug3Func(): logFunc('called. tempJunkThreadPriority=%s, old=%s', tempJunkThreadPriority, self.tempJunkThreadPriority)
        self.tempJunkThreadPrioritySet = True
        self.tempJunkThreadPriority = tempJunkThreadPriority

    def requestTempJunkAcquisitionAlgorithm2 (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-tempjunkacquisitionalgorithm2').debug3Func(): logFunc('called. requested=%s', requested)
        self.tempJunkAcquisitionAlgorithm2Requested = requested
        self.tempJunkAcquisitionAlgorithm2Set = False

    def isTempJunkAcquisitionAlgorithm2Requested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-tempjunkacquisitionalgorithm2-requested').debug3Func(): logFunc('called. requested=%s', self.tempJunkAcquisitionAlgorithm2Requested)
        return self.tempJunkAcquisitionAlgorithm2Requested

    def getTempJunkAcquisitionAlgorithm2 (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-tempjunkacquisitionalgorithm2').debug3Func(): logFunc('called. self.tempJunkAcquisitionAlgorithm2Set=%s, self.tempJunkAcquisitionAlgorithm2=%s', self.tempJunkAcquisitionAlgorithm2Set, self.tempJunkAcquisitionAlgorithm2)
        if self.tempJunkAcquisitionAlgorithm2Set:
            return self.tempJunkAcquisitionAlgorithm2
        return None

    def hasTempJunkAcquisitionAlgorithm2 (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-tempjunkacquisitionalgorithm2').debug3Func(): logFunc('called. self.tempJunkAcquisitionAlgorithm2Set=%s, self.tempJunkAcquisitionAlgorithm2=%s', self.tempJunkAcquisitionAlgorithm2Set, self.tempJunkAcquisitionAlgorithm2)
        if self.tempJunkAcquisitionAlgorithm2Set:
            return True
        return False

    def setTempJunkAcquisitionAlgorithm2 (self, tempJunkAcquisitionAlgorithm2):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-tempjunkacquisitionalgorithm2').debug3Func(): logFunc('called. tempJunkAcquisitionAlgorithm2=%s, old=%s', tempJunkAcquisitionAlgorithm2, self.tempJunkAcquisitionAlgorithm2)
        self.tempJunkAcquisitionAlgorithm2Set = True
        self.tempJunkAcquisitionAlgorithm2 = tempJunkAcquisitionAlgorithm2


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.analyzerObj:
            self.analyzerObj._clearAllReadData()
        
        if self.qShellObj:
            self.qShellObj._clearAllReadData()
        
        if self.systemDefaultsObj:
            self.systemDefaultsObj._clearAllReadData()
        
        if self.dispatcherObj:
            self.dispatcherObj._clearAllReadData()
        

        
        self.description = 0
        self.descriptionSet = False
        
        self.tempJunkThreadPriority2 = 0
        self.tempJunkThreadPriority2Set = False
        
        self.tempJunkAcquisitionAlgorithm = 0
        self.tempJunkAcquisitionAlgorithmSet = False
        
        self.tempJunkDecision2 = 0
        self.tempJunkDecision2Set = False
        
        self.tempJunkDecision = 0
        self.tempJunkDecisionSet = False
        
        self.number = 0
        self.numberSet = False
        
        self.tempJunkThreadPriority = 0
        self.tempJunkThreadPrioritySet = False
        
        self.tempJunkAcquisitionAlgorithm2 = 0
        self.tempJunkAcquisitionAlgorithm2Set = False
        

    def _getSelfKeyPath (self, line
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        ancestorVal = Value()
        ancestorVal.setString(line);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("line", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("content", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        line, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(line, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(line, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       line, 
                       
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

        keyPath = self._getSelfKeyPath(line, 
                                       
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
                               line, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        
        if self.analyzerObj:
            res = self.analyzerObj._collectItemsToDelete(line, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-analyzer-failed').errorFunc(): logFunc('analyzerObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.qShellObj:
            res = self.qShellObj._collectItemsToDelete(line, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-q-shell-failed').errorFunc(): logFunc('qShellObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.systemDefaultsObj:
            res = self.systemDefaultsObj._collectItemsToDelete(line, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.dispatcherObj:
            res = self.dispatcherObj._collectItemsToDelete(line, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-dispatcher-failed').errorFunc(): logFunc('dispatcherObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasDescription():
            valDescription = Value()
            if self.description is not None:
                valDescription.setString(self.description)
            else:
                valDescription.setEmpty()
            tagValueList.push(("description", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valDescription)
        
        if self.hasTempJunkThreadPriority2():
            valTempJunkThreadPriority2 = Value()
            if self.tempJunkThreadPriority2 is not None:
                valTempJunkThreadPriority2.setString(self.tempJunkThreadPriority2)
            else:
                valTempJunkThreadPriority2.setEmpty()
            tagValueList.push(("temp-junk-thread-priority-2", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valTempJunkThreadPriority2)
        
        if self.hasTempJunkAcquisitionAlgorithm():
            valTempJunkAcquisitionAlgorithm = Value()
            if self.tempJunkAcquisitionAlgorithm is not None:
                valTempJunkAcquisitionAlgorithm.setEnum(self.tempJunkAcquisitionAlgorithm.getValue())
            else:
                valTempJunkAcquisitionAlgorithm.setEmpty()
            tagValueList.push(("temp-junk-acquisition-algorithm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valTempJunkAcquisitionAlgorithm)
        
        if self.hasTempJunkDecision2():
            valTempJunkDecision2 = Value()
            if self.tempJunkDecision2 is not None:
                valTempJunkDecision2.setEnum(self.tempJunkDecision2.getValue())
            else:
                valTempJunkDecision2.setEmpty()
            tagValueList.push(("temp-junk-decision-2", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valTempJunkDecision2)
        
        if self.hasTempJunkDecision():
            valTempJunkDecision = Value()
            if self.tempJunkDecision is not None:
                valTempJunkDecision.setEnum(self.tempJunkDecision.getValue())
            else:
                valTempJunkDecision.setEmpty()
            tagValueList.push(("temp-junk-decision", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valTempJunkDecision)
        
        if self.hasNumber():
            valNumber = Value()
            if self.number is not None:
                valNumber.setString(self.number)
            else:
                valNumber.setEmpty()
            tagValueList.push(("number", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valNumber)
        
        if self.hasTempJunkThreadPriority():
            valTempJunkThreadPriority = Value()
            if self.tempJunkThreadPriority is not None:
                valTempJunkThreadPriority.setString(self.tempJunkThreadPriority)
            else:
                valTempJunkThreadPriority.setEmpty()
            tagValueList.push(("temp-junk-thread-priority", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valTempJunkThreadPriority)
        
        if self.hasTempJunkAcquisitionAlgorithm2():
            valTempJunkAcquisitionAlgorithm2 = Value()
            if self.tempJunkAcquisitionAlgorithm2 is not None:
                valTempJunkAcquisitionAlgorithm2.setEnum(self.tempJunkAcquisitionAlgorithm2.getValue())
            else:
                valTempJunkAcquisitionAlgorithm2.setEmpty()
            tagValueList.push(("temp-junk-acquisition-algorithm-2", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valTempJunkAcquisitionAlgorithm2)
        

        
        if self.analyzerObj:
            valBegin = Value()
            (tag, ns, prefix) = ("analyzer" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.analyzerObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-analyzer-failed').errorFunc(): logFunc('analyzerObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.qShellObj:
            valBegin = Value()
            (tag, ns, prefix) = ("q-shell" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.qShellObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-q-shell-failed').errorFunc(): logFunc('qShellObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.systemDefaultsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("system-defaults" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.systemDefaultsObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.dispatcherObj:
            valBegin = Value()
            (tag, ns, prefix) = ("dispatcher" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.dispatcherObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-dispatcher-failed').errorFunc(): logFunc('dispatcherObj._fillWriteTagValues() failed. PARAMS')
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

        
        if self.isDescriptionRequested():
            valDescription = Value()
            valDescription.setEmpty()
            tagValueList.push(("description", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valDescription)
        
        if self.isTempJunkThreadPriority2Requested():
            valTempJunkThreadPriority2 = Value()
            valTempJunkThreadPriority2.setEmpty()
            tagValueList.push(("temp-junk-thread-priority-2", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valTempJunkThreadPriority2)
        
        if self.isTempJunkAcquisitionAlgorithmRequested():
            valTempJunkAcquisitionAlgorithm = Value()
            valTempJunkAcquisitionAlgorithm.setEmpty()
            tagValueList.push(("temp-junk-acquisition-algorithm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valTempJunkAcquisitionAlgorithm)
        
        if self.isTempJunkDecision2Requested():
            valTempJunkDecision2 = Value()
            valTempJunkDecision2.setEmpty()
            tagValueList.push(("temp-junk-decision-2", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valTempJunkDecision2)
        
        if self.isTempJunkDecisionRequested():
            valTempJunkDecision = Value()
            valTempJunkDecision.setEmpty()
            tagValueList.push(("temp-junk-decision", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valTempJunkDecision)
        
        if self.isNumberRequested():
            valNumber = Value()
            valNumber.setEmpty()
            tagValueList.push(("number", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valNumber)
        
        if self.isTempJunkThreadPriorityRequested():
            valTempJunkThreadPriority = Value()
            valTempJunkThreadPriority.setEmpty()
            tagValueList.push(("temp-junk-thread-priority", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valTempJunkThreadPriority)
        
        if self.isTempJunkAcquisitionAlgorithm2Requested():
            valTempJunkAcquisitionAlgorithm2 = Value()
            valTempJunkAcquisitionAlgorithm2.setEmpty()
            tagValueList.push(("temp-junk-acquisition-algorithm-2", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valTempJunkAcquisitionAlgorithm2)
        

        
        if self.analyzerObj:
            valBegin = Value()
            (tag, ns, prefix) = ("analyzer" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.analyzerObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-analyzer-failed').errorFunc(): logFunc('analyzerObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.qShellObj:
            valBegin = Value()
            (tag, ns, prefix) = ("q-shell" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.qShellObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-q-shell-failed').errorFunc(): logFunc('qShellObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.systemDefaultsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("system-defaults" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.systemDefaultsObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.dispatcherObj:
            valBegin = Value()
            (tag, ns, prefix) = ("dispatcher" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.dispatcherObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-dispatcher-failed').errorFunc(): logFunc('dispatcherObj._fillReadTagValues() failed. PARAMS')
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
        
        if self.isDescriptionRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "description") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-description').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "description", "description", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-description-bad-value').infoFunc(): logFunc('description not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setDescription(tempVar)
            for logFunc in self._log('read-tag-values-description').debug3Func(): logFunc('read description. description=%s, tempValue=%s', self.description, tempValue.getType())
        
        if self.isTempJunkThreadPriority2Requested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "temp-junk-thread-priority-2") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-tempjunkthreadpriority2').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "tempJunkThreadPriority2", "temp-junk-thread-priority-2", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-temp-junk-thread-priority-2-bad-value').infoFunc(): logFunc('tempJunkThreadPriority2 not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTempJunkThreadPriority2(tempVar)
            for logFunc in self._log('read-tag-values-temp-junk-thread-priority-2').debug3Func(): logFunc('read tempJunkThreadPriority2. tempJunkThreadPriority2=%s, tempValue=%s', self.tempJunkThreadPriority2, tempValue.getType())
        
        if self.isTempJunkAcquisitionAlgorithmRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "temp-junk-acquisition-algorithm") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-tempjunkacquisitionalgorithm').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "tempJunkAcquisitionAlgorithm", "temp-junk-acquisition-algorithm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-temp-junk-acquisition-algorithm-bad-value').infoFunc(): logFunc('tempJunkAcquisitionAlgorithm not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTempJunkAcquisitionAlgorithm(tempVar)
            for logFunc in self._log('read-tag-values-temp-junk-acquisition-algorithm').debug3Func(): logFunc('read tempJunkAcquisitionAlgorithm. tempJunkAcquisitionAlgorithm=%s, tempValue=%s', self.tempJunkAcquisitionAlgorithm, tempValue.getType())
        
        if self.isTempJunkDecision2Requested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "temp-junk-decision-2") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-tempjunkdecision2').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "tempJunkDecision2", "temp-junk-decision-2", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-temp-junk-decision-2-bad-value').infoFunc(): logFunc('tempJunkDecision2 not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTempJunkDecision2(tempVar)
            for logFunc in self._log('read-tag-values-temp-junk-decision-2').debug3Func(): logFunc('read tempJunkDecision2. tempJunkDecision2=%s, tempValue=%s', self.tempJunkDecision2, tempValue.getType())
        
        if self.isTempJunkDecisionRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "temp-junk-decision") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-tempjunkdecision').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "tempJunkDecision", "temp-junk-decision", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-temp-junk-decision-bad-value').infoFunc(): logFunc('tempJunkDecision not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTempJunkDecision(tempVar)
            for logFunc in self._log('read-tag-values-temp-junk-decision').debug3Func(): logFunc('read tempJunkDecision. tempJunkDecision=%s, tempValue=%s', self.tempJunkDecision, tempValue.getType())
        
        if self.isNumberRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "number") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-number').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "number", "number", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-number-bad-value').infoFunc(): logFunc('number not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setNumber(tempVar)
            for logFunc in self._log('read-tag-values-number').debug3Func(): logFunc('read number. number=%s, tempValue=%s', self.number, tempValue.getType())
        
        if self.isTempJunkThreadPriorityRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "temp-junk-thread-priority") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-tempjunkthreadpriority').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "tempJunkThreadPriority", "temp-junk-thread-priority", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-temp-junk-thread-priority-bad-value').infoFunc(): logFunc('tempJunkThreadPriority not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTempJunkThreadPriority(tempVar)
            for logFunc in self._log('read-tag-values-temp-junk-thread-priority').debug3Func(): logFunc('read tempJunkThreadPriority. tempJunkThreadPriority=%s, tempValue=%s', self.tempJunkThreadPriority, tempValue.getType())
        
        if self.isTempJunkAcquisitionAlgorithm2Requested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "temp-junk-acquisition-algorithm-2") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-tempjunkacquisitionalgorithm2').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "tempJunkAcquisitionAlgorithm2", "temp-junk-acquisition-algorithm-2", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-temp-junk-acquisition-algorithm-2-bad-value').infoFunc(): logFunc('tempJunkAcquisitionAlgorithm2 not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTempJunkAcquisitionAlgorithm2(tempVar)
            for logFunc in self._log('read-tag-values-temp-junk-acquisition-algorithm-2').debug3Func(): logFunc('read tempJunkAcquisitionAlgorithm2. tempJunkAcquisitionAlgorithm2=%s, tempValue=%s', self.tempJunkAcquisitionAlgorithm2, tempValue.getType())
        

        
        if self.analyzerObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "analyzer") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "analyzer", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.analyzerObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-analyzer-failed').errorFunc(): logFunc('analyzerObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "analyzer") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "analyzer", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.qShellObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "q-shell") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "q-shell", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.qShellObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-q-shell-failed').errorFunc(): logFunc('qShellObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "q-shell") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "q-shell", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.systemDefaultsObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "system-defaults") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.systemDefaultsObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "system-defaults") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.dispatcherObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "dispatcher") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "dispatcher", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.dispatcherObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-dispatcher-failed').errorFunc(): logFunc('dispatcherObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "dispatcher") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "dispatcher", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "line", 
        "namespace": "line", 
        "className": "LineMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.line_maapi_gen import LineMaapi", 
        "baseClassName": "LineMaapiBase", 
        "baseModule": "line_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qtc", 
            "yangName": "content", 
            "namespace": "content", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "name": "content"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "isCurrent": true, 
            "yangName": "line", 
            "namespace": "line", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "keyLeaf": {
                "varName": "line", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "line"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "memberName": "analyzer", 
            "yangName": "analyzer", 
            "className": "BlinkyAnalyzerMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.analyzer.analyzer_maapi_gen import BlinkyAnalyzerMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "memberName": "qShell", 
            "yangName": "q-shell", 
            "className": "BlinkyQShellMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.q_shell.q_shell_maapi_gen import BlinkyQShellMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "memberName": "systemDefaults", 
            "yangName": "system-defaults", 
            "className": "BlinkySystemDefaultsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.system_defaults.system_defaults_maapi_gen import BlinkySystemDefaultsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "memberName": "dispatcher", 
            "yangName": "dispatcher", 
            "className": "BlinkyDispatcherMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.dispatcher.dispatcher_maapi_gen import BlinkyDispatcherMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "tempJunkThreadPriority2", 
            "yangName": "temp-junk-thread-priority-2", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "tempJunkAcquisitionAlgorithm", 
            "yangName": "temp-junk-acquisition-algorithm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "tempJunkDecision2", 
            "yangName": "temp-junk-decision-2", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "tempJunkDecision", 
            "yangName": "temp-junk-decision", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "number", 
            "yangName": "number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "tempJunkThreadPriority", 
            "yangName": "temp-junk-thread-priority", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "tempJunkAcquisitionAlgorithm2", 
            "yangName": "temp-junk-acquisition-algorithm-2", 
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
            "content", 
            "qwilt_tech_content_line"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "tempJunkThreadPriority2", 
            "yangName": "temp-junk-thread-priority-2", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "tempJunkAcquisitionAlgorithm", 
            "yangName": "temp-junk-acquisition-algorithm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "tempJunkDecision2", 
            "yangName": "temp-junk-decision-2", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "tempJunkDecision", 
            "yangName": "temp-junk-decision", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "number", 
            "yangName": "number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "tempJunkThreadPriority", 
            "yangName": "temp-junk-thread-priority", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "tempJunkAcquisitionAlgorithm2", 
            "yangName": "temp-junk-acquisition-algorithm-2", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


