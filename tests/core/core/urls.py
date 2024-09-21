from microdjango.urls import path, include

urlpatterns = [
    path('', include('portfolio.urls')),
]
