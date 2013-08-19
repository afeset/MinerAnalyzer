#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: michaelg
# 

#
# This file implements HTTP request and response parser
# It uses python package mimetools to implement the logic
#
# TODO: handle parse errors

import urlparse
import mimetools
from StringIO import StringIO

class HttpCommon:
    def _parseHeaders(self, headers):
        self.headers = mimetools.Message(StringIO(headers))

class HttpRequest(HttpCommon):
    def __init__(self, data):
        request, headers = data.split('\r\n', 1)
        #print "====Start headers==="
        #print headers
        #print "--------------------"
        self._parseHeaders(headers)
        self.method, self.path, self.httpVersion = request.split()
        self._parseUrl()

    def _parseUrl(self):
        self.parsedUrl = urlparse.urlparse(self.path, "http")
        self.host = self.headers.get("Host", "")
        self.fullUrl = "http://" + self.host + self.path
        self.paramLists = urlparse.parse_qs(self.parsedUrl.query, keep_blank_values=True)
        self.params = {}
        for name, pList in self.paramLists.iteritems():
            self.params[name] = pList[-1]

class HttpResponse(HttpCommon):
    def __init__(self, data):
        response, headers = data.split('\r\n', 1)
        self._parseHeaders(headers)
        self.httpVersion, statusCodeStr, self.statusString = response.split(" ", 2)
        self.statusCode = int(statusCodeStr)
        self.length = int(self.headers.get("content-length", -1))
        self.contentType = self.headers.gettype()

class Uri:
    def __init__(self, data):
        self.parsedUrl = urlparse.urlparse(data, "http")
        self.host = self.parsedUrl.netloc
        self.paramLists = urlparse.parse_qs(self.parsedUrl.query, keep_blank_values=True)
        self.params = {}
        for name, pList in self.paramLists.iteritems():
            self.params[name] = pList[-1]

