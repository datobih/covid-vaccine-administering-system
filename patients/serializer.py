from rest_framework import serializers
from .models import Patient,VaccineCase
import random
import datetime
import json

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
        
        dosage_timeline={'timeline':[]}
        vaccine_case=VaccineCase(case_id=case_id,
        sample_result=sample_result,
        viral_level=viral_level,
        patient=patient,dosage_timeline=json.dumps(dosage_timeline))
        vaccine_case.save()   
        
        attrs['vaccine_pk']=vaccine_case.pk

        return attrs

class AdministerVaccineSerializer(serializers.Serializer):
    pk=serializers.IntegerField()

    def round_up_even(num):
        return num+(num%10)

    def validate(self, attrs):
        super().validate(attrs)

        vaccine_case=VaccineCase.objects.get(pk=attrs['pk'])
        if(not vaccine_case):
             raise serializers.ValidationError('Invalid vaccine case primary key')
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
        dosage_timeline=json.loads(vaccine_case.dosage_timeline)
        dosage_timeline['timeline'].append(current_time)

        #Convert dosage_timeline to string
        vaccine_case.dosage_timeline=json.dumps(dosage_timeline)
        times_more=viral_level/20
        vaccine_case.save()

        attrs['times_more']=times_more
        return attrs


class VaccineCaseSerializer(serializers.ModelSerializer):


    class Meta:
        model=VaccineCase
        fields=['case_id','sample_result',
        'viral_level','test_type','test_date',
        'dosage_timeline']

class PatientSerializer(serializers.ModelSerializer):
    vaccine_cases=serializers.ListSerializer(child=VaccineCaseSerializer(),
    allow_empty=True)

    class Meta:
        model=Patient
        fields=['fullname','gender',
        'age','health_status','vaccine_cases']