# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: yoave

from a.infra.basic.return_codes import ReturnCodes
import service
from a.sys.blinky.util.simple_container_wrapper import SimpleContainerWrapper

G_NAME_GROUP_NET_INTERFACES_CONTENT = "content"

class Content(object):
    """This class represents a content service object"""

    def __init__ (self, logger):
        """Instantiate a new content service object.

        Args:
            logger

        Raises:
            None
        """

        self._log = logger.createLoggerSameModule(G_NAME_GROUP_NET_INTERFACES_CONTENT)

        self.analytics = None
        self.acquisition = None
        self.delivery = None

        self.blinkyContent = None

#-----------------------------------------------------------------------------------------------------------------------  
    def __str__(self):
        strList = []
        strList.append("analytics: %s" % self.analytics)
        strList.append("acquisition: %s" % self.acquisition)
        strList.append("delivery: %s" % self.delivery)

        return '\t'.join(strList) 


#-----------------------------------------------------------------------------------------------------------------------
    def notifyAttachToBlinky(self, blinkyContent):

        self._log("notify-attach-blinky").debug2("attach by blinky content")

        # analytics
        blinkyContent.setCreateAnalyticsFunctor(self.createAnalytics)
        blinkyContent.setDeleteAnalyticsFunctor(self.deleteAnalytics)

        # acquisition
        blinkyContent.setCreateAcquisitionFunctor(self.createAcquistion)
        blinkyContent.setDeleteAcquisitionFunctor(self.deleteAcquistion)

        # delivery
        blinkyContent.setCreateDeliveryFunctor(self.createDelivery)
        blinkyContent.setDeleteDeliveryFunctor(self.deleteDelivery)

        self.blinkyContent = blinkyContent

#-----------------------------------------------------------------------------------------------------------------------
    def setConfigErrorStr(self, msg):
        if self.blinkyContent:
            self.blinkyContent.setConfigErrorStr(msg)

#-----------------------------------------------------------------------------------------------------------------------
    def createAnalytics(self, phase, blinkyAnalytics):
        self._log("create-analytics").debug2("phase=%s, blinkyAnalytics=%s", phase, blinkyAnalytics)

        if (phase.isPreparePrivate()):

            analytics = service.AnalyticsService(self._log)
            self.analytics = SimpleContainerWrapper(self._log, analytics)
            self.analytics.attachToBlinky(blinkyAnalytics)

        elif (phase.isAbortPrivate()):
            self.analytics = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def deleteAnalytics(self, phase):
        self._log("delete-analytics").debug2("phase=%s", phase)

        if (phase.isCommitPrivate()):
            self.analytics = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def createAcquistion(self, phase, blinkyAcquistion):
        self._log("create-acquisition").debug2("phase=%s, blinkyAcquistion=%s", phase, blinkyAcquistion)

        if (phase.isPreparePrivate()):

            acquisition = service.AcquistionService(self._log)
            self.acquisition = SimpleContainerWrapper(self._log, acquisition)
            self.acquisition.attachToBlinky(blinkyAcquistion)

        elif (phase.isAbortPrivate()):
            self.acquisition = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def deleteAcquistion(self, phase):
        self._log("delete-acquisition").debug2("phase=%s", phase)

        if (phase.isCommitPrivate()):
            self.acquisition = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def createDelivery(self, phase, blinkyDelivery):
        self._log("create-delivery").debug2("phase=%s, blinkyDelivery=%s", phase, blinkyDelivery)

        if (phase.isPreparePrivate()):

            delivery = service.DeliveryService(self._log)
            self.delivery = SimpleContainerWrapper(self._log, delivery)
            self.delivery.attachToBlinky(blinkyDelivery)

        elif (phase.isAbortPrivate()):
            self.delivery = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def deleteDelivery(self, phase):
        self._log("delete-delivery").debug2("phase=%s", phase)

        if (phase.isCommitPrivate()):
            self.delivery = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def isLineEnabled(self):
        if ((not self.analytics is None) and (self.analytics.isServiceEnabled() is True)):
            return True

        if ((not self.acquisition is None) and (self.acquisition.isServiceEnabled() is True)):
            return True

        return False

#-----------------------------------------------------------------------------------------------------------------------
    def isDeliveryEnabled(self):
        if self.delivery is None:
            return False

        return self.delivery.isServiceEnabled()

#-----------------------------------------------------------------------------------------------------------------------
    def preparePrivateAfter(self):
        """all content services are being evaluated and verified for correctness system-wise"""

        self._log("content-prepare-private-after").debug3("Content: preparePrivateAfter was called")

        # delivey and line cannot coexist
        if self.isDeliveryEnabled() is True:
  
            if self.isLineEnabled() is True:
                self._log("delivery-and-line").error("Delivey and Line cannot coexist")
                self.setConfigErrorStr("Delivey and Analytics/Acquisition is not supported")
                return ReturnCodes.kGeneralError

        elif self.isLineEnabled() is True:

            # cannot acquire without analytics
            if not ((self.analytics.isServiceEnabled() is True) and (self.acquisition.isServiceEnabled() is True)):
                self._log("acquire-without-analytics").error("Cannot acquire without analytics")
                self.setConfigErrorStr("Acquisition without Analytics is not supported")
                return ReturnCodes.kGeneralError
            
        return ReturnCodes.kOk 
