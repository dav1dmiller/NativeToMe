from random import randint
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import *
from django.db.models import Q
from .models import Tribe

# Create your views here.
"""Python functions that take a request and render a web page"""
@login_required
def tribeHomePage(request, tribeID):
    tribe = Tribe.objects.get(pk=tribeID)
    current_user = User.objects.get(username = request.user.username)
    form = createTribePostForm(request.POST)
    #Collection of all tribeMembers
    members = tribe.tribeMembers.all()
    print(members)
    #check if current_user in the given tribe's list of members
    if current_user in members:
        inTribe = True
    else:
        inTribe = False


    print(inTribe)
    context = {'tribe': tribe,
               'form': form,
               'members':members,
               'inTribe':inTribe}
    if request.method == "GET":
        print("tribeHomePage GET")
        context = {'tribe' : tribe,
                   'form' : form,
                   'members':members,
                   'inTribe':inTribe}
        return render(request, 'tribes/tribeHomePage.html/', context)

    elif request.method == "POST" and current_user == tribe.tribeOwner:
        """Create Post"""
        print("tribeHomePage POST")
        if form.is_valid():
            tribe.tribeName = form.cleaned_data.get("tribeName")
            tribe.description = form.cleaned_data.get("description")
            tribe.save()
            return render(request, 'tribes/tribeHomePage.html/', context)
        else:
            print("Invalid form!")
            return HttpResponseRedirect('tribes/tribeHomePage.html/', {})
    else:
        return render(request, 'tribes/tribeHomePage.html/', context)


def tribeSearchPage(request):
    if request.method == "GET":
        queryset_list = Tribe.objects.all()
        query = request.GET.get("searchField")
        if query:
            match = queryset_list.filter(Q(tribeName__icontains=query))
            context = { "object_list":match}
            if match:
                return render(request, 'tribes/tribeSearchPage.html/', context)
            else:
                return render(request, 'tribes/tribeSearchPage.html/', {})
        return render(request, 'tribes/tribeSearchPage.html/', {})


def tribeCreate(request):
    current_user = User.objects.get(username=request.user.username)
    print(current_user)
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = createTribeForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            tribe = Tribe()
            # process the data in form.cleaned_data as required
            tribe.tribeID = randint(0,1000)
            tribe.tribeName = form.cleaned_data.get("tribeName")
            tribe.location = form.cleaned_data.get("location")
            tribe.description = form.cleaned_data.get("description")
            tribe.choices = form.cleaned_data.get("choices")
            tribe.privacyMode = form.cleaned_data.get("privacyMode")
            """tribe.tribeOwner = request.user does not work because of incompatible types"""
            """tribe.tribeOwner = UserProfile.user"""
            tribe.tribeOwner = current_user.username
            tribe.save()
            #When a tribe is created. The person who creates it is in the tribe. Add member.
            tribe.tribeMembers.add(current_user)

            if Tribe.tribe_present(tribe.tribeName) == True:
                print("Successfully created " + tribe.tribeName + "!")
                print(tribe.tribeID)
                print(tribe.tribeOwner)
            # redirect to a new URL:
            return HttpResponseRedirect('/', {'tribe' : tribe })
    else:
        print("Failed to create tribe")
        form = createTribeForm()
    return render(request, 'tribes/tribeCreatePage.html/', {'form':form})


def tribeManagePage(request, tribeID):
    print("Tribe Manage Page")
    tribe = Tribe.objects.get(pk=tribeID)
    form = editTribeForm(request.POST)
    current_user = User.objects.filter(username=request.user.username)
    #collection of tribe members
    members = tribe.tribeMembers.all()
    # check if current_user in the given tribe's list of members
    for current_user in members:
        # set bool variable to use in html render
        if current_user == members:
            inTribe = True
        else:
            inTribe = False

    context = {'tribe': tribe,
               'form': form,
               'members': members,
               'inTribe': inTribe}

    if request.method == "GET":
        """If the user is tribe owner"""
        return render(request, 'tribes/tribeManagePage.html/', context)
    # if this is a POST request we need to process the form data
    elif request.method == "POST" and current_user == tribe.tribeOwner:
        if form.is_valid():
            tribe.tribeName = form.cleaned_data.get("tribeName")
            tribe.description = form.cleaned_data.get("description")
            tribe.save()
            print("Successfully managed tribe")
            return render(request, 'tribes/tribeHomePage.html/', context)
        else:
            print("Manage tribe failed")
            return render(request, 'tribes/tribeManagePage.html/', {'form':form})
