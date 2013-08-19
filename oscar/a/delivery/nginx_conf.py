#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: hagaia
# 

import os

import a.infra.file.utils
import utils

if  __package__ is None:
    G_NAME_MODULE_DELIVERY = "unknown"
    G_NAME_GROUP_DELIVERY_NGINX_CONF = "unknown"
else:
    from . import G_NAME_MODULE_DELIVERY 
    from . import G_NAME_GROUP_DELIVERY_NGINX_CONF

#-----------------------------------------------------------------
class NginxConf(object):

    #-----------------------------------------------------------------------------------------------
    def __init__ (self, name, logger):
        self.__name = name
        self.__log = logger.createLogger(G_NAME_MODULE_DELIVERY, G_NAME_GROUP_DELIVERY_NGINX_CONF)
        
    #----------------------------------------------------------------------------------------------- 
    def createDirs(self,deliveryConf):
        """
            Create Nginx directories

            Args:                
                deliveryConf - Delivery Configuration                    
        """

        # Directories To Create
        ###########################
        dirsToCreate = [deliveryConf.ngxLogDir, deliveryConf.ngxRecordsDir, deliveryConf.ngxConfDir, deliveryConf.ngxStatusDir, 
                        deliveryConf.ngxVolatilePrefixDir, deliveryConf.ngxContentBase, deliveryConf.ngxLogDirBase]
        for dirToCreate in dirsToCreate:
            try:
                a.infra.file.utils.makeDirs(dirToCreate,reuseExisting = True)
                self.__log("create-log-dir").info("Create/Validate Nginx Directory - %s",dirToCreate)
            except OSError, e:
                self.__log("create-dir-err").error("Failed to create Nginx directory - %s",dirToCreate,utils.parseErrnoToString(e))
                return False

        # Symbolic Links to Create
        ###########################
        softlinks = { deliveryConf.mediaDir : deliveryConf.ngxMediaDirSymlink,
                      deliveryConf.metaDir : deliveryConf.ngxMetaDirSymlink,
                      deliveryConf.browniesDir : deliveryConf.ngxBrowniesDirSymlink,
                      deliveryConf.filesDir     : deliveryConf.ngxFilesDirSymLink,   
                      deliveryConf.ngxStatusDir : deliveryConf.ngxStatusDirSymlink,                      
                      deliveryConf.ngxConfDir   : deliveryConf.ngxConfDirSymlink,
                      deliveryConf.ngxRecordsDir   : deliveryConf.ngxRecordsDirSymlink}

        for target in softlinks:
            source = softlinks[target]
            if os.path.islink(source):#not using os.path.exists as this is a softlink and we check the link existance and not the target        
                originalTarget = os.path.realpath(source)            
                os.remove(source)
                self.__log("remove-old-softlink").debug1("Removing softlink %s pointing to %s",
                                                         source, originalTarget)            
            elif os.path.exists(source):
                self.__log("softlink-exists-not-link-err").error("Softlink already %s exists as a real path", source)
                return False

            try:
                os.symlink(os.path.relpath(target, os.path.dirname(source)), source)
                self.__log("create-softlink").info("Create/Validate Nginx softlink %s pointing to %s",
                                                   source, target)
            except OSError, e:
                self.__log("create-softlink-err").error("Failed to create Nginx softlink %s pointing to %s",
                                                        source, target)
                return False

               
        return True

    #-----------------------------------------------------------------------------------------------   
    def prepareConfFile (self,deliveryConf):

        """
            Create Nginx Configuration file From Template Configuration File and Received Configuration

            Args:
                deliveryConf - Delivery Configuration                    

            Returns: True in success

        """
        self.__log("prepare-conf").debug1("Prepare Nginx Confiuration")
        
        
        # open template file for reading
        #=================================
        filePath = os.path.join(deliveryConf.imageDir, deliveryConf.kConf.kTemplateFileName)

        try:
            templateFile = open(filePath,'r')
            self.__log("open-template-conf").debug1("Open Nginx Template configuration File, Path - %s",filePath)
        except IOError, e:
            self.__log("open-template-conf-failed").error("Failed to open Nginx Template configuration File, Path - %s - %s",filePath,utils.parseErrnoToString(e))
            return False        

        # open for write and truncate nginx configuration file
        #======================================================
        confPath = deliveryConf.ngxConfFile

        try:
            confFile = open(confPath,'w')
            self.__log("open-conf").debug1(" Open/Create Nginx Configuration File, Path - %s", confPath)
        except IOError, e:
            self.__log("open-conf-failed").error("Failed to Open/Create Nginx Configuration File, Path - %s - %s",confPath,utils.parseErrnoToString(e))
            templateFile.close()
            return False


        confTemplate = templateFile.read()
        self.__log("read-conf").debug1(" Read Nginx Template Configuration File, Path - %s", templateFile)
        
        # calc conf        
        mask                     = self.__createCpuAffinityMask(deliveryConf)
        logLevel                 = self.__createModuleLog(deliveryConf)
        deliveryInterfacesNames  = self.__createDeliveryInterfacesNames(deliveryConf)
        deliveryPacingParameters = self.__cretaeDeliveryPacingConf(deliveryConf)

        (enableDiskThreads,diskThreadsAio) = self.__createEnableDiskThreadsConf(deliveryConf)
            
        (extListenIpAddresses,extQstatusLocations,intListenIpAddresses) = self.__createServersConfiguration(deliveryConf)

        internalQstatusLocations = self.__createQstatusLocations()

        if deliveryConf.nginxEnableMaxBodySizeHandling:
            enableMaxBodyHandling = 1
        else:
            enableMaxBodyHandling = 0
        
        # prepare conf data
        confData = {deliveryConf.kConf.kIpAddressesTemplate     : extListenIpAddresses,
                    deliveryConf.kConf.kRateLimitTemplate       : deliveryConf.nginxMaxSessionKBps,
                    deliveryConf.kConf.kLogFileTemplate         : deliveryConf.ngxErrorLogFile,
                    deliveryConf.kConf.kRecordsLogFileTemplate  : deliveryConf.ngxRecordsLogFile,
                    deliveryConf.kConf.kPidFileTemplate         : deliveryConf.ngxPidFile,
                    deliveryConf.kConf.kMediaPathTemplate       : deliveryConf.kConf.kMediaDirectoryName,
                    deliveryConf.kConf.kNgxLogLevelTemplate     : deliveryConf.nginxLogLevel, 
                    deliveryConf.kConf.kNgxNumOfWorkersTemplate : deliveryConf.nginxNumberOfWorkers, 
                    deliveryConf.kConf.kNgxWorkerConnectionsTemplate  : deliveryConf.nginxNumberOfWorkerConnections,
                    deliveryConf.kConf.kNgxWorkersAffinityTemplate    :  mask,
                    deliveryConf.kConf.kNgxModuleLogLevelTemplate     : logLevel, 
                    deliveryConf.kConf.kNgxPrefetchGapTemplate        : deliveryConf.nginxPrefetchGap,
                    deliveryConf.kConf.kNgxPrefetchContinuesTemplate  : deliveryConf.nginxPrefetchContinues,
                    deliveryConf.kConf.kNgxEnableReadaheadTemplate    : deliveryConf.nginxEnableReadahead,
                    deliveryConf.kConf.kNgxPartialReadaheadTemplate   : deliveryConf.nginxPartialReadahead,
                    deliveryConf.kConf.kContentChunkSizeTemplate      : (deliveryConf.contentChunkSizeKByte*1024),
                    deliveryConf.kConf.kIoBlockSizeTemplate           : str(deliveryConf.ioBlockSizeKByte),
                    deliveryConf.kConf.kDeliveryInterfacesTemplate    : deliveryInterfacesNames,
                    deliveryConf.kConf.kQstatusListenIpAddressTemplate   : intListenIpAddresses,
                    deliveryConf.kConf.kQStatusExternalInterfaceTemplate : extQstatusLocations,   
                    deliveryConf.kConf.kQStatusInternalInterfaceTemplate : internalQstatusLocations,                                            
                    deliveryConf.kConf.kDeliveryPacingTemplate           : deliveryPacingParameters,
                    deliveryConf.kConf.kConnectionKeepAliveTemplate      : deliveryConf.nginxConnectionKeepaliveSec,
                    deliveryConf.kConf.kNumOfDisksTemplate               : deliveryConf.nginxNumOfDisks,
                    deliveryConf.kConf.kEnableIoDisksThreadsTemplate     : enableDiskThreads,
                    deliveryConf.kConf.kDiskThreadsNginxAioTemplate      : diskThreadsAio,
                    deliveryConf.kConf.kNgxClientHeaderTimeoutTemplate   : deliveryConf.nginxClientHeaderTimeoutSec,
                    deliveryConf.kConf.kNgxClientBodyTimeoutTemplate     : deliveryConf.nginxClientBodyTimeoutSec,
                    deliveryConf.kConf.kNgxClientMaxBodySizeTemplate     : deliveryConf.nginxClientMaxBodySizeByte,
                    deliveryConf.kConf.kNgxResponseSendTimeoutTemplate   : deliveryConf.nginxResponseSendTimeoutSec,
                    deliveryConf.kConf.kNgxEnableMaxBodySizeHandlingTemplate : enableMaxBodyHandling
                    }


        self.__log("nginx-new-conf-data").debug2("Nginx Conf full data: %s", confData)
   
        confFile.write(confTemplate % confData)

        templateFile.close()
        confFile.close()

        self.__log("nginx-new-conf").info("Nginx New Configuration - %s", deliveryConf.getActiveConfigString())

        return True


    #----------------------------------------------------------------------------------------------- 
    #Build the Listen Directive  
    def __createServersConfiguration (self,deliveryConf):

        isLoopBackAddressAlreadyConfigured = False
        intListeningAddress = ""
        extQstatusLocations = "" 
        extListeningAddress = []    

        ifList = deliveryConf.getActiveInterfaces()

        #External Listening IP Address
        for iConf in ifList:
            if iConf.ipv4Address:
                extListeningAddress.append("listen\t%s:%s backlog=%s rcvbuf=%s sndbuf=%s;" % (iConf.ipv4Address, deliveryConf.port,
                    deliveryConf.listenBacklogSize, deliveryConf.socketRcvBufByte, deliveryConf.socketSndBufByte))

                # Avoid creating 2 same entries
                if ((iConf.ipv4Address == deliveryConf.kConf.kNginxStatusIp) and (deliveryConf.port == deliveryConf.nginxStatusPort)):
                    isLoopBackAddressAlreadyConfigured = True

            if iConf.ipv6Address:
                extListeningAddress.append("listen\t[%s]:%s backlog=%s rcvbuf=%s sndbuf=%s;" % (iConf.ipv6Address, deliveryConf.port,
                    deliveryConf.listenBacklogSize, deliveryConf.socketRcvBufByte, deliveryConf.socketSndBufByte))

        extListeningAddress = '\n\t'.join(extListeningAddress)
        
                
        # External Q-Status Support
        # In case status address configured as external or User param       
        if isLoopBackAddressAlreadyConfigured or deliveryConf.nginxOpenQstatusExternally:
            extQstatusLocations = self.__createQstatusLocations()
        else:
            extQstatusLocations = ""
            
                            
        # Intenal Listening Address (Q-Status)
        # Listen On Local Host (127.0.0.1) as well for qwilt status fetching
        intListeningAddress = ("listen\t%s:%s;" % (deliveryConf.kConf.kNginxStatusIp, deliveryConf.nginxStatusPort))
       
        return (extListeningAddress,extQstatusLocations,intListeningAddress)

    #----------------------------------------------------------------------------------------------- 
    # Return Delivery Interfaces Names
    def __createDeliveryInterfacesNames (self, deliveryConf):

        interfacesNames = ""
        for iConf in deliveryConf.InterfaceMap.values():

            if interfacesNames:
                interfacesNames = interfacesNames + " "
                
            interfacesNames = interfacesNames + iConf.name  + ":" + iConf.egressInterface

        return interfacesNames             


    #----------------------------------------------------------------------------------------------- 
    def __createQstatusLocations(self):
        
        # Qwilt Statistics
                
        qStatusLocations =  """ 
        # Qwilt Counters
        location = /qwilt_status {
           qwilt_status on;
        }

        # Qwilt Counters
        location = /q-status {
           qwilt_status on;
        }

        # Qwilt Site Counters
        location = /q-site-status {
           qwilt_status on;
        }

        # Qwilt Stats
        location = /q-stats {
           qwilt_status on;
        }

        # Qwilt Log Filter
        location = /q-log-filter {
           qwilt_status on;
        }        
        """

        return qStatusLocations



    #----------------------------------------------------------------------------------------------- 
    #Build the Module Log Level Directive  
    def __createModuleLog (self,deliveryConf):

        # Not Configured - Do not create directive replace Template with nothing
        if not len(deliveryConf.nginxModuleLogLevel):
            return ""

        logLevel = deliveryConf.kConf.kNgxModlueLogLevelPrefix + deliveryConf.nginxModuleLogLevel + ";"

        return logLevel


    #----------------------------------------------------------------------------------------------- 
    #Build the CPU Affinity Directive  
    def __createCpuAffinityMask (self,deliveryConf):

        # Empty List
        if not len(deliveryConf.nginxCpuAffinityList):
            return ""

        mask = ""

        deliveryConf.nginxCpuAffinityList = [int(i) for i in deliveryConf.nginxCpuAffinityList]

        maxCore = max(deliveryConf.nginxCpuAffinityList)

        reverseRange = range(maxCore + 1)
        reverseRange.reverse()

        for cpu in reverseRange:
            if cpu in deliveryConf.nginxCpuAffinityList:
                mask = mask + "1"
            else:
                mask = mask + "0"
                        
        self.__log("nginx-cpu").debug1("Nginx Workers CPU Affinity - %s", mask)

        sMask = deliveryConf.kConf.kNgxCpuAffinityDirectivePrefix
             
        sMask = sMask + str(mask)

        sMask = sMask + ";"

        return sMask

   
    #----------------------------------------------------------------------------------------------- 
    def __cretaeDeliveryPacingConf (self,deliveryConf):

        if deliveryConf.nginxDisablePacing:
            ngxDisablePacing = 1
        else:
            ngxDisablePacing = 0

        line = ("%s %s %s %s %s" % (ngxDisablePacing, deliveryConf.nginxPacingUseNewAlgo, deliveryConf.nginxPacingMinTimerTimeMsec, 
                                 deliveryConf.nginxPacingSustainedMaxRateFactor, deliveryConf.nginxPacingSustainedMaxBucketSizeFactor))

        self.__log("nginx-cpu").debug1("Nginx Delveiry Pacing - %s", line)

        return line

    #----------------------------------------------------------------------------------------------- 
    def __createEnableDiskThreadsConf(self,deliveryConf):
        
        if deliveryConf.nginxEnableIoDiskThreads:
            enable = 1
            aio = "on"
        else:
            enable = 0
            aio = "off"

        return (enable,aio)



