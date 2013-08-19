#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: shmulika
# 

import re

from a.infra.basic.return_codes import ReturnCodes

# Bypass for PyChecker
if  __package__ is None:
    G_GROUP_NAME_OMREPORT_PARSER           = "unknown"
else:
    from . import G_GROUP_NAME_OMREPORT_PARSER

#----------------------------------------------------------------------------------------------------------------------------------------
# EXAMPLE USAGE OF THIS UTILITY:
#   # notice this is just a toy, not a real application
#   # notice the units are ment for a single parsing, multiple parsing should be made with new units.
# 
#   # initialize the parser with units
#   elementUnit = a.sys.format.omreport.parser.OmreportUnit(self._log, "element", titleField = "Device")
#   elementUnit.addField("Device           ", mandatory = True,  allowMany = False)
#   elementUnit.addField("Serial No.       ", mandatory = False, allowMany = True)
#   unitList = a.sys.format.omreport.parser.OmreportUnitList(self._log, "element-list", elementUnit, titleString = "System Components (FRU) Information")
#   headerUnit = a.sys.format.omreport.parser.OmreportUnit(self._log, "header", titleString = "Power Supplies Information")
#   headerUnit.addField("Redundancy Status",          mandatory = False, allowMany = False)
#   omreportParser = a.sys.format.omreport.parser.OmreportParser(self._log, self._name)
#   omreportParser.append(headerUnit)
#   omreportParser.append(unitList)
#   
#   omreportParser.parseText(text)
#   
#   # read results
#   if not headerUnit.finishedParsing():
#       return "failed parsing header"
#   if not unitList.finishedParsing():
#       return "failed parsing list"
#   if not headerUnit.hasParsedField("Redundancy Status"):
#       return "couldn't find redundnacy status"
#   print headerUnit.getParsedField("Redundancy Status")
#   for parsedElement in unitList.getParsedUnits():
#       if not parsedElement.hasParsedField("Device"):
#           return "couldn't find status of device"
#       print parsedElement.getParsedField("Device")
#
#----------------------------------------------------------------------------------------------------------------------------------------


# Internal Parsing exception classes, never raised to the user.
class _OmreportParseExceptionBase(Exception):
    def __init__ (self, msg):
        Exception.__init__(self, msg)

class _OmreportParseExceptionNotStarted(_OmreportParseExceptionBase):
    """ Raised by a OmreportUnit when it is called, but it yet to encounter its title """
    def __init__ (self, msg):
        _OmreportParseExceptionBase.__init__(self, msg)

class _OmreportParseExceptionUnrecognized(_OmreportParseExceptionBase):
    """ Raised by a OmreportUnit when it does not recognize the parsed line (field or string) """
    def __init__ (self, msg):
        _OmreportParseExceptionBase.__init__(self, msg)

class _OmreportParseExceptionFinished(_OmreportParseExceptionBase):
    """ Raised by a OmreportUnit when the current line (or a previous line) completed the parsing of the unit """
    def __init__ (self, msg):
        _OmreportParseExceptionBase.__init__(self, msg)

class _OmreportParseExceptionError(_OmreportParseExceptionBase):
    """ Raised by a OmreportUnit when the current line caused a parsing error """
    def __init__ (self, msg):
        _OmreportParseExceptionBase.__init__(self, msg)


