import os.path
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException
from werkzeug.utils import redirect
from werkzeug.wsgi import SharedDataMiddleware
import jinja2


templateLoader = jinja2.FileSystemLoader('templates')
templateEnv = jinja2.Environment(loader=templateLoader)


def hello(request, name='World'):
    message = 'Hello ' + name + '!'
    if request.accept_mimetypes.best == 'text/html':
        # for browsers
        template = templateEnv.get_template('hello.html')
        response = Response(template.render(title=message, name=name),
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
        template = templateEnv.get_template('helloform.html')
        return Response(
            template.render(),
            mimetype='text/html'
        )


URL_MAP = Map([
    Rule('/', endpoint=hello),
    Rule('/hello', endpoint=hello),
    Rule('/hello/<name>', endpoint=hello),
    Rule('/sayhello', endpoint=helloform),
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
