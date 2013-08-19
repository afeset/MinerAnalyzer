# 
# Copyright Qwilt, 2013
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: lena

class TimeZoneInfo(object):
    """Timezone information class

    Holds the timezone information.

    Attributes:
        name: timezone name
        standardOffset: standard offset
        dstOffset: dst offset if exists (None otherwise)
        standardAbbr = standardAbbr
        self.dstAbbr = dstAbbr (None otherwise)
        self.validData = True
    """

    def __init__ (self, name=None):
        self.__initialize(name)

    def __initialize (self, name):
        self.setValues (name, None, None, None, None)
        self.validData = False

    def setValues (self, name, standardOffset, dstOffset, standardAbbr, dstAbbr):
        """Fills the object fields with the given values   

        Args:
            name, standardOffset, dstOffset, standardAbbr, dstAbbr, isdst
        """
        self.name = name
        self.standardOffset = standardOffset
        self.dstOffset = dstOffset
        self.standardAbbr = standardAbbr
        self.dstAbbr = dstAbbr
        self.validData = True

    def dumpToDict (self):
        """Returns a dictionary which represents the object  
        
        Returns: 
            A dictionary: <field name> : <value>
        """
        dic = {}
        dic['name'] = self.name
        dic['standardOffset'] = self.standardOffset
        dic['dstOffset'] = self.dstOffset
        dic['standardAbbr'] = self.standardAbbr
        dic['dstAbbr'] = self.dstAbbr 
        dic['validData'] = self.validData
        return dic

    def loadFromDict (self, dic):
        """Updates the object fields with the given dictionary values   
        
        Args: 
            dic: <field name> : <value>  dictionary
        """
        self.name = dic.get('name', 'NoVal')
        self.standardOffset = dic.get('standardOffset', 'NoVal')
        self.dstOffset = dic.get('dstOffset', 'NoVal')
        self.standardAbbr = dic.get('standardAbbr', 'NoVal')
        self.dstAbbr = dic.get('dstAbbr', 'NoVal')
        self.validData = dic.get('validData', 'NoVal')
        if self.name == 'NoVal' or self.standardOffset == 'NoVal' or self.dstOffset == 'NoVal' or self.standardAbbr == 'NoVal' or self.dstAbbr == 'NoVal' or self.validData == 'NoVal':
            self.__initialize(dic.get('name', 'NoVal'))



