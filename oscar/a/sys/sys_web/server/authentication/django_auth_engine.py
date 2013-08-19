import django.contrib.auth
import datetime
import time

class DjangoAuthEngine(object):
    def __init__(self, authLogger, alwaysAuthenticated):
        self.authLogger = authLogger
        self.isAlwaysAuthenticated = alwaysAuthenticated
        # This value is used by django module Do not modify it
        self.SESSIONID_COOKIE_NAME = "sessionid"
        # This value is defined is qwilt api document
        self.SESSIONID_PARAMETER_NAME = "sessionId"

    def authenticate(self, username, password):
        user = django.contrib.auth.authenticate(username=username, password=password)
        if user is not None:
            self.authLogger.info("User %s authenticated" % username)
            self.deleteExpiredSessions()
        else:
            self.authLogger.warning("User %s authentication failed" % username)
        return user

    def doLogin(self, request, user):
        # Creates new session and register user in it
        self.authLogger.info("Login user %s" % user.username)
        django.contrib.auth.login(request, user)
        # nothing to do with response so
        return None

    def doLogout(self, request):
        self.authLogger.info("Logout user %s" % request.user.username)
        django.contrib.auth.logout(request)
        # nothing to do with response so
        return None

    def getSessionById(self, sessionId):
        from django.contrib.sessions.models import Session
        try:
            return Session.objects.get(pk=sessionId)
        except Session.DoesNotExist:
            return None

    def extractUserFromSession(self, session):
        from django.contrib.auth.models import User
        userId = session.get_decoded().get(django.contrib.auth.SESSION_KEY, None)
        if not userId:
            return None
        try:
            return User.objects.get(pk=userId)
        except User.DoesNotExist:
            return None

    def getSessionIdFromRequest(self, request):
        if self.SESSIONID_PARAMETER_NAME in request.GET:
            return request.GET[self.SESSIONID_PARAMETER_NAME]
        elif self.SESSIONID_COOKIE_NAME in request.COOKIES:
            return request.COOKIES[self.SESSIONID_COOKIE_NAME]
        else:
            return ""

    def getUsernameFromRequest(self, request):
        sessionId = self.getSessionIdFromRequest(request)
        if not sessionId:
            return ""
        session = self.getSessionById(sessionId)
        if not sessionId:
            return ""
        user = self.extractUserFromSession(session)
        if not user:
            return ""
        return user.username

    def isSessionExpired(self, request):
        """Checks whether the session is expired"""
        sessionId = self.getSessionIdFromRequest(request)
        if not sessionId:
            # not exists -> not expired
            return False
        session = self.getSessionById(sessionId)
        # if we id is provided but there is no session object or date is expired - return True
        return session is None or (session.expire_date < datetime.datetime.now())

    def deleteExpiredSessions(self):
        """Cleanups expired sessions"""
        self.authLogger.info("Cleanup sessions expired till now")
        # copied from django/core/management/commands/cleanup.py
        from django.db import transaction
        from django.contrib.sessions.models import Session
        Session.objects.filter(expire_date__lt=datetime.datetime.now()).delete()
        transaction.commit_unless_managed()

    def isRequestAuthenticated(self, request):
        self.authLogger.info("Checking authentication of request to %s" % request.get_full_path())
        if self.isAlwaysAuthenticated:
            self.authLogger.info("Authentication is always approved")
            return True
        sessionId = self.getSessionIdFromRequest(request)
        if not sessionId:
            self.authLogger.info("No session id is specified in request to %s" % request.get_full_path())
            return False
        session = self.getSessionById(sessionId)
        if session is None:
            self.authLogger.warning("Session id %s from request to %s doesn't exist in database" % (sessionId, request.get_full_path()))
            return False
        if session.expire_date < datetime.datetime.now():
            #expiredTime = time.localtime(int(session.expire_date))
            s = session.expire_date.strftime("%Y-%m-%d %H:%M:%S %Z")
            self.authLogger.warning("Session id %s from request to %s was expired at %s" % (sessionId, request.get_full_path(), s))
            return False
        user = self.extractUserFromSession(session)
        if user is None:
            # This should not generally happen
            self.authLogger.warning("User is not found for existing session: %s", sessionId)
            return False
        # Finally
        self.authLogger.info("Request to %s was successfuly authenticated" % request.get_full_path())
        return True

