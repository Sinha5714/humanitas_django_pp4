from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import (
    TemplateView, UpdateView, DetailView, DeleteView)
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactUsForm, ProfileForm
from .models import Profile, Contact




def home(request):
    """
    view to render home page
    """
    return render(request, 'index.html')

def about(request):
    """
    View to render about page
    """
    return render(request, 'about.html')

class ContactMessage(View):
    """
    This view displays the contact form and if the user
    is registered and inserts the user email into the
    email field
    """
    template_name = 'contact.html'
    success_message = 'Message has been sent successfully.'

    def get(self, request, *args, **kwargs):
        """
        Retrieves users email and inputs into email input
        """
        if request.user.is_authenticated:
            email = request.user.email
            contact_form = ContactUsForm(initial={'email': email})
        else:
            contact_form = ContactUsForm()
        return render(request, 'contact.html',
                      {'contact_form': contact_form})

    def post(self, request):
        """
        Checks that the provided info is valid format
        and then posts to database
        """
        contact_form = ContactUsForm(data=request.POST)

        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            if request.user.is_authenticated:
                contact.user = request.user
                contact.save()
                messages.success(
                    request, "Message has been sent successfully!")
                return render(request, 'index.html')
            else:
                messages.error(request, 'NEED TO BE LOGGED IN TO SEND MESSAGE')
                contact_form = ContactUsForm()
                return render(request, 'contact.html',
                              {'contact_form': contact_form})

        return render(request, 'contact.html',
                      {'contact_form': contact_form})


class UserProfilePageView(LoginRequiredMixin, DetailView):
    """
    A class view to see detail
    of user profile
    """
    model = Profile
    template_name = 'home/profile_page.html'

    def get_object(self, *args, **kwargs):
        return self.request.user


class UserUpdateProfile(SuccessMessageMixin, UpdateView):
    """
    A class view to update
    user profile
    """
    model = Profile
    form_class = ProfileForm
    success_url = '/profile_page'
    template_name = 'home/add_profile.html'
    success_message = 'Your profile has been updated successfully!'

    def get_object(self, *args, **kwargs):
        return self.request.user.profile

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DeleteUser(LoginRequiredMixin, SuccessMessageMixin,
                 DeleteView):
    """
    A class view that handles a
    deletion of profile object if
    it exists
    """
    model = User
    template_name = 'home/delete_user.html'

    def get_object(self, *args, **kwargs):
        return self.request.user

    def post(self, request, *args, **kwargs):
        if Profile.objects.filter(user=request.user).exists():
            profile = Profile.objects.filter(user=request.user)
            profile.delete()

        request.user.is_active = False
        request.user.save()
        messages.success(request, 'Your Profile is deleted successfully!')

        return HttpResponseRedirect(reverse('account_logout'))
