import tornado.httpserver
import tornado.ioloop
import tornado.wsgi
from wsgi_app import app


def main():
    container = tornado.wsgi.WSGIContainer(app)
    http_server = tornado.httpserver.HTTPServer(container)
    http_server.listen(9000)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
