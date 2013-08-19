#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: hagaia
# 

import os

#------------------------------------------------------------------------------------------------
class KDeliveryConf:
                           
    # Nginx Executable Name
    kNginxExeName = "nginx"
        
    # Web Server Template File Name
    kTemplateFileName = "template_conf.txt"

    # The string needed to be replaced in Web Server Template Configuration File  
    #--------------------------------------------------------------------------------   
    kIpAddressesTemplate            = "Q_LISTEN_IP_ADDRESSES"
    kRateLimitTemplate              = "Q_RATE_LIMIT"
    kLogFileTemplate                = "Q_LOG_FILE"
    kRecordsLogFileTemplate         = "Q_RECORDS_LOG_FILE"
    kPidFileTemplate                = "Q_PID_FILE"
    kMediaPathTemplate              = "Q_MEDIA_PATH"  
    kNgxLogLevelTemplate            = "Q_LOG_LEVEL" 
    kNgxNumOfWorkersTemplate        = "Q_NUM_OF_WORKERS" 
    kNgxWorkerConnectionsTemplate   = "Q_WORKER_CONNECTIONS"
    kNgxWorkersAffinityTemplate     = "Q_WORKERS_CPU_AFFINITY" 
    kNgxModuleLogLevelTemplate      = "Q_MODULE_LOG_LEVEL"
    kNgxPrefetchGapTemplate         = "Q_PREFETCH_GAP"
    kNgxPrefetchContinuesTemplate   = "Q_PREFETCH_CONTINUES"
    kNgxEnableReadaheadTemplate     = "Q_ENABLE_READAHEAD"
    kNgxPartialReadaheadTemplate    = "Q_PARTIAL_READAHEAD"
    kContentChunkSizeTemplate       = "Q_CONTENT_CHUNK_SIZE"
    kIoBlockSizeTemplate            = "Q_IO_BLOCK_SIZE"
    kDeliveryInterfacesTemplate     = "Q_DELIVERY_INTERFACES"
    kQstatusListenIpAddressTemplate = "Q_STATUS_LISTEN_IP_ADDRESSES"
    kQStatusExternalInterfaceTemplate =  "Q_SUPPORT_EXTERNAL_Q_STATUS"
    kQStatusInternalInterfaceTemplate =  "Q_SUPPORT_INTERNAL_Q_STATUS"
    kDeliveryPacingTemplate         = "Q_DELIVERY_PACING"
    kConnectionKeepAliveTemplate    = "Q_CONNECTION_KEEPALIVE"
    kNumOfDisksTemplate             = "Q_NUM_OF_DISKS"
    kEnableIoDisksThreadsTemplate   = "Q_ENABLE_IO_DISKS_THREADS"
    kDiskThreadsNginxAioTemplate    = "Q_DISK_THREADS_NGINX_AIO"
    kNgxClientHeaderTimeoutTemplate = "Q_CLIENT_HEADER_TIMEOUT"
    kNgxClientBodyTimeoutTemplate   = "Q_CLIENT_BODY_TIMEOUT"
    kNgxClientMaxBodySizeTemplate   = "Q_CLIENT_MAX_BODY_SIZE"
    kNgxEnableMaxBodySizeHandlingTemplate = "Q_ENABLE_MAX_BODY_HANDLING"
    kNgxResponseSendTimeoutTemplate = "Q_RESPONSE_SEND_TIMEOUT" 
        
    # Nginx Configuration Constant Values 
    #--------------------------------------------------------------------------------   
    kNgxLogLevelListValue          = ["debug","info","notice","warn","error","crit"]
    kNgxLogLevelDefualtValue       = "notice"
    kNgxCpuAffinityDirectivePrefix = "worker_cpu_affinity "
    kNgxModlueLogLevelPrefix       = "qwilt_log "

    # Nginx Directories and Files Tree
    #--------------------------------------------------------------------------
    # status dir
    kStatusDir = "status"

    # Logs Dir
    kLogsDir   = "logs"

    # Configuration Dir
    kConfDir   = "conf"

    # Records Dir
    kRecordsDir = "records"

    kPidFileTemplateName        = "nginx.pid"
    kLogFileTemplateName        = "error.log"
    kRecordsLogFileTemplateName = "records.log"
    kConfFileName               = "nginx.conf"

    #content base dir
    kContentRootDir = "content"

    # Content Data Directory Name
    kMediaDirectoryName = os.path.join(kContentRootDir,"media")

    # Content Meta Data Directory Name
    kMetaDataDirectoryName = os.path.join(kContentRootDir,"meta")

    # Content Brownies Directory Name
    kBrowniesDataDirectoryName = os.path.join(kContentRootDir,"brownies")

    # Content Files Directory Name e.g. netflix access policy file, crossdomain.xml
    kFilesDataDirectoryName = os.path.join(kContentRootDir,"files")

    # Web application file name
    kWebAppFileName = "titles-delivered.dat"

    # The URL of fetching Status(counters) from Nginx
    kNginxStatusUrl = "/qwilt_status"

    # The IP of fetching Status(counters) from Nginx
    kNginxStatusIp = "127.0.0.1"

    # Topper Directories
    kTopperDataDir        = "delivery/00/vidTransactions"
    kTopperHeadersDir     = "delivery/00/fixed/vidTransactions"
    kTopperRawRecordsDir  = "delivery/00/raw"


    # Delivery Manager Constants
    #--------------------------------------------------------------------------

    # Delivery Manager Main Loop Sleep
    kMainLoopSleepTimeSec = 0.1

    # Reporter - Time Interval Values
    #=======================================================
    # Time Interval to fetch counters from Nginx Processes
    kFetchCountersFromNginxIntervalMsec = 1000

    # Read VM + Disk Stats from Linux
    kReadLinuxStatsIntervalMsec = 1000

    # Time Interval to report counters to Stat module
    kReportToStatIntervalMsec = 30000
       
    # Time Interval to report L2 and L7 Video volume to Topper (V record)
    kVolumeReportIntervalMsec = 10000

    # Time Interval to report to Web application File
    kWebAppFileUpdateIntervalMsec = 1000

    # Time Interval to check Rotation of Topper File  
    kTopperFileRotateIntervalMsec = 10000

    # Time Interval to check if Nginx Error log should be rotated
    kNginxLogRotateIntervalMsec = 1000

    # Resource Manager - Time Interval Values
    #=======================================================
    # Resource Manager Thread Loop Sleep
    kResourceManagerLoopSleepTimeSec = 0.05

    # Time Interval to calculate bandwidth to Line
    kBandwidthCalcIntervalMsec = 0 # disable - determined by 'kResourceManagerLoopSleepTimeSec'

    #=======================================================

    # Timeout for IPC HTTP request
    kIpcHttpRequestTimeoutSec = 20

    # Maximum time of waiting for child process to Terminate
    kMaxWaitTimeForChildProcessMsec = 2000

    # Delay between run ngixn failures
    kDaleyInNginxRunMSec = 1000
    
    # Max retries to run Nginx when it is in down state
    kMaxRunNginxRetries = 5

    # Command line of old worker process on shutdown
    kOldWorkerShutdownCmd = "nginx: worker process is shutting down"

    # Ethernet headers are 14 bytes
    kEthHeaderLength     = 14 


