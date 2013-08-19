import glob
import fnmatch
import os
import sys
import shutil
import subprocess

class PathCalculator:
    PATH_TYPE_VAR = "var"
    PATH_TYPE_RUN = "run"

    @classmethod
    def s_getComponentPath (cls, partitionPathManager, subSystem, componentClassName, componentInstanceName, pathType=None, subPath = None):        
        path = os.path.join(cls.s_getComponentClassPath(partitionPathManager, subSystem, componentClassName), componentInstanceName)

        if not pathType:
            return path  
        #code added only as pychecker forced me to do something with cls. It took less then 7 minutes to write it
        pathTypes = [getattr(cls, variableName) for variableName in dir(cls) if variableName.startswith("PATH_TYPE")]      
        if not pathType in pathTypes:
            print "unsupported path type:", pathType
            sys.exit(1)#TODO(nirs) FATAL

        path = os.path.join(path, pathType)

        if not subPath:
            return path
        path = os.path.join(path, subPath)

        return path

    @classmethod
    def s_getComponentClassPath (cls, partitionPathManager, subSystem, componentClassName): 
        __pychecker__ = 'unusednames=cls' 
        return os.path.join(partitionPathManager.getFullPath(), subSystem, componentClassName)

class PartitionPathManager:            
    def __init__ (self, path, size, isStub, isTmpfs, isContent):
        self._path = path
        self._partitionSize = size
        self._isStub = isStub
        self._isTmpfs = isTmpfs
        self._isContent = isContent

    def getFullPath (self):
        return self._path   

    def getIsTmpfs (self):
        return self._isTmpfs

    def getIsContent (self):
        return self._isContent
        
    def mount (self):
        if not os.path.exists(self.getFullPath()):
            os.makedirs(self.getFullPath())
        if self._isTmpfs:
            if self._partitionSize is None:
                print "tmpfs", self.getFullPath(), "size was not set"
                sys.exit(1)#TODO(nirs) FATAL
            elif not self._isStub:
                mountCmd="mount -t tmpfs -o size=%dm tmpfs %s"%(self._partitionSize, self.getFullPath())
                rc = subprocess.call(mountCmd, shell=True)
                if rc!=0:
                    print "failed to mount %s using command '%s'. rc=%d"%(self.getFullPath(), mountCmd, rc)
                    sys.exit(1)#TODO(nirs) FATAL
        else:
            if not self._partitionSize is None:
                print "tmpfs", self.getFullPath(), "size was set - this is not supported for non tmpfs partitions"
                sys.exit(1)

    def unmountIfNeeded (self):
        if self.getIsTmpfs():
            if os.path.exists(self.getFullPath()):
                if not self._isStub:                
                    unmountCmd="umount %s"%(self.getFullPath())
                    subprocess.call(unmountCmd, shell=True)  #not checking the return code -
                                                             #if the disk was unmounted and the directory deletion failed, the directory will still be there                   
                try:                  
                    shutil.rmtree(self.getFullPath())
                except:
                    print "Failed to unmount: %s"%self.getFullPath()
                    return False
        return True
                
        

    def clean (self, subSystem):
        runDirs = glob.glob(PathCalculator.s_getComponentPath(self, subSystem, "*","*",PathCalculator.PATH_TYPE_RUN))
        for dirToDel in runDirs:
            shutil.rmtree(dirToDel)


class PartitionsTable:
    def __init__(self):        
        self._partitions = {}        

    def initRootPath (self, rootPath, directoriesPrefix, isStub = False):
        self._rootPath = rootPath
        self._directoriesPrefix = directoriesPrefix
        self._isStub = isStub

    def addPartition (self, name, pathRelToPrefix, size = None, isTmpfs = False, isContent = False):        
        self._partitions[name] = PartitionPathManager(os.path.join(self._rootPath, self._directoriesPrefix, pathRelToPrefix), size, self._isStub, isTmpfs, isContent)

    def getPartition (self, partitionName):        
        if partitionName in self._partitions:
            return self._partitions[partitionName]

    def getContentDisks (self):  
        toReturn = {}      
        for partitionName in sorted(self._partitions):
            if self._partitions[partitionName].getIsContent():
                toReturn[partitionName]=self._partitions[partitionName]
        return toReturn

    def mount (self):        
        for part in sorted(self._partitions):
            self._partitions[part].mount()

    def unmountIfNeeded (self):  
        success = True      
        for part in sorted(self._partitions):
            if not self._partitions[part].unmountIfNeeded():                
                success = False
        return success

    def unmountPrevVerTmpfs (self, globPatternRelToPrefix):    
        globPattern = os.path.join(self._rootPath, self._directoriesPrefix, globPatternRelToPrefix)
        partitionsPathes = glob.glob(globPattern)   
        success = True
        for path in sorted(partitionsPathes):
            pathManager = PartitionPathManager(path, 1, self._isStub, True, False)
            if not pathManager.unmountIfNeeded():                
                success = False
        return success

    def clean (self, subSystem):        
        for part in sorted(self._partitions):
            self._partitions[part].clean(subSystem)
            


