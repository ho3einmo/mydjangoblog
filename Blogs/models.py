from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.jpg', blank=True, null=True)
    def __str__(self):
        
        return self.title + self.date.strftime(' %Y-%m-%d %H:%M:%S')
    
    def snippet(self):
        return self.body[:50] 