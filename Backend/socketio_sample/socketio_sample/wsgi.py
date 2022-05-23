"""
WSGI config for socketio_sample project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import socketio
from server import sio

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "socketio_sample.settings")

djanngo_app = get_wsgi_application()

application = socketio.WSGIApp(sio, djanngo_app)
import eventlet
import eventlet.wsgi

eventlet.wsgi.server(eventlet.listen(("", 8000)), application)
