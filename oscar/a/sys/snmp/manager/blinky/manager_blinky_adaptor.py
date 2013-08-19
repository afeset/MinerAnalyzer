#
# Copyright Qwilt, 2013
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: naamas
# 

from a.infra.basic.return_codes import ReturnCodes

from a.sys.snmp.tech_snmp_manager.tech.snmp.blinky_snmp_gen import BlinkySnmp
from a.sys.snmp.tech_snmp_manager.tech.snmp.counters.blinky_counters_oper_gen import BlinkyOperCounters as BlinkySnmpOperCounters

from a.sys.snmp.manager.blinky.community_transformator import CommunityTransformator
from a.sys.snmp.manager.blinky.destination_transformator import DestinationTransformator
from a.sys.snmp.manager.blinky.counters_transformator import CountersTransformator
from a.sys.snmp.manager.blinky.snmp_transformator import SnmpTransformator


import a.sys.blinky.domain_priority

from xml.dom.minidom import *
import os


# Bypass for PyChecker
if  __package__ is None:
    G_GROUP_NAME_SNMP_MANAGER_BLINKY_ADAPTOR           = "unknown"
else:
    from . import G_GROUP_NAME_SNMP_MANAGER_BLINKY_ADAPTOR


class ManagerBlinkyAdaptor:

    def __init__ (self, logger, configDomain, dpDomain, maapiDomain):
        self._log = logger.createLoggerSameModule(G_GROUP_NAME_SNMP_MANAGER_BLINKY_ADAPTOR)
        self._configDomain = configDomain
        self._dpDomain = dpDomain
        self._maapiDomain = maapiDomain

        self._snmpTransformator = None
        self._countersTransformator = None
        self._communityTransformator = None
        self._destinationTransformator = None

        self._confdConfFile = None

    def createAndAttachBlinkySnmp(self, snmpManager):
        self._log("create-and-attach-blinky-snmp").debug1("called.")
        self._blinkySnmp = a.sys.snmp.tech_snmp_manager.tech.snmp.blinky_snmp_gen.BlinkySnmp.s_create(self._log, self._configDomain)

        res = self._attachToBlinkySnmp(self._blinkySnmp, snmpManager)
        if res != ReturnCodes.kOk:
            self._log("create-and-attach-blinky-snmp-attach-failed").error("self._attachToBlinkySnmp() failed.")
            return ReturnCodes.kGeneralError

        self._configDomain.registerNode(self._blinkySnmp)

        self._snmpTransformator = SnmpTransformator(self._log, self._dpDomain, self._maapiDomain, self._blinkySnmp)
        res = self._dpDomain.registerTransformationCallpoint(self._snmpTransformator.getCallpointName(), self._blinkySnmp, self._snmpTransformator.getRelativeKeyPath(), self._snmpTransformator)
        if res != ReturnCodes.kOk:
            self._log("create-and-attach-blinky-snmp-register-snmp-transformation-failed").error("self._dpDomain.registerTransformationCallpoint(snmp) failed.")
            return ReturnCodes.kGeneralError

        self._communityTransformator = CommunityTransformator(self._log, self._dpDomain, self._maapiDomain, self._blinkySnmp)
        res = self._dpDomain.registerTransformationCallpoint(self._communityTransformator.getCallpointName(), self._blinkySnmp, self._communityTransformator.getRelativeKeyPath(), self._communityTransformator)
        if res != ReturnCodes.kOk:
            self._log("create-and-attach-blinky-snmp-register-community-transformation-failed").error("self._dpDomain.registerTransformationCallpoint(community) failed.")
            return ReturnCodes.kGeneralError

        self._destinationTransformator = DestinationTransformator(self._log, self._dpDomain, self._maapiDomain, self._blinkySnmp, self._communityTransformator.getCommunityUtils())
        self._destinationTransformator.setSnmpManager(snmpManager)
        res = self._dpDomain.registerTransformationCallpoint(self._destinationTransformator.getCallpointName(), self._blinkySnmp, self._destinationTransformator.getRelativeKeyPath(), self._destinationTransformator)
        if res != ReturnCodes.kOk:
            self._log("create-and-attach-blinky-snmp-register-destination-transformation-failed").error("self._dpDomain.registerTransformationCallpoint(destination) failed.")
            return ReturnCodes.kGeneralError

        self._countersTransformator = CountersTransformator(self._log, self._maapiDomain)

        res = self._attachToBlinkySnmpCounters(self._dpDomain, self._blinkySnmp, snmpManager, self._countersTransformator)
        if res != ReturnCodes.kOk:
            self._log("create-and-attach-blinky-snmp-attach-counters-failed").error("self._attachToBlinkySnmpCounters() failed.")
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def _attachToBlinkySnmpCounters (self, dpDomain, blinkySnmp, snmpManager, countersTransformator):
        self._log("attach-to-blinky-snmp-counters").debug1("called. dpDomain=%s, blinkySnmp=%s", dpDomain, blinkySnmp)

        snmpManager.setReadSnmpCountersFunctor(countersTransformator.readSnmpCounters)

        blinkyOperCounters = BlinkySnmpOperCounters(self._log)
        blinkyOperCounters.setParent(blinkySnmp)
        blinkyOperCounters.setConfigObj(blinkySnmp)
        blinkyOperCounters.setDomain(dpDomain)
        blinkyOperCounters.setBasicFunctors(self._createFunctorSnmpCountersGetObj(snmpManager))                                       

        rc = blinkyOperCounters.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-snmp-counters-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-snmp-counters-done").debug1("done. dpDomain=%s, blinkySnmp=%s", dpDomain, blinkySnmp)
        return ReturnCodes.kOk

    def _createFunctorSnmpCountersGetObj (self, snmpManager):
        self._log("create-functor-snmp-counters-get-obj").debug2("created")

        def functorSnmpCountersGetObj (dpTrxContext, operData):
            self._log("functor-snmp-counters-get-obj").debug2("functor called. dpTrxContext=%s, operData=%s", dpTrxContext, operData)

            rc = snmpManager.getObjCountersOperData(dpTrxContext, operData)
            if rc != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError 

            return ReturnCodes.kOk

        return functorSnmpCountersGetObj

    def setConfdConfFile (self, confdConfFile):
        self._log("set-confd-conf-file").debug1("called. confdConfFile=%s", confdConfFile)
        self._confdConfFile = confdConfFile

    def _attachToBlinkySnmp (self, blinkySnmp, snmpManager):
        """ attaches the snmp manager to the given blinky snmp
        """
        self._log("attach-to-blinky-snmp").debug3("attaching")

        # regular container functors        
        blinkySnmp.setValueSetFunctor               (self._createFunctorSnmpValueSet(snmpManager))
        blinkySnmp.setNotifyTrxProgressFunctor      (self._createFunctorTrxProgress(snmpManager), True)
        blinkySnmp.setDestroySelfFunctor            (self._createFunctorSnmpDestroySelf(blinkySnmp, snmpManager)) 
        blinkySnmp.setCreateNotificationsFunctor    (self._createFunctorCreateNotifications(snmpManager))
        blinkySnmp.setCreateCommunityListFunctor    (self._createFunctorCreateCommunityList(snmpManager))
        blinkySnmp.setDoActionFunctor               (self._createFunctorClearSnmpCounters(snmpManager))
        blinkySnmp.setDestroySelfFunctor            (self._createFunctorSnmpDestroySelf(blinkySnmp, snmpManager))        

       # error message functor        
        snmpManager.setConfigMsgFunctor(lambda msgStr: blinkySnmp.setConfigErrorStr(msgStr))

        snmpManager.setEnableSnmpAgentFunctor(self.enableSnmpAgent)

        # active the blinky node
        rc = blinkySnmp.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-snmp-failed-activating").error("failed to activate")
            return ReturnCodes.kGeneralError 

        self._log("attach-to-blinky-snmp-activated").debug2("attached and activated")
        return ReturnCodes.kOk

