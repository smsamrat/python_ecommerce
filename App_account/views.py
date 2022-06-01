from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# Create your views here.

def userSign(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(data = request.POST)
        if form.is_valid():  
            form.save()
            messages.success(request,"Account Created Successfully")
            return redirect('login')
    return render(request,'app_account/signup.html',context={'form':form})

def userlogin(request):
    form =AuthenticationForm()
    if request.method == "POST":
        form =AuthenticationForm(request,data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
            return redirect('store')
    return render(request,'app_account/login.html',context={'form':form})

def userlogout(request):
    logout(request)
    messages.warning(request,"You are logged Out")
    return redirect('login')
