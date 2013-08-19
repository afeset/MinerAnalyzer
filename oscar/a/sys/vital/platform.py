#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

import json
import os

class VitalPlatformData:
    __LEGACY_FIELD_NAME_PROPERTIES_FILE_VERSION="properties-file-version"

    LEGACY_FIELD_NAME_TYPE="type"#old - from "version 0"
    LEGACY_FIELD_TYPE_VALUE_QB100="qb100"
    LEGACY_FIELD_TYPE_VALUE_QVM30="qvm30"
    LEGACY_FIELD_TYPE_VALUE_QM10="qm10"

    LEGACY_FIELD_NAME_PLATFORM="platform"
    LEGACY_FIELD_PLATFORM_VALUE_QB_100 = "QB-100"
    LEGACY_FIELD_PLATFORM_VALUE_QVM_30 = "QVM-30"
    LEGACY_FIELD_PLATFORM_VALUE_QM_10 = "QM-10"

    LEGACY_FIELD_NAME_SUB_PLATFORM="sub-platform"
    LEGACY_FIELD_SUB_PLATFORM_VALUE_6A2 = "6a2"
    LEGACY_FIELD_SUB_PLATFORM_VALUE_6B2 = "6b2"
    LEGACY_FIELD_SUB_PLATFORM_VALUE_10B5 = "10b5"
    LEGACY_FIELD_SUB_PLATFORM_VALUE_6V2 = "6v2"
    LEGACY_FIELD_SUB_PLATFORM_VALUE_6M2 = "6m2"

    LEGACY_FIELD_NAME_PRIMARY_KERNEL_TYPE="primary-kernel-type"
    LEGACY_FIELD_NAME_SECONDARY_KERNEL_TYPE="secondary-kernel-type"
    LEGACY_FIELD_KERNEL_TYPE_VALUE_STANDARD="standard"
    LEGACY_FIELD_KERNEL_TYPE_VALUE_CUSTOM="custom"
    LEGACY_FIELD_KERNEL_TYPE_VALUE_NONE="none"

    ###### new format fields #################################3
    __FIELD_NAME_FORMAT_VERSION="format-version"
    FIELD_NAME_PLATFORM="platform"
    FIELD_PLATFORM_VALUE_QB_6A2   = "qb-6a2"
    FIELD_PLATFORM_VALUE_QB_6B2   = "qb-6b2"
    FIELD_PLATFORM_VALUE_QB_10B5  = "qb-10b5"
    FIELD_PLATFORM_VALUE_QVM_6V2  = "qvm-6v2"
    FIELD_PLATFORM_VALUE_QM_6M2   = "qm-6m2"

    ##############################
    FORMAT_VERSION = 100

    
    def __init__ (self):
        self._data=None
        self._legacyData=None

    def getField (self, fieldName):
        return self._data[fieldName]

    def getLegacyField (self, fieldName):
        return self._legacyData[fieldName]

    def getAsStr(self):        
        return str(self._data)

    def getLegacyAsStr(self):        
        return str(self._legacyData)

    def loadDict(self, data):            
        """loading a standard dictionary. Throws exception in case of error"""
        self._data = data
        self._legacyFromStandard()

    def loadLegacyDict(self, data):            
        """loading a legacy dictionary. Throws exception in case of error"""
        self._legacyData = data
        self._fixLegacyData()
        self._standardFromLegacy()

    def loadAsMini(self): 
        data = {self.__FIELD_NAME_FORMAT_VERSION: self.FORMAT_VERSION, self.FIELD_NAME_PLATFORM: self.FIELD_PLATFORM_VALUE_QM_6M2}
        self.loadDict(data)

    def loadAsQb6B2 (self):
        data = {self.__FIELD_NAME_FORMAT_VERSION: self.FORMAT_VERSION, self.FIELD_NAME_PLATFORM: self.FIELD_PLATFORM_VALUE_QB_6B2}
        self.loadDict(data)

    def loadAsQb10B5 (self):
        data = {self.__FIELD_NAME_FORMAT_VERSION: self.FORMAT_VERSION, self.FIELD_NAME_PLATFORM: self.FIELD_PLATFORM_VALUE_QB_10B5}
        self.loadDict(data)


    def getDict (self):
        return self._data

    def getLegacyDict (self):
        return self._legacyData

    def loadFromFile(self, fileName):   
        """loading a legacy file. Throws exception in case of error"""
        with open(fileName, 'r') as fd:
            data = json.load(fd)
            self.loadDict(data)            

    def loadFromLegacyFile(self, fileName):   
        """loading a legacy file. Throws exception in case of error"""
        with open(fileName, 'r') as fd:
            data = json.load(fd)
            self.loadLegacyDict(data)       

    def saveToFile(self, fileName):   
        """saving a legacy file. Throws exception in case of error"""
        with open(fileName, 'wt') as fd:
            json.dump(self.getDict(), fd, indent=4)

    def saveToLegacyFile(self, fileName):   
        """saving a legacy file. Throws exception in case of error"""
        with open(fileName, 'wt') as fd:
            json.dump(self.getLegacyDict(), fd, indent=4)
            
    def _fixLegacyData (self):
        if not self.__LEGACY_FIELD_NAME_PROPERTIES_FILE_VERSION in self._legacyData:
            self._legacyData[self.__LEGACY_FIELD_NAME_PROPERTIES_FILE_VERSION]=0

        if self._legacyData[self.__LEGACY_FIELD_NAME_PROPERTIES_FILE_VERSION] <= 0:
            #if self.LEGACY_FIELD_NAME_TYPE does not exists we will fly to kibinimat. we are counting on it
            if self._legacyData[self.LEGACY_FIELD_NAME_TYPE]==self.LEGACY_FIELD_TYPE_VALUE_QB100:
                self._legacyData[self.LEGACY_FIELD_NAME_PLATFORM]=self.LEGACY_FIELD_PLATFORM_VALUE_QB_100
                self._legacyData[self.LEGACY_FIELD_NAME_SUB_PLATFORM]=self.LEGACY_FIELD_SUB_PLATFORM_VALUE_6A2
                self._legacyData[self.LEGACY_FIELD_NAME_PRIMARY_KERNEL_TYPE]=self.LEGACY_FIELD_KERNEL_TYPE_VALUE_CUSTOM
                self._legacyData[self.LEGACY_FIELD_NAME_SECONDARY_KERNEL_TYPE]=self.LEGACY_FIELD_KERNEL_TYPE_VALUE_STANDARD

            if self._legacyData[self.LEGACY_FIELD_NAME_TYPE]==self.LEGACY_FIELD_TYPE_VALUE_QVM30:
                self._legacyData[self.LEGACY_FIELD_NAME_PLATFORM]=self.LEGACY_FIELD_PLATFORM_VALUE_QVM_30
                self._legacyData[self.LEGACY_FIELD_NAME_SUB_PLATFORM]=self.LEGACY_FIELD_SUB_PLATFORM_VALUE_6V2
                self._legacyData[self.LEGACY_FIELD_NAME_PRIMARY_KERNEL_TYPE]=self.LEGACY_FIELD_KERNEL_TYPE_VALUE_STANDARD
                self._legacyData[self.LEGACY_FIELD_NAME_SECONDARY_KERNEL_TYPE]=self.LEGACY_FIELD_KERNEL_TYPE_VALUE_STANDARD

            if self._legacyData[self.LEGACY_FIELD_NAME_TYPE]==self.LEGACY_FIELD_TYPE_VALUE_QM10:
                self._legacyData[self.LEGACY_FIELD_NAME_PLATFORM]=self.LEGACY_FIELD_PLATFORM_VALUE_QM_10
                self._legacyData[self.LEGACY_FIELD_NAME_SUB_PLATFORM]=self.LEGACY_FIELD_SUB_PLATFORM_VALUE_6M2
                self._legacyData[self.LEGACY_FIELD_NAME_PRIMARY_KERNEL_TYPE]=self.LEGACY_FIELD_KERNEL_TYPE_VALUE_NONE
                self._legacyData[self.LEGACY_FIELD_NAME_SECONDARY_KERNEL_TYPE]=self.LEGACY_FIELD_KERNEL_TYPE_VALUE_NONE 

            self._legacyData[self.__LEGACY_FIELD_NAME_PROPERTIES_FILE_VERSION] = 1

    def _standardFromLegacy (self):
        self._data = {}
        self._data[self.__FIELD_NAME_FORMAT_VERSION]=self.FORMAT_VERSION
        if self._legacyData[self.LEGACY_FIELD_NAME_SUB_PLATFORM]==self.LEGACY_FIELD_SUB_PLATFORM_VALUE_6A2:
            platform = self.FIELD_PLATFORM_VALUE_QB_6A2
        elif self._legacyData[self.LEGACY_FIELD_NAME_SUB_PLATFORM]==self.LEGACY_FIELD_SUB_PLATFORM_VALUE_6B2:
            platform = self.FIELD_PLATFORM_VALUE_QB_6B2
        elif self._legacyData[self.LEGACY_FIELD_NAME_SUB_PLATFORM]==self.LEGACY_FIELD_SUB_PLATFORM_VALUE_10B5:
            platform = self.FIELD_PLATFORM_VALUE_QB_10B5
        elif self._legacyData[self.LEGACY_FIELD_NAME_SUB_PLATFORM]==self.LEGACY_FIELD_SUB_PLATFORM_VALUE_6V2:
            platform = self.FIELD_PLATFORM_VALUE_QVM_6V2
        else:# self._legacyData[self.LEGACY_FIELD_NAME_SUB_PLATFORM]==self.LEGACY_FIELD_SUB_PLATFORM_VALUE_6M2:
            platform = self.FIELD_PLATFORM_VALUE_QM_6M2

        self._data[self.FIELD_NAME_PLATFORM] = platform

    def _legacyFromStandard (self):
        self._legacyData={}
        if self._data[self.FIELD_NAME_PLATFORM]==self.FIELD_PLATFORM_VALUE_QB_6A2:
            self._legacyData[self.LEGACY_FIELD_NAME_TYPE]=self.LEGACY_FIELD_TYPE_VALUE_QB100
            self._legacyData[self.LEGACY_FIELD_NAME_PLATFORM]=self.LEGACY_FIELD_PLATFORM_VALUE_QB_100
            self._legacyData[self.LEGACY_FIELD_NAME_SUB_PLATFORM]=self.LEGACY_FIELD_SUB_PLATFORM_VALUE_6A2
            self._legacyData[self.LEGACY_FIELD_NAME_PRIMARY_KERNEL_TYPE]=self.LEGACY_FIELD_KERNEL_TYPE_VALUE_CUSTOM
            self._legacyData[self.LEGACY_FIELD_NAME_SECONDARY_KERNEL_TYPE]=self.LEGACY_FIELD_KERNEL_TYPE_VALUE_STANDARD
    
        if self._data[self.FIELD_NAME_PLATFORM]==self.FIELD_PLATFORM_VALUE_QB_6B2:
            self._legacyData[self.LEGACY_FIELD_NAME_TYPE]=self.LEGACY_FIELD_TYPE_VALUE_QB100
            self._legacyData[self.LEGACY_FIELD_NAME_PLATFORM]=self.LEGACY_FIELD_PLATFORM_VALUE_QB_100
            self._legacyData[self.LEGACY_FIELD_NAME_SUB_PLATFORM]=self.LEGACY_FIELD_SUB_PLATFORM_VALUE_6B2
            self._legacyData[self.LEGACY_FIELD_NAME_PRIMARY_KERNEL_TYPE]=self.LEGACY_FIELD_KERNEL_TYPE_VALUE_CUSTOM
            self._legacyData[self.LEGACY_FIELD_NAME_SECONDARY_KERNEL_TYPE]=self.LEGACY_FIELD_KERNEL_TYPE_VALUE_STANDARD

        if self._data[self.FIELD_NAME_PLATFORM]==self.FIELD_PLATFORM_VALUE_QB_10B5:
            self._legacyData[self.LEGACY_FIELD_NAME_TYPE]=self.LEGACY_FIELD_TYPE_VALUE_QB100
            self._legacyData[self.LEGACY_FIELD_NAME_PLATFORM]=self.LEGACY_FIELD_PLATFORM_VALUE_QB_100
            self._legacyData[self.LEGACY_FIELD_NAME_SUB_PLATFORM]=self.LEGACY_FIELD_SUB_PLATFORM_VALUE_10B5
            self._legacyData[self.LEGACY_FIELD_NAME_PRIMARY_KERNEL_TYPE]=self.LEGACY_FIELD_KERNEL_TYPE_VALUE_CUSTOM
            self._legacyData[self.LEGACY_FIELD_NAME_SECONDARY_KERNEL_TYPE]=self.LEGACY_FIELD_KERNEL_TYPE_VALUE_STANDARD

        if self._data[self.FIELD_NAME_PLATFORM]==self.FIELD_PLATFORM_VALUE_QVM_6V2:
            self._legacyData[self.LEGACY_FIELD_NAME_TYPE]=self.LEGACY_FIELD_TYPE_VALUE_QVM30
            self._legacyData[self.LEGACY_FIELD_NAME_PLATFORM]=self.LEGACY_FIELD_PLATFORM_VALUE_QVM_30
            self._legacyData[self.LEGACY_FIELD_NAME_SUB_PLATFORM]=self.LEGACY_FIELD_SUB_PLATFORM_VALUE_6V2
            self._legacyData[self.LEGACY_FIELD_NAME_PRIMARY_KERNEL_TYPE]=self.LEGACY_FIELD_KERNEL_TYPE_VALUE_STANDARD
            self._legacyData[self.LEGACY_FIELD_NAME_SECONDARY_KERNEL_TYPE]=self.LEGACY_FIELD_KERNEL_TYPE_VALUE_STANDARD
    
        if self._data[self.FIELD_NAME_PLATFORM]==self.FIELD_PLATFORM_VALUE_QM_6M2:
            self._legacyData[self.LEGACY_FIELD_NAME_TYPE]=self.LEGACY_FIELD_TYPE_VALUE_QM10
            self._legacyData[self.LEGACY_FIELD_NAME_PLATFORM]=self.LEGACY_FIELD_PLATFORM_VALUE_QM_10
            self._legacyData[self.LEGACY_FIELD_NAME_SUB_PLATFORM]=self.LEGACY_FIELD_SUB_PLATFORM_VALUE_6M2
            self._legacyData[self.LEGACY_FIELD_NAME_PRIMARY_KERNEL_TYPE]=self.LEGACY_FIELD_KERNEL_TYPE_VALUE_NONE
            self._legacyData[self.LEGACY_FIELD_NAME_SECONDARY_KERNEL_TYPE]=self.LEGACY_FIELD_KERNEL_TYPE_VALUE_NONE 
    
        self._legacyData[self.__LEGACY_FIELD_NAME_PROPERTIES_FILE_VERSION] = 1


    @classmethod
    def s_getDirectory(cls, vitalPath):
        __pychecker__="unusednames=cls"
        return os.path.join(vitalPath,"platform")

    @classmethod
    def s_getDefaultFileName(cls, vitalPath):
        __pychecker__="unusednames=cls"
        return os.path.join(vitalPath,"platform/platform.json")

    @classmethod
    def s_getLegacyDirectory(cls, vitalPath):
        __pychecker__="unusednames=cls"
        return os.path.join(vitalPath,"platform/0/var")

    @classmethod
    def s_getLegacyDefaultFileName(cls, vitalPath):
        __pychecker__="unusednames=cls"
        return os.path.join(vitalPath,"platform/0/var/properties.json")


