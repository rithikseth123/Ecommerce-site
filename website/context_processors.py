from django.shortcuts import render, redirect
from cart.models import Cart, CartItem


def custom_context(request):
    if request.user.id is not None:
        user_cart = Cart.objects.filter(user=request.user.id)
        if len(user_cart) != 0:
            user_cart_items = CartItem.objects.filter(cart=user_cart[0].id)
        else:
            user_cart_items = []
    else:
        user_cart_items = []
    return {"user_cart_items": len(user_cart_items)}
