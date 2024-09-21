from microdjango.urls import url, path, include

urlpatterns = [
    path('', include('portfolio.urls'))
]
