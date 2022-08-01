

from django.db import models
from django.contrib.auth.models import User

from tinymce.models import HTMLField

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length = 200, null = True )
    price = models.FloatField()
    digital = models.BooleanField(default = False ,null =True , blank =False)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
class Blog(models.Model):
    thumbnail = models.ImageField()
    date_created = models.DateField(auto_now=True)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    body = HTMLField()
    
    def __str__(self):
        return str(self.title)

    

