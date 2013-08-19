import sys
import logging, logging.handlers
from logging import *  # Import everything since we extends it
import path

import os, socket, pwd, grp, datetime, time  # mainly for env logging
import inspect # for trace & here functions

# === Globals =====================================================================================

# Additional  loglevels
NOTICE=logging.INFO  + 5;
DEBUG2=logging.DEBUG - 2;
DEBUG3=logging.DEBUG - 3;
DEBUG4=logging.DEBUG - 4;
DEBUG5=logging.DEBUG - 5;

# Stderr channel contants & defaults
STDERR_LOGLEVEL_DEFAULT = NOTICE
STDERR_LOGLEVEL_QUIET   = ERROR

# File channel constands & defaults
FILE_LOGLEVEL_DEFAULT      = INFO
FILE_CH_MAX_SIZE_DEFAULT   = 64 * 1024
FILE_CH_MAX_FILES_DEFAULT  = 3



FORMAT_DEFAULT      = "%(asctime)s.%(msecs)03d %(name)s[%(process)d] %(levelname)s: %(message)s"
FORMAT_DATE_DEFAULT = "%Y%m%d %H%M%S"  # - see time.strftime


# === Logger ======================================================================================

class Logger(logging.Logger):
    """
    Deriving from logging.Logger, add Qwilt specific features:
        - .debug2() to debug5() for multiple verbose levels
        - TBD
    """      
     
    # --- __init__ --------------------------------------------------------------------------------
    def __init__(self, name, level=logging.NOTSET):

        # Channels        
        self.file_ch   = None
        self.stderr_ch = None

        # Log level
        self.file_loglevel   = FILE_LOGLEVEL_DEFAULT
        self.stderr_loglevel = STDERR_LOGLEVEL_DEFAULT
        
        # Log formats
        self.file_format        = FORMAT_DEFAULT
        self.stderr_format      = FORMAT_DEFAULT
        self.file_date_format   = FORMAT_DATE_DEFAULT
        self.stderr_date_format = FORMAT_DATE_DEFAULT

        # File channel parameters
        self.file_ch_filename   = None
        self.file_ch_max_size   = FILE_CH_MAX_SIZE_DEFAULT
        self.file_ch_max_files  = FILE_CH_MAX_FILES_DEFAULT

            
        # Create the original logger
        logging.Logger.__init__(self, name, level)

        # Add debug level
        logging.addLevelName(NOTICE, "NOTICE")
        logging.addLevelName(DEBUG2, "DEBUG2")
        logging.addLevelName(DEBUG3, "DEBUG3")
        logging.addLevelName(DEBUG4, "DEBUG4")
        logging.addLevelName(DEBUG5, "DEBUG5")

    # --- logging functions -----------------------------------------------------------------------
    # Additional logging functions

    def notice(self, msg, *args, **kwargs):          
            self.log(NOTICE, msg, *args, **kwargs);

    def debug2(self, msg, *args, **kwargs):          
            self.log(DEBUG2, msg, *args, **kwargs);

    def debug3(self, msg, *args, **kwargs):          
            self.log(DEBUG3, msg, *args, **kwargs);

    def debug4(self, msg, *args, **kwargs):          
            self.log(DEBUG4, msg, *args, **kwargs);

    def debug5(self, msg, *args, **kwargs):          
            self.log(DEBUG5, msg, *args, **kwargs);
    
    # --- _frameToStr -----------------------------------------------------------------------------
    def _frameToStr(self,frame):
        """ Helper function. Formats an inpect module stack frame as string. """
        s = "%s():%d at %s:%d" % ( frame[3], frame[2], frame[1], frame[2] )  # func, line, file, line
        return s

    # --- trace -----------------------------------------------------------------------------------
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
    def here(self, msg="", *args, **kwargs):
        """ Logs a the callet's location with DEBUG level """
         
        # Get stack frames 
        frames = inspect.stack()

        # Log caller location and msg.
        s = self._frameToStr(frames[1])   # frames[1] -> caller frame
        self.notice("Logger: HERE: " + s + " " + msg, *args, **kwargs)  # "keep" '%' for debug()

    # --- cfgLogger -------------------------------------------------------------------------------
    def cfgLogger(self, cfg):
        """ 
        Configure the logger using 'cfg' dictionary. If a parameters is not set, no action is taken.
        """

        # Config log levels
        self.cfgLoggingLevels( cfg )

        # Config file channel
        self.cfgFileChannel( cfg )
         
    # --- cfgLoggingLevels ------------------------------------------------------------------------
    def cfgLoggingLevels(self, cfg):
        """ 
        Configures logging levels - saves logging levels and applies it to existsing channels 
        The following parameters are referenced:
            log_verbose - Sets the logging level. 0: default, 1: info, 2: debug, 3:debug2, ...
            log_quiet   - Log only errors and above to stderr. Does not affect file logging
        """
               
        
        # Get configuration values
        verbose  = cfg.get("log_verbose")
        quiet    = cfg.get("log_quiet")
        
        # If verbose was set, translate verbose value to log levels. Otherwise keep current levels
        if   verbose is None:
            # Not set, keep current levels
            new_file_loglevel   = self.file_loglevel  
            new_stderr_loglevel = self.stderr_loglevel
        elif verbose == 1:
            new_file_loglevel   = new_stderr_loglevel = INFO
        elif verbose == 2:
            new_file_loglevel   = new_stderr_loglevel = DEBUG
        elif verbose == 3:
            new_file_loglevel   = new_stderr_loglevel = DEBUG2
        elif verbose == 4:
            new_file_loglevel   = new_stderr_loglevel = DEBUG3
        elif verbose == 5:
            new_file_loglevel   = new_stderr_loglevel = DEBUG4
        elif verbose >= 6:
            new_file_loglevel   = new_stderr_loglevel = DEBUG5
        else:  # revert to default
            new_file_loglevel   = FILE_LOGLEVEL_DEFAULT
            new_stderr_loglevel = STDERR_LOGLEVEL_DEFAULT
      
        # If quiet -> force stderr channel to quite
        if quiet:
            new_stderr_loglevel = STDERR_LOGLEVEL_QUIET

        # Was stderr log level changed?
        if new_stderr_loglevel != self.stderr_loglevel:

            # Yes, save it
            self.stderr_loglevel = new_stderr_loglevel

            # Update the channel, if exists
            if self.stderr_ch:
                self.stderr_ch.setLevel(self.stderr_loglevel)
            
            # Log it
            self.debug2("Logger: stderr channel loglevel is %s" % logging.getLevelName(self.stderr_loglevel) )

        # Was file log level changed?
        if new_file_loglevel != self.file_loglevel:

            # Yes, save it
            self.file_loglevel = new_file_loglevel

            # Update the channel, if exists
            if self.file_ch:
                self.file_ch.setLevel(self.file_loglevel)
            
            # Log it
            self.debug2("Logger: file channel loglevel is %s" % logging.getLevelName(self.file_loglevel) )


    # --- cfgFileChannel -------------------------------------------------------------------------
    def cfgFileChannel(self, cfg):
        """ 
        Configures file channel parameters. Up on change recreate the channel
        The following parameters are referenced:
            log_file    - Creates a log file handler with logging level is info. If file logging 
                          is already set, the current log file is closed first.
                          set to 'no' value to disable file logging
            log_file_max_size  - Log file max size in bytes. Zero=unlimitted
            log_file_max_files - Log file max backup files count. Zero=none
        """
                
        # Get configuration values, if set. Otherwise keep their currenet value
        new_filename  = cfg.get("log_file",           self.file_ch_filename)
        new_max_size  = cfg.get("log_file_max_size",  self.file_ch_max_size)
        new_max_files = cfg.get("log_file_max_files", self.file_ch_max_files)
                                           
        # If there are no changes, we are done
        if ( (self.file_ch_filename  == new_filename) and
             (self.file_ch_max_size  == new_max_size) and
             (self.file_ch_max_files == new_max_files) ) :         
           # No changes -> NOP
            return

        # Changes, remove old file channel first (if exists)
        if self.file_ch:
            self.debug2("Logger: closing current file channel: %s" %  self.file_ch_filename )
            self.removeHandler(self.file_ch)
            self.file_ch = None

        # Save the new params
        self.file_ch_filename  = new_filename
        self.file_ch_max_size  = new_max_size
        self.file_ch_max_files = new_max_files

        # If file name is None, no file logging -> done
        if self.file_ch_filename is None:
            self.debug2("Logger: file channel logging is disabled");
            return

        # Create the log file dir, if required
        createDirIfRequired(os.path.dirname(self.file_ch_filename))

        # Create new file channel and set its level
        self.file_ch = logging.handlers.RotatingFileHandler(self.file_ch_filename,
                                                           'a',
                                                            self.file_ch_max_size,
                                                            self.file_ch_max_files)
        self.file_ch.setLevel(self.file_loglevel)
        
        # Create formatter and and it to channel
        formatter = logging.Formatter(self.file_format, self.file_date_format)
        self.file_ch.setFormatter(formatter)
        
        # add ch to logger
        self.addHandler(self.file_ch)

        self.debug2("Logger: file channel with level %s created at: %s " %  
                              ( logging.getLevelName(self.file_loglevel), 
                                self.file_ch_filename ) )
        self.debug2("Logger: Max log file size is %d. Max log file backups count is %d " % 
                     (self.file_ch_max_size, self.file_ch_max_files) )

    # --- weakAddCfgDefaults ----------------------------------------------------------------------
    def weakAddCfgDefaults(self, cfg):
        """ Add logger default options to cfg object """

        # Build default dictionary  
        opts = {
            'log_file'           : path.logFileUser(),
            'log_file_max_size'  : FILE_CH_MAX_SIZE_DEFAULT,
            'log_file_max_files' : FILE_CH_MAX_FILES_DEFAULT
        }
        
        # Add defaults to cfg 
        cfg.weakAdd(opts, source="logger-default") 
         

    # --- notifyCfgDone ---------------------------------------------------------------------------
    def notifyCfgDone(self, cfg):
        """
        Called when configuration is done. unless 'log_env' has 'no; value, log some env data.
        """
    
        # Check log env not disabled
        if not cfg.hasNoValue( 'log_env' ):
            self.logEnv()  

    # --- logEnv ----------------------------------------------------------------------------------
    def logEnv(self, header=None):
        """ Collecte and log various enviroment info such as hostname, argumnets """
    
        if header:
            self.debug("Logger-env: prog=%s header='%s'" % (path.progName(), header)  )
             
        self.debug("Logger-env: progPath=%s"     % path.progPath()  )
        self.debug("Logger-env: progAbsPath=%s"  % path.progAbsPath()  )
        self.debug("Logger-env: date=%s"         % time.asctime()    )
        self.debug("Logger-env: argv=%s"         % str(sys.argv)     )
        self.debug("Logger-env: cwd=%s"          % str(os.getcwd())  )
      
        uid = os.getuid()    ;  euid = os.geteuid()
        gid = os.getgid()    ;  egid = os.getegid() 
        self.debug("Logger-env: uid=%s(%d) euid=%s(%d) guid=%s(%d) egid=%s(%d)" % 
                    ( pwd.getpwuid(uid)[0], uid, pwd.getpwuid(euid)[0], euid,
                      grp.getgrgid(gid)[0], gid, grp.getgrgid(egid)[0], egid ) )
                        
        self.debug("Logger-env: pid=%d  ppid=%d  pgpid=%d"  % ( os.getpid(), os.getppid(), os.getpgrp() ) )
        self.debug("Logger-env: hostname=%s  uname=%s"      % ( socket.gethostname(), str(os.uname())   ) )
      
        self.debug("Logger-env: pythonVersion=%s" % sys.version.replace("\n","")  )
        self.debug("Logger-env: pythonPath=%s"    % str(sys.path)  )

        # Additonal info at lower lever
        for v in sorted(os.environ.keys()):
            self.debug("Logger-env:     os.environ[%s]=%s"  % (v, os.environ[v]) )
            
