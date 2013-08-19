


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

from instances_maapi_base_gen import InstancesMaapiBase




class BlinkyInstancesMaapi(InstancesMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-instances")
        self.domain = None

        

        
        self.warnTotalRecordCountRequested = False
        self.warnTotalRecordCount = None
        self.warnTotalRecordCountSet = False
        
        self.periodicWorkRecordCountRequested = False
        self.periodicWorkRecordCount = None
        self.periodicWorkRecordCountSet = False
        
        self.aggregationPeriodRequested = False
        self.aggregationPeriod = None
        self.aggregationPeriodSet = False
        
        self.maxTotalRecordCountRequested = False
        self.maxTotalRecordCount = None
        self.maxTotalRecordCountSet = False
        
        self.periodicWorkIntervalRequested = False
        self.periodicWorkInterval = None
        self.periodicWorkIntervalSet = False
        
        self.warnSessionIdCountRequested = False
        self.warnSessionIdCount = None
        self.warnSessionIdCountSet = False
        
        self.instanceRequested = False
        self.instance = None
        self.instanceSet = False
        
        self.maxSessionIdCountRequested = False
        self.maxSessionIdCount = None
        self.maxSessionIdCountSet = False
        
        self.rotateFileIntervalRequested = False
        self.rotateFileInterval = None
        self.rotateFileIntervalSet = False
        
        self.recordWriteIntervalRequested = False
        self.recordWriteInterval = None
        self.recordWriteIntervalSet = False
        
        self.archiveRequested = False
        self.archive = None
        self.archiveSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestWarnTotalRecordCount(True)
        
        self.requestPeriodicWorkRecordCount(True)
        
        self.requestAggregationPeriod(True)
        
        self.requestMaxTotalRecordCount(True)
        
        self.requestPeriodicWorkInterval(True)
        
        self.requestWarnSessionIdCount(True)
        
        self.requestInstance(True)
        
        self.requestMaxSessionIdCount(True)
        
        self.requestRotateFileInterval(True)
        
        self.requestRecordWriteInterval(True)
        
        self.requestArchive(True)
        
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestWarnTotalRecordCount(True)
        
        self.requestPeriodicWorkRecordCount(True)
        
        self.requestAggregationPeriod(True)
        
        self.requestMaxTotalRecordCount(True)
        
        self.requestPeriodicWorkInterval(True)
        
        self.requestWarnSessionIdCount(True)
        
        self.requestInstance(True)
        
        self.requestMaxSessionIdCount(True)
        
        self.requestRotateFileInterval(True)
        
        self.requestRecordWriteInterval(True)
        
        self.requestArchive(True)
        
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestWarnTotalRecordCount(False)
        
        self.requestPeriodicWorkRecordCount(False)
        
        self.requestAggregationPeriod(False)
        
        self.requestMaxTotalRecordCount(False)
        
        self.requestPeriodicWorkInterval(False)
        
        self.requestWarnSessionIdCount(False)
        
        self.requestInstance(False)
        
        self.requestMaxSessionIdCount(False)
        
        self.requestRotateFileInterval(False)
        
        self.requestRecordWriteInterval(False)
        
        self.requestArchive(False)
        
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestWarnTotalRecordCount(False)
        
        self.requestPeriodicWorkRecordCount(False)
        
        self.requestAggregationPeriod(False)
        
        self.requestMaxTotalRecordCount(False)
        
        self.requestPeriodicWorkInterval(False)
        
        self.requestWarnSessionIdCount(False)
        
        self.requestInstance(False)
        
        self.requestMaxSessionIdCount(False)
        
        self.requestRotateFileInterval(False)
        
        self.requestRecordWriteInterval(False)
        
        self.requestArchive(False)
        
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setWarnTotalRecordCount(None)
        self.warnTotalRecordCountSet = False
        
        self.setPeriodicWorkRecordCount(None)
        self.periodicWorkRecordCountSet = False
        
        self.setAggregationPeriod(None)
        self.aggregationPeriodSet = False
        
        self.setMaxTotalRecordCount(None)
        self.maxTotalRecordCountSet = False
        
        self.setPeriodicWorkInterval(None)
        self.periodicWorkIntervalSet = False
        
        self.setWarnSessionIdCount(None)
        self.warnSessionIdCountSet = False
        
        self.setInstance(None)
        self.instanceSet = False
        
        self.setMaxSessionIdCount(None)
        self.maxSessionIdCountSet = False
        
        self.setRotateFileInterval(None)
        self.rotateFileIntervalSet = False
        
        self.setRecordWriteInterval(None)
        self.recordWriteIntervalSet = False
        
        self.setArchive(None)
        self.archiveSet = False
        
        

    def write (self
              , instances
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(instances, trxContext)

    def read (self
              , instances
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(instances, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , instances
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(instances, 
                                  True,
                                  trxContext)



    def requestWarnTotalRecordCount (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-warntotalrecordcount').debug3Func(): logFunc('called. requested=%s', requested)
        self.warnTotalRecordCountRequested = requested
        self.warnTotalRecordCountSet = False

    def isWarnTotalRecordCountRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-warntotalrecordcount-requested').debug3Func(): logFunc('called. requested=%s', self.warnTotalRecordCountRequested)
        return self.warnTotalRecordCountRequested

    def getWarnTotalRecordCount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-warntotalrecordcount').debug3Func(): logFunc('called. self.warnTotalRecordCountSet=%s, self.warnTotalRecordCount=%s', self.warnTotalRecordCountSet, self.warnTotalRecordCount)
        if self.warnTotalRecordCountSet:
            return self.warnTotalRecordCount
        return None

    def hasWarnTotalRecordCount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-warntotalrecordcount').debug3Func(): logFunc('called. self.warnTotalRecordCountSet=%s, self.warnTotalRecordCount=%s', self.warnTotalRecordCountSet, self.warnTotalRecordCount)
        if self.warnTotalRecordCountSet:
            return True
        return False

    def setWarnTotalRecordCount (self, warnTotalRecordCount):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-warntotalrecordcount').debug3Func(): logFunc('called. warnTotalRecordCount=%s, old=%s', warnTotalRecordCount, self.warnTotalRecordCount)
        self.warnTotalRecordCountSet = True
        self.warnTotalRecordCount = warnTotalRecordCount

    def requestPeriodicWorkRecordCount (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-periodicworkrecordcount').debug3Func(): logFunc('called. requested=%s', requested)
        self.periodicWorkRecordCountRequested = requested
        self.periodicWorkRecordCountSet = False

    def isPeriodicWorkRecordCountRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-periodicworkrecordcount-requested').debug3Func(): logFunc('called. requested=%s', self.periodicWorkRecordCountRequested)
        return self.periodicWorkRecordCountRequested

    def getPeriodicWorkRecordCount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-periodicworkrecordcount').debug3Func(): logFunc('called. self.periodicWorkRecordCountSet=%s, self.periodicWorkRecordCount=%s', self.periodicWorkRecordCountSet, self.periodicWorkRecordCount)
        if self.periodicWorkRecordCountSet:
            return self.periodicWorkRecordCount
        return None

    def hasPeriodicWorkRecordCount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-periodicworkrecordcount').debug3Func(): logFunc('called. self.periodicWorkRecordCountSet=%s, self.periodicWorkRecordCount=%s', self.periodicWorkRecordCountSet, self.periodicWorkRecordCount)
        if self.periodicWorkRecordCountSet:
            return True
        return False

    def setPeriodicWorkRecordCount (self, periodicWorkRecordCount):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-periodicworkrecordcount').debug3Func(): logFunc('called. periodicWorkRecordCount=%s, old=%s', periodicWorkRecordCount, self.periodicWorkRecordCount)
        self.periodicWorkRecordCountSet = True
        self.periodicWorkRecordCount = periodicWorkRecordCount

    def requestAggregationPeriod (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-aggregationperiod').debug3Func(): logFunc('called. requested=%s', requested)
        self.aggregationPeriodRequested = requested
        self.aggregationPeriodSet = False

    def isAggregationPeriodRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-aggregationperiod-requested').debug3Func(): logFunc('called. requested=%s', self.aggregationPeriodRequested)
        return self.aggregationPeriodRequested

    def getAggregationPeriod (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-aggregationperiod').debug3Func(): logFunc('called. self.aggregationPeriodSet=%s, self.aggregationPeriod=%s', self.aggregationPeriodSet, self.aggregationPeriod)
        if self.aggregationPeriodSet:
            return self.aggregationPeriod
        return None

    def hasAggregationPeriod (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-aggregationperiod').debug3Func(): logFunc('called. self.aggregationPeriodSet=%s, self.aggregationPeriod=%s', self.aggregationPeriodSet, self.aggregationPeriod)
        if self.aggregationPeriodSet:
            return True
        return False

    def setAggregationPeriod (self, aggregationPeriod):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-aggregationperiod').debug3Func(): logFunc('called. aggregationPeriod=%s, old=%s', aggregationPeriod, self.aggregationPeriod)
        self.aggregationPeriodSet = True
        self.aggregationPeriod = aggregationPeriod

    def requestMaxTotalRecordCount (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-maxtotalrecordcount').debug3Func(): logFunc('called. requested=%s', requested)
        self.maxTotalRecordCountRequested = requested
        self.maxTotalRecordCountSet = False

    def isMaxTotalRecordCountRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-maxtotalrecordcount-requested').debug3Func(): logFunc('called. requested=%s', self.maxTotalRecordCountRequested)
        return self.maxTotalRecordCountRequested

    def getMaxTotalRecordCount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-maxtotalrecordcount').debug3Func(): logFunc('called. self.maxTotalRecordCountSet=%s, self.maxTotalRecordCount=%s', self.maxTotalRecordCountSet, self.maxTotalRecordCount)
        if self.maxTotalRecordCountSet:
            return self.maxTotalRecordCount
        return None

    def hasMaxTotalRecordCount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-maxtotalrecordcount').debug3Func(): logFunc('called. self.maxTotalRecordCountSet=%s, self.maxTotalRecordCount=%s', self.maxTotalRecordCountSet, self.maxTotalRecordCount)
        if self.maxTotalRecordCountSet:
            return True
        return False

    def setMaxTotalRecordCount (self, maxTotalRecordCount):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-maxtotalrecordcount').debug3Func(): logFunc('called. maxTotalRecordCount=%s, old=%s', maxTotalRecordCount, self.maxTotalRecordCount)
        self.maxTotalRecordCountSet = True
        self.maxTotalRecordCount = maxTotalRecordCount

    def requestPeriodicWorkInterval (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-periodicworkinterval').debug3Func(): logFunc('called. requested=%s', requested)
        self.periodicWorkIntervalRequested = requested
        self.periodicWorkIntervalSet = False

    def isPeriodicWorkIntervalRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-periodicworkinterval-requested').debug3Func(): logFunc('called. requested=%s', self.periodicWorkIntervalRequested)
        return self.periodicWorkIntervalRequested

    def getPeriodicWorkInterval (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-periodicworkinterval').debug3Func(): logFunc('called. self.periodicWorkIntervalSet=%s, self.periodicWorkInterval=%s', self.periodicWorkIntervalSet, self.periodicWorkInterval)
        if self.periodicWorkIntervalSet:
            return self.periodicWorkInterval
        return None

    def hasPeriodicWorkInterval (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-periodicworkinterval').debug3Func(): logFunc('called. self.periodicWorkIntervalSet=%s, self.periodicWorkInterval=%s', self.periodicWorkIntervalSet, self.periodicWorkInterval)
        if self.periodicWorkIntervalSet:
            return True
        return False

    def setPeriodicWorkInterval (self, periodicWorkInterval):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-periodicworkinterval').debug3Func(): logFunc('called. periodicWorkInterval=%s, old=%s', periodicWorkInterval, self.periodicWorkInterval)
        self.periodicWorkIntervalSet = True
        self.periodicWorkInterval = periodicWorkInterval

    def requestWarnSessionIdCount (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-warnsessionidcount').debug3Func(): logFunc('called. requested=%s', requested)
        self.warnSessionIdCountRequested = requested
        self.warnSessionIdCountSet = False

    def isWarnSessionIdCountRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-warnsessionidcount-requested').debug3Func(): logFunc('called. requested=%s', self.warnSessionIdCountRequested)
        return self.warnSessionIdCountRequested

    def getWarnSessionIdCount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-warnsessionidcount').debug3Func(): logFunc('called. self.warnSessionIdCountSet=%s, self.warnSessionIdCount=%s', self.warnSessionIdCountSet, self.warnSessionIdCount)
        if self.warnSessionIdCountSet:
            return self.warnSessionIdCount
        return None

    def hasWarnSessionIdCount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-warnsessionidcount').debug3Func(): logFunc('called. self.warnSessionIdCountSet=%s, self.warnSessionIdCount=%s', self.warnSessionIdCountSet, self.warnSessionIdCount)
        if self.warnSessionIdCountSet:
            return True
        return False

    def setWarnSessionIdCount (self, warnSessionIdCount):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-warnsessionidcount').debug3Func(): logFunc('called. warnSessionIdCount=%s, old=%s', warnSessionIdCount, self.warnSessionIdCount)
        self.warnSessionIdCountSet = True
        self.warnSessionIdCount = warnSessionIdCount

    def requestInstance (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-instance').debug3Func(): logFunc('called. requested=%s', requested)
        self.instanceRequested = requested
        self.instanceSet = False

    def isInstanceRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-instance-requested').debug3Func(): logFunc('called. requested=%s', self.instanceRequested)
        return self.instanceRequested

    def getInstance (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-instance').debug3Func(): logFunc('called. self.instanceSet=%s, self.instance=%s', self.instanceSet, self.instance)
        if self.instanceSet:
            return self.instance
        return None

    def hasInstance (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-instance').debug3Func(): logFunc('called. self.instanceSet=%s, self.instance=%s', self.instanceSet, self.instance)
        if self.instanceSet:
            return True
        return False

    def setInstance (self, instance):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-instance').debug3Func(): logFunc('called. instance=%s, old=%s', instance, self.instance)
        self.instanceSet = True
        self.instance = instance

    def requestMaxSessionIdCount (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-maxsessionidcount').debug3Func(): logFunc('called. requested=%s', requested)
        self.maxSessionIdCountRequested = requested
        self.maxSessionIdCountSet = False

    def isMaxSessionIdCountRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-maxsessionidcount-requested').debug3Func(): logFunc('called. requested=%s', self.maxSessionIdCountRequested)
        return self.maxSessionIdCountRequested

    def getMaxSessionIdCount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-maxsessionidcount').debug3Func(): logFunc('called. self.maxSessionIdCountSet=%s, self.maxSessionIdCount=%s', self.maxSessionIdCountSet, self.maxSessionIdCount)
        if self.maxSessionIdCountSet:
            return self.maxSessionIdCount
        return None

    def hasMaxSessionIdCount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-maxsessionidcount').debug3Func(): logFunc('called. self.maxSessionIdCountSet=%s, self.maxSessionIdCount=%s', self.maxSessionIdCountSet, self.maxSessionIdCount)
        if self.maxSessionIdCountSet:
            return True
        return False

    def setMaxSessionIdCount (self, maxSessionIdCount):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-maxsessionidcount').debug3Func(): logFunc('called. maxSessionIdCount=%s, old=%s', maxSessionIdCount, self.maxSessionIdCount)
        self.maxSessionIdCountSet = True
        self.maxSessionIdCount = maxSessionIdCount

    def requestRotateFileInterval (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-rotatefileinterval').debug3Func(): logFunc('called. requested=%s', requested)
        self.rotateFileIntervalRequested = requested
        self.rotateFileIntervalSet = False

    def isRotateFileIntervalRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-rotatefileinterval-requested').debug3Func(): logFunc('called. requested=%s', self.rotateFileIntervalRequested)
        return self.rotateFileIntervalRequested

    def getRotateFileInterval (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-rotatefileinterval').debug3Func(): logFunc('called. self.rotateFileIntervalSet=%s, self.rotateFileInterval=%s', self.rotateFileIntervalSet, self.rotateFileInterval)
        if self.rotateFileIntervalSet:
            return self.rotateFileInterval
        return None

    def hasRotateFileInterval (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-rotatefileinterval').debug3Func(): logFunc('called. self.rotateFileIntervalSet=%s, self.rotateFileInterval=%s', self.rotateFileIntervalSet, self.rotateFileInterval)
        if self.rotateFileIntervalSet:
            return True
        return False

    def setRotateFileInterval (self, rotateFileInterval):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-rotatefileinterval').debug3Func(): logFunc('called. rotateFileInterval=%s, old=%s', rotateFileInterval, self.rotateFileInterval)
        self.rotateFileIntervalSet = True
        self.rotateFileInterval = rotateFileInterval

    def requestRecordWriteInterval (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-recordwriteinterval').debug3Func(): logFunc('called. requested=%s', requested)
        self.recordWriteIntervalRequested = requested
        self.recordWriteIntervalSet = False

    def isRecordWriteIntervalRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-recordwriteinterval-requested').debug3Func(): logFunc('called. requested=%s', self.recordWriteIntervalRequested)
        return self.recordWriteIntervalRequested

    def getRecordWriteInterval (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-recordwriteinterval').debug3Func(): logFunc('called. self.recordWriteIntervalSet=%s, self.recordWriteInterval=%s', self.recordWriteIntervalSet, self.recordWriteInterval)
        if self.recordWriteIntervalSet:
            return self.recordWriteInterval
        return None

    def hasRecordWriteInterval (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-recordwriteinterval').debug3Func(): logFunc('called. self.recordWriteIntervalSet=%s, self.recordWriteInterval=%s', self.recordWriteIntervalSet, self.recordWriteInterval)
        if self.recordWriteIntervalSet:
            return True
        return False

    def setRecordWriteInterval (self, recordWriteInterval):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-recordwriteinterval').debug3Func(): logFunc('called. recordWriteInterval=%s, old=%s', recordWriteInterval, self.recordWriteInterval)
        self.recordWriteIntervalSet = True
        self.recordWriteInterval = recordWriteInterval

    def requestArchive (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-archive').debug3Func(): logFunc('called. requested=%s', requested)
        self.archiveRequested = requested
        self.archiveSet = False

    def isArchiveRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-archive-requested').debug3Func(): logFunc('called. requested=%s', self.archiveRequested)
        return self.archiveRequested

    def getArchive (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-archive').debug3Func(): logFunc('called. self.archiveSet=%s, self.archive=%s', self.archiveSet, self.archive)
        if self.archiveSet:
            return self.archive
        return None

    def hasArchive (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-archive').debug3Func(): logFunc('called. self.archiveSet=%s, self.archive=%s', self.archiveSet, self.archive)
        if self.archiveSet:
            return True
        return False

    def setArchive (self, archive):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-archive').debug3Func(): logFunc('called. archive=%s, old=%s', archive, self.archive)
        self.archiveSet = True
        self.archive = archive


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.warnTotalRecordCount = 0
        self.warnTotalRecordCountSet = False
        
        self.periodicWorkRecordCount = 0
        self.periodicWorkRecordCountSet = False
        
        self.aggregationPeriod = 0
        self.aggregationPeriodSet = False
        
        self.maxTotalRecordCount = 0
        self.maxTotalRecordCountSet = False
        
        self.periodicWorkInterval = 0
        self.periodicWorkIntervalSet = False
        
        self.warnSessionIdCount = 0
        self.warnSessionIdCountSet = False
        
        self.instance = 0
        self.instanceSet = False
        
        self.maxSessionIdCount = 0
        self.maxSessionIdCountSet = False
        
        self.rotateFileInterval = 0
        self.rotateFileIntervalSet = False
        
        self.recordWriteInterval = 0
        self.recordWriteIntervalSet = False
        
        self.archive = 0
        self.archiveSet = False
        

    def _getSelfKeyPath (self, instances
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        ancestorVal = Value()
        ancestorVal.setString(instances);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("instances", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", "qtc-pt"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("pre-topper", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", "qtc-pt"))
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
                        instances, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(instances, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(instances, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       instances, 
                       
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

        keyPath = self._getSelfKeyPath(instances, 
                                       
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
                               instances, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasWarnTotalRecordCount():
            valWarnTotalRecordCount = Value()
            if self.warnTotalRecordCount is not None:
                valWarnTotalRecordCount.setInt64(self.warnTotalRecordCount)
            else:
                valWarnTotalRecordCount.setEmpty()
            tagValueList.push(("warn-total-record-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper"), valWarnTotalRecordCount)
        
        if self.hasPeriodicWorkRecordCount():
            valPeriodicWorkRecordCount = Value()
            if self.periodicWorkRecordCount is not None:
                valPeriodicWorkRecordCount.setInt64(self.periodicWorkRecordCount)
            else:
                valPeriodicWorkRecordCount.setEmpty()
            tagValueList.push(("periodic-work-record-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper"), valPeriodicWorkRecordCount)
        
        if self.hasAggregationPeriod():
            valAggregationPeriod = Value()
            if self.aggregationPeriod is not None:
                valAggregationPeriod.setInt64(self.aggregationPeriod)
            else:
                valAggregationPeriod.setEmpty()
            tagValueList.push(("aggregation-period", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper"), valAggregationPeriod)
        
        if self.hasMaxTotalRecordCount():
            valMaxTotalRecordCount = Value()
            if self.maxTotalRecordCount is not None:
                valMaxTotalRecordCount.setInt64(self.maxTotalRecordCount)
            else:
                valMaxTotalRecordCount.setEmpty()
            tagValueList.push(("max-total-record-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper"), valMaxTotalRecordCount)
        
        if self.hasPeriodicWorkInterval():
            valPeriodicWorkInterval = Value()
            if self.periodicWorkInterval is not None:
                valPeriodicWorkInterval.setInt64(self.periodicWorkInterval)
            else:
                valPeriodicWorkInterval.setEmpty()
            tagValueList.push(("periodic-work-interval", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper"), valPeriodicWorkInterval)
        
        if self.hasWarnSessionIdCount():
            valWarnSessionIdCount = Value()
            if self.warnSessionIdCount is not None:
                valWarnSessionIdCount.setInt64(self.warnSessionIdCount)
            else:
                valWarnSessionIdCount.setEmpty()
            tagValueList.push(("warn-session-id-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper"), valWarnSessionIdCount)
        
        if self.hasInstance():
            valInstance = Value()
            if self.instance is not None:
                valInstance.setString(self.instance)
            else:
                valInstance.setEmpty()
            tagValueList.push(("instance", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper"), valInstance)
        
        if self.hasMaxSessionIdCount():
            valMaxSessionIdCount = Value()
            if self.maxSessionIdCount is not None:
                valMaxSessionIdCount.setInt64(self.maxSessionIdCount)
            else:
                valMaxSessionIdCount.setEmpty()
            tagValueList.push(("max-session-id-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper"), valMaxSessionIdCount)
        
        if self.hasRotateFileInterval():
            valRotateFileInterval = Value()
            if self.rotateFileInterval is not None:
                valRotateFileInterval.setInt64(self.rotateFileInterval)
            else:
                valRotateFileInterval.setEmpty()
            tagValueList.push(("rotate-file-interval", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper"), valRotateFileInterval)
        
        if self.hasRecordWriteInterval():
            valRecordWriteInterval = Value()
            if self.recordWriteInterval is not None:
                valRecordWriteInterval.setInt64(self.recordWriteInterval)
            else:
                valRecordWriteInterval.setEmpty()
            tagValueList.push(("record-write-interval", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper"), valRecordWriteInterval)
        
        if self.hasArchive():
            valArchive = Value()
            if self.archive is not None:
                valArchive.setBool(self.archive)
            else:
                valArchive.setEmpty()
            tagValueList.push(("archive", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper"), valArchive)
        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isWarnTotalRecordCountRequested():
            valWarnTotalRecordCount = Value()
            valWarnTotalRecordCount.setEmpty()
            tagValueList.push(("warn-total-record-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper"), valWarnTotalRecordCount)
        
        if self.isPeriodicWorkRecordCountRequested():
            valPeriodicWorkRecordCount = Value()
            valPeriodicWorkRecordCount.setEmpty()
            tagValueList.push(("periodic-work-record-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper"), valPeriodicWorkRecordCount)
        
        if self.isAggregationPeriodRequested():
            valAggregationPeriod = Value()
            valAggregationPeriod.setEmpty()
            tagValueList.push(("aggregation-period", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper"), valAggregationPeriod)
        
        if self.isMaxTotalRecordCountRequested():
            valMaxTotalRecordCount = Value()
            valMaxTotalRecordCount.setEmpty()
            tagValueList.push(("max-total-record-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper"), valMaxTotalRecordCount)
        
        if self.isPeriodicWorkIntervalRequested():
            valPeriodicWorkInterval = Value()
            valPeriodicWorkInterval.setEmpty()
            tagValueList.push(("periodic-work-interval", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper"), valPeriodicWorkInterval)
        
        if self.isWarnSessionIdCountRequested():
            valWarnSessionIdCount = Value()
            valWarnSessionIdCount.setEmpty()
            tagValueList.push(("warn-session-id-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper"), valWarnSessionIdCount)
        
        if self.isInstanceRequested():
            valInstance = Value()
            valInstance.setEmpty()
            tagValueList.push(("instance", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper"), valInstance)
        
        if self.isMaxSessionIdCountRequested():
            valMaxSessionIdCount = Value()
            valMaxSessionIdCount.setEmpty()
            tagValueList.push(("max-session-id-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper"), valMaxSessionIdCount)
        
        if self.isRotateFileIntervalRequested():
            valRotateFileInterval = Value()
            valRotateFileInterval.setEmpty()
            tagValueList.push(("rotate-file-interval", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper"), valRotateFileInterval)
        
        if self.isRecordWriteIntervalRequested():
            valRecordWriteInterval = Value()
            valRecordWriteInterval.setEmpty()
            tagValueList.push(("record-write-interval", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper"), valRecordWriteInterval)
        
        if self.isArchiveRequested():
            valArchive = Value()
            valArchive.setEmpty()
            tagValueList.push(("archive", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper"), valArchive)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isWarnTotalRecordCountRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "warn-total-record-count") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-warntotalrecordcount').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "warnTotalRecordCount", "warn-total-record-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-warn-total-record-count-bad-value').infoFunc(): logFunc('warnTotalRecordCount not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setWarnTotalRecordCount(tempVar)
            for logFunc in self._log('read-tag-values-warn-total-record-count').debug3Func(): logFunc('read warnTotalRecordCount. warnTotalRecordCount=%s, tempValue=%s', self.warnTotalRecordCount, tempValue.getType())
        
        if self.isPeriodicWorkRecordCountRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "periodic-work-record-count") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-periodicworkrecordcount').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "periodicWorkRecordCount", "periodic-work-record-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-periodic-work-record-count-bad-value').infoFunc(): logFunc('periodicWorkRecordCount not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPeriodicWorkRecordCount(tempVar)
            for logFunc in self._log('read-tag-values-periodic-work-record-count').debug3Func(): logFunc('read periodicWorkRecordCount. periodicWorkRecordCount=%s, tempValue=%s', self.periodicWorkRecordCount, tempValue.getType())
        
        if self.isAggregationPeriodRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "aggregation-period") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-aggregationperiod').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "aggregationPeriod", "aggregation-period", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-aggregation-period-bad-value').infoFunc(): logFunc('aggregationPeriod not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setAggregationPeriod(tempVar)
            for logFunc in self._log('read-tag-values-aggregation-period').debug3Func(): logFunc('read aggregationPeriod. aggregationPeriod=%s, tempValue=%s', self.aggregationPeriod, tempValue.getType())
        
        if self.isMaxTotalRecordCountRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "max-total-record-count") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-maxtotalrecordcount').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "maxTotalRecordCount", "max-total-record-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-max-total-record-count-bad-value').infoFunc(): logFunc('maxTotalRecordCount not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMaxTotalRecordCount(tempVar)
            for logFunc in self._log('read-tag-values-max-total-record-count').debug3Func(): logFunc('read maxTotalRecordCount. maxTotalRecordCount=%s, tempValue=%s', self.maxTotalRecordCount, tempValue.getType())
        
        if self.isPeriodicWorkIntervalRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "periodic-work-interval") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-periodicworkinterval').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "periodicWorkInterval", "periodic-work-interval", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-periodic-work-interval-bad-value').infoFunc(): logFunc('periodicWorkInterval not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPeriodicWorkInterval(tempVar)
            for logFunc in self._log('read-tag-values-periodic-work-interval').debug3Func(): logFunc('read periodicWorkInterval. periodicWorkInterval=%s, tempValue=%s', self.periodicWorkInterval, tempValue.getType())
        
        if self.isWarnSessionIdCountRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "warn-session-id-count") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-warnsessionidcount').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "warnSessionIdCount", "warn-session-id-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-warn-session-id-count-bad-value').infoFunc(): logFunc('warnSessionIdCount not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setWarnSessionIdCount(tempVar)
            for logFunc in self._log('read-tag-values-warn-session-id-count').debug3Func(): logFunc('read warnSessionIdCount. warnSessionIdCount=%s, tempValue=%s', self.warnSessionIdCount, tempValue.getType())
        
        if self.isInstanceRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "instance") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-instance').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "instance", "instance", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-instance-bad-value').infoFunc(): logFunc('instance not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setInstance(tempVar)
            for logFunc in self._log('read-tag-values-instance').debug3Func(): logFunc('read instance. instance=%s, tempValue=%s', self.instance, tempValue.getType())
        
        if self.isMaxSessionIdCountRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "max-session-id-count") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-maxsessionidcount').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "maxSessionIdCount", "max-session-id-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-max-session-id-count-bad-value').infoFunc(): logFunc('maxSessionIdCount not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMaxSessionIdCount(tempVar)
            for logFunc in self._log('read-tag-values-max-session-id-count').debug3Func(): logFunc('read maxSessionIdCount. maxSessionIdCount=%s, tempValue=%s', self.maxSessionIdCount, tempValue.getType())
        
        if self.isRotateFileIntervalRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "rotate-file-interval") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-rotatefileinterval').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "rotateFileInterval", "rotate-file-interval", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-rotate-file-interval-bad-value').infoFunc(): logFunc('rotateFileInterval not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setRotateFileInterval(tempVar)
            for logFunc in self._log('read-tag-values-rotate-file-interval').debug3Func(): logFunc('read rotateFileInterval. rotateFileInterval=%s, tempValue=%s', self.rotateFileInterval, tempValue.getType())
        
        if self.isRecordWriteIntervalRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "record-write-interval") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-recordwriteinterval').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "recordWriteInterval", "record-write-interval", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-record-write-interval-bad-value').infoFunc(): logFunc('recordWriteInterval not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setRecordWriteInterval(tempVar)
            for logFunc in self._log('read-tag-values-record-write-interval').debug3Func(): logFunc('read recordWriteInterval. recordWriteInterval=%s, tempValue=%s', self.recordWriteInterval, tempValue.getType())
        
        if self.isArchiveRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "archive") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-archive').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "archive", "archive", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-archive-bad-value').infoFunc(): logFunc('archive not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setArchive(tempVar)
            for logFunc in self._log('read-tag-values-archive').debug3Func(): logFunc('read archive. archive=%s, tempValue=%s', self.archive, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "instances", 
        "namespace": "instances", 
        "className": "InstancesMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_pre_topper.tech.content.pre_topper.instances.instances_maapi_gen import InstancesMaapi", 
        "baseClassName": "InstancesMaapiBase", 
        "baseModule": "instances_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qtc-pt", 
            "yangName": "pre-topper", 
            "namespace": "pre_topper", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "name": "pre-topper"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-pt", 
            "isCurrent": true, 
            "yangName": "instances", 
            "namespace": "instances", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "keyLeaf": {
                "varName": "instances", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "instances"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "warnTotalRecordCount", 
            "yangName": "warn-total-record-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "periodicWorkRecordCount", 
            "yangName": "periodic-work-record-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "aggregationPeriod", 
            "yangName": "aggregation-period", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxTotalRecordCount", 
            "yangName": "max-total-record-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "periodicWorkInterval", 
            "yangName": "periodic-work-interval", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "warnSessionIdCount", 
            "yangName": "warn-session-id-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "instance", 
            "yangName": "instance", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxSessionIdCount", 
            "yangName": "max-session-id-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rotateFileInterval", 
            "yangName": "rotate-file-interval", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "recordWriteInterval", 
            "yangName": "record-write-interval", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "archive", 
            "yangName": "archive", 
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
            "qwilt_tech_content_pre_topper"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "warnTotalRecordCount", 
            "yangName": "warn-total-record-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "periodicWorkRecordCount", 
            "yangName": "periodic-work-record-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "aggregationPeriod", 
            "yangName": "aggregation-period", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxTotalRecordCount", 
            "yangName": "max-total-record-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "periodicWorkInterval", 
            "yangName": "periodic-work-interval", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "warnSessionIdCount", 
            "yangName": "warn-session-id-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "instance", 
            "yangName": "instance", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxSessionIdCount", 
            "yangName": "max-session-id-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rotateFileInterval", 
            "yangName": "rotate-file-interval", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "recordWriteInterval", 
            "yangName": "record-write-interval", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "archive", 
            "yangName": "archive", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


