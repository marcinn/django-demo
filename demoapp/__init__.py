__version__ = '1.0'

from demoapp import app_settings


def get_salt(request):
    salt = '.'.join([request.META[key] for key in app_settings.SALT_REQUEST_META_KEYS])
    print salt
    return salt
