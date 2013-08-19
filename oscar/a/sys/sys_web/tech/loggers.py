import a.sys.sys_web.server.log
import django.conf
import functools
import os

logsDir          = os.path.join(django.conf.settings.A_APPLICATION_ROOT_DIR, "logs")

# Create the main logger / errorLogger
errorLogger =  a.sys.sys_web.server.log.createLogger(a.sys.sys_web.server.log.FlushLogger, "error")

# Create the access logger
accessLogger =  a.sys.sys_web.server.log.createLogger(a.sys.sys_web.server.log.FlushLogger, "access")

# Create logger for authentication events
authLogger =  a.sys.sys_web.server.log.createLogger(a.sys.sys_web.server.log.FlushLogger, "auth")

# based on django.views.decorators.cache.never_cache decorator
def viewLogging(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        a.sys.sys_web.server.log.logRequest(accessLogger, request, view_func)
        try: 
            response = view_func(request, *args, **kwargs)
        except:
            a.sys.sys_web.server.log.logRequest(errorLogger, request, view_func)
            errorLogger.exception("Exception occurred")
            accessLogger.exception("Exception occurred")
            raise
        else:
            a.sys.sys_web.server.log.logResponse(accessLogger, response)
        finally:
            accessLogger.emitFlush()

        return response
    return functools.wraps(view_func, assigned=django.utils.decorators.available_attrs(view_func))(_wrapped_view_func)

