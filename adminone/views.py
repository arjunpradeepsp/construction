from cmath import log
from django.shortcuts import render

# Create your views here.
def fnHome(request):
    return render(request,'home.html')
def fnFirst(request0):
       return render(request0,'welcome.html') 
    
def fnLogin(request1):
    return render(request1,'login.html')