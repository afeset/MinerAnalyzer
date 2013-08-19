#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

import glob
import os
import sys
import re
import shutil
import stat
import time
import traceback
import a.infra.file.utils
import a.infra.network.utils

G_NAME_MODULE_SYS_MNG_FILE = "mng-file"
G_NAME_GROUP_SYS_MNG_FILE_GENERAL = "general"

class ReturnObject:
    class Field:
        def __init__ (self, key, data):
            self._key = key
            self._data = data

        def yangString (self):
            return "%s \"%s\""%(str(self._key),str(self._data))

    class FewFields:
        def __init__ (self):
            self._data = []

        def yangString (self):
            outStr = ""            
            for child in self._data:
                outStr = outStr + " " + child.yangString()
            return outStr

        def addChild (self, child):
            self._data.append(child)

        def isEmpty (self):
            return self._data == []

    class Container:
        def __init__ (self, key):
            self._key = key
            self._data = []

        def yangString (self):
            outStr = "%s __BEGIN\n"
            for child in self._data:
                outStr = outStr + child.yangString()
            outStr = outStr + "\n%s __END"%self._key
            return outStr

        def addChild (self, child):
            self._data.append(child)

        def isEmpty (self):
            return self._data == []

    class List:
        def __init__ (self, key):
            self._key = key
            self._data = []

        def yangString (self):
            outStr = ""            
            for child in self._data:
                outStr = outStr + "%s __BEGIN %s %s __END\n"%(self._key,child.yangString(),self._key)
            return outStr

        def addChild (self, node):
            self._data.append(node)

        def isEmpty (self):
            return self._data == []
    

    def __init__ (self, errorLines=None):
        self._output = self.FewFields()
        self._errors = []
        self._printableOutput = ""
        if errorLines:
            self._errors += errorLines

    def addOutput (self, output):        
        self._output.addChild(output)        

    def addPrintableOutput (self, output):
        self._printableOutput = output

    def addErrorLine (self, line):
        self._errors.append(line)

    def getOutputYangString(self):
        return self._output.yangString()

    def getPrintableOutput(self):        
        return self._printableOutput

    def getErrorString(self):
        return "\n".join(self._errors)

    def getErrors(self):
        return self._errors

    def isOk (self):
        return self._errors == []

    def addAnotherReturnObject (self, obj):
        self._output._data += obj._output._data
        self._errors += obj._errors
        self._printableOutput += obj._printableOutput




