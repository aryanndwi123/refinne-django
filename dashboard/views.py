from django.shortcuts import render, HttpResponse,redirect
from coupons.models import Coupons
import random
from django.contrib import messages
from django.contrib.auth import authenticate 
from django.contrib.auth.models import User

def dashboard(request):
    user = authenticate(username="mayasa", password="mayasa")
    if request.user.is_authenticated:
 
        return render(request,'dashboard/dashboard.html')
    else:
        return redirect('/login')
    
    
   
    
    

def coup_verification(request):
    user = authenticate(username="mayasa", password="mayasa")
    if request.user.is_authenticated:
 
        if request.method=='POST':
            verificationcode = request.POST['verificationcode']
            name = request.POST['name']
            username = request.POST['username']
            
            
            
            code_entry = Coupons.objects.filter(name = name).values('code')
            
  
            
            
            
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


 
