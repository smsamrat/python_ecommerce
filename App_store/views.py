from sre_parse import CATEGORIES
from unicodedata import category
from django.shortcuts import render,redirect
from .models import Product,Category
from django.contrib import messages

# Create your views here.

def store(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request,'app_store/store.html',context)

def categoryfetchItem(request,slug):

    if(Category.objects.filter(slug=slug)):
        products = Product.objects.filter(category__slug=slug)
        context = {
        'products': products
    }
        return render(request,'app_store/store.html',context)
    else:
        messages.warning(request,'Product is not available')
        return render(request,'app_store/store.html')