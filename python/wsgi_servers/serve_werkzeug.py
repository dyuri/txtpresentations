from wsgi_app import app
from werkzeug.serving import run_simple

run_simple('', 9000, app, use_reloader=True, use_debugger=True)
