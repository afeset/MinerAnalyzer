import m.io_targets.json_file as json_file

class MetaData:
    class KeyValuePair:
        def __init__(self, jsonObj=None):
            if jsonObj:
                self.key = jsonObj.get("key", "")
                self.value = jsonObj.get("value", "")
            else:
                self.key = ""
                self.value = ""
        def __str__(self):
            return "key: %s, value: %s" % (self.key, self.value)

    class NumericKeyValuePair:
        def __init__(self, jsonObj=None):
            if jsonObj:
                self.key = jsonObj.get("key", 0)
                self.value = jsonObj.get("value", "")
            else:
                self.key = 0
                self.value = ""
        def __str__(self):
            return "key: %d, value: %s" % (self.key, self.value)

    class Segment:
        def __init__(self, jsonObj=None):
            if jsonObj:
                self.startOffset = jsonObj.get("startOffset", 0)
                self.length = jsonObj.get("length", 0)
            else:
                self.startOffset = 0
                self.length = 0
        def __str__(self):
            return "start: %d, length: %d end: %d" % (self.startOffset, self.length, self.startOffset+self.length)
        
    class SubItemInfo:
        def __init__(self, jsonObj=None):
            if jsonObj:
                self.subCid = jsonObj.get("subCid", 0)
                self.isFullyAcquired = jsonObj.get("isFullyAcquired", False)
                self.segment = MetaData.Segment(jsonObj.get("segment", None))
            else:
                self.subCid = 0
                self.isFullyAcquired = False
                self.segment = MetaData.Segment
        def __str__(self):
            return "subCid: %d, fullyAcquired: %s, segment: (%s)" % (self.subCid, self.isFullyAcquired, self.segment)
    
    def _getRepeated(self, klass, jsonObj, name):
        l = jsonObj.get(name, [])
        return map(klass, l)

    def __init__(self, jsonObj=None):
        if jsonObj:
            self.contentType = jsonObj.get('contentType', '')
            self.location = jsonObj.get("location", '')
            self.siteId = jsonObj.get("siteId", 0)
            self.contentLength = jsonObj.get("contentLength", 0)
            self.isFullyAcquired = jsonObj.get("isFullyAcquired", False)
            self.segment = self._getRepeated(MetaData.Segment, jsonObj, "segment")
            self.bytesAcquired = jsonObj.get("bytesAcquired", 0)
            self.mediaRelativeFilePath = jsonObj.get("mediaRelativeFilePath", "")
            self.bytesDiskSize = jsonObj.get("bytesDiskSize", 0)
            self.creationTime = jsonObj.get("creationTime", "")
            self.lastUpdateTime = jsonObj.get("lastUpdateTime", "")
            self.softResponseValidationTokens = self._getRepeated(MetaData.KeyValuePair, jsonObj, "softResponseValidationTokens")
            self.hardResponseValidationTokens = self._getRepeated(MetaData.KeyValuePair, jsonObj, "hardResponseValidationTokens")
            self.subItemsInfo = self._getRepeated(MetaData.SubItemInfo, jsonObj, "subItemsInfo")
            self.locationByCdnId = self._getRepeated(MetaData.NumericKeyValuePair, jsonObj, "locationByCdnId")
        else:
            self.contentType = "video/mp4"
            self.location = ''
            self.siteId = 0
            self.contentLength = 0
            self.isFullyAcquired = False
            self.segment = []
            self.bytesAcquired = 0
            self.mediaRelativeFilePath = ""
            self.bytesDiskSize = 0
            self.creationTime = ""
            self.lastUpdateTime = ""
            self.softResponseValidationTokens = []
            self.hardResponseValidationTokens = []
            self.subItemsInfo = []
            self.locationByCdnId = []

    @property
    def cid(self):
        return self.mediaRelativeFilePath.rsplit("/", 1)[1]
    def __str__(self):
        return "site:%d cid=%s content-length:%d content-type:%s full:%s acquired:%d on-disk:%d segments:[%s] %s" % \
               (self.siteId, self.cid, self.contentLength, self.contentType, self.isFullyAcquired, \
                self.bytesAcquired, self.bytesDiskSize, "[" + ", ".join("("+str(s)+")" for s in self.segment)+"]", self.location)
class iMeta(json_file.iJson):
    def __init__(self, fileHandle):
        json_file.iJson.__init__(self, fileHandle)
    def next(self):
        try:
            (obj,) = json_file.iJson.next(self)
            return (MetaData(obj), )
        except:
            raise
    def getVariableNames(self):
        return ["metadata", ]

def parseUriFromMeta(meta):
    from m.http import Uri
    return Uri(meta.location)
