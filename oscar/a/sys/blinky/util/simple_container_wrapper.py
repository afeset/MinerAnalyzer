# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: yoave

from a.infra.basic.return_codes import ReturnCodes

if  __package__ is None:
    G_NAME_GROUP_BLINKY_UTIL_SIMPLE_OBJECT_WRAPPER = "unknown"
else:
    from . import G_NAME_GROUP_BLINKY_UTIL_SIMPLE_OBJECT_WRAPPER

class SimpleContainerWrapper(object):
    """This class wrapps a real container
        For simple objects that has no containers nor lists

        each phase will call its coressponding function in the real object (if exists)

        Example:
                
                obj.preparePrivateValueSet(data)
                obj.preparePublicValueSet(data) 
                obj.commitPrivateValueSet(data) 
                obj.commitPublicValueSet(data) 
                obj.abortPrivateValueSet(data) 
                obj.abortPublicValueSet(data) 
                 
                obj.preparePrivateDestroySelf() 
                obj.preparePublicDestroySelf() 
                obj.commitPrivateDestroySelf() 
                obj.commitPublicDestroySelf() 
                obj.abortPrivateDestroySelf() 
                obj.abortPublicDestroySelf()

        For objects that need oper callbacks

        Example:
                obj.getCounters(tctx, operData)
                obj.getStatus(tctx, operData) 

        For objects that need notification for transaction progress

        Example:
                
                obj.preparePrivateBefore()
                obj.preparePrivateAfter() 
                obj.preparePublicBefore()
                obj.preparePublicAfter()
                obj.commitPrivateBefore() 
                obj.commitPrivateAfter() 
                obj.commitPublicBefore() 
                obj.commitPublicAfter() 
                obj.abortPrivateBefore() 
                obj.abortPrivateAfter() 
                obj.abortPublicBefore() 
                obj.abortPublicAfter() 
                
            If object has additional data either container or list
            its possible to register additional callbacks

            Example:

            obj.notifyAttachToBlinky(blinkyObject)
    """

    def __init__ (self, logger, realObject, 
                  notifyTrxProgressFunctor=False, notifyDescendantsModifications=True,
                  setOperDataFunctor=False):
        """Instantiate a new wrapper object.

        Args:
            logger
            realObject - the real object that is wrapped
            notifyTrxProgressFunctor - should register notify trx progress functor
            notifyDescendantsModifications -  should notify on descendants modifications

        Raises:
            None
        """

        self._log = logger.createLoggerSameModule(G_NAME_GROUP_BLINKY_UTIL_SIMPLE_OBJECT_WRAPPER)
        self.realObject = realObject
        self.notifyTrxProgressFunctor = notifyTrxProgressFunctor
        self.notifyDescendantsModifications = notifyDescendantsModifications
        self.setOperDataFunctor = setOperDataFunctor
        self.blinkyObject = None

#-----------------------------------------------------------------------------------------------------------------------  
    def __str__(self):
        return str(self.realObject)

#-----------------------------------------------------------------------------------------------------------------------
    def __eq__(self, other):
        try:
            return (self.realObject == other.realObject)
        except AttributeError:
            return NotImplemented

#-----------------------------------------------------------------------------------------------------------------------
    def __iter__(self):
        return self.realObject.__iter__()
            
#-----------------------------------------------------------------------------------------------------------------------
    def __getattr__(self, name):
        # customize the meaning of attribute access
        # note: only works for new style classes i.e. those that inherit from object
        return getattr(self.realObject, name)

