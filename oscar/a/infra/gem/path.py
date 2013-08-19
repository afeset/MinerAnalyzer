import os, sys
import inspect 

QWILT="qwilt"
VAR_DIR="/var"   # Until I will found something batter

_homeDir = os.path.expanduser("~")

_cfgDirUser=os.path.join(_homeDir, QWILT, "cfg")
_logDirUser=os.path.join(_homeDir, QWILT, "log")
_logDirSys =os.path.join(VAR_DIR,  QWILT, "log")
       
logFilenameTemplate="%(prog)s.log"  
cfgFilenameTemplate="%(prog)s.cfg"
       
_progAbsPath=None       
       
# ==== Helper functions ===========================================================================       
       
# === prog paths =================================================================================    
           
# --- progPath ------------------------------------------------------------------------------------
def progPath():
    """ Returns the program's real path. Real path means, all softlinks are dereferenced """
    absPath = progAbsPath()
    path=os.path.realpath (absPath)
    return path 

# --- progAbsPath ---------------------------------------------------------------------------------
def progAbsPath():
    """ Returns the program's absolute path. """
    global _progAbsPath;
    
    # If first call, calc the path
    if not _progAbsPath:
        relPath = inspect.stack()[-1][1]  # Use the last stack frame data
        _progAbsPath = os.path.abspath( relPath )
  
    return _progAbsPath 


# --- progName ------------------------------------------------------------------------------------
def progName():
    """ Returns the program real name (slinks are resolved) """
    path = progPath()
    basename = os.path.basename(path)
    (name,ext) = os.path.splitext(basename)
    return name

# --- progInvocationName --------------------------------------------------------------------------
def progInvocationName():
    """ Returns the program invocation name (slinks are not resolved) """
    basename = os.path.basename(sys.argv[0])
    (name,ext) = os.path.splitext(basename)
    return name


# --- progIsSlink ---------------------------------------------------------------------------------
def progIsSlink():
    """ Returns True if program was invoked using slink """

    # progName != invocation name -> soft line
    isSlink = ( progName() != progInvocationName() )
    return isSlink



# === user path's =================================================================================

# --- logDirUser ----------------------------------------------------------------------------------
def logDirUser ():
    """ 
    Returns the default user log dir. 
    """
    global _logDirUser
    dir=_logDirUser;
    return dir

# --- logFileUser ---------------------------------------------------------------------------------
def logFileUser():
    """ 
    Returns the user default log file name. 
    """
    dir = logDirUser()
    fname=os.path.join( dir, logFilenameTemplate % { 'prog': progName() } )
    return fname

# --- cfgDirUser ----------------------------------------------------------------------------------
def cfgDirUser():
    """ Returns the user cfg dir """
    global _cfgDirUser
    dir=_cfgDirUser;
    return dir

# --- cfgFileUser ---------------------------------------------------------------------------------
def cfgFileUser():
    """ Returns the user cfg file name. """
    dir=cfgDirUser();
    fname=os.path.join( dir, cfgFilenameTemplate % { 'prog': progName() } )
    return fname

# === sys paths ===================================================================================
 
# --- logDirSys -----------------------------------------------------------------------------------
def logDirSys ():
    """ 
    Returns the default system log dir. 
    """
    global _logDirSys
    dir=_logDirSys;
    return dir

# --- logFileSys ----------------------------------------------------------------------------------
def logFileSys(createDir=False):
    """ 
    Returns the default system log file name. 
    """
    dir = logDirSys()
    fname=os.path.join( dir, logFilenameTemplate % { 'prog': progName() } )
    return fname

# --- cfgDirSys -----------------------------------------------------------------------------------
def cfgDirSys():
    """ Returns the system cfg dir """
    (h,t) = os.path.split( progPath() );
    return h

# --- cfgFileSys ----------------------------------------------------------------------------------
def cfgFileSys():
    """ Returns the system cfg file name """
    dir = cfgDirSys()
    fname=os.path.join( dir, cfgFilenameTemplate % { 'prog': progName() } )
    return fname

# === misc ========================================================================================


# --- addOptparseOptions --------------------------------------------------------------------------
def addOptparseOptions(parser):
    """ Creates optparse OptionGroup for the logger options and adds them to the parser """

    import optparse
 
    # Create the options group
    group = optparse.OptionGroup(parser, "Path options")
    parser.add_option_group(group)

    # Add the logger options
    ### NOTE: All destinations should begin with 'log_'

    group.add_option("--dump-path",
                      action="store_true", dest="path_dump",
                      help="Dump program paths & names")

# --- notifyCfgDone ---------------------------------------------------------------------------
def notifyCfgDone(cfg, logger):
    """
    Called when configuration is done. The following takes place:
       - The configuration is examined and program paths are shown
    """

    # Check self dump
    if cfg.get( 'path_dump' ):
        showPaths(logger)
 


# --- showPaths -----------------------------------------------------------------------------------
def showPaths(logger):
    
    w = 21;
    logger.notice("path: %-*s %s" % ( w, "progName():",           progName()           ) );
    logger.notice("path: %-*s %s" % ( w, "progInvocationName():", progInvocationName() ) );
    logger.notice("path:");
    
    logger.notice("path: %-*s %s" % ( w, "progPath():"   , progPath()    ) );
    logger.notice("path: %-*s %s" % ( w, "progAbsPath():", progAbsPath() ) );
    logger.notice("path:");
   
    logger.notice("path: %-*s %s" % ( w, "logFileUser():", logFileUser() ) );
    logger.notice("path: %-*s %s" % ( w, "logFileSys():" , logFileSys()  ) );
    logger.notice("path:");  

    logger.notice("path: %-*s %s" % ( w, "cfgFileUser():", cfgFileUser() ) );
    logger.notice("path: %-*s %s" % ( w, "cfgFileSys():" , cfgFileSys()  ) );
 