class OmreportParser():
    """ The OmreportParser is a utility to parse the output of the omreport tool.
    It works with "parsing building-blocks" called OmreportUnits, which should be defined by the user and appended to the parser before parsing.
    The output of the parser is stored within the OmreportUnits.
    See also OmreportUnit & OmreportUnitList.
    """
    def __init__ (self, logger, instanceName):
        self._log = logger.createLoggerSameModule(G_GROUP_NAME_OMREPORT_PARSER, instance = instanceName)
        self._name = instanceName
        self._units = []


    def append (self, omreportUnitBase):
        """ appends the given OmreportUnit to the ordered-list of units to parse.
        Parsing is an ordered task, which required the Units to be appended in the order of their expected apperance in the text.
        See example-usage of code.
        """
        self._units.append(omreportUnitBase)


    def parseLines (self, lines):
        """ parses a list of lines by order of list.
        parsing results are stored in the parsed elements.
        Returns: ReturnCodes.kOk on success, ReturnCodes.kGeneralError on failure
        """
        stillToBeParsedUnits = self._units[:]
 
        try: # catch _OmreportParseExceptionError, and return error code if does
            for line in lines:
                self._log("parse-lines-line").debug1("parsing line: %s", line)                        
                lineParsed = False
                possibleUnits = stillToBeParsedUnits[:]
               
                while (not lineParsed) and (len(possibleUnits) > 0):                
                    try:                    
                        possibleUnits[0].parseLine(line)                    
                        lineParsed = True
    
                        if stillToBeParsedUnits[0].wasParsed() and stillToBeParsedUnits[0] is not possibleUnits[0]:
                            # need to "finish parsing" the unit that was parsed before the current unit (if at all)
                            stillToBeParsedUnits[0].finishParsing()
                            stillToBeParsedUnits = possibleUnits[:]
                        
                    except _OmreportParseExceptionFinished:
                        # this line is not part of the currently checked unit, and it has already finished parsing (no need to finish it again later so advance the "stillToBeParsedUnits")
                        stillToBeParsedUnits = stillToBeParsedUnits[1:]
                        possibleUnits = stillToBeParsedUnits[:]
    
                    except _OmreportParseExceptionNotStarted:
                        # the currently checked unit might not exist at all, so try the next unit
                        possibleUnits = possibleUnits[1:]            
                    except _OmreportParseExceptionUnrecognized:
                        # the currently checked unit might have ended, so try the next unit
                        possibleUnits = possibleUnits[1:]            
                                       
            # done parsing line - finish the last unit
            if len(stillToBeParsedUnits) > 0 and stillToBeParsedUnits[0].wasParsed():
                stillToBeParsedUnits[0].finishParsing()

            return ReturnCodes.kOk

        except:
            self._log("parse-lines-failure").error("failed parsing omreport lines: %s", lines)                        
            return ReturnCodes.kGeneralError



    def parseText (self, text):        
        """ breaks the given text into a list of lines, and parses the lines.
        parsing results are stored in the parsed elements.
        Returns: ReturnCodes.kOk on success, ReturnCodes.kGeneralError on failure
        """
        return self.parseLines(text.split('\n'))



