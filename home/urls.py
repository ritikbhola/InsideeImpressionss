from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from home import views

urlpatterns = [
    
    # path('home', views.index, name='home'),
    path('about', views.about, name='about'),
    path('gallery', views.gallery, name='gallery'),
    path('orders', views.orders, name='orders'),
    path('order1', views.order1, name='order1'),
    path('', views.index, name='home'),
] 