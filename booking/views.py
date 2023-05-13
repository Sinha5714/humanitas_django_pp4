
import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Booking
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


# Create your views here.


def generate_daylist():
    daylist = []
    today = datetime.date.today()
    for i in range(7):
        day = {}
        curr_day = today + datetime.timedelta(days=i)
        weekday = curr_day.strftime("%A").upper()
        day["date"] = str(curr_day)
        day["day"] = weekday
        day["A_booked"] = (
            Booking.objects.filter(date=str(curr_day)).filter(
                timeblock="A").exists()
        )
        day["B_booked"] = (
            Booking.objects.filter(date=str(curr_day)).filter(
                timeblock="B").exists()
        )
        day["C_booked"] = (
            Booking.objects.filter(date=str(curr_day)).filter(
                timeblock="C").exists()
        )
        day["D_booked"] = (
            Booking.objects.filter(date=str(curr_day)).filter(
                timeblock="D").exists()
        )
        day["E_booked"] = (
            Booking.objects.filter(date=str(curr_day)).filter(
                timeblock="E").exists()
        )
        day["F_booked"] = (
            Booking.objects.filter(date=str(curr_day)).filter(
                timeblock="F").exists()
        )
        if day["day"] != "SUNDAY":
            daylist.append(day)
    return daylist


def booking_home(request):
    context = {"days": generate_daylist()}
    return render(request, "booking/booking_home.html", context)


class BookingListView(ListView):
    model = Booking
    template_name = "booking/bookings.html"
    context_object_name = "sessions"
    ordering = ["-date"]
