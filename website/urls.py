from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="main-page"),
    path("all-product/", views.AllProductView.as_view(), name="all-product"),
    path("recent-product/", views.RecentProductView.as_view(), name="recent-product"),
    path("add-product/", views.AddProductView.as_view(), name="add-product"),
    path("add-product/thank-you/", views.ThankYouView.as_view(), name="thank-you"),
    path("category/", views.CategoryView.as_view(), name="category"),
    path(
        "product/<slug:slug>/", views.SingleProductView.as_view(), name="single-product"
    ),
    path(
        "category/<slug:slug>/",
        views.CategoryDetailView.as_view(),
        name="sort-category",
    )
]
