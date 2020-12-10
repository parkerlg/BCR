from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def indexPageView(request) :
    return render(request, 'home/landing.html')

def aboutusPageView(request) :
    return render(request, 'home/aboutus.html')

