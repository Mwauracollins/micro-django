from importlib import import_module
import os
from urllib.parse import parse_qs

from microdjango.http.response import HttpResponse
from microdjango.urls.resolvers import URLResolver


class MicroDjango:
    def __init__(self, settings_module):
        self.settings = import_module(settings_module)
        self.urlconf = import_module(self.settings.ROOT_URLCONF)
        self.url_resolver = URLResolver(self.urlconf.urlpatterns)

    def get_response(self, request):
        view, kwargs = self.url_resolver.resolve(request.path)
        print(f"Resolved view: {view}")
        print(f"Resolved kwargs: {kwargs}")
        if view:
            return view(request, **kwargs)
        return HttpResponse("Not Found", status_code=404)
class WSGIHandler:
    def __init__(self, application):
        self.application = application

    def __call__(self, environ, start_response):
        request = WSGIRequest(environ)
        response = self.application.get_response(request)
        start_response(f"{response.status_code} {response.reason_phrase}", list(response.headers.items()))
        return [response.content.encode('utf-8')]

class WSGIRequest:
    def __init__(self, environ):
        self.environ = environ
        self.method = environ['REQUEST_METHOD']
        self.path = environ['PATH_INFO']
        self.GET = parse_qs(environ['QUERY_STRING'])
def get_wsgi_application():
    os.environ.setdefault("MICRODJANGO_SETTINGS_MODULE", "myproject.settings")
    application = MicroDjango(os.environ["MICRODJANGO_SETTINGS_MODULE"])
    return WSGIHandler(application)