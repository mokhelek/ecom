from django.contrib import admin
from . models import *
from customers.models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Blog)
admin.site.register(Category)

admin.site.register(Headline)

