


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes
from a.infra.misc.init_guard import InitGuard

from a.sys.confd.pyconfdlib.tag_values import TagValues
from a.sys.confd.pyconfdlib.value import Value
from a.sys.confd.pyconfdlib.key_path import KeyPath

from school_maapi_base_gen import SchoolMaapiBase

from a.sys.blinky.example.ut.school_example.school.person.person_maapi_list_gen import BlinkyPersonMaapiList



class BlinkySchoolMaapi(SchoolMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-school")
        self.domain = None

        
        self.personListObj = None
        

        
        self.bestStudentRequested = False
        self.bestStudent = None
        self.bestStudentSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestBestStudent(True)
        
        
        
        if not self.personListObj:
            self.personListObj = self.newPersonList()
            self.personListObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestBestStudent(True)
        
        
        
        if not self.personListObj:
            self.personListObj = self.newPersonList()
            self.personListObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestBestStudent(False)
        
        
        
        if not self.personListObj:
            self.personListObj = self.newPersonList()
            self.personListObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestBestStudent(False)
        
        
        
        if not self.personListObj:
            self.personListObj = self.newPersonList()
            self.personListObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setBestStudent(None)
        self.bestStudentSet = False
        
        
        if self.personListObj:
            self.personListObj.clearAllSet()
        

    def write (self
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(trxContext)

    def read (self
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(
                                  True,
                                  trxContext)

    def newPersonList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-personlist').debug3Func(): logFunc('called.')
        personList = BlinkyPersonMaapiList(self._log)
        personList.init(self.domain)
        return personList

    def setPersonListObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-personlist').debug3Func(): logFunc('called. obj=%s', obj)
        self.personListObj = obj

    def getPersonListObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-personlist').debug3Func(): logFunc('called. self.personListObj=%s', self.personListObj)
        return self.personListObj

    def hasPersonList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-personlist').debug3Func(): logFunc('called. self.personListObj=%s', self.personListObj)
        if self.personListObj:
            return True
        return False



    def requestBestStudent (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-beststudent').debug3Func(): logFunc('called. requested=%s', requested)
        self.bestStudentRequested = requested
        self.bestStudentSet = False

    def isBestStudentRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-beststudent-requested').debug3Func(): logFunc('called. requested=%s', self.bestStudentRequested)
        return self.bestStudentRequested

    def getBestStudent (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-beststudent').debug3Func(): logFunc('called. self.bestStudentSet=%s, self.bestStudent=%s', self.bestStudentSet, self.bestStudent)
        if self.bestStudentSet:
            return self.bestStudent
        return None

    def hasBestStudent (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-beststudent').debug3Func(): logFunc('called. self.bestStudentSet=%s, self.bestStudent=%s', self.bestStudentSet, self.bestStudent)
        if self.bestStudentSet:
            return True
        return False

    def setBestStudent (self, bestStudent):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-beststudent').debug3Func(): logFunc('called. bestStudent=%s, old=%s', bestStudent, self.bestStudent)
        self.bestStudentSet = True
        self.bestStudent = bestStudent


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.personListObj:
            self.personListObj._clearAllReadData()
        

        
        self.bestStudent = 0
        self.bestStudentSet = False
        

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("school", "http://qwilt.com/model/school-example", "sche"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       
                       readAllOrFail,
                       trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-read').debug3Func(): logFunc('called. PARAMS, readAllOrFail=%s', readAllOrFail)

        if readAllOrFail:
            self._clearAllReadData()

        tagValueList = TagValues()

        res = self._fillReadTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-fill-read-tag-value-failed').errorFunc(): logFunc('_fillReadTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(
                                       None)

        res = self.domain.readMaapi(tagValueList, keyPath, trxContext)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-domain-failed').errorFunc(): logFunc('domain.readMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        res = self._readTagValues(tagValueList, readAllOrFail)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-read-tag-values-failed').errorFunc(): logFunc('_readTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-read-done').debug3Func(): logFunc('done. PARAMS, readAllOrFail=%s', readAllOrFail)
        return ReturnCodes.kOk

    def _collectItemsToDelete (self,
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        
        if self.personListObj:
            res = self.personListObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-people-failed').errorFunc(): logFunc('personListObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasBestStudent():
            valBestStudent = Value()
            if self.bestStudent is not None:
                valBestStudent.setString(self.bestStudent)
            else:
                valBestStudent.setEmpty()
            tagValueList.push(("best-student", "http://qwilt.com/model/school-example"), valBestStudent)
        

        
        if self.personListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("people" , "http://qwilt.com/model/school-example", "sche")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.personListObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-people-failed').errorFunc(): logFunc('personListObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isBestStudentRequested():
            valBestStudent = Value()
            valBestStudent.setEmpty()
            tagValueList.push(("best-student", "http://qwilt.com/model/school-example"), valBestStudent)
        

        
        if self.personListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("people" , "http://qwilt.com/model/school-example", "sche")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.personListObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-people-failed').errorFunc(): logFunc('personListObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isBestStudentRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "best-student") or \
                (ns != "http://qwilt.com/model/school-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-beststudent').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "bestStudent", "best-student", "http://qwilt.com/model/school-example", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-best-student-bad-value').infoFunc(): logFunc('bestStudent not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setBestStudent(tempVar)
            for logFunc in self._log('read-tag-values-best-student').debug3Func(): logFunc('read bestStudent. bestStudent=%s, tempValue=%s', self.bestStudent, tempValue.getType())
        

        
        if self.personListObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "people") or \
                (ns != "http://qwilt.com/model/school-example") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "people", "http://qwilt.com/model/school-example", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.personListObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-people-failed').errorFunc(): logFunc('personListObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "people") or \
                (ns != "http://qwilt.com/model/school-example") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "people", "http://qwilt.com/model/school-example", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "school", 
        "namespace": "school", 
        "className": "SchoolMaapi", 
        "importStatement": "from a.sys.blinky.example.ut.school_example.school.school_maapi_gen import SchoolMaapi", 
        "baseClassName": "SchoolMaapiBase", 
        "baseModule": "school_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "sche", 
            "yangName": "school", 
            "namespace": "school", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/school-example", 
            "name": "school"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "sche", 
            "memberName": "personList", 
            "yangName": "people", 
            "className": "BlinkyPersonMaapiList", 
            "importStatement": "from a.sys.blinky.example.ut.school_example.school.person.person_maapi_list_gen import BlinkyPersonMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/school-example"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/school-example", 
            "moduleYangNamespacePrefix": "sche", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "bestStudent", 
            "yangName": "best-student", 
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
            "ut", 
            "school_example"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/school-example", 
            "moduleYangNamespacePrefix": "sche", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "bestStudent", 
            "yangName": "best-student", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


