# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

import pyconfdlib

import copy

from a.infra.basic.return_codes import ReturnCodes
from a.sys.confd.pyconfdlib.value import Value
from a.sys.confd.pyconfdlib.value import ConfdValueLow

class KeyPath(object):

    """ 
    A class representing a keypath. 
    It holds bi-dimensional lists of the values constructing the keypath
    """

    def __init__ (self):
        self._key = []

    def __str__ (self):
        return self.getCannonicalStr()

    def getCannonicalStr (self):
        str_ = ""
        if len(self._key):
            for level in self._key:
                if not level:
                    break
                if level[0].isXmlTag():
                    str_ += "/%s" % (level[0].getCannonicalStr())
                else:
                    for val in level:
                        str_ += "{%s}" % val.getCannonicalStr()
        else:
            str_ = "/"
        return str_

    def getLen (self):
        return len(self._key)

    def isEqual (self, other):
        if self.getLen() != other.getLen():
            for logFunc in pyconfdlib._log("is-equal-different-len").debug4Func(): logFunc("isEqual: different lengths. self=%s, other=%s", str(self), str(other))
            return False
        return self.isEqualLen(other, self.getLen())

    def isEqualLen (self, other, compareLen):
        for logFunc in pyconfdlib._log("is-equal-len").debug4Func(): logFunc("isEqualLen called. self=%s, other=%s, len=%d", str(self), str(other), compareLen)
        if (self.getLen() < compareLen) or \
            (other.getLen() < compareLen):
            return False
        for i, level in enumerate(self._key):
            if i < compareLen:
                if len(level) != len(other._key[i]):
                    return False
                for j, val in enumerate(level):
                    if not val.isEqual(other._key[i][j]):
                        return False
            else:
                break
        return True

    def getPrefix (self):
        for logFunc in pyconfdlib._log("get-prefix").debug4Func(): logFunc("called. self=%s", str(self))
        if self._key and self._key[0]:
            val = self._key[0][0]
            (tag, ns, prefix) = val.asXmlTag()
            if not prefix:
                for logFunc in pyconfdlib._log("get-prefix-as-xml-tag-failed").errorFunc(): logFunc("val.asXmlTag() returned None. val=%s, self=%s", str(val), str(self))
                return None
            for logFunc in pyconfdlib._log("get-prefix-done").debug4Func(): logFunc("done. self=%s, prefix=%s", str(self), prefix)
            return prefix

    def getNameSpaceId (self):
        for logFunc in pyconfdlib._log("get-namespace-id").debug4Func(): logFunc("getNameSpaceId called. self=%s", str(self))
        if self._key and self._key[0]:
            val = self._key[0][0]
            (tag, ns, prefix) = val.asXmlTag()
            if not ns:
                for logFunc in pyconfdlib._log("get-namespace-id-as-xml-tag-failed").errorFunc(): logFunc("val.asXmlTag() returned None. val=%s, self=%s", str(val), str(self))
                return None
            for logFunc in pyconfdlib._log("get-namespace-id-done").debug4Func(): logFunc("getNameSpaceId done. self=%s, ns=%s", str(self), ns)
            return ns

    def getAt (self, position):
        #for logFunc in pyconfdlib._log("get-at").debug4Func(): logFunc("getAt called. self=%s, position=%d", str(self), position)
        if (self.getLen() < position) or \
            not len(self._key[position]):
            for logFunc in pyconfdlib._log("get-at-out-of-boundaries").errorFunc(): logFunc("getAt out-of-boundaries. self=%s, position=%d, len=%d", str(self), position, self.getLen())
            return None
        #for logFunc in pyconfdlib._log("get-at-done").debug4Func(): logFunc("getAt done. self=%s, position=%d, value=%s", str(self), position, str(self._key[position][0]))
        return copy.copy(self._key[position][0])

    def insertToKeyPathAt (self, value, pos):
        for logFunc in pyconfdlib._log("insert-to-key-path-at").debug4Func(): logFunc("insertToKeyPathAt called. self=%s, value=%s, pos=%s", str(self), str(value), str(pos))
        if self.getLen() == pyconfdlib.MAXDEPTH:
            for logFunc in pyconfdlib._log("add-key-path-postfix-too-long").errorFunc(): logFunc("addKeyPathPostfix: keypath is at max depth, cannot add a postfix. self=%s, value=%s", str(self), str(value))
            return ReturnCodes.kGeneralError
        if isinstance(value, list):
            self._key.insert(pos, copy.deepcopy(value))
        else:
            self._key.insert(pos, [copy.deepcopy(value)])
        for logFunc in pyconfdlib._log("insert-to-key-path-at-done").debug4Func(): logFunc("insertToKeyPathAt done. self=%s, value=%s, pos=%s", str(self), str(value), str(pos))
        return ReturnCodes.kOk

    def addKeyPathPostfix (self, value):
        for logFunc in pyconfdlib._log("add-key-path-postfix").debug4Func(): logFunc("addKeyPathPostfix called. self=%s, value=%s", str(self), str(value))
        if self.getLen() == pyconfdlib.MAXDEPTH:
            for logFunc in pyconfdlib._log("add-key-path-postfix-too-long").errorFunc(): logFunc("addKeyPathPostfix: keypath is at max depth, cannot add a postfix. self=%s, value=%s", str(self), str(value))
            return ReturnCodes.kGeneralError
        if isinstance(value, list):
            self._key.append(copy.deepcopy(value))
        else:
            self._key.append([copy.deepcopy(value)])
        for logFunc in pyconfdlib._log("add-key-path-postfix-done").debug4Func(): logFunc("addKeyPathPostfix done. self=%s, value=%s", str(self), str(value))
        return ReturnCodes.kOk

    def addKeyPathPrefix (self, value):
        for logFunc in pyconfdlib._log("add-key-path-prefix").debug4Func(): logFunc("addKeyPathPrefix called. self=%s, value=%s", str(self), str(value))
        if self.getLen() == pyconfdlib.MAXDEPTH:
            for logFunc in pyconfdlib._log("add-key-path-prefix-too-long").errorFunc(): logFunc("addKeyPathPrefix: keypath is at max depth, cannot add a prefix. self=%s, value=%s", str(self), str(value))
            return ReturnCodes.kGeneralError
        if isinstance(value, list):
            self._key.insert(0, copy.deepcopy(value))
        else:
            self._key.insert(0, [copy.deepcopy(value)])
        for logFunc in pyconfdlib._log("add-key-path-prefix-done").debug4Func(): logFunc("addKeyPathPrefix done. self=%s, value=%s", str(self), str(value))
        return ReturnCodes.kOk

    def joinKeyPath (self, keyPathToAdd):
        for logFunc in pyconfdlib._log("join-key-path").debug4Func(): logFunc("joinKeyPath called. self=%s, keyPathToAdd=%s", str(self), str(keyPathToAdd))
        if (self.getLen() + len(keyPathToAdd._key)) > pyconfdlib.MAXDEPTH:
            for logFunc in pyconfdlib._log("join-key-path-too-long").errorFunc(): logFunc("joinKeyPath: result is too long, cannot join keypath. self=%s, selfLen=%d, keyPathToAdd=%d", str(self), self.getLen(), str(keyPathToAdd), len(keyPathToAdd._key))
            return ReturnCodes.kGeneralError
        self._key.extend(copy.deepcopy(keyPathToAdd._key))
        for logFunc in pyconfdlib._log("join-key-path-done").debug4Func(): logFunc("joinKeyPath done. self=%s", self._key)
        for logFunc in pyconfdlib._log("join-key-path-done").debug4Func(): logFunc("joinKeyPath done. self=%s, keyPathToAdd=%s", str(self), str(keyPathToAdd))
        return ReturnCodes.kOk

    def getKeyPathPostfixFlattened (self, pathToRemove, leaveLowestKey):
        resKeyPath = KeyPath()
        for logFunc in pyconfdlib._log("get-key-path-postfix-flattened").debug4Func(): logFunc("getKeyPathPostfixFlattened called. self=%s, keyPathToRemove=%s, resKeyPath=%s, leaveLowestKey=%s",
                                                                 str(self), str(pathToRemove), str(resKeyPath), leaveLowestKey)
        for i, level in enumerate(self._key):
            if i < pathToRemove.getLen():
                continue
            if level[0].isXmlTag():
                resKeyPath._key.append(copy.deepcopy(level))

        for logFunc in pyconfdlib._log("get-key-path-postfix-flattened-done").debug4Func(): logFunc("getKeyPathPostfixFlattened done. self=%s, keyPathToRemove=%s, resKeyPath=%s, leaveLowestKey=%s",
                                                                      str(self), str(pathToRemove), str(resKeyPath), leaveLowestKey)
        return resKeyPath

    def copyPartial (self, other, lenToCopy):
        for logFunc in pyconfdlib._log("copy-partial").debug4Func(): logFunc("copyPartial called. self=%s, other=%s, lenToCopy=%d",
                                               str(self), str(other), lenToCopy)
        if other.getLen() < lenToCopy:
            for logFunc in pyconfdlib._log("copy-partial-too-short").errorFunc(): logFunc("copyPartial other keypath is too short. self=%s, other=%s, , otherLen=%d, lenToCopy=%d",
                                                            str(self), str(other), other.getLen(), lenToCopy)
        self._key = copy.deepcopy(other._key[:lenToCopy])
        for logFunc in pyconfdlib._log("copy-partial-done").debug4Func(): logFunc("copyPartial done. self=%s, other=%s, lenToCopy=%d",
                                                    str(self), str(other), lenToCopy)
    def copyStaticPartUpToLowestList (self, other):
        for logFunc in pyconfdlib._log("copy-static-part-up-to-lowest-list").debug4Func(): logFunc("called. self=%s, other=%s",
                                                                     str(self), str(other))
        self._key = []
        startCopying = False
        for level in reversed(other._key):
            if level:
                if startCopying:
                    self._key.insert(0, copy.deepcopy(level))
                if not level[0].isXmlTag():
                    startCopying = True
                    
            """if level: 
                if level[0].isXmlTag():
                    if startCopying:
                        self._key.insert(0, copy.deepcopy(level))
                else:
                    startCopying = True"""
        for logFunc in pyconfdlib._log("copy-static-part-up-to-lowest-list-done").debug4Func(): logFunc("done. self=%s, other=%s",
                                                                          str(self), str(other))

    def getListKeys (self):
        for logFunc in pyconfdlib._log("get-list-keys").debug4Func(): logFunc("getListKeys called. self=%s", str(self))
        keys = []
        for level in self._key:
            if level:
                if not level[0].isXmlTag():
                    keys.append(copy.deepcopy(level[0]))
        for logFunc in pyconfdlib._log("get-list-keys-done").debug4Func(): logFunc("getListKeys done. self=%s, keys=%s", str(self), [str(key) for key in keys])
        return keys

    def isTagEqual (self, keyDepth, ns, tag):
        #for logFunc in pyconfdlib._log("is-tag-equal").debug4Func(): logFunc("isTagEqual called. self=%s, keyDepth=%d, ns=%s, tag=%s", str(self), keyDepth, ns, tag)
        if keyDepth < self.getLen():
            if self._key[keyDepth] and self._key[keyDepth][0].isXmlTag():
                (valTag, valNs, valPrefix) = self._key[keyDepth][0].asXmlTag()
                if ns == valNs and tag == valTag:
                    #for logFunc in pyconfdlib._log("is-tag-equal-true").debug4Func(): 
                    #   logFunc("isTagEqual True. self=%s, keyDepth=%d, ns=%s, tag=%s", str(self), keyDepth, ns, tag)
                    return True
                else:
                    #for logFunc in pyconfdlib._log("is-tag-equal-false").debug4Func(): 
                    #   logFunc("isTagEqual False. self=%s, keyDepth=%d, ns=%s, tag=%s, actualTag=%s", str(self), keyDepth, ns, tag, self._key[keyDepth][0].asXmlTag())
                    return False

        for logFunc in pyconfdlib._log("is-tag-equal-bad-depth").debug4Func(): logFunc("isTagEqual bad depth. self=%s, keyDepth=%d, ns=%s, tag=%s",
                                                                                       str(self), keyDepth, ns, tag)
        return False

    def isDescendantOf (self, other):
        for logFunc in pyconfdlib._log("is-descendant-of").debug4Func(): logFunc("isDescendantOf called. self=%s, other=%s", str(self), other)

        if self.getLen() >= other.getLen():
            for logFunc in pyconfdlib._log("is-descendant-of-too-short").debug4Func(): logFunc("isDescendantOf False. self too short. self=%s, other=%s", str(self), other)
            return False

        if self.isEqualLen(other, self.getLen()):
            for logFunc in pyconfdlib._log("is-descendant-of-true").debug4Func(): logFunc("isDescendantOf True. self=%s, other=%s", str(self), other)
            return True
            
        for logFunc in pyconfdlib._log("is-descendant-of-false").debug4Func(): logFunc("isDescendantOf False. isEqualLen() returned False. self=%s, other=%s", str(self), other)
        return False

