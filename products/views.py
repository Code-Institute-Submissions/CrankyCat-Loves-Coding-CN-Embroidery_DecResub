"""product page view"""
from django.shortcuts import render
from .models import Product

# Create your views here.


def all_products(request):
    """A view to return the product page
    including sorting and searching queries
    """

    products = Product.objects.all()
    # get all objects from Product model and return context

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
