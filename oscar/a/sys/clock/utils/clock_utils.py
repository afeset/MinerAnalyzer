#
# Copyright Qwilt, 2013
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: lenak
# 

#
# Due to the fact the oscar_core has a problem to import modules that use blinky, this module was created.
# It includes a fraction of the clock_manager functionality that is needed for oscar_core. 
#

import re
import shutil
import subprocess

from a.infra.basic.return_codes import ReturnCodes
from a.sys.clock.utils.clock_cent_os_def import kConfigFilePath, kConfigUtility

class ClockUtils(object):

    @classmethod
    def s_setTimezone(cls, log, timeZone, configFileName = kConfigFilePath, configUtility = kConfigUtility):
        """Sets the new time-zone configuration.
        Changes the time-zone name in the configuration file and runs the config utility.
    
        Args:
            timeZone: new time-zone to be configured  

        Returns:
            ReturnCodes.kOk on success, ReturnCodes.kGeneralError otherwise
        """
        log("set-time-zone-called").debug4("ClockUtils.s_setTimezone() called: timezone=%s", timeZone)
        originalFileName = configFileName
        (rc, originalFile) = cls._s_openFile(log, originalFileName, 'r')
        if rc == ReturnCodes.kOk: 
            # create a new file name: clock.tmp.qb
            newFileName = originalFileName + '.tmp.qb' 
            (rc, newFile) = cls._s_openFile(log, newFileName, 'w')
            if rc == ReturnCodes.kOk:
                lines = originalFile.readlines()
                cls._s_readTimeZoneAndSetLines(log, lines, True, timeZone)
                newFile.writelines(lines)
                newFile.close()
                shutil.move(newFileName, originalFileName)
                log("set-time-zone-utility-called").debug4("ClockUtils.s_setTimezone(): time zone=%s, utility=%s child process called", timeZone, configUtility)
                proc = subprocess.Popen(configUtility)
                childReturnCode = proc.wait()
                if childReturnCode:
                    log("set-time-zone-utility-process-err").error("ClockUtils.s_setTimezone(): time zone=%s, utility=%s process returned an err=%s", timeZone, configUtility, childReturnCode)
                    rc = ReturnCodes.kGeneralError
            else: # (rc == ReturnCodes.kOk)
                rc = ReturnCodes.kGeneralError
            
            originalFile.close()
        else: # (rc == ReturnCodes.kOk)
            rc = ReturnCodes.kGeneralError
        log("set-time-zone-ended").debug4("ClockUtils.s_setTimezone() ended: rc=%s", rc)
        return rc

    @classmethod
    def s_getCurrentTimeZone (cls, log, configFileName = kConfigFilePath):
        """Returns the current time-zone configured in Linux  

        Returns:
            A tuple: return code and the current time-zone. ReturnCodes.kOk and time-zone on success, ReturnCodes.kGeneralError and None otherwise  
        """
        log("get-current-time-zone-called").debug4("ClockUtils.s_getCurrentTimeZone() called")
        currentTimeZone = None
        (rc, configFile) = cls._s_openFile(log, configFileName, 'r')
        if rc == ReturnCodes.kOk:
            currentTimeZone = cls._s_readTimeZoneAndSetLines(log, configFile.readlines())
        else:
            rc = ReturnCodes.kGeneralError
        log("get-current-time-zone-ended").debug4("ClockUtils.s_getCurrentTimeZone() ended: rc=%s, currentTimeZone=%s", rc, currentTimeZone)
        return (rc, currentTimeZone)

    @classmethod
    def _s_readTimeZoneAndSetLines (cls, log, lines, setLines = False, reqTimeZone = ''):
        """Parses the config file lines.
        
        Args:
            lines: the lines read from a config file in the format of /etc/sysconfig/clock
            setLines: If true, the given lines list is updated with ZONE= set to the value of reqTimeZone
            reqTimeZone: new time-zone, set in lines if setLines is true.
        Returns:
            The time zone as found in lines. 
        """

        __pychecker__ = 'no-argsused'

        log("read-timezone-and-set-lines-called").debug4("ClockUtils._s_readTimeZoneAndSetLines() called: lines=%s, setLines=%s, reqTimeZone=%s", lines, setLines, reqTimeZone) 
        currentTimeZone = None
        lineIndex = None 
        newLine = 'ZONE=' + '"' + reqTimeZone + '"' + '\n'
        for i in range(len(lines)):
            line = lines[i]
            match = re.match('^[\s]*ZONE[\s]*=[\s]*[\'"]?([\w/+-_]+)[\'"]?', line) 
            if match:
                currentTimeZone = match.group(1)
                lineIndex = i

        if currentTimeZone is None:
            log("read-timezone-and-set-lines-no-zone").info("ClockUtils._s_readTimeZoneAndSetLines() - ZONE info was not found at the config file, UTC assumed ") 
            currentTimeZone = 'UTC'
            if setLines:
                lines.insert(0, newLine)
        else:
            if setLines:
                lines[lineIndex] = newLine
        log("read-timezone-and-set-lines-ended").debug4("ClockUtils._s_readTimeZoneAndSetLines() ended: currentTimeZone=%s", currentTimeZone) 
        return currentTimeZone

    @classmethod
    def _s_openFile (cls, log, fileName, mode):
        """Opens the given fileName  
        
        Args:
            fileName: given file name
            mode: the needed mode
        Returns:
            A tuple: return code and the file descriptor. ReturnCodes.kOk and file descriptor on success, ReturnCodes.kGeneralError and None otherwise  
        """

        __pychecker__ = 'no-argsused'

        log("open-file-called").debug4("ClockUtils._s_openFile() called: file=%s, mode=%s", fileName, mode) 
        rc = ReturnCodes.kOk
        try:
            fileDscp = open(fileName, mode)
        except IOError as e:
            fileDscp = None
            log("openFile-exception").warning("ClockUtils._s_openFile(): file=%s mode=%s open raised exception=%s", fileName, mode, e) 
            rc = ReturnCodes.kGeneralError
        return (rc, fileDscp)

