import time

# This is dummy implementation so it often doesn't use function argument sof we suppress warnings on them
__pychecker__ = 'no-argsused'

DEFAULT_SESSION_AGE = 3600

class User:
    USERNAME = "viewer"
    PASSWORD = "viewer"
    def __init__(self):
        self.username = User.USERNAME
        self.password = User.PASSWORD

class Session:
    def __init__(self, sessionId):
        self.sessionId = sessionId
        self.expire_date = int(sessionId)

class Dummy_Auth_Engine(object):
    """
    Dummy_Auth_Engine implements authentication engine for single user with username="viewer" password="viewer"
    Session id is equal to its expiration time 
    """

    def __init__(self, authLogger):
        self.authLogger = authLogger
        # This value is used by django module Do not modify it
        self.SESSIONID_COOKIE_NAME = "dummy-sessionid"
        # This value is defined is qwilt api document
        self.SESSIONID_PARAMETER_NAME = "sessionId"

    def createSessionId(self):
        return int(time.time()) + DEFAULT_SESSION_AGE

    def authenticate(self, username, password):
        if username != User.USERNAME or password != User.PASSWORD:
            return False
        return User()

    def doLogin(self, request, user):
        # Creates new session and register user in it
        self.authLogger.info("Login user %s" % user.username)
        sessionId = self.createSessionId()
        def setSessionCookie(response):
            response.set_cookie(self.SESSIONID_COOKIE_NAME, str(sessionId), max_age=DEFAULT_SESSION_AGE)
        return setSessionCookie

    def doLogout(self, request):
        self.authLogger.info("Logout user %s" % request.user.username)
        def deleteSessionCookie(response):
            response.delete_cookie(self.SESSIONID_COOKIE_NAME)
        return deleteSessionCookie

    def getSessionById(self, sessionId):
        return Session(sessionId)

    def extractUserFromSession(self, session):
        return User()

    def getSessionIdFromRequest(self, request):
        if self.SESSIONID_PARAMETER_NAME in request.GET:
            return request.GET[self.SESSIONID_PARAMETER_NAME]
        elif self.SESSIONID_COOKIE_NAME in request.COOKIES:
            return request.COOKIES[self.SESSIONID_COOKIE_NAME]
        else:
            return ""

    def getUsernameFromRequest(self, request):
        return User.USERNAME

    def isSessionExpired(self, request):
        """Checks whether the session is expired"""
        sessionId = self.getSessionIdFromRequest(request)
        if not sessionId:
            # not exists -> not expired
            return False
        session = self.getSessionById(sessionId)
        # if we id is provided but there is no session object or date is expired - return True
        return session is None or (session.expire_date < int(time.time()))

    def deleteExpiredSessions(self):
        """Cleanups expired sessions"""
        self.authLogger.info("Cleanup sessions expired till now")

    def isRequestAuthenticated(self, request):
        sessionId = self.getSessionIdFromRequest(request)
        if not sessionId:
            # no session is Okay
            return True
        session = self.getSessionById(sessionId)
        if session is None:
            return False
        if session.expire_date < time.time():
            return False
        user = self.extractUserFromSession(session)
        if user is None:
            # This should not generally happen
            self.authLogger.warning("User is not found for existing session: %d", sessionId)
            return False
        # Finally
        return True

