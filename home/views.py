from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import EmailMessage
from .forms import ContactUsForm

# Create your views here.


def home(request):
    return render(request, 'index.html')


def contact(request):
    """
    view to render contact page
    """
    form = ContactUsForm()

    return render(request, 'contact.html', {'form': form})
