from urllib.parse import urlparse

from django.urls import path
from .views import CreateSuperUser
urlpatterns = [
    path('create-super-user/',CreateSuperUser.as_view(),name='create-super-user')
]