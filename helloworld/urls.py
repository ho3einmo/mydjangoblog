from django.contrib import admin
from django.urls import path ,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',views.about),
    path('',views.home),
    path('Blogs/',include('Blogs.urls')),
    path('twiter/',include('twiter.urls')),
]

urlpatterns += staticfiles_urlpatterns()