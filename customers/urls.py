"""Defines URL patterns for customers"""
from django.urls import path, include
from .import views


app_name = 'customers'
urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),  #the login and logout are in here 
    path('register/', views.register, name='register'),
    path('logout/', views.logout_page, name='logoutpage'),
    
]