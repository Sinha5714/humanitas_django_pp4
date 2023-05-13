from datetime import datetime

from django.urls import path

from . import views

urlpatterns = [
    path("", views.bookinghome, name="booking_home"),
]
