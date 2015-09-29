from zope.interface import implementer

from .interfaces import ISignedSessionCookieConfig

@implementer(ISignedSessionCookieConfig)
class SignedSessionCookieConfig(object):

    def __init__(self, 
                 secret,
                 salt=None,
                 cookie_name='session',
                 max_age=None,
                 path=None,
                 domain=None,
                 secure=True,
                 http_only=True,
                ):
        self.secret = secret
        self.salt = salt
        self.cookie_name = cookie_name
        self.max_age = max_age
        self.path = path
        self.domain = domain
        self.secure = secure
        self.http_only = http_only

    def getCookieAttrs(self):
        """-> dict for configuring the Pyramid session cookie class."""
        result = dict([(key, value) for key, value in self.__dict__.items()
                       if value is not None])
        result['httponly'] = result.pop('http_only')
        return result
