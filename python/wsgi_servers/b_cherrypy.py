from cherrypy import wsgiserver
from wsgi_app import app

server = wsgiserver.CherryPyWSGIServer(('0.0.0.0', 9000), app,
                                       request_queue_size=500,
                                       server_name='localhost')

if __name__ == '__main__':
    try:
        server.start()
    except KeyboardInterrupt:
        server.stop()
