#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

G_NAME_MODULE_SYS_LINUX_MANAGER_ = "linux-manager"
G_NAME_GROUP_SYS_LINUX_MANAGER_GENERAL = "general"
G_NAME_GROUP_SYS_LINUX_MANAGER_VARIABLE_COLLECTION = "var-collection"

import time
import os
from a.infra.basic.return_codes import ReturnCodes
import a.sys.blinky.domain_priority
import a.sys.mng.variable_collection.collection
import variable_collection.blinky.collection

from a.sys.linux.manager.variable_collection.blinky.tech_linux_variables.tech.linux_.variable_collection.variable.blinky_variable_list_gen import BlinkyVariableList
     
class Manager:
    DEFAULT_SLEEP_TIME = 0.1

    def __init__ (self):
        self._domain = None
        self._wasStopped = False

    def initLogger (self, logger):
        self._log = logger.createLogger(G_NAME_MODULE_SYS_LINUX_MANAGER_, 
                                        G_NAME_GROUP_SYS_LINUX_MANAGER_GENERAL)
        self._logVarCollection = logger.createLogger(G_NAME_MODULE_SYS_LINUX_MANAGER_, 
                                                     G_NAME_GROUP_SYS_LINUX_MANAGER_VARIABLE_COLLECTION)

    def initSysVarDir (self, dirName):
        self._sysVarDir = dirName
        self._variableCollectionOrigDataDir = os.path.join(self._sysVarDir, "state", "variable-collection", "orig")

    def attachToBlinky (self, blinkyAgent):
        self._log("attach").debug1("attaching to blinky")
        self._domain = blinkyAgent.createConfigDomain("linux-manager", a.sys.blinky.domain_priority.DomainPriority.kApplicationDefault)
        if not self._attachToCfgPathVariableCollections(self._domain, "/proc", "0", "proc"):
            self._log("failed-attach-proc").error("failed attaching to blinky 'proc' variable collection")
            a.infra.process.processFatal("Failed attaching to blinky")
        if not self._attachToCfgPathVariableCollections(self._domain, "/sys", "0", "sys"):
            self._log("failed-attach-proc").error("failed attaching to blinky 'sys' variable collection")
            a.infra.process.processFatal("Failed attaching to blinky")        
        self._domain.registrationDone()
        rc = self._domain.triggerSubscriptions()
        if (rc != ReturnCodes.kOk):
            self._log("trigger-failed").error("failed to trigger subscription for linux manager domain")
            #NOT a fatal as we don't want this module to fail the system


    def launch (self):
        while not self._wasStopped:
            time.sleep(self.DEFAULT_SLEEP_TIME)
        self._deattachFromBlinky()

    def stop (self):
        self._log("stopped").debug1("rising 'wasStopped' flag")
        self._wasStopped = True

    def _deattachFromBlinky (self):
        self._log("deattach").debug1("deattaching from blinky")
        self._domain.shutdown()
        return True

    def _attachToCfgPathVariableCollections (self, domain, path, linuxId, collectionId):
        self._logVarCollection("attach").debug1("attaching '%s' variable collection manager to cfg under '%s %s'", path, linuxId, collectionId)
        pathCollection = a.sys.mng.variable_collection.collection.PathVariablesCollection(self._logVarCollection, path)
        pathCollection.initUseOrigValuesFile(os.path.join(self._variableCollectionOrigDataDir, ".".join([linuxId, collectionId])+".json"))
        blinkyVariableList = BlinkyVariableList.s_create(self._logVarCollection, collectionId, linuxId, domain)
        collectionHandler = variable_collection.blinky.collection.CollectionHandler(self._log, pathCollection)        
        rc = collectionHandler.attachToBlinky(blinkyVariableList)
        if (rc != ReturnCodes.kOk):
            self._log("attach-failed").error("attach failed. path=%s, linuxId=%s, collectionId=%s", path, linuxId, collectionId)
            return False
        self._domain.registerNode(blinkyVariableList)
        return True

    def createDirs (self):
        if not os.path.exists(self._variableCollectionOrigDataDir):
            os.makedirs(self._variableCollectionOrigDataDir)

