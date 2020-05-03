from django.db import models
from django.utils import timezone
from django.db.models import Q
from django.contrib.auth.models import User


"""This is the blueprint for a tribe table in the database"""
class Tribe(models.Model):
    objects = models.Manager()
    tribeID = models.IntegerField(primary_key=True)
    tribeName = models.CharField(max_length=50)
    # How long its been a tribe
    dateOfCreation = models.DateField(default=timezone.now)
    # Location
    location = models.CharField(max_length=30)
    # Privacy
    choices = [('Public', 'Private'), ('Private', 'Public')]
    privacyMode = models.CharField(max_length=7, choices=choices, default='Private')
    # Number of members
    numOfMembers = models.IntegerField(default=1)
    # Description
    description = models.TextField(blank=True)
    # owner, tribe founder(s)
    tribeOwner = models.CharField(max_length=50)

    def tribe_present(tribeName):
        if Tribe.objects.filter(tribeName=tribeName).exists():
            return True
        else:
            return False

    def tribe_search(tribeName):
        q = Q()
        for t in Tribe:
            q |= Q(name_icontains=t)
            return Tribe.objects.filter(q)

    def __str__(self):
        """String for representing the Model object 'tribeName'."""
        return self.tribeName

class Posts(models.Model):
    objects = models.Manager()
    tribePosterID = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    image = models.ImageField(default='blankProfile.jpg', upload_to='profile_pics')
    description = models.TextField(blank=True)
    choices = [('Like', 'Dislike'), ('Like', 'Dislike')]
    likeOption = models.CharField(max_length=7, choices=choices)
    dateOfCreation = models.DateField(default=timezone.now)