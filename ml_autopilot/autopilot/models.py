from django.db import models

# Create your models here.


class File(models.Model):
    file = models.FileField(upload_to="files")


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(
        max_length=1, choices=(("M", "Male"), ("F", "Female"), ("O", "Other"))
    )
    ip_address = models.GenericIPAddressField()
    address = models.TextField()
