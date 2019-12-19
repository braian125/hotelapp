"""Users Routes"""

from django.urls import path
from users import views

urlpatterns = [
    path(
        route='login/',
        view=views.SignInView.as_view(),
        name='signin'
    ),
    path(
        route='logout',
        view=views.Logout.as_view(),
        name='logout'
    ),
    path(
        route='signup',
        view=views.SignUpView.as_view(),
        name='signup'
    ),
    path(
        route='me',
        view=views.UpdateAgentView.as_view(),
        name='detail'
    ),
]