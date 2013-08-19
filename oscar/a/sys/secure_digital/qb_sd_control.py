#!/usr/local/bin/python2.6
# 
# Copyright Qwilt, 2013
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: shmulika

import optparse
import subprocess
import sys

import a.infra.process
from a.infra.basic.return_codes import ReturnCodes
import a.sys.secure_digital.utils
import a.sys.secure_digital.manager


class QbSdControl(object):

    def __init__ (self, log):
        self._log = log # TODO(shmulika): creat esma emoduel
        

    def _init (self):
        if self._externalSecureDigital:
            self._sdManager = a.sys.secure_digital.manager.SdManager(self._log, isExternalSD = True, platformType = self._platformType, cardReaderDeviceModel = self._cardReaderDeviceModel)        
        else:
            self._sdManager = a.sys.secure_digital.manager.SdManager(self._log)        


    def genericAction_run (self, args):
        return self.run(args)


    def run (self, args = None):
        rc = self._parseArguments(args)
        if rc != ReturnCodes.kOk:
            return rc
        
        self._init()

        # Tech interface methods
        if self._shouldReInstallEntireSecureDigital:
            self._runReInstallEntireSecureDigital()
        elif self._shouldInvalidateEntireSecureDigital:
            self._runInvalidateEntireSecureDigital()
        elif self._shouldReInstallMain:  
            self._runInstallMainAndKrusty()
        elif self._shouldUpdateMainIfNecessary:
            self._runUpdateMainAndKrustyIfNecessary()
        elif self._shouldInvalidateMain:
            self._runInvalidateMainAndKrusty()
        elif self._shouldUpdateSoftwarePackage:
            self._runUpdateSofwarePackage()
        elif self._shouldInvalidateSoftwarePackage:
            self._runInvalidateSofwarePackage()
        elif self._shouldRecreateVital: 
            self._runReCreateVital()   
        elif self._shouldInvalidateVital:
            self._runInvalidateVital()   
        elif self._shouldDumpStatus:
            self._runDumpStatus()
        elif self._shouldSetBootSystemDisk:
            self._runSetBootSystemDisk()    
        elif self._shouldSetBootSecureDigital: 
            self._runSetBootSecureDigital()            
        elif self._shouldDumpBootMethod:
            self._runDumpBootMethod()            
        elif self._shouldEraseSystem:
            self._runBootSecureDigitalRecovery()
        elif self._shouldReloadSystemRecovery:
            self._runBootSecureDigitalRecovery(manualRecovery = True)
        elif self._shouldMountAll:
            self._runMountAllPartitions()
        elif self._shouldUmountAll:      
            self._runUmountAllPartitions() 
        elif self._shouldWipeSd:
            self._runWipeSd() 
        elif self._shouldDumpVarLogMessages:
            self._runDumpVarLogMessages()
        elif self._shouldDumpBashHistory: 
            self._runDumpBashHistory()

        # Debug options
        elif self._shouldInstallBoot:
            self._runInstallBoot()
        elif self._shouldInvalidateBoot:        
            self._runInvalidateBoot()
        elif self._shouldCreatePartitions:
            self._runInstallPartitions()        
        else:
            # default operation - dump sd status
            self._runDumpStatus()
                
        return ReturnCodes.kOk
        

    def _runReInstallEntireSecureDigital (self):      
        if self._externalSecureDigital:
            if self._platformType is None:
                self._log("re-install-entire-secure-digital").error("when performing operation on an external secure digital, platform type for which it is inteded must be specified")
                print "when performing operation on an external secure digital, platform type for which it is inteded must be specified"
                return

            print "Installing the contents of the external recovery media, this may take several minutes..."
            rc = self._sdManager.reInstallEntireExternalSecureDigital(progressOut = self._getProgressOutputStream(), packageFilename = self._qbPackageFile)
        else:
            print "Installing the contents of the recovery media, this may take several minutes..."
            rc = self._sdManager.reInstallEntireSecureDigital(progressOut = self._getProgressOutputStream())
        
        self._runPrintMessage(rc)


    def _runInvalidateEntireSecureDigital (self):
        if self._externalSecureDigital:
            print "Invalidating the external recovery media, this may take a few moments..."
            rc = self._sdManager.invalidateEntireExternalSecureDigital(progressOut = self._getProgressOutputStream())
        else:
            print "Invalidating the recovery media, this may take a few moments..."
            rc = self._sdManager.invalidateEntireSecureDigital(progressOut = self._getProgressOutputStream())

        self._runPrintMessage(rc)


    def _runInstallMainAndKrusty (self):
        print "Re-installing the recovery media software, this may take a several minutes..."
        rc = self._sdManager.reInstallMain(progressOut = self._getProgressOutputStream())
        self._runPrintMessage(rc)


    def _runUpdateMainAndKrustyIfNecessary(self):
        print "Checking for an updated major version of recovery media software and updating, this may take a several minutes..."
        rc = self._sdManager.checkAndUpdateMain(progressOut = self._getProgressOutputStream())
        self._runPrintMessage(rc)



    def _runInvalidateMainAndKrusty (self):
        print "Invalidating recovery media software..."
        rc = self._sdManager.invalidateMain(progressOut = self._getProgressOutputStream())
        self._runPrintMessage(rc)


    def _runUpdateSofwarePackage (self):
        print "Updating software package:"
        if self._shouldUseDefaultSofwarePackage:
            rc = self._sdManager.copyRecoveryPackage(self._getProgressOutputStream(), None)
        else:
            rc = self._sdManager.copyRecoveryPackage(self._getProgressOutputStream(), self._qbPackageFile)

        self._runPrintMessage(rc)


    def _runInvalidateSofwarePackage (self):
        print "Invalidating software package:"
        rc = self._sdManager.invalidateRecoveryPackage(self._getProgressOutputStream())
        self._runPrintMessage(rc)


    def _runReCreateVital (self):
        print "Re-creating vital:"
        rc = self._sdManager.reInstallVital(self._getProgressOutputStream())
        self._runPrintMessage(rc)


    def _runInvalidateVital (self):
        print "Invalidating vital:"
        rc = self._sdManager.invalidateVital(self._getProgressOutputStream())
        self._runPrintMessage(rc)


    def _runDumpStatus (self):
        print "Dumping status of the recovery media:"
        rc = self._sdManager.dumpSecureDigitalStatus(progressOut = self._getProgressOutputStream())
        self._runPrintMessage(rc)


    def _runSetBootSystemDisk (self):
        print "Setting system disk as the boot device:"
        rc = self._sdManager.setBootSystemDisk(progressOut = self._getProgressOutputStream())
        self._runPrintMessage(rc)


    def _runSetBootSecureDigital (self):
        print "Setting recovery media as the boot device:"
        rc = self._sdManager.setBootSecureDigital(progressOut = self._getProgressOutputStream())
        self._runPrintMessage(rc)

    def _runDumpBootMethod (self):
        print "Dumping boot method status:"
        rc = self._sdManager.dumpBootMethodStatus(progressOut = self._getProgressOutputStream())
        self._runPrintMessage(rc)


    def _runBootSecureDigitalRecovery (self, manualRecovery = False):
        if manualRecovery:
            print "Setting next boot to recovery mode:"
        else:
            print "Setting next boot to system-erase:"

        rc = self._sdManager.setSecureDigitalRecoveryOnBoot(self._getProgressOutputStream(), manualRecovery)
        self._runPrintMessage(rc)

        if rc == ReturnCodes.kOk:
            if not self._noReboot:
                print "Rebooting system..."
                subprocess.call(["reboot"]) # TODO(shmulika): replace with captain interface when nirs provides it
            else:
                print "Not rebooting system."


    def _runMountAllPartitions (self):
        print "Mounting recovery media partitions:"
        rc = self._sdManager.mountAllPartitions(progressOut = self._getProgressOutputStream())
        self._runPrintMessage(rc)


    def _runUmountAllPartitions (self):
        print "Umounting recovery media partitions:"
        rc = self._sdManager.umountAllPartitions(progressOut = self._getProgressOutputStream())
        self._runPrintMessage(rc)


    def _runWipeSd (self): 
        if self._externalSecureDigital:
            print "Wiping the external recovery media, this may take a few moments..."
            rc = self._sdManager.wipeEntireExternalSd(progressOut = self._getProgressOutputStream())
        else:
            print "Wiping the recovery media, this may take a few moments..."
            rc = self._sdManager.wipeEntireSd(progressOut = self._getProgressOutputStream())
        
        self._runPrintMessage(rc)


    def _runDumpVarLogMessages (self):
        self._sdManager.dumpVarLogMessages(progressOut = self._getProgressOutputStream())


    def _runDumpBashHistory (self):
        self._sdManager.dumpBashHistory(progressOut = self._getProgressOutputStream())


    def _runInvalidateBoot (self):
        print "Invalidating the boot partition of the recovery media, this may take a few moments..."
        rc = self._sdManager.invalidateBoot(progressOut = self._getProgressOutputStream())
        self._runPrintMessage(rc)


    def _runInstallBoot (self):
        print "Installing the boot partition of the recovery media, this may take a few moments..."
        rc = self._sdManager.reInstallBoot(progressOut = self._getProgressOutputStream())
        self._runPrintMessage(rc)


    def _runInstallPartitions (self):
        print "Installing the partitions of the recovery media, this may take a few moments..."
        rc = self._sdManager.reInstallPartitions(progressOut = self._getProgressOutputStream())
        self._runPrintMessage(rc)


    def _runPrintMessage (self, returnCode):
        if returnCode == ReturnCodes.kOk:
            print "Done."
        else:
            print "Failed: " + self._sdManager.getLastErrorMsg()


    def _getProgressOutputStream (self):
        return sys.stdout
             

    def _parseArguments (self, args = None):
        # When ran by the GenericAction wrapper, args is passed by argument,
        # When ran from command line, use sysargs

        if args:
            parser = optparse.OptionParser(usage="",prog="qb-sd-control")
        else:
            parser = optparse.OptionParser()

        parser.add_option("--full-install", dest="shouldReInstallEntireSecureDigital", action="store_true", default=False,
                          help="secure digital card entire content should be created (existing content deleted)")

        parser.add_option("--invalidate", dest="shouldInvalidateEntireSecureDigital", action="store_true", default=False,
                          help="secure digital card should be invalidated (will not be used)")

        parser.add_option("--recovery-software-install", dest="shouldReInstallMain", action="store_true", default=False,
                          help="secure digital card's recovery software (krusty) should be installed (or re-installed)")

        parser.add_option("--recovery-software-update-if-necessary", dest="shouldUpdateMainIfNecessary", action="store_true", default=False,
                          help="secure digital card's recovery software (krusty) should be udpated if a new major version is available")

        parser.add_option("--recovery-software-invalidate", dest="shouldInvalidateMain", action="store_true", default=False,
                          help="secure digital card's recovery software (krusty) should be invalidated")

        parser.add_option("--update-software-package", dest="shouldUpdateSoftwarePackage", action="store_true", default=False,
                          help="udpate the (QB) software package on the secure digital")

        parser.add_option("--package-file", dest="qbPackageFile", default=None,
                          help="use the specified QB package file")

        parser.add_option("--default", dest="shouldUseDefaultSofwarePackage", action="store_true", default=False,
                          help="the the default QB package file")

        parser.add_option("--invalidate-software-package", dest="shouldInvalidateSoftwarePackage", action="store_true", default=False,
                          help="invalidate the (QB) software package on the secure digital")

        parser.add_option("--recreate-vital", dest="shouldRecreateVital", action="store_true", default=False,
                          help="re-create the vital on the secure digital")

        parser.add_option("--invalidate-vital", dest="shouldInvalidateVital", action="store_true", default=False,
                          help="invalidate the vital on the secure digital")

        parser.add_option("--dump-status", dest="shouldDumpStatus", action="store_true", default=False,
                          help="dumps the status of the secure digital")

        parser.add_option("--set-boot-secure-digital", dest="shouldSetBootSecureDigital", action="store_true", default=False,
                          help="set the secure digital as the boot device")

        parser.add_option("--set-boot-system-disk", dest="shouldSetBootSystemDisk", action="store_true", default=False,
                          help="set the system disk as the boot device")

        parser.add_option("--dump-boot-method", dest="shouldDumpBootMethod", action="store_true", default=False,
                          help="dumps the boot method")

        parser.add_option("--erase-system", dest="shouldEraseSystem", action="store_true", default=False,
                          help="will reboot and re-install oscar completely (factory default)")

        parser.add_option("--reload-system-recovery", dest="shouldReloadSystemRecovery", action="store_true", default=False,
                          help="will reboot and launch manual recovery")

        parser.add_option("--no-reboot", dest="noReboot", action="store_true", default=False,
                          help="when given, actions will finish before doing system reboot")

        parser.add_option("--mount-all", dest="shouldMountAll", action="store_true", default=False,
                          help="mounts all the secure digital partitions")

        parser.add_option("--umount-all", dest="shouldUmountAll", action="store_true", default=False,
                          help="umounts all the secure digital partitions")

        parser.add_option("--dump-bash-history", dest="shouldDumpBashHistory", action="store_true", default=False,
                          help="dumps the boot method")

        parser.add_option("--dump-var-log-messages", dest="shouldDumpVarLogMessages", action="store_true", default=False,
                          help="dumps the boot method")



        parser.add_option("--partitions", dest="shouldCreatePartitions", action="store_true", default=False,
                          help="secure digital card partitions should be created (existing content deleted)")

        parser.add_option("--boot-install", dest="shouldInstallBoot", action="store_true", default=False,
                          help="sd boot partition should be installed (or re-installed)")

        parser.add_option("--invalidate-boot", dest="shouldInvalidateBoot", action="store_true", default=False,
                          help="sd boot partition should be invalidated (will not be used)")

        parser.add_option("--wipe", dest="shouldWipeSd", action="store_true", default=False,
                          help="secure digital card should be wiped (all content will be deleted)")


        parser.add_option("--external-secure-digital", dest="externalSecureDigital", action="store_true", default=False,
                          help="performs action on an external secure digital")

        parser.add_option("--platform-type", dest="platformType", default=None,
                          help="to use only with --external-secure-digital, specifies the type of platform for which to install the external secure digital")

        parser.add_option("--card-reader", dest="cardReaderDeviceModel", default=None,
                          help="to use only with --external-secure-digital, specifies the card reader device model containing the external secure digital")
        
        if args:
            (options, args) = parser.parse_args(args)
        else:
            (options, args) = parser.parse_args()

        self._shouldReInstallEntireSecureDigital  = options.shouldReInstallEntireSecureDigital
        self._shouldInvalidateEntireSecureDigital = options.shouldInvalidateEntireSecureDigital
        self._shouldReInstallMain                 = options.shouldReInstallMain        
        self._shouldUpdateMainIfNecessary         = options.shouldUpdateMainIfNecessary
        self._shouldInvalidateMain                = options.shouldInvalidateMain
        self._shouldUpdateSoftwarePackage         = options.shouldUpdateSoftwarePackage
        self._shouldInvalidateSoftwarePackage     = options.shouldInvalidateSoftwarePackage
        self._shouldUseDefaultSofwarePackage      = options.shouldUseDefaultSofwarePackage
        self._shouldRecreateVital                 = options.shouldRecreateVital
        self._shouldInvalidateVital               = options.shouldInvalidateVital
        self._shouldDumpStatus                    = options.shouldDumpStatus
        self._shouldSetBootSystemDisk             = options.shouldSetBootSystemDisk
        self._shouldSetBootSecureDigital          = options.shouldSetBootSecureDigital
        self._shouldDumpBootMethod                = options.shouldDumpBootMethod
        self._shouldEraseSystem                   = options.shouldEraseSystem
        self._shouldReloadSystemRecovery          = options.shouldReloadSystemRecovery        
        self._shouldMountAll                      = options.shouldMountAll
        self._shouldUmountAll                     = options.shouldUmountAll
        self._shouldDumpVarLogMessages            = options.shouldDumpVarLogMessages
        self._shouldDumpBashHistory               = options.shouldDumpBashHistory

        self._shouldCreatePartitions              = options.shouldCreatePartitions
        self._shouldInvalidateBoot                = options.shouldInvalidateBoot        
        self._shouldWipeSd                        = options.shouldWipeSd
        self._shouldInstallBoot                   = options.shouldInstallBoot
                                     
        self._qbPackageFile                       = options.qbPackageFile
        self._noReboot                            = options.noReboot

        self._externalSecureDigital               = options.externalSecureDigital          
        self._cardReaderDeviceModel               = options.cardReaderDeviceModel

        if options.platformType == 'qb-100':
            self._platformType = 'qb-6b2'
        elif options.platformType == 'qb-200':
            self._platformType = 'qb-10b5'
        elif options.platformType is None:
            self._platformType = None
        else:
            print "Error: unrecognized platform type %s." % options.platformType
            return ReturnCodes.kGeneralError

        # TODO(shmulika): log these parsing
        return ReturnCodes.kOk



def main ():
    pass # TODO(shmulika)

if __name__ == "__main__":    
    main()    
