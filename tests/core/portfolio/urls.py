from microdjango.urls import path
from portfolio import views

urlpatterns = [
    path('', views.home, name="home"),  # Changed from 'home/' to ''
]