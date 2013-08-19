#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: michaelg
# 

#
# This file implements main high level statements of miner language
#

import common
import commands
import time
import sys
import miner_globals

NAMES = [ "SET", "ALIAS", "IMPORT", "SOURCE", "HELP", "EVAL", "HISTORY", "USAGE", "DOC", "EXIT", "PARAM"]

allVariables = []

aliasCommands = {}

importMap = {"io_targets":None, "http":None, "aggregate":None, "accumulate":None, "re":None, "runtime":None}

readRecords = 0
writeRecords = 0

class EvalStatement:
    """
    Evaluate expression
    """
    NAME = "EVAL"
    SHORT_HELP = "EVAL <expression> - evaluates expression"
    LONG_HELP = """EVAL <expression>
    Evaluates expression
"""
    def __init__(self, expression=None):
        self.myExpression = expression
    def getImports(self):
        """
        Gets import section
        """
        s = ""
        for i in importMap.keys():
            s += "import %s\n" % i
        return s

    def getGlobalVariables(self):
        """
        Gets global variables section
        """
        s = ""
        for (name, val) in allVariables:
            s += "%s = %s\n" % (name, val)
        return s

    def getCommand(self):
        s = self.getImports()
        s += self.getGlobalVariables()
        s += "def evaluate():\n"
        globalExpressions = self.myExpression.getGlobalExpressions()
        for e in globalExpressions:
            s += e.getGlobalSection()
        s += "    return %s\n" % self.myExpression.getValue() 
        s += "print evaluate()\n"
        return s

    def dump(self):
        """Dumps command to stdout"""
        print self.getCommand()

    def execute(self):
        """
        Evaluates and prints expression
        """
        s = self.getCommand()
        exec s in globals()

class DocStatement(EvalStatement):
    """
    Get documentation for python modules, classes or functions
    """
    NAME = "DOC"
    SHORT_HELP = "DOC <id> - gets documentation for id"
    LONG_HELP = """DOC <id>
DOC <module_name.id>
    Gets documentation for python modules, classes or fumctions if available
    Module should be imported before use or it should be preloaded module "runtime"
"""
    def __init__(self, docId):
        EvalStatement.__init__(self)
        self.myDocId = docId;
    def getCommand(self):
        s = self.getImports()
        s += "def getDocString():\n"
        s += """
    try:
        return %s.__doc__
    except:
        return "No documentation specified for %s"\n
""" % (self.myDocId, self.myDocId)
        s += "print getDocString()\n"
        return s

class MiningCommand(EvalStatement):
    """
    Generates and executes mining code
    """
    def __init__(self, source, stack, destination):
        """
        source      - io_command.Source
        stack       - list of Commands
        destination - io_command.Destintion
        """
        EvalStatement.__init__(self)
        self.mySource = source
        self.myDestination = destination
        self.stack = stack
        pos = 0
        for command in self.stack:
            if pos == 0:
                command.setParent(self.mySource)
            else:
                command.setParent(self.stack[pos-1])
            pos += 1

    def getCommand(self):
        """
        Get whole command
        """
        s = self.getImports()
        s += self.getGlobalVariables()
        depth = 0
        s += self.mySource.createLoader("loader")
        parentGenerator = self.mySource 
        for command in self.stack:
            if depth==0:
                # last in stack - use loader as generator
                generatorName = "loader"
            else:
                generatorName = "stack%d" % (depth-1)

            s += command.createGenerator("stack%d"%depth, generatorName)
            parentGenerator = command
            depth += 1
        s += self.myDestination.createSaver("saver", "stack%d"%(depth-1), parentGenerator.getVariableNames())
        return s

    def execute(self):
        """
        Executes command
        Returns tuple consisting of (number of read records, number of written records, processing time in seconds)
        """
        global readRecords
        global writeRecords
        readRecords = 0
        writeRecords = 0
        s = self.getCommand()
        s += "saver()\n"
        startTime = time.clock()
        exec s in globals()
        endTime = time.clock()
        return (readRecords, writeRecords, (endTime-startTime))
        

