from cmath import log
from urllib import request
from django.shortcuts import render

# Create your views here.
def fnHome(request):
    return render(request,'home.html')
def fnFirst(request0):
       return render(request0,'welcome.html') 
    
def fnLogin(request1):
    return render(request1,'login.html')

def fnabout(request2):
    return render(request2,'about.html')

def fncontact(request3):
    return render(request3,'contact.html')

def fnmenu(request4):
    return render(request4,'menu.html')

def fnsign(request5):
    return render(request5,'sign.html')

def fnoffer(request6):
    return render(request6,'offer.html')
def fncrt(request7):
    return render(request7,'crt.html')