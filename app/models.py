from django.db import models

# Create your models here.
from django.core import validators
class Student(models.Model):
    sid=models.IntegerField()
    sname=models.CharField(max_length=100,validators=[validators.MinLengthValidator(5)])
    
    sage=models.IntegerField()
    smobile=models.CharField(max_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])

    def __str__(self):
        return self.sname