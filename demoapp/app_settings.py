from django.conf import settings

ACCESS_PASSWORD = getattr(settings, 'DEMO_ACCESS_PASSWORD', 'demo')
REQUIRE_PASSWORD = getattr(settings, 'DEMO_REQUIRE_PASSWORD', True)
LOGIN_URL = getattr(settings, 'DEMO_LOGIN_URL', '/demo-login/')
COOKIE_NAME = getattr(settings, 'DEMO_COOKIE_NAME', 'demo_session')
SALT_REQUEST_META_KEYS = getattr(
    settings, 'DEMO_SALT_REQUEST_META_KEYS', ['REMOTE_ADDR', 'REMOTE_HOST', 'HTTP_USER_AGENT'])
