from django.contrib.auth.decorators import login_required
from django.core.checks import templates
from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import editProfileForm
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from .models import UserProfile

"""Python functions that take a request and render a web page"""
def loginView(request):
    print("Login")
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
        if request.method == "GET":
            print("User Profile GET")
            profile = UserProfile()
            profile.user = request.user  # get the profile base on the user
            form = editProfileForm(request.POST, request.FILES)
            return render(request, 'accounts/userprofile/userprofile.html', {'form' : form, 'profile':profile })
        else:
            print("User Profile POST")
            form = editProfileForm(request.POST, request.FILES)
            # check if form is valid
            print(form.is_valid())
            if form.is_valid():
                profile = UserProfile()
                profile.user = request.user #get the profile base on the user
                print("<!---------------------Its working---------------------!>")
                print(profile.user)

                profile.location = form.cleaned_data.get("location")
                profile.school = form.cleaned_data.get("school")
                profile.hobbies = form.cleaned_data.get("hobbies")
                profile.bio = form.cleaned_data.get("bio")
                profile.save()
                print(profile.hobbies)
                print(profile.location)
                print(profile.bio)
                print(profile.school)
                return render(request, 'accounts/userprofile/userprofile.html', {'profile' : profile })
            else:
                print("Invalid form!")
                return HttpResponseRedirect('/accounts/userprofile/userprofile.html', {})

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
