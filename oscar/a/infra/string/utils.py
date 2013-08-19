# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

# This Python class mimics the basic::ReturnCodes class

import string

class Utils:
    @staticmethod
    def s_turnToPrintable(inputStr):
        newStr = []
        for char in inputStr:
            if char in string.printable:
                newStr.append(char)
            else:
                newStr.append(r'\x{0:02x}'.format(ord(char))) 
        return "".join(newStr)

