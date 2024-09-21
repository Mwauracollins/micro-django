
from microdjango.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world!")
