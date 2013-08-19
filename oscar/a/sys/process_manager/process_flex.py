#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

import os
import shutil
import a.infra.file.utils
import a.infra.process
import a.sys.process.captain
import a.infra.log.main_logger_blinky
import common
from process_base import ProcessBase, StateMachine

class ProcessFlex(ProcessBase):
    def __init__ (self, name, logger):
        ProcessBase.__init__(self, name, logger)
        self._lastWatchdogMark = None
        self._actualState = None
        self._desiredState = None

    def initBlinky (self, blinky, pmBlinkyData, pmBlinkyCopy):
        self._blinky = blinky
        self._pmBlinkyData = pmBlinkyData
        self._pmBlinkyCopy = pmBlinkyCopy

#---------------------------------------------------------------------------------------------
    def updateStatus (self):
        actualState = self._pmBlinkyCopy.getActualState()
        if actualState is not None:
            #existing process
            self._prevActualState = self._actualState
            if actualState != common.ProcessState.DOWN:
                if not self._getIsRunning():
                    #thought the process is a live - but found out that it is down...
                    self._actualState=common.ProcessState.DOWN
                    self._pmBlinkyCopy.writeActualState(self._actualState)
                else:
                    self._actualState = actualState                   
                
                if self._actualState!=self._prevActualState:
                    self._log("flex-actual-state-changed").debug1("process '%s' actual state changed from '%s' to '%s'", 
                                                                   self.getName(), self._prevActualState, self._actualState)

        else:
            #first run/ new process
            self._actualState = common.ProcessState.DOWN
            self._prevActualState = common.ProcessState.DOWN
            self._desiredState = common.ProcessState.DOWN
            self._pmBlinkyCopy.writeActualState(self._actualState)
            self._log("flex-actual-state-first").debug1("process '%s' initial actual/prev/desired state were set to the default 'down'", 
                                                        self.getName())

        self._log("flex-update-status").debug5("process '%s' updateStatus resulted with actual-state = %s", self.getName(), self._actualState)

        self._testWatchdog()

    def _testWatchdog (self):
        self._log("flex-test-watchdog").debug5("process '%s' test watchdog", self.getName())
        mark = self._pmBlinkyCopy.getWatchdogMark()
        if mark != self._lastWatchdogMark:
            self._log("kicking-the-wd").debug4("watchdog was kicked on state '%s'", self._stateMachine.getState())
            self._timer.kick()

    def getDesiredState (self):        
        return self._desiredState

    def getActualState(self):
        return self._actualState

    def _getPrevActualState (self):
        return self._prevActualState

    def _getInitialMachineState (self):
        return StateMachine.DOWN #TODO(nirs) trivial implementation - will change when PM need to recover from failure

    def _setDesiredState (self, state):        
        self._desiredState = state
        self._pmBlinkyCopy.writeDesiredState(self._desiredState)


    def getProcessType(self):
        return self._pmBlinkyCopy.getProcessType()

    def getIsBlocking(self):
        return False

    def getMinLevelPmCanTakeDown (self):
        return common.ProcessState.DOWN


    def _getCommandLine (self):
        cmd = [self._getExecutable()]
        if self._getInitParamFilesDir() is not None:
            cmd+=[a.infra.process.captain.Captain.OPTION_INIT_PARAM_FILES_DIR_STR, self._getInitParamFilesDir()]
        if self._getExtraArgs() is not None:
            cmd+=[self._getExtraArgs().split()]
        return cmd        
    
    def _getExecutable (self):
        return self._pmBlinkyCopy.getExecutable()

    def _getExtraArgs (self):
        return self._pmBlinkyCopy.getExtraArgs()

    def _getRedirectDir (self):
        return self._pmBlinkyCopy.getRedirectDir()

    def _getCwd (self):
        return self._pmBlinkyCopy.getCwd()

    def _getOsEnv (self):
        #in flex processes the os-env is set at the agent
        return None

    def _getAffinity (self):
        #in flex processes the affinity is set at the agent
        return None

    def _getChrootDir (self):
        #in flex processes the root dir is set at the agent
        return None

    def _getInitParamFilesDir (self):
        return self._pmBlinkyCopy.getInitParamFilesDir()

    def _getStateTransitionTimeout (self):
        return self._pmBlinkyCopy.getStateTransitionTimeout()

    def _getStateTransitionWarningThreshold (self):
        return self._pmBlinkyCopy.getStateTransitionWarningThreshold()

    def _getWatchdogTimeout (self):
        return self._pmBlinkyCopy.getWatchdogTimeout()

    def _getWatchdogWarningThreshold (self):
        return self._pmBlinkyCopy.getWatchdogWarningThreshold()

    def _getKillTimeout (self):
        return self._pmBlinkyCopy.getKillTimeout()

    def _getKillWarningThreshold (self):
        return self._pmBlinkyCopy.getKillWarningThreshold()

    def _preExecute (self):
        #turning the requested states to actual...
        self._pmBlinkyCopy.configuredToActual()    


    def _launch (self):
        if self._getIsRunning():
            a.infra.process.processFatal("Failed launching process '%s' - process is already running", self._name)

        self._log("launching-flex-process").notice("launching process '%s'", self.getName())
        self._preExecute()        
        
        self._actualState = common.ProcessState.DORMANT
        self._pmBlinkyCopy.writeActualState(self._actualState)
        self._run()




