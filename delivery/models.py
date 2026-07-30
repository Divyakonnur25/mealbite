from django.db import models

# Create your models here.
class Customer(models.Model):
    
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=10)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.username
