from django.shortcuts import render
from django.urls import path
from . import views

app_name = 'Blogs'
urlpatterns = [
    path('',views.list, name='list'),
    path('<slug>', views.detail, name='detail'),
]