class ManagedFlexProcess(ProcessFlex):
    """a flex process that is matching a process using the a::sys::process::ManagedCaptain"""
    def __init__ (self, name, logger):
        ProcessFlex.__init__ (self, name, logger)

    def _preExecute (self):
        ProcessFlex._preExecute (self)

        processCaptainInitParams={a.sys.process.captain.ManagedCaptain.INIT_PARAM_DATA_PROCESS_NAME: self.getName()}

        logCentralBlinkyData = a.infra.log.main_logger_blinky.ModuleCentralBlinkyData(self._log)
        logCentralBlinkyData.initBlinky(self._blinky)
        logBlinkyData = logCentralBlinkyData.getProcessBlinkyData(self.getName())
        logBlinkyData.configuredToActual()
        logDir = logBlinkyData.readLogDir()
        if logDir is not None:
            a.infra.file.utils.makeDirs(logDir, reuseExisting=True)
        loggerInitParams={a.infra.log.main_logger.MainLogger.INIT_PARAM_DATA_LOG_DIR: logDir,
                          a.infra.log.main_logger.MainLogger.INIT_PARAM_DATA_LOG_LEVEL: logBlinkyData.readLogLevel(),
                          a.infra.log.main_logger.MainLogger.INIT_PARAM_DATA_LOG_FILE_SIZE: 0,#TODO(nirs) bring from blinky
                          a.infra.log.main_logger.MainLogger.INIT_PARAM_DATA_LOG_TOTAL_SIZE: 0, #TODO(nirs) bring from blinky
                          a.infra.log.main_logger.MainLogger.INIT_PARAM_DATA_LOG_PEARL_CONFIGURATION_FILE_NAMES_LIST:None,
                          a.infra.log.main_logger.MainLogger.INIT_PARAM_DATA_LOG_PEARL_CONFIGURATION_FILE_LOAD_PERIOD:None
                         }      


        blinkyCentralBlinkyData = a.sys.blinky.pearl.ModuleCentralBlinkyData(self._log)
        blinkyCentralBlinkyData.initBlinky(self._blinky)
        blinkyInitParams={a.sys.blinky.pearl.Blinky.INIT_PARAM_DATA_CONFD_PERSISTENT_DIR:blinkyCentralBlinkyData.readConfdPersistentDir(),
                          a.sys.blinky.pearl.Blinky.INIT_PARAM_DATA_CONFD_VOLATILE_DIR:blinkyCentralBlinkyData.readConfdVolatileDir()}

        initParamsFileDir = self._getInitParamFilesDir()
        if os.path.exists(initParamsFileDir):
            shutil.rmtree(initParamsFileDir)#TODO(nirs) review with gaash
        a.infra.file.utils.makeDirs(initParamsFileDir, reuseExisting=True)
        a.sys.process.captain.ManagedCaptain.s_createInitParamFiles(self._log,
                                                                    initParamsFileDir,
                                                                    {a.sys.process.captain.ManagedCaptain.INIT_PARAM_DICT_KEY_PROCESS_CAPTAIN:processCaptainInitParams,
                                                                     a.sys.process.captain.ManagedCaptain.INIT_PARAM_DICT_KEY_MAIN_LOGGER:loggerInitParams,                                                                     
                                                                     a.sys.process.captain.ManagedCaptain.INIT_PARAM_DICT_KEY_BLINKY:blinkyInitParams})

        




