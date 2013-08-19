#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: amiry
# 

import os, time, threading
import a.infra.subprocess
from  a.infra.file.rotating_file_size_enforcer import RotatingFileSizeEnforcer

if  __package__ is None:
    G_GROUP_NAME_LOGPUSHER_ADAPTER  = "unknown"
else:
    from . import G_GROUP_NAME_LOGPUSHER_ADAPTER

HISTORY_ENFORCE_SIZE_INTERVAL_SEC = 300 # 5 minutes

class LogpusherAdapter:

#-----------------------------------------------------------------------------------------------------------------------
    def __init__ (self, logger, logpusherExecutable, monitorListenPort, forceIfaceToBind, historyDirMaxSizeMB):
        self._log = logger.createLoggerSameModule(G_GROUP_NAME_LOGPUSHER_ADAPTER)
        self._logpusherExecutable = logpusherExecutable

        # TODO(amiry) - Currently we support only one instance of logpusher.
        # When we want to support more, the listen port should be allocated in the reporting manager
        self._monitorListenPort = monitorListenPort
        self._forceIfaceToBind = forceIfaceToBind
        self._historyDirMaxSizeMB = historyDirMaxSizeMB

        self._logpusher = None
        self._startCnt = 0
        self._logType = None
        self._logDir = None
        self._confDir = None
        self._historyDir = None
        self._configFile = None
        self._shouldRestart = False
        self._currIfaceName = None
        self._gotFirstNetworkConfig = False
        self._gracefullyStopped = True

        # Name is initialized wnen export configuration initialized (and changed).
        # Network configuration is loaded from a dirrerent thread and might be initialized before
        # the export is initialized
        self._name = "[uninitialized]"

        # We need to synch the network configuration change and the watchdog.
        # Other configuration changes is also synched by the export_list_manager
        # self._netConfigurationLock = threading.RLock()
        self._netConfigurationLock = threading.Lock()

#-----------------------------------------------------------------------------------------------------------------------
    def updateConfig (self, logType, logDir, confDir, historyDir, name):
        self._log("update-config").debug1("Update config (%s)" % self._name)
        self._logType = logType
        self._logDir = logDir
        self._confDir = confDir
        self._historyDir = historyDir
        self._configFile = os.path.join(self._confDir, "logpusher.conf")
        self._pidFile = os.path.join(self._confDir, "logpusher.pid")
        self._name = name
        self._shouldRestart = True

        # File size enforcer on the history dir
        self._historySizeEnforcer = RotatingFileSizeEnforcer(self._log, self._logDir, "tran-"+self._name+"-", ".log.bz")
        self._historySizeEnforcer.initFileRotatingPattern(
            "%s.%s" % (RotatingFileSizeEnforcer.KICK_NUM_4, RotatingFileSizeEnforcer.EPOCH_SECONDS_10))
        self._historySizeEnforcer.setTotalSize(self._historyDirMaxSizeMB * 1024 * 1024)
        self._lastHistoryDirSizeEnforce = 0

#-----------------------------------------------------------------------------------------------------------------------
    def updateNetworkConfig (self, newIfaceList):

        self._log("update-network-config").debug1("Update network config (%s). New config %s" % (self._name, newIfaceList))

        self._gotFirstNetworkConfig = True

        ifaceChanged = False    # Need to change iface
        configChanged = False   # Only need to restart

        if self._currIfaceName:
            # Check if the configuration of the active iface changed
            newIface = newIfaceList.get(self._currIfaceName)
            if newIface is None:
                self._log("curr-iface-not-exist").notice("Curr iface doesn't exist in new network configuration (%s). Curr iface %s, new iface list %s" % 
                                                           (self._name, self._currIfaceName, newIfaceList))
                ifaceChanged = True
            else:
                if not self._isIfaceActive(newIface):
                    self._log("curr-iface-not-active").notice("Curr iface is not active in new network configuration (%s). Curr iface %s, new iface %s" % 
                                                               (self._name, self._currIfaceName, newIface))
                    ifaceChanged = True
                else:
                    if self._currIface["ipv4Address"] != newIface["ipv4Address"]:
                        self._log("curr-iface-chenge-ip").notice("Curr iface changed ip (%s). Curr iface %s, new config %s" % 
                                                                   (self._name, self._currIfaceName, newIface))
                        configChanged = True

        # If iface nas changed, we need to get a new iface to bind
        if not self._currIfaceName or ifaceChanged:
            self._getActiveIfaceToBind(newIfaceList)
            # If we got a new iface we need to restart.
            # If no iface is active, this whould cause the watchdog to stop the logpusher.
            self._shouldRestart = True

        if configChanged:
            # Curr iface config changed. Need to restart
            self._shouldRestart = True

