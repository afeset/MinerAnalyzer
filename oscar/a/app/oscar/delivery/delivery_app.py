#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: hagaia
# 

import os 

from optparse import OptionParser
import a.delivery.delivery_manager
import a.delivery.delivery_conf

if  __package__ is None:
    G_NAME_MODULE_DELIVERY_APP = "unknown"
    G_NAME_GROUP_DELIVERY_APP_DELIVERY_APP = "unknown"
else:
    from . import G_NAME_MODULE_DELIVERY_APP
    from . import G_NAME_GROUP_DELIVERY_APP_DELIVERY_APP

class DeliveryApp(object):

    """
    This is the interface between Oscar application and Delivery Module
    Delivery module is in-charge on Oscar Content Delivery
    """    

    #consts for sections/fields names in sys-param
    CONFIG_SECTION_DELIVERY_MNG            = "delivery-mngr"
    CONFIG_VAR_REPORT_TO_TOPPER            = "report-to-topper"
    CONFIG_NGINX_LOG_LEVEL                 = "nginx-log-level"
    CONFIG_NGINX_MODULE_LOG_LEVEL          = "nginx-module-log-level"
    CONFIG_NGINX_MAX_SESSION_KBPS          = "nginx-max-session-kbps"
    CONFIG_NGINX_MAX_LIVELIHOOD_RETRIES    = "nginx-max-livelihood-retries"
    CONFIG_NGINX_FETCH_COUNTERS_TIMOUT_SEC = "nginx-fetch-counters-timeout-sec"
    CONFIG_NGINX_NUM_OF_WORKERS            = "nginx-num-of-workers"
    CONFIG_NGINX_NUM_OF_WORKER_CONNECTIONS = "nginx-num-of-worker-connections"
    CONFIG_NGINX_READ_PREFETCH_GAP         = "nginx-read-prefetch-gap"
    CONFIG_NGINX_READ_PREFETCH_CONTINUES   = "nginx-read-prefetch-continues"
    CONFIG_NGINX_READ_ENABLE_READAHEAD     = "nginx-read-enable-readahead"
    CONFIG_NGINX_READ_PARTIAL_READAHEAD    = "nginx-read-partial-readahead"
    CONFIG_NGINX_READ_IO_BLOCK_SIZE_KBYTE  = "nginx-read-io-block-size-kbyte"
    CONFIG_CONTENT_CHUNK_SIZE_KBYTE        = "content-chunk-size-kbyte"    
    CONFIG_NGINX_LISTEN_BACKLOG_SIZE       = "nginx-listen-backlog-size"
    CONFIG_NGINX_SOCKET_RCVBUF_BYTE        = "nginx-socket-rcvbuf-byte"
    CONFIG_NGINX_SOCKET_SNDBUF_BYTE        = "nginx-socket-sndbuf-byte"
    CONFIG_MAX_TIME_TOPPER_REOPEN_WAIT_SEC = "max-time-topper-reopen-wait-sec"
    CONFIG_OLD_WORKERS_TIMEOUT_SEC         = "old-workers-timeout-sec"
    CONFIG_WORKERS_GENERATION_LIMIT        = "workers-generation-limit"
    CONFIG_NGINX_OPEN_Q_STATUS_EXTERNALY   = "nginx-open-q-status-externally"
    CONFIG_NGINX_CONNECTION_KEEPALIVE_SEC  = "nginx-connection-keepalive-sec"
    CONFIG_NGINX_ENABLE_IO_DISKS_THREADS   = "nginx_enable-io-disks-threads"
    
    CONFIG_NGINX_DISABLE_PACING                          = "nginx-pacing-disable" 
    CONFIG_NGINX_PACING_USE_NEW_ALGO                     = "nginx-pacing-use-new-algo"
    CONFIG_NGINX_PACING_MIN_TIMER_TIME_MSEC              = "nginx-pacing-min-timer-time-msec"
    CONFIG_NGINX_PACING_SUSTAINED_MAX_RATE_FACTOR        = "nginx-pacing-sustained-max-rate-factor"
    CONFIG_NGINX_PACING_SUSTAIEND_MAX_BUCKET_SIZE_FACTOR = "nginx-pacing-sustained-max-bucket-size-factor"
    

    CONFIG_DELIVERY_BW_FILTER_FACTOR                     = "delivery-bw-filter-factor"
    CONFIG_DELIVERY_VOLUME_ENABLE_IP_TABLES              = "delivery-volume-enable-ip-tables"

    CONFIG_NGINX_CLIENT_HEADER_TIMEOUT_SEC               = "nginx-client-header-timeout-sec"    
    CONFIG_NGINX_CLIENT_BODY_TIMEOUT_SEC                 = "nginx-client-body-timeout-sec"      
    CONFIG_NGINX_CLIENT_MAX_BODY_SIZE_BYTE               = "nginx-client-max-body-size-byte" 
    CONFIG_NGINX_ENABLE_MAX_BODY_SIZE_HANDLING           = "nginx-enable-max-body-size-handling"
    CONFIG_NGINX_RESPONSE_SEND_TIMEOUT_SEC               = "nginx-response-send-timeout-sec"

    CONFIG_NGINX_WORKER_MAX_MEMORY_SIZE_MBYTE            = "nginx-worker-max-memory-size-mbyte"

    CONFIG_DELIVERY_RESTART_NGINX_IF_WORKER_CRASH        = "delivery-restart-nginx-if-worker-crash"    

        
    #default values for data in sys-param
    #-------------------------------------------------------
    # You can find Defualts in a.delivery.delivery_conf
        
    #consts use for the specificParams dictionary provided on "initspecificParams"
    SPECIFIC_PARAM_KEY_WEB_BIN_DIR      = "web-bin-dir"    
    SPECIFIC_PARAM_KEY_WEB_PORT         = "web-port"
    SPECIFIC_PARAM_KEY_WEB_STATUS_PORT  = "web-status-port"
    SPECIFIC_PARAM_KEY_IMAGE_DIR        = "image-dir"
    SPECIFIC_PARAM_KEY_VAR_DIR          = "var-dir"
    SPECIFIC_PARAM_KEY_SYS_VAR_DIR      = "sys-var-dir"
    SPECIFIC_PARAM_KEY_SYS_RUN_DIR      = "sys-run-dir"
    SPECIFIC_PARAM_KEY_DATA_VAR_DIR     = "data-var-dir"
    SPECIFIC_PARAM_KEY_REPORT_DIR       = "report-dir"  
    SPECIFIC_PARAM_KEY_WEB_STATUS_DIR   = "web-status-dir"    
    SPECIFIC_PARAM_KEY_MEDIA_DIR        = "media-dir"
    SPECIFIC_PARAM_KEY_META_DIR         = "meta-dir"
    SPECIFIC_PARAM_KEY_BROWNIES_DIR     = "brownies-dir"
    SPECIFIC_PARAM_KEY_IS_MINI_MACHINE  = "mini-kill-all"

    SPECIFIC_PARAM_KEY_FILES_DIR             = "files-dir"    
    SPECIFIC_PARAM_KEY_NGINX_CPU_AFFINITY    = "nginx-cpu-affinity"
    SPECIFIC_PARAM_KEY_NET_SIGNAL_FILE_NAME  = "net-signal-file"

    SPECIFIC_PARAM_KEY_TOTAL_LOG_SIZE = "total-log-size"
    SPECIFIC_PARAM_KEY_LOG_FILE_SIZE  = "log-file-size"

    SPECIFIC_PARAM_KEY_ALLOW_REDIRECT_FILE  = "allow-redirect-file"

    SPECIFIC_PARAM_NUM_OF_DISKS  = "num-of-disks"

    #private consts
       
    def __init__ (self):
        self.__deliveryConf = a.delivery.delivery_conf.DeliveryConf()

    ###implementing functions called directly by oscar
    #-------------------------------------------------------------------------------------------------
    def daemonControlInitLogger(self, logger):
        """
        Init the class logger to be used.
    
        Args:
            logger: a logger from which new loggers shall be created
        """
        self.__logger = logger
        self.__log = logger.createLogger(G_NAME_MODULE_DELIVERY_APP, G_NAME_GROUP_DELIVERY_APP_DELIVERY_APP)

    #-----------------------------------------------------------------------------------------------------------------------
    def  daemonControlInitBlinky(self, agent):
        """Init the process blinky to be used.

        Args:
            agent: a blinky agent
        """

        self.__blinkyAgent = agent


    #-----------------------------------------------------------------------------------------------------------------------
    def  daemonControlInitStats(self, statsDir):
        """
        Init Stats Module
        """

        self.__deliveryConf.statsDir = statsDir
        
    #-------------------------------------------------------------------------------------------------
    def daemonControlInitExternalData(self, sysParamsCfg, specificParams):
        """
        Init the data provided from outside
        
        Args:
            sysParamsCfg: a contatiner holding the sys params base configuration (that are destined to move to blinky)
            specificParams: a dictionary holding the data under the "SPECIFIC_PARAM_KEY_..." keys defined at the begining of this class                                            
        """       
        
        self.__loadSpecificParamsCfg(specificParams)
                                                                                                                                                                    
        # Print specificParams Configuration
        #---------------------------------------------------------------------------
        logLine=""        
        for k,v  in specificParams.iteritems():
            logLine = logLine + "\n" + str(k) + " : " + str(v)

        self.__log("conf-param").notice(logLine)


        # It prints it's Sys param inside the call
        #---------------------------------------------------------------------------
        self.__loadSysParamsCfg(sysParamsCfg)


        # Calculate configuration Implications
        #---------------------------------------------------------------------------
        self.__deliveryConf.calcPaths()
                                                                                                                                                                
        
    #-------------------------------------------------------------------------------------------------
    def daemonControlCreateUpdateData (self, updateDir, sysParamsCfg, logger):

        """
        reload configuration
    
        This function is called in the context of oscar core.
        It is responsible to create the update information (taken from sys params) and store it in a file
        accessible to the process        
        """

        self.__log = logger
                
        self.__loadSysParamsCfg(sysParamsCfg)        

        deliveryDictConfig = {}
    
        try:
            filename = os.path.join(updateDir, self.__deliveryConf.kOscarUpdateConfigFileName)
    
            for key in self.__deliveryConf.configDict:
                if hasattr(self.__deliveryConf,key):
                    deliveryDictConfig[key] = getattr(self.__deliveryConf,key)
    
            a.infra.format.json.writeToFile(logger, deliveryDictConfig, filename)
        except (IOError, TypeError) as ex:
            self.__log("error-write-cfg").error("Error in write configuration file %s - %s", filename, ex)          
            
    #-------------------------------------------------------------------------------------------------
    def __loadSpecificParamsCfg(self, specificParams):

        self.__deliveryConf.ngxBinDir                 = specificParams[self.SPECIFIC_PARAM_KEY_WEB_BIN_DIR]
        self.__deliveryConf.port                      = specificParams[self.SPECIFIC_PARAM_KEY_WEB_PORT]
        self.__deliveryConf.nginxStatusPort           = specificParams[self.SPECIFIC_PARAM_KEY_WEB_STATUS_PORT]        
        self.__deliveryConf.topperDir                 = specificParams[self.SPECIFIC_PARAM_KEY_REPORT_DIR]
        self.__deliveryConf.imageDir                  = specificParams[self.SPECIFIC_PARAM_KEY_IMAGE_DIR]
        self.__deliveryConf.sysVarDir                 = specificParams[self.SPECIFIC_PARAM_KEY_SYS_VAR_DIR]
        self.__deliveryConf.sysRunDir                 = specificParams[self.SPECIFIC_PARAM_KEY_SYS_RUN_DIR]
        self.__deliveryConf.dataVarDir                = specificParams[self.SPECIFIC_PARAM_KEY_DATA_VAR_DIR]
        self.__deliveryConf.webStatusDir              = specificParams[self.SPECIFIC_PARAM_KEY_WEB_STATUS_DIR]
        self.__deliveryConf.mediaDir                  = specificParams[self.SPECIFIC_PARAM_KEY_MEDIA_DIR]
        self.__deliveryConf.metaDir                   = specificParams[self.SPECIFIC_PARAM_KEY_META_DIR]
        self.__deliveryConf.browniesDir               = specificParams[self.SPECIFIC_PARAM_KEY_BROWNIES_DIR]
        self.__deliveryConf.isMini                    = specificParams[self.SPECIFIC_PARAM_KEY_IS_MINI_MACHINE]
        self.__deliveryConf.filesDir                  = specificParams[self.SPECIFIC_PARAM_KEY_FILES_DIR]         
        self.__deliveryConf.nginxCpuAffinityList      = specificParams[self.SPECIFIC_PARAM_KEY_NGINX_CPU_AFFINITY]
        self.__deliveryConf.netSignalFileName         = specificParams[self.SPECIFIC_PARAM_KEY_NET_SIGNAL_FILE_NAME]        
        self.__deliveryConf.nginxDirectoryLogSizeByte = specificParams[self.SPECIFIC_PARAM_KEY_TOTAL_LOG_SIZE]
        self.__deliveryConf.nginxLogFileSizeByte      = specificParams[self.SPECIFIC_PARAM_KEY_LOG_FILE_SIZE]        
        self.__deliveryConf.allowLineRedirectFileName = specificParams[self.SPECIFIC_PARAM_KEY_ALLOW_REDIRECT_FILE]
        self.__deliveryConf.nginxNumOfDisks           = specificParams[self.SPECIFIC_PARAM_NUM_OF_DISKS]
             
    #-------------------------------------------------------------------------------------------------
    def __loadSysParamsCfg(self, sysParamsCfg):

        __pychecker__ = "maxlines=400"
      
        # In debug I may use sysParamsCfg == None
        if sysParamsCfg == None:
            return

        deliveryDefaultConf = a.delivery.delivery_conf.KDeliveryDefaultConf()

        # Should Delivery Manager rotate V+F records file into Topper Directories
        #---------------------------------------------------------------------------
        self.__deliveryConf.reportToTopper   = sysParamsCfg.getBool(self.CONFIG_SECTION_DELIVERY_MNG,
                                                                    self.CONFIG_VAR_REPORT_TO_TOPPER,
                                                                    deliveryDefaultConf.DEFAULT_REPORT_TO_TOPPER)                                                                        

        self.__log("report-to-topper").notice("sys-params - report to topper = %s",str(self.__deliveryConf.reportToTopper))


        # Nginx Log Level
        #---------------------------------------------------------------------------
        nginxLogLevel = sysParamsCfg.getString(self.CONFIG_SECTION_DELIVERY_MNG,
                                               self.CONFIG_NGINX_LOG_LEVEL,
                                               deliveryDefaultConf.DEFAULT_NGINX_LOG_LEVEL)

        if nginxLogLevel in self.__deliveryConf.kConf.kNgxLogLevelListValue:
            self.__deliveryConf.nginxLogLevel = nginxLogLevel
            self.__log("nginx-log-level").notice("sys-params - nginx log level = %s",str(self.__deliveryConf.nginxLogLevel))
        else:
            self.__deliveryConf.nginxLogLevel = self.__deliveryConf.kNgxLogLevelDefualtValue
            self.__log("nginx-log-level-err").error("Sys Param Cfg - Unfamiliar Nginx Log Level - %s",nginxLogLevel)


        # Nginx Module Log Level
        #---------------------------------------------------------------------------
        self.__deliveryConf.nginxModuleLogLevel = sysParamsCfg.getString(self.CONFIG_SECTION_DELIVERY_MNG,
                                                                         self.CONFIG_NGINX_MODULE_LOG_LEVEL,
                                                                         deliveryDefaultConf.DEFAULT_NGINX_MODULE_LOG_LEVEL)

        self.__log("nginx-module-log-level").notice("sys-params - nginx module log level = %s",str(self.__deliveryConf.nginxModuleLogLevel))

        # Nginx Session Max Bitrate
        #---------------------------------------------------------------------------
        self.__deliveryConf.nginxMaxSessionKBps = sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_MNG,
                                                                      self.CONFIG_NGINX_MAX_SESSION_KBPS,
                                                                      deliveryDefaultConf.DEFAULT_NGINX_MAX_SESSION_KBPS)

        self.__log("nginx-max-session-kbps").notice("sys-params - nginx max session = %d kbps",self.__deliveryConf.nginxMaxSessionKBps)


        # Nginx Max Livelihhod retries before Delivery Exit
        #---------------------------------------------------------------------------
        self.__deliveryConf.maxFetchCounterError = sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_MNG,
                                                                       self.CONFIG_NGINX_MAX_LIVELIHOOD_RETRIES,
                                                                       deliveryDefaultConf.DEFAULT_NGINX_MAX_LIVELIHOOD_RETRIES)

        self.__log("max-fetch-counter-err").notice("sys-params - max fetch counter error = %d",self.__deliveryConf.maxFetchCounterError)        

        # max time to fetch counters from nginx before failure
        #---------------------------------------------------------------------------
        self.__deliveryConf.countersFetchTimeoutSec = sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_MNG,
                                                                          self.CONFIG_NGINX_FETCH_COUNTERS_TIMOUT_SEC,
                                                                          deliveryDefaultConf.DEFAULT_NGINX_FETCH_COUNTERS_TIMOUT_SEC)

        self.__log("counter-fetch-timeout-sec").notice("sys-params - counter-fetch-timeout-sec = %d",self.__deliveryConf.countersFetchTimeoutSec)

        # number of workers processes
        #---------------------------------------------------------------------------
        self.__deliveryConf.nginxNumberOfWorkers = self.getNumberOfNginxWorkers(sysParamsCfg)

        self.__log("num-of-workers").notice("sys-params - num-of-nginx-workers = %d",self.__deliveryConf.nginxNumberOfWorkers)


        # number of worker connections
        #---------------------------------------------------------------------------
        self.__deliveryConf.nginxNumberOfWorkerConnections = sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_MNG,
                                                                                 self.CONFIG_NGINX_NUM_OF_WORKER_CONNECTIONS,
                                                                                 deliveryDefaultConf.DEFAULT_NGINX_NUM_OF_WORKER_CONNECTIONS)

        self.__log("num-of-worker-connections").notice("sys-params - num-of-nginx-worker-connections = %d",self.__deliveryConf.nginxNumberOfWorkerConnections)


        # read from disk configuration
        #---------------------------------------------------------------------------
        self.__deliveryConf.nginxPrefetchGap = sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_MNG,
                                                              self.CONFIG_NGINX_READ_PREFETCH_GAP,
                                                              deliveryDefaultConf.DEFAULT_NGINX_READ_PREFETCH_GAP)

        self.__deliveryConf.nginxPrefetchContinues = sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_MNG,
                                                                    self.CONFIG_NGINX_READ_PREFETCH_CONTINUES,
                                                                    deliveryDefaultConf.DEFAULT_NGINX_READ_PREFETCH_CONTINUES)
                
        self.__deliveryConf.nginxEnableReadahead = sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_MNG,
                                                                  self.CONFIG_NGINX_READ_ENABLE_READAHEAD,
                                                                  deliveryDefaultConf.DEFAULT_NGINX_READ_ENABLE_READAHEAD)

        self.__deliveryConf.nginxPartialReadahead = sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_MNG,
                                                                   self.CONFIG_NGINX_READ_PARTIAL_READAHEAD,
                                                                   deliveryDefaultConf.DEFAULT_NGINX_READ_PARTIAL_READAHEAD)

        self.__log("readahead").notice("sys-params - readahead info - prefetch-gap = %d  prefetch-continues = %d  enable-readahead = %d partial-readahead = %d",
                                       self.__deliveryConf.nginxPrefetchGap, self.__deliveryConf.nginxPrefetchContinues, 
                                       self.__deliveryConf.nginxEnableReadahead,  self.__deliveryConf.nginxPartialReadahead)

        self.__deliveryConf.ioBlockSizeKByte = sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_MNG,
                                                                   self.CONFIG_NGINX_READ_IO_BLOCK_SIZE_KBYTE,
                                                                   deliveryDefaultConf.DEFAULT_NGINX_READ_IO_BLOCK_SIZE_KBYTE)

        self.__log("io-block-size").notice("sys-params - io-block-size = %d KByte",self.__deliveryConf.ioBlockSizeKByte)

        # Content(media file) chunk size
        #---------------------------------------------------------------------------
        self.__deliveryConf.contentChunkSizeByte = sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_MNG,
                                                                       self.CONFIG_CONTENT_CHUNK_SIZE_KBYTE,
                                                                       deliveryDefaultConf.DEFAULT_CONTENT_CHUNK_SIZE_KBYTE)

        self.__log("content-chunk-size").notice("sys-params - content-chunk-size = %d KByte",self.__deliveryConf.contentChunkSizeKByte)

        # Nginx Socket Configuration
        #---------------------------------------------------------------------------

        self.__deliveryConf.listenBacklogSize = sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_MNG,
                                                                    self.CONFIG_NGINX_LISTEN_BACKLOG_SIZE,
                                                                    deliveryDefaultConf.DEFAULT_NGINX_LISTEN_BACKLOG_SIZE)

        self.__deliveryConf.socketRcvBufByte = sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_MNG,
                                                                   self.CONFIG_NGINX_SOCKET_RCVBUF_BYTE,
                                                                   deliveryDefaultConf.DEFAULT_NGINX_SOCKET_RCVBUF_BYTE)

        self.__deliveryConf.socketSndBufByte = sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_MNG,
                                                                   self.CONFIG_NGINX_SOCKET_SNDBUF_BYTE,
                                                                   deliveryDefaultConf.DEFAULT_NGINX_SOCKET_SNDBUF_BYTE)

        self.__log("socket-conf").notice("sys-params - listen-backlog-size = %d socket-rcvbuf = %d socket-sndbuf = %d",
                                         self.__deliveryConf.listenBacklogSize,
                                         self.__deliveryConf.socketRcvBufByte,
                                         self.__deliveryConf.socketSndBufByte)


        # Max Time Delivery Manager waits for Nginx worker to Reopen records log file
        #---------------------------------------------------------------------------
        self.__deliveryConf.maxTimeReopenWaitSec = sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_MNG,
                                                                       self.CONFIG_MAX_TIME_TOPPER_REOPEN_WAIT_SEC,
                                                                       deliveryDefaultConf.DEFAULT_MAX_TIME_TOPPER_REOPEN_WAIT_SEC)

        self.__log("reopen-wait").notice("sys-params - max-time-topper-reopen-wait-sec = %d ",self.__deliveryConf.maxTimeReopenWaitSec)

        # Nginx old workers monitoring
        #---------------------------------------------------------------------------
        self.__deliveryConf.nginxOldWorkersTimeLimitSec     = sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_MNG,
                                                                                  self.CONFIG_OLD_WORKERS_TIMEOUT_SEC,
                                                                                  deliveryDefaultConf.DEFAULT_OLD_WORKERS_TIMEOUT_SEC)

        self.__deliveryConf.nginxOldWorkersGenerationLimit  = self.getWorkersGenerationLimit(sysParamsCfg)

        self.__log("workers-conf").notice("sys-params - old-workers-timeout-sec = %d workers-generation-limit = %d",
                                           self.__deliveryConf.nginxOldWorkersTimeLimitSec,
                                           self.__deliveryConf.nginxOldWorkersGenerationLimit)


        # Nginx Open q-status externally
        #---------------------------------------------------------------------------
        self.__deliveryConf.nginxOpenQstatusExternally = sysParamsCfg.getBool(self.CONFIG_SECTION_DELIVERY_MNG,
                                                                              self.CONFIG_NGINX_OPEN_Q_STATUS_EXTERNALY,
                                                                              deliveryDefaultConf.DEFAULT_NGINX_OPEN_Q_STATUS_EXTERNALY)

        self.__log("q-status-externally").notice("sys-params - open q-status externally = %s",str(self.__deliveryConf.nginxOpenQstatusExternally))



        # Nginx connection keep alive value
        #---------------------------------------------------------------------------
        self.__deliveryConf.nginxConnectionKeepaliveSec = sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_MNG,
                                                                              self.CONFIG_NGINX_CONNECTION_KEEPALIVE_SEC,
                                                                              deliveryDefaultConf.DEFAULT_NGINX_CONNECTION_KEEPALIVE_SEC)

        self.__log("keep-alive").notice("sys-params - nginx connection keepalive sec = %s",str(self.__deliveryConf.nginxConnectionKeepaliveSec))


        # Delivery Pacing
        #---------------------------------------------------------------------------
        self.__deliveryConf.nginxDisablePacing = sysParamsCfg.getBool(self.CONFIG_SECTION_DELIVERY_MNG,
                                                                      self.CONFIG_NGINX_DISABLE_PACING,
                                                                      deliveryDefaultConf.DEFAULT_NGINX_DISABLE_PACING)

        self.__deliveryConf.nginxPacingUseNewAlgo = sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_MNG,
                                                                        self.CONFIG_NGINX_PACING_USE_NEW_ALGO,
                                                                        deliveryDefaultConf.DEFAULT_NGINX_PACING_USE_NEW_ALGO)

        self.__deliveryConf.nginxPacingMinTimerTimeMsec = sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_MNG,
                                                                              self.CONFIG_NGINX_PACING_MIN_TIMER_TIME_MSEC,
                                                                              deliveryDefaultConf.DEFAULT_NGINX_PACING_MIN_TIMER_TIME_MSEC)

        self.__deliveryConf.nginxPacingSustainedMaxRateFactor = sysParamsCfg.getFloat(self.CONFIG_SECTION_DELIVERY_MNG,
                                                                                      self.CONFIG_NGINX_PACING_SUSTAINED_MAX_RATE_FACTOR,
                                                                                      deliveryDefaultConf.DEFAULT_NGINX_PACING_SUSTAINED_MAX_RATE_FACTOR)

        self.__deliveryConf.nginxPacingSustainedMaxBucketSizeFactor = sysParamsCfg.getFloat(self.CONFIG_SECTION_DELIVERY_MNG,
                                                                                            self.CONFIG_NGINX_PACING_SUSTAIEND_MAX_BUCKET_SIZE_FACTOR,
                                                                                            deliveryDefaultConf.DEFAULT_NGINX_PACING_SUSTAIEND_MAX_BUCKET_SIZE_FACTOR)
        

        self.__log("delivery-pacing").notice("sys-params - Delivery Pacing: Disable = %s, New Algo = %d MinSleepTime = %d SustainedFactorPercent = %s SustainedBucketSizeFactor = %s",
                                             str(self.__deliveryConf.nginxDisablePacing),self.__deliveryConf.nginxPacingUseNewAlgo,
                                             self.__deliveryConf.nginxPacingMinTimerTimeMsec,str(self.__deliveryConf.nginxPacingSustainedMaxRateFactor), 
                                             str(self.__deliveryConf.nginxPacingSustainedMaxBucketSizeFactor))

        # Delivery Bandwidth algo
        #---------------------------------------------------------------------------
        self.__deliveryConf.bwFilterFactorPercent = sysParamsCfg.getFloat(self.CONFIG_SECTION_DELIVERY_MNG,
                                                                          self.CONFIG_DELIVERY_BW_FILTER_FACTOR,
                                                                          deliveryDefaultConf.DEFAULT_DELIVERY_BW_FILTER_FACTOR)


        self.__log("delivery-bw").notice("sys-params - Delivery BW, BW Filter Factor = %d%%",
                                         (self.__deliveryConf.bwFilterFactorPercent * 100))

        # IO Disks Threads
        #---------------------------------------------------------------------------
        self.__deliveryConf.nginxEnableIoDiskThreads = sysParamsCfg.getBool(self.CONFIG_SECTION_DELIVERY_MNG,
                                                                            self.CONFIG_NGINX_ENABLE_IO_DISKS_THREADS,
                                                                            deliveryDefaultConf.DEFAULT_NGINX_ENABLE_IO_DISKS_THREADS)

        self.__log("enable-disks-threads").notice("sys-params - Enable IO Disks Threads = %s",str(self.__deliveryConf.nginxEnableIoDiskThreads))    


         # Delivery Volume
        #---------------------------------------------------------------------------
        self.__deliveryConf.deliveryVolumeEnableIpTables = sysParamsCfg.getBool(self.CONFIG_SECTION_DELIVERY_MNG,
                                                                                self.CONFIG_DELIVERY_VOLUME_ENABLE_IP_TABLES,
                                                                                deliveryDefaultConf.DEFAULT_DELIVERY_VOLUME_ENABLE_IP_TABLES)


        self.__log("delivery-volume").notice("sys-params - Delivery Volume, Enable IP Tables = %s",
                                             self.__deliveryConf.deliveryVolumeEnableIpTables)

        # Client Header Timeout
        #---------------------------------------------------------------------------
        self.__deliveryConf.nginxClientHeaderTimeoutSec = sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_MNG,
                                                                              self.CONFIG_NGINX_CLIENT_HEADER_TIMEOUT_SEC,
                                                                              deliveryDefaultConf.DEFAULT_NGINX_CLIENT_HEADER_TIMEOUT_SEC)

        self.__log("client-header-time").notice("sys-params - Client Header Timeout  = %s sec",str(self.__deliveryConf.nginxClientHeaderTimeoutSec))    



        # Client Body Timeout
        #---------------------------------------------------------------------------
        self.__deliveryConf.nginxClientBodyTimeoutSec = sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_MNG,
                                                                            self.CONFIG_NGINX_CLIENT_BODY_TIMEOUT_SEC,
                                                                            deliveryDefaultConf.DEFAULT_NGINX_CLIENT_BODY_TIMEOUT_SEC)

        self.__log("client-body-time").notice("sys-params - Client Body Timeout  = %s sec",str(self.__deliveryConf.nginxClientBodyTimeoutSec))
        
        
        # Client Body Max Size
        #---------------------------------------------------------------------------
        self.__deliveryConf.nginxClientMaxBodySizeKbyte = sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_MNG,
                                                                              self.CONFIG_NGINX_CLIENT_MAX_BODY_SIZE_BYTE,
                                                                              deliveryDefaultConf.DEFAULT_NGINX_CLIENT_MAX_BODY_SIZE_BYTE)

        self.__log("client-max-body-size").notice("sys-params - Client Max Body Size  = %s Byte",str(self.__deliveryConf.nginxClientMaxBodySizeKbyte))

        
        self.__deliveryConf.nginxEnableMaxBodySizeHandling = sysParamsCfg.getBool(self.CONFIG_SECTION_DELIVERY_MNG,
                                                                                  self.CONFIG_NGINX_ENABLE_MAX_BODY_SIZE_HANDLING,
                                                                                  deliveryDefaultConf.DEFAULT_NGINX_ENABLE_MAX_BODY_SIZE_HANDLING)

        self.__log("max-body-size-handling").notice("sys-params - Enable Max Body Size Handling  = %s",str(self.__deliveryConf.nginxEnableMaxBodySizeHandling))    


        # Response Send Timeout
        #---------------------------------------------------------------------------
        self.__deliveryConf.nginxResponseSendTimeoutSec = sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_MNG,
                                                                              self.CONFIG_NGINX_RESPONSE_SEND_TIMEOUT_SEC,
                                                                              deliveryDefaultConf.DEFAULT_NGINX_RESPONSE_SEND_TIMEOUT_SEC)

        self.__log("response-send-timeout").notice("sys-params - Response Send Timeout  = %s sec",str(self.__deliveryConf.nginxResponseSendTimeoutSec))
        

        # Nginx Worker Max Memory Size
        #---------------------------------------------------------------------------
        self.__deliveryConf.nginxWorkerMaxMemorySizeMbyte = sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_MNG,
                                                                                self.CONFIG_NGINX_WORKER_MAX_MEMORY_SIZE_MBYTE,
                                                                                deliveryDefaultConf.DEFAULT_NGINX_WORKER_MAX_MEMORY_SIZE_MBYTE)

        self.__log("nginx-worker-max-memory").notice("sys-params - Nginx Worker Max Memory Size  = %s MByte",str(self.__deliveryConf.nginxWorkerMaxMemorySizeMbyte))


        # Restart nginx when worker crashed
        #---------------------------------------------------------------------------
        self.__deliveryConf.deliveryRestartOnWorkerCrash= sysParamsCfg.getBool(self.CONFIG_SECTION_DELIVERY_MNG,
                                                                               self.CONFIG_DELIVERY_RESTART_NGINX_IF_WORKER_CRASH,
                                                                               deliveryDefaultConf.DEFAULT_DELIVERY_RESTART_NGINX_IF_WORKER_CRASH)

        self.__log("delivery-restart-on-crash").notice("sys-params - Restart Nginx if Worker Crashed = %s",str(self.__deliveryConf.deliveryRestartOnWorkerCrash))
         

        
    #-------------------------------------------------------------------------------------------------     
    def daemonControlStart (self):

        self.__deliveryManager = a.delivery.delivery_manager.DeliveryManager("delivery-manager", self.__logger, self.__blinkyAgent)
        self.__log("run-delivery-app").info("Start Delivery Application")

        # if Init Failed do not run
        if not self.__deliveryManager.init(self.__deliveryConf):
            return False


        if not self.__deliveryManager.start():
            return False

        return True

    #-------------------------------------------------------------------------------------------------     
    def daemonControlRun(self):
        """
        Launching Delivery untill stop command is called    
        This function returns only after calling to daemonControlStop      
        """
        
        return self.__deliveryManager.run()
            
    #-----------------------------------------------------------------------------------------------
    def daemonControlStop (self):
        """
           Stop Delivery - This function is called from a context of signal handling.       
        """
                
        self.__deliveryManager.stop()


    # --- getLogDirs --------------------------------------------------------------------------------------------------
    def getLogDirs(self, dataVarDir):

        # Returns a list of directories containing log files 
        return [self.__deliveryConf.clacLogDir(dataVarDir)]

    # --- getLogDir --------------------------------------------------------------------------------------------------
    def getLogDir(self, entity, dataVarDir):
        dirPerEntity = self.getLogDirsPerEntity(dataVarDir)
        if entity in dirPerEntity:
            return dirPerEntity[entity]
        return None

    #-----------------------------------------------------------------------------------------------
    def getLogDirsPerEntity (self, dataVarDir):
        return {self.getNginxEntityName(): self.__deliveryConf.clacLogDir(dataVarDir)}

    #-----------------------------------------------------------------------------------------------
    def getNginxEntityName (self):
        return "nginx"

    #-----------------------------------------------------------------------------------------------
    def getNumberOfNginxWorkers (self, sysParamsCfg):
        return sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_MNG,
                                   self.CONFIG_NGINX_NUM_OF_WORKERS,
                                   a.delivery.delivery_conf.KDeliveryDefaultConf().DEFAULT_NGINX_NUM_OF_WORKERS)
    
    #-----------------------------------------------------------------------------------------------
    def getWorkersGenerationLimit (self, sysParamsCfg):
        return sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_MNG,
                             self.CONFIG_WORKERS_GENERATION_LIMIT,
                             a.delivery.delivery_conf.KDeliveryDefaultConf().DEFAULT_WORKERS_GENERATION_LIMIT)
