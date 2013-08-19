import django.http
from django.core.servers.basehttp import FileWrapper
import os

class FileStream(FileWrapper):
    def __init__(self, fileName, chunkSize=16*1024, deleteAfter=False):
        self.fileName = fileName
        self.deleteAfter = deleteAfter
        self.fileHandler = open(self.fileName, "rb")
        FileWrapper.__init__(self, self.fileHandler, chunkSize)
    def __del__(self):
        try:
            self.fileHandler.close()
        except:
            pass
        if self.deleteAfter:
            try:
                os.unlink(self.fileName)
            except:
                pass

class HttpFileResponse(django.http.HttpResponse):
    def __init__(self, fileName, contentType, chunkSize=16*1024, deleteAfter=False, saveAs=None):
        if not os.path.isfile(fileName):
            django.http.HttpResponse.__init__(self, content="File '%s' doesn't exist" % fileName, status=404)
            self.fileStream = None
        else:
            self.fileStream = FileStream(fileName, chunkSize, deleteAfter)
            django.http.HttpResponse.__init__(self, self.fileStream, content_type=contentType)
            self['Content-Length'] = str(os.path.getsize(fileName))
            if saveAs:
                self['Content-Disposition'] = 'attachment; filename=%s' % saveAs



