# 
# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: nirs

import os     
import logging

import a.infra.format.json
import a.sys.mng.file
import a.sys.std_process.micro_captain

G_NAME_MODULE_APP_MNG_FILE = "mng-file"
G_NAME_GROUP_APP_MNG_FILE_DEFAULT = "default"
G_NAME_GROUP_APP_MNG_FILE_ARG_PARSER = "arg-parser"

def printError (msg):
    print "Error:", msg

class FileOperationsApp(a.sys.std_process.micro_captain.MicroAppInterface):
    INIT_PARAM_FILES_DIR_ENV_VAR_NAME = "QB_FILE_OPERARTIONS_INIT_PARAM_FILES_DIR"
    #init params handling
    INIT_PARAM_FILE_NAME = "file-operations-init-params.json"
    #kept fields
    INIT_PARAM_DATA_ROOT_DIR="root-dir"    

    def __init__ (self):
        pass      

    def initLogger(self, logger):
        self._log = logger.createLogger(G_NAME_MODULE_APP_MNG_FILE, G_NAME_GROUP_APP_MNG_FILE_DEFAULT)

    def initFromParamFile(self, initParamFilesDirName):
        data = a.infra.format.json.readFromFile(self._log, 
                                                os.path.join(initParamFilesDirName, self.INIT_PARAM_FILE_NAME))
        self.initFromDictionary(data)

    def initFromDictionary(self, data):
        self.init(data[self.INIT_PARAM_DATA_ROOT_DIR])

    def init (self, rootDir):
        self._rootDir = rootDir
        self._log("root-dir").debug3("root dir is '%s'", self._rootDir)
        self._fileOperations = a.sys.mng.file.FileOperations(self._log, rootDir)


    def addToOptParser(self, optParser):
        optParser.add_option("-c", "--command", type="string", action="store", dest="cmd", help="command to run.")

    def parseCmdLine(self, options, args):
        if not options.cmd:
            self._log("missing-cmd").error("command option is missing")
            a.infra.process.processFatal("Missing command")             
        self._cmd =  options.cmd              
        self._argParser = self.ArgsParser(self._log)
        self._args = args

    def run (self):
        if self._cmd == "copy": 
            result = self._doCopy()
        elif self._cmd == "rename":
            result = self._doRename()
        elif self._cmd == "delete":
            result = self._doDelete()
        elif self._cmd == "mkdir":
            result = self._doMkdir()
        elif self._cmd == "rmdir":
            result = self._doRmdir()
        elif self._cmd == "dir":
            result = self._doDir()
        elif self._cmd == "show-filesystem":
            result = self._doShowFileSystem()
        else:
            printError("invalid command")
            return 1

        if result is None:
            return 1

        #printing the data even if there are errors. important for "dir" for example
        output = result.getPrintableOutput()
        if output:
            print output

        if not result.isOk():
            errors = result.getErrors()
            for error in errors:
                printError(error)
            return 1

        return 0


    def processName (self):
        #not set, will get the data from init param file
        return None

    def changedEarlyLogLevel (self):        
        return logging.WARN

    @classmethod
    def s_getInitParamsFilesDirEnvVarName (cls):        
        return cls.INIT_PARAM_FILES_DIR_ENV_VAR_NAME

    @classmethod
    def s_createInitParamFiles(cls, dbglog, initParamFilesDir, dictionary):        
        a.infra.format.json.writeToFile(dbglog, dictionary, os.path.join(initParamFilesDir, cls.INIT_PARAM_FILE_NAME), indent=4)


    #business logic

    class ArgsParser:
        def __init__ (self, logger):
            self._log = logger.createLoggerSameModule(G_NAME_GROUP_APP_MNG_FILE_ARG_PARSER)
            self._argsDict={}
    
        def init (self, args, knownOptions, knownFlags):
            self._log("args").debug3("%s",args)
            i=1#skipping the script name
            numOfArgs = len(args)
            #running according to the args order to avoid issues caused by a value that equals to a option
            while i<numOfArgs:
                if args[i] in knownOptions:
                    if (i+1)<numOfArgs:
                        self._argsDict[args[i]] = args[i+1]
                        i = i+2
                    else:
                        self._log("missing-option-value").error("option '%s' value is missing", args[i])
                        printError("option '%s' value is missing"%args[i])
                        return False
    
                elif args[i] in knownFlags:
                    self._argsDict[args[i]] = True
                    if (i+1)<numOfArgs and args[i+1]=="__LEAF":#running from yang                        
                        i = i+2
                    else:
                        i = i+1 #running from cli spec
    
                else:
                    self._log("invalid-option").error("option '%s' is invalid", args[i])
                    printError("option '%s' is invalid"%args[i])
                    return False
    
            #adding values to missing flags
            for flag in knownFlags:
                if not flag in self._argsDict:
                    self._argsDict[flag]=False
    
            return True
    
        def popArg (self, field):
            if not field in self._argsDict:        
                self._log("pop-no-field").error("command missing param '%s'", field)
                printError("invalid syntax - missing '%s'"%field)
                return (False, None)
            return (True, self._argsDict.pop(field))

    def _doCopy(self): 
        OPT_SOURCE =  "source"     
        OPT_DEST =  "destination"   

        if not self._argParser.init(self._args, [OPT_SOURCE, OPT_DEST], []):
            return None  
        (found, source) = self._argParser.popArg(OPT_SOURCE)
        if not found:
            return None

        (found, destination) = self._argParser.popArg(OPT_DEST)
        if not found:
            return None

        self._log("copy").info("copy '%s' to '%s'", source, destination)
        result = self._fileOperations.copy(source, destination)
        return result

    def _doRename(self): 
        OPT_SOURCE =  "source"     
        OPT_DEST =  "destination"   
        if not self._argParser.init(self._args, [OPT_SOURCE, OPT_DEST], []):
            return None

        (found, source) = self._argParser.popArg(OPT_SOURCE)
        if not found:
            return None

        (found, destination) = self._argParser.popArg(OPT_DEST)
        if not found:
            return None

        self._log("rename").info("copy '%s' to '%s'", source, destination)
        result = self._fileOperations.move(source, destination)
        return result

    def _doDelete(self): 
        OPT_PATH =  "path"     
        FLAG_DIR =  "allow-dir"   
        if not self._argParser.init(self._args, [OPT_PATH], [FLAG_DIR]):
            return None

        (found, path) = self._argParser.popArg(OPT_PATH)
        if not found:
            return None

        (found, allowDir) = self._argParser.popArg(FLAG_DIR)
        if not found:
            return None

        self._log("delete").info("delete '%s'", path)
        result = self._fileOperations.delete(path, allowDir)
  
        return result

    def _doMkdir(self): 
        OPT_DIR =  "directory"     
        if not self._argParser.init(self._args, [OPT_DIR], []):
            return None

        (found, directory) = self._argParser.popArg(OPT_DIR)
        if not found:
            return None

        self._log("make-dir").info("creating dir '%s'", directory)
        result = self._fileOperations.makeDir(directory)
        return result

    def _doRmdir(self): 
        OPT_DIR =  "directory"     
        if not self._argParser.init(self._args, [OPT_DIR], []):
            return None

        (found, directory) = self._argParser.popArg(OPT_DIR)
        if not found:
            return None

        self._log("remove-dir").info("removing dir '%s'", directory)
        result = self._fileOperations.deleteEmptyDir(directory)
        return result

    def _doDir(self): 
        OPT_PATH =  "path"     
        FLAG_SHOW_DIRS =  "show-directories"   
        FLAG_SHOW_DIRS_SIZE =  "show-directories-size"   
        FLAG_RECURSIVE =  "recursive" 
        if not self._argParser.init(self._args, [OPT_PATH], [FLAG_SHOW_DIRS, FLAG_SHOW_DIRS_SIZE, FLAG_RECURSIVE]):
            return None

        (found, path) = self._argParser.popArg(OPT_PATH)
        if not found:
            return None

        (found, showDirs) = self._argParser.popArg(FLAG_SHOW_DIRS)
        if not found:
            return None

        (found, showDirsSize) = self._argParser.popArg(FLAG_SHOW_DIRS_SIZE)
        if not found:
            return None

        (found, recursive) = self._argParser.popArg(FLAG_RECURSIVE)
        if not found:
            return None

        result = self._fileOperations.dir(path, showDirs, showDirsSize, recursive)
        return result

    def _doShowFileSystem(self): 
        if not self._argParser.init(self._args, [], []):
            return None

        result = self._fileOperations.showFileSystem()
        return result



