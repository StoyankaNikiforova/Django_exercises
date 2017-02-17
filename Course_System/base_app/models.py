from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    @classmethod
    def exists(cls, email):
        emails = User.objects.email.all()
        if email in emails:
            return False
        return True   


class Teacher(User):
    title = models.CharField(max_length=90)
    is_teacher = True


class Student(User):
    is_teacher = False
