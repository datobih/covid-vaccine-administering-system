from urllib import response
from django.test import TestCase
from django.contrib.auth import get_user_model
from patients.models import Patient
from django.urls import reverse
from rest_framework.authtoken.models import Token

User=get_user_model()

# Create your tests here.
class BaseTestCase(TestCase):

    def setUp(self) -> None:
        credentials={
            'username':'testUser',
            'password':'123456789',
            'first_name':'Test',
            'last_name':'User'
        }

        patient_credentials={
        'first_name':'Bola',
        'last_name':'Tayo',
        'gender':'Male',
        'age':'17',
        'genotype':'AA',
        'blood_group':'O',
        'phone_number':'08134343454',
        'email':'dayodele89@gmail.com'}
        self.user=User.objects.create_superuser(**credentials)
        self.patient=Patient.objects.create(**patient_credentials)



class TestUserCase(BaseTestCase):

    def test_is_user_available(self):
        self.assertEquals('testUser',self.user.username)

class TestPatientCase(BaseTestCase):
    def test_create_patient(self):
        patient_credentials={
        'first_name':'Bola',
        'last_name':'Tayo',
        'gender':'Male',
        'age':'17',
        'genotype':'AA',
        'blood_group':'O',
        'phone_number':'08134343454',
        'email':'dayodele89@gmail.com'}

        response=self.client.post(reverse('add-patient'),data=patient_credentials)
        print(response)

    def test_get_all_patient(self):
        response=self.client.get(reverse('get-patients'))
        print(response)

    