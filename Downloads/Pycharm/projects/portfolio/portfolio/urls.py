from django.contrib import admin
from django.urls import path
from . import views
from django.shortcuts import render


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('workExperience/', views.workExperience, name='workExperience'),
    path('projects/', views.projects, name='projects'),
    path('education/', views.education, name='education'),
    path('contact/', views.contact_view, name='contact'),
]
