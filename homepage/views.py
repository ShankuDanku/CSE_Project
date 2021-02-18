from django.shortcuts import render
from scrapers import ebay,Amazon,snapdeal,ajio
from filters import basic

def HomePage(request):
    if request.method=='POST' and request.POST.get('search'):
       print(request.POST)
       data=[]
       data=Amazon.amazon(request.POST['search'])
       data.extend(ebay.ebay(request.POST['search']))
       #data.extend(snapdeal.snapdeal(request.POST['search']))
       data.extend(ajio.ajio(request.POST['search']))
       if request.POST['min']=='':
           mi=0
       else:
           mi=int(request.POST['min'])
       if request.POST['max']=='':
           ma=None
       else:
           ma=int(request.POST['max'])
       data=basic.minmax(data,mi,ma)
       if request.POST.get('asc')=='on':
           data=basic.sortascending(data)
       elif request.POST.get('desc')=='on':
           data=basic.sortascending(data)
           data.reverse()
       if request.POST.get('misc'):
            data=basic.misc(data,request.POST.get('misc'))
       return render(request,'homepage/HomePage.html',{'data':data})
    else:
        print(request.POST)
        return render(request,'homepage/HomePage.html')
def about(request):
    return render(request,'homepage/about.html')