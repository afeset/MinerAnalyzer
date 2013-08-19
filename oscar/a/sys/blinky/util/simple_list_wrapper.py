# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: yoave

from a.infra.basic.return_codes import ReturnCodes
import common

if  __package__ is None:
    G_NAME_GROUP_BLINKY_UTIL_SIMPLE_LIST = "unknown"
else:
    from . import G_NAME_GROUP_BLINKY_UTIL_SIMPLE_LIST

class SimpleList(object):
    """This class holds a map of blinky real objects
        Note: Only for simple lists that has no containers nor data
    """

    def __init__ (self, logger, createObjectFunctor, fromKeyFunctor):
        """
        Args:
            logger
            createObjectFunctor -   Callable function that creats a new real object
                                    
                                    Func(logger, name)
                                    Args:
                                        logger
                                        name
                                    Return:
                                        object instance
                                        hasattr(obj,'attachToBlinky') == True
                                    Raise:
                                        a.sys.blinky.util.common.ConfigError

            fromKeyFunctor -        Callable function that converts the key to any hashable type
                                    Func(key)
                                    Args:
                                        key
                                    Return:
                                        object key
                                        hasattr(obj,'__eq__') == True
                                        hasattr(obj,'__hash__') == True
                                    Raise:
                                        None
        Raises:
            None
        """

        self._log = logger.createLoggerSameModule(G_NAME_GROUP_BLINKY_UTIL_SIMPLE_LIST)
        self.createObjectFunctor = createObjectFunctor 
        self.fromKeyFunctor = fromKeyFunctor
        self.blinkyList = None
        self.isOrdered = False

        # These maps map from a string to a Real object
        # map active objects
        self.objectMap = {}

        # map candidate objects (not yet active)
        # note: startTrx() is not called before 1st trx
        self.candidateObjectMap = {}

        # Support ordered-by user lists
        self.orderedObjectList = []
        self.candidateOrderedObjectList = []

#-----------------------------------------------------------------------------------------------------------------------
    def attachToBlinky(self, blinkyList):
        """
        The real node is attached to the blinky world
        """

        for logFunc in self._log("attach-to-blinky").debug1Func(): logFunc("start attach to blinky. blinkyList=%s", blinkyList)

        # phase 1: save the blinky node
        self.blinkyList = blinkyList

        # phase 2: its callbacks to the blinky node
        self.blinkyList.setCreateFunctor(self.create)
        self.blinkyList.setDeleteFunctor(self.delete)
        self.blinkyList.setNotifyTrxProgressFunctor(self.trxProgress, True)
        self.blinkyList.setDestroySelfFunctor(self.destroySelf)

        # If this is an ordered-by user list, set the moved-after functor
        if hasattr(self.blinkyList, 'setMovedAfterFunctor'):
            self.blinkyList.setMovedAfterFunctor(self.movedAfter)
            self.isOrdered = True

        for logFunc in self._log("init-blinky-activating").debug1Func(): logFunc("activating blinky. blinkyList=%s", blinkyList)

        # phase 3: notify blinky node it can activate these callbacks
        rc = self.blinkyList.activate()
        if (rc != ReturnCodes.kOk):
            for logFunc in self._log("init-blinky-activate-failed").errorFunc(): logFunc("activation has failed. blinkyList=%s", blinkyList)
            return ReturnCodes.kGeneralError

        for logFunc in self._log("init-blinky-activated").debug1Func(): logFunc("blinky was activated. blinkyList=%s", blinkyList)
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def trxProgress (self, progress):

        for logFunc in self._log("trx-progress").debug1Func(): logFunc("%s: Transaction progress", progress)

        if progress.isPreparePrivateBefore():
            self.startTrx()
        if progress.isCommitPrivateBefore():
            self.commitTrx()
        if progress.isAbortPrivateBefore():
            self.abortTrx()

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def create(self, phase, key, blinkyObject):
        for logFunc in self._log("create").debug1Func(): logFunc("%s: Create object <%s>", phase, key)

        name = self.fromKeyFunctor(key)

        if (phase.isPreparePrivate()):
            return self.preparePrivateOnCreate(name, blinkyObject)
        if (phase.isCommitPublic()):
            return self.commitPublicOnCreate(name, blinkyObject)

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def delete(self, phase, key):
        for logFunc in self._log("delete").debug1Func(): logFunc("%s: Delete object <%s>", phase, key)

        name = self.fromKeyFunctor(key)

        if (phase.isPreparePrivate()):
            return self.preparePrivateOnDelete(name)

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def startTrx(self):

        for logFunc in self._log("start-trx").debug3Func(): logFunc("start list transaction")

        # copy of the running configuration as the new candidate
        self.candidateObjectMap = self.objectMap.copy()
        self.candidateOrderedObjectList = list(self.orderedObjectList)


#-----------------------------------------------------------------------------------------------------------------------
    def commitTrx(self):

        for logFunc in self._log("commit-trx").debug3Func(): logFunc("commit list transaction")

        self.objectMap.clear()
        self.objectMap = self.candidateObjectMap
        self.candidateObjectMap = None

        self.orderedObjectList = self.candidateOrderedObjectList
        self.candidateOrderedObjectList = None

#-----------------------------------------------------------------------------------------------------------------------
    def abortTrx(self):

        for logFunc in self._log("abort-trx").debug3Func(): logFunc("abort list transaction")

        self.candidateObjectMap.clear()
        self.candidateObjectMap = None

        self.candidateOrderedObjectList = None
     
#-----------------------------------------------------------------------------------------------------------------------
    def preparePrivateOnCreate(self, name, blinkyObject):
        """creates a new real object"""
            
        if name in self.objectMap:
            for logFunc in self._log("object-exists").noticeFunc(): logFunc("object '%s' already exists", name)
            return ReturnCodes.kGeneralError

        if name in self.candidateObjectMap:
            for logFunc in self._log("object-recreated").noticeFunc(): logFunc("object '%s' already was created", name)
            return ReturnCodes.kGeneralError

        # create the new object 
        try:
            newObject = self.createObjectFunctor(self._log, name)
        except common.ConfigError as ex:
            for logFunc in self._log("object-invalid").errorFunc(): logFunc("Object '%s' is invalid: %s", name, ex)
            self.blinkyList.setConfigErrorStr(str(ex))
            return ReturnCodes.kGeneralError

        # attach real object to blinky
        rc = newObject.attachToBlinky(blinkyObject)
        if (rc != ReturnCodes.kOk):
            for logFunc in self._log("prepare-private-create-failed-init-blinky").errorFunc(): logFunc("attachToBlinky failed. name=%s", name)
            return ReturnCodes.kGeneralError

        # inserts the new object to the candidate
        self.candidateObjectMap[name] = newObject
        self.candidateOrderedObjectList.append(name)

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def commitPublicOnCreate(self, name, blinkyObject):
        """attaches the new real object to the blinky oper world"""
    
        if name not in self.candidateObjectMap:
            for logFunc in self._log("object-not-exists").noticeFunc(): logFunc("object '%s' does not exist. blinkyObject=%s", name, blinkyObject)
            return ReturnCodes.kGeneralError
    
        # attach real object to blinky oper
        newObject = self.candidateObjectMap[name]
        newObject.attachToBlinkyOper()
    
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def preparePrivateOnDelete(self, name):
        """deletes an existing object"""

        if not name in self.objectMap:
            for logFunc in self._log("object-not-exists").noticeFunc(): logFunc("object '%s' does not exist", name)
            return ReturnCodes.kGeneralError

        if not name in self.candidateObjectMap:
            for logFunc in self._log("object-redeleted").noticeFunc(): logFunc("object '%s' already was deleted", name)
            return ReturnCodes.kGeneralError

        # removes the object from the candidate
        del self.candidateObjectMap[name]
        self.candidateOrderedObjectList.remove(name)

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def destroySelf(self, phase):
        for logFunc in self._log("destroy-self").debug1Func(): logFunc("%s: Destroy object", phase)

        if (phase.isCommitPrivate()):
            # deactivate object blinky list
            rc = self.blinkyList.deactivate()

            if (rc != ReturnCodes.kOk):
                for logFunc in self._log("destroy-self-deactivate-failed").debug1Func(): logFunc("deactivate-failed.  rc=%s", rc)
                return  ReturnCodes.kOk

            self.blinkyList = None
            for logFunc in self._log("destroy-self-end").debug1Func(): logFunc("end")

        return  ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def movedAfter (self, phase, movedKey, afterKey):
        for logFunc in self._log("moved-after").debug1Func(): logFunc("movedAfter(): called. phase=%s, movedKey=%s, afterKey=%s", phase, movedKey, afterKey)
        if (phase.isPreparePrivate()):
            movedName = self.fromKeyFunctor(movedKey)
            self.candidateOrderedObjectList.remove(movedName)
            if afterKey:
                afterName = self.fromKeyFunctor(afterKey)
                afterNameIndex = self.candidateOrderedObjectList.index(afterName)
                self.candidateOrderedObjectList.insert(afterNameIndex+1, movedName)
            else:
                self.candidateOrderedObjectList.insert(0, movedName)
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def getObjectByKey(self, key, isRunning=True):
        """Returns a real object by key, or None if not found"""

        name = self.fromKeyFunctor(key)
        obj = None

        if isRunning:
            obj = self.objectMap.get(name)
        else:
            if not self.candidateObjectMap is None:
                obj = self.candidateObjectMap.get(name)

        return obj

#-----------------------------------------------------------------------------------------------------------------------
    def runningValues(self):
        if not self.isOrdered:
            return self.objectMap.values() 

        values = []
        for name in self.orderedObjectList:
            values.append(self.objectMap.get(name))
        return values

#-----------------------------------------------------------------------------------------------------------------------
    def candidateValues(self):
    
        if self.candidateObjectMap is None:
            # not in transaction, therefore the candidate is actually the running configuration
            return self.runningValues()

        if not self.isOrdered:
            return self.candidateObjectMap.values()

        values = []
        for name in self.candidateOrderedObjectList:
            values.append(self.candidateObjectMap.get(name))
        return values

    #-----------------------------------------------------------------------------------------------------------------------
    def __str__(self):

        strLines = []
        objectList = self.objectMap.values() 
        for obj in objectList:
            strLines.append("%s" % (obj))

        return '\n'.join(strLines)


class SimpleStringList(SimpleList):
    """This class holds a map of strings to blinky real objects"""

    def __init__ (self, logger, createObjectFunctor):
        # blinky key (a.sys.blinky.list_key.ListKey) to string
        fromKeyFunctor = lambda key: str(key)
        SimpleList.__init__(self, logger, createObjectFunctor, fromKeyFunctor)
