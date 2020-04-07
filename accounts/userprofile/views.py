from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.db import models, transaction
from django.forms import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User #default user model from django
from django.db.models.signals import post_save #when profile is updated this can save for us
from django.dispatch import receiver
# Create your views here.


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name',
                  'last_name',
                  'email')
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('url', 'location', 'company')

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return HttpResponseRedirect('/userprofile/userprofile.html')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