class _OmreportUnitBase:
    """ Base class for all types of OmreportUnits used with the OmreportParser.
    """
    def __init__ (self, logger, instanceName, titleString = None, titleField = None):
        self._log = logger.createLoggerSameModule(G_GROUP_NAME_OMREPORT_PARSER, instance = instanceName)
        self._name = instanceName

        if titleString is not None:
            self._titleString = self._trim(titleString)
            self._titleField  = None
        elif titleField is not None:
            self._titleField  = self._trim(titleField)
            self._titleString = None

        self._resetParsing()
        
        
    def clone (self):
        cloned = _OmreportUnitBase(self._log, self._name)
        cloned.copyFrom(self)
        return cloned

    def copyFrom (self, other):
        self._titleString = other._titleString
        self._titleField  = other._titleField       


    def _resetParsing (self):
        self._parsingStarted = False        
        self._parsingFinished = False

        self._lastParsedLine   = None
        self._lastParsedField  = None
        self._lastParsedString = None


    def parseLine (self, line):
        # TODO(shmulika): fix this comment up
        """ Try to find : , if not exist - parse as a string """
        self._log("parse-line").debug2("parsing line: %s", line)
        self._lastParsedLine   = None
        self._lastParsedField  = None
        self._lastParsedString = None

        if self._parsingFinished:
            # parsing already finished - not part of the unit
            self._log("parse-line-already-finished").warning("cannot parse (line=%s), parsing of this unit has already finished", line)
            raise _OmreportParseExceptionFinished("cannot parse (line=%s), parsing of this unit (name = %s) has already finished"%(line, self._name))
        
        try:
            field, value = self.breakLineToFieldAndValue(line)                
            self.parseField(field, value)
            self._lastParsedField  = field
        except KeyError:
            line = self._trim(line)
            self.parseString(line)
            self._lastParsedLine = line

        self._lastParsedLine = line


    def parseField (self, field, value):        
        self._log("parse-field").debug2("parsing (field=%s, value=%s)", field, value)
        self._parseExpectedTitle(self._titleField, field)
           

    def parseString (self, string):                
        self._log("parse-string").debug2("parsing (string=%s)", string)
        self._parseExpectedTitle(self._titleString, string)



    def startParsing (self):
        self._parsingStarted = True

    def finishParsing (self):
        self._parsingFinished = True

    def isTitleString (self, string):
        return self._titleString == string

    def isTitleField (self, field):
        return self._titleField == field

    def ignoreNextTitleFields (self):
        self._titleField = None


    def _parseExpectedTitle (self, expectedTitle, givenTitle):
        self._log("parse-expected-title").debug2("expecting title: %s; given title: %s", expectedTitle, givenTitle)

        if not self._parsingStarted:            
            # parsing has not started yet
            if expectedTitle is None:
                # the given title cannot start the unit
                self._log("parse-expected-title-not-yet-started").debug2("cannot parse (string=%s), parsing of this unit has not started yet", givenTitle)
                raise _OmreportParseExceptionNotStarted("cannot parse (string=%s), parsing of this unit (name = %s) has not started yet"%(givenTitle, self._name))

            if expectedTitle == givenTitle:
                # this is the start of the unit                
                self.startParsing()                
                self._log("parse-expected-title-starting").debug1("started parsing unit with title=%s", givenTitle)                
        else:
            # already started parsing before, but not finished yet
            if expectedTitle == givenTitle:
                # this is the start of another unit
                self.finishParsing() # TODO(shmulika): maybe this should be called only by the upper layer!!!
                self._log("parse-expected-title-now-finished").debug2("not parsing (string=%s), already parsed it. this is the title of another unit", givenTitle)
                raise _OmreportParseExceptionFinished("not parsing (string=%s), unit (name = %s) already parsed it. this is the title of another unit"%(givenTitle, self._name))
        
        if not self._parsingStarted:  
            # the given string was no the title of the unit
            self._log("parse-expected-title-not-yet-started").debug2("cannot parse (string=%s), parsing of this unit has not started yet", givenTitle)
            raise _OmreportParseExceptionNotStarted("cannot parse (string=%s), parsing of this unit (name = %s) has not started yet"%(givenTitle, self._name))          
                    
                
    def wasParsed (self):
        return self._parsingStarted

    def finishedParsing (self):
        return self._parsingFinished

    def breakLineToFieldAndValue (self, line):        
        # breaking the RE into elements for explanation:
        # \s*                   - white space before content
        # (?P<field>[^:]*?)     - field content itself (without ':'), minimal search so not to take extra whitespaces
        # \s*                   - white space after content
        # :                     - ':' seperating field from value 
        # and the same for value....
        matches = re.search("^\s*(?P<field>[^:]*?)\s*:\s*(?P<value>.*?)\s*$", line)        
        try:
            field = matches.group("field")
            value = matches.group("value")
            self._log("break-line-to-field-and-value").debug4("line (%s) was broken to field=(%s) and value=(%s)", line, field, value)
            return (field, value)
        except:
            raise KeyError

    def _trim (self, string):        
        return string.strip()


class _OmreportUnitField():
    def __init__ (self, field, mandatory, allowMany):
        self.field = field
        self.mandatory = mandatory
        self.allowMany = allowMany
  
    

