import ctypes
import pyconfdlib

import a.infra.process.captain
from pyconfdlib import ConfdValues

class ConfdHkeypath():
    """ 
    A Wrapper for a confd_hkeypath_t struct. 
    """
    def __init__ (self, hkeypathPtr=None):
        if hkeypathPtr is None:
            self._myHkeypathPtr=pyconfdlib.dll.py_allocConfdHkeypath()
            self._myIsMine=True
        else:
            self._myHkeypathPtr=hkeypathPtr
            self._myIsMine=False

    def getLen (self):
        self._raiseIfNull()
        return pyconfdlib.dll.py_getHkeypathLen(self._myHkeypathPtr)

    def setLen (self, newLen):
        self._raiseIfNull()
        return pyconfdlib.dll.py_setHkeypathLen(self._myHkeypathPtr, newLen)

    def getValue (self, level, keyIndex, checkLevel=True):
        self._raiseIfNull()
        # TODO(orens): check level and index so that we have a nice exception
        checkLevelInt=0
        if checkLevel:
            checkLevelInt=1
        value=pyconfdlib.dll.py_getHkeypathValue(self._myHkeypathPtr, level, keyIndex, checkLevelInt)
        if not value:
            raise Exception("Got a NULL pointer for getValue(level=%s, keyIndex=%s)" % (level, keyIndex))
        return ConfdValues(value)

    def copyValueTo (self, level, keyIndex, value, indexInValue):
        self._raiseIfNull()
        # TODO(orens): check level and index so that we have a nice exception
        srcValue=pyconfdlib.dll.py_getHkeypathValue(self._myHkeypathPtr, level, keyIndex)
        if not srcValue:
            raise Exception("Got a NULL pointer for copyValueTo(level=%s, keyIndex=%s)" % (level, keyIndex))
        pyconfdlib.dll.py_confd_value_dup_to(srcValue, 0, value, indexInValue)

    def addKeyPathPostfix(self, value):
        for logFunc in pyconfdlib._log("add-key-path-postfix").debug4Func(): logFunc("ConfdHkeypath.addKeyPathPostfix()(): old=%s, value=%s", self, value)
        if (self._myHkeypathPtr):
            # move each value column one step backwards
            len_ = self.getLen()
            if (len_+1 < pyconfdlib.MAXDEPTH):
                temp=ConfdHkeypath()
                value.copyTo(temp.getValue(0,0,False))
                temp.getValue(1,0,False).CONFD_SET_NOEXISTS()
                temp.setLen(1)

                for i in range(len_):
                    for j in range(pyconfdlib.MAXKEYLEN):
                        for logFunc in pyconfdlib._log("add-key-path-postfix-moving").debug4Func():
                            logFunc("ConfdHkeypath.addKeyPathPostfix()(): moving value, i=%s, j=%s, v=%s",
                                    i, j, self.getValue(i,j))
                        self.getValue(i,j).copyTo(temp.getValue(i+1,j,False))
                        temp.getValue(i+1,j+1,False).CONFD_SET_NOEXISTS()
                        for logFunc in pyconfdlib._log("add-key-path-postfix-after-moving").debug4Func():
                            logFunc("ConfdHkeypath.addKeyPathPostfix()(): after moving value, i=%s, j=%s, v=%s",
                                    i, j, self.getValue(i,j))
                        if self.getValue(i, j+1).getType() == pyconfdlib.C_NOEXISTS:
                            break
                    temp.setLen(temp.getLen()+1)
                self._free()
                # Own the pointer instead of temp
                self._myHkeypathPtr = temp._myHkeypathPtr
                temp._myHkeypathPtr=None
                self._myIsMine=True
            else:
                # Cant add another level - the path is too deep already
                for logFunc in pyconfdlib._log("add-key-path-postfix-too-deep").errorFunc():
                    logFunc("ConfdHkeypath.addKeyPathPostfix() - too deep - fatal. myKeyPath=%s, value=%s",
                           self._myHkeypathPtr, value)
                a.infra.process.processFatal("ConfdHkeypath.addKeyPathPostfix() - too deep - fatal. myKeyPath=%s, value=%s" % 
                                       (self._myHkeypathPtr, value))
        else:
            # create a new key path
            temp=self.__class__()
            value.copyTo(temp.getValue(0,0,False))
            temp.getValue(1,0,False).CONFD_SET_NOEXISTS()
            temp.setLen(1)
            # Own the pointer instead of temp
            self._myHkeypathPtr = temp._myHkeypathPtr
            temp._myHkeypathPtr=None
            self._myIsMine=True
            for logFunc in pyconfdlib._log("add-key-path-postfix-new-key-path").debug3Func():
                logFunc("ConfdHkeypath.addKeyPathPostfix() - new keyPath. myKeyPath=%s, value=%s",
                        self._myHkeypathPtr, value)
        for logFunc in pyconfdlib._log("add-key-path-postfix-after").debug4Func():
            logFunc("ConfdHkeypath.addKeyPathPostfix() - after. myKeyPath=%s, value=%s",
                    self._myHkeypathPtr, value)

    def copyFrom(self, other, len_ = -1):
        """
        Copies another ConfdHkeypath object into this object.
        if len_ is specified, only the first 'len' keys are copied.
        """
        self._free()
        if len_ < 0:
            len_ = other.getLen()
        self._myHkeypathPtr = pyconfdlib.dll.py_confd_hkeypath_dup_len(other._myHkeypathPtr, len_);
        self._myIsMine=True
        if (len_ < pyconfdlib.MAXDEPTH):
            self.getValue(len_, 0, False).CONFD_SET_NOEXISTS()

    def clone(self):
        ret=ConfdHkeypath()
        ret.copyFrom(self)
        return ret

    def isTagEqual(self, keyDepth, ns, tag):
        """
        keyDepth : int
        ns : string or int
        tag: string or int
        """
        pyconfdlib.checkTypes({ns : [int, str], tag : [int, str]})
        for logFunc in pyconfdlib._log("is-tag-equal-called").debug3Func(): logFunc("ConfdHkeypath.isTagEqual(): ns=%s, tag=%s", ns, tag)
        if isinstance(ns, str):
            ns=pyconfdlib.strToHash(ns)
        if isinstance(tag, str):
            tag=pyconfdlib.strToHash(tag)
        if (keyDepth > self.getLen()):
            for logFunc in pyconfdlib._log("is-tag-equal-too-short").debug3Func():
                logFunc("ConfdHkeypath.isTagEqual(): tag too short. self=%s, keyDepth=%s", self, keyDepth)
            return False
        searchKey = self.getLen() - keyDepth - 1
        value=self.getValue(searchKey,0)
        valueType = value.getType()
        valueNs = value.CONFD_GET_XMLTAG_NS()
        valueTag = value.CONFD_GET_XMLTAG()
        for logFunc in pyconfdlib._log("is-tag-equal-value").debug3Func(): logFunc("ConfdHkeypath.isTagEqual(): value: type=%s, ns=%s (%d), tag=%s (%d)",
                                                     valueType, pyconfdlib.hashToStr(valueNs), valueNs, pyconfdlib.hashToStr(valueTag), valueTag)
        if valueType != pyconfdlib.C_XMLTAG:
            for logFunc in pyconfdlib._log("is-tag-equal-wrong-type").debug3Func():
                logFunc("ConfdHkeypath.isTagEqual(): wrong type. self=%s, value.getType()=%s", self, valueType)
            return False
        if valueNs != ns:
            for logFunc in pyconfdlib._log("is-tag-equal-wrong-ns").debug3Func():
                logFunc("ConfdHkeypath.isTagEqual(): wrong ns. self=%s, value.ns()=%s, ns=%s",
                        self, valueNs, ns)
            return False
        if valueTag != tag:
            for logFunc in pyconfdlib._log("is-tag-equal-wrong-tag").debug3Func():
                logFunc("ConfdHkeypath.isTagEqual(): wrong tag. self=%s, value.tag=%s, tag=%s",
                        self, valueTag, tag)
            return False
        for logFunc in pyconfdlib._log("is-tag-equal-true").debug3Func():
            logFunc("ConfdHkeypath.isTagEqual(): true. self=%s, keyDepth=%s, ns=%s, tag=%s", self, keyDepth, ns, tag)
        return True

    def toString(self, includeLeadingSlash=False):
        ret=str(self)
        if (not includeLeadingSlash) and (ret[0]=='/'):
            return ret[1:]
        return ret

    def getNameSpaceId(self):
        """
        Returns the namespace id - an integer.
        Assumes that every keypath starts with an xmltag (not a key). 
        Therefore, the namespace can be extracted from the top most item
        """
        nsId=self.getValue(self.getLen()-1, 0).CONFD_GET_XMLTAG_NS()
        return nsId

    def getAt (self, position):
        """
        get the confd value at a specific position
        """
        return self.getValue(self.getLen()-position-1, 0)

    def _raiseIfNull (self):
        if not self._myHkeypathPtr:
            raise Exception("I have a NULL pointer, sorry.")

    def _free (self):
        if self._myHkeypathPtr and self._myIsMine:
            pyconfdlib.dll.py_deallocConfdHkeypath(self._myHkeypathPtr)
            self._myValuePtr = None

    def __del__ (self):
        self._free()

    def __str__ (self):
        if not self._myHkeypathPtr:
            return "(NULL)"
        buf=ctypes.create_string_buffer(pyconfdlib.kMaxStringSize)
        len_=pyconfdlib.dll.py_confd_pp_kpath(buf, ctypes.sizeof(buf), self._myHkeypathPtr)
        if len_ >= ctypes.sizeof(buf):
            buf=ctypes.create_string_buffer(len_+1)
            len_=pyconfdlib.dll.py_confd_pp_kpath(buf, ctypes.sizeof(buf), self._myHkeypathPtr)
        return buf.value[:len_]


