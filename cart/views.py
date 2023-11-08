from django.shortcuts import render, redirect
from cart.models import Cart, CartItem
from website.models import Product
from django.views.generic import ListView, View, DetailView


# Create your views here.
def add_to_cart(request):
    if request.method == "POST":
        print("-----------")
        product_id = request.POST.get("product_id")
        user_cart = Cart.objects.filter(user=request.user.id)
        print(user_cart)
        if len(user_cart) == 0:
            Cart.objects.create(user=request.user)
        user_cart = Cart.objects.get(user=request.user)
        user_cart_items = CartItem.objects.filter(cart=user_cart, product=product_id)
        if len(user_cart_items) == 0:
            CartItem.objects.create(
                cart=user_cart, product=Product.objects.get(pk=product_id)
            )
        else:
            user_cart_items = CartItem.objects.get(
                cart=user_cart, product=Product.objects.get(pk=product_id)
            )
            user_cart_items.quantity += 1
            user_cart_items.save()

    return redirect("cart-item")


def remove_from_cart(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        user_cart = Cart.objects.get(user=request.user)

        # Check if the item is already in the cart
        user_cart_item = CartItem.objects.filter(
            cart=user_cart, product=product_id
        ).first()

        if user_cart_item:
            # If the item is in the cart, decrease its quantity
            if user_cart_item.quantity > 1:
                user_cart_item.quantity -= 1
                user_cart_item.save()
            else:
                # If the quantity is 1, remove the item from the cart
                user_cart_item.delete()

    return redirect("cart-item")


class CartView(View):
    def get(self, request):
        print("---------------")
        if request.user.is_authenticated:
            try:
                cart = Cart.objects.get(user=request.user)

                if request.user.id is not None:
                    user_cart = Cart.objects.filter(user=request.user.id)
                    print(user_cart)
                if len(user_cart) != 0:
                    total = 0
                    user_cart_items = CartItem.objects.filter(cart=user_cart[0].id)
                    print(user_cart_items)
                    for i in user_cart_items:
                        i.total = i.quantity * i.product.cost
                        total = i.total + total
                    print(total)
                else:
                    user_cart_items = []

                return render(
                    request,
                    "cart/cart_product.html",
                    {
                        "cart_items": user_cart_items,
                        "total_cart_items": len(user_cart_items),
                        "total": total,
                    },
                )
            except Cart.DoesNotExist:
                print("User doesn't have a cart")
                return render(request, "cart/cart_product.html", {"products": []})
        else:
            return render(request, "cart/cart_product.html", {"products": []})
