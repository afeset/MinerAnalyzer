
import django_auth_engine
import dummy_auth_engine

def getAuthenticationEngine(authLogger, useDummyAuthentication = False, alwaysAuthenticated=False):
    """
    This is factory function that returns authentication engine
    Currently 2 engines are available - one is based on django.contrib.auth, another one is dummy
    """
    # this is factory so we return diffent classes no interface class is yet available!
    __pychecker__ = "no-returnvalues"
    if useDummyAuthentication:
        return dummy_auth_engine.Dummy_Auth_Engine(authLogger)
    else:
        return django_auth_engine.DjangoAuthEngine(authLogger, alwaysAuthenticated)

