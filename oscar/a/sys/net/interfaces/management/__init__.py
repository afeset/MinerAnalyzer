# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: yoave

from a.infra.basic.return_codes import ReturnCodes
#from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.management.management_data_gen import ManagementData

G_NAME_GROUP_NET_INTERFACES_MANAGEMENT = "management"

#-----------------------------------------------------------------------------------------------------------------------
class Management(object):
    """A generic management service object.
    """

    def __init__(self, logger):
        """
        Args:
            logger

        Raises:
            None
        """

        self.name = G_NAME_GROUP_NET_INTERFACES_MANAGEMENT
        self._log = logger.createLoggerSameModule(self.name)

        # data
        self.candidateEnabled = False
        self.runningEnabled = False

        self.blinkyMng =None
#-----------------------------------------------------------------------------------------------------------------------  
    def __str__(self):     
        return str("%s: %s" % (self.name, self.runningEnabled)) 

#-----------------------------------------------------------------------------------------------------------------------
    def notifyAttachToBlinky(self, blinkyMng):
        self.blinkyMng = blinkyMng

#-----------------------------------------------------------------------------------------------------------------------
    def preparePrivateValueSet(self, data):

        # we are successfull 
        self.candidateEnabled = data.enabled
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def commitPrivateValueSet(self, data):
        __pychecker__="no-argsused"  # data not used

        self.runningEnabled = self.candidateEnabled
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def abortPrivateValueSet(self, data):
        __pychecker__="no-argsused"  # data not used

        self.candidateEnabled = self.runningEnabled
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def isServiceEnabled(self):
        return self.candidateEnabled


