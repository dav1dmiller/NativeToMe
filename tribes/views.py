from django.contrib.auth import authenticate
from django.shortcuts import render

# Create your views here.
"""Python functions that take a request and render a web page"""
def tribeHomePage(request):
    return render(request, 'tribes/tribeHomePage.html/', {'title':'Tribe'})