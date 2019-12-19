"""Hotel models"""

from django.db import models
from django.contrib.auth.models import User


class Hotel(models.Model):
    """Hotel model"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    category = models.IntegerField()
    photo = models.ImageField(upload_to='hotels/photos')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)