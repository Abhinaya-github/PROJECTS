from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView,DeleteView,UpdateView
from teachers.models import Teacher
from django.urls import reverse_lazy
   

# Create your views here.
class TeacherRead(ListView):
    model=Teacher


class CreateTeacher(CreateView):
    model=Teacher
    fields=('name','subject','experience','contact')
    success_url = reverse_lazy('teacherslist')

class TeacherDetail(DetailView):
    model=Teacher

class TeacherDelete(DeleteView):
    model = Teacher
    template_name = "teachers/teacher_confirm_delete.html"
    success_url = reverse_lazy('teacherslist')

class TeacherUpdate(UpdateView):
    model = Teacher
    fields = ('name', 'subject', 'experience', 'contact')
    success_url = reverse_lazy('teacherslist')