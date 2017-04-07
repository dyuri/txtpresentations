# vim: foldmethod=marker

RESPONSE = 'Hello world!\n'.encode('latin1')  # bytes


# {{{ WSGI app function
def app(environ, start_response):
    """
    Simple WSGI app function
    """

    path = environ.get('PATH_INFO', '').strip('/')

    if path == 'EX':
        raise Exception('Test exception')

    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)

    return [RESPONSE]
# }}}
