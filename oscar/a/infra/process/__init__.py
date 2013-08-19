#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

import traceback
import sys       

global _g_captain
_g_captain = None

def setGlobalCaptain(captain):
    global _g_captain
    _g_captain = captain

def clearGlobalCaptain_EXPERIMENTAL_USE_BY_OSCAR_CORE_ONLY():
    global _g_captain
    _g_captain = None

def stopRequest():
    global _g_captain
    if _g_captain:
        _g_captain.stopRequest()
    else:
        processFatal("stop request with no captain defined")

def processFatal(msg, *args):
    print "fatal:%s (%s)"%(msg,args)
    global _g_captain
    if _g_captain:
        _g_captain.processFatal(msg,*args)
    else:
        #temp implementation #TODO(nirs) remove        
        try:
            fatalMessage = (msg % args)
        except:
            #we have a problem in the msg creation - recovering the best way we can
            fatalMessage = "msg: %s; args: %s".format(msg, args)
        print fatalMessage
        traceback.print_stack()
        sys.exit(1)

def logUserMessage (userLogMessage):
    if _g_captain:
        _g_captain.logUserMessage(userLogMessage)
    else:
        processFatal("trying to log user message with no captain available")
        
def getIsRelaxMode ():
    if _g_captain:
        return _g_captain.getIsRelaxMode()
    else:
        processFatal("trying to check relax mode with not captain available")

def getWasStopped ():
    if _g_captain:
        return _g_captain.getWasStopped()
    else:
        processFatal("trying to check captain stopping flag with no captain available")
                
def substitueSystemKnownPaths (pathPattern):
    if _g_captain:
        return _g_captain.substitueSystemKnownPaths(pathPattern)
    else:
        processFatal("trying to substitue system known pathes")

                
def getProcessId ():
    if _g_captain:
        return _g_captain.getProcessId()
    else:
        processFatal("trying to check process id with no captain available")
                
def getKickNumber ():
    if _g_captain:
        return _g_captain.getKickNumber()
    else:
        processFatal("trying to check kick number with no captain available")

def getPlatformBasicDataUnsafe ():
    if _g_captain:
        return _g_captain.getPlatformBasicData()
    else:
        processFatal("trying to get platform basic data with no captain available")

def getPlatformBasicDataOrCrash ():
    if _g_captain:
        data = _g_captain.getPlatformBasicData()
        if data is None:
            processFatal("trying to get platform basic data which is not available")
        return data
    else:
        processFatal("trying to get platform basic data with no captain available")

def getApplicationVersionUnsafe ():
    if _g_captain:
        return _g_captain.getApplicationVersion()
    else:
        processFatal("trying to get application version data with no captain available")

def getApplicationVersionOrCrash ():
    if _g_captain:
        data = _g_captain.getApplicationVersion()
        if data is None:
            processFatal("trying to get application version which is not available")
        return data
    else:
        processFatal("trying to get application version data with no captain available")

def getOsef ():
    if _g_captain:
        return _g_captain.getOsef()
    else:
        processFatal("trying to get OSEF no captain available")


G_NAME_MODULE_INFRA_PROCESS = "infra-process"
G_NAME_GROUP_INFRA_PROCESS_CAPTAIN = "captain"


