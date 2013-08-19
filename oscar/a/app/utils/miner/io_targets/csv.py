from log_stream import *

class iCSV(iLog):
    def __init__(self, fileName, vars=None):
        iLog.__init__(self, fileName)
        if not vars:
            vars = self.myFileHandler.readline()
        self.myHeaders = vars.rstrip()
        self.myVars = self.myHeaders.split(",")
    def getVariableNames(self):
        return self.myVars
    def getValues(self, line):
        line = line.strip()
        values = []
        prevPos = 0
        l = len(line)
        while True:
            comaPos = line.find(',', prevPos)
            if comaPos == -1:
                comaPos = l
            subString = line[prevPos:comaPos].strip()
            try:
                value = int(subString)
            except:
                try:
                    value = float(subString)
                except:
                    if len(subString)>1 and subString[0]=='"':
                        # find closing quote
                        quoteStart = line.find('"', prevPos)
                        quoteEnd   = line.find('"', quoteStart+1)
                        if quoteEnd == -1:
                            value = line[quoteStart+1:]
                            comaPos = l
                        else:
                            value  = line[quoteStart+1:quoteEnd]
                            comaPos = line.find(',', quoteEnd+1)
                            if comaPos < 0:
                                comaPos = l
                    else:
                        value  = subString
            values.append(value)
            if comaPos == l:
                break
            prevPos = comaPos + 1
        return values

class oCSV(oLog):
    def __init__(self, fileName, variableNames):
        oLog.__init__(self, fileName, variableNames)
        self.myFileHandler.write(",".join(self.myVars)+ "\n")
    def recordToString(self, record):
        return (",".join(self.toStr(e) for e in record) + "\n")
    def toStr(self, val):
        s = str(val)
        if s.find(',') != -1 or s.find(" ") != -1:
            s = '"' + s + '"'
        return s