class OmreportUnit(_OmreportUnitBase):
    """ OmreportUnit represents a group of expected lines (of field/values) to parse.
    The expected lines inside a unit are not ordered, which means both the following text examples will be parsed the same by a unit:
        'Device : Fan
         Serial : 1234'

        'Serial : 1234
         Device : Fan'

    The user needs to declare the expected fields with the addField() method.
    The unit is given to a OmreportParser, and after parsing it will contain parsed results, that can be read with:
        hasParsedField(), getParsedField().


    """
    def __init__ (self, logger, instanceName, titleString = None, titleField = None):
        self._fields = {}
        _OmreportUnitBase.__init__(self, logger, instanceName, titleString, titleField)
        
    ################
    # User Methods
    ################

    def addField (self, field, mandatory = False, allowMany = False):
        """ adds an expected field to the unit.
        Arguemnts:  field     - string, name of the field, e.g. such as "Device" in the omreport line 'Device : Fan Probe Mod 2'
                    mandatory - when True, parsing of this unit will fail, if the specified field was not encountered.
                    allowMany - when True, multiple repititions of this field will not fail the parsing; instead all the values will be returned in a list.
        Returns: None
        """
        field = self._trim(field)
        self._fields[field] = _OmreportUnitField(field, mandatory, allowMany)
        
    def hasParsedField (self, field):
        """ checks whether a field was parsed
        Arguments:  field     - string, name of the field, e.g. such as "Device" in the omreport line 'Device : Fan Probe Mod 2'
        Returns: True when field was parsed.
        """
        field = self._trim(field)
        return field in self._parsedFields

    def getParsedField (self, field):
        """ returns the parsed value of a field
        Arguments:  field     - string, name of the field, e.g. such as "Device" in the omreport line 'Device : Fan Probe Mod 2'
        Returns: result value of the parsing (e.g. "Fan Probe Mod 2" in above example), or None when not parsed.
        """
        field = self._trim(field)
        if not self.hasParsedField(field):
            return None
        return self._parsedFields[field]
    
    def getParsedFieldCommaSeperated (self, field):
        """ returns the parsed value of a field as a comma seperated string.
        usually applicable when field was added with allowMany=True
        Arguments:  field     - string, name of the field, e.g. such as "Device" in the omreport line 'Device : Fan Probe Mod 2'
        Returns: comma-seperated string of result values of the parsing, or None when not parsed.
        """
        value = self.getParsedField(field)
        if value is None:
            return None
        if isinstance(value, list):
            return ",".join(value)
        else:
            return value

    ################
    # Internal Methods
    ################

    def clone (self):        
        cloned = OmreportUnit(self._log, self._name)        
        cloned.copyFrom(self)
        return cloned

    def copyFrom (self, other):
        _OmreportUnitBase.copyFrom(self, other)
        self._fields = other._fields
        

    def _resetParsing (self):
        _OmreportUnitBase._resetParsing(self)
        self._parsedFields = {}
        self._lastParseField = None

    
    def parseString (self, string):
        _OmreportUnitBase.parseString(self, string)
        self._log("parse-string").debug2("strings are not recognized inside an OmreportUnit")
        self._lastParseField = None

        if self.isTitleString(string):
            self._log("parse-string-list-title").debug2("string %s is the list title", string)
            return 

        raise _OmreportParseExceptionUnrecognized("unit %s does not recognize (string=%s)"%(self._name, string))


    def parseField (self, field, value):        
        _OmreportUnitBase.parseField(self, field, value)        
        self._log("parse-field").debug2("parsing (field=%s, value=%s)", field, value)        

        if field == "" and self._lastParseField is not None:
            field = self._lastParseField
            self._log("parse-field").debug1("empty field, attaching value to the last parsed field=%s", field)

        self._lastParseField = None
        if field not in self._fields:
            # unrecognized field - don't parse
            self._log("parse-field-unrecognized").debug1("unrecognized (field=%s, value=%s)", field, value)
            raise _OmreportParseExceptionUnrecognized("unit %s does not recognize (field=%s, value=%s)"%(self._name, field, value))
        
        if field not in self._parsedFields:
            # recognized field, that hasn't been parsed yet
            self._log("parse-field-parsed").debug1("parsed (field=%s, value=%s)", field, value)
            self._parsedFields[field] = value
            self._lastParseField = field            

        else:            
            # recognized field, that has already been parsed
            if not self._fields[field].allowMany:
                self._log("parse-field-many-not-allowed").error("field %s appeared more then once (first-appearnace-value = %s; current-appearnace-value = %s)", field, self._parsedFields[field], value)
                raise _OmreportParseExceptionError("field %s appeared more then once for unit %s"%(field, self._name))
            try:
                self._parsedFields[field].append(value)
            except:
                self._parsedFields[field] = [self._parsedFields[field], value]

            self._lastParseField = field
            self._log("parse-field-parsed-list").debug1("parsed (field=%s, value=%s), value was added to list of values", field, value)
              
    
    def finishParsing (self):
        _OmreportUnitBase.finishParsing(self)
        self._log("finish-parsing").debug1("finishing parsing")

        for fieldData in self._fields.values():
            if fieldData.mandatory:
                if fieldData.field not in self._parsedFields:
                    self._log("finish-parsing-mandatory-not-parsed").error("mandatory field %s not parsed")
                    raise _OmreportParseExceptionError("mandatory field %s not parsed for unit %s"%(fieldData.field, self._name)) 



