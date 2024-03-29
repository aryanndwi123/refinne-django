from django.shortcuts import render, HttpResponse,redirect
from coupons.models import Coupons
from coins.models import Coins
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login ,logout
from django.contrib import messages

import random

# Create your views here.
def home(request):
    allCoupons = Coupons.objects.all()
    username = request.user.username
    
    userCoins = Coins.objects.filter(username = username)
    
    
    if(User.objects.filter(username=username).exists() and request.user.profile.position == "owner"):
          data = True
    
    else:
        data = False
    
    
    context = {'data':data,'allCoupons': allCoupons,'userCoins':userCoins}
    
    return render(request,'home/home.html', context)






  

def search(request):
    query=request.GET['query']
    if len(query)>70:
        allCoupons = Coupons.objects.none()
    else:    
        allCouponsName = Coupons.objects.filter(name__icontains=query)
        allCouponsContent = Coupons.objects.filter(content__icontains=query)
        allCoupons = allCouponsName.union(allCouponsContent)
    
    username = request.user.username
    userCoins = Coins.objects.filter(username = username)   
    params = {'allCoupons': allCoupons, 'query' : query,'userCoins':userCoins }
    return render(request, 'home/search.html',params)

def cafesearch(request):
    query="one"       
    allCouponsName = Coupons.objects.filter(name__icontains=query)
    allCouponsContent = Coupons.objects.filter(content__icontains=query)
    allCoupons = allCouponsName.union(allCouponsContent)
    username = request.user.username
    userCoins = Coins.objects.filter(username = username)
    params = {'allCoupons': allCoupons, 'query' : query,'userCoins':userCoins}
    return render(request, 'categories/cafe.html',params)

def dinningsearch(request):
    query="dinning"       
    allCouponsName = Coupons.objects.filter(name__icontains=query)
    allCouponsContent = Coupons.objects.filter(content__icontains=query)
    allCoupons = allCouponsName.union(allCouponsContent)
    username = request.user.username
    userCoins = Coins.objects.filter(username = username)
    params = {'allCoupons': allCoupons, 'query' : query,'userCoins':userCoins}
    return render(request, 'categories/dinning.html',params)



def c_save(request):
    username = request.user.username
    password = request.user.password
    user = authenticate(username=username, password=password)
    if request.user.is_authenticated and request.user.profile.position == "owner":
        
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
            location = request.POST['location']
            if len(request.FILES ) != 0:
                image = request.FILES['image']
    
            
            c_save = Coupons(name=name,offer=offer,conditions=conditions,content=content,code=code,slug=slug,location=location,image=image)
            c_save.save()
         
            
        return render(request,'dashboard/dashboard.html')
    else:
        return redirect('/login')
    
    
    
        
        



def handleLogin(request):
     if request.method == 'POST':
        #change parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        
        user = authenticate(username=loginusername , password = loginpassword)
        
        if user is not None:
            login(request, user)
            messages.success(request, "succesfully Logged in")
            return redirect('/')
        else:
            messages.error(request,"Invalid credentials")
            return redirect('/login')
     return render(request,'home/login.html')   
 
 
def handleLogout(request):
    # if request.method == 'POST':
    logout(request)
    messages.success(request, "succesfully logout")
    return redirect('/')

def privacypolicy(request):
    return render(request,'home/privacypolicy.html')    
    

def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        # pass2 = request.POST.get('pass2')
        
        
        
        if len(username) < 5:
            messages.error(request,"Username is too short")
            return redirect('/signup')
        
        if pass1 != pass2:
            messages.error(request,"Password does not match") 
            print(pass1 , pass2)
            return redirect('/signup')
          
        if len(pass1) < 5:
            messages.error(request,"Password is too short")
            return redirect('/signup')
            
        
        myuser = User.objects.create_user(username=username,password=pass1)
        
        myuser.save()
        print("User created")
        user = authenticate(username=username , password = pass1)
        
        if user is not None:
            login(request, user)
            messages.success(request, "succesfully Logged in")
            return redirect('/')
    
    else:
      return render(request,'home/signup.html')  
  
  
def handleProfile(request):
    user = authenticate(username="mayasa", password="mayasa")
    if request.user.is_authenticated:
        username = request.user.username
        userCoins = Coins.objects.filter(username = username)
        
        params = {'userCoins':userCoins}
        return render(request,'profile/profile.html',params)
    else:
        return redirect('/login')
        
           
    
    


        
         

        
    

