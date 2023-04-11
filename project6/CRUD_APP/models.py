from django.db import models


class Student(models.Model):
    sid = models.IntegerField()
    fname = models.CharField(max_length=80)
    dob = models.DateField()
    mail = models.EmailField()
    city = models.CharField(max_length=25)

# Create your models here.
