# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: yoave

from a.infra.basic.return_codes import ReturnCodes
#from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.content.analytics.analytics_data_gen import AnalyticsData
#from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.content.acquisition.acquisition_data_gen import AcquisitionData
#from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.content.delivery.delivery_data_gen import DeliveryData

G_NAME_GROUP_NET_INTERFACES_CONTENT_ANALYTICS = "analytics"
G_NAME_GROUP_NET_INTERFACES_CONTENT_ACQUISITION = "acquisition"
G_NAME_GROUP_NET_INTERFACES_CONTENT_DELIVERY = "delivery"

#############
# SERVICE   
#############
#-----------------------------------------------------------------------------------------------------------------------
class _BaseService(object):
    """a generic base service object.
    """

    def __init__(self, logger, name):
        """
        Args:
            logger

        Raises:
            None
        """

        self.name = name
        self._log = logger.createLoggerSameModule(name)

        # data
        self.candidateEnabled = False
        self.runningEnabled = False

        self.blinkyService = None

#-----------------------------------------------------------------------------------------------------------------------  
    def __str__(self):     
        return str("%s: %s" % (self.name, self.runningEnabled)) 

#-----------------------------------------------------------------------------------------------------------------------
    def notifyAttachToBlinky(self, blinkyService):
        self.blinkyService = blinkyService

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


#############
# ANALYTICS
#############
#-----------------------------------------------------------------------------------------------------------------------
class AnalyticsService(_BaseService):
    """Analytics service object.
    """

    def __init__(self, logger):
        """
        Args:
            logger

        Raises:
            None
        """

        _BaseService.__init__(self, logger, G_NAME_GROUP_NET_INTERFACES_CONTENT_ANALYTICS)

#############
# ACQUISITION
#############
#-----------------------------------------------------------------------------------------------------------------------
class AcquistionService(_BaseService):
    """Acquisition service object.
    """

    def __init__(self, logger):
        """
        Args:
            logger

        Raises:
            None
        """

        _BaseService.__init__(self, logger, G_NAME_GROUP_NET_INTERFACES_CONTENT_ACQUISITION)

#############
# DELIVERY
#############
#-----------------------------------------------------------------------------------------------------------------------
class DeliveryService(_BaseService):
    """Delivery service object.
    """

    def __init__(self, logger):
        """
        Args:
            logger

        Raises:
            None
        """

        _BaseService.__init__(self, logger, G_NAME_GROUP_NET_INTERFACES_CONTENT_DELIVERY)




