from django.shortcuts import render
from django.shortcuts import HttpResponse 
from . import models
# Create your views here.
def list(request):
    list_of_blogs = models.Blog.objects.all().order_by('-date')
    # return HttpResponse('Hello, world!')
    return render(request,'Blogs/list.html',{'list_of_blogs': list_of_blogs})
def detail(request, slug):
    # return HttpResponse('This is the detail page for blog: ' + slug)
    blog = models.Blog.objects.get(slug=slug)
    return render(request, 'Blogs/detail.html', {'blog': blog })