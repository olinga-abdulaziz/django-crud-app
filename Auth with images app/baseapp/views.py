from django.shortcuts import render
from django.views import generic
from .models import Records
from django.urls import reverse_lazy
# Create your views here.
class HomeView(generic.ListView):
    model=Records
    template_name='baseapp/home.html'

class UploadView(generic.CreateView):
    model=Records
    fields='__all__'
    template_name='baseapp/upload.html'
    succcess_url=reverse_lazy('home')

