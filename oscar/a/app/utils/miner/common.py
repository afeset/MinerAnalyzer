#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: michaelg
# 

#
# This file contains definition of basic Generator interface
# And all Exceptions
#

class GeneratorBase:
    def __init__(self):
        self.myParent = None
    def setParent(self, parent):
        self.myParent = parent
    def getVariableNames(self):
        raise NotImplementedError

# Exception types
class InvalidInputFiles(Exception):
    pass

class NoFilesInPattern(InvalidInputFiles):
    def __init__(self, fileNamePatterns):
        self.myFileNamePatterns = fileNamePatterns
    def __str__(self):
        return "Pattern(s) '%s' doesn't match any files" % " ".join(self.myFileNamePatterns)

class UnknownInputFileType(InvalidInputFiles):
    def __init__(self, fileName):
        self.myFileName = fileName
    def __str__(self):
        return "Unsupported type of input file '%s'" % self.myFileName

class FileDoesntExist(InvalidInputFiles):
    def __init__(self, fileName):
        self.myFileName = fileName
    def __str__(self):
        return "File '%s' doesn't exist or is not a file" % self.myFileName


class FailedToOpenFile(InvalidInputFiles):
    def __init__(self, fileName, fileType):
        self.myFileName = fileName
        self.myFileType = fileType
    def __str__(self):
        return "Failed to open %s file '%s'" % (self.myFileType, self.myFileName)

class UnknownOutputFileType(Exception):
    def __init__(self, fileName):
        self.myFileName = fileName
    def __str__(self):
        return "Unsupported type of output file '%s'" % self.myFileName


class CompilerSyntaxError(Exception):
    def __init__(self, offset):
        self.offset = offset
    def __str__(self):
        return "Syntax error at position %d" % self.offset

class ExecutorNotification(Exception):
    """This is not exception but rather a method to notify executor about some valid user input"""
    pass

class ExecutorSourceStatement(ExecutorNotification):
    def __init__(self, fileName):
        self.myFileName = fileName
    def getFileName(self):
        return self.myFileName
    def __str__(self):
        return "SOURCE %s" % self.myFileName

