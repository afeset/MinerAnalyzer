 # Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: yoave

import json
import os

class LineNicStats(object):
    """This class manages the line NICs status and counters"""

    KEY_LINE_NAME = "name"
    KEY_LINE_TYPE = "type"
    KEY_LINE_UP = "up"
    KEY_LINE_SPEED = "speed"
    KEY_LINE_MAC = "mac"
    KEY_LINE_COUNTERS = "counters"

    KEY_LINE_COUNTERS_RX_PACKETS = "ipackets"
    KEY_LINE_COUNTERS_RX_BYTES = "ibytes"
    KEY_LINE_COUNTERS_RX_ERRORS = "ierrors"
    KEY_LINE_COUNTERS_RX_DROPS = "idrops"
    KEY_LINE_COUNTERS_RX_MCASTS = "imcasts"
    KEY_LINE_COUNTERS_RX_BCASTS = "ibcasts"
    KEY_LINE_COUNTERS_TX_PACKETS = "opackets"
    KEY_LINE_COUNTERS_TX_BYTES = "obytes"
    KEY_LINE_COUNTERS_TX_ERRORS = "oerrors"

    KEY_LINE_COUNTERS_RX_ERRORS_GIANTS = "ierrGiants"
    KEY_LINE_COUNTERS_RX_ERRORS_MISSED = "ierrMissed"
    KEY_LINE_COUNTERS_RX_ERRORS_CRC = "ierrCrc"
    KEY_LINE_COUNTERS_RX_ERRORS_LEN = "ierrLen"
    KEY_LINE_COUNTERS_RX_ERRORS_RUNTS = "ierrRunts"

#-----------------------------------------------------------------------------------------------------------------------
    def __init__ (self, logger, name, filename):
        self.name = name
        self._log = logger
        self.filename = filename
        self.nicData = None

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def compareByNames(nicX, nicY):
        return cmp(nicX[LineNicStats.KEY_LINE_NAME], nicY[LineNicStats.KEY_LINE_NAME])

#-----------------------------------------------------------------------------------------------------------------------
    def getNicData(self, ifIndex):

        self._log("line-nics-read-data").debug4("%s: read line nics for interrface #%s", self.name, ifIndex)

        self.nicData = None
        if ifIndex>=0 and os.path.exists(self.filename):   
            
            fd = open(self.filename, 'r')

            try:
                # load data from json file
                data = json.load(fd)    
            except ValueError:
                self._log("line-load-data").debug1("%s: failed loading data from file %s", self.name, self.filename)
            else:
                self._log("line-all-data").debug5("%s: all line nics data is - %s", self.name, data)
                nicList = data["nic"]
    
                # sort devices by NIC names
                nicList.sort(cmp=LineNicStats.compareByNames)
    
                if ifIndex < len(nicList):
                    self.nicData = nicList[ifIndex]
            finally:
                fd.close()

        self._log("line-nic-data").debug4("%s: line nic data is - %s", self.name, self.nicData)
        return self.nicData







