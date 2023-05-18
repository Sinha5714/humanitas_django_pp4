from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.conf import settings
from django.views.generic import TemplateView, UpdateView, DetailView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import ContactUsForm, ProfileForm
from .models import Profile


# Create your views here.


def home(request):
    """
    view to render home page
    """
    return render(request, 'index.html')


def contact(request):
    """
    view to render contact page and send message
    if user is logged in
    """
    form = ContactUsForm()
    if request.method == 'POST':
        form = ContactUsForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            if request.user.is_authenticated:
                send_mail(
                    subject=name,
                    message=message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=['shubhamsinha5714@gmail.com']
                )
                messages.success(
                    request, 'Your message has been sent succesfully!')
                return redirect(reverse('home') + '#')
            else:
                messages.error(request, 'Login to send message!')
                form = ContactUsForm()
                return redirect(reverse('contact') + '#')
        else:
            form = ContactUsForm
    return render(request, 'contact.html', {'form': form})


class UserSetUpProfile(SuccessMessageMixin, UpdateView):
    """
    A class view to update
    user profile
    """
    model = Profile
    form = ProfileForm
    template_name = 'home/add_profile.html'
    success_message = 'YOUR PROFLE IS SET UP SUCCESSFULLY'

    def get_object(self, *args, **kwargs):
        return self.request.user.username

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UserProfilePageView(LoginRequiredMixin, DetailView):
    """
    A class view to see detail
    of user profile
    """
    model = Profile
    template_name = 'home/profile_page.html'
