from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name

class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.email


