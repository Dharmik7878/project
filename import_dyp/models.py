from django.db import models

class hardware(models.Model):
    imimg=models.URLField(max_length=100)
    imtitle=models.CharField(max_length=50)
    imdtl=models.TextField(max_length=500)

class crudoil(models.Model):
    imimg=models.URLField(max_length=100)
    imtitle=models.CharField(max_length=50)
    imdtl=models.TextField(max_length=500)

class motor(models.Model):
    imimg=models.URLField(max_length=100)
    imtitle=models.CharField(max_length=50)
    imdtl=models.TextField(max_length=500)

class motorspl(models.Model):
    imimg=models.URLField(max_length=100)
    imtitle=models.CharField(max_length=50)
    imdtl=models.TextField(max_length=500)

class mechanical(models.Model):
    imimg=models.URLField(max_length=100)
    imtitle=models.CharField(max_length=50)
    imdtl=models.TextField(max_length=500)
# Create your models here.