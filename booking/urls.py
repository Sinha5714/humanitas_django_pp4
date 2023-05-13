from datetime import datetime

from django.urls import path
from .views import BookingListView, BookingDetailView
from . import views

urlpatterns = [
    path("", views.booking_home, name="booking_home"),
    path("bookings/", BookingListView.as_view(), name="bookings"),
    path("bookings/<int:pk>/", BookingDetailView.as_view(),
         name="booking_detail"),
]