#------------------------------------------------------------------------------------------------
class KDeliveryDefaultConf:

    #default values for data in sys-param
    DEFAULT_REPORT_TO_TOPPER                = True
    DEFAULT_NGINX_LOG_LEVEL                 = "notice"
    DEFAULT_NGINX_MODULE_LOG_LEVEL          = "N"
    DEFAULT_NGINX_MAX_SESSION_KBPS          = 700
    DEFAULT_NGINX_MAX_LIVELIHOOD_RETRIES    = 30
    DEFAULT_NGINX_FETCH_COUNTERS_TIMOUT_SEC = 20    
    DEFAULT_NGINX_NUM_OF_WORKERS            = 88
    DEFAULT_NGINX_NUM_OF_WORKER_CONNECTIONS = 2048
    DEFAULT_NGINX_READ_PREFETCH_GAP         = 0
    DEFAULT_NGINX_READ_PREFETCH_CONTINUES   = 0
    DEFAULT_NGINX_READ_ENABLE_READAHEAD     = 0
    DEFAULT_NGINX_READ_PARTIAL_READAHEAD    = 0
    DEFAULT_NGINX_READ_IO_BLOCK_SIZE_KBYTE  = 1024
    DEFAULT_CONTENT_CHUNK_SIZE_KBYTE        = 1024
    DEFAULT_NGINX_LISTEN_BACKLOG_SIZE       = 20480
    DEFAULT_NGINX_SOCKET_RCVBUF_BYTE        = 65536
    DEFAULT_NGINX_SOCKET_SNDBUF_BYTE        = 1048576
    DEFAULT_MAX_TIME_TOPPER_REOPEN_WAIT_SEC = 60
    DEFAULT_OLD_WORKERS_TIMEOUT_SEC         = 60*10 # 10 minutes
    DEFAULT_WORKERS_GENERATION_LIMIT        = 3
    DEFAULT_NGINX_OPEN_Q_STATUS_EXTERNALY   = False
    DEFAULT_NGINX_CONNECTION_KEEPALIVE_SEC  = 15
 
    ## Enable Thread per Disk support of IO Operations
    DEFAULT_NGINX_ENABLE_IO_DISKS_THREADS   = False
    ##!!!!!!!!------------------------------------------------------------------------------------!!!!!
    ## In case nginx_enable-io-disks-threads = False, should change the following configuration as well
    ## nginx-num-of-workers = 88
    ## nginx-num-of-worker-connections = 2048
    ## workers-generation-limit = 3
    ## delivery.NOFILE=5120 --- qb100 user params
    ##!!!!!!!!------------------------------------------------------------------------------------!!!!!
    ## In case nginx_enable-io-disks-threads = True, should change the following configuration as well
    ## nginx-num-of-workers = 4
    ## nginx-num-of-worker-connections = 5000
    ## workers-generation-limit = 12
    # delivery.NOFILE=11000 --- qb100 user params
    ##!!!!!!!!------------------------------------------------------------------------------------!!!!!

    #Delivery Pacing
    #-------------------    
    # When set to True Delivery use Global Rate-Limit configuration (DEFAULT_NGINX_MAX_SESSION_KBPS)
    # and ignores any pacing configuration arrives from brownie
    # When Setting nginx-max-session-kbps to 0 no rate limit at all
    DEFAULT_NGINX_DISABLE_PACING = False

    DEFAULT_NGINX_PACING_USE_NEW_ALGO                     = 1
    DEFAULT_NGINX_PACING_MIN_TIMER_TIME_MSEC              = 10
    DEFAULT_NGINX_PACING_SUSTAINED_MAX_RATE_FACTOR        = 1.0
    DEFAULT_NGINX_PACING_SUSTAIEND_MAX_BUCKET_SIZE_FACTOR = 2.0

    DEFAULT_DELIVERY_BW_FILTER_FACTOR        = 0.0
    DEFAULT_DELIVERY_VOLUME_ENABLE_IP_TABLES = True

    # Specifies how long to wait for the client to send a request header
    # This timeout is reached only if a header is not received in one read (needs clarification). 
    # If the client has not sent anything within this timeout period, 
    # nginx returns the HTTP status code 408 ("Request timed out")
    DEFAULT_NGINX_CLIENT_HEADER_TIMEOUT_SEC   = 20

    # Directive sets the read timeout for the request body from client.
    # The timeout is set only if a body is not get in one readstep. 
    # If after this time the client send nothing, nginx returns error "Request time out" (408). 
    DEFAULT_NGINX_CLIENT_BODY_TIMEOUT_SEC     = 0

    # Specifies the maximum accepted body size of a client request, as indicated by the request header Content-Length.
    # If the stated content length is greater than this size, then the client receives the HTTP error code 413 ("Request Entity Too Large"). 
    # It should be noted that web browsers do not usually know how to properly display such an HTTP error.
    # Set to 0 to disable
    DEFAULT_NGINX_CLIENT_MAX_BODY_SIZE_BYTE  = 1

    # Id not enabked, Use native nginx handling for body size bigger than
    # self.nginxClientMaxBodySizeByte
    DEFAULT_NGINX_ENABLE_MAX_BODY_SIZE_HANDLING = True

    # Specifies the response timeout to the client. 
    # This timeout does not apply to the entire transfer 
    # but, rather, only between two subsequent client-read operations. 
    # Thus, if the client has not read any data for this amount of time, 
    # then nginx shuts down the connection. 
    DEFAULT_NGINX_RESPONSE_SEND_TIMEOUT_SEC = 60


    # Max Allowed virtual memory for nginx worker
    # Using ulimit -Sv in nginx execution
    # 0 - disable max memory for worker
    DEFAULT_NGINX_WORKER_MAX_MEMORY_SIZE_MBYTE = 0


    # When enabled(default) Delivey Manager will restart Nginx in case 
    # Nginx Counter ("General-NginxWorkerProcessCrashed") is different than 0
    DEFAULT_DELIVERY_RESTART_NGINX_IF_WORKER_CRASH = True

