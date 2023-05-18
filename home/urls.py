from django.urls import path
from . import views
# Internal:
from .views import home, contact, UserUpdateProfile, UserProfilePageView, DeleteUser


urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('profile_page/', UserProfilePageView.as_view(), name='profile_page'),
    path('update_profile/', UserUpdateProfile.as_view(), name='update_profile'),
    path('delete_user/', DeleteUser.as_view(), name='delete_user'),

]
