#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

import os
import captain
import signal
import a.infra.process.captain

if  __package__ is None:
    G_NAME_MODULE_SYS_STD_PROCESS = "unknown"
    G_NAME_GROUP_SYS_STD_PROCESS_MICRO_CAPTAIN = "unknown"
else:
    from . import G_NAME_MODULE_SYS_STD_PROCESS 
    from . import G_NAME_GROUP_SYS_STD_PROCESS_MICRO_CAPTAIN


class MicroCaptain(captain.Captain):
    #init param dicts    
    INIT_PARAM_DICT_KEY_MICRO_APP = "micro-app"

    def __init__(self, microApp):
        captain.Captain.__init__(self, processName = microApp.processName(),
                                 earlyLogLevel = microApp.changedEarlyLogLevel(), 
                                 initParamFilesDirEnvVar = microApp.s_getInitParamsFilesDirEnvVarName()) 
        self._microApp = microApp    

    def _createClients (self):
        captain.Captain._createClients(self)
        self._microClient = MicroCaptainAppClient(self._log, self._microApp)
        self._microClient.initCaptain(self)
        self._addClient("micro-captain-client", self._microClient)
        self._microClient.createApplicationClients()
        

    def run (self):
        a.infra.process.setGlobalCaptain(self)
        try:   
            __pychecker__='no-argsused'
                 
            self.earlyInit()
            if self._microClient.isSupportTerminationBySignal():
                #setting sigterm to stop the process
                def doOnSigEnd(signum, frame):                
                    self.promoteStopSequenceType(a.infra.process.captain.Captain.STOP_SEQUENCE_TYPE_STD)
                signal.signal(signal.SIGTERM, doOnSigEnd)
                signal.signal(signal.SIGINT, doOnSigEnd)

            self.fullStart()
            self.fullStop()
            self.lateShutdown()
            return self._microClient.getReturnCode()
        except Exception as exception:
            a.infra.process.processFatal("process failure: %s", str(exception))

    @classmethod
    def s_microCaptainCreateInitParamFiles(cls, dbglog, microAppClass, initParamFilesDir, dictionary):
        captain.Captain.s_createInitParamFiles(dbglog, initParamFilesDir, dictionary)
        MicroCaptainAppClient.s_createInitParamFiles(dbglog, microAppClass, initParamFilesDir, dictionary[cls.INIT_PARAM_DICT_KEY_MICRO_APP])
        
    @classmethod    
    def s_microCaptainSetParamFilesDirEnvVarIfNeeded (cls, dbglog, microAppClass, initParamFilesDirName):
        cls._dummy = cls#satisfying pychecker
        MicroCaptainAppClient.s_setParamFilesDirEnvVarIfNeeded(dbglog, microAppClass, initParamFilesDirName)       


class MicroCaptainAppClient(object):
    def __init__(self, logger, microApp):
        self._log = logger
        self._microApp = microApp
        self._microApp.initLogger(self._log)
        self._returnCode = 1

    def initCaptain (self, captainInstance):
        self._captain = captainInstance
        self._microApp.initCaptain(captainInstance)

    def createApplicationClients (self):
        self._microApp.createCaptainClients()

    def captainClient_initFromParamFile (self):
        self._microApp.initFromParamFile(self._captain.getInitParamFilesDirName())

    def captainClient_addToOptParser (self):
        self._microApp.addToOptParser(self._captain.getOptParser())

    def captainClient_parseCmdLine (self):       
        (options, args) = self._captain.getParsedCmd()
        self._microApp.parseCmdLine(options, args)

    def captainClient_passive2Active (self):
        self._microApp.passive2Active()

    def captainClient_active2Up (self):
        self._returnCode = self._microApp.run()

    def getReturnCode (self):
        return self._returnCode

    def isSupportTerminationBySignal(self):
        return self._microApp.isSupportTerminationBySignal()

    @classmethod
    def s_createInitParamFiles (cls, dbglog, microAppClass, initParamFilesDirName, dataDictionary):
        cls._dummy = cls#satisfying pychecker
        microAppClass.s_createInitParamFiles(dbglog, initParamFilesDirName, dataDictionary)

    @classmethod
    def s_setParamFilesDirEnvVarIfNeeded (cls, dbglog, microAppClass, initParamFilesDirName):
        cls._dummy = cls#satisfying pychecker
        varName = microAppClass.s_getInitParamsFilesDirEnvVarName()
        if not varName is None:
            dbglog("set-env").debug1("setting the env variable '$%s=%s'", varName, initParamFilesDirName)
            os.environ[varName] = initParamFilesDirName
        
            


class MicroAppInterface(object):
    def initLogger(self, logger):
        """Init the logger for the application

        Args:
            logger

        Returns:
            None

        Raises:
            None
        """
        pass

    def initCaptain (self, captainInstance):
        """Init the captain used by the application. This is used for creating extra captain clients
        """
        self._captain = captainInstance

    def createCaptainClients (self):
        pass

    def initFromParamFile(self, initParamFilesDirName):
        """Init the the class by reading the data from the init params

        Args:
            initParamFilesDirName

        Returns:
            None

        Raises:
            None
        """
        pass

    def addToOptParser(self, optParser):
        """Add options to the opt parser of the executable

        Args:
            optParser

        Returns:
            None

        Raises:
            None
        """
        pass

    def parseCmdLine(self, options, args):
        """Use the parsed data from the command line

        Args:
            options - "options" data as returned from the opt parser
            args - "args" data as returned from the opt parser


        Returns:
            None

        Raises:
            None
        """
        pass

    def passive2Active (self):
        """Use for attaching to blinky
        """
        pass

    def run (self):
        """run the application main function

        Args:
            None

        Returns:
            Executable return value

        Raises:
            None
        """
        return 1

    def changedEarlyLogLevel (self):
        """Return the early log level of the logger (until moving to the real logger)

        Args:
            None

        Returns:
            log level (from logging.XXX) or None for no change

        Raises:
            None
        """
        return None

    def isSupportTerminationBySignal (self):
        """Return True if the application knows how to exit gracefully on sig int and sigterm"""
        return False

    @classmethod
    def s_getInitParamsFilesDirEnvVarName (cls):
        """Return the env var that indicates the directory of the init param files. None if no such env var
        """
        return None


    @classmethod
    def s_createInitParamFiles(cls, dbglog, initParamFilesDir, dataDictionary):
        """create the init param file for the application
        """
        pass


