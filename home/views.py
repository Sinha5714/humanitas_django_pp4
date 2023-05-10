from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import ContactUsForm

# Create your views here.


def home(request):
    return render(request, 'index.html')


def contact(request):
    """
    view to render contact page
    """
    form = ContactUsForm()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            send_mail(
                subject=name,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['shubhamsinha5714@gmail.com']
            )
            messages.success(request, 'THANK YOU FOR YOUR MESSAGE')

            return redirect(reverse('contact') + '#')

        else:
            form = ContactUsForm()
            return redirect(reverse('contact') + '#')

    return render(request, 'contact.html', {'form': form})