#------------------------------------------------------------------------------------------------
class DeliveryConf:

    # Each configurable variable has config change sevirity
    kNoConfigLevel       = 0
    kGeneralConfigLevel  = 1
    kNginxConfigLevel    = 2

    kOscarUpdateConfigFileName = "delivery_manager.cfg"

    def __init__ (self):

        __pychecker__ = "maxlines=400"
        
        #------------------------------------------------------      
        # delivery config id is incremented on every change
        self.configId         = 0

        # Delivery Interface map
        self.InterfaceMap = {}   
        
        # is Part of Unit Test
        self.isUT   = False

        # Is start Web Server
        # Should be up when IP Address configured and Interface is Up 
        self.isWebServerAdminUp    = False

        #----------------------------------------------------------------------------
        # Constatnts
        #----------------------------------------------------------------------------
        self.kConf = KDeliveryConf()

        #----------------------------------------------------------------------------
        # Specific Params
        #----------------------------------------------------------------------------
        # Nginx Exe Path
        self.ngxBinDir        = ""
      
        # Nginx Port
        self.port             = 0
      
        #qwilt_status port
        self.nginxStatusPort  = 0
      
        # Delivery Topper Directory
        self.topperDir        = ""
      
        # Nginx Template Configuration Path
        self.imageDir         = ""
      
        self.sysVarDir        = ""
        self.sysRunDir        = ""
        self.dataVarDir       = ""
      
        # Web UI Status Directory
        self.webStatusDir    = ""
      
        self.mediaDir = ""
        self.metaDir = ""
        self.browniesDir= ""
        self.filesDir  = ""
      
        # System Stats Directory
        self.statsDir = ""
      
        # falg is MINI platform
        self.isMini = True
      
        # List of CPU cores to bind Nginx workers procesess
        self.nginxCpuAffinityList = []
      
        # Existence of that file sign that Net Manager Process is up and
        # Delviery Manager can start and activate config agent (blinky) and 
        # start getting configuration
        self.netSignalFileName = ""        
      
        # Nginx Log Configuration
        #----------------------------------------------
        self.nginxDirectoryLogSizeByte  = 20*1024*1204
        self.nginxLogFileSizeByte       = 1024*1204
      
        # When This file sexist, Line can redirect to Delivery
        # It is Delivery responsability to create/delete it 
        # when it can serve redirects (Nginx Up)
        self.allowLineRedirectFileName = ""
      
        # Number os supported Disks
        self.nginxNumOfDisks = 22
                
        #----------------------------------------------------------------------------
        # User Params
        #----------------------------------------------------------------------------
        defaultConf = KDeliveryDefaultConf()

        self.configDict = {}

        # General Configuration
        #------------------------
        self.reportToTopper      = defaultConf.DEFAULT_REPORT_TO_TOPPER
        self.configDict['reportToTopper'] = {"configLevel" : self.kGeneralConfigLevel}

        # Max Number of failures in fetching Nginx Counters before nginx restart 
        self.maxFetchCounterError = defaultConf.DEFAULT_NGINX_MAX_LIVELIHOOD_RETRIES
        self.configDict['maxFetchCounterError'] = {"configLevel" : self.kGeneralConfigLevel}

        # max time to fetch counters from nginx before failure
        self.countersFetchTimeoutSec = defaultConf.DEFAULT_NGINX_FETCH_COUNTERS_TIMOUT_SEC
        self.configDict['countersFetchTimeoutSec'] = {"configLevel" : self.kGeneralConfigLevel}

        # Maximum time to wait Nginx worker reopen records log in Topper File Rotation
        self.maxTimeReopenWaitSec = defaultConf.DEFAULT_MAX_TIME_TOPPER_REOPEN_WAIT_SEC
        self.configDict['maxTimeReopenWaitSec'] = {"configLevel" : self.kGeneralConfigLevel}

        # Nginx old workers monitoring        
        self.nginxOldWorkersTimeLimitSec     = defaultConf.DEFAULT_OLD_WORKERS_TIMEOUT_SEC
        self.configDict['nginxOldWorkersTimeLimitSec'] = {"configLevel" : self.kGeneralConfigLevel}

        self.nginxOldWorkersGenerationLimit  = defaultConf.DEFAULT_WORKERS_GENERATION_LIMIT
        self.configDict['nginxOldWorkersGenerationLimit'] = {"configLevel" : self.kGeneralConfigLevel}

        # Low-pass filter factor to calculate bandwidth (in percent)
        self.bwFilterFactorPercent = defaultConf.DEFAULT_DELIVERY_BW_FILTER_FACTOR
        self.configDict['bwFilterFactorPercent'] = {"configLevel" : self.kGeneralConfigLevel}

        # Enable ip tables for volume reporting
        self.deliveryVolumeEnableIpTables = defaultConf.DEFAULT_DELIVERY_VOLUME_ENABLE_IP_TABLES
        self.configDict['deliveryVolumeEnableIpTables'] = {"configLevel" : self.kGeneralConfigLevel}

        # Restart Nginx if Worker crashed
        self.deliveryRestartOnWorkerCrash= defaultConf.DEFAULT_DELIVERY_RESTART_NGINX_IF_WORKER_CRASH
        self.configDict['deliveryRestartOnWorkerCrash'] = {"configLevel" : self.kGeneralConfigLevel}
        

        # Nginx Configuration
        #---------------------------------------------------------------------------------------------------------------
    
        self.nginxLogLevel = defaultConf.DEFAULT_NGINX_LOG_LEVEL
        self.configDict['nginxLogLevel'] = {"configLevel" : self.kNginxConfigLevel}

        self.nginxModuleLogLevel = defaultConf.DEFAULT_NGINX_MODULE_LOG_LEVEL
        self.configDict['nginxModuleLogLevel'] = {"configLevel" : self.kNginxConfigLevel}

        # 700 K Byte Per Second
        self.nginxMaxSessionKBps = defaultConf.DEFAULT_NGINX_MAX_SESSION_KBPS
        self.configDict['nginxMaxSessionKBps'] = {"configLevel" : self.kNginxConfigLevel}

        # The distance in content chunk blocks from current block to be fetched
        self.nginxPrefetchGap = defaultConf.DEFAULT_NGINX_READ_PREFETCH_GAP
        self.configDict['nginxPrefetchGap'] = {"configLevel" : self.kNginxConfigLevel}

        # if != 0 the prefetch is to [0-nginxPrefetchGap] and not only to nginxPrefetchGap block
        self.nginxPrefetchContinues = defaultConf.DEFAULT_NGINX_READ_PREFETCH_CONTINUES
        self.configDict['nginxPrefetchContinues'] = {"configLevel" : self.kNginxConfigLevel}

        # 0 - readahead disabled
        # 1 - readahead on redirect session first request or offset == 0
        # 2 - readahead on every request 
        self.nginxEnableReadahead = defaultConf.DEFAULT_NGINX_READ_ENABLE_READAHEAD
        self.configDict['nginxEnableReadahead'] = {"configLevel" : self.kNginxConfigLevel}

        # request offset (A-B)
        # 0 - readahead the content chunk contains A and content chunk contains B
        # 1 - readahead the content chunk contains B
        self.nginxPartialReadahead = defaultConf.DEFAULT_NGINX_READ_PARTIAL_READAHEAD
        self.configDict['nginxPartialReadahead'] = {"configLevel" : self.kNginxConfigLevel}
                
        # number of workers processes
        self.nginxNumberOfWorkers = defaultConf.DEFAULT_NGINX_NUM_OF_WORKERS
        self.configDict['nginxNumberOfWorkers'] = {"configLevel" : self.kNginxConfigLevel}

        # Maximum number of connection per Nginx Worker
        self.nginxNumberOfWorkerConnections = defaultConf.DEFAULT_NGINX_NUM_OF_WORKER_CONNECTIONS
        self.configDict['nginxNumberOfWorkerConnections'] = {"configLevel" : self.kNginxConfigLevel}

        # Content(media file) chunk size
        self.contentChunkSizeKByte = defaultConf.DEFAULT_CONTENT_CHUNK_SIZE_KBYTE
        self.configDict['contentChunkSizeKByte'] = {"configLevel" : self.kNginxConfigLevel}

        # Read from Disk IO Block Size in KByte
        self.ioBlockSizeKByte = defaultConf.DEFAULT_NGINX_READ_IO_BLOCK_SIZE_KBYTE
        self.configDict['ioBlockSizeKByte'] = {"configLevel" : self.kNginxConfigLevel}

        # The backlog argument defines the maximum length to 
        # which the queue of pending connections for sockfd may grow
        self.listenBacklogSize = defaultConf.DEFAULT_NGINX_LISTEN_BACKLOG_SIZE
        self.configDict['listenBacklogSize'] = {"configLevel" : self.kNginxConfigLevel}

        # Maximum Socket Send Buffer
        self.socketSndBufByte = defaultConf.DEFAULT_NGINX_SOCKET_SNDBUF_BYTE
        self.configDict['socketSndBufByte'] = {"configLevel" : self.kNginxConfigLevel}

        # Maximum Socket Receive Buffer
        self.socketRcvBufByte = defaultConf.DEFAULT_NGINX_SOCKET_RCVBUF_BYTE
        self.configDict['socketRcvBufByte'] = {"configLevel" : self.kNginxConfigLevel}

        # Nginx Open q-status externally
        self.nginxOpenQstatusExternally = defaultConf.DEFAULT_NGINX_OPEN_Q_STATUS_EXTERNALY
        self.configDict['nginxOpenQstatusExternally'] = {"configLevel" : self.kNginxConfigLevel}

        # How long a connection should stay valid in case of no traffic
        self.nginxConnectionKeepaliveSec = defaultConf.DEFAULT_NGINX_CONNECTION_KEEPALIVE_SEC
        self.configDict['nginxConnectionKeepaliveSec'] = {"configLevel" : self.kNginxConfigLevel}

        # New Delveiry pacing algorithem (leaky bucket)
        self.nginxPacingUseNewAlgo = defaultConf.DEFAULT_NGINX_PACING_USE_NEW_ALGO
        self.configDict['nginxPacingUseNewAlgo'] = {"configLevel" : self.kNginxConfigLevel}

        self.nginxPacingMinTimerTimeMsec = defaultConf.DEFAULT_NGINX_PACING_MIN_TIMER_TIME_MSEC
        self.configDict['nginxPacingMinTimerTimeMsec'] = {"configLevel" : self.kNginxConfigLevel}

        self.nginxPacingSustainedMaxRateFactor = defaultConf.DEFAULT_NGINX_PACING_SUSTAINED_MAX_RATE_FACTOR
        self.configDict['nginxPacingSustainedMaxRateFactor'] = {"configLevel" : self.kNginxConfigLevel}

        self.nginxPacingSustainedMaxBucketSizeFactor = defaultConf.DEFAULT_NGINX_PACING_SUSTAIEND_MAX_BUCKET_SIZE_FACTOR
        self.configDict['nginxPacingSustainedMaxBucketSizeFactor'] = {"configLevel" : self.kNginxConfigLevel}

        self.nginxDisablePacing = defaultConf.DEFAULT_NGINX_DISABLE_PACING
        self.configDict['nginxDisablePacing'] = {"configLevel" : self.kNginxConfigLevel}
        
        # Enable Thread per Disks for IO
        self.nginxEnableIoDiskThreads = defaultConf.DEFAULT_NGINX_ENABLE_IO_DISKS_THREADS
        self.configDict['nginxEnableIoDiskThreads'] = {"configLevel" : self.kNginxConfigLevel}

        self.nginxClientHeaderTimeoutSec = defaultConf.DEFAULT_NGINX_CLIENT_HEADER_TIMEOUT_SEC
        self.configDict['nginxClientHeaderTimeoutSec'] = {"configLevel" : self.kNginxConfigLevel}

        self.nginxClientBodyTimeoutSec = defaultConf.DEFAULT_NGINX_CLIENT_BODY_TIMEOUT_SEC
        self.configDict['nginxClientBodyTimeoutSec'] = {"configLevel" : self.kNginxConfigLevel}

        self.nginxClientMaxBodySizeByte = defaultConf.DEFAULT_NGINX_CLIENT_MAX_BODY_SIZE_BYTE
        self.configDict['nginxClientMaxBodySizeByte'] = {"configLevel" : self.kNginxConfigLevel}

        self.nginxEnableMaxBodySizeHandling = defaultConf.DEFAULT_NGINX_ENABLE_MAX_BODY_SIZE_HANDLING
        self.configDict['nginxEnableMaxBodySizeHandling'] = {"configLevel" : self.kNginxConfigLevel}

        self.nginxResponseSendTimeoutSec = defaultConf.DEFAULT_NGINX_RESPONSE_SEND_TIMEOUT_SEC
        self.configDict['nginxResponseSendTimeoutSec'] = {"configLevel" : self.kNginxConfigLevel}
        
        self.nginxWorkerMaxMemorySizeMbyte = defaultConf.DEFAULT_NGINX_WORKER_MAX_MEMORY_SIZE_MBYTE
        self.configDict['nginxWorkerMaxMemorySizeMbyte'] = {"configLevel" : self.kNginxConfigLevel}

        
   
    #----------------------------------------------
    def validateConfiguration (self, log):

        if self.contentChunkSizeKByte < self.ioBlockSizeKByte:
            log("size-mismatch").error("Delivery Conf - Content Chunk Size (%d) < Io Block Size (%d)",self.contentChunkSizeKByte,self.ioBlockSizeKByte)
            self.contentChunkSizeKByte = self.ioBlockSizeKByte


    #----------------------------------------------
    def updateUserParamConfigIfChanged (self, newDictConfig, log):

        self.__configChanged = self.kNoConfigLevel

        for key, value in self.configDict.iteritems():
            if key in newDictConfig:
                self.setIfChanged(newDictConfig[key], key, value['configLevel'], log)

        return self.__configChanged

    #----------------------------------------------
    def setIfChanged (self,varNewValue,varName,configLevel, log):

        if hasattr (self,varName) is False:
            log("config-not-exist").notice("Named attribute does not exist in Current Configuration- %s",varName)
            return False

        curValue = getattr(self,varName)            
                
        if curValue == varNewValue:
            log("no-update-config").debug2("No Update Configuration of Variable %s",varName)
            return False
        
        setattr(self, varName, varNewValue)

        if self.__configChanged < configLevel:
            self.__configChanged = configLevel

        log("update-config").notice("Update Configuration of Variable %s from %s to %s - Config Level = %d",varName,str(curValue),str(varNewValue),configLevel)
        return True

    #----------------------------------------------
    def clacLogDir (self, dataVarDir):
        __pychecker__ = 'no-argsused'
        return os.path.join(dataVarDir, "log", "nginx")

    #----------------------------------------------
    def calcPaths(self):
        self.ngxConfDir       = os.path.join(self.sysRunDir, self.kConf.kConfDir)
        self.ngxConfFile      = os.path.join(self.ngxConfDir, self.kConf.kConfFileName)

        self.ngxStatusDir     = os.path.join(self.sysRunDir, self.kConf.kStatusDir)
        self.actualNgxPidFile = os.path.join(self.ngxStatusDir, self.kConf.kPidFileTemplateName)
        
        # Delviery Records
        self.ngxRecordsDir           = os.path.join(self.topperDir, self.kConf.kTopperRawRecordsDir)        
        self.actualNgxRecordsLogFile = os.path.join(self.ngxRecordsDir, self.kConf.kRecordsLogFileTemplateName)

        self.ngxVolatilePrefixDir = os.path.join(self.sysRunDir, "nginx")
        self.ngxPidFile = os.path.join(self.kConf.kStatusDir, self.kConf.kPidFileTemplateName)
       
        self.ngxErrorLogFile = os.path.join(self.kConf.kLogsDir, self.kConf.kLogFileTemplateName)
        self.ngxRecordsLogFile = os.path.join(self.kConf.kRecordsDir, self.kConf.kRecordsLogFileTemplateName)

        self.ngxContentBase = os.path.join(self.ngxVolatilePrefixDir, self.kConf.kContentRootDir)
        self.ngxMediaDirSymlink = os.path.join(self.ngxVolatilePrefixDir, self.kConf.kMediaDirectoryName)
        self.ngxMetaDirSymlink = os.path.join(self.ngxVolatilePrefixDir, self.kConf.kMetaDataDirectoryName)
        self.ngxBrowniesDirSymlink = os.path.join(self.ngxVolatilePrefixDir, self.kConf.kBrowniesDataDirectoryName)
        self.ngxFilesDirSymLink = os.path.join(self.ngxVolatilePrefixDir, self.kConf.kFilesDataDirectoryName)
       
        self.ngxStatusDirSymlink = os.path.join(self.ngxVolatilePrefixDir,self.kConf.kStatusDir)
        
        self.ngxConfDirSymlink   = os.path.join(self.ngxVolatilePrefixDir,self.kConf.kConfDir)
        self.ngxRecordsDirSymlink   = os.path.join(self.ngxVolatilePrefixDir,self.kConf.kRecordsDir)

        # Nginx Logs
        self.ngxLogDir             = self.clacLogDir(self.dataVarDir)
        self.ngxLogDirBase         = os.path.join(self.ngxVolatilePrefixDir,self.kConf.kLogsDir)        
        self.ngxLogFileSymLink     = os.path.join(self.ngxLogDirBase, self.kConf.kLogFileTemplateName)

    #---------------------------------------------- 
    def getActiveInterfaces (self):

        activeInterfaces = []

        for iConf in self.InterfaceMap.values():
            if iConf.isUp():
                activeInterfaces.append(iConf)
        
        return activeInterfaces

    #---------------------------------------------- 
    def getActiveConfigString (self):

        ipv4List = []
        ipv6List = []

        for iConf in self.InterfaceMap.values():
            if iConf.isUp():
                if iConf.ipv4Address:
                    ipv4List.append(iConf.ipv4Address)
                
                if iConf.ipv6Address:
                    ipv6List.append(iConf.ipv6Address)
        
        return "IPv4 = %s, IPv6 = %s, Port = '%s'" % (ipv4List,ipv6List,self.port)
               
