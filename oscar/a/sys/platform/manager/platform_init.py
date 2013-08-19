# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities 
# without explicit written permission from Qwilt.
# 
# Author: shmulika
#

#TODO(shmulika): this is a temporary file, we need to decide with Gaash where all this code goes to

import a.infra.process
import a.sys.blinky.domain_priority
import a.sys.platform.manager.manager
import a.sys.platform.manager.dell.fans
import a.sys.platform.manager.dell.power
import a.sys.platform.manager.dell.power_source
import a.sys.platform.manager.dell.fans_source
import a.sys.platform.manager.dell.fru_source
import a.sys.platform.manager.blinky.manager_blinky_adaptor
import a.sys.platform.manager.blinky.fans_blinky_adaptor
import a.sys.platform.manager.blinky.power_blinky_adaptor
import a.sys.platform.manager.blinky.source_blinky_adaptor

# Bypass for PyChecker
if  __package__ is None:
    G_MODULE_NAME_PLATFORM_MANAGER            = "unknown"
    G_GROUP_NAME_PLATFORM_INITIALIZER         = "unknown"
else:
    from . import G_MODULE_NAME_PLATFORM_MANAGER                  
    from . import G_GROUP_NAME_PLATFORM_INITIALIZER        


class PlatformInitializer:
    #TODO(shmulika): this is temporary for right now    

    def __init__ (self, logger):
        self._log = logger.createLogger(G_MODULE_NAME_PLATFORM_MANAGER, G_GROUP_NAME_PLATFORM_INITIALIZER)
        self._platformType = None
        self._platformSpecificInitializer = None

        # logical elements
        self._platformManager = None
        self._platformFans    = None
        self._platformPower   = None

        self._platformFanUnits = {}
        self._platformPowerSupplyUnits = {}

        # blinky/configuration      
        self._configDomain = None
        self._operDomain   = None
        self._maapiDomain  = None

        self._platformManagerBlinkyAdaptor = None
        self._platformFansBlinkyAdaptor    = None
        self._platformPowerBlinkyAdaptor   = None


    def initPlatformManagedComponenets (self):        
        self._log("init-platform").debug1("initializing platform")    
        self._platformManager = a.sys.platform.manager.manager.PlatformManager(self._log)        

        self._powerReporter = a.sys.platform.manager.dell.power_source.PowerSource(self._log)
        self._fansReporter  = a.sys.platform.manager.dell.fans_source.FansSource(self._log)
        self._fruReporter   = a.sys.platform.manager.dell.fru_source.FruSource(self._log)
        
        self._platformManager.addReporter(self._powerReporter)
        self._platformManager.addReporter(self._fansReporter)
        self._platformManager.addReporter(self._fruReporter)

        self._platformFans = a.sys.platform.manager.dell.fans.FansSubsystem(self._log)
        self._platformFans.initFansReporter(self._fansReporter)

        self._platformPower = a.sys.platform.manager.dell.power.PowerSuppliesSubsystem(self._log)
        self._platformPower.initPowerSuppliesReporter(self._powerReporter)
        self._platformPower.initFruReporter(self._fruReporter)        

        self._platformManager.addManagedElement(self._platformFans)
        self._platformManager.addManagedElement(self._platformPower)


    def initBlinkyAgent (self, blinkyAgent):
        self._createDomains(blinkyAgent)        
        self._platformManagerBlinkyAdaptor = a.sys.platform.manager.blinky.manager_blinky_adaptor.ManagerBlinkyAdaptor(self._log, self, self._configDomain, self._operDomain, self._maapiDomain)
        self._platformFansBlinkyAdaptor    = a.sys.platform.manager.blinky.fans_blinky_adaptor.FansBlinkyAdaptor(self._log, self, self._configDomain, self._operDomain, self._maapiDomain)
        self._platformPowerBlinkyAdaptor   = a.sys.platform.manager.blinky.power_blinky_adaptor.PowerBlinkyAdaptor(self._log, self, self._configDomain, self._operDomain, self._maapiDomain)
        self._platformSourceBlinkyAdaptor  = a.sys.platform.manager.blinky.source_blinky_adaptor.SourceBlinkyAdaptor(self._log, self, self._configDomain, self._operDomain, self._maapiDomain)

        self._platformManagerBlinkyAdaptor.createAndAttachBlinkyPlatform(self._platformManager)
        self._platformFansBlinkyAdaptor.createAndAttachBlinkyFans(self._platformFans)
        self._platformPowerBlinkyAdaptor.createAndAttachBlinkyPower(self._platformPower)

        self._platformSourceBlinkyAdaptor.createAndAttachBlinkySourceList()
        self._platformSourceBlinkyAdaptor.createAndAttachBlinkySource(self._powerReporter, "power")
        self._platformSourceBlinkyAdaptor.createAndAttachBlinkySource(self._fansReporter , "fans")
        self._platformSourceBlinkyAdaptor.createAndAttachBlinkySource(self._fruReporter  , "fru")

        self._registerDone()


    def _createDomains (self, blinkyAgent):
        self._log("create-domains").debug1("creating domains in blinkyAgent=%s", blinkyAgent)    
        priority=a.sys.blinky.domain_priority.DomainPriority.kDefault
        self._configDomain = blinkyAgent.createConfigDomain("config-platform", priority)
        self._operDomain   = blinkyAgent.createConfigDomain("oper-platform", priority)
        self._maapiDomain  = blinkyAgent.createMaapiDomain("maapi-platform")



    def _registerDone (self):
        self._log("register-done").debug1("finishing registration and triggering subscriptions.")    
        self._operDomain.registrationDone() # TODO(shmulika): naamas might change this interface later for the oper-domain.        
        self._configDomain.registrationDone()
        self._configDomain.triggerSubscriptions()


