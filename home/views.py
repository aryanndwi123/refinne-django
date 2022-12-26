from django.shortcuts import render, HttpResponse
from coupons.models import Coupons
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
            uid = ' '.join([str(random.randint(0, 999)).zfill(3) for _ in range(2)])
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


    

