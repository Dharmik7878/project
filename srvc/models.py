from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUaserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("The Username must be set")
        user = self.model(username=username)
        user.set_password(password)
        user.save(useing = self._db)
        return user

class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    def crate_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.crate_user(username, password, **extra_fields)
    
    objects = CustomUaserManager()

    USERNAME = FIELD="username"
    REQUIRED_FIELDS=['email']

    def _str_(self):
        return self.username
    
class register(models.Model):
    rname=models.CharField(max_length=50)
    runame=models.CharField(max_length=50)
    remail=models.EmailField(max_length=50)
    rmobile=models.CharField(max_length=10)
    rcrtpass=models.CharField(max_length=10)
    rconpass=models.CharField(max_length=10)

class contact(models.Model):
    cname=models.CharField(max_length=50)
    cemail=models.EmailField(max_length=80)
    csub=models.TextField(max_length=100)
    cmsg=models.TextField(max_length=200)

class FeedBack(models.Model):
    fbname=models.CharField(max_length=50)
    fbemail=models.EmailField(max_length=80)
    fbnum=models.CharField(max_length=10)
    fbsrv=models.CharField(max_length=200)
    fbmsg=models.TextField(max_length=200)

class ExportForm(models.Model):
    id = models.AutoField(primary_key=True)
    CustomerName=models.CharField(max_length=30)
    Email=models.EmailField(max_length=100)
    contact=models.CharField(max_length=10)
    Product=models.CharField(max_length=50)
    Quantity=models.CharField(max_length=10)
    Country=models.CharField(max_length=10)
    Shipping=models.TextField(max_length=200)
    Payment=models.CharField(max_length=3)

class ImportForm(models.Model):
    id = models.AutoField(primary_key=True)
    CustomerName=models.CharField(max_length=30)
    Email=models.EmailField(max_length=100)
    contact=models.CharField(max_length=10)
    Product=models.CharField(max_length=50)
    Quantity=models.CharField(max_length=10)
    St=models.CharField(max_length=10)
    Shipping=models.TextField(max_length=200)
    Payment=models.CharField(max_length=3)


# Create your models here.