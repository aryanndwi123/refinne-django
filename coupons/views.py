from django.shortcuts import render, HttpResponse
from coupons.models import Coupons

# Create your views here.
def couponsHome(request):
    allCoupons = Coupons.objects.all()
    
    context = {'allCoupons': allCoupons}
    
    return render(request,'coupons/couponsHome.html', context)


def search(request):
    query=request.GET['query']
    if len(query)>70:
        allCoupons = Coupons.objects.none()
    else:    
        allCouponsTitle = Coupons.objects.filter(title__icontains=query)
        allCouponsContent = Coupons.objects.filter(content__icontains=query)
        allCoupons = allCouponsTitle.union(allCouponsContent)
    params = {'allCoupons': allCoupons, 'query' : query}
    return render(request, 'home/search.html',params)



def couponsPost(request,slug):
    one_entry = Coupons.objects.filter(slug = slug)
    
    context = {'one_entry': one_entry}
    
    
    return render(request,'coupons/couponsPost.html',context)