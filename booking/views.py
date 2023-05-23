
import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import BookingForm
from .models import Booking
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# Function to generate daylist


def generate_daylist():
    daylist = []
    today = datetime.date.today()
    for i in range(7):
        day = {}
        next_day = today + datetime.timedelta(days=i+1)
        weekday = next_day.strftime("%A").upper()
        day["date"] = str(next_day)
        day["day"] = weekday
        day["A_booked"] = (
            Booking.objects.filter(date=str(next_day)).filter(
                timeblock="A").exists()
        )
        day["B_booked"] = (
            Booking.objects.filter(date=str(next_day)).filter(
                timeblock="B").exists()
        )
        day["C_booked"] = (
            Booking.objects.filter(date=str(next_day)).filter(
                timeblock="C").exists()
        )
        day["D_booked"] = (
            Booking.objects.filter(date=str(next_day)).filter(
                timeblock="D").exists()
        )
        day["E_booked"] = (
            Booking.objects.filter(date=str(next_day)).filter(
                timeblock="E").exists()
        )
        day["F_booked"] = (
            Booking.objects.filter(date=str(next_day)).filter(
                timeblock="F").exists()
        )
        day["G_booked"] = (
            Booking.objects.filter(date=str(next_day)).filter(
                timeblock="G").exists()
        )
        if day["day"] != "":
            daylist.append(day)
    return daylist


def booking_home(request):
    context = {"days": generate_daylist()}
    return render(request, "booking/booking_home.html", context)


class BookingListView(ListView):
    """
    Class model for list view for bookings
    """
    model = Booking
    template_name = "booking/bookings.html"
    context_object_name = "bookings"
    ordering = ["-date"]


class BookingDetailView(LoginRequiredMixin, DetailView):
    """
    Class model for detail view for bookings
    """
    model = Booking


class BookingCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Class model for create a new booking
    """
    model = Booking
    fields = ["date", "timeblock", "helptype"]
    form = BookingForm()
    template_name = "booking/add_booking.html"
    success_message = 'Your booking is confirmed!'
    success_url = '/bookings'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_initial(self):
        return {
            "date": self.kwargs.get("date"),
            "timeblock": self.kwargs.get("timeblock"),
        }


class BookingUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Class model for editing an existing booking
    """
    model = Booking
    fields = ["date", "timeblock", "helptype"]
    form = BookingForm()
    template_name = "booking/add_booking.html"
    success_message = 'Your booking is updated successfully!'
    success_url = '/bookings'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        booking = self.get_object()
        if self.request.user == booking.user:
            return True
        return False


def cancel_booking(request, pk):
    """
    Deletes the booking identified by it's primary key by the user
    """
    booking = Booking.objects.get(pk=pk)

    if request.method == 'POST':
        booking.delete()
        messages.success(request, "Booking is cancelled")
        return redirect('bookings')

    return render(
        request, 'booking/booking_confirm_delete.html', {'booking': booking})
