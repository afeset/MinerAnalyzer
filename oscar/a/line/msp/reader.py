#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

if  __package__ is None:
    G_NAME_MODULE_LINE_MSP = "unknown"
    G_NAME_GROUP_LINE_MSP_READER = "unknown"
else:
    from . import G_NAME_MODULE_LINE_MSP 
    from . import G_NAME_GROUP_LINE_MSP_CLI_GEN 

import a.infra.format.json

class Reader:
    OUR_VANILLA_SIGNATURE_MSP_FIELD = "vanillaSignatures"
    OUR_SITE_GROUP_NAME_FOR_POLICY_MSP_FIELD = "siteGroupNameInPolicy"
    
    def __init__ (self, aLogger):
        self._log = None
        if aLogger:
            self._log = aLogger.createLogger(G_NAME_MODULE_LINE_MSP, G_NAME_GROUP_LINE_MSP_READER)
        self._sitesSet = set([])

    def loadData (self, aDataStr):
        if not type(aDataStr) is dict:
            if self._log:
                self._log("invalid-structure").error("got an invalid data format - not a dictionary but a %s", type(aDataStr))
            return "got an invalid data format - not a dictionary but a %s"%type(aDataStr)

        (errStr, siteList) = self._extractData(aDataStr)
        if errStr:
            return errStr

        self._sitesSet.update(set(siteList))

        return None

    def loadDataFromFile (self, aFileName):
        try:
            data = a.infra.format.json.readFromFile(self._log, aFileName)
        except IOError as e:
            if self._log:
                self._log("read-failed").exception("failed to read msp file '%s': %s", aFileName, e.strerror)
            return e.strerror

        return self.loadData(data)

    def clear (self):
        self._sitesSet = set([])

    def generateCliScript(self):
        output = []
        for site in sorted(self._sitesSet):
            if self._log:
                self._log("adding-to-cli").exception("adding to cli site '%s'", site)
            output += ["tech content signatures sites site %s\n"%site,"!\n"]
        return output


    def _extractData(self, aData):
        if not self.OUR_VANILLA_SIGNATURE_MSP_FIELD in aData:
            if self._log:
                self._log("no-vanilla").error("missing '%s' field in MSP file", self.OUR_VANILLA_SIGNATURE_MSP_FIELD)
            return ("missing '%s' field in MSP file"%self.OUR_VANILLA_SIGNATURE_MSP_FIELD, [])

        signaturesList = aData[self.OUR_VANILLA_SIGNATURE_MSP_FIELD]

        if not type(signaturesList) is list:
            if self._log:
                self._log("invalid-structure").error("got an invalid signature-list - not a list (%s)",type(signaturesList))
                return ("got an invalid '%s' - not a list but a %s"%(self.OUR_VANILLA_SIGNATURE_MSP_FIELD,type(signaturesList)), [])
                        
        sitesList = []
        counter = 0;
        for element in signaturesList:
            if not type(element) is dict:
                if self._log:
                    self._log("invalid-structure").error("got an invalid element in the signature-list: not a dictionary but a %s. element number %d",type(element), counter)
                    return ("got an invalid element in the signature-list: not a dictionary but a %s. element number %d"%(type(element), counter), [])
            if not self.OUR_SITE_GROUP_NAME_FOR_POLICY_MSP_FIELD in element:
                if self._log:
                    self._log("no-site").debug2("no '%s' in element number %d",self.OUR_SITE_GROUP_NAME_FOR_POLICY_MSP_FIELD, counter)
                    counter += 1
                    continue
            site = element[self.OUR_SITE_GROUP_NAME_FOR_POLICY_MSP_FIELD]
            if not type(site) is str:
                if self._log:
                    self._log("invalid-structure").error("got an invalid site - not a string but a %s. element number %d",type(site), counter)
                    return ("got an invalid site - not a string but a %s. element number %d"%(type(site), counter), [])

            if site in sitesList:
                if self._log:
                    self._log("site-already-found").debug3("finding site '%s' more than once",site)
            else:
                if self._log:
                    self._log("site-found").debug2("finding site '%s'",site)
                sitesList.append(site)
            counter += 1
        
        return (None, sitesList)


        
    





