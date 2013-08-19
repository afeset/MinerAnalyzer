#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: hagaia
# 

import Queue
import os
import time
import datetime

import a.infra.process

import nginx_manager
import nginx_status
import nginx_command 
import reporter
import config_agent
import resource_manager
import delivery_conf
import delivery_volume
import utils

if  __package__ is None:
    G_NAME_MODULE_DELIVERY = "unknown"
    G_NAME_GROUP_DELIVERY_DELIVERY_MNG = "unknown"
else:
    from . import G_NAME_MODULE_DELIVERY 
    from . import G_NAME_GROUP_DELIVERY_DELIVERY_MNG


#---------------------------------------------------------
class DeliveryManager(object):
    
    def __init__ (self, name, logger, blinkyAgent):
        self.__name = name        
        self.__log = logger.createLogger(G_NAME_MODULE_DELIVERY, G_NAME_GROUP_DELIVERY_DELIVERY_MNG)        
        self.__nginxManager    = nginx_manager.NginxManager("nginx-manager",logger)
        self.__ngxStatus       = nginx_status.NginxStatus("nginx-status",logger)
        self.__ngxCmd          = nginx_command.NginxCommand("nginx-cmd",logger)        
        self.__reporter        = reporter.Reporter("delivery-reporter",logger)
        self.__resourceManager = resource_manager.ResourceManager("resource-manager",logger)
        self.__isStop = False
        self.__conf   = None
        self.__blinkyAgent = blinkyAgent

        self.__confQueue = Queue.Queue()
        self.__configAgent = config_agent.ConfigAgent("config-agent",logger,blinkyAgent,self.__confQueue)
        self.__duringConfig = False

        self.__timeService = utils.TimesSerivce()
        self.__ipTablesClient = delivery_volume.IpTablesClient(logger)
    
    #-------------------------------------------------------------------------------------------------
    def init (self, conf):

        self.__log("init-delivery-manager-mark1").info("-------------------------------------------------------------------------------------")
        self.__log("init-delivery-manager").notice("Init Delivery Manager")
        self.__log("init-delivery-manager-mark2").info("-------------------------------------------------------------------------------------")
        self.__conf = conf        
        
        self.__conf.validateConfiguration(self.__log)

        self.__ipTablesClient.init(conf)

        self.__ngxCmd.init(conf)

        self.__resourceManager.init(conf,self.__ngxStatus)

        if not self.__nginxManager.init(conf,self.__ngxCmd,self.__ngxStatus):
            return False

        if not self.__reporter.init(conf,self.__ngxCmd,self.__ngxStatus):
            return False

        return True


    #-------------------------------------------------------------------------------------------------
    def start (self):

        if not self.__conf.isWebServerAdminUp:
            self.__log("start-nginx-down").notice("Nginx start at Down state No IPs, No Device and Interface Down")
        
        # start
        #---------------------------------------------------
        if not self.__start():        
            return False      
            
        self.__log("finish-start").notice("Delivery Manager Finish Start Stage waiting for Configuration")

        return True

    #-------------------------------------------------------------------------------------------------
    def run (self):
                        
        # Main Loop
        #---------------------------------------------------
        retVal = self.__mainLoop()

        self.__log("exit-main-loop").notice("Delivery Manager Exit from Main Loop")
            
        # end
        #---------------------------------------------------
        self.__end()

        return retVal

    
    #-------------------------------------------------------------------------------------------------
    def stop (self):

        self.__isStop = True
        
        
    #private     
    #-------------------------------------------------------------------------------------------------
    def __start (self):

        self.__log("start-delivery-manager-mark1").info("-------------------------------------------------------------------------------------")
        self.__log("start-delivery-manager").notice("Start Delivery Manager")
        self.__log("start-delivery-manager-mark2").info("-------------------------------------------------------------------------------------")
    
        if not self.__nginxManager.start():
            return False

        if self.__isStop:
            return False

        # Start config agent that Delivery Manager is use to recieve configuration
        # only after Net Manager Process is Up         
        if self.__configAgent.start(self.__conf.netSignalFileName) is False:
            self.__log("net-mng-max-time").error("Failed to Start Config Agent - Net Manager is Down")
            return False


        # success in starting config agant
        # start reporter
        if not self.__reporter.start():
            self.__log("start-reporter-err").error("Failed to start Delivery Manager Reporter")
            self.__configAgent.end()
            return False
                  
        # success in init of Config Agant and Reporter              
        return True

    #-------------------------------------------------------------------------------------------------
    def __mainLoop (self):

        retVal = True
        newItem = None
        newConf = False
        self.__timeService.init()

        self.__log("run-delivery-manager-mark1").info("-------------------------------------------------------------------------------------")
        self.__log("run-delivery-manager").info("Delivery Manager - Main Loop")
        self.__log("run-delivery-manager-mark2").info("-------------------------------------------------------------------------------------")

        while 1 :

            if self.__ngxStatus.isOperInProgress() is False and self.__isStop:
                self.__log("stop-cmd").notice("Delivery Manager received stop command")
                break 
                    
            retVal = self.__oneTick()

            if not retVal:
                self.__log("nginx-down-exit").notice("Nginx is Down - Exit Delivery Manager")
                break

            # Calculate time to sleep
            sleepTimeoutSec = self.__timeService.sleepTimeFromInitSec(self.__log, self.__conf.kConf.kMainLoopSleepTimeSec)
 
            # Nginx Manager is during operation
            # Do not take new configuration or Oscar Update
            #================================================
            if self.__ngxStatus.isOperInProgress() is True:
                self.__log("config-sleep").debug5("Oper In Progress - Delivery Manager sleeps for %.4f secs", sleepTimeoutSec)
                time.sleep(sleepTimeoutSec)
                self.__timeService.init()
                continue
            # During new configuration handling
            #================================================
            elif (newConf is True):
                self.__log("config-sleep").debug5("During New Configuration - Delivery Manager sleeps for %.4f secs", sleepTimeoutSec)
                time.sleep(sleepTimeoutSec)
            #================================================
            else:
                try:
                    self.__log("config-queue-get").debug5("Delivery Manager gets new item from configuration queue (timeout= %.4f secs)", sleepTimeoutSec)
                    newItem = self.__confQueue.get(block=True,timeout=sleepTimeoutSec)
                    newConf = True                
                except Queue.Empty:
                    newConf = False
                          
            # start 'one tick' actual duration timing from here
            # not taking into account sleep time
            self.__timeService.init()

            # Handle new configuration
            if newConf is True:
                shouldConfigure = self.__shouldConfigure(newItem)

                if shouldConfigure is True:
                    self.__configure(newItem)                   
                    newItem = None
                    newConf = False

            # Handle configuration update if exists and
            # not during configuration procedure
            elif self.__duringConfig is False:
                (retVal,newDictConfig) = self.__getConfigUpdateIfExist()
                if retVal is True:
                    self.__updateConfigIfNeeded(newDictConfig)
        
        return retVal

    #-------------------------------------------------------------------------------------------------
    def __oneTick (self):

        if not self.__nginxManager.oneTick():            
            return False
               
        self.__reporter.oneTick()        

        return True

    #-------------------------------------------------------------------------------------------------
    def __shouldConfigure (self, dynamicConf):

        # Pre Net
        #------------------
        if dynamicConf.isPreNet is True:
            # do nothing
            pass

        # Post Net 
        #------------------
        else:

            # delay reconfig for stability (Post Net only)
            timeNow = time.time()
            timeLimit = dynamicConf.timeToConfigure

            if (timeNow  < timeLimit):
                self.__log("pre-delay-reconfig").debug4("Delivery Manager needs to delay the new configuration by %.3f seconds more", 
                                                        (timeLimit - timeNow))
                return False
            else:
                self.__log("post-delay-reconfig").debug1("Delivery Manager passed the delay of new configuration by %.3f seconds", 
                                                         (timeNow - timeLimit))

        return True

    #-------------------------------------------------------------------------------------------------
    def __configure (self, dynamicConf):
       
        self.__log("receive-new-config").notice("Delivery Manager recieved new Configration - PreNet = %s", str(dynamicConf.isPreNet))
        
        if len(dynamicConf.iconfList) > 2:
            a.infra.process.processFatal("Delivery Manager does not support more than 2 Interfaces")
            return
        
        # 1st config transaction - create interfaces
        if len(self.__conf.InterfaceMap) == 0:        
            for newConf in dynamicConf.iconfList:
                currentConf = delivery_conf.InterfaceConf(newConf.name)
                self.__conf.InterfaceMap[newConf.name] = currentConf
                self.__log("detect-new-interface").info("%s: Delivery Manager detected a new interface", newConf.name)

        
        # Pre Net
        #------------------
        # Cofiguration is not changed during pre net.
        # Nginx may go down
        if dynamicConf.isPreNet is True:

            self.__duringConfig = True

            oldWebServerState = self.__conf.isWebServerAdminUp
            interfaceMapClone = {}
            shouldStayUp = False

            # interfaces that are going to be changed
            for newConf in dynamicConf.iconfList:
                currentConf = self.__conf.InterfaceMap[newConf.name]
                self.__configInterfacePreNet(currentConf, newConf)
                interfaceMapClone[newConf.name] = newConf

            # loop over all interfaces
            for interface in self.__conf.InterfaceMap:
                currentConf = self.__conf.InterfaceMap[interface]
                
                if currentConf.isUp():
                    newConf = interfaceMapClone.get(interface, currentConf)

                    # interface state is up, will be up and at least one ip address remains unchanged
                    if newConf.isUp() and (
                        (currentConf.ipv4Address and currentConf.ipv4Address == newConf.ipv4Address) or 
                        (currentConf.ipv6Address and currentConf.ipv6Address == newConf.ipv6Address)):
                        shouldStayUp = True
                        break

            self.__conf.isWebServerAdminUp = shouldStayUp

            # Nginx State should change from up to down
            if oldWebServerState and not self.__conf.isWebServerAdminUp:
                self.__log("nginx-config-state").notice("Pre Net - Configuration changed Set Admin Down State - Stop Nginx")
                self.__nginxManager.stop()


        # Post Net 
        #------------------
        else:

            self.__duringConfig = False
            
            # interfaces that were changed
            for newConf in dynamicConf.iconfList:
                currentConf = self.__conf.InterfaceMap[newConf.name]
                self.__configInterfacePostNet(currentConf, newConf)

            # loop over all interfaces
            for interface in self.__conf.InterfaceMap:
                currentConf = self.__conf.InterfaceMap[interface]
                if currentConf.isUp():

                    if self.__conf.isWebServerAdminUp is True:
                        # at least one of the IPs was changed and nginx is still up
                        self.__log("postnet-config-state-reload").info("Post Net - Set Nginx to Reload Configuration State")
                        self.__ngxStatus.shouldReloadConfig = True
                    else:
                        self.__log("postnet-config-state-up").info("Post Net - Set Nginx to Admin Up State")
    
                    self.__conf.isWebServerAdminUp = True

                    # we are done (at least one interface is up and configured)
                    break

            # update ip tables after first transaction
            if self.__conf.configId == 0:
                self.__ipTablesClient.start()

            # config has changed
            self.__conf.configId+= 1
            self.__configUpdated()
            
    #-------------------------------------------------------------------------------------------------
    def __configInterfacePreNet (self, currentConf, newConf):

        name = newConf.name
        self.__log("receive-new-config-interface-pre").info("%s: Pre Net - Delivery Manager recieved new Interface Configration", name)
        self.__log("receive-new-config-interface-details-pre").debug1("%s: Pre Net - new Interface Configration - %s", name, newConf)
        self.__log("receive-curr-config-interface-details-pre").debug2("%s: Pre Net - current Interface Configration - %s", name, currentConf)

        if currentConf is None:
             a.infra.process.processFatal("%s: Pre Net - Interface does not exist",name)

        # interface configuration is going to be changed
        
        # Ipv4 is going to be changed
        if newConf.ipv4Address != None and newConf.ipv4Address != currentConf.ipv4Address:
            self.__log("prenet-config-ipv4").info("%s: Pre Net - Change Delivery Interface IPv4 Address - %s",name,newConf.ipv4Address)
        else:
            newConf.ipv4Address = currentConf.ipv4Address 

        # Ipv6 is going to be changed
        if newConf.ipv6Address != None and newConf.ipv6Address != currentConf.ipv6Address:
            self.__log("prenet-config-ipv6").info("%s: Pre Net - Change Delivery Interface IPv6 Address - %s",name,newConf.ipv6Address)
        else:
            newConf.ipv6Address = currentConf.ipv6Address 

        # Interface egress is going to be changed
        if newConf.egressInterface != None and newConf.egressInterface != currentConf.egressInterface:
            self.__log("prenet-config-device").info("%s: Pre Net - Change Delivery Interface Device - %s",name,newConf.egressInterface)
        else:
            newConf.egressInterface = currentConf.egressInterface
        
        # Interface Admin is going to be changed
        if newConf.deliveryInterAdmin != None and newConf.deliveryInterAdmin != currentConf.deliveryInterAdmin:
            self.__log("prenet-config-enable").info("%s: Pre Net - Change Delivery Interface Admin - %s",name,newConf.deliveryInterAdmin)
        else:
            newConf.deliveryInterAdmin = currentConf.deliveryInterAdmin

    #-------------------------------------------------------------------------------------------------
    def __configInterfacePostNet (self, currentConf, newConf):

        name = newConf.name
        self.__log("receive-new-config-interface-post").info("%s: Post Net - Delivery Manager recieved new Interface Configration", name)
        self.__log("receive-new-config-interface-details-post").debug1("%s: Post Net - new Interface Configration - %s", name, newConf)
        self.__log("receive-curr-config-interface-details-post").debug2("%s: Post Net - current Interface Configration - %s", name, currentConf)

        if currentConf is None:
            a.infra.process.processFatal("%s: Post Net - Interface does not exist",name)

        if newConf.ipv4Address != None and newConf.ipv4Address != currentConf.ipv4Address:
            self.__log("postnet-config-ipv4").info("%s: Post Net - Change Delivery Interface IPv4 Address - %s",name,newConf.ipv4Address)
            currentConf.ipv4Address = newConf.ipv4Address

        if newConf.ipv6Address != None and newConf.ipv6Address != currentConf.ipv6Address:
            self.__log("postnet-config-ipv6").info("%s: Post Net - Change Delivery Interface IPv6 Address - %s",name,newConf.ipv6Address)
            currentConf.ipv6Address = newConf.ipv6Address

        if newConf.egressInterface != None and newConf.egressInterface != currentConf.egressInterface:
            self.__log("postnet-config-device").info("%s: Post Net - Change Delivery Interface Device - %s",name,newConf.egressInterface)
            currentConf.egressInterface = newConf.egressInterface

        if newConf.deliveryInterAdmin != None and newConf.deliveryInterAdmin != currentConf.deliveryInterAdmin:
            self.__log("postnet-config-enable").info("%s: Post Net - Change Delivery Interface Admin - %s",name,newConf.deliveryInterAdmin)
            currentConf.deliveryInterAdmin = newConf.deliveryInterAdmin

