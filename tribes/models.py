from django.db import models

"""This is the blueprint for a tribe table in the database"""
class Tribe(models.Model):
    tribeID = models.IntegerField(primary_key=True)
    tribeName = models.CharField(max_length=50)
    # How long its been a tribe
    dateOfCreation = models.DateField()
    # Location
    location = models.CharField(max_length=30)
    # Number of members
    numOfMembers = models.IntegerField()
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