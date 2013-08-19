# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities 
# without explicit written permission from Qwilt.
# 
# Author: shmulika
#


import re
from collections import namedtuple

G_NAME_GROUP_GRUB_CONF_GENERATOR = "grub-conf-generator"

class GrubConfGenerator:
    GRUB_DEFAULT_COMMENT_HEADER = "# This file was created by the GrubConfGenerator utility class"
    GRUB_DEFAULT_DEFAULT = 0
    GRUB_DEFAULT_TIMEOUT = 15


    def __init__ (self, logger):
        self._log = logger.createLoggerSameModule(G_NAME_GROUP_GRUB_CONF_GENERATOR)        

        self._bootOptions = []
        self._commentHeader = ""
        self._default = self.GRUB_DEFAULT_DEFAULT
        self._timeout = self.GRUB_DEFAULT_TIMEOUT


    def load (self, filename):
        self._log("load").info("loading grub.conf file=%s", filename)
        text = self._readTextFromFile(filename)
        self._log("load").info("loaded grub.conf file=%s", filename)
        self.loadFromText(text)


    def loadFromText (self, text):
        self._log("load-from-text").info("loading text of grub.conf, text=%s", text)
        self._commentHeader = self._getCommentHeaderFromText(text)

        default = self._getDefaultFromText(text)
        if default is not None:
            self._default = default

        timeout = self._getTimeoutFromText(text)
        if timeout is not None:
            self._timeout = timeout

        self._bootOptions = self._getBootOptionsFromText(text)


    def save (self, filename):
        text = self._generate()
        self._log("saev").info("savnig grub.conf file=%s, text=%s", filename, text)
        self._writeTextToFile(filename, text)        


    def addBootOptionsFromFile (self, filename):        
        self.addBootOptions(self._readTextFromFile(filename))


    def addBootOptions (self, text):
        self._log("add-boot-options").info("adding boot options='%s'", text)
        self._bootOptions.extend(self._getBootOptionsFromText(text))

    
    def getBootOptions (self):
        return [(index, bootOption.getTitle(), bootOption.getText()) for index, bootOption in zip(xrange(len(self._bootOptions)), self._bootOptions)]


    def setDefaultBootOption (self, index):
        self._log("set-default-boot-option").info("set default=%s", index)
        self._default = str(index)


    def getDefaultBootOption (self):
        return int(self._default)


    def setTimeout (self, timeoutSeconds):
        self._log("set-timeout").info("set timeout=%s", timeoutSeconds)
        self._timeout = str(timeoutSeconds)


    def getTimeout (self):
        return int(self._timeout)


    def setCommentHeader (self, commentHeader):
        self._log("set-timeout").info("set comment-header=%s", commentHeader)
        lines = commentHeader.splitlines()
        commentHeaderLines = []
        for line in lines:
            if line[0] != "#":
                commentHeaderLines.append("#" + line)
            else:
                commentHeaderLines.append(line)

        commentHeader = "\n".join(commentHeaderLines)
        self._commentHeader = commentHeader


    def getCommentHeader (self):
        return self._commentHeader


    def _getDefaultFromText (self, text):
        return self._getFieldFromText(text, "default")


    def _getTimeoutFromText (self, text):
        return self._getFieldFromText(text, "timeout")


    def _getBootOptionsFromText (self, text):
        bootOptions = []
        currentBootOptionLines = None

        lines = text.splitlines()
        for line in lines:
            matches = re.search("^\s*title\s(?P<title>.*)$", line)
            try:
                title = matches.group("title")
                self._log("get-boot-options-from-text").info("found new title line = '%s', title = '%s'", line, title)
                
                if currentBootOptionLines is not None:
                    bootOptions.append(BootOption(currentBootOptionLines[0], "\n".join(currentBootOptionLines)))
                
                currentBootOptionLines = [line]
            except:
                if currentBootOptionLines is not None:
                    currentBootOptionLines.append(line)

        if currentBootOptionLines is not None:
            text = "\n".join(currentBootOptionLines) + "\n"            
            bootOptions.append(BootOption(currentBootOptionLines[0], text))

        return bootOptions



    def _getCommentHeaderFromText (self, text):
        lines = text.splitlines()
        commentHeaderLines = []

        for line in lines:
            if len(line) > 0 and line[0] == "#":
                commentHeaderLines.append(line)
            else:
                break

        return "\n".join(commentHeaderLines)


    def _getFieldFromText (self, text, field):
        lines = text.splitlines()
        
        for line in lines:
            matches = re.search("^\s*%s\s*=\s*(?P<value>.*)\s*$" % field, line)
            try:
                value = matches.group("value")
                self._log("get-field-from-text").info("got %s=%s, from line='%s'", field, value, line)
                return value
            except:
                pass

        self._log("get-field-from-text").info("couldn't find %s value in text=%s", field, text)
        return None
    
    def _readTextFromFile (self, filename):
        with open(filename, 'r') as fileInput:
            text = fileInput.read()

        return text

    def _writeTextToFile (self, filename, text):
        with open(filename, 'w') as fileOutput:
            fileOutput.write(text)


    def _generate (self):
        defaultLine = "default=%s" % (self._default)
        timeoutLine = "timeout=%s" % (self._timeout)
        bootOptionsLines = "\n".join([bootOption.getText() for bootOption in self._bootOptions])
        return "\n".join([self._commentHeader, defaultLine, timeoutLine, bootOptionsLines])


class BootOption:
    def __init__ (self, title, text):
        self._title = title
        self._text  = text

    def getTitle (self):
        return self._title

    def getText (self):
        return self._text

    def __str__ (self):
        return "(BootOption: title=%s, text=%s)" % (self._title, self._text)


