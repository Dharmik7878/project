from django.db import models

class ProductDetail(models.Model):
    id = models.AutoField(primary_key=True)
    productname = models.CharField(max_length=20)
    tracknumber = models.CharField(max_length=9)
    status = models.CharField(max_length=10)
    origin = models.CharField(max_length=10)
    destination = models.CharField(max_length=10)
    estimatedlv = models.DateField()
    dateshiped = models.DateField()