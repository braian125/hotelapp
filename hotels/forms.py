"""Hotel forms"""

from django import forms
from hotels.models import Hotel

class HotelForm(forms.ModelForm):
    """Hotel model form."""

    class Meta:
        """Form settings."""

        model = Hotel
        fields = ('user', 'name', 'address', 'category', 'photo')