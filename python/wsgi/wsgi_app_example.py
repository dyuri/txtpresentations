# vim: foldmethod=marker

RESPONSE = 'Hello world!\n'.encode('latin1')  # bytes


# {{{ WSGI app function
def app_func(environ, start_response):
    """
    Simple WSGI app function
    """
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)

    return [RESPONSE, b' app_func']
# }}}


# {{{ WSGI app class
class AppClass(object):
    """
    Simple WSGI app class - iterable
    """

    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response

    def __iter__(self):
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)

        yield RESPONSE
        yield b' AppClass'
# }}}


# {{{ WSGI middleware
class PathMiddleware(object):

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        path = environ.get('PATH_INFO', '').strip('/')

        for res in self.app(environ, start_response):
            yield res

        yield b'\n\nPath: '+path.encode('latin-1')
# }}}


# {{{ main
if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    # s = make_server('', 9000, app_func)
    # s = make_server('', 9000, AppClass)
    s = make_server('', 9000, PathMiddleware(AppClass))

    s.serve_forever()
# }}}
