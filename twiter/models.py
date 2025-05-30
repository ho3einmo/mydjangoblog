from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tweet(models.Model):
    text = models.CharField(max_length=480)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        
        return self.text[:50] + self.created_at.strftime(' %Y-%m-%d %H:%M:%S')