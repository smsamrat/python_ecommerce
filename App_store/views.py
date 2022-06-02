from django.shortcuts import render
from .models import Product,Category

# Create your views here.

def store(request):
    products = Product.objects.all()
    context ={
         'object_list': products
    }
    return render(request,'app_store/store.html',context)
