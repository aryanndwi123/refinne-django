from django.shortcuts import render
from coupons.models import Coupons
import random
from django.contrib import messages

def dashboard(request):
   
    
    return render(request,'dashboard/dashboard.html')

def coup_verification(request):
    if request.method=='POST':
        verificationcode = request.POST['verificationcode']
        name = request.POST['name']
        print(verificationcode,name)
        
        
        code_entry = Coupons.objects.filter(name = name).values('code')    
        
        
        
        if code_entry[0]['code'] == verificationcode:
            
            
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


def coupons_activated(request):
   
    
    return render(request,'dashboard/coupons_activated.html')


 
