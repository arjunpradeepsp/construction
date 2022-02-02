from django.shortcuts import render

# Create your views here.
def fnHome(request):
    return render(request,'home.html')