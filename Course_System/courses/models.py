from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=20, unique=True)
    discription = models.TextField(max_length=100)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    
