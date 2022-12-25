from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home),
    path('search', views.search, name='search'),
    path('dashboard', views.c_save, name='coupons_detail'),
    
    
    
]
