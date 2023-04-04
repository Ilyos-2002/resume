from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resume.html/', views.resume, name='resume'),
    path('portfolio.html/', views.portfolio, name='portfolio'),
    path('contact.html/', views.contact, name='contact'),

]
