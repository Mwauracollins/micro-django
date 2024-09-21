import re
from importlib import import_module


class URLPattern:
    def __init__(self, pattern, view):
        self.pattern = re.compile(pattern)
        self.view = view


class URLResolver:
    def __init__(self, urlpatterns):
        self.urlpatterns = urlpatterns

    def resolve(self, path):
        print(f"Resolving path: {path}")
        for pattern in self.urlpatterns:
            print(f"Checking pattern: {pattern}")
            if isinstance(pattern, Path):
                match = pattern.match(path)
                if match:
                    if callable(pattern.view):
                        return pattern.view, match.groupdict()
                    elif isinstance(pattern.view, (list, tuple)):
                        # This is an included URLconf
                        sub_resolver = URLResolver(pattern.view)
                        sub_path = path[match.end():]
                        sub_match = sub_resolver.resolve(sub_path if sub_path else '/')
                        if sub_match:
                            return sub_match
            elif isinstance(pattern, URLPattern):
                match = pattern.pattern.match(path)
                if match:
                    return pattern.view, match.groupdict()
        print("No match found")
        return None, None

class Path:
    def __init__(self, route, view, name=None):
        self.route = route
        self.view = view
        self.name = name
        self.pattern = re.compile(f'^{route}')  # Remove $ to allow matching of sub-paths

    def match(self, path):
        return self.pattern.match(path)

    def __str__(self):
        return f"Path('{self.route}', {self.view}, name='{self.name}')"


def path(route, view, name=None):
    return Path(route, view, name=name)

def url(pattern, view):
    return URLPattern(pattern, view)


def include(arg):
    if isinstance(arg, str):
        module = import_module(arg)
        return getattr(module, 'urlpatterns', [])
    return arg if isinstance(arg, (list, tuple)) else [arg]