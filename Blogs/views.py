from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse 
from . import models
from . import forms
# Create your views here.
def list(request):
    list_of_blogs = models.Blog.objects.all().order_by('-date')
    # return HttpResponse('Hello, world!')
    return render(request,'Blogs/list.html',{'list_of_blogs': list_of_blogs})
def detail(request, slug):
    # return HttpResponse('This is the detail page for blog: ' + slug)
    blog = models.Blog.objects.get(slug=slug)
    return render(request, 'Blogs/detail.html', {'blog': blog })

@login_required(login_url="/accounts/login")
def create(request):
    if request.method == 'POST':
        form = forms.BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('Blogs:list')
    else:
            form = forms.BlogForm()   
    return render(request, 'Blogs/create.html', { 'form': form})