# === Misc functions ==============================================================================          

# --- _createLogger -------------------------------------------------------------------------------
def _createLogger():
          
    """ 
    Creates and returns Qwilt logger object. The new logger is set for stderr logging of warnings
    and above.
    Logger name is set to the program name.
    """

    # Get progam name 
    name   = path.progName();

    # Create the logger 
    logger = Logger(name)

    # Create stderr stream handler and set its level to warning. 
    logger.stderr_ch = logging.StreamHandler(sys.stderr)
    logger.stderr_ch.setLevel(logger.stderr_loglevel)

    # Create formatter
    formatter = Formatter(logger.stderr_format, logger.stderr_date_format)

    # add formatter to ch
    logger.stderr_ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(logger.stderr_ch)
  
    # return the logger
    return logger
    
# --- createDirIfRequired -------------------------------------------------------------------------
def createDirIfRequired(dir):
    """ 
    Creates the directory unless it is already exists. 
    All required parent directories are creates as well
    """

    # If dir is empty -> NOP
    if not dir:
        return

    # If already existing directory -> NOP
    if os.path.isdir(dir):
        return;
   
    # Does not exist (or nor a dir) -> Create it (and its parents too)
    os.makedirs(dir)        


# === optparse ====================================================================================

# --- addOptparseOptions --------------------------------------------------------------------------
def addOptparseOptions(parser):
    """ Creates optparse OptionGroup for the logger options and adds them to the parser """

    import optparse
 
    # Create the options group
    group = optparse.OptionGroup(parser, "Logger options")
    parser.add_option_group(group)

    # Add the logger options
    ### NOTE: All destinations should begin with 'log_'
    group.add_option("-v", "--verbose",
                      action="count", dest="log_verbose",
                      help="Set verbose level. Repeat to increase details of messages")

    group.add_option("--no-verbose",
                      action="store_const", dest="log_verbose", const=0,
                      help="Disable verbose (useful to override config options)")

    group.add_option("--quiet",
                      action="store_true", dest="log_quiet",
                      help="Log only errors and above to stderr. Does not affect file logging")

    group.add_option("--log-file",
                      action="store", dest="log_file", type="string",
                      help="Log file name")

    group.add_option("--no-log-file",
                      action="store_true", dest="no_log_file",
                      help="Disable logging to file")

    group.add_option("--log-file-max-size",
                      action="store", dest="log_file_max_size", type="int",
                      help="Log file max size in bytes. Zero=unlimitted")

    group.add_option("--log-file-max-files",
                      action="store", dest="log_file_max_files", type="int",
                      help="Log file max backup files count. Zero=none")

    group.add_option("--no-log-env",
                      action="store_true", dest="no_log_env",
                      help="Disable environment data logging at the beginning")


