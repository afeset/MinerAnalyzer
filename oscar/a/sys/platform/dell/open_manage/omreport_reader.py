# Copyright Qwilt, 2013
# 
# The code contained in this file may not be used by any other entities 
# without explicit written permission from Qwilt.
# 
# Author: shmulika
#

import re
import subprocess as originalsubprocess
import a.infra.subprocess


# Bypass for PyChecker
if  __package__ is None:
    G_GROUP_NAME_OMREPORT_READER           = "unknown"
else:
    from . import G_GROUP_NAME_OMREPORT_READER        


class OmreportReader:
    OMREPORT_CMD = "/opt/dell/srvadmin/bin/omreport"

    # this should be configurable
    OMREPORT_DEFAULT_KILL_TIMEOUT = 10
    OMREPORT_DEFAULT_WARNING_TIMEOUT = 5

    def __init__ (self, instanceName, logger, omreportArgs):
        """ 
        Arguments:
            instanceName
            logger
            omreportArgs - list of args to specify the omreport, e.g. ["chassis", "fans"] or ["chassis", "pwrsupplies"]
        """
        self._name = instanceName
        self._log = logger.createLoggerSameModule(G_GROUP_NAME_OMREPORT_READER, instance = self._name)
        self._omreportArgs = omreportArgs

        self._wasWarningTimeout = False
        self._wasKillingTimeout = False

        self._lastReadText = None
        self._comparisonFilterPattern     = None
        self._comparisonFilterreplacement = None

    def initComparisonFilter (self, pattern, replacement):
        """
        If this filter is initialized, then the text of the omreport is filtered before looking for differences from previous omreports.
        This enables to ignore some small unimportant values in the report, like fan's speed reading.
        The text is filtered line-by-line with the command re.sub(pattern, replacement, line)
        """
        self._comparisonFilterPattern     = pattern
        self._comparisonFilterreplacement = replacement
    

    def read (self, killTimeout = OMREPORT_DEFAULT_KILL_TIMEOUT, warningTimeout = OMREPORT_DEFAULT_WARNING_TIMEOUT):
        """
        Executes the omreport process, and returns the text output of the omreport.
        Arguments: killTimeout - seconds to let the omreport process execute before killing it by force.

        Returns: string when successfull, or None when executing omreport or reading the text failed for any reason.
        """
        text = self._readOmreport(killTimeout, warningTimeout)
        filteredText = self._filterOmreportForComparison(text)
        
        if filteredText != self._lastReadText:
            self._log("omreport-read").notice('omreport text changed to is: """%s"""', text)
            self._lastReadText = filteredText

        return text


    def _filterOmreportForComparison (self, text):
        if self._comparisonFilterPattern is not None and self._comparisonFilterreplacement is not None:
            lines = text.splitlines()
            filteredLines = [re.sub(self._comparisonFilterPattern, self._comparisonFilterreplacement, line) for line in lines]
            return "\n".join(filteredLines)

        return text
            

    def _readOmreport (self, killTimeout, warningTimeout):
        # TODO(shmulika): write doc
        subprocess = a.infra.subprocess.Subprocess("omreport-reader", self._log)
        args = [OmreportReader.OMREPORT_CMD]
        args.extend(self._omreportArgs)
        args = " ".join(args)
        
        self._wasWarningTimeout = False
        self._wasKillingTimeout = False

        try:
            self._log("read-starting").debug2("starting the omreport with args=%s", args)
            subprocess.start(args, stdout = originalsubprocess.PIPE, shell = True)
        except:
            self._log("read-start-failed").error("failed reading omreport with args=%s", args, exc_info = 1)
            return None

        try:
            self._log("read-communicate").debug2("communicating (waiting for stdout result) with omreport process, with KillTimeout=%s", OmreportReader.OMREPORT_DEFAULT_KILL_TIMEOUT)
            omreportStdout, omreportStderr = subprocess.communicate(killTimeOut = killTimeout, warningTimeOut = warningTimeout)
        except:
            self._log("read-communicate-failed").error("failed communicating with omreport with args=%s", args, exc_info = 1)
            return None

        self._wasKillingTimeout = subprocess.hasTimeoutKilling() or subprocess.hasTimeoutTerminating()
        self._wasWarningTimeout = subprocess.hasTimeoutWarning()        

        returnCode = subprocess.getReturnCode()
        if returnCode != 0:
            self._log("read-omreport-failed").error("running omreport with args=%s, exited with return code = %s", args, returnCode)
            return None

        if omreportStdout is None:
            self._log("read-omreport-no-stdout").error("failed getting stdout of omreport with args=%s", args)
            return None

        self._log("read-done").debug2('omreport with args=%s, finished with stdout="""%s"""', args, omreportStdout)
        return omreportStdout


    def hasTimeoutWarning (self):
        """ Returns: True, when the warning timeout was exceeded """
        return self._wasWarningTimeout

    
    def hasTimeoutKilling (self):
        """ Returns: True, when the killing timeout was exceeded """
        return self._wasKillingTimeout
