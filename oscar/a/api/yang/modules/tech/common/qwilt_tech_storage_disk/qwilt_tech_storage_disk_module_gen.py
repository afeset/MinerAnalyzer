
# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes


class DiskTypesType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kRaid0Disk=_Type_(1, "kRaid0Disk", "raid0-disk")
    
    kRaid1Disk=_Type_(2, "kRaid1Disk", "raid1-disk")
    
    kRaid1Array=_Type_(3, "kRaid1Array", "raid1-array")
    
    kVolume=_Type_(4, "kVolume", "volume")
    

    @staticmethod
    def isValidValue (value):
        return DiskTypesType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return DiskTypesType._Type_.getByValue(value)


class DiskOperationalStatusType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kDown=_Type_(2, "kDown", "down")
    
    kUp=_Type_(1, "kUp", "up")
    

    @staticmethod
    def isValidValue (value):
        return DiskOperationalStatusType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return DiskOperationalStatusType._Type_.getByValue(value)


class RaidArrayImplementationType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kDirectory=_Type_(3, "kDirectory", "directory")
    
    kNone=_Type_(0, "kNone", "none")
    
    kSimulatedDevice=_Type_(2, "kSimulatedDevice", "simulated-device")
    
    kDell=_Type_(1, "kDell", "dell")
    

    @staticmethod
    def isValidValue (value):
        return RaidArrayImplementationType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return RaidArrayImplementationType._Type_.getByValue(value)


class FileSystemOperationalStatusType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kDown=_Type_(3, "kDown", "down")
    
    kNone=_Type_(0, "kNone", "none")
    
    kUnknown=_Type_(1, "kUnknown", "unknown")
    
    kUp=_Type_(2, "kUp", "up")
    

    @staticmethod
    def isValidValue (value):
        return FileSystemOperationalStatusType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return FileSystemOperationalStatusType._Type_.getByValue(value)


class PhysicalStateType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kReady=_Type_(2, "kReady", "ready")
    
    kForeign=_Type_(1, "kForeign", "foreign")
    
    kFault=_Type_(5, "kFault", "fault")
    
    kAbsent=_Type_(4, "kAbsent", "absent")
    
    kOnline=_Type_(3, "kOnline", "online")
    

    @staticmethod
    def isValidValue (value):
        return PhysicalStateType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return PhysicalStateType._Type_.getByValue(value)


class PhysicalStatusType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kFailure=_Type_(2, "kFailure", "failure")
    
    kOk=_Type_(1, "kOk", "ok")
    

    @staticmethod
    def isValidValue (value):
        return PhysicalStatusType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return PhysicalStatusType._Type_.getByValue(value)


class FileSystemOperationalStatusReasonType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kNoDevice=_Type_(5, "kNoDevice", "no-device")
    
    kOk=_Type_(0, "kOk", "ok")
    
    kUuidError=_Type_(2, "kUuidError", "uuid-error")
    
    kUnknown=_Type_(1, "kUnknown", "unknown")
    
    kFileSystemError=_Type_(6, "kFileSystemError", "file-system-error")
    
    kUuidMismatch=_Type_(3, "kUuidMismatch", "uuid-mismatch")
    
    kMountError=_Type_(4, "kMountError", "mount-error")
    

    @staticmethod
    def isValidValue (value):
        return FileSystemOperationalStatusReasonType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return FileSystemOperationalStatusReasonType._Type_.getByValue(value)


class DiskPhysicalImplementationType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kDirectory=_Type_(3, "kDirectory", "directory")
    
    kNone=_Type_(0, "kNone", "none")
    
    kSimulatedDevice=_Type_(2, "kSimulatedDevice", "simulated-device")
    
    kDell=_Type_(1, "kDell", "dell")
    

    @staticmethod
    def isValidValue (value):
        return DiskPhysicalImplementationType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return DiskPhysicalImplementationType._Type_.getByValue(value)


class PhysicalFailurePredictedType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kTrue=_Type_(1, "kTrue", "true")
    
    kFalse=_Type_(0, "kFalse", "false")
    

    @staticmethod
    def isValidValue (value):
        return PhysicalFailurePredictedType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return PhysicalFailurePredictedType._Type_.getByValue(value)


class ContentDiskFailureReasonType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kNone=_Type_(0, "kNone", "none")
    
    kFileSystemError=_Type_(5, "kFileSystemError", "file-system-error")
    
    kRaidError=_Type_(4, "kRaidError", "raid-error")
    
    kAbsent=_Type_(2, "kAbsent", "absent")
    
    kPhysicalError=_Type_(3, "kPhysicalError", "physical-error")
    
    kOther=_Type_(1, "kOther", "other")
    

    @staticmethod
    def isValidValue (value):
        return ContentDiskFailureReasonType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return ContentDiskFailureReasonType._Type_.getByValue(value)


