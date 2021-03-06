Changelog
=========

0.7 (unreleased)
----------------

- Add script for uninstalling the root traversal hook (PR #2).

0.6.1 (2015-12-08)
------------------

- Packaging bug:  add missing ``MANIFEST.in``.

0.6 (2015-11-23)
----------------

- Transferred copyright to Zope Foundation, relicensed to ZPL 2.1.

- Rename from ``zope2.signedsessioncookie`` -> ``zope2.sessioncookie``.

- Replace locally-defined ``EncryptingPickleSerialzer`` with
  ``pyramid_nacl_session.EncryptedSerializer``.  Closes #8 and #9.

0.5 (2015-10-08)
----------------

- Add support for (optionally) encrypting session cookies, rather than
  signing them.

0.4 (2015-10-05)
----------------

- Add an attribute, ``signedsessioncookie_installed``, to the root object
  during installation.

0.3 (2015-09-30)
----------------

- Fix rendering ``http_only`` cookie attribute.

0.2 (2015-09-29)
----------------

- Add support for extra Pyramid session configuration via ZCML:
  ``hash_algorithm``, ``timeout``, ``reissue_time``.

- Suppress empty / None values in cookie attributes passed to
  ``ZPublisher.HTTPResponse.setCookie``.

- Refactor install script to allow reuse from other modules.

- Fix compatibility w/ ``zope.configuration 3.7.4``.

0.1 (2015-09-18)
----------------

- Initial release.

