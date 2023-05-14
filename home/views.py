from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.conf import settings
from django.views.generic import TemplateView, UpdateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import ContactUsForm


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
                messages.success(request, 'THANK YOU FOR YOUR MESSAGE')
                return redirect(reverse('contact') + '#')
            else:
                messages.error(request, 'Login to send message!')
                form = ContactUsForm()
                return redirect(reverse('contact') + '#')
        else:
            form = ContactUsForm
    return render(request, 'contact.html', {'form': form})
