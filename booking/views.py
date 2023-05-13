
import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Booking


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