class DiskOperationalStatusReasonType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kNone=_Type_(0, "kNone", "none")
    
    kFileSystemError=_Type_(5, "kFileSystemError", "file-system-error")
    
    kRaidError=_Type_(4, "kRaidError", "raid-error")
    
    kAbsent=_Type_(2, "kAbsent", "absent")
    
    kPhysicalError=_Type_(3, "kPhysicalError", "physical-error")
    
    kOther=_Type_(1, "kOther", "other")
    

    @staticmethod
    def isValidValue (value):
        return DiskOperationalStatusReasonType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return DiskOperationalStatusReasonType._Type_.getByValue(value)


class FileSystemTypeType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kExt3=_Type_(3, "kExt3", "ext3")
    
    kNone=_Type_(0, "kNone", "none")
    
    kUnknown=_Type_(1, "kUnknown", "unknown")
    
    kExt4=_Type_(4, "kExt4", "ext4")
    
    kDirectory=_Type_(5, "kDirectory", "directory")
    
    kOther=_Type_(2, "kOther", "other")
    

    @staticmethod
    def isValidValue (value):
        return FileSystemTypeType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return FileSystemTypeType._Type_.getByValue(value)


class RaidArrayStatusType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kFailure=_Type_(2, "kFailure", "failure")
    
    kOk=_Type_(1, "kOk", "ok")
    
    kCritical=_Type_(3, "kCritical", "critical")
    

    @staticmethod
    def isValidValue (value):
        return RaidArrayStatusType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return RaidArrayStatusType._Type_.getByValue(value)


class DiskFunctionalTypesType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kContent=_Type_(1, "kContent", "content")
    
    kSystem=_Type_(2, "kSystem", "system")
    

    @staticmethod
    def isValidValue (value):
        return DiskFunctionalTypesType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return DiskFunctionalTypesType._Type_.getByValue(value)


class RaidArrayRaidType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kNone=_Type_(0, "kNone", "none")
    
    kRaid1=_Type_(2, "kRaid1", "raid1")
    
    kRaid0=_Type_(1, "kRaid0", "raid0")
    

    @staticmethod
    def isValidValue (value):
        return RaidArrayRaidType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return RaidArrayRaidType._Type_.getByValue(value)


class RaidArrayStateType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kReady=_Type_(1, "kReady", "ready")
    
    kFault=_Type_(2, "kFault", "fault")
    

    @staticmethod
    def isValidValue (value):
        return RaidArrayStateType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return RaidArrayStateType._Type_.getByValue(value)




