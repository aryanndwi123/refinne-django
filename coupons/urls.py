from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.couponsHome),
    path('<str:slug>', views.couponsPost),
   
    
]