class OmreportUnitList(_OmreportUnitBase):
    """ Represents a reptition of the same OmreportUnit.
    Used, for example, to parse the many fans reported in a list in the output of "omreport chassis fans"
    The OmreportUnitList is initialized with a template OmreportUnit; and with which string or field starts a single unit
    (this is necessary to seperate the repititions from one another)    
    """
    def __init__ (self, logger, instanceName, templateOmreportUnit, titleString = None, titleField = None, isTitlePartOfUnit = False):
        self._unit = templateOmreportUnit        
        self._isTitlePartOfUnit = isTitlePartOfUnit
        _OmreportUnitBase.__init__(self, logger, instanceName, titleString, titleField)
        
    ################
    # User Methods
    ################

    def getParsedUnits (self):
        """ Returns a list of parsed OmreportUnits (parsed "duplicates" of the template OmreportUnit).
        """
        return self._parsedUnits


    ################
    # Internal Methods
    ################
        
    def clone (self):        
        cloned = OmreportUnitList(self._log, self._name, self._unit)        
        cloned.copyFrom(self)
        return cloned

    def copyFrom (self, other):
        _OmreportUnitBase.copyFrom(self, other)
        self._unit.copyFrom(other._unit)
        

    def _resetParsing (self):
        _OmreportUnitBase._resetParsing(self)
        self._parsedUnits = []
        self._currentParsedUnit = self._unit.clone()
       
     
    def parseField (self, field, value):        
        _OmreportUnitBase.parseField(self, field, value)
        self._log("parse-field").debug2("parsing (field=%s, value=%s)", field, value)

        if self.isTitleField(field):
            if self._isTitlePartOfUnit:
                # when the title field is part of the unit, we expect more of these fields to come in the list,
                # so we ignore all the next title fields to come (not consider them as title fields of new list units)
                self.ignoreNextTitleFields()
                self._log("parse-field-list-title").debug2("field %s is the list title and also part of the unit", field)
            else:
                self._log("parse-field-list-title").debug2("field %s is the list title", field)
                return 

        doneParsing = False
        while not doneParsing:            
            try:
                self._currentParsedUnit.parseField(field, value)                
                # note: if this raises _OmreportParseExceptionNotStarted, then the list might be empty - and we need to pass this info the the upper layer
                # note: if this raises _OmreportParseExceptionUnrecognized, then the list might be empty - and we need to pass this info the the upper layer
                doneParsing = True
                
            except _OmreportParseExceptionFinished:
                # this field belongs probably to a new unit
                self._parsedUnits.append(self._currentParsedUnit)
                self._currentParsedUnit = self._unit.clone()                
            
            
    # TODO(shmulika): code repitition from above (method parseField) - find way to avoid this
    def parseString (self, string):        
        _OmreportUnitBase.parseString(self, string)
        self._log("parse-string").debug2("parsing (string=%s)", string)

        if self.isTitleString(string):
            self._log("parse-string-list-title").debug2("string %s is the list title", string)
            return 

        doneParsing = False
        while not doneParsing:            
            try:
                self._currentParsedUnit.parseString(string)                
                # note: if this raises _OmreportParseExceptionNotStarted, then the list might be empty - and we need to pass this info the the upper layer
                # note: if this raises _OmreportParseExceptionUnrecognized, then the list might be empty - and we need to pass this info the the upper layer
                doneParsing = True
                
            except _OmreportParseExceptionFinished:
                # this field belongs probably to a new unit                
                self._parsedUnits.append(self._currentParsedUnit)
                self._currentParsedUnit = self._unit.clone()  
            

    def finishParsing (self):
        _OmreportUnitBase.finishParsing(self)
        self._log("finish-parsing").debug1("finishing parsing")
        if self._currentParsedUnit.wasParsed():
            self._currentParsedUnit.finishParsing()
            self._parsedUnits.append(self._currentParsedUnit)
            

    



