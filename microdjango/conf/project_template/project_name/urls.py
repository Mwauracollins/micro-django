from microdjango.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
]
