from urllib.parse import urlparse

from django.urls import path
from .views import (
    CreateSuperUserView,LoginUserView,GetUserDetails
)
urlpatterns = [
    path('create-super-user/',CreateSuperUserView.as_view(),name='create-super-user'),
    path('login/',LoginUserView.as_view(),name='login-user'),
    path('user-details/',GetUserDetails.as_view(),name='user-details')
]