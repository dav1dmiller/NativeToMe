from django.core.checks import templates
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.template import loader, context
from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView, FormView, RedirectView
from django.http import HttpResponseRedirect, HttpResponse


# Python functions that take a request and send back http response
def loginView(request):
    username=request.POST.get('username', False)
    password=request.POST.get('password', False)
    #print(username)
    #print(password)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'userprofile/userProfile.html', {})
    else:
        print("Failed to log in!")
        return render(request, 'accounts/login.html/', {'title':'Login'})

@csrf_protect
def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print("Successfully created user...")
            return HttpResponseRedirect('/accounts/login.html/')
    else:
        print("Failed to create user...")
        form = UserCreationForm()
    return render(request, 'accounts/register.html/', {"form":form})
