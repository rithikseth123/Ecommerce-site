from django.contrib import admin

# Register your models here.
from .models import Cart, CartItem


class CartItemAdmin(admin.ModelAdmin):
    list_display = ["cart", "product", "quantity"]


admin.site.register(Cart)
admin.site.register(CartItem, CartItemAdmin)
