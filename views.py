from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import JsonResponse
from django.core import serializers
from datetime import datetime

# Create your views here.
from django.http import HttpResponse
from pages.models import tehnia

def homePageView(request):
    return HttpResponse('Hello, World!')

def datafromlogin(request):
    getname=tehnia.objects.values_list('name', flat=True).distinct()
    getname= list(getname)
    print('cvdvdfdf')
    print(getname)
    print (type(getname))
    return render_to_response('index.html', {'getname':getname})



def getdata(request):
    print('EFDCDFGDTG')
    name = request.GET.get('name', None)
    print('&*&*&*&*')
    print(name)
    today = datetime.now()
    
    products = tehnia.objects.filter(created__year=today.year, created__month=today.month).values_list('name','height','weight')
    curmonth=list(products)
    print('######33')
    print(curmonth)
    for i in curmonth:
        print(i)
    myheight=tehnia.objects.filter(name__contains=name).values_list('height', flat=True)
    myweight=tehnia.objects.filter(name__contains=name).values_list('weight', flat=True)
    h_objects = list(myheight)
    w_objects = list(myweight)
    data = {
        'height': h_objects ,
        'weight': w_objects 
        }
    return JsonResponse(data)
