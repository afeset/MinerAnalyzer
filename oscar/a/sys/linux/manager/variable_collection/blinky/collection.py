#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

if  __package__ is None:
    G_NAME_MODULE_SYS_LINUX_MANAGER_VARIABLE_COLLECTION_BLINKY = "unknown"
    G_NAME_GROUP_SYS_LINUX_MANAGER_VARIABLE_COLLECTION_BLINKY_COLLECTION = "unknown"
else:
    from . import G_NAME_MODULE_SYS_LINUX_MANAGER_VARIABLE_COLLECTION_BLINKY
    from . import G_NAME_GROUP_SYS_LINUX_MANAGER_VARIABLE_COLLECTION_BLINKY_COLLECTION

from a.infra.basic.return_codes import ReturnCodes

import variable

class CollectionHandler(object):
    def __init__ (self, logger, variableCollection):
        self._log=logger.createLogger(G_NAME_MODULE_SYS_LINUX_MANAGER_VARIABLE_COLLECTION_BLINKY, G_NAME_GROUP_SYS_LINUX_MANAGER_VARIABLE_COLLECTION_BLINKY_COLLECTION, 
                                      instance=variableCollection.getFullName())
        self._variableCollection = variableCollection
        self._blinkyVariableList = None
        self._variableHandlers = {} # a temporary container, holding newly created variable handlers until commit public where they are used for attachToBlinkyOper()

    def attachToBlinky(self, blinkyVariableList):
        self._log("attach-to-blinky").debug1("attachToBlinky(): blinkyVariableList=%s", blinkyVariableList)
        self._blinkyVariableList = blinkyVariableList
        self._blinkyVariableList.setCreateFunctor(self.prepareCandidateAddVariable)
        self._blinkyVariableList.setDeleteFunctor(self.prepareCandidateDeleteVariable)
        self._blinkyVariableList.setDestroySelfFunctor(self.destroySelf)
        self._blinkyVariableList.setNotifyTrxProgressFunctor(self.trxProgress, True)

        self._log("init-blinky-activating").debug1("attachToBlinky(): activating. blinkyVariableList=%s", blinkyVariableList)

        res = self._blinkyVariableList.activate()
        if (res != ReturnCodes.kOk):
            self._log("init-blinky-activate-failed").error("attachToBlinky(): activate-failed. blinkyVariableList=%s", blinkyVariableList)
            return ReturnCodes.kGeneralError

        self._log("init-blinky-activated").debug1("attachToBlinky(): activated. blinkyVariableList=%s", blinkyVariableList)
        return ReturnCodes.kOk


    def trxProgress (self, progress):
        self._log("trx-progress").debug1("trxProgress(): called.  progress=%s", progress)

        if progress.isPreparePrivateBefore():
            rc = self._variableCollection.configStartTransaction()
            if rc!=ReturnCodes.kOk:
                self._log("failed-start-transaction").error("failed to start transaction, rc=%s", rc)
                return ReturnCodes.kGeneralError

        if progress.isCommitPrivateAfter():
            rc = self._variableCollection.configCommitTransaction()
            if rc!=ReturnCodes.kOk:
                self._log("failed-commit-transaction").error("failed to commit transaction, rc=%s", rc)
                return ReturnCodes.kGeneralError

        if progress.isAbortPrivateAfter():
            rc = self._variableCollection.configAbortTransaction()
            if rc!=ReturnCodes.kOk:
                self._log("failed-abort-transaction").error("failed to abort transaction, rc=%s", rc)
                return ReturnCodes.kGeneralError

        # this return also covers phases that we don't need to support
        return ReturnCodes.kOk


    def prepareCandidateAddVariable(self, phase, key, blinkyVariable):
        self._log("create").debug1("create(): called. phase=%s, key=%s, blinkyVariable=%s", phase, key, blinkyVariable)

        if (phase.isPreparePrivate()):
            (rc, errorMsg) = self._variableCollection.prepareCandidateAddVariable(self._keyToName(key))

            isValidVar = True
            if errorMsg:
                self._log("prepare-add-error-message").error("prepare phase error msg on variable add: %s", errorMsg)
                if not blinkyVariable.isInTrigger():
                    self._blinkyVariableList.setConfigErrorStr(errorMsg)
            if rc != ReturnCodes.kOk:
                isValidVar = False
                self._log("prepare-failed").error("prepare cfg returned with error: %s", rc)
                if not blinkyVariable.isInTrigger():
                    return ReturnCodes.kGeneralError
                else:
                    pass
                    # not failing the transaction in order to allow the system to start
                    #but also not continue as the variable is not really in the list

            realVariable = None
            if isValidVar:
                realVariable = self._variableCollection.getCandidateVariable(self._keyToName(key))
                if realVariable is None:
                    self._log("prepare-no-var").error("prepare cfg returned but created no variable")
                    return ReturnCodes.kGeneralError

            variableHandler = variable.VariableHandler(self._log, realVariable)
            rc=variableHandler.attachToBlinky(blinkyVariable)
            if (rc != ReturnCodes.kOk):
                self._log("prepare-private-create-failed-init-blinky").error("create(): attachToBlinky() failed. phase=%s, key=%s", phase, key)
                return ReturnCodes.kGeneralError
            self._variableHandlers[self._keyToName(key)] = variableHandler

        elif (phase.isCommitPublic()):
            if not self._keyToName(key) in self._variableHandlers:
                self._log("commit-public-no-var-handler").error("variable handler not found. name=%s", key)
                # not failing the transaction in commit phase
                return ReturnCodes.kOk
            variableHandler = self._variableHandlers[self._keyToName(key)]
            rc = variableHandler.attachToBlinkyOper()
            if (rc != ReturnCodes.kOk):
                self._log("commit-public-create-failed-blinky-oper").error("create(): attachToBlinkyOper() failed. phase=%s, key=%s", phase, key)
                # not failing the transaction in commit phase
                return ReturnCodes.kOk
            # remove the handler from the container - it is only needed to attach the oper
            del self._variableHandlers[self._keyToName(key)]

        elif (phase.isAbortPublic()):
            if not self._keyToName(key) in self._variableHandlers:
                self._log("abort-public-no-var-handler").error("variable handler not found. name=%s", key)
                # not failing the transaction in commit phase
                return ReturnCodes.kOk
            # remove the handler from the container - it is only needed to attach the oper
            del self._variableHandlers[self._keyToName(key)]


        # this return also covers phases that we don't need to support
        return ReturnCodes.kOk

    def prepareCandidateDeleteVariable(self, phase, key):
        self._log("delete").debug1("prepareCandidateDeleteVariable(): called. phase=%s, key=%s", phase, key)
        if (phase.isPreparePrivate()):
            (rc, errorMsg) = self._variableCollection.prepareCandidateDeleteVariable(self._keyToName(key))
            if errorMsg:
                self._log("prepare-add-error-message").error("prepare phase error msg on variable add: %s", errorMsg)
            if rc!=ReturnCodes.kOk:
                self._log("prepare-failed").error("prepare cfg failed. rc=%s", rc)
                return ReturnCodes.kGeneralError

        # this return also covers phases that we don't need to support
        return ReturnCodes.kOk


    def destroySelf(self, phase):
        """
        Called when the node is deleted. Need to detach from blinky in commit-private
        """
        self._log("destroy-self").debug1("destroySelf(): called.  phase=%s", phase)
        if (phase.isCommitPrivate()):
            res = self._blinkyVariableList.deactivate()
            if (res != ReturnCodes.kOk):
                self._log("destroy-self-deactivate-failed").error("destroySelf(): deactivate-failed.  res=%s", res)
                # This function should not fail
                return  ReturnCodes.kOk

            self._blinkyVariableList = None
            self._log("destroy-self-end").debug1("destroySelf(): end")
        return  ReturnCodes.kOk

    def _keyToName (self, key):
        __pychecker__ = 'unusednames=self' 
        return str(key)

