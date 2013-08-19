# 
# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# ver 1.0 
#
# Author: orens/amiry
#
##########################################################################################################        

import time

class EventReportLimiter:
    def __init__ (self, minTimeBetweenReports):
        self._minTimeBetweenReports = minTimeBetweenReports
        self._lastReportTime = 0
        self._numSkippedReports = 0

    def shouldReport (self):
        """Counts an event. Returns a tuple (shouldReport, numEventsSinceLastReport)"""
        curTime = time.time()
        if curTime - self._lastReportTime > self._minTimeBetweenReports:
            retValue = (True, self._numSkippedReports+1)
            self._numSkippedReports = 0
            self._lastReportTime = curTime
        else:
            self._numSkippedReports += 1
            retValue = (False, 0)
        return retValue

