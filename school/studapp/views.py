from django.shortcuts import render,get_list_or_404
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from .models import Student
from django.urls import reverse,reverse_lazy
# Create your views here.

class StudList(ListView):
    model=Student
    template_name='studapp/stud_list.html'
    context_object_name='students'

class AddStudent(CreateView):
    model=Student
    fields='__all__'
    template_name='studapp/stud_Add.html'
    success_url=reverse_lazy('studapp:studlist')

class StudDetail(DetailView):
    model=Student
    queryset=Student.objects.all()
    template_name='studapp/stud_detail.html'

class UpdateStudent(UpdateView):
    model=Student
    fields='__all__'
    template_name='studapp/stud_update.html'
    success_url=reverse_lazy('studapp:studlist')

class DeleteStudent(DeleteView):
    model=Student
    template_name='studapp/stud_delete.html'
    success_url=reverse_lazy('studapp:studlist')
    

    
