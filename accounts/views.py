from django.contrib.auth.decorators import login_required
from django.core.checks import templates
from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect, HttpResponse


"""Python functions that take a request and render a web page"""
def loginView(request):
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        print("User Homepage after Login")
        return render(request, 'home/home.html', {})
    else:
        print("Failed to login")
        return render(request, 'accounts/login.html/', {'title':'Login'})

@login_required
def profileView(request):
        print("User Profile")
        return render(request, 'accounts/userprofile/userprofile.html', {'profile' : 'userprofile'})

def logoutView(request):
        logout(request)
        return render(request, 'accounts/logout.html/', {'title': 'Login'})

@csrf_protect
def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/login.html/')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html/', {"form" : form})
