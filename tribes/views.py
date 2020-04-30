from random import randint
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import createTribeForm
from django.db.models import Q
from accounts.models import UserProfile

# Create your views here.
from .models import Tribe
"""Python functions that take a request and render a web page"""
@login_required
def tribeHomePage(request, tribeID):
        tribe = Tribe.objects.get(pk=tribeID)
        context = {"tribe" : tribe }
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
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = createTribeForm(request.POST, request.FILES)
        user = UserProfile()
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
            tribe.tribeOwner = request.user.username
            tribe.save()

            if Tribe.tribe_present(tribe.tribeName) == True:
                print("Successfully created " + tribe.tribeName + "!")
                print(tribe.tribeID)
                print(tribe.tribeOwner)
            # redirect to a new URL:
            return HttpResponseRedirect('/', {"tribe" : tribe })
    else:
        print("Failed to create tribe")
        form = createTribeForm()
    return render(request, 'tribes/tribeCreatePage.html/', {'form':form})