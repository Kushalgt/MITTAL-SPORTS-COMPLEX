from django.db import models

class Contact(models.Model):
    email=models.CharField(max_length=122)
    password=models.CharField(max_length=122)
    username=models.CharField(max_length=122)
    slotsbooked=models.CharField(max_length=122)
    #date=models.DateField()

