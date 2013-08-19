import django.http

import functools
import django.utils.decorators
import json

DEFAULT_SESSION_AGE = 24*3600

class Environment:
    def __init__(self, authenticationEngine, accessLogger, errorLogger=None, loginUrl=None, loginRedirectUrl=None, loginTemplateName=None, sessionAge=DEFAULT_SESSION_AGE):
        self.engine = authenticationEngine
        self.accessLogger = accessLogger
        self.errorLogger = errorLogger
        self.loginUrl = loginUrl
        self.loginFailUrl = (loginUrl + "?authFailed=1") if loginUrl else None
        self.loginRedirectUrl = loginRedirectUrl
        self.loginTemplateName = loginTemplateName
        self.sessionAge = sessionAge


# based on django.views.decorators.cache.never_cache decorator
def viewLogging(view_func):
    from a.sys.sys_web.server.log import logRequest, logResponse
    def _wrapped_view_func(request, env, *args, **kwargs):
        logRequest(env.accessLogger, request, view_func)
        try: 
            response = view_func(request, env, *args, **kwargs)
        except:
            if env.errorLogger:
                logRequest(env.errorLogger, request, view_func)
                env.errorLogger.exception("Exception occurred")    
            env.accessLogger.exception("Exception occurred")    
            raise
        else:
            logResponse(env.accessLogger, response)
        finally:
            env.accessLogger.emitFlush()
        return response
    return functools.wraps(view_func, assigned=django.utils.decorators.available_attrs(view_func))(_wrapped_view_func)

@viewLogging
def login(request, env):
    # To get hostname
    import socket
    # Return login template with relevant context variables

    # Build template context 

    loginContext = {}
    loginContext['authFailed'] = "true" if 'authFailed' in request.GET else "false"

    # next Uri is extracted from 'next' parameter if we were redirected here from some internal page
    loginContext['successUri'] = request.GET.get('next', env.loginRedirectUrl)

    loginContext['failUri'] = env.loginFailUrl

    loginContext['invalidSession'] = "true" if 'invalidSession' in request.GET else "false"

    contextVars = { 'a': {'login': loginContext, 'hostName': socket.gethostname()}}

    context = django.template.RequestContext( request, contextVars )
    # Calc the response 
    template = django.template.loader.get_template(env.loginTemplateName)

    response = django.http.HttpResponse(template.render(context))
    return response

@viewLogging
def apiLogin(request, env):
    if request.method == 'POST' and 'username' in request.POST and 'password' in request.POST:
        # POST performs redirect only
        user = env.engine.authenticate(request.POST['username'], request.POST['password'])

        responseFixup = None
        if user:
            # successful login
            responseFixup = env.engine.doLogin(request, user)
            redirectUri = request.POST.get('successUri', env.loginRedirectUrl)
        else:
            redirectUri = request.POST.get('failUri', env.loginRedirectUrl)
        response = django.http.HttpResponseRedirect(redirectUri)
        if responseFixup:
            responseFixup(response)
    else:
        response = django.http.HttpResponse("Waiting for valid authentication request", status=401)
    return response

@viewLogging
def apiLogout(request, env):
    responseFixup = env.engine.doLogout(request)
    response = django.http.HttpResponseRedirect(env.loginUrl)
    if responseFixup:
        responseFixup(response)
    return response

@viewLogging
def apiSession(request, env):
    from django.contrib.sessions.backends.db import SessionStore
    from django.contrib.sessions.models import Session
    from django.contrib.auth.models import User

    def invalidResponse(msg):
        return { "result": {"value": -1, "error-message": msg} }

    if request.method != 'POST':
        return django.http.HttpResponse("Waiting for POST")
    if not 'operation' in request.POST:
        return httpJsonResponse(invalidResponse("no operation provided"))

    operation = request.POST['operation']
    if operation == "create":
        if 'username' not in request.POST or 'password' not in request.POST:
            response = invalidResponse("no username/password provided")
        else:
            user = env.engine.authenticate(request.POST['username'], request.POST['password'])
            if user is None:
                response = invalidResponse("Login failed")
            else:
                # create new session object
                session = SessionStore()
                session[django.contrib.auth.SESSION_KEY] = user.id
                session[django.contrib.auth.BACKEND_SESSION_KEY] = user.backend
                session.set_expiry(request.POST.get('expiration', DEFAULT_SESSION_AGE))
                session.save()
                response = { "result": { "value": 0 },
                             "session": { "sessionId": session.session_key}
                           }
    elif operation == "terminate":
        if env.engine.SESSIONID_PARAMETER_NAME not in request.POST:
            response = invalidResponse("sessionId is not provided")
        else:
            sessionId = request.POST[env.engine.SESSIONID_PARAMETER_NAME]
            session = getSessionById(sessionId)
            if session is None:
                authLogger.warning("Trying to terminate unknown session %s" % sessionId)
            else:
                authLogger.info("Terminating session %s", sessionId)
                session.delete()
            response={
                        "result": {
                           "value": 0
                        }
                     }
    elif operation == "get-user":
        # This is undocumented debug feature
        if env.engine.SESSIONID_PARAMETER_NAME not in request.POST:
            response = invalidResponse("sessionId is not provided")
        else:
            sessionId = request.POST[env.engine.SESSIONID_PARAMETER_NAME]
            session = getSessionById(sessionId)
            if session is None:
                response = invalidResponse("Unknown session")
            else:
                user = extractUserFromSession(session)
                if user is None:
                    response = invalidResponse("Failed to resolve user for id %d" % userId)
                else:
                    response={
                                "result": {
                                   "username": user.username
                                }
                             }
    else:
        response = invalidResponse("Unsupported operation %s" % operation)

    httpResponse = httpJsonResponse(response)
    return httpResponse

def redirectToLogin(request, env):
    from django.contrib.auth.views import redirect_to_login
    sessionExpired = env.engine.isSessionExpired(request)
    loginUrl = env.loginUrl
    if sessionExpired:
        loginUrl += "?sessionExpired=1"
    return redirect_to_login(request.path,
                             login_url=loginUrl,
                             redirect_field_name="next")

# decorator for views that should authomatically redrect to login page
# if request is not authenticaticated
def redirectIfNotAuthenticated(env):
    def decorator(view_func):
        @functools.wraps(view_func, assigned=django.utils.decorators.available_attrs(view_func))
        def wrappedView(request, *args, **kwargs):
            if not env.engine.isRequestAuthenticated(request):
                env.accessLogger.warning("Accessing system without authenticated user")
                env.errorLogger.warning("Accessing system without authenticated user")
                return redirectToLogin(request, env)
            else:
                return view_func(request, *args, **kwargs)
        return wrappedView
    return decorator

def httpJsonResponse(dictionary):
    s = json.dumps(dictionary, sort_keys=True, indent=4)
    # Build the response 
    httpResponse = django.http.HttpResponse(s)
    httpResponse['Cache-Control']  = 'no-cache'
    httpResponse['Content-Type']   = 'application/json'
    return httpResponse



