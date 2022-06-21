from django.db import models

class Members(models.Model):
    firstname=models.CharField(max_length=25)
    lastname=models.CharField(max_length=25)