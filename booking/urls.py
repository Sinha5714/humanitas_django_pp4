from datetime import datetime

from django.urls import path, register_converter
from .views import (BookingListView, BookingDetailView,
                    BookingCreateView, BookingUpdateView)
from . import views


class DateConverter:
    regex = r"\d{4}-\d{2}-\d{2}"

    def to_python(self, value):
        return datetime.strptime(value, "%Y-%m-%d")

    def to_url(self, value):
        return value


register_converter(DateConverter, "yyyy")

urlpatterns = [
    path("", views.booking_home, name="booking_home"),
    path("bookings/", BookingListView.as_view(), name="bookings"),
    path("bookings/<int:pk>/", BookingDetailView.as_view(),
         name="booking_detail"),
    path("bookings/add/", BookingCreateView.as_view(), name="booking_add"),
    path(
        "bookings/add/<yyyy:date>/<str:timeblock>",
        BookingCreateView.as_view(),
        name="booking_add_spec"),
    path("bookings/<int:pk>/edit", BookingUpdateView.as_view(),
         name="booking_edit"),
    path("bookings/<int:pk>/cancel",
         views.cancel_booking, name="booking_cancel"),
]
