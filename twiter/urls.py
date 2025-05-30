from django.shortcuts import render
from django.urls import path
from . import views

app_name = 'twiter'
urlpatterns = [
    path('',views.list),
    path('post/',views.post, name='post'),
    path('<slug>', views.detail, name='detail'),
]