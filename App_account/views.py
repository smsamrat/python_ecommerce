from django.shortcuts import render

# Create your views here.

def userSign(request):
    return render(request,'app_account/signup.html')
