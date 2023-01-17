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

def signup(request):
    if request.method == 'POST':
        #change parameters
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        fname = request.POST['fname']
        lname = request.POST['lname']
        age = request.POST['age']
        pnumber = request.POST['pnumber']
        email = request.POST['email']
        
    
        
        #Check for error inputs
        if len(username) > 10:
            messages.error(request, "Username Must be under 10 characters")
            return redirect('home')
        
        if pass1 != pass2 :
            messages.error(request, "passwords do not match")
            return redirect("home")
        
        
        
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "SUCESSFULLY CREATED ACCOUNT")
        
    return render(request,'s_base.html')
    
    
            
    
        
        
    
            
    
    


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
            return redirect('coupons')
     return render(request,'l_base.html')   
 
 
def handleLogout(request):
    # if request.method == 'POST':
    logout(request)
    messages.success(request, "succesfully logout")
    return redirect('home')
    
    return HttpResponse('handleLogout')

        
    

