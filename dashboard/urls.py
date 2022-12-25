
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('coupons_activated', views.coupons_activated, name="coupons_activated"),
    path('verification', views.coup_verification),
   
    
]