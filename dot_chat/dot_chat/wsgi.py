"""
WSGI config for dot_chat project.
"""

import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "dot_chat.settings"
)


application = get_wsgi_application()