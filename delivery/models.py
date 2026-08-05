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
    max_length=500,
    blank=True,
    default="https://images.pexels.com/photos/262978/pexels-photo-262978.jpeg"
)

    
class Menu(models.Model):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="menus"
    )
    item_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    image = models.URLField(blank=True)

    def __str__(self):
        return f"{self.item_name} - {self.restaurant.restaurant_name}"


class Cart(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )

    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(default=1)

    added_at = models.DateTimeField(auto_now_add=True)

    def total(self):
        return self.quantity * self.menu.price

    def __str__(self):
        return f"{self.customer.username} - {self.menu.item_name}"


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def total(self):
        return self.quantity * self.price