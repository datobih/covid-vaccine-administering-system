from django.db import models

# Create your models here.

patient_status_choices=[('Healthy','Healthy'),
    ('Infected','Infected'),
]
gender_choices=[('Male','Male'),('Female','Female')]
genotype_choices=[('AA','AA'),('AS','AS'),('SS','SS')]

class Patient(models.Model):
    fullname=models.CharField(max_length=50,unique=True)
    gender=models.CharField(max_length=6,choices=gender_choices)
    age=models.IntegerField()
    genotype=models.CharField(choices=genotype_choices,max_length=2,default='')
    email=models.EmailField(default='')
    blood_group=models.CharField(max_length=2,null=True,blank=True,default=None)
    phone_number=models.CharField(max_length=11,default='')

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
