from csv import *
from pickle_stream import *
from stdout import *
from qbl_coal import *
from log_stream import *

__all__ = [ 'iCoal', 'oCoal', 'iCsv', 'oCsv', 'oStdout', 'iPickle', 'oPickle', 'iRaw', 'oRaw', 'iLog', 'oLog', 'iQdl', 'iTransaction', 'GPBChain']

extensionToTypeMap = {
    '.csv':   'csv',
    '.qbl':   'coal',
    '.pic':   'pickle',
    '.txt':   'log',
    'stdout': 'stdout',
    '.log':   'log'
}

typeToClassMap = {
    'csv':    'CSV',
    'coal':   'Coal',
    'pickle': 'Pickle',
    'stdout': 'Stdout',
    'log':    'Log',
    'raw':    'Raw',
    'qdl':    'Qdl',
    'transaction': 'Transaction',
    'gpbchain': 'GPBChain',
}

def getTypeByExtension(extension):
    return extensionToTypeMap.get(extension, None)

def getInputStreamClass(inputType):
    className = typeToClassMap.get(inputType, None)
    if not className:
        return None
    else:
        return "io_targets.i%s" % className

def getOutputStreamClass(outputType):
    className = typeToClassMap.get(outputType, None)
    if not className:
        return None
    else:
        return "io_targets.o%s" % className

class UnexistingIStream:
    def __init__(self, inputType):
        self.myInputType = inputType
    def __str__(self):
        return "iStream for type %s doesn't exist" % self.myInputType


def iStreamFactory(inputType, fileName, streamVars):
    iStreamName = getInputStreamClass(inputType)
    if not iStreamName:
        raise UnexistingIStream(inputType)
    iStreamClass = globals()["i%s" % typeToClassMap[inputType]]
    return iStreamClass(fileName, **streamVars)

__all__ += ['getTypeByExtension', 'getInputStreamClass', 'getOutputStreamClass', 'iStreamFactory', 'UnexistingIStream']


