from django.shortcuts import render, redirect
from django.views.generic import View, ListView
from .models import Order, OrderItems
from cart.models import Cart, CartItem
from django.urls import reverse_lazy

# Create your views here.


class OrderView(View):
    def post(self, request):
        total_price = request.POST.get("total_price")
        user_cart = Cart.objects.get(user=request.user)
        user_cart_items = CartItem.objects.filter(cart=user_cart)
        new_order = Order.objects.create(user=request.user, total_price=total_price)
        for user_cart_item in user_cart_items:
            OrderItems.objects.create(
                order=new_order,
                product=user_cart_item.product,
                quantity=user_cart_item.quantity,
            )

        user_cart.delete()
        return render(request, "order/success.html", {"order": new_order})


class OrderListView(ListView):
    template_name = "order/order_list.html"
    model = Order
    context_object_name = "order_list"
