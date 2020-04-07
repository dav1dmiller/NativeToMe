from django.db import models
from django.utils import timezone



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

    def __str__(self):
        """String for representing the Model object 'tribeID'."""
        return self.tribeID

    def __str__(self):
        """String for representing the Model object 'tribeName'."""
        return self.tribeName

    def __str__(self):
        """String for representing the Model object 'dateOfCreation'."""
        return self.dateOfCreation

    def __str__(self):
        """String for representing the Model object 'location'."""
        return self.location

    def __str__(self):
        """String for representing the Model object 'numOfMembers'."""
        return self.numOfMembers

    def __str__(self):
        """String for representing the Model object 'tribeOwner'."""
        return self.tribeOwner