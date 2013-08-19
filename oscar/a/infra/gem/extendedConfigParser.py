
from ConfigParser import *

# === Constants ===================================================================================
EXTENDS_OPTION_DEFAULT = "Extends"
FLATTEN_MAX_ITERATIONS = 15

# === ExtendedConfigParser ========================================================================

class ExtendedConfigParser( SafeConfigParser ):
    
    # --- __init__ --------------------------------------------------------------------------------
    def __init__(self, logger, defaults=None):

        # Use the specified logger
        self.logger = logger

        # Init vars
        self.flattenOk  = []
        self.flattenErr = []

        # Call the parent init function
        SafeConfigParser.__init__(self, defaults)

    # --- chopQuotes ------------------------------------------------------------------------------
    def chopQuotes(self, s, keepQuotes=False):
        """ 
        chops surrounding quotes (single or double) of 's', if any. Returns the result.
        if keepQuotes is True, return 's' is returned as is.
        """
     
        # Some reasons to keep the value as is
        if keepQuotes or not isinstance(s,str) or (len(s) < 2):
            return s

        # Check for quotes
        if ( ( s[0] == "\"" and s[-1] == "\"") or 
             ( s[0] == "'"  and s[-1] == "'" ) ):
            # Quoted, chop first and last chars
            return s[1:-1]

        # Not matched
        return s       

    # --- get -------------------------------------------------------------------------------------
    def get(self, section, option, raw=False, vars=None, keepQuotes=False):
        """ Overrides get() to chop value surrounding quotes (if any), provided keepQuotes is False """
         
        val = SafeConfigParser.get(self, section, option, raw, vars )
        val = self.chopQuotes(val, keepQuotes)
        return val

    # --- items -----------------------------------------------------------------------------------
    def items(self, section, raw=False, vars=None, keepQuotes=False):
        """ Overrides items() to chop values surrounding qoutes (if any), provided keepQuotes is False """
         
        # Get items
        curItems = SafeConfigParser.items(self, section, raw, vars )

        # By pass list copy if quotes are kept
        if keepQuotes:
            return curItems
        
        # Loop all items pairs and chop their values
        newItems = []
        for ( option , val ) in curItems:
            val = self.chopQuotes(val, keepQuotes)
            newItems.append( (option, val) )

        # Done
        return newItems


    # --- defaults --------------------------------------------------------------------------------
    def defaults(self, keepQuotes=False):
        """ Overrides defaults() to chop values surrounding qoutes (if any), provided keepQuotes is False """
         
        # Get items
        curDefaults = SafeConfigParser.defaults(self)

        # By pass list copy if quotes are kept
        if keepQuotes:
            return curDefaults

        # Loop all entries and chop their values
        newDefaults = {}
        for option in curDefaults.keys():
            val = curDefaults[option]
            newDefaults[option] = self.chopQuotes(val, keepQuotes)
        
        # Done        
        return newDefaults

    # --- optionxform -----------------------------------------------------------------------------      
    def optionxform(self, optionstr):
        """ Overrides optionxform() to make options comparition case sensitive """
        return optionstr


    # --- weakAddConfigParser ---------------------------------------------------------------------
    def weakAddConfigParser(self, newCfg):
        """ Adds all options in cfg into self. If options already exists, it will be ignored """

        # If newCfg is None -> NOP
        if not newCfg:  
            self.logger.debug4("weakAddConfigParser() merge with None object, nothign to do")
            return

        # Get new sections and add the default sections as well
        newSections = newCfg.sections()
        newSections.append(DEFAULTSECT)

        # Loop all new sections
        for newSection in newSections:

            # Get self options & new section items. 
            # Is it the default section?
            if newSection == DEFAULTSECT:
                # Default section -> just get them
                selfOpts = self.defaults().keys()
                newItems = newCfg.defaults()
                
            else:
                # Standard section, make sure self has newSection and get them
                if not self.has_section(newSection):
                     self.add_section(newSection)
                selfOpts = self.options(newSection)
                newItems = dict( newCfg.items(newSection, raw=True) )

            # Loop all options in newSection
            for option in newItems.keys():

                # Check if option already exists
                if option in selfOpts:
                    self.logger.debug4("weakAddConfigParser() option already exists, ignored." \
                                       " section=%s option=%s" % (newSection, option) )
                    continue
    
                # Option does not exists, add it
                newVal = newItems[option];
                self.logger.debug4("weakAddConfigParser() adding option." \
                                       " section=%s option=%s val=%s" % (newSection, option, newVal) )
                self.set(newSection, option, newVal)
   
    # --- getValOrRaw -----------------------------------------------------------------------------
    def getValOrRaw(self, section, option, raw=False, vars=None):
        """ Like get() but in case of interpolation error, returns the raw value """
    
        try:
            # Get it
            val = self.get(section, option, raw, vars)
            return val
    
        except InterpolationError:
            # In case of interpolation error, get the raw value
            val = self.get(section, option, True, vars)
            return "[Interpolation error of '%s=%s']" % (option, val)
    
    # --- dump ------------------------------------------------------------------------------------
    def dump(self, name=None, raw=False, vars=None ):
        """ Dumps the configuration object into the logger at NOTICE level """

        # Log header
        if not name:
            name = __name__ + " object"
        self.logger.notice("%s content dump:" % name)
         
        # Get sections and the default sections as well
        sections = sorted( self.sections() )
        sections.insert( 0, DEFAULTSECT )

        # Loop all sections
        for section in sections:

            # Log section name
            self.logger.notice("    [%s]",section)

            # Get items
            # Is it the default section?
            if section == DEFAULTSECT:
                # Default section
                items = self.defaults()                
            else:
                # Standatd section, get all options safely
                items = {}
                for option in self.options(section): 
                    items[option] = self.getValOrRaw(section, option, raw, vars)

            # Loop all options in section
            options = sorted( items.keys() )
            for option in options:

                # Log option and it value
                self.logger.notice("    %s=%s" % ( option, items[option] ) ) 

            self.logger.notice("")

    # --- flatten ---------------------------------------------------------------------------------
    def flatten(self, extendsOption=None, sections=None):
        """ saff """

        # Setup defaults
        if not extendsOption:
            extendsOption = EXTENDS_OPTION_DEFAULT
  
        # By default, flatten all sections              
        if not sections:
            sections = self.sections()

        # Flannen until nothing there are no changes.  Limit the iteration count to protect from loops
        iter   = 1
        change = True 
        while ( change and (iter <= FLATTEN_MAX_ITERATIONS) ):

            # Mark no changes in this iterarion and clear the not done section list
            change = False
            notDoneSections = []
              
            # Loop all sections
            for section in sections:
                 self.logger.debug4( "ExtendedConfigParser.flatten: --- Processing. section=%s  iter=%s" % (section, iter) )
                  
                 # If section is already flatten (with or without error) -> NOP
                 if (section in self.flattenOk) or (section in self.flattenErr):
                     continue
                  
                 # If section does have 'Extends' option mark it as 'flatten OK', declare 'change' and continue
                 if not self.has_option( section, extendsOption ):
                     self.flattenOk.append(section)
                     change = True
                     self.logger.debug3("ExtendedConfigParser.flatten: Section does not have extends option -> No need to flatten it."
                                        "  section=%s" % section )
                     continue;
                     
                 # Get parent section
                 parentSection = self.get(section, extendsOption)

                 # If parent section does not exist or has error, warn, mark error and ignore it
                 if not self.has_section(parentSection) or (parentSection in self.flattenErr):
                     self.flattenErr.append(section)
                     self.logger.debug("ExtendedConfigParser.flatten: Parent section does not exist or has error -> can't flatten."
                                        "  section=%s  parent=%s" % (section, parentSection) )
                     continue;
            
                 # If parent section is not (yet) flatten, declare 'not done' and continue
                 if not parentSection in self.flattenOk:
                     self.logger.debug3("ExtendedConfigParser.flatten: Parent section is not (yet) flatten"
                                        " -> Skipped for this iteration."
                                        "  section=%s  parentSection=%s  iter=%d" % (section, parentSection, iter) )
                     notDoneSections.append(section);
                     continue;

                 # Flatten the section
                 self._flattenSection(extendsOption, section, parentSection)

                 # Declare 'change' occured
                 change = True

            # -- END OF LOOP section
            iter = iter + 1

        # --- END OF WHILE iter  
        
        # Add 'not done' section to error list
        self.flattenErr.extend(notDoneSections)

        # Warn if error list is not empty  

        if len (self.flattenErr) != 0:
            self.logger.debug("ExtendedConfigParser.flatten: some section were not flatten successfuly."
                             "  sections=%s  iter=%d  iterMax=%d" % ( self.flattenErr, iter, FLATTEN_MAX_ITERATIONS ) )


    # --- _flattenSection -------------------------------------------------------------------------
    def _flattenSection(self, extendsOption, section, parentSection):
        """ saff """
         
        self.logger.debug3("ExtendedConfigParser.flatten: Flattening section."
                           "  section=%s  parentSection=%s" % (section, parentSection) )

        # Assume OK
        ok = True

        # Get scetion options
        opts = self.options( section ) 

        # Loop all parent options
        for opt in self.options( parentSection ):
 
            # Calc special options
            optAddEnd = opt + "+e" 
            optAddBeg = opt + "+b" 

            # First, skip the 'Extends' option itself
            if opt == extendsOption:
                pass;

            # If section already have that option, keep it
            elif opt in opts:
                self.logger.debug4("ExtendedConfigParser.flatten: Keeping section option."
                                   "  option=%s" % (opt) )
             
            # If section has add at the end, do it
            elif optAddEnd in opts:

                # Get section option and delete it
                val = self.get(section, optAddEnd, raw=True)
                self.remove_option(section, optAddEnd)
                
                # Get parent section value, adds them and set the new option
                pVal = self.get(parentSection, opt, raw=True)
                val  = pVal + val
                self.set(section, opt, val)
                self.logger.debug4("ExtendedConfigParser.flatten: solving add at the end option."
                                   "  option=%s  parentSection=%s  val=%s" % (opt, parentSection, val) )

            # If section has add at the beginning, do it
            elif optAddBeg in opts:

                # Get section option and delete it
                val = self.get(section, optAddBeg, raw=True)
                self.remove_option(section, optAddBeg)
                
                # Get parent section value, adds them and set the new option
                pVal = self.get(parentSection, opt, raw=True)
                val  =  val + pVal
                self.set(section, opt, val)
                self.logger.debug4("ExtendedConfigParser.flatten: solving add at the beginning option."
                                   "  option=%s  parentSection=%s  val=%s" % (opt, parentSection, val) )

            # Parent option does not exists at section, inherent it
            else:
                
                # Get parent section value, set it
                val = self.get(parentSection, opt, raw=True)
                self.set(section, opt, val)
                self.logger.debug4("ExtendedConfigParser.flatten: inherenting option."
                                   "  option=%s  parentSection=%s  val=%s" % (opt, parentSection, val) )
        # -- END OF LOOP

        # Loop all section options and verify no special option exist
        # In otherword, hunt for option with '+' in their names
        for opt in self.options( section ):
            if opt.find("+") >= 0 :
                ok = False
                self.logger.debug("ExtendedConfigParser.flatten: special option did not resovle."
                                   "  section=%s  option=%s  val=%s" % ( section, opt ) )

        # Add section to OK or Err list
        if ok:
            self.flattenOk.append(section)
        else:
            self.flattenErr.append(section)

    # --- isFlattenOk -----------------------------------------------------------------------------
    def isFlattenOk(self, section):
        """ Returns True if section was flatten successfully """

        return section in self.flattenOk
