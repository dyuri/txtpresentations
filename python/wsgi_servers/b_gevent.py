from gevent import wsgi
from wsgi_app import app

wsgi.WSGIServer(('', 9000), app, spawn='default').serve_forever()
