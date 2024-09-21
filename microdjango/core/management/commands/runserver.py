import os
from wsgiref.simple_server import make_server
from ...handlers import get_wsgi_application


def run_server(addr='localhost', port=8000):
    os.environ.setdefault("MICRODJANGO_SETTINGS_MODULE", "myproject.settings")
    application = get_wsgi_application()

    with make_server(addr, port, application) as httpd:
        print(f"Serving on http://{addr}:{port}")
        httpd.serve_forever()