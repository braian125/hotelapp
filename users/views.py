"""Users views"""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView
from django.contrib.auth.models import User
from hotels.models import Hotel
from users.models import Agent
from users.forms import SignupForm

# Create your views here.
class SignInView(auth_views.LoginView):
    """SignIn view."""

    template_name = 'users/auth/signin.html'

class SignUpView(FormView):
    """Users sign up"""

    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)

class Logout(LoginRequiredMixin, auth_views.LogoutView):
    """Users Logout"""

    template_name = ''

class UpdateAgentView(LoginRequiredMixin, UpdateView):
    """Update user agent"""

    template_name = 'users/user_profile.html'
    model = Agent
    fields = ['phone', 'picture']

    def get_object(self):
        """Return user's agent"""
        return self.request.user.agent

    def get_success_url(self):
        """Return to user's agent"""
        username = self.object.user.username
        return reverse('users:detail')