


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

from sub_task_interval_maapi_base_gen import SubTaskIntervalMaapiBase




class BlinkySubTaskIntervalMaapi(SubTaskIntervalMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-subTaskInterval")
        self.domain = None

        

        
        self.readRedirectNeighbourTableMsecRequested = False
        self.readRedirectNeighbourTableMsec = None
        self.readRedirectNeighbourTableMsecSet = False
        
        self.triggerTitleTableSaveMsecRequested = False
        self.triggerTitleTableSaveMsec = None
        self.triggerTitleTableSaveMsecSet = False
        
        self.readRedirectEnablerMsecRequested = False
        self.readRedirectEnablerMsec = None
        self.readRedirectEnablerMsecSet = False
        
        self.readBrownieQuotaMsecRequested = False
        self.readBrownieQuotaMsec = None
        self.readBrownieQuotaMsecSet = False
        
        self.logDebugStatsMsecRequested = False
        self.logDebugStatsMsec = None
        self.logDebugStatsMsecSet = False
        
        self.readDeliveryBlockerUpdatesMsecRequested = False
        self.readDeliveryBlockerUpdatesMsec = None
        self.readDeliveryBlockerUpdatesMsecSet = False
        
        self.readExternalStateMsecRequested = False
        self.readExternalStateMsec = None
        self.readExternalStateMsecSet = False
        
        self.writeAcquiredTitlesMsecRequested = False
        self.writeAcquiredTitlesMsec = None
        self.writeAcquiredTitlesMsecSet = False
        
        self.readExternalConfigMsecRequested = False
        self.readExternalConfigMsec = None
        self.readExternalConfigMsecSet = False
        
        self.readDeliveredTitlesMsecRequested = False
        self.readDeliveredTitlesMsec = None
        self.readDeliveredTitlesMsecSet = False
        
        self.requestNeighbourDiscoveryMsecRequested = False
        self.requestNeighbourDiscoveryMsec = None
        self.requestNeighbourDiscoveryMsecSet = False
        
        self.updateRedirectQuotaMsecRequested = False
        self.updateRedirectQuotaMsec = None
        self.updateRedirectQuotaMsecSet = False
        
        self.checkContentDisksSizeMsecRequested = False
        self.checkContentDisksSizeMsec = None
        self.checkContentDisksSizeMsecSet = False
        
        self.sampleCountersMsecRequested = False
        self.sampleCountersMsec = None
        self.sampleCountersMsecSet = False
        
        self.attenuatePastVolumeMsecRequested = False
        self.attenuatePastVolumeMsec = None
        self.attenuatePastVolumeMsecSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestReadRedirectNeighbourTableMsec(True)
        
        self.requestTriggerTitleTableSaveMsec(True)
        
        self.requestReadRedirectEnablerMsec(True)
        
        self.requestReadBrownieQuotaMsec(True)
        
        self.requestLogDebugStatsMsec(True)
        
        self.requestReadDeliveryBlockerUpdatesMsec(True)
        
        self.requestReadExternalStateMsec(True)
        
        self.requestWriteAcquiredTitlesMsec(True)
        
        self.requestReadExternalConfigMsec(True)
        
        self.requestReadDeliveredTitlesMsec(True)
        
        self.requestRequestNeighbourDiscoveryMsec(True)
        
        self.requestUpdateRedirectQuotaMsec(True)
        
        self.requestCheckContentDisksSizeMsec(True)
        
        self.requestSampleCountersMsec(True)
        
        self.requestAttenuatePastVolumeMsec(True)
        
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestReadRedirectNeighbourTableMsec(True)
        
        self.requestTriggerTitleTableSaveMsec(True)
        
        self.requestReadRedirectEnablerMsec(True)
        
        self.requestReadBrownieQuotaMsec(True)
        
        self.requestLogDebugStatsMsec(True)
        
        self.requestReadDeliveryBlockerUpdatesMsec(True)
        
        self.requestReadExternalStateMsec(True)
        
        self.requestWriteAcquiredTitlesMsec(True)
        
        self.requestReadExternalConfigMsec(True)
        
        self.requestReadDeliveredTitlesMsec(True)
        
        self.requestRequestNeighbourDiscoveryMsec(True)
        
        self.requestUpdateRedirectQuotaMsec(True)
        
        self.requestCheckContentDisksSizeMsec(True)
        
        self.requestSampleCountersMsec(True)
        
        self.requestAttenuatePastVolumeMsec(True)
        
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestReadRedirectNeighbourTableMsec(False)
        
        self.requestTriggerTitleTableSaveMsec(False)
        
        self.requestReadRedirectEnablerMsec(False)
        
        self.requestReadBrownieQuotaMsec(False)
        
        self.requestLogDebugStatsMsec(False)
        
        self.requestReadDeliveryBlockerUpdatesMsec(False)
        
        self.requestReadExternalStateMsec(False)
        
        self.requestWriteAcquiredTitlesMsec(False)
        
        self.requestReadExternalConfigMsec(False)
        
        self.requestReadDeliveredTitlesMsec(False)
        
        self.requestRequestNeighbourDiscoveryMsec(False)
        
        self.requestUpdateRedirectQuotaMsec(False)
        
        self.requestCheckContentDisksSizeMsec(False)
        
        self.requestSampleCountersMsec(False)
        
        self.requestAttenuatePastVolumeMsec(False)
        
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestReadRedirectNeighbourTableMsec(False)
        
        self.requestTriggerTitleTableSaveMsec(False)
        
        self.requestReadRedirectEnablerMsec(False)
        
        self.requestReadBrownieQuotaMsec(False)
        
        self.requestLogDebugStatsMsec(False)
        
        self.requestReadDeliveryBlockerUpdatesMsec(False)
        
        self.requestReadExternalStateMsec(False)
        
        self.requestWriteAcquiredTitlesMsec(False)
        
        self.requestReadExternalConfigMsec(False)
        
        self.requestReadDeliveredTitlesMsec(False)
        
        self.requestRequestNeighbourDiscoveryMsec(False)
        
        self.requestUpdateRedirectQuotaMsec(False)
        
        self.requestCheckContentDisksSizeMsec(False)
        
        self.requestSampleCountersMsec(False)
        
        self.requestAttenuatePastVolumeMsec(False)
        
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setReadRedirectNeighbourTableMsec(None)
        self.readRedirectNeighbourTableMsecSet = False
        
        self.setTriggerTitleTableSaveMsec(None)
        self.triggerTitleTableSaveMsecSet = False
        
        self.setReadRedirectEnablerMsec(None)
        self.readRedirectEnablerMsecSet = False
        
        self.setReadBrownieQuotaMsec(None)
        self.readBrownieQuotaMsecSet = False
        
        self.setLogDebugStatsMsec(None)
        self.logDebugStatsMsecSet = False
        
        self.setReadDeliveryBlockerUpdatesMsec(None)
        self.readDeliveryBlockerUpdatesMsecSet = False
        
        self.setReadExternalStateMsec(None)
        self.readExternalStateMsecSet = False
        
        self.setWriteAcquiredTitlesMsec(None)
        self.writeAcquiredTitlesMsecSet = False
        
        self.setReadExternalConfigMsec(None)
        self.readExternalConfigMsecSet = False
        
        self.setReadDeliveredTitlesMsec(None)
        self.readDeliveredTitlesMsecSet = False
        
        self.setRequestNeighbourDiscoveryMsec(None)
        self.requestNeighbourDiscoveryMsecSet = False
        
        self.setUpdateRedirectQuotaMsec(None)
        self.updateRedirectQuotaMsecSet = False
        
        self.setCheckContentDisksSizeMsec(None)
        self.checkContentDisksSizeMsecSet = False
        
        self.setSampleCountersMsec(None)
        self.sampleCountersMsecSet = False
        
        self.setAttenuatePastVolumeMsec(None)
        self.attenuatePastVolumeMsecSet = False
        
        

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



    def requestReadRedirectNeighbourTableMsec (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-readredirectneighbourtablemsec').debug3Func(): logFunc('called. requested=%s', requested)
        self.readRedirectNeighbourTableMsecRequested = requested
        self.readRedirectNeighbourTableMsecSet = False

    def isReadRedirectNeighbourTableMsecRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-readredirectneighbourtablemsec-requested').debug3Func(): logFunc('called. requested=%s', self.readRedirectNeighbourTableMsecRequested)
        return self.readRedirectNeighbourTableMsecRequested

    def getReadRedirectNeighbourTableMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-readredirectneighbourtablemsec').debug3Func(): logFunc('called. self.readRedirectNeighbourTableMsecSet=%s, self.readRedirectNeighbourTableMsec=%s', self.readRedirectNeighbourTableMsecSet, self.readRedirectNeighbourTableMsec)
        if self.readRedirectNeighbourTableMsecSet:
            return self.readRedirectNeighbourTableMsec
        return None

    def hasReadRedirectNeighbourTableMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-readredirectneighbourtablemsec').debug3Func(): logFunc('called. self.readRedirectNeighbourTableMsecSet=%s, self.readRedirectNeighbourTableMsec=%s', self.readRedirectNeighbourTableMsecSet, self.readRedirectNeighbourTableMsec)
        if self.readRedirectNeighbourTableMsecSet:
            return True
        return False

    def setReadRedirectNeighbourTableMsec (self, readRedirectNeighbourTableMsec):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-readredirectneighbourtablemsec').debug3Func(): logFunc('called. readRedirectNeighbourTableMsec=%s, old=%s', readRedirectNeighbourTableMsec, self.readRedirectNeighbourTableMsec)
        self.readRedirectNeighbourTableMsecSet = True
        self.readRedirectNeighbourTableMsec = readRedirectNeighbourTableMsec

    def requestTriggerTitleTableSaveMsec (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-triggertitletablesavemsec').debug3Func(): logFunc('called. requested=%s', requested)
        self.triggerTitleTableSaveMsecRequested = requested
        self.triggerTitleTableSaveMsecSet = False

    def isTriggerTitleTableSaveMsecRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-triggertitletablesavemsec-requested').debug3Func(): logFunc('called. requested=%s', self.triggerTitleTableSaveMsecRequested)
        return self.triggerTitleTableSaveMsecRequested

    def getTriggerTitleTableSaveMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-triggertitletablesavemsec').debug3Func(): logFunc('called. self.triggerTitleTableSaveMsecSet=%s, self.triggerTitleTableSaveMsec=%s', self.triggerTitleTableSaveMsecSet, self.triggerTitleTableSaveMsec)
        if self.triggerTitleTableSaveMsecSet:
            return self.triggerTitleTableSaveMsec
        return None

    def hasTriggerTitleTableSaveMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-triggertitletablesavemsec').debug3Func(): logFunc('called. self.triggerTitleTableSaveMsecSet=%s, self.triggerTitleTableSaveMsec=%s', self.triggerTitleTableSaveMsecSet, self.triggerTitleTableSaveMsec)
        if self.triggerTitleTableSaveMsecSet:
            return True
        return False

    def setTriggerTitleTableSaveMsec (self, triggerTitleTableSaveMsec):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-triggertitletablesavemsec').debug3Func(): logFunc('called. triggerTitleTableSaveMsec=%s, old=%s', triggerTitleTableSaveMsec, self.triggerTitleTableSaveMsec)
        self.triggerTitleTableSaveMsecSet = True
        self.triggerTitleTableSaveMsec = triggerTitleTableSaveMsec

    def requestReadRedirectEnablerMsec (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-readredirectenablermsec').debug3Func(): logFunc('called. requested=%s', requested)
        self.readRedirectEnablerMsecRequested = requested
        self.readRedirectEnablerMsecSet = False

    def isReadRedirectEnablerMsecRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-readredirectenablermsec-requested').debug3Func(): logFunc('called. requested=%s', self.readRedirectEnablerMsecRequested)
        return self.readRedirectEnablerMsecRequested

    def getReadRedirectEnablerMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-readredirectenablermsec').debug3Func(): logFunc('called. self.readRedirectEnablerMsecSet=%s, self.readRedirectEnablerMsec=%s', self.readRedirectEnablerMsecSet, self.readRedirectEnablerMsec)
        if self.readRedirectEnablerMsecSet:
            return self.readRedirectEnablerMsec
        return None

    def hasReadRedirectEnablerMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-readredirectenablermsec').debug3Func(): logFunc('called. self.readRedirectEnablerMsecSet=%s, self.readRedirectEnablerMsec=%s', self.readRedirectEnablerMsecSet, self.readRedirectEnablerMsec)
        if self.readRedirectEnablerMsecSet:
            return True
        return False

    def setReadRedirectEnablerMsec (self, readRedirectEnablerMsec):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-readredirectenablermsec').debug3Func(): logFunc('called. readRedirectEnablerMsec=%s, old=%s', readRedirectEnablerMsec, self.readRedirectEnablerMsec)
        self.readRedirectEnablerMsecSet = True
        self.readRedirectEnablerMsec = readRedirectEnablerMsec

    def requestReadBrownieQuotaMsec (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-readbrowniequotamsec').debug3Func(): logFunc('called. requested=%s', requested)
        self.readBrownieQuotaMsecRequested = requested
        self.readBrownieQuotaMsecSet = False

    def isReadBrownieQuotaMsecRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-readbrowniequotamsec-requested').debug3Func(): logFunc('called. requested=%s', self.readBrownieQuotaMsecRequested)
        return self.readBrownieQuotaMsecRequested

    def getReadBrownieQuotaMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-readbrowniequotamsec').debug3Func(): logFunc('called. self.readBrownieQuotaMsecSet=%s, self.readBrownieQuotaMsec=%s', self.readBrownieQuotaMsecSet, self.readBrownieQuotaMsec)
        if self.readBrownieQuotaMsecSet:
            return self.readBrownieQuotaMsec
        return None

    def hasReadBrownieQuotaMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-readbrowniequotamsec').debug3Func(): logFunc('called. self.readBrownieQuotaMsecSet=%s, self.readBrownieQuotaMsec=%s', self.readBrownieQuotaMsecSet, self.readBrownieQuotaMsec)
        if self.readBrownieQuotaMsecSet:
            return True
        return False

    def setReadBrownieQuotaMsec (self, readBrownieQuotaMsec):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-readbrowniequotamsec').debug3Func(): logFunc('called. readBrownieQuotaMsec=%s, old=%s', readBrownieQuotaMsec, self.readBrownieQuotaMsec)
        self.readBrownieQuotaMsecSet = True
        self.readBrownieQuotaMsec = readBrownieQuotaMsec

    def requestLogDebugStatsMsec (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-logdebugstatsmsec').debug3Func(): logFunc('called. requested=%s', requested)
        self.logDebugStatsMsecRequested = requested
        self.logDebugStatsMsecSet = False

    def isLogDebugStatsMsecRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-logdebugstatsmsec-requested').debug3Func(): logFunc('called. requested=%s', self.logDebugStatsMsecRequested)
        return self.logDebugStatsMsecRequested

    def getLogDebugStatsMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-logdebugstatsmsec').debug3Func(): logFunc('called. self.logDebugStatsMsecSet=%s, self.logDebugStatsMsec=%s', self.logDebugStatsMsecSet, self.logDebugStatsMsec)
        if self.logDebugStatsMsecSet:
            return self.logDebugStatsMsec
        return None

    def hasLogDebugStatsMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-logdebugstatsmsec').debug3Func(): logFunc('called. self.logDebugStatsMsecSet=%s, self.logDebugStatsMsec=%s', self.logDebugStatsMsecSet, self.logDebugStatsMsec)
        if self.logDebugStatsMsecSet:
            return True
        return False

    def setLogDebugStatsMsec (self, logDebugStatsMsec):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-logdebugstatsmsec').debug3Func(): logFunc('called. logDebugStatsMsec=%s, old=%s', logDebugStatsMsec, self.logDebugStatsMsec)
        self.logDebugStatsMsecSet = True
        self.logDebugStatsMsec = logDebugStatsMsec

    def requestReadDeliveryBlockerUpdatesMsec (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-readdeliveryblockerupdatesmsec').debug3Func(): logFunc('called. requested=%s', requested)
        self.readDeliveryBlockerUpdatesMsecRequested = requested
        self.readDeliveryBlockerUpdatesMsecSet = False

    def isReadDeliveryBlockerUpdatesMsecRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-readdeliveryblockerupdatesmsec-requested').debug3Func(): logFunc('called. requested=%s', self.readDeliveryBlockerUpdatesMsecRequested)
        return self.readDeliveryBlockerUpdatesMsecRequested

    def getReadDeliveryBlockerUpdatesMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-readdeliveryblockerupdatesmsec').debug3Func(): logFunc('called. self.readDeliveryBlockerUpdatesMsecSet=%s, self.readDeliveryBlockerUpdatesMsec=%s', self.readDeliveryBlockerUpdatesMsecSet, self.readDeliveryBlockerUpdatesMsec)
        if self.readDeliveryBlockerUpdatesMsecSet:
            return self.readDeliveryBlockerUpdatesMsec
        return None

    def hasReadDeliveryBlockerUpdatesMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-readdeliveryblockerupdatesmsec').debug3Func(): logFunc('called. self.readDeliveryBlockerUpdatesMsecSet=%s, self.readDeliveryBlockerUpdatesMsec=%s', self.readDeliveryBlockerUpdatesMsecSet, self.readDeliveryBlockerUpdatesMsec)
        if self.readDeliveryBlockerUpdatesMsecSet:
            return True
        return False

    def setReadDeliveryBlockerUpdatesMsec (self, readDeliveryBlockerUpdatesMsec):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-readdeliveryblockerupdatesmsec').debug3Func(): logFunc('called. readDeliveryBlockerUpdatesMsec=%s, old=%s', readDeliveryBlockerUpdatesMsec, self.readDeliveryBlockerUpdatesMsec)
        self.readDeliveryBlockerUpdatesMsecSet = True
        self.readDeliveryBlockerUpdatesMsec = readDeliveryBlockerUpdatesMsec

    def requestReadExternalStateMsec (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-readexternalstatemsec').debug3Func(): logFunc('called. requested=%s', requested)
        self.readExternalStateMsecRequested = requested
        self.readExternalStateMsecSet = False

    def isReadExternalStateMsecRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-readexternalstatemsec-requested').debug3Func(): logFunc('called. requested=%s', self.readExternalStateMsecRequested)
        return self.readExternalStateMsecRequested

    def getReadExternalStateMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-readexternalstatemsec').debug3Func(): logFunc('called. self.readExternalStateMsecSet=%s, self.readExternalStateMsec=%s', self.readExternalStateMsecSet, self.readExternalStateMsec)
        if self.readExternalStateMsecSet:
            return self.readExternalStateMsec
        return None

    def hasReadExternalStateMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-readexternalstatemsec').debug3Func(): logFunc('called. self.readExternalStateMsecSet=%s, self.readExternalStateMsec=%s', self.readExternalStateMsecSet, self.readExternalStateMsec)
        if self.readExternalStateMsecSet:
            return True
        return False

    def setReadExternalStateMsec (self, readExternalStateMsec):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-readexternalstatemsec').debug3Func(): logFunc('called. readExternalStateMsec=%s, old=%s', readExternalStateMsec, self.readExternalStateMsec)
        self.readExternalStateMsecSet = True
        self.readExternalStateMsec = readExternalStateMsec

    def requestWriteAcquiredTitlesMsec (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-writeacquiredtitlesmsec').debug3Func(): logFunc('called. requested=%s', requested)
        self.writeAcquiredTitlesMsecRequested = requested
        self.writeAcquiredTitlesMsecSet = False

    def isWriteAcquiredTitlesMsecRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-writeacquiredtitlesmsec-requested').debug3Func(): logFunc('called. requested=%s', self.writeAcquiredTitlesMsecRequested)
        return self.writeAcquiredTitlesMsecRequested

    def getWriteAcquiredTitlesMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-writeacquiredtitlesmsec').debug3Func(): logFunc('called. self.writeAcquiredTitlesMsecSet=%s, self.writeAcquiredTitlesMsec=%s', self.writeAcquiredTitlesMsecSet, self.writeAcquiredTitlesMsec)
        if self.writeAcquiredTitlesMsecSet:
            return self.writeAcquiredTitlesMsec
        return None

    def hasWriteAcquiredTitlesMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-writeacquiredtitlesmsec').debug3Func(): logFunc('called. self.writeAcquiredTitlesMsecSet=%s, self.writeAcquiredTitlesMsec=%s', self.writeAcquiredTitlesMsecSet, self.writeAcquiredTitlesMsec)
        if self.writeAcquiredTitlesMsecSet:
            return True
        return False

    def setWriteAcquiredTitlesMsec (self, writeAcquiredTitlesMsec):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-writeacquiredtitlesmsec').debug3Func(): logFunc('called. writeAcquiredTitlesMsec=%s, old=%s', writeAcquiredTitlesMsec, self.writeAcquiredTitlesMsec)
        self.writeAcquiredTitlesMsecSet = True
        self.writeAcquiredTitlesMsec = writeAcquiredTitlesMsec

    def requestReadExternalConfigMsec (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-readexternalconfigmsec').debug3Func(): logFunc('called. requested=%s', requested)
        self.readExternalConfigMsecRequested = requested
        self.readExternalConfigMsecSet = False

    def isReadExternalConfigMsecRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-readexternalconfigmsec-requested').debug3Func(): logFunc('called. requested=%s', self.readExternalConfigMsecRequested)
        return self.readExternalConfigMsecRequested

    def getReadExternalConfigMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-readexternalconfigmsec').debug3Func(): logFunc('called. self.readExternalConfigMsecSet=%s, self.readExternalConfigMsec=%s', self.readExternalConfigMsecSet, self.readExternalConfigMsec)
        if self.readExternalConfigMsecSet:
            return self.readExternalConfigMsec
        return None

    def hasReadExternalConfigMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-readexternalconfigmsec').debug3Func(): logFunc('called. self.readExternalConfigMsecSet=%s, self.readExternalConfigMsec=%s', self.readExternalConfigMsecSet, self.readExternalConfigMsec)
        if self.readExternalConfigMsecSet:
            return True
        return False

    def setReadExternalConfigMsec (self, readExternalConfigMsec):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-readexternalconfigmsec').debug3Func(): logFunc('called. readExternalConfigMsec=%s, old=%s', readExternalConfigMsec, self.readExternalConfigMsec)
        self.readExternalConfigMsecSet = True
        self.readExternalConfigMsec = readExternalConfigMsec

    def requestReadDeliveredTitlesMsec (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-readdeliveredtitlesmsec').debug3Func(): logFunc('called. requested=%s', requested)
        self.readDeliveredTitlesMsecRequested = requested
        self.readDeliveredTitlesMsecSet = False

    def isReadDeliveredTitlesMsecRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-readdeliveredtitlesmsec-requested').debug3Func(): logFunc('called. requested=%s', self.readDeliveredTitlesMsecRequested)
        return self.readDeliveredTitlesMsecRequested

    def getReadDeliveredTitlesMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-readdeliveredtitlesmsec').debug3Func(): logFunc('called. self.readDeliveredTitlesMsecSet=%s, self.readDeliveredTitlesMsec=%s', self.readDeliveredTitlesMsecSet, self.readDeliveredTitlesMsec)
        if self.readDeliveredTitlesMsecSet:
            return self.readDeliveredTitlesMsec
        return None

    def hasReadDeliveredTitlesMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-readdeliveredtitlesmsec').debug3Func(): logFunc('called. self.readDeliveredTitlesMsecSet=%s, self.readDeliveredTitlesMsec=%s', self.readDeliveredTitlesMsecSet, self.readDeliveredTitlesMsec)
        if self.readDeliveredTitlesMsecSet:
            return True
        return False

    def setReadDeliveredTitlesMsec (self, readDeliveredTitlesMsec):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-readdeliveredtitlesmsec').debug3Func(): logFunc('called. readDeliveredTitlesMsec=%s, old=%s', readDeliveredTitlesMsec, self.readDeliveredTitlesMsec)
        self.readDeliveredTitlesMsecSet = True
        self.readDeliveredTitlesMsec = readDeliveredTitlesMsec

    def requestRequestNeighbourDiscoveryMsec (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-requestneighbourdiscoverymsec').debug3Func(): logFunc('called. requested=%s', requested)
        self.requestNeighbourDiscoveryMsecRequested = requested
        self.requestNeighbourDiscoveryMsecSet = False

    def isRequestNeighbourDiscoveryMsecRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-requestneighbourdiscoverymsec-requested').debug3Func(): logFunc('called. requested=%s', self.requestNeighbourDiscoveryMsecRequested)
        return self.requestNeighbourDiscoveryMsecRequested

    def getRequestNeighbourDiscoveryMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-requestneighbourdiscoverymsec').debug3Func(): logFunc('called. self.requestNeighbourDiscoveryMsecSet=%s, self.requestNeighbourDiscoveryMsec=%s', self.requestNeighbourDiscoveryMsecSet, self.requestNeighbourDiscoveryMsec)
        if self.requestNeighbourDiscoveryMsecSet:
            return self.requestNeighbourDiscoveryMsec
        return None

    def hasRequestNeighbourDiscoveryMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-requestneighbourdiscoverymsec').debug3Func(): logFunc('called. self.requestNeighbourDiscoveryMsecSet=%s, self.requestNeighbourDiscoveryMsec=%s', self.requestNeighbourDiscoveryMsecSet, self.requestNeighbourDiscoveryMsec)
        if self.requestNeighbourDiscoveryMsecSet:
            return True
        return False

    def setRequestNeighbourDiscoveryMsec (self, requestNeighbourDiscoveryMsec):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-requestneighbourdiscoverymsec').debug3Func(): logFunc('called. requestNeighbourDiscoveryMsec=%s, old=%s', requestNeighbourDiscoveryMsec, self.requestNeighbourDiscoveryMsec)
        self.requestNeighbourDiscoveryMsecSet = True
        self.requestNeighbourDiscoveryMsec = requestNeighbourDiscoveryMsec

    def requestUpdateRedirectQuotaMsec (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-updateredirectquotamsec').debug3Func(): logFunc('called. requested=%s', requested)
        self.updateRedirectQuotaMsecRequested = requested
        self.updateRedirectQuotaMsecSet = False

    def isUpdateRedirectQuotaMsecRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-updateredirectquotamsec-requested').debug3Func(): logFunc('called. requested=%s', self.updateRedirectQuotaMsecRequested)
        return self.updateRedirectQuotaMsecRequested

    def getUpdateRedirectQuotaMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-updateredirectquotamsec').debug3Func(): logFunc('called. self.updateRedirectQuotaMsecSet=%s, self.updateRedirectQuotaMsec=%s', self.updateRedirectQuotaMsecSet, self.updateRedirectQuotaMsec)
        if self.updateRedirectQuotaMsecSet:
            return self.updateRedirectQuotaMsec
        return None

    def hasUpdateRedirectQuotaMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-updateredirectquotamsec').debug3Func(): logFunc('called. self.updateRedirectQuotaMsecSet=%s, self.updateRedirectQuotaMsec=%s', self.updateRedirectQuotaMsecSet, self.updateRedirectQuotaMsec)
        if self.updateRedirectQuotaMsecSet:
            return True
        return False

    def setUpdateRedirectQuotaMsec (self, updateRedirectQuotaMsec):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-updateredirectquotamsec').debug3Func(): logFunc('called. updateRedirectQuotaMsec=%s, old=%s', updateRedirectQuotaMsec, self.updateRedirectQuotaMsec)
        self.updateRedirectQuotaMsecSet = True
        self.updateRedirectQuotaMsec = updateRedirectQuotaMsec

    def requestCheckContentDisksSizeMsec (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-checkcontentdiskssizemsec').debug3Func(): logFunc('called. requested=%s', requested)
        self.checkContentDisksSizeMsecRequested = requested
        self.checkContentDisksSizeMsecSet = False

    def isCheckContentDisksSizeMsecRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-checkcontentdiskssizemsec-requested').debug3Func(): logFunc('called. requested=%s', self.checkContentDisksSizeMsecRequested)
        return self.checkContentDisksSizeMsecRequested

    def getCheckContentDisksSizeMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-checkcontentdiskssizemsec').debug3Func(): logFunc('called. self.checkContentDisksSizeMsecSet=%s, self.checkContentDisksSizeMsec=%s', self.checkContentDisksSizeMsecSet, self.checkContentDisksSizeMsec)
        if self.checkContentDisksSizeMsecSet:
            return self.checkContentDisksSizeMsec
        return None

    def hasCheckContentDisksSizeMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-checkcontentdiskssizemsec').debug3Func(): logFunc('called. self.checkContentDisksSizeMsecSet=%s, self.checkContentDisksSizeMsec=%s', self.checkContentDisksSizeMsecSet, self.checkContentDisksSizeMsec)
        if self.checkContentDisksSizeMsecSet:
            return True
        return False

    def setCheckContentDisksSizeMsec (self, checkContentDisksSizeMsec):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-checkcontentdiskssizemsec').debug3Func(): logFunc('called. checkContentDisksSizeMsec=%s, old=%s', checkContentDisksSizeMsec, self.checkContentDisksSizeMsec)
        self.checkContentDisksSizeMsecSet = True
        self.checkContentDisksSizeMsec = checkContentDisksSizeMsec

    def requestSampleCountersMsec (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-samplecountersmsec').debug3Func(): logFunc('called. requested=%s', requested)
        self.sampleCountersMsecRequested = requested
        self.sampleCountersMsecSet = False

    def isSampleCountersMsecRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-samplecountersmsec-requested').debug3Func(): logFunc('called. requested=%s', self.sampleCountersMsecRequested)
        return self.sampleCountersMsecRequested

    def getSampleCountersMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-samplecountersmsec').debug3Func(): logFunc('called. self.sampleCountersMsecSet=%s, self.sampleCountersMsec=%s', self.sampleCountersMsecSet, self.sampleCountersMsec)
        if self.sampleCountersMsecSet:
            return self.sampleCountersMsec
        return None

    def hasSampleCountersMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-samplecountersmsec').debug3Func(): logFunc('called. self.sampleCountersMsecSet=%s, self.sampleCountersMsec=%s', self.sampleCountersMsecSet, self.sampleCountersMsec)
        if self.sampleCountersMsecSet:
            return True
        return False

    def setSampleCountersMsec (self, sampleCountersMsec):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-samplecountersmsec').debug3Func(): logFunc('called. sampleCountersMsec=%s, old=%s', sampleCountersMsec, self.sampleCountersMsec)
        self.sampleCountersMsecSet = True
        self.sampleCountersMsec = sampleCountersMsec

    def requestAttenuatePastVolumeMsec (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-attenuatepastvolumemsec').debug3Func(): logFunc('called. requested=%s', requested)
        self.attenuatePastVolumeMsecRequested = requested
        self.attenuatePastVolumeMsecSet = False

    def isAttenuatePastVolumeMsecRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-attenuatepastvolumemsec-requested').debug3Func(): logFunc('called. requested=%s', self.attenuatePastVolumeMsecRequested)
        return self.attenuatePastVolumeMsecRequested

    def getAttenuatePastVolumeMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-attenuatepastvolumemsec').debug3Func(): logFunc('called. self.attenuatePastVolumeMsecSet=%s, self.attenuatePastVolumeMsec=%s', self.attenuatePastVolumeMsecSet, self.attenuatePastVolumeMsec)
        if self.attenuatePastVolumeMsecSet:
            return self.attenuatePastVolumeMsec
        return None

    def hasAttenuatePastVolumeMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-attenuatepastvolumemsec').debug3Func(): logFunc('called. self.attenuatePastVolumeMsecSet=%s, self.attenuatePastVolumeMsec=%s', self.attenuatePastVolumeMsecSet, self.attenuatePastVolumeMsec)
        if self.attenuatePastVolumeMsecSet:
            return True
        return False

    def setAttenuatePastVolumeMsec (self, attenuatePastVolumeMsec):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-attenuatepastvolumemsec').debug3Func(): logFunc('called. attenuatePastVolumeMsec=%s, old=%s', attenuatePastVolumeMsec, self.attenuatePastVolumeMsec)
        self.attenuatePastVolumeMsecSet = True
        self.attenuatePastVolumeMsec = attenuatePastVolumeMsec


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.readRedirectNeighbourTableMsec = 0
        self.readRedirectNeighbourTableMsecSet = False
        
        self.triggerTitleTableSaveMsec = 0
        self.triggerTitleTableSaveMsecSet = False
        
        self.readRedirectEnablerMsec = 0
        self.readRedirectEnablerMsecSet = False
        
        self.readBrownieQuotaMsec = 0
        self.readBrownieQuotaMsecSet = False
        
        self.logDebugStatsMsec = 0
        self.logDebugStatsMsecSet = False
        
        self.readDeliveryBlockerUpdatesMsec = 0
        self.readDeliveryBlockerUpdatesMsecSet = False
        
        self.readExternalStateMsec = 0
        self.readExternalStateMsecSet = False
        
        self.writeAcquiredTitlesMsec = 0
        self.writeAcquiredTitlesMsecSet = False
        
        self.readExternalConfigMsec = 0
        self.readExternalConfigMsecSet = False
        
        self.readDeliveredTitlesMsec = 0
        self.readDeliveredTitlesMsecSet = False
        
        self.requestNeighbourDiscoveryMsec = 0
        self.requestNeighbourDiscoveryMsecSet = False
        
        self.updateRedirectQuotaMsec = 0
        self.updateRedirectQuotaMsecSet = False
        
        self.checkContentDisksSizeMsec = 0
        self.checkContentDisksSizeMsecSet = False
        
        self.sampleCountersMsec = 0
        self.sampleCountersMsecSet = False
        
        self.attenuatePastVolumeMsec = 0
        self.attenuatePastVolumeMsecSet = False
        

    def _getSelfKeyPath (self, line
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("sub-task-interval", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("house-keeper", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("analyzer", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
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

        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasReadRedirectNeighbourTableMsec():
            valReadRedirectNeighbourTableMsec = Value()
            if self.readRedirectNeighbourTableMsec is not None:
                valReadRedirectNeighbourTableMsec.setInt64(self.readRedirectNeighbourTableMsec)
            else:
                valReadRedirectNeighbourTableMsec.setEmpty()
            tagValueList.push(("read-redirect-neighbour-table-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valReadRedirectNeighbourTableMsec)
        
        if self.hasTriggerTitleTableSaveMsec():
            valTriggerTitleTableSaveMsec = Value()
            if self.triggerTitleTableSaveMsec is not None:
                valTriggerTitleTableSaveMsec.setInt64(self.triggerTitleTableSaveMsec)
            else:
                valTriggerTitleTableSaveMsec.setEmpty()
            tagValueList.push(("trigger-title-table-save-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valTriggerTitleTableSaveMsec)
        
        if self.hasReadRedirectEnablerMsec():
            valReadRedirectEnablerMsec = Value()
            if self.readRedirectEnablerMsec is not None:
                valReadRedirectEnablerMsec.setInt64(self.readRedirectEnablerMsec)
            else:
                valReadRedirectEnablerMsec.setEmpty()
            tagValueList.push(("read-redirect-enabler-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valReadRedirectEnablerMsec)
        
        if self.hasReadBrownieQuotaMsec():
            valReadBrownieQuotaMsec = Value()
            if self.readBrownieQuotaMsec is not None:
                valReadBrownieQuotaMsec.setInt64(self.readBrownieQuotaMsec)
            else:
                valReadBrownieQuotaMsec.setEmpty()
            tagValueList.push(("read-brownie-quota-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valReadBrownieQuotaMsec)
        
        if self.hasLogDebugStatsMsec():
            valLogDebugStatsMsec = Value()
            if self.logDebugStatsMsec is not None:
                valLogDebugStatsMsec.setInt64(self.logDebugStatsMsec)
            else:
                valLogDebugStatsMsec.setEmpty()
            tagValueList.push(("log-debug-stats-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valLogDebugStatsMsec)
        
        if self.hasReadDeliveryBlockerUpdatesMsec():
            valReadDeliveryBlockerUpdatesMsec = Value()
            if self.readDeliveryBlockerUpdatesMsec is not None:
                valReadDeliveryBlockerUpdatesMsec.setInt64(self.readDeliveryBlockerUpdatesMsec)
            else:
                valReadDeliveryBlockerUpdatesMsec.setEmpty()
            tagValueList.push(("read-delivery-blocker-updates-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valReadDeliveryBlockerUpdatesMsec)
        
        if self.hasReadExternalStateMsec():
            valReadExternalStateMsec = Value()
            if self.readExternalStateMsec is not None:
                valReadExternalStateMsec.setInt64(self.readExternalStateMsec)
            else:
                valReadExternalStateMsec.setEmpty()
            tagValueList.push(("read-external-state-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valReadExternalStateMsec)
        
        if self.hasWriteAcquiredTitlesMsec():
            valWriteAcquiredTitlesMsec = Value()
            if self.writeAcquiredTitlesMsec is not None:
                valWriteAcquiredTitlesMsec.setInt64(self.writeAcquiredTitlesMsec)
            else:
                valWriteAcquiredTitlesMsec.setEmpty()
            tagValueList.push(("write-acquired-titles-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valWriteAcquiredTitlesMsec)
        
        if self.hasReadExternalConfigMsec():
            valReadExternalConfigMsec = Value()
            if self.readExternalConfigMsec is not None:
                valReadExternalConfigMsec.setInt64(self.readExternalConfigMsec)
            else:
                valReadExternalConfigMsec.setEmpty()
            tagValueList.push(("read-external-config-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valReadExternalConfigMsec)
        
        if self.hasReadDeliveredTitlesMsec():
            valReadDeliveredTitlesMsec = Value()
            if self.readDeliveredTitlesMsec is not None:
                valReadDeliveredTitlesMsec.setInt64(self.readDeliveredTitlesMsec)
            else:
                valReadDeliveredTitlesMsec.setEmpty()
            tagValueList.push(("read-delivered-titles-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valReadDeliveredTitlesMsec)
        
        if self.hasRequestNeighbourDiscoveryMsec():
            valRequestNeighbourDiscoveryMsec = Value()
            if self.requestNeighbourDiscoveryMsec is not None:
                valRequestNeighbourDiscoveryMsec.setInt64(self.requestNeighbourDiscoveryMsec)
            else:
                valRequestNeighbourDiscoveryMsec.setEmpty()
            tagValueList.push(("request-neighbour-discovery-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valRequestNeighbourDiscoveryMsec)
        
        if self.hasUpdateRedirectQuotaMsec():
            valUpdateRedirectQuotaMsec = Value()
            if self.updateRedirectQuotaMsec is not None:
                valUpdateRedirectQuotaMsec.setInt64(self.updateRedirectQuotaMsec)
            else:
                valUpdateRedirectQuotaMsec.setEmpty()
            tagValueList.push(("update-redirect-quota-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valUpdateRedirectQuotaMsec)
        
        if self.hasCheckContentDisksSizeMsec():
            valCheckContentDisksSizeMsec = Value()
            if self.checkContentDisksSizeMsec is not None:
                valCheckContentDisksSizeMsec.setInt64(self.checkContentDisksSizeMsec)
            else:
                valCheckContentDisksSizeMsec.setEmpty()
            tagValueList.push(("check-content-disks-size-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valCheckContentDisksSizeMsec)
        
        if self.hasSampleCountersMsec():
            valSampleCountersMsec = Value()
            if self.sampleCountersMsec is not None:
                valSampleCountersMsec.setInt64(self.sampleCountersMsec)
            else:
                valSampleCountersMsec.setEmpty()
            tagValueList.push(("sample-counters-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valSampleCountersMsec)
        
        if self.hasAttenuatePastVolumeMsec():
            valAttenuatePastVolumeMsec = Value()
            if self.attenuatePastVolumeMsec is not None:
                valAttenuatePastVolumeMsec.setInt64(self.attenuatePastVolumeMsec)
            else:
                valAttenuatePastVolumeMsec.setEmpty()
            tagValueList.push(("attenuate-past-volume-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valAttenuatePastVolumeMsec)
        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isReadRedirectNeighbourTableMsecRequested():
            valReadRedirectNeighbourTableMsec = Value()
            valReadRedirectNeighbourTableMsec.setEmpty()
            tagValueList.push(("read-redirect-neighbour-table-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valReadRedirectNeighbourTableMsec)
        
        if self.isTriggerTitleTableSaveMsecRequested():
            valTriggerTitleTableSaveMsec = Value()
            valTriggerTitleTableSaveMsec.setEmpty()
            tagValueList.push(("trigger-title-table-save-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valTriggerTitleTableSaveMsec)
        
        if self.isReadRedirectEnablerMsecRequested():
            valReadRedirectEnablerMsec = Value()
            valReadRedirectEnablerMsec.setEmpty()
            tagValueList.push(("read-redirect-enabler-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valReadRedirectEnablerMsec)
        
        if self.isReadBrownieQuotaMsecRequested():
            valReadBrownieQuotaMsec = Value()
            valReadBrownieQuotaMsec.setEmpty()
            tagValueList.push(("read-brownie-quota-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valReadBrownieQuotaMsec)
        
        if self.isLogDebugStatsMsecRequested():
            valLogDebugStatsMsec = Value()
            valLogDebugStatsMsec.setEmpty()
            tagValueList.push(("log-debug-stats-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valLogDebugStatsMsec)
        
        if self.isReadDeliveryBlockerUpdatesMsecRequested():
            valReadDeliveryBlockerUpdatesMsec = Value()
            valReadDeliveryBlockerUpdatesMsec.setEmpty()
            tagValueList.push(("read-delivery-blocker-updates-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valReadDeliveryBlockerUpdatesMsec)
        
        if self.isReadExternalStateMsecRequested():
            valReadExternalStateMsec = Value()
            valReadExternalStateMsec.setEmpty()
            tagValueList.push(("read-external-state-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valReadExternalStateMsec)
        
        if self.isWriteAcquiredTitlesMsecRequested():
            valWriteAcquiredTitlesMsec = Value()
            valWriteAcquiredTitlesMsec.setEmpty()
            tagValueList.push(("write-acquired-titles-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valWriteAcquiredTitlesMsec)
        
        if self.isReadExternalConfigMsecRequested():
            valReadExternalConfigMsec = Value()
            valReadExternalConfigMsec.setEmpty()
            tagValueList.push(("read-external-config-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valReadExternalConfigMsec)
        
        if self.isReadDeliveredTitlesMsecRequested():
            valReadDeliveredTitlesMsec = Value()
            valReadDeliveredTitlesMsec.setEmpty()
            tagValueList.push(("read-delivered-titles-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valReadDeliveredTitlesMsec)
        
        if self.isRequestNeighbourDiscoveryMsecRequested():
            valRequestNeighbourDiscoveryMsec = Value()
            valRequestNeighbourDiscoveryMsec.setEmpty()
            tagValueList.push(("request-neighbour-discovery-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valRequestNeighbourDiscoveryMsec)
        
        if self.isUpdateRedirectQuotaMsecRequested():
            valUpdateRedirectQuotaMsec = Value()
            valUpdateRedirectQuotaMsec.setEmpty()
            tagValueList.push(("update-redirect-quota-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valUpdateRedirectQuotaMsec)
        
        if self.isCheckContentDisksSizeMsecRequested():
            valCheckContentDisksSizeMsec = Value()
            valCheckContentDisksSizeMsec.setEmpty()
            tagValueList.push(("check-content-disks-size-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valCheckContentDisksSizeMsec)
        
        if self.isSampleCountersMsecRequested():
            valSampleCountersMsec = Value()
            valSampleCountersMsec.setEmpty()
            tagValueList.push(("sample-counters-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valSampleCountersMsec)
        
        if self.isAttenuatePastVolumeMsecRequested():
            valAttenuatePastVolumeMsec = Value()
            valAttenuatePastVolumeMsec.setEmpty()
            tagValueList.push(("attenuate-past-volume-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valAttenuatePastVolumeMsec)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isReadRedirectNeighbourTableMsecRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "read-redirect-neighbour-table-msec") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-readredirectneighbourtablemsec').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "readRedirectNeighbourTableMsec", "read-redirect-neighbour-table-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-read-redirect-neighbour-table-msec-bad-value').infoFunc(): logFunc('readRedirectNeighbourTableMsec not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setReadRedirectNeighbourTableMsec(tempVar)
            for logFunc in self._log('read-tag-values-read-redirect-neighbour-table-msec').debug3Func(): logFunc('read readRedirectNeighbourTableMsec. readRedirectNeighbourTableMsec=%s, tempValue=%s', self.readRedirectNeighbourTableMsec, tempValue.getType())
        
        if self.isTriggerTitleTableSaveMsecRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "trigger-title-table-save-msec") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-triggertitletablesavemsec').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "triggerTitleTableSaveMsec", "trigger-title-table-save-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-trigger-title-table-save-msec-bad-value').infoFunc(): logFunc('triggerTitleTableSaveMsec not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTriggerTitleTableSaveMsec(tempVar)
            for logFunc in self._log('read-tag-values-trigger-title-table-save-msec').debug3Func(): logFunc('read triggerTitleTableSaveMsec. triggerTitleTableSaveMsec=%s, tempValue=%s', self.triggerTitleTableSaveMsec, tempValue.getType())
        
        if self.isReadRedirectEnablerMsecRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "read-redirect-enabler-msec") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-readredirectenablermsec').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "readRedirectEnablerMsec", "read-redirect-enabler-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-read-redirect-enabler-msec-bad-value').infoFunc(): logFunc('readRedirectEnablerMsec not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setReadRedirectEnablerMsec(tempVar)
            for logFunc in self._log('read-tag-values-read-redirect-enabler-msec').debug3Func(): logFunc('read readRedirectEnablerMsec. readRedirectEnablerMsec=%s, tempValue=%s', self.readRedirectEnablerMsec, tempValue.getType())
        
        if self.isReadBrownieQuotaMsecRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "read-brownie-quota-msec") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-readbrowniequotamsec').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "readBrownieQuotaMsec", "read-brownie-quota-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-read-brownie-quota-msec-bad-value').infoFunc(): logFunc('readBrownieQuotaMsec not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setReadBrownieQuotaMsec(tempVar)
            for logFunc in self._log('read-tag-values-read-brownie-quota-msec').debug3Func(): logFunc('read readBrownieQuotaMsec. readBrownieQuotaMsec=%s, tempValue=%s', self.readBrownieQuotaMsec, tempValue.getType())
        
        if self.isLogDebugStatsMsecRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "log-debug-stats-msec") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-logdebugstatsmsec').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "logDebugStatsMsec", "log-debug-stats-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-log-debug-stats-msec-bad-value').infoFunc(): logFunc('logDebugStatsMsec not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setLogDebugStatsMsec(tempVar)
            for logFunc in self._log('read-tag-values-log-debug-stats-msec').debug3Func(): logFunc('read logDebugStatsMsec. logDebugStatsMsec=%s, tempValue=%s', self.logDebugStatsMsec, tempValue.getType())
        
        if self.isReadDeliveryBlockerUpdatesMsecRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "read-delivery-blocker-updates-msec") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-readdeliveryblockerupdatesmsec').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "readDeliveryBlockerUpdatesMsec", "read-delivery-blocker-updates-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-read-delivery-blocker-updates-msec-bad-value').infoFunc(): logFunc('readDeliveryBlockerUpdatesMsec not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setReadDeliveryBlockerUpdatesMsec(tempVar)
            for logFunc in self._log('read-tag-values-read-delivery-blocker-updates-msec').debug3Func(): logFunc('read readDeliveryBlockerUpdatesMsec. readDeliveryBlockerUpdatesMsec=%s, tempValue=%s', self.readDeliveryBlockerUpdatesMsec, tempValue.getType())
        
        if self.isReadExternalStateMsecRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "read-external-state-msec") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-readexternalstatemsec').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "readExternalStateMsec", "read-external-state-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-read-external-state-msec-bad-value').infoFunc(): logFunc('readExternalStateMsec not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setReadExternalStateMsec(tempVar)
            for logFunc in self._log('read-tag-values-read-external-state-msec').debug3Func(): logFunc('read readExternalStateMsec. readExternalStateMsec=%s, tempValue=%s', self.readExternalStateMsec, tempValue.getType())
        
        if self.isWriteAcquiredTitlesMsecRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "write-acquired-titles-msec") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-writeacquiredtitlesmsec').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "writeAcquiredTitlesMsec", "write-acquired-titles-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-write-acquired-titles-msec-bad-value').infoFunc(): logFunc('writeAcquiredTitlesMsec not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setWriteAcquiredTitlesMsec(tempVar)
            for logFunc in self._log('read-tag-values-write-acquired-titles-msec').debug3Func(): logFunc('read writeAcquiredTitlesMsec. writeAcquiredTitlesMsec=%s, tempValue=%s', self.writeAcquiredTitlesMsec, tempValue.getType())
        
        if self.isReadExternalConfigMsecRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "read-external-config-msec") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-readexternalconfigmsec').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "readExternalConfigMsec", "read-external-config-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-read-external-config-msec-bad-value').infoFunc(): logFunc('readExternalConfigMsec not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setReadExternalConfigMsec(tempVar)
            for logFunc in self._log('read-tag-values-read-external-config-msec').debug3Func(): logFunc('read readExternalConfigMsec. readExternalConfigMsec=%s, tempValue=%s', self.readExternalConfigMsec, tempValue.getType())
        
        if self.isReadDeliveredTitlesMsecRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "read-delivered-titles-msec") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-readdeliveredtitlesmsec').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "readDeliveredTitlesMsec", "read-delivered-titles-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-read-delivered-titles-msec-bad-value').infoFunc(): logFunc('readDeliveredTitlesMsec not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setReadDeliveredTitlesMsec(tempVar)
            for logFunc in self._log('read-tag-values-read-delivered-titles-msec').debug3Func(): logFunc('read readDeliveredTitlesMsec. readDeliveredTitlesMsec=%s, tempValue=%s', self.readDeliveredTitlesMsec, tempValue.getType())
        
        if self.isRequestNeighbourDiscoveryMsecRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "request-neighbour-discovery-msec") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-requestneighbourdiscoverymsec').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "requestNeighbourDiscoveryMsec", "request-neighbour-discovery-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-request-neighbour-discovery-msec-bad-value').infoFunc(): logFunc('requestNeighbourDiscoveryMsec not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setRequestNeighbourDiscoveryMsec(tempVar)
            for logFunc in self._log('read-tag-values-request-neighbour-discovery-msec').debug3Func(): logFunc('read requestNeighbourDiscoveryMsec. requestNeighbourDiscoveryMsec=%s, tempValue=%s', self.requestNeighbourDiscoveryMsec, tempValue.getType())
        
        if self.isUpdateRedirectQuotaMsecRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "update-redirect-quota-msec") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-updateredirectquotamsec').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "updateRedirectQuotaMsec", "update-redirect-quota-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-update-redirect-quota-msec-bad-value').infoFunc(): logFunc('updateRedirectQuotaMsec not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setUpdateRedirectQuotaMsec(tempVar)
            for logFunc in self._log('read-tag-values-update-redirect-quota-msec').debug3Func(): logFunc('read updateRedirectQuotaMsec. updateRedirectQuotaMsec=%s, tempValue=%s', self.updateRedirectQuotaMsec, tempValue.getType())
        
        if self.isCheckContentDisksSizeMsecRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "check-content-disks-size-msec") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-checkcontentdiskssizemsec').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "checkContentDisksSizeMsec", "check-content-disks-size-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-check-content-disks-size-msec-bad-value').infoFunc(): logFunc('checkContentDisksSizeMsec not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setCheckContentDisksSizeMsec(tempVar)
            for logFunc in self._log('read-tag-values-check-content-disks-size-msec').debug3Func(): logFunc('read checkContentDisksSizeMsec. checkContentDisksSizeMsec=%s, tempValue=%s', self.checkContentDisksSizeMsec, tempValue.getType())
        
        if self.isSampleCountersMsecRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "sample-counters-msec") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-samplecountersmsec').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "sampleCountersMsec", "sample-counters-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-sample-counters-msec-bad-value').infoFunc(): logFunc('sampleCountersMsec not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setSampleCountersMsec(tempVar)
            for logFunc in self._log('read-tag-values-sample-counters-msec').debug3Func(): logFunc('read sampleCountersMsec. sampleCountersMsec=%s, tempValue=%s', self.sampleCountersMsec, tempValue.getType())
        
        if self.isAttenuatePastVolumeMsecRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "attenuate-past-volume-msec") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-attenuatepastvolumemsec').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "attenuatePastVolumeMsec", "attenuate-past-volume-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-attenuate-past-volume-msec-bad-value').infoFunc(): logFunc('attenuatePastVolumeMsec not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setAttenuatePastVolumeMsec(tempVar)
            for logFunc in self._log('read-tag-values-attenuate-past-volume-msec').debug3Func(): logFunc('read attenuatePastVolumeMsec. attenuatePastVolumeMsec=%s, tempValue=%s', self.attenuatePastVolumeMsec, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "subTaskInterval", 
        "namespace": "sub_task_interval", 
        "className": "SubTaskIntervalMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.system_defaults.analyzer.house_keeper.sub_task_interval.sub_task_interval_maapi_gen import SubTaskIntervalMaapi", 
        "baseClassName": "SubTaskIntervalMaapiBase", 
        "baseModule": "sub_task_interval_maapi_base_gen"
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
            "isCurrent": false, 
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
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "system-defaults"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "yangName": "analyzer", 
            "namespace": "analyzer", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "analyzer"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "yangName": "house-keeper", 
            "namespace": "house_keeper", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "house-keeper"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "yangName": "sub-task-interval", 
            "namespace": "sub_task_interval", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "sub-task-interval"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "readRedirectNeighbourTableMsec", 
            "yangName": "read-redirect-neighbour-table-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "triggerTitleTableSaveMsec", 
            "yangName": "trigger-title-table-save-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "readRedirectEnablerMsec", 
            "yangName": "read-redirect-enabler-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "readBrownieQuotaMsec", 
            "yangName": "read-brownie-quota-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "logDebugStatsMsec", 
            "yangName": "log-debug-stats-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "readDeliveryBlockerUpdatesMsec", 
            "yangName": "read-delivery-blocker-updates-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "readExternalStateMsec", 
            "yangName": "read-external-state-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "writeAcquiredTitlesMsec", 
            "yangName": "write-acquired-titles-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "readExternalConfigMsec", 
            "yangName": "read-external-config-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "readDeliveredTitlesMsec", 
            "yangName": "read-delivered-titles-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "requestNeighbourDiscoveryMsec", 
            "yangName": "request-neighbour-discovery-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "updateRedirectQuotaMsec", 
            "yangName": "update-redirect-quota-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "checkContentDisksSizeMsec", 
            "yangName": "check-content-disks-size-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "sampleCountersMsec", 
            "yangName": "sample-counters-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "attenuatePastVolumeMsec", 
            "yangName": "attenuate-past-volume-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
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
            "typeHandler": "handler: IntHandler", 
            "memberName": "readRedirectNeighbourTableMsec", 
            "yangName": "read-redirect-neighbour-table-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "triggerTitleTableSaveMsec", 
            "yangName": "trigger-title-table-save-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "readRedirectEnablerMsec", 
            "yangName": "read-redirect-enabler-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "readBrownieQuotaMsec", 
            "yangName": "read-brownie-quota-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "logDebugStatsMsec", 
            "yangName": "log-debug-stats-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "readDeliveryBlockerUpdatesMsec", 
            "yangName": "read-delivery-blocker-updates-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "readExternalStateMsec", 
            "yangName": "read-external-state-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "writeAcquiredTitlesMsec", 
            "yangName": "write-acquired-titles-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "readExternalConfigMsec", 
            "yangName": "read-external-config-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "readDeliveredTitlesMsec", 
            "yangName": "read-delivered-titles-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "requestNeighbourDiscoveryMsec", 
            "yangName": "request-neighbour-discovery-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "updateRedirectQuotaMsec", 
            "yangName": "update-redirect-quota-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "checkContentDisksSizeMsec", 
            "yangName": "check-content-disks-size-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "sampleCountersMsec", 
            "yangName": "sample-counters-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "attenuatePastVolumeMsec", 
            "yangName": "attenuate-past-volume-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


