from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    birthday=models.DateField()

    def __str__(self):
        return self.name
