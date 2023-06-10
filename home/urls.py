from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('search', views.search, name='search'),
    path('cafe', views.cafesearch, name='cafesearch'),
    path('dinning', views.dinningsearch, name='dinningsearch'),    
    path('dashboard', views.c_save, name='coupons_detail'),
    path('signup', views.handleSignup, name='signup'),
    path('login', views.handleLogin, name='login'),
    path('logout', views.handleLogout, name='logout'),
    path('profile', views.handleProfile, name='logout'),
    path('privacypolicy', views.privacypolicy, name='privacypolicy'),
    
  
    
    
    
    
]
