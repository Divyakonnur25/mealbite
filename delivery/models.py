from django.db import models

# Create your models here.
class Customer(models.Model):
    
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=10)
    address = models.CharField(max_length=100)



class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    cuisine = models.CharField(max_length=100)

    opening_time = models.TimeField()
    closing_time = models.TimeField()

    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=0.0
    )

    image = models.URLField(
    blank=True,
    default="https://images.pexels.com/photos/262978/pexels-photo-262978.jpeg"
)