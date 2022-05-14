from django.urls import path 
from . import views


app_name ="shop"

urlpatterns = [ 
    path("", views.shop , name = "shop"),
    path("cart/", views.cart , name = "cart"),
    path("checkout/", views.checkout , name = "checkout"),

    path("update_item/", views.updateItem, name ="update_Item")
]