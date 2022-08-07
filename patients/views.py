from typing import ClassVar
from django.shortcuts import render
from rest_framework.views import APIView
import random
from patients.models import Patient, VaccineCase
from rest_framework.authtoken.models import Token
from datetime import datetime
from .serializer import AddPatientSerializer,NewPatientCaseSerializer
from rest_framework.response import Response


# Create your views here.

class AddPatientView(APIView):
    def post(self,request):
        data=request.data
        serializer=AddPatientSerializer(data=data)
        if(not serializer.is_valid):
            return Response(serializer.errors,status=400)

        return Response(data=serializer.validated_data,
         status=200)

class NewPatientCase(APIView):
    def post(self,request,**kwargs):
        data=request.data
        serializer=NewPatientCaseSerializer(data=data)
        if(not serializer.is_valid()):
            return Response(data=serializer.errors,status=400)
        
        vaccine_case_pk=serializer.validated_data['vaccine_pk']
        return Response({'vaccine_case_pk':vaccine_case_pk},status=200)



class AdministerVaccine(APIView):
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

class PatientStatus(APIView):
    def post(self,request,**kwargs):
        pass





