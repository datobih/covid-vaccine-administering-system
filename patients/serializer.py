from rest_framework import serializers
from .models import Patient,VaccineCase
import random


class AddPatientSerializer(serializers.Serializer):
    fullname=serializers.CharField()
    gender=serializers.CharField(max_length=1)
    age=serializers.CharField(max_length=3)
    health_status=serializers.CharField()

    def validate(self, attrs):
        super().validate(attrs)
        
        patient=Patient.objects.create(
        fullname=attrs['fullname'],
        gender=attrs['gender'],age=attrs['age'],
        health_status=attrs['health_status'])
        attrs['pk']=patient.pk
        return attrs


class NewPatientCaseSerializer(serializers.Serializer):
    pk=serializers.IntegerField()


    def validate(self, attrs):
        super().validate(attrs)
        patient=Patient.objects.get(pk=attrs['pk'])
        if(not patient):
            raise serializers.ValidationError('Invalid patient primary key')

        patient_count=patient.vaccine_cases.count()
        if(patient_count==0):
            case_id='#1'

        else:
            case_id=f'#{str(patient_count+1)}'
            sample_result=random.randint(0,100)
            viral_level=sample_result
        
        vaccine_case=VaccineCase(case_id=case_id,
        sample_result=sample_result,
        viral_level=viral_level,
        patient=patient,dosage_timeline='')
        vaccine_case.save()   
        
        attrs['vaccine_pk']=vaccine_case.pk

        return attrs

class AdministerVaccineSerializer(serializers.Serializer):
    pk=serializers.IntegerField()


    def validate(self, attrs):
        super().validate(attrs)
        return 