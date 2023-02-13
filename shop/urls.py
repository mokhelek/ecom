from django.urls import path 
from . import views


app_name ="shop"

urlpatterns = [ 
    path("", views.shop , name = "shop"),
    path("cart/", views.cart , name = "cart"),
    path("checkout/", views.checkout , name = "checkout"),

    path("update_item/", views.updateItem, name ="update_Item"),
    path("process_order/", views.processOrder, name ="update_Item"),
    
    path("posts/", views.posts, name ="posts"),
    path("read_post/<int:post_id>/", views.read_post, name ="read_post"),
    path("viewCategory/<int:category_id>/", views.viewCategory, name ="viewCategory"),
]