from django import forms
from . import models
class BlogForm(forms.ModelForm):
    class Meta:
        model=models.Blog
        fields=['title','slug','body','image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        
        }