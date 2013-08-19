#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: shmulika
# 

from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.qwilt_tech_system_alarms_module_gen import AlarmNameType
from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.simulate.simulate_data_gen import SimulateData

from a.infra.basic.return_codes import ReturnCodes
import a.infra.time.monotonic_clock

# Bypass for PyChecker
if  __package__ is None:
    G_MODULE_NAME_ALARM_SOURCE                  = "unknown"
    G_GROUP_NAME_ALARM_SOURCE_BASE              = "unknown"
else:
    from . import G_MODULE_NAME_ALARM_SOURCE     
    from . import G_GROUP_NAME_ALARM_SOURCE_BASE        



class AlarmSourceError(Exception):
    """Error thrown when alarm source encountered an error"""
    def __init__ (self, msg):
        Exception.__init__(self, msg)


class AlarmInfo:
    """ Just the Necessary information, for issuing the alarm """
    def __init__ (self, name, entity, simulated, source):
        self.name = name
        self.entity = entity
        self.simulated = simulated
        self.source = source

    def __str__ (self):
        return "{AlarmInfo: (name = %s, entity = %s, simulated = %s, source = %s)}" % (self.name, self.entity, self.simulated, self.source) 
    


class AlarmSourceBase:
    """ Base class for all AlarmSources

    An AlarmSource is responsible for gathering information from a specific part of the system (e.g. disks, interafces, etc),
    most commonly from tables via MAAPI, checking that information and produce an alarm if required.
    The AlarmSource is operated by the AlarmManager, and returns any alarms to it.

    """

    def __init__ (self, logger, instanceName):
        self._log = logger.createLogger(G_MODULE_NAME_ALARM_SOURCE, G_GROUP_NAME_ALARM_SOURCE_BASE, instance = instanceName)
        self._maapiDomain = None
        self._instanceName = instanceName
        self._supportedAlarmNames = []
        self._staticMaapiList = None
        self._staticMaapiListKeys = None
        self._staticMaapiListTuplesKeyObject = None
        self._staticMaapiListInitialized = False
    

    def initSupportedAlarmNames (self):
        """ Adds all the supported alarms to the list, that is returned by method getDeclaredAlarms()

        This method is called at initialization of the object.

        Extensions of this class should implement this function, using the _addSupportedAlarmName() method.

        Returns: None
        Raises: None
        """
        pass


    def _pollUnsimulatedActiveAlarms (self):
        """ Produces and returns alarms that should be reported (not including simulated alarms)

        The AlarmSource should gather any information (from tables via MAAPI) required to check & produce the alarm.

        Extensions of this class should implement this function.

        Returns: list of AlarmInfo... [AlarmInfo]
        Raises: AlarmSourceError - if there was an error gathering alarms
        """
        raise AlarmSourceError("method _pollUnsimulatedActiveAlarms() must be implemented")


    def pollActiveAlarms (self, simulatedAlarms):
        """ Produces and returns alarms that should be reported.

        The AlarmSource should gather any information (from tables via MAAPI) required to check & produce the alarm.
        Must also produce and return alarms according to the given simulated alarms.

        Should not be overriden by extending classes.

        Arguments: simulatedAlarms - list of SimulateData... [SimulateData]
        Returns: list of AlarmInfo... [AlarmInfo]
        Raises: AlarmSourceError - if there was an error gathering alarms or creating simulated alarms
        """
        activeAlarms = self._pollUnsimulatedActiveAlarms()

        for simulatedAlarm in simulatedAlarms:
            if self.isSupportedAlarmName(simulatedAlarm.name):
                activeAlarms.append(self._createAlarmInfoFromSimulatedAlarm(simulatedAlarm))

        return activeAlarms


    def _createAlarmInfoFromSimulatedAlarm (self, simulatedAlarm):
        """ Creates and return an alarm according to the given simulated alarm

        Should not be overriden by extending classes.

        Arguments: simulatedAlarm of type SimulateData
        Returns: alarm of type AlarmInfo
        Raises: AlarmSourceError - if cannot create alarm according to the given simulated alarm
        """
        return self._newAlarmInfo(simulatedAlarm.name, simulatedAlarm.entity, simulated = True)


    def _newAlarmInfo (self, name, entity, simulated = False):
        """ Creates a new AlarmInfo object, with the given alarmName and entity
        Utility for 
        """
        alarmInfo = AlarmInfo(name, entity, simulated, self.getInstanceName())
        return alarmInfo


    def _addSupportedAlarmName (self, name):
        """ Adds a AlarmNameType that is added to the list of supported alarms, that is returned by method getDeclaredAlarms()
        To be used by extensions of this class, for conveniency.

        Should not be overriden by extending classes.

        Arguments:
            name - enum of AlarmNameType

        Returns: None
        Raises: None        
        """ 
        self._supportedAlarmNames.append(name)


    def getSupportedAlarmNames (self):
        """ Returns a list of all the declared alarms, that this source can generate.
        This includes declared alarms that cannot be activated yet (will be able to activate in later verions),
        Also includes declared alarms that are already deprecated

        Should not be overriden by extending classes.

        Returns: list of enums of AlarmNameType
        Raises: None
        """
        return self._supportedAlarmNames


    def isSupportedAlarmName (self, name):
        return name in self._supportedAlarmNames


    def getInstanceName (self):
        return self._instanceName


    def setMaapiDomain (self, maapiDomain):
        self._maapiDomain = maapiDomain


    def _getMaapiDomain (self):
        return self._maapiDomain

