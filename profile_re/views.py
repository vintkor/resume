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

    def get_object(self, queryset=None):
        return User.objects.select_related('profile').prefetch_related(
            'profile__skilllevel_set',
            'profile__userlanguagelevel_set',
            'profile__hobieuser_set',
            'profile__company_set',
        ).get(id=self.kwargs.get('pk'))
