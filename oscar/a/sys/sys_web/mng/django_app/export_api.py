import django.conf
import os
import os.path
import django.http
import exporter

import warnings
with warnings.catch_warnings():
    #jpype module uses deprecated sets module
    warnings.simplefilter("ignore")
    import jpype
import loggers
from a.sys.sys_web.server.file_server import HttpFileResponse

import a.sys.sys_web.mng.django_app as api
import auth_conf
import tempfile

gIsJavaInitialized = False

def initJava():
    global gIsJavaInitialized
    if gIsJavaInitialized:
        return

    os.environ['JAVA_HOME'] = "/usr/lib/jvm/jre"
    loggers.accessLogger.info("Initializing java %s" % os.environ['JAVA_HOME'])
    SX_JAR = os.path.join(django.conf.settings.A_APPLICATION_ROOT_DIR, 'SX.jar')

    options = [
        '-Djava.class.path=%s' % SX_JAR,
        '-Xmx1024m'
    ]

    loggers.accessLogger.info("JVM path = %s, class path = %s" % (jpype.getDefaultJVMPath(), SX_JAR))
    try:
        jpype.startJVM(jpype.getDefaultJVMPath(), *options)
    except:
        pass
    gIsJavaInitialized = True

@loggers.viewLogging
def export(request):
    if not auth_conf.engine.isRequestAuthenticated(request):
        loggers.mainLogger.warning("Accessing export api without authorized user")
        return django.http.HttpResponse("Requires authentication", status = 401)

    initJava()
    # Get request paramaters dictionary 
    requestParamsDict = request.GET;
    filename = requestParamsDict.get("filename", "reports.xlsx")
    reportType = requestParamsDict.get("reportType", "content")
    exportAll = requestParamsDict.get("all", None)
    # Decode request params into sections params
    if exportAll is None:
        sectionsParams = api.decodeSystemApiSectionsParams(requestParamsDict)
    else:
        sectionsParams = None

    tempFileTuple = tempfile.mkstemp(suffix=".xlsx", prefix="export-", dir=os.path.join(django.conf.settings.A_APPLICATION_ROOT_DIR, "temp"))
    os.close(tempFileTuple[0])
    exportFileName = tempFileTuple[1]

    if reportType == "content":
        exporterObj = exporter.ContentExporter()
    else:
        exporterObj = exporter.OverviewExporter()

    loggers.accessLogger.debug("..... Before export")
    exporterObj.export(sectionsParams, os.path.join(django.conf.settings.A_APPLICATION_ROOT_DIR, "export_templates"), exportFileName)

    loggers.accessLogger.info("..... Running java garbage collector")
    jpype.java.lang.System.gc()
    loggers.accessLogger.info("..... Java garbage collector done")
    loggers.accessLogger.debug("..... After export")
    # shutdown doesn't work correctly
    #jpype.shutdownJVM()
    response = HttpFileResponse(exportFileName, 'application/vnd.ms-excel', deleteAfter=True, saveAs=filename)
    return response

