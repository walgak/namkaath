from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),              # Fixes {% url 'home' %}
    path('services/', views.services, name='services'), # Fixes {% url 'services' %}
    path('portfolio/', views.portfolio, name='portfolio'), # Fixes {% url 'portfolio' %}
    path('contact/', views.contact, name='contact'),    # Fixes {% url 'contact' %}
]