#---------------------------------------------------------------------------------------------------------------------

    def enableSnmpAgent (self, enable, verifyOnly):
        """
        enables/disables snmp agent in confd.
        It writes the new configuration to the confd.conf file and ask confd to reload its configuration
        """
        self._log("enable-snmp-agent").debug2("called. enable=%s, verifyOnly=%s, self._confdConfFile=%s", enable, verifyOnly, self._confdConfFile)

        enabledStr = 'false'
        if enable:
            # set the snmpAgent enabled node to true
            enabledStr = 'true'

        try:
            dom = parse(self._confdConfFile)
        except:
            self._log("enable-snmp-agent-parse-file-failed").exception("failed to parse confd.conf xml file: %s", self._confdConfFile)
            return ReturnCodes.kGeneralError

        # get the "snmpAgent" node
        if not dom.getElementsByTagName("snmpAgent"):
            self._log("enable-snmp-agent-failed-get-snmp-agent").error("dom.getElementsByTagName(snmpAgent) failed. enable=%s, verifyOnly=%s", enable, verifyOnly)
            return ReturnCodes.kGeneralError
        snmpElem = dom.getElementsByTagName("snmpAgent")[0]
        if not snmpElem.getElementsByTagName("enabled"):
            self._log("enable-snmp-agent-failed-get-enabled").error("snmpElem.getElementsByTagName(enabled) failed. enable=%s, verifyOnly=%s", enable, verifyOnly)
            return ReturnCodes.kGeneralError

        # get the "enabled" node
        enabledElem = snmpElem.getElementsByTagName("enabled")[0]
        if not enabledElem.firstChild:
            self._log("enable-snmp-agent-failed-get-enabled-child").error("enabledElem.firstChild is none. enable=%s, verifyOnly=%s", enable, verifyOnly)
            return ReturnCodes.kGeneralError

        # check if the "enabled" value should change
        if enabledElem.firstChild.wholeText != enabledStr:
            enabledElem.firstChild.replaceWholeText(enabledStr)

            try:
                os.rename(self._confdConfFile, '%s.before_config' % self._confdConfFile)
                confdConfFileObj = open(self._confdConfFile, 'w')
                if not verifyOnly:
                    # in commit phase - write the new value
                    confdConfFileObj.write(dom.toxml())

                confdConfFileObj.close()

                if not verifyOnly:
                    # ask confd to reload the configuration
                    res = self._blinkySnmp.getDomain().confdReloadConfig()
                    if res != ReturnCodes.kOk:
                        self._log("enable-snmp-agent-reload-failed").error("confdReloadConfig() failed")
                        return ReturnCodes.kGeneralError
            except:
                self._log("enable-snmp-agent-open-file-failed").exception("failed to open confd.conf xml file: %s", self._confdConfFile)
                return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

