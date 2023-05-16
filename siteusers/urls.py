from django.urls import path
from . import views
# Internal:
from .views import UserSetUpProfile, UserProfilePageView


urlpatterns = [
    path('add_profile/', UserSetUpProfile.as_view(), name='profile_add'),
    path('profile_page/', UserProfilePageView.as_view(), name='profile_page'),
]
