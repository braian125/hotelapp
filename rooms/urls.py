"""Rooms Routes"""

from django.urls import path
from hotels import views
from django.views.generic import TemplateView

urlpatterns = [
    path(
        route='<int:hotel_id>',
        view=TemplateView.as_view(template_name='hotels/detail.html'),
        name='hotelRooms'
    ),
]