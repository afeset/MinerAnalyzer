#!/usr/local/bin/python2.6

# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: effiz


## The following functions are getters for over time records

# common to all data types
def getTime (lst):
    return safeGetFromReportRecord(lst,0)

# sessions over time getters from array:  
# time, totalSessions, 0, servableSessions, 0, servableBGSSessions, 0, deliveredSessions, 0, servableUndeliveredSessions, 0, servableUndeliveredBGSSessions

def getTotalSessions(lst):
    return safeGetFromReportRecord(lst,1)

def getServableSessions(lst):
    return safeGetFromReportRecord(lst,3)

def getServableBGSSessions(lst):
    return safeGetFromReportRecord(lst,5)

def getDeliveredSessions(lst):
    return safeGetFromReportRecord(lst,7)

def getServableUndeliveredSessions(lst):
    return safeGetFromReportRecord(lst,9)

def getServableUndeliveredBGSSessions(lst):
    return safeGetFromReportRecord(lst,11)


# seconds over time getters from array:  
# time, totalSeconds, 0, servableSeconds, 0, servableBGSSeconds, 0, deliveredSeconds, 0, servableUndeliveredSeconds, 0, servableUndeliveredBGSSeconds

def getTotalSeconds(lst):
    return safeGetFromReportRecord(lst,1)

def getServableSeconds(lst):
    return safeGetFromReportRecord(lst,3)

def getServableBGSSeconds(lst):
    return safeGetFromReportRecord(lst,5)

def getDeliveredSeconds(lst):
    return safeGetFromReportRecord(lst,7)

def getServableUndeliveredSeconds(lst):
    return safeGetFromReportRecord(lst,9)

def getServableUndeliveredBGSSeconds(lst):
    return safeGetFromReportRecord(lst,11)


# volume over time getters from array:  
# time, totalL2EstimatedVolume, 0, totalL7Volume, 0, servableL7Volume, 0, servableBGSL7Volume, 0, deliveredL7Volume, 0, servableUndeliveredL7Volume, 0, servableUndeliveredBGSL7Volume, 
#       deliveredL2Port0InVolume, deliveredL2Port0OutVolume, linedL2Port0InVolume, linedL2Port1InVolume, linedL2Port2InVolume, linedL2Port3InVolume, 
#       deliveredL2Port0InVideoVolume, deliveredL2Port0OutVideoVolume, linedL2Port0InVideoVolume, linedL2Port1InVideoVolume, linedL2Port2InVideoVolume, linedL2Port3InVideoVolume, 

def getTotalL2EstimatedVolume(lst):
    return safeGetFromReportRecord(lst,1)

def getTotalL7Volume(lst):
    return safeGetFromReportRecord(lst,3)

def getServableL7Volume(lst):
    return safeGetFromReportRecord(lst,5)

def getServableBGSL7Volume(lst):
    return safeGetFromReportRecord(lst,7)

def getDeliveredL7Volume(lst):
    return safeGetFromReportRecord(lst,9)

def getServableUndeliveredL7Volume(lst):
    return safeGetFromReportRecord(lst,11)

def getServableUndeliveredBGSL7Volume(lst):
    return safeGetFromReportRecord(lst,13)

def getDeliveredL2Port0InVolume(lst):
    return safeGetFromReportRecord(lst,14)

def getDeliveredL2Port0OutVolume(lst):
    return safeGetFromReportRecord(lst,15)

def getDeliveredL2Port1InVolume(lst):
    return safeGetFromReportRecord(lst,26)

def getDeliveredL2Port1OutVolume(lst):
    return safeGetFromReportRecord(lst,27)

def getLinedL2Port0InVolume(lst):
    return safeGetFromReportRecord(lst,16)

def getLinedL2Port1InVolume(lst):
    return safeGetFromReportRecord(lst,17)

def getLinedL2Port2InVolume(lst):
    return safeGetFromReportRecord(lst,18)

def getLinedL2Port3InVolume(lst):
    return safeGetFromReportRecord(lst,19)

def getLinedL2Port4InVolume(lst):
    return safeGetFromReportRecord(lst,30)

def getLinedL2Port5InVolume(lst):
    return safeGetFromReportRecord(lst,31)

def getLinedL2Port6InVolume(lst):
    return safeGetFromReportRecord(lst,32)

def getLinedL2Port7InVolume(lst):
    return safeGetFromReportRecord(lst,33)

def getDeliveredL2Port0InVideoVolume(lst):
    return safeGetFromReportRecord(lst,20)

def getDeliveredL2Port0OutVideoVolume(lst):
    return safeGetFromReportRecord(lst,21)

def getDeliveredL2Port1InVideoVolume(lst):
    return safeGetFromReportRecord(lst,28)

def getDeliveredL2Port1OutVideoVolume(lst):
    return safeGetFromReportRecord(lst,29)

def getLinedL2Port0InVideoVolume(lst):
    return safeGetFromReportRecord(lst,22)

def getLinedL2Port1InVideoVolume(lst):
    return safeGetFromReportRecord(lst,23)

def getLinedL2Port2InVideoVolume(lst):
    return safeGetFromReportRecord(lst,24)

def getLinedL2Port3InVideoVolume(lst):
    return safeGetFromReportRecord(lst,25)

def getLinedL2Port4InVideoVolume(lst):
    return safeGetFromReportRecord(lst,34)

def getLinedL2Port5InVideoVolume(lst):
    return safeGetFromReportRecord(lst,35)

def getLinedL2Port6InVideoVolume(lst):
    return safeGetFromReportRecord(lst,36)

def getLinedL2Port7InVideoVolume(lst):
    return safeGetFromReportRecord(lst,37)


# clients over time getters from array:
# time, clients
def getClients(lst):
    return safeGetFromReportRecord(lst,1)



def safeGetFromReportRecord (lst,indx,default=0):
    try:
        return long(lst[indx])

    except IndexError:
        return default