#TODO(nirs) make sure only one instance of these command is running simultaniusly
class FileOperations:
    OUR_SUPPORTED_NETWORK_PROTOCOLS = ["ftp", "rcp", "scp", "http", "sftp"]
    def __init__ (self, logger, rootDir):
        self._log = logger.createLogger(G_NAME_MODULE_SYS_MNG_FILE, G_NAME_GROUP_SYS_MNG_FILE_GENERAL)
        self._rootDir = os.path.abspath(rootDir)#this assignment is assumed by A. the nirmalze path function, b. the error messages

    def copy (self, source, destination):        
        try:
            toRetrun = ReturnObject()

            (rc, clacedSources) = self._normalizePath(source, allowNetworkLocation=True, globToListMode = True)
            toRetrun.addAnotherReturnObject(rc)
            if not clacedSources:
                return toRetrun

            (rc, calcedDestination) = self._normalizePath(destination, allowNetworkLocation=True)
            toRetrun.addAnotherReturnObject(rc)
            if not calcedDestination:
                return toRetrun

            dest = calcedDestination[0]
            if len(clacedSources) > 1 and not os.path.isdir(dest):
                toRetrun.addErrorLine("'%s' is not a directory"%os.path.relpath(dest, self._rootDir))
                return toRetrun

            for s in sorted(clacedSources):
                try:
                    rc = self._copy (s, dest)                    
                except Exception, inst:
                    self._log("copy-operation-failed-for-file").debug1("copying '%s' to '%s' failed: %s. st=%s", 
                                                                       s, dest, inst, traceback.format_tb(sys.exc_info()[2]))
                    rc = ReturnObject(errorLines=["failed coping '%s' to '%s'"%(os.path.relpath(s, self._rootDir), os.path.relpath(dest, self._rootDir))])

                toRetrun.addAnotherReturnObject(rc)

            return toRetrun
        except Exception, inst:
            self._log("copy-operation-failed").debug1("copying '%s' to '%s' failed: %s. st=%s", 
                                                       source, destination, inst, traceback.format_tb(sys.exc_info()[2]))
            return ReturnObject(errorLines=[self._getWeirdMessage()])

    def move (self, source, destination):        
        try:
            toRetrun = ReturnObject()

            (rc, clacedSources) = self._normalizePath(source, allowNetworkLocation=True, globToListMode = True)
            toRetrun.addAnotherReturnObject(rc)
            if not clacedSources:
                return toRetrun

            (rc, calcedDestination) = self._normalizePath(destination, allowNetworkLocation=True)
            toRetrun.addAnotherReturnObject(rc)
            if not calcedDestination:
                return toRetrun

            dest = calcedDestination[0]
            if len(clacedSources) > 1 and not os.path.isdir(dest):
                toRetrun.addErrorLine("'%s' is not a directory"%os.path.relpath(dest, self._rootDir))
                return toRetrun

            for s in sorted(clacedSources):
                try:
                    rc = self._move (s, dest)                    
                except Exception, inst:
                    self._log("move-operation-failed-for-file").debug1("moving '%s' to '%s' failed: %s. st=%s", 
                                                                       s, dest, inst, traceback.format_tb(sys.exc_info()[2]))
                    rc = ReturnObject(errorLines=["failed moving '%s' to '%s'"%(os.path.relpath(s, self._rootDir), os.path.relpath(dest, self._rootDir))])

                toRetrun.addAnotherReturnObject(rc)

            return toRetrun
        except Exception, inst:
            self._log("move-operation-failed").debug2("moving '%s' to '%s' failed: %s. st=%s", 
                                                       source, destination, inst, traceback.format_tb(sys.exc_info()[2]))
            return ReturnObject(errorLines=[self._getWeirdMessage()])


    def delete (self, path, alsoDirs):        
        try:
            toRetrun = ReturnObject()

            (rc, clacedPathes) = self._normalizePath(path, globToListMode = True)
            toRetrun.addAnotherReturnObject(rc)
            if not clacedPathes:
                return toRetrun

            for p in sorted(clacedPathes):
                try:
                    if os.path.isdir(p) and alsoDirs:
                        rc = self._deleteDir (p)
                    else:
                        rc = self._deleteFile (p)
                except Exception, inst:
                    self._log("delete-operation-failed-for-file").debug1("deleting '%s' failed: %s. st=%s", 
                                                                         p, inst, traceback.format_tb(sys.exc_info()[2]))
                    rc = ReturnObject(errorLines=["failed deleting '%s'"%(os.path.relpath(p, self._rootDir))])

                toRetrun.addAnotherReturnObject(rc)

            return toRetrun

        except Exception, inst:
            self._log("del-file-operation-failed").debug1("deleting '%s' failed: %s. st=%s", 
                                                          path, inst, traceback.format_tb(sys.exc_info()[2]))
            return ReturnObject(errorLines=[self._getWeirdMessage()])

    def deleteEmptyDir (self, path):        
        try:
            toRetrun = ReturnObject()

            (rc, clacedPathes) = self._normalizePath(path, globToListMode = True)
            toRetrun.addAnotherReturnObject(rc)
            if not clacedPathes:
                return toRetrun

            for p in sorted(clacedPathes):
                try:
                    rc = self._deleteEmptyDir (p)
                except Exception, inst:
                    self._log("remove-dir-operation-failed-for-file").debug1("removing'%s' failed: %s. st=%s", 
                                                                            p, inst, traceback.format_tb(sys.exc_info()[2]))
                    rc = ReturnObject(errorLines=["failed removing '%s'"%(os.path.relpath(p, self._rootDir))])

                toRetrun.addAnotherReturnObject(rc)

            return toRetrun

        except Exception, inst:
            self._log("del-empty-dir-operation-failed").debug1("deleting empty dir '%s' failed: %s. st=%s", 
                                                               path, inst, traceback.format_tb(sys.exc_info()[2]))
            return ReturnObject(errorLines=[self._getWeirdMessage()])


    def dir (self, path, showDirs, showDirsSize, showDirsData):        
        #filling up the assumptions of the function
        if showDirsData:
            showDirsSize = True
        if showDirsSize:
            showDirs = True
        try:
            toRetrun = ReturnObject()

            (rc, clacedPathes) = self._normalizePath(path, globToListMode = True)
            toRetrun.addAnotherReturnObject(rc)
            if not clacedPathes:
                return toRetrun

            for p in sorted(clacedPathes):
                try:
                    rc = self._dir (p, showDirs, showDirsSize, showDirsData)
                except Exception, inst:
                    self._log("list-dir-operation-failed-for-file").debug1("listing '%s' failed: %s. st=%s", 
                                                                            p, inst, traceback.format_tb(sys.exc_info()[2]))
                    rc = ReturnObject(errorLines=["failed listing '%s'"%(os.path.relpath(p, self._rootDir))])

                toRetrun.addAnotherReturnObject(rc)

            return toRetrun

        except Exception, inst:
            self._log("dir-operation-failed").debug1("listing dir '%s' failed: %s. st=%s", 
                                                     path, inst, traceback.format_tb(sys.exc_info()[2]))
            return ReturnObject(errorLines=[self._getWeirdMessage()])

    def makeDir (self, path):        
        try:
            (rc, path) = self._normalizePath(path)
            if not rc.isOk():
                return rc

            return self._makeDir (path[0])
        except Exception, inst:
            self._log("make-dir-operation-failed").debug1("making dir '%s' failed: %s. st=%s", 
                                                          path, inst, traceback.format_tb(sys.exc_info()[2]))
            return ReturnObject(errorLines=[self._getWeirdMessage()])

    def showFileSystem (self):        
        try:            
            return self._showFileSystem (self._rootDir)
        except Exception, inst:
            self._log("show-file-system-operation-failed").debug1("show file system failed: %s.", inst)
            return ReturnObject(errorLines=[self._getWeirdMessage()])


    #private
    def _normalizePath (self, path, allowNetworkLocation = False, globToListMode = False):
        self._log("normalize-path").debug3("normalize path '%s'", path)
        if self._isNetworkPath(path):
            if allowNetworkLocation:
                return (ReturnObject(), [path])
            else:
                self._log("network-path-not-supported").debug2("trying to use network path %s when not supported", path)
                return (ReturnObject(errorLines=["'%s' - network path not supported"%path]),[])

        if os.path.commonprefix([os.path.realpath(path), self._rootDir])==self._rootDir:
            #when called from clispec the path always starts with the root path
            newPath = os.path.relpath(path, self._rootDir)
            self._log("full-path-given").debug3("full path given: '%s', changing to '%s'",path, newPath)
            path=newPath            

        if path.startswith("/"):
            self._log("invalid-path-root", isForceStackTrace=True).debug2("trying to operate over a path starting with \"/\" ('%s'). "
                                                                          "not supported", path)
            return (ReturnObject(errorLines=["'%s' - access denied"%path]),[])

        actualPath = os.path.join(self._rootDir, path)
        if globToListMode:
            pathes = glob.glob(actualPath)
        else:
            pathes = [actualPath]

        resultedPathes = []
        #removing any symbolic links from the way and getting a canonical path
        returnObj = ReturnObject()
        for p in pathes:
            absPath = os.path.realpath(p)        
            userFacingPath = os.path.relpath(absPath, self._rootDir)
            self._log("real-path").debug3("real normalized path is '%s'", absPath)

            if os.path.commonprefix([absPath, self._rootDir])!=self._rootDir:
                self._log("illegal-out-of-root", isForceStackTrace=True).debug2("trying to operate over and path '%s' which is not under '%s'", 
                                                                                absPath, self._rootDir)
                returnObj.addErrorLine("'%s' - access denied"%userFacingPath)
                continue

            if os.path.islink(absPath):
                #not support to happen as we used "readlink"
                self._log("illegal-symlink", isForceStackTrace=True).debug2("trying to operate over and symbolic link '%s'. not supported", 
                                                                            absPath)
                returnObj.addErrorLine("'%s' is a symbolic link. access denied"%userFacingPath)
                continue
                
            self._log("final-path").debug3("normalized path is '%s'", absPath)
            resultedPathes += [absPath]
        
        if not resultedPathes and returnObj.isOk():
            returnObj.addErrorLine("'%s' - no matching files"%path)

        return (returnObj, resultedPathes)


    def _getWeirdMessage (self):
        return "operation failed"


    def _copyOrMove (self, move, source, destination):
        #assuming source&dest are not symbolic links
        toReturn = ReturnObject()

        copyOrMoveStr = "copy"
        if move:
            copyOrMoveStr = "move"


        isSourceNetworkLocation = False
        isDestNetworkLocation = False

        if not move:
            isSourceNetworkLocation = self._isNetworkPath(source)
            isDestNetworkLocation = self._isNetworkPath(destination)
            
            if isSourceNetworkLocation and isDestNetworkLocation:
                self._log("source-and-dest-network").debug2("source '%s' and destination '%s' are both network devices - not supported", source, destination)
                toReturn.addErrorLine("copy between network devices is not supported")
                return toReturn       
            
        if not isSourceNetworkLocation and not os.path.exists(source):
            self._log("no-source").debug2("trying to %s non existing source '%s'", copyOrMoveStr, source)
            toReturn.addErrorLine("'%s' does not exists"%os.path.relpath(source, self._rootDir))
            return toReturn

        if not isDestNetworkLocation and not os.path.exists(os.path.dirname(destination)):
            self._log("destination-path-not-exist").debug2("trying to %s '%s' to an none existsing path '%s'", 
                                                           copyOrMoveStr, source, os.path.dirname(destination))
            toReturn.addErrorLine("'%s' does not exists"%os.path.relpath(os.path.dirname(destination), self._rootDir))
            return toReturn

        if isSourceNetworkLocation:
            if os.path.isdir(destination):
                self._log("destination-exists-dir-from-net").debug3("trying to %s '%s' to directory '%s'", 
                                                                   copyOrMoveStr, source, destination)
                destination = os.path.join(destination, os.path.basename(source))
            if os.path.isdir(destination):
                self._log("destination-inner-exists-dir-from-net").debug2("trying override directory '%s' using '%s'. Not allowed", 
                                                                          destination, source)
                toReturn.addErrorLine("'%s' is a directory"%os.path.relpath(destination, self._rootDir))
                return toReturn
            if os.path.exists(destination):
                try:
                    os.remove(destination)
                except:
                    self._log("failed-delete-orig-dest").exception("%s command failed to remove original destination '%s'", copyOrMoveStr, destination)
                    toReturn.addErrorLine("operation failed")
                    return toReturn
            error = a.infra.network.utils.download(self._log, source, destination)
            if error:
                toReturn.addErrorLine(error)
                if os.path.exists(destination):
                    try:
                        os.remove(destination)
                    except:
                        self._log("failed-delete-created-dest").exception("%s command failed to remove created destination '%s'", copyOrMoveStr, destination)
                    return toReturn

        elif isDestNetworkLocation:
            if os.path.isdir(source):
                self._log("dir-source-to-net").debug3("trying to %s directory '%s' to network device '%s'", 
                                                       copyOrMoveStr, source, destination)                
                toReturn.addErrorLine("'%s' is a directory"%os.path.relpath(source, self._rootDir))
                return toReturn
            error = a.infra.network.utils.upload(self._log, source, destination)
            if error:
                toReturn.addErrorLine(error)
                return toReturn        

        elif os.path.isdir(source):
            self._log("source-dir").debug3("%s directory '%s'", copyOrMoveStr, source)
            if os.path.exists(destination):
                self._log("destination-exists").debug3("%s directory. destination '%s' exists", copyOrMoveStr, destination)
                if not os.path.isdir(destination):
                    self._log("destination-exists-not-dir").debug2("trying to %s '%s' over an existing file '%s'", 
                                                                   copyOrMoveStr, source, destination)
                    toReturn.addErrorLine("'%s' already exists"%os.path.relpath(destination, self._rootDir))
                    return toReturn
                #A deviation from linux behavior - Not a test done by linux
                destination = os.path.join(destination, os.path.basename(source))
                self._log("actual-destination").debug3("actual destination is '%s'", destination)
                if os.path.exists(destination):
                    if not os.path.isdir(destination):
                        self._log("destination-exists-inner-not-dir").debug2("trying to %s '%s' over an existing file '%s'", 
                                                                             copyOrMoveStr, source, destination)
                        toReturn.addErrorLine("'%s' already exists as a non directory"%os.path.relpath(destination, self._rootDir))
                        return toReturn   
                    else:
                        #a deviation from linux behavior. can be fixed when using distutils.dir_util.copy_tree in this case
                        self._log("destination-exists-inner-dir").debug2("trying to %s '%s' over an existing dir '%s'", 
                                                                         copyOrMoveStr, source, destination)
                        toReturn.addErrorLine("'%s' already exists"%os.path.relpath(destination, self._rootDir))
                        return toReturn
            try:
                if move:
                    shutil.move(source, destination)
                else:
                    shutil.copytree(source, destination, symlinks=True)#coping symlinks as is so if they point to some protected data it will not be copied
            except shutil.Error, err:      
                self._log("failed-on-files").debug3("trying to %s '%s' to '%s' failed: '%s'", copyOrMoveStr, source, destination, err)              
                for fileError in err.args[0]:
                    errorStr = fileError[2]
                    errorStr = re.sub("\[[^\[\]]+\] ","", errorStr)
                    errorStr = errorStr.replace(self._rootDir+"/", "")
                    toReturn.addErrorLine(errorStr)
                self._log("failed-on-few-files").debug2("trying to %s '%s' to '%s' failed on few files: '%s'", copyOrMoveStr, source, destination, 
                                                        ";".join(toReturn.getErrorString()))
                return toReturn
        
        else:#file            
            if os.path.exists(destination):
                if not os.path.isdir(destination):
                    self._log("destination-exists-overrun").debug3("overruning '%s' with '%s'", copyOrMoveStr, destination, source)
                else:#directory
                    destination = os.path.join(destination, os.path.basename(source))
                    self._log("actual-destination").debug3("actual destination is '%s'", destination)
                    if os.path.exists(destination):
                        if os.path.isdir(destination):
                            self._log("destination-exists-file-over-dir").debug2("trying to %s file '%s' over an existing dir '%s'", 
                                                                                 copyOrMoveStr, source, destination)
                            toReturn.addErrorLine("'%s' already exists as a directory"%os.path.relpath(destination, self._rootDir))
                            return toReturn   
                    else:
                        #a deviation from linux behavior. can be fixed when using distutils.dir_util.copy_tree in this case
                        self._log("destination-exists-overrun").debug3("overruning '%s' with '%s'", destination, source)
                    
            try:
                if move:
                    shutil.move(source, destination)                
                else:
                    shutil.copy2(source, destination)
            except shutil.Error, err:      
                self._log("failed-single-file-dbg").debug3("trying to %s file '%s' to '%s' failed: '%s'", 
                                                           copyOrMoveStr, source, destination, err)              
                for fileError in err.args[0]:
                    errorStr = fileError[2]
                    errorStr = re.sub("\[[^\[\]]+\] ","", errorStr)
                    errorStr = errorStr.replace(self._rootDir+"/", "")
                    toReturn.addErrorLine(errorStr)
                self._log("failed-single-file").debug2("trying to %s '%s' to '%s' failed: '%s'", 
                                                       copyOrMoveStr, source, destination, ";".join(toReturn.getErrorString()))
                return toReturn
                
        return toReturn

    def _copy (self, source, destination):
        return self._copyOrMove (False, source, destination)

    def _move (self, source, destination):
        if source == self._rootDir:
            toReturn = ReturnObject()
            self._log("move-root").notice("trying to move the users root dir", source)
            toReturn.addErrorLine("cannot move the user's root dir")
            return toReturn
        return self._copyOrMove (True, source, destination)

    def _deleteFile(self, path):
        toReturn = ReturnObject()
        
        if not os.path.lexists(path):
            self._log("del-no-such-file").notice("trying to delete file '%s' - no such file", path)
            toReturn.addErrorLine("'%s' - no such file"%os.path.relpath(path, self._rootDir))
            return toReturn
        if not os.path.isfile(path):
            self._log("del-not-file").notice("trying to delete file '%s' - not a file", path)
            toReturn.addErrorLine("'%s' is a directory"%os.path.relpath(path, self._rootDir))
            return toReturn
        os.remove(path)
        return toReturn

    def _deleteEmptyDir(self, path):
        toReturn = ReturnObject()
        if path == self._rootDir:
            self._log("del-root").notice("trying to remove the users root dir", path)
            toReturn.addErrorLine("cannot remove the user's root dir")
            return toReturn
        if not os.path.lexists(path):
            self._log("del-no-dir").notice("trying to delete dir '%s' - no such dir", path)
            toReturn.addErrorLine("'%s' - no such directory"%os.path.relpath(path, self._rootDir))
            return toReturn
        if not os.path.isdir(path):
            self._log("del-not-a-dir").notice("trying to delete dir '%s' - not a dir", path)
            toReturn.addErrorLine("'%s' is not a directory"%os.path.relpath(path, self._rootDir))
            return toReturn
        if os.listdir(path):
            self._log("del-not-empty-dir").notice("trying to delete dir '%s' - dir is not empty", path)
            toReturn.addErrorLine("'%s' is not empty"%os.path.relpath(path, self._rootDir))
            return toReturn
        os.rmdir(path)
        return toReturn

    def _deleteDir(self, path):
        toReturn = ReturnObject()

        if path == self._rootDir:
            self._log("del-root").notice("trying to remove the users root dir", path)
            toReturn.addErrorLine("cannot remove the user's root dir")
            return toReturn

        if not os.path.lexists(path):
            self._log("del-no-dir").debug2("trying to delete dir '%s' - no such dir", path)
            toReturn.addErrorLine("'%s' - no such directory"%os.path.relpath(path, self._rootDir))
            return toReturn
        if not os.path.isdir(path):
            self._log("del-not-a-dir").debug2("trying to delete dir '%s' - not a dir", path)
            toReturn.addErrorLine("'%s' is not a directory"%os.path.relpath(path, self._rootDir))
            return toReturn

        try:
            shutil.rmtree(path)
        except shutil.Error, err:      
            self._log("failed-rmdir-dbg").debug3("trying to delete tree '%s': '%s'", path, err)              
            for fileError in err.args[0]:
                errorStr = fileError[2]
                errorStr = re.sub("\[[^\[\]]+\] ","", errorStr)
                errorStr = errorStr.replace(self._rootDir+"/", "")
                toReturn.addErrorLine(errorStr)
            self._log("failed-del-files").debug2("trying to delete tree '%s' failed: '%s'", path, ";".join(toReturn.getErrorString()))
            return toReturn

        return toReturn


    class PathInfo:
        def __init__ (self, dirName, baseName, modificationTime, size, permissions):
            self.dirName = dirName
            self.baseName = baseName
            self.modificationTime = modificationTime
            self.size = size
            self.permissions = permissions

    def _getPathInfo (self, fullPath, sizeOnly = False):
        dirName = os.path.dirname(fullPath)
        baseName = os.path.basename(fullPath)
        size = os.path.getsize(fullPath)
        modificationTime = None
        permissions = None
        if not sizeOnly:
            file_stats = os.stat(fullPath)
            modificationTime = time.strftime("%a %b %d %H:%M:%S %Y",time.localtime(file_stats[stat.ST_MTIME]))
            permissions = ""
            if stat.S_ISDIR(file_stats[stat.ST_MODE]):
                permissions = permissions+"d"
            else:
                permissions = permissions+"-"
            if os.access(fullPath, os.R_OK):
                permissions = permissions+"r"
            else:
                permissions = permissions+"-"
            if os.access(fullPath, os.W_OK):
                permissions = permissions+"w"
            else:
                permissions = permissions+"-"
            if os.access(fullPath, os.X_OK):
                permissions = permissions+"x"
            else:
                permissions = permissions+"-"

        return self.PathInfo(dirName=dirName, baseName=baseName, modificationTime=modificationTime, size=size, permissions=permissions)

    def _recursiveDir (self, fullPath, recursionDepth, showDirs, showDirsSize, recurseShowFiles):        
        #assuming that recurseShowFiles==True ==> showDirsSize==True ==> showDirs=True
        self._log("recursive-dir").debug3("_recursiveDir (fullPath=%s, recursionDepth=%s, showDirs=%s, showDirsSize=%s, recurseShowFiles=%s)", 
                                          fullPath, recursionDepth, showDirs, showDirsSize, recurseShowFiles)
        filesList =[]
        dirsList = []
        totalSize = 0
        errorsList = []

        try:
            if os.path.islink(fullPath):
                self._log("dir-symlink").debug2("dir a symlink. skipped", fullPath)
                errorsList.append((os.path.relpath(fullPath, self._rootDir), "symbolic links are not supported - skipping"))
    
            if not os.path.isdir(fullPath):
                self._log("recursive-dir-file").debug4("_recursiveDir on file '%s'", fullPath)
                needToWriteFile = (recurseShowFiles or recursionDepth<=1)
                fileInfo = self._getPathInfo(fullPath, sizeOnly=not needToWriteFile)
                self._log("file-size").debug5("file '%s' size is %d", fullPath, fileInfo.size)
                if needToWriteFile:
                    filesList += [fileInfo]
                    totalSize = fileInfo.size
                else:                    
                    totalSize = fileInfo.size
    
            else:

                scanSubFolders = False

                if recursionDepth == 0:
                    #first path - no need to write it in the files list, just scan its files
                    scanSubFolders = True
                    dirInfo = self._getPathInfo(fullPath, sizeOnly=True)

                else:
                    if not showDirs:#no need to show dir and not the first loop (looking the first dir)
                        self._log("skipping-dir").debug4("_recursiveDir skipping dir '%s'", fullPath)                        
        
                    elif not showDirsSize:#assuming that not showDirsSize => not recursive
                        self._log("dir-no-size").debug4("_recursiveDir dir '%s' no size check", fullPath)
                        needToWriteDir = (recursionDepth>=1)
                        dirInfo = self._getPathInfo(fullPath, sizeOnly=not needToWriteDir)
                        if needToWriteDir:
                            dirsList += [dirInfo]

                    elif not recurseShowFiles:
                        self._log("dir-size-no-recurse").debug4("_dir size no recurse on dir '%s'", fullPath)
                        needToWriteDir = (recursionDepth==1)
                        dirInfo = self._getPathInfo(fullPath, sizeOnly= not needToWriteDir)
                        if needToWriteDir:
                            dirsList += [dirInfo]
                        scanSubFolders = True

                    else:
                        self._log("dir-recurse").debug4("_dir recurse on dir '%s'", fullPath)
                        dirInfo = self._getPathInfo(fullPath, sizeOnly=False)
                        dirsList += [dirInfo]
                        scanSubFolders = True


                if scanSubFolders:
                    self._log("scan-childs").debug4("scanning childs")
                    for childPath in os.listdir(fullPath):                
                        fullChildPath = os.path.join(fullPath, childPath)
                        (files, dirs, size, errors) = self._recursiveDir(fullChildPath, recursionDepth=recursionDepth+1, showDirs=showDirs, showDirsSize=showDirsSize, recurseShowFiles = recurseShowFiles)
                        filesList += files
                        dirsList += dirs
                        if showDirsSize:
                            dirInfo.size += size #total size of the dir                    
                        errorsList += errors

                if showDirsSize:#assuming that not showDirsSize => not recursive
                    self._log("dir-total-size").debug4("_recursiveDir on dir '%s' - total size", dirInfo.size)
                    totalSize = dirInfo.size
                

        except (IOError, os.error), why:
            self._log("dir-file-error").debug2("failed when listing path '%s': %s", fullPath, why)
            why = str(why).replace(self._rootDir+"/", "")
            errorsList.append((os.path.relpath(fullPath, self._rootDir), why))
        
        return (filesList, dirsList, totalSize, errorsList)

    def _dir (self, fullPath, showDirs, showDirsSize, showDirsData):
        #assuming that showDirsData==True ==> showDirsSize==True ==> showDirs=True
        toReturn = ReturnObject()

        if not os.path.exists(fullPath):
            self._log("dir-path-not-exist").debug2("trying to dir '%s' which does not exists", fullPath)
            toReturn.addErrorLine("'%s' does not exists"%os.path.relpath(fullPath, self._rootDir))
            return toReturn

        (files, dirs, size, errors) = self._recursiveDir (fullPath, recursionDepth=0, showDirs=showDirs, 
                                                          showDirsSize=showDirsSize, recurseShowFiles=showDirsData)
        
        filesAndDirs = files+dirs

        perDirDict = {}
        for pathInfo in filesAndDirs:
            if not pathInfo.dirName in perDirDict:
                perDirDict[pathInfo.dirName] = {}
            perDirDict[pathInfo.dirName][pathInfo.baseName]=pathInfo

        dirsYangOutput = ReturnObject.List("directory")
        dirsReadableOutput = ""
        for dirName in sorted(perDirDict):
            self._log("print-dir").debug3("printing directory '%s'",dirName)
            dirYangOutput = ReturnObject.FewFields()
            dirYangOutput.addChild(ReturnObject.Field("name", os.path.relpath(dirName, self._rootDir)))
            specificDirReadableOutput = "directory: %s\n"%os.path.relpath(dirName, self._rootDir)            
            filesYangOutput = ReturnObject.List("file")
            for fileName in sorted(perDirDict[dirName]):
                self._log("print-file").debug4("printing file '%s'",fileName)
                pathInfo = perDirDict[dirName][fileName]
                fileYangOutput = ReturnObject.FewFields()                
                fileYangOutput.addChild(ReturnObject.Field("name", pathInfo.baseName))
                fileYangOutput.addChild(ReturnObject.Field("permissions", pathInfo.permissions))
                fileYangOutput.addChild(ReturnObject.Field("size", pathInfo.size))
                fileYangOutput.addChild(ReturnObject.Field("modified", pathInfo.modificationTime))
                fileReadableOutput = "%s %10s %s %s"%(pathInfo.permissions, pathInfo.size, pathInfo.modificationTime, pathInfo.baseName)
                filesYangOutput.addChild(fileYangOutput)
                specificDirReadableOutput += "%s\n"%fileReadableOutput
            dirYangOutput.addChild(filesYangOutput)
            dirsYangOutput.addChild(dirYangOutput)
            dirsReadableOutput+="%s\n"%specificDirReadableOutput  

            
        toReturn.addOutput(dirsYangOutput)
        toReturn.addPrintableOutput(dirsReadableOutput)

        for error in errors:
            toReturn.addErrorLine("%s: %s"%(error[0], error[1]))

        return toReturn

    def _makeDir(self, path):
        toReturn = ReturnObject()        
        if os.path.lexists(path):
            self._log("mkdir-exists").debug2("trying to create an already existing named dir ('%s')", path)
            toReturn.addErrorLine("'%s' already exists"%os.path.relpath(path, self._rootDir))
            return toReturn
        if not os.path.exists(os.path.dirname(path)):
            self._log("dir-path-not-exist").debug2("trying to mkdir '%s' in a not existing directory '%s'", path, os.path.dirname(path))
            toReturn.addErrorLine("'%s' does not exists"%os.path.relpath(os.path.dirname(path), self._rootDir))
            return toReturn
        a.infra.file.utils.mkdir(path)
        return toReturn

    def _showFileSystem (self, path):
        toReturn = ReturnObject()
        if not os.path.exists(path):
            self._log("show-ssytem-path-not-exist").debug2("trying to show-system on a not existing directory '%s'", path)
            toReturn.addErrorLine("'%s' does not exists"%os.path.relpath(path, self._rootDir))
            return toReturn        
        st = os.statvfs(path)
        free = st.f_bavail * st.f_frsize
        total = st.f_blocks * st.f_frsize
        self._log("disk-stats").debug3("disk stats for path '%s': total=%d, free=%d", path, total, free)
        toReturn.addOutput(ReturnObject.Field("size", total))
        toReturn.addOutput(ReturnObject.Field("free", free))
        toReturn.addOutput(ReturnObject.Field("flags", "rw"))
        return toReturn

    def _isNetworkPath (self, path):
        for protocol in self.OUR_SUPPORTED_NETWORK_PROTOCOLS:
            if path.lower().startswith(protocol+"://"):
                return True
        return False
