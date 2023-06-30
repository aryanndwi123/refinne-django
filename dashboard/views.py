from django.shortcuts import render, HttpResponse,redirect
from coupons.models import Coupons
from owner.models import Profile
from django.db.models import FloatField
from django.db.models.functions import Cast
from coins.models import Coins
import random
from django.contrib import messages
from django.contrib.auth import authenticate 
from django.contrib.auth.models import User

def dashboard(request):
    username = request.user.username
    password = request.user.password
    owner = request.user.profile.position
    user = authenticate(username=username, password=password)
    if request.user.is_authenticated and owner == True:
        print(owner)
 
        return render(request,'dashboard/dashboard.html')
    else:
        return redirect('/login')
    
    
   
    
    

def coup_verification(request):
    username = request.user.username
    password = request.user.password
    user = authenticate(username=username, password=username)
    if request.user.is_authenticated:
 
        if request.method=='POST':
            verificationcode = request.POST['verificationcode']
            name = request.POST['name']
            username = request.POST['username']
            
            
            
            code_entry = Coupons.objects.filter(name = name).values('code')
            
            #Coins authentication
            if User.objects.filter(username=username).exists() and Coins.objects.filter(username = username).exists():
                user_coins = Coins.objects.filter(username = username).values('coins')
                user_coins = Coins.objects.annotate(as_float=Cast('coins', FloatField())).get()
                coupons_coins = Coupons.objects.filter(name = name).values('coins')
                coupons_coins = Coupons.objects.annotate(as_float=Cast('coins', FloatField())).get()

                user_coins = user_coins.as_float + coupons_coins.as_float
                total_coins = Coins.objects.get(username=username)
                total_coins.coins = user_coins
                total_coins.save()
                
            
  
            
            
            
            if code_entry[0]['code'] == verificationcode and User.objects.filter(username=username).exists() :
                
                
                coupons = Coupons.objects.get(name = name)
                while True:
                    uid = ''.join([str(random.randint(0, 999)).zfill(3) for _ in range(2)])
                    try:
                        coupons.code=uid            
                        break
                    except:
                        continue
                
                coupons.save()
                messages.success(request,'verified')
            
        else:
             
            messages.error(request,'unverified')
        
        return render(request,'dashboard/coup_verification/coup_verification.html')
        
    else:
        return redirect('/login')
      
        
   
    
    


def coupons_activated(request):
   
    
    return render(request,'dashboard/coupons_activated.html')


 
