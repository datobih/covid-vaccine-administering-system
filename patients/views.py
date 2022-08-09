from typing import ClassVar
from django.shortcuts import render
from rest_framework.views import APIView
import random
from patients.models import Patient, VaccineCase
from rest_framework.authtoken.models import Token
from datetime import datetime
from .serializer import (
    AddPatientSerializer, AdministerVaccineSerializer,
    NewPatientCaseSerializer, PatientSerializer)
from rest_framework.response import Response


# Create your views here.



class AddPatientView(APIView):
    def post(self,request):
        data=request.data
        print(data)
        serializer=AddPatientSerializer(data=data)
        if(not serializer.is_valid()):
            print('ADD PATIENT SERIALIZER NOT VALID')
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
    def post(self,request,**kwargs):
        data=request.data
        serializer=AdministerVaccineSerializer(data=data)
        if(not serializer.is_valid()):
            return Response(serializer.errors,status=400)

        return Response({'times_more':
        serializer.validated_data['times_more']})






class PatientStatus(APIView):
    def post(self,request,**kwargs):
        data=request.data
        if(len(data)==1):
            if('pk' in data):
                pk=data['pk']
                patient=Patient.objects.get(pk=pk)
                if(not patient):
                    return Response({'error':
                    'Patient not found from the pk provided'})

                serializer=PatientSerializer(patient)
                return Response(serializer.data)


        return Response({'error':'pk not found'},status=400)




