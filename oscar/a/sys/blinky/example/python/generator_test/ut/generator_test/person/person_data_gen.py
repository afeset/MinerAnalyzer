


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket

from a.infra.net.mac_address import MacAddress
from a.sys.blinky.example.python.generator_test.ut.generator_test_types.generator_test_types_module_gen import GenderT
import struct


class PersonData(object):

    def __init__ (self):

        self.homeIp = None
        self._myHasHomeIp=False
        
        self.name = ""
        self._myHasName=False
        
        self.gender = GenderT.kMale
        self._myHasGender=False
        
        self.number = "123"
        self._myHasNumber=False
        
        self.mobileIp = ""
        self._myHasMobileIp=False
        
        self.homeIp6 = None
        self._myHasHomeIp6=False
        
        self.officeIp6 = None
        self._myHasOfficeIp6=False
        
        self.officeIp = None
        self._myHasOfficeIp=False
        
        self.desiredGender = GenderT.kMale
        self._myHasDesiredGender=False
        
        self.linux_ = ""
        self._myHasLinux_=False
        
        self.secondaryNumber = "789"
        self._myHasSecondaryNumber=False
        
        self.employed = False
        self._myHasEmployed=False
        
        self.height = 175
        self._myHasHeight=False
        
        self.macAddress = MacAddress('\0'*6)
        self._myHasMacAddress=False
        

    def copyFrom (self, other):

        self.homeIp=other.homeIp
        self._myHasHomeIp=other._myHasHomeIp
        
        self.name=other.name
        self._myHasName=other._myHasName
        
        self.gender=other.gender
        self._myHasGender=other._myHasGender
        
        self.number=other.number
        self._myHasNumber=other._myHasNumber
        
        self.mobileIp=other.mobileIp
        self._myHasMobileIp=other._myHasMobileIp
        
        self.homeIp6=other.homeIp6
        self._myHasHomeIp6=other._myHasHomeIp6
        
        self.officeIp6=other.officeIp6
        self._myHasOfficeIp6=other._myHasOfficeIp6
        
        self.officeIp=other.officeIp
        self._myHasOfficeIp=other._myHasOfficeIp
        
        self.desiredGender=other.desiredGender
        self._myHasDesiredGender=other._myHasDesiredGender
        
        self.linux_=other.linux_
        self._myHasLinux_=other._myHasLinux_
        
        self.secondaryNumber=other.secondaryNumber
        self._myHasSecondaryNumber=other._myHasSecondaryNumber
        
        self.employed=other.employed
        self._myHasEmployed=other._myHasEmployed
        
        self.height=other.height
        self._myHasHeight=other._myHasHeight
        
        self.macAddress=other.macAddress
        self._myHasMacAddress=other._myHasMacAddress
        
    # has...() methods

    def hasHomeIp (self):
        return self._myHasHomeIp

    def hasName (self):
        return self._myHasName

    def hasGender (self):
        return self._myHasGender

    def hasNumber (self):
        return self._myHasNumber

    def hasMobileIp (self):
        return self._myHasMobileIp

    def hasHomeIp6 (self):
        return self._myHasHomeIp6

    def hasOfficeIp6 (self):
        return self._myHasOfficeIp6

    def hasOfficeIp (self):
        return self._myHasOfficeIp

    def hasDesiredGender (self):
        return self._myHasDesiredGender

    def hasLinux_ (self):
        return self._myHasLinux_

    def hasSecondaryNumber (self):
        return self._myHasSecondaryNumber

    def hasEmployed (self):
        return self._myHasEmployed

    def hasHeight (self):
        return self._myHasHeight

    def hasMacAddress (self):
        return self._myHasMacAddress


    # setHas...() methods

    def setHasHomeIp (self):
        self._myHasHomeIp=True

    def setHasName (self):
        self._myHasName=True

    def setHasGender (self):
        self._myHasGender=True

    def setHasNumber (self):
        self._myHasNumber=True

    def setHasMobileIp (self):
        self._myHasMobileIp=True

    def setHasHomeIp6 (self):
        self._myHasHomeIp6=True

    def setHasOfficeIp6 (self):
        self._myHasOfficeIp6=True

    def setHasOfficeIp (self):
        self._myHasOfficeIp=True

    def setHasDesiredGender (self):
        self._myHasDesiredGender=True

    def setHasLinux_ (self):
        self._myHasLinux_=True

    def setHasSecondaryNumber (self):
        self._myHasSecondaryNumber=True

    def setHasEmployed (self):
        self._myHasEmployed=True

    def setHasHeight (self):
        self._myHasHeight=True

    def setHasMacAddress (self):
        self._myHasMacAddress=True


    def clearAllHas (self):

        self._myHasHomeIp=False

        self._myHasName=False

        self._myHasGender=False

        self._myHasNumber=False

        self._myHasMobileIp=False

        self._myHasHomeIp6=False

        self._myHasOfficeIp6=False

        self._myHasOfficeIp=False

        self._myHasDesiredGender=False

        self._myHasLinux_=False

        self._myHasSecondaryNumber=False

        self._myHasEmployed=False

        self._myHasHeight=False

        self._myHasMacAddress=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasHomeIp:
            x = "+"
        leafStr = socket.inet_ntop(socket.AF_INET, struct.pack('!L', self.homeIp))
        items.append(x + "HomeIp="+leafStr)

        x=""
        if self._myHasName:
            x = "+"
        leafStr = str(self.name)
        items.append(x + "Name="+leafStr)

        x=""
        if self._myHasGender:
            x = "+"
        leafStr = str(self.gender)
        items.append(x + "Gender="+leafStr)

        x=""
        if self._myHasNumber:
            x = "+"
        leafStr = str(self.number)
        items.append(x + "Number="+leafStr)

        x=""
        if self._myHasMobileIp:
            x = "+"
        leafStr = str(self.mobileIp)
        items.append(x + "MobileIp="+leafStr)

        x=""
        if self._myHasHomeIp6:
            x = "+"
        leafStr = socket.inet_ntop(socket.AF_INET6, self.homeIp6)
        items.append(x + "HomeIp6="+leafStr)

        x=""
        if self._myHasOfficeIp6:
            x = "+"
        (ip, prefix) = self.officeIp6
        leafStr = "%s/%d" % (socket.inet_ntop(socket.AF_INET6, ip), prefix)
        items.append(x + "OfficeIp6="+leafStr)

        x=""
        if self._myHasOfficeIp:
            x = "+"
        (ip, prefix) = self.officeIp
        leafStr = "%s/%d" % (socket.inet_ntop(socket.AF_INET, struct.pack('!L', ip)), prefix)
        items.append(x + "OfficeIp="+leafStr)

        x=""
        if self._myHasDesiredGender:
            x = "+"
        leafStr = str(self.desiredGender)
        items.append(x + "DesiredGender="+leafStr)

        x=""
        if self._myHasLinux_:
            x = "+"
        leafStr = str(self.linux_)
        items.append(x + "Linux_="+leafStr)

        x=""
        if self._myHasSecondaryNumber:
            x = "+"
        leafStr = str(self.secondaryNumber)
        items.append(x + "SecondaryNumber="+leafStr)

        x=""
        if self._myHasEmployed:
            x = "+"
        leafStr = str(self.employed)
        items.append(x + "Employed="+leafStr)

        x=""
        if self._myHasHeight:
            x = "+"
        leafStr = str(self.height)
        items.append(x + "Height="+leafStr)

        x=""
        if self._myHasMacAddress:
            x = "+"
        leafStr = str(self.macAddress)
        items.append(x + "MacAddress="+leafStr)

        return "{PersonData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "PersonData", 
        "namespace": "person", 
        "importStatement": "from a.sys.blinky.example.python.generator_test.ut.generator_test.person.person_data_gen import PersonData"
    }, 
    "ancestors": [
        {
            "namespace": "person", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: Ipv4AddressHandlerPy", 
            "memberName": "homeIp", 
            "yangName": "home-ip", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "gender", 
            "yangName": "gender", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "male", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "number", 
            "yangName": "number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BuiltinStringHandler", 
            "memberName": "mobileIp", 
            "yangName": "mobile-ip", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: Ipv6AddressHandlerPy", 
            "memberName": "homeIp6", 
            "yangName": "home-ip6", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: Ipv6PrefixHandlerPy", 
            "memberName": "officeIp6", 
            "yangName": "office-ip6", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: Ipv4PrefixHandlerPy", 
            "memberName": "officeIp", 
            "yangName": "office-ip", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "desiredGender", 
            "yangName": "desired-gender", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "linux_", 
            "yangName": "linux", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "secondaryNumber", 
            "yangName": "secondary-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "789", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "employed", 
            "yangName": "employed", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "height", 
            "yangName": "height", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "175", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: MacAddressHandlerPy", 
            "memberName": "macAddress", 
            "yangName": "mac-address", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "module": {}, 
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
    "createTime": "2013"
}
"""