class Import:
    NAME = "IMPORT"
    SHORT_HELP = "IMPORT <import-path> - adds additional import path to execution"
    LONG_HELP = """IMPORT <import-path>
IMPORT                 - lists defined import-pathes
IMPORT - <import-path> - removes specified import-path
    Adds additional import path to mining execution
    Allows to use custom commands
"""
    @staticmethod
    def add(path):
        importedModule = None
        try:
            if path in importMap and importMap[path] is not None:
                print "Reloading module '%s'" % path
                importedModule = reload(importMap[path])
            else:
                importedModule = __import__(path)
            Import._wasModified = True
        except BaseException as e:
            print "Failed to import '%s':\n  %s " % (path, str(e)) 
            #traceback.print_exc()
        else:
            importMap[path] = importedModule

    @staticmethod
    def show():
        for i in importMap.keys():
            print i

    @staticmethod
    def remove(path):
        try:
            del importMap[path]
            Import._wasModified = True
        except:
            pass

    @staticmethod
    def checkIfWasModified():
        wasModified = Import._wasModified
        Import._wasModified = False
        return wasModified
    _wasModified = False

class Alias:
    NAME = "ALIAS"
    SHORT_HELP = "ALIAS <name> = command | ... | -  creates named alias to the chain of mining commands"
    LONG_HELP = """ALIAS <name> = command | ... |
ALIAS "description" <name> = command | ... | 
ALIAS          - lists defined aliases
ALIAS - <name> - removes specified alias
    Create named alias to the chain of mining commands
    Aliased chain cannot have any parameters and is substituted as is.
    The only way to control behavior of aliased comand is using variables
"""
    aliasDescriptions = {}
    @staticmethod
    def add(name, commandChain, description=None):
        aliasCommands[name] = commandChain
        if description:
            Alias.aliasDescriptions[name] = description
    @staticmethod
    def show():
        for name,value in aliasCommands.iteritems():
            print "%-6s - %s" % (name, Alias.aliasDescriptions.get(name, ""))
    @staticmethod
    def remove(name):
        try:
            del aliasCommands[name]
            del Alias.aliasDescriptions[name]
        except:
            pass

class Set:
    NAME = "SET"
    SHORT_HELP = "SET [<name> [= <expression>]] - sets or dumps variables"
    LONG_HELP = """SET <name> = <expression>
SET <name>   - show value of variable
SET          - show values of all variables
SET - <name> - remove variable
    SET command is used to define value of global variable
    that can be used later in mining commands.
    The expression is evaluated once before command execution
"""
    @staticmethod
    def showAll():
        for name, value in allVariables:
            print "%s = %s" % (name, value)
    @staticmethod
    def show(name):
        for name1, value1 in allVariables:
            if name == name1:
                print value1
                return
        print "undefined"
    @staticmethod
    def setValue(name, value):
        for i in range(len(allVariables)):
            # If exists, replace existing tuple (tuples are immutable, cannot simply change value of existing tuple)
            if name == allVariables[i][0]:
                allVariables[i] = (name, value)
                return
        # Add new variables at the end of the list, as a tuple (name, value)
        allVariables.append((name, value))
    @staticmethod
    def remove(name):
        for i in range(len(allVariables)):
            if name == allVariables[i][0]:
                del allVariables[i]

class SourceStatement:
    NAME = "SOURCE"
    SHORT_HELP = "SOURCE <filename> - executes miner script"
    LONG_HELP = """SOURCE <filename>
    Executes miner script specified by <filename>
"""
    @staticmethod
    def execute(fileName):
        raise common.ExecutorSourceStatement(fileName)

class History:
    NAME = "HISTORY"
    SHORT_HELP = "HISTORY [<num>] - dumps command history"
    LONG_HELP = """HISTORY [<num>]
    Dumps commans history,
    <num> specifies number of latest commands to dump - by default 10
          if <num> == 0 dumps all available history:
"""
    @staticmethod
    def execute(limit=10):
        import readline
        if limit <= 0:
            limit = 1000 # Some big number
        if readline.get_current_history_length() < limit:
            limit = readline.get_current_history_length()
        for index in range(readline.get_current_history_length()-limit, readline.get_current_history_length()):
            s = readline.get_history_item(index+1)
            print " %d: %s" % (index+1, s)

