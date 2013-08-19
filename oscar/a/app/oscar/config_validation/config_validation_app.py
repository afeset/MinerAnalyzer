#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: naamas
# 

from a.infra.basic.return_codes import ReturnCodes
import a.infra.process
import time

from a.sys.blinky.domain_priority import DomainPriority
import a.sys.blinky.config_validation.validation.blinky_validation.blinky_blinky_validation_gen 
import a.sys.utils.configuration_allowed_file

#from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.interface_maapi_list_gen import BlinkyInterfaceMaapiList

G_NAME_MODULE_APP_OSCAR_CONFIG_VALIDATION = "config-validation-app"
G_NAME_GROUP_APP_OSCAR_CONFIG_VALIDATION_GENERAL = "general"

class ConfigValidationApp (object): 
    #"""This application is the daemon in-charge of blocking configuration changes when not all processes are up and running"""

    CONFIG_VALIDATION_STATUS_FILE = "config-validation-status-file"

    CONFIG_SECTION_CONFIG_VALIDATION = "config-validation"
    CONFIG_VAR_DISABLE_VALIDATION = "disable-validation"
    DEFAULT_DISABLE_VALIDATION = "False"

    SYSTEM_STATUS_ENABLE_TRX = "system-status-enable-trx"

    # default values 
    DEFAULT_SLEEP_TIME = 0.2

    def __init__ (self):
        self._log = None
        self.agent = None

        self.wasStopped = False
        self.sleepSecTime = self.DEFAULT_SLEEP_TIME

        self.systemStatusDirName = None
        self.configurationAllowedFile = None

        self.blinkyDomain = None
        self.blinkyValidationNode= None
        self.disableValidation = False

    @staticmethod
    def getSystemStatusEnableTrxStr ():
        return ConfigValidationApp.SYSTEM_STATUS_ENABLE_TRX

    def setDisableConfigValidation(self, disable):
        self.disableValidation = disable

    def setSystemStatusDir (self, dirName):
        self.systemStatusDirName = dirName

    def daemonControlInitLogger(self, logger):
        """Init the process logger to be used.

        Args:
            logger: a logger from which new loggers shall be created
        """

        self._log = logger.createLogger(G_NAME_MODULE_APP_OSCAR_CONFIG_VALIDATION, 
                                        G_NAME_GROUP_APP_OSCAR_CONFIG_VALIDATION_GENERAL)

        self.configurationAllowedFile = a.sys.utils.configuration_allowed_file.ConfigurationAllowedFile(self.systemStatusDirName, self._log)

        self._log("logger-net-manager").debug1("config validation logger init.")
             
    def  daemonControlInitBlinky(self, agent):
        """Init the process blinky to be used.

        Args:
            agent: a blinky agent
        """
        self._log("blinky-net-manager").debug1("net manager blinky init.")
        self.agent = agent
      
    def daemonControlInitExternalData(self, sysParamsCfg, specificParams):
        """Init the data provided from outside

        Args:
            sysParamsCfg: a contatiner holding the sys params base configuration 
            specificParams: a dictionary holding the data under the "SPECIFIC_PARAM_KEY_..."                                        
        """

        self._log("ext-data-config-validation").debug1("exteranl data init")
        self._log("params-cfg-config-validation").debug3("sysParamsCfg=%s, specificParams=%s", sysParamsCfg, specificParams)

        self.configValidationStatusFileName = specificParams[self.CONFIG_VALIDATION_STATUS_FILE]
        if not self.disableValidation:
            self.disableValidation = sysParamsCfg.getBool(self.CONFIG_SECTION_CONFIG_VALIDATION, 
                                                          self.CONFIG_VAR_DISABLE_VALIDATION, 
                                                          self.DEFAULT_DISABLE_VALIDATION)

    def validateTrx (self, tctx):
        __pychecker__='no-argsused'
        self._log("validat-trx").debug3('called. tctx=%s, configValidationStatusFileName=%s', tctx, self.configValidationStatusFileName)
        if self.disableValidation or tctx.getUserContext() == 'system':
            return ReturnCodes.kOk
        else:
            allowed = False
            try:
                allowed = self.configurationAllowedFile.readConfigurationAllowed()
            except Exception, err:
                self._log("validat-trx-read-failed").error('failed to read configuration allowed file. exception: %s', err)
                self.blinkyValidationNode.setTransError(tctx, "System is not fully up. Configuration is not allowed at the moment. Please try again in a few minutes.")
                return ReturnCodes.kGeneralError

            if allowed:
                self._log("validat-trx-enable").debug3('transactions are enabled')
                return ReturnCodes.kOk
            else:
                self._log("validat-trx-disable").notice('transactions are disabled')
                # TODO (naamas) - add error string (waiting for net_manager branch to collapse to main)
                self.blinkyValidationNode.setTransError(tctx, "System is not fully up. Configuration is not allowed at the moment. Please try again in a few minutes.")
                return ReturnCodes.kGeneralError

    def destroySelf (self, phase, blinkyNode):
        self._log("destroy-self").debug1("destroySelf() called, phase=%s", phase)
        if (phase.isCommitPrivate()):
            res = blinkyNode.deactivate()
            if (res != ReturnCodes.kOk):
                self._log("destroy-self-deactivate-failed").debug1("destroySelf() - deactivate-failed, phase=%s", phase)
                # This function should not fail
                return  ReturnCodes.kOk
            self._log("destroy-self-end").debug1("destroySelf() - end, phase=%s", phase)
        return ReturnCodes.kOk
      
    def destroySelfTech (self, phase):
        ret = self.destroySelf(phase, self.blinkyValidationNode)
        self.blinkyValidationNode = None
        return ret

    def attachToBlinky (self, modelPoint, blinkyObjCreator, destroySelfFunc):
        self._log("attach-to-blinky").notice("called. modelPoint=%s, blinkyObjCreator=%s, destroySelfFunc=%s", 
                                             modelPoint, blinkyObjCreator, destroySelfFunc)
        blinkyObj = blinkyObjCreator(self._log, self.blinkyDomain)
        blinkyObj.setValidateTrxFunctor(self.validateTrx)
        blinkyObj.setDestroySelfFunctor(destroySelfFunc)

        rc = blinkyObj.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-activate-failed").error("blinkyObj.activate(). modelPoint=%s, blinkyObjCreator=%s, destroySelfFunc=%s, blinkyObj=%s", 
                                                                modelPoint, blinkyObjCreator, destroySelfFunc, blinkyObj)
            return None

        self._log("attach-to-blinky-done").notice("done. modelPoint=%s, blinkyObjCreator=%s, destroySelfFunc=%s, blinkyObj=%s", 
                                                  modelPoint, blinkyObjCreator, destroySelfFunc, blinkyObj)

        #self.testMaapi()
        """
        rc = self.blinkyDomain.registerSnmp()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-register-snmp-failed").error("blinkyDomain.registerSnmp(). modelPoint=%s", modelPoint)
            return None

        ifIndexOid = [1, 3, 6, 1, 2, 1, 2, 2, 1, 1, 2]
        ifAdminStatusColRow = ("ifAdminStatus", [2])
        ifOperStatusColRow = ("ifOperStatus", [2])
        rc = self.blinkyDomain.sendSnmpTrap(None, "linkDown", oids=[ifIndexOid], colRows=[ifAdminStatusColRow, ifOperStatusColRow])
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-send-snmp-trap-failed").error("blinkyDomain.sendSnmpTrap(). modelPoint=%s", modelPoint)
            return None
        """

        return blinkyObj

    def testMaapi (self):

        self._log('test-maapi').debug3('called')

        #maapiDomain = self.agent.createMaapiDomain("config-validation-maapi")
        #maapiInterfaceList = BlinkyInterfaceMaapiList(self._log)



    def daemonControlSystemInit(self):
        """before launching the process - doing things other processes shall wait for"""

        self._log("launch-config-validation").notice("config validation has been launched.")
        
        # activate
        self.blinkyDomain = self.agent.createConfigDomain("config-validation", DomainPriority.kDummy)

        self.blinkyValidationNode = self.attachToBlinky("validation", 
                                                        a.sys.blinky.config_validation.validation.blinky_validation.blinky_blinky_validation_gen.BlinkyBlinkyValidation.s_create, 
                                                        self.destroySelfTech)
        if not self.blinkyValidationNode:
            a.infra.process.processFatal("%s: Failed to attach to blinky tech", G_NAME_MODULE_APP_OSCAR_CONFIG_VALIDATION)

        self.blinkyDomain.registrationDone()
 

    def daemonControlRun(self):
        """launching the process - actually do nothing till we stopped"""
        # run in an endless loop and triggered by confd events
        self.wasStopped = False
        while not self.wasStopped:
            time.sleep(self.sleepSecTime)

        # shutdown
        if self.blinkyDomain:
            self.blinkyDomain.shutdown()

        self._log("done-config-validation").notice("config validation has been terminated")

    def daemonControlStop(self):
        """stopping the process"""

        self._log("stop-config-validation").notice("config validation has been stopped.")
        self.wasStopped = True