class ComponetPathManager:
    def __init__ (self, partitionTable, subSystem, componentClassName, componentInstanceName):
        self._partitionTable = partitionTable
        self._subSystem = subSystem
        self._componentClassName = componentClassName
        self._componentInstanceName = componentInstanceName
        self._dirsToCreate = []
        self._symlinksToCreate = {}

    def _calcDir (self, partitionPathManager, pathType, subPath):
        path = PathCalculator.s_getComponentPath(partitionPathManager, self._subSystem, self._componentClassName, self._componentInstanceName, pathType, subPath)
        return path

    def getExpectedDir (self, partitionName, pathType, subPath = None):
        finalPath = self._calcDir(self._partitionTable.getPartition(partitionName), 
                                  pathType, subPath)
        return finalPath
            
    def initAddPath (self, partitionName, pathType, subPath = None):
        finalPath = self._calcDir(self._partitionTable.getPartition(partitionName), 
                                  pathType, subPath)
        self._dirsToCreate.append(finalPath)
        return finalPath

    def initAddSymlinkOnRunPath (self, partitionName, subPath, targetPath):
        finalPath = self._calcDir(self._partitionTable.getPartition(partitionName), 
                                  PathCalculator.PATH_TYPE_RUN, subPath)
        self._symlinksToCreate[finalPath] = targetPath
        return finalPath

    def createDirsIfNeeded (self):
        for dirToCreate in sorted(self._dirsToCreate):            
            if not os.path.exists(dirToCreate):
                os.makedirs(dirToCreate)

    def createSymLinks (self):
        for symlink in sorted(self._symlinksToCreate):  
            baseDir = os.path.dirname(symlink)         
            if not os.path.exists(baseDir):
                os.makedirs(baseDir)
            if os.path.lexists(symlink):
                print "trying to create an already existing symlink"
                sys.exit(1) #TODO(nirs) fatal - this shall not happen
            os.symlink(os.path.relpath(self._symlinksToCreate[symlink], os.path.dirname(symlink)), symlink)



class SubSystemPathManager:
    def __init__ (self, partitionTable, subSystem):
        self._partitionTable = partitionTable
        self._subSystem = subSystem
        self._componentsClasses = {}

    def addComponent (self, componentClassName, componentInstanceName):
        if not componentClassName in self._componentsClasses:
            self._componentsClasses[componentClassName] = {}
        if componentInstanceName in self._componentsClasses[componentClassName]:
            print "component %s/%s already defined"%(componentClassName, componentInstanceName)
            sys.exit(1) #TODO(nirs) FATAL
        componentPathManager = ComponetPathManager(self._partitionTable, self._subSystem, 
                                                   componentClassName, componentInstanceName)
        self._componentsClasses[componentClassName][componentInstanceName] = componentPathManager
        return componentPathManager

    def _getAllMatchingComps (self, componentClassGlobPattern = "*", componentNameGlobPattern ="*"):
        componentsList = []
        for componentClassName in self._componentsClasses:
            if not fnmatch.fnmatch(componentClassName, componentClassGlobPattern):
                continue
            for componentInstanceName in self._componentsClasses[componentClassName]:
                if not fnmatch.fnmatch(componentInstanceName, componentNameGlobPattern):
                    continue
                componentsList.append(self._componentsClasses[componentClassName][componentInstanceName])

        return componentsList


    def createDirsIfNeeded (self, componentClassGlobPattern = "*", componentNameGlobPattern ="*"):
        componentsList = self._getAllMatchingComps(componentClassGlobPattern, componentNameGlobPattern)
        for componentPathManager in componentsList:
            componentPathManager.createDirsIfNeeded()


    def createSymLinks (self, componentClassGlobPattern = "*", componentNameGlobPattern ="*"):
        componentsList = self._getAllMatchingComps(componentClassGlobPattern, componentNameGlobPattern)
        for componentPathManager in componentsList:
            componentPathManager.createSymLinks()

    def clean (self):
        self._partitionTable.clean(self._subSystem)
