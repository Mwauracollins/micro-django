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
            match = pattern.match(path)
            if match:
                if isinstance(pattern.view, (list, tuple)):
                    # This is an included URLconf
                    new_path = path[match.end():]
                    for included_pattern in pattern.view:
                        sub_match = included_pattern.match(new_path)
                        if sub_match:
                            return included_pattern.view, sub_match.groupdict()
                else:
                    return pattern.view, match.groupdict()
        print("No match found")
        return None, None

class Path:
    def __init__(self, route, view, name=None):
        self.route = route
        self.view = view
        self.name = name
        self.pattern = re.compile(f'^{route}$')

    def match(self, path):
        return self.pattern.match(path)


def path(route, view, name=None):
    return Path(route, view, name=name)

def url(pattern, view):
    return URLPattern(pattern, view)


def include(arg):
    if isinstance(arg, str):
        return import_module(arg).urlpatterns
    else:
        return arg