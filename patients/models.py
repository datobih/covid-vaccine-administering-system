from django.db import models

# Create your models here.

patient_status_choices=[('Healthy','Healthy'),
    ('Infected','Infected'),
]
gender_choices=[('M','M'),('F','F')]

class Patient(models.Model):
    fullname=models.CharField(max_length=50,unique=True)
    gender=models.CharField(max_length=2,choices=gender_choices)
    age=models.IntegerField()
    health_status=models.CharField(choices=patient_status_choices,max_length=15,default='Infected')

    def __str__(self) -> str:
        return self.fullname



class VaccineCase(models.Model):
    case_id=models.CharField(max_length=100)
    sample_result=models.IntegerField()
    viral_level=models.IntegerField()
    test_type=models.CharField(default='Oropharyngeal',max_length=50)
    test_date=models.DateTimeField(auto_now_add=True)
    dosage_timeline=models.CharField(max_length=200)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='vaccine_cases')

    def __str__(self):
        return self.case_id
