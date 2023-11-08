from django.urls import path
from . import views

urlpatterns = [
    path("", views.OrderView.as_view(), name="order"),
    path("order/", views.OrderListView.as_view(), name="order-list"),
]
