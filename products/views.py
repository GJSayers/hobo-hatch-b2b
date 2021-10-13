from django.shortcuts import render
from .models import Product, ProductCategory, ProductType


def collections(request):
    """
    A view to show all products / product collections
    """

    products = Product.objects.all()
    categories = ProductCategory()
    product_type = ProductType()

    context = {
        'products': products,
        'categories': categories,
        'product_type': product_type,
    }
    return render(request, 'products/collections.html', context)
