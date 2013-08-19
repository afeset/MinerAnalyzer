#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: michaelg
# 

#
# This file implements completion logic
# and runInteractive() function for interactive mode
#
# on windows platform completion logic requires manual installation of pyreadline package
#

import executor
import commands
import statements
import io_command
import atexit
import glob
import os
import sys
import traceback
import miner_version
import miner_globals

pathToScript = os.path.dirname(sys.argv[0])
HISTORY_FILE_NAME = os.path.expanduser(os.path.join("~",".coal-mining-history"))

if sys.platform.startswith("win") or miner_globals.runsUnderPypy:
    # on windows platform or under pypy
    import readline_replacement as readline
    sys.modules['readline'] = readline
    import pyreadline.rlmain
    readline.rl.read_inputrc(os.path.join(pathToScript, "pyreadlineconfig.py"))
    if miner_globals.pyreadlineLogFile:
        import pyreadline.logger
        pyreadline.logger.start_file_log(miner_globals.pyreadlineLogFile)
else:
    import readline
    readline.read_init_file(os.path.join(pathToScript, "readline.ini"))
    readline.set_completer_delims(" \t\n\"\\/-+*^%:~!%'`@$><=,;|&{}()?:[]")

readline.parse_and_bind("tab: complete")

try:
    readline.read_history_file(HISTORY_FILE_NAME)
except IOError:
    pass

atexit.register(readline.write_history_file, HISTORY_FILE_NAME)

# There are number different completion states:
# 1. if we are inside string - completion is disabled
# 2. if it is first command - Treat it as statement or "READ"
# 3. If first word after PIPE -> command or "WRITE"
# 4. If after HELP can by any
# 5. If after READ or write -> FILE
# 6. Otherwise -> symbols or variables

COMPLETE_NONE = 0
COMPLETE_STATEMENTS = 1
COMPLETE_COMMANDS = 2
COMPLETE_FOR_HELP = 3
COMPLETE_SYMBOLS = 4
COMPLETE_FILE = 5
def getCompletionState():
    """
    Determine completion state according to the current readline global state
    """
    line = readline.get_line_buffer()
    beginIndex = readline.get_begidx()
    endIndex = readline.get_endidx()
    # check if we are in string (only double quotes are allowed)
    inString = False
    position = 0
    countBackspaces = 0
    while position<beginIndex:
        if line[position] == '"' and countBackspaces%2==0:
            inString = not inString
            countBackspaces = 0
        elif inString and line[position] == '\\':
            countBackspaces += 1
        else:
            countBackspaces = 0
        position += 1
    if inString:
        return COMPLETE_NONE
    start = line.rfind("|", 0, endIndex)+1
    if start == 0:
        firstCommand = True
    else:
        firstCommand = False
    while start < beginIndex and line[start].isspace():
        start += 1
    if start == beginIndex:
        # We are on the first word
        if firstCommand:
            return COMPLETE_STATEMENTS
        else:
            return COMPLETE_COMMANDS

    position = start
    while line[position].isalpha() and position < beginIndex:
        position += 1

    # check if first command in the load or save then we want to complete files
    command = line[start:position]
    if command == "READ" or command == "WRITE" or command == "SOURCE":
        return COMPLETE_FILE
    if command == "HELP":
        return COMPLETE_FOR_HELP
    if command == "ALIAS":
        return COMPLETE_COMMANDS

    return COMPLETE_SYMBOLS


class FileCompleter:
    """
    Implements file completer
    """
    def __init__(self):
        self.completions = []
    def getCompletions(self, text):
        # This function is called once when TAB is preseed
        line = readline.get_line_buffer()
        endIndex = readline.get_endidx()
        # get the filename to complete
        position = readline.get_begidx()
        while position > 0:
            position -= 1
            if line[position] in u' \t\n':
                position += 1
                break
        text = line[position:endIndex]
        text = os.path.expanduser(text)
        completions = map(os.path.basename, glob.glob(text + '*'))
        self.completions = []
        fileDir = os.path.dirname(text)
        basenameText = os.path.basename(text)
        # mark all directories with slash at the end
        for f in completions:
            if os.path.isdir(os.path.join(fileDir,f)):
                self.completions.append(f + os.sep)
            else:
                self.completions.append(f)

        if len(self.completions) == 0:
            self.completions = []
        elif len(self.completions) == 1:
            # if there is only one completion - insert left text as is
            readline.insert_text(self.completions[0][len(basenameText):])
            # if completion is a file add space at the end
            if not self.completions[0].endswith(os.path.sep):
                readline.insert_text(" ")
            self.completions = []
        else:
            # Try to find common prefix
            commonPrefix = os.path.commonprefix(completions)
            if len(os.path.join(fileDir,commonPrefix)) > len(text):
                # add common suffix
                substruct = 0 if not fileDir else (len(fileDir)+1)
                readline.insert_text(commonPrefix[len(text) - substruct:])
                self.completions = []
            else:
                # add empty string to avoid auto completion
                self.completions.append(" ")

    def complete(self, text, state):
        if state == 0:
            self.getCompletions(text)
        return self.completions[state]

