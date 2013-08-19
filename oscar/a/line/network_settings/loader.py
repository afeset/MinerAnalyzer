#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

class Loader:
    CONFIG_SECTION_NETWORK_SETTINGS = "network-settings"
    CONFIG_VAR_NETWORK_SETTINGS_SIGNATURE_PREFIX = "signature"
    CONFIG_VAR_NETWORK_SETTINGS_SIGNATURE_SUBNET_SUFFIX = "subnet"
    CONFIG_VAR_NETWORK_SETTINGS_CGID_PREFIX = "cgid"
    CONFIG_VAR_NETWORK_SETTINGS_CGID_ALTERNATIVE_REDIRECT_SUFFIX = "alternative-redirect"
    CONFIG_VAR_NETWORK_SETTINGS_CGID_ALTERNATIVE_REDIRECT_ADDRESS_FORMAT_SUFFIX = "address-format"

    class SignatureData:
        class Subnet:
            def __init__ (self, ip, mask):
                self._ip = ip
                self._mask = mask

            def getQshellStr (self):
                return "{ipAddress={text=%s}, mask=%s}"%(self._ip, self._mask)

        def __init__ (self, signatureName):
            self._signatureName = signatureName
            self._subnets = []

        def addSubnet (self, ip, mask):
            self._subnets.append(self.Subnet(ip, mask))

        def getQshellSubnetStr (self):
            subnetsQshellStringsList = []
            for subnet in self._subnets:
                subnetsQshellStringsList.append(subnet.getQshellStr())
            subnetsQshellString = ",".join(subnetsQshellStringsList)

            qshellStr = "{signatureName=%s, subnets={ %s }, subnetsListControl={change=true}}"%(self._signatureName, subnetsQshellString)
            return qshellStr


    class CgidData:
        class AlternativeRedirectData:
            def __init__ (self):
                self._addressFormat = ""
            def setAddressFormat (self, addressFormat):
                self._addressFormat = addressFormat

            def getQshellStr (self):
                return '"%s"'%(self._addressFormat)

        def __init__ (self, cgid):
            self._cgid = cgid
            self._alternativeRedirectData = self.AlternativeRedirectData()
        def getAlternativeRedirectData (self):
            return self._alternativeRedirectData
        def getQshellAlternativeRedirectDataStr (self):
            qshellStr = "{cgid=%s, alternativeRedirectAddressFormat=%s}"%(self._cgid, self._alternativeRedirectData.getQshellStr())
            return qshellStr

    def __init__ (self):
        self._signaturesData = {}
        self._cgidsData = {}

        self._readErrors = []
    
    def readFromUserParamFile (self, cfg):        
        if cfg.has_section(self.CONFIG_SECTION_NETWORK_SETTINGS):
            for option in cfg.options(self.CONFIG_SECTION_NETWORK_SETTINGS):
                tokens = option.split(".")
                if tokens[0] == self.CONFIG_VAR_NETWORK_SETTINGS_SIGNATURE_PREFIX:
                    tokens = tokens[1:]
                    if not tokens:
                        self._readErrors.append("invalid option: %s"%option)
                        continue
                    signature = tokens[0]
                    tokens = tokens[1:]
                    if not tokens:
                        self._readErrors.append("invalid option: %s"%option)
                        continue

                    if not signature in self._signaturesData:
                        self._signaturesData[signature] = self.SignatureData(signature)
                    signatureData = self._signaturesData[signature]

                    if tokens[0] == self.CONFIG_VAR_NETWORK_SETTINGS_SIGNATURE_SUBNET_SUFFIX:
                        tokens = tokens[1:]
                        if tokens:
                            self._readErrors.append("invalid option: %s"%option)
                            continue
                        subnets = cfg.get(self.CONFIG_SECTION_NETWORK_SETTINGS,option).split(",")
                        for subnet in subnets:
                            ipAndMask = subnet.split("/")
                            if len(ipAndMask) == 1:
                                ipAndMask.append("32")
                            if len(ipAndMask) != 2:
                                self._readErrors.append("invalid subnet for option '%s': %s"%(option, subnet))
                                continue
                            signatureData.addSubnet(ipAndMask[0], ipAndMask[1])
                    else:
                        self._readErrors.append("invalid option: %s"%option)
                        continue

                elif tokens[0] == self.CONFIG_VAR_NETWORK_SETTINGS_CGID_PREFIX:
                    tokens = tokens[1:]
                    if not tokens:
                        self._readErrors.append("invalid option: %s"%option)
                        continue
                    cgid = tokens[0]
                    tokens = tokens[1:]
                    if not tokens:
                        self._readErrors.append("invalid option: %s"%option)
                        continue

                    if not cgid in self._cgidsData:
                        self._cgidsData[cgid] = self.CgidData(cgid)
                    cgidData = self._cgidsData[cgid]

                    if tokens[0] == self.CONFIG_VAR_NETWORK_SETTINGS_CGID_ALTERNATIVE_REDIRECT_SUFFIX:
                        tokens = tokens[1:]
                        if not tokens:
                            self._readErrors.append("invalid option: %s"%option)
                            continue
                        alternativeRedirectData = cgidData.getAlternativeRedirectData()
                        if tokens[0] == self.CONFIG_VAR_NETWORK_SETTINGS_CGID_ALTERNATIVE_REDIRECT_ADDRESS_FORMAT_SUFFIX:
                            tokens = tokens[1:]
                            if tokens:
                                self._readErrors.append("invalid option: %s"%option)
                                continue
                            addressFormat = cfg.get(self.CONFIG_SECTION_NETWORK_SETTINGS,option)
                            alternativeRedirectData.setAddressFormat(addressFormat)                            
                        else:
                            self._readErrors.append("invalid option: %s"%option)
                            continue

                    else:
                        self._readErrors.append("invalid option: %s"%option)
                        continue

                else:
                    self._readErrors.append("invalid option: %s"%option)
                    continue

    @classmethod
    def s_getUserParamFileData (cls, cfg):
        options = []
        if cfg.has_section(cls.CONFIG_SECTION_NETWORK_SETTINGS):
            options.append("[%s]"%cls.CONFIG_SECTION_NETWORK_SETTINGS)
            for option in cfg.options(cls.CONFIG_SECTION_NETWORK_SETTINGS):
                options.append("%s = %s"%(option, cfg.get(cls.CONFIG_SECTION_NETWORK_SETTINGS,option)))
        return "\n".join(options)

    def getReadErrors (self):
        return self._readErrors

    def getQshellCommand (self):
        subnetsForSignaturesQshellStringsList = []
        for signature in sorted(self._signaturesData):
            subnetsForSignaturesQshellStringsList.append(self._signaturesData[signature].getQshellSubnetStr())
        subnetsForSignaturesQshellString = ",".join(subnetsForSignaturesQshellStringsList)

        alternativeRedirectForCgidsQshellStringsList = []
        for cgid in sorted(self._cgidsData):
            alternativeRedirectForCgidsQshellStringsList.append(self._cgidsData[cgid].getQshellAlternativeRedirectDataStr())
        alternativeRedirectForCgidsQshellString = ",".join(alternativeRedirectForCgidsQshellStringsList)

        return "line.configSet(subnetsForSignatures={ %s }, subnetsForSignaturesListControl={change=true}, alternativeRedirectForCgids={ %s }, alternativeRedirectForCgidsListControl={change=true} )"%(subnetsForSignaturesQshellString, alternativeRedirectForCgidsQshellString)

