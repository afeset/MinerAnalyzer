#!/usr/local/bin/python2.6
# 
# Copyright Qwilt, 2013
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: lena

import optparse

from a.infra.basic.return_codes import ReturnCodes
from a.sys.clock.app.clock_main import ClockMain 
from a.sys.clock.manager.clock_manager_base import ClockManagerBase
from a.sys.clock.manager.clock_manager_cent_os import ClockManagerCentOs
from a.sys.clock.manager.time_zone_info import TimeZoneInfo

# Bypass for PyChecker
if  __package__ is None:
    G_NAME_MODULE_CLOCK_OPERATION = "unknown"
    G_NAME_GROUP_CLOCK_OPERATION = "unknown"
else:
    from . import G_NAME_MODULE_CLOCK_OPERATION 
    from . import G_NAME_GROUP_CLOCK_OPERATION


class TimeZoneInfoOperation(object):
    """ Manages Blinky Adapter

    Attributes:
        clockManager: managed clock manager object
        options: command options
        args: command argumets
        mode: command mode, one of the strings: "all", "current", "name"
        name: time zone name, if the command mode is "name"

    """

    def __init__ (self, logger):
        self._log = logger.createLogger(G_NAME_MODULE_CLOCK_OPERATION, G_NAME_GROUP_CLOCK_OPERATION)
        self._clockManager = None
        self._options = None
        self._args = None
        self._mode = None
        self._name = None

    def genericAction_run (self, args):
        """Implements the genericAction_run() function and prints the wanted output

        Args:
            args: Command arguments, after genric action parsering

        Returns:
            ReturnCodes.kOk on success, ReturnCodes.kGeneralError otherwise
        """
        self._log("generic-action-run-called").debug3("genericAction_run() called: args=%s", args)
        rc = ReturnCodes.kOk
        if self._initClockManager(ClockMain.kSupportedTimezoneList) == ReturnCodes.kOk:
            parser = optparse.OptionParser(usage="", prog="timezone-info")
            (self._options, self._args) = parser.parse_args(args)
    
            errString = self._prepare()
    
            if errString == None:
                if self._run() != ReturnCodes.kOk:
                    rc = ReturnCodes.kGeneralError
                    self._log("generic-action-failed").debug1("genericAction_run(): _run() failed")
            else:
                print errString
                rc = ReturnCodes.kGeneralError
                self._log("generic-action-failed").debug1("genericAction_run(): _prepare() failed=%s", errString)
        else:
            print "Internal error: Error initializing clock manager"
            rc = ReturnCodes.kGeneralError
            self._log("generic-action-failed").debug1("genericAction_run() called: _initClockManager() failed")

        self._log("generic-action-run-ended").debug3("genericAction_run() ended: rc=%s", rc)
        return rc

    def _initClockManager(self, supportedList):
        """Initializes the clock manager object

        Args:
            supportedList: time-zone supported list

        Returns:
            ReturnCodes.kOk on success, ReturnCodes.kGeneralError otherwise
        """
        self._log("init-clock-manager-called").debug3("_initClockManager() called: supportedList=%s", supportedList)
        rc = ReturnCodes.kOk
        self._clockManager = ClockManagerCentOs(self._log)
        self._clockManager.initTimezoneSupportedList(supportedList)
        if self._clockManager.createClockManager() != ReturnCodes.kOk:
            rc = ReturnCodes.kGeneralError
        return rc

    def _prepare (self):
        """Reads the command arguments 

        Returns:
            None on success, error string otherwise
        """

        self._log("prepare-called").debug3("_prepare() called")
        errString = None
        if len(self._args) == 2:
            arg1 = self._args[1]
            if arg1 == 'all':
                self._mode = arg1
            else:
                self._mode = 'name'
                self._name = arg1
            self._log("prepare-read-arguments").debug3("_prepare() read arguments: mode=%s, name=%s", self._mode, self._name)
        elif len(self._args) == 1:
            self._mode = 'current'
    
        return errString

    def _run (self):
        """Runs the command.
        
        Calls ClockManager method and prints it's output

        Returns:
            ReturnCodes.kOk on success, ReturnCodes.kGeneralError otherwise
        """

        self._log("run-called").debug3("_run() called")
        rc = ReturnCodes.kOk 
        infoList = []
        errString = self._clockManager.getTimeZoneInfo (self._mode, self._name, infoList)

        if errString == None:
            infoList.sort(key = lambda tz: tz.name) # print the time-zone list in a sorted order
            for tz in infoList: # check object validity
                if tz.validData:
                    tzInfoStr = "%s %s %s" % (tz.name, tz.standardAbbr, tz.standardOffset)
                    if tz.dstAbbr:
                        tzInfoStr += " %s %s" % (tz.dstAbbr, tz.dstOffset)
                    print tzInfoStr
        else:
            print errString
            rc = ReturnCodes.kGeneralError

        self._log("run-ended").debug3("_run() ended: rc=%s, error string=%s, tzInfo list=%s", rc, errString, infoList)
        return rc
