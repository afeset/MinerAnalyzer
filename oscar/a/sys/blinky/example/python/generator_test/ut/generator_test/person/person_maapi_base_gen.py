


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class PersonMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , person
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , person
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , person
                       
                       , trxContext=None):
        raise NotImplementedError()



    # descendants

    # status
    def newStatus (self):
        raise NotImplementedError()

    def setStatusObj (self, obj):
        raise NotImplementedError()

    def getStatusObj (self):
        raise NotImplementedError()

    def hasStatus (self):
        raise NotImplementedError()




    # config leaves

    # homeIp
    def requestHomeIp (self, requested):
        raise NotImplementedError()

    def isHomeIpRequested (self):
        raise NotImplementedError()

    def getHomeIp (self):
        raise NotImplementedError()

    def hasHomeIp (self):
        raise NotImplementedError()

    def setHomeIp (self, homeIp):
        raise NotImplementedError()

    # name
    def requestName (self, requested):
        raise NotImplementedError()

    def isNameRequested (self):
        raise NotImplementedError()

    def getName (self):
        raise NotImplementedError()

    def hasName (self):
        raise NotImplementedError()

    def setName (self, name):
        raise NotImplementedError()

    # gender
    def requestGender (self, requested):
        raise NotImplementedError()

    def isGenderRequested (self):
        raise NotImplementedError()

    def getGender (self):
        raise NotImplementedError()

    def hasGender (self):
        raise NotImplementedError()

    def setGender (self, gender):
        raise NotImplementedError()

    # number
    def requestNumber (self, requested):
        raise NotImplementedError()

    def isNumberRequested (self):
        raise NotImplementedError()

    def getNumber (self):
        raise NotImplementedError()

    def hasNumber (self):
        raise NotImplementedError()

    def setNumber (self, number):
        raise NotImplementedError()

    # mobileIp
    def requestMobileIp (self, requested):
        raise NotImplementedError()

    def isMobileIpRequested (self):
        raise NotImplementedError()

    def getMobileIp (self):
        raise NotImplementedError()

    def hasMobileIp (self):
        raise NotImplementedError()

    def setMobileIp (self, mobileIp):
        raise NotImplementedError()

    # homeIp6
    def requestHomeIp6 (self, requested):
        raise NotImplementedError()

    def isHomeIp6Requested (self):
        raise NotImplementedError()

    def getHomeIp6 (self):
        raise NotImplementedError()

    def hasHomeIp6 (self):
        raise NotImplementedError()

    def setHomeIp6 (self, homeIp6):
        raise NotImplementedError()

    # officeIp6
    def requestOfficeIp6 (self, requested):
        raise NotImplementedError()

    def isOfficeIp6Requested (self):
        raise NotImplementedError()

    def getOfficeIp6 (self):
        raise NotImplementedError()

    def hasOfficeIp6 (self):
        raise NotImplementedError()

    def setOfficeIp6 (self, officeIp6):
        raise NotImplementedError()

    # officeIp
    def requestOfficeIp (self, requested):
        raise NotImplementedError()

    def isOfficeIpRequested (self):
        raise NotImplementedError()

    def getOfficeIp (self):
        raise NotImplementedError()

    def hasOfficeIp (self):
        raise NotImplementedError()

    def setOfficeIp (self, officeIp):
        raise NotImplementedError()

    # desiredGender
    def requestDesiredGender (self, requested):
        raise NotImplementedError()

    def isDesiredGenderRequested (self):
        raise NotImplementedError()

    def getDesiredGender (self):
        raise NotImplementedError()

    def hasDesiredGender (self):
        raise NotImplementedError()

    def setDesiredGender (self, desiredGender):
        raise NotImplementedError()

    # linux_
    def requestLinux_ (self, requested):
        raise NotImplementedError()

    def isLinux_Requested (self):
        raise NotImplementedError()

    def getLinux_ (self):
        raise NotImplementedError()

    def hasLinux_ (self):
        raise NotImplementedError()

    def setLinux_ (self, linux_):
        raise NotImplementedError()

    # secondaryNumber
    def requestSecondaryNumber (self, requested):
        raise NotImplementedError()

    def isSecondaryNumberRequested (self):
        raise NotImplementedError()

    def getSecondaryNumber (self):
        raise NotImplementedError()

    def hasSecondaryNumber (self):
        raise NotImplementedError()

    def setSecondaryNumber (self, secondaryNumber):
        raise NotImplementedError()

    # employed
    def requestEmployed (self, requested):
        raise NotImplementedError()

    def isEmployedRequested (self):
        raise NotImplementedError()

    def getEmployed (self):
        raise NotImplementedError()

    def hasEmployed (self):
        raise NotImplementedError()

    def setEmployed (self, employed):
        raise NotImplementedError()

    # height
    def requestHeight (self, requested):
        raise NotImplementedError()

    def isHeightRequested (self):
        raise NotImplementedError()

    def getHeight (self):
        raise NotImplementedError()

    def hasHeight (self):
        raise NotImplementedError()

    def setHeight (self, height):
        raise NotImplementedError()

    # macAddress
    def requestMacAddress (self, requested):
        raise NotImplementedError()

    def isMacAddressRequested (self):
        raise NotImplementedError()

    def getMacAddress (self):
        raise NotImplementedError()

    def hasMacAddress (self):
        raise NotImplementedError()

    def setMacAddress (self, macAddress):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "person", 
        "namespace": "person", 
        "className": "PersonMaapi", 
        "importStatement": "from a.sys.blinky.example.python.generator_test.ut.generator_test.person.person_maapi_gen import PersonMaapi", 
        "baseClassName": "PersonMaapiBase", 
        "baseModule": "person_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "le", 
            "isCurrent": true, 
            "yangName": "people", 
            "namespace": "person", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "keyLeaf": {
                "varName": "person", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "person"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "le", 
            "memberName": "status", 
            "yangName": "status", 
            "className": "BlinkyStatusMaapi", 
            "importStatement": "from a.sys.blinky.example.python.generator_test.ut.generator_test.person.status.status_maapi_gen import BlinkyStatusMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: Ipv4AddressHandlerPy", 
            "memberName": "homeIp", 
            "yangName": "home-ip", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "gender", 
            "yangName": "gender", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "male", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "number", 
            "yangName": "number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: BuiltinStringHandler", 
            "memberName": "mobileIp", 
            "yangName": "mobile-ip", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: Ipv6AddressHandlerPy", 
            "memberName": "homeIp6", 
            "yangName": "home-ip6", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: Ipv6PrefixHandlerPy", 
            "memberName": "officeIp6", 
            "yangName": "office-ip6", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: Ipv4PrefixHandlerPy", 
            "memberName": "officeIp", 
            "yangName": "office-ip", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "desiredGender", 
            "yangName": "desired-gender", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "linux_", 
            "yangName": "linux", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "secondaryNumber", 
            "yangName": "secondary-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "789", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "employed", 
            "yangName": "employed", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "height", 
            "yangName": "height", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "175", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: MacAddressHandlerPy", 
            "memberName": "macAddress", 
            "yangName": "mac-address", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "env": {
        "namespaces": [
            "a", 
            "sys", 
            "blinky", 
            "example", 
            "python", 
            "generator_test", 
            "ut", 
            "generator_test"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: Ipv4AddressHandlerPy", 
            "memberName": "homeIp", 
            "yangName": "home-ip", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "gender", 
            "yangName": "gender", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "male", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "number", 
            "yangName": "number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: BuiltinStringHandler", 
            "memberName": "mobileIp", 
            "yangName": "mobile-ip", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: Ipv6AddressHandlerPy", 
            "memberName": "homeIp6", 
            "yangName": "home-ip6", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: Ipv6PrefixHandlerPy", 
            "memberName": "officeIp6", 
            "yangName": "office-ip6", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: Ipv4PrefixHandlerPy", 
            "memberName": "officeIp", 
            "yangName": "office-ip", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "desiredGender", 
            "yangName": "desired-gender", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "linux_", 
            "yangName": "linux", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "secondaryNumber", 
            "yangName": "secondary-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "789", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "employed", 
            "yangName": "employed", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "height", 
            "yangName": "height", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "175", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: MacAddressHandlerPy", 
            "memberName": "macAddress", 
            "yangName": "mac-address", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


