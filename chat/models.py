from django.db import models
from studdybuddy.models import Profile

class Room(models.Model):
    """Represents chat rooms that users can join"""
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)
    user1 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="rooms1", default=1)
    user2 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="rooms2", default=1)
    


    def __str__(self):
        """Returns human-readable representation of the model instance."""
        return self.name