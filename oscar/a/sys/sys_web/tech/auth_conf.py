import a.sys.sys_web.server.authentication
import a.sys.sys_web.server.authentication.views
import loggers
import django.conf

engine = a.sys.sys_web.server.authentication.getAuthenticationEngine(
                loggers.authLogger,
                django.conf.settings.A_PARAMETERS.getBooleanParameter("use-dummy-authentication", False),
                django.conf.settings.A_PARAMETERS.getBooleanParameter("always-authenticate", False))

env = a.sys.sys_web.server.authentication.views.Environment(engine, 
                                                accessLogger = loggers.accessLogger, errorLogger = loggers.errorLogger,
                                                loginUrl = "/m/client/login/")


