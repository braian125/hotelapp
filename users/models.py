"""Agent users model"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Agent(models.Model):
    """Agent Model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone = models.CharField(max_length=20, blank=True)
    picture = models.ImageField(upload_to='users/images', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    


    