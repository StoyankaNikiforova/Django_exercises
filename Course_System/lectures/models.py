from django.db import models
from courses.models import Course


class Lecture(models.Model):
    name = models.CharField(max_length=20)
    week = models.CharField(max_length=20)
    course = models.ForeignKey(Course)
    url = models.URLField(max_length=1000)