from include.a.line.report.coal_report_pb2 import CoalRecordGpb
from infra.log.msg_data_pb2 import MsgDataGpb
from line.va.transaction_pb2 import TransactionSummaryGpb
import http
import rlcompleter
#symbolCompleter = rlcompleter.Completer(symbols).complete
class CompleterWrap(rlcompleter.Completer):
    """
    Complete symbols and defined variables
    """
    def __init__(self):
        self.symbols = {}
        # Create dummy objects for completion
        self.symbols['coal'] = CoalRecordGpb()
        self.symbols['msgData'] = MsgDataGpb()
        self.symbols['transaction'] = TransactionSummaryGpb()
        self.symbols['request'] = http.HttpRequest("GET / HTTP/1.1\r\n\r\n")
        self.symbols['response'] = http.HttpResponse("HTTP/1.1 200 OK\r\n\r\n")
        self.symbols['uri'] = http.Uri("http://host:80/path?var=value")
        runtimeNS = __import__('runtime', globals())
        self.symbols['runtime'] = runtimeNS
        for moduleName, moduleHandle in statements.importMap.iteritems():
            if moduleHandle:
                self.symbols[moduleName] = moduleHandle
        rlcompleter.Completer.__init__(self, self.symbols)
        self.noMore = False
        self.parentState = 0
        self.matchedVars = []

    def complete(self, text, state):
        if state == 0:
            self.noMore = False
            self.parentState = 0
            # DISTINCT and SELECT are hack to support FOR command
            # statements is a list of (name, value) tuples, we need only the names
            self.matchedVars = filter(lambda var: var.startswith(text), map(lambda x: x[0], statements.allVariables) +
                                       ["True", "False", "None", "DISTINCT", "SELECT"])
        if state<len(self.matchedVars):
            return self.matchedVars[state]
        while not self.noMore:
            completion = rlcompleter.Completer.complete(self, text, self.parentState)
            if not completion:
                self.noMore = True
            else:
                self.parentState += 1
                if completion.find("._") == -1:
                    return completion
        return None

theSymbolCompleter = CompleterWrap()

def symbolCompleter(text, state):
    try:
        return theSymbolCompleter.complete(text, state)
    except:
        return None

fileCompleter = FileCompleter().complete

statementsForCompletion = statements.NAMES + io_command.SOURCE_COMMAND_NAMES
commandsForCompletion = commands.NAMES + io_command.DESTINATION_COMMAND_NAMES
helpTopicsForCompletion = statementsForCompletion + commandsForCompletion

def completeFromList(text, state, itemsList):
    return filter(lambda c: c.startswith(text), itemsList)[state]

def myCompleterFunc(text, state):
    completionState = getCompletionState()
    if completionState == COMPLETE_FILE:
        return fileCompleter(text, state)
    elif completionState == COMPLETE_SYMBOLS:
        return symbolCompleter(text, state)
    elif completionState == COMPLETE_COMMANDS:
        return completeFromList(text, state, commandsForCompletion + statements.aliasCommands.keys())
    elif completionState == COMPLETE_STATEMENTS:
        return completeFromList(text, state, statementsForCompletion)
    elif completionState == COMPLETE_FOR_HELP:
        return completeFromList(text, state, helpTopicsForCompletion)
    else:
        return None

readline.set_completer(myCompleterFunc)

def runInteractive():
    """
    Main function for interactive mode
    """
    print "------------- Welcome to the Miner %s ----------------" % miner_version.version
    print "You can run HELP command anytime to get more information."
    print "Press TAB key for context base completion"
    print "    - F1  key to get context base HELP"
    print "    - Ctrl-H to get list of keyboard bindings"
    print "    - Ctrl-D to exit"
    while True:
        s = ""
        try:
            s = raw_input(">>> ")
        except KeyboardInterrupt:
            print
            continue
        except EOFError:
            break
        if not s: continue
        executor.execute(s)
        if statements.Import.checkIfWasModified():
            global theSymbolCompleter
            theSymbolCompleter = CompleterWrap()

    print "\nGoodbye"