#-----------------------------------------------------------------
class DynamicDeliveryConf:

    def __init__ (self):

        self.isPreNet = False
        self.iconfList = [] # list of InterfaceConf objects 

        # when (time in secs) the delivery manager should apply new config
        self.timeToConfigure = 0

    def __str__(self):       
        return str(self.iconfList)

#-----------------------------------------------------------------
class InterfaceConf:

    def __init__ (self, name):
        self.name       = name

        # Nginx Ipv4 Address
        self.ipv4Address  = None

        # Nginx Ipv6 Address
        self.ipv6Address  = None

        # Delivery Default Egress Interface Name
        self.egressInterface     = None

        # Delivery Interface state
        self.deliveryInterAdmin     = None

    #----------------------------------------------   
    def __str__(self):
        strList = []
        strList.append("%s:" % self.name)
        strList.append("ipv4: %s" % self.ipv4Address)
        strList.append("ipv6: %s" % self.ipv6Address)
        strList.append("device: %s" % self.egressInterface)
        strList.append("enable: %s" % self.deliveryInterAdmin)
        
        return ' '.join(strList)

    #----------------------------------------------        
    def hasIp (self):
        if (self.ipv4Address and (len(self.ipv4Address)) != 0 or 
            (self.ipv6Address and len(self.ipv6Address) != 0)):
            return True

        return False

   #----------------------------------------------        
    def isUp (self):
        # If Valid IPv4 or IPv6 and Interface Up
        if self.hasIp() and (self.egressInterface and len(self.egressInterface) != 0) and self.deliveryInterAdmin:
            return True

        return False
