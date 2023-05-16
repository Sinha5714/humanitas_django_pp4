from django.urls import path
from . import views
# Internal:
from .views import UserSetUpProfile


urlpatterns = [
    path('add_profile/', UserSetUpProfile.as_view(), name='profile_add'),
]
