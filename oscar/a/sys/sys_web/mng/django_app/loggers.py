import a.sys.sys_web.server.log
import functools
import django.utils.decorators
import django.conf
import os

logsDir          = os.path.join(django.conf.settings.A_APPLICATION_ROOT_DIR, "logs")

# Create the main logger / errorLogger
mainLogger =  a.sys.sys_web.server.log.createLogger(a.sys.sys_web.server.log.FlushLogger, "main")

# Create the access logger
accessLogger =  a.sys.sys_web.server.log.createLogger(a.sys.sys_web.server.log.FlushLogger, "access")

# Create the api logger
apiLogger =  a.sys.sys_web.server.log.createLogger(a.sys.sys_web.server.log.ApiLogger, "api")

# Create the logger for ux module
uxLogger =  a.sys.sys_web.server.log.createLogger(a.sys.sys_web.server.log.ApiLogger, "ux")

# Create logger for authentication events
authLogger =  a.sys.sys_web.server.log.createLogger(a.sys.sys_web.server.log.FlushLogger, "auth")

# based on django.views.decorators.cache.never_cache decorator
def viewLogging(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        a.sys.sys_web.server.log.logRequest(accessLogger, request, view_func)
        try: 
            response = view_func(request, *args, **kwargs)
        except:
            a.sys.sys_web.server.log.logRequest(mainLogger, request, view_func)
            mainLogger.exception("Exception occurred")    
            accessLogger.exception("Exception occurred")    
            raise
        else:
            a.sys.sys_web.server.log.logResponse(accessLogger, response)
        finally:
            accessLogger.emitFlush()
            apiLogger.emitFlush()

        return response
    return functools.wraps(view_func, assigned=django.utils.decorators.available_attrs(view_func))(_wrapped_view_func)

