"""Hotels Views"""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from hotels.models import Hotel
from hotels.forms import HotelForm

# Create your views here.
class HotelList(ListView):
    """Return all hotels"""

    template_name = 'hotels/hotels.html'
    model = Hotel
    ordering = ('-created',)
    context_object_name = 'hotels'

class CreateHotelView(LoginRequiredMixin, CreateView):
    """Create a new hotel"""

    template_name = 'hotels/new.html'
    form_class = HotelForm
    success_url = reverse_lazy('hotels:hotels')
    
    """def get_context_data(self, **kwargs):
        Add user and agent to context.
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['agent'] = self.request.user.agent
        return context"""

class HotelDetailView(LoginRequiredMixin, DetailView):
    template_name = 'hotels/detail.html'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    queryset = Hotel.objects.all()

class HotelUpdateView(LoginRequiredMixin, DetailView):
    template_name = 'hotels/update.html'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    queryset = Hotel.objects.all()