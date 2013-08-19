import path
#import qwilt
import logger as mLogger
import extendedConfigParser



# === Globals =====================================================================================

NO_KEY_PREFIX="no_"
MAIN_CFG_SECTION_DEFAULT="main-cfg"
USER_CFG_FILE_CFG_OPTION="cfg_user_file"
SYS_CFG_FILE_CFG_OPTION="cfg_sys_file"

# === Cfg =========================================================================================
class Cfg:
     
    # --- __init__ --------------------------------------------------------------------------------
    def __init__(self, logger, newValues = {}, source = "ctor"):

        # Use the specified logger
        self.logger = logger                 
       
        # Holds the configuration dictionary
        self.values = {}

        # A list of keys that have 'no' value
        self.noValues = []

        # Holds the source for both values and noValues
        self.source = {}

        # Set the initial cfg
        self.weakAdd(newValues, source)  

    # --- get -------------------------------------------------------------------------------------
    def get(self, key, default=None):
        """ 
        Returns:
           key has value -> key's value.
           key has 'no' value -> None
           key does not exist -> default arg. Note default parameter default is None
        """
       
        # Key has value?
        if self.hasValue(key):
            return self.values[key]

        # Key has 'no' value?
        if self.hasNoValue(key):
            return None
        
        # Key does not exist
        return default

    # --- hasValue --------------------------------------------------------------------------------
    def hasValue(self, key):
        """ Returns True if key has a value """
        return key in self.values

    # --- hasNoValue ------------------------------------------------------------------------------
    def hasNoValue(self, key):
        """ Returns True if key has no value """
        return key in self.noValues

    # --- keys ------------------------------------------------------------------------------------
    def keys(self):
        """ Returns a list of existing keys """
        return self.values.keys() 

    # --- noValueKeys -----------------------------------------------------------------------------
    def noValueKeys(self):
        """ Returns a list of existing keys which has been set to 'no' value """
        return self.noValues[:]

    # --- weakAdd ---------------------------------------------------------------------------------
    def weakAdd(self, newValues, source='unknown'):
       """ 
       Adds values dictonary to the configuration. 
       Addition is weak. If a new key already exists, the current value will hold and the new value
       will be discarded.
       A key begining with 'no_' (regardless of its value) has priority over the std key. 
       'no_' keys are kept and will prevent setting a value to this key in the future.
       'source' is an optional paramter used with the debug logs
       """
   
       self.logger.debug2("Cfg: weakAdd(): adding options. source=%s  newValues=%s" % ( source, newValues) )

       # Build a list of unique keys by removing any key that have 'no' key as well
       ukeys = []
       for k in newValues.keys():

           # Chop the 'no' prefix, if any
           basek = _baseKey(k)
           
           # If 'std' key has also 'no' key, don't add it
           if (k == basek) and ( _makeNoKey(k) in newValues ):
                # Yes, log it (and don't add it to the list)
                self.logger.debug3("Cfg: 'no' key exists in new values -> ignoring 'std' key. " \
                                     "key=%s  val=%s  src=%s" % (k, newValues[k], source ) )
           else:
                # No, save the key
                ukeys.append(k)

       # Scan the unique keys and add them, unless alreay exist
       for k in ukeys:

           # Chop the 'no' prefix, if any
           basek = _baseKey(k)
           
           # Skip if key already has a value
           if basek in self.values:
               # Value exists -> skip it
               self.logger.debug3("Cfg: key already has value -> ignored. " \
                                    "key=%s  existingKey=%s  existingVal=%s  source=%s" 
                                     % ( k, basek, self.values[basek], source ) )
               continue
  
           # Skip key if it has 'no' value
           if basek in self.noValues: 
               # 'no' key Exists -> skip it
               self.logger.debug3("Cfg: key already marked 'no' key -> ignored. " \
                                    "key=%s  existingKey=%s  source=%s"
                                     % ( k, basek, source ) )
               continue
               
           # Add the key depending on its kind
           if ( k == basek ):
               # 'std' key, add it to values
               v = newValues[k]
               self.values[basek] = v
               self.source[basek] = source
               self.logger.debug3("Cfg: adding value. " \
                                    "key=%s  val=%s  source=%s" % ( k, v, source ) )
           else:
               # 'no' value, add it to 'no' values list
               self.noValues.append(basek)
               self.source[basek] = source
               self.logger.debug3("Cfg: adding 'no' key. key=%s  source=%s" % ( k, source ) )

       # Print debug info     
       self.logger.debug3("Cfg: Values after adding:  source=%s  values=%s" % ( source, self.values) )
       self.logger.debug3("Cfg: 'no' values after adding:  source=%s  noKeys=%s" % ( source, self.noValues) )
         
    # --- weakAddOptparseOptions ------------------------------------------------------------------
    def weakAddOptparseOptions(self, options, source="optparse"):
        """ Converts optparse option object to dictionary and pass it to weakAdd() """
        
        # If options is None -> NOP
        if options is None:           
            self.logger.debug2("Cfg: weakAddOptparseOptions(): options is None -> NOP. source=%s" % ( source) )
            return

        # Loop all options and build dictionary from them
        values = {}
        for option in vars(options):            

            # Get option value
            value = getattr(options, option)
            
            # Skip None options because parseopt set them with no reason
            if value is None:
                continue
            
            # Add value to dictionary        
            values[option] = value;

        # Add options
        self.weakAdd(values,source)          

    # --- weakAddConfigFileOptions ----------------------------------------------------------------
    def weakAddConfigFileOptions(self, file, section=None, source=None):
        """ 
        Reads a config file using ExtendedConfigParser and 'weakAdd' all options in 'section'
        (if exists) into this configuration object.
        Returns the ExtendedConfigParser object or None if failed to read the file.
        'section' default is 'main-cfg'. 
        The configuration section is removed from returned object.
        weakAdd() source is the file name & section name unless 'source' is specified.
        If 'file' is None (or empty), do nothing
        """

        # First, if file is None -> NOP
        if not file:
            self.logger.debug("Cfg: weakAddConfigFileOptions() file is None -> NOP")
            return None

        # Create the cfgFile object
        cfgFile = extendedConfigParser.ExtendedConfigParser(logger=self.logger)

        # Read the file & check read something
        readFileList = cfgFile.read(file)
        if len(readFileList) != 1 :
            self.logger.debug("Cfg: weakAddConfigFileOptions(), failed to read file. file=%s" % file)
            return None
        
        # Default section?
        if not section:
            section = MAIN_CFG_SECTION_DEFAULT
        
        # log it
        self.logger.info("Cfg: Read configuration file. file=%s  section=%s" % (file, section) )

        # Check section exists. If not, we are done
        if not cfgFile.has_section(section):
            self.logger.debug("Cfg: weakAddConfigFileOptions(), section does not exists->NOP. file=%s  section=%s"
                          % ( file, section ) )
            return cfgFile

        # Get all options from 'section' add build dictionary from them
        values = {}
        for option in cfgFile.options(section):

            # Get option value
            value = cfgFile.get(section, option)
            
            # Skip None options (just in case)
            if value is None:
                continue
            
            # Add value to dictionary        
            values[option] = value;

        # If source is empty, use file name
        if not source:
            source = "%s[%s]" % (file,section)

        # Add options
        self.weakAdd(values, source) 
        
        # Remove configuration section from cfgFile
        cfgFile.remove_section(section)   

        # Return config file object
        return cfgFile
                 
    # --- weakAddConfigFileOptionsWithCfgOption ---------------------------------------------------    
    def weakAddConfigFileOptionsWithCfgOption(self, cfgOption, defaultFile, section=None):
        """
        Check 'cfgOption':
             - If it has value, that value is used as configuration file name
             - If it has 'no' value, returns None
             - If it does not exists, defaultFile is used and 'cfgOption' is set to 'defaultFile'
        Once file name is calculated, weakAddConfigFileOptions() is called to do the real work.
        """
        
        # Check 'no' value
        if self.hasNoValue(cfgOption) :
            self.logger.debug("Cfg: skipping configuration read due to 'no' value file name. cfgOption=%s"
                              % cfgOption)
            return None
        
        # Check cfgOption has value
        if self.hasValue(cfgOption):
             # Has value, use it
             file = self.get(cfgOption)
        else:
             # option does not exist, use default and set it
             file = defaultFile
             self.weakAdd( { cfgOption:file}, "Cfg-default-filename")
       
        # Do the real work
        return self.weakAddConfigFileOptions(file, section)

    # --- weakAddUserConfigFileOptions ------------------------------------------------------------
    def weakAddUserConfigFileOptions(self, section=None):
       """"
       Reads a user config file option from section 'main-cfg' by default.
       File name is taken from 'cfg_user_file' config option. 
       If the option does not exist, the file name is defined by path.cfgFileUser() and the 
       configuration option is set.
       If the option is set to 'no' value the file is not read.
       Function returns a ExtendedConfigParser object (or None)
       """
       
       # Get default file name
       defaultFile = path.cfgFileUser();
       
       # Do it
       return self.weakAddConfigFileOptionsWithCfgOption( USER_CFG_FILE_CFG_OPTION, defaultFile, section )
       
    # --- weakAddSysConfigFileOptions ------------------------------------------------------------
    def weakAddSysConfigFileOptions(self, section=None):
       """"
       Reads a user config file option from section 'main-cfg' by default.
       File name is taken from 'cfg_sys_file' config option. 
       If the option does not exist, the file name is defined by path.cfgFileSys() and the 
       configuration option is set.
       If the option is set to 'no' value the file is not read.
       Function returns a ExtendedConfigParser object (or None)
       """
       
       # Get default file name
       defaultFile = path.cfgFileSys();
       
       # Do it
       return self.weakAddConfigFileOptionsWithCfgOption( SYS_CFG_FILE_CFG_OPTION, defaultFile, section )

    # --- weakAddUserAndSysConfigFilesOptions ------------------------------------------------------------
    def weakAddUserAndSysConfigFilesOptions(self, section=None):
        """"
        Reads the user and system config files using weakAddUserConfigFileOptions() and 
        weakAddUserConfigFileOptions().
        Function returns a ExtendedConfigParser object which contains the parsed user and system config
        files. User options has priority over system options.
        Return None if nothing was found.
        """

        # Read user's configuration file and update cfg object
        userCfgFile = self.weakAddUserConfigFileOptions(section)
            
        # Read system's configuration file and update cfg object
        sysCfgFile = self.weakAddSysConfigFileOptions(section)
    
        # Merge files user and system config files objects.
        # Begin with user file object
        cfgFile = userCfgFile
        
        # Merge system file
        # If current file object is exists, add to it system file object. Other wish, use the system object
        if cfgFile:
            cfgFile.weakAddConfigParser(sysCfgFile)
        else:
            cfgFile = sysCfgFile

        # Done, return merged cfgFile
        return cfgFile
    
    # --- dump ------------------------------------------------------------------------------------
    def dump(self, name=None, otherLogger=None):
        """ Dumps the configuration to the logger """

        # Log header
        if not name:
            name = __name__ + " object"
        self.logger.notice("%s content dump:" % name)
     
        # Get value and 'no' values keys    
        allKeys = self.keys()
        allKeys.extend(self.noValueKeys() )

        # Loop all keys 
        for key in sorted(allKeys):

            # Calc the value string
            if self.hasNoValue(key):
                 s = "NO %s" % (key)
            else:
                 s = "%s=%s" % ( key, self.get(key) )

            # print it
            msg="    %-30s  # %s"  %  (s, self.source[key])
            self.logger.notice(msg)
            if otherLogger != None:
                otherLogger.info(msg)


    # --- notifyCfgDone ---------------------------------------------------------------------------
    def notifyCfgDone(self, cfgFile):
        """
        Called when configuration is done. The following takes place:
           - The configuration is examined and this object and cfgFile object configurations are 
             dumpped if required
        """
    
        # Check self dump
        if self.get( 'cfg_dump' ):
            self.dump("notifyCfgDone() configuration object")
    
        # Check cfgFile dump raw
        if self.get( 'cfg_file_dump_raw' ) and cfgFile:
            cfgFile.dump("notifyCfgDone() raw configuration file", raw=True)
        
        # Check cfgFile dump
        if self.get( 'cfg_file_dump' ) and cfgFile:
            cfgFile.dump("notifyCfgDone() configuration file", raw=False)

        


