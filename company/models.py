from django.db import models



class Company(models.Model):
    name=models.CharField(max_length=50)
    type=models.CharField(max_length=50)
    payment_type=models.CharField(max_length=50)
    
