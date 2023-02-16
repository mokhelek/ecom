

from django.db import models
from django.contrib.auth.models import User

from tinymce.models import HTMLField

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=150)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length = 200, null = True )
    price = models.FloatField()
    description = models.TextField( default="product description not provided")
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null =True , blank =True)
    digital = models.BooleanField(default = False ,null =True , blank =False)
    featured = models.BooleanField(default=False)
    
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

    
class Headline(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.title
