"""
ASGI config for mysite project.
Provides `application` and aliases `app` and `handler` for compatibility.
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_asgi_application()

# aliases
app = application
handler = application
