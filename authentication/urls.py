from urllib.parse import urlparse

from django.urls import path
from .views import CreateSuperUser
urlpatterns = [
    path('',CreateSuperUser.as_view(),'create-super-user')
]