class ExitStatement:
    NAME = "EXIT"
    SHORT_HELP = "EXIT [<status>] - exits miner"
    LONG_HELP = """EXIT [<status>]
    Exits miner,
    <status> specifies exit status code
"""
    @staticmethod
    def execute(status=0):
        sys.exit(status)

class Usage:
    NAME = "USAGE"
    SHORT_HELP = 'USAGE "script description" name="description" [name2=".."] *=".." >=".."'
    LONG_HELP = """USAGE "script description" name="description" [name2="description"] *="description" >="description"
USAGE command validates that all required script parameters were provided otherwise it prints
    usage and exits.
    []  - means optional parameter
    * - positional parameters, usually used for input files (can be optional), accessed by $* or $1, $2
    >  - output parameter, can be optional, specified in script by -o <>, accessed by $>
"""
    @staticmethod
    def execute(scriptDescription, parameterList):
        if miner_globals.printUsage:
            Usage.printUsageAndExit(scriptDescription, parameterList)
        for p in parameterList:
            if "isOptional" not in p:
                if p["name"] == "*" and "1" not in miner_globals.scriptParameters:
                    Usage.printUsageAndExit(scriptDescription, parameterList)
                elif p["name"] not in miner_globals.scriptParameters:
                    Usage.printUsageAndExit(scriptDescription, parameterList)

    @staticmethod
    def printUsageAndExit(scriptDescription, parameterList):
        commandParams = []
        for p in parameterList:
            if p["name"].isdigit():
                commandParams.append("arg%s" % p["name"])
            elif p["name"] == "*":
                commandParams.append("args...")
            elif p["name"] == ">":
                commandParams.append("-o ..")
            else:
                commandParams.append("%s=.." % p["name"])
            if "isOptional" in p:
                commandParams[-1] = "[" + commandParams[-1] + "]"
        print "Usage: %s" % " ".join(commandParams)
        print scriptDescription
        for p in parameterList:
            if p["name"].isdigit():
                name = "arg%s" % p["name"]
            elif p["name"] == "*":
                name = "args"
            elif p["name"] == ">":
                name = "-o"
            else:
                name = p["name"]
            print "  %-4s - %s" % (name, p["description"])
        sys.exit(1)

class ParamStatement:
    NAME = "PARAM"
    SHORT_HELP = 'PARAM name=value'
    LONG_HELP = """PARAM name=value
PARAM name?=value
    Sets global parameter value.
    If '?=' form is used then value is set only if it is not already defined
"""
    @staticmethod
    def setValue(id, value):
        miner_globals.scriptParameters[id] = value
    @staticmethod
    def setValueIfNotDefined(id, value):
        if id not in miner_globals.scriptParameters:
            miner_globals.scriptParameters[id] = value

class Help:
    NAME = "HELP"
    SHORT_HELP = "HELP [command] - provides help information about command"
    LONG_HELP = """HELP [command]
    Provides help information about command(s)
"""
    @staticmethod
    def printHelp(commandName=None):
        if not commandName:
            print "Format of mining command is:"
            print "READ <filename> | comand1 | command2 ... | WRITE filename/STDOUT"
            print "Where minning command is one of:"
            for commandClass in commands.commandClasses:
                print "    %s" % commandClass.SHORT_HELP
            print "\nAdditional commands are:"
            for commandClass in statementClasses:
                print "    %s" % commandClass.SHORT_HELP
        else:
            for commandClass in commands.commandClasses + statementClasses:
                if commandName == commandClass.NAME:
                    print commandClass.LONG_HELP
                    return
            countMatches = 0
            for commandClass in commands.commandClasses + statementClasses:
                if  commandClass.NAME.startswith(commandName):
                    print "    %s" % commandClass.SHORT_HELP
                    countMatches += 1
            if countMatches == 0:
                print "Unknown command %s" % commandName


statementClasses = [Import, Alias, Set, SourceStatement, Help, EvalStatement, History, Usage, DocStatement, ExitStatement, ParamStatement]