#---------------------------------------------------------------------------------------------------------------------

    def _createFunctorSnmpValueSet (self, snmpManager):
        self._log("create-functor-snmp-value-set").debug2("created blinky-adapter functor")

        def functorSnmpValueSet (phase, snmpData):
            self._log("functor-snmp-value-set").debug2("functor called. phase=%s, snmpData=%s", phase, snmpData)
            if phase.isPreparePrivate():
                self._log("prepare-private-process").debug2("calling snmp manager's preparePrivateSnmpData()")
                rc = snmpManager.preparePrivateSnmpData(snmpData)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorSnmpValueSet

#---------------------------------------------------------------------------------------------------------------------

    def _createFunctorClearSnmpCounters (self, snmpManager):
        self._log("create-functor-clear-snmp-counters").debug2("created clear snmp counters functor")

        def functorClearSnmpCounters (userInfo, actionPoint, actionName, params, nParams):
            self._log("functor-clear-snmp-counters").debug2("functor called. userInfo=%s, actionPoint=%s, actionName=%s, params=%s, nParams=%s", userInfo, actionPoint, actionName, params, nParams)
            rc = snmpManager.clearSnmpCounters(userInfo)
            if rc != ReturnCodes.kOk:
                self._log("functor-clear-snmp-counters-snmp-manager-failed").error("snmpManager.clearSnmpCounters() failed. userInfo=%s, actionPoint=%s, actionName=%s, params=%s, nParams=%s", userInfo, actionPoint, actionName, params, nParams)
                return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorClearSnmpCounters

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorTrxProgress (self, snmpManager):
        def functorTrxProgress (progress):
            """ Calls snmpManager progress functors according to given progress """
            self._log("functor-trx-progress").debug1("functor called.  progress=%s", progress)

            if progress.isPreparePrivateBefore():
                rc = snmpManager.configStartTransaction()
                if rc!=ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            if progress.isPreparePrivateAfter():
                rc = snmpManager.configPreparePrivateAfter()
                if rc!=ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            if progress.isPreparePublicAfter():
                rc = snmpManager.configPreparePublicAfter()
                if rc!=ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            if progress.isCommitPublicBefore():
                rc = snmpManager.configCommitTransaction()
                if rc!=ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            if progress.isAbortPrivateAfter():
                rc = snmpManager.configAbortTransaction()
                if rc!=ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorTrxProgress

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorSnmpDestroySelf (self, blinkySnmp, snmpManager):
        self._log("create-destroy-self-functor").debug3("creating destroy-self functor")

        def functorDestroySelf (phase):
            self._log("functor-destroy").debug2("functor called. phase=%s", phase)

            if phase.isCommitPrivate():
                self._log("destroy-snmp-manager").debug1("commit destroying snmp-manager")
                snmpManager.destroy()
                blinkySnmp.deactivate()

            return ReturnCodes.kOk

        return functorDestroySelf

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorDescendantDestroySelf (self, blinkyObj):
        self._log("create-destroy-self-descendant-functor").debug3("creating destroy-self-descendant functor")

        def functorDestroySelfDescendant (phase):
            self._log("functor-destroy-descendant").debug2("functor called. phase=%s", phase)

            if phase.isCommitPrivate():
                blinkyObj.deactivate()

            return ReturnCodes.kOk

        return functorDestroySelfDescendant
