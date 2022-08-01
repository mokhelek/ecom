from django.db.models.signals import post_save
from .models import *
from customers.models import *
from django.contrib.auth.models import User

from django.dispatch import receiver

@receiver(post_save,sender=User)
def create_customer(sender,instance,created,**kwargs):
    if created:
        Customer.objects.create(user=instance)
