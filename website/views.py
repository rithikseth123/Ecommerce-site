from django.shortcuts import render

from django.views.generic import View, CreateView, DetailView, TemplateView
from .models import Product, Category
from cart.models import Cart, CartItem
from .forms import ProductForm
import random

# Create your views here.


class IndexView(View):
    def get(self, request):
        # products=Product.objects.all().order_by("cost")[:4]
        products = list(Product.objects.all())
        random.shuffle(products)
        products = products[:4:]
        all_category = Category.objects.all()
        if request.user.id is not None:
            user_cart = Cart.objects.filter(user=request.user.id)
            if len(user_cart) != 0:
                user_cart_items = CartItem.objects.filter(cart=user_cart[0].id)
            else:
                user_cart_items = []
        else:
            user_cart_items = []
        return render(
            request,
            "website/index.html",
            {
                "products": products,
                "all_category": all_category,
                "total_cart_items": len(user_cart_items),
            },
        )


class AllProductView(View):
    def get(self, request):
        # products=Product.objects.all().order_by("cost")
        products = list(Product.objects.all())
        random.shuffle(products)
        return render(request, "website/all_product.html", {"products": products})


class RecentProductView(View):
    def get(self, request):
        products = Product.objects.all().order_by("-id")[:4]
        return render(request, "website/recent_product.html", {"products": products})


class AddProductView(CreateView):
    model = Product
    template_name = "website/add_product.html"
    # fields="__all__"
    form_class = ProductForm
    success_url = "thank-you"


class ThankYouView(TemplateView):
    template_name = "website/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "ThankYou For Adding Product!!"
        return context


class CategoryView(View):
    def get(self, request):
        all_category = Category.objects.all()
        return render(
            request, "website/all_category.html", {"all_category": all_category}
        )


class SingleProductView(DetailView):
    template_name = "website/product_detail.html"
    model = Product


class CategoryDetailView(View):
    def get(self, request, slug):
        sorted_category = Product.objects.filter(category__slug=slug)
        # print(sorted_category)
        return render(
            request,
            "website/filter_by_category.html",
            {"sorted_category": sorted_category},
        )


