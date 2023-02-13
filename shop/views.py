
from multiprocessing import context
from django.shortcuts import render
from . models import *
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required
from customers.models import *

import datetime

# Create your views here.
def shop(request):
    categories = Category.objects.all()

    if request.user.is_authenticated:  #if user has logged in ...!
        ads = Headline.objects.all()
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()  # I HAVE SEEN THIS NOTATION SEVERAL TIMES
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items':0 , 'shipping' : False}
        cartItems =order['get_cart_items']

    products = Product.objects.all()
    context ={'products':products , 'cartItems':cartItems,"ads":ads, "categories":categories }
    return render(request, 'shop/shop.html', context)

@login_required
def cart(request):
 
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()  
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items':0 , 'shipping' : False}
        cartItems =order['get_cart_items']

    context ={'items': items, 'order':order, }
    return render(request, 'shop/cart.html', context)

@login_required
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()  # I HAVE SEEN THIS NOTATION SEVERAL TIMES
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items':0, 'shipping' : False}
        cartItems =order['get_cart_items']

    context ={'items': items, 'order':order, "cartItems":cartItems}
    return render(request, 'shop/checkout.html', context)

@login_required
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user.customer
    product =Product.objects.get(id = productId)
    order , created = Order.objects.get_or_create(customer = customer, complete = False)

    orderItem , created = OrderItem.objects.get_or_create(order = order , product = product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)

    elif action == "remove":
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()

    
    return JsonResponse('item was added', safe = False)

@login_required
def processOrder(request):
     transaction_id = datetime.datetime.now.timestamp()

     if request.user.is_authenticated:
         data =json.loads(request.body)
         customer =request.user.customer
         order,created =Order.objects.get_or_create(customer = customer , complete =False)
         total = float(data['form']['total'])
         order.transaction_id = transaction_id
         if total == order.get_cart_total:
             order.complete =True
         order.save()
         #if order.shipping ==True :

     else:
         print("user is not logged in ..")

     return JsonResponse('payment complete', safe = False)
 

def viewCategory(request,category_id ):
    category = Category.objects.get(id = category_id)
    categoryProducts = category.product_set.all()
    context = {
        "categoryProducts":categoryProducts,
        "category":category, 
    }
    return render(request, 'shop/viewCategory.html', context)



def posts(request):
    posts = Blog.objects.all().order_by("-date_created")
    
    context = {"posts":posts}
     
    return render(request,"shop/blog_list.html",context)

def read_post(request,post_id):
    read_post = Blog.objects.get(id = post_id)
    context = {"read_post":read_post}
    
    return render(request,"shop/read_post.html",context)