#-----------------------------------------------------------------------------------------------------------------------
    def updateNetworkStatus (self, newIfaceList):

        self._log("update-network-status").debug1("Update network status (%s). New config %s" % (self._name, newIfaceList))

        # If we don't have an interface we need to do the whole network update
        if self._currIfaceName is None:
            self.updateNetworkConfig(newIfaceList)
            return

        # If we do have an iface, check it its status has changed.
        for ifaceName, iface in newIfaceList.items():
            if ifaceName == self._currIfaceName:
                if self._currIface["ipv4ServiceStatus"] and not iface["ipv4ServiceStatus"]:
                    self._log("iface-service-status-changed").notice("Bind iface %s service status changed from %s to %s" % 
                        (self._currIfaceName, self._currIface["ipv4ServiceStatus"], iface["ipv4ServiceStatus"]))
                    if self._forceIfaceToBind:
                        self._log("no-failover").notice("Failover is not allowed. Forced iface is %s" % self._forceIfaceToBind)
                        self.stop()
                    else:
                        prevName = self._currIfaceName
                        self._getActiveIfaceToBind(newIfaceList)
                        self._log("failover").notice("Failover from iface %s to %s" % (prevName, self._currIfaceName))
                        self._shouldRestart = True

                # Update the curr iface
                self._currIface["ipv4ServiceStatus"] = iface["ipv4ServiceStatus"]

#-----------------------------------------------------------------------------------------------------------------------
    def watchdog (self):

        self._log("watchdog").debug2("Watchdog (%s)" % self._name)

        if self._shouldRestart:
            self.stop()
            self._shouldRestart = False

        self._log("watchdog-before").debug2("Watchdog (%s). Before configuration lock" % self._name)

        with self._netConfigurationLock:

            self._log("watchdog-after").debug2("Watchdog (%s). After configuration lock" % self._name)

            if self._currIfaceName is None:
                if self._gotFirstNetworkConfig:
                    self._log("no-net-config-warning").warning("Can't start logpusher (%s). No network interface is available" % self._name)
                else:
                    self._log("no-net-config-ok").notice("Can't start logpusher (%s). Waiting for network config" % self._name)
                return
    
            if self._logpusher is None or not self._logpusher.isUp():
                if not self._gracefullyStopped:
                    self._log("should-start").warning("Logpusher is down (%s). Starting" % self._name)
                self._start()


        # Enforce "sent archive" size limit
        if time.time() - self._lastHistoryDirSizeEnforce > HISTORY_ENFORCE_SIZE_INTERVAL_SEC:
            self._log("history-enforce-size").debug1("Watchdod (%s). Enforce history dir size (%d MB)" % (self._name, self._historyDirMaxSizeMB))
            self._historySizeEnforcer.enforceSize()

#-----------------------------------------------------------------------------------------------------------------------
    def _start (self):

        self._log("starting-logpusher").notice("Starting logpusher (%s)", self._name)
        if not self._createConfigFile():
            return False

        if self._logpusher is None:
            self._logpusher = a.infra.subprocess.Subprocess("llnw-logpusher", self._log)
            if self._logpusher is None:
                self._log("error-creating-subprocess").warning("Error creating subprocess (%s)" % self._name)
                return

        cmd = "%s -d -f %s" % (self._logpusherExecutable, self._configFile)
        self._logpusher.start(cmd, shell = True, setpgrp = True,
                              stdout = a.infra.subprocess.PIPE,
                              stderr = a.infra.subprocess.STDOUT,
                              bufsize = 1)

        self._writePidFile()
        self._startCnt += 1

        # Read logpusher stdout in the background
        self._thread = threading.Thread(target = self._logOutput, args = (self._log, self._logpusher))
        self._thread.daemon = True # thread dies with the program
        self._thread.start()
        self._gracefullyStopped = False

#-----------------------------------------------------------------------------------------------------------------------
    def stop (self):

        if not self._logpusher:
            return

        if self._logpusher.isUp():
            self._log("stoping-logpusher").notice("Stopping logpusher (%s)", self._name)
            self._logpusher.stop(5) # Timeout 5 seconds
            self._deletePidFile()
            #self._logpusher = None
            self._gracefullyStopped = True


