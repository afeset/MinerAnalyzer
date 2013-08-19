#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: hagaia
# 

import os
import time

import delivery_conf
import a.sys.net.net_manager
from a.sys.net.interfaces import client as net_client
from a.sys.net.interfaces.ip import IpVersion

if  __package__ is None:
    G_NAME_MODULE_DELIVERY = "unknown"
    G_NAME_GROUP_DELIVERY_CONF_AGENT = "unknown"
else:
    from . import G_NAME_MODULE_DELIVERY 
    from . import G_NAME_GROUP_DELIVERY_CONF_AGENT

#-----------------------------------------------------------------
class ConfigAgent(object):

    #---------------------------------------------------------
    def __init__ (self, name, logger, blinkyAgent, queue):

        self.__name = name        
        self.__blinkyAgent = blinkyAgent
        self.__log = logger.createLogger(G_NAME_MODULE_DELIVERY, G_NAME_GROUP_DELIVERY_CONF_AGENT)

        if self.__blinkyAgent != None:    
            self.__netPreListener = a.sys.net.net_manager.NetPreListener("delivery-net-preconfig", 
                                                                         DeliveryNetCfgNotifier(self.preNet))  
            self.__netPostListener = a.sys.net.net_manager.NetPostListener("delivery-net-postconfig",
                                                                           DeliveryNetCfgNotifier(self.postNet))

        self.__confQueue = queue

        self.__startNetConfig = False

    #-------------------------------------------------------------------------------------------------
    def start (self, netManagerSignalFile):

        self.__netMngSignalFile = netManagerSignalFile

        # If Net Manager Signal File is configured and Valid
        # Activate Config Pre and Post Listeners
        if len(self.__netMngSignalFile):
            if not self.__isNetManagerUp():
                return False
                    
        if self.__blinkyAgent != None:
            self.__log("start-config-agent").info("Start Delivery Config Agent - Signal File - %s",self.__netMngSignalFile)  
            self.__netPreListener.activate(self.__log, self.__blinkyAgent)
            self.__netPostListener.activate(self.__log, self.__blinkyAgent)

        return True


    #-------------------------------------------------------------------------------------------------
    def end (self):

        if self.__blinkyAgent != None:
            self.__netPreListener.shutdown()
            self.__netPostListener.shutdown()
            self.__log("end-config-agent").info("End Delivery Config Agent")  

    #-------------------------------------------------------------------------------------------------
    # in case of ip change
    # set nginx down and than 
    # call only on change
    # always pre and post is called on any change
    def preNet (self, iConfList, deliveryStabilityDelay=0):
        __pychecker__="no-argsused"  # deliveryStabilityDelay not used

        dynamicConf = delivery_conf.DynamicDeliveryConf()
        dynamicConf.isPreNet = True
        dynamicConf.timeToConfigure = 0 # no delay

        for iConf in iConfList:
            ifChanged = self.hasInterfaceChanged(iConf, "Pre Net")
            if ifChanged is True:
                dynamicConf.iconfList.append(iConf)

        changed = (len(dynamicConf.iconfList)>0)

        if changed:
            self.__startNetConfig = True 
            self.__confQueue.put_nowait(dynamicConf)                
        else:
            self.__log("prenet-config-err").error("Pre Net called but no Configuration Change")

        return changed
            
    #-------------------------------------------------------------------------------------------------
    def postNet (self, iConfList, deliveryStabilityDelay=0):

        self.__log("config-post-net").info("Post Net - Config Agent recieved new Configration (delay=%s)", deliveryStabilityDelay)

        if not self.__startNetConfig:
            self.__log("postnet-no-prenet").error("Post Net called but Pre Net not called first")
            return False
        else:
            self.__startNetConfig = False

        dynamicConf = delivery_conf.DynamicDeliveryConf()
        dynamicConf.isPreNet = False
        dynamicConf.timeToConfigure = time.time() + deliveryStabilityDelay

        for iConf in iConfList:
            ifChanged = self.hasInterfaceChanged(iConf, "Post Net")
            if ifChanged is True:
                dynamicConf.iconfList.append(iConf)

        changed = (len(dynamicConf.iconfList)>0)

        if changed:
            self.__startNetConfig = False 
            self.__confQueue.put_nowait(dynamicConf)                
        else:
            self.__log("postnet-config-err").error("Post Net called but no Configuration Change")

        return changed

    #-------------------------------------------------------------------------------------------------
    def hasInterfaceChanged (self, iConf, actionName):

        # any data member that was changed has a value, otherwise None
        self.__log("config-agent-interface").debug1("%s - Config Agent recieved new Configration: %s", actionName, iConf)

        changed = False

        # IPv4 is going to be changed
        if iConf.ipv4Address != None:
            self.__log("config-ipv4").info("%s: %s - Change Delivery Interface IPv4 Address - %s", iConf.name, actionName, iConf.ipv4Address)                    
            changed = True

        # IPv6 is going to be changed
        if iConf.ipv6Address != None:
            self.__log("config-ipv6").info("%s: %s - Change Delivery Interface IPv6 Address - %s", iConf.name, actionName, iConf.ipv6Address)                    
            changed = True

        # Egress Device is going to be changed
        if iConf.egressInterface != None:
            self.__log("config-device").info("%s: %s - Change Delivery Device Egress Interface - %s", iConf.name, actionName, iConf.egressInterface)                    
            changed = True

        # Interface Admin change 
        if iConf.deliveryInterAdmin != None:
            self.__log("config-enable").info("%s: %s - Change Delivery Interface Admin - %s", iConf.name, actionName, iConf.deliveryInterAdmin)            
            changed = True   
                    
        if changed is False:
            self.__log("config-interface-err").error("%s: %s Interface called but no Configuration Change", iConf.name, actionName)
                        
        return changed
            

    # private
    #-------------------------------------------------------------------------------------------------
    def __isNetManagerUp (self):
        """
        Return true in case Net Manager Signal File is Valid
        If valid it means Net Manager Process is up and read to recieve configuration
        """

        if os.path.isfile(self.__netMngSignalFile):
            return True
            
        return False



    
