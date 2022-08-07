from typing import ClassVar
from django.shortcuts import render
from django.views.generic import View
import random
from patients.models import Patient, VaccineCase
from rest_framework.authtoken.models import Token
from datetime import datetime

# Create your views here.

class AddPatientView(View):
    def post(self,request):
        data=request.POST
        fullname=data['fullname']
        gender=data['gender']
        age=data['age']
        health_status=data['health_status']


        patient=Patient.objects.create(fullname=fullname,
        gender=gender,age=age,health_status=health_status)


        

        
    def get(self,request):
        pass

class NewPatientCase(View):
    def post(self,request,**kwargs):
        data=request.POST
        case_id='#1'
        sample_result=random.randint(0,100)
        viral_level=sample_result
        patient=Patient.objects.get(pk=kwargs['pk'])
        vaccine_case=VaccineCase(case_id=case_id,sample_result=sample_result,
        viral_level=viral_level,patient=patient,dosage_timeline='')
        vaccine_case.save()



class AdministerVaccine(View):
    def round_up_even(num):
        return num+(num%10)

    def post(self,request,**kwargs):
        data=request.POST
        pk=kwargs['pk']

        vaccine_case=VaccineCase.objects.get(pk=pk)
        viral_level=vaccine_case.viral_level
        if(viral_level<20):
            viral_level-=0
        elif(viral_level==0):
            pass

        else:
            viral_level-=20
            viral_level=self.round_up_even(viral_level)
        
        vaccine_case.viral_level=viral_level
        vaccine_case.dosage_timeline
        current_time=str(datetime.now())
        vaccine_case.dosage_timeline+=current_time+','
        times_more=viral_level/20
        vaccine_case.save()

class PatientStatus(View):
    def get(self,request,**kwargs):
        pass