#-----------------------------------------------------------------------------------------------------------------------
    def _createConfigFile (self):
        try:
            # Create logpusher's config file
            f = open(self._configFile, 'w')

            # We do our own bzip2
            # f.write("log %s/*.log bzip2 flock olddir %s type %s\n" % (self._logDir, self._historyDir, self._logType))
            f.write("log %s/*.log.bz2 oldtime 1s flock olddir %s type %s\n" % (self._logDir, self._historyDir, self._logType))

            f.write("monitorListenAddress localhost\n");
            f.write("monitorListenPort %d\n" % self._monitorListenPort);
            f.write("sourceAddress %s\n" % self._currIface["ipv4Address"]);
            f.close()
            self._log("create-config-file").info("logpusher config file created (%s). File %s" % (self._name, self._configFile))
            return True
        except Exception as ex:
            self._log("create-config-file-error").error("Error creating logpusher config file (%s). File %s. Exception %s" % (self._name, self._configFile, ex))
            return False

#-----------------------------------------------------------------------------------------------------------------------
    def _getActiveIfaceToBind(self, ifaceList):

        newIface = None
        newIfaceName = None
        for ifaceName, iface in ifaceList.items():
            if self._isIfaceActive(iface):
                newIface = iface
                newIfaceName = ifaceName
                break
            elif ifaceName == self._forceIfaceToBind:
                # The current iface is the iface that we are forced to bind to and if is not active...
                break


        with self._netConfigurationLock:

            if newIface:
                self._currIface = newIface.copy()
            else:
                self._currIface = None
            self._currIfaceName = newIfaceName

            self._log("get-iface-to-bind").debug1("Got iface %s. %s" %(self._currIfaceName, self._currIface))

#-----------------------------------------------------------------------------------------------------------------------
    def _isIfaceActive(self, iface):
        enable = iface.get("enable", False)
        ipv4ServiceStatus = iface.get("ipv4ServiceStatus", False)
        return enable and ipv4ServiceStatus

#-----------------------------------------------------------------------------------------------------------------------
    def _writePidFile (self):
        if self._logpusher:
           pid = self._logpusher.getPid() 

           try:
               # Create logpusher's pid file
               f = open(self._pidFile, 'w')
               f.write("%d" % (pid))
               f.close()
               self._log("create-pid-file").debug1("logpusher pid file created (%s). File %s" % (self._name, self._pidFile))
               return True
           except Exception as ex:
               self._log("create-pid-file-error").error("Error creating logpusher pid file (%s). File %s. Exception %s" % (self._name, self._pidFile, ex))
               return False

#-----------------------------------------------------------------------------------------------------------------------
    def _deletePidFile (self):
        try:
            # Delete logpusher's pid file. Indicates proper shutdown
            os.remove(self._pidFile)
            self._log("delete-pid-file").debug1("logpusher pid file deleted (%s). File %s" % (self._name, self._pidFile))
            return True
        except Exception as ex:
            self._log("delete-pid-file-error").error("Error deleting logpusher pid file (%s). File %s. Exception %s" % (self._name, self._pidFile, ex))
            return False

#-----------------------------------------------------------------------------------------------------------------------
    def _readPidFile (self):
        try:
            with open(self._pidFile, 'r') as f:
                pid = f.read()
                try:
                    int_pid = int(pid)
                except ValueError:
                    self._log("pid-file-error").error("Error reading logpusher pid file (%s). File %s Dosen't contain a pid" % (self._name, self._pidFile))
                    return 0
                return int_pid
        except Exception as ex:
            # No pid file
            self._log("read-pid-file-error").debug1("Error reading logpusher pid file (%s). File %s. Exception %s" % (self._name, self._pidFile, ex))
            return 0

#-----------------------------------------------------------------------------------------------------------------------
    def _logOutput(self, logger, logpusher):
        while True:
            try:
                line = logpusher.stdout.readline()
                if not line:
                    logger("logpusher-stdout-thread-exit").notice("Logpusher stdout logging thread exit (%s)" % self._name)
                    break
                logger("logpusher-stdout").notice("%s: %s" % (self._name, line.rstrip()))
            except IOError, ex:
                logger("logpusher-stdout-ioerror").warning("%s: %s" % (self._name, ex))

