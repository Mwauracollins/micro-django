class View:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def dispatch(self, request, *args, **kwargs):
        handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        return handler(request, *args, **kwargs)

    def http_method_not_allowed(self, request, *args, **kwargs):
        from microdjango.http.response import HttpResponse  # Local import
        allowed_methods = [m.upper() for m in self.http_method_names if hasattr(self, m)]
        return HttpResponse(f"Method {request.method} not allowed.", status=405)
