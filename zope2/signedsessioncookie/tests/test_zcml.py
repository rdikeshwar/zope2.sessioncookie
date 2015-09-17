import unittest


class Test__doConfigure(unittest.TestCase):

    def _callFUT(self, *args, **kw):
        from zope2.signedsessioncookie.zcml import _doConfigure
        return _doConfigure(*args, **kw)

    def test_it(self):
        from zope.component import getUtility
        from ..config import SignedSessionCookieConfig
        from ..interfaces import ISignedSessionCookieConfig
        self._callFUT('SECRET', 'SALT', 'COOKIE', 1234,
                      '/foo', 'www.example.com', False, False)
        config = getUtility(ISignedSessionCookieConfig)
        self.assertTrue(isinstance(config, SignedSessionCookieConfig))
        self.assertEqual(config.secret, 'SECRET')
        self.assertEqual(config.salt, 'SALT')
        self.assertEqual(config.cookie_name, 'COOKIE')
        self.assertEqual(config.max_age, 1234)
        self.assertEqual(config.path, '/foo')
        self.assertEqual(config.domain, 'www.example.com')
        self.assertEqual(config.secure, False)
        self.assertEqual(config.http_only, False)


class Test_configureSSC(unittest.TestCase):

    def _callFUT(self, *args, **kw):
        from zope2.signedsessioncookie.zcml import configureSSC
        return configureSSC(*args, **kw)

    def test_it(self):
        from zope2.signedsessioncookie.zcml import _doConfigure
        context = _Context()
        self._callFUT(context, 'SECRET', 'SALT', 'COOKIE', 1234,
                      '/foo', 'www.example.com', False, False)
        self.assertEqual(len(context.actions), 1)
        args, kw = context.actions[0]
        self.assertEqual(args, ())
        self.assertEqual(kw, {
            'callable': _doConfigure,
            'discriminator': 'configureSSC',
            'args': ('SECRET', 'SALT', 'COOKIE', 1234,
                     '/foo', 'www.example.com', False, False),
        })



class _Context(object):
    def __init__(self):
        self.actions = []

    def action(self, *args, **kw):
        self.actions.append((args, kw))