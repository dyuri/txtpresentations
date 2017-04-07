from wsgi_app import app
from wsgiref.simple_server import make_server

s = make_server('', 9000, app)
s.serve_forever()
