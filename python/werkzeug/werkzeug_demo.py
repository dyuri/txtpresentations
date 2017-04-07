import os.path
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException
from werkzeug.utils import redirect
from werkzeug import secure_filename
from werkzeug.wsgi import SharedDataMiddleware


def hello(request, name='World'):
    message = 'Hello ' + name + '!'
    if request.accept_mimetypes.best == 'text/html':
        # for browsers
        response = Response('<h1>' + message + '</h1>',
                            mimetype='text/html')
    elif request.accept_mimetypes.best == 'application/json':
        # httpie --json
        response = Response('{"message": "' + message + '"}',
                            mimetype='application/json')
    else:
        # httpie / wget
        response = Response(message)

    return response


def helloform(request):
    name = None
    if request.method == 'POST':
        name = request.form['name']
        url = '/hello/'+name if name else '/hello'

        return redirect(url)
    else:
        return Response(
            '''
<form action="" name="upload" method="POST">
    <input type="text" name="name"/>
    <button>Go</button>
</form>
            ''',
            mimetype='text/html'
        )


def upload(request):
    name = None
    file = None
    if request.method == 'POST':
        name = secure_filename(request.form['name'])
        file = request.files['file']

        file.save(
            os.path.join(
                os.path.join(
                    os.path.dirname(__file__),
                    'static'
                ),
                name
            )
        )

        url = '/static/'+name

        return redirect(url)
    else:
        return Response(
            '''
<form action="" name="upload" method="POST" enctype="multipart/form-data">
    <input type="text" placeholder="name" name="name"/>
    <input type="file" placeholder="file" name="file"/>
    <button>Go</button>
</form>
            ''',
            mimetype='text/html'
        )


URL_MAP = Map([
    Rule('/', endpoint=hello),
    Rule('/hello', endpoint=hello),
    Rule('/hello/<name>', endpoint=hello),
    Rule('/sayhello', endpoint=helloform),
    Rule('/upload', endpoint=upload),
])


def dispatch(request):
    adapter = URL_MAP.bind_to_environ(request.environ)
    try:
        endpoint, values = adapter.match()
        return endpoint(request, **values)
    except HTTPException as e:
        return e


def application(environ, start_response):
    request = Request(environ)
    response = dispatch(request)

    return response(environ, start_response)

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('', 9000,
               SharedDataMiddleware(application, {
                   '/static': os.path.join(os.path.dirname(__file__), 'static')
               }),
               use_debugger=True, use_reloader=True)
