from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView


class UsersList(ListView):
    template_name = 'profile_re/users.html'
    context_object_name = 'users'
    model = User


class UserDetail(DetailView):
    template_name = 'profile_re/user.html'
    context_object_name = 'user'
    model = User
