from django.urls import path
from .views import AddPatientView, GetAllPatientsView
urlpatterns = [
    path('add-patient/',AddPatientView.as_view(),name='add-patient'),
    path('get-patients/',GetAllPatientsView.as_view(),name='get-patients')
]