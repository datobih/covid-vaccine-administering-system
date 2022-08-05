from django.db import models

# Create your models here.
class Patient(models.Model):
    fullname=models.CharField(max_length=50)
    age=models.IntegerField()
    health_status=models.CharField()


class VaccineCase(models.Model):
    sample_result=models.IntegerField()
    viral_level=models.IntegerField()
    test_type=models.CharField(default='Oropharyngeal')
    test_date=models.DateTimeField(auto_now_add=True)
    dosage_timeline=models.CharField(max_length=200)
