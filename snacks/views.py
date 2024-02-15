from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Snack
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class SnackListView(ListView):
    model = Snack
    template_name = 'snack_list.html'

class SnackDetailView(DetailView):
    model = Snack
    template_name = 'snack_detail.html'

class SnackListView(ListView):
    model = Snack
    template_name = 'snack_list.html'

class SnackDetailView(DetailView):
    model = Snack
    template_name = 'snack_detail.html'

class SnackCreateView(CreateView):
    model = Snack
    fields = ['title', 'purchaser', 'description']
    template_name = 'snack_create.html'
    success_url = reverse_lazy('snack_list')

class SnackUpdateView(UpdateView):
    model = Snack
    fields = ['title', 'purchaser', 'description']
    template_name = 'snack_update.html'
    success_url = reverse_lazy('snack_list')

class SnackDeleteView(DeleteView):
    model = Snack
    template_name = 'snack_delete.html'
    success_url = reverse_lazy('snack_list')