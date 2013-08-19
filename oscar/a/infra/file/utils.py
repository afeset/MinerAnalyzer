# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

import os
import shutil

# --- mkdir ---------------------------------------------------------------------------------------------------
def mkdir(dir, absMode = None, reuseExisting = False):
    """Create a directory
    Not including all intermediate-level directories needed to contain the leaf directory
     
        Args:
            dir - directory to create
            absMode - creation mode in octal values. default is 0777
            reuseExisting - if the directory already exists - dont do anything
     
        Returns:
            None
     
        Raises:
            OSError: In cases of parent dir does not exists, an existing file with such name, permission error, etc.            

    """
    # Don't remake dir if already exists
    if (reuseExisting):
        if os.path.isdir(dir):
            return

    # Set umask to zero, to enable the creation of 777 dirs
    oldUmask = os.umask(0) 
    try:
        # Create the dir
        if (absMode is not None):
            os.mkdir(dir, absMode)
        else:
            os.mkdir(dir)
    except:
        # maybe the directory was created by another thread
        if not os.path.isdir(dir):
            os.umask(oldUmask)
            raise

    os.umask(oldUmask)

# --- makeDirs ---------------------------------------------------------------------------------------------------
def makeDirs(dir, absMode = None, reuseExisting = False):
    """Create a directory including all intermediate-level directories needed to contain the leaf directory
     
        Args:
            dir - directory to create
            absMode - creation mode in octal values. default is 0777
            reuseExisting - if the directory already exists - dont do anything
     
        Returns:
            None
     
        Raises:
            OSError: In cases of an existing file with such name, permission error, etc.            

    """

    # Don't remake dir if already exists
    if (reuseExisting):
        if os.path.isdir(dir):
            return

    # calc path depth
    depth = 0
    (head, tail) = os.path.split(dir)
    while head:
        if tail:
            depth += 1 
        if head == '/':
            break
        (head, tail) = os.path.split(head)
    
    retries = 0
    # Set umask to zero, to enable the creation of 777 dirs
    oldUmask = os.umask(0) 
    while retries <= depth:
        retries += 1
        try:
            # Create the dir
            if (absMode is not None):
                os.makedirs(dir, absMode)
            else:
                os.makedirs(dir)
        except:
            # maybe the directory was created by another thread
            if os.path.isdir(dir):
                break
            else:
                if retries == depth:
                    os.umask(oldUmask)
                    raise

    os.umask(oldUmask)

# --- symlink ------------------------------------------------------------------------------------------------
def symlink(source, linkName, removeExisting=False, createDirs=False):
    """Create a symbolic link : linkName -> source
            
        Args:
            source - where to point to
            linkName - link name
            removeExisting - If True, remove the "linkName" if it is already exist and points to a different source.
                             If False, no check is done, link is always created (os.symlink raises something if linkName exists)
     
        Returns:
            None
     
        Raises:
            OSError: In cases of an existing file with such name, permission error, etc.            
    """

    # Create dirs if they do not exist
    if createDirs:
        baseDir = os.path.dirname(linkName)         
        if not os.path.exists(baseDir):
            os.makedirs(baseDir)

    # If linkName already exists, and points to a different location, then delete it
    needToCreate = True
    if (removeExisting):
        if os.path.lexists(linkName):
            currentSource = os.readlink(linkName)
            if currentSource != source:
                os.remove(linkName)
            else:
                needToCreate = False

    # Create the link if needed
    if needToCreate:
        os.symlink(source, linkName)


# --- removeFile ---------------------------------------------------------------------------------------------------
def removeFile(filename, ignoreNonExisting=False):
    # Don't remake dir if alreay exists
    if (ignoreNonExisting and not os.path.lexists(filename)):
        return

    os.remove(filename)


# --- moveFiles ---------------------------------------------------------------------------------------------------
def moveFilesOnly(fromDir, toDir):
    """Move content from one directory to another directory. Does not move directories (nor links to directories).
       If the source directory does not exists - nothing will happen.
       If the target directory does not exists - it will be created

       In the future, if you want to extend the function so it will move directories as well,
       dont forget the scenarios in which the toDir is a direct/indirect child of the fromDir

        Args:
            fromDir
            toDir

        Returns:
            dictionary sourceFile->destFile

        Raises:
            OSError: In cases of an existing file with "toDir" name, permission error, etc.            
    """
    if not os.path.exists(fromDir):
        return

    makeDirs(toDir, reuseExisting = True)

    moved = {}

    listOfFiles = os.listdir(fromDir)
    for f in listOfFiles:
        srcFile = os.path.join(fromDir, f)
        if os.path.isdir(srcFile):
            pass            
        else:
            destFile = os.path.join(toDir, f)
            shutil.move(srcFile, destFile)
            moved[srcFile] = destFile

    return moved


# --- directory size utils ---------------------------------------------------------------------------------------------------

def isDirectorySizeAboveLimit(dirPath,countDirs,limit):
    """ Check if the the directory located in dirPath exceeds the limit.
        This function is unsafe in the sense that it will not check if the 
        directory exists or not, nor if it is even a dir. it is the users responsibilty.

        Args:
            dirPath
            countDirs (bool)
            limit

        Returns:
            True/False

        Raises:
            OSError: permission error, etc.            
    """
    sizeSoFar = 0
    for root,dirs,files in os.walk(dirPath):
        if countDirs:
            files+=dirs

        for f in files:
            fp = os.path.join(root,f)
            sizeSoFar += os.path.getsize(fp)               
            if sizeSoFar > limit:
                return True,limit
    return False,sizeSoFar




def isDirectorySizeAboveLimitSafe(dirPath,countDirs,limit):
    """ Check if the the directory located in dirPath exceeds the limit.
        This function is safe - it will check that the path is dir and will skip any 
        file that is missing

        Args:
            dirPath
            countDirs (bool)
            limit

        Returns:
            True/False

        Raises:
            OSError: permission error, etc.            
    """
    if not os.path.isdir(dirPath):
        return False,0
    sizeSoFar = 0
    for root,dirs,files in os.walk(dirPath):
        if countDirs:
            files+=dirs

        for f in files:
            fp = os.path.join(root,f)
            try:
                sizeSoFar += os.path.getsize(fp)
            except Exception:
                pass
            if sizeSoFar > limit:
                return True,limit
    return False,sizeSoFar
