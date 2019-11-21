from django.shortcuts import render
from .models import User
from django.views.generic import CreateView
from .forms import UserForm
from django.urls import reverse_lazy

class UserRegister(CreateView):
    model = User
    form_class = UserForm
    template_name = 'userRegister.html'
    success_url = reverse_lazy('index')

userRegister = UserRegister.as_view()
