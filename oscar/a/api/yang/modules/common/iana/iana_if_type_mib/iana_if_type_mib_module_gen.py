
# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes


class Ianatunneltype(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kL2f=_Type_(7, "kL2f", "l2f")
    
    kSixtofour=_Type_(11, "kSixtofour", "sixToFour")
    
    kMinimal=_Type_(4, "kMinimal", "minimal")
    
    kPptp=_Type_(6, "kPptp", "pptp")
    
    kUdp=_Type_(8, "kUdp", "udp")
    
    kMsdp=_Type_(10, "kMsdp", "msdp")
    
    kTeredo=_Type_(14, "kTeredo", "teredo")
    
    kL2tp=_Type_(5, "kL2tp", "l2tp")
    
    kOther=_Type_(1, "kOther", "other")
    
    kIsatap=_Type_(13, "kIsatap", "isatap")
    
    kSixoverfour=_Type_(12, "kSixoverfour", "sixOverFour")
    
    kAtmp=_Type_(9, "kAtmp", "atmp")
    
    kGre=_Type_(3, "kGre", "gre")
    
    kDirect=_Type_(2, "kDirect", "direct")
    

    @staticmethod
    def isValidValue (value):
        return Ianatunneltype._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return Ianatunneltype._Type_.getByValue(value)


class Ianaiftype(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kIfGsn=_Type_(145, "kIfGsn", "if-gsn")
    
    kDocscableupstream=_Type_(129, "kDocscableupstream", "docsCableUpstream")
    
    kIpovercdlc=_Type_(109, "kIpovercdlc", "ipOverCdlc")
    
    kMacsecuncontrolledif=_Type_(232, "kMacsecuncontrolledif", "macSecUncontrolledIF")
    
    kCes=_Type_(133, "kCes", "ces")
    
    kArap=_Type_(88, "kArap", "arap")
    
    kVoicedid=_Type_(213, "kVoicedid", "voiceDID")
    
    kE1=_Type_(19, "kE1", "e1")
    
    kRpr=_Type_(225, "kRpr", "rpr")
    
    kRfc877x25=_Type_(5, "kRfc877x25", "rfc877x25")
    
    kDtm=_Type_(140, "kDtm", "dtm")
    
    kInterleave=_Type_(124, "kInterleave", "interleave")
    
    kIso88025tokenring=_Type_(9, "kIso88025tokenring", "iso88025TokenRing")
    
    kDs1=_Type_(18, "kDs1", "ds1")
    
    kX86laps=_Type_(242, "kX86laps", "x86Laps")
    
    kStarlan=_Type_(11, "kStarlan", "starLan")
    
    kAtmdxi=_Type_(105, "kAtmdxi", "atmDxi")
    
    kLocaltalk=_Type_(42, "kLocaltalk", "localTalk")
    
    kVoiceoverframerelay=_Type_(153, "kVoiceoverframerelay", "voiceOverFrameRelay")
    
    kCctemul=_Type_(61, "kCctemul", "cctEmul")
    
    kDigitalwrapperoverheadchannel=_Type_(186, "kDigitalwrapperoverheadchannel", "digitalWrapperOverheadChannel")
    
    kQ2931=_Type_(201, "kQ2931", "q2931")
    
    kHomepna=_Type_(220, "kHomepna", "homepna")
    
    kDvbrccmaclayer=_Type_(146, "kDvbrccmaclayer", "dvbRccMacLayer")
    
    kHiperlan2=_Type_(183, "kHiperlan2", "hiperlan2")
    
    kRs232=_Type_(33, "kRs232", "rs232")
    
    kIeee80212=_Type_(55, "kIeee80212", "ieee80212")
    
    kHdlc=_Type_(118, "kHdlc", "hdlc")
    
    kIeee80211=_Type_(71, "kIeee80211", "ieee80211")
    
    kDs0bundle=_Type_(82, "kDs0bundle", "ds0Bundle")
    
    kCoffee=_Type_(132, "kCoffee", "coffee")
    
    kV36=_Type_(65, "kV36", "v36")
    
    kMpegtransport=_Type_(214, "kMpegtransport", "mpegTransport")
    
    kRsrb=_Type_(79, "kRsrb", "rsrb")
    
    kReachdsl=_Type_(192, "kReachdsl", "reachDSL")
    
    kVirtualipaddress=_Type_(112, "kVirtualipaddress", "virtualIpAddress")
    
    kBgppolicyaccounting=_Type_(162, "kBgppolicyaccounting", "bgppolicyaccounting")
    
    kDcn=_Type_(141, "kDcn", "dcn")
    
    kAtmradio=_Type_(189, "kAtmradio", "atmRadio")
    
    kPropatm=_Type_(197, "kPropatm", "propAtm")
    
    kNsip=_Type_(27, "kNsip", "nsip")
    
    kLmp=_Type_(227, "kLmp", "lmp")
    
    kProteon10mbit=_Type_(12, "kProteon10mbit", "proteon10Mbit")
    
    kTdlc=_Type_(116, "kTdlc", "tdlc")
    
    kSiptg=_Type_(203, "kSiptg", "sipTg")
    
    kV35=_Type_(45, "kV35", "v35")
    
    kPdnetherloop1=_Type_(217, "kPdnetherloop1", "pdnEtherLoop1")
    
    kVoicefxs=_Type_(102, "kVoicefxs", "voiceFXS")
    
    kMyrinet=_Type_(99, "kMyrinet", "myrinet")
    
    kAflane8023=_Type_(59, "kAflane8023", "aflane8023")
    
    kSlip=_Type_(28, "kSlip", "slip")
    
    kIeee8023adlag=_Type_(161, "kIeee8023adlag", "ieee8023adLag")
    
    kVoiceem=_Type_(100, "kVoiceem", "voiceEM")
    
    kPropbwap2mp=_Type_(184, "kPropbwap2mp", "propBWAp2Mp")
    
    kAtmsubinterface=_Type_(134, "kAtmsubinterface", "atmSubInterface")
    
    kInfiniband=_Type_(199, "kInfiniband", "infiniband")
    
    kIso88022llc=_Type_(41, "kIso88022llc", "iso88022llc")
    
    kDocscablemcmtsdownstream=_Type_(229, "kDocscablemcmtsdownstream", "docsCableMCmtsDownstream")
    
    kLinegroup=_Type_(210, "kLinegroup", "linegroup")
    
    kGr303rdt=_Type_(177, "kGr303rdt", "gr303RDT")
    
    kTrasnphdlc=_Type_(123, "kTrasnphdlc", "trasnpHdlc")
    
    kUsb=_Type_(160, "kUsb", "usb")
    
    kTunnel=_Type_(131, "kTunnel", "tunnel")
    
    kHdsl2=_Type_(168, "kHdsl2", "hdsl2")
    
    kSixtofour=_Type_(215, "kSixtofour", "sixToFour")
    
    kMplstunnel=_Type_(150, "kMplstunnel", "mplsTunnel")
    
    kSmdsicip=_Type_(52, "kSmdsicip", "smdsIcip")
    
    kDvbrcstdma=_Type_(241, "kDvbrcstdma", "dvbRcsTdma")
    
    kLapb=_Type_(16, "kLapb", "lapb")
    
    kH323gatekeeper=_Type_(164, "kH323gatekeeper", "h323Gatekeeper")
    
    kActelismetaloop=_Type_(223, "kActelismetaloop", "actelisMetaLOOP")
    
    kFastether=_Type_(62, "kFastether", "fastEther")
    
    kPropwirelessp2p=_Type_(157, "kPropwirelessp2p", "propWirelessP2P")
    
    kPropcnls=_Type_(89, "kPropcnls", "propCnls")
    
    kRadsl=_Type_(95, "kRadsl", "radsl")
    
    kDocscablemaclayer=_Type_(127, "kDocscablemaclayer", "docsCableMaclayer")
    
    kMpc=_Type_(113, "kMpc", "mpc")
    
    kAal2=_Type_(187, "kAal2", "aal2")
    
    kIso88025crfpint=_Type_(98, "kIso88025crfpint", "iso88025CRFPInt")
    
    kVoicefxo=_Type_(101, "kVoicefxo", "voiceFXO")
    
    kVoiceemfgd=_Type_(211, "kVoiceemfgd", "voiceEMFGD")
    
    kHostpad=_Type_(90, "kHostpad", "hostPad")
    
    kDs0=_Type_(81, "kDs0", "ds0")
    
    kG703at2mb=_Type_(67, "kG703at2mb", "g703at2mb")
    
    kArcnetplus=_Type_(36, "kArcnetplus", "arcnetPlus")
    
    kDocscabledownstream=_Type_(128, "kDocscabledownstream", "docsCableDownstream")
    
    kDdnx25=_Type_(4, "kDdnx25", "ddnX25")
    
    kAdsl2plus=_Type_(238, "kAdsl2plus", "adsl2plus")
    
    kVdsl=_Type_(97, "kVdsl", "vdsl")
    
    kMfsiglink=_Type_(167, "kMfsiglink", "mfSigLink")
    
    kSip=_Type_(31, "kSip", "sip")
    
    kTermpad=_Type_(91, "kTermpad", "termPad")
    
    kPropdocswirelessmaclayer=_Type_(180, "kPropdocswirelessmaclayer", "propDocsWirelessMaclayer")
    
    kPon155=_Type_(207, "kPon155", "pon155")
    
    kModem=_Type_(48, "kModem", "modem")
    
    kIeee1394=_Type_(144, "kIeee1394", "ieee1394")
    
    kSonet=_Type_(39, "kSonet", "sonet")
    
    kVoicefgdeana=_Type_(212, "kVoicefgdeana", "voiceFGDEANA")
    
    kFastetherfx=_Type_(69, "kFastetherfx", "fastEtherFX")
    
    kDs3=_Type_(30, "kDs3", "ds3")
    
    kCblvectastar=_Type_(228, "kCblvectastar", "cblVectaStar")
    
    kIeee80216wman=_Type_(237, "kIeee80216wman", "ieee80216WMAN")
    
    kGigabitethernet=_Type_(117, "kGigabitethernet", "gigabitEthernet")
    
    kIso88024tokenbus=_Type_(8, "kIso88024tokenbus", "iso88024TokenBus")
    
    kIdsl=_Type_(154, "kIdsl", "idsl")
    
    kDvbasiin=_Type_(172, "kDvbasiin", "dvbAsiIn")
    
    kL3ipvlan=_Type_(136, "kL3ipvlan", "l3ipvlan")
    
    kIpswitch=_Type_(78, "kIpswitch", "ipSwitch")
    
    kRadiomac=_Type_(188, "kRadiomac", "radioMAC")
    
    kPropdocswirelessupstream=_Type_(182, "kPropdocswirelessupstream", "propDocsWirelessUpstream")
    
    kPlc=_Type_(174, "kPlc", "plc")
    
    kMsdsl=_Type_(143, "kMsdsl", "msdsl")
    
    kArcnet=_Type_(35, "kArcnet", "arcnet")
    
    kMpls=_Type_(166, "kMpls", "mpls")
    
    kOther=_Type_(1, "kOther", "other")
    
    kAviciopticalether=_Type_(233, "kAviciopticalether", "aviciOpticalEther")
    
    kTr008=_Type_(176, "kTr008", "tr008")
    
    kEconet=_Type_(206, "kEconet", "econet")
    
    kMocaversion1=_Type_(236, "kMocaversion1", "mocaVersion1")
    
    kProppointtopointserial=_Type_(22, "kProppointtopointserial", "propPointToPointSerial")
    
    kSonetpath=_Type_(50, "kSonetpath", "sonetPath")
    
    kVoiceoverip=_Type_(104, "kVoiceoverip", "voiceOverIp")
    
    kLapf=_Type_(119, "kLapf", "lapf")
    
    kIp=_Type_(126, "kIp", "ip")
    
    kVirtualtg=_Type_(202, "kVirtualtg", "virtualTg")
    
    kSdlc=_Type_(17, "kSdlc", "sdlc")
    
    kPropmultiplexor=_Type_(54, "kPropmultiplexor", "propMultiplexor")
    
    kOpticalchannel=_Type_(195, "kOpticalchannel", "opticalChannel")
    
    kPrimaryisdn=_Type_(21, "kPrimaryisdn", "primaryISDN")
    
    kAdsl=_Type_(94, "kAdsl", "adsl")
    
    kDvbrccupstream=_Type_(148, "kDvbrccupstream", "dvbRccUpstream")
    
    kRegular1822=_Type_(2, "kRegular1822", "regular1822")
    
    kFrf16mfrbundle=_Type_(163, "kFrf16mfrbundle", "frf16MfrBundle")
    
    kFciplink=_Type_(224, "kFciplink", "fcipLink")
    
    kEplrs=_Type_(87, "kEplrs", "eplrs")
    
    kProteon80mbit=_Type_(13, "kProteon80mbit", "proteon80Mbit")
    
    kAtmvirtual=_Type_(149, "kAtmvirtual", "atmVirtual")
    
    kIpoveratm=_Type_(114, "kIpoveratm", "ipOverAtm")
    
    kAsync=_Type_(84, "kAsync", "async")
    
    kCiscoislvlan=_Type_(222, "kCiscoislvlan", "ciscoISLvlan")
    
    kEthernetcsmacd=_Type_(6, "kEthernetcsmacd", "ethernetCsmacd")
    
    kHdh1822=_Type_(3, "kHdh1822", "hdh1822")
    
    kSonetvt=_Type_(51, "kSonetvt", "sonetVT")
    
    kHippiinterface=_Type_(57, "kHippiinterface", "hippiInterface")
    
    kPdnetherloop2=_Type_(218, "kPdnetherloop2", "pdnEtherLoop2")
    
    kChannel=_Type_(70, "kChannel", "channel")
    
    kA12mppswitch=_Type_(130, "kA12mppswitch", "a12MppSwitch")
    
    kPropdocswirelessdownstream=_Type_(181, "kPropdocswirelessdownstream", "propDocsWirelessDownstream")
    
    kPon622=_Type_(208, "kPon622", "pon622")
    
    kDvbrccdownstream=_Type_(147, "kDvbrccdownstream", "dvbRccDownstream")
    
    kFrforward=_Type_(158, "kFrforward", "frForward")
    
    kRfc1483=_Type_(159, "kRfc1483", "rfc1483")
    
    kAflane8025=_Type_(60, "kAflane8025", "aflane8025")
    
    kL3ipxvlan=_Type_(137, "kL3ipxvlan", "l3ipxvlan")
    
    kEon=_Type_(25, "kEon", "eon")
    
    kIsup=_Type_(179, "kIsup", "isup")
    
    kGr303idt=_Type_(178, "kGr303idt", "gr303IDT")
    
    kWwanpp2=_Type_(244, "kWwanpp2", "wwanPP2")
    
    kGfp=_Type_(221, "kGfp", "gfp")
    
    kIso88025fiber=_Type_(115, "kIso88025fiber", "iso88025Fiber")
    
    kDvbtdm=_Type_(240, "kDvbtdm", "dvbTdm")
    
    kFramerelayinterconnect=_Type_(58, "kFramerelayinterconnect", "frameRelayInterconnect")
    
    kUltra=_Type_(29, "kUltra", "ultra")
    
    kG703at64k=_Type_(66, "kG703at64k", "g703at64k")
    
    kStacktostack=_Type_(111, "kStacktostack", "stackToStack")
    
    kNfas=_Type_(175, "kNfas", "nfas")
    
    kSrp=_Type_(151, "kSrp", "srp")
    
    kPppmultilinkbundle=_Type_(108, "kPppmultilinkbundle", "pppMultilinkBundle")
    
    kAdsl2=_Type_(230, "kAdsl2", "adsl2")
    
    kCompositelink=_Type_(155, "kCompositelink", "compositeLink")
    
    kEthernet3mbit=_Type_(26, "kEthernet3mbit", "ethernet3Mbit")
    
    kSonetoverheadchannel=_Type_(185, "kSonetoverheadchannel", "sonetOverheadChannel")
    
    kIso88023csmacd=_Type_(7, "kIso88023csmacd", "iso88023Csmacd")
    
    kFibrechannel=_Type_(56, "kFibrechannel", "fibreChannel")
    
    kVoiceoveratm=_Type_(152, "kVoiceoveratm", "voiceOverAtm")
    
    kMiox25=_Type_(38, "kMiox25", "miox25")
    
    kOpticaltransport=_Type_(196, "kOpticaltransport", "opticalTransport")
    
    kDocscableupstreamchannel=_Type_(205, "kDocscableupstreamchannel", "docsCableUpstreamChannel")
    
    kVoiceencap=_Type_(103, "kVoiceencap", "voiceEncap")
    
    kQllc=_Type_(68, "kQllc", "qllc")
    
    kHssi=_Type_(46, "kHssi", "hssi")
    
    kFast=_Type_(125, "kFast", "fast")
    
    kEscon=_Type_(73, "kEscon", "escon")
    
    kQam=_Type_(226, "kQam", "qam")
    
    kPara=_Type_(34, "kPara", "para")
    
    kBasicisdn=_Type_(20, "kBasicisdn", "basicISDN")
    
    kIso88025dtr=_Type_(86, "kIso88025dtr", "iso88025Dtr")
    
    kDlsw=_Type_(74, "kDlsw", "dlsw")
    
    kAtmbond=_Type_(234, "kAtmbond", "atmbond")
    
    kHyperchannel=_Type_(14, "kHyperchannel", "hyperchannel")
    
    kIsdn=_Type_(63, "kIsdn", "isdn")
    
    kIso88026man=_Type_(10, "kIso88026man", "iso88026Man")
    
    kH323proxy=_Type_(165, "kH323proxy", "h323Proxy")
    
    kMacseccontrolledif=_Type_(231, "kMacseccontrolledif", "macSecControlledIF")
    
    kDigitalpowerline=_Type_(138, "kDigitalpowerline", "digitalPowerline")
    
    kSmdsdxi=_Type_(43, "kSmdsdxi", "smdsDxi")
    
    kSs7siglink=_Type_(156, "kSs7siglink", "ss7SigLink")
    
    kSoftwareloopback=_Type_(24, "kSoftwareloopback", "softwareLoopback")
    
    kV37=_Type_(120, "kV37", "v37")
    
    kX213=_Type_(93, "kX213", "x213")
    
    kVoicefgdos=_Type_(235, "kVoicefgdos", "voiceFGDOS")
    
    kCnr=_Type_(85, "kCnr", "cnr")
    
    kAtmlogical=_Type_(80, "kAtmlogical", "atmLogical")
    
    kIsdnu=_Type_(76, "kIsdnu", "isdnu")
    
    kX25huntgroup=_Type_(122, "kX25huntgroup", "x25huntGroup")
    
    kFddi=_Type_(15, "kFddi", "fddi")
    
    kMvl=_Type_(191, "kMvl", "mvl")
    
    kTelink=_Type_(200, "kTelink", "teLink")
    
    kWwanpp=_Type_(243, "kWwanpp", "wwanPP")
    
    kAtmima=_Type_(107, "kAtmima", "atmIma")
    
    kFramerelay=_Type_(32, "kFramerelay", "frameRelay")
    
    kImt=_Type_(190, "kImt", "imt")
    
    kAal5=_Type_(49, "kAal5", "aal5")
    
    kIpoverclaw=_Type_(110, "kIpoverclaw", "ipOverClaw")
    
    kIpforward=_Type_(142, "kIpforward", "ipForward")
    
    kAtmvciendpt=_Type_(194, "kAtmvciendpt", "atmVciEndPt")
    
    kFrdlciendpt=_Type_(193, "kFrdlciendpt", "frDlciEndPt")
    
    kAtmfuni=_Type_(106, "kAtmfuni", "atmFuni")
    
    kFramerelayservice=_Type_(44, "kFramerelayservice", "frameRelayService")
    
    kV11=_Type_(64, "kV11", "v11")
    
    kX25mlp=_Type_(121, "kX25mlp", "x25mlp")
    
    kVoiceovercable=_Type_(198, "kVoiceovercable", "voiceOverCable")
    
    kOpticalchannelgroup=_Type_(219, "kOpticalchannelgroup", "opticalChannelGroup")
    
    kDvbrcsmaclayer=_Type_(239, "kDvbrcsmaclayer", "dvbRcsMacLayer")
    
    kLapd=_Type_(77, "kLapd", "lapd")
    
    kSipsig=_Type_(204, "kSipsig", "sipSig")
    
    kFramerelaympi=_Type_(92, "kFramerelaympi", "frameRelayMPI")
    
    kSdsl=_Type_(96, "kSdsl", "sdsl")
    
    kDs1fdl=_Type_(170, "kDs1fdl", "ds1FDL")
    
    kPpp=_Type_(23, "kPpp", "ppp")
    
    kAtm=_Type_(37, "kAtm", "atm")
    
    kGtp=_Type_(216, "kGtp", "gtp")
    
    kHippi=_Type_(47, "kHippi", "hippi")
    
    kDvbasiout=_Type_(173, "kDvbasiout", "dvbAsiOut")
    
    kPropvirtual=_Type_(53, "kPropvirtual", "propVirtual")
    
    kShdsl=_Type_(169, "kShdsl", "shdsl")
    
    kBridge=_Type_(209, "kBridge", "bridge")
    
    kL2vlan=_Type_(135, "kL2vlan", "l2vlan")
    
    kX25ple=_Type_(40, "kX25ple", "x25ple")
    
    kBsc=_Type_(83, "kBsc", "bsc")
    
    kIsdns=_Type_(75, "kIsdns", "isdns")
    
    kMediamailoverip=_Type_(139, "kMediamailoverip", "mediaMailOverIp")
    
    kIbm370parchan=_Type_(72, "kIbm370parchan", "ibm370parChan")
    
    kPos=_Type_(171, "kPos", "pos")
    

    @staticmethod
    def isValidValue (value):
        return Ianaiftype._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return Ianaiftype._Type_.getByValue(value)




"""
Extracted from the below data: 
{
    "conditionalDebugName": null, 
    "enumTypes": [
        {
            "className": "Ianatunneltype", 
            "enums": [
                {
                    "yangName": "l2f", 
                    "displayName": "l2f", 
                    "name": "kL2f", 
                    "value": "7"
                }, 
                {
                    "yangName": "iana_tunnel_type_six_to_four", 
                    "displayName": "sixToFour", 
                    "name": "kSixtofour", 
                    "value": "11"
                }, 
                {
                    "yangName": "minimal", 
                    "displayName": "minimal", 
                    "name": "kMinimal", 
                    "value": "4"
                }, 
                {
                    "yangName": "pptp", 
                    "displayName": "pptp", 
                    "name": "kPptp", 
                    "value": "6"
                }, 
                {
                    "yangName": "udp", 
                    "displayName": "udp", 
                    "name": "kUdp", 
                    "value": "8"
                }, 
                {
                    "yangName": "msdp", 
                    "displayName": "msdp", 
                    "name": "kMsdp", 
                    "value": "10"
                }, 
                {
                    "yangName": "teredo", 
                    "displayName": "teredo", 
                    "name": "kTeredo", 
                    "value": "14"
                }, 
                {
                    "yangName": "l2tp", 
                    "displayName": "l2tp", 
                    "name": "kL2tp", 
                    "value": "5"
                }, 
                {
                    "yangName": "other", 
                    "displayName": "other", 
                    "name": "kOther", 
                    "value": "1"
                }, 
                {
                    "yangName": "isatap", 
                    "displayName": "isatap", 
                    "name": "kIsatap", 
                    "value": "13"
                }, 
                {
                    "yangName": "sixOverFour", 
                    "displayName": "sixOverFour", 
                    "name": "kSixoverfour", 
                    "value": "12"
                }, 
                {
                    "yangName": "atmp", 
                    "displayName": "atmp", 
                    "name": "kAtmp", 
                    "value": "9"
                }, 
                {
                    "yangName": "gre", 
                    "displayName": "gre", 
                    "name": "kGre", 
                    "value": "3"
                }, 
                {
                    "yangName": "direct", 
                    "displayName": "direct", 
                    "name": "kDirect", 
                    "value": "2"
                }
            ], 
            "importStatement": "from a.api.yang.modules.common.iana.iana_if_type_mib.iana_if_type_mib_module_gen import Ianatunneltype"
        }, 
        {
            "className": "Ianaiftype", 
            "enums": [
                {
                    "yangName": "if_gsn", 
                    "displayName": "if-gsn", 
                    "name": "kIfGsn", 
                    "value": "145"
                }, 
                {
                    "yangName": "docsCableUpstream", 
                    "displayName": "docsCableUpstream", 
                    "name": "kDocscableupstream", 
                    "value": "129"
                }, 
                {
                    "yangName": "ipOverCdlc", 
                    "displayName": "ipOverCdlc", 
                    "name": "kIpovercdlc", 
                    "value": "109"
                }, 
                {
                    "yangName": "macSecUncontrolledIF", 
                    "displayName": "macSecUncontrolledIF", 
                    "name": "kMacsecuncontrolledif", 
                    "value": "232"
                }, 
                {
                    "yangName": "ces", 
                    "displayName": "ces", 
                    "name": "kCes", 
                    "value": "133"
                }, 
                {
                    "yangName": "arap", 
                    "displayName": "arap", 
                    "name": "kArap", 
                    "value": "88"
                }, 
                {
                    "yangName": "voiceDID", 
                    "displayName": "voiceDID", 
                    "name": "kVoicedid", 
                    "value": "213"
                }, 
                {
                    "yangName": "e1", 
                    "displayName": "e1", 
                    "name": "kE1", 
                    "value": "19"
                }, 
                {
                    "yangName": "rpr", 
                    "displayName": "rpr", 
                    "name": "kRpr", 
                    "value": "225"
                }, 
                {
                    "yangName": "rfc877x25", 
                    "displayName": "rfc877x25", 
                    "name": "kRfc877x25", 
                    "value": "5"
                }, 
                {
                    "yangName": "dtm", 
                    "displayName": "dtm", 
                    "name": "kDtm", 
                    "value": "140"
                }, 
                {
                    "yangName": "interleave", 
                    "displayName": "interleave", 
                    "name": "kInterleave", 
                    "value": "124"
                }, 
                {
                    "yangName": "iso88025TokenRing", 
                    "displayName": "iso88025TokenRing", 
                    "name": "kIso88025tokenring", 
                    "value": "9"
                }, 
                {
                    "yangName": "ds1", 
                    "displayName": "ds1", 
                    "name": "kDs1", 
                    "value": "18"
                }, 
                {
                    "yangName": "x86Laps", 
                    "displayName": "x86Laps", 
                    "name": "kX86laps", 
                    "value": "242"
                }, 
                {
                    "yangName": "starLan", 
                    "displayName": "starLan", 
                    "name": "kStarlan", 
                    "value": "11"
                }, 
                {
                    "yangName": "atmDxi", 
                    "displayName": "atmDxi", 
                    "name": "kAtmdxi", 
                    "value": "105"
                }, 
                {
                    "yangName": "localTalk", 
                    "displayName": "localTalk", 
                    "name": "kLocaltalk", 
                    "value": "42"
                }, 
                {
                    "yangName": "voiceOverFrameRelay", 
                    "displayName": "voiceOverFrameRelay", 
                    "name": "kVoiceoverframerelay", 
                    "value": "153"
                }, 
                {
                    "yangName": "cctEmul", 
                    "displayName": "cctEmul", 
                    "name": "kCctemul", 
                    "value": "61"
                }, 
                {
                    "yangName": "digitalWrapperOverheadChannel", 
                    "displayName": "digitalWrapperOverheadChannel", 
                    "name": "kDigitalwrapperoverheadchannel", 
                    "value": "186"
                }, 
                {
                    "yangName": "q2931", 
                    "displayName": "q2931", 
                    "name": "kQ2931", 
                    "value": "201"
                }, 
                {
                    "yangName": "homepna", 
                    "displayName": "homepna", 
                    "name": "kHomepna", 
                    "value": "220"
                }, 
                {
                    "yangName": "dvbRccMacLayer", 
                    "displayName": "dvbRccMacLayer", 
                    "name": "kDvbrccmaclayer", 
                    "value": "146"
                }, 
                {
                    "yangName": "hiperlan2", 
                    "displayName": "hiperlan2", 
                    "name": "kHiperlan2", 
                    "value": "183"
                }, 
                {
                    "yangName": "rs232", 
                    "displayName": "rs232", 
                    "name": "kRs232", 
                    "value": "33"
                }, 
                {
                    "yangName": "ieee80212", 
                    "displayName": "ieee80212", 
                    "name": "kIeee80212", 
                    "value": "55"
                }, 
                {
                    "yangName": "hdlc", 
                    "displayName": "hdlc", 
                    "name": "kHdlc", 
                    "value": "118"
                }, 
                {
                    "yangName": "ieee80211", 
                    "displayName": "ieee80211", 
                    "name": "kIeee80211", 
                    "value": "71"
                }, 
                {
                    "yangName": "ds0Bundle", 
                    "displayName": "ds0Bundle", 
                    "name": "kDs0bundle", 
                    "value": "82"
                }, 
                {
                    "yangName": "coffee", 
                    "displayName": "coffee", 
                    "name": "kCoffee", 
                    "value": "132"
                }, 
                {
                    "yangName": "v36", 
                    "displayName": "v36", 
                    "name": "kV36", 
                    "value": "65"
                }, 
                {
                    "yangName": "mpegTransport", 
                    "displayName": "mpegTransport", 
                    "name": "kMpegtransport", 
                    "value": "214"
                }, 
                {
                    "yangName": "rsrb", 
                    "displayName": "rsrb", 
                    "name": "kRsrb", 
                    "value": "79"
                }, 
                {
                    "yangName": "reachDSL", 
                    "displayName": "reachDSL", 
                    "name": "kReachdsl", 
                    "value": "192"
                }, 
                {
                    "yangName": "virtualIpAddress", 
                    "displayName": "virtualIpAddress", 
                    "name": "kVirtualipaddress", 
                    "value": "112"
                }, 
                {
                    "yangName": "bgppolicyaccounting", 
                    "displayName": "bgppolicyaccounting", 
                    "name": "kBgppolicyaccounting", 
                    "value": "162"
                }, 
                {
                    "yangName": "dcn", 
                    "displayName": "dcn", 
                    "name": "kDcn", 
                    "value": "141"
                }, 
                {
                    "yangName": "atmRadio", 
                    "displayName": "atmRadio", 
                    "name": "kAtmradio", 
                    "value": "189"
                }, 
                {
                    "yangName": "propAtm", 
                    "displayName": "propAtm", 
                    "name": "kPropatm", 
                    "value": "197"
                }, 
                {
                    "yangName": "nsip", 
                    "displayName": "nsip", 
                    "name": "kNsip", 
                    "value": "27"
                }, 
                {
                    "yangName": "lmp", 
                    "displayName": "lmp", 
                    "name": "kLmp", 
                    "value": "227"
                }, 
                {
                    "yangName": "proteon10Mbit", 
                    "displayName": "proteon10Mbit", 
                    "name": "kProteon10mbit", 
                    "value": "12"
                }, 
                {
                    "yangName": "tdlc", 
                    "displayName": "tdlc", 
                    "name": "kTdlc", 
                    "value": "116"
                }, 
                {
                    "yangName": "sipTg", 
                    "displayName": "sipTg", 
                    "name": "kSiptg", 
                    "value": "203"
                }, 
                {
                    "yangName": "v35", 
                    "displayName": "v35", 
                    "name": "kV35", 
                    "value": "45"
                }, 
                {
                    "yangName": "pdnEtherLoop1", 
                    "displayName": "pdnEtherLoop1", 
                    "name": "kPdnetherloop1", 
                    "value": "217"
                }, 
                {
                    "yangName": "voiceFXS", 
                    "displayName": "voiceFXS", 
                    "name": "kVoicefxs", 
                    "value": "102"
                }, 
                {
                    "yangName": "myrinet", 
                    "displayName": "myrinet", 
                    "name": "kMyrinet", 
                    "value": "99"
                }, 
                {
                    "yangName": "aflane8023", 
                    "displayName": "aflane8023", 
                    "name": "kAflane8023", 
                    "value": "59"
                }, 
                {
                    "yangName": "slip", 
                    "displayName": "slip", 
                    "name": "kSlip", 
                    "value": "28"
                }, 
                {
                    "yangName": "ieee8023adLag", 
                    "displayName": "ieee8023adLag", 
                    "name": "kIeee8023adlag", 
                    "value": "161"
                }, 
                {
                    "yangName": "voiceEM", 
                    "displayName": "voiceEM", 
                    "name": "kVoiceem", 
                    "value": "100"
                }, 
                {
                    "yangName": "propBWAp2Mp", 
                    "displayName": "propBWAp2Mp", 
                    "name": "kPropbwap2mp", 
                    "value": "184"
                }, 
                {
                    "yangName": "atmSubInterface", 
                    "displayName": "atmSubInterface", 
                    "name": "kAtmsubinterface", 
                    "value": "134"
                }, 
                {
                    "yangName": "infiniband", 
                    "displayName": "infiniband", 
                    "name": "kInfiniband", 
                    "value": "199"
                }, 
                {
                    "yangName": "iso88022llc", 
                    "displayName": "iso88022llc", 
                    "name": "kIso88022llc", 
                    "value": "41"
                }, 
                {
                    "yangName": "docsCableMCmtsDownstream", 
                    "displayName": "docsCableMCmtsDownstream", 
                    "name": "kDocscablemcmtsdownstream", 
                    "value": "229"
                }, 
                {
                    "yangName": "linegroup", 
                    "displayName": "linegroup", 
                    "name": "kLinegroup", 
                    "value": "210"
                }, 
                {
                    "yangName": "gr303RDT", 
                    "displayName": "gr303RDT", 
                    "name": "kGr303rdt", 
                    "value": "177"
                }, 
                {
                    "yangName": "trasnpHdlc", 
                    "displayName": "trasnpHdlc", 
                    "name": "kTrasnphdlc", 
                    "value": "123"
                }, 
                {
                    "yangName": "usb", 
                    "displayName": "usb", 
                    "name": "kUsb", 
                    "value": "160"
                }, 
                {
                    "yangName": "tunnel", 
                    "displayName": "tunnel", 
                    "name": "kTunnel", 
                    "value": "131"
                }, 
                {
                    "yangName": "hdsl2", 
                    "displayName": "hdsl2", 
                    "name": "kHdsl2", 
                    "value": "168"
                }, 
                {
                    "yangName": "sixToFour", 
                    "displayName": "sixToFour", 
                    "name": "kSixtofour", 
                    "value": "215"
                }, 
                {
                    "yangName": "mplsTunnel", 
                    "displayName": "mplsTunnel", 
                    "name": "kMplstunnel", 
                    "value": "150"
                }, 
                {
                    "yangName": "smdsIcip", 
                    "displayName": "smdsIcip", 
                    "name": "kSmdsicip", 
                    "value": "52"
                }, 
                {
                    "yangName": "dvbRcsTdma", 
                    "displayName": "dvbRcsTdma", 
                    "name": "kDvbrcstdma", 
                    "value": "241"
                }, 
                {
                    "yangName": "lapb", 
                    "displayName": "lapb", 
                    "name": "kLapb", 
                    "value": "16"
                }, 
                {
                    "yangName": "h323Gatekeeper", 
                    "displayName": "h323Gatekeeper", 
                    "name": "kH323gatekeeper", 
                    "value": "164"
                }, 
                {
                    "yangName": "actelisMetaLOOP", 
                    "displayName": "actelisMetaLOOP", 
                    "name": "kActelismetaloop", 
                    "value": "223"
                }, 
                {
                    "yangName": "fastEther", 
                    "displayName": "fastEther", 
                    "name": "kFastether", 
                    "value": "62"
                }, 
                {
                    "yangName": "propWirelessP2P", 
                    "displayName": "propWirelessP2P", 
                    "name": "kPropwirelessp2p", 
                    "value": "157"
                }, 
                {
                    "yangName": "propCnls", 
                    "displayName": "propCnls", 
                    "name": "kPropcnls", 
                    "value": "89"
                }, 
                {
                    "yangName": "radsl", 
                    "displayName": "radsl", 
                    "name": "kRadsl", 
                    "value": "95"
                }, 
                {
                    "yangName": "docsCableMaclayer", 
                    "displayName": "docsCableMaclayer", 
                    "name": "kDocscablemaclayer", 
                    "value": "127"
                }, 
                {
                    "yangName": "mpc", 
                    "displayName": "mpc", 
                    "name": "kMpc", 
                    "value": "113"
                }, 
                {
                    "yangName": "aal2", 
                    "displayName": "aal2", 
                    "name": "kAal2", 
                    "value": "187"
                }, 
                {
                    "yangName": "iso88025CRFPInt", 
                    "displayName": "iso88025CRFPInt", 
                    "name": "kIso88025crfpint", 
                    "value": "98"
                }, 
                {
                    "yangName": "voiceFXO", 
                    "displayName": "voiceFXO", 
                    "name": "kVoicefxo", 
                    "value": "101"
                }, 
                {
                    "yangName": "voiceEMFGD", 
                    "displayName": "voiceEMFGD", 
                    "name": "kVoiceemfgd", 
                    "value": "211"
                }, 
                {
                    "yangName": "hostPad", 
                    "displayName": "hostPad", 
                    "name": "kHostpad", 
                    "value": "90"
                }, 
                {
                    "yangName": "ds0", 
                    "displayName": "ds0", 
                    "name": "kDs0", 
                    "value": "81"
                }, 
                {
                    "yangName": "g703at2mb", 
                    "displayName": "g703at2mb", 
                    "name": "kG703at2mb", 
                    "value": "67"
                }, 
                {
                    "yangName": "arcnetPlus", 
                    "displayName": "arcnetPlus", 
                    "name": "kArcnetplus", 
                    "value": "36"
                }, 
                {
                    "yangName": "docsCableDownstream", 
                    "displayName": "docsCableDownstream", 
                    "name": "kDocscabledownstream", 
                    "value": "128"
                }, 
                {
                    "yangName": "ddnX25", 
                    "displayName": "ddnX25", 
                    "name": "kDdnx25", 
                    "value": "4"
                }, 
                {
                    "yangName": "adsl2plus", 
                    "displayName": "adsl2plus", 
                    "name": "kAdsl2plus", 
                    "value": "238"
                }, 
                {
                    "yangName": "vdsl", 
                    "displayName": "vdsl", 
                    "name": "kVdsl", 
                    "value": "97"
                }, 
                {
                    "yangName": "mfSigLink", 
                    "displayName": "mfSigLink", 
                    "name": "kMfsiglink", 
                    "value": "167"
                }, 
                {
                    "yangName": "sip", 
                    "displayName": "sip", 
                    "name": "kSip", 
                    "value": "31"
                }, 
                {
                    "yangName": "termPad", 
                    "displayName": "termPad", 
                    "name": "kTermpad", 
                    "value": "91"
                }, 
                {
                    "yangName": "propDocsWirelessMaclayer", 
                    "displayName": "propDocsWirelessMaclayer", 
                    "name": "kPropdocswirelessmaclayer", 
                    "value": "180"
                }, 
                {
                    "yangName": "pon155", 
                    "displayName": "pon155", 
                    "name": "kPon155", 
                    "value": "207"
                }, 
                {
                    "yangName": "modem", 
                    "displayName": "modem", 
                    "name": "kModem", 
                    "value": "48"
                }, 
                {
                    "yangName": "ieee1394", 
                    "displayName": "ieee1394", 
                    "name": "kIeee1394", 
                    "value": "144"
                }, 
                {
                    "yangName": "sonet", 
                    "displayName": "sonet", 
                    "name": "kSonet", 
                    "value": "39"
                }, 
                {
                    "yangName": "voiceFGDEANA", 
                    "displayName": "voiceFGDEANA", 
                    "name": "kVoicefgdeana", 
                    "value": "212"
                }, 
                {
                    "yangName": "fastEtherFX", 
                    "displayName": "fastEtherFX", 
                    "name": "kFastetherfx", 
                    "value": "69"
                }, 
                {
                    "yangName": "ds3", 
                    "displayName": "ds3", 
                    "name": "kDs3", 
                    "value": "30"
                }, 
                {
                    "yangName": "cblVectaStar", 
                    "displayName": "cblVectaStar", 
                    "name": "kCblvectastar", 
                    "value": "228"
                }, 
                {
                    "yangName": "ieee80216WMAN", 
                    "displayName": "ieee80216WMAN", 
                    "name": "kIeee80216wman", 
                    "value": "237"
                }, 
                {
                    "yangName": "gigabitEthernet", 
                    "displayName": "gigabitEthernet", 
                    "name": "kGigabitethernet", 
                    "value": "117"
                }, 
                {
                    "yangName": "iso88024TokenBus", 
                    "displayName": "iso88024TokenBus", 
                    "name": "kIso88024tokenbus", 
                    "value": "8"
                }, 
                {
                    "yangName": "idsl", 
                    "displayName": "idsl", 
                    "name": "kIdsl", 
                    "value": "154"
                }, 
                {
                    "yangName": "dvbAsiIn", 
                    "displayName": "dvbAsiIn", 
                    "name": "kDvbasiin", 
                    "value": "172"
                }, 
                {
                    "yangName": "l3ipvlan", 
                    "displayName": "l3ipvlan", 
                    "name": "kL3ipvlan", 
                    "value": "136"
                }, 
                {
                    "yangName": "ipSwitch", 
                    "displayName": "ipSwitch", 
                    "name": "kIpswitch", 
                    "value": "78"
                }, 
                {
                    "yangName": "radioMAC", 
                    "displayName": "radioMAC", 
                    "name": "kRadiomac", 
                    "value": "188"
                }, 
                {
                    "yangName": "propDocsWirelessUpstream", 
                    "displayName": "propDocsWirelessUpstream", 
                    "name": "kPropdocswirelessupstream", 
                    "value": "182"
                }, 
                {
                    "yangName": "plc", 
                    "displayName": "plc", 
                    "name": "kPlc", 
                    "value": "174"
                }, 
                {
                    "yangName": "msdsl", 
                    "displayName": "msdsl", 
                    "name": "kMsdsl", 
                    "value": "143"
                }, 
                {
                    "yangName": "arcnet", 
                    "displayName": "arcnet", 
                    "name": "kArcnet", 
                    "value": "35"
                }, 
                {
                    "yangName": "mpls", 
                    "displayName": "mpls", 
                    "name": "kMpls", 
                    "value": "166"
                }, 
                {
                    "yangName": "other", 
                    "displayName": "other", 
                    "name": "kOther", 
                    "value": "1"
                }, 
                {
                    "yangName": "aviciOpticalEther", 
                    "displayName": "aviciOpticalEther", 
                    "name": "kAviciopticalether", 
                    "value": "233"
                }, 
                {
                    "yangName": "tr008", 
                    "displayName": "tr008", 
                    "name": "kTr008", 
                    "value": "176"
                }, 
                {
                    "yangName": "econet", 
                    "displayName": "econet", 
                    "name": "kEconet", 
                    "value": "206"
                }, 
                {
                    "yangName": "mocaVersion1", 
                    "displayName": "mocaVersion1", 
                    "name": "kMocaversion1", 
                    "value": "236"
                }, 
                {
                    "yangName": "propPointToPointSerial", 
                    "displayName": "propPointToPointSerial", 
                    "name": "kProppointtopointserial", 
                    "value": "22"
                }, 
                {
                    "yangName": "sonetPath", 
                    "displayName": "sonetPath", 
                    "name": "kSonetpath", 
                    "value": "50"
                }, 
                {
                    "yangName": "voiceOverIp", 
                    "displayName": "voiceOverIp", 
                    "name": "kVoiceoverip", 
                    "value": "104"
                }, 
                {
                    "yangName": "lapf", 
                    "displayName": "lapf", 
                    "name": "kLapf", 
                    "value": "119"
                }, 
                {
                    "yangName": "ip", 
                    "displayName": "ip", 
                    "name": "kIp", 
                    "value": "126"
                }, 
                {
                    "yangName": "virtualTg", 
                    "displayName": "virtualTg", 
                    "name": "kVirtualtg", 
                    "value": "202"
                }, 
                {
                    "yangName": "sdlc", 
                    "displayName": "sdlc", 
                    "name": "kSdlc", 
                    "value": "17"
                }, 
                {
                    "yangName": "propMultiplexor", 
                    "displayName": "propMultiplexor", 
                    "name": "kPropmultiplexor", 
                    "value": "54"
                }, 
                {
                    "yangName": "opticalChannel", 
                    "displayName": "opticalChannel", 
                    "name": "kOpticalchannel", 
                    "value": "195"
                }, 
                {
                    "yangName": "primaryISDN", 
                    "displayName": "primaryISDN", 
                    "name": "kPrimaryisdn", 
                    "value": "21"
                }, 
                {
                    "yangName": "adsl", 
                    "displayName": "adsl", 
                    "name": "kAdsl", 
                    "value": "94"
                }, 
                {
                    "yangName": "dvbRccUpstream", 
                    "displayName": "dvbRccUpstream", 
                    "name": "kDvbrccupstream", 
                    "value": "148"
                }, 
                {
                    "yangName": "regular1822", 
                    "displayName": "regular1822", 
                    "name": "kRegular1822", 
                    "value": "2"
                }, 
                {
                    "yangName": "frf16MfrBundle", 
                    "displayName": "frf16MfrBundle", 
                    "name": "kFrf16mfrbundle", 
                    "value": "163"
                }, 
                {
                    "yangName": "fcipLink", 
                    "displayName": "fcipLink", 
                    "name": "kFciplink", 
                    "value": "224"
                }, 
                {
                    "yangName": "eplrs", 
                    "displayName": "eplrs", 
                    "name": "kEplrs", 
                    "value": "87"
                }, 
                {
                    "yangName": "proteon80Mbit", 
                    "displayName": "proteon80Mbit", 
                    "name": "kProteon80mbit", 
                    "value": "13"
                }, 
                {
                    "yangName": "atmVirtual", 
                    "displayName": "atmVirtual", 
                    "name": "kAtmvirtual", 
                    "value": "149"
                }, 
                {
                    "yangName": "ipOverAtm", 
                    "displayName": "ipOverAtm", 
                    "name": "kIpoveratm", 
                    "value": "114"
                }, 
                {
                    "yangName": "async", 
                    "displayName": "async", 
                    "name": "kAsync", 
                    "value": "84"
                }, 
                {
                    "yangName": "ciscoISLvlan", 
                    "displayName": "ciscoISLvlan", 
                    "name": "kCiscoislvlan", 
                    "value": "222"
                }, 
                {
                    "yangName": "ethernetCsmacd", 
                    "displayName": "ethernetCsmacd", 
                    "name": "kEthernetcsmacd", 
                    "value": "6"
                }, 
                {
                    "yangName": "hdh1822", 
                    "displayName": "hdh1822", 
                    "name": "kHdh1822", 
                    "value": "3"
                }, 
                {
                    "yangName": "sonetVT", 
                    "displayName": "sonetVT", 
                    "name": "kSonetvt", 
                    "value": "51"
                }, 
                {
                    "yangName": "hippiInterface", 
                    "displayName": "hippiInterface", 
                    "name": "kHippiinterface", 
                    "value": "57"
                }, 
                {
                    "yangName": "pdnEtherLoop2", 
                    "displayName": "pdnEtherLoop2", 
                    "name": "kPdnetherloop2", 
                    "value": "218"
                }, 
                {
                    "yangName": "channel", 
                    "displayName": "channel", 
                    "name": "kChannel", 
                    "value": "70"
                }, 
                {
                    "yangName": "a12MppSwitch", 
                    "displayName": "a12MppSwitch", 
                    "name": "kA12mppswitch", 
                    "value": "130"
                }, 
                {
                    "yangName": "propDocsWirelessDownstream", 
                    "displayName": "propDocsWirelessDownstream", 
                    "name": "kPropdocswirelessdownstream", 
                    "value": "181"
                }, 
                {
                    "yangName": "pon622", 
                    "displayName": "pon622", 
                    "name": "kPon622", 
                    "value": "208"
                }, 
                {
                    "yangName": "dvbRccDownstream", 
                    "displayName": "dvbRccDownstream", 
                    "name": "kDvbrccdownstream", 
                    "value": "147"
                }, 
                {
                    "yangName": "frForward", 
                    "displayName": "frForward", 
                    "name": "kFrforward", 
                    "value": "158"
                }, 
                {
                    "yangName": "rfc1483", 
                    "displayName": "rfc1483", 
                    "name": "kRfc1483", 
                    "value": "159"
                }, 
                {
                    "yangName": "aflane8025", 
                    "displayName": "aflane8025", 
                    "name": "kAflane8025", 
                    "value": "60"
                }, 
                {
                    "yangName": "l3ipxvlan", 
                    "displayName": "l3ipxvlan", 
                    "name": "kL3ipxvlan", 
                    "value": "137"
                }, 
                {
                    "yangName": "eon", 
                    "displayName": "eon", 
                    "name": "kEon", 
                    "value": "25"
                }, 
                {
                    "yangName": "isup", 
                    "displayName": "isup", 
                    "name": "kIsup", 
                    "value": "179"
                }, 
                {
                    "yangName": "gr303IDT", 
                    "displayName": "gr303IDT", 
                    "name": "kGr303idt", 
                    "value": "178"
                }, 
                {
                    "yangName": "wwanPP2", 
                    "displayName": "wwanPP2", 
                    "name": "kWwanpp2", 
                    "value": "244"
                }, 
                {
                    "yangName": "gfp", 
                    "displayName": "gfp", 
                    "name": "kGfp", 
                    "value": "221"
                }, 
                {
                    "yangName": "iso88025Fiber", 
                    "displayName": "iso88025Fiber", 
                    "name": "kIso88025fiber", 
                    "value": "115"
                }, 
                {
                    "yangName": "dvbTdm", 
                    "displayName": "dvbTdm", 
                    "name": "kDvbtdm", 
                    "value": "240"
                }, 
                {
                    "yangName": "frameRelayInterconnect", 
                    "displayName": "frameRelayInterconnect", 
                    "name": "kFramerelayinterconnect", 
                    "value": "58"
                }, 
                {
                    "yangName": "ultra", 
                    "displayName": "ultra", 
                    "name": "kUltra", 
                    "value": "29"
                }, 
                {
                    "yangName": "g703at64k", 
                    "displayName": "g703at64k", 
                    "name": "kG703at64k", 
                    "value": "66"
                }, 
                {
                    "yangName": "stackToStack", 
                    "displayName": "stackToStack", 
                    "name": "kStacktostack", 
                    "value": "111"
                }, 
                {
                    "yangName": "nfas", 
                    "displayName": "nfas", 
                    "name": "kNfas", 
                    "value": "175"
                }, 
                {
                    "yangName": "srp", 
                    "displayName": "srp", 
                    "name": "kSrp", 
                    "value": "151"
                }, 
                {
                    "yangName": "pppMultilinkBundle", 
                    "displayName": "pppMultilinkBundle", 
                    "name": "kPppmultilinkbundle", 
                    "value": "108"
                }, 
                {
                    "yangName": "adsl2", 
                    "displayName": "adsl2", 
                    "name": "kAdsl2", 
                    "value": "230"
                }, 
                {
                    "yangName": "compositeLink", 
                    "displayName": "compositeLink", 
                    "name": "kCompositelink", 
                    "value": "155"
                }, 
                {
                    "yangName": "ethernet3Mbit", 
                    "displayName": "ethernet3Mbit", 
                    "name": "kEthernet3mbit", 
                    "value": "26"
                }, 
                {
                    "yangName": "sonetOverheadChannel", 
                    "displayName": "sonetOverheadChannel", 
                    "name": "kSonetoverheadchannel", 
                    "value": "185"
                }, 
                {
                    "yangName": "iso88023Csmacd", 
                    "displayName": "iso88023Csmacd", 
                    "name": "kIso88023csmacd", 
                    "value": "7"
                }, 
                {
                    "yangName": "fibreChannel", 
                    "displayName": "fibreChannel", 
                    "name": "kFibrechannel", 
                    "value": "56"
                }, 
                {
                    "yangName": "voiceOverAtm", 
                    "displayName": "voiceOverAtm", 
                    "name": "kVoiceoveratm", 
                    "value": "152"
                }, 
                {
                    "yangName": "miox25", 
                    "displayName": "miox25", 
                    "name": "kMiox25", 
                    "value": "38"
                }, 
                {
                    "yangName": "opticalTransport", 
                    "displayName": "opticalTransport", 
                    "name": "kOpticaltransport", 
                    "value": "196"
                }, 
                {
                    "yangName": "docsCableUpstreamChannel", 
                    "displayName": "docsCableUpstreamChannel", 
                    "name": "kDocscableupstreamchannel", 
                    "value": "205"
                }, 
                {
                    "yangName": "voiceEncap", 
                    "displayName": "voiceEncap", 
                    "name": "kVoiceencap", 
                    "value": "103"
                }, 
                {
                    "yangName": "qllc", 
                    "displayName": "qllc", 
                    "name": "kQllc", 
                    "value": "68"
                }, 
                {
                    "yangName": "hssi", 
                    "displayName": "hssi", 
                    "name": "kHssi", 
                    "value": "46"
                }, 
                {
                    "yangName": "fast", 
                    "displayName": "fast", 
                    "name": "kFast", 
                    "value": "125"
                }, 
                {
                    "yangName": "escon", 
                    "displayName": "escon", 
                    "name": "kEscon", 
                    "value": "73"
                }, 
                {
                    "yangName": "qam", 
                    "displayName": "qam", 
                    "name": "kQam", 
                    "value": "226"
                }, 
                {
                    "yangName": "para", 
                    "displayName": "para", 
                    "name": "kPara", 
                    "value": "34"
                }, 
                {
                    "yangName": "basicISDN", 
                    "displayName": "basicISDN", 
                    "name": "kBasicisdn", 
                    "value": "20"
                }, 
                {
                    "yangName": "iso88025Dtr", 
                    "displayName": "iso88025Dtr", 
                    "name": "kIso88025dtr", 
                    "value": "86"
                }, 
                {
                    "yangName": "dlsw", 
                    "displayName": "dlsw", 
                    "name": "kDlsw", 
                    "value": "74"
                }, 
                {
                    "yangName": "atmbond", 
                    "displayName": "atmbond", 
                    "name": "kAtmbond", 
                    "value": "234"
                }, 
                {
                    "yangName": "hyperchannel", 
                    "displayName": "hyperchannel", 
                    "name": "kHyperchannel", 
                    "value": "14"
                }, 
                {
                    "yangName": "isdn", 
                    "displayName": "isdn", 
                    "name": "kIsdn", 
                    "value": "63"
                }, 
                {
                    "yangName": "iso88026Man", 
                    "displayName": "iso88026Man", 
                    "name": "kIso88026man", 
                    "value": "10"
                }, 
                {
                    "yangName": "h323Proxy", 
                    "displayName": "h323Proxy", 
                    "name": "kH323proxy", 
                    "value": "165"
                }, 
                {
                    "yangName": "macSecControlledIF", 
                    "displayName": "macSecControlledIF", 
                    "name": "kMacseccontrolledif", 
                    "value": "231"
                }, 
                {
                    "yangName": "digitalPowerline", 
                    "displayName": "digitalPowerline", 
                    "name": "kDigitalpowerline", 
                    "value": "138"
                }, 
                {
                    "yangName": "smdsDxi", 
                    "displayName": "smdsDxi", 
                    "name": "kSmdsdxi", 
                    "value": "43"
                }, 
                {
                    "yangName": "ss7SigLink", 
                    "displayName": "ss7SigLink", 
                    "name": "kSs7siglink", 
                    "value": "156"
                }, 
                {
                    "yangName": "softwareLoopback", 
                    "displayName": "softwareLoopback", 
                    "name": "kSoftwareloopback", 
                    "value": "24"
                }, 
                {
                    "yangName": "v37", 
                    "displayName": "v37", 
                    "name": "kV37", 
                    "value": "120"
                }, 
                {
                    "yangName": "x213", 
                    "displayName": "x213", 
                    "name": "kX213", 
                    "value": "93"
                }, 
                {
                    "yangName": "voiceFGDOS", 
                    "displayName": "voiceFGDOS", 
                    "name": "kVoicefgdos", 
                    "value": "235"
                }, 
                {
                    "yangName": "cnr", 
                    "displayName": "cnr", 
                    "name": "kCnr", 
                    "value": "85"
                }, 
                {
                    "yangName": "atmLogical", 
                    "displayName": "atmLogical", 
                    "name": "kAtmlogical", 
                    "value": "80"
                }, 
                {
                    "yangName": "isdnu", 
                    "displayName": "isdnu", 
                    "name": "kIsdnu", 
                    "value": "76"
                }, 
                {
                    "yangName": "x25huntGroup", 
                    "displayName": "x25huntGroup", 
                    "name": "kX25huntgroup", 
                    "value": "122"
                }, 
                {
                    "yangName": "fddi", 
                    "displayName": "fddi", 
                    "name": "kFddi", 
                    "value": "15"
                }, 
                {
                    "yangName": "mvl", 
                    "displayName": "mvl", 
                    "name": "kMvl", 
                    "value": "191"
                }, 
                {
                    "yangName": "teLink", 
                    "displayName": "teLink", 
                    "name": "kTelink", 
                    "value": "200"
                }, 
                {
                    "yangName": "wwanPP", 
                    "displayName": "wwanPP", 
                    "name": "kWwanpp", 
                    "value": "243"
                }, 
                {
                    "yangName": "atmIma", 
                    "displayName": "atmIma", 
                    "name": "kAtmima", 
                    "value": "107"
                }, 
                {
                    "yangName": "frameRelay", 
                    "displayName": "frameRelay", 
                    "name": "kFramerelay", 
                    "value": "32"
                }, 
                {
                    "yangName": "imt", 
                    "displayName": "imt", 
                    "name": "kImt", 
                    "value": "190"
                }, 
                {
                    "yangName": "aal5", 
                    "displayName": "aal5", 
                    "name": "kAal5", 
                    "value": "49"
                }, 
                {
                    "yangName": "ipOverClaw", 
                    "displayName": "ipOverClaw", 
                    "name": "kIpoverclaw", 
                    "value": "110"
                }, 
                {
                    "yangName": "ipForward", 
                    "displayName": "ipForward", 
                    "name": "kIpforward", 
                    "value": "142"
                }, 
                {
                    "yangName": "atmVciEndPt", 
                    "displayName": "atmVciEndPt", 
                    "name": "kAtmvciendpt", 
                    "value": "194"
                }, 
                {
                    "yangName": "frDlciEndPt", 
                    "displayName": "frDlciEndPt", 
                    "name": "kFrdlciendpt", 
                    "value": "193"
                }, 
                {
                    "yangName": "atmFuni", 
                    "displayName": "atmFuni", 
                    "name": "kAtmfuni", 
                    "value": "106"
                }, 
                {
                    "yangName": "frameRelayService", 
                    "displayName": "frameRelayService", 
                    "name": "kFramerelayservice", 
                    "value": "44"
                }, 
                {
                    "yangName": "v11", 
                    "displayName": "v11", 
                    "name": "kV11", 
                    "value": "64"
                }, 
                {
                    "yangName": "x25mlp", 
                    "displayName": "x25mlp", 
                    "name": "kX25mlp", 
                    "value": "121"
                }, 
                {
                    "yangName": "voiceOverCable", 
                    "displayName": "voiceOverCable", 
                    "name": "kVoiceovercable", 
                    "value": "198"
                }, 
                {
                    "yangName": "opticalChannelGroup", 
                    "displayName": "opticalChannelGroup", 
                    "name": "kOpticalchannelgroup", 
                    "value": "219"
                }, 
                {
                    "yangName": "dvbRcsMacLayer", 
                    "displayName": "dvbRcsMacLayer", 
                    "name": "kDvbrcsmaclayer", 
                    "value": "239"
                }, 
                {
                    "yangName": "lapd", 
                    "displayName": "lapd", 
                    "name": "kLapd", 
                    "value": "77"
                }, 
                {
                    "yangName": "sipSig", 
                    "displayName": "sipSig", 
                    "name": "kSipsig", 
                    "value": "204"
                }, 
                {
                    "yangName": "frameRelayMPI", 
                    "displayName": "frameRelayMPI", 
                    "name": "kFramerelaympi", 
                    "value": "92"
                }, 
                {
                    "yangName": "sdsl", 
                    "displayName": "sdsl", 
                    "name": "kSdsl", 
                    "value": "96"
                }, 
                {
                    "yangName": "ds1FDL", 
                    "displayName": "ds1FDL", 
                    "name": "kDs1fdl", 
                    "value": "170"
                }, 
                {
                    "yangName": "ppp", 
                    "displayName": "ppp", 
                    "name": "kPpp", 
                    "value": "23"
                }, 
                {
                    "yangName": "atm", 
                    "displayName": "atm", 
                    "name": "kAtm", 
                    "value": "37"
                }, 
                {
                    "yangName": "gtp", 
                    "displayName": "gtp", 
                    "name": "kGtp", 
                    "value": "216"
                }, 
                {
                    "yangName": "hippi", 
                    "displayName": "hippi", 
                    "name": "kHippi", 
                    "value": "47"
                }, 
                {
                    "yangName": "dvbAsiOut", 
                    "displayName": "dvbAsiOut", 
                    "name": "kDvbasiout", 
                    "value": "173"
                }, 
                {
                    "yangName": "propVirtual", 
                    "displayName": "propVirtual", 
                    "name": "kPropvirtual", 
                    "value": "53"
                }, 
                {
                    "yangName": "shdsl", 
                    "displayName": "shdsl", 
                    "name": "kShdsl", 
                    "value": "169"
                }, 
                {
                    "yangName": "bridge", 
                    "displayName": "bridge", 
                    "name": "kBridge", 
                    "value": "209"
                }, 
                {
                    "yangName": "l2vlan", 
                    "displayName": "l2vlan", 
                    "name": "kL2vlan", 
                    "value": "135"
                }, 
                {
                    "yangName": "x25ple", 
                    "displayName": "x25ple", 
                    "name": "kX25ple", 
                    "value": "40"
                }, 
                {
                    "yangName": "bsc", 
                    "displayName": "bsc", 
                    "name": "kBsc", 
                    "value": "83"
                }, 
                {
                    "yangName": "isdns", 
                    "displayName": "isdns", 
                    "name": "kIsdns", 
                    "value": "75"
                }, 
                {
                    "yangName": "mediaMailOverIp", 
                    "displayName": "mediaMailOverIp", 
                    "name": "kMediamailoverip", 
                    "value": "139"
                }, 
                {
                    "yangName": "ibm370parChan", 
                    "displayName": "ibm370parChan", 
                    "name": "kIbm370parchan", 
                    "value": "72"
                }, 
                {
                    "yangName": "pos", 
                    "displayName": "pos", 
                    "name": "kPos", 
                    "value": "171"
                }
            ], 
            "importStatement": "from a.api.yang.modules.common.iana.iana_if_type_mib.iana_if_type_mib_module_gen import Ianaiftype"
        }
    ], 
    "createTime": "2013", 
    "module": {
        "prefix": "iana_if_type_mib"
    }, 
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "common", 
            "iana", 
            "iana_if_type_mib"
        ]
    }
}
"""


