django-demo
===========

Reusable app to protect access to project under development.

Installation
------------

pip install git+git://github.com/dboczek/django-demo.git

Setup
-----

In Django `settings.py`

1. add demoapp to `INSTALLED_APPS`
2. add `demoapp.middleware.PasswordMiddleware` to MIDDLEWARE_CLASSES after `django.middleware.locale.LocaleMiddleware` (if used)
3. run `python manage.py dbsync' or 'python manage.py migrate demoapp` if you're using South. 


Settings
--------
Look [app_settings.py](demoapp/app_settings.py) for available settings. 