#-----------------------------------------------------------------------------#
    
class MaapiObject:
    def __init__ (self, logger, alarmSource):
        self._log = logger.createLogger(G_MODULE_NAME_ALARM_SOURCE, G_GROUP_NAME_ALARM_SOURCE_BASE)
        self._alarmSource = alarmSource
        self._initialized = False
        self._object = None

    def _initialize (self):
        if self._initialized:
            # already initialized
            return True

        if self._object is None:
            maapiDomain = self._alarmSource._getMaapiDomain()
            if maapiDomain is None:
                self._log("initialize-no-domain").debug1("can't init maapi object. domain not created yet")
                return False

            self._object = self._getMaapiObject(self._log)
            if self._object is None:
                self._log("intialize-not-created").warning("MaapiList object was not created by _getMaapiObject(), cannot initialize maapi object")
                return False

            # init the maapi list with the domain
            self._object.init(maapiDomain)            
            self._requestObject(self._object)                


        self._initialized = True
        self._log("intialize-done").debug1("Maapi object was initialized. object=%s", self._object)
        return True


    def get (self):
        """ gets the maapi object
        First call to this method initalizes the maapi object
        All calls read the updated values of the object
        Returns: the maapi object when successfull, None when failed
        """
        # try to initialize it (take cares of itself, does not initialize twice)
        if not self._initialize():
            self._log("get-failed-initializing").warning("Failed initializing the maapi object.")
            return None
                  
        timeElapsor = _TimeElapsor(self._log)  
        timeElapsor.set()  
        rc = self._object.read()
        self._log("get-elapsed-msec").debug2("reading the object took over %s msecs", timeElapsor.getElapsedMsecs())

        if rc != ReturnCodes.kOk:
            self._log("get-failed-reading").warning("Failed reading the maapi object.")
            return None

        self._log("get-done").debug2("returning the maapi object=%s", self._object)
        return self._object
    
    def _getMaapiObject (self, logger):
        """ Creates and returns a maapi object (Blinky generated) specific for the extension class.
        In failure cases - returns None.
        Failure does not cause immediate harm (further maapi operation will simply not occur).

        Extensions of this class should implement this function

        Returns: MaapiObject
        Raises: None
        """
        return None
               
    def _requestObject (self, object):
        """ Calls the extensions-specific request maapi fields """
        pass

#-----------------------------------------------------------------------------#

