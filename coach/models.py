from django.db import models

# Create your models here.
class Coach(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    theme = models.CharField(max_length=100)
    date = models.DateField()
