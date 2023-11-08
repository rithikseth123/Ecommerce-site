from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.CartView.as_view(), name="cart-item"),
    path("add", views.add_to_cart, name="add-to-cart"),
    path("remove", views.remove_from_cart, name="remove-from-cart"),
]
