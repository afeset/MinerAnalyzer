# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.basic.return_codes import ReturnCodes

class SimpleTrxContext(object):
    def __init__ (self):
        self.myTrxElements=[]
        self.myStatus=ReturnCodes.kOk
        self.myErrorText=""
        
    def copyFromTrxContext (self, trxContext):
        # Shallow copy
        self.myTrxElements=trxContext.getTrxElements()[:]

    def getTrxElements (self):
        return self.myTrxElements

    def getStatus(self):
        return self.myStatus

    def getErrorText(self): 
        return self.myErrorText

    def setErrorText(self, errorText): 
        self.myErrorText=errorText

