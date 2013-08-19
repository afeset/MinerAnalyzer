#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: hagaia
# Modified by: yoave

import os
import shutil

import a.infra.format.json

import copy
import utils
import delivery_volume
import delivery_conf

#from a.infra.misc.timeout_guard import TimeoutGuard
from threading import Lock

if  __package__ is None:
    G_NAME_MODULE_DELIVERY = "unknown"
    G_NAME_GROUP_DELIVERY_RESOURCE_MNG = "unknown"
else:
    from . import G_NAME_MODULE_DELIVERY 
    from . import G_NAME_GROUP_DELIVERY_RESOURCE_MNG

#-----------------------------------------------------------------
class ResourceConf:

    def __init__ (self):

        self.kConf = delivery_conf.KDeliveryConf() # constants
        
        self.configId                   = 0
        self.allowLineRedirectFileName  = ""
        self.bwFilterFactorPercent      = None
        self.port                       = 0
        self.isMini                     = None
        self.deliveryVolumeEnableIpTables= None
        self.InterfaceMap               = {}

    def __str__ (self):
        strList = []
        strList.append("configId: %s" % self.configId)
        strList.append("allowLineRedirectFileName: '%s'" % self.allowLineRedirectFileName)
        strList.append("bwFilterFactorPercent: %s" % self.bwFilterFactorPercent)
        strList.append("port: %s" % self.port)
        strList.append("isMini: '%s'" % self.isMini)
        strList.append("deliveryVolumeEnableIpTables: %s" % self.deliveryVolumeEnableIpTables)

        for ifname in self.InterfaceMap:
            strList.append("%s" % (self.InterfaceMap[ifname]))
        
        return '\n'.join(strList)

