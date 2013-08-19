#
# Copyright Qwilt, 2013
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: Shmulika
# 

class PlatformBase(object):
    """ The Handler class defines the dictionary of the platform data.
    It is an API class used by other classes in other projects (merged into them manually, not released automatically).
    """

    ####################################################################################
    # NOTE: All the constants are API to using classes, maintain backward compatability!
    ####################################################################################

    ##### GLOBAL DICTIONARY CONSTANTS
    ### VALUES
    FILE_VERSION_VALUE  = "1"

    ## FIELDS
    FIELD_FILE_VERSION     = "version"
    FIELD_DISKS            = "disks"
    FIELD_RAID             = "raid"    
    FIELD_PLATFORM         = "platform"
    FIELD_BIOS             = "bios"


    ##### DISK DICTIONARY CONSTANTS
    ## DISK NAMES
    # System disk's disk + partitions
    DISK_NAME_SYS_DISK = "sys_disk"
    DISK_NAME_SYS_BOOT = "sys_boot"
    DISK_NAME_SYS_VG   = "sys_vg"
    
    # System disk's logical volumes
    DISK_NAME_SYS_SYS   = "sys_sys"
    DISK_NAME_SYS_VITAL = "sys_vital"
    DISK_NAME_SYS_DATA  = "sys_data"
    DISK_NAME_SYS_USER  = "sys_user"
    DISK_NAME_SYS_RFS0  = "sys_rfs0"
    DISK_NAME_SYS_RFS1  = "sys_rfs1"
    DISK_NAME_SYS_RFS2  = "sys_rfs2"
    DISK_NAME_SYS_SWAP  = "sys_swap"

    # SD disk + partitions
    DISK_NAME_SD_DISK  = "sd_disk"
    DISK_NAME_SD_BOOT  = "sd_boot"
    DISK_NAME_SD_FAT   = "sd_fat"
    DISK_NAME_SD_VITAL = "sd_vital"
    DISK_NAME_SD_MAIN  = "sd_main"

    ## FIELD NAMES
    DISK_FIELD_TYPE            = "type"                  # these should have the same values on all systems
    DISK_FIELD_FORMAT          = "format"
    DISK_FIELD_FS_TYPE         = "filesystem-type"               
    DISK_FIELD_FS_LABEL        = "filesystem-label"
    DISK_FIELD_INDEX           = "index"
    DISK_FIELD_MOUNT_POINT     = "mount-point"
    DISK_FIELD_PARENT          = "parent"
    DISK_FIELD_LVM_NAME        = "lvm-name"    

    DISK_FIELD_OS_DEVICE       = "os-device"             # these have platform-specific values
    DISK_FIELD_GRUB_DEVICE     = "grub-device"  
    DISK_FIELD_PARTITION_TYPE  = "partition_type"  
    DISK_FIELD_PARTITION_START = "partition_start"
    DISK_FIELD_PARTITION_END   = "partition_end"
    DISK_FIELD_SIZE            = "size"
    DISK_FIELD_IDENTIFIER      = "identifier"
    DISK_FIELD_DEVICE_MODEL    = "device-model"
    DISK_FIELD_SCSI_DISK       = "scsi-disk"
    

    ## RAID FIELD NAMES
    RAID_FIELD_CONTROLLER_TYPE    = "type"                  # these should have the same values on all systems
    RAID_FIELD_NUM_OF_CONTROLLERS = "num"
    RAID_FIELD_SYSTEM_VDISK_NAME  = "system-vdisk-name"
    RAID_FIELD_SYSTEM_OS_DEVICE   = "system-os-device"

    ## BIOS FIELD NAMES
    BIOS_FIELD_CONTROLLER_TYPE    = "type"  
    BIOS_FIELD_SETTINGS_LIST      = "settings"  
    BIOS_SETTINGS_FIELD_ATTRIBUTE = "attribute"
    BIOS_SETTINGS_FIELD_TYPE      = "type"
    BIOS_SETTINGS_FIELD_VALUE     = "value"
    BIOS_SETTINGS_FIELD_IS_MANDATORY = "is-mandatory"


    ## FIELD ENUM VALUES
    NONE_VALUE        = None
                      
    TYPE_DISK         = "disk" # TODO(shmulika): name not expliciti enough!!!!!!!!!!!!!!!!
    TYPE_PARTITON     = "partition"
    TYPE_LV           = "logical-volume"

    FORMAT_FILESYSTEM = "filesystem"
    FORMAT_VG         = "volume-group"    

    FILESYSTEM_BOOT   = "ext3"
    FILESYSTEM_VITAL  = "ext3"
    FILESYSTEM_COMMON = "ext4"
    FILESYSTEM_SWAP   = "swap"
    FILESYSTEM_FAT    = "fat32"

    IDENTIFIER_MODEL  = DISK_FIELD_DEVICE_MODEL
    IDENTIFIER_SCSI   = DISK_FIELD_SCSI_DISK

    RAID_CONTROLLER_TYPE_DELL = "dell"

    BIOS_CONTROLLER_TYPE_DELL = "dell"

    BIOS_SETTINGS_TYPE_SETTING = "setting"
    BIOS_SETTINGS_TYPE_SEQUENCE = "sequence"
    
        
    ## PLATFORM_DATA FILENAMES
    PLATFORM_TYPE_QM_6M2  = "qm-6m2" 
    PLATFORM_TYPE_QVM_6V2 = "qvm-6v2"
    PLATFORM_TYPE_QB_6A2  = "qb-6a2" 
    PLATFORM_TYPE_QB_6B2  = "qb-6b2" 
    PLATFORM_TYPE_QB_10B5 = "qb-10b5"

    @staticmethod
    def s_getDataFileBaseName (platformName):
        return "%s.json"%platformName
    
    PLATFORM_BASIC_DATA_FILES_PREFIX = "basic"

    def __init__ (self):
        pass

    #########################################################################################
    # FIELD HANDLING METHODS
    #########################################################################################

    def isNoneValue (self, value):
        return value == self.NONE_VALUE


