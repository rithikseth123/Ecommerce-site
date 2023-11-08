from django.db import models
from django.contrib.auth.models import User
from website.models import Product

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"


class OrderItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in {self.order}"
