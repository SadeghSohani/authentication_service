from statistics import mode
from django.db import models

class Users(models.Model) :
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)

class UserPanel(models.Model) :
    username = models.CharField(max_length=200)
    flight_id = models.IntegerField()
