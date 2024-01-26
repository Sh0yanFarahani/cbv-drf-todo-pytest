from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy


class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('task:task-list')