#-----------------------------------------------------------------
class ResourceManager(object):

    DEFAULT_TIMEOUT_MILI_SEC = 400

    #-------------------------------------------------------------------------------------------------
    def __init__ (self, name, logger):

        self.__name = name                
        self.__log = logger.createLogger(G_NAME_MODULE_DELIVERY, G_NAME_GROUP_DELIVERY_RESOURCE_MNG)    
        self.__ngxStatus = None        
        self.__conf      = None
        self.__confLock = Lock()
        self.__lastConfigId= 0

        self.__timeFromLastBandwidthCalcMsec = 0

        self._prevBandwidthSample = 0
        self._currentBandwidthSample = 0

        self._volumeManager = delivery_volume.VolumeManager(self.__log)
        self.__redirectFile = DeliveryStateFile()

        # dedicated thread in charge of resource manager
        self.__thread = utils.PeriodicThread(self.__log, self.__name)

        self.__timeService = utils.TimesSerivce()
        self.__localTimeService = utils.TimesSerivce()


    #-------------------------------------------------------------------------------------------------
    def init (self, deliveryConf, ngxStatus):

        if deliveryConf.isMini is True:
            ResourceManager.DEFAULT_TIMEOUT_MILI_SEC = 5000
            self.__log("default-timeout").notice("Change Default Timeout to %s msec on Mini",ResourceManager.DEFAULT_TIMEOUT_MILI_SEC)

        self.__conf = ResourceConf()
        self.updateConf(deliveryConf)
        self.__ngxStatus = ngxStatus

        self._volumeManager.init(self.__conf)

        if not len(self.__conf.allowLineRedirectFileName):
            self.__log("exist-in-init").notice("Allow Line Redirect File Name is empty - %s",self.__conf.allowLineRedirectFileName)
            return

        # delete file if somehow exist
        if self.__deleteIfExist() :
            self.__log("exist-in-init").notice("Allow Line Redirect File is valid in init - %s",self.__conf.allowLineRedirectFileName)

        # start thread
        self.__thread.init(self._oneTick, deliveryConf.kConf.kResourceManagerLoopSleepTimeSec)
        self.__thread.start()

    #-------------------------------------------------------------------------------------------------
    def updateConf (self, deliveryConf):

        # update ResourceConf from DeliveryConf @ thread-safe
        with self.__confLock:
                         
            self.__conf.bwFilterFactorPercent      = deliveryConf.bwFilterFactorPercent     
            self.__conf.allowLineRedirectFileName  = deliveryConf.allowLineRedirectFileName 
            self.__conf.port                       = deliveryConf.port                       
            self.__conf.isMini                     = deliveryConf.isMini                     
            self.__conf.deliveryVolumeEnableIpTables = False # volume based interface counters (see OSC-2316)
            self.__conf.InterfaceMap               = copy.deepcopy(deliveryConf.InterfaceMap)
            self.__conf.configId+=1 

            self.__log("update-conf-end").info("%s: update configuration done - %s", self.__name, self.__conf)

    #-------------------------------------------------------------------------------------------------
    # In case Oper Status is Up 
    #  validtae exitance of Line-Delivery-Allow-Redirect file, Create if not Exist
    # In case Oper Status is Down
    #  delete file if exist 
    def _oneTick (self):

        timeFromLastTickMsec = self.__timeService.tickFromLastMsec()

        if not len(self.__conf.allowLineRedirectFileName):
            return

        shouldUpdate = False

        # Update Bandwidth
        #--------------------------------------------------------------------------------------------------- 
        if self.__handleBandwidth(timeFromLastTickMsec):
            shouldUpdate = True

        # Update conf status
        #--------------------------------------------------------------------------------------------------- 
        if self.__handleConfStatus():
            shouldUpdate = True

        # if operetional state is up we create/update the file (if needed)
        if self.__ngxStatus.operStatus:
            self.__updateOrCreateIfNotExist(shouldUpdate)

        # if opertional state is down and file exist delete it
        else:
            self.__deleteIfExist()

    #-------------------------------------------------------------------------------------------------
    def end (self):

        self.__thread.stop()
        self.__thread.join(timeout=2.0) # wait until the thread terminates up to 2 secs

        if self.__thread.isAlive() is True:
            self.__log("thread-alive-after-stop").warning("Thread is still Alive after Stop")

        if not len(self.__conf.allowLineRedirectFileName):
            return

        # delete file before exit
        self.__deleteIfExist()

     #protected 
    #-------------------------------------------------------------------------------------------------
    def _handleBandwidthForUnitTest (self, bandwidthIntervalMsec):
        self.__updateBandwidth(bandwidthIntervalMsec)


     #private   
    #-------------------------------------------------------------------------------------------------
    def __deleteIfExist (self):

        try:
            if os.path.exists(self.__conf.allowLineRedirectFileName):
                self.__log("file-not-exist").info("Allow line Redirect File exist - Delete it")
                os.remove(self.__conf.allowLineRedirectFileName)
                return True

        except Exception, e:
            self.__log("delete-if-exist").error("Fail to Check If Exist or Remove File %s -%s",self.__conf.allowLineRedirectFileName,utils.parseErrnoToString(e))
        
        return False

    #-------------------------------------------------------------------------------------------------
    def __updateOrCreateIfNotExist (self, shouldUpdate):  

        try:
            if not os.path.exists(self.__conf.allowLineRedirectFileName):
                self.__log("create-file").info("Allow line Redirect File is created - data: %s", self.__redirectFile)
            else:
                if not shouldUpdate:
                    return True

                self.__log("update-file").debug4("Allow line Redirect File is updated - data: %s", self.__redirectFile)

            #timeoutGuard = TimeoutGuard(self.__log, 'update-or-create', self.DEFAULT_TIMEOUT_MILI_SEC)
            self.__redirectFile.writeToFile(self.__log, self.__conf.allowLineRedirectFileName)
            #timeoutGuard.checkAndLog(self.__redirectFile.writeToFile)

            return True

        except Exception, e:
            self.__log("cretae-file-error").error("Fail to Check If Exist or Create File %s -%s",self.__conf.allowLineRedirectFileName,utils.parseErrnoToString(e))
        
        return False

    #-------------------------------------------------------------------------------------------------
    def __handleBandwidth (self, timeFromLastTickMsec):

        self.__timeFromLastBandwidthCalcMsec = self.__timeFromLastBandwidthCalcMsec + timeFromLastTickMsec
     
        if self.__timeFromLastBandwidthCalcMsec >= self.__conf.kConf.kBandwidthCalcIntervalMsec:
     
            self.__localTimeService.init()            
     
            #timeoutGuard = TimeoutGuard(self.__log, 'handle-bandwidth', self.DEFAULT_TIMEOUT_MILI_SEC) 
            self.__updateBandwidth(self.__timeFromLastBandwidthCalcMsec)
            #timeoutGuard.checkAndLog(self.__updateBandwidth)

            self.__timeFromLastBandwidthCalcMsec = 0

            self.__log("handle-bandwidth").debug4("Handle Bandwidth (%d ms) - Interval %d",
                                               self.__localTimeService.tickFromInitMsec(),self.__conf.kConf.kBandwidthCalcIntervalMsec)
            return True

        return False

    #-------------------------------------------------------------------------------------------------
    def __updateBandwidth (self, bandwidthIntervalMsec):

        volume = delivery_volume.VolumeCounters()

        if self._volumeManager.collectVolume(volume):
            self.__calcBandwidth(volume, bandwidthIntervalMsec)
            self.__redirectFile.deliverdBwKbps = int(self._currentBandwidthSample)
              
    #-------------------------------------------------------------------------------------------------
    def __calcBandwidth (self, volume, bandwidthIntervalMsec):
        totalBytesOut = 0

        i = 0        
        # critical section @ thread-safe
        self.__confLock.acquire()
        for iConf in self.__conf.InterfaceMap.values():
            totalBytesOut += volume.volumeCounters[i].bytesOut

            self.__log("calc-bandwidth-interface").debug3("Calculate Bandwidth Interface - %s Device = %s -- RX = %s TX = %s",
                                                          iConf.name, iConf.egressInterface, 
                                                          volume.volumeCounters[i].bytesIn, volume.volumeCounters[i].bytesOut)
            i = i + 1
        self.__confLock.release()

        self.__log("total-bandwidth-data").debug3("Total Tx Bytes %s  (interval-msec=%s)", totalBytesOut, bandwidthIntervalMsec)

        # calc in Kilobit per second
        currentBandwidth = totalBytesOut/float(bandwidthIntervalMsec) # KB/sec
        currentBandwidth *= 8       # Kb/sec

        self._prevBandwidthSample = self._currentBandwidthSample

        # low-pass filter to reduce burst affect
        bwFilterFactorPercent = self.__conf.bwFilterFactorPercent
        self._currentBandwidthSample = (currentBandwidth*(1-bwFilterFactorPercent)) + (self._prevBandwidthSample*bwFilterFactorPercent)

        self.__log("total-bandwidth-calc").debug3("Calculate Bandwidth - current bw = %.2f Kb/sec -- filtered-bw-sample current/previous = %.2f/%.2f Kb/sec (filter-factor=%.2f)", 
                                                  currentBandwidth, self._currentBandwidthSample, self._prevBandwidthSample, bwFilterFactorPercent)

    #-------------------------------------------------------------------------------------------------
    def __handleConfStatus (self):

        if self.__conf.configId != self.__lastConfigId:
            # critical section @ thread-safe
            self.__confLock.acquire()

            self.__lastConfigId = self.__conf.configId
            self.__log("conf-status-change").debug1("Conf Status change detected (id=%s): %s", self.__lastConfigId, self.__conf.InterfaceMap)

            #timeoutGuard = TimeoutGuard(self.__log, 'handle-conf-status', self.DEFAULT_TIMEOUT_MILI_SEC)
            self.__updateConfStatus()
            #timeoutGuard.checkAndLog(self.__updateConfStatus)

            self.__confLock.release()

            return True

        return False

    #-------------------------------------------------------------------------------------------------
    def __updateConfStatus (self):  

        # clear
        self.__redirectFile.clearInterfaces()  

        # loops over all delivery interfaces
        for iConf in self.__conf.InterfaceMap.values():
            isIpv4Delivered = False
            isIpv6Delivered = False

            if iConf.isUp():
                if iConf.ipv4Address:
                    isIpv4Delivered = True
                
                if iConf.ipv6Address:
                    isIpv6Delivered = True

            # update interface ipv4 and ipv6 status
            self.__redirectFile.addDeliveryInterface(iConf.name, isIpv4Delivered, isIpv6Delivered)

            self.__log("conf-status-interface").debug3("Conf Delivery Interface - %s -- ipv4 status = %s ipv6 status = %s",
                                                       iConf.name, isIpv4Delivered, isIpv6Delivered)