#################################################################
# GETTERS
#################################################################

    def getPlatformManager (self):
        return self._platformManager

    def getPowerSubsystem (self):
        return self._platformPower

    def getFansSubsystem (self):
        return self._platformFans


## TODO(shmulika): this might be used when we have different platform types
##################################################################
## PLATFORM SPECIFIC CLASSES
##################################################################
#
#    def initPlatformType (self, platformType = "Dell"):
#        self._log("init-platform").debug1("initializing platform of type = %s", platformType)    
#        self._determineSpecificPlatform(platformType)
#
# 
#    def initPlatformManagedComponenets (self):        
#        for reporter in self._platformSpecificInitializer.initReporters():
#            self._platformManager.addReporter(reporter)
#
#        self._platformFans    = self._platformSpecificInitializer.initFansSubsystem()
#        self._platformPower   = self._platformSpecificInitializer.initPowerSubsystem()
#
#        self._platformManager.addManagedElement(self._platformFans)
#        self._platformManager.addManagedElement(self._platformPower)
#
#
#
#    def _determineSpecificPlatform (self, platformType):
#        self._log("determine-specific-platform").debug2("determening platform type according to given type = %s", platformType)    
#        
#        if self._platformType == "Dell":
#            self._log("determine-specific-platform").debug1("determined platform is Dell")    
#            self._setSpecificPlatform(platformType, DellSpecificInitializer(self._log))            
#        else:
#            self._log("init-platform-unsupported-platfrom-type").error("unsupported platform type %s, cannot init", platformType)    
#            a.infra.process.processFatal("unsupported platform type %s, cannot init", platformType)
#                    
#
#    def _setSpecificPlatform (self, platformType, specificPlatformInitializer):
#        self._platformType = platformType
#        self._platformSpecificInitializer = specificPlatformInitializer
#
#
#class PlatformSpecificInitializer:
#    def __init__ (self, logger, name):
#        self._log = logger.createLoggerSameModule(G_GROUP_NAME_PLATFORM_INITIALIZER, instance = name)
#
#    def initReporters (self):
#        """ Creates, Inits all the reporters needed to manage the platform
#        Returns: the list of reporters (so could be added to platform manager)
#        """
#        return []
#
#    def initPowerSubsystem (self):
#        """ Creates and inits the power-supplies subsystem
#        Returns: the power-supplies subsystem
#        """
#        return None
#
#
#    def initFansSubsystem (self):
#        """ Creates and inits the fans subsystem
#        Returns: the fans subsystem
#        """
#        return None
#
#
#class DellSpecificInitializer(PlatformSpecificInitializer):
#    def __init__ (self, logger):
#        PlatformSpecificInitializer.__init__(self, logger, "dell-initializer")
#
#    def initReporters (self):
#        self._log("init-dell-platform").debug1("initializing reportes for Dell platform")    
#        self._powerReporter = a.sys.platform.manager.dell.power_source.PowerSource(self._log)
#        self._fansReporter  = a.sys.platform.manager.dell.fan_omreporter.FansSource(self._log)
#        self._fruReporter   = a.sys.platform.manager.dell.fru_source.FruSource(self._log)
#        return [self._powerReporter, self._fansReporter, self._fruReporter]
#
#    def initPowerSubsystem (self):
#        self._log("init-dell-power-sub-systems").debug1("initializing power sub-system for Dell platform")            
#        self._platformPower = a.sys.platform.manager.dell.power.PowerSuppliesSubsystem(self._log)
#        self._platformPower.initPowerSuppliesReporter(self._powerReporter)
#        self._platformPower.initFruReporter(self._fruReporter)        
#        return self._platformPower
#
#    def initFansSubsystem (self):
#        self._log("init-dell-fans-sub-systems").debug1("initializing fans sub-system for Dell platform")            
#        self._platformFans = a.sys.platform.manager.dell.fans.FansSubsystem(self._log)
#        self._platformFans.initFansReporter(self._fansReporter)
#        return self._platformFans

     
