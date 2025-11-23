"""
WSGI config for mysite project.

Exposes the WSGI callable as ``application`` and also provides `app` and `handler`
aliases for platforms that expect those names (e.g., Vercel).
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()

# Aliases expected by some serverless hosts (Vercel)
app = application
handler = application