#-------------------------------------------------------------------------------
class DeliveryInterfacStateGpb(object):
    def __init__(self):
        self.interfaceName = ""
        self.deliveryIPv4State=False
        self.deliveryIPv6State=False

class DeliveryStateFile(object):
    DELIVERY_INTERFACES_KEY = "deliveryInterfaces"
    
    def __init__(self):

        # MUST contain only data that should be dumpped into json
        self.deliverdBwKbps = 0
        self.deliveryInterfaces = []

    #-------------------------------------------------------------------------------------------------
    def __str__(self):
        data = self._getDataToDump()

        return str(data)

    #-------------------------------------------------------------------------------------------------
    def clearInterfaces(self):
        self.deliveryInterfaces[:] = []

    #-------------------------------------------------------------------------------------------------
    def addDeliveryInterface(self, name, isIpv4Delivered, isIpv6Delivered):
        delivery = DeliveryInterfacStateGpb()
        delivery.interfaceName = name
        delivery.deliveryIPv4State = isIpv4Delivered
        delivery.deliveryIPv6State = isIpv6Delivered

        self.deliveryInterfaces.append(delivery)

    #-------------------------------------------------------------------------------------------------
    def writeToFile (self, log, filename):

        data = self._getDataToDump()

        tempfile = "%s.tmp" % filename
        a.infra.format.json.writeToFile(log, data, tempfile, indent=4)
        shutil.move(tempfile, filename)

    #-------------------------------------------------------------------------------------------------
    def _getDataToDump(self):

        # in order to serialize obj as a JSON formatted stream
        # we convert the file object into a dictionary
        data = self.__dict__.copy()

        deliveryIfList = []
        for delivery in self.deliveryInterfaces:
            # we convert each interface object into a dictionary as well 
            deliveryData = delivery.__dict__.copy()
            deliveryIfList.append(deliveryData)

        data[DeliveryStateFile.DELIVERY_INTERFACES_KEY] = deliveryIfList

        return data
