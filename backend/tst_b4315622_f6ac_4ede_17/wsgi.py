"""
WSGI config for tst_b4315622_f6ac_4ede_17 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "tst_b4315622_f6ac_4ede_17.settings"
)

application = get_wsgi_application()
