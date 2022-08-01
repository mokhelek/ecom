
from shop.models import *
from customers.models import *


def cartItems(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer = customer, complete = False)
      
        cartItems = order.get_cart_items
        return {"cartItems":cartItems}
    
    else:
        return {}