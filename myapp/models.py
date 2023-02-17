from django.db import models

# Create your models here.
class Introduction(models.Model):
    intro= models.CharField(max_length=200)
    