#-------------------------------------------------------------------------------------------------
    def __getConfigUpdateIfExist (self):

        """ 
            Chech for existance of new configuration
            Return pair of (isExist,NewConf) 
        """

        ok = True

        filename = os.path.join(self.__conf.sysRunDir, self.__conf.kOscarUpdateConfigFileName)

        if not os.path.exists(filename):
            return (False,None)

        try:
            tempFilename = filename + ".tmp." + datetime.datetime.now().strftime("%Y%m%d-%H%M%S-%f")
            os.rename(filename, tempFilename)
            newDictConfig = a.infra.format.json.readFromFile(self.__log, tempFilename)

        except (IOError, ValueError) as ex:
            self.__log("error-load-cfg").error("Error in loading configuration file %s. %s", tempFilename, ex)
            ok = False

        try:
            os.remove(tempFilename)
        except Exception as ex:
            self.__log("error-remove-cfg").error("Error in remove configuration file %s. %s", tempFilename, ex)

        if not ok:
            return (False,None)

        self.__log("update-cfg").notice("Updating configuration from file %s", filename)
    
        return (True,newDictConfig)


    #-------------------------------------------------------------------------------------------------
    def __updateConfigIfNeeded(self, newDictConfig):

        configChange = self.__conf.updateUserParamConfigIfChanged(newDictConfig,self.__log)

        # No new configuration
        if configChange == self.__conf.kNoConfigLevel:
            self.__log("no-change").notice("Service Oscar Update: Delivery Configuration not changed")
            return

        if configChange == self.__conf.kGeneralConfigLevel:
            self.__log("general-change").notice("Service Oscar Update: Delivery Configuration changed, Nginx Restrart is not needed")

        elif configChange == self.__conf.kNginxConfigLevel:
            self.__log("nginx-change").notice("Service Oscar Update: Delivery Configuration changed, Restrat Nginx if in Up State")  
            self.__ngxStatus.updateConfigCounter = (self.__ngxStatus.updateConfigCounter + 1)
            self.__nginxManager.stop()

        # update others about config changes
        self.__configUpdated()
        return

    #-------------------------------------------------------------------------------------------------
    def __configUpdated (self):
        self.__resourceManager.updateConf(self.__conf)

    #-------------------------------------------------------------------------------------------------
    def __end (self):

        self.__log("end-delivery-manager-mark1").info("-------------------------------------------------------------------------------------")
        self.__log("end-delivery-manager").notice("End Delivery Manager")
        self.__log("end-delivery-manager-mark2").info("-------------------------------------------------------------------------------------")

        self.__resourceManager.end()
    
        self.__nginxManager.end()        

        self.__configAgent.end()

        self.__reporter.end()

        self.__ipTablesClient.end()

        self.__log("exit-delivery-manager").notice("Delivery Manager Stopped and Exit")

    #-------------------------------------------------------------------------------------------------
    def isNginxUp (self):
        return self.__nginxManager.isAlive()

    # UT Functions
    #-------------------------------------------------------------------------------------------------
    def getConfigAgentUT (self):
        return self.__configAgent

    #-----------------------------------
    def getUpdateConfigCounterUT (self):
        return self.__ngxStatus.updateConfigCounter

    #-----------------------------------
    def setRestartNginxFlagUT (self):
        self.__ngxStatus.startNginxRestart()

    


    
