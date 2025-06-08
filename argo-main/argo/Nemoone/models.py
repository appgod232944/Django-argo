from django.db import models

class Kar(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
