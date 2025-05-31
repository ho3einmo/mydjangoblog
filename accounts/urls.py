from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.sign_up, name='sing_up'),
]