#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorCreateCommunityList (self, snmpManager):
        self._log("create-functor-create-community-list").debug3("creating create-community-list functor")

        def functorCreateCommunityList (phase, blinkyCommunityList):
            self._log("functor-create-community-list").debug2("functor called. phase=%s, blinkyCommunityList=%s", phase, blinkyCommunityList)

            if phase.isCommitPrivate():
                self._log("create-community-list").debug1("commit creating community-list")
                blinkyCommunityList.setCreateFunctor(self._createFunctorCreateCommunity(snmpManager))
                blinkyCommunityList.setDeleteFunctor(self._createFunctorDeleteCommunity(snmpManager))
                blinkyCommunityList.setDestroySelfFunctor(self._createFunctorDescendantDestroySelf(blinkyCommunityList))
                res = blinkyCommunityList.activate()
                if res != ReturnCodes.kOk:
                    self._log("create-community-list-activate-failed").error("blinkyCommunityList.activate() failed. phase=%s, blinkyCommunityList=%s",
                                                                             phase, blinkyCommunityList)
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorCreateCommunityList

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorCreateNotifications (self, snmpManager):
        self._log("create-functor-create-notifications").debug3("creating create-notifications functor")

        def functorCreateNotificaitons (phase, blinkyNotifications):
            self._log("functor-create-notifications").debug2("functor called. phase=%s, blinkyNotifications=%s", phase, blinkyNotifications)

            if phase.isCommitPrivate():
                self._log("create-notifications").debug1("commit creating notifications")
                blinkyNotifications.setCreateDestinationListFunctor(self._createFunctorCreateDestinationList(snmpManager))
                blinkyNotifications.setDestroySelfFunctor(self._createFunctorDescendantDestroySelf(blinkyNotifications))
                res = blinkyNotifications.activate()
                if res != ReturnCodes.kOk:
                    self._log("create-notifications-activate-failed").error("blinkyNotifications.activate() failed. phase=%s, blinkyNotifications=%s",
                                                                            phase, blinkyNotifications)
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorCreateNotificaitons

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorCreateDestinationList (self, snmpManager):
        self._log("create-functor-create-destination-list").debug3("creating create-destination-list functor")

        def functorCreateDestinationList (phase, blinkyDestinationList):
            self._log("functor-create-destination-list").debug2("functor called. phase=%s, blinkyDestinationList=%s", phase, blinkyDestinationList)

            if phase.isCommitPrivate():
                self._log("create-destination-list").debug1("commit creating destination-list")
                blinkyDestinationList.setCreateFunctor(self._createFunctorCreateDestination(snmpManager))
                blinkyDestinationList.setDeleteFunctor(self._createFunctorDeleteDestination(snmpManager))
                blinkyDestinationList.setDestroySelfFunctor(self._createFunctorDescendantDestroySelf(blinkyDestinationList))
                res = blinkyDestinationList.activate()
                if res != ReturnCodes.kOk:
                    self._log("create-destination-list-activate-failed").error("blinkyDestinationList.activate() failed. phase=%s, blinkyDestinationList=%s",
                                                                               phase, blinkyDestinationList)
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorCreateDestinationList

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorCreateDestination (self, snmpManager):
        self._log("create-functor-create-destination").debug3("creating create-destinationfunctor")

        def functorCreateDestination (phase, key, blinkyDestination):
            self._log("functor-create-destination").debug2("functor called. phase=%s, key=%s, blinkyDestination=%s", phase, key, blinkyDestination)

            if phase.isCommitPrivate():
                self._log("create-destination").debug1("commit creating destination")
                res = snmpManager.commitPrivateAddDestination(key)
                if res != ReturnCodes.kOk:
                    self._log("delete-destination-remove-failed").error("snmpManager.commitPrivateAddDestination() failed. phase=%s, key=%s",
                                                                        phase, key)
                    return ReturnCodes.kGeneralError
                blinkyDestination.setValueSetFunctor(self._createFunctorDestinationValueSet(snmpManager, key))
                blinkyDestination.setDestroySelfFunctor(self._createFunctorDescendantDestroySelf(blinkyDestination))
                res = blinkyDestination.activate()
                if res != ReturnCodes.kOk:
                    self._log("create-destination-activate-failed").error("blinkyDestination.activate() failed. phase=%s, key=%s, blinkyDestination=%s",
                                                                          phase, key, blinkyDestination)
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorCreateDestination

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorDeleteDestination (self, snmpManager):
        self._log("create-functor-delete-destination").debug3("creating delete-destinationfunctor")

        def functorDeleteDestination (phase, key):
            self._log("functor-delete-destination").debug2("functor called. phase=%s, key=%s", phase, key)

            if phase.isCommitPrivate():
                self._log("delete-destination").debug1("commit deleting destination")
                res = snmpManager.commitPrivateRemoveDestination(key)
                if res != ReturnCodes.kOk:
                    self._log("delete-destination-remove-failed").error("snmpManager.commitPrivateRemoveDestination() failed. phase=%s, key=%s",
                                                                        phase, key)
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorDeleteDestination

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorCreateCommunity (self, snmpManager):
        self._log("create-functor-create-community").debug3("creating create-community functor")

        def functorCreateCommunity (phase, key, blinkyCommunity):
            self._log("functor-create-community").debug2("functor called. phase=%s, key=%s, blinkyCommunity=%s", phase, key, blinkyCommunity)

            if phase.isCommitPrivate():
                self._log("create-community").debug1("commit creating community")
                res = snmpManager.commitPrivateAddCommunity(key)
                if res != ReturnCodes.kOk:
                    self._log("create-community-remove-failed").error("snmpManager.commitPrivateAddCommunity() failed. phase=%s, key=%s",
                                                                      phase, key)
                    return ReturnCodes.kGeneralError
                blinkyCommunity.setValueSetFunctor(self._createFunctorCommunityValueSet(snmpManager, key))
                blinkyCommunity.setDestroySelfFunctor(self._createFunctorDescendantDestroySelf(blinkyCommunity))
                res = blinkyCommunity.activate()
                if res != ReturnCodes.kOk:
                    self._log("create-community-activate-failed").error("blinkyCommunity.activate() failed. phase=%s, key=%s, blinkyCommunity=%s",
                                                                        phase, key, blinkyCommunity)
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorCreateCommunity

