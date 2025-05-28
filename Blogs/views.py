from django.shortcuts import render
from django.shortcuts import HttpResponse 
from . import models
# Create your views here.
def list(request):
    list_of_blogs = models.Blog.objects.all().order_by('-date')
    # return HttpResponse('Hello, world!')
    return render(request,'Blogs/list.html',{'list_of_blogs': list_of_blogs})
