from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import createTribeForm

# Create your views here.
"""Python functions that take a request and render a web page"""
@login_required
def tribeHomePage(request):
    return render(request, 'tribes/tribeHomePage.html/', {'title':'Tribe'})

@login_required
def tribeCreate(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = createTribeForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            print("Successfully created a tribe")
            # redirect to a new URL:
            return HttpResponseRedirect('/tribes/tribeHomePage.html/')
    else:
        print("Failed to create tribe")
        form = createTribeForm()
    return render(request, 'tribes/create.html/', {'form':form})