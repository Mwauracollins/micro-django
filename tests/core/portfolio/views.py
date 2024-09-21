from microdjango.http import HttpResponse

# Create your views here
def home(request):
    return HttpResponse('Hello world this is microdjango')