
class oStdout:
    def __init__(self, filename, variableNames):
        self.myVars = variableNames
        print "="*60
        print ",".join(self.myVars)
        print "-"*60
    def save(self, record):
        print ",".join(self.toStr(e) for e in record)
    def toStr(self, val):
        s = str(val)
        if s.find(',') != -1 or s.find(" ") != -1:
            s = '"' + s + '"'
        return s
    def close(self):
        pass

