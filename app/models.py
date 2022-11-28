from django.db import models
from os import killpg

class Customer(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    loggedin = models.BooleanField(editable=False, default=True)