from django.shortcuts import render,redirect
from .models import Product,Category
from django.contrib import messages

# Create your views here.

def store(request):
    return render(request,'app_store/store.html')

