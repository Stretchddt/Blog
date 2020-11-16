from django.urls import path
from .views import my_profile

app_name = 'profiles'

urlpatterns = [
    path('myprofile/', my_profile, name='my-profile'),
]    