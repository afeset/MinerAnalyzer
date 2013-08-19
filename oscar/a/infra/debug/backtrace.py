#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

import os
import sys
import inspect

class Frame:
    def __init__ (self, fileName, lineNum, pyModuleName, className, function, argsList):
        self.fileName     = fileName
        self.lineNum      = lineNum
        self.pyModuleName = pyModuleName
        self.className    = className 
        self.function     = function
        self.argsList     = argsList

class Backtrace:
    def __init__ (self):
        self._frames = []
        self._currentFrameIndex = -1

    def initFromPythonFrame (self, pythonFrame, currentFrameIndex=0,
                             maxFrameIndex=sys.maxint, maxFrameIndexIncludingArgs=-1):

        self._frames = []
        self._currentFrameIndex=currentFrameIndex
        maxIndexToCollect = max(maxFrameIndex, maxFrameIndexIncludingArgs)
        frameIndex = -1

        while hasattr(pythonFrame, "f_code"):
            frameIndex += 1
            if frameIndex > maxIndexToCollect:
                break

            co = pythonFrame.f_code
            filename = os.path.normcase(co.co_filename)
            #getting the class and the module from the same frame                   
            className = "<unknown>"                                           
            pyModuleName = "<unknown>"                                       
            if hasattr(pythonFrame, "f_locals"):                                              
                calledObj = pythonFrame.f_locals.get('self', None)                            
                if hasattr(calledObj,"__class__"):#not sure if needed (just in case)
                    className=calledObj.__class__.__name__                          
                if hasattr(calledObj,"__module__"):#not sure if needed (just in case)
                    pyModuleName=calledObj.__module__                               
            argsList = []                                                           
            if frameIndex <= maxFrameIndexIncludingArgs:
                try:#not sure if needed (just in case)                                                                 
                    args, _, _, values = inspect.getargvalues(pythonFrame)                        
                    argsList = [(argName, values[argName]) for argName in args]         
                except:                                                                 
                    pass

            collectedFrame = Frame(fileName=filename, 
                                   lineNum=pythonFrame.f_lineno, 
                                   pyModuleName=pyModuleName, 
                                   className=className, 
                                   function=co.co_name, 
                                   argsList=argsList)                                                                
            self._frames.append(collectedFrame)  
            pythonFrame = pythonFrame.f_back                                                            


    def initByFrame (self, collectedFrame):
        self._frames = [collectedFrame]
        self._currentFrameIndex=0


    def getFrames (self):
        return self._frames

    def getCurrentFrameIndex (self):
        return self._currentFrameIndex

