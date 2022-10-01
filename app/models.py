from django.db import models

# Create your models here.
class Link(models.Model):
    url = models.CharField(max_length=1000)
    short_url = models.CharField(max_length=30,blank=True,null=True)