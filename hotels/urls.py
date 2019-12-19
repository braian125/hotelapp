"""Hotels Routes"""

from django.urls import path
from hotels import views

urlpatterns = [
    path(
        route='',
        view=views.HotelList.as_view(),
        name='hotels'
    ),
    path(
        route='new',
        view=views.CreateHotelView.as_view(),
        name='hotelCreate'
    ),
    path(
        route='<int:id>',
        view=views.HotelDetailView.as_view(),
        name='hotelDetail'
    ),
    path(
        route='update/<int:id>',
        view=views.HotelUpdateView.as_view(),
        name='hotelUpdate'
    ),
]