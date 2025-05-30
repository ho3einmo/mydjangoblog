from django.shortcuts import render
from django.shortcuts import HttpResponse
from . import models
# Create your views here.
def list(request):
    return HttpResponse("This is the list of tweets")
def post(request):
    post_text = models.Tweet.objects.all()
    return render(request, 'twiter/post.html', {'post_text': post_text})
def detail(request, slug):
    return HttpResponse('This is the detail page for tweet: ' + slug)