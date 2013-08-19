#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

import json
import datetime
import shutil
import os
import a.infra.file.utils

def readFromFile (logger, fileName):
    """load a json file.

    Reads a json file and returns the data held in the file.

    Args:
        logger: logger to send messages to. can be None
        fileName: The name of the file to be loaded (full path or relative to current working directory)

    Returns:
        An object representing the data held in the file. 

    Raises:
        IOError: An error occurred accessing the file
        ValueError: An error occurred trying to parse the json object
    """
    if logger:
        logger("json-load-file").debug5("loading file '%s'", fileName)#TODO(nirs) rise level when this class is not used for blinky
    with open(fileName, 'r') as fd:
        data = json.load(fd)
        if logger:
            logger("json-load-file-read").debug5("Data read from file '%s': %s",fileName, data)#TODO(nirs) rise level when this class is not used for blinky
        return data
    

def writeToFile (logger, data, fileName, tempFileName = None, mkdir=False, indent=None):
    """dump data into a json file.
 
    Write the data into a file with the provided name in JSON format. The writing opperation is "atomic" - 
    If one is tring to read the file it is wither not exist/in its old version/in its complete new version
 
    Args:
        logger: logger to send messages to, can be None
        data: a Dictionary or a List to be written to the file
        fileName: The target file name to write the data into (full path or relative to current working directory)
        tempFileName: a temporary file to be used by the function. If None will use a variation of "fileName".
        mkdir: create the directory of the fileName and tempFileName if needed
 
    Returns:
        None
 
    Raises:
        IOError: An error occurred accessing the file
        TypeError: An error occurred trying to serialize "data"
    """
    if not tempFileName:
        tempFileName = fileName+".tmp."+datetime.datetime.now().strftime("%Y%m%d-%H%M%S-%f")

    if logger:
        logger("json-dump-file").debug5("dumping to file '%s' using temp file name: '%s'",fileName,tempFileName)#TODO(nirs) rise level when this class is not used for blinky
        logger("json-dump-file").debug4("dumping to file '%s': %s",fileName,data)#TODO(nirs) rise level when this class is not used for blinky
    try:
        if mkdir:
            a.infra.file.utils.makeDirs(os.path.dirname(tempFileName), reuseExisting=True)
        with open(tempFileName, 'w') as fd:
            json.dump(data, fd, indent=indent)
        if mkdir:
            a.infra.file.utils.makeDirs(os.path.dirname(fileName), reuseExisting=True)
        shutil.move(tempFileName, fileName)
    finally:
        #cleaning my mess also in case of a failure
        if os.path.exists(tempFileName):
            os.remove(tempFileName)

                  

