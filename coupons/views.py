from django.shortcuts import render, HttpResponse
from coupons.models import Coupons
from coins.models import Coins
from django.contrib.auth.models import User

# Create your views here.
def couponsHome(request):
    allCoupons = Coupons.objects.all()
    username = request.user.username
    userCoins = Coins.objects.filter(username = username)
    if(User.objects.filter(username=username).exists() and request.user.profile.position == "owner"):
          data = True
    
    else:
        data = False
    
    
    context = {'data':data,'allCoupons': allCoupons,'userCoins':userCoins}
    
    return render(request,'coupons/couponsHome.html', context)


def search(request):
    query=request.GET['query']
    if len(query)>70:
        allCoupons = Coupons.objects.none()
    else:    
        allCouponsTitle = Coupons.objects.filter(title__icontains=query)
        allCouponsContent = Coupons.objects.filter(content__icontains=query)
        allCoupons = allCouponsTitle.union(allCouponsContent)
        username = request.user.username
        userCoins = Coins.objects.filter(username = username)
    params = {'allCoupons': allCoupons, 'query' : query,'userCoins':userCoins}
    return render(request, 'home/search.html',params)



def couponsPost(request,slug):
    one_entry = Coupons.objects.filter(slug = slug)
    username = request.user.username
    userCoins = Coins.objects.filter(username = username)
    
    context = {'one_entry': one_entry,'userCoins':userCoins}
    
    
    return render(request,'coupons/couponsPost.html',context)