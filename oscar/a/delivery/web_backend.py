#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: hagaia
# 

import os
import utils

#-------------------------------------------------------------------------------------------------
class WebBackend (object):

    def __init__ (self, log):
        self.__log = log

    #-------------------------------------------------------------------------------------------------    
    def init (self,deliveryConf):
        self.__webBackendFileName = os.path.join(deliveryConf.webStatusDir, deliveryConf.kConf.kWebAppFileName)
        self.__log("init-web-backend").info("Init Web Backend - File Name %s",self.__webBackendFileName)

    #-------------------------------------------------------------------------------------------------
    def writeTitelsDeliverd(self, num):

        fileNameTemp = self.__webBackendFileName + ".tmp"

        try:
            tempFile = open(fileNameTemp,'w')
        except IOError, e:            
            self.__log("open-temp").error("Failed to Open Temp File %s - %s",fileNameTemp,utils.parseErrnoToString(e))
            return False

        try:
            tempFile.write(str(num))
            retVal = True
        except Exception, e:            
            self.__log("write-temp").error("Failed to write to File %s - %s",fileNameTemp,utils.parseErrnoToString(e))
            retVal = False

        tempFile.close()

        if retVal:
            os.rename(fileNameTemp,self.__webBackendFileName)    
            self.__log("titels-deliverd").debug3("Write Report - Titels Deliverd = %s to File = %s", str(num),self.__webBackendFileName)

        return True
