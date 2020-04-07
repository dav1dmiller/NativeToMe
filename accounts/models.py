from django.db import models
# Template of how we are going to store data for this APP
# Create your models here.
from django.db import models
from django.contrib.auth.models import User #default user model from django
from django.db.models.signals import post_save #when profile is updated this can save for us
from django.dispatch import receiver

"""This is the blueprint for a profile table in the database"""

class UserProfile(models.Model):
    objects = models.Manager()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='blankProfile.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    hobbies = models.CharField(max_length=100, blank=True)

    def __str__(self):
        """String for representing the Model object 'user'."""
        return self.user
    def __str__(self):
        """String for representing the Model object 'image'."""
        return self.image
    def __str__(self):
        """String for representing the Model object 'bio'."""
        return self.bio
    def __str__(self):
        """String for representing the Model object 'location'."""
        return self.location
    def __str__(self):
        """String for representing the Model object 'birth_date'."""
        return self.birth_date
    def __str__(self):
        """String for representing the Model object 'birth_date'."""
        return self.hobbies


