import os
import stat
import time
import logging
import logging.handlers
import inspect

import fcntl

import pprint
import sys

# based on logging.handlers.WatchedFileHandler
class LockedWatchedLoggerFileHandler(logging.FileHandler):

    def __init__(self, filename, mode='a', encoding=None, delay=0, manualFlush = False):
        self.manualFlush = manualFlush 
        logging.FileHandler.__init__(self, filename, mode, encoding, delay)
        if not os.path.exists(self.baseFilename):
            self.dev, self.ino = -1, -1
        else:
            fileStat = os.stat(self.baseFilename)
            self.dev, self.ino = fileStat[stat.ST_DEV], fileStat[stat.ST_INO]

        # Init records list    
        self.records = []

    def emit(self, record):
        # Just save the record
        self.records.append(record)
        if not self.manualFlush:
            self.emitFlush()

    def emitFlush(self):
        
        # Check if file was changed 
        if not os.path.exists(self.baseFilename):
            fileStat = None
            changed = 1
        else:
            fileStat = os.stat(self.baseFilename)
            changed = (fileStat[stat.ST_DEV] != self.dev) or (fileStat[stat.ST_INO] != self.ino)
        if changed and self.stream is not None:
            self.stream.flush()
            self.stream.close()
            self.stream = self._open()
            if fileStat is None:
                fileStat = os.stat(self.baseFilename)
            self.dev, self.ino = fileStat[stat.ST_DEV], fileStat[stat.ST_INO]

        # About to print all the recors, first lock the file
        # Make sure lock is released even if an exception was raised
        fcntl.flock(self.stream, fcntl.LOCK_EX)
        try: 
            # Emit all the stored records
            for record in self.records:
                logging.FileHandler.emit(self, record)
               
        finally:
            fcntl.flock(self.stream, fcntl.LOCK_UN)
            self.records = []


class FlushLogger(logging.Logger):

    def __init__(self, name, level=logging.NOTSET):
        logging.Logger.__init__(self, name, level)
          
    def emitFlush(self):    
        for handler in self.handlers:
            if hasattr(handler, 'emitFlush'):
                handler.emitFlush()

    # --- logging functions -----------------------------------------------------------------------
    # Additional logging functions, for now mapped to the existing levels

    def notice(self, msg, *args, **kwargs):          
            self.log(logging.INFO, msg, *args, **kwargs);

    def debug2(self, msg, *args, **kwargs):          
            self.log(logging.DEBUG, msg, *args, **kwargs);

    def debug3(self, msg, *args, **kwargs):          
            self.log(logging.DEBUG, msg, *args, **kwargs);

    def debug4(self, msg, *args, **kwargs):          
            self.log(logging.DEBUG, msg, *args, **kwargs);

    def debug5(self, msg, *args, **kwargs):          
            self.log(logging.DEBUG, msg, *args, **kwargs);

    
    # --- _frameToStr -----------------------------------------------------------------------------
    # from gem
    def _frameToStr(self,frame):
        """ Helper function. Formats an inpect module stack frame as string. """
        s = "%s():%d at %s:%d" % ( frame[3], frame[2], frame[1], frame[2] )  # func, line, file, line
        return s

    # --- trace -----------------------------------------------------------------------------------
    # from gem
    def trace(self, msg=None, *args, **kwargs):
        """ Logs a stack trace with DEBUG level """

        # Log msg, if any  
        if msg:
            self.notice("Logger: stack trace: " + msg, *args, **kwargs)

        # Get stack frames
        frames = inspect.stack()

        # Dump all frames, skipping the first one (of this call)
        n=0
        for frame in frames[1:]:
            self.notice("Logger: stack trace: #%d: %s" % (n, self._frameToStr(frame) ) )
            n = n +1

    # --- here ------------------------------------------------------------------------------------
    # from gem
    def here(self, msg="", *args, **kwargs):
        """ Logs a the callet's location with DEBUG level """
         
        # Get stack frames 
        frames = inspect.stack()

        # Log caller location and msg.
        s = self._frameToStr(frames[1])   # frames[1] -> caller frame
        self.notice("Logger: HERE: " + s + " " + msg, *args, **kwargs)  # "keep" '%' for debug()


class ApiLogger(FlushLogger):
   def __init__(self, name, level=logging.NOTSET):
        FlushLogger.__init__(self, name, level)
        self.lineSeperator = "=" * 100

   def _getTime(self):
       s = time.strftime("%Y-%m-%d %H:%M:%S %Z")
       return s

   def logRequestStart(self):
       self.info(self.lineSeperator) 
       self.info("%s [%d] - REQUEST START", self._getTime(), os.getpid() )
       self.trace()

   def logRequestEnd(self):
       self.info("%s [%d] - REQUEST END", self._getTime(), os.getpid() )
       self.info(self.lineSeperator) 
       self.info("\n") 
       self.emitFlush()
       
