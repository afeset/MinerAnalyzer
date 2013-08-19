# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities 
# without explicit written permission from Qwilt.
# 
# Author: shmulika
#
__pychecker__ = 'maxrefs=20' 
from a.infra.basic.return_codes import ReturnCodes

import a.sys.platform.manager.source
import a.sys.platform.dell.open_manage.omreport_reader
import a.sys.platform.dell.open_manage.omreport_parser

class Source(a.sys.platform.manager.source.Source):
    """
    The Dell/Source is responsible for gathering information from an omreport (for example, `omreport chassis fans`)    
    It is also responsible for storing the result of the last read, for get operation.
    Reading and getting are separate processes.
    This is the base class for all omreporters.
    The base class also provides typical parsing functionallity, of a report that has a "header" unit and a "element list" unit.
    Extension calsses are responsible for specifying the exact omreport to run, and to translate the parsed text into data structure.
    """

    OMREPORT_CMD = "omreport"
    
    def __init__ (self, instanceName, logger, omreportArgs):
        """ omreportArgs - list of args to specify the omreport, e.g. ["chassis", "fans"] or ["chassis", "pwrsupplies"]
        """
        a.sys.platform.manager.source.Source.__init__(self, instanceName, logger)
        self._omreportReader = a.sys.platform.dell.open_manage.omreport_reader.OmreportReader(self._name, self._log, omreportArgs)


    def _initComparisonFilter (self, pattern, replacement):
        self._omreportReader.initComparisonFilter(pattern, replacement)
        

    ### extension's responsiblity - read & parse section """
    def _createHeaderUnit (self):
        """ Should be implemented by extension classes
        Creates and returns the units required for the parsing of a standard omreport.
        Returns: the header unit, or None if no header is expected.
        """
        return None

    def _createListUnit (self):
        """ Should be implemented by extension classes
        Creates and returns the units required for the parsing of a standard omreport.
        Returns: the list unit, or None if no list is expected.
        """
        return None


    def _translateHeaderAndListUnit (self, headerUnit, elementUnitList):
        """ Should be implemented by extension classes
        Takes the standard header and list units, after their fields parsed by the omreport parser.
        The method is to retrieve information from the parsed unit, create & store a data-structure containing that information.
        Note: this is done in a single method, instead of two methods, because a Lock should be placed around the update of the data.
        Return: The translated data, or None if parsing failed.
        """
        __pychecker__ = "unusednames=headerUnit,elementUnitList"        
        return None


    ### base responsibiity - read & parse section """
    def _poll (self, warningTimeout, timeout, simulationFile = None):
        """ Polls the source and updates the stored data for next getData() calls.
        Arguments:
            timeout         - maximum time to try the poll, if exceeded - stop and return POLL_TIMEOUT
            warningTimeout  - warning timeout < timeout; if exceeded (but poll done) must call _reportWarningTimeout
            simulationFile  - when not None, should read the file and take information from it instead of usual source of information

        Should be extended by specific reporter class.
        Returns:
            Source.POLL_TIMEOUT         - when the command timed out
            Source.POLL_PARSE_ERROR     - when parsing the information failed
            Source.POLL_FILE_ERROR      - when reading the file failed
            Source.POLL_ERROR           - when there was an error
            Source.POLL_OK              - when poll was ok
         
        Raises: None
        """
        __pychecker__ = "unusednames=warningTimeout"        
        if simulationFile is not None:
            text = self._readFile(simulationFile)
            if text is None:
                return Source.POLL_FILE_ERROR
        else:
            text = self._read(timeout, warningTimeout) 
            
            if self._omreportReader.hasTimeoutKilling():
                self._log("poll-read-timed-out").error("reading text from the omreport timed out, process was killed")
                return Source.POLL_TIMEOUT

            if text is None:
                self._log("poll-read-failed").warning("reading text from the omreport failed")
                return Source.POLL_ERROR
        
        self._log("poll-read-text").debug3("read this text to parse: %s", text)          

        if self._omreportReader.hasTimeoutWarning():
            self._log("poll-read-warning-timeout").warning("reading text from the omreport took more than warning threshold")
            self._reportWarningTimeout()

        return self._parseAndUpdate(text)

    def _readFile (self, filename):
        try:
            with open(filename, mode='r') as fileInput:
                text = fileInput.read()
            self._log("read-file").debug3('read omreport text from file=%s, text="""%s"""', filename, text)
            return text
        except:
            self._log("read-file-failed").error("failed reading omreport text from file=%s", filename)
            return None


    def _read (self, killTimeout, warningTimeout):
        """ Reads the Omreport of the specific Omreporter (from the reader specific)
        And updates the parsed data.
        Note: for extensions classes, this could be a hook to retrieve the text from somewhere else (besides the omreport tool), for example
        from a configured text file
        """
        return self._omreportReader.read(killTimeout, warningTimeout)        


    def _parseAndUpdate (self, text):
        """"
        Returns: Source.POLL_OK - if poll succesfull, Source.POLL_PARSE_ERROR - if failed parsing the text
        """
        udpatedData = self._parse(text)
        if udpatedData is None:
            return Source.POLL_PARSE_ERROR
    
        self._updateData(udpatedData)
        return Source.POLL_OK


    def _parse (self, text):
        omreportParser = a.sys.platform.dell.open_manage.omreport_parser.OmreportParser(self._log, self._name)

        headerUnit  = self._createHeaderUnit()
        unitList    = self._createListUnit()

        if headerUnit is not None:
            omreportParser.append(headerUnit)
        if unitList is not None:
            omreportParser.append(unitList)

        self._log("parse-text-parse-call").debug2("calling the omreport parser with text = %s", text)        
        rc = omreportParser.parseText(text)
        self._log("parse-text-parse-return").debug2("returned from call to omreport parser, return-code = %s", rc)        

        if rc != ReturnCodes.kOk:
            # parsing failed - do not try to use results
            headerUnit = None
            unitList = None
        else:
            if headerUnit is None or not self._checkHeaderUnit(headerUnit):
                # if parsring of the header unit failed - do not tkae it upward
                headerUnit = None
            if unitList is None or not self._checkListUnit(unitList):
                # same for list of elements
                unitList = None

        translatedData = self._translateHeaderAndListUnit(headerUnit, unitList)        

        return translatedData


    def _checkHeaderUnit (self, headerUnit):
        if headerUnit.finishedParsing():
            self._log("check-header-unit-valid").debug2("the header of the omreport has been parsed by the OmreportParser")            
            return True
        else:
            self._log("check-header-unit-not-parsed").warning("the header of the omreport has not been parsed by the OmreportParser")            
            return False

    def _checkListUnit (self, unitList):
        if unitList.finishedParsing():
            self._log("check-list-unit-valid").debug2("the element list of the omreport has been parsed by the OmreportParser")
            return True
        else:
            self._log("check-list-unit-not-parsed").error("the element list of the omreport has not been parsed by the OmreportParser")
            return False




