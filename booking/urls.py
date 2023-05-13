from datetime import datetime

from django.urls import path
from .views import BookingListView
from . import views

urlpatterns = [
    path("", views.booking_home, name="booking_home"),
    path("bookings/", BookingListView.as_view(), name="bookings"),
]