#-----------------------------------------------------------------------
class DeliveryNetCfgNotifier(net_client.InterfaceCfgNotifier):

    #---------------------------------------------------------
    def __init__(self, notifyFunc):

        data = net_client.InterfaceDataInfo(net_client.IfDataMembers.kIpAddress,
                                            net_client.IfDataMembers.kIpv6Address,
                                            net_client.IfDataMembers.kDeviceName,
                                            net_client.IfDataMembers.kEnable)

        net_client.InterfaceCfgNotifier.__init__(self, delivery=data, delivery2=data)
        self.__notifyFunc = notifyFunc

    #---------------------------------------------------------
    def notifyChangeOnInterfaces(self, mng=None, delivery=None, delivery2=None):
        __pychecker__="no-argsused"  # mng not used (always None)

        iConfList = []

        ######################
        # temp@2.7 - 1/15/2013
        deliveryStabilityDelay = 0
        
        if delivery is not None:
            iConf = self.getDeliveryConfigChange(delivery[0], delivery[1])
            deliveryStabilityDelay = delivery[1].deliveryStabilityDelay
            iConfList.append(iConf)

        if delivery2 is not None:
            iConf = self.getDeliveryConfigChange(delivery2[0], delivery2[1])
            deliveryStabilityDelay = delivery2[1].deliveryStabilityDelay
            iConfList.append(iConf)

        if len(iConfList) > 0:
            self.__notifyFunc(iConfList, deliveryStabilityDelay)

    #---------------------------------------------------------
    def getDeliveryConfigChange(self, name, data):

        iConf = delivery_conf.InterfaceConf(name)

        if data.isOn(net_client.IfDataMembers.kIpAddress):
            iConf.ipv4Address = data.getByKey(net_client.IfDataMembers.kIpAddress)

        if data.isOn(net_client.IfDataMembers.kIpv6Address):
            iConf.ipv6Address = data.getByKey(net_client.IfDataMembers.kIpv6Address)

        if data.isOn(net_client.IfDataMembers.kDeviceName):
            iConf.egressInterface = data.getByKey(net_client.IfDataMembers.kDeviceName)

        if data.isOn(net_client.IfDataMembers.kEnable):
            iConf.deliveryInterAdmin = data.getByKey(net_client.IfDataMembers.kEnable)

        return iConf

        
