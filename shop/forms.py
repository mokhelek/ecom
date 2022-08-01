
from django import forms 
from .models import Blog
from tinymce.widgets import TinyMCE


class Blogform(forms.ModelForm):
    body = forms.CharField(widget= forms.Textarea(attrs={'cols': 10, 'rows':2}))
    title = forms.CharField(widget= forms.Textarea(attrs={'cols': 20, 'rows':2}))
    class Meta:
        model = Blog
        fields = ['title','body']
       