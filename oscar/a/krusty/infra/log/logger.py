# 
# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: nirs

import logging
import logging.handlers
import sys
import os

logging.NOTICE = 25
logging.addLevelName(logging.NOTICE, "NOTICE")
logging.DEBUG1 = logging.DEBUG
logging.addLevelName(logging.DEBUG1, "DEBUG1")
logging.DEBUG2 = logging.DEBUG1-1
logging.addLevelName(logging.DEBUG2, "DEBUG2")
logging.DEBUG3 = logging.DEBUG2-1
logging.addLevelName(logging.DEBUG3, "DEBUG3")
logging.DEBUG4 = logging.DEBUG3-1
logging.addLevelName(logging.DEBUG4, "DEBUG4")
logging.DEBUG5 = logging.DEBUG4-1
logging.addLevelName(logging.DEBUG5, "DEBUG5")

def currentframe():
    """Return the frame object for the caller's stack frame."""
    return sys._getframe(3)

#
# _srcfile is used when walking the stack to check when we've got the first
# caller stack frame.
#
if hasattr(sys, 'frozen'): #support for py2exe
    _srcfile = "logging%s__init__%s" % (os.sep, __file__[-4:])
elif __file__[-4:].lower() in ['.pyc', '.pyo']:
    _srcfile = __file__[:-4] + '.py'
else:
    _srcfile = __file__
_srcfile = os.path.normcase(_srcfile)


class LoggerManager(object):
    def __init__ (self, loggerName, logLevel = logging.NOTSET):
        self.loggerName = loggerName
        self.logLevel = logLevel
        self._pylogger = logging.Logger(loggerName, logLevel)
        self.formatter = logging.Formatter('%(name)s: %(asctime)s.%(msecs)d000 <%(levelname)s> [%(process)d/%(thread)d/%('+
                                           Logger.KEY_INSTANCE+')s] %('+
                                           Logger.KEY_OUR_FUNC_NAME+')s#%('+
                                           Logger.KEY_OUR_LINE_NUM+')s %(message)s', "%Y%m%d-%H%M%S")        

    def initAddSyslogHandler(self, logLevel = logging.DEBUG5):
        try:
            handler = logging.handlers.SysLogHandler()
            handler.setLevel(logLevel)
            handler.setFormatter(self.formatter)
            self._pylogger.addHandler(handler)
        except:
            print "ERROR: Logger '%s' failed to add sys-log handler'"%(self.loggerName)

    def initAddTextFileHandler(self, filename, logLevel = logging.DEBUG5):
        try:
            handler = logging.FileHandler(filename)
            handler.setLevel(logLevel)
            handler.setFormatter(self.formatter)
            self._pylogger.addHandler(handler)
        except:
            print "ERROR: Logger '%s' failed to add handler to file '%s'"%(self.loggerName, filename)

    def initAddStreamHandler(self, stream = None, logLevel = logging.DEBUG5):
        try:
            handler = logging.StreamHandler(stream)
            handler.setLevel(logLevel)
            handler.setFormatter(self.formatter)
            self._pylogger.addHandler(handler)
        except:
            print "ERROR: Logger '%s' failed to add handler to stream"%(self.loggerName)

    def createLogger(self, defaultMsgModule, defaultMsgGroup):
        return Logger(self._pylogger, self.logLevel, msgModule=defaultMsgModule, msgGroup=defaultMsgGroup, instance=None)
        pass
    