def createLogger(LoggerClass, loggerName):
    """
    Creates logger of provided class and given name
    log level is extracted from the configuration parameters
    """
    import django.conf

    logLevelDictionary= { "debug"  : logging.DEBUG,
                          "info"   : logging.INFO,
                          "warning": logging.WARNING,
                          "error"  : logging.ERROR }
    logLevel = django.conf.settings.A_PARAMETERS.getMappedParameter("%s-log-level"%loggerName, logLevelDictionary, logging.WARNING)
    logger =  LoggerClass(loggerName, level=logLevel)

    formatter  = logging.Formatter('%(asctime)s [%(process)d] %(levelname)s %(module)s %(funcName)s():%(lineno)d - %(message)s')

    channel = LockedWatchedLoggerFileHandler( os.path.join(django.conf.settings.A_APPLICATION_ROOT_DIR, "logs", "%s.log" % loggerName) ) 
    channel.setLevel(logLevel)
    channel.setFormatter(formatter)
    logger.addHandler(channel)
    return logger

                   
    
# ==== NullLogger =====================================================================================================

class NullLogger:
    def error(self, *kwords):
        pass

    #def warn / warning(self, *kwords):
    #    pass

    def info(self, *kwords):
        pass

    def debug(self, *kwords):
        pass
    def debug2(self, *kwords):
        pass
    def debug3(self, *kwords):
        pass
    def debug4(self, *kwords):
        pass
    def debug5(self, *kwords):
        pass
    
                       
"""
def test(logger, flush=False):
    # 'application' code
    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')
    if flush:
        logger.emitFlush()

mainLogger, accessLogger, apiLogger) = createLoggers(".")
test(mainLogger)
test(accessLogger)
apiLogger.logRequestStart()
test(apiLogger, True)
apiLogger.logRequestEnd()

"""

########### Log Decorators ############################
def logStartData(logger):
    import django.conf
    logger.info( "+++ START DATA +++") 
    logger.info( "  os.getcwd()=%s" % os.getcwd() )
    logger.info( "  sys.path()=%s\n" % str(sys.path) )
    logger.info( "  sys.modules['django'].__file__=%s" % str(sys.modules['django'].__file__) );
    logger.info( "  ROOT_DIR=%s" % str( django.conf.settings.A_APPLICATION_ROOT_DIR) )
    logger.info( "  TEMPLATE_DIRS=%s" % str( django.conf.settings.TEMPLATE_DIRS) )
    for item in sorted( django.conf.settings.A_PARAMETERS.items(), key=lambda t: t[0]):
        logger.debug("  PARAMETERS: '%s' = '%s'" % (item[0], item[1]) )


    envKeys = os.environ.keys()
    envKeys.sort();
    for x in envKeys:
        logger.debug( "     os.environ: %-10s = '%s'" % (x , os.environ[x]) )

    logger.info( "+++ START DATA - END +++") 

def logRequest(logger, request, viewFunc):
    
    logger.info("-" * 80)
    logger.info("-" * 80)

    logger.info("REQUEST: function: %s.%s()" % ( viewFunc.__module__ , viewFunc.__name__ ) )
    logger.info("REQUEST: [%s] '%s'" % (request.method , request.get_full_path() ))
    logger.info("REQUEST: is_secure=%s  is_ajax=%s"   % ( request.is_secure(), request.is_ajax() ) )

    for item in sorted( request.GET.items(), key=lambda t: t[0]):
        logger.info("REQUEST: GET: '%s' = '%s'" % (item[0], item[1]) )

    for item in sorted( request.POST.items(), key=lambda t: t[0]):
        if item[0] == 'password':
            val = "X"*len(item[1])
        else:
            val = item[1]
        logger.info("REQUEST: POST: '%s' = '%s'" % (item[0], val) )

    for item in sorted( request.COOKIES.items(), key=lambda t: t[0]):
        logger.debug("REQUEST: COOKIES: '%s' = '%s'" % (item[0], item[1]) )

    for item in sorted( request.META.items(), key=lambda t: t[0]):
        logger.debug("REQUEST: META: '%s' = '%s'" % (item[0], item[1]) )

def logResponse(logger, response):
    
    logger.info("\n")
    logger.info("RESPONSE: status code: %s" , response.status_code)
    logger.info("RESPONSE: content length: %s" , str(response.tell()) if response._is_string else "iterable object" )
        
    for item in sorted( response.items() , key=lambda t: t[0]):
        logger.info("RESPONSE: header: '%s': '%s'" % (item[0], item[1]) )

def logContextVars(logger, contextVars):
    
    logger.debug("\n")
    logger.debug("CONTEXT: vars: %s" % ( pprint.pformat (contextVars) ) )




