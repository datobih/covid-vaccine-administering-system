from django.urls import path
from .views import AddPatientView
urlpatterns = [
    path('add-patient/',AddPatientView.as_view(),name='add-patient')
]