from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect


from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class TaskList(LoginRequiredMixin, ListView):
    model = Task

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['name',]   
    success_url = reverse_lazy('task:task-list')  

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task:task-list')  


    def get(self, request: HttpRequest, *args: Any, **kwargs: Any):
        task = get_object_or_404(self.model, id=kwargs['pk']).delete()
        return HttpResponseRedirect('/')
    def get_queryset(self):
        return self.model.objects.all()

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['name']
    success_url = reverse_lazy('task:task-list')

class TaskComplate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['done']

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any):
        object = get_object_or_404(self.model, id=kwargs['pk'])
        object.done = True
        object.save()
        return HttpResponseRedirect('/')



