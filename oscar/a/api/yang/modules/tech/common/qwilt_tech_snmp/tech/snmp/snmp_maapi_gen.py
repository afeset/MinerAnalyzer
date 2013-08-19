


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes
from a.infra.misc.init_guard import InitGuard

from a.sys.confd.pyconfdlib.tag_values import TagValues
from a.sys.confd.pyconfdlib.value import Value
from a.sys.confd.pyconfdlib.key_path import KeyPath

from snmp_maapi_base_gen import SnmpMaapiBase

from a.api.yang.modules.tech.common.qwilt_tech_snmp.tech.snmp.system_defaults.system_defaults_maapi_gen import BlinkySystemDefaultsMaapi
from a.api.yang.modules.tech.common.qwilt_tech_snmp.tech.snmp.community.community_maapi_list_gen import BlinkyCommunityMaapiList
from a.api.yang.modules.tech.common.qwilt_tech_snmp.tech.snmp.notifications.notifications_maapi_gen import BlinkyNotificationsMaapi
from a.api.yang.modules.tech.common.qwilt_tech_snmp.tech.snmp.counters.counters_maapi_gen import BlinkyCountersMaapi



class BlinkySnmpMaapi(SnmpMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-snmp")
        self.domain = None

        
        self.systemDefaultsObj = None
        
        self.communityListObj = None
        
        self.notificationsObj = None
        
        self.countersObj = None
        

        
        self.enabledRequested = False
        self.enabled = None
        self.enabledSet = False
        
        self.contactRequested = False
        self.contact = None
        self.contactSet = False
        
        self.locationRequested = False
        self.location = None
        self.locationSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestEnabled(True)
        
        self.requestContact(True)
        
        self.requestLocation(True)
        
        
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.requestConfigAndOper()
        
        if not self.communityListObj:
            self.communityListObj = self.newCommunityList()
            self.communityListObj.requestConfigAndOper()
        
        if not self.notificationsObj:
            self.notificationsObj = self.newNotifications()
            self.notificationsObj.requestConfigAndOper()
        
        if not self.countersObj:
            self.countersObj = self.newCounters()
            self.countersObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestEnabled(True)
        
        self.requestContact(True)
        
        self.requestLocation(True)
        
        
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.requestConfig()
        
        if not self.communityListObj:
            self.communityListObj = self.newCommunityList()
            self.communityListObj.requestConfig()
        
        if not self.notificationsObj:
            self.notificationsObj = self.newNotifications()
            self.notificationsObj.requestConfig()
        
        if not self.countersObj:
            self.countersObj = self.newCounters()
            self.countersObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestEnabled(False)
        
        self.requestContact(False)
        
        self.requestLocation(False)
        
        
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.requestOper()
        
        if not self.communityListObj:
            self.communityListObj = self.newCommunityList()
            self.communityListObj.requestOper()
        
        if not self.notificationsObj:
            self.notificationsObj = self.newNotifications()
            self.notificationsObj.requestOper()
        
        if not self.countersObj:
            self.countersObj = self.newCounters()
            self.countersObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestEnabled(False)
        
        self.requestContact(False)
        
        self.requestLocation(False)
        
        
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.clearAllRequested()
        
        if not self.communityListObj:
            self.communityListObj = self.newCommunityList()
            self.communityListObj.clearAllRequested()
        
        if not self.notificationsObj:
            self.notificationsObj = self.newNotifications()
            self.notificationsObj.clearAllRequested()
        
        if not self.countersObj:
            self.countersObj = self.newCounters()
            self.countersObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setEnabled(None)
        self.enabledSet = False
        
        self.setContact(None)
        self.contactSet = False
        
        self.setLocation(None)
        self.locationSet = False
        
        
        if self.systemDefaultsObj:
            self.systemDefaultsObj.clearAllSet()
        
        if self.communityListObj:
            self.communityListObj.clearAllSet()
        
        if self.notificationsObj:
            self.notificationsObj.clearAllSet()
        
        if self.countersObj:
            self.countersObj.clearAllSet()
        

    def write (self
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(trxContext)

    def read (self
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(
                                  True,
                                  trxContext)

    def newSystemDefaults (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-systemdefaults').debug3Func(): logFunc('called.')
        systemDefaults = BlinkySystemDefaultsMaapi(self._log)
        systemDefaults.init(self.domain)
        return systemDefaults

    def setSystemDefaultsObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-systemdefaults').debug3Func(): logFunc('called. obj=%s', obj)
        self.systemDefaultsObj = obj

    def getSystemDefaultsObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-systemdefaults').debug3Func(): logFunc('called. self.systemDefaultsObj=%s', self.systemDefaultsObj)
        return self.systemDefaultsObj

    def hasSystemDefaults (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-systemdefaults').debug3Func(): logFunc('called. self.systemDefaultsObj=%s', self.systemDefaultsObj)
        if self.systemDefaultsObj:
            return True
        return False

    def newCommunityList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-communitylist').debug3Func(): logFunc('called.')
        communityList = BlinkyCommunityMaapiList(self._log)
        communityList.init(self.domain)
        return communityList

    def setCommunityListObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-communitylist').debug3Func(): logFunc('called. obj=%s', obj)
        self.communityListObj = obj

    def getCommunityListObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-communitylist').debug3Func(): logFunc('called. self.communityListObj=%s', self.communityListObj)
        return self.communityListObj

    def hasCommunityList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-communitylist').debug3Func(): logFunc('called. self.communityListObj=%s', self.communityListObj)
        if self.communityListObj:
            return True
        return False

    def newNotifications (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-notifications').debug3Func(): logFunc('called.')
        notifications = BlinkyNotificationsMaapi(self._log)
        notifications.init(self.domain)
        return notifications

    def setNotificationsObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-notifications').debug3Func(): logFunc('called. obj=%s', obj)
        self.notificationsObj = obj

    def getNotificationsObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-notifications').debug3Func(): logFunc('called. self.notificationsObj=%s', self.notificationsObj)
        return self.notificationsObj

    def hasNotifications (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-notifications').debug3Func(): logFunc('called. self.notificationsObj=%s', self.notificationsObj)
        if self.notificationsObj:
            return True
        return False

    def newCounters (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-counters').debug3Func(): logFunc('called.')
        counters = BlinkyCountersMaapi(self._log)
        counters.init(self.domain)
        return counters

    def setCountersObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-counters').debug3Func(): logFunc('called. obj=%s', obj)
        self.countersObj = obj

    def getCountersObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-counters').debug3Func(): logFunc('called. self.countersObj=%s', self.countersObj)
        return self.countersObj

    def hasCounters (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-counters').debug3Func(): logFunc('called. self.countersObj=%s', self.countersObj)
        if self.countersObj:
            return True
        return False



    def requestEnabled (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-enabled').debug3Func(): logFunc('called. requested=%s', requested)
        self.enabledRequested = requested
        self.enabledSet = False

    def isEnabledRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-enabled-requested').debug3Func(): logFunc('called. requested=%s', self.enabledRequested)
        return self.enabledRequested

    def getEnabled (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-enabled').debug3Func(): logFunc('called. self.enabledSet=%s, self.enabled=%s', self.enabledSet, self.enabled)
        if self.enabledSet:
            return self.enabled
        return None

    def hasEnabled (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-enabled').debug3Func(): logFunc('called. self.enabledSet=%s, self.enabled=%s', self.enabledSet, self.enabled)
        if self.enabledSet:
            return True
        return False

    def setEnabled (self, enabled):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-enabled').debug3Func(): logFunc('called. enabled=%s, old=%s', enabled, self.enabled)
        self.enabledSet = True
        self.enabled = enabled

    def requestContact (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-contact').debug3Func(): logFunc('called. requested=%s', requested)
        self.contactRequested = requested
        self.contactSet = False

    def isContactRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-contact-requested').debug3Func(): logFunc('called. requested=%s', self.contactRequested)
        return self.contactRequested

    def getContact (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-contact').debug3Func(): logFunc('called. self.contactSet=%s, self.contact=%s', self.contactSet, self.contact)
        if self.contactSet:
            return self.contact
        return None

    def hasContact (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-contact').debug3Func(): logFunc('called. self.contactSet=%s, self.contact=%s', self.contactSet, self.contact)
        if self.contactSet:
            return True
        return False

    def setContact (self, contact):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-contact').debug3Func(): logFunc('called. contact=%s, old=%s', contact, self.contact)
        self.contactSet = True
        self.contact = contact

    def requestLocation (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-location').debug3Func(): logFunc('called. requested=%s', requested)
        self.locationRequested = requested
        self.locationSet = False

    def isLocationRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-location-requested').debug3Func(): logFunc('called. requested=%s', self.locationRequested)
        return self.locationRequested

    def getLocation (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-location').debug3Func(): logFunc('called. self.locationSet=%s, self.location=%s', self.locationSet, self.location)
        if self.locationSet:
            return self.location
        return None

    def hasLocation (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-location').debug3Func(): logFunc('called. self.locationSet=%s, self.location=%s', self.locationSet, self.location)
        if self.locationSet:
            return True
        return False

    def setLocation (self, location):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-location').debug3Func(): logFunc('called. location=%s, old=%s', location, self.location)
        self.locationSet = True
        self.location = location


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.systemDefaultsObj:
            self.systemDefaultsObj._clearAllReadData()
        
        if self.communityListObj:
            self.communityListObj._clearAllReadData()
        
        if self.notificationsObj:
            self.notificationsObj._clearAllReadData()
        
        if self.countersObj:
            self.countersObj._clearAllReadData()
        

        
        self.enabled = 0
        self.enabledSet = False
        
        self.contact = 0
        self.contactSet = False
        
        self.location = 0
        self.locationSet = False
        

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("snmp", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", "qt-snmp"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       
                       readAllOrFail,
                       trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-read').debug3Func(): logFunc('called. PARAMS, readAllOrFail=%s', readAllOrFail)

        if readAllOrFail:
            self._clearAllReadData()

        tagValueList = TagValues()

        res = self._fillReadTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-fill-read-tag-value-failed').errorFunc(): logFunc('_fillReadTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(
                                       None)

        res = self.domain.readMaapi(tagValueList, keyPath, trxContext)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-domain-failed').errorFunc(): logFunc('domain.readMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        res = self._readTagValues(tagValueList, readAllOrFail)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-read-tag-values-failed').errorFunc(): logFunc('_readTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-read-done').debug3Func(): logFunc('done. PARAMS, readAllOrFail=%s', readAllOrFail)
        return ReturnCodes.kOk

    def _collectItemsToDelete (self,
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        
        if self.systemDefaultsObj:
            res = self.systemDefaultsObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.communityListObj:
            res = self.communityListObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-community-failed').errorFunc(): logFunc('communityListObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.notificationsObj:
            res = self.notificationsObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-notifications-failed').errorFunc(): logFunc('notificationsObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.countersObj:
            res = self.countersObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-counters-failed').errorFunc(): logFunc('countersObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasEnabled():
            valEnabled = Value()
            if self.enabled is not None:
                valEnabled.setBool(self.enabled)
            else:
                valEnabled.setEmpty()
            tagValueList.push(("enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"), valEnabled)
        
        if self.hasContact():
            valContact = Value()
            if self.contact is not None:
                valContact.setString(self.contact)
            else:
                valContact.setEmpty()
            tagValueList.push(("contact", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"), valContact)
        
        if self.hasLocation():
            valLocation = Value()
            if self.location is not None:
                valLocation.setString(self.location)
            else:
                valLocation.setEmpty()
            tagValueList.push(("location", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"), valLocation)
        

        
        if self.systemDefaultsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("system-defaults" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", "qt-snmp")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.systemDefaultsObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.communityListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("community" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", "qt-snmp")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.communityListObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-community-failed').errorFunc(): logFunc('communityListObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.notificationsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("notifications" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", "qt-snmp")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.notificationsObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-notifications-failed').errorFunc(): logFunc('notificationsObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.countersObj:
            valBegin = Value()
            (tag, ns, prefix) = ("counters" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", "qt-snmp")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.countersObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-counters-failed').errorFunc(): logFunc('countersObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isEnabledRequested():
            valEnabled = Value()
            valEnabled.setEmpty()
            tagValueList.push(("enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"), valEnabled)
        
        if self.isContactRequested():
            valContact = Value()
            valContact.setEmpty()
            tagValueList.push(("contact", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"), valContact)
        
        if self.isLocationRequested():
            valLocation = Value()
            valLocation.setEmpty()
            tagValueList.push(("location", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"), valLocation)
        

        
        if self.systemDefaultsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("system-defaults" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", "qt-snmp")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.systemDefaultsObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.communityListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("community" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", "qt-snmp")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.communityListObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-community-failed').errorFunc(): logFunc('communityListObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.notificationsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("notifications" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", "qt-snmp")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.notificationsObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-notifications-failed').errorFunc(): logFunc('notificationsObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.countersObj:
            valBegin = Value()
            (tag, ns, prefix) = ("counters" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", "qt-snmp")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.countersObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-counters-failed').errorFunc(): logFunc('countersObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isEnabledRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "enabled") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-enabled').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "enabled", "enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-enabled-bad-value').infoFunc(): logFunc('enabled not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setEnabled(tempVar)
            for logFunc in self._log('read-tag-values-enabled').debug3Func(): logFunc('read enabled. enabled=%s, tempValue=%s', self.enabled, tempValue.getType())
        
        if self.isContactRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "contact") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-contact').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "contact", "contact", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-contact-bad-value').infoFunc(): logFunc('contact not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setContact(tempVar)
            for logFunc in self._log('read-tag-values-contact').debug3Func(): logFunc('read contact. contact=%s, tempValue=%s', self.contact, tempValue.getType())
        
        if self.isLocationRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "location") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-location').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "location", "location", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-location-bad-value').infoFunc(): logFunc('location not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setLocation(tempVar)
            for logFunc in self._log('read-tag-values-location').debug3Func(): logFunc('read location. location=%s, tempValue=%s', self.location, tempValue.getType())
        

        
        if self.systemDefaultsObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "system-defaults") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.systemDefaultsObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "system-defaults") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.communityListObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "community") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "community", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.communityListObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-community-failed').errorFunc(): logFunc('communityListObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "community") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "community", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.notificationsObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "notifications") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "notifications", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.notificationsObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-notifications-failed').errorFunc(): logFunc('notificationsObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "notifications") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "notifications", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.countersObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "counters") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "counters", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.countersObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-counters-failed').errorFunc(): logFunc('countersObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "counters") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "counters", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "snmp", 
        "namespace": "snmp", 
        "className": "SnmpMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_snmp.tech.snmp.snmp_maapi_gen import SnmpMaapi", 
        "baseClassName": "SnmpMaapiBase", 
        "baseModule": "snmp_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "qt", 
            "yangName": "tech", 
            "namespace": "tech", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech", 
            "name": "tech"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-snmp", 
            "yangName": "snmp", 
            "namespace": "snmp", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "name": "snmp"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-snmp", 
            "memberName": "systemDefaults", 
            "yangName": "system-defaults", 
            "className": "BlinkySystemDefaultsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_snmp.tech.snmp.system_defaults.system_defaults_maapi_gen import BlinkySystemDefaultsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-snmp", 
            "memberName": "communityList", 
            "yangName": "community", 
            "className": "BlinkyCommunityMaapiList", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_snmp.tech.snmp.community.community_maapi_list_gen import BlinkyCommunityMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-snmp", 
            "memberName": "notifications", 
            "yangName": "notifications", 
            "className": "BlinkyNotificationsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_snmp.tech.snmp.notifications.notifications_maapi_gen import BlinkyNotificationsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-snmp", 
            "memberName": "counters", 
            "yangName": "counters", 
            "className": "BlinkyCountersMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_snmp.tech.snmp.counters.counters_maapi_gen import BlinkyCountersMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "contact", 
            "yangName": "contact", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "location", 
            "yangName": "location", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "common", 
            "qwilt_tech_snmp"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "contact", 
            "yangName": "contact", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "location", 
            "yangName": "location", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