# === Helper functions ============================================================================
  
# --- _makeNoKey ----------------------------------------------------------------------------------
def _makeNoKey(key):
    """ returns a 'no' key for a standard key """
    return  NO_KEY_PREFIX + key

# --- _baseKey ------------------------------------------------------------------------------------
def _baseKey(key):
    """ Return for 'no' key return the base of it. Otherwise returns the original key """

    # Get 'no' prefix length
    no_len = len(NO_KEY_PREFIX)
        
    # Return for 'no' key return the base of it
    if key[:no_len] == NO_KEY_PREFIX:
         return key[no_len:]

    # 'standard' key, return the original  
    return key

# === optparse ====================================================================================

# --- addOptparseOptions --------------------------------------------------------------------------
def addOptparseOptions(parser):
    """ Creates optparse OptionGroup for the config options and adds them to the parser """

    import optparse
 
    # Create the options group
    group = optparse.OptionGroup(parser, "Configuration options")
    parser.add_option_group(group)

    # Add the cfg options
    ### NOTE: All destinations should begin with 'cfg_'

    group.add_option("-C", "--user-cfg-file",
                      action="store", dest="cfg_user_file", type="string",
                      help="Sets the user's configuration file name")

    group.add_option("--no-user-cfg-file",
                      action="store_true", dest="no_cfg_user_file",
                      help="Disables user's configuration file reading")

    group.add_option("--sys-cfg-file",
                      action="store", dest="cfg_sys_file", type="string",
                      help="Sets the system's configuration file name")

    group.add_option("--no-sys-cfg-file",
                      action="store_true", dest="no_cfg_sys_file",
                      help="Disables system's configuration file reading")

    group.add_option("--dump-cfg",
                      action="store_true", dest="cfg_dump",
                      help="Dump the configuration")

    group.add_option("--dump-cfg-file",
                      action="store_true", dest="cfg_file_dump",
                      help="Dump the configuration file object")

    group.add_option("--dump-cfg-file-raw",
                      action="store_true", dest="cfg_file_dump_raw",
                      help="Dump the configuration file object in raw format")

