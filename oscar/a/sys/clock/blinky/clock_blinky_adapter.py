#!/usr/local/bin/python2.6
# 
# Copyright Qwilt, 2013
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: lenak

from a.infra.basic.return_codes import ReturnCodes
from a.sys.clock.manager.clock_manager_base import ClockManagerBase
from a.sys.clock.tech_system_clock.tech.system.clock.blinky_clock_gen import BlinkyClock

# Bypass for PyChecker
if  __package__ is None:
    G_NAME_MODULE_CLOCK_BLINKY_ADAPTER = "unknown"
    G_NAME_GROUP_CLOCK_BLINKY_ADAPTER = "unknown"
else:
    from . import G_NAME_MODULE_CLOCK_BLINKY_ADAPTER 
    from . import G_NAME_GROUP_CLOCK_BLINKY_ADAPTER

class ClockBlinkyAdapter(object):
    """ Manages Blinky Adapter

    Attributes:
        clockManager: managed clock manager cent os object
        blinkyClock: blinky node object
    """

    def __init__ (self, logger):
        self._log = logger.createLogger(G_NAME_MODULE_CLOCK_BLINKY_ADAPTER, G_NAME_GROUP_CLOCK_BLINKY_ADAPTER)
        self._clockManager = None
        self._blinkyClockConfig = None 


    def attachToBlinky (self, blinkyClockOper, blinkyClockConfig, clockManager):
        """ attaches the clock manager to the given blinky clock

        Args: 
            clockManager: managed clock manager cent os objsect
            blinkyClockOper: blinky oper node object
            blinkyClockConfig: blinky config node object
        Returns:
            ReturnCodes.kOk on success, ReturnCodes.kGeneralError otherwise
        """

        self._log("attach-to-blinky-clock").debug2("attachToBlinky() called: blinkyClockConfig=%s  blinkyClockOper=%s, clockManager=%s", 
                                                   blinkyClockConfig, blinkyClockOper, clockManager)

        rc = ReturnCodes.kOk
        self._clockManager = clockManager
        self._blinkyClockConfig = blinkyClockConfig

        if self._configAttachToBlinky() != ReturnCodes.kOk or self._operAttachToBlinky(blinkyClockOper) != ReturnCodes.kOk:
            self._log("attach-to-blinky-clock-failed-activating").error("attachToBlinky() failed ")
            rc = ReturnCodes.kGeneralError

        return rc

    def _configAttachToBlinky (self):
        """ attaches the clock manager to the config blinky node

        Returns:
            ReturnCodes.kOk on success, ReturnCodes.kGeneralError otherwise
        """

        self._log("config-attach-to-blinky-clock").debug2("_configAttachToBlinky() called")

        # functors        
        self._blinkyClockConfig.setValueSetFunctor (self._valueSetFunctor)
        self._blinkyClockConfig.setDestroySelfFunctor (self._destroySelfFunctor)        
        
        # activate the blinky node
        rc = self._blinkyClockConfig.activate()
        if rc != ReturnCodes.kOk:
            self._log("config-attach-to-blinky-clock-failed-activating").error("_configAttachToBlinky(): failed to activate blinky clock config. blinkyClockConfig=%s, clockManager=%s ", 
                                                                               self._blinkyClockConfig, self._clockManager)
            rc = ReturnCodes.kGeneralError
        return rc

    def _operAttachToBlinky (self, blinkyClockOper):
        """ attaches the clock manager to the oper blinky node

        Returns:
            ReturnCodes.kOk on success, ReturnCodes.kGeneralError otherwise
        """

        self._log("oper-attach-to-blinky-clock").debug2("_operAttachToBlinky() called")

        # functors
        blinkyClockOper.setBasicFunctors(self._clockManager.getObjectStatus)                                       

        # active the blinky node
        rc = blinkyClockOper.activate()
        if rc != ReturnCodes.kOk:
            self._log("oper-attach-to-blinky-clock-failed-activating").error("_operAttachToBlinky(): failed to activate blinky clock oper")
            rc = ReturnCodes.kGeneralError 
        return rc


    def _valueSetFunctor (self, phase, clockData):
        """ valueSet functor

        Args: 
            phase: transaction phase
            clockData: blinky data object
        Returns:
            ReturnCodes.kOk on success, ReturnCodes.kGeneralError otherwise
        """

        self._log("value-set-functor").debug3("valueSetFunctor() called. phase=%s, clockData=%s", phase, clockData)
        rc = ReturnCodes.kOk

        if phase.isPreparePrivate():
            self._log("prepare-private-process").debug3("valueSetFunctor(): prepare private phase")
            rc = self._clockManager.configBeginTrx()
            if rc == ReturnCodes.kOk:
                errString = self._clockManager.setCandidate(clockData)
                if errString != None:
                    self._log("prepare-private-err").info("valueSetFunctor(): setCandidate() returned an err string=%s", errString)
                    self._blinkyClockConfig.setConfigErrorStr(errString)
                    rc = ReturnCodes.kGeneralError

        elif phase.isCommitPrivate():
            self._log("commit-private-process").debug3("valueSetFunctor(): commit private phase")
            rc = self._clockManager.commitTrx()
            if rc != ReturnCodes.kOk:
                rc = ReturnCodes.kGeneralError

        elif phase.isAbortPrivate():
            self._log("abort-private-process").debug3("valueSetFunctor(): abort private phase")
            rc = self._clockManager.abortTrx()
            if rc != ReturnCodes.kOk:
                rc = ReturnCodes.kGeneralError

        self._log("value-set-functor").debug3("valueSetFunctor() ended: rc=%s", rc)
        return rc

    def _destroySelfFunctor (self, phase):
        """ destroySelf functor

        Args: 
            phase: transaction phase
        Returns:
            ReturnCodes.kOk
        """

        self._log("functor-destroy").debug3("functor called. phase=%s", phase)
        if phase.isCommitPrivate():
            self._blinkyClockConfig.deactivate()
        
        return ReturnCodes.kOk
