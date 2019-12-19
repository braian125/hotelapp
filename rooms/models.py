from django.db import models
from hotels.models import Hotel

# Create your models here.
class Room(models.Model):
    """Room hotels model"""

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    room_code = models.CharField(max_length=10)
    description = models.CharField(max_length=255, blank=True)
    fare = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
