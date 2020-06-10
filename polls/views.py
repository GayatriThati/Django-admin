from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def home(request):
    context = {'name': 'Gayatri papa'}
    #return HttpResponse("Hello")
    return render(request,'polls/home.html',context) 

def house(request):
    context = {'name' : 'sahith babu'}
    return render(request,'polls/home.html',context)

def add(request):
    #num1 = int(request.GET["num1"])
    #num2 = int(request.GET["num2"])
    num1 = int(request.POST["num1"])
    num2 = int(request.POST["num2"])
    result = num1+num2
    context = {'result' : result}
    return render(request,'polls/add_result.html',context)


def product_detail_view(request):
    obj = Product.objects.get(id = 1)
    '''
    context = {'title' : obj.title,
               
               'price' : obj.price
               }
    '''
    context = {'object' : obj}
    return render(request,"polls/product_detail.html",context)