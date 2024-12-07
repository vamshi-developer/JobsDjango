from django.db import models

# Create your models here.
class HydJobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=250)
    title=models.CharField(max_length=250)
    eligibility=models.CharField(max_length=250)
    address=models.CharField(max_length=250)
    email=models.EmailField()
    phonenumber=models.BigIntegerField()