class Logger(object):
    KEY_INSTANCE = "instance"
    KEY_OUR_FILE_NAME = "our_file_name"
    KEY_OUR_FUNC_NAME = "our_func_name"
    KEY_OUR_LINE_NUM = "our_line_num"
    def __init__(self, pylogger, logLevel, msgModule, msgGroup, instance):
        self._pylogger = pylogger
        self._logLevel = logLevel
        self._module = msgModule
        self._group = msgGroup
        self._instance = instance
        if self._instance is None:
            self._instance = ""

    def createLogger(self, msgModule, msgGroup, instance = None):
        if instance is None:
            instance = self._instance
        return Logger(self._pylogger, self._logLevel, msgModule=msgModule, msgGroup=msgGroup, instance=instance)

    def createLoggerSameModule(self, msgGroup, instance = None):
        if instance is None:
            instance = self._instance
        return Logger(self._pylogger, self._logLevel, msgModule=self._module, msgGroup=msgGroup, instance=instance)

    def __call__ (self, msgName, **kwargs):
        __pychecker__="no-args"
        return MsgSender(self, self._module, self._group, msgName, self._instance)

    def _send (self, msgSender):
        if self._logLevel > msgSender.logLevel:
            return

        logLevel = msgSender.logLevel
        msg = msgSender.msg
        args = msgSender.args
        kwargs = msgSender.kwargs
        if "extra" not in kwargs:
            kwargs["extra"] = {}
        (fileName, line, func) = self._findCaller()
        kwargs["extra"][self.KEY_INSTANCE] = self._instance
        kwargs["extra"][self.KEY_OUR_FILE_NAME] = fileName
        kwargs["extra"][self.KEY_OUR_FUNC_NAME] = func
        kwargs["extra"][self.KEY_OUR_LINE_NUM] = line

        self._pylogger.log(logLevel, msg, *args, **kwargs)
            
    def _findCaller(self):
        f = currentframe()
        #On some versions of IronPython, currentframe() returns None if
        #IronPython isn't run with -X:Frames.
        if f is not None:
            f = f.f_back
        rv = "(unknown file)", 0, "(unknown function)"
        while hasattr(f, "f_code"):
            co = f.f_code
            filename = os.path.normcase(co.co_filename)
            if filename == _srcfile:
                f = f.f_back
                continue
            rv = (filename, f.f_lineno, co.co_name)
            break
        return rv            
            
class MsgSender(object):
    def __init__(self, logger, msgModule, msgGroup, msgName, instance):
        self._logger = logger
        self._msgModule = msgModule
        self._msgGroup = msgGroup
        self._msgName = msgName
        self._instance = instance
        if self._instance is None:
            self._instance = ""

    def log(self, level, msg, *args, **kwargs):
        self._log(level, msg, args, kwargs)

    def debug5 (self, msg, *args, **kwargs):
        self._log(logging.DEBUG5, msg, args, kwargs)

    def debug4 (self, msg, *args, **kwargs):
        self._log(logging.DEBUG4, msg, args, kwargs)

    def debug3 (self, msg, *args, **kwargs):
        self._log(logging.DEBUG3, msg, args, kwargs)

    def debug2 (self, msg, *args, **kwargs):
        self._log(logging.DEBUG2, msg, args, kwargs)

    def debug1 (self, msg, *args, **kwargs):
        self._log(logging.DEBUG1, msg, args, kwargs)

    debug = debug1

    def info (self, msg, *args, **kwargs):
        self._log(logging.INFO, msg, args, kwargs)

    def notice (self, msg, *args, **kwargs):
        self._log(logging.NOTICE, msg, args, kwargs)

    def warning (self, msg, *args, **kwargs):
        self._log(logging.WARNING, msg, args, kwargs)

    def error (self, msg, *args, **kwargs):
        self._log(logging.ERROR, msg, args, kwargs)

    def exception(self, msg, *args):
        """
        Convenience method for logging an ERROR with exception information.
        """
        self._log(logging.ERROR, msg, args, {'exc_info': 1})

    def _critical (self, msg, *args, **kwargs):
        self._log(logging.CRITICAL, msg, args, kwargs)

    def _log(self, level, msg, args, kwargs):
        self.logLevel = level
        self.msg = msg
        self.args = args
        self.kwargs = kwargs
        try:
            self._logger._send(self)
        except:
            try:
                print "ERROR: logger failed to send message: %s (%s)"%(msg, args)
            except:
                print "ERROR: logger failed to send message"



