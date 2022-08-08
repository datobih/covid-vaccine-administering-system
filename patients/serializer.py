from rest_framework import serializers
from .models import Patient,VaccineCase
import random
from datetime import datetime
import json

class AddPatientSerializer(serializers.Serializer):
    first_name=serializers.CharField(max_length=50)
    last_name=serializers.CharField(max_length=50)
    gender=serializers.CharField(max_length=1)
    age=serializers.CharField(max_length=3)
    genotype=serializers.CharField()
    email=serializers.EmailField()
    blood_group=serializers.CharField()
    phone_number=serializers.CharField(max_length=11)
    
    def validate(self, attrs):
        super().validate(attrs)
        
        patient=Patient.objects.create(
        first_name=attrs['first_name'],
        last_name=attrs['last_name'],
        gender=attrs['gender'],
        age=attrs['age'],
        genotype=attrs['genotype'],
        email=attrs['email'],
        phone_number=attrs['phone_number'],
        blood_group=attrs['blood_group']
        )
        attrs['pk']=patient.pk
        attrs['status']=200
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

    def is_dosage_valid(current_timestamp,recent_timestamp):
        time_difference=current_timestamp-recent_timestamp
        if(time_difference<592200):
            return False
        return True

    def validate(self, attrs):
        super().validate(attrs)
        current_time=datetime.now()
        vaccine_case=VaccineCase.objects.get(pk=attrs['pk'])
        if(not vaccine_case):
             raise serializers.ValidationError('Invalid vaccine case primary key')
        dosage_timeline=json.loads(vaccine_case.dosage_timeline)
        timeline=dosage_timeline['timeline']
        if(len(timeline)!=0):
            recent_timestamp=timeline[len(timeline)-1]
            current_timestamp=current_time.timestamp()

            if(not self.is_dosage_valid(current_timestamp,recent_timestamp)):
                raise serializers.ValidationError(
                'Inelligible to take a dose at the moment')
        
        

        viral_level=vaccine_case.viral_level
        if(viral_level<20):
            viral_level-=0
        elif(viral_level==0):
            raise serializers.ValidationError()

        else:
            viral_level-=20
            viral_level=self.round_up_even(viral_level)
        
        vaccine_case.viral_level=viral_level
        vaccine_case.dosage_timeline
        current_time=datetime.now()

        dosage_timeline['timeline'].append(current_time.timestamp())

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