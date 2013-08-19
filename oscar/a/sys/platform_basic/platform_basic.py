#
# Copyright Qwilt, 2013
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: Shmulika
# 

import os
import json
import a.infra.format.json

import platform_base

class PlatformBasic(platform_base.PlatformBase):
    """ TODO(shmulika): doc this
    """

    #initialization fields
    INIT_PARAM_DATA_PLATFORM_BASIC_DIR = "platform-basic-dir"
    INIT_PARAM_DATA_PLATFORM_TYPE      = "platform-type"

    _INIT_PARAM_FILE_NAME = "platform-basic-init-params.json"    


    def __init__ (self, log):
        platform_base.PlatformBase.__init__ (self)

        self._log = log # TODO(shmulika): createSameModule
        self._platformType      = None
        self._platformBasicDir = None

    #########################################################################################
    # INITIALIZATION METHODS
    #########################################################################################

    def init (self, platformBasicDir, platformType):
        """ Initializes the platform_basic directory from which all the platform data is loaded, and the platform type
        Source dir should be the directory into which the platform basic package was released        
        Raises: OS Error if directory/file of platform_basic paths do not exist, or there's an error reading from the files.
        """
        self._platformBasicDir = platformBasicDir
        self._platformType = platformType

        platformFilename = os.path.join(self._platformBasicDir, self.PLATFORM_BASIC_DATA_FILES_PREFIX,  self.s_getDataFileBaseName(platformType))
        self._log("init").debug1("PlatformBasic initialized (platformBasicDir=%s, platformType=%s), loading platform data from file=%s:", platformBasicDir, platformType, platformFilename)
        self._platformDictionary = self._loadFromJson(platformFilename)                        
        self._log("init").debug1("platform data from file=%s was loaded. Data=%s", platformFilename, self._platformDictionary)



    ###########################################
    # CAPTAIN CLIENT INITIALIZATION INTERFACE
    ##########################################

    def initCaptain (self, captain):
        """ set the captain object used by the class
        """
        self._captain = captain

    def initFromDictionary (self, data):
        """ Initializes the platform_basic directory using a dictionary. see "init" for more details
        """
        return self.init(platformBasicDir = data[self.INIT_PARAM_DATA_PLATFORM_BASIC_DIR],
                         platformType = data[self.INIT_PARAM_DATA_PLATFORM_TYPE])   
        
    def captainClient_initFromParamFile (self):
        """ Initializes the platform_basic directory from which all the platform data is loaded, and the platform type
        Fatal in case of failure
        """

        initParamFilesDirName = self._captain.getInitParamFilesDirName()
        initParamFileName = os.path.join(initParamFilesDirName, self._INIT_PARAM_FILE_NAME)
        try:
            if os.path.exists(initParamFileName):
                self._log("read-init-file").debug2("reading init file %s", initParamFileName)
                data = a.infra.format.json.readFromFile(self._log, initParamFileName)
            else:
                a.infra.process.processFatal("Failed to init platform data. File %s does not exists", initParamFileName)

        except Exception as exception:
            a.infra.process.processFatal("Failed to read platform data init file: %s", exception)
        
        self._log("init-values").debug2("Init values: '%s'", data)

        try:
            self.initFromDictionary(data)
        except Exception as exception:
            a.infra.process.processFatal("Failed to init platform data: %s", exception)


    #########################################################################################
    # CREATORS
    #########################################################################################

    def createPlatformBasicForPlatformType (self, platformType):
        """ Creates and returns a new platform basic for a specified platform type
        For usages that require information on other platform types
        """
        newPlatformBasic = PlatformBasic(self._log)
        newPlatformBasic.init(self._platformBasicDir, platformType)
        return newPlatformBasic


    #########################################################################################
    # DATA GETTER METHODS
    #########################################################################################

    def getPlatformType (self):
        """ Returns the platform type (a string) of this platform.
        """
        return self._platformDictionary[self.FIELD_PLATFORM]


    def getDiskProperty (self, diskName, field, dictionary = None):
        """ Returns a property of a disk.
        Arguments:
            diskName   - Constant (one of PlatformBasic.DISK_NAME_*) which is the name of the disk
            field      - Constant (one of PlatformBasic.DISK_FIELD_*) which is the name of the property (field)
            dictionary - If None, the dictionary of the initialized platform is used, o.w. should be a platform dictionary gotten 
        """
        if dictionary is None:
            dictionary = self._platformDictionary

        return dictionary[self.FIELD_DISKS][diskName][field]


    def getPartitionsUnderDisk (self, diskName, dictionary = None):
        """ Returns a list of all the partitions listed under the given disk.
        The list is ordered by the indices of the partitions.        
        Arguments:
            dictionary - a platform_data dictionary of a certain platform (result of getQmDictionary(), getQvmDictionary(), and so...)
            diskName   - string, name of the disk of which partitions should be returned

        Returns:    list of the disk-names of the partitions
                    Empty list, if `diskName` has no partition
                    None, if a disk named `diskName` does not exist in the dictionary.
        """
        return self._getDisksUnderDisk(diskName, diskTypeFilter = [self.TYPE_PARTITON], dictionary = dictionary)


    def getLogicalVolumesUnderDisk (self, diskName, dictionary = None):
        """ Returns a list of all the logical volume listed under the given disk (should usually be a volume group disk).
        The list is ordered by the indices of the volumes.        
        Arguments:
            dictionary - a platform_data dictionary of a certain platform (result of getQmDictionary(), getQvmDictionary(), and so...)
            diskName   - string, name of the disk of which volumes should be returned

        Returns:    list of the disk-names of the volumes
                    Empty list, if `diskName` has no volumes
                    None, if a disk named `diskName` does not exist in the dictionary.
        """
        return self._getDisksUnderDisk(diskName, diskTypeFilter = [self.TYPE_LV], dictionary = dictionary)


    def getVolumeGroupsUnderDisk (self, diskName, dictionary = None):
        """ Returns a list of all the volume groups listed under the given disk.
        The list is ordered by the indices of the groups.        
        Arguments:
            dictionary - a platform_data dictionary of a certain platform (result of getQmDictionary(), getQvmDictionary(), and so...)
            diskName   - string, name of the disk of which volumes should be returned

        Returns:    list of the disk-names of the groups
                    Empty list, if `diskName` has no groups
                    None, if a disk named `diskName` does not exist in the dictionary.
        """
        return self._getDisksUnderDisk(diskName, diskFormatFilter = [self.FORMAT_VG], dictionary = dictionary)


    def getRaidProperty (self, field, dictionary = None):
        """ Returns a property of the raid.
        Arguments:
            field      - Constant (one of PlatformBasic.DISK_FIELD_*) which is the name of the property (field)
            dictionary - If None, the dictionary of the initialized platform is used, o.w. should be a platform dictionary gotten 
        """
        if dictionary is None:
            dictionary = self._platformDictionary

        return dictionary[self.FIELD_RAID][field]

    def getBiosProperty (self, field, dictionary = None):
        """ Returns a property of the bios.
        Arguments:
            field      - Constant (one of PlatformBasic.DISK_FIELD_*) which is the name of the property (field)
            dictionary - If None, the dictionary of the initialized platform is used, o.w. should be a platform dictionary gotten 
        """
        if dictionary is None:
            dictionary = self._platformDictionary

        return dictionary[self.FIELD_BIOS][field]

    #########################################################################################
    # STATIC METHODS
    #########################################################################################

    @classmethod
    def s_createInitParamFile (cls, dbgLog, initParamFilesDirName,  dictionary):
        a.infra.format.json.writeToFile(dbgLog, dictionary, os.path.join(initParamFilesDirName, cls._INIT_PARAM_FILE_NAME), indent=4)


    #########################################################################################
    # LOGIC PRIVATE
    #########################################################################################

    def _getDisksUnderDisk (self, diskName, diskTypeFilter = None, diskFormatFilter = None, dictionary = None):
        """ Returns a list of all the partitions listed under the given disk.
        The list is ordered by the indices of the partitions.        
        Arguments:
            dictionary       - a platform_data dictionary of a certain platform (result of getQmDictionary(), getQvmDictionary(), and so...)
            diskName         - string, name of the disk of which partitions should be returned
            diskTypeFilter   - a list of disk types, only these types of disks will be returned (if None - not used)
            diskFormatFilter - a list of disk formats, only these types of disks will be returned (if None - not used)

        Returns:    list of the disk-names of the partitions
                    Empty list, if `diskName` has no partition
                    None, if a disk named `diskName` does not exist in the dictionary.
        """
        if dictionary is None:
            dictionary = self._platformDictionary

        if diskName not in dictionary[self.FIELD_DISKS]:
            return None

        disksAndDictionaryUnderDisk = []

        # find disks that the given disk is their parents, and are also partitions
        for disk, diskDictionary in dictionary[self.FIELD_DISKS].iteritems():
            if (diskTypeFilter is None) or (diskDictionary[self.DISK_FIELD_PARENT] == diskName and diskDictionary[self.DISK_FIELD_TYPE] in diskTypeFilter):
                if (diskFormatFilter is None) or (diskDictionary[self.DISK_FIELD_PARENT] == diskName and diskDictionary[self.DISK_FIELD_FORMAT] in diskFormatFilter):
                    disksAndDictionaryUnderDisk.append((disk, diskDictionary))

        disksAndDictionaryUnderDisk = sorted(disksAndDictionaryUnderDisk, key = lambda (disk, dictionary): dictionary[self.DISK_FIELD_INDEX])
        disksUnderDisk = [disk for disk, diskDictionary in disksAndDictionaryUnderDisk]

        return disksUnderDisk

    #########################################################################################
    # UTILITIES PRIVATE
    #########################################################################################

    def _loadFromJson (self, filename):
        with open(filename, 'r') as fileInput:
            return json.load(fileInput)

