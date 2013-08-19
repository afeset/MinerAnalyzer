#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 
try:
    import pycurl
except:
    pass

import os

#TODO(nirs) ellaborate on the return codes when we have the time
def upload (logger, sourceFile, targetUrl):
    logger("upload").debug2("upload '%s' to '%s'", sourceFile, targetUrl)
    try:
        curly = pycurl.Curl()
    except:
        logger("upload-not-supported").debug2("download failed as it is not supported")
        return "upload operation is not supported"
    curly.setopt(pycurl.URL, targetUrl)
    curly.setopt(pycurl.UPLOAD, 1)
    try:
        with open(sourceFile, 'rb') as fd:
            curly.setopt(pycurl.READFUNCTION, fd.read)
            fileSize = os.path.getsize(sourceFile)
            curly.setopt(pycurl.INFILESIZE, fileSize)
            curly.perform()
            curly.close()
    except IOError, err:
        logger("upload-failed-source").debug2("upload failed to open source file '%s' for reading/get its size: %s", sourceFile, err.strerror)
        return "Failed to read source file"
    except pycurl.error, err:
        logger("upload-failed-dest").debug2("upload failed to write to destination file '%s': %s", targetUrl, err[1])
        return "Failed to upload file: %s"%err[1]      
        
    return None  



def download (logger, sourceUrl, targetFile):
    try:
        curly = pycurl.Curl()
    except:
        logger("download-not-supported").debug2("download failed as it is not supported")
        return "download operation is not supported"

    curly.setopt(pycurl.URL, sourceUrl)

    try:
        with open(targetFile, 'wb') as fd:
            curly.setopt(pycurl.WRITEFUNCTION, fd.write)
            curly.perform()
            curly.close()

    except IOError, err:
        logger("download-failed-target").debug2("download failed to open target file '%s' for writing: %s", targetFile, err.strerror)
        return "Failed to read source file"
    except pycurl.error, err:
        logger("download-failed-source").debug2("download failed to read to source file '%s': %s", sourceUrl, err[1])
        return "Failed to download file: %s"%err[1]

    return None  

