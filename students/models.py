from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.CharField(primary_key=True, max_length=8)
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} {self.lastname}'