"""
Extracted from the below data: 
{
    "conditionalDebugName": null, 
    "enumTypes": [
        {
            "className": "DiskTypesType", 
            "enums": [
                {
                    "yangName": "raid0_disk", 
                    "displayName": "raid0-disk", 
                    "name": "kRaid0Disk", 
                    "value": "1"
                }, 
                {
                    "yangName": "raid1_disk", 
                    "displayName": "raid1-disk", 
                    "name": "kRaid1Disk", 
                    "value": "2"
                }, 
                {
                    "yangName": "raid1_array", 
                    "displayName": "raid1-array", 
                    "name": "kRaid1Array", 
                    "value": "3"
                }, 
                {
                    "yangName": "volume", 
                    "displayName": "volume", 
                    "name": "kVolume", 
                    "value": "4"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import DiskTypesType"
        }, 
        {
            "className": "DiskOperationalStatusType", 
            "enums": [
                {
                    "yangName": "disk_status_down", 
                    "displayName": "down", 
                    "name": "kDown", 
                    "value": "2"
                }, 
                {
                    "yangName": "disk_status_up", 
                    "displayName": "up", 
                    "name": "kUp", 
                    "value": "1"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import DiskOperationalStatusType"
        }, 
        {
            "className": "RaidArrayImplementationType", 
            "enums": [
                {
                    "yangName": "raid_array_implementation_type_directory", 
                    "displayName": "directory", 
                    "name": "kDirectory", 
                    "value": "3"
                }, 
                {
                    "yangName": "raid_array_implementation_type_none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "0"
                }, 
                {
                    "yangName": "raid_array_implementation_type_simulated_device", 
                    "displayName": "simulated-device", 
                    "name": "kSimulatedDevice", 
                    "value": "2"
                }, 
                {
                    "yangName": "raid_array_implementation_type_dell", 
                    "displayName": "dell", 
                    "name": "kDell", 
                    "value": "1"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import RaidArrayImplementationType"
        }, 
        {
            "className": "FileSystemOperationalStatusType", 
            "enums": [
                {
                    "yangName": "file_system_status_down", 
                    "displayName": "down", 
                    "name": "kDown", 
                    "value": "3"
                }, 
                {
                    "yangName": "file_system_status_none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "0"
                }, 
                {
                    "yangName": "file_system_status_unknown", 
                    "displayName": "unknown", 
                    "name": "kUnknown", 
                    "value": "1"
                }, 
                {
                    "yangName": "file_system_status_up", 
                    "displayName": "up", 
                    "name": "kUp", 
                    "value": "2"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import FileSystemOperationalStatusType"
        }, 
        {
            "className": "PhysicalStateType", 
            "enums": [
                {
                    "yangName": "ready", 
                    "displayName": "ready", 
                    "name": "kReady", 
                    "value": "2"
                }, 
                {
                    "yangName": "foreign", 
                    "displayName": "foreign", 
                    "name": "kForeign", 
                    "value": "1"
                }, 
                {
                    "yangName": "fault", 
                    "displayName": "fault", 
                    "name": "kFault", 
                    "value": "5"
                }, 
                {
                    "yangName": "absent", 
                    "displayName": "absent", 
                    "name": "kAbsent", 
                    "value": "4"
                }, 
                {
                    "yangName": "online", 
                    "displayName": "online", 
                    "name": "kOnline", 
                    "value": "3"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import PhysicalStateType"
        }, 
        {
            "className": "PhysicalStatusType", 
            "enums": [
                {
                    "yangName": "failure", 
                    "displayName": "failure", 
                    "name": "kFailure", 
                    "value": "2"
                }, 
                {
                    "yangName": "ok", 
                    "displayName": "ok", 
                    "name": "kOk", 
                    "value": "1"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import PhysicalStatusType"
        }, 
        {
            "className": "FileSystemOperationalStatusReasonType", 
            "enums": [
                {
                    "yangName": "no_device", 
                    "displayName": "no-device", 
                    "name": "kNoDevice", 
                    "value": "5"
                }, 
                {
                    "yangName": "file_system_reason_ok", 
                    "displayName": "ok", 
                    "name": "kOk", 
                    "value": "0"
                }, 
                {
                    "yangName": "uuid_error", 
                    "displayName": "uuid-error", 
                    "name": "kUuidError", 
                    "value": "2"
                }, 
                {
                    "yangName": "unknown", 
                    "displayName": "unknown", 
                    "name": "kUnknown", 
                    "value": "1"
                }, 
                {
                    "yangName": "file_system_status_file_system_error", 
                    "displayName": "file-system-error", 
                    "name": "kFileSystemError", 
                    "value": "6"
                }, 
                {
                    "yangName": "uuid_mismatch", 
                    "displayName": "uuid-mismatch", 
                    "name": "kUuidMismatch", 
                    "value": "3"
                }, 
                {
                    "yangName": "mount_error", 
                    "displayName": "mount-error", 
                    "name": "kMountError", 
                    "value": "4"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import FileSystemOperationalStatusReasonType"
        }, 
        {
            "className": "DiskPhysicalImplementationType", 
            "enums": [
                {
                    "yangName": "disk_physical_implementation_type_directory", 
                    "displayName": "directory", 
                    "name": "kDirectory", 
                    "value": "3"
                }, 
                {
                    "yangName": "disk_physical_implementation_type_none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "0"
                }, 
                {
                    "yangName": "disk_physical_implementation_type_simulated_device", 
                    "displayName": "simulated-device", 
                    "name": "kSimulatedDevice", 
                    "value": "2"
                }, 
                {
                    "yangName": "disk_physical_implementation_type_dell", 
                    "displayName": "dell", 
                    "name": "kDell", 
                    "value": "1"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import DiskPhysicalImplementationType"
        }, 
        {
            "className": "PhysicalFailurePredictedType", 
            "enums": [
                {
                    "yangName": "true", 
                    "displayName": "true", 
                    "name": "kTrue", 
                    "value": "1"
                }, 
                {
                    "yangName": "false", 
                    "displayName": "false", 
                    "name": "kFalse", 
                    "value": "0"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import PhysicalFailurePredictedType"
        }, 
        {
            "className": "ContentDiskFailureReasonType", 
            "enums": [
                {
                    "yangName": "none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "0"
                }, 
                {
                    "yangName": "file_system_error", 
                    "displayName": "file-system-error", 
                    "name": "kFileSystemError", 
                    "value": "5"
                }, 
                {
                    "yangName": "raid_error", 
                    "displayName": "raid-error", 
                    "name": "kRaidError", 
                    "value": "4"
                }, 
                {
                    "yangName": "content_disk_reason_absent", 
                    "displayName": "absent", 
                    "name": "kAbsent", 
                    "value": "2"
                }, 
                {
                    "yangName": "physical_error", 
                    "displayName": "physical-error", 
                    "name": "kPhysicalError", 
                    "value": "3"
                }, 
                {
                    "yangName": "content_disk_reason_other", 
                    "displayName": "other", 
                    "name": "kOther", 
                    "value": "1"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import ContentDiskFailureReasonType"
        }, 
        {
            "className": "DiskOperationalStatusReasonType", 
            "enums": [
                {
                    "yangName": "none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "0"
                }, 
                {
                    "yangName": "file_system_error", 
                    "displayName": "file-system-error", 
                    "name": "kFileSystemError", 
                    "value": "5"
                }, 
                {
                    "yangName": "raid_error", 
                    "displayName": "raid-error", 
                    "name": "kRaidError", 
                    "value": "4"
                }, 
                {
                    "yangName": "disk_reason_absent", 
                    "displayName": "absent", 
                    "name": "kAbsent", 
                    "value": "2"
                }, 
                {
                    "yangName": "physical_error", 
                    "displayName": "physical-error", 
                    "name": "kPhysicalError", 
                    "value": "3"
                }, 
                {
                    "yangName": "disk_reason_other", 
                    "displayName": "other", 
                    "name": "kOther", 
                    "value": "1"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import DiskOperationalStatusReasonType"
        }, 
        {
            "className": "FileSystemTypeType", 
            "enums": [
                {
                    "yangName": "file_system_type_ext3", 
                    "displayName": "ext3", 
                    "name": "kExt3", 
                    "value": "3"
                }, 
                {
                    "yangName": "file_system_type_none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "0"
                }, 
                {
                    "yangName": "file_system_type_unknown", 
                    "displayName": "unknown", 
                    "name": "kUnknown", 
                    "value": "1"
                }, 
                {
                    "yangName": "file_system_type_ext4", 
                    "displayName": "ext4", 
                    "name": "kExt4", 
                    "value": "4"
                }, 
                {
                    "yangName": "file_system_type_directory", 
                    "displayName": "directory", 
                    "name": "kDirectory", 
                    "value": "5"
                }, 
                {
                    "yangName": "file_system_type_other", 
                    "displayName": "other", 
                    "name": "kOther", 
                    "value": "2"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import FileSystemTypeType"
        }, 
        {
            "className": "RaidArrayStatusType", 
            "enums": [
                {
                    "yangName": "failure", 
                    "displayName": "failure", 
                    "name": "kFailure", 
                    "value": "2"
                }, 
                {
                    "yangName": "ok", 
                    "displayName": "ok", 
                    "name": "kOk", 
                    "value": "1"
                }, 
                {
                    "yangName": "critical", 
                    "displayName": "critical", 
                    "name": "kCritical", 
                    "value": "3"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import RaidArrayStatusType"
        }, 
        {
            "className": "DiskFunctionalTypesType", 
            "enums": [
                {
                    "yangName": "content", 
                    "displayName": "content", 
                    "name": "kContent", 
                    "value": "1"
                }, 
                {
                    "yangName": "system", 
                    "displayName": "system", 
                    "name": "kSystem", 
                    "value": "2"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import DiskFunctionalTypesType"
        }, 
        {
            "className": "RaidArrayRaidType", 
            "enums": [
                {
                    "yangName": "raid_array_raid_type_none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "0"
                }, 
                {
                    "yangName": "raid_array_raid_type_raid1", 
                    "displayName": "raid1", 
                    "name": "kRaid1", 
                    "value": "2"
                }, 
                {
                    "yangName": "raid_array_raid_type_raid0", 
                    "displayName": "raid0", 
                    "name": "kRaid0", 
                    "value": "1"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import RaidArrayRaidType"
        }, 
        {
            "className": "RaidArrayStateType", 
            "enums": [
                {
                    "yangName": "raid_array_state_ready", 
                    "displayName": "ready", 
                    "name": "kReady", 
                    "value": "1"
                }, 
                {
                    "yangName": "raid_array_state_fault", 
                    "displayName": "fault", 
                    "name": "kFault", 
                    "value": "2"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import RaidArrayStateType"
        }
    ], 
    "createTime": "2013", 
    "module": {
        "prefix": "qt_strg_dsk"
    }, 
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "common", 
            "qwilt_tech_storage_disk"
        ]
    }
}
"""


