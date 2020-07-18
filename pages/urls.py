from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'pages'

urlpatterns = [
    
    path('', views.index_view, name="home"),
    path('contact/', views.contact_view, name="contact"),
    path('about/', views.about_view, name="about"),
    path('privacy', views.privacy_view, name="privacy"),
    
]