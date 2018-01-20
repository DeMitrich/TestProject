# Create your models here.
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __repr__(self):
        return  self.name + ' ' + self.last_name

