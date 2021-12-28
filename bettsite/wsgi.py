"""
WSGI config for bettsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import eventlet
from engineio.static_files import get_static_file
import socketio
from django.core.wsgi import get_wsgi_application
from django.conf import settings
#from gevent import pywsgi
from django.contrib.staticfiles.handlers import StaticFilesHandler
from England.views import sio


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bettsite.settings')
application = get_wsgi_application()
app = socketio.WSGIApp(sio,application)




import eventlet.wsgi
eventlet.wsgi.server(eventlet.listen(('0.0.0.0',00000)),app)


#pywsgi.WSGIServer(('localhost',8000), app).serve_forever()