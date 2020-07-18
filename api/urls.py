from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'api'

urlpatterns = [
    
    path('', views.index, name="home"),
    path('predict', views.predict, name="predict")
]