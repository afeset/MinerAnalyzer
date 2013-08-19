


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

# Must be set here to avoid stupid warnings about stuff in BlinkyOperData
__pychecker__="no-classattr"

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket





class CountersOperData (object):

    def __init__ (self):

        self.commandWarningTimeouts = 0
        self._myHasCommandWarningTimeouts=False
        self._myCommandWarningTimeoutsRequested=False
        
        self.commandErrors = 0
        self._myHasCommandErrors=False
        self._myCommandErrorsRequested=False
        
        self.fileErrors = 0
        self._myHasFileErrors=False
        self._myFileErrorsRequested=False
        
        self.reads = 0
        self._myHasReads=False
        self._myReadsRequested=False
        
        self.parsingErrors = 0
        self._myHasParsingErrors=False
        self._myParsingErrorsRequested=False
        
        self.commandTimeouts = 0
        self._myHasCommandTimeouts=False
        self._myCommandTimeoutsRequested=False
        


    def copyFrom (self, other):

        self.commandWarningTimeouts=other.commandWarningTimeouts
        self._myHasCommandWarningTimeouts=other._myHasCommandWarningTimeouts
        self._myCommandWarningTimeoutsRequested=other._myCommandWarningTimeoutsRequested
        
        self.commandErrors=other.commandErrors
        self._myHasCommandErrors=other._myHasCommandErrors
        self._myCommandErrorsRequested=other._myCommandErrorsRequested
        
        self.fileErrors=other.fileErrors
        self._myHasFileErrors=other._myHasFileErrors
        self._myFileErrorsRequested=other._myFileErrorsRequested
        
        self.reads=other.reads
        self._myHasReads=other._myHasReads
        self._myReadsRequested=other._myReadsRequested
        
        self.parsingErrors=other.parsingErrors
        self._myHasParsingErrors=other._myHasParsingErrors
        self._myParsingErrorsRequested=other._myParsingErrorsRequested
        
        self.commandTimeouts=other.commandTimeouts
        self._myHasCommandTimeouts=other._myHasCommandTimeouts
        self._myCommandTimeoutsRequested=other._myCommandTimeoutsRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isCommandWarningTimeoutsRequested():
            self.commandWarningTimeouts=other.commandWarningTimeouts
            self._myHasCommandWarningTimeouts=other._myHasCommandWarningTimeouts
            self._myCommandWarningTimeoutsRequested=other._myCommandWarningTimeoutsRequested
        
        if self.isCommandErrorsRequested():
            self.commandErrors=other.commandErrors
            self._myHasCommandErrors=other._myHasCommandErrors
            self._myCommandErrorsRequested=other._myCommandErrorsRequested
        
        if self.isFileErrorsRequested():
            self.fileErrors=other.fileErrors
            self._myHasFileErrors=other._myHasFileErrors
            self._myFileErrorsRequested=other._myFileErrorsRequested
        
        if self.isReadsRequested():
            self.reads=other.reads
            self._myHasReads=other._myHasReads
            self._myReadsRequested=other._myReadsRequested
        
        if self.isParsingErrorsRequested():
            self.parsingErrors=other.parsingErrors
            self._myHasParsingErrors=other._myHasParsingErrors
            self._myParsingErrorsRequested=other._myParsingErrorsRequested
        
        if self.isCommandTimeoutsRequested():
            self.commandTimeouts=other.commandTimeouts
            self._myHasCommandTimeouts=other._myHasCommandTimeouts
            self._myCommandTimeoutsRequested=other._myCommandTimeoutsRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasCommandWarningTimeouts():
            self.commandWarningTimeouts=other.commandWarningTimeouts
            self._myHasCommandWarningTimeouts=other._myHasCommandWarningTimeouts
            self._myCommandWarningTimeoutsRequested=other._myCommandWarningTimeoutsRequested
        
        if other.hasCommandErrors():
            self.commandErrors=other.commandErrors
            self._myHasCommandErrors=other._myHasCommandErrors
            self._myCommandErrorsRequested=other._myCommandErrorsRequested
        
        if other.hasFileErrors():
            self.fileErrors=other.fileErrors
            self._myHasFileErrors=other._myHasFileErrors
            self._myFileErrorsRequested=other._myFileErrorsRequested
        
        if other.hasReads():
            self.reads=other.reads
            self._myHasReads=other._myHasReads
            self._myReadsRequested=other._myReadsRequested
        
        if other.hasParsingErrors():
            self.parsingErrors=other.parsingErrors
            self._myHasParsingErrors=other._myHasParsingErrors
            self._myParsingErrorsRequested=other._myParsingErrorsRequested
        
        if other.hasCommandTimeouts():
            self.commandTimeouts=other.commandTimeouts
            self._myHasCommandTimeouts=other._myHasCommandTimeouts
            self._myCommandTimeoutsRequested=other._myCommandTimeoutsRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.commandWarningTimeouts=other.commandWarningTimeouts
        self._myHasCommandWarningTimeouts=other._myHasCommandWarningTimeouts
        
        self.commandErrors=other.commandErrors
        self._myHasCommandErrors=other._myHasCommandErrors
        
        self.fileErrors=other.fileErrors
        self._myHasFileErrors=other._myHasFileErrors
        
        self.reads=other.reads
        self._myHasReads=other._myHasReads
        
        self.parsingErrors=other.parsingErrors
        self._myHasParsingErrors=other._myHasParsingErrors
        
        self.commandTimeouts=other.commandTimeouts
        self._myHasCommandTimeouts=other._myHasCommandTimeouts
        


    def setAllNumericToZero (self):
        
        self.commandWarningTimeouts=0
        self.setHasCommandWarningTimeouts()
        self.commandErrors=0
        self.setHasCommandErrors()
        self.fileErrors=0
        self.setHasFileErrors()
        self.reads=0
        self.setHasReads()
        self.parsingErrors=0
        self.setHasParsingErrors()
        self.commandTimeouts=0
        self.setHasCommandTimeouts()
        
        pass

    def subtractAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasCommandWarningTimeouts():
            if other.hasCommandWarningTimeouts():
                self.commandWarningTimeouts -= other.commandWarningTimeouts
        
        if self.hasCommandErrors():
            if other.hasCommandErrors():
                self.commandErrors -= other.commandErrors
        
        if self.hasFileErrors():
            if other.hasFileErrors():
                self.fileErrors -= other.fileErrors
        
        if self.hasReads():
            if other.hasReads():
                self.reads -= other.reads
        
        if self.hasParsingErrors():
            if other.hasParsingErrors():
                self.parsingErrors -= other.parsingErrors
        
        if self.hasCommandTimeouts():
            if other.hasCommandTimeouts():
                self.commandTimeouts -= other.commandTimeouts
        
        
        pass


    def addAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasCommandWarningTimeouts():
            if other.hasCommandWarningTimeouts():
                self.commandWarningTimeouts += other.commandWarningTimeouts
        
        if self.hasCommandErrors():
            if other.hasCommandErrors():
                self.commandErrors += other.commandErrors
        
        if self.hasFileErrors():
            if other.hasFileErrors():
                self.fileErrors += other.fileErrors
        
        if self.hasReads():
            if other.hasReads():
                self.reads += other.reads
        
        if self.hasParsingErrors():
            if other.hasParsingErrors():
                self.parsingErrors += other.parsingErrors
        
        if self.hasCommandTimeouts():
            if other.hasCommandTimeouts():
                self.commandTimeouts += other.commandTimeouts
        
        
        pass


    # has...() methods

    def hasCommandWarningTimeouts (self):
        return self._myHasCommandWarningTimeouts

    def hasCommandErrors (self):
        return self._myHasCommandErrors

    def hasFileErrors (self):
        return self._myHasFileErrors

    def hasReads (self):
        return self._myHasReads

    def hasParsingErrors (self):
        return self._myHasParsingErrors

    def hasCommandTimeouts (self):
        return self._myHasCommandTimeouts




    # setHas...() methods

    def setHasCommandWarningTimeouts (self):
        self._myHasCommandWarningTimeouts=True

    def setHasCommandErrors (self):
        self._myHasCommandErrors=True

    def setHasFileErrors (self):
        self._myHasFileErrors=True

    def setHasReads (self):
        self._myHasReads=True

    def setHasParsingErrors (self):
        self._myHasParsingErrors=True

    def setHasCommandTimeouts (self):
        self._myHasCommandTimeouts=True




    # isRequested...() methods

    def isCommandWarningTimeoutsRequested (self):
        return self._myCommandWarningTimeoutsRequested

    def isCommandErrorsRequested (self):
        return self._myCommandErrorsRequested

    def isFileErrorsRequested (self):
        return self._myFileErrorsRequested

    def isReadsRequested (self):
        return self._myReadsRequested

    def isParsingErrorsRequested (self):
        return self._myParsingErrorsRequested

    def isCommandTimeoutsRequested (self):
        return self._myCommandTimeoutsRequested




    # setRequested...() methods

    def setCommandWarningTimeoutsRequested (self):
        self._myCommandWarningTimeoutsRequested=True

    def setCommandErrorsRequested (self):
        self._myCommandErrorsRequested=True

    def setFileErrorsRequested (self):
        self._myFileErrorsRequested=True

    def setReadsRequested (self):
        self._myReadsRequested=True

    def setParsingErrorsRequested (self):
        self._myParsingErrorsRequested=True

    def setCommandTimeoutsRequested (self):
        self._myCommandTimeoutsRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myCommandWarningTimeoutsRequested:
            x = "+CommandWarningTimeouts="
            if self._myHasCommandWarningTimeouts:
                leafStr = str(self.commandWarningTimeouts)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myCommandErrorsRequested:
            x = "+CommandErrors="
            if self._myHasCommandErrors:
                leafStr = str(self.commandErrors)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myFileErrorsRequested:
            x = "+FileErrors="
            if self._myHasFileErrors:
                leafStr = str(self.fileErrors)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myReadsRequested:
            x = "+Reads="
            if self._myHasReads:
                leafStr = str(self.reads)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myParsingErrorsRequested:
            x = "+ParsingErrors="
            if self._myHasParsingErrors:
                leafStr = str(self.parsingErrors)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myCommandTimeoutsRequested:
            x = "+CommandTimeouts="
            if self._myHasCommandTimeouts:
                leafStr = str(self.commandTimeouts)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{CountersOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+CommandWarningTimeouts="
        if self._myHasCommandWarningTimeouts:
            leafStr = str(self.commandWarningTimeouts)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myCommandWarningTimeoutsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+CommandErrors="
        if self._myHasCommandErrors:
            leafStr = str(self.commandErrors)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myCommandErrorsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+FileErrors="
        if self._myHasFileErrors:
            leafStr = str(self.fileErrors)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myFileErrorsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+Reads="
        if self._myHasReads:
            leafStr = str(self.reads)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myReadsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+ParsingErrors="
        if self._myHasParsingErrors:
            leafStr = str(self.parsingErrors)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myParsingErrorsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+CommandTimeouts="
        if self._myHasCommandTimeouts:
            leafStr = str(self.commandTimeouts)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myCommandTimeoutsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{CountersOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setCommandWarningTimeoutsRequested()
        self.setCommandErrorsRequested()
        self.setFileErrorsRequested()
        self.setReadsRequested()
        self.setParsingErrorsRequested()
        self.setCommandTimeoutsRequested()
        
        


    def setCommandWarningTimeouts (self, commandWarningTimeouts):
        self.commandWarningTimeouts = commandWarningTimeouts
        self.setHasCommandWarningTimeouts()

    def setCommandErrors (self, commandErrors):
        self.commandErrors = commandErrors
        self.setHasCommandErrors()

    def setFileErrors (self, fileErrors):
        self.fileErrors = fileErrors
        self.setHasFileErrors()

    def setReads (self, reads):
        self.reads = reads
        self.setHasReads()

    def setParsingErrors (self, parsingErrors):
        self.parsingErrors = parsingErrors
        self.setHasParsingErrors()

    def setCommandTimeouts (self, commandTimeouts):
        self.commandTimeouts = commandTimeouts
        self.setHasCommandTimeouts()


"""
Extracted from the below data: 
{
    "node": {
        "className": "CountersOperData", 
        "namespace": "counters", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.source.counters.counters_oper_data_gen import CountersOperData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "platform", 
            "isCurrent": false
        }, 
        {
            "namespace": "manager", 
            "isCurrent": false
        }, 
        {
            "namespace": "source", 
            "isCurrent": false
        }, 
        {
            "namespace": "counters", 
            "isCurrent": true
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "commandWarningTimeouts", 
            "yangName": "command-warning-timeouts", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "commandErrors", 
            "yangName": "command-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "fileErrors", 
            "yangName": "file-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "reads", 
            "yangName": "reads", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "parsingErrors", 
            "yangName": "parsing-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "commandTimeouts", 
            "yangName": "command-timeouts", 
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
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "common", 
            "qwilt_tech_platform_manager"
        ]
    }, 
    "createTime": "2013"
}
"""


