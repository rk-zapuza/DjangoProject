from django.contrib import admin
from django.urls import path, include
from Home import views
import Home

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
]