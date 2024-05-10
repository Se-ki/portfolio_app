from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('gallery/', views.gallery, name="gallery"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
]