class StaticMaapiList:
    def __init__ (self, logger, alarmSource):
        # TODO(shmulika): change this to own group
        self._log = logger.createLogger(G_MODULE_NAME_ALARM_SOURCE, G_GROUP_NAME_ALARM_SOURCE_BASE)
        self._alarmSource = alarmSource
        self._initialized = False
        self._list = None
        self._keys = None
        self._tuplesKeyObject = None


    def _getKeys (self, maapiList):
        """ Takes an uninitialized MAAPI List object (generated by Blinky), and tries to read its keys.
        If read is successfull - returns a list of keys.
        If fails - returns None

        To be used by extension classes for convinient MAAPI access.
        """
        timeElapsor = _TimeElapsor(self._log)  
        timeElapsor.set()
        rc = maapiList.readListKeys()
        self._log("get-keys-elapsed-msec").debug2("reading the list keys took over %s msecs", timeElapsor.getElapsedMsecs())
        if rc != ReturnCodes.kOk:
            self._log("get-keys-failed").error("failed reading keys for maapi list")
            return None

        timeElapsor.set()
        keys = maapiList.getListKeys()
        self._log("get-keys-elapsed-msec").debug2("getting the list keys took over %s msecs", timeElapsor.getElapsedMsecs())
        self._log("get-keys").debug2("read keys from maapi list. keys = %s", keys)
        return keys


    def _initialize (self):
        """ Initializes the static maapi list (calls on extension-implemented method getSpecificMaapiListObject)
        Returns: True when successful, False when failed
        """
        if self._initialized:
            # already initialized
            return True

        if self._list is None:
            maapiDomain = self._alarmSource._getMaapiDomain()
            if maapiDomain is None:
                self._log("initialize-no-domain").debug1("can't get keys for maapi list. domain not created yet")
                return False

            self._list = self._getMaapiList(self._log)
            if self._list is None:
                self._log("intialize-not-created").warning("MaapiList object was not created by _getSpecificMaapiList(), cannot initialize static list")
                return False

            # init the maapi list with the domain
            self._list.init(maapiDomain)            

        if self._keys is None:
            self._keys = self._getKeys(self._list)
            if self._keys is None:
                self._log("intialize-failed-getting-keys").warning("Failed getting keys from MaapiList object, cannot initialize static list")
                return False
        
        if self._tuplesKeyObject is None:
            listKeyObject = []
            for key in self._keys:            
                mappiObject = self._getNewObject(self._list)            
                if mappiObject is None:
                    self._log("intialize-object-not-created").warning("Maapi object was not created by _getSpecificMaapiListNewObject(), cannot initialize static list")
                    return False
    
                self._requestObject(mappiObject)                
                self._setObject(self._list, key, mappiObject)
                listKeyObject.append((key, mappiObject))
    
            self._tuplesKeyObject = listKeyObject

        self._initialized = True
        self._log("intialize-done").debug1("Maapi static list was initialized. list=%s; tuple-keys-objects=%s", self._list, self._tuplesKeyObject)
        return True


    def get (self):
        """ gets a static maapi list (calls on extension-implemented method getSpecificMaapiListObject)
        First call to this method initalizes the list object, and gets all the keys via MAAPI
        All calls read the updated values for the keys in the list
        Returns: List of tuples [(key, MaapiObject)] when successfull, None when failed
        """
        # try to initialize it (take cares of itself, does not initialize twice)
        if not self._initialize():
            self._log("get-failed-initializing").warning("Failed initializing the static maapi list.")
            return None
                  
        timeElapsor = _TimeElapsor(self._log)  
        timeElapsor.set()
        rc = self._list.read()
        self._log("get-elapsed-msec").debug2("reading the list took over %s msecs", timeElapsor.getElapsedMsecs())
        if rc != ReturnCodes.kOk:
            self._log("get-failed-reading").warning("Failed reading the static maapi list.")
            return None


        self._log("get-done").debug2("returning static maapi tuple list of keys and objects. list=%s", self._tuplesKeyObject)
        return self._tuplesKeyObject

        
    def _getMaapiList (self, logger):
        """ Creates and returns a MaapiList object (Blinky generated) specific for the extension class.
        Used by the Static list handler methods of the base.
        In failure cases - returns None.
        Failure does not cause immediate harm (further static maapi operation will simply not occur).

        Extensions of this class should implement this function (if static maapi list functionality desired)

        Returns: MaapiList
        Raises: None
        """
        return None

    def _getNewObject (self, list):
        """ Calls the extension-specific MaapiList NewObject method. """
        return None

    def _requestObject (self, object):
        """ Calls the extensions-specific request maapi fields """
        pass

    def _setObject (self, list, key, object):
        """ Calls the extension-specific MaapiList setObject method. """
        pass

#-----------------------------------------------------------------------------#

class DynamicMaapiList:
    def __init__ (self, logger, alarmSource):
        # TODO(shmulika): change this to own group
        self._log = logger.createLogger(G_MODULE_NAME_ALARM_SOURCE, G_GROUP_NAME_ALARM_SOURCE_BASE)
        self._alarmSource = alarmSource
        self._initialized = False
        self._list = None
        self._keys = None
        self._tuplesKeyObject = None


    def _getKeys (self, maapiList):
        """ Takes an uninitialized MAAPI List object (generated by Blinky), and tries to read its keys.
        If read is successfull - returns a list of keys.
        If fails - returns None

        To be used by extension classes for convinient MAAPI access.
        """
        timeElapsor = _TimeElapsor(self._log)  
        timeElapsor.set()
        rc = maapiList.readListKeys()
        self._log("get-keys-elapsed-msec").debug2("reading the list keys took over %s msecs", timeElapsor.getElapsedMsecs())
        if rc != ReturnCodes.kOk:
            self._log("get-keys-failed").error("failed reading keys for maapi list")
            return None

        timeElapsor.set()
        keys = maapiList.getListKeys()
        self._log("get-keys-elapsed-msec").debug2("getting the list keys took over %s msecs", timeElapsor.getElapsedMsecs())
        self._log("get-keys").debug2("read keys from maapi list. keys = %s", keys)
        return keys


    def _initialize (self):
        """ Initializes the static maapi list (calls on extension-implemented method getSpecificMaapiListObject)
        Returns: True when successful, False when failed
        """
        if not self._initialized:
            # create the list object itself at first initialization, do not re-create it every time...
            maapiDomain = self._alarmSource._getMaapiDomain()
            if maapiDomain is None:
                self._log("initialize-no-domain").debug1("can't get keys for maapi list. domain not created yet")
                return False
    
            self._list = self._getMaapiList(self._log)
            if self._list is None:
                self._log("intialize-not-created").warning("MaapiList object was not created by _getSpecificMaapiList(), cannot initialize static list")
                return False
    
            # init the maapi list with the domain
            self._list.init(maapiDomain)            

        # the keys must be refreshed each time, because elements of the list might change.
        self._keys = self._getKeys(self._list)
        if self._keys is None:
            self._log("intialize-failed-getting-keys").warning("Failed getting keys from MaapiList object, cannot initialize static list")
            return False

        listKeyObject = []
        for key in self._keys:            
            mappiObject = self._getNewObject(self._list)            
            if mappiObject is None:
                self._log("intialize-object-not-created").warning("Maapi object was not created by _getSpecificMaapiListNewObject(), cannot initialize static list")
                return False

            self._requestObject(mappiObject)                
            self._setObject(self._list, key, mappiObject)
            listKeyObject.append((key, mappiObject))

        self._tuplesKeyObject = listKeyObject

        self._initialized = True
        self._log("intialize-done").debug1("Maapi static list was initialized. list=%s; tuple-keys-objects=%s", self._list, self._tuplesKeyObject)
        return True


    def get (self):
        """ gets a static maapi list (calls on extension-implemented method getSpecificMaapiListObject)
        First call to this method initalizes the list object, and gets all the keys via MAAPI
        All calls read the updated values for the keys in the list
        Returns: List of tuples [(key, MaapiObject)] when successfull, None when failed
        """
        # try to initialize it (take cares of itself, does not initialize twice)
        if not self._initialize():
            self._log("get-failed-initializing").warning("Failed initializing the static maapi list.")
            return None

        timeElapsor = _TimeElapsor(self._log)  
        timeElapsor.set()
        rc = self._list.read()
        self._log("get-elapsed-msec").debug2("reading the list took over %s msecs", timeElapsor.getElapsedMsecs())
        if rc != ReturnCodes.kOk:
            self._log("get-failed-reading").warning("Failed reading the static maapi list.")
            return None


        self._log("get-done").debug2("returning static maapi tuple list of keys and objects. list=%s", self._tuplesKeyObject)
        return self._tuplesKeyObject


    def _getMaapiList (self, logger):
        """ Creates and returns a MaapiList object (Blinky generated) specific for the extension class.
        Used by the Static list handler methods of the base.
        In failure cases - returns None.
        Failure does not cause immediate harm (further static maapi operation will simply not occur).

        Extensions of this class should implement this function (if static maapi list functionality desired)

        Returns: MaapiList
        Raises: None
        """
        return None

    def _getNewObject (self, list):
        """ Calls the extension-specific MaapiList NewObject method. """
        return None

    def _requestObject (self, object):
        """ Calls the extensions-specific request maapi fields """
        pass

    def _setObject (self, list, key, object):
        """ Calls the extension-specific MaapiList setObject method. """
        pass

#-----------------------------------------------------------------------------#

class _TimeElapsor:
    """ Convenient time counter utility, that simply tells you how much time has elapsed since setting it """
    def __init__ (self, logger):
        self._logger = logger        

        self._startTime = None

    def _secondsToNano (self, seconds):
        return 1000000000 * seconds

    def _nanoToSeconds (self, nanos):
        return float(nanos) / 1000000000.0

    def _nanoToMsecs (self, nanos):
        return float(nanos) / 1000000.0

    def set(self):
        self._startTime = a.infra.time.monotonic_clock.monotonicTimeNano()

    def getElapsedNanos (self):
        now = a.infra.time.monotonic_clock.monotonicTimeNano() 
        elapsed = now - self._startTime
        return elapsed

    def getElapsedSeconds (self):        
        return self._nanoToSeconds(self.getElapsedNanos())

    def getElapsedMsecs (self):        
        return self._nanoToMsecs(self.getElapsedNanos())








