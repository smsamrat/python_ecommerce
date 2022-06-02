from django.shortcuts import render,redirect
from .models import Product,Category
from django.contrib import messages

# Create your views here.

def store(request):
    products = Product.objects.all()
    context ={
         'object_list': products
    }
    return render(request,'app_store/store.html',context)

def product_fetch_by_category(request, slug):
    if (Category.objects.filter(slug = slug)):
        products = Product.objects.filter(category__slug = slug)
        return render(request,'app_store/store.html',context={'object_list':products})
    else:
        messages.warning(request,'Product is not available')
        return redirect('store')

def product_details(request,cat_slug,prod_slug):
    if(Category.objects.filter(slug=cat_slug)):
        if(Product.objects.filter(slug=prod_slug)):
            products = Product.objects.filter(slug=prod_slug).first()
    return render(request,'app_store/product_details.html',context={'single_product':products})