#-----------------------------------------------------------------------------------------------------------------------
    def attachToBlinky(self, blinkyObject):
        """here the real node is attached to the blinky world"""

        for logFunc in self._log("attach-to-blinky").debug1Func(): logFunc("attach to blinky - start")

        # phase 1 - save the blinky node
        self.blinkyObject = blinkyObject

        # phase 2 - give its callbacks to the blinky node

        # set value functor
        if hasattr(self.blinkyObject, 'setValueSetFunctor'):
            for logFunc in self._log("value-set-functor").debug3Func(): logFunc("ValueSet functor was registerd by %s", blinkyObject)
            self.blinkyObject.setValueSetFunctor(self.valueSet)

        if self.notifyTrxProgressFunctor:
            for logFunc in self._log("notify-trx-progress").debug3Func(): logFunc("NotifyTrxProgressFunctor was registered")
            blinkyObject.setNotifyTrxProgressFunctor(self.trxProgress, self.notifyDescendantsModifications)

        self.blinkyObject.setDestroySelfFunctor(self.destroySelf)
        self.blinkyObject.setAttachedObject(self)

        # in case real object need to register additional callbacks
        self._callAttribute('notifyAttachToBlinky', self.blinkyObject)

        # phase 3 - notify blinky node it can activate these callbacks 
        rc = self.blinkyObject.activate()
        if (rc != ReturnCodes.kOk):
            for logFunc in self._log("attach-to-blinky-activate-failed").errorFunc(): logFunc("activate failed")
            return ReturnCodes.kGeneralError

        for logFunc in self._log("attach-to-blinky").debug1Func(): logFunc("attach to blinky - end")

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def attachToBlinkyOper(self):
        """here the real node is attached to the blinky oper world"""

        for logFunc in self._log("attach-to-blinky-oper").debug1Func(): logFunc("attach to blinky oper - start. object=%s, blinky=%s", self.realObject, self.blinkyObject)

        # phase 1 - give its callbacks to the blinky oper node

        if self.setOperDataFunctor is True:
            # get status functor
            if hasattr(self.realObject, 'getStatus'):
                if hasattr(self.realObject, 'getBlinkyOperStatusObj'):
                    for logFunc in self._log("get-blinky-oper-status-obj").debug1Func(): logFunc("calling getBlinkyOperStatusObj on %s", self.realObject)
                    blinkyOperObj = self.realObject.getBlinkyOperStatusObj()
                    if hasattr(blinkyOperObj, 'setBasicFunctors'):
                        blinkyOperObj.setConfigObj(self.blinkyObject)
                        blinkyOperObj.setDomain(self.blinkyObject.getDomain())
                        blinkyOperObj.setBasicFunctors(self.realObject.getStatus)
                        rc = blinkyOperObj.activate()
                        if (rc != ReturnCodes.kOk):
                            for logFunc in self._log("attach-to-blinky-oper-activate-status-failed").errorFunc(): logFunc("blinkyOperObj.activate() failed. blinkyOperObj=%s", blinkyOperObj)
                            # not failing the transaction in commit phase
                            return

            # get counters functor
            if hasattr(self.realObject, 'getCounters'):
                if hasattr(self.realObject, 'getBlinkyOperCountersObj'):
                    for logFunc in self._log("get-blinky-oper-counters-obj").debug1Func(): logFunc("calling getBlinkyOperCountersObj on %s", self.realObject)
                    blinkyOperObj = self.realObject.getBlinkyOperCountersObj()
                    if hasattr(blinkyOperObj, 'setBasicFunctors'):
                        blinkyOperObj.setConfigObj(self.blinkyObject)
                        blinkyOperObj.setDomain(self.blinkyObject.getDomain())
                        blinkyOperObj.setBasicFunctors(self.realObject.getCounters)
                        rc = blinkyOperObj.activate()
                        if (rc != ReturnCodes.kOk):
                            for logFunc in self._log("attach-to-blinky-oper-activate-counters-failed").errorFunc(): logFunc("blinkyOperObj.activate() failed. blinkyOperObj=%s", blinkyOperObj)
                            # not failing the transaction in commit phase
                            return

            # get alarms functor
            if hasattr(self.realObject, 'getAlarms'):
                if hasattr(self.realObject, 'getBlinkyOperAlarmsObj'):
                    for logFunc in self._log("get-blinky-oper-alarms-obj").debug1Func(): logFunc("calling getBlinkyOperAlarmsObj on %s", self.realObject)
                    blinkyOperObj = self.realObject.getBlinkyOperAlarmsObj()
                    if hasattr(blinkyOperObj, 'setBasicFunctors'):
                        blinkyOperObj.setConfigObj(self.blinkyObject)
                        blinkyOperObj.setDomain(self.blinkyObject.getDomain())
                        blinkyOperObj.setBasicFunctors(self.realObject.getAlarms)
                        rc = blinkyOperObj.activate()
                        if (rc != ReturnCodes.kOk):
                            for logFunc in self._log("attach-to-blinky-oper-activate-alarms-failed").errorFunc(): logFunc("blinkyOperObj.activate() failed. blinkyOperObj=%s", blinkyOperObj)
                            # not failing the transaction in commit phase
                            return

            # in case real object need to register additional callbacks
            self._callAttribute('notifyAttachToBlinkyOper', self.blinkyObject)

        for logFunc in self._log("attach-to-blinky-oper").debug1Func(): logFunc("attach to blinky oper - end")

