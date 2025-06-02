from django.db import models

class ExportProduct(models.Model):
    eximg=models.URLField(max_length=500)
    extitle=models.CharField(max_length=20)
    exdesc=models.TextField(max_length=200)

# Create your models here.