from django.shortcuts import render, HttpResponse,redirect
from coupons.models import Coupons
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login ,logout
from django.contrib import messages

import random

# Create your views here.
def home(request):
    allCoupons = Coupons.objects.all()
    
    context = {'allCoupons': allCoupons}
    
    return render(request,'home/home.html', context)


  

def search(request):
    query=request.GET['query']
    if len(query)>70:
        allCoupons = Coupons.objects.none()
    else:    
        allCouponsName = Coupons.objects.filter(name__icontains=query)
        allCouponsContent = Coupons.objects.filter(content__icontains=query)
        allCoupons = allCouponsName.union(allCouponsContent)
    params = {'allCoupons': allCoupons, 'query' : query}
    return render(request, 'home/search.html',params)

def c_save(request):
    
    if request.method=='POST':
        name = request.POST['name']
        offer = request.POST['offer']
        conditions = request.POST['conditions']
        while True:
            uid = ''.join([str(random.randint(0, 999)).zfill(3) for _ in range(2)])
            try:
                code=uid            
                break
            except:
                continue
        
        slug = request.POST['slug']
        content = request.POST['content']
        
        c_save = Coupons(name=name,offer=offer,conditions=conditions,content=content,code=code,slug=slug)
        c_save.save()
         
            
    return render(request,'dashboard/dashboard.html')



def handleLogin(request):
     if request.method == 'POST':
        #change parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        
        user = authenticate(username=loginusername , password = loginpassword)
        
        if user is not None:
            login(request, user)
            messages.success(request, "succesfully Logged in")
            return redirect('home')
        else:
            messages.error(request,"Invalid credentials")
            return redirect('home')
     return render(request,'home/login.html')   
 
 
def handleLogout(request):
    # if request.method == 'POST':
    logout(request)
    messages.success(request, "succesfully logout")
    return redirect('home')
    
    

def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        age = request.POST['age']
        pnumber = request.POST['pnumber']
        pass1 = request.POST['pass1']
        
        pass2 = request.POST.get('pass2', False)
        
        if len(username) < 10:
            messages.error(request,"Username is too short")
            return redirect('home/signup.html')
        
        if pass1 != pass2:
            messages.error(request,"Password does not match") 
            return redirect('home/signup.html')
          
        if len(pass1) < 5:
            messages.error(request,"Password is too short")
            return redirect('home/signup.html')
            
        
        myuser = User.objects.create_user(username=username,email=email,password=pass1,first_name=fname,last_name=lname)
        myuser.first_name =fname
        myuser.last_name = lname
        myuser.save()
        print("User created")
        return HttpResponse('done') 
    
    else:
      return render(request,'home/signup.html')       
    
    


        
         

        
    

