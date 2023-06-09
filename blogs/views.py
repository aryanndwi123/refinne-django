from django.shortcuts import render, HttpResponse,redirect
from coupons.models import Coupons
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login ,logout
from django.contrib import messages
import random
from django.db import models
from django.utils import timezone



def blogHome(request):
    return render('home/home.html')


