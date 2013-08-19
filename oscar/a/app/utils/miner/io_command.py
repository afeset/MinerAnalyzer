#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: michaelg
# 

#
# This file contains io command
# First input file is read once before mining command execution to
# validate its existance, check its correctness and detemine record variables
# In general file format is determined from the extension:
#   .qbl - coals records
#   .csv - coma separated values with variables names in the first line
#   .pic - pickle serialization

from common import *
import io_targets
import os
import glob
import re

SOURCE_COMMAND_NAMES = ["READ", "ITERATE"]

class Source(GeneratorBase):
    def __init__(self, fileNamePatterns, sourceType=None, streamVars=None):
        self.myStreamVars = streamVars
        fileNames = []
        for pattern in fileNamePatterns:
            if re.search(r'[\[\]?*]', pattern):
                fileNames.extend(sorted(glob.glob(os.path.expanduser(pattern))))
            else:
                fileNames.append(os.path.expanduser(pattern))
        if not fileNames:
            raise NoFilesInPattern(fileNamePatterns)
        for fileName in fileNames:
            if not os.path.isfile(fileName):
                raise FileDoesntExist(fileName)

        if not sourceType:
            ext = os.path.splitext(fileNames[0])[1]
            self.mySourceType = io_targets.getTypeByExtension(ext)
            if not self.mySourceType:
                raise UnknownInputFileType(fileNames[0])
        else:
            self.mySourceType = sourceType
        self.myFileNames = fileNames
        try:
            source = io_targets.iStreamFactory(self.mySourceType, self.myFileNames[0], self.myStreamVars)
        except:
            raise FailedToOpenFile(self.myFileNames[0], self.mySourceType)
        self.myVars = source.getVariableNames()
        source.close()

    def getVariableNames(self):
        return self.myVars

    def createLoader(self, loaderName):
        sourceName = io_targets.getInputStreamClass(self.mySourceType)
        if not sourceName:
            raise UnknownInputFileType(self.myFileNames[0])

        fileNames = ['r"%s"'%f for f in self.myFileNames]

        s = """
def %s():
    global readRecords
    for fileName in [%s]:
        istream = %s(fileName %s)
        print "-- Mining %%s ..." %% fileName
        for record in istream:
            readRecords += 1
            yield record
        istream.close()
""" %   (loaderName, ", ".join(fileNames), sourceName, "" if not self.myStreamVars or not len(self.myStreamVars) else (", **%s" % self.myStreamVars))
        return s

class IteratorStream(GeneratorBase):
    def __init__(self, streamVars, expression):
        self.myVars = streamVars
        self.myExpressionStr = expression

    def getVariableNames(self):
        return self.myVars

    def createLoader(self, loaderName):
        if len(self.myVars)==1:
            vars = self.myVars[0]
            yieldVars = "(%s,)" % vars
        else:
            vars = "(%s)" % ",".join(self.myVars)
            yieldVars  = vars
        recordStr = []
        s = """
def %s():
    global readRecords
    print "-- Mining %s ..."
    for %s in %s:
        readRecords += 1
        yield %s
""" %   (loaderName, self.myExpressionStr, vars, self.myExpressionStr, yieldVars)
        return s

DESTINATION_COMMAND_NAMES = ["WRITE", "STDOUT"]

class Destination:
    def __init__(self, fileName, destinationType=None, streamVars=None):
        self.myStreamVars = streamVars
        if not destinationType:
            if fileName == "stdout":
                self.myDestinationType = "stdout"
            else:
                ext = os.path.splitext(fileName)[1]
                self.myDestinationType = io_targets.getTypeByExtension(ext)
                if not self.myDestinationType:
                    raise UnknownOutputFileType(fileName)
        else:
            self.myDestinationType = destinationType
        self.myFileName   = os.path.expanduser(fileName)
    def getConstructor(self, variableNames):
        oStreamClass = io_targets.getOutputStreamClass(self.myDestinationType)
        varListStr = ", ".join(('"%s"'%e) for e in variableNames)
        return """%s(r"%s", [%s] %s)""" % (oStreamClass, self.myFileName, varListStr, "" if not self.myStreamVars or not len(self.myStreamVars) else (", **%s" % self.myStreamVars))
    def createSaver(self, saverName, generatorName, variableNames):
        s = """
def %s():
    print "-- Destination %%s" %% r"%s"
    ostream = %s
    global writeRecords
    for record in %s():
        writeRecords += 1
        ostream.save(record)
    ostream.close()
""" %   (saverName, self.myFileName, self.getConstructor(variableNames), generatorName)
        return s

