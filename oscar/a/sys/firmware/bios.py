#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

import subprocess as originalsubprocess
import re

import a.infra.subprocess
import a.sys.platform.dell.open_manage.omreport_reader
import a.sys.platform.dell.open_manage.omreport_parser

G_NAME_MODULE_FIRMWARE_BIOS = "firmware-bios"
G_NAME_GROUP_FIRMWARE_BIOS_CONFIG = "config"
OMREPORT_CMD = "/opt/dell/srvadmin/bin/omreport"
OMCONFIG_CMD = "/opt/dell/srvadmin/bin/omconfig"

class BiosConfig(object):
    DEAFULT_KILL_TIMEOUT        = 100
    DEAFULT_WARNING_TIMEOUT     = 50

    def __init__ (self, logger):
        self._log = logger.createLogger(G_NAME_MODULE_FIRMWARE_BIOS, G_NAME_GROUP_FIRMWARE_BIOS_CONFIG)
        self._platformBasicData = None

    def initPlatfromBasicData (self, platformBasicData):
        self._platformBasicData = platformBasicData

    def getConfigCommands (self):
        biosType = self._platformBasicData.getBiosProperty(self._platformBasicData.BIOS_FIELD_CONTROLLER_TYPE)

        configCommands = []

        if biosType == self._platformBasicData.BIOS_CONTROLLER_TYPE_DELL: 
            settings = self._platformBasicData.getBiosProperty(self._platformBasicData.BIOS_FIELD_SETTINGS_LIST)
            for setting in settings:
                attribute = setting[self._platformBasicData.BIOS_SETTINGS_FIELD_ATTRIBUTE]
                attributeType = setting[self._platformBasicData.BIOS_SETTINGS_FIELD_TYPE]
                value = setting[self._platformBasicData.BIOS_SETTINGS_FIELD_VALUE]
                args = [OMCONFIG_CMD,
                        "chassis",
                        "biossetup",
                        "attribute=%s"%attribute,
                        "%s=%s"%(attributeType, value)]
                configCommands.append(args)

        return configCommands


    @classmethod
    def s_getIsSdConfiguredBootDevice (cls, logger, platformBasicData):
        """ test if the bios is configurable
        return None in case of failure
        """
        __pychecker__="no-argsused"
        biosType = platformBasicData.getBiosProperty(platformBasicData.BIOS_FIELD_CONTROLLER_TYPE)
        if not biosType == platformBasicData.BIOS_CONTROLLER_TYPE_DELL:
            return True

        args = OMREPORT_CMD + " chassis biossetup display=shortnames"
        returnCode, omreportStdout, omreportStderr = cls._s_runCommand(logger, args, shell=True)
        
        if returnCode != 0:
            logger("read-omreport-failed").error("running omreport with args=%s, exited with return code = %s", args, returnCode)
            return None
        if omreportStdout is None:
            logger("read-omreport-no-stdout").error("failed getting stdout of omreport with args=%s", args)
            return None
        
        exp = re.compile("[\s]")
        omreportStdout = exp.sub('', omreportStdout)
        if "HddSeq:1.Disk.SDInternal.1-1" in omreportStdout:
            logger("sd-boot-found").debug3("boot device found to be sd")
            return True

        if "HddSeq:1.RAID.Integrated.1-1" in omreportStdout:
            logger("sys-boot-found").debug3("boot device found to be system disk")
            return False

        logger("unknown-boot-found").error("boot device is unknown. output was: %s", omreportStdout)
        return None
            
            

    @classmethod
    def s_canSetBootDevice (cls, logger, platformBasicData):
        """ test if the bios is configurable
        """
        __pychecker__="no-argsused"
        biosType = platformBasicData.getBiosProperty(platformBasicData.BIOS_FIELD_CONTROLLER_TYPE)
        return biosType == platformBasicData.BIOS_CONTROLLER_TYPE_DELL

    @classmethod
    def s_setBootDeviceSd (cls, logger, platformBasicData):
        logger("from-sd").info("setting boot from SD")
        return cls._s_setBootDevice(logger, platformBasicData, True)

    @classmethod
    def s_setBootDeviceSystemDisk (cls, logger, platformBasicData):
        logger("from-sys").info("setting boot from system-disk")
        return cls._s_setBootDevice(logger, platformBasicData, False)

    @classmethod
    def _s_setBootDevice (cls, logger, platformBasicData, fromSd):
        """ test if the bios is configurable
        """
        __pychecker__="no-argsused"
        biosType = platformBasicData.getBiosProperty(platformBasicData.BIOS_FIELD_CONTROLLER_TYPE)

        configCommands = []

        if biosType == platformBasicData.BIOS_CONTROLLER_TYPE_DELL: 
            order = "Disk.SDInternal.1-1,RAID.Integrated.1-1"
            if not fromSd:
                order = "RAID.Integrated.1-1,Disk.SDInternal.1-1"
            args = [OMCONFIG_CMD,
                    "chassis",
                    "biossetup",
                    "attribute=HddSeq",
                    "sequence=%s"%order]
            configCommands.append({"args":args})

        else:
            if fromSd:
                logger("no-need-config").debug1("no need to set boot seq on this platfrom - SD is always used")
                return True
            else:
                logger("cannot-config").error("cannot set boot seq on this platfrom - SD is always used")
                return False

        success = cls._s_runCommands(logger, "set-boot-dev-cmd", configCommands)
        if not success:
            logger("failed-config").error("failed to run boot seq setting commands")
            return False
        
        logger("done-config").debug1("done running boot seq setting commands")
        return True
        

    @classmethod
    def _s_runCommand (cls, logger, args, killTimeout = DEAFULT_KILL_TIMEOUT, warningTimeout = DEAFULT_WARNING_TIMEOUT, shell = False):
        __pychecker__ = "unusednames=cls"
        subprocess = a.infra.subprocess.Subprocess("bios", logger)
        if not shell and isinstance(args, str):
            args = args.split()        
        try:
            logger("run-command").notice("running command, args=%s", args)
            subprocess.start(args, stdout = originalsubprocess.PIPE, stderr = originalsubprocess.PIPE, shell = shell)
            omreportStdout, omreportStderr = subprocess.communicate(killTimeOut = killTimeout, warningTimeOut = warningTimeout)
            logger("run-command").notice("command stdout = %s, stderr = %s", omreportStdout, omreportStderr)
        except Exception as exception:
            logger("run-command").error("Failed executing cmd %s, error=%s", args, exception, exc_info = 1)
            return (1, "", "")
        
        returnCode = subprocess.getReturnCode()                
        logger("run-command").notice("command rc = %s", returnCode)
        return (returnCode, omreportStdout, omreportStderr)


    @classmethod
    def _s_runCommands (cls, logger, cmdBatchName, listOfCommandsDict, continueOnError = False):         
        logger("call-cmd").debug2("running command batch %s", cmdBatchName)
        counter = 0
        try:
            for linuxCommandDict in listOfCommandsDict:            
                try:                
                    logger("call-cmd").debug2("running command %d %s", counter, linuxCommandDict)
                    rc, omreportStdout, omreportStderr = cls._s_runCommand(logger, **linuxCommandDict)
                    if rc != 0:
                        logger("cmd-fail").error("failed running cmd %d: %s", counter, linuxCommandDict)
                        if not continueOnError:
                            return False
                except:
                    logger("subprocess-failed").exception("failed running cmd %d: %s", counter, linuxCommandDict)
                    if not continueOnError:
                        return False
                counter += 1
        except:
            logger("failed").exception("failed running due to unexpected exception")
            return False

        return True
