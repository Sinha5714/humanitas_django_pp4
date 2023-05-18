from django.urls import path
from . import views
# Internal:
from .views import home, contact, UserSetUpProfile, UserProfilePageView



urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),

]