class ConfdHKeyPathLow(object):

    @staticmethod
    def allocConfdHKeyPath ():
        confdHKeyPathPtr = pyconfdlib.dll.py_allocConfdHkeypath()
        for logFunc in pyconfdlib._log("alloc-confd-hkeypath").debug4Func(): logFunc("allocConfdHKeyPath called. confdHKeyPathPtr=%s", str(confdHKeyPathPtr))
        return confdHKeyPathPtr

    @staticmethod
    def deallocConfdHKeyPath (confdHKeyPathPtr):
        for logFunc in pyconfdlib._log("dealloc-confd-hkeypath").debug4Func(): logFunc("deallocConfdHKeyPath called. confdHKeyPathPtr=%s", str(confdHKeyPathPtr))
        pyconfdlib.dll.py_deallocConfdHkeypath(confdHKeyPathPtr)
        

    @staticmethod
    def ConfdHKeyPathToStr (confdHKeyPathPtr):
        if not confdHKeyPathPtr:
            return "(NULL)"
        buf=pyconfdlib.createStringBuffer(pyconfdlib.kMaxStringSize)
        len_=pyconfdlib.dll.py_confd_pp_kpath(buf, pyconfdlib.sizeof(buf), confdHKeyPathPtr)
        if len_ >= pyconfdlib.sizeof(buf):
            buf=pyconfdlib.createStringBuffer(len_+1)
            len_=pyconfdlib.dll.py_confd_pp_kpath(buf, pyconfdlib.sizeof(buf), confdHKeyPathPtr)
        return buf.value[:len_]

    @staticmethod
    def deepConvertConfdHKeyPathToPyKeyPath (confdHKeyPathPtr, pyKeyPath):
        """
        This function performs a deep convertion of a confd_hkeypath object to a python KeyPath object.
        It reallocates all data memory, making the python KeyPath object its owner.
        pyKeyPath must be pre-constructed
        """
        for logFunc in pyconfdlib._log("deep-convert-confd-hkeypath-to-pykeypath").debug4Func(): logFunc("deepConvertConfdHKeyPathToPyKeyPath called. confdHKeyPathPtr=%s, pyKeyPath=%s", ConfdHKeyPathLow.ConfdHKeyPathToStr(confdHKeyPathPtr), pyKeyPath)
        if not pyKeyPath or not confdHKeyPathPtr:
            for logFunc in pyconfdlib._log("deep-convert-confd-value-to-pyvalue-invalid-args").errorFunc(): logFunc("deepConvertConfdValueToPyValue invalid args: confdHKeyPathPtr=%s, pyKeyPath=%s", ConfdHKeyPathLow.ConfdHKeyPathToStr(confdHKeyPathPtr), pyKeyPath)
            return ReturnCodes.kGeneralError
        confdKeyPathLen = pyconfdlib.dll.py_getHkeypathLen(confdHKeyPathPtr)
        for logFunc in pyconfdlib._log("deep-convert-confd-hkeypath-to-pykeypath-len").debug4Func(): logFunc("deepConvertConfdHKeyPathToPyKeyPath: confdKetPathLen=%d, confdHKeyPathPtr=%s, pyKeyPath=%s", confdKeyPathLen, ConfdHKeyPathLow.ConfdHKeyPathToStr(confdHKeyPathPtr), pyKeyPath)
        for i in range(confdKeyPathLen):
            level = []
            for j in range(pyconfdlib.MAXKEYLEN):
                confdValPtr = pyconfdlib.dll.py_getHkeypathValue(confdHKeyPathPtr, confdKeyPathLen-1-i, j, False)
                pyValue = Value()
                rc = ConfdValueLow.deepConvertConfdValueToPyValue(confdValPtr, pyValue)
                if rc != ReturnCodes.kOk:
                    for logFunc in pyconfdlib._log("deep-convert-confd-hkeypath-to-pykeypath-convert-keypath-failed").errorFunc(): logFunc("deepConvertConfdHKeyPathToPyKeyPath: deepConvertConfdValueToPyValue "\
                                                                                                             "failed: i=%d, j=%d, confdHKeyPathPtr=%s, pyKeyPath=%s, rc=%s", i, j, ConfdHKeyPathLow.ConfdHKeyPathToStr(confdHKeyPathPtr), pyKeyPath, str(rc))
                    return ReturnCodes.kGeneralError
                if pyValue.getType() == Value.kEmpty:
                    break
                level.append(pyValue)
            if level:
                #for logFunc in pyconfdlib._log("deep-convert-confd-hkeypath-to-pykeypath-appending").debug4Func(): logFunc("deepConvertConfdHKeyPathToPyKeyPath: appending level=%s", level)
                pyKeyPath._key.append(level)

        for logFunc in pyconfdlib._log("deep-convert-confd-hkeypath-to-pykeypath-done").debug4Func(): logFunc("deepConvertConfdHKeyPathToPyKeyPath done. confdHKeyPathPtr=%s, pyKeyPath=%s", ConfdHKeyPathLow.ConfdHKeyPathToStr(confdHKeyPathPtr), pyKeyPath)
        return ReturnCodes.kOk