#----------------------------------------------------------------------------------------------------------------------

    def _createFunctorDeleteCommunity (self, snmpManager):
        self._log("create-functor-delete-community").debug3("creating delete-community functor")

        def functorDeleteCommunity (phase, key):
            self._log("functor-delete-community").debug2("functor called. phase=%s, key=%s", phase, key)

            if phase.isCommitPrivate():
                self._log("delete-community").debug1("commit deleting community")
                res = snmpManager.commitPrivateRemoveCommunity(key)
                if res != ReturnCodes.kOk:
                    self._log("delete-community-remove-failed").error("snmpManager.commitPrivateRemoveCommunity() failed. phase=%s, key=%s",
                                                                      phase, key)
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorDeleteCommunity

#---------------------------------------------------------------------------------------------------------------------

    def _createFunctorDestinationValueSet (self, snmpManager, key):
        self._log("create-functor-destination-value-set").debug2("created blinky-adapter functor, key=%s", key)

        def functorDestinationValueSet (phase, destinationData):
            self._log("functor-destination-value-set").debug2("functor called. key=%s, phase=%s, destinationData=%s", key, phase, destinationData)
            if phase.isCommitPrivate():
                self._log("commit-private-destination").debug2("calling snmp manager's commitPrivateDestinationData()")
                rc = snmpManager.commitPrivateDestinationData(key, destinationData)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorDestinationValueSet

#---------------------------------------------------------------------------------------------------------------------

    def _createFunctorCommunityValueSet (self, snmpManager, key):
        self._log("create-functor-community-value-set").debug2("created blinky-adapter functor, key=%s", key)

        def functorCommunityValueSet (phase, communityData):
            self._log("functor-community-value-set").debug2("functor called. key=%s, phase=%s, communityData=%s", key, phase, communityData)
            if phase.isCommitPrivate():
                self._log("commit-private-community").debug2("calling snmp manager's commitPrivateCommunityData()")
                rc = snmpManager.commitPrivateCommunityData(key, communityData)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return functorCommunityValueSet

