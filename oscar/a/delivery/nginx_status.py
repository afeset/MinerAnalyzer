#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: hagaia
# 

import utils

from a.infra.misc.enum_with_value import EnumWithValue

if  __package__ is None:
    G_NAME_MODULE_DELIVERY = "unknown"
    G_NAME_GROUP_DELIVERY_NGINX_STATUS = "unknown"
else:
    from . import G_NAME_MODULE_DELIVERY 
    from . import G_NAME_GROUP_DELIVERY_NGINX_STATUS

#-----------------------------------------------------------------
class CurrentOperation(EnumWithValue):

    """contains a single data member"""

    def __init__ (self, value, name):

        EnumWithValue.__init__(self, value, name) 

#-----------------------------------------------------------------
class CurrentOperationTypes(object):

    """ optional data members """

    kNoOperation     = CurrentOperation(0, "kNoOperation")

    kConfigOperation = CurrentOperation(1, "kConfigOperation")

    kStopOperation   = CurrentOperation(2, "kStopOperation")

#-----------------------------------------------------------------
class NginxStatus(object):


    def __init__ (self, name, logger):

        self.kOperStabilizationTimeMsec = 2000

        self.reset()

        self.__name = name
        self.__log = logger.createLogger(G_NAME_MODULE_DELIVERY, G_NAME_GROUP_DELIVERY_NGINX_STATUS) 

        # counts config updates causes nginx restart (oscar-update)
        self.updateConfigCounter = 0

        # counts number of nginx change in state from down to up
        self.nginxStartCounter = 0        

    #-----------------------------------------------------------------
    def reset (self):

        # Operational Status
        self.operStatus = False

        # If True restart nginx
        self.shouldRestartNginx = False

        # If True Nginx should reload configuration
        self.shouldReloadConfig = False

        # Nginx is during operation (config,end)
        self.operInProcess = CurrentOperationTypes.kNoOperation

        # If Nginx during operation, the attribute holds start operation time
        self.operStartTime = utils.TimesSerivce()

    #-----------------------------------------------------------------
    def startOperation (self, newOperation):

        if self.operInProcess != CurrentOperationTypes.kNoOperation:
            self.__log("err-oper-state").error("Try to start new operation - %s during operation - %s",newOperation,self.operInProcess)
            return False

        self.__log("new-oper").notice("Nginx Start New Operation - %s",newOperation)

        self.operInProcess = newOperation
        self.operStartTime.init()

        return True

    #-----------------------------------------------------------------
    def endOperation (self):

        self.__log("end-oper").notice("Nginx End Operation - %s",self.operInProcess)

        if self.operInProcess == CurrentOperationTypes.kNoOperation:
            self.__log("err-end-state").error("Try to End non valid operation")

        self.operInProcess = CurrentOperationTypes.kNoOperation
        self.operStartTime.reset()

        
    #-----------------------------------------------------------------
    def isOperInProgress (self):

        if (self.operInProcess == CurrentOperationTypes.kNoOperation):
            return False

        return True

    #-----------------------------------------------------------------
    def startNginxRestart (self):

        self.shouldRestartNginx = True
        self.__log("restart-nginx").notice("Start Nginx Restart!!")




