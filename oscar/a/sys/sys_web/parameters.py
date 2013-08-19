import json
import os

def loadDictionaryFromJsonFile(fileName):
    """Saves Python dictrionary as json file"""
    try:
        fp = open(fileName, "r")
    except IOError:
        return None
    dictionary = json.load(fp)
    fp.close()
    return dictionary

def saveDictionaryToJsonFile(dictionary, fileName):
    """Saves Python dictrionary as json file"""
    fp = open(fileName, "w")
    json.dump(dictionary, fp, indent=4)
    fp.close()

PARAMS_FILE_NAME="params.json"

class Parameters:
    def __init__(self, dirName=None, fileName=None, dictionary=None):
        """
        Initializes parameters class in one of the following forms
        1. No arguments
        2. Specifies dictionary with parameters (dictionary=XXX)
        3. Specifies json file containing this dictionary (fileName="file.json")
        4. Specifies directiory with json file `params.json` (dirName="sys_web/data/mng")
        IMPORTANT! parameter names coming from ConfigData are always in lower case
        """
        if dirName is not None:
            fileName = os.path.join(dirName, PARAMS_FILE_NAME)
        if fileName is not None:
            self.fileName = fileName
        if dictionary is not None:
            self.setDictionary(dictionary)

        if dictionary is None and fileName is not None:
            # load dictionary from file
            self.load()

    def setDictionary(self, dictionary):
        self.dictionary = dictionary

    def getDictionary(self):
        return self.dictionary
    
    def load(self):
        self.dictionary = loadDictionaryFromJsonFile(self.fileName)
    def save(self):
        if self.dictionary is not None:
            saveDictionaryToJsonFile(self.dictionary, self.fileName)

    def hasParameter(self, name):
        if self.dictionary is None or not name in self.dictionary:
            return False
        else:
            return True

    def getBooleanParameter(self, name, default):
        if self.dictionary is None or not name in self.dictionary:
            return default
        val = self.dictionary[name]
        if isinstance(val, str) or isinstance(val, unicode):
            strVal = val.lower()
            if strVal == "true" or strVal == "yes":
                return True
            elif strVal == "false" or strVal == "no":
                return False
            else:
                return default
        else:
            return bool(val)

    def getBooleanParameterAsStr(self, name, default):
        boolVal = self.getBooleanParameter(name, default)
        return str(boolVal).lower()

    def getIntParameter(self, name, default):
        if self.dictionary is None or not name in self.dictionary:
            return default
        val = self.dictionary[name]
        return int(val)

    def getIntListParameter(self,name,default):
        if self.dictionary is None or not name in self.dictionary:
            return default
        strVal = self.dictionary[name].strip()
        arr = strVal.split(' ')
        return map(int,arr)

    def getParameter(self, name, default):
        if self.dictionary is None or not name in self.dictionary:
            return default
        return self.dictionary[name]

    def getMappedParameter(self, name, mapDictionary, default):
        if self.dictionary is None or not name in self.dictionary:
            return default
        symbolicName = self.dictionary[name]
        return mapDictionary.get(symbolicName, default)

    def items(self):
        if self.dictionary:
            return self.dictionary.items()
        else:
            return []

    def setParameter(self, name, value):
        if not self.dictionary:
            self.dictionary = {}
        self.dictionary[name] = value
