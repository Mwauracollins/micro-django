from microdjango.http import HttpResponse

# Create your views here
def home(request):
    return HttpResponse("Welcode to my page")
