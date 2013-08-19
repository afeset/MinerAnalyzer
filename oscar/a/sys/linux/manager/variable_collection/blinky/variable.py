#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

if  __package__ is None:
    G_NAME_MODULE_SYS_LINUX_MANAGER_VARIABLE_COLLECTION_BLINKY = "unknown"
    G_NAME_GROUP_SYS_LINUX_MANAGER_VARIABLE_COLLECTION_BLINKY_VARIABLE = "unknown"
else:
    from . import G_NAME_MODULE_SYS_LINUX_MANAGER_VARIABLE_COLLECTION_BLINKY
    from . import G_NAME_GROUP_SYS_LINUX_MANAGER_VARIABLE_COLLECTION_BLINKY_VARIABLE

from a.infra.basic.return_codes import ReturnCodes

from a.sys.linux.manager.variable_collection.blinky.tech_linux_variables.tech.linux_.variable_collection.variable.status.blinky_status_oper_gen import BlinkyOperStatus

import a.sys.mng.variable_collection.variable

class VariableHandler(object):
    def __init__ (self, logger, variable):
        varName = "none"
        if variable:
            varName = variable.getFullName()
        self._log=logger.createLogger(G_NAME_MODULE_SYS_LINUX_MANAGER_VARIABLE_COLLECTION_BLINKY, G_NAME_GROUP_SYS_LINUX_MANAGER_VARIABLE_COLLECTION_BLINKY_VARIABLE, 
                                      instance=varName)
        self._variable = variable
        self._blinkyVariable = None

    def isValidVar (self):
        return self._variable is not None

    def attachToBlinky(self, blinkyVariable):
        self._log("attach-to-blinky").debug1("attachToBlinky() called")
        self._blinkyVariable = blinkyVariable

        if self.isValidVar():
            self._blinkyVariable.setValueSetFunctor(self.valueSet)
            self._blinkyVariable.setDestroySelfFunctor(self.destroySelf)
        else:
            self._blinkyVariable.setValueSetFunctor(self.valueSetInvalidVar)
            self._blinkyVariable.setDestroySelfFunctor(self.destroySelfInvalidVar)

        rc = self._blinkyVariable.activate()
        if (rc != ReturnCodes.kOk):
            self._log("attach-to-blinky-activate-failed").debug2("activate() failed")
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def attachToBlinkyOper(self):
        self._log("attach-to-blinky-oper").debug1("attachToBlinkyOper() called")
        self._blinkyOperObj = BlinkyOperStatus(self._log)
        self._blinkyOperObj.setConfigObj(self._blinkyVariable)
        self._blinkyOperObj.setDomain(self._blinkyVariable.getDomain())
        if self.isValidVar():
            self._blinkyOperObj.setBasicFunctors(self.getStatus)
        else:
            self._blinkyOperObj.setBasicFunctors(self.getStatusInvalidVar)
        rc = self._blinkyOperObj.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-oper-activate-failed").error("blinkyOperObj.activate() failed. self._blinkyOperObj=%s", self._blinkyOperObj)
            return ReturnCodes.kGeneralError
    
        return ReturnCodes.kOk

    def valueSet(self, phase, data):
        self._log("value-set").debug2("valueSet() called, phase=%s, data=%s", phase, data)
        translatedData = a.sys.mng.variable_collection.variable.VariableData(data.name, data.value)
        if (phase.isPreparePrivate()):
            (rc, errorMsg) = self._variable.preparePrivateValueSet(translatedData)
            if errorMsg:
                self._log("prepare-error-message").error("prepare phase error msg: %s", errorMsg)
                self._blinkyVariable.setConfigErrorStr(errorMsg)
            if rc != ReturnCodes.kOk:
                self._log("prepare-failed").error("prepare cfg returned with rc = %s", rc)
                return ReturnCodes.kGeneralError

        elif (phase.isCommitPrivate()):
            rc = self._variable.commitPrivateValueSet(translatedData)
            if rc != ReturnCodes.kOk:
                self._log("commit-failed").error("commit cfg returned with rc = %s", rc)
                return ReturnCodes.kGeneralError

        # this return also covers phases that we don't need to support
        return ReturnCodes.kOk


    def destroySelf(self, phase):
        self._log("destroy-self").debug2("destroySelf() called, phase=%s", phase)

        if (phase.isCommitPublic()):
            rc = self._blinkyOperObj.deactivate()
            if rc!=ReturnCodes.kOk:
                self._log("destroy-self-oper-deactivate-failed").error("deleting variable %s _blinkyOperObj.deactivate() failed", self._variable.getFullName())
                #NOT returning failure code as we do not want to crash the process
        elif (phase.isCommitPrivate()):
            self._log("specific-commit-private-on-delete").debug4("deleting variable %s", self._variable.getFullName())
            rc = self._variable.commitPrivateOnDelete()
            if rc!=ReturnCodes.kOk:
                self._log("specific-commit-on-delete-failed").error("deleting variable %s operation failed", self._variable.getFullName())
                #NOT returning failure code as we do not want to crash the process

            rc = self._blinkyVariable.deactivate()
            if (rc != ReturnCodes.kOk):
                self._log("destroy-self-deactivate-failed").debug2("destroySelf(): deactivate() failed")
                # This function should not fail
                return ReturnCodes.kOk#returning Ok as in the real_person example
            self._blinkyVariable = None

        self._log("destroy-self-end").debug2("destroySelf(): end")

        # this return also covers phases that we don't need to support
        return ReturnCodes.kOk

    def valueSetInvalidVar(self, phase, data):
        self._log("value-set-invalid-var").debug2("valueSetInvalidVar() called, phase=%s, data=%s", phase, data)
        if (phase.isPreparePrivate()):
            if not self._blinkyVariable.isInTrigger():
                errorMsg = "Cannot change variable '%s': variable is not supported"%data.name
                self._log("prepare-failed-not-in-trigger").error("prepare cfg failed as we are not in trigger - %s",
                                                                  errorMsg)
                self._blinkyVariable.setConfigErrorStr(errorMsg)
                return ReturnCodes.kGeneralError
            else:
                self._log("prepare-invalid-var").debug1("prepare cfg for invalid variable %s",
                                                        data.name)
                
            return ReturnCodes.kOk

        elif (phase.isCommitPrivate()):
            self._log("commit-invalid-var").notice("Proposingly set the value of unavailble variable %s to %s",
                                                   data.name, data.value)
            return ReturnCodes.kOk

        # this return also covers phases that we don't need to support
        return ReturnCodes.kOk


    def destroySelfInvalidVar(self, phase):
        self._log("destroy-self-invalid-var").debug2("destroySelfInvalidVar() called, phase=%s", phase)

        if (phase.isCommitPrivate()):
            rc = self._blinkyVariable.deactivate()
            if (rc != ReturnCodes.kOk):
                self._log("destroy-self-invalid-var-deactivate-failed").debug2("destroySelfInvalidVar(): deactivate() failed")
                # This function should not fail
                return ReturnCodes.kOk#returning Ok as in the real_person example
            self._blinkyVariable = None
            self._log("destroy-self-invalid-var-end").debug2("destroySelfInvalidVar(): end")

        # this return also covers phases that we don't need to support
        return ReturnCodes.kOk


    def getStatus (self, tctx, operData):
        """
        This callback is activated when any of "status" container leaves is requested
        The operData will answer with 'True' when asked whether this field is requested
        Application code below should set the value for the requested field, but it can
        also set values for fields that were not requested. In the future this could be used
        for blinky internal optimizations
        """
        __pychecker__ = 'unusednames=tctx' 

        variableStatus = self._variable.getStatus()

        if operData.isActualValueRequested():
            actualValue = variableStatus.getActualValue()
            if actualValue is None:
                self._log("get-actual-value-not-set").error("trying to get variable actual value when it is not set. variable %s", self._variable.getFullName())
                return ReturnCodes.kGeneralError
            self._log("get-actual-value").debug2("got variable actual value. %s=%s", self._variable.getFullName(), actualValue)
            operData.setActualValue(actualValue)

        if operData.isInitialValueRequested():
            initialValue = variableStatus.getInitialValue()
            if initialValue is None:
                self._log("get-initial-value-not-set").error("trying to get variable initial value when it is not set. variable %s", self._variable.getFullName())
                return ReturnCodes.kGeneralError
            self._log("get-initial-value").debug2("got variable initial value. %s=%s", self._variable.getFullName(), initialValue)
            operData.setInitialValue(initialValue)        

        return ReturnCodes.kOk

    def getStatusInvalidVar (self, tctx, operData):
        """
        This callback is activated when any of "status" container leaves is requested
        The operData will answer with 'True' when asked whether this field is requested
        Application code below should set the value for the requested field, but it can
        also set values for fields that were not requested. In the future this could be used
        for blinky internal optimizations
        """
        __pychecker__ = 'unusednames=tctx' 

        if operData.isActualValueRequested():
            self._log("get-actual-value-invalid").notice("return actual value for invalid variable")
            operData.setActualValue("invalid")

        if operData.isInitialValueRequested():
            self._log("get-initial-value").notice("return initial value for invalid variable")
            operData.setInitialValue("invalid")        

        return ReturnCodes.kOk