#-----------------------------------------------------------------------------------------------------------------------
    def _callAttribute(self, functAttr, *args, **kwargs):
        """This calls the coressponding function of the real object (if exists)"""

        if hasattr(self.realObject, functAttr):
            for logFunc in self._log("functor-call").debug2Func(): logFunc("%s: Functor %s is called, blinkyObject=%s",
                                             type(self.realObject), functAttr, self.blinkyObject)

            functor = getattr(self.realObject, functAttr)
            rc = functor(*args, **kwargs)
            
            for logFunc in self._log("functor-result").debug2Func(): logFunc("%s: Functor result code is %s", type(self.realObject), rc)

            return rc

        for logFunc in self._log("no-functor-call").debug3Func(): logFunc("%s: Functor %s does not exist, blinkyObject=%s",
                                            type(self.realObject), functAttr, self.blinkyObject)

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def _callByPhaseHelper(self, phaseName, funcPostfix, *args, **kwargs):
        """This calls the coressponding function of the real object (if exists)"""

        functAttr = "%s%s" % (phaseName, funcPostfix)
        return self._callAttribute(functAttr, *args, **kwargs)

#-----------------------------------------------------------------------------------------------------------------------
    def _callByPhase(self, phase, funcPostfix, *args, **kwargs):
        """This is a wrapper for a callback in each phase"""

        phaseName = None

        if (phase.isPreparePrivate()):
            phaseName = 'preparePrivate'
        elif (phase.isPreparePublic()):
            phaseName = 'preparePublic'
        elif (phase.isCommitPrivate()):
            phaseName = 'commitPrivate'
        elif (phase.isCommitPublic()):
            phaseName = 'commitPublic'
        elif (phase.isAbortPrivate()):
            phaseName = 'abortPrivate'
        elif (phase.isAbortPublic()):
            phaseName = 'abortPublic'

        if not phaseName is None:
            return self._callByPhaseHelper(phaseName, funcPostfix, *args, **kwargs)

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def valueSet(self, phase, data):
        """This callback is activated when a change was made to one (or more) ot the node's direct leaves"""

        for logFunc in self._log("object-value-set").debug1Func(): logFunc("%s: Set object %s data - %s", phase, type(self.realObject), data)
        rc = self._callByPhase(phase, 'ValueSet', data)
        return rc

#-----------------------------------------------------------------------------------------------------------------------
    def destroySelf(self, phase):
        """Called when the node is deleted. Need to detach from blinky in commit-private"""

        for logFunc in self._log("object-destroy-self").debug1Func(): logFunc("%s: Destory object %s", phase, type(self.realObject))

        if (phase.isCommitPrivate()):

            # deactivate blinky object
            rc = self.blinkyObject.deactivate()

            if (rc != ReturnCodes.kOk):
                for logFunc in self._log("destroy-self-deactivate-failed").errorFunc(): logFunc("deactivate-failed, phase=%s", phase)
                return  ReturnCodes.kOk

            self.blinkyObject = None
            for logFunc in self._log("destroy-self-end").debug1Func(): logFunc("end, phase=%s", phase)

        rc = self._callByPhase(phase, 'DestroySelf')
        return rc

#-----------------------------------------------------------------------------------------------------------------------
    def trxProgress (self, progress):

        for logFunc in self._log("trx-progress").debug2Func(): logFunc("object progress=%s", progress)

        functAttr = None

        # prepare progress
        if (progress.isPreparePrivateBefore()):
            functAttr = 'preparePrivateBefore'
        elif (progress.isPreparePrivateAfter()):
            functAttr = 'preparePrivateAfter'
        elif (progress.isPreparePublicBefore()):
            functAttr = 'preparePublicBefore'
        elif (progress.isPreparePublicAfter()):
            functAttr = 'preparePublicAfter'
        # commit progress
        elif (progress.isCommitPrivateBefore()):
            functAttr = 'commitPrivateBefore'
        elif (progress.isCommitPrivateAfter()):
            functAttr = 'commitPrivateAfter'
        elif (progress.isCommitPublicBefore()):
            functAttr = 'commitPublicBefore'
        elif (progress.isCommitPublicAfter()):
            functAttr = 'commitPublicAfter'
        # abort progress
        elif (progress.isAbortPrivateBefore()):
            functAttr = 'abortPrivateBefore'
        elif (progress.isAbortPrivateAfter()):
            functAttr = 'abortPrivateAfter'
        elif (progress.isAbortPublicBefore()):
            functAttr = 'abortPublicBefore'
        elif (progress.isAbortPublicAfter()):
            functAttr = 'abortPublicAfter'

        if not functAttr is None:
            return self._callAttribute(functAttr)

        return ReturnCodes.kOk

