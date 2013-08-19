#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: michaelg
# 

#
# This file provides implementation of main execute command function
#

import compiler
import statements
import a.infra.gpb.chain_exceptions
import traceback
import common
import sys
import re
import string
import loggers
import os
import miner_globals

# debug mode if enable parser and compilation log files are created
def setDebugMode(debugMode):
    if debugMode:
        loggers.setDebugMode()
    miner_globals.debugMode = debugMode

class ParameterSubstitutor(string.Template):
    idpattern = "[0-9>*]|[a-zA-Z][_a-zA-Z0-9]*"
    def __init__(self, command):
        string.Template.__init__(self, command)

    def update(self):
        return self.safe_substitute(miner_globals.scriptParameters)

def createAliases(aliases):
    if not aliases:
        return
    for a in aliases:
        execute("ALIAS %s" % a, verbose=False)

def createVariables(variables):
    if not variables:
        return
    for v in variables:
        execute("SET %s" % v, verbose=False)

def createImports(imports):
    if not imports:
        return
    for i in imports:
        execute("IMPORT %s" % i, verbose=False)

def executeCommands(commands, verbose=True):
    if not commands:
        return
    for c in commands:
        execute(c, verbose)

_gScriptPath = []

def setScriptPath(scriptPath):
    global _gScriptPath
    _gScriptPath = _gScriptPath

def executeScript(scriptFileName):
    scriptFH = None
    try:
        if os.path.exists(scriptFileName):
            scriptFH = open(scriptFileName, "r")
        else:
            for fileName in [os.path.join(e,scriptFileName) for e in _gScriptPath]:
                if os.path.exists(fileName):
                    scriptFH = open(fileName, "r")
    except:
        print "Failed to open %s" % scriptFileName
        traceback.print_exc()
        return
    if not scriptFH:
        print "Script %s was not found" % scriptFileName
        return

    while True:
        line = scriptFH.readline()
        if not line:
            break
        line = line.rstrip('\n')
        if line == "": continue
        # check if span to multiple lines
        while line[-1] == "\\" or line[-1] == "|":
            contLine = scriptFH.readline()
            contLine = contLine.rstrip('\n')
            if line[-1] == "\\":
                line = line[0:-1]
            line += contLine

        execute(line)
    scriptFH.close()

def printDoc(id):
    import statements
    try:
        stmt = statements.DocStatement(id)
        stmt.execute()
    except:
        print "Invalid id - " + id
    
def printHelp(id):
    import statements
    statements.Help.printHelp(id)

def execute(command, verbose=True):
    '''
    Main execute function
    '''
    if not command:
        return
    command = command.strip()
    # pound is miner's comment as well
    if command=="" or command[0] =="#":
        return
    if '$' in command:
        # substitute parameters
        substitutor = ParameterSubstitutor(command)
        command = substitutor.update()

    result = None
    try:
        result = compiler.parseCommand(command)
        if not result:
            return
        try:
            if isinstance(result, statements.MiningCommand):
                (coals, diamonds, deltaTime) = result.execute()
                if deltaTime<0.001:
                    rate=0
                else:
                    rate=coals/deltaTime
                print "Processed %d coals into %d diamonds for %.3f seconds, %d coals/sec." % (coals, diamonds, deltaTime, rate)
            else:
                result.execute()
        except KeyboardInterrupt:
            print "Execution aborted"
    except common.ExecutorSourceStatement as source:
        executeScript(source.getFileName())
    except common.CompilerSyntaxError as err:
        offset = err.offset
        if offset < 0:
            offset = len(command)
        startVisualOffset = int(offset/60) * 60
        print "Syntax Error at:"
        print command[startVisualOffset:startVisualOffset+60]
        print "-"*(offset-startVisualOffset) + "^"
    except common.InvalidInputFiles as err:
        print "Invalid input file(s): %s" % str(err)
    except IOError as err:
        print str(err)
    except a.infra.gpb.chain_exceptions.NotCompleteMessageException as err:
        print "Invalid COAL record file format, %s" % str(err)
    except SystemExit as e:
        sys.exit(e)
    except:
        print "Exception occured"
        print "================="
        if result:
            print "Prepared code:"
            result.dump()
        traceback.print_exc()
        print "-----------------"

