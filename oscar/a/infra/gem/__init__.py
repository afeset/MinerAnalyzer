
import cfg as mCfg
import path as mPath
import logger as mLogger

# --- Globals -------------------------------------------------------------------------------------
mainLogger  = None
mainCfg     = None
mainExtraCfg = None

# --- logger --------------------------------------------------------------------------------------
def logger():

    """ 
    Returns Qwilt's main logger object. 
    On the first call the logger is created and set for stderr logging of notice and above. 
    Logger name is set to the program name.
    """

    global mainLogger

    # If logger does exist, create it
    if not mainLogger:
        mainLogger = mLogger._createLogger();

    # Return the logger
    return mainLogger

# --- cfg -------------------------------------------------------------------------------------
def cfg():

    """ 
    Returns Qwilt's main configuration object. 
    On the first call the object is created.
    """

    global mainCfg

    # If main cfg file does exist, create it
    if not mainCfg:
        mainCfg = mCfg.Cfg( logger() );

    # Return the logger
    return mainCfg

# --- extraCfg ------------------------------------------------------------------------------------
def extraCfg():
    """ 
    Returns extendedConfigParser object of the extra configuration in user & system config filse 
    or None if not exist.
    """

    return mainExtraCfg

# --- addOptparseOptions --------------------------------------------------------------------------
def addOptparseOptions(parser):
    """" Add submodules optparse options """

    logger().debug2("%s:addOptparseOptions() - called" % __name__ )
     
    mPath.addOptparseOptions(parser)
    mLogger.addOptparseOptions(parser)
    mCfg.addOptparseOptions(parser)

# --- readConfigFiles -----------------------------------------------------------------------------
def readConfigFiles():
    """ 
    Reads the user and system config file. Update configuration object and the sub modules.
    Additional file configulation is avaible with extraCfg()
    """   

    logger().debug2("%s:readConfigFiles() - called" % __name__ )

    global mainExtraCfg

    # Read config file, update config object and save the config file object
    mainExtraCfg = cfg().weakAddUserAndSysConfigFilesOptions()

    # Update all modules on cfg change
    updateCfg() 

# --- updateCfg -----------------------------------------------------------------------------------
def updateCfg():
    """" Updates all module on configulation changes. """

    c = cfg()
    logger().cfgLogger(c)

# --- updateCmdlineOptions ------------------------------------------------------------------------
def updateCmdlineOptions(optparseOptions):
    """ 
    Update the main configuration with the command line options object (from optparse). Then,
    updates the modules on the configulation changes.
    """  
   
    logger().debug2("%s:updateCmdlineOptions() - called" % __name__ )
       
    # Update cfg with command line options   
    cfg().weakAddOptparseOptions(optparseOptions) 
    
    # Update all modules on cfg change
    updateCfg() 

# --- updateAppEarlyCfg ---------------------------------------------------------------------------
def updateAppEarlyCfg(appEarly):
    """"
    Update the main configuration with the early application cfg. Then, updates the modules on 
    the configulation changes.
    """  

    logger().debug2("%s:updateAppEarlyCfg() - called" % __name__ )
   
    # Update cfg with command line options   
    cfg().weakAdd(appEarly, source="updateAppEarlyCfg") 
    
    # Update all modules on cfg change
    updateCfg() 



# --- updateAppCfgDefaults ------------------------------------------------------------------------
def updateAppCfgDefaults(appCfgDefaults):
    """"
    Update the main configuration with the application defaults. Then, updates the modules on 
    the configulation changes.
    """  

    logger().debug2("%s:updateAppCfgDefaults() - called" % __name__ )
   
    # Update cfg with command line options   
    cfg().weakAdd(appCfgDefaults, source="updateAppCfgDefaults") 
    
    # Update all modules on cfg change
    updateCfg() 

# --- updateInternalCfgDefaults -------------------------------------------------------------------
def updateInternalCfgDefaults():
    """"
    Update the main configuration with the internal defaults. Then, updates the modules on 
    the configulation changes.
    """  

    logger().debug2("%s:updateInternalCfgDefaults() - called" % __name__ )
   
    logger().weakAddCfgDefaults( cfg() )
    
    # Update all modules on cfg change
    updateCfg() 

# --- notifyCfgDone -------------------------------------------------------------------------------
def notifyCfgDone():
    """ 
    The application calls this function to notify configuration is done and infra will take
    the post configuration actions
    """

    logger().debug("%s:notifyCfgDone() - called" % __name__ )

    mPath.notifyCfgDone( cfg(), logger() )
    cfg().notifyCfgDone( extraCfg() )
    logger().notifyCfgDone( cfg() )
