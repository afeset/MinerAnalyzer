# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from utils import Utils
from a.infra.misc.enum_with_value import EnumWithValue

class DomainPriority(object):
    class DomainPriorities(EnumWithValue):
        def __init__ (self, value, name):
            EnumWithValue.__init__(self, value, name)
    
    kDummy=DomainPriorities(1, "kDummy")

    kGlobalBegin=DomainPriorities(1000, "kGlobalBegin")

    kSystemIP_NetworkBefore=DomainPriorities(2500, "kSystemIP_NetworkBefore")
    kSystemIP_NetworkMain=DomainPriorities(3000,"kSystemIP_NetworkMain")
    kSystemIP_NetworkAfter=DomainPriorities(3500, "kSystemIP_NetworkAfter")

    kApplicationDefault=DomainPriorities(4000,"kApplicationDefault")
    
    kDefault=DomainPriorities(5000,"kDefault")
    kUnitTestDefault=DomainPriorities(5500,"kUnitTestDefault")


    kGlobalEnd=DomainPriorities(9000,"kGlobalEnd")

