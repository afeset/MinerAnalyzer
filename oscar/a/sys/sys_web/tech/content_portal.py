import loggers
import auth_conf
from   a.sys.sys_web.server.authentication.views import redirectIfNotAuthenticated, redirectToLogin
import django.http
from django.core.servers.basehttp import FileWrapper
import django.conf
import os
import json

@loggers.viewLogging
@redirectIfNotAuthenticated(auth_conf.env)
def serveContent(request, path):
    fileName = os.path.join(django.conf.settings.A_APPLICATION_ROOT_DIR, "content", "media", path)
    if not os.path.isfile(fileName):
        return django.http.HttpResponseNotFound(content="%s file (%s) non found" % (path, fileName))

    contentType = "application/octet-stream"
    metaFileName = os.path.join(django.conf.settings.A_APPLICATION_ROOT_DIR, "content", "meta", "%s.meta" % path)
    if os.path.isfile(metaFileName):
        metaFH = open(metaFileName, "r")
        try:
            metaData = json.load(metaFH)
            contentType = metaData["contentType"]
            isFullyAcquired = metaData.get("isFullyAcquired", True)
            if not isFullyAcquired:
                s = "'%s' is not fully acquired\nAvailable ranges are:\n"  % path
                for segment in metaData["segment"]:
                    s += "  [%d-%d) len %d\n" %(segment['startOffset'], segment['startOffset'] + segment['length'], segment['length'])
                return django.http.HttpResponse(s, content_type="text/plain")
        except:
            metaFH.close()
            return django.http.HttpResponse("Invalid meta file", content_type="text/plain")
        metaFH.close()
    loggers.accessLogger.info("path: %s size: %s" %(fileName, str(os.path.getsize(fileName))))
    fileHandler = open(fileName, "rb")
    wrapper = FileWrapper(fileHandler, 256*1024)
    response = django.http.HttpResponse(wrapper, content_type=contentType)
    response['Content-Length'] = str(os.path.getsize(fileName))
    return response

# since some streamers (VLC) doesn't support cookie we extract session cookie from URL and
# redirect to serveContent
@loggers.viewLogging
@redirectIfNotAuthenticated(auth_conf.env)
def streamVideo(request, path):
    sessionId = auth_conf.engine.getSessionIdFromRequest(request)
    newPath = "/tech/content/%s?%s=%s" % (path, auth_conf.engine.SESSIONID_PARAMETER_NAME, sessionId)
    loggers.accessLogger.info("Redirecting to serveContent: %s" % newPath)
    return django.http.HttpResponseRedirect(newPath)

