
from django.shortcuts import render
from . models import *
from django.http import JsonResponse
import json

# Create your views here.
def shop(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()  # I HAVE SEEN THIS NOTATION SEVERAL TIMES
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items':0 , 'shipping' : False}
        cartItems =order['get_cart_items']

    products = Product.objects.all()
    context ={'products':products , 'cartItems':cartItems}
    return render(request, 'shop/shop.html', context)

def cart(request):
 
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()  # I HAVE SEEN THIS NOTATION SEVERAL TIMES
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items':0 , 'shipping' : False}

    context ={'items': items, 'order':order}
    return render(request, 'shop/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()  # I HAVE SEEN THIS NOTATION SEVERAL TIMES
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items':0, 'shipping' : False}

    context ={'items': items, 'order':order}
    return render(request, 'shop/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print("action:" , action)

    customer = request.user.customer
    product =Product.objects.get(id = productId)
    order , created = Order.objects.get_or_create(customer = customer, complete = False)
    orderItem , created = OrderItem.objects.get_or_create(order = order , product = product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)

    elif action == "remove":
        orderItem.quantity = (orderItem.quantity - 1)

    if orderItem.quantity <= 0:
        orderItem.delete()

    orderItem.save()
    return JsonResponse('item was added', safe = False)