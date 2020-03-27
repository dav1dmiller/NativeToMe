from django.core.checks import templates
from django.shortcuts import render
from django.template import loader, context
from django.views.generic import CreateView, FormView, RedirectView
from django.http import HttpResponseRedirect, HttpResponse


# Python functions that take a request and send back http response

def loginView(request):
    return render(request, 'login.html', {'title':'Login'})

def registerView(request):
    return render(request, 'register.html', {'title':'Login'})
