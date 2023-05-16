from django.shortcuts import render
from .models import Profile
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin)
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import UpdateView, DetailView
from django.contrib import messages
from django.urls import reverse
from .forms import ProfileForm

# Create your views here.


class UserSetUpProfile(SuccessMessageMixin, UpdateView):
    """
    A class view to update
    user profile
    """
    model = Profile
    form = ProfileForm
    template_name = 'siteusers/add_profile.html'
    success_url = reverse('home')
    success_message = 'YOUR PROFLE IS SET UP SUCCESSFULLY'

    def get_object(self, *args, **kwargs):
        return self.request.user.profile

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UserProfilePageView(LoginRequiredMixin, DetailView):
    """
    A class view to see detail
    of user profile
    """
    model = Profile
    template_name = 'siteusers/profile_page.html'

    def get_object(self, *args, **kwargs):
        return